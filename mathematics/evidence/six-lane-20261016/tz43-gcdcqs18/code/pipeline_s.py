#!/usr/bin/env python3
"""README A0/A1: gcDCQS(g^4 : 2) search pipeline (numpy + kissat; adapted from the gcdcqs32 lane's pipeline2.py).

Points: (i, a) -> g*i + a (i = 0..3 groups, a = 0..g-1 coordinates), stem points 4g, 4g+1.
Group G = A4 x H: A4 = <pi1 = (1 2 3), pi2 = (0 1)(2 3)> on group indices, H a group of order g acting on the
coordinates regularly (left multiplication) and diagonally on all groups; both stem points fixed.
1. Kramer–Mesner (code/cqs_km_s.py) solved by kissat (native --time), sample i with seed seed0 + i; later
   samples exclude earlier row sets.
2. Good colouring of the derived design at x = 0 (hole (G_0 ∪ S)∖{x}) by the copied colour_model.anchored
   with R = Stab_G(x) (= <pi1>), anchor h (default point 1), hole-avoiding class-orbit stabilizers from --avoid
   ('R' or '1' tokens); options --strengthen/--profile/--symbreak as in the copied model.
3. Transport to every group point y by the least e in G with e(x) = y; stem frames = orbits of the derived
   triples at each stem point under the subgroup of G fixing every group index (Lemma K: H-orbits).
4. Format S certificate; route-1 checker (and the route-2 binary if present) run on it.
All outputs exclusive-create in a new OUT directory.
Usage: pipeline_s.py OUT --g G --H NAME [--avoid SPEC] [--samples K] [--seed0 S] [--km-timeout T]
       [--col-timeout T] [--col-seed S] [--anchor P] [--strengthen] [--profile P10] [--symbreak] [--no-solve]
       [--stop-on-first] [--model-from KISSAT_LOG]
H names: C<g> (cyclic), P<a>.<b>[.<c>] (abelian mixed radix), D<k> (dihedral of order 2k), S3xC3, GD9."""
import lane_guard  # noqa: F401

import argparse
import collections
import hashlib
import itertools
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lane_guard import fresh_dir, xopen  # noqa: E402
from lanelib import closure, gcsts_params, kissat, model_satisfies, parse_status  # noqa: E402
from cqs_km_s import CQSKMS  # noqa: E402
import colour_model as cm  # noqa: E402


def coord_gens(name, g):
    """Generators (permutations of range(g)) of a regular left action of a group of order g."""
    if name.startswith("C"):
        assert int(name[1:]) == g
        return [tuple((a + 1) % g for a in range(g))]
    if name.startswith("P"):
        rad = [int(z) for z in name[1:].split(".")]
        assert eval("*".join(map(str, rad))) == g
        w = [1] * len(rad)
        for i in range(len(rad) - 2, -1, -1):
            w[i] = w[i + 1] * rad[i + 1]
        gens = []
        for i, ri in enumerate(rad):
            gens.append(tuple(a - ((a // w[i]) % ri) * w[i] + (((a // w[i]) % ri + 1) % ri) * w[i] for a in range(g)))
        return gens
    if name.startswith("D"):  # r^i s^e <-> i + k e
        k = int(name[1:])
        assert 2 * k == g
        r = tuple(((a % k + 1) % k) + k * (a // k) for a in range(g))
        s = tuple(((-(a % k)) % k) + k * (1 - a // k) for a in range(g))
        return [r, s]
    if name == "S3xC3":
        assert g == 18
        els = sorted(itertools.permutations(range(3)))
        idx = {e: i for i, e in enumerate(els)}
        lab = lambda sg, c: 3 * idx[sg] + c  # noqa: E731
        decomp = [(els[a // 3], a % 3) for a in range(18)]
        mulS = lambda p, q: tuple(p[q[t]] for t in range(3))  # noqa: E731
        gens = []
        for hs, hc in (((1, 0, 2), 0), ((1, 2, 0), 0), ((0, 1, 2), 1)):
            gens.append(tuple(lab(mulS(hs, sg), (hc + c) % 3) for sg, c in decomp))
        return gens
    if name == "GD9":  # (Z3 x Z3) x| Z2 with inversion; (u1, u2, e) <-> 9e + 3u1 + u2
        assert g == 18
        dec = [((a % 9) // 3, a % 3, a // 9) for a in range(18)]
        lab = lambda u1, u2, e: 9 * e + 3 * (u1 % 3) + (u2 % 3)  # noqa: E731
        t1 = tuple(lab(u1 + 1, u2, e) for u1, u2, e in dec)
        t2 = tuple(lab(u1, u2 + 1, e) for u1, u2, e in dec)
        sw = tuple(lab(-u1, -u2, 1 - e) for u1, u2, e in dec)
        return [t1, t2, sw]
    raise SystemExit(f"unknown H {name}")


def build_group(g, hname):
    v = 4 * g + 2
    def lift(imap, cmap):
        return tuple([g * imap[i] + cmap[a] for i in range(4) for a in range(g)] + [4 * g, 4 * g + 1])
    ident = list(range(g))
    gens = [lift({0: 0, 1: 2, 2: 3, 3: 1}, ident), lift({0: 1, 1: 0, 2: 3, 3: 2}, ident)]
    gens += [lift({i: i for i in range(4)}, h) for h in coord_gens(hname, g)]
    group_of = [i for i in range(4) for _ in range(g)] + [-1, -1]
    return v, gens, group_of


def derived(blocks, x):
    return sorted(tuple(p for p in b if p != x) for b in blocks if x in b)


def certificate_text(v, g, r, s, blocks, col, frames, header):
    L = [f"# {header}", f"GCDCQS {v} 4 {g} 2", f"COLOURS {r}", f"HOLEFREE {s}", "GROUPS"]
    L += [" ".join(str(g * i + a) for a in range(g)) for i in range(4)]
    L += ["STEM", f"{4 * g} {4 * g + 1}", "BLOCKS"]
    L += [" ".join(map(str, b)) for b in sorted(tuple(sorted(b)) for b in blocks)]
    for y in range(4 * g):
        L.append(f"POINT {y}")
        for j, C in enumerate(col[y]):
            L.append(f"CLASS {j}")
            L += [" ".join(map(str, t)) for t in C]
    for a in (4 * g, 4 * g + 1):
        L.append(f"STEMPOINT {a}")
        for k, C in frames[a]:
            L.append(f"FRAME {k}")
            L += [" ".join(map(str, t)) for t in C]
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--g", type=int, required=True)
    ap.add_argument("--H", required=True)
    ap.add_argument("--avoid", default=None, help="';'-separated tokens R or 1 (default: R then 1's)")
    ap.add_argument("--samples", type=int, default=1)
    ap.add_argument("--seed0", type=int, default=0)
    ap.add_argument("--km-timeout", type=int, default=600)
    ap.add_argument("--col-timeout", type=int, default=600)
    ap.add_argument("--col-seed", type=int, default=1)
    ap.add_argument("--anchor", type=int, default=1)
    ap.add_argument("--strengthen", action="store_true")
    ap.add_argument("--profile", default=None)
    ap.add_argument("--symbreak", action="store_true")
    ap.add_argument("--no-solve", action="store_true")
    ap.add_argument("--stop-on-first", action="store_true")
    ap.add_argument("--model-from", default=None, help="decode-only: colouring model from this kissat log")
    a = ap.parse_args()
    fresh_dir(a.out)
    prog = xopen(os.path.join(a.out, "progress.jsonl"))

    def log(rec):
        prog.write(json.dumps(rec) + "\n")
        prog.flush()
        print(json.dumps(rec), flush=True)

    g = a.g
    v, gens, group_of = build_group(g, a.H)
    r, s = gcsts_params(v - 1, g + 1)
    G = closure(gens, v)
    assert len(G) == 12 * g, f"group order {len(G)} != {12 * g}"
    x = 0
    R = [e for e in G if e[x] == x]
    ident = tuple(range(v))
    assert all(e[a.anchor] == a.anchor for e in R) and group_of[a.anchor] == 0 and a.anchor != x
    Hsub = [e for e in G if all(group_of[e[g * i]] == i for i in range(4))]
    assert len(Hsub) == g
    spec = a.avoid.split(";") if a.avoid else (["R"] + ["1"] * ((s - 1) // len(R)) if (s - 1) % len(R) == 0 else None)
    stabs = [R if t == "R" else [ident] for t in spec]
    assert sum(len(R) // len(st) for st in stabs) == s, f"avoid spec {spec} does not give {s} classes"
    t0 = time.time()
    km = CQSKMS(v, group_of, gens)
    summ = {"v": v, "g": g, "r": r, "s": s, "H": a.H, "group_order": len(G), "R_order": len(R), "anchor": a.anchor,
            "avoid": spec, "km": km.summary(), "km_build_seconds": round(time.time() - t0, 2), "args": vars(a),
            "samples": [], "certificates": []}
    log({"km": summ["km"], "km_build_seconds": summ["km_build_seconds"], "group_order": len(G), "R_order": len(R),
         "r": r, "s": s, "avoid": spec})
    cnf, rv = km.cnf()
    for i in range(a.samples):
        p = os.path.join(a.out, f"km_{i}.cnf")
        sha = cnf.write(p)
        st, model, dt = kissat(p, a.km_timeout, seed=a.seed0 + i, log=p + ".log")
        rec = {"sample": i, "km_seed": a.seed0 + i, "km_cnf_sha256": sha, "km_vars": cnf.nv,
               "km_clauses": len(cnf.clauses), "km_status": st, "km_seconds": round(dt, 3)}
        summ["samples"].append(rec)
        if st != "SAT":
            log(rec)
            break
        sel = [j for j, xx in enumerate(rv) if xx in model]
        rec["rows"] = sel
        cnf.add([-rv[j] for j in sel])
        blocks = km.blocks_of(sel)
        rec["blocks"] = len(blocks)
        rec["block_types"] = dict(collections.Counter(
            "+".join(str(c) for c in sorted(collections.Counter(group_of[q] for q in b).values(), reverse=True))
            for b in blocks))
        der = derived(blocks, x)
        hole = [q for q in range(v) if (group_of[q] == group_of[x] or group_of[q] == -1) and q != x]
        pts = [q for q in range(v) if q != x]
        rc, orbits, choice, cosets, stb, sizes = cm.anchored(der, pts, hole, R, a.anchor, stabs, strengthen=a.strengthen,
                                                             profile=a.profile, symbreak=a.symbreak)
        cp = os.path.join(a.out, f"col_{i}.cnf")
        csha = rc.write(cp)
        rec.update({"derived_triples": len(der), "triple_orbits": len(orbits), "class_orbit_sizes": sizes,
                    "col_cnf_sha256": csha, "col_vars": rc.nv, "col_clauses": len(rc.clauses)})
        log({kk: rec[kk] for kk in rec if kk != "rows"})
        if a.no_solve:
            continue
        if a.model_from:
            cst, cmodel = parse_status(open(a.model_from).read())
            assert cst == "SAT" and model_satisfies(cp, cmodel), "retained model does not satisfy the rebuilt CNF"
            cdt = 0.0
        else:
            cst, cmodel, cdt = kissat(cp, a.col_timeout, seed=a.col_seed, log=cp + ".log")
        rec["col_status"], rec["col_seconds"] = cst, round(cdt, 3)
        log({"sample": i, "col_status": cst, "col_seconds": rec["col_seconds"]})
        if cst != "SAT":
            continue
        classes = cm.decode(cmodel, orbits, choice, cosets, stb, R)
        cm.verify_good_colouring(der, pts, hole, classes, r, s)
        col = {}
        for e in G:
            y = e[x]
            if y not in col:
                col[y] = [sorted(tuple(sorted(e[q] for q in t)) for t in C) for C in classes]
        assert sorted(col) == list(range(4 * g))
        frames = {}
        for al in (4 * g, 4 * g + 1):
            dset = set(derived(blocks, al))
            fr = []
            while dset:
                t = min(dset)
                orb = {tuple(sorted(e[q] for q in t)) for e in Hsub}
                assert orb <= dset
                dset -= orb
                k = ({0, 1, 2, 3} - {group_of[q] for q in t}).pop()
                fr.append((k, sorted(orb)))
            frames[al] = sorted(fr)
        cert = os.path.join(a.out, f"gcdcqs{g}_4_2_s{i}.txt")
        text = certificate_text(v, g, r, s, blocks, col, frames,
                                f"gcDCQS({g}^4:2) candidate: G = A4 x {a.H} (order {len(G)}), R order {len(R)}, "
                                f"avoid {';'.join(spec)}, KM sample {i} (seed {a.seed0 + i}), colouring seed {a.col_seed}")
        with xopen(cert) as fh:
            fh.write(text)
        crt = {"sample": i, "certificate": cert, "sha256": hashlib.sha256(text.encode()).hexdigest()}
        chk = subprocess.run([sys.executable, os.path.join(HERE, "check_gcdcqs_s.py"), cert], capture_output=True, text=True)
        crt["route1"] = json.loads(chk.stdout)["result"]
        cbin = os.path.join(HERE, "bin", "check_gcdcqs_s_c")
        if os.path.exists(cbin):
            crt["route2"] = subprocess.run([cbin, cert], capture_output=True, text=True).stdout.strip()
        summ["certificates"].append(crt)
        log(crt)
        if a.stop_on_first and crt["route1"] == "PASS":
            break
    summ["total_seconds"] = round(time.time() - t0, 2)
    with xopen(os.path.join(a.out, "summary.json")) as fh:
        json.dump(summ, fh, indent=1)
    print("DONE", json.dumps({"certificates": summ["certificates"], "total_seconds": summ["total_seconds"]}), flush=True)


if __name__ == "__main__":
    main()
