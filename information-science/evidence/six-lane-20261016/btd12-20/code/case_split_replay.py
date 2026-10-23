#!/usr/bin/env python3
"""case_split_replay.py -- pinned manifest and clean replay of the computer-assisted case split for
BTD(12,20;4,3,10;6,4) (notes/case-split-r2.md Parts C and E).  Python 3 stdlib + nauty + drat-trim (+ kissat only via
the controls).

  /usr/bin/python3 -B code/case_split_replay.py --write-manifest   pin everything (evidence/case-split-manifest-v1.json)
  /usr/bin/python3 -B code/case_split_replay.py TAG                replay into runs/case-split-replay-TAG/ (fresh)

Replay steps (one process at a time, native limits only, nothing killed, nothing outside the replay directory written):
 1. every pinned file and tool binary has its manifest SHA-256;
 2. regenerate the d-type lists with nauty exactly as pinned (geng -q -d1 -D6 n 1:12 | multig -q -e12 -D6 -T |
    code/mg_filter.py) and the e-multisets / e-combos with code/e_multisets.py and code/e_combos.py; each output must be
    byte-identical to the pinned file (so code/case_list.py on the pinned inputs gives the pinned cases.jsonl, which is
    rebuilt and compared as well);
 3. code/tetrad_facts.py, code/enum_crosscheck.py and code/dcomp_controls.py must PASS again;
 4. for every case of cases.jsonl: rebuild its CNF text with code/dcomp_cnf.py exactly as code/cert_run.py wrote it and
    compare with the stored runs/cert-v1/cnf/<id>.cnf (SHA-256, and the SHA recorded in the results file); then run
    bin/drat-trim on the stored CNF and the stored proof runs/cert-v1/proof/<id>.drat (-t 600); it must print
    `s VERIFIED` and exit 0; every case index 0..3072 must be covered exactly once;
 5. write result.json with every count, hash and the verdict PASS / FAIL.
"""
import hashlib
import json
import os
import subprocess
import sys
import time

CODE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(CODE)
sys.path.insert(0, CODE)

PINNED = ["code/mg_filter.py", "code/e_multisets.py", "code/e_combos.py", "code/case_list.py", "code/dcomp_cnf.py",
          "code/btd_cnf_a.py", "code/cert_run.py", "code/tetrad_facts.py", "code/enum_crosscheck.py",
          "code/dcomp_controls.py", "code/verify_btd.py", "code/btd_check.c", "code/case_split_replay.py",
          "runs/mg-v1/mg-n4.txt", "runs/mg-v1/mg-n5.txt", "runs/mg-v1/mg-n6.txt", "runs/mg-v1/mg-n7.txt",
          "runs/mg-v1/mg-n8.txt", "runs/mg-v1/mg-n9.txt", "runs/mg-v1/mg-n10.txt", "runs/e-v1/e-multisets.json",
          "runs/e-v1/e-combos-v2.jsonl", "runs/cases-v1/cases.jsonl", "runs/cert-v1/results-0-20.jsonl",
          "runs/cert-v1/results-20-3073.jsonl", "notes/case-split-r1.md", "notes/case-split-r2.md",
          "controls/checkers-v1/checker-controls.json", "evidence/tetrad-facts-v1.json",
          "evidence/enum-crosscheck-v1.json", "controls/dcomp-v1/controls.json"]
FIXTURES = ["btd_3_3_1_1_3_3_2_rows_201_120_012", "btd_3_6_2_2_6_3_4_doubled_repeated_columns",
            "francel_hurd_fig2_btd_4_12_3_6_15_5_16", "cpro1_2501_fig20_btd_12_16_4_4_12_9_8",
            "cpro1_2501_fig19_btd_14_21_6_3_12_8_6", "cpro1_2505_fig4_btd_16_22_9_1_11_8_5"]
TOOLS = {"geng": "/opt/homebrew/Cellar/nauty/2.9.3/bin/geng", "multig": "/opt/homebrew/Cellar/nauty/2.9.3/bin/multig",
         "genbg": "/opt/homebrew/Cellar/nauty/2.9.3/bin/genbg", "kissat": "/opt/homebrew/bin/kissat",
         "drat-trim": os.path.join(LANE, "bin", "drat-trim"), "btd_check": os.path.join(LANE, "bin", "btd_check"),
         "python3": "/usr/bin/python3"}
COMMANDS = {
    "d_type_lists": "for n in 4..10: geng -q -d1 -D6 n 1:12 | multig -q -e12 -D6 -T | python3 -B code/mg_filter.py "
                    "> runs/mg-v1/mg-n<n>.txt",
    "e_multisets": "python3 -B code/e_multisets.py runs/e-v1/e-multisets.json",
    "e_combos": "python3 -B code/e_combos.py runs/e-v1/e-multisets.json runs/e-v1/e-combos-v2.jsonl "
                "(calls geng -q -d1 -D6 n lo:e | multig -q -e<e> -D6 -T, lo = max(1, ceil(n/2)))",
    "case_list": "python3 -B code/case_list.py runs/cases-v1/cases.jsonl",
    "certificates": "python3 -B code/cert_run.py runs/cases-v1/cases.jsonl runs/cert-v1 --start 0 --stop 20, then "
                    "--start 20 --stop 3073; per case: kissat -q --time=600 CNF PROOF; drat-trim CNF PROOF -t 600",
    "cross_checks": "python3 -B code/tetrad_facts.py; code/enum_crosscheck.py (genbg -q -d2:2 -D6:2 n e 2e:2e); "
                    "code/dcomp_controls.py",
}
PARAMS = (12, 20, 4, 3, 10, 6, 4)


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for ch in iter(lambda: f.read(1 << 22), b""):
            h.update(ch)
    return h.hexdigest()


def write_manifest():
    out = os.path.join(LANE, "evidence", "case-split-manifest-v1.json")
    files = {p: sha(os.path.join(LANE, p)) for p in PINNED}
    for fx in FIXTURES:
        p = f"controls/checkers-v1/{fx}.btd"
        files[p] = sha(os.path.join(LANE, p))
    tools = {k: {"path": v, "sha256": sha(v)} for k, v in TOOLS.items()}
    man = {"created_host": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "params": list(PARAMS), "files": files,
           "tools": tools, "commands": COMMANDS, "nauty_version": "2.9.3 (Homebrew Cellar)",
           "kissat_version": "4.0.4", "drat_trim_upstream_commit": "2e3b2dc0ecf938addbd779d42877b6ed69d9a985",
           "certificate_store": "runs/cert-v1/cnf/<id>.cnf and runs/cert-v1/proof/<id>.drat (SHA-256 per case in the "
                                "two results files)", "cases": 3073}
    with open(out, "x") as f:
        json.dump(man, f, indent=1)
        f.write("\n")
    print(out, sha(out))
    return 0


def cnf_text(case, enc_sha):
    import dcomp_cnf
    F, _ = dcomp_cnf.build(PARAMS, case["rows"])
    return (f"c dcomp_cnf.py sha256 {enc_sha}\nc params {' '.join(map(str, PARAMS))} case {case['id']}\n"
            f"p cnf {F.nv} {len(F.clauses)}\n" + "".join(" ".join(map(str, c)) + " 0\n" for c in F.clauses))


def replay(tag):
    rd = os.path.join(LANE, "runs", f"case-split-replay-{tag}")
    os.makedirs(rd)
    man = json.load(open(os.path.join(LANE, "evidence", "case-split-manifest-v1.json")))
    res = {"tag": tag, "started_host": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
           "manifest_sha256": sha(os.path.join(LANE, "evidence", "case-split-manifest-v1.json")), "checks": {}}
    ok = True

    def check(name, cond, detail=None):
        nonlocal ok
        res["checks"][name] = bool(cond) if detail is None else {"ok": bool(cond), "detail": detail}
        ok &= bool(cond)
        print(("ok " if cond else "BAD"), name, "" if detail is None else detail)

    # 1. pins
    bad = [p for p, h in man["files"].items() if sha(os.path.join(LANE, p)) != h]
    check("pinned_files", not bad, bad[:5])
    badt = [k for k, v in man["tools"].items() if sha(v["path"]) != v["sha256"]]
    check("pinned_tools", not badt, badt)
    # 2. regenerate
    py = [sys.executable, "-B"]
    for n in range(4, 11):
        g = subprocess.run(["geng", "-q", "-d1", "-D6", str(n), "1:12"], capture_output=True, check=True)
        m = subprocess.run(["multig", "-q", "-e12", "-D6", "-T"], input=g.stdout, capture_output=True, check=True)
        f = subprocess.run(py + [os.path.join(CODE, "mg_filter.py")], input=m.stdout, capture_output=True, check=True)
        p = os.path.join(rd, f"mg-n{n}.txt")
        with open(p, "xb") as fh:
            fh.write(f.stdout)
        check(f"regen_mg_n{n}", sha(p) == man["files"][f"runs/mg-v1/mg-n{n}.txt"])
    p = os.path.join(rd, "e-multisets.json")
    subprocess.run(py + [os.path.join(CODE, "e_multisets.py"), p], capture_output=True, check=True)
    check("regen_e_multisets", sha(p) == man["files"]["runs/e-v1/e-multisets.json"])
    p2 = os.path.join(rd, "e-combos.jsonl")
    subprocess.run(py + [os.path.join(CODE, "e_combos.py"), p, p2], capture_output=True, check=True)
    check("regen_e_combos", sha(p2) == man["files"]["runs/e-v1/e-combos-v2.jsonl"])
    p3 = os.path.join(rd, "cases.jsonl")
    subprocess.run(py + [os.path.join(CODE, "case_list.py"), p3], capture_output=True, check=True)
    check("regen_cases", sha(p3) == man["files"]["runs/cases-v1/cases.jsonl"])
    # 3. facts, cross-checks, controls
    q = subprocess.run(py + [os.path.join(CODE, "tetrad_facts.py"), os.path.join(rd, "tetrad-facts.json")],
                       capture_output=True, text=True)
    check("tetrad_facts", q.returncode == 0 and "TETRAD-FACTS PASS" in q.stdout)
    q = subprocess.run(py + [os.path.join(CODE, "enum_crosscheck.py"), os.path.join(LANE, "runs", "e-v1",
                                                                                      "e-multisets.json"),
                             os.path.join(rd, "enum-crosscheck.json")], capture_output=True, text=True)
    check("enum_crosscheck", q.returncode == 0 and "ENUM-CROSSCHECK PASS" in q.stdout)
    q = subprocess.run(py + [os.path.join(CODE, "dcomp_controls.py"), os.path.join(rd, "dcomp-controls")],
                       capture_output=True, text=True)
    check("dcomp_controls", q.returncode == 0 and "DCOMP-CONTROLS PASS" in q.stdout)
    # 4. certificates
    recs = {}
    for fn in ("results-0-20.jsonl", "results-20-3073.jsonl"):
        for line in open(os.path.join(LANE, "runs", "cert-v1", fn)):
            o = json.loads(line)
            if "idx" in o:
                if o["idx"] in recs:
                    check("no_duplicate_case_records", False, o["idx"])
                recs[o["idx"]] = o
    cases = [json.loads(x) for x in open(os.path.join(LANE, "runs", "cases-v1", "cases.jsonl"))]
    check("coverage", sorted(recs) == list(range(len(cases))) and len(cases) == 3073, len(cases))
    enc_sha = sha(os.path.join(CODE, "dcomp_cnf.py"))
    n_cnf = n_ver = 0
    bad_cases = []
    t0 = time.time()
    with open(os.path.join(rd, "per-case.jsonl"), "x") as pc:
        for idx, case in enumerate(cases):
            r = recs[idx]
            cnf = os.path.join(LANE, "runs", "cert-v1", "cnf", f"{case['id']}.cnf")
            proof = os.path.join(LANE, "runs", "cert-v1", "proof", f"{case['id']}.drat")
            txt = cnf_text(case, enc_sha)
            hs = hashlib.sha256(txt.encode()).hexdigest()
            cnf_ok = r["id"] == case["id"] and hs == r["cnf_sha256"] == sha(cnf)
            pr_ok = sha(proof) == r.get("proof_sha256")
            dt = subprocess.run([os.path.join(LANE, "bin", "drat-trim"), cnf, proof, "-t", "600"], capture_output=True,
                                text=True)
            ver = dt.returncode == 0 and any(ln.strip() == "s VERIFIED" for ln in dt.stdout.splitlines())
            n_cnf += cnf_ok
            n_ver += ver and pr_ok
            if not (cnf_ok and pr_ok and ver):
                bad_cases.append(case["id"])
            pc.write(json.dumps({"idx": idx, "id": case["id"], "cnf_rebuilt_equal": cnf_ok, "proof_sha_equal": pr_ok,
                                 "drat_verified": ver}) + "\n")
    check("cnf_rebuilt_equal_all", n_cnf == len(cases), n_cnf)
    check("drat_verified_all", n_ver == len(cases) and not bad_cases, {"verified": n_ver, "bad": bad_cases[:10]})
    res["certificate_check_wall_s"] = round(time.time() - t0, 1)
    res["ended_host"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    res["verdict"] = "PASS" if ok else "FAIL"
    with open(os.path.join(rd, "result.json"), "x") as f:
        json.dump(res, f, indent=1)
        f.write("\n")
    print("VERDICT", res["verdict"])
    return 0 if ok else 1


def main(argv):
    if len(argv) == 2 and argv[1] == "--write-manifest":
        return write_manifest()
    if len(argv) == 2 and not argv[1].startswith("-"):
        return replay(argv[1])
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
