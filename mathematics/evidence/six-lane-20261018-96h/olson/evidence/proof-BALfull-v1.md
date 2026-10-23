# Lemma BAL-forall, Theorem ROT-ZB+ and Corollary INV*/OLSON-ZB+: balance of every longest zero-sum under 2kappa + k <= 2p - 1, v1

Owner ContinueOlson (math-2 lane, 96-hour continuation).  Written after /bin/date 2026-10-19T01:00:10-0700.  Status: CANDIDATE, written
proof [W], UNREVIEWED.  Frozen scope: evidence/BALfull-scope-v1.md
f2b82c5ee3e33b2f1ae3eb32eb6e15a31ffcc3870ea374e3000c557886f32315 (frozen before this text).  No computation is a premise.
No novelty claim; no Lean.  Not unrestricted INV*(p), not ordered Olson for D_2p in general, not the all-groups target;
terminal k = p (S(p)) stays a separate parked boundary.  Relation to the unreviewed proof-ROT-ZB-v2.md (65dbedbf...f5f1):
Lemma BAL-forall replaces its Lemma BAL1 and its alternative (B); Lemma ROOM is restated here with its proof so that this
text does not depend on the unreviewed file.

## 0. Statements

Setting (S') (ROT-ZR's Setting (S) with its kappa-range replaced, as in the frozen scope): p >= 5 prime; 1 <= k <= p - 1;
kappa integer, 1 <= kappa < p; Y a sequence of R = 2p + 2kappa - k odd elements of C_(2p) satisfying (S1) at kappa (every
zero-sum subsequence has length <= 2kappa).  Z is a LONGEST zero-sum subsequence of Y, |Z| = 2t (0 <= t <= kappa);
Y' := Y - Z (zero-sum-free), L := |Y'| = R - 2t >= 2p - k >= p + 1.  g is ANY index-<1 generator of Y' (an odd generator
whose least positive coefficients a_i of the terms of Y' have W := sum a_i <= 2p - 1; one exists by SC0); m := #{i : a_i = 1},
h := L - m, slack := 2p - 1 - W, e' := W - L = sum (a_i - 1).  By ROT-ZR Lemma ZSTRUCT (valid for every such Z and g):
Z = g^(n+) * N, N = (-s_1 g) ... (-s_(n-) g), s_i odd, 1 <= s_i <= min(2t - 1, slack), n+ + n- = 2t, S(N) := sum s_i = n+
(mod 2p).  Z is BALANCED (relative to g) if S(N) = n+.

**Lemma BAL-forall.**  In (S'), if L >= 2t + 1 then Z is balanced relative to g.  In particular, if 2kappa + k <= 2p - 1, then
EVERY longest zero-sum Z of Y is balanced relative to EVERY index-<1 generator g of Y - Z.

**Lemma ROOM.**  In (S'), if Z is balanced relative to g and L >= 2t, then W <= 2p - 1 - n+; every a_i <= p - 2 and every
s_i <= p - 2; and E := sum over the heavy terms (coefficient or s at least 3) of (coefficient - 1, resp. s - 1) satisfies
    E = e' + n+ - n- <= k - 1 - 2kappa + n+ <= k - 1.

**Theorem ROT-ZB+.**  Let p >= 7 be prime and w an avoider of length 4p - 2 over D_(2p).  Suppose some admissible normal
form of w has terminal k and kappa^ with 2 <= k <= p - 1, kappa^ >= 1 and 2kappa^ + k <= 2p - 1.  Then every rotation
letter of w lies in one set {rho_c, rho_-c}, c != 0.

**Corollary INV*/OLSON-ZB+.**  For every prime p >= 7:
- (a) every avoider of length 4p - 2 with o_F <= p - 1 and F >= 2o_F - 1 satisfies INV*;
- (b) every word of length 4p - 1 with o_F <= p - 1 and F >= 2o_F - 1 has an identity 2p-subword in increasing index order.

## 1. Imports (accepted scopes only)

- ROT-ZR (proof-ROT-ZR-v1.md e8903ff4...a7, verdict R/olson-rotzr-parent-verdict-v1.md 6d8bb6c9...e799): Lemma REALIZE
  (statement: for zero-sum-free Y' of L >= p + 1 odd elements with an SC0 generator g and W <= 2p - 1, every integer in
  [2, W] is the weight of a sub-multiset of Y' with at least two terms) and Lemma ZSTRUCT with the facts listed under
  Setting (S) (Y' zero-sum-free; m - slack >= 3).  Their proofs use only: Z longest, L >= p + 1, W <= 2p - 1, and (for
  ZSTRUCT's n- >= 1 when t >= 1) t < p; no kappa <= (p-1)/2 except through (S1), which (S') assumes.  No other ROT-ZR
  lemma is used (in particular not LAMBDA or EBOUND).
- Lemma S1-sharp (evidence/proof-S1-sharp-v1.md 992ab63f...0cb0c, erratum 1 bf504cdf...f9507, parent verdict run
  review/olson-s1sharp-parent-verdict-v1.md bd4a0a60...4f41): (ZP_kappa) => (S1_kappa) for p >= 5, kappa <= floor(2p/3).
- The word-level chain exactly as used by ROT-ZR's verdict: GRX, normal form/PM*, K1, DAV, KETA's k-free inequality
  eta + a_max <= E + 2, Theorem SHgen and Lemma SHgen-E with the V3 caller discharge, restricted REFL (o_F <= p), K01
  (terminal 2 <= k <= p-1, kappa^ <= 1), RGR-LONG and the ordered deletion ledger.

## 2. Proof of Lemma BAL-forall

Notation.  P := (the n+ terms g of Z) together with all terms of Y'.  Each x in P has coefficient c(x) (1 for the terms g
of Z, a_i for the terms of Y').  For X <= P: A(X) := sum c(x), mass(X) := A(X) - |X| = sum (c(x) - 1) >= 0; mass is
additive and mass(P) = e'.  For N0 <= N: S(N0) := sum of its s_i, f(N0) := S(N0) + |N0|.  Thus f(N) = S(N) + n-.

(F) Fullness.  For every integer v in [0, W + n+] some X <= P has A(X) = v: v = 0 (empty), v = 1 (one term g of Y'; m >= 3),
v in [2, W] (REALIZE), v in [W + 1, W + n+] (all of Y' plus v - W terms g of Z).

Suppose Z is not balanced.  S(N) = n+ (mod 2p), S(N) >= 0 and n+ <= 2t <= 2kappa < 2p, so S(N) = n+ + 2pj with j >= 1.

(Lo) If N0 <= N and S(N0) <= m + n+, then f(N0) <= 2t.
  N0 together with S(N0) terms g (taken from the n+ in Z and the m in Y') is a zero-sum subsequence of Y of length f(N0);
  Z is longest.

(Hi) If N0 <= N and 2p - W <= S(N0) <= 2p + n+, then f(N0) >= 2p - e'.
  v := n+ + 2p - S(N0) lies in [0, W + n+]; take X <= P with A(X) = v by (F).  The subsequence (N - N0) u X of Y (N - N0
  and X are disjoint parts of Y) has sum (-(S(N) - S(N0)) + v) g = (2p - 2pj) g = 0, so it is a zero-sum and
  (n- - |N0|) + |X| <= 2t = n+ + n-.  Since |X| = v - mass(X) >= v - e' = n+ + 2p - S(N0) - e', this gives
  2p - e' <= S(N0) + |N0| = f(N0).

Walk.  List the terms of N in any order; let N^(i) be the first i of them.  S(N^(i)) is strictly increasing from 0 to
S(N) = n+ + 2pj > m + n+ (m <= L <= W <= 2p - 1).  Let i* := max{i : S(N^(i)) <= m + n+}; then 0 <= i* < n-, and
f(N^(i*)) <= 2t by (Lo).  Let s be the next term's value; s <= slack by ZSTRUCT.  Then
    m + n+ + 1 <= S(N^(i*+1)) <= m + n+ + slack = 2p - 1 + n+ - (W - m) <= 2p - 1 + n+,
and m + n+ + 1 >= 2p - W, because W + m = 2m + sum of the h heavy coefficients >= 2(L - h) + 3h >= 2L >= 2p + 2.  So (Hi)
applies to N^(i*+1):
    2p - e' <= f(N^(i*+1)) = f(N^(i*)) + s + 1 <= 2t + slack + 1 = 2t + 2p - W.
Hence W - e' <= 2t, i.e. L <= 2t, contradicting L >= 2t + 1.  So Z is balanced.
If 2kappa + k <= 2p - 1, then L - 2t = 2p + 2kappa - k - 4t >= 2p - k - 2kappa >= 1 (t <= kappa), for every longest Z (all
have the same length 2t) and every index-<1 generator g of Y - Z.  []

Remarks.  (i) The proof uses s_i <= slack but not s_i <= 2t - 1, and (S1) only through t <= kappa.  (ii) Without
"longest" the conclusion fails trivially (p = 7, Y' = g^8, Z = g (-5g)^3 is an unbalanced zero-sum, but g^5 (-5g) is a
longer one).  (iii) Whether L >= 2t + 1 can be weakened to L >= 2t is not decided here; the proof shows that an unbalanced
longest Z forces L <= 2t, i.e. R <= 4t.

## 3. Proof of Lemma ROOM

Suppose n+ >= 1 and W >= 2p - n+.  By (F) (restricted to Y') there is Q <= Y' with coefficient sum 2p - n+ (<= W), and
|Q| = (2p - n+) - mass(Q) >= 2p - n+ - e'.  g^(n+) Q (the g's taken from Z) has coefficient sum 2p, so it is a zero-sum of Y
and n+ + |Q| <= 2t, i.e. 2p - e' <= 2t + n+ - n+ ... precisely: n+ + 2p - n+ - e' <= 2t, so 2p <= 2t + e' <= 2t + 2p - 1 - L,
i.e. L <= 2t - 1, contradicting L >= 2t.  Hence W <= 2p - 1 - n+ (trivial for n+ = 0).
Weights.  e' <= 2p - 1 - L <= k - 1 (L >= 2p - k), so every a_i <= 1 + e' <= k <= p - 1, i.e. a_i <= p - 2 (odd); every
s_i <= slack <= 2p - 1 - L <= k - 1 <= p - 2.
Count.  The heavies are the terms a_i g with a_i >= 3 and -s_i g with s_i >= 3; terms with coefficient or s equal to 1
contribute 0 to both sides below.  e' = W - L <= 2p - 1 - n+ - L = (k - 1 - 2kappa + 2t) - n+ = k - 1 - 2kappa + n-; with
balance sum (s_i - 1) = n+ - n-, so E = e' + n+ - n- <= k - 1 - 2kappa + n+ <= k - 1 (n+ <= 2t <= 2kappa).  []

## 4. Proof of Theorem ROT-ZB+

Let w^ be the normal form (ZX verdict overlay 1; normal form of proof-ROT-few-E-v4 Sec. 0): avoider, same length,
rotation multiset and F; k odd blocks; GRX gives kappa^ >= 0 and (ZP) at kappa^ for its rotation sequence Y (all-plus
pattern); DAV gives kappa^ <= k - 1; |Y| = R = 2p + 2kappa^ - k.
- (S1).  kappa^ <= min(k - 1, (2p - 1 - k)/2) <= (2p - 2)/3 <= floor(2p/3) (the minimum is largest at k = (2p+1)/3), so
  Lemma S1-sharp gives (S1) at kappa^, and (S') holds with kappa = kappa^ (1 <= kappa^ < p, 2 <= k <= p - 1).
- Balance.  Take any longest Z and any index-<1 generator g of Y - Z.  If t = 0, Z is empty (balanced).  Otherwise Lemma
  BAL-forall applies (2kappa^ + k <= 2p - 1).
- Lemma ROOM (L >= 2t + 1 >= 2t): g = Y(c) with c != 0 (g is an odd generator), every rotation has SHgen weight
  |b| <= p - 2 (no rho_0), and E <= k - 1.  If E = 0, every rotation is rho_c or rho_-c.
- Otherwise eta >= 1 and SHgen's hypotheses hold: (H) 2H = 2p - 2 - 2kappa^ >= k - 1 >= E by 2kappa^ + k <= 2p - 1;
  (K) KETA's k-free inequality gives eta + a_max <= E + 2 <= k + 1 <= 2p - k - 1, i.e. k <= 2p - eta - a_max - 1 (k <= p-1).
  Theorem SHgen (all runs nonempty) or Lemma SHgen-E (empty runs; caller: expansions keep k and the empty runs, base
  words have one nonzero rotation pair and o_F <= k <= p - 1, inside restricted REFL; the V3 overlay discharge as in the
  ROT-ZR verdict) gives w^ an identity 2p-subword, contradicting avoidance.  So E = 0, and the rotation multiset of w
  (= that of w^) lies in {rho_c, rho_-c}.  []

## 5. Proof of the Corollary

(a) Let o := o_F <= p - 1 and F >= 2o - 1; kappa(w) := p - 1 - (F - o)/2, so the condition reads 2kappa(w) + o <= 2p - 1.
Every admissible normal form has 1 <= k <= o, k = o (mod 2), kappa^ = kappa(w) - (o - k)/2.
- k = 1: Proposition K1.
- 2 <= k <= p - 1 and kappa^ = 0: ROT-K01.
- 2 <= k <= p - 1 and kappa^ >= 1: 2kappa^ + k = 2kappa(w) - o + 2k <= 2kappa(w) + o <= 2p - 1 (k <= o): Theorem ROT-ZB+.
In every case the rotations lie in one nonzero pair; restricted REFL (o <= p) gives INV*.
(b) Ordered deletion ledger exactly as in the K01/KP/ZR verdicts: Case 1 (R <= 2) uses o <= p - 1 <= 2p - 3 and framed
equal pairs; Case 2 (deletion inside an odd block of length >= 3) gives (o - 1, F - 1) with F - 1 >= 2(o - 1) - 1; Case 3
(rotation deletions) gives (o or o - 2, F) with F >= 2o - 1 >= 2(o - 2) - 1.  Both conditions (o <= p - 1, F >= 2o - 1)
are preserved, every relevant deletion is covered by (a), and RGR-LONG completes.  []

## 6. Relation to earlier criteria (internal comparison; not a premise)

- ROT-ZB v2's uniform condition 2F >= 2p + 3o_F - 5 implies F >= 2o_F - 1 (as o_F <= 2p - 3), so Corollary ZB+ contains
  Corollary ZB; e.g. p = 31, o_F = 30: F >= 59 here versus F >= 74 there.  ROT-ZB+'s terminal criterion contains
  ROT-ZB's (it drops (B)) and ROT-ZR's on 2 <= k <= p - 1 wherever ROT-ZR's (H') 2kappa^ + k <= 2p - 1 - G holds.
- Together with S1-sharp's corollary (3o_F <= 2p + 1, any F), the INV* residual with o_F <= p - 1 is contained in
  {3o_F >= 2p + 3 and F <= 2o_F - 3}; terminal cells with k <= p - 1 and 2kappa^ + k >= 2p, the cells k = p (S(p)
  boundary) and the reflection half o_F > p remain open.

## 7. Falsification controls and limits

- Each hypothesis is used at an identified step: Z longest in (Lo)/(Hi); L >= p + 1 and W <= 2p - 1 in (F) and in
  W + m >= 2p - 1; s_i <= slack in the walk step; L >= 2t + 1 only in the final inequality.
- Consistency (aid, not a premise): probe v5 (balance_probe_v5.py 1ba1b898..., RECEIPT 932f3a67...) found no unbalanced
  longest zero-sum in any completed (Z, g) item (support <= 3, p = 13, 17, 19 partly), as Lemma BAL-forall predicts.
- Limits: written mathematics relative to the imports above (index-one/Savchev-Chen statements via the parent import record;
  2007 proofs not read); no Lean, no human review, no literature search; a search miss would never be novelty evidence.
