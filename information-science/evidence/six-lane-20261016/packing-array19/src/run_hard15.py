#!/usr/bin/env python3
"""[Guard15 import variant; same frozen research/solver/helper/cap/predicate settings, per-stage effective disk threshold12,334,217,728B.]
[run_hard14.py = run_hard13.py with stream_check14: identical solve/check/caps and helper lifecycle, stronger per-stage free-space threshold 12.2e9 +64MiB metadata headroom; same STOP-hard12/STOP-m2r12 controls.]
[run_hard13.py = run_hard12.py with stream_check13 (helper lock, lane-RSS headroom check, per-helper RSS cap on the own
child). The placement list is written to ext.json.tmp-<pid>-<ns> and renamed to ext.json only after the helper exited
with rc 0; a successful run writes extend-receipt-<time>.json (helper peak RSS etc.); a failed helper (non-zero rc, RSS
cap) writes extend-failed-<time>.json, keeps the claim (the tag stays UNKNOWN; no retry loop) and the runner continues
with the next item; an admission refusal releases the claim and ends the runner. Stop files unchanged
(cycle2/STOP-hard12 / STOP-m2r12, as created by rss_watchdog4). FIFO prefixes v13*.]
[run_hard12.py = run_hard11.py with stream_check12 (admission re-check inside the bigmem lock before the checker spawn);
stop file cycle2/STOP-hard12; FIFO prefixes v12*; witness names *12_*; SAT candidates are preserved first and the
two verifiers run as registered helpers under a CPU token (handle_sat).]
[run_hard11.py = run_hard10.py on stream_check11 (revision 11): SIGTERM handler installed; stop file cycle2/STOP-hard11 and the
free-disk floor are re-checked after every token acquisition and before every construction/helper/solver/checker
admission (stream_check11.admitted_reason); a refused admission writes no record for the unrun case/batch,
releases the claim (archive/claims-released + archive/MANIFEST.tsv) and ends the runner; helpers run through
stream_check11.run_helper under a token; the token is never released while an owned child is alive.]
Runner revision 10 for the remaining M1 ms06 hard cases, staged token-gated pipeline
(stream_check10.kissat_staged: kissat 4.0.4 --seed=1 binary DRAT buffered zstd-1 in memory, then
drat-trim -i; one lane CPU token per pipeline covers CNF construction, solve and check).
  direct TAG...: encode_skel(spec) CNF (SHA compared with pass 1) -> cycle2/hard5/<tag>.json
                 (claims h5_<tag>, shared with run_hard8.py; a tag with an existing record is skipped)
  split TAG...:  one-column placements cycle2/part/<tag>/ext.json (extend_p1q m=1, created if missing)
                 in batches of BATCH -> cycle2/part/<tag>/batch_*.json + summary_batched.json
                 (claims pb9_<tag>, shared with run_hard9.py)
A SAT result writes the decoded array to cycle2/witness/, runs both verifiers and stops the runner.
Stop file cycle2/STOP-hard10 (checked before every case/batch; a released claim is moved to
archive/claims-released/ with a line in archive/MANIFEST.tsv); parent disk floor checked likewise.
Usage: run_hard10.py MODE LIMIT_S CHECK_BUDGET_S BATCH TAG [TAG ...]
"""
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_partbatch  # noqa: E402
import encode_skel  # noqa: E402
import stream_check15 as S  # noqa: E402

LANE = os.path.dirname(HERE)
C2 = os.path.join(LANE, "cycle2")
VENV_PY = os.path.expanduser("~/.local/state/research-explorer/venv/bin/python")
STOP = os.path.join(C2, "STOP-hard12")


def claim(name):
    d = os.path.join(C2, "claims")
    os.makedirs(d, exist_ok=True)
    try:
        fd = os.open(os.path.join(d, name + ".claim"), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        return False
    os.write(fd, ("%d %s run_hard14\n" % (os.getpid(), time.strftime("%Y-%m-%dT%H:%M:%S%z"))).encode())
    os.close(fd)
    return True


def release(name, why):
    src = os.path.join(C2, "claims", name + ".claim")
    rel = os.path.join(LANE, "archive", "claims-released")
    os.makedirs(rel, exist_ok=True)
    dst = os.path.join(rel, name + ".%s.claim" % time.strftime("%Y%m%dT%H%M%S"))
    if os.path.exists(dst):
        raise SystemExit("archive destination exists: " + dst)
    os.rename(src, dst)
    h = hashlib.sha256(open(dst, "rb").read()).hexdigest()
    with open(os.path.join(LANE, "archive", "MANIFEST.tsv"), "a") as f:
        f.write("%s\t%s\t%s\t%s\t%s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S%z"), os.path.relpath(src, LANE),
                                          os.path.relpath(dst, LANE), h, why))


def aborted_path():
    d = os.path.join(C2, "aborted")
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, "%s-%d-%d.json" % (os.path.basename(__file__)[:-3], os.getpid(), time.time_ns()))


def must_stop():
    if not os.path.exists(STOP) and not S.disk_free_ok():
        with open(STOP, "w") as f:
            f.write("%s disk floor: free %d < %d bytes\n" % (time.strftime("%Y-%m-%dT%H:%M:%S%z"), S.disk_free_bytes(),
                                                            S.DISK_FLOOR))
    return os.path.exists(STOP)


VERIFIERS = [[sys.executable, os.path.join(HERE, "verify_pa.py")], [os.path.join(LANE, "bin", "verify_pa2")]]


def handle_sat(name, res, X, spec):
    """SAT candidate handling (parent audit blocker 4): the raw solver output and the decoded array are written
    FIRST (preserved whatever happens next); then both verifiers run as registered helpers (run_helper:
    ACTIVE/SPAWNING lifecycle, SIGTERM forwarding) under a CPU token with the usual admission re-checks. A refused
    admission or an abort leaves the candidate preserved and marks the verification as deferred."""
    N, k, q = spec.get("N", 19), spec.get("k", 8), spec.get("q", 6)
    os.makedirs(os.path.join(C2, "witness"), exist_ok=True)
    rawp = os.path.join(C2, "witness", name + ".solver.txt")
    with open(rawp, "w") as f:
        f.write(res["solver_out"])
    vals = set()
    for line in res["solver_out"].splitlines():
        if line.startswith("v "):
            vals.update(int(t) for t in line.split()[1:] if t != "0")
    arr = [[([s for s in range(q) if X[r][c][s] in vals] + [-1])[0] for c in range(k)] for r in range(N)]
    p = os.path.join(C2, "witness", name + ".txt")
    with open(p, "w") as f:
        f.write("".join(" ".join(map(str, row)) + "\n" for row in arr))
    res.update({"model_file": os.path.relpath(p, LANE), "solver_output_file": os.path.relpath(rawp, LANE)})
    try:
        with S.Token(stage="verify") as tok:
            res["verify_token"] = tok.name
            for j, cmd in enumerate(VERIFIERS, 1):
                rc, out = S.run_helper(cmd + [p, str(N), str(k), str(q)])
                res["verify%d_rc" % j], res["verify%d" % j] = rc, out.strip()[-2000:]
    except S.AdmissionDenied as e:
        res["verification_deferred"] = "admission refused: %s" % e
    except SystemExit as e:
        res["verification_deferred"] = "abort: %r" % e
    if S.ABORT[0] and "verification_deferred" not in res:
        res["verification_deferred"] = "abort during verification"


def run_direct(tag, limit, budget):
    out = os.path.join(C2, "hard5", tag + ".json")
    if os.path.exists(out):
        return None
    spec = json.load(open(os.path.join(LANE, "cases19skel", "specs", tag + ".json")))
    p1 = json.load(open(os.path.join(LANE, "cases19skel", "results", tag + ".json")))
    hold = {}

    def build():
        F, X, _ = encode_skel.build(spec)
        hold["X"] = X
        return S.cnf_bytes_of(F)

    res = S.kissat_staged(build, os.path.join(LANE, "scratch", "fifo", "v15k_" + tag), limit, budget)
    if (res.get("admission_denied") or res.get("aborted_by_sigterm")) and res.get("status") != "SAT":
        S.write_json(aborted_path(), dict(res, solver_out=""))
        return {"stopped": True, "reason": res.get("admission_denied") or "sigterm"}
    res.update({"tag": tag, "mode": "directk-staged", "encoder": "encode_skel.py", "runner": "run_hard15.py",
                "cnf_matches_pass1_sha": res["cnf_sha256"] == p1["cnf_sha256"]})
    if res["status"] == "SAT":
        handle_sat("direct13_" + tag, res, hold["X"], spec)
    res["solver_out"] = ""
    os.makedirs(os.path.dirname(out), exist_ok=True)
    S.write_json(out, res)
    return res


def run_split(tag, limit, budget, bsize):
    d = os.path.join(C2, "part", tag)
    if os.path.exists(os.path.join(d, "summary.json")) or os.path.exists(os.path.join(d, "summary_batched.json")):
        return None
    os.makedirs(d, exist_ok=True)
    spec_path = os.path.join(LANE, "cases19skel", "specs", tag + ".json")
    ext = os.path.join(d, "ext.json")
    if not os.path.exists(ext):
        tmp = "%s.tmp-%d-%d" % (ext, os.getpid(), time.time_ns())
        with S.Token(stage="extend_p1q"):
            rc, out = S.run_helper([VENV_PY, os.path.join(HERE, "extend_p1q.py"), spec_path, tmp, "1"])
        info = dict(S.LAST_HELPER, out_tail=out[-300:], tmp=os.path.relpath(tmp, LANE))
        if rc != 0 or info.get("cap_hit") or not os.path.exists(tmp):  # an RSS-cap trip is a failure even with rc 0
            S.write_json(os.path.join(d, "extend-failed-%s.json" % time.strftime("%Y%m%dT%H%M%S")), info)
            return {"extend_failed": True, "tag": tag, "helper": info}
        os.rename(tmp, ext)
        S.write_json(os.path.join(d, "extend-receipt-%s.json" % time.strftime("%Y%m%dT%H%M%S")), info)
    E = json.load(open(ext))
    spec = json.load(open(spec_path))
    n = E["num_full"]
    st = {"single_checked": 0, "batches": 0, "batch_UNSAT_checked": 0, "batch_other": 0, "SAT": 0}
    for j in range(0, n, bsize):
        idx = list(range(j, min(n, j + bsize)))
        bp = os.path.join(d, "batch_%05d_%05d.json" % (idx[0], idx[-1]))
        if not os.path.exists(bp) and must_stop():
            return {"stopped": True}
        if os.path.exists(bp):
            r = json.load(open(bp))
        else:
            hold = {}

            def build():
                F, X, sel = encode_partbatch.build(spec, [E["full"][i] for i in idx])
                hold["X"] = X
                return S.cnf_bytes_of(F)

            r = S.kissat_staged(build, os.path.join(LANE, "scratch", "fifo", "v15pb_%s_%05d" % (tag, idx[0])), limit, budget)
            if (r.get("admission_denied") or r.get("aborted_by_sigterm")) and r.get("status") != "SAT":
                S.write_json(aborted_path(), dict(r, solver_out=""))
                return {"stopped": True, "reason": r.get("admission_denied") or "sigterm"}
            r.update({"tag": tag, "indices": idx, "encoder": "encode_partbatch.py", "runner": "run_hard15.py"})
            if r["status"] == "SAT":
                handle_sat("partbatch13_%s_%05d" % (tag, idx[0]), r, hold["X"], spec)
            r["solver_out"] = ""
            S.write_json(bp, r)
        st["batches"] += 1
        if r["status"] == "UNSAT" and r["checked"]:
            st["batch_UNSAT_checked"] += len(idx)
        elif r["status"] == "SAT":
            st["SAT"] += 1
            break
        else:
            st["batch_other"] += len(idx)
    res = {"tag": tag, "num_sub": n, **st, "runner": "run_hard15.py"}
    res["decided_unsat"] = st["batch_UNSAT_checked"] == n and st["SAT"] == 0
    S.write_json(os.path.join(d, "summary_batched.json"), res)
    return res


def main():
    S.install_sigterm_handler()
    S.set_stop_files([STOP])
    mode, limit, budget, bsize = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
    for tag in sys.argv[5:]:
        if S.ABORT[0]:
            print(time.strftime("%H:%M:%S"), "ABORT -- stopping", flush=True)
            return
        if must_stop():
            print(time.strftime("%H:%M:%S"), "STOP -- stopping", flush=True)
            return
        cn = ("h5_" if mode == "direct" else "pb9_") + tag
        if not claim(cn):
            continue
        try:
            r = run_direct(tag, limit, budget) if mode == "direct" else run_split(tag, limit, budget, bsize)
        except (S.AdmissionDenied, SystemExit) as e:
            r = {"stopped": True, "reason": repr(e)}
        if r is None:
            continue
        if r.get("extend_failed"):
            print(time.strftime("%H:%M:%S"), "extend failed (claim kept, item UNKNOWN):", json.dumps(r)[:400], flush=True)
            continue
        if r.get("stopped"):
            release(cn, "run_hard13 stop: claim released (stop/abort/admission refused)")
            print(time.strftime("%H:%M:%S"), "stopped inside", cn, "-- claim released", flush=True)
            return
        keep = ("tag", "status", "checked", "solve_seconds", "check_seconds", "drat_bytes", "token", "token_wait_seconds",
                "drat_trim_peak_rss_kb", "num_sub", "batches", "batch_UNSAT_checked", "batch_other", "SAT", "decided_unsat")
        print(time.strftime("%H:%M:%S"), json.dumps({k: r.get(k) for k in keep if k in r}), flush=True)
        if r.get("status") == "SAT" or r.get("SAT"):
            print("SAT FOUND -- stopping this runner", flush=True)
            return


if __name__ == "__main__":
    main()
