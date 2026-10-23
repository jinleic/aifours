"""Parse o3_models output files and re-verify every reported family with cdf_tools (independent).

usage: python3 verify_o3.py OUT_JSON FILE [FILE ...]
  Every FILE is one o3_models stdout capture (SOL lines and SUMMARY lines; m2 range jobs may be split
  over several files).  Each family gets all three checks of cdf_tools.all_checks.  The canonical
  family set (each block translated to its lexicographically least translate, blocks sorted) is
  hashed, so different methods (m1, m2) can be compared for identical solution sets.
"""
import sys, os, json, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cdf_tools import all_checks

def canon_block(B, v):
    return min(tuple(sorted((x - s) % v for x in B)) for s in B)

def canon_family(F, v):
    return tuple(sorted(canon_block(B, v) for B in F))

def main():
    out_json, files = sys.argv[1], sys.argv[2:]
    fams, summaries = [], []
    for fn in files:
        for line in open(fn):
            if line.startswith("SOL "):
                fams.append([[int(x) for x in blk.split()] for blk in line[4:].strip().split(" | ")])
            elif line.startswith("SUMMARY "):
                summaries.append(json.loads(line[8:]))
    p, k = summaries[0]["p"], summaries[0]["k"]
    assert all(s["p"] == p and s["k"] == k for s in summaries)
    n_ok, bad = 0, []
    canon = set()
    for i, F in enumerate(fams):
        r = all_checks(p, k, F)
        if r["ok"]: n_ok += 1
        else: bad.append(i)
        canon.add(canon_family(F, p))
    h = hashlib.sha256(json.dumps(sorted(canon)).encode()).hexdigest()
    res = dict(files=files, p=p, k=k, summaries=summaries, n_sol_lines=len(fams),
               n_solutions_reported=sum(s["n_solutions"] for s in summaries),
               all_complete=all(s["complete"] for s in summaries),
               n_verified_all_checks=n_ok, failed_indices=bad[:50], n_distinct_canonical=len(canon),
               canonical_set_sha256=h, example=fams[0] if fams else None)
    json.dump(res, open(out_json, "w"), indent=1)
    print(json.dumps({a: b for a, b in res.items() if a not in ("summaries", "example")}))
    sys.exit(0 if not bad and len(fams) == res["n_solutions_reported"] else 1)

if __name__ == "__main__":
    main()
