"""Single-command replay of the Theorem L exact certificates (review/LOCAL_THEOREM.md).

Run from the lane root:  ../depolarizing/env/bin/python -B code/replay_theorem_L.py
1. checks SHA-256 of the pinned inputs listed in evidence/theorem_L_manifest.json;
2. copies them into a fresh sandbox evidence/replay/theorem_L-<host time>/ and runs the certificate script there
   with this interpreter (needs sympy + python-flint), so the pinned output is never overwritten;
3. compares the regenerated output with the manifest's expected fields and with the pinned output
   (canonical SHA-256 without the wall-time key 'seconds');
4. writes <sandbox>/receipt.json and exits 0 iff every check passes.
"""
import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys
import time

LANE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical_sha(obj):
    obj = {k: v for k, v in obj.items() if k != "seconds"}
    s = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def main():
    with open(os.path.join(LANE, "evidence", "theorem_L_manifest.json")) as f:
        man = json.load(f)
    checks = {}
    for rel, want in man["inputs_sha256"].items():
        checks["input sha256 " + rel] = sha256_file(os.path.join(LANE, rel)) == want
    pinned_path = os.path.join(LANE, man["pinned_output"]["path"])
    checks["pinned output file sha256"] = sha256_file(pinned_path) == man["pinned_output"]["file_sha256"]
    with open(pinned_path) as f:
        pinned = json.load(f)
    checks["pinned output canonical sha256"] = canonical_sha(pinned) == man["pinned_output"]["canonical_sha256_without_seconds"]

    stamp = time.strftime("%Y%m%dT%H%M%S%z")
    box = os.path.join(LANE, "evidence", "replay", "theorem_L-" + stamp)
    os.makedirs(os.path.join(box, "code"))
    os.makedirs(os.path.join(box, "evidence"))
    for rel in man["inputs_sha256"]:
        shutil.copy2(os.path.join(LANE, rel), os.path.join(box, rel))
    env = dict(os.environ, OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1",
               VECLIB_MAXIMUM_THREADS="1", PYTHONHASHSEED="0")
    proc = subprocess.run([sys.executable, "-B", os.path.join(box, "code", "local_theorem_exact.py")],
                          cwd=os.path.join(box, "code"), env=env, capture_output=True, text=True)
    with open(os.path.join(box, "stdout.txt"), "w") as f:
        f.write(proc.stdout)
    with open(os.path.join(box, "stderr.txt"), "w") as f:
        f.write(proc.stderr)
    checks["certificate script exit code 0"] = proc.returncode == 0
    out_path = os.path.join(box, "evidence", "local_theorem_exact.json")
    regen = {}
    if os.path.exists(out_path):
        with open(out_path) as f:
            regen = json.load(f)
    for key, want in man["expected_fields"].items():
        checks["expected " + key] = regen.get(key) == want
    checks["regenerated == pinned (canonical, without 'seconds')"] = bool(regen) and canonical_sha(regen) == canonical_sha(pinned)
    try:
        import flint
        import sympy
        versions = {"sympy": sympy.__version__, "python-flint": flint.__version__}
    except ImportError as exc:  # pragma: no cover - reported in receipt
        versions = {"import_error": str(exc)}
    receipt = {
        "host_time": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "python": platform.python_version(),
        "interpreter": sys.executable,
        "versions": versions,
        "sandbox": os.path.relpath(box, LANE),
        "regenerated_output_file_sha256": sha256_file(out_path) if os.path.exists(out_path) else None,
        "regenerated_canonical_sha256": canonical_sha(regen) if regen else None,
        "seconds": regen.get("seconds"),
        "checks": checks,
        "all_ok": all(checks.values()),
    }
    with open(os.path.join(box, "receipt.json"), "w") as f:
        json.dump(receipt, f, indent=1)
    print(json.dumps(receipt, indent=1))
    sys.exit(0 if receipt["all_ok"] else 1)


if __name__ == "__main__":
    main()
