# Theorem ROT-ZR: rotation rigidity for terminal kappa^ >= 2 with 3k > 2p + 1 allowed (longest zero-sum + SC0 realization), v1

Owner OlsonRotationRigidity.  Written after host clock __CLOCK__.  Status [W], UNREVIEWED.
No novelty claim.  Not ROT(p), INV*(p) or ordered Olson in general.  No computation was run for this file.

## 0. Dependencies (exact; all parent-accepted at their accepted scopes)

- Normal form w^, kappa^ >= 0 and integral for k >= 2, (ZP), Lemma DAV, Proposition K1 (one block):
  proof-ROT-few-E-v4.md Sec. 0, L28-43 (ac560eb8...ea8f), as used by the accepted terminal criterion
  (R/olson-zx-s1c-parent-verdict-v1.md, 2f8d376b...e6af; overlay retained).
- Lemma S1 (a): (ZP) at kappa <= (p - 1)/2 gives (S1) (every zero-sum has length <= 2 kappa), accepted
  (R/olson-zx-s1c-parent-verdict-v1.md).
- Lemma SC0: proof-ROT-ZXSC-v1.md Sec. 0 (15958303...bb1a), accepted (R/olson-zxsc-parent-verdict-v1.md,
  cf039654...b134); explicit Savchev-Chen / Yuan index-one import.
- KETA and ROT-K01: proof-ROT-K01-v1.md (b3ecdb4e...b378), accepted with overlay (R/olson-k01-parent-verdict-v1.md,
  e11144f6...0df4).
- Theorem SHgen (proof-SHgen-v3.md, fcbd5a97...eb5e) with exactly its accepted hypotheses (H) 2H >= E and
  (K) k <= 2p - eta - a_max - 1; Lemma SHgen-E (proof-ROT-few-E-v4.md Sec. 1) with the caller discharge of the K01
  verdict and R/olson-zs-v2-parent-verdict-v1.md (2ba1fedc...0734) overlay V3.
- Restricted REFL: Corollary REFL-few-odd (R/olson-refl-fewodd-parent-verdict-v1.md, 16436c07...f1ca), o_F <= p.
- RGR-LONG and the ordered deletion ledger, as in the K01 verdict.
Not used: ROT-KP (proof-ROT-KP-v1.md, under review), any finite search, ZX Steps C-G.

Notation as in the K01 verdict: rho_x -> Y(x) = (1, x) in C_2 x C_p; for g = Y(c), c != 0, b_g is the odd coefficient
with |b| <= p - 2 (b_g(Y(0)) = p); heavy = |b| >= 3; E = sum over heavies of (|b| - 1).  For a zero-sum-free sequence
of length >= p + 1, Lemma SC0 gives g with all coefficients a_i odd in [1, 2p - 1] and W := sum a_i <= 2p - 1; the
"weight" of a sub-multiset is the sum of its a_i (an integer).

## 1. Lemma REALIZE

**Lemma REALIZE.**  Let Y' be a zero-sum-free sequence of L >= p + 1 odd elements of C_(2p), with SC0 generator g,
coefficients a_i and W = sum a_i <= 2p - 1; m := #{i : a_i = 1}.  Then every integer s in [2, W] is the weight of a
sub-multiset of Y' with at least two terms.
Proof.  Sort the heavy coefficients a_(1) <= ... <= a_(h) (h = L - m) and put X_i := m + sum_(j<i) a_(j).
- Claim: a_(i) <= X_i for every i.  Suppose a_(i) >= X_i + 1 and let n := h - i + 1 >= 1.  Every a_(j), j >= i, is
  >= X_i + 1, so W >= X_i + n(X_i + 1).  Also L = m + (i - 1) + n <= X_i + n, so X_i >= p + 1 - n.
  - n = 1: W >= 2X_i + 1 >= 2p + 1.
  - 2 <= n <= p - 1: W >= (n + 1)(p + 1 - n) + n >= 2p + n, as (n + 1)(p + 1 - n) is concave in n and equals
    3p - 3 >= 2p at n = 2 and 2p at n = p - 1.
  - n >= p: W >= 3n >= 3p.
  Each contradicts W <= 2p - 1.
- So the sorted list 1, ..., 1, a_(1), ..., a_(h) has every term <= 1 + (sum of the earlier terms); hence the
  sub-multiset weights fill [0, W], and for each heavy value a (first occurrence a_(i0)) the strictly smaller terms
  (total X_(i0) >= a) realize a, necessarily with at least two terms.
- Given s in [2, W], take a realization Q.  If |Q| = 1, then Q = {q} with q heavy (s >= 2 and coefficients are odd, so
  s >= 3); replace q by at least two strictly smaller terms realizing a_q.  []

## 2. Lemma ZSTRUCT and Lemma LAMBDA

Setting (S).  p >= 5 prime; 1 <= k <= p - 1; kappa >= 0; Y a sequence of R = 2p + 2kappa - k odd elements of C_(2p)
satisfying (S1) at kappa.  Z is a LONGEST zero-sum of Y, |Z| = 2t with 0 <= t <= kappa, and Y' := Y - Z.

- Y' is zero-sum-free (else Z could be lengthened) and L := |Y'| = R - 2t >= 2p - k >= p + 1.  Let g, a_i, W, m be as in
  Lemma REALIZE, and slack := 2p - 1 - W >= 0, e' := W - L (even).
- Since W >= L + 2h and m = L - h: m - slack >= 2L - 2p + 1 + h >= 3.

**Lemma ZSTRUCT.**  In (S), every z in Z is g or -s g with s odd, 1 <= s <= min(2t - 1, slack).
Proof.  Write z = r g with r odd in [1, 2p - 1].
- If 3 <= r <= W: Lemma REALIZE gives Q in Y' of weight r with |Q| >= 2, and (Z - {z}) u Q is a zero-sum of length
  >= 2t + 1: contradiction.  So r = 1 or r >= W + 1.
- If r >= W + 1, put s := 2p - r <= slack < m.  Then g^s z is a zero-sum (g^s from Y'), of length s + 1 <= 2t.  []

Write Z = g^(n+) (-s_1 g) ... (-s_(n-) g), n+ + n- = 2t.  As sigma(Z) = 0: sum s_i = n+ (mod 2p).  If t >= 1 then
n- >= 1 (2t g != 0 since 1 <= t <= kappa < p).

**Lemma LAMBDA.**  In (S) with t >= 1, sum s_i = n+ holds if (Lambda1) m >= 4t - 2, or (Lambda2) n-(2t - 1) < 2p.
(Lambda1) holds whenever 8 kappa <= 4p - 3k + 5; (Lambda2) holds whenever 2kappa(2kappa - 1) < 2p.
Proof.
- (Lambda2): 1 <= sum s_i <= n-(2t - 1) < 2p and 0 <= n+ < 2p, so the congruence is equality.
- (Lambda1): let P_j := s_1 + ... + s_j.  If P_j <= m, then the first j negatives U and g^(P_j) from Y' form a zero-sum
  of length j + P_j, so P_j <= 2t - j.  P_1 <= 2t - 1; if P_j <= 2t - j then P_(j+1) <= 4t - 2 <= m, so
  P_(j+1) <= 2t - j - 1.  Hence sum s_i <= 2t - n- = n+, and the congruence with 1 <= sum s_i gives equality.
- m >= L - e'/2 >= (3L - 2p + 1)/2 with L = 2p + 2kappa - k - 2t, so m >= 4t - 2 iff 14t <= 4p + 6kappa - 3k + 5,
  implied by t <= kappa and 8kappa <= 4p - 3k + 5.  (Lambda2) follows from n- <= 2t <= 2kappa.  []

## 3. Lemma EBOUND

**Lemma EBOUND.**  In (S), assume t = 0 or sum s_i = n+.  Then, relative to c (g = Y(c), c != 0), every rotation has
|b| <= p - 2 (no rho_0), and
    E <= k - 1 + G(kappa),   G(kappa) := max over odd s in [1, max(1, 2kappa - 1)] of ( 2kappa(s - 1)/(s + 1) - s ).
In particular G(1) = G(2) = -1, G(3) = 0, G(4) = 1, G(5) = 2, and G(kappa) <= 2kappa - 4 sqrt(kappa) + 1.
Proof.
- Coefficients: a_i <= 1 + e' <= 1 + (2p - 1 - L) <= k <= p - 1, so a_i <= p - 2 (odd); z in Z has |b| <= 2t - 1 <=
  2kappa - 1 <= p - 2 (kappa <= (p - 1)/2 is part of (S1) via Lemma S1 (a); otherwise use 2t - 1 <= p - 2 directly
  from 2t <= R... see the Theorem's hypothesis kappa <= (p - 1)/2).
- t = 0: E = e' <= 2p - 1 - R = k - 1 - 2kappa.
- t >= 1, s := max s_i (>= 1; s <= slack by Lemma ZSTRUCT).  E = e' + sum (s_i - 1) = e' + n+ - n-, and
  e' = 2p - 1 - L - slack <= k - 1 - 2kappa + 2t - s.  With n+ = 2t - n- this gives E <= k - 1 - 2kappa + 4t - s - 2n-.
  From n+ = sum s_i <= n- s: n- >= 2t/(s + 1).  So E <= k - 1 - 2kappa + 4ts/(s + 1) - s, increasing in t, and t <= kappa
  gives E <= k - 1 + 2kappa(s - 1)/(s + 1) - s <= k - 1 + G(kappa).
- AM-GM: s + 4kappa/(s + 1) >= 4 sqrt(kappa) - 1, so 2kappa(s-1)/(s+1) - s = 2kappa - s - 4kappa/(s+1) <= 2kappa -
  4 sqrt(kappa) + 1.  []

## 4. Theorem ROT-ZR

**Theorem ROT-ZR.**  Let p >= 7 be prime and w an avoider of length 4p - 2 over D_(2p).  Suppose some admissible normal
form w^ of w has terminal k and kappa^ with 2 <= k <= p - 1, 0 <= kappa^ <= (p - 1)/2, and
- (Lambda) 8kappa^ <= 4p - 3k + 5 or 2kappa^(2kappa^ - 1) < 2p;
- (H') k - 1 + G(kappa^) <= 2p - 2 - 2kappa^;
- (K') k - 1 + G(kappa^) <= 2p - k - 3.
Then all rotation letters of w lie in one set {rho_c, rho_-c}, c != 0.
Proof.  GRX gives (ZP); Lemma S1 (a) gives (S1) at kappa^.  Setting (S) holds with Y the rotation sequence of w^.
Lemma LAMBDA (by (Lambda)) and Lemma EBOUND give c != 0 with the SHgen weights and E <= k - 1 + G(kappa^).  If E = 0,
done.  Otherwise eta >= 1; (H) holds by (H'); (K) holds by KETA (eta + a_max <= E + 2 <= 2p - k - 1, by (K')).
Theorem SHgen or Lemma SHgen-E (caller: o_F = k <= p - 1 <= p, restricted REFL) contradicts avoidance.  []

**Corollary ROT-ZR2 (kappa^ = 2).**  For p >= 7 prime, every terminal pair (k, 2) with 3 <= k <= p - 1 satisfies the
hypotheses: 2*2*3 = 12 < 2p; G(2) = -1, so (H') is k <= 2p - 4 and (K') is 2k <= 2p - 1.
**Corollary ROT-ZR3 (kappa^ = 3).**  G(3) = 0: (H') k <= 2p - 7, (K') k <= p - 1; (Lambda) holds for p >= 17
(30 < 2p), and for p = 11, 13 when k <= (4p - 19)/3 (k <= 8, resp. k <= 11).

**Corollary INV*-ZR2 / OLSON-ZR2 (uniform).**  Let p >= 7 be prime.
- (a) Every avoider of length 4p - 2 with o_F <= p - 1 and F - o_F >= 2p - 6 (kappa(w) <= 2) satisfies INV*.
- (b) Every word of length 4p - 1 over D_(2p) with o_F <= p - 1 and F - o_F >= 2p - 6 has an identity 2p-subword in
  increasing index order.
Proof.  (a) Normal forms have k <= o_F <= p - 1 and kappa^ <= kappa(w) <= 2, integral and >= 0 for k >= 2.  k = 1:
Proposition K1.  kappa^ <= 1: ROT-K01.  kappa^ = 2 (then k >= 3 by DAV): ROT-ZR2.  Restricted REFL (o_F <= p).
(b) The accepted deletion ledger (o_F <= p - 1 <= 2p - 3; Case 2 gives (o - 1, F - 1); Case 3 gives (o or o - 2, F)),
then (a) and RGR-LONG.  []
**Corollary INV*-ZR3 / OLSON-ZR3.**  For p >= 17 prime the same with F - o_F >= 2p - 8 (kappa(w) <= 3), using ROT-ZR3
for kappa^ = 3 (k >= 4 by DAV).

## 5. Scope

- New relative to the accepted results: terminal kappa^ = 2 with (2p + 1)/3 < k <= p - 1 (p >= 7), kappa^ = 3 with
  (2p + 1)/3 < k <= p - 1 (p >= 17; p = 11, 13 partly), and further (k, kappa^) satisfying the three conditions.
  Uniformly: o_F <= p - 1 with F - o_F >= 2p - 6 (p >= 7), and with F - o_F >= 2p - 8 (p >= 17).
- Examples: p = 11, terminal (8, 2), (9, 2), (10, 2), (8, 3) [k <= 8 for kappa^ = 3 at p = 11]; uniform p = 11:
  o_F = 9, 10 with F >= o_F + 16.
- Not covered by this route: k = p (L = p, SC0 does not apply); kappa^ > (p - 1)/2; (k, kappa^) failing (Lambda),
  (H') or (K'); o_F > p (REFL).  Sufficient conditions only; no existence of avoiders is asserted.
