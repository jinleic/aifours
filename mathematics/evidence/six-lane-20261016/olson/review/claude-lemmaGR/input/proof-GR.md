# Route (b): run-constant reflection words with rigid rotations (Lemma GR)

Lane MathOlson; written after host clock 2026-10-16T22:20:03-07:00.  Status:
written proof [W]; exact small-prime checks in code/gr_window.py (results in
Section 5); NOT yet hostile-reviewed.

## 1. Class

RGR(p): words w of length 4p-1 over D_{2p} whose rotations all lie in
{rho_x, rho_-x} for one x != 0 and whose maximal (cyclic) reflection runs are each
constant (one letter sigma_{y_i} repeated; different runs may differ).  Normalise
x = 1 (automorphism rho_v -> rho_{v/x}, sigma_v -> sigma_{v/x}).  If F, R >= 1, w is a
cyclic alternation R_1 S_1 R_2 S_2 ... R_k S_k: R_i has a_i letters rho_1 and b_i
letters rho_{-1}; S_i = sigma_{y_i}^{l_i}, l_i >= 1; S_i lies between R_i and
R_{i+1} (indices mod k).  Theorem R is the subcase y_1 = ... = y_k.

## 2. Lemma GR (exact criterion)

For z in {+1,-1}^k put f_i = [z_i != z_{i+1}], Phi = sum f_i (even),
delta = #{i : l_i != f_i mod 2}, C_max = F - delta,
E+ = sum_{z_i=+1} a_i + sum_{z_i=-1} b_i,  E- = R - E+,
s0 = 2p - C_max,  s1 = 2p - Phi,
Ach(z) = 2Z intersect [ max(-s1, s0 - 2E-, -E-),  min(s1, 2E+ - s0, E+) ],
tau(z) = - 2^{-1} sum_i z_i (y_i - y_{i-1})  in Z_p.

**Lemma GR.**  w in RGR(p) with F, R >= 1 has an identity 2p-subword iff some
z in {+-1}^k satisfies  Ach(z) intersect (tau(z) + pZ) != empty.

**Corollary GR-W (window).**  If some z has |Ach(z)| >= p, then w has an identity
2p-subword.  (p consecutive even integers are pairwise distinct mod p.)

### Proof of Lemma GR

Selections with an even number of reflections <-> data (z; c_i; chosen rotations):
z_i is the sign of the zone of R_i (parity of selected reflections before R_i,
fixed up to one global sign), c_i is the number of letters chosen from S_i with
c_i = f_i mod 2, 0 <= c_i <= l_i.  As S_i is constant, sigma_{y_i}^{c_i} is sigma_{y_i}
(c_i odd) or 1, and the ordered product is rho_V with
V = sum_i z_i n_i + sum_{f_i = 1} z_i y_i,
n_i = (#rho_1 chosen in R_i) - (#rho_{-1} chosen in R_i).
Summation by parts (z_{i+1} = -z_i exactly when f_i = 1):
sum_{f_i=1} z_i y_i = sum_i y_i (z_i - z_{i+1})/2 = sum_i z_i (y_i - y_{i-1})/2.
Call a rotation of R_i effectively positive if it contributes +1 (rho_1 with
z_i = +1 or rho_{-1} with z_i = -1).  With A+, A- the numbers of chosen
effectively positive/negative rotations and t = A+ - A-, V = t - tau(z) (mod p).
Size: C + A+ + A- = 2p with C = sum c_i.
Realisable C: exactly the even numbers in [Phi, C_max] (start from c_i = f_i and
add pairs inside runs up to l_i - [l_i != f_i mod 2]; Phi <= C_max since each
run satisfies f_i <= l_i - [l_i != f_i]).
For even t, (A+, A-) = ((2p-C+t)/2, (2p-C-t)/2) is admissible iff
C <= 2p - |t|, C >= 2p + t - 2E+, C >= 2p - t - 2E-; together with Phi <= C <= C_max
(all bounds even) a C exists iff |t| <= s1, s0 - 2E- <= t <= 2E+ - s0,
t <= E+ and t >= -E- (the last two from 2p+t-2E+ <= 2p-|t| and its mirror).
So the realisable t for pattern z are exactly Ach(z), and V = 0 iff t = tau(z)
mod p.  Global sign change z -> -z maps Ach to -Ach and tau to -tau, consistent
with the realised first zone being +.  Identity subwords are invariant under
cyclic rotation, so the cyclic run model is exact.  []

## 3. The obstruction family is covered (all primes p >= 5)

w_p = sigma_0^{p-2} rho_1^{p-2} sigma_1^{p-2} rho_1^{p-2} sigma_2^4 rho_1^3: runs
R_1 = rho_1^{p-2} (S_3 = sigma_0^{p-2} before, S_1 = sigma_1^{p-2} after),
R_2 = rho_1^{p-2}, S_2 = sigma_2^4, R_3 = rho_1^3.  Take z = (-1,+1,+1): f = (1,0,1),
Phi = 2, delta = 0 (l = p-2, 4, p-2), C_max = 2p, s0 = 0, s1 = 2p-2, E+ = p+1,
E- = p-2.  Ach(z) = 2Z intersect [-(p-2), p+1] = {-(p-3), ..., p+1}: exactly p even
integers.  By Corollary GR-W, w_p has a solution for every p >= 5 (positive
control; the explicit one in verify-consult.md 1b has t = p+1).

## 4. What remains (precise)

Covered here: every word of RGR(p) (Lemma GR is an exact decision procedure),
structurally by Corollary GR-W when some window has >= p even integers.
Remaining for a structural proof inside RGR(p): words in Res whose run data
(k; a_i, b_i, l_i) give |Ach(z)| <= p-1 for every z; for these Lemma GR still
decides, but through the reflection values (tau), not structure.
Outside route (b): Res words with a rotation value outside {+-x} or a
non-constant reflection run.
