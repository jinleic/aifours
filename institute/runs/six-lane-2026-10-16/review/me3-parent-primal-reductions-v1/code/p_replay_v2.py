"""ME3 parent desk (ME3ParentPrimal): full replay of the primal chart P leaf record with the parent evaluator (v2).

Usage: p_replay_v2.py RUN_DIR SPEC SPEC_SHA LEAVES LEAVES_SHA PRIMAL PRIMAL_SHA LIMIT EXTRA_DEPTH STOP_EPOCH
  LIMIT = 0 replays every leaf (else only the first LIMIT leaves: a SAMPLE, never an acceptance run).
  EXTRA_DEPTH = maximal recorded extra bisection depth used only when a leaf's claimed outcome is not certified
  directly by the parent evaluator. v2 change vs v1 (v1 kept only the first 2000 such records): EVERY such leaf is
  written to RUN_DIR/subdivisions.txt.gz as
  "<line> <cell> <path|-> <OUTCOME> <subdiv_ok 0/1> <n_subboxes_certified> <deepest> <direct-failure diagnostics>".
Reads LEAVES in place (gzip stream, never copied); hashes it before and after. Writes only RUN_DIR/RESULT.json and
RUN_DIR/subdivisions.txt.gz (exclusive create). In-process guards: free bytes on / >= 12e9, max RSS <= 1.4 GiB,
host clock < STOP_EPOCH; any guard trip ends the run with status UNKNOWN (never a pass).
"""
import sys
import os
import re
import json
import gzip
import time
import hashlib
import resource
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import p_core_v1 as C  # noqa: E402

FLOOR = 12_000_000_000
RSS_CAP = int(1.4 * 2**30)
LINE = re.compile(rb"^(0|[1-9][0-9]*) (-|[01]+) (SGE|DPOS|INFEAS|FAIL)\n$")
CLAIMED = {"SGE": 891318, "DPOS": 8018, "INFEAS": 46344}


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for blk in iter(lambda: fh.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


def free_bytes():
    st = os.statvfs("/")
    return st.f_bavail * st.f_frsize


def maxrss():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  # bytes on Darwin


def main():
    run, specp, spec_sha, leafp, leaf_sha, primp, prim_sha = sys.argv[1:8]
    limit, extra_depth, stop_epoch = int(sys.argv[8]), int(sys.argv[9]), float(sys.argv[10])
    t0 = time.time()
    res = {"script": "p_replay_v2.py", "argv": sys.argv[1:], "started_epoch": t0}
    pre = {"spec": sha256_file(specp), "primal": sha256_file(primp), "leaves": sha256_file(leafp)}
    res["pre_hashes"] = pre
    if pre["spec"] != spec_sha or pre["primal"] != prim_sha or pre["leaves"] != leaf_sha:
        res["status"] = "FAIL_INPUT_HASH"
        write(run, res)
        return 2
    spec = json.load(open(specp))
    primal = json.load(open(primp))
    T = C.parse_q(spec["T"])
    assert T == Fraction(11, 50), T
    prec = int(spec["prec"])
    geom = C.Geometry(spec)
    ev = C.Evaluator(T, prec)
    res["evaluator"] = {"T": str(T), "prec": prec, "region": [[str(a), str(b)] for a, b in geom.region],
                        "nsplit": geom.nsplit, "weights": [str(x) for x in geom.weights], "max_depth": geom.max_depth}
    counts = {"SGE": 0, "DPOS": 0, "INFEAS": 0, "FAIL": 0}
    methods = {}
    depth_hist = {}
    cover_errors = []
    n_cover_errors = 0
    format_errors = []
    subdiv = []
    n_subdiv = 0
    n_subdiv_ok = 0
    subdiv_deepest = {}
    subdiv_boxes = 0
    fails = []
    dpos_bb = None
    hasher = hashlib.sha256()
    n = 0
    guard = None
    sdraw = open(os.path.join(run, "subdivisions.txt.gz"), "xb")
    sdgz = gzip.GzipFile(fileobj=sdraw, mode="wb", mtime=0)
    with gzip.open(leafp, "rb") as fh:
        for raw in fh:
            hasher.update(raw)
            n += 1
            m = LINE.match(raw)
            if not m:
                if len(format_errors) < 50:
                    format_errors.append({"line": n, "raw": raw[:80].decode("latin-1")})
                continue
            ci = int(m.group(1))
            path = m.group(2).decode()
            if path == "-":
                path = ""
            out = m.group(3).decode()
            box, errs = geom.feed(ci, path)
            if errs:
                n_cover_errors += len(errs)
                for e in errs:
                    if len(cover_errors) < 50:
                        cover_errors.append({"line": n, "error": e})
            if box is None:
                continue
            counts[out] += 1
            depth_hist[len(path)] = depth_hist.get(len(path), 0) + 1
            ok, how = ev.verify(box, out)
            if not ok and out in ("SGE", "DPOS"):
                sok, nsub, deep, first = ev.verify_subdiv(box, out, geom, extra_depth)
                n_subdiv += 1
                subdiv_boxes += nsub
                subdiv_deepest[deep] = subdiv_deepest.get(deep, 0) + 1
                sdgz.write(f"{n} {ci} {path if path else '-'} {out} {int(sok)} {nsub} {deep} "
                           f"{diag(ev, box, out)}\n".encode())
                rec = {"line": n, "cell": ci, "path": path, "outcome": out, "direct": how, "subdiv_ok": sok,
                       "subboxes_certified": nsub, "deepest": deep}
                if first:
                    rec["first_failure"] = first
                if len(subdiv) < 200 or not sok:
                    subdiv.append(rec)
                if sok:
                    n_subdiv_ok += 1
                    ok, how = True, "subdiv"
            key = f"{out}:{how if ok else 'FAIL'}"
            methods[key] = methods.get(key, 0) + 1
            if not ok and len(fails) < 200:
                fails.append({"line": n, "cell": ci, "path": path, "outcome": out, "reason": how,
                              "box": [[str(a), str(b)] for a, b in box]})
            if out == "DPOS":
                lo = [iv[0] for iv in box]
                hi = [iv[1] for iv in box]
                dpos_bb = [lo, hi] if dpos_bb is None else [[min(a, b) for a, b in zip(dpos_bb[0], lo)],
                                                             [max(a, b) for a, b in zip(dpos_bb[1], hi)]]
            if n % 50000 == 0:
                fb, rs, now = free_bytes(), maxrss(), time.time()
                print(f"progress {n} {counts} methods={methods} cover_err={n_cover_errors} fails={len(fails)} "
                      f"elapsed={now - t0:.1f} free={fb} maxrss={rs}", flush=True)
                if fb < FLOOR:
                    guard = f"disk floor: free {fb} < {FLOOR}"
                elif rs > RSS_CAP:
                    guard = f"rss cap: {rs} > {RSS_CAP}"
                elif now > stop_epoch:
                    guard = f"stop time reached at {now}"
                if guard:
                    break
            if limit and n >= limit:
                break
    res["leaves_read"] = n
    res["line_sha256_of_read_lines"] = hasher.hexdigest()
    res["counts"] = counts
    res["methods"] = methods
    res["depth_histogram"] = {str(k): v for k, v in sorted(depth_hist.items())}
    res["format_errors_first50"] = format_errors
    sdgz.close()
    sdraw.close()
    res["subdivisions_file_sha256"] = sha256_file(os.path.join(run, "subdivisions.txt.gz"))
    res["subdivisions_first200_plus_all_failed"] = subdiv
    res["n_subdivided_leaves"] = n_subdiv
    res["n_subdiv_ok"] = n_subdiv_ok
    res["subdiv_deepest_histogram"] = {str(k): v for k, v in sorted(subdiv_deepest.items())}
    res["subdiv_total_subboxes_certified"] = subdiv_boxes
    res["fails_first200"] = fails
    n_fail = sum(v for k, v in methods.items() if k.endswith(":FAIL")) + counts["FAIL"]
    res["n_unverified_leaves"] = n_fail
    res["dpos_bounding_box_exact"] = None if dpos_bb is None else [[str(x) for x in dpos_bb[0]],
                                                                    [str(x) for x in dpos_bb[1]]]
    if guard:
        res["status"] = "UNKNOWN_GUARD"
        res["guard"] = guard
    elif limit:
        res["status"] = "SAMPLE_ONLY"
    else:
        fin = geom.finish()
        n_cover_errors += len(fin)
        for e in fin:
            if len(cover_errors) < 50:
                cover_errors.append({"line": "end", "error": e})
        total = sum(counts.values())
        checks = {
            "no_format_errors": not format_errors,
            "coverage_complete_no_errors": n_cover_errors == 0,
            "cells_seen": geom.cells_seen,
            "cells_expected": geom.ncells,
            "every_leaf_verified": n_fail == 0,
            "no_FAIL_leaves": counts["FAIL"] == 0,
            "counts_match_primal_json": all(counts[k] == primal["counts"][k] for k in counts),
            "counts_match_task_claim": all(counts[k] == v for k, v in CLAIMED.items()) and total == 945680,
            "line_hash_matches_primal_json": hasher.hexdigest() == primal["leaf_lines_sha256"],
            "depth_hist_matches_primal_json": res["depth_histogram"] == primal["depth_histogram"],
            "total_leaves": total,
        }
        res["checks"] = checks
        ok_all = all(v for k, v in checks.items() if k.startswith(("no_", "coverage", "every", "counts", "line",
                                                                    "depth")))
        ok_all = ok_all and checks["cells_seen"] == checks["cells_expected"]
        res["status"] = "PASS_FULL_REPLAY" if ok_all else "FAIL"
    res["cover_errors_first50"] = cover_errors
    res["n_cover_errors"] = n_cover_errors
    post = sha256_file(leafp)
    res["post_leaves_sha256"] = post
    if post != leaf_sha:
        res["status"] = "FAIL_LEAVES_CHANGED_DURING_RUN"
    res["elapsed_seconds"] = round(time.time() - t0, 2)
    res["maxrss_bytes"] = maxrss()
    res["free_bytes_end"] = free_bytes()
    write(run, res)
    print("RESULT", res["status"], json.dumps({k: res[k] for k in ("counts", "methods", "n_cover_errors",
                                                                  "n_unverified_leaves", "elapsed_seconds")}))
    return 0 if res["status"] in ("PASS_FULL_REPLAY", "SAMPLE_ONLY") else 1


def write(run, res):
    with open(os.path.join(run, "RESULT.json"), "x") as fh:
        json.dump(res, fh, indent=1)


def diag(ev, box, out):
    """Direct-failure diagnostics for a leaf that needed recorded subdivision (informational)."""
    if out == "SGE":
        balls, P, z, a, G = ev.G_naive(box)
        Gm, a1m = ev.G_mvf(box, balls, P, z, a)
        return (f"a1n={int(a[1] > 0)} a1m={int(a1m > 0)} Gn_lo={float(G.lower()):.3e} "
                f"Gm_lo={float(Gm.lower()):.3e}")
    balls, a, d, D, P, z = ev.D_naive(box)
    Dm, am = ev.D_mvf(box, balls, a, d, P, z)
    return (f"an={''.join(str(int(x > 0)) for x in a)} am={''.join(str(int(x > 0)) for x in am)} "
            f"Dn_lo={float(D.lower()):.3e} Dm_lo={float(Dm.lower()):.3e}")


if __name__ == "__main__":
    sys.exit(main())
