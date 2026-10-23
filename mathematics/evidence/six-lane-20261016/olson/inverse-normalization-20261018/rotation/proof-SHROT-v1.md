# Proposition SH-ROT: non-rigid avoiders of length 4p-4 exist for every prime p >= 5

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T04:44:39-07:00.  Status [W], UNREVIEWED.  This is
SHARPNESS information for ROT, not a counterexample: ROT concerns length 4p-2, ordered Olson length 4p-1.  No
literature/novelty claim.  Uses only Lemma GRX (parent-accepted, any constant-block representation).

**Proposition SH-ROT.**  For every prime p >= 5 the word
    w_p = rho_(-3) sigma_2^(2p-5) rho_1^(2p-1) sigma_0        (length 4p-4)
has no identity 2p-subword, and its rotation values {-3, 1} do not lie in one {c, -c} (-3 = +-1 would force p | 2 or
p | 4).
Proof.  Representation (cyclic): X_1 = {-3}, S_1 = sigma_2^(2p-5), X_2 = {1^(2p-1)}, S_2 = sigma_0; l_1, l_2 odd,
F = 2p-4, R = 2p, theta_1 = y_2 - y_1 = -2.
z = (+,+): Phi = 0, delta = 2, C_max = 2p-6, so m = 2p-C ranges over the even numbers in [6, 2p]; T = 0.  A size-m
sub-multiset of {-3, 1^(2p-1)} sums to m (m <= 2p-1 ones; m even < 2p, so not 0 mod p) or to m-4 (with -3), which is
0 mod p only for m = 4 < 6, m = p+4 (odd) or m >= 2p+4.  No solution.
z = (+,-): Phi = 2, delta = 0, C_max = 2p-4, m even in [4, 2p-2]; T = theta_1 = -2; X^z = {-3, (-1)^(2p-1)}.  The size-m
sums are -m (without -3) and -3-(m-1) = -(m+2) (with -3): together exactly the even integers -2p, ..., -4, which are
p-1 consecutive even integers and contain no integer congruent to -2 mod p (the candidates -2 and -2-2p lie outside).
No solution.  By GRX w_p avoids.  []

Checks [F] (code/sharp_rot_family_v1.py, out/sharp_rot_family_v1.jsonl, 04:44:38-04:44:39): fresh raw DP confirms w_p
avoids and is non-rigid for every prime 5 <= p <= 31; for p in {5, 7, 11, 13} every one-letter insertion (all letters,
all positions: 170, 350, 902, 1274 words) of w_p gives a word of length 4p-3 that is rigid or has an identity
2p-subword.  Consequence: "every avoider of length L is rotation-rigid" is false at L = 4p-4 for all p >= 5; ROT (L = 4p-2)
therefore has at most two letters of slack; at L = 4p-3 no counterexample is known (finite-exact: all-odd k-block
representations at length 4p-3 have no non-rigid avoider for k <= 6 at p = 7 and k <= 4 at p = 11; see README log).
