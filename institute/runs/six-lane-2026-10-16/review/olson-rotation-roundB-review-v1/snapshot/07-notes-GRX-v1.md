# Lemma GRX: exact solvability criterion for EVERY word over D_(2p) (OB1)

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T01:52:10-07:00.  Status [W] unreviewed; the
statement is a direct generalisation of Lemma GR (olson/proof-GR.md Sec. 2, reviewed) and Lemma GR0
(c2/invstar/proof-GR0-r1.md, unreviewed); the proof below is self-contained.  Controls [F] in Sec. 3.

## 1. Representation and statement

p odd prime, conventions of olson/proof-dihedral-partial.md Sec. 0.  Let w have F >= 1 reflections.  Read w
cyclically and cut every maximal cyclic reflection run at each change of value: w is a cyclic alternation
    R_1 S_1 R_2 S_2 ... R_k S_k,   S_i = sigma_(y_i)^(l_i) (l_i >= 1),   R_i = rotations with value multiset X_i,
|X_i| = r_i >= 0 (R_i may be EMPTY; then y_(i-1) != y_i when the blocks are maximal, but the criterion below holds
for every such representation, maximal or not).  y_0 := y_k, theta_i := y_(i-1) - y_i, sum theta_i = 0.
For z in {+-1}^k: f_i = [z_i != z_(i+1)] (z_(k+1) = z_1), Phi = sum f_i (even), delta = #{i : l_i != f_i mod 2},
C_max = F - delta, X^z := multiset union over i of z_i X_i (each value multiplied by z_i), R = sum r_i,
T(z) := sum_{i : z_i = +1} theta_i (mod p), and Sigma_m(Y) := set of sums of size-m sub-multisets of Y.

**Lemma GRX.**  w has an identity 2p-subword iff there are z and an even C with Phi <= C <= C_max, 0 <= 2p - C <= R
and T(z) in Sigma_(2p-C)(X^z).
(F = 0: identity 2p-subword iff 0 in Sigma_(2p)(X); rotations commute.  The sign pattern may be normalised z_1 = +1.)

## 2. Proof

A selection with an even number of reflections is given by (i) z_i := (-1)^(number of selected reflections
cyclically before R_i, counted from a fixed cut point at the end of S_k), (ii) c_i := number of selected letters of
S_i, with c_i = f_i (mod 2) [the parity of selected reflections in S_i is exactly what changes the zone sign between
R_i and R_(i+1)], (iii) any sub-multiset of each X_i.  Conversely each such datum with 0 <= c_i <= l_i is realised
(choose any c_i letters of the constant block S_i; any chosen rotations).  Because S_i is constant, its c_i selected
letters multiply to sigma_(y_i) (c_i odd) or 1 (c_i even); so the ordered product, read from the cut, is
    rho_V,  V = sum_i z_i (sum of chosen values in X_i) + sum_{i : f_i = 1} z_i y_i      (mod p),
by induction along the word (a rotation rho_x in a zone of sign z contributes z x; a reflection sigma_y entered in
a zone of sign z contributes z y and flips the zone sign; the even total makes the product a rotation).
Summation by parts: sum_{f_i=1} z_i y_i = sum_i y_i (z_i - z_(i+1))/2 = sum_i z_i (y_i - y_(i-1))/2 = -(sum_i z_i theta_i)/2,
and sum_i z_i theta_i = 2 sum_{z_i=+1} theta_i - sum_i theta_i = 2 T(z).  Hence V = sigma - T(z), sigma := the sum of
the chosen elements of X^z.  The size is C + m with C = sum c_i, m = number of chosen rotations.  For fixed z the
realisable C are exactly the even numbers in [Phi, C_max]: c_i ranges over the integers in [0, l_i] congruent to
f_i mod 2, i.e. from f_i up to l_i - [l_i != f_i mod 2]; summing, C ranges over all values of the right parity
between Phi and F - delta (each c_i moves in steps of 2), and Phi + C_max = F - delta + Phi is even because F = sum l_i
= delta + Phi (mod 2).  The rotations are chosen independently of the c_i.  So the selection is an identity
2p-subword iff C + m = 2p and sigma = T(z), as claimed.  The global sign change z -> -z maps X^z -> -X^z and
T(z) -> sum_{z_i=-1} theta_i = -T(z), so z_1 = +1 is a normalisation.  Identity subwords are invariant under cyclic
rotation of w (UV = 1 iff VU = 1), so the cyclic reading is exact.  []

Specialisations: all rotation values in {1, -1} gives Lemma GR (Sigma_m(X^z) is then the window
{m - 2q : max(0, m - E+) <= q <= min(m, E-)}, E+- as in GR), and with empty runs Lemma GR0.

## 3. Controls [F] (code/grx.py, code/rawdp.py, code/test_grx_v1.py; output tmp/test_grx_v1.out.json)

GRX (literal implementation) == fresh raw DP == unchanged olson/code/was_verify.py dp_has on every word:
3,730 exhaustive D10 avoiders (N = 18; all NO); 3,738 RGR avoiders p = 7, N = 26 (all NO); 16 positive family
words p in {5,7,11,13} (all NO); 608 negative controls (positive controls with an explicit random 2p-index set forced
to multiply to the identity; all YES); 1,800 random words p = 5, 7, N = 4p-3..4p-1 (uniform and near-rigid with one
random rotation); 313 deletions and 287 one-letter substitutions of known avoiders.  0 disagreements, 0 unexpected
values.  (Wall 3.0 s, 01:52:07-01:52:10 PDT.)  Hash pins are in the closing manifest.
