# Erratum to v38: cut D^-|C with D_L>=4 asserted r=4 without excluding r=5 and r=6

Actual `/bin/date` before this body: **Mon Oct 26 03:05:28 PDT 2026**. InfoRecursiveMDS18-2. Additive erratum; v38 (SHA256 `b5a5b7d1646bd70039f958c46d73cb2f6f637003c3a066df1c7503bf8479c5b8`) is unchanged. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO.

## 1. What is wrong

v38 §3 (Lambda=B, cut D^-|C), case D_L>=4, says "the tail A[1,5+a] and O-row 2 give |E_L|=-a=f_0-1, so r=4". Both facts give only |E_L| = 4-r-a = f_0-1; they do not fix r. The cases r=6 and r=5 were never excluded. They are closed below; the r=4 argument of v38 is correct as written. Re-derived in the same pass and found correct: v38 §2 (both values of g) and the band lists, D_L formulas and the D_L<=-4 clauses of §§3–4. The r=4 degree argument of §4 was not re-derived here.

## 2. The missing cases

Notation of v38 §3: O-band 5, 5+a, u, 5-d, 10-d; D_L = 5-a-f_0 = r; O-row 1 = C[10,14]+v+A[5+a,9+a] (A^-'s first five from v3); O-row 2 = A[1,5+a]+v+Lambda[1,5-a] with the pure-K' O-tail A[1,5+a] = K' minus (E_L+k_1); O-row 4 = (Lambda's last 5-d = q_2+E_R)+v+C[10-d,14]; the pure-K' P-tail is A's last g = f_0+d+a vertices = K' minus (E_R+k_2), so g = k-1-|E_R|; P-row at D|A = D[10-f_0,9+d]+v+A[1,10-f_0-d].

- r=6 (k=4): q=6 rigidity gives |E_L| = -2-a in {0,3}, so a=-2 and f_0=1; g = 3-|E_R| in {0,3} with g>=1 gives g=3, |E_R|=0, d=4. A = A[1,7] with the designated K' paths A[1,3] and A[5,7], so K4(K') is exhausted. O-row 1 contains A[3], A[5,7], i.e. all four K', so C[10,14] is all Q; O-row 4 = Lambda[L-1]+v+C[6,14] = O minus {q_2} then needs four consecutive K' in C[6,9]. Impossible.
- r=5 (k=5): a+f_0 = 0, |E_L| = -1-a, g = d, |E_R| = 4-d. The Lemma (2+c_0+c_L<=5) leaves a=-1 (E_L empty) or d=4 (E_R empty).
  - d=4, a<=-2: in O-row 1 the P-tail A[6+a,9+a] (K' minus {k_2}) and A[5+a] (end of the O-tail, hence k_2) are all five K', so C[10,14] is all Q, while O-row 4 = q_2+v+C[6,14] = O minus {q_2} has only four Q. Impossible.
  - a=-1 (f_0=1, A interior 8, O-tail A[1,4] = K' minus {k_1}, P-tail A[9-d,8]): the P-row at D|A = D[9,9+d]+v+A[1,9-d] contains A[1,4] and A[9-d], whose label lies outside A[1,4] and so is k_1; all five K' are there, so A[5,8-d] and D[9,9+d] are all Q. These give at least three adjacent Q pairs off the two Q-paths (3-d+d for d<=3, four for d=4), against the two allowed by (Q5). Impossible.

So the case D_L>=4 forces r=4, and v38's conclusion for the cut D^-|C stands; the v38 Result is unchanged.

All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged.
