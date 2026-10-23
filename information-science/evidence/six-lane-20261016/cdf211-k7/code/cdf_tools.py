"""Direct verifiers for cyclic (v,k,1) difference families.  They are independent of every search code.

diff_check : the multiset of ordered within-block differences mod v must be exactly Z_v \\ {0}.
pair_check : develop every base block over Z_v; every unordered pair of points must lie in exactly one
             developed block, which certifies the cyclic S(2,k,v).
corr_check : periodic auto- and cross-correlation of the block indicator sequences must be <= 1
             (perfect optical orthogonal code), and the block count must be (v-1)/(k(k-1)).

Run as a script for the retained controls on the two published cyclic (505,7,1) families
(Hetman, arXiv:2604.04975v1; blocks parsed from the TeX in sources/).
  - Accept: both families, a mirror (one block negated), a translated block, and a unit multiple.
  - Reject, for the intended reason: an element change, a dropped block, a duplicated block, and a
    repeated element.
"""
import re, os, sys, json, itertools, math
from collections import Counter

def diff_check(v, k, blocks):
    t = (v - 1) // (k * (k - 1))
    bad = [i for i, B in enumerate(blocks) if len(B) != k or len({x % v for x in B}) != k]
    cnt = Counter()
    for B in blocks:
        S = [x % v for x in B]
        for a in S:
            for b in S:
                if a != b: cnt[(a - b) % v] += 1
    missing = sum(1 for d in range(1, v) if cnt[d] == 0)
    repeated = sum(1 for d in range(1, v) if cnt[d] > 1)
    ok = ((v - 1) % (k * (k - 1)) == 0 and len(blocks) == t and not bad and missing == 0 and repeated == 0
          and cnt[0] == 0 and sum(cnt.values()) == v - 1)
    return dict(ok=ok, n_blocks=len(blocks), expected_blocks=t, bad_blocks=bad, missing=missing, repeated=repeated)

def pair_check(v, k, blocks):
    hit = bytearray(v * v); dup = 0; nb = 0
    for B in blocks:
        S = sorted({x % v for x in B})
        for s in range(v):
            D = sorted((x + s) % v for x in S); nb += 1
            for a, b in itertools.combinations(D, 2):
                if hit[a * v + b]: dup += 1
                hit[a * v + b] = 1
    covered = sum(hit)
    return dict(ok=(dup == 0 and covered == v * (v - 1) // 2), developed_blocks=nb, pairs_covered=covered,
                duplicate_hits=dup, total_pairs=v * (v - 1) // 2)

def corr_check(v, k, blocks):
    sets = [{x % v for x in B} for B in blocks]
    worst_auto = max((len(S & {(x + s) % v for x in S}) for S in sets for s in range(1, v)), default=0)
    worst_cross = max((len(S & {(x + s) % v for x in T}) for S, T in itertools.combinations(sets, 2) for s in range(v)), default=0)
    ok = worst_auto <= 1 and worst_cross <= 1 and len(blocks) == (v - 1) // (k * (k - 1)) and all(len(S) == k for S in sets)
    return dict(ok=ok, worst_auto=worst_auto, worst_cross=worst_cross)

def all_checks(v, k, blocks):
    d, p, c = diff_check(v, k, blocks), pair_check(v, k, blocks), corr_check(v, k, blocks)
    return dict(ok=d["ok"] and p["ok"] and c["ok"], diff=d, pair=p, corr=c)

def hetman_505():
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sources", "tex-hetman-2604.04975")
    tex = open(os.path.join(root, "S_2,7,505_.tex")).read()
    fams = []
    for line in tex.splitlines():
        if "\\item $2525" in line:
            fams.append([[int(x) for x in m.split(",")] for m in re.findall(r"\\\{(\d+(?:,\s*\d+){6})\\\}", line)])
    return fams

if __name__ == "__main__":
    fams = hetman_505(); out = dict(parsed_families=[len(f) for f in fams]); v, k = 505, 7
    F = fams[0]
    out["family1"] = all_checks(v, k, F)
    out["family2"] = all_checks(v, k, fams[1])
    pos = {"mirror_block3": [B if i != 3 else [(-x) % v for x in B] for i, B in enumerate(F)],
           "translate_block5": [B if i != 5 else [(x + 17) % v for x in B] for i, B in enumerate(F)],
           "unit_multiple_2": [[(2 * x) % v for x in B] for B in F]}
    neg = {"element_change": [B if i != 0 else B[:-1] + [(B[-1] + 1) % v] for i, B in enumerate(F)],
           "drop_block": F[:-1],
           "duplicate_block": F[:3] + [F[2]] + F[4:],
           "repeated_element": [B if i != 1 else B[:-1] + [B[0]] for i, B in enumerate(F)]}
    out["positive_variants"] = {n: all_checks(v, k, b)["ok"] for n, b in pos.items()}
    out["negative_variants"] = {n: all_checks(v, k, b) for n, b in neg.items()}
    reasons = {"element_change": lambda r: r["diff"]["repeated"] > 0 and r["pair"]["duplicate_hits"] > 0,
               "drop_block": lambda r: r["diff"]["n_blocks"] == 11 and r["diff"]["missing"] == 42,
               "duplicate_block": lambda r: r["diff"]["repeated"] == 42 and r["pair"]["duplicate_hits"] > 0,
               "repeated_element": lambda r: r["diff"]["bad_blocks"] == [1]}
    out["negative_rejected_for_intended_reason"] = {n: (not out["negative_variants"][n]["ok"]) and reasons[n](out["negative_variants"][n]) for n in neg}
    ok = (out["parsed_families"] == [12, 12] and out["family1"]["ok"] and out["family2"]["ok"]
          and all(out["positive_variants"].values()) and all(out["negative_rejected_for_intended_reason"].values()))
    out["all_controls_pass"] = ok
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "verifier-controls-505.json"), "w"), indent=1)
    print(json.dumps({a: b for a, b in out.items() if a != "negative_variants"}, indent=1))
    sys.exit(0 if ok else 1)
