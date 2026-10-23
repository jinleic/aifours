# Theorem BASE1: STAB and LS+ at the first kappa beyond S1-sharp, p = 1 (mod 3), v1

Owner OlsonSTABSuccessor (Slice A).  Written after /bin/date 2026-10-19T05:27:08-0700.  Status: CANDIDATE, written proof [W], UNREVIEWED.
Imports (accepted scopes only): Lemma S1-sharp at kappa0 (verdict review/olson-s1sharp-parent-verdict-v1.md; source
992ab63f...0cb0c + mandatory erratum 1 bf504cdf...f9507); the index-one theorem as recorded in run of 2026-10-16
review/olson-index-one-primary-statement-parent-v1.md (e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6), with n = 2p; Theorem SLZ3 (verdict
review/olson-SLZ3-parent-verdict-v1.md 2b7b08a3ec861e953e35d2802d8deba2ae584edeed36f04350fc3a9c6fa1ae24; source 0cfe637f...3c1c + erratum 1 483d9d1b...da59) for the Corollary only.
Lemma CF of proof-CF-XT-v1.md (aa602d45...191f, through erratum-1-CF-XT-ROW-range.md) in the Corollary only.  The unreviewed
TV, MAX and STAB => LS+ texts of the lane are NOT imported; the needed instances are re-derived here.  No computation.

## 0. Statement
Let p >= 7 be prime with p = 1 (mod 3), kappa := (2p + 1)/3 = floor(2p/3) + 1 (so kappa <= p - 2), c := (2p + 1)/3 = 3^(-1) mod 2p.
Theorem BASE1 (STAB(p, kappa)).  An odd sequence Y over C_(2p) with (ZP_kappa), a long zero-sum and |Y| = 3kappa + 1 = 2p + 2 is
E2(kappa) = g^(p+3) (3g)^(p-1) or E3(kappa) = g^(2p-1) (cg)^3 for an odd generator g.  (E3 with h := cg reads h^3 (3h)^(2p-1).)
Corollary BASE1+ (LS+(p, kappa)).  Every odd sequence over C_(2p) with (ZP_kappa) and a long zero-sum has length <= 2p + 2.
Both E2(kappa), E3(kappa) do satisfy (ZP_kappa) and are long zero-sums (S1-sharp erratum 1, items (F1), (F2) of the fix map
for Codex 1 / Claude A-m4, read in the accepted verdict as the sharpness families).

## 1. Proof of the Theorem
A long zero-sum of Y has length >= 2p + 2 = |Y|, so Y =: T is itself a zero-sum, N := |T| = 2p + 2 = 3kappa + 1.  Put u := 2kappa =
(4p + 2)/3, delta := u - p = (p + 2)/3 (odd, >= 3), l := N - u = kappa + 1 = (2p + 4)/3 (even), D := u - l = kappa - 1 = 2delta - 2.
Steps 1-8 are those of proof-S1-sharp-v1.md Sec. 2 (with erratum 1), re-checked at these values:
S1 Every proper nonempty zero-sum of T has length <= 2p + 1, hence is not long, hence (ZP_kappa) gives length <= u; its complement
   too, so lengths lie in [l, u].
S2 A nested split would give a proper zero-sum of length >= 2l = 2kappa + 2 > u.  So all proper zero-sums are minimal.
S3 If no proper zero-sum had length u, T would satisfy (ZP_(kappa-1)) = (ZP_(kappa0)) (its proper zero-sums have length <= u - 2 =
   2kappa0, and N > 2p), contradicting S1-sharp (T has a zero-sum of length N > 2kappa0).  So there is a proper zero-sum Q,
   |Q| = u, Q' := T - Q, |Q'| = l; both minimal; D >= 0.
S4 |Q| = (4p + 2)/3 >= p + 2: index one (n = 2p); the basis element is an odd generator g (orders 1, p give even terms, order 2
   gives length 2); Q = g^m S_Q, coefficients odd in [1, 2p - 1] summing to 2p; mass(S_Q) = 2p - u = p - delta = (2p - 2)/3;
   S_Q nonempty; m = u - |S_Q| >= (p + 3delta)/2 = p + 1; b_min := min S_Q <= p - delta + 1 = (2p + 1)/3; every b in S_Q has
   b <= p - delta - 2|S_Q| + 3.
S5 (MC) For Q1 <= Q, W <= Q' with equal coefficient sums mod 2p, other than (Q, empty) and (empty, Q'): |W| <= |Q1| <= |W| + D.
S6 Every coefficient of Q' is <= D + 1 (the S1-sharp argument: it uses m = p + delta - |S_Q|, D <= 2delta - 2, m >= (p + 3delta)/2
   >= D + 2 and the S4 bounds; all hold here).
S7 A_(Q') = 2p (the S1-sharp argument ends with l <= D; here l = D + 2).
S8 With Q' = g^(t') R (R: terms of Q' other than g): (8a) t' < b_min; (8b) no nonempty Z <= R has A_Z in [b_min - t', b_min - 1];
   (8c) R_low := terms of R with coefficient <= t' has A(R_low) <= b_min - t' - 1.
S9' (equality analysis replacing S1-sharp Step 9).  A_R = 2p - t', |R| = l - t', and with base := (3l - 2p)/2 = 2,
   X := sum over R of (b - 3)/2 = t' - 2 >= 0, so t' >= 2.  Let R_high := terms of R with coefficient > t'.
   - |R_high| <= 1 gives l - t' <= |R_low| + 1 <= (b_min - t' - 1)/3 + 1, so 3l <= b_min + 2t' + 2 <= 3b_min (8a): l <= b_min <=
     (2p + 1)/3 < l.  Impossible; so |R_high| >= 2.
   - t' odd: high terms have b >= t' + 2, so X >= 2(t' - 1)/2 > t' - 2.  Impossible.  So t' is even, and each high term contributes
     >= (t' - 2)/2 to X.
   - t' = 2: X = 0, every term of R is 3g: Q' = g^2 (3g)^((2p-2)/3).
   - t' >= 4: X = t' - 2 forces |R_high| = 2, both equal to (t' + 1)g, and R_low = (3g)^(n3); A_R = 2p - t' gives
     n3 = (2p - 2)/3 - t' >= 0; (8c) gives 3n3 <= b_min - t' - 1, i.e. b_min >= 2p - 1 - 2t'; with b_min <= (2p + 1)/3 this forces
     t' >= (2p - 2)/3.  Hence t' = (2p - 2)/3, n3 = 0, b_min = (2p + 1)/3 = c, and Q' = g^(c-1) (cg)^2.
S10 (Q from Q').  First case, Q' = g^2 (3g)^((2p-2)/3): for b in S_Q write b = i + 3k, i := b mod 3 in {0, 1, 2}, k >= 0; then
   k <= (2p + 1)/9 <= (2p - 2)/3 and W := g^i (3g)^k <= Q' has A_W = b; MC with Q1 := {bg} gives |W| = i + k <= 1, so (i, k) = (0, 1)
   (b >= 3): every term of S_Q is 3g, |S_Q| = mass/2 = (p - 1)/3, m = u - (p - 1)/3 = p + 1, and T = g^(p+3) (3g)^(p-1) = E2(kappa).
   Second case, Q' = g^(c-1) (cg)^2, b_min = c: every term of S_Q has mass >= c - 1 = mass(S_Q), so S_Q = {cg}, m = u - 1 =
   (4p - 1)/3, and T = g^(2p-1) (cg)^3 = E3(kappa).  []

## 2. Proof of the Corollary
Let |Y| >= 2p + 3 with (ZP_kappa) and a long zero-sum; let T be a shortest long zero-sum.  SLZ3 gives |T| <= 3kappa + 1 = 2p + 2, so
|T| = 2p + 2 and some term y of Y lies outside T.  T y satisfies (ZP_kappa), and T is (ZP_kappa) with a long zero-sum of length
2p + 2 = 3kappa + 1, so by the Theorem T = E2(kappa) or E3(kappa).  It remains to show that E2(kappa) y and E3(kappa) y violate
(ZP_kappa) for every odd y (the instance of the lane's unreviewed Lemma MAX needed here, re-derived in CF form; e = (p - 1)/3).
- E2(kappa) = g^(p+3) (3g)^(p-1): CF w.r.t. g gives delta0 = p - 3, U = 1^(p-1).  If y = g: delta0 becomes p - 4 and W = 1^(e-1) has
  rho = e - 1, |W| + 2rho = 3e - 3 = p - 4: forbidden.  Otherwise y adds mu := (c_y - 1)/2 in [1, p - 1]; take rho := min(e - 1, mu - 1)
  and W := 1^(p + rho - mu) {mu} (0 <= p + rho - mu <= p - 1): sigma(W) = p + rho, and |W| + 2rho = p + 1 + 3rho - mu >= p - 3 = delta0
  (if mu <= e, rho = mu - 1 and 3mu - 3 >= mu - 4; if mu > e, rho = e - 1 and 3e - 3 = p - 4 >= mu - 4); |W| + 2rho <= 2p.  Forbidden.
- E3(kappa) = g^(2p-1) (cg)^3: CF w.r.t. g gives delta0 = 1, U = (mu*)^3 with mu* = (c - 1)/2 = (p - 1)/3; y = g gives g^(2p).
  Otherwise put nu(x) := -3mu_x mod p (nu(mu*) = 1).  With delta0 = 1 every nonempty W with rho(W) in [0, e - 1] is forbidden,
  i.e. nu(W) in Phi := {0} u {p - 3rho : 1 <= rho <= e - 1} = {0} u {4, 7, ..., p - 3}.  The four sets (mu*)^t {y}, 0 <= t <= 3, have
  nu = nu_y, ..., nu_y + 3 (nu_y in [1, p - 1]).  If nu_y <= p - 4 these four consecutive integers lie in [1, p - 1] and contain one
  that is = 1 (mod 3) and in [4, p - 3] (as p - 3 = 1, p - 2 = 2, p - 1 = 0 (mod 3)); if nu_y >= p - 3 they contain p, i.e. 0.  Forbidden.
So T y violates (ZP_kappa): contradiction.  []

## 3. Scope and remarks
- Exactly the cell (p, kappa) = (p, (2p + 1)/3), p = 1 (mod 3) prime (p = 7, 13, 19, 31, ...).  Sequence level only; not INV*,
  not ordered Olson.  It is the base cell of STAB and LS+ for these p; the cell p = 2 (mod 3), kappa = (2p + 2)/3 is NOT covered
  (there S2 fails: N = 3kappa, and the S1-sharp verdict's overlay records extra boundary perturbations for p = 2 (mod 3)).
- S9' is the new step: the S1-sharp Step 9 obstruction 'base = 2' is turned into an exact equality analysis.
- Consistency (aid, not premise): probe v12's complete cell p = 7, kappa = 5 found exactly the E2/E3 families at length 16.
