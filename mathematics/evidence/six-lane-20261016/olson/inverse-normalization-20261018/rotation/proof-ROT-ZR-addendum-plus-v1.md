# Addendum ZR+ to Theorem ROT-ZR: KETA+, LAMBDA+, and kappa^ = 3, 4, 5 for every 2 <= k <= p - 1 (p >= 11, 19, 29), v1

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T14:44:56-07:00.  Status [W], UNREVIEWED.
Builds on proof-ROT-ZR-v1.md (e8903ff4...69a7, unreviewed; not edited).  Same dependencies as that file (its Sec. 0);
nothing else is imported.  No novelty claim.  Not ROT(p), INV*(p) or ordered Olson in general.  No computation was run;
the small numerical checks below are hand arithmetic shown in full.

## 1. Lemma KETA+

**Lemma KETA+.**  Let k <= p, let every rotation have SHgen weight |b| <= p - 2 relative to c (no rho_0), and let
E <= 2p - k - 2.  Then SHgen's (K) k <= 2p - eta - a_max - 1 holds whenever eta >= 1.
Proof.  eta = 1: the only heavy has a_max <= p - 2, so eta + a_max <= p - 1 <= 2p - k - 1 as k <= p.  eta >= 2: every
heavy has weight >= 3, so E >= (a_max - 1) + 2(eta - 1), i.e. eta + a_max <= E + 3 - eta <= E + 1 <= 2p - k - 1.  []
(KETA, accepted, needs E <= 2p - k - 3.  As E is even, KETA+ gains exactly when k is even.)

## 2. Lemma LAMBDA+

Setting (S) and notation of proof-ROT-ZR-v1.md Sec. 2; t >= 1; s* (t) := the least odd integer >= p/t;
L_t := 2p + 2kappa - k - 2t.

**Lemma LAMBDA+.**  In (S), sum s_i = n+ holds if t(2t - 1) < p, or if (3 L_t - 2p + 1 + s*(t))/2 >= 4t - 2.
Proof.  Suppose sum s_i != n+.  Then sum s_i = n+ + 2p lambda with lambda >= 1, so sum s_i >= 2p; as n- <= 2t,
s_max >= 2p/n- >= p/t, and s_max is odd, so s_max >= s*(t).  By Lemma ZSTRUCT s_max <= 2t - 1, so t(2t - 1) >= p.
Also slack >= s_max >= s*(t), so e' = 2p - 1 - L - slack <= 2p - 1 - L_t - s*(t) and m >= L_t - e'/2 >=
(3 L_t - 2p + 1 + s*(t))/2.  If this is >= 4t - 2, the induction in the proof of Lemma LAMBDA (Lambda1) applies verbatim
(it uses only m >= 4t - 2) and gives sum s_i = n+: contradiction.  []
L_t decreases in k, so the second condition is hardest at k = p - 1, where L_t = p + 1 + 2(kappa - t).

## 3. Theorem ROT-ZR+

**Theorem ROT-ZR+.**  Theorem ROT-ZR of proof-ROT-ZR-v1.md holds with (Lambda) replaced by
- (Lambda+) for every integer t in [1, kappa^] with t(2t - 1) >= p: (3 L_t - 2p + 1 + s*(t))/2 >= 4t - 2,
and (K') replaced by
- (K'+) Ebar <= 2p - k - 2, where Ebar is the largest even integer <= k - 1 + G(kappa^),
and (H') read with Ebar.
Proof.  As for ROT-ZR, with Lemma LAMBDA+ for every possible t (t is not known in advance) and KETA+ for (K); E is
even (each heavy contributes |b| - 1, even), so E <= Ebar.  []

## 4. Corollaries (hand arithmetic)

G(3) = 0, G(4) = 1, G(5) = 2 (proof-ROT-ZR-v1.md Lemma EBOUND).  Throughout 2 <= k <= p - 1, and kappa^ <= k - 1 (DAV).

**ROT-ZR3+ (kappa^ = 3, every p >= 11).**  Ebar <= k - 1.  (H'): k - 1 <= 2p - 8.  (K'+): k - 1 <= 2p - k - 2, i.e.
k <= p - 1/2.  (Lambda+): t(2t - 1) >= p needs t = 3 and p <= 15, i.e. p in {11, 13}; at k = p - 1, L_3 = p + 1 and the
condition reads (p + 4 + s*(3))/2 >= 10: p = 11, s* = 5: 10 >= 10; p = 13, s* = 5: 11 >= 10.
**ROT-ZR4 (kappa^ = 4, every p >= 19).**  Ebar <= k.  (H'): k <= 2p - 10.  (K'+): k <= 2p - k - 2, i.e. k <= p - 1.
(Lambda+): t = 4 needs p <= 28 (p in {19, 23}); t = 3 needs p <= 15 (none).  At k = p - 1, L_4 = p + 1:
(p + 4 + s*(4))/2 >= 14: p = 19, s* = 5: 14 >= 14; p = 23, s* = 7: 17 >= 14.
**ROT-ZR5 (kappa^ = 5, every p >= 29).**  Ebar <= k + 1 if k is odd, <= k if k is even.  (H'): k + 1 <= 2p - 12.
(K'+): k odd: k + 1 <= 2p - k - 2, i.e. k <= p - 3/2, true as odd k <= p - 2; k even: k <= p - 1.  (Lambda+): t = 5 needs
p <= 45 (p in {29, 31, 37, 41, 43}); t = 4 needs p <= 28 (none).  At k = p - 1, L_5 = p + 1: (p + 4 + s*(5))/2 >= 18,
i.e. p + s* >= 32: s* = 7, 7, 9, 9, 9 for p = 29, 31, 37, 41, 43.
Smaller k only increase L_t, so the checks at k = p - 1 suffice.

**Corollary INV*-ZR+ / OLSON-ZR+ (uniform).**  Let p be prime and K in {3, 4, 5} with p >= 11, 19, 29 respectively.
- (a) Every avoider of length 4p - 2 with o_F <= p - 1 and F - o_F >= 2p - 2 - 2K (kappa(w) <= K) satisfies INV*.
- (b) Every word of length 4p - 1 over D_(2p) with the same inequalities has an identity 2p-subword in increasing
  index order.
Proof.  Normal forms: k <= o_F <= p - 1, 0 <= kappa^ <= kappa(w) <= K.  k = 1: Proposition K1; kappa^ <= 1: ROT-K01;
kappa^ = 2: ROT-ZR2 (p >= 7); kappa^ = 3: ROT-ZR3+ (p >= 11); kappa^ = 4: ROT-ZR4 (p >= 19); kappa^ = 5: ROT-ZR5
(p >= 29).  Restricted REFL (o_F <= p); (b) by the accepted deletion ledger and RGR-LONG as in proof-ROT-ZR-v1.md.  []

## 5. Scope

- Supersedes the kappa^ = 3 corollary of proof-ROT-ZR-v1.md (there p >= 17, or k <= (4p - 19)/3 for p = 11, 13).
- Not covered by this route: k = p; kappa^ = 3 at p = 7 with k = 6; kappa^ = 4 at p in {11, 13, 17} for the largest k;
  kappa^ = 5 at p < 29 for the largest k; kappa^ >= 6 at k = p - 1 (there G(kappa^) >= 3 makes (K'+) fail), and generally
  every (k, kappa^) failing (Lambda+), (H') or (K'+); o_F > p (REFL).  Sufficient conditions only.
