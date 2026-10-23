# Theorem LS+-RED: for p >= 9e - 13 every LS+ counterexample has a single dominant generator and an index-one core with
# a in {-1, -1/2}; the two-heavy-value case is impossible, v1

Owner OlsonSTABSuccessor (Slice A).  Written after /bin/date 2026-10-19T06:09:38-0700.  Status: CANDIDATE, written proof [W], UNREVIEWED.  LS+ is NOT
proved here (case (alpha) remains); this is a reduction with one case closed.
Dependencies (exact): Lemma CF (proof-CF-XT-v1.md aa602d45e154a7787ac3f0270a3c26deb5e8c6a70736cf4a82c700f5368c191f) and the accepted prerequisite package (parent verdict run
review/olson-CFXT-ROW-LSII-parent-verdict-v1.md ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0, incl. erratum-2-prereq-consolidated.md fb136e6e...06d5); Lemma CT
(proof-LSplus-e2-v1.md 2effb09ea4e28553ab0321a64b3e660c422d767ef940fcf58615dec8edc208b1, candidate); Lemma CTgen (lemma-CTgen-v1.md 462d52aa1c6708a1071e06e0d88d0558b7f58e00c14bd42565655a123f92e5ad, candidate);
parent-accepted SLZ3 (verdict 2b7b08a3ec861e953e35d2802d8deba2ae584edeed36f04350fc3a9c6fa1ae24; cut-down to length 3kappa + 2 only); the index-one theorem (parent import record
e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6) with n = p; the greedy subset-sum step of proof-LSplus-e2-v1.md Sec. 3 (C).  No LS/LS+/STAB hypothesis; no computation.
Credit context [INFERENCE, scout v3]: the index-one/greedy steps are Savchev-Chen 2007 Thm 8 / Prop 5; not imports beyond the record.

## 0. Setting and statement
p prime, floor(2p/3) + 1 <= kappa <= p - 2, e := p - kappa (so 3e <= p - 1), e >= 3 (e = 2 is Theorem LS+2), and p >= 9e - 13.
An LS+ counterexample is an odd Y over C_(2p) with (ZP_kappa), a zero-sum of length >= 2p + 2 and |Y| >= 3kappa + 2; by SLZ3 (a shortest
long zero-sum has length <= 3kappa + 1) we may cut it to |Y| = 3kappa + 2 = 3p - 3e + 2 keeping a long zero-sum.
Theorem LS+-RED.  For such Y (length 3kappa + 2): (A) exactly one odd value exceeds multiplicity kappa; it is a generator g with
v_g(Y) >= 2p - 3e + 4 (delta0 := 2p - v_g <= 3e - 4).  (B) With CF data (delta0, U) w.r.t. g, an inclusion-maximal mod-p zero-sum
Z0 <= U has |Z0| <= delta0 - 1, U' := U - Z0 is zero-sum-free over Z_p, and U' = (x_u a)_(u in U') with integers x_u >= 1,
S' := sum x_u <= p - 1, and a in {-1, -1/2}; with delta' := delta0 - |Z0| >= 1 and E' := S' - |U'|: delta' + E' <= 2e - 2 if a = -1 and
delta' + E' <= e - 1 if a = -1/2.

## 1. Proof of (A)
CT with n := kappa (|Y| - n = 2kappa + 2, even, in the window): sum_x min(kappa, v_x) <= p + kappa - 2 = 2p - e - 2, so the excess over
kappa is >= (3p - 3e + 2) - (2p - e - 2) = p - 2e + 4 >= 1.  Three values above kappa would need 3kappa <= 2p - e - 2, i.e. p <= 2e - 2: no.
By CTgen (N = 3kappa + 2) the involution has multiplicity <= kappa, so every value above kappa is a generator.
- One value g above kappa: v_g - kappa >= p - 2e + 4, i.e. v_g >= 2p - 3e + 4.  This is (A).
- Two values u, v above kappa (case (beta)): they contribute 2kappa to the truncated sum, so the remaining terms R number at most
  e - 2.  v_u + v_v >= 3p - 4e + 4.  Not both are >= p (u^p v^p would be a zero-sum of length 2p, C_p-sum p(alpha + beta) = 0); not both
  <= p - 1 (else 2p - 2 >= 3p - 4e + 4, p <= 4e - 6).  Say v_u >= p > v_v >= p - e + 1; then v_u >= 2p - 4e + 5.  Sec. 2 shows (beta) is
  impossible, which proves (A).
## 2. Case (beta) is impossible
g := u (a generator), M = v_u, delta0 = 2p - M in [1, 4e - 5] (M <= 2p - 1); U = mu1^(v1) R' with v1 := v_v in [p - e + 1, p - 1],
mu1 := mu(v) != 0, s := |R'| <= e - 2.  r = v1 + s <= p + e - 3, so every W <= U with rho(W) <= e - 1 has |W| + 2rho(W) <= 2p and CF (F)
gives (F*): rho(W) <= e - 1 implies |W| + 2rho(W) <= delta0 - 1.
Step 1 (mu1 = 1, delta0 >= 3e - 2).  Let x1 := mu1^(-1) and t_rho in [1, p - 1], t_rho = rho x1 (mod p), rho in [1, e - 1].  If
t_rho <= v1, W = mu1^(t_rho) has residue rho, so t_rho + 2rho <= delta0 - 1.  Hence the signed representative t~_rho is in
[1, delta0 - 1 - 2rho] or in [-(p - 1 - v1), -1], all inside [alpha, beta] := [-(e - 2), 4e - 8].  With x~ := t~_1, each
(t~_rho + x~) - t~_(rho+1) is = 0 (mod p) and lies in [2alpha - beta, 2beta - alpha] <= [-(6e - 12), 9e - 18], so it is 0 (p >= 9e - 13):
t~_rho = rho x~.  If x~ < 0 then (e - 1)|x~| <= p - 1 - v1 <= e - 2: impossible.  So x~ > 0 and (e - 1)(x~ + 2) <= delta0 - 1 <= 4e - 6 <
4(e - 1): x~ = 1 (mu1 = 1, v = 3g) and delta0 >= 3e - 2.  Then v_u = 2p - delta0 <= 2p - 3e + 2, so s = |Y| - v_u - v1 >= 1, and
v1 = p - 3e + 2 + delta0 - s.
Step 2 (the extra terms).  Let mu0 in [2, p - 1] be the mu-value of a term of R' (mu0 != 0, 1).  Sets W = 1^t u {mu0} (0 <= t <= v1)
have integer sum t + mu0.
(i) If mu0 <= p + 1 - delta0 and v1 + mu0 >= p: t := p - mu0 in [1, v1] gives residue 0 and |W| = p - mu0 + 1 >= delta0: against (F*).
(ii) If mu0 = p - m with 1 <= m <= delta0 - 2: t := m + e - 1 <= v1 (as v1 >= p - e + 1 >= 5e - 8 >= m + e - 1, using p >= 6e - 9) gives
     residue e - 1 and |W| + 2(e - 1) = m + 3e - 2; so (F*) forces m <= delta0 - 3e + 1.
(iii) Otherwise mu0 <= p - 1 - v1 = 3e - 3 - delta0 + s <= s - 1.
Let R+ be the terms of type (iii) ('positive', mu0 >= 2) with P := sum mu0 >= 2|R+|, and R- those of type (ii) ('negative') with
N := sum (m + 1) >= 2|R-|; |R+| + |R-| = s >= 1.
(iv) v1 + P <= p - 1.  Else add the R+ terms one at a time; the first partial sum P_k with v1 + P_k >= p has P_k <= 2s - 2; then
     W := 1^(p - P_k) u (those k terms) has 1 <= p - P_k <= v1, residue 0 and |W| >= p - 2s + 3 >= delta0 (p >= 6e - 12): against (F*).
(v) N <= delta0 - 3e + 2.  Else add the R- terms one at a time; the first partial sum N_k >= delta0 - 3e + 3 has N_k <= 2delta0 - 6e + 4 <=
     2e - 6; with M_k := N_k - k, W := 1^(M_k + e - 1) u (those k terms) has M_k + e - 1 <= 3e - 7 <= v1, integer sum kp + e - 1 (residue
     e - 1) and |W| + 2(e - 1) = N_k + 3e - 3 >= delta0: against (F*).
(vi) From v1 = p - 3e + 2 + delta0 - s and (iv): delta0 <= 3e - 3 + s - P; with (v): N + 3e - 2 <= delta0.  So N + P <= s - 1 < 2s <= N + P.
Contradiction.  []
## 3. Proof of (B)
g as in (A); r = |U| = p - 3e + 2 + delta0 <= p - 2, so (F*) holds as in Sec. 2.  (F*) with rho = 0 gives |Z0| <= delta0 - 1; U' is
zero-sum-free; applying (F*) to W' u Z0: every W' <= U' with rho(W') <= e - 1 has |W'| + 2rho(W') <= delta' - 1.  |U'| = p - 3e + 2 + delta'
>= p - 3e + 3, so U' (-sigma(U')) is a minimal zero-sum of length >= (p + 3)/2 = floor(p/2) + 2 and 2|U'| >= p + 1 (p >= 6e - 5): index
one gives u = x_u a, S' <= p - 1 (so delta' + E' <= 3e - 3), and every integer in [0, S'] is an x-sum.  For rho in [1, e - 1] let
s_rho = rho a^(-1) (mod p) in [1, p - 1]: if s_rho <= S' a sub-multiset with x-sum s_rho has residue rho and >= s_rho - E' elements, so
s_rho <= delta' + E' - 1 - 2rho <= 3e - 4 - 2rho; otherwise s~_rho is in [-(p - 1 - S'), -1] with p - 1 - S' = 3e - 3 - delta' - E' <= 3e - 4.
All s~_rho lie in [-(3e - 4), 3e - 6]; consecutive differences of the lifted sequence lie in [-(9e - 14), 9e - 16] and are = 0 (mod p),
hence 0 (p >= 9e - 13): s~_rho = rho x~ with x~ := s~_1.  x~ > 0 would give (e - 1)x~ <= 3e - 4 - 2(e - 1) = e - 2 < e - 1: impossible.  So
x~ < 0 and (e - 1)|x~| <= 3e - 3 - delta' - E' <= 3e - 4 < 3(e - 1): |x~| in {1, 2}, i.e. a = -1 (then delta' + E' <= 2e - 2) or a = -1/2
(then delta' + E' <= e - 1).  []

## 4. Remaining for LS+ (exact) and next lever
LS+(p, kappa) for p >= 9e - 13 reduces to excluding (A)+(B) with a = -1 (U' consists of the elements -(2x_u - 1)g, mostly -g) or a = -1/2
(U' mostly involutions: x_u = 1 gives mu = (p - 1)/2).  Levers: pair removal (g, -c'g) inside a long zero-sum (as in LS-II' Step 5') and
even deletion of involutions (CTgen) force every long zero-sum to contain almost all non-involution terms; together with the
first-crossing bounds on Z0 (as in LS-lin Step 6) this is the next bounded step.  The band p < 9e - 13 needs other tools (scout v3:
Gao-Li-Yuan-Zhuang 2015, Chen-Savchev 'shorter long' theorem in C_p coordinates) [INFERENCE].  Sequence level only.
