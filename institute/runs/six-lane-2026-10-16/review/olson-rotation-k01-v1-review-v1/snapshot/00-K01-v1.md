# Lemma K1 and Theorem ROT-K01: rotation rigidity for terminal kappa^ in {0, 1} and every 2 <= k <= p - 1, v1

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T13:39:23-07:00.  Status [W], UNREVIEWED.

This file changes no file.
- It extends Theorem ROT-K0 of proof-ROT-K0-v2.md (4e7ae21c...da57, unreviewed) from kappa^ = 0 to kappa^ in {0, 1}.
- It extends the kappa^ in {0, 1} range of the accepted Theorem ROT-ZX-SC (proof-ROT-ZXSC-v1.md, 15958303...bb1a;
  R/olson-zxsc-parent-verdict-v1.md, cf039654...b134) from 5k <= 4p - 1 to k <= p - 1.
Imports:
- Lemma SC0 (proof-ROT-ZXSC-v1.md Sec. 0, accepted; it rests on the explicit Savchev-Chen / Yuan import);
- Corollary S1+ (accepted);
- Lemma KETA, which is re-proved in Sec. 1 below so that this file does not depend on the unreviewed K0 file;
- the accepted terminal criterion and its imports (normal form, K1, GRX, DAV, SHgen, SHgen-E, REFL-few-odd, RGR-LONG,
  OLSON case structure), at their accepted scopes.
No novelty claim.  Not ROT(p), INV*(p) or ordered Olson in general.

## 1. Lemma KETA (re-proved)

With the SHgen definitions (proof-SHgen-v3.md, fcbd5a97...eb5e, L39-42), suppose eta >= 1.
- Every heavy has a_j >= 3, since a_j is odd and the rho_(+-c) are light.
- So E >= (a_max - 1) + 2(eta - 1) >= a_max + eta - 2.
Hence, if E <= k - 1 and k <= p - 1, then 2p - eta - a_max - 1 >= 2p - E - 3 >= 2p - k - 2 >= k, which is (K).

## 2. Lemma K1

**Lemma K1.**  Let p >= 5 be prime and 1 <= k <= p - 1.  Let Y be a sequence of R = 2p + 2 - k odd elements of Z_(2p) in
which every zero-sum subsequence has length <= 2 ((S1) at kappa = 1).  Then there is a generator g such that:
- every b_g(y) is odd with |b_g(y)| <= k - 1;
- cost_g(Y) <= k - 1, with E <= k - 2 and N <= 1.
Proof.  The nonempty zero-sums of Y are exactly the "pairs": two occurrences with sum 0.  Two disjoint pairs would form
a zero-sum of length 4, so any two pairs share an occurrence.
- Case (i): Y has no pair.
  - Then Y is zero-sum-free of length R >= p + 3.
  - Lemma SC0 gives Y = (a_1 g) ... (a_R g) with odd a_i >= 1 and sum a_i <= 2p - 1.
  - So cost_g(Y) = sum (a_i - 1) <= 2p - 1 - R = k - 3.
  - Each a_i <= k - 2 <= p - 2, so b_g = a_i.  N = 0.
- Case (ii): there is a pair {u, v} (occurrences, v = -u as values).
  - (ii.0) One of Y - {u}, Y - {v} is zero-sum-free, say Y_0 := Y - {u}, after renaming.
    - Otherwise there are pairs P' avoiding u and P'' avoiding v.  Both meet {u, v}, so P' = {v, x} and P'' = {u, y}.
    - As P' and P'' meet, x = y.  Then x = -v = -u, so u = v as values and u = (1, 0).
    - In that subcase Y has three occurrences of (1, 0), and four would give two disjoint pairs.  Then Y - {u, v}
      contains no pair (every pair meets {u, v}), so it is zero-sum-free of length 2p - k >= p + 1.  By Lemma SC0 it is
      (a_i g) with sum a_i <= 2p - 1.  But it contains x = (1, 0) = p g, of weight p, so the sum is
      >= p + (2p - k - 1) >= 2p.  A contradiction.
  - So Y_0 = Y - {u} is zero-sum-free, of length L := 2p + 1 - k >= p + 2, and it contains the occurrence v = -u.
  - Lemma SC0 gives Y_0 = (a_1 g) ... (a_L g) with odd a_i >= 1 and W := sum a_i <= 2p - 1.  Hence
    sum over Y_0 of (a_i - 1) = W - L <= k - 2.
  - (ii.1) u != (1, 0): if u = (1, 0), then v = (1, 0) lies in Y_0 with weight p, and W >= p + (L - 1) = 3p - k >= 2p.
    A contradiction.
  - (ii.2) v = g, i.e. u = -g.
    - Let a be the weight of v in Y_0, so u = -a g, and suppose a >= 3.
    - Let h be the number of terms of Y_0 with weight >= 3 (v among them) and m := L - h the number of copies of g.
      Then W - L >= (a - 1) + 2(h - 1), so a <= k + 1 - 2h.
    - Hence m - a >= (2p + 1 - k - h) - (k + 1 - 2h) = 2p - 2k + h >= 3.  So g^a <= Y_0.
    - Then g^a u is a zero-sum of length a + 1 >= 4, contrary to (S1).  So a = 1.
  - Hence cost_g(Y) = (W - L) + cost(-g) <= (k - 2) + 1 = k - 1, with E = W - L <= k - 2 and N = 1.
  - Every a_i <= 1 + (k - 2) = k - 1 <= p - 2, so b_g(a_i g) = a_i; and b_g(u) = -1.  []

## 3. Theorem ROT-K01 and corollaries

**Theorem ROT-K01.**  Let p >= 5 be prime and w an avoider of length 4p - 2.  Suppose some normal form w^ produced by
the accepted process has terminal k with 2 <= k <= p - 1 and kappa^ in {0, 1}.  Then all rotation letters of w lie in
one {rho_c, rho_-c}, c != 0.
Proof.
- GRX (all-plus) gives (ZP) at kappa^.  S1+ (kappa^ <= 1 <= (p + 1)/2) gives (S1).
- For kappa^ = 0, Y is zero-sum-free of length 2p - k >= p + 1, and Lemma SC0 gives cost <= k - 1, N = 0, all
  weights in [1, k], hence <= p - 2 by parity.  This is Lemma K0 of the K0 file, re-derived.
- For kappa^ = 1, Lemma K1 applies.
- In both cases g = Y(c) with c != 0, all |b| <= p - 2, and E <= k - 1.
- SHgen conditions:
  - (H): 2H = 2p - 2 - 2kappa^ >= 2p - 4 >= k - 1 >= E;
  - (K): Lemma KETA, Sec. 1.
- Theorem SHgen, or Lemma SHgen-E with Corollary REFL-few-odd for o_F <= k <= p, gives E = 0.  []
- k = 1 is K1.

**Corollary INV*-K01 / OLSON-K01 (uniform).**  Let p >= 5 be prime.
- (a) Every avoider of length 4p - 2 with o_F <= p - 1 and F >= o_F + 2p - 4 (kappa(w) <= 1) satisfies INV*.
- (b) Every word of length 4p - 1 with o_F <= p - 1 and F - o_F >= 2p - 4 has an identity 2p-subword in increasing
  index order.
Proof.
- (a) Every normal form has k <= o_F <= p - 1 and kappa^ <= kappa(w) <= 1.  The theorem (or K1 for k = 1) gives the
  pair, and REFL-few-odd applies since o_F <= p.
- (b) The OLSON-ZX proof with the accepted deletion ledger.  Case 1 needs o <= 2p - 3.  Case 2 gives (o - 1, F - 1).
  Case 3 gives (o or o - 2, F).  None raises o or lowers F - o.  []

## 4. Scope

- New, relative to the accepted results: terminal kappa^ in {0, 1} with (4p - 1)/5 < k <= p - 1, and uniformly
  o_F <= p - 1 with F >= o_F + 2p - 4.
  - Examples: p = 7: o_F = 6 with F >= 16; p = 11: o_F in {9, 10} with F >= o_F + 18; p = 13: o_F in {11, 12}.
- This file subsumes Theorem ROT-K0 (kappa^ = 0).  It also subsumes the kappa^ in {0, 1} cases of ROT-ZX-SC, by the
  same method plus the pair structure for kappa^ = 1.
- Not covered by this route:
  - k = p: kappa^ = 0 then needs the length-p case S(p), and kappa^ = 1 needs Lemma SC0 at length p + 1 for Y_0;
  - kappa^ >= 2 beyond 3k <= 2p + 1.
- Sufficient classes only; no existence claim.
