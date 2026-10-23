#!/usr/bin/env python3
"""probe_twisted_aut_census_v1.py (ContinueCFR21, mols39 lane; frozen before execution; stdlib only; <=280 s).
For each pinned known difference matrix (raw k x n file), compute the full group of TWISTED automorphisms
(mu, pi, tau): mu unit of Z_n, pi in S_k, tau in Z_n^k, acting by (s.c)_x = mu c_{pi^-1 x} + tau_x, that map the
column set C onto itself; tau is determined up to nothing (exact action). Search: for each (mu, pi), the image set
I = {mu c_{pi^-1 .}} must equal C + tau; tau is forced to be v0 - c for a fixed reference image v0 and some c in C.
Reports group order, the untwisted subgroup order (tau = 0), and for each element: mu, pi cycle type, tau.
Args: list of triples name path sha256 n (repeated)."""
import sys, json, hashlib, itertools, time
from math import gcd
T0 = time.monotonic()
args = sys.argv[1:]; items = [args[i:i + 4] for i in range(0, len(args), 4)]
def ctype(perm):
    k = len(perm); seen = [False] * k; t = []
    for i in range(k):
        if not seen[i]:
            L = 0; j = i
            while not seen[j]: seen[j] = True; j = perm[j]; L += 1
            t.append(L)
    return "".join(map(str, sorted(t, reverse=True)))
res = []
for name, path, want, nstr in items:
    raw = open(path, 'rb').read(); h = hashlib.sha256(raw).hexdigest()
    if h != want: print(json.dumps({"status": "INPUT_PIN_MISMATCH", "path": path, "got": h})); sys.exit(2)
    n = int(nstr); rows = [[int(t) % n for t in ln.split()] for ln in raw.decode().splitlines() if ln.strip()]
    k = len(rows); cols = [tuple(r[c] for r in rows) for c in range(n)]; C = set(cols)
    ok = all(len({(rows[i][c] - rows[j][c]) % n for c in range(n)}) == n for i in range(k) for j in range(i + 1, k))
    units = [u for u in range(1, n) if gcd(u, n) == 1]
    elems = []
    c0 = cols[0]
    for mu in units:
        for perm in itertools.permutations(range(k)):
            pinv = [0] * k
            for x in range(k): pinv[perm[x]] = x
            img = [tuple((mu * c[pinv[x]]) % n for x in range(k)) for c in cols]
            v0 = img[0]
            Iset = set(img)
            for c in cols:
                tau = tuple((v0[x] - c[x]) % n for x in range(k))
                if all(tuple((cc[x] + tau[x]) % n for x in range(k)) in Iset for cc in cols):
                    # I = C + tau  <=> the twisted map c -> img - tau maps C onto C
                    t2 = tuple((-t) % n for t in tau)
                    elems.append({"mu": mu, "pi": list(perm), "cycle_type": ctype(list(perm)), "tau": list(t2)})
    unt = [e for e in elems if not any(e["tau"])]
    res.append({"name": name, "n": n, "k": k, "dm_ok": ok, "twisted_order": len(elems), "untwisted_order": len(unt),
                "elements": elems[:200]})
print(json.dumps({"status": "OK", "results": res, "wall_s": round(time.monotonic() - T0, 3)}, sort_keys=True))
