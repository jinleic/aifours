#!/usr/bin/env python3
"""Parent replay of LOWER48's 37 load-bearing final UNSATs and 137 phase certificates.

No solver or worker LRAT checker is trusted. Regenerate exact CNFs, feed them
through a FIFO to the pinned parent's drat-trim, and independently verify the
addition-only RUP proof extracted from gzip LRAT. No large CNF/proof is stored.
Written officer-counting exclusions remove 94 non-load-bearing streams.
"""
import gzip
import hashlib
import importlib.util
import itertools
import json
import os
import subprocess
import sys
import threading
import time
from collections import Counter, defaultdict, deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
SNAP = HERE / "ame46-lower48-parent-inputs-v1"
OUT = HERE / "ame46-lower48-parent-replay-v1"
DT = HERE / "moqls7-parent-proofcheck-v1/drat-trim"
DT_SHA = "a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37"
CONVERTER = HERE / "lrat_gzip_additions_v1.py"
PAIRINGS = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))
sys.path.insert(0, str(SNAP / "code"))
import large_t_gen as base
import large_t_lex as lex


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def now():
    return subprocess.check_output(["date", "+%Y-%m-%d %H:%M:%S %Z"], text=True).strip()


def partitions(h, cap=6, count=6):
    if h == 0:
        yield ()
    elif count:
        for a in range(min(cap, h), 1, -1):
            for rest in partitions(h - a, a, count - 1):
                yield (a,) + rest


def canonical(prof):
    return tuple(sorted(tuple(p) for p in prof))


def profiles(h):
    parts = sorted(set(partitions(h)))
    return {canonical(p) for p in itertools.combinations_with_replacement(parts, 4)
            if all(max(p[i]) <= min(len(p[j]) for j in range(4) if j != i) for i in range(4))}


def written_exclusion(t, h, prof):
    sizes = list(map(len, prof))
    sigma1 = 6 * sum(sizes) - 4 * h
    sigma2 = sum(sizes[i] * sizes[j] for i in range(4) for j in range(i + 1, 4)) - 6 * h
    f = [sigma2 - a * sigma1 + a * (a + 1) // 2 * t for a in range(5)]
    binary = t == 28 and canonical(prof) == canonical(((4, 4), (2, 2, 2, 2), (2, 2, 2, 2), (2, 2, 2, 2)))
    return min(f) < 0 or binary, f, binary


def phase_certificate(N, cert):
    forms = Counter()
    weight = 0
    for entry in cert:
        w, k, points = entry["w"], entry["k"], entry["corners"]
        if type(w) is not int or w == 0 or k not in range(3) or len(points) != 4:
            raise ValueError("bad compact certificate entry")
        a, b, c, d = points
        if not all(x in N for x in points):
            raise ValueError("phase corner outside support")
        rp, cp = PAIRINGS[k]
        row = lambda x: tuple(x[i] for i in rp)
        col = lambda x: tuple(x[i] for i in cp)
        if not (row(a) == row(b) and row(c) == row(d) and row(a) != row(c) and
                col(a) == col(c) and col(b) == col(d) and col(a) != col(b)):
            raise ValueError("phase corners not a rectangle")
        R, C = defaultdict(set), defaultdict(set)
        for x in N:
            R[row(x)].add(col(x))
            C[col(x)].add(row(x))
        if any(len(R[row(x)]) != 2 or len(C[col(x)]) != 2 for x in points):
            raise ValueError("phase rectangle not a genuine component")
        for x, sign in ((a, 1), (b, -1), (c, -1), (d, 1)):
            forms[x] += w * sign
        weight += w
    if any(forms.values()) or weight % 2 != 1:
        raise ValueError("phase weighted form nonzero or weight sum even")
    return {"forms": len(cert), "weight_sum": weight, "verdict": "PASS"}


def check_rup(text, proof, label, folder):
    """Two CPU workers at most: CNF writer/checker, then converter/checker."""
    fifo = folder / (label + ".cnf.fifo")
    os.mkfifo(fifo)
    nv = int(text.split("\n", 1)[0].split()[2])
    writer_errors, statuses, tail = [], [], deque(maxlen=8)
    state = {"trip": None, "peak_rss_bytes": 0}
    children, stopped = [], threading.Event()
    start = time.monotonic()

    def writer():
        try:
            with fifo.open("wb") as f:
                f.write(text.encode())
        except OSError as e:
            writer_errors.append(str(e))

    def monitor():
        while not stopped.wait(1):
            ids = [os.getpid()] + [p.pid for p in list(children) if p.poll() is None]
            rss = subprocess.run(["ps", "-o", "rss=", "-p", ",".join(map(str, ids))], capture_output=True, text=True)
            total = sum(int(v) for v in rss.stdout.split() if v.isdigit()) * 1024
            state["peak_rss_bytes"] = max(state["peak_rss_bytes"], total)
            free = os.statvfs(folder)
            why = ("RSS cap" if total > 6 * 2**30 else
                   "free disk floor" if free.f_bavail * free.f_frsize < 12_000_000_000 else
                   "wall deadline" if time.monotonic() - start > 660 else None)
            if why and state["trip"] is None:
                state["trip"] = why
                for p in list(children):
                    if p.poll() is None:
                        p.terminate()

    with (folder / (label + ".converter.stderr")).open("xb") as err:
        producer = subprocess.Popen([sys.executable, "-B", str(CONVERTER), str(proof), str(nv)],
                                    stdout=subprocess.PIPE, stderr=err)
        children.append(producer)
        threading.Thread(target=writer, daemon=True).start()
        checker = subprocess.Popen([str(DT), str(fifo), "-I", "-U", "-t", "600"],
                                   stdin=producer.stdout, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        children.append(checker)
        producer.stdout.close()
        watcher = threading.Thread(target=monitor, daemon=True)
        watcher.start()
        output_hash = hashlib.sha256()
        for raw in checker.stdout:
            output_hash.update(raw)
            line = raw.decode(errors="replace").strip()
            tail.append(line)
            if line.startswith("s "):
                statuses.append(line)
        for p in children:
            try:
                p.wait(timeout=30)
            except subprocess.TimeoutExpired:
                state["trip"] = state["trip"] or "child did not exit"
                p.terminate()
                try:
                    p.wait(timeout=30)
                except subprocess.TimeoutExpired:
                    state["trip"] = "child survived SIGTERM; left running"
        stopped.set()
        watcher.join(timeout=2)
    passed = (state["trip"] is None and not writer_errors and
              checker.returncode == producer.returncode == 0 and statuses == ["s VERIFIED"])
    r = {"proof": str(proof), "cnf_sha256": hashlib.sha256(text.encode()).hexdigest(),
         "checker_rc": checker.returncode, "converter_rc": producer.returncode,
         "statuses": statuses, "writer_errors": writer_errors, "guard": state,
         "wall_seconds": time.monotonic() - start, "output_sha256": output_hash.hexdigest(),
         "tail": list(tail), "verified": passed}
    with (folder / (label + ".json")).open("x") as f:
        json.dump(r, f, indent=1)
        f.write("\n")
    return r


def main():
    OUT.mkdir(exist_ok=False)
    started = now()
    if sha(DT) != DT_SHA:
        raise ValueError("parent drat-trim changed")
    pins = json.loads((SNAP / "parent-pin-receipt.json").read_text())["files"]
    for rel, item in pins.items():
        if sha(SNAP / rel) != item["sha256"]:
            raise ValueError("input pin mismatch: " + rel)
    smoke = OUT / "smoke"
    smoke.mkdir(exist_ok=False)
    old = HERE / "ame46-lower46-parent-inputs-v1/conversion-smoke-v1"
    smoke_rows = []
    for p in sorted(old.glob("*.lrat")):
        gz = smoke / (p.name + ".gz")
        with gz.open("xb") as f:
            f.write(gzip.compress(p.read_bytes(), mtime=0))
        expected = p.name.startswith("unsat-")
        r = check_rup(p.with_suffix(".cnf").read_text(), gz, p.stem, smoke)
        smoke_rows.append({"case": p.stem, "expected_verified": expected, "ok": r["verified"] == expected})
    if len(smoke_rows) != 6 or not all(r["ok"] for r in smoke_rows):
        raise ValueError("gzip/RUP smoke failed")
    receipt = json.loads((SNAP / "evidence/v2_receipt_r2.json").read_text())
    proofs, phases, cases = [], [], []
    if {(c["t"], c["e"]) for c in receipt["cases"]} != {(26,0),(27,2),(28,2),(28,3),(29,3),(29,4),(30,4),(30,5)}:
        raise ValueError("wrong case list")
    for case in receipt["cases"]:
        report = json.loads((SNAP / case["report"]).read_text())
        t, e, h = case["t"], case["e"], 36 - case["t"]
        if report["outcome"] != "EXCLUDED" or report["guard_tripped"] is not None:
            raise ValueError("incomplete or resource-tripped report")
        actual = [canonical(p["profile"]) for p in report["profiles"]]
        if len(actual) != len(set(actual)) or set(actual) != profiles(h):
            raise ValueError("incomplete or duplicate deficit profiles")
        if len(case["profiles"]) != len(report["profiles"]):
            raise ValueError("receipt/report profile count mismatch")
        case_rows = []
        for po, pr in zip(case["profiles"], report["profiles"]):
            prof = pr["profile"]
            if po["profile"] != prof:
                raise ValueError("receipt/report profile order mismatch")
            written, alpha, binary = written_exclusion(t, h, prof)
            row = {"profile": prof, "written_exclusion": written, "alpha": alpha, "binary_exclusion": binary}
            case_rows.append(row)
            if written:
                continue
            S = base.SmallGen(prof)
            S.build_gen(e, h)
            for g in lex.generators(S):
                lex.add_lex_leader(S, g)
            if pr["status"] != "ENUMERATED" or len(pr["reps"]) != len(po["reasons"]):
                raise ValueError("incomplete representative list")
            blocks, seen = [], set()
            for k, (rep, reason) in enumerate(zip(pr["reps"], po["reasons"])):
                N = tuple(rep["N"])
                if (len(N) != 2*h+e or len(set(N)) != len(N) or frozenset(N) in seen or
                    any(len(x) != 4 or any(c not in "012345" for c in x) for x in N)):
                    raise ValueError("bad representative support")
                seen.add(frozenset(N))
                points = [tuple(map(int, x)) for x in N]
                if any(x not in S.var for x in points):
                    raise ValueError("point outside normal-form product")
                blocks.append([-S.var[x] for x in points])
                if reason["k"] != k or set(reason["N"]) != set(N) or reason["reason"] != "phase obstruction":
                    raise ValueError("load-bearing support lacks a bound phase certificate")
                cert = phase_certificate(set(N), reason["certificate_compact"])
                phases.append({"t": t, "e": e, "profile": prof, "index": k, **cert})
            text = lex.dimacs(S.nv, S.cl + blocks)
            if hashlib.sha256(text.encode()).hexdigest() != po["final"]["cnf_sha256"]:
                raise ValueError("regenerated final CNF differs")
            path = SNAP / po["final"]["proof"]
            r = check_rup(text, path, f"p{len(proofs):02d}", OUT)
            proofs.append({"t": t, "e": e, "profile": prof, **r})
            print(json.dumps({"proofs_done": len(proofs), "t": t, "e": e,
                              "verified": r["verified"], "wall_seconds": round(r["wall_seconds"], 2)}), flush=True)
            if not r["verified"]:
                raise ValueError("proof failed or resource/time limit reached; UNKNOWN")
        cases.append({"t": t, "e": e, "profiles": case_rows})
    passed = len(proofs) == 37 and len(phases) == 137 and all(r["verified"] for r in proofs)
    result = {"started_at_pt": started, "ended_at_pt": now(), "driver_sha256": sha(Path(__file__)),
              "converter_sha256": sha(CONVERTER), "drat_trim_sha256": sha(DT), "smoke": smoke_rows,
              "cases": cases, "proofs": proofs, "phases": phases,
              "load_bearing_final_proofs": len(proofs), "load_bearing_phase_certificates": len(phases),
              "verdict": "PASS" if passed else "FAIL",
              "scope": "37 load-bearing final CNFs regenerated and RUP-verified,137 phase certificates independently checked;94 redundant streams not rechecked; written lemmas and imported LOWER46/reviews remain separate"}
    with (OUT / "result.json").open("x") as f:
        json.dump(result, f, indent=1)
        f.write("\n")
    print(json.dumps({"verdict": result["verdict"], "proofs": len(proofs), "phase_certificates": len(phases)}))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
