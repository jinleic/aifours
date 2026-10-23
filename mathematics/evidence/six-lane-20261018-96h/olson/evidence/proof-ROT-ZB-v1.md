# Lemma BAL1, Lemma ROOM, Theorem ROT-ZB and Corollary INV*/OLSON-ZB: rotation rigidity for terminal k <= p-1 with 4kappa^ <= 2p-k+1, v1

Owner ContinueOlson (math-2 lane, 96-hour continuation).  Written after /bin/date 2026-10-19T00:45:39-0700.  Status: CANDIDATE, written
proof [W], UNREVIEWED.  No computation is a premise.  No novelty claim; no Lean.  Not unrestricted INV*(p), not ordered
Olson for D_2p in general, not the all-groups target.

## 0. Statements

Setting (S') (ROT-ZR's Setting (S) with its kappa-range replaced): p >= 5 prime; 1 <= k <= p-1; kappa integer with
1 <= kappa < p; Y a sequence of R = 2p + 2kappa - k odd elements of C_(2p) satisfying (S1) at kappa; Z a LONGEST
zero-sum of Y, |Z| = 2t (0 <= t <= kappa); Y' := Y - Z, L := |Y'| = R - 2t >= 2p - k >= p + 1; g, a_i, W, m, slack,
e' := W - L as in ROT-ZR Lemma REALIZE (SC0 generator g of Y', W = sum of the coefficients a_i <= 2p - 1).
By ROT-ZR Lemma ZSTRUCT, Z = g^(n+) * N with N = (-s_1 g) ... (-s_(n-) g), s_i odd, 1 <= s_i <= min(2t - 1, slack),
n+ + n- = 2t, and S(N) := sum s_i = n+ (mod 2p).  Z is BALANCED if S(N) = n+.

**Lemma BAL1.**  In (S'), Z is balanced whenever L + n+ >= 4t - 1, or 2L + e' + n+ >= 2p - 1 + 2t.  In particular Z is
balanced whenever 4kappa <= 2p - k + 1, or kappa + k <= p.

**Lemma ROOM.**  In (S'), if Z is balanced and 2kappa + k <= 2p, then W <= 2p - 1 - n+, and relative to c with g = Y(c)
(c != 0) every rotation has SHgen weight |b| <= p - 2 (no rho_0) and
    E <= k - 1 - 2kappa + n+ <= k - 1.

**Theorem ROT-ZB.**  Let p >= 7 be prime and w an avoider of length 4p - 2 over D_(2p).  Suppose some admissible normal
form of w has terminal k and kappa^ with 2 <= k <= p - 1, kappa^ >= 1, 2kappa^ + k <= 2p - 1, and
  (B) 4kappa^ <= 2p - k + 1, or kappa^ + k <= p, or ROT-ZR's (Lambda) [8kappa^ <= 4p - 3k + 5 or 2kappa^(2kappa^ - 1) < 2p].
Then every rotation letter of w lies in one set {rho_c, rho_-c}, c != 0.

**Corollary INV*/OLSON-ZB.**  For every prime p >= 7:
- (a) every avoider of length 4p - 2 with o_F <= p - 1 and 2F >= 2p + 3o_F - 5 satisfies INV*;
- (b) every word of length 4p - 1 with o_F <= p - 1 and 2F >= 2p + 3o_F - 5 has an identity 2p-subword in increasing
  index order.
(Equivalently, at length 4p - 2: o_F <= p - 1 and kappa(w) <= (2p - o_F + 1)/4, kappa(w) := p - 1 - (F - o_F)/2.)

## 1. Imports (accepted scopes only)

- ROT-ZR (proof-ROT-ZR-v1.md e8903ff4...a7, verdict R/olson-rotzr-parent-verdict-v1.md 6d8bb6c9...e799): Lemmas REALIZE and
  ZSTRUCT and the definitions of Setting (S).  Neither lemma uses kappa <= (p-1)/2 except through (S1), which (S') assumes
  directly; ZSTRUCT's n- >= 1 for t >= 1 needs only kappa < p.  Lemma LAMBDA only for the (Lambda) alternative of (B).
- Lemma S1-sharp (evidence/proof-S1-sharp-v1.md 992ab63f...0cb0c with erratum 1 bf504cdf...f9507; parent verdict run
  review/olson-s1sharp-parent-verdict-v1.md bd4a0a60...4f41): (ZP) => (S1) for kappa <= floor(2p/3).
- The word-level chain exactly as used by ROT-ZR's verdict: GRX, normal form/PM*, K1, DAV, KETA's k-free inequality
  eta + a_max <= E + 2, Theorem SHgen and Lemma SHgen-E with the V3 caller discharge, restricted REFL (o_F <= p), K01
  (terminal 2 <= k <= p-1, kappa^ <= 1), the ZX terminal criterion (with S1-sharp), RGR-LONG and the ordered deletion ledger.

## 2. Proof of Lemma BAL1

P := g^(n+) Y' (every term of Y with positive coefficient); |P| = n+ + L, total coefficient W + n+.  By REALIZE, every
integer in [0, W] is the coefficient sum of a sub-multiset of Y'; adding the n+ copies of g, every integer in
[0, W + n+] is the coefficient sum of a sub-multiset of P.
(*) Let N_0 <= N with S_0 := S(N_0) <= W + n+.  Put c := W + n+ - S_0, choose P_c <= P with coefficient sum c, and
P_0 := P - P_c.  As every coefficient is >= 1, |P_c| <= c, so |P_0| >= n+ + L - c.  N_0 P_0 has coefficient sum
S_0 - S_0 = 0: it is a zero-sum of Y, so (Z longest) |N_0| + |P_0| <= 2t, i.e.
    S_0 + |N_0| <= 2t + e'      (using n+ + L - c = S_0 + L - W = S_0 - e').
Suppose Z unbalanced.  S(N) = n+ (mod 2p), S(N) >= 0 and n+ <= 2t <= 2kappa < 2p, so S(N) >= n+ + 2p > W + n+.  Order N
increasingly, s_1 <= ... <= s_(n-), with prefix sums P_i, and let i_0 := max{i : P_i <= W + n+} (so i_0 < n-).  By (*),
P_(i_0) <= 2t + e' - i_0, and W + n+ < P_(i_0 + 1) = P_(i_0) + s_(i_0+1).
- With s_(i_0+1) <= 2t - 1: L + e' + n+ < 2t + e' - i_0 + 2t - 1, i.e. L + n+ <= 4t - 2.
- With s_(i_0+1) <= slack = 2p - 1 - W: L + e' + n+ < 2t + e' - i_0 + 2p - 1 - L - e', i.e. 2L + e' + n+ <= 2p - 2 + 2t.
This proves the first sentence.  For the second: L = 2p + 2kappa - k - 2t and t <= kappa give
L + n+ - (4t - 1) >= 2p + 2kappa - k + 1 - 6kappa = 2p - k + 1 - 4kappa, and
2L + e' + n+ - (2p - 1 + 2t) >= 4p + 4kappa - 2k - 6t - 2p + 1 >= 2p - 2k + 1 - 2kappa (both with e', n+ >= 0).  []

## 3. Proof of Lemma ROOM

Suppose n+ >= 1 and W >= 2p - n+.  By REALIZE there is Q <= Y' with coefficient sum 2p - n+ (<= W), and
|Q| >= (2p - n+) - e' (every coefficient a contributes a - 1 <= e' in total).  g^(n+) Q (the g's taken from Z) has
coefficient sum 2p: it is a zero-sum of Y, so n+ + |Q| <= 2t, i.e. 2p - n+ - e' <= n-, i.e. 2p <= 2t + e'.  But
e' <= 2p - 1 - L, so L <= 2t - 1; while L = 2p + 2kappa - k - 2t >= 2t because 2kappa + k <= 2p and t <= kappa.
Contradiction; hence W <= 2p - 1 - n+ (trivial for n+ = 0).
Weights.  Every a_i <= 1 + e' <= 1 + (2p - 1 - L) <= k <= p - 1, so a_i <= p - 2 (odd), and b_g(a_i g) = a_i.  Every
s_i <= slack <= 2p - 1 - L <= k - 1 <= p - 2.  So every rotation has |b| <= p - 2, none is rho_0, and the heavies are
exactly the terms a_i g with a_i >= 3 and -s_i g with s_i >= 3.
Count.  e' = W - L <= 2p - 1 - n+ - L = (k - 1 - 2kappa + 2t) - n+.  With balance,
E = e' + sum (s_i - 1) = e' + n+ - n- <= k - 1 - 2kappa + 2t - n- = k - 1 - 2kappa + n+ <= k - 1 (as n+ <= 2t <= 2kappa).  []

## 4. Proof of Theorem ROT-ZB

Let w^ be the normal form (ZX verdict overlay 1; normal form of proof-ROT-few-E-v4 Sec. 0): avoider, same length,
rotation multiset and F; k odd blocks; GRX gives kappa^ >= 0 and (ZP) for its rotation sequence Y (all-plus pattern);
DAV gives kappa^ <= k - 1; |Y| = R = 2p + 2kappa^ - k.
- (S1).  Under (B), kappa^ <= max((2p - k + 1)/4, p - k, (4p - 1)/8, sqrt(p)) <= floor(2p/3) (k >= 2, p >= 7), so Lemma
  S1-sharp gives (S1) at kappa^.  So (S') holds with kappa = kappa^.
- Balance.  If t = 0 Z is empty.  If t >= 1: under the first two alternatives of (B), Lemma BAL1; under (Lambda),
  ROT-ZR Lemma LAMBDA (whose proof uses only (S') and the stated inequality).
- Lemma ROOM (2kappa^ + k <= 2p - 1 <= 2p) gives g = Y(c), c != 0, every |b| <= p - 2 and E <= k - 1.  If E = 0, every
  rotation is rho_c or rho_-c.
- Otherwise eta >= 1 and SHgen's hypotheses hold: (H) 2H = 2p - 2 - 2kappa^ >= k - 1 >= E by 2kappa^ + k <= 2p - 1;
  (K) KETA's k-free inequality gives eta + a_max <= E + 2 <= k + 1 <= 2p - k - 1, i.e. k <= 2p - eta - a_max - 1 (k <= p-1).
  Theorem SHgen (all runs nonempty) or Lemma SHgen-E (empty runs; caller: expansions keep k and the empty runs, base
  words have one nonzero rotation pair and o_F <= k <= p - 1, inside restricted REFL; the V3 overlay discharge as in the
  ROT-ZR verdict) gives w^ an identity 2p-subword, contradicting avoidance.  So E = 0, and the rotation multiset of w
  (= that of w^) lies in {rho_c, rho_-c}: the original rotations lie in one nonzero pair.  []

## 5. Proof of the Corollary

(a) Let o := o_F <= p - 1 and 2F >= 2p + 3o - 5; kappa(w) := p - 1 - (F - o)/2, so the condition reads
4kappa(w) <= 2p - o + 1.  Every admissible normal form has 1 <= k <= o, k = o (mod 2), kappa^ = kappa(w) - (o - k)/2.
- k = 1: Proposition K1.
- 3k <= 2p + 1: S1-sharp corollary chain (ZX terminal criterion).
- 2 <= k <= p - 1 and kappa^ <= 1: ROT-K01.
- Otherwise (2p+1)/3 < k <= o <= p - 1 and kappa^ >= 2.  Then 4kappa^ = 4kappa(w) - 2(o - k) <= 2p - o + 1 - 2o + 2k
  <= 2p - k + 1 (as k <= o), so (B) holds; and 2kappa^ + k = 2kappa(w) - o + 2k <= 2kappa(w) + o <= 2p - 1, because
  2F >= 2p + 3o - 5 >= 4o - 2 (o <= p - 1 <= 2p - 3) gives F >= 2o - 1, i.e. 2kappa(w) + o = 2p - 2 - F + 2o <= 2p - 1.
  Theorem ROT-ZB applies.
In every case the rotations lie in one nonzero pair; restricted REFL (o <= p) gives INV*.
(b) Ordered deletion ledger exactly as in the K01/KP/ZR verdicts: Case 1 (R <= 2) uses o <= p - 1 <= 2p - 3 and framed
equal pairs; Case 2 (deletion inside an odd block of length >= 3) gives (o - 1, F - 1), and 2(F - 1) >= 2p + 3(o - 1) - 5;
Case 3 (rotation deletions) gives (o or o - 2, F).  Both conditions are preserved, every relevant deletion is covered by
(a), and RGR-LONG completes.  []

## 6. Coverage relative to accepted results (internal comparison; planning arithmetic, not a premise)

- Uniform: previously o_F <= p - 1 needed F - o_F >= 2p - 6 (ZR2, p >= 7) or 2p - 8 (ZR3, p >= 17), i.e. kappa(w) <= 2
  or 3; the new condition is kappa(w) <= (2p - o_F + 1)/4 (e.g. p = 31, o_F = 30: kappa(w) <= 8).  It contains ZR3's
  band whenever p >= 13 (p + (3o - 5)/2 <= o + 2p - 8 iff o <= 2p - 11).
- Terminal cells (k, kappa^) with (2p+1)/3 < k <= p, kappa^ >= 2 not covered by K01/KP/T3/T4 before, now covered by
  ROT-ZB (lane arithmetic): p = 31: 28 of 202; p = 61: 129 of 803; p = 101: 386 of 2255.  k = p is untouched.

## 7. Scope and limits

Written proof relative to Sec. 1.  Unreviewed; needs parent derivation and both model-family hostile reviews.  The
remaining rotation residual: k = p (all kappa^ >= 2), and k <= p - 1 with (B) failing or 2kappa^ + k > 2p - 1 and T4
failing.  Balance beyond (B) is supported only by a finite aid (probe v5, support <= 3, p <= 19 partly), not a premise.
Reflection half for o_F > p untouched.  No literature search; no novelty claim.
