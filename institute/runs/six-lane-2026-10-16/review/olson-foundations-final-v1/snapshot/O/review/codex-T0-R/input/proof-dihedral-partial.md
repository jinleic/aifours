# Ordered EGZ in D_{2p}: proved components, dependency map, exact residual

Lane MathOlson, 2026-10-16 (PDT).  Evidence labels: **[W]** written proof;
**[R]** independently reviewed (Codex, see receipts); **[C]** computer-checked
mechanism/construction (not a proof); **[F]** finite-exact exhaustive
computation.  Nothing here proves ordered Olson for every D_{2p}: Section 6
states the exact residual class that remains OPEN in this lane.

## 0. Conventions

p odd prime; D_{2p} = {(v,e)}, (v,e)(v',e') = (v + e v', e e'); rotations
rho_x = (x,+1), reflections sigma_y = (y,-1).  w is a word of length N; an
identity 2p-subword is an increasing index set of size 2p with ordered product
(0,+1).  Existence is invariant under cyclic rotation of w and under
automorphisms (rho_v -> rho_{uv}, sigma_v -> sigma_{uv+c}, u != 0).

Gap model (F >= 1 reflections): cyclically w = X_1 f_1 X_2 f_2 ... X_F f_F,
f_t = sigma_{y_t}; X_t = block of n_t rotations before f_t ("gap t"); R = sum n_t.
Bracket product of gap t: beta_t = y_{t-1} - y_t - (sum of X_t).
Marked formulation (proof-theoremP.md, Steps 1-4): a colouring u of gaps
(u_t = 1 "Minus") with one gap fixed to 0 and marks m_r for rotations encode
every selection with an even number of reflections bijectively (reflection f_t
selected iff u_t != u_{t+1}; rotation r selected iff m_r XOR u_gap(r) = 1); the
ordered product is rho_V with V = sum_{t in Minus} beta_t + sum_{marked} x_r,
and the size is Z = #{colour changes} + #{selected rotations}.

## 1. Lemma EGZ [W, classical]
If R >= 3p-1, an identity 2p-subword exists (2p rotations with zero sum).

## 2. Theorem P [W][R][C]  (proof-theoremP.md; review/codex-theoremP/receipt.json)
If N <= 4p-1 and F + sum_t floor(n_t/2) >= 3p-1, an identity 2p-subword exists.

## 3. Doubling Lemma [W][C]
Let N = 4p-1, F >= 1.  Let 0 <= j and a cyclic stretch of 2j+1 distinct
consecutive gaps t_0, ..., t_0+2j be given; call t_0+2i (i = 0..j) P-gaps and
t_0+2i-1 (i = 1..j) M-gaps.  Suppose a set K of rotations lying in P-gaps has
|K| = p - 2j - sum_{M-gaps} n_t >= 0 and
    sum_{M-gaps} beta_t + sum_{r in K} x_r = 0 (mod p).
Then w has an identity 2p-subword.

Proof.  U := {f_{t-1}, f_t : t an M-gap} u {all rotations in M-gaps} u K.
|U| = 2j + sum n_M + |K| = p, and U is the selection with colouring "M-gaps
Minus, all other gaps Plus" and marks = K, so its product is rho_V with
V = sum_M beta_t + sum_K x = 0: U is an identity p-subword.
V-family: freeze all 2j+1 stretch gaps to Plus (one of them is the fixed gap);
free parameters are the colours of the F-2j-1 other gaps and one mark for each
rotation not in U (R - (p - 2j) marks; rotations of M-gaps all lie in U).
M = F + R - p - 1 = 3p - 2 parameters.  The V-selection never contains U's
letters (U's reflections lie between frozen gaps; U's rotations are not
parameters).  The marked value is linear and the size quadratic, so the box
Chevalley-Warning argument of Theorem P (deg Q <= 3(p-1) < M) gives a nonzero
parameter point with V-value 0 and V-size = 0 mod p; injectivity gives
V-size >= 1, and V avoids U so V-size <= 4p-1-p = 3p-1; hence V-size in {p, 2p}.
If 2p, done.  If p, the union U u V is the selection with Minus(U u V) =
Minus(V) u M-gaps (the M-gaps are isolated between frozen Plus gaps) and
marked(U u V) = marked(V) u K; by the marked formula its value is
value(V) + 0 = 0 and its size is 2p.  QED.
Special case j = 0: some gap contains p rotations with zero sum (e.g. p equal
rotations, or any gap with >= 2p-1 rotations by EGZ).

## 4. Lemma Davenport-alpha [W]
Let I be a set of pairwise non-adjacent gaps (cyclically).  Items:
(2, y_{t-1} - y_t) for t in I (empty bracket: both reflections of gap t,
rotations of gap t unselected) and (1, x_r) for every rotation r outside the
gaps of I.  Any subset of items is a valid selection (Minus = chosen bracket
gaps, all isolated) whose (size, value) is the item sum.  Items live in
Z_{2p} + Z_p, whose Davenport constant is 3p - 1 (rank-2 formula
D(Z_m + Z_n) = m + n - 1 for m | n; Olson 1969 / van Emde Boas-Kruyswijk).
If |I| + #(rotations outside I-gaps) >= 3p - 1, a nonempty item subset sums to
(0,0); its size is a positive multiple of 2p below 4p, i.e. 2p.  QED.

## 5. Theorem R (rigid words) [W][C]
If N = 4p-1, p >= 3, and every letter of w lies in {rho_x, rho_{-x}, sigma_y}
for some x != 0 and y, then w has an identity 2p-subword.

Proof.  Normalise x = 1, y = 0 by an automorphism.  If F >= 2p take 2p
reflections (sigma_0^{2p} = 1).  If F = 0 use Lemma EGZ.  If some maximal run
of rotations (a gap) contains >= p copies of rho_1 or of rho_{-1}, use the
Doubling Lemma with j = 0.  Otherwise 1 <= F <= 2p-1 and every rotation run
R_i (i = 1..k, alternating cyclically with reflection runs S_i of lengths
l_i >= 1) has net d_i = #rho_1 - #rho_{-1} with |d_i| <= p-1.
Selections: for a sign pattern z in {+-1}^k let f_i = [z_i != z_{i+1}]
(cyclic, so sum f_i is even); pick c_i reflections from S_i with c_i = f_i
(mod 2), 0 <= c_i <= l_i (the order is irrelevant since all are sigma_0), and
any rotations.  Rotations of R_i get sign z_i; reflections contribute 0.
With E+ = sum_{z_i=+} a_i + sum_{z_i=-} b_i (a_i, b_i = numbers of rho_1,
rho_{-1} in R_i), E- = R - E+, D(z) = E+ - E- = sum z_i d_i, and
delta(z) = #{i : f_i != l_i mod 2}, the reflection count C = sum c_i can be any
even number in [sum f_i, F - delta(z)].  Choosing A effectively-positive and A
effectively-negative rotations gives value 0; size 2A + C = 2p is achievable
with A <= min(E+, E-) iff |D(z)| + delta(z) <= R + F - 2p = 2p - 1 (note
sum f_i <= k <= F <= 2p-1).
Choice of z: natural flips f_i = l_i mod 2 for i < k, f_k fixed by parity, so
delta <= 1.  Let d*_i = z*_i d_i, P_j = d*_1 + ... + d*_j.  The walk P_0 = 0,
..., P_k = D* has steps of size <= p-1, so some P_j' is within (p-1)/2 of D*/2.
If j' in {0,k} then |D*| <= p-1 and z* works.  Otherwise flip the signs of R_1..
R_j' (toggle f_k and f_j'): |D| = |D* - 2P_j'| <= p-1 and delta <= 3, so
|D| + delta <= p+2 <= 2p-1 for p >= 3.  QED.
[C] code/rigid_construct.py builds the explicit selection and multiplies it out;
no failure in 20000 random rigid words for each p in {3,5,7,11,13}.
[C] The rigid feasibility reduction (|D|+delta <= 2p-1) agreed with exact DP on
6600 random rigid words (p = 3,5,7).

### 5.1 Corollary R' (rigid with few removable defects) [W]
If deleting a set Delta of at most p-3 letters leaves a rigid word and the
deletion merges no two gaps of w that contain template rotations, then w has an
identity 2p-subword: apply the proof of Theorem R to w - Delta (length
4p-1-|Delta|, bound 2p-1-|Delta| >= p+2), with the Doubling Lemma applied to w
itself for runs with >= p equal template rotations (merge-freeness keeps those
runs inside single gaps of w).

## 6. Dependency map and EXACT residual (open)

Proved: a word of length 4p-1 over D_{2p} (p >= 3) has an identity 2p-subword if
ANY of: (1) R >= 3p-1; (2) F + sum floor(n_t/2) >= 3p-1; (3) a Doubling
stretch exists; (4) Davenport-alpha items >= 3p-1; (5) w is rigid; (5')
Corollary R' applies.

Residual (NOT proved): words satisfying none of (1)-(5').  Necessary features:
R <= 3p-2 (so F >= p+1); #(even gaps) = F - #(odd gaps) <= 2p-3; no gap contains
p rotations with zero sum (so every gap has <= 2p-2 rotations); and for every
rigid template more than p-3 defects or a merging defect reflection.
Computer evidence only [C]/[F]: no counterexample for p = 3, 5 (all words) and
none in random/near-rigid sampling for p <= 13.  A complete proof needs a
row/Cauchy-Davenport lemma covering "diverse" residual words, which is not
written here.
