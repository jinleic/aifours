"""Independent validation of xr1 on a small prime (default (61,4,1)), sharing no code with xr1.c.

1. Realizable class sets: every k-set {0 < ...} with distinct classes cls(d) = log_g(d) mod n
   (n = (p-1)/2, g = least primitive root). Multiplicity = number of translation classes realising it.
2. All class partitions of Z_n into t realizable sets (exact cover, bitmasks, fewest-candidates branching).
3. Cross-checks:
   - number of DFs = sum over partitions of the product of multiplicities; it must equal the independent
     C count (indep_full_cdf: 1,087,552 for (61,4,1));
   - for every canonical class set R1 (lexicographically least rotation containing 0), the number of
     partitions containing R1 must equal xr1's per-R1 "sols" (xr1 output file given as argument).
usage: python3 validate_xr1.py P K XR1_OUTPUT [OUT_JSON]
"""
import sys, itertools, json, re
from collections import Counter

p, k, xr1_out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
n, t, m = (p - 1) // 2, (p - 1) // (k * (k - 1)), k * (k - 1) // 2
def prim_root(q):
    fs = [d for d in range(2, q) if (q - 1) % d == 0 and all(d % e for e in range(2, d))]
    return next(h for h in range(2, q) if all(pow(h, (q - 1) // f, q) != 1 for f in fs))
g = prim_root(p)
L = {}; x = 1
for e in range(p - 1): L[x] = e; x = x * g % p
cls = lambda d: L[d % p] % n
mult = Counter()
for rest in itertools.combinations(range(1, p), k - 1):
    B = (0,) + rest
    cs = [cls(b - a) for a, b in itertools.combinations(B, 2)]
    if len(set(cs)) == m:
        mult[sum(1 << c for c in cs)] += 1
# each translation class with distinct classes has k representatives containing 0
assert all(v % k == 0 for v in mult.values())
mult = {S: v // k for S, v in mult.items()}
sets = list(mult)
by = {c: [S for S in sets if S >> c & 1] for c in range(n)}
FULL = (1 << n) - 1
parts = []
def xc(cov, chosen):
    if cov == FULL:
        parts.append(tuple(sorted(chosen))); return
    rem = [c for c in range(n) if not cov >> c & 1]
    best = None
    for c in rem:
        cand = [S for S in by[c] if not S & cov]
        if best is None or len(cand) < len(best[1]): best = (c, cand)
        if not cand: return
    for S in best[1]: xc(cov | S, chosen + [S])
xc(0, [])
parts = set(parts)
n_df = sum(eval("*".join(str(mult[S]) for S in P)) for P in parts)
def canonical(S):
    e = [c for c in range(n) if S >> c & 1]
    if 0 not in e: return False
    for c in e:
        r = sorted((x - c) % n for x in e)
        if r < e: return False
    return True
inc = Counter()
for P in parts:
    for S in P:
        if canonical(S): inc[S] += 1
xr = {}
for line in open(xr1_out):
    if line.startswith("R1 "):
        mk = int(re.search(r"mask=([0-9a-f]+)", line).group(1), 16)
        xr[mk] = xr.get(mk, 0) + int(re.search(r"sols=(\d+)", line).group(1))
mismatch = [(hex(S), inc.get(S, 0), xr.get(S, 0)) for S in set(inc) | set(xr) if inc.get(S, 0) != xr.get(S, 0)]
canon_sets = [S for S in sets if canonical(S)]
res = dict(p=p, k=k, g=g, n_realizable_class_sets=len(sets), n_partitions=len(parts), n_dfs=n_df,
           n_canonical_class_sets=len(canon_sets), n_r1_processed_by_xr1=len(xr),
           incidences_total=sum(inc.values()), xr1_sols_total=sum(xr.values()), mismatches=mismatch[:20],
           n_mismatch=len(mismatch))
print(json.dumps(res))
if len(sys.argv) > 4: json.dump(res, open(sys.argv[4], "w"), indent=1)
