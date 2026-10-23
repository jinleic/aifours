# Lemma CTgen (global): a generator of multiplicity >= N - 2kappa - 1 in every (ZP_kappa) sequence of length N with a
# zero-sum of length >= 2p + 2, v1

Owner OlsonSTABSuccessor.  Written after /bin/date 2026-10-19T06:00:33-0700 (clock re-read before hashing; see checkpoint-006).  Status: CANDIDATE [W],
UNREVIEWED.  Derivation proposed by the parent (IRC, 'HIGH-LEVERAGE parent derivation to check NOW'), checked and written here.
Uses only Lemma CT of proof-LSplus-e2-v1.md (2effb09ea4e28553ab0321a64b3e660c422d767ef940fcf58615dec8edc208b1), i.e. Lemma RS(a) of proof-ROW-v1.md (Cauchy-Davenport).

## Statement
Let p >= 5 be prime, kappa an integer with (p - 3)/2 <= kappa <= p - 1, and Y an odd sequence over C_(2p) with (ZP_kappa), |Y| = N with
2kappa + 3 <= N, and a zero-sum T of length >= 2p + 2.  Then the involution p has multiplicity <= N - 2kappa - 2 in Y, and some
GENERATOR g has v_g(Y) >= N - 2kappa - 1.  In particular, at N = 3kappa + 2: v_g(Y) >= kappa + 1 (>= p - e, e := p - kappa).
## Proof
n := N - 2kappa - 2 >= 1 and N - n = 2kappa + 2 is even and in [2kappa + 2, 2p] (kappa <= p - 1), so Lemma CT gives
sum_x min(n, v_x) <= p + n - 2 < N (as p - 2 < 2kappa + 2).  Hence some odd x has v_x >= n + 1.  Suppose the involution p had
v_p(Y) >= n + 1.  Let m be the number of occurrences of p in T and W the rest of T; |W| <= N - v_p(Y) <= 2kappa + 1 < 2p.  Then
|T| - 2p is even, >= 2 and <= |T| - |W| = m; deleting |T| - 2p occurrences of p from T removes an element sum of (|T| - 2p)p = 0, so
a zero-sum of length exactly 2p remains, contradicting (ZP_kappa).  So v_p(Y) <= n, and the odd x with v_x >= n + 1 is a
generator.  []
## Consequence (scope note only)
For floor(2p/3) + 1 <= kappa <= p - 2 and N = 3kappa + 2 the generator hypothesis 'v_g >= p - e' of the length-(3kappa + 2) dichotomy
(proof-ROW-v1.md Sec. 4 as restricted by erratum-2-prereq-consolidated.md R12) is supplied for every LS+ counterexample of length
3kappa + 2 with a long zero-sum, relative to this candidate lemma.  The reviewed scopes of the earlier texts are not changed.
