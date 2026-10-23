#!/usr/bin/env python3
"""mutations_general.py -- deliberate-corruption controls for pc_check.py and pc_expand_general.py (README 1.6).

Given a PASS certificate and its PC-SEED, writes mutated copies to OUTDIR (a fresh directory; it must not exist), runs
pc_check.py on each certificate mutation and pc_expand_general.py on each seed mutation, and compares the outcome with
the intended one. Semantic mutations are re-canonicalized (points sorted in blocks, lines sorted) so that they fail
for the intended semantic reason and not for format. Affine relabelings x -> u x + c (u a unit mod v) must PASS.
A non-affine relabeling must fail the +1 test (C1). The class-permutation test (C2) is exercised on the synthetic
K_6 one-factorizations (k = 2) as in the v = 100 lane. Deterministic (random.Random(20261017)). Nothing is deleted.
Usage: mutations_general.py CERT SEED OUTDIR
"""
import json
import math
import os
import random
import subprocess
import sys

CODE = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable


def load(path):
    lines = open(path).read().rstrip("\n").split("\n")
    rows = [tuple(map(int, l.split())) for l in lines[1:]]
    return lines[0], [(r[0], tuple(r[1:])) for r in rows]


def dump(head, rows):
    rows = sorted((c, tuple(sorted(B))) for c, B in rows)
    return (head + "\n" + "\n".join(f"{c} " + " ".join(map(str, B)) for c, B in rows) + "\n").encode()


def relabel_rows(rows, f):
    classes = {}
    for c, B in rows:
        classes.setdefault(c, []).append(tuple(sorted(f(x) for x in B)))
    order = sorted(sorted(P) for P in classes.values())
    return [(k, B) for k, P in enumerate(order) for B in P]


def check(path):
    p = subprocess.run([PY, os.path.join(CODE, "pc_check.py"), path], capture_output=True, text=True)
    return p.returncode, p.stdout.strip().split("\n")[-1]


def main(argv):
    if len(argv) != 4:
        print(__doc__, file=sys.stderr)
        return 2
    cert, seed, out = argv[1], argv[2], argv[3]
    os.makedirs(out)
    rnd = random.Random(20261017)
    head, rows = load(cert)
    v, ncl = int(head.split()[1]), int(head.split()[3])
    raw = open(cert, "rb").read()
    bset = {B for _, B in rows}
    cases = []
    # 1. one point changed (to a block not already present): pair coverage
    i = rnd.randrange(len(rows))
    c, B = rows[i]
    for y in range(v):
        if y not in B and tuple(sorted(B[1:] + (y,))) not in bset:
            nb = tuple(sorted(B[1:] + (y,)))
            break
    m = list(rows); m[i] = (c, nb)
    cases.append(("point_changed", dump(head, m), "FAIL D2"))
    # 2. two points swapped between blocks of different classes
    while True:
        i, j = rnd.randrange(len(rows)), rnd.randrange(len(rows))
        (c1, B1), (c2, B2) = rows[i], rows[j]
        if c1 != c2 and B1[0] not in B2 and B2[0] not in B1:
            break
    m = list(rows)
    m[i] = (c1, tuple(sorted(B1[1:] + (B2[0],))))
    m[j] = (c2, tuple(sorted(B2[1:] + (B1[0],))))
    cases.append(("points_swapped_between_classes", dump(head, m), "FAIL D2"))
    # 3. one block moved to another class
    i = rnd.randrange(len(rows)); c, B = rows[i]
    m = list(rows); m[i] = ((c + 1) % ncl, B)
    cases.append(("block_moved_to_other_class", dump(head, m), "FAIL R1"))
    # 4. one block replaced by a copy of a block of another class
    while True:
        i, j = rnd.randrange(len(rows)), rnd.randrange(len(rows))
        if rows[i][0] != rows[j][0]:
            break
    m = list(rows); m[j] = (rows[j][0], rows[i][1])
    cases.append(("block_duplicated", dump(head, m), "FAIL D1"))
    # 5. non-affine random relabeling: design and resolution stay valid, the +1 test must fail
    perm = list(range(v)); rnd.shuffle(perm)
    affine = any(all(perm[x] == (u * x + perm[0]) % v for x in range(v)) for u in range(v))
    cases.append(("random_nonaffine_relabel" + ("_AFFINE?" if affine else ""),
                  dump(head, relabel_rows(rows, lambda x: perm[x])), "FAIL C1"))
    # 6-8. affine relabelings must PASS
    units = [u for u in range(2, v) if math.gcd(u, v) == 1]
    u3 = 3 if 3 in units else units[0]
    for name, u, c0 in ((f"affine_{u3}x+7", u3, 7), ("translate_x+1", 1, 1), ("negate_-x", v - 1, 0)):
        cases.append((name, dump(head, relabel_rows(rows, lambda x, u=u, c0=c0: (u * x + c0) % v)), "PASS"))
    # 9-15. format corruptions
    lines = raw.decode().split("\n")
    cases.append(("no_final_newline", raw[:-1], "FAIL F"))
    l2 = list(lines); l2[5] = l2[5] + " "
    cases.append(("trailing_space", "\n".join(l2).encode(), "FAIL F"))
    l2 = list(lines); tok = l2[3].split(); tok[1] = "0" + tok[1]; l2[3] = " ".join(tok)
    cases.append(("leading_zero", "\n".join(l2).encode(), "FAIL F"))
    l2 = list(lines); tok = l2[7].split(); tok[1], tok[2] = tok[2], tok[1]; l2[7] = " ".join(tok)
    cases.append(("points_not_ascending", "\n".join(l2).encode(), "FAIL F"))
    l2 = list(lines); l2[1], l2[-2] = l2[-2], l2[1]
    cases.append(("lines_out_of_order", "\n".join(l2).encode(), "FAIL F"))
    l2 = list(lines); del l2[-2]
    cases.append(("truncated_last_block", "\n".join(l2).encode(), "FAIL F"))
    l2 = list(lines); h = l2[0].split(); h[3] = str(int(h[3]) + 1); l2[0] = " ".join(h)
    cases.append(("header_nclasses_plus1", "\n".join(l2).encode(), "FAIL F"))
    # 16-17. the C2 code path on K_6 one-factorizations (k = 2)
    k6_cyc = [[(0, 1), (2, 3), (4, 5)], [(0, 2), (1, 4), (3, 5)], [(0, 3), (1, 5), (2, 4)],
              [(0, 4), (1, 3), (2, 5)], [(0, 5), (1, 2), (3, 4)]]
    k6_non = [[(0, 1), (2, 3), (4, 5)], [(0, 2), (1, 5), (3, 4)], [(0, 3), (1, 4), (2, 5)],
              [(0, 4), (1, 2), (3, 5)], [(0, 5), (1, 3), (2, 4)]]
    for name, F, want in (("k2_v6_cyclic_onefactorization", k6_cyc, "PASS"),
                          ("k2_v6_noncyclic_onefactorization", k6_non, "FAIL C2")):
        body = [(c, B) for c, P in enumerate(sorted(F)) for B in sorted(P)]
        cases.append((name, dump("POINT-CYCLIC-RESOLUTION 6 2 5 3", body), want))
    results, ok = [], True
    for name, data, want in cases:
        path = os.path.join(out, name + ".cert")
        with open(path, "xb") as f:
            f.write(data)
        rc, verdict = check(path)
        good = verdict.startswith(want) and ((rc == 0) == (want == "PASS"))
        ok &= good
        results.append({"case": name, "expected": want, "got": verdict, "rc": rc, "as_intended": good})
        print(f"{'ok ' if good else 'BAD'} {name}: expected {want!r}, got {verdict!r}")
    # seed mutations: pc_expand_general.py must refuse
    sl = open(seed).read().rstrip("\n").split("\n")
    blk_idx = [k for k, l in enumerate(sl) if l.startswith(("X ", "Y "))]
    smuts = []
    k0 = blk_idx[0]
    t0 = sl[k0].split(" ")
    pts = sorted(set(int(x) for x in t0[1:]))
    newp = (pts[0] + 1) % v
    while newp in pts:
        newp = (newp + 1) % v
    pts2 = sorted(pts[1:] + [newp])
    smuts.append(("seed_point_changed", "\n".join(sl[:k0] + [t0[0] + " " + " ".join(map(str, pts2))] + sl[k0 + 1:]) + "\n",
                  "SEED-FAIL"))
    smuts.append(("seed_drop_last_line", "\n".join(sl[:-1]) + "\n", "SEED-FAIL"))
    tshort = sl[1].split(" ")
    smuts.append(("seed_short_t_changed", "\n".join(sl[:1] + ["SHORT " + str(int(tshort[1]) + 4)] + sl[2:]) + "\n",
                  "SEED-FAIL"))
    for name, text, want in smuts:
        path = os.path.join(out, name + ".seed")
        with open(path, "x") as f:
            f.write(text)
        target = path + ".cert"
        p = subprocess.run([PY, os.path.join(CODE, "pc_expand_general.py"), path, target],
                           capture_output=True, text=True)
        got = p.stdout.strip()
        good = p.returncode != 0 and want in got and not os.path.exists(target)
        ok &= good
        results.append({"case": name, "expected": f"expander refuses ({want})", "got": got, "rc": p.returncode,
                        "as_intended": good})
        print(f"{'ok ' if good else 'BAD'} {name}: expander rc={p.returncode} {got!r}")
    with open(os.path.join(out, "mutations-report.json"), "x") as f:
        json.dump({"certificate": cert, "seed": seed, "results": results, "all_as_intended": ok}, f, indent=1)
        f.write("\n")
    print("MUTATIONS", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
