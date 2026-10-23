# K63-TG-erratum-v1: hypothesis of Theorem K63-CLIQUE and the remark on the 3-marker

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T01:56:54-0700.
- **Overlays:** `K63-TG-v1.md`, sha256 3e6a7cf604027a60f5e0b055c5d203cc0c167e08ca59ac81c36fc3a943ebc071 (frozen, unchanged). Found by my own re-read immediately after
  freezing, before sending it to the parent.

## E1: hypothesis (statement correction)
Theorem K63-CLIQUE must assume **gcd(r_v, 6) = 1**, i.e. v != i* and v does not carry the 3-marker. Section 2 (i)
needs 3 not dividing r_v: if 9 | n_v, then gcd(n_v, T) can be 18 (tau = 9) and the granularity bound drops to 1/18.
The "Remark on the 3-marker" is **wrong and withdrawn**: in K6.3 a C-vertex may carry the 3-marker (then f_d = 1). The
corrected statement: *no K6.3 configuration has a C-vertex v with gcd(r_v, 6) = 1 and alpha_vc = alpha*_vc = 3 for all
c in C \ {v}.* In the K6.3 residue (d carries the 3-marker, f_d >= 2) every non-i* C-vertex satisfies
gcd(r_v, 6) = 1, so the conclusion about the v14 patterns is unchanged.

## E2: section 2 (iii) when f_d = 1
The sentence "All pairwise gcds among these labels equal 3, except ..." holds for f_d >= 2. If f_d = 1, then
lambda*_d = 5^(h_d) w_d alpha*_vd shares no prime with any lambda*_c = 3 r_c except the prime 2 with lambda*_(i*) when
alpha*_vd = 2 (no C-cofactor contains 5 when h_d >= 1, since the 5-marker lies on at most one vertex). By Sun(2) every
allowed S_R containing d is then contained in {d, i*}, so the conclusion of (iii) (at most three C-elements, and three
C-elements together with d only in {d, i*, x, y} with alpha*_vd = 2) holds a fortiori, and steps (iv) and (v) are
unchanged. Also, if some other C-vertex carries the 3-marker (so f_d = 1), its label 3 r_c still has gcd 3 with every
other C-label; steps (i) and (iii) are unaffected (in (i), L absorbs the extra power of 3, 3 | tau and tau <= 9 still
hold, and gcd(n_v, L tau) = 6).
