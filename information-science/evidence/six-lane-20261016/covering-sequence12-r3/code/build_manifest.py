#!/usr/bin/env python3
"""build_manifest.py -- run manifest for lane covering-sequence12-r3: toolchain, source/binary SHA-256, the exact
commands, and one record per search job (argv, range or necklace count, examined, covering, status, host start/end
times, receipt hashes), plus per-(n,R,L) accounting: B ranges partition [0, 2^L) and examined sums to 2^L; A count
equals N(L) (recomputed here) and the periods sum to 2^L; compare.json all_ok.

Usage (from the lane root): build_manifest.py OUT.json        (OUT created exclusively; read-only otherwise)
Job start = birth time of the job's .found file (each program creates it just before enumerating); job end =
modification time of its .txt receipt (written once at the end). Both are host filesystem clock readings.
"""
import datetime
import glob
import hashlib
import json
import os
import platform
import subprocess
import sys
from math import gcd

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENV = "export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1"
COMMANDS = {
    "compile (06:53-06:54)": [
        "cc -O2 -Wall -Wextra -o bin/cs_brute code/cs_brute.c",
        "cc -O2 -Wall -Wextra -o bin/cs_neck code/cs_neck.c"],
    "controls/verifier-v1 (06:52:20, superseded draft of the controls script, not preserved)": [
        "/usr/bin/python3 code/verifier_controls.py sources/parent-screen-cpro1-length36.txt controls/verifier-v1"],
    "controls/verifier-v2 (06:52:50; script archive/code/verifier_controls.v2.py, verifier archive/code/verify_cs.v1.py)": [
        "/usr/bin/python3 code/verifier_controls.py sources/parent-screen-cpro1-length36.txt controls/verifier-v2"],
    "controls/verifier-v3 (07:09:37; current code/verifier_controls.py and code/verify_cs.py)": [
        "/usr/bin/python3 code/verifier_controls.py sources/parent-screen-cpro1-length36.txt controls/verifier-v3"],
    "controls/calibration-v1": [
        ENV + " && mkdir -p controls/calibration-v1 && for L in $(seq 1 13); do /usr/bin/python3 code/compare_runs.py "
        "run controls/calibration-v1/n9R3L$L 9 3 $L 1 600 || echo \"NOT-OK at L=$L\"; done",
        ENV + " && for spec in \"10 3 17\" \"11 3 21\" \"9 2 21\" \"8 2 15\" \"8 3 7\"; do set -- $spec; for L in "
        "$(seq 1 $3); do /usr/bin/python3 code/compare_runs.py run controls/calibration-v1/n$1R$2L$L $1 $2 $L 1 900 "
        "|| echo \"NOT-OK n=$1 R=$2 L=$L\"; done; done"],
    "runs/bench-v1": [
        "export OMP_NUM_THREADS=1 && mkdir -p runs/bench-v1 && ./bin/cs_brute 12 3 28 0 268435456 600 "
        "runs/bench-v1/B-12-3-28 && ./bin/cs_neck 12 3 28 600 runs/bench-v1/A-12-3-28"],
    "runs/L34-v1": [
        "export OMP_NUM_THREADS=1 && mkdir runs/L34-v1 && T=$((1<<34)); for k in 0 1 2 3; do lo=$((T*k/4)); "
        "hi=$((T*(k+1)/4)); ./bin/cs_brute 12 3 34 $lo $hi 3000 runs/L34-v1/B-12-3-34-00$k > "
        "runs/L34-v1/B-12-3-34-00$k.stdout 2>&1 & done; wait",
        "export OMP_NUM_THREADS=1 && ./bin/cs_neck 12 3 34 3000 runs/L34-v1/A-12-3-34 && /usr/bin/python3 "
        "code/compare_runs.py compare runs/L34-v1/compare 12 3 34 runs/L34-v1/B-12-3-34-000,runs/L34-v1/B-12-3-34-001,"
        "runs/L34-v1/B-12-3-34-002,runs/L34-v1/B-12-3-34-003 runs/L34-v1/A-12-3-34"],
    "runs/L35-v1": [
        "export OMP_NUM_THREADS=1 && mkdir runs/L35-v1 && T=$((1<<35)); for k in 0 1 2; do lo=$((T*k/3)); "
        "hi=$((T*(k+1)/3)); ./bin/cs_brute 12 3 35 $lo $hi 3000 runs/L35-v1/B-12-3-35-00$k > "
        "runs/L35-v1/B-12-3-35-00$k.stdout 2>&1 & done; wait",
        "export OMP_NUM_THREADS=1 && ./bin/cs_neck 12 3 35 3000 runs/L35-v1/A-12-3-35",
        "/usr/bin/python3 code/compare_runs.py compare runs/L35-v1/compare 12 3 35 runs/L35-v1/B-12-3-35-000,"
        "runs/L35-v1/B-12-3-35-001,runs/L35-v1/B-12-3-35-002 runs/L35-v1/A-12-3-35"],
    "runs/L36-v1": [
        "export OMP_NUM_THREADS=1 && mkdir runs/L36-v1 && T=$((1<<36)); for k in 0 1 2; do lo=$((T*k/3)); "
        "hi=$((T*(k+1)/3)); ./bin/cs_brute 12 3 36 $lo $hi 3000 runs/L36-v1/B-12-3-36-00$k > "
        "runs/L36-v1/B-12-3-36-00$k.stdout 2>&1 & done; wait",
        "export OMP_NUM_THREADS=1 && ./bin/cs_neck 12 3 36 3000 runs/L36-v1/A-12-3-36",
        "/usr/bin/python3 code/compare_runs.py compare runs/L36-v1/compare 12 3 36 runs/L36-v1/B-12-3-36-000,"
        "runs/L36-v1/B-12-3-36-001,runs/L36-v1/B-12-3-36-002 runs/L36-v1/A-12-3-36",
        "/usr/bin/python3 code/classes_report.py runs/L36-v1/A-12-3-36.found 36 "
        "sources/parent-screen-cpro1-length36.txt runs/L36-v1/classes-report.json"],
    "runs/lower-v1": [
        ENV + " && mkdir runs/lower-v1 && ( for L in 33; do /usr/bin/python3 code/compare_runs.py run "
        "runs/lower-v1/n12R3L$L 12 3 $L 1 3000 || echo \"NOT-OK L=$L\"; done > runs/lower-v1/loop1.log 2>&1 & "
        "for L in 32 31; do /usr/bin/python3 code/compare_runs.py run runs/lower-v1/n12R3L$L 12 3 $L 1 3000 || "
        "echo \"NOT-OK L=$L\"; done > runs/lower-v1/loop2.log 2>&1 & for L in $(seq 1 30); do /usr/bin/python3 "
        "code/compare_runs.py run runs/lower-v1/n12R3L$L 12 3 $L 1 3000 || echo \"NOT-OK L=$L\"; done > "
        "runs/lower-v1/loop3.log 2>&1 & wait )"],
    "certs/L36-v1": [
        "/usr/bin/python3 code/export_l36.py runs/L36-v1 sources/parent-screen-cpro1-length36.txt certs/L36-v1"],
}
# time limit argument (seconds) used per job directory; it does not affect COMPLETE results
SECS = {"controls/calibration-v1/n9R3": "600", "controls/calibration-v1": "900", "runs/bench-v1": "600",
        "runs/L34-v1": "3000", "runs/L35-v1": "3000", "runs/L36-v1": "3000", "runs/lower-v1": "3000"}


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def host(ts):
    return datetime.datetime.fromtimestamp(ts).astimezone().isoformat(timespec="seconds")


def receipt(path):
    d = {}
    for line in open(path):
        k, _, v = line.rstrip("\n").partition(" ")
        d[k] = v
    return d


def necklaces(L):
    tot = 0
    for d in range(1, L + 1):
        if L % d == 0:
            tot += sum(1 for k in range(1, d + 1) if gcd(k, d) == 1) * 2 ** (L // d)
    assert tot % L == 0
    return tot // L


def secs_for(rel):
    for key in sorted(SECS, key=len, reverse=True):
        if rel.startswith(key):
            return SECS[key]
    raise KeyError(rel)


def main(argv):
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    os.chdir(LANE)
    out = {"lane": "information-science/evidence/six-lane-20261016/covering-sequence12-r3",
           "generated_at_host": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
           "toolchain": {"cc": subprocess.run(["cc", "--version"], capture_output=True, text=True).stdout.split("\n")[0],
                         "python_for_scripts": "/usr/bin/python3 " + platform.python_version(),
                         "machine": platform.machine(), "os": platform.platform()},
           "working_directory_for_all_commands": "lane root",
           "commands": COMMANDS, "files": {}, "jobs": [], "accounting": []}
    for pat in ("code/*", "archive/code/*", "bin/*", "sources/*"):
        for p in sorted(glob.glob(pat)):
            if os.path.isfile(p):
                out["files"][p] = {"sha256": sha(p), "bytes": os.path.getsize(p)}
    groups = {}
    for rp in sorted(glob.glob("runs/**/*.txt", recursive=True) + glob.glob("controls/calibration-v1/**/*.txt",
                                                                             recursive=True)):
        first = open(rp).readline().strip()
        if first not in ("program cs_brute", "program cs_neck"):
            continue
        r = receipt(rp)
        pre = rp[:-4]
        n, R, L = int(r["n"]), int(r["R"]), int(r["L"])
        prog = r["program"]
        job = {"program": prog, "prefix": pre, "n": n, "R": R, "L": L, "status": r["status"],
               "seconds": float(r["seconds"]), "start_host": host(os.stat(pre + ".found").st_birthtime),
               "end_host": host(os.stat(rp).st_mtime), "receipt_sha256": sha(rp), "found_sha256": sha(pre + ".found"),
               "found_lines": sum(1 for line in open(pre + ".found") if line.strip())}
        # jobs launched by compare_runs.py "run" used the absolute lane path for the binary and the relative prefix
        via_driver = pre.startswith("controls/calibration-v1/") or pre.startswith("runs/lower-v1/")
        lane_bin = LANE + "/bin/" if via_driver else "./bin/"
        if prog == "cs_brute":
            job.update({"lo": int(r["lo"]), "hi": int(r["hi"]), "examined": int(r["examined"]),
                        "covering": int(r["covering"])})
            job["argv"] = [lane_bin + "cs_brute", str(n), str(R), str(L), r["lo"], r["hi"], secs_for(pre), pre]
        else:
            job.update({"necklaces_generated": int(r["necklaces_generated"]),
                        "necklace_number_formula": int(r["necklace_number_formula"]),
                        "sum_of_periods": int(r["sum_of_periods"]), "selfcheck_flags": r["selfcheck_flags"].split()[0],
                        "counts_ok": r["counts_ok"], "covering": int(r["covering_representatives"])})
            job["argv"] = [lane_bin + "cs_neck", str(n), str(R), str(L), secs_for(pre), pre]
        out["jobs"].append(job)
        groups.setdefault((os.path.dirname(pre), n, R, L), []).append(job)
    allok = True
    for (d, n, R, L), jobs in sorted(groups.items(), key=lambda kv: (kv[0][1], kv[0][2], kv[0][3], kv[0][0])):
        bj = sorted((j for j in jobs if j["program"] == "cs_brute"), key=lambda j: j["lo"])
        aj = [j for j in jobs if j["program"] == "cs_neck"]
        part = bool(bj) and bj[0]["lo"] == 0 and bj[-1]["hi"] == 2 ** L and all(
            bj[i]["hi"] == bj[i + 1]["lo"] for i in range(len(bj) - 1))
        b_ok = part and all(j["status"] == "COMPLETE" and j["examined"] == j["hi"] - j["lo"] for j in bj)
        b_exam = sum(j["examined"] for j in bj)
        b_ok &= b_exam == 2 ** L and all(j["covering"] == j["found_lines"] for j in bj)
        NL = necklaces(L)
        a_ok = len(aj) == 1 and aj[0]["status"] == "COMPLETE" and aj[0]["necklaces_generated"] == NL and \
            aj[0]["sum_of_periods"] == 2 ** L and aj[0]["selfcheck_flags"] == "0" and aj[0]["counts_ok"] == "1" and \
            aj[0]["covering"] == aj[0]["found_lines"]
        cmp_path = os.path.join(d, "compare.json") if os.path.exists(os.path.join(d, "compare.json")) else \
            os.path.join(d, "compare", "compare.json")
        cmp_ok = None
        if os.path.exists(cmp_path):
            c = json.load(open(cmp_path))
            cmp_ok = bool(c["all_ok"]) and (c["n"], c["R"], c["L"]) == (n, R, L)
        acc = {"dir": d, "n": n, "R": R, "L": L, "B_jobs": len(bj),
               "B_ranges": [[j["lo"], j["hi"]] for j in bj], "B_ranges_partition_0_2L": part,
               "B_examined_total": b_exam, "two_to_L": 2 ** L, "B_covering_strings": sum(j["covering"] for j in bj),
               "A_necklaces": aj[0]["necklaces_generated"] if aj else None, "N_L_recomputed": NL,
               "A_sum_of_periods": aj[0]["sum_of_periods"] if aj else None,
               "A_covering_classes": aj[0]["covering"] if aj else None,
               "compare_json": cmp_path if cmp_ok is not None else None,
               "compare_json_sha256": sha(cmp_path) if cmp_ok is not None else None,
               "compare_all_ok": cmp_ok, "B_ok": b_ok, "A_ok": a_ok,
               "complete_and_consistent": b_ok and a_ok and cmp_ok is not False and (
                   (sum(j["covering"] for j in bj) == 0) == (aj[0]["covering"] == 0))}
        allok &= acc["complete_and_consistent"]
        out["accounting"].append(acc)
    cover = {}
    for acc in out["accounting"]:
        if (acc["n"], acc["R"]) == (12, 3) and acc["dir"] != "runs/bench-v1":
            cover[acc["L"]] = acc
    excl = sorted(L for L, a in cover.items() if a["complete_and_consistent"] and a["B_covering_strings"] == 0
                  and a["A_covering_classes"] == 0)
    out["summary_12_3"] = {
        "lengths_with_complete_runs": sorted(cover),
        "lengths_excluded_by_both_implementations": excl,
        "every_L_from_1_to_35_excluded": excl == list(range(1, 36)),
        "L36": {k: cover[36][k] for k in ("B_covering_strings", "A_covering_classes", "compare_all_ok")} if 36 in cover
        else None,
        "counting_bound": "L <= 13 impossible: at most L windows, each covering 299 words, 13*299 = 3887 < 4096"}
    out["all_accounting_ok"] = allok
    with open(argv[1], "x") as f:
        json.dump(out, f, indent=1)
        f.write("\n")
    print(json.dumps(out["summary_12_3"]))
    print("jobs", len(out["jobs"]), "groups", len(out["accounting"]), "all_accounting_ok", allok)
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
