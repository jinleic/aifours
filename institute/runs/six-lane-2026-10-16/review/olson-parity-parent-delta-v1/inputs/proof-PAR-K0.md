# PAR in the regime kappa = 0 (all primes p >= 5), and the block-chain certificate

Lane `olson`, owner OlsonParity.  Written after host clock 2026-10-17T03:56:13-07:00.
Status: written proof [W], not yet hostile-reviewed.  Depends only on Lemma WAS
(../repr-WAS.md, reviewed) through the half-window form frozen in README.md Sec. 1.

## 1. Notation and the half-window lemma

RGR word of length N = 4p-2, x = 1, cyclic runs R_1 S_1 ... R_k S_k (S_j between R_j
and R_{j+1}); a_t, b_t, r_t = a_t + b_t, d_t = a_t - b_t; l_j; A, B, R = A + B, F, D = A - B;
o_F, o_R odd reflection / rotation runs, e_F = k - o_F, e_R = k - o_R; H = (F - o_F)/2;
kappa := p - 1 - H = (R + o_F - 2p)/2 (an integer: F + R even, F = o_F mod 2).
For a set Q of rotation runs ("pattern"; proper means Q != empty, [k]): u_Q :=
2^{-1} sum_{t in Q} theta_t in Z_p (theta_t = y_{t-1} - y_t), additive, u_{[k]} = 0;
D_Q = sum_Q d_t; m(Q) = number of maximal cyclic blocks of Q; the 2m(Q) reflection runs
S_j with exactly one of R_j, R_{j+1} in Q are the boundary runs of Q, beta(Q) of them even.

**Lemma H (half windows).**  For every proper pattern Q put
  lambda(Q) := min( p - m(Q) + 1,  D_Q + B - kappa + m(Q) - beta(Q),  floor((D_Q + B)/2) + 1 ),
  I(Q) := [1 - lambda(Q^c), lambda(Q) - 1]  (an integer interval, possibly empty).
Then the word has no identity 2p-subword iff u_Q notin I(Q) (mod p) for every proper Q
and 0 notin I(empty) (mod p), where I(empty) := [-min(p, A - kappa - 1, floor(A/2)),
min(p, B - kappa - 1, floor(B/2))].  If A, B <= 2p - 1, the last condition is equivalent to
min(A, B) <= kappa.  [Correction 2026-10-17T07:39 PDT, after the Codex review
review/olson-kbh-codex-review-v1.note.md: the earlier statement replaced the empty/full
condition by min(A, B) <= kappa without the bound A, B <= 2p - 1, which is false, e.g.
p = 5, w = rho_1^10 sigma_0^8 (k = 1, H = 4, kappa = B = 0, no proper patterns) satisfies it
but rho_1^10 = 1.]  Every avoider has A, B <= 2p - 1 (2p letters rho_1, resp. rho_{-1}, form
an identity 2p-subword), so for avoiders the zero condition min(A, B) <= kappa is necessary;
Lemma OR (proof-PAR-Kplus-partial.md Sec. 1) and Lemma M0 do not increase A or B, so the bound
persists under those reductions.  All uses in this directory are of this necessary direction.
Proof.  Lemma WAS: avoid iff 2u_P notin Ach(z_P) (mod p) for every P subset [k]
(z_i = +1 iff i in P), Ach(z) = the even integers in [lo, hi] (../proof-GR.md Sec. 2).
Since 2 is invertible mod p this is u_P notin Z cap [lo/2, hi/2]; with c = C_max/2,
hi/2 rounded down is min(p - Phi/2, E+ + c - p, floor(E+/2)) and lo/2 rounded up is
-min(p - Phi/2, E- + c - p, floor(E-/2)) (C_max and Phi are even).  For a proper P with
Phi = 2m boundaries, beta of them even: delta = beta + (o_F - (2m - beta)), so
c = H + m - beta = p - 1 - kappa + m - beta; E+ = A_P + B_{P^c} = D_P + B; P^c has the
same boundaries and E+(P^c) = E-(P).  This gives hi/2 = lambda(P) - 1 and
lo/2 = 1 - lambda(P^c).  For P = empty (z = -1, Phi = 0, c = H, E+ = B, E- = A) the
half window is I(empty) as displayed (P = [k] gives its negative).  Its end points lie in
[-p, p]; the end -p (resp. p) occurs only if floor(A/2) >= p, i.e. A >= 2p (resp. B >= 2p).
So for A, B <= 2p - 1 the only multiple of p it can contain is 0, which it contains iff
A, B >= kappa + 1.  []
(Machine check of this algebra against ../code/gr_window.py `ach`: notes-checkpoint.md,
258,094 random cases, 0 mismatches.)

Normalisation.  The automorphism rho_v -> rho_{-v}, sigma_v -> sigma_{-v} preserves
avoidance, RGR, the run structure and all inherited conditions, and swaps A, B; so we may
assume B <= A.  Then an avoider has B <= kappa ("zero condition").

Inherited conditions in these parameters (F = 4p - 2 - R): (Pairs) H <= p-1 <=> kappa >= 0;
(V) R + H <= 3p-2 <=> kappa <= o_F - 1; (P) F + sum floor(r_t/2) <= 3p-2 <=> R + o_R >= 2p.

## 2. Block-chain lemma (value-independent certificate; no winding hypothesis)

**Lemma BC.**  Let w be an avoider (RGR, length 4p-2, F, R >= 1).  Let (P_1, ..., P_s),
s >= 2, be an ordered partition of [k] into nonempty proper patterns, Q_t := P_1 u ... u P_t.
Suppose
 (a) lambda(P_1) + ... + lambda(P_s) >= p + 1;
 (b) for 2 <= t <= s-1, with X = Q_{t-1}, Y = P_t, Z = Q_t^c:
     lambda(X u Y) + lambda(Y u Z) + lambda(Z u X) >= p + 1   and
     lambda(X) + lambda(Y) + lambda(Z) >= 1;
 (c) lambda(P_s) + lambda(P_s^c) >= 1.
Then w has an identity 2p-subword (contradiction).

Proof.  As w avoids, for every proper Q the residue u_Q is not that of any element of
I(Q); in particular |I(Q)| <= p - 1, i.e. lambda(Q) + lambda(Q^c) <= p.
Claim: if y is an integer, y = u_Q (mod p) and 1 - lambda(Q^c) <= y <= p + lambda(Q) - 1,
then lambda(Q) <= y <= p - lambda(Q^c).  Indeed, write l = lambda(Q), l' = lambda(Q^c); the
integers [1 - l', l - 1] and [p + 1 - l', p + l - 1] are congruent to elements of I(Q), so y
avoids them; as l + l' <= p, the three ranges [1 - l', l - 1], [l, p - l'],
[p + 1 - l', p + l - 1] tile [1 - l', p + l - 1] in this order (when l + l' <= 1 the outer
ranges are empty and [1 - l', p + l - 1] is contained in [l, p - l']).
For each t choose an integer v_t = u_{P_t} (mod p) in [lambda(P_t), p - lambda(P_t^c)]
(possible: if l + l' >= 1 the interval [1 - l', p + l - 1] has >= p integers and contains a
representative, which lies in [l, p - l'] by the claim; if l + l' <= 0 the interval
[l, p - l'] itself has >= p + 1 integers).  Put V_t = v_1 + ... + v_t = u_{Q_t} (mod p).
Induction: V_t in [lambda(Q_t), p - lambda(Q_t^c)] for 1 <= t <= s-1.  For t = 1 this is
the choice of v_1.  For 2 <= t <= s-1, V_t = V_{t-1} + v_t lies in
[lambda(Q_{t-1}) + lambda(P_t), 2p - lambda(Q_{t-1}^c) - lambda(P_t^c)], and with
X, Y, Z as in (b) (Q_{t-1}^c = Y u Z, P_t^c = Z u X, Q_t = X u Y, Q_t^c = Z) condition (b)
says exactly that this range lies in [1 - lambda(Q_t^c), p + lambda(Q_t) - 1]; the claim
gives the induction step.  Finally V_s = u_{[k]} = 0 (mod p), V_s = sum v_t >= sum
lambda(P_t) >= p + 1 by (a), and V_s = V_{s-1} + v_s <= (p - lambda(P_s)) +
(p - lambda(P_s^c)) <= 2p - 1 by (c) (Q_{s-1}^c = P_s).  No multiple of p lies in
[p + 1, 2p - 1].  []

Remarks.  s = 2 is the full-window certificate (|I(P_1)| >= p).  s = 3 is the
"Cauchy-Davenport" certificate: (a) plus the first inequality of (b).

## 3. Theorem K0

**Theorem K0.**  Let p >= 5 be prime and w in RGR_{4p-2}(p) with F, R >= 1, k <= p,
satisfying (P) and (V).  If kappa(w) = 0 and w has an even run, then w has an identity
2p-subword.  In particular PAR(p) holds for every inherited avoider with kappa = 0.

Proof.  Suppose w avoids.  Normalise B <= A; the zero condition gives B <= kappa = 0, so
every rotation letter is rho_1: d_t = r_t >= 1, D = R, D_Q = R_Q := sum_{t in Q} r_t.

Step 1 (counting).  kappa = 0 means R = 2p - o_F.  (V) gives o_F >= 1, so R <= 2p - 1;
k <= p gives R >= p >= 5.  R = o_R (mod 2) and R = o_F (mod 2), so e_R = e_F (mod 2);
(P) gives o_R >= o_F, i.e. e_R <= e_F.  As w has an even run, e_F >= 1.

Step 2 (interval windows).  For a proper cyclic interval Q (m = 1) Lemma H gives
lambda(Q) = min(p, R_Q + 1 - beta(Q), floor(R_Q/2) + 1).  Since R_Q <= 2p - 1 the cap p
never binds, and R_Q + 1 - beta >= floor(R_Q/2) + 1 unless beta = 2 and R_Q <= 2; in that
case lambda(Q) = R_Q - 1 = floor(R_Q/2).  So
  lambda(Q) = floor(R_Q/2) + 1 - t_Q,   t_Q := [beta(Q) = 2 and R_Q <= 2],   lambda(Q) >= 0,
and lambda(Q) = 0 only if R_Q = 1 (and t_Q = 1).

Step 3 (the partition).  Cut the cycle at every odd reflection run.  This gives o_F
segments G (G = the rotation runs strictly between two cyclically consecutive odd
reflection runs; if o_F = 1 the single segment is all k runs); a segment with c_G rotation
runs contains c_G - 1 even reflection runs.  In every segment with c_G >= 2 cut also at its
first internal reflection run (right after its first rotation run).  The resulting parts
are cyclic intervals; each has at most one even boundary run, so t_P = 0 and
lambda(P) = floor(R_P/2) + 1.  The number of parts is s >= 2 (s >= o_F; if o_F = 1 then
e_F = k - 1 >= 1 and the segment is cut once more).  Writing n_e, n_o for the numbers of
parts with R_P even / odd,
  sum_P lambda(P) = (R + 2 n_e + n_o)/2 = p + (2 n_e + n_o - o_F)/2.
Score a segment by score(G) = sum over its parts of (2 if R_P even, 1 if odd).  Then
2 n_e + n_o = sum_G score(G) and there are o_F segments, so condition (a) of Lemma BC is
  sum_G (score(G) - 1) >= 2.
A segment with c_G = 1 has score 1 + [r even].  A segment with c_G >= 2 has two parts,
score >= 2, and score = 3 when R_G is odd (its two parts then have opposite parities).
Since e_F >= 1 some segment has c_G >= 2 (contribution >= 1).  If a second segment
contributes, done.  Otherwise there is exactly one segment G0 with c_{G0} >= 2 and every
other segment is a single odd rotation run; then all even reflection runs and all even
rotation runs lie in G0, so e_F = c_{G0} - 1 and R_{G0} = c_{G0} - e_R = c_{G0} - e_F = 1
(mod 2) (Step 1).  So score(G0) = 3 and the sum is 2.  This proves (a).

Step 4 (conditions (b), (c) for the parts in cyclic order).  At step t the sets
X = Q_{t-1}, Y = P_t, Z = Q_t^c are nonempty cyclic intervals partitioning the cycle, and
X u Y, Y u Z, Z u X are proper cyclic intervals (complements of Z, X, Y).
Lower inequality: each lambda >= 0, and lambda(X) = lambda(Y) = lambda(Z) = 0 would force
R = 3 < 5.  Upper inequality: R_{XuY} + R_{YuZ} + R_{ZuX} = 2R is even, so at most two of
the three are odd, and
  lambda(XuY) + lambda(YuZ) + lambda(ZuX) >= (2R - 2)/2 + 3 - (t_{XuY} + t_{YuZ} + t_{ZuX}).
Two of the t's equal to 1 would give two of the unions R-value <= 2, and any two of the
unions cover the cycle, so R <= 4 < 5.  Hence the sum is >= R + 1 = 2p - o_F + 1 >= p + 1
(o_F <= k <= p).  (c): lambda(P_s), lambda(P_s^c) >= 0 and both 0 would force R = 2.
Lemma BC now gives the contradiction.  []

Which hypotheses are used: zero condition (from avoidance), (V) only as o_F >= 1, (P) as
e_R <= e_F, k <= p in Step 4, kappa = 0 throughout.  (Pairs) is implied by kappa = 0;
(E), (D0) are not used.

## 4. Numerical controls (aids; finite)

par_windows.py + session code (recorded in notes-checkpoint.md): the Step 3 partition
satisfies (a), (b), (c) of Lemma BC with lambda computed by the general Lemma H formula for
ALL inherited kappa = 0 violators with k <= p at p = 5 (2,122 rotation-canonical run data)
and p = 7 (289,645), and for 400 random kappa = 0 inherited violators at each of
p = 11, 13, 17, 19, 23, 29, 31: 0 failures.

## 5. What remains for PAR(p)

kappa >= 1 (then 1 <= kappa <= o_F - 1 <= k - 1 and B <= kappa).  See notes-checkpoint.md
for why the partition certificate of Lemma BC cannot cover all of this regime for large
p (explicit p = 17 run datum with best partition sum = p, and p = 19 data where even the LP
relaxation of the lambda system is feasible while the integer system is not).
