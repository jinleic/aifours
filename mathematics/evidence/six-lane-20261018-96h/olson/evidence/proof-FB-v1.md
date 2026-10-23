# Lemma FB (full balance with room), Theorem ROT-FB and Corollary INV*/OLSON-FB, v1

Owner ContinueOlson (math-2 lane, 96-hour continuation).  Written after /bin/date 2026-10-19T01:56:55-0700.  Status: CANDIDATE, written
proof [W], UNREVIEWED.  Frozen scope: evidence/TMAX-scope-v1.md 858d9a3ed099594ddacbaa0f438fe79cd8c323b6b604c58407e07ae0a5b3568f
(frozen before this text).  Within that scope this text proves ROUTE-ALL(T) (Sec. 4, Remark); the proof is not specific to
t = kappa and gives more.  No computation is a premise.  No novelty claim; no Lean.  Not unrestricted INV*(p), not ordered
Olson for D_2p, not the all-groups target.

## 0. Statements

Setting (S') exactly as in the accepted BAL-full v2 (run review/olson-balfull-rotzb-parent-verdict-v1.md 56b988ee...1bc0):
p >= 5 prime; 1 <= k <= p - 1; kappa integer, 1 <= kappa < p; Y a sequence of R = 2p + 2kappa - k odd elements of C_(2p)
with (S1) at kappa; Z a LONGEST zero-sum subsequence, |Z| = 2t (0 <= t <= kappa); Y' := Y - Z (zero-sum-free),
L := R - 2t >= 2p - k >= p + 1; g ANY index-<1 generator of Y' (odd generator; the least positive coefficients a_i of the
terms of Y' have W := sum a_i <= 2p - 1); m := #{i : a_i = 1}; h := L - m; slack := 2p - 1 - W; e' := W - L.  By ROT-ZR
Lemma ZSTRUCT (accepted in (S') through its proof, verdict overlay 5): Z = g^(n+) N, N = (-s_1 g) ... (-s_(n-) g), s_i odd,
1 <= s_i <= min(2t - 1, slack), n+ + n- = 2t, S(N) := sum s_i = n+ (mod 2p); and n- >= 1 if t >= 1.

**Lemma FB.**  In (S'), S(N) <= slack = 2p - 1 - W.  Consequently Z is balanced (S(N) = n+) and W + n+ <= 2p - 1.
(Every longest Z, every index-<1 generator g of Y - Z; no hypothesis relating L and t.)

**Corollary FB-E.**  In (S'): every a_i <= p - 2 and every s_i <= p - 2; n+ <= 2p - 1 - L <= k - 1; and
    E := e' + sum (s_i - 1) = e' + n+ - n-  satisfies  E <= k - 1 - 2kappa + n+.
In particular E <= k - 1 - 2kappa + min(2t - 1, k - 1) for t >= 1, and E = e' <= k - 1 - 2kappa for t = 0.

**Theorem ROT-FB.**  Let p >= 7 be prime and w an avoider of length 4p - 2 over D_(2p).  Suppose some admissible normal
form w^ of w has terminal k and kappa^ >= 1 with
  (a) 2 <= k <= p - 1 and the rotation sequence Y of w^ satisfies (S1) at kappa^ -- automatic when kappa^ <= floor(2p/3); or
  (b) k = p, (S1) at kappa^ (automatic when kappa^ <= floor(2p/3)), and every zero-sum of Y has length <= 2kappa^ - 2.
Then every rotation letter of w lies in one set {rho_c, rho_-c}, c != 0.

**Corollary INV*/OLSON-FB.**  For every prime p >= 7 and kappa(w) := p - 1 - (F - o_F)/2:
- (a) every avoider of length 4p - 2 with o_F <= p - 1 and kappa(w) <= floor(2p/3), i.e. F - o_F >= 2(p - 1 - floor(2p/3)),
  satisfies INV*;
- (b) every word of length 4p - 1 over D_(2p) with o_F <= p - 1 and F - o_F >= 2(p - 1 - floor(2p/3)) has an identity
  2p-subword in increasing index order.

## 1. Imports (accepted scopes only)

- ROT-ZR (proof-ROT-ZR-v1.md e8903ff4...a7, verdict R/olson-rotzr-parent-verdict-v1.md 6d8bb6c9...e799): Lemma ZSTRUCT and
  the Setting fact m - slack >= 2L - 2p + 1 + h >= 3, both in (S') through their proofs (BAL-full verdict overlay 5).
  REALIZE is used only inside ZSTRUCT.
- SC0 / Savchev-Chen-Yuan index-one theorem (author statement via the parent import record): an index-<1 generator of a
  zero-sum-free sequence of length >= p + 1 in C_(2p) exists.
- Lemma S1-sharp (evidence/proof-S1-sharp-v1.md 992ab63f...0cb0c + erratum 1 bf504cdf...f9507; verdict run
  review/olson-s1sharp-parent-verdict-v1.md bd4a0a60...4f41): (ZP_kappa) => (S1_kappa) for p >= 5, kappa <= floor(2p/3).
- The word-level chain at the scopes used by the ROT-ZB/BAL-full verdict: ZX overlays 1 and 2 (normal form, existential
  reading), GRX (ZP), DAV, K1, K01, KETA's k-free inequality eta + a_max <= E + 2, Theorem SHgen and Lemma SHgen-E with the
  ROT-ZR verdict's caller discharge, restricted REFL (o_F <= p), RGR-LONG and the ordered deletion ledger; the normal form
  with 1 <= k <= o_F, k = o_F (mod 2) (proof-ROT-few-E-v4.md Sec. 0; ROT-ZR verdict m4).
- NOT used: Lemma BAL1, BAL-forall, ROOM, LAMBDA, EBOUND (Lemma FB and Corollary FB-E replace them).

## 2. Proof of Lemma FB

Put delta := 2p - W = slack + 1 >= 1, so every s_i <= delta - 1.  Suppose S(N) >= delta (then N is nonempty and delta >= 2).
Order the terms of N so that s_(1) >= s_(2) >= ...; let S_i := s_(1) + ... + s_(i) and let r be least with S_r >= delta.
- r >= 2, since s_(1) <= delta - 1.  S_(r-1) <= delta - 1, and with x := r - 1: x <= S_(r-1) <= delta - 1 (every s >= 1) and
  x s_(r) <= S_(r-1) <= delta - 1 (s_(r) is the least of the first r terms).
- y := S_r - delta satisfies 0 <= y <= s_(r) - 1, and
    y + r = S_(r-1) + s_(r) - delta + r <= s_(r) + x <= (delta - 1)/x + x <= delta,
  because u -> (delta - 1)/u + u is convex on [1, delta - 1] and equals delta at both ends.
- y <= delta - 2 = slack - 1 < m (Setting fact m - slack >= 3), so Y' contains y terms equal to g.
Let Z* := (Y' with y terms g removed) u g^(n+) u (N - {-s_(1) g, ..., -s_(r) g}), a subsequence of Y (its three parts are
disjoint parts of Y' and Z).  Its coefficient sum is
    (W - y) + n+ - (S(N) - S_r) = W + n+ - S(N) + delta = 2p + n+ - S(N) = 0 (mod 2p),
as S(N) = n+ (mod 2p); so Z* is a zero-sum of Y, of length
    (L - y) + n+ + (n- - r) = L + 2t - (y + r) >= 2t + L - delta = 2t + (L + W - 2p) >= 2t + 2      (W >= L >= p + 1).
This contradicts the maximality of Z.  Hence S(N) <= delta - 1 = 2p - 1 - W.
Then 0 <= S(N) <= 2p - 1, 0 <= n+ <= 2t <= 2kappa < 2p and S(N) = n+ (mod 2p) give S(N) = n+, and n+ <= 2p - 1 - W.  []

Remarks.  (i) Only ZSTRUCT's bound s_i <= slack, the Setting fact m >= slack + 3, the maximality of Z and n+ < 2p are used;
(S1) enters only through t <= kappa < p and L >= p + 1.  (ii) Lemma FB contains the accepted BAL-forall (balance) and
ROOM's W-bound (W <= 2p - 1 - n+) without their hypotheses L >= 2t + 1, L >= 2t; the zero-sum Z* (all of Y' but y units,
all units of Z, and N minus its r largest terms) is a different witness from those used there.

## 3. Proof of Corollary FB-E

W + n+ <= 2p - 1 and W >= L give n+ <= 2p - 1 - L and e' = W - L <= 2p - 1 - L - n+; L >= 2p - k (t <= kappa) gives
2p - 1 - L <= k - 1 <= p - 2.  So every a_i <= 1 + e' <= p - 1, i.e. a_i <= p - 2 (odd), and every
s_i <= slack = 2p - 1 - W <= 2p - 1 - L <= p - 2.  With balance, sum (s_i - 1) = n+ - n- and
    E = e' + n+ - n- <= (2p - 1 - L - n+) + n+ - n- = 2p - 1 - L - n- = 2p - 1 - R + n+ = k - 1 - 2kappa + n+
(L + n- = R - n+).  For t >= 1, n- >= 1 gives n+ <= 2t - 1; for t = 0, n+ = 0 and E = e'.  []

## 4. Proof of Theorem ROT-FB

Let w^ be the normal form (ZX overlays 1 and 2; proof-ROT-few-E-v4.md Sec. 0): avoider, same length, rotation multiset
and F; k odd blocks; GRX gives kappa^ >= 0 and (ZP) at kappa^ for its rotation sequence Y; DAV gives kappa^ <= k - 1;
|Y| = R = 2p + 2kappa^ - k; H = p - 1 - kappa^.
- (S1).  Case (a) or (b): if kappa^ <= floor(2p/3), Lemma S1-sharp gives (S1) at kappa^; otherwise it is the hypothesis.
- Case (a): (S') holds with kappa = kappa^ (1 <= kappa^ <= k - 1 < p, 1 <= k <= p - 1).  Case (b): the longest zero-sum has
  length 2t <= 2kappa^ - 2, so L = R - 2t = p + 2kappa^ - 2t >= p + 2; the objects of (S') (Y' zero-sum-free with
  L >= p + 1, SC0 generator, ZSTRUCT, the Setting fact) and the proofs of Lemma FB and Corollary FB-E use k <= p - 1 only
  through L >= p + 1 and 2p - 1 - L <= p - 2, which hold here (2p - 1 - L <= p - 3).  So Lemma FB and Corollary FB-E hold
  in case (b) with k = p.
- Take any longest Z and any index-<1 generator g = Y(c) of Y - Z; c != 0 (g has order 2p).  By Corollary FB-E every
  rotation has SHgen weight b = a_i, 1 or -s_i with |b| <= p - 2 (no rho_0; the lights are the terms g and -g), and
  E <= k - 1 - 2kappa^ + n+.  If E = 0, every rotation is rho_c or rho_-c.
- Otherwise eta >= 1 and SHgen's hypotheses hold:
  (H) n+ <= 2p - 1 - L <= k - 1 (L >= 2p - k), so E <= 2k - 2 - 2kappa^ <= 2p - 2 - 2kappa^ = 2H (k <= p).
  (K) KETA's k-free inequality gives eta + a_max <= E + 2 <= k + 1 - 2kappa^ + n+.  Case (a): n+ <= 2t - 1 <= 2kappa^ - 1
      (t >= 1), or n+ = 0 (t = 0), so eta + a_max <= k <= 2p - 1 - k (k <= p - 1).  Case (b): t >= 1 would give
      n+ <= 2t - 1 <= 2kappa^ - 3 and eta + a_max <= p - 2 <= p - 1 = 2p - 1 - k; t = 0 gives eta + a_max <= p + 1 - 2kappa^
      <= p - 1.  In both cases k <= 2p - eta - a_max - 1.
  Theorem SHgen (all runs nonempty) or Lemma SHgen-E (empty runs; ROT-ZR verdict discharge: expansions preserve k and odd
  blocks; base words have length 4p - 2, one nonzero pair, and o_F(u°) <= k <= p, so restricted REFL and the accepted V3
  caller apply; the normal form preserves rotation letters) gives w^ an identity 2p-subword, contradicting avoidance.
So E = 0 and the rotation multiset of w (= that of w^) lies in {rho_c, rho_-c}.  []

Remark (scope T-MAX).  For (T) (2 <= k <= p - 1, 2kappa + k >= 2p, longest zero-sum of length exactly 2kappa), the
generator g = Y(c) of any longest Z gives E_c <= 2H and eta_c + a_max,c <= 2p - 1 - k (or E_c = 0): ROUTE-ALL(T) holds for
every Y in (T), (S1) assumed when kappa > floor(2p/3).  No obstruction family of the kind (ii) exists.

## 5. Proof of the Corollary

(a) Let o := o_F <= p - 1 and kappa(w) <= floor(2p/3).  Every admissible normal form has 1 <= k <= o, k = o (mod 2) (accepted
normal form; F >= 1 by the rotations-only EGZ bound, the even-block terminal form excluded by K1/Davenport), and
kappa^ = kappa(w) - (o - k)/2 <= kappa(w) (F is preserved).
- k = 1: Proposition K1.
- 2 <= k <= p - 1 and kappa^ <= 1: ROT-K01 (kappa^ = 0 included).
- 2 <= k <= p - 1 and 2 <= kappa^ <= kappa(w) <= floor(2p/3): Theorem ROT-FB (a).
In every case the rotations lie in one nonzero pair; restricted REFL (o <= p) gives INV*.
(b) Ordered deletion ledger as in the K01/KP/ZR/ZB verdicts: Case 1 (R <= 2) uses o <= p - 1 <= 2p - 3 and framed equal
pairs; Case 2 (deletion inside an odd block of length >= 3) gives (o - 1, F - 1), so F - o is unchanged; Case 3 (rotation
deletions) gives (o or o - 2, F), so F - o does not decrease.  Both conditions (o <= p - 1, F - o >= 2(p - 1 - floor(2p/3)))
are preserved, every relevant deletion is covered by (a), and RGR-LONG completes.  []

## 6. Relation to accepted results (internal comparison; not a premise)

- Terminal level: ROT-FB (a) contains ROT-ZB+ (there kappa^ <= min(k - 1, (2p - 1 - k)/2) <= (2p - 2)/3), ROT-ZB, ROT-ZR on
  2 <= k <= p - 1, and the ZX terminal criterion with S1-sharp (3k <= 2p + 1 gives kappa^ <= k - 1 <= floor(2p/3)).
  ROT-FB (b) adds the k = p cells whose rotation sequence has no zero-sum of length 2kappa^ (any kappa^ <= floor(2p/3)).
- Uniform: Corollary FB's band F - o_F >= 2(p - 1 - floor(2p/3)) contains Corollary ZB+'s F >= 2o_F - 1 wherever
  o_F - 1 >= 2(p - 1 - floor(2p/3)); below that, the accepted S1-sharp corollary (3o_F <= 2p + 1, any F) applies.  E.g.
  p = 31, o_F = 30: F >= 50 here (F >= 60 for ZB+, parity included).
- Remaining rotation residual within terminal k <= p: (i) kappa^ >= floor(2p/3) + 1 (hence k >= floor(2p/3) + 2) with (S1)
  FAILING at kappa^ (by (ZP) the rotation sequence then has a zero-sum of length >= 2p + 2); (ii) k = p with a zero-sum of
  length exactly 2kappa^ (complement of length exactly p; S(p) open), or with (S1) failing.  Terminal k >= p + 1 (forcing
  o_F >= p + 1) and the reflection half o_F > p remain open.  A word is residual only if every admissible normal form lies in
  a residual cell (ZX overlay 2).  Uniformly for o_F <= p - 1 the residual is contained in {kappa(w) >= floor(2p/3) + 1 and
  o_F >= floor(2p/3) + 2}.

## 7. Falsification controls and limits

- Each hypothesis is used at an identified step: Z longest (Z*), s_i <= slack (r >= 2, y <= slack - 1), m >= slack + 3
  (units available), n+ < 2p (balance), L >= p + 1 and W >= L (|Z*| >= 2t + 2), t <= kappa (L >= 2p - k), k <= p (H),
  k <= p - 1 or t <= kappa^ - 1 (K).
- Consistency (aids, not premises): probes v6/v8 (no unbalanced longest Z) and v9 (run evidence/probe-v9: within (T), every
  normalized form with S(N) >= n+ + 2p or e' + 2n+ >= 2p was DP-checked and none had Z longest; p = 7 exhaustive control set
  equality) are consistent with Lemma FB.  A dedicated falsification probe of Lemma FB is planned (launch plan to the
  parent first).
- Limits: written mathematics relative to the imports above (index-one/Savchev-Chen statements via the parent import record;
  2007 proofs not read); no Lean, no human review, no literature search; a search miss would never be novelty evidence.
