#!/usr/bin/env python3
"""Parent runner for the prompt-only Claude-authored CFR/DM checker (cfr27-claude-verifier-v1).
Runs checker.py on the 4 pinned positives (python3 -B and python3 -O -B), the 43 parent control fixtures
(expected verdicts from their parent JSON records), and argument controls. Native RLIMIT_CPU only; no timeouts/kills."""
import hashlib, json, os, resource, subprocess, sys, time
HERE = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/cfr27-claude-verifier-v1"
REV = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review"
PY = "/usr/bin/python3"
CHECKER = HERE + "/checker.py"
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()
def lim():
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
def run(flags, kind, rows, n, path, expsha):
    argv = [PY, *flags, CHECKER, kind, str(rows), str(n), path, expsha]
    t = time.time()
    p = subprocess.run(argv, capture_output=True, text=True, preexec_fn=lim)
    out = p.stdout.strip()
    try:
        obj = json.loads(out); parsed = True
    except Exception:
        obj = None; parsed = False
    return {"argv": argv[1:], "exit": p.returncode, "parsed_one_json": parsed and out.count("\n") == 0 or parsed,
            "stdout": out[:2000], "stderr": p.stderr[-2000:], "wall_s": round(time.time() - t, 3), "json": obj}
checker_sha = sha(CHECKER)
assert checker_sha == "49628fd83e9af84516e18f4ac89c5fc5410e5ecb31e07687a64f695920d5901e", checker_sha
man = json.load(open(REV + "/cfr27-parent-inputs-v1/manifest.json"))
pos = {"A-CFR": ("cfr", 5), "A-DM": ("dm", 6), "B-CFR": ("cfr", 5), "B-DM": ("dm", 6)}
cases = []
for flags in ([" -B"[1:]], ["-O", "-B"]):
    for name, (kind, rows) in pos.items():
        path = REV + "/cfr27-parent-inputs-v1/" + name + ".raw"
        r = run(flags, kind, rows, 27, path, sha(path))
        r.update(case=name, expect_accept=True, ok=(r["exit"] == 0))
        cases.append(r)
ctl = REV + "/cfr27-parent-controls-v1"
for fn in sorted(os.listdir(ctl)):
    if not fn.endswith(".raw"):
        continue
    meta = json.load(open(ctl + "/" + fn[:-4] + ".json"))
    expect_accept = meta["status"] == "PASS"
    path = ctl + "/" + fn
    assert sha(path) == meta["fixture_sha256"]
    r = run(["-B"], meta["kind"], meta["expected_rows"], meta["expected_n"], path, meta["expected_sha256"])
    r.update(case=meta["case"], expect_accept=expect_accept, parent_category=meta.get("actual_category"),
             ok=(r["exit"] == 0) if expect_accept else (r["exit"] == 1))
    cases.append(r)
A = REV + "/cfr27-parent-inputs-v1/A-CFR.raw"; Ad = REV + "/cfr27-parent-inputs-v1/A-DM.raw"
for label, args in [("wrong-sha", ("cfr", 5, 27, A, "0" * 64)), ("wrong-rows-4", ("cfr", 4, 27, A, sha(A))),
                    ("wrong-n-25", ("cfr", 5, 25, A, sha(A))), ("kind-swap-dm-on-cfr", ("dm", 5, 27, A, sha(A))),
                    ("kind-swap-cfr-on-dm", ("cfr", 6, 27, Ad, sha(Ad))), ("uppercase-sha", ("cfr", 5, 27, A, sha(A).upper())),
                    ("missing-file", ("cfr", 5, 27, HERE + "/does-not-exist.raw", "0" * 64))]:
    r = run(["-B"], *args)
    r.update(case=label, expect_accept=False, ok=(r["exit"] in (1, 2)))
    cases.append(r)
res = {"checker_sha256": checker_sha, "python": subprocess.run([PY, "--version"], capture_output=True, text=True).stdout.strip(),
       "n_cases": len(cases), "n_ok": sum(c["ok"] for c in cases),
       "accepts": sum(c["exit"] == 0 for c in cases), "rejects": sum(c["exit"] != 0 for c in cases),
       "all_one_json": all(c["json"] is not None for c in cases), "cases": cases,
       "finished": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
with open(HERE + "/result.json", "x") as f:
    json.dump(res, f, indent=1)
print(json.dumps({k: v for k, v in res.items() if k != "cases"}))
print([ (c["case"], c["exit"]) for c in cases if not c["ok"]])
