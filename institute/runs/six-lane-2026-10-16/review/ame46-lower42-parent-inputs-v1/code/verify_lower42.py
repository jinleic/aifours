#!/usr/bin/env python3
"""verify_lower42.py: executable finite facts for review/SUPPORT_LOWER42.r1.md (lane ame46-support).

Standard library only, exact integers. Facts checked:
 F1 (classification). Among all C(16,8) = 12870 subsets N of {0,1}^4 with |N| = 8, those whose six 2-dimensional
    marginals are uniform (exactly two points over every cell of every coordinate pair) are exactly the ten parity
    sets {x : sum_{i in U} x_i = c mod 2}, |U| in {3, 4}, c in {0, 1}.
 F2 (blocks). For each of the ten sets, embedded as N(v) = {(v[x1], ..., v[x4])} in a 2^4 subcube of [6]^4 (the
    embedding values are irrelevant; the default subcube is {4,5}^4), the connected components of the support graph
    of each of the three reshapings 12|34, 13|24, 14|23 are exactly two 2x2 blocks with four entries each.
 F3 (phase obstruction). For each set, with the block congruence phi_rc - phi_rc' - phi_r'c + phi_r'c' = pi
    (mod 2 pi) for every block (rows r != r', columns c != c'), the script finds three blocks, one in each reshaping,
    and signs eps in {+1, -1} such that the signed sum of the three left sides is identically zero (every phase
    coefficient 0). The right sides then sum to an odd multiple of pi, which is not 0 mod 2 pi, so the system has no
    real or complex solution. The coefficient vector of the combination is printed and re-verified.
 F4 (embedding independence). F2 and F3 are re-run on every one of the 15^4 = 50625 subcubes {a_i < b_i} of
    [6]^4 with the identification 0 -> a_i, 1 -> b_i.
Writes evidence/verify_lower42.json and prints a summary; exit status 0 iff all facts hold.
"""
import itertools
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
RESHAPINGS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]


def uniform_2_marginals(N):
    for i, j in PAIRS:
        cnt = {}
        for x in N:
            cnt[(x[i], x[j])] = cnt.get((x[i], x[j]), 0) + 1
        if sorted(cnt.values()) != [2, 2, 2, 2] or len(cnt) != 4:
            return False
    return True


def parity_sets():
    out = {}
    for U in [u for k in (3, 4) for u in itertools.combinations(range(4), k)]:
        for c in (0, 1):
            out[(U, c)] = frozenset(x for x in itertools.product((0, 1), repeat=4) if sum(x[i] for i in U) % 2 == c)
    return out


def components(S, rows, cols):
    adj = {}
    for x in S:
        r = ("r", (x[rows[0]], x[rows[1]]))
        c = ("c", (x[cols[0]], x[cols[1]]))
        adj.setdefault(r, set()).add(c)
        adj.setdefault(c, set()).add(r)
    seen, comps = set(), []
    for v in sorted(adj):
        if v in seen:
            continue
        stack, comp = [v], []
        seen.add(v)
        while stack:
            u = stack.pop()
            comp.append(u)
            for w in adj[u]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        rs = sorted(u[1] for u in comp if u[0] == "r")
        cs = sorted(u[1] for u in comp if u[0] == "c")
        comps.append((rs, cs))
    return comps


def blocks_of(S):
    """Return per reshaping the list of blocks; a block is a dict {point: sign} for the congruence
    phi(r1,c1) - phi(r1,c2) - phi(r2,c1) + phi(r2,c2) = pi.  None if some component is not a 4-entry 2x2 block."""
    out = []
    for rows, cols in RESHAPINGS:
        bl = []
        for rs, cs in components(S, rows, cols):
            if len(rs) != 2 or len(cs) != 2:
                return None

            def el(r, c):
                x = [0] * 4
                x[rows[0]], x[rows[1]] = r
                x[cols[0]], x[cols[1]] = c
                return tuple(x)
            pts = {el(rs[0], cs[0]): 1, el(rs[0], cs[1]): -1, el(rs[1], cs[0]): -1, el(rs[1], cs[1]): 1}
            if any(p not in S for p in pts):
                return None
            bl.append(pts)
        out.append(bl)
    return out


def find_obstruction(bls):
    """Three blocks, one per reshaping, and signs, whose signed sum vanishes identically."""
    for b0, b1, b2 in itertools.product(*bls):
        for e1, e2 in itertools.product((1, -1), repeat=2):
            tot = {}
            for blk, eps in ((b0, 1), (b1, e1), (b2, e2)):
                for p, s in blk.items():
                    tot[p] = tot.get(p, 0) + eps * s
            if all(v == 0 for v in tot.values()):
                return [(sorted(b0.items()), 1), (sorted(b1.items()), e1), (sorted(b2.items()), e2)]
    return None


def verify_combination(comb):
    tot = {}
    for items, eps in comb:
        for p, s in items:
            tot[p] = tot.get(p, 0) + eps * s
    # three congruences each with right side pi: the signed right sides sum to (1 + e1 + e2) pi, an odd multiple
    rhs = sum(eps for _, eps in comb)
    return all(v == 0 for v in tot.values()) and rhs % 2 == 1


def main():
    cube = list(itertools.product((0, 1), repeat=4))
    uniform = [frozenset(N) for N in itertools.combinations(cube, 8) if uniform_2_marginals(N)]
    psets = parity_sets()
    f1 = set(uniform) == set(psets.values()) and len(uniform) == 10 and len(set(psets.values())) == 10
    report = {"F1_classification_holds": f1, "n_subsets_checked": 12870, "n_uniform": len(uniform), "sets": []}
    ok_all = f1
    for (U, c), N in sorted(psets.items()):
        emb = {0: 4, 1: 5}
        S = frozenset(tuple(emb[b] for b in x) for x in N)
        bls = blocks_of(S)
        f2 = bls is not None and all(len(b) == 2 for b in bls)
        comb = find_obstruction(bls) if f2 else None
        f3 = comb is not None and verify_combination(comb)
        report["sets"].append({
            "U": [i + 1 for i in U], "c": c, "N_in_subcube_45": ["".join(map(str, x)) for x in sorted(S)],
            "F2_two_2x2_blocks_per_reshaping": f2,
            "blocks": [[["".join(map(str, p)) + ("+" if s > 0 else "-") for p, s in sorted(b.items())] for b in bl]
                       for bl in bls] if bls else None,
            "F3_obstruction": [{"block": ["".join(map(str, p)) + ("+" if s > 0 else "-") for p, s in items],
                                "coefficient": eps} for items, eps in comb] if comb else None,
            "F3_obstruction_verified": f3})
        ok_all &= f2 and f3
    # F4: every subcube embedding
    f4 = True
    for vals in itertools.product(itertools.combinations(range(6), 2), repeat=4):
        for (U, c), N in psets.items():
            S = frozenset(tuple(vals[i][x[i]] for i in range(4)) for x in N)
            bls = blocks_of(S)
            if bls is None or not all(len(b) == 2 for b in bls):
                f4 = False
                break
            comb = find_obstruction(bls)
            if comb is None or not verify_combination(comb):
                f4 = False
                break
        if not f4:
            break
    report["F4_all_50625_subcubes_hold"] = f4
    ok_all &= f4
    report["all_required_true"] = bool(ok_all)
    report["python"] = sys.version.split()[0]
    with open(os.path.join(HERE, "..", "evidence", "verify_lower42.json"), "w") as fh:
        json.dump(report, fh, indent=1)
    print(json.dumps({k: v for k, v in report.items() if k != "sets"}, indent=1))
    for s_ in report["sets"]:
        print(s_["U"], s_["c"], s_["F2_two_2x2_blocks_per_reshaping"], s_["F3_obstruction_verified"],
              [(o["block"], o["coefficient"]) for o in s_["F3_obstruction"]])
    sys.exit(0 if ok_all else 1)


if __name__ == "__main__":
    main()
