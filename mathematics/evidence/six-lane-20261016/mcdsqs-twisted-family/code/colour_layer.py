#!/usr/bin/env python3
"""F3.3 (README §3, frozen 04:20): T1 colouring test for a given G-invariant SQS(2p) on
F_p x Z2 (blocks file from sqs_layer_sat.py, lines "x,i x,i x,i x,i").  Relabels (x,i) as the
y in Z_{2p} with y = x (mod p), y = i (mod 2); colours the derived design at 0 invariantly
under R = <g^2> with the anchor p (README Lemma B structure, code/ppcsym.py); on SAT,
transports by G = <y+2, g*y+1> (least element rule) and writes an MCDSQS certificate, then
runs code/check_mcdsqs.py.  Writes only into a fresh OUTDIR.
Usage: colour_layer.py BLOCKS P G OUTDIR [TIMEOUT]
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def deletion_disabled(*a, **k):
    raise RuntimeError("deletion disabled in this lane")


os.remove = os.unlink = os.rmdir = os.removedirs = deletion_disabled
from mcdsqs_lib import chi_index, closure, derived, kissat, mult_perm, transport, verify_colouring, write_certificate
import ppcsym


def main():
    bfile, p, g, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    to = int(sys.argv[5]) if len(sys.argv) > 5 else 300
    rgen = int(sys.argv[6]) if len(sys.argv) > 6 else None  # colouring symmetry y -> rgen*y
    if os.path.exists(out) and os.listdir(out):
        sys.exit(f"refusing to write into non-empty {out}")
    os.makedirs(out, exist_ok=True)
    v = 2 * p
    lab = lambda x, i: x if x % 2 == i else x + p
    blocks = []
    for line in open(bfile):
        pts = [tuple(int(c) for c in tok.split(",")) for tok in line.split()]
        blocks.append(tuple(sorted(lab(x, i) for x, i in pts)))
    gens = [tuple((y + 2) % v for y in range(v)), tuple((g * y + 1) % v for y in range(v))]
    bset = set(blocks)
    assert all(tuple(sorted(s[y] for y in b)) in bset for s in gens for b in blocks), "not G-invariant"
    ncol = chi_index(v - 1)
    anchor = p
    rgen = g * g % v if rgen is None else rgen
    R = closure([mult_perm(rgen, v)], v)
    der = derived(blocks, 0)
    pts = list(range(1, v))
    deg = sum(1 for t in der if anchor in t)
    cnf, orbits, choice, cosets, stb, sizes = ppcsym.anchored(der, pts, R, anchor, ncol - deg)
    cp = os.path.join(out, "col.cnf")
    sha = cnf.write(cp)
    st, model, dt = kissat(cp, to, seed=1, log=cp + ".log")
    rec = {"p": p, "g": g, "R_generator": rgen, "R_order": len(R), "class_orbit_sizes": sizes, "col_cnf_sha256": sha,
           "col_vars": cnf.nv, "col_status": st, "col_seconds": round(dt, 3)}
    if st == "SAT":
        classes = ppcsym.decode(model, orbits, choice, cosets, stb, R)
        verify_colouring(der, pts, classes, ncol)
        rec["class_sizes_at_0"] = [len(C) for C in classes]
        G = closure(gens, v)
        col = transport(G, {0: classes}, v)
        cert = os.path.join(out, f"mcdsqs{v}_k0.txt")
        rec["certificate_sha256"] = write_certificate(
            cert, v, ncol, blocks, col, f"mcDSQS({v}) k=0 SQS, G=<y+2,{g}y+1>, R=<{rgen}>, anchor {p}")
        chk = subprocess.run([sys.executable, os.path.join(HERE, "check_mcdsqs.py"), cert], capture_output=True, text=True)
        rec["checker"] = json.loads(chk.stdout)["result"]
    json.dump(rec, open(os.path.join(out, "result.json"), "w"), indent=1)
    print(json.dumps(rec))


if __name__ == "__main__":
    main()
