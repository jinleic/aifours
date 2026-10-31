#!/usr/bin/env python3
"""Exact algebraic witness checks (reviewer-written) for the sharpness examples:
 (a) (1/2)[[s2,s2,0],[1,-1,s2],[1,-1,-s2]] has exactly 8 nonzeros and orthonormal rows, in Q(sqrt2)
     represented as pairs (a,b) = a + b*sqrt2 with rational a,b (Fraction).
 (b) 3x3 Fourier matrix (1/sqrt3) [w^{jk}] is unitary: exact in Z[w], w^2 = -1 - w, conj(w) = w^2.
 (c) negative: the 3x3 pattern with exactly 7 nonzeros (two zeros in distinct rows/cols) forces a
     one-term row inner product; exact symbolic statement is checked numerically only as a sanity run
     over random fillings (necessarily nonzero inner product). """
from fractions import Fraction as F
import itertools, json, hashlib, random, subprocess, sys
def clock(): return subprocess.run(["/bin/date","-u","+%Y-%m-%dT%H:%M:%SZ"],capture_output=True,text=True).stdout.strip()
c0 = clock()
# (a) Q(sqrt2)
def mul(x,y): return (x[0]*y[0]+2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def add(x,y): return (x[0]+y[0], x[1]+y[1])
h = F(1,2); s2 = (F(0), F(1)); one = (F(1),F(0)); zero=(F(0),F(0))
def sc(x,c): return (x[0]*c, x[1]*c)
M = [[sc(s2,h), sc(s2,h), zero],[sc(one,h), sc(one,-h), sc(s2,h)],[sc(one,h), sc(one,-h), sc(s2,-h)]]
gram = [[zero]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        acc = zero
        for k in range(3): acc = add(acc, mul(M[i][k], M[j][k]))   # real entries: no conjugation
        gram[i][j] = acc
a_ok = all(gram[i][j] == (one if i==j else zero) for i in range(3) for j in range(3))
a_nnz = sum(1 for i in range(3) for j in range(3) if M[i][j] != zero)
# (b) Z[w] : elements a + b w, w^2 = -1 - w ; conj(a + b w) = a + b w^2 = (a - b) - b w
def wm(x,y):
    a,b = x; c,d = y
    return (a*c - b*d, a*d + b*c - b*d)
def wconj(x): a,b = x; return (a-b, -b)
def wpow(k):
    r = (1,0)
    for _ in range(k % 3): r = wm(r,(0,1))
    return r
Fm = [[wpow(j*k) for k in range(3)] for j in range(3)]
b_ok = True
for i in range(3):
    for j in range(3):
        acc = (0,0)
        for k in range(3):
            p = wm(Fm[i][k], wconj(Fm[j][k])); acc = (acc[0]+p[0], acc[1]+p[1])
        b_ok &= (acc == ((3,0) if i==j else (0,0)))   # (1/sqrt3)^2 normalisation gives identity
# (c) sanity: 3x3 with 7 nonzeros, zeros at (0,0) and (1,1): rows 0 and 1 overlap only in column 2
random.seed(1); c_min = 1.0
for _ in range(2000):
    r0 = [0, complex(random.gauss(0,1),random.gauss(0,1)), complex(random.gauss(0,1),random.gauss(0,1))]
    r1 = [complex(random.gauss(0,1),random.gauss(0,1)), 0, complex(random.gauss(0,1),random.gauss(0,1))]
    ip = sum(a*b.conjugate() for a,b in zip(r0,r1))
    c_min = min(c_min, abs(ip)/ (abs(r0[2])*abs(r1[2])))
c1 = clock()
rec = {"script_sha256": hashlib.sha256(open(__file__,"rb").read()).hexdigest(), "clock_start_utc": c0, "clock_end_utc": c1,
       "a_3x3_eight_nonzero_orthogonal_exact": {"orthonormal_rows": a_ok, "nnz": a_nnz},
       "b_3x3_fourier_unitary_exact_Zw": b_ok,
       "c_7nnz_pattern_single_term_overlap_ratio_min": c_min, "c_note": "ratio |<r0,r1>|/(|r0[2]||r1[2]|) is identically 1: a single-term inner product cannot vanish"}
print(json.dumps(rec, indent=1))
json.dump(rec, open(__file__.replace(".py","-receipt.json"),"w"), indent=1)
