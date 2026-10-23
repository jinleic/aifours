#!/usr/bin/env python3
"""mutations.py -- deliberate-corruption controls for pc_check.py and pc_expand.py (README 1.5).

Given a PASS certificate (and its seed), writes mutated copies to OUTDIR, runs pc_check.py on each and compares the
first failing check with the intended one. Semantic mutations are re-canonicalized (blocks sorted, lines sorted) so
that they fail for the intended semantic reason and not for format. Positive invariance controls (affine
relabelings) must PASS. Seed mutations must be refused by pc_expand.py. Deterministic (random.Random(20261017)).
Usage: mutations.py CERT SEED OUTDIR
"""
import json
import os
import random
import subprocess
import sys

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable


def load(path):
    lines = open(path).read().rstrip("\n").split("\n")
    head = lines[0]
    rows = [tuple(map(int, l.split())) for l in lines[1:]]
    return head, [(r[0], tuple(r[1:])) for r in rows]


def dump(head, rows, canon=True):
    if canon:
        rows = sorted((c, tuple(sorted(B))) for c, B in rows)
    return (head + "\n" + "\n".join(f"{c} " + " ".join(map(str, B)) for c, B in rows) + "\n").encode()


def check(path):
    p = subprocess.run([PY, os.path.join(LANE, "code", "pc_check.py"), path], capture_output=True, text=True)
    return p.returncode, p.stdout.strip().split("\n")[-1]


def main(argv):
    cert, seed, out = argv[1], argv[2], argv[3]
    os.makedirs(out, exist_ok=True)
    rnd = random.Random(20261017)
    head, rows = load(cert)
    v = int(head.split()[1])
    raw = open(cert, "rb").read()
    bset = {B for _, B in rows}
    cases = []

    # 1. one point changed (new block not already present): pair coverage
    i = rnd.randrange(len(rows))
    c, B = rows[i]
    for y in range(v):
        if y not in B:
            nb = tuple(sorted(B[1:] + (y,)))
            if nb not in bset:
                break
    m = list(rows); m[i] = (c, nb)
    cases.append(("point_changed", dump(head, m), "FAIL D2"))
    # 2. two points swapped between blocks of different classes
    while True:
        i, j = rnd.randrange(len(rows)), rnd.randrange(len(rows))
        (c1, B1), (c2, B2) = rows[i], rows[j]
        x, y = B1[0], B2[0]
        if c1 != c2 and x not in B2 and y not in B1:
            break
    m = list(rows); m[i] = (c1, tuple(sorted(B1[1:] + (y,)))); m[j] = (c2, tuple(sorted(B2[1:] + (x,))))
    cases.append(("points_swapped_between_classes", dump(head, m), "FAIL D2"))
    # 3. one block moved to another class
    i = rnd.randrange(len(rows)); c, B = rows[i]
    m = list(rows); m[i] = ((c + 1) % int(head.split()[3]), B)
    cases.append(("block_moved_to_other_class", dump(head, m), "FAIL R1"))
    # 4. one block replaced by a copy of a block of another class
    while True:
        i, j = rnd.randrange(len(rows)), rnd.randrange(len(rows))
        if rows[i][0] != rows[j][0]:
            break
    m = list(rows); m[j] = (rows[j][0], rows[i][1])
    cases.append(("block_duplicated", dump(head, m), "FAIL D1"))
    # 5. non-affine random relabeling: design and resolution stay valid, +1 invariance must fail
    perm = list(range(v)); rnd.shuffle(perm)
    affine = any(all(perm[x] == (u * x + perm[0]) % v for x in range(v)) for u in range(v))
    m = [(c, tuple(sorted(perm[x] for x in B))) for c, B in rows]
    # class indices must follow the sorted order of the relabeled classes for strict format
    classes = {}
    for c, B in m:
        classes.setdefault(c, []).append(B)
    order = sorted(sorted(P) for P in classes.values())
    m = [(k, B) for k, P in enumerate(order) for B in P]
    cases.append(("random_nonaffine_relabel" + ("_AFFINE?" if affine else ""), dump(head, m), "FAIL C1"))
    # 6-8. affine relabelings must PASS
    for name, u, t in (("affine_3x+7", 3, 7), ("translate_x+1", 1, 1), ("negate_-x", v - 1, 0)):
        m = [(c, tuple(sorted((u * x + t) % v for x in B))) for c, B in rows]
        classes = {}
        for c, B in m:
            classes.setdefault(c, []).append(B)
        order = sorted(sorted(P) for P in classes.values())
        m = [(k, B) for k, P in enumerate(order) for B in P]
        cases.append((name, dump(head, m), "PASS"))
    # 9. class trade: two disjoint blocks of class P and two of class P' with the same union are exchanged;
    #    design, partitions and block set unchanged, so only C2 (classes mapped to classes) can fail
    byc = {}
    for c, B in rows:
        byc.setdefault(c, []).append(B)
    seen = {}
    trade = None
    for c in sorted(byc):
        P = byc[c]
        for a in range(len(P)):
            for b in range(a + 1, len(P)):
                key = frozenset(P[a]) | frozenset(P[b])
                if key in seen and seen[key][0] != c:
                    trade = (seen[key], (c, P[a], P[b]))
                    break
                seen.setdefault(key, (c, P[a], P[b]))
            if trade:
                break
        if trade:
            break
    if trade:
        (c1, A1, A2), (c2, B1, B2) = trade
        m = []
        for c, B in rows:
            if c == c1 and B in (A1, A2):
                m.append((c2, B))
            elif c == c2 and B in (B1, B2):
                m.append((c1, B))
            else:
                m.append((c, B))
        cases.append(("class_trade_2x2", dump(head, m), "FAIL C2"))
    # 10-15. format corruptions
    lines = raw.decode().split("\n")
    cases.append(("no_final_newline", raw[:-1], "FAIL F"))
    l2 = list(lines); l2[5] = l2[5] + " "
    cases.append(("trailing_space", "\n".join(l2).encode(), "FAIL F"))
    l2 = list(lines); tok = l2[3].split(); tok[1] = "0" + tok[1]
    l2[3] = " ".join(tok)
    cases.append(("leading_zero", "\n".join(l2).encode(), "FAIL F"))
    l2 = list(lines); tok = l2[7].split(); tok[1], tok[2] = tok[2], tok[1]; l2[7] = " ".join(tok)
    cases.append(("points_not_ascending", "\n".join(l2).encode(), "FAIL F"))
    l2 = list(lines); l2[1], l2[-2] = l2[-2], l2[1]
    cases.append(("lines_out_of_order", "\n".join(l2).encode(), "FAIL F"))
    l2 = list(lines); del l2[-2]
    cases.append(("truncated_last_block", "\n".join(l2).encode(), "FAIL F"))
    l2 = list(lines); h = l2[0].split(); h[3] = str(int(h[3]) + 1); l2[0] = " ".join(h)
    cases.append(("header_nclasses_plus1", "\n".join(l2).encode(), "FAIL F"))
    # 16-17. C2 code path on a synthetic k = 2 case (the 2-(6,2,1) design K_6, whose edge set is +1 invariant).
    #    No 2- or 3-class re-partition of the v = 100 certificate exists (searched in the lane log), so the
    #    "classes not mapped to classes while the block set is invariant" case is exercised on the one-factorizations
    #    of K_6: of its 6 labeled one-factorizations exactly one is +1 invariant (exhaustive, lane log).
    k6_cyc = [[(0, 1), (2, 3), (4, 5)], [(0, 2), (1, 4), (3, 5)], [(0, 3), (1, 5), (2, 4)],
              [(0, 4), (1, 3), (2, 5)], [(0, 5), (1, 2), (3, 4)]]
    k6_non = [[(0, 1), (2, 3), (4, 5)], [(0, 2), (1, 5), (3, 4)], [(0, 3), (1, 4), (2, 5)],
              [(0, 4), (1, 2), (3, 5)], [(0, 5), (1, 3), (2, 4)]]
    for name, F, want in (("k2_v6_cyclic_onefactorization", k6_cyc, "PASS"),
                          ("k2_v6_noncyclic_onefactorization", k6_non, "FAIL C2")):
        body = [(c, B) for c, P in enumerate(sorted(F)) for B in sorted(P)]
        cases.append((name, dump("POINT-CYCLIC-RESOLUTION 6 2 5 3", body), want))

    results = []
    ok = True
    for name, data, want in cases:
        path = os.path.join(out, name + ".cert")
        with open(path, "wb") as f:
            f.write(data)
        rc, verdict = check(path)
        good = verdict.startswith(want) and ((rc == 0) == (want == "PASS"))
        ok &= good
        results.append({"case": name, "expected": want, "got": verdict, "rc": rc, "as_intended": good})
        print(f"{'ok ' if good else 'BAD'} {name}: expected {want!r}, got {verdict!r}")
    # seed mutations: pc_expand.py must refuse
    sl = open(seed).read().rstrip("\n").split("\n")
    smuts = []
    t = sl[2].split(); t[1] = str((int(t[1]) + v // 4) % v); t[1:] = map(str, sorted(map(int, t[1:])))
    smuts.append(("seed_X_point_plus_q", "\n".join(sl[:2] + [" ".join(t)] + sl[3:]) + "\n", "(S1)"))
    t = sl[-1].split(); t[1] = str((int(t[1]) + 1) % v); t[1:] = map(str, sorted(map(int, t[1:])))
    smuts.append(("seed_Y_point_plus_1", "\n".join(sl[:-1] + [" ".join(t)]) + "\n", "SEED-FAIL"))
    smuts.append(("seed_drop_Y_line", "\n".join(sl[:-1]) + "\n", "SEED-FAIL expected"))
    for name, text, want in smuts:
        path = os.path.join(out, name + ".seed")
        with open(path, "w") as f:
            f.write(text)
        p = subprocess.run([PY, os.path.join(LANE, "code", "pc_expand.py"), path, path + ".cert"],
                           capture_output=True, text=True)
        got = p.stdout.strip()
        good = p.returncode != 0 and want in got and not os.path.exists(path + ".cert")
        ok &= good
        results.append({"case": name, "expected": f"expander refuses ({want})", "got": got, "rc": p.returncode,
                        "as_intended": good})
        print(f"{'ok ' if good else 'BAD'} {name}: expander rc={p.returncode} {got!r}")
    with open(os.path.join(out, "mutations-report.json"), "w") as f:
        json.dump({"certificate": cert, "seed": seed, "class_trade_found": bool(trade), "results": results,
                   "all_as_intended": ok}, f, indent=1)
        f.write("\n")
    print("MUTATIONS", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
