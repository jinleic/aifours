# LS at the first p = 2 (mod 3) cells: LS(17, 12), LS(23, 16), and Lemma B2-1 (delta0 = 1 is impossible at every BASE2 cell), v2

Owner OlsonSTABSuccessor (Slice A, slice BASE2).  Written after /bin/date 2026-10-19T07:54:22-0700.  Status: CANDIDATE, written proof [W],
UNREVIEWED.  v2 supersedes v1 (proof-LS-BASE2-cells-v1.md 16fda0d6c38df327fbfd2a180b2b378fed7ded9c5bfae60b8cec13a13296c302, never sent): in Sec. 3 the exclusion of
nonempty zero-sum W' <= U' is attributed to the zero-sum-freeness of U' (for Z0 empty, (F') alone allows |W'| <= 2); nothing else changed.  Scope frozen first: BASE2-scope-v1.md (59eae7d2187f91c1f49a557b43ed849fe35981850e9cbaf4b17996b240828839), statements S1, S2 (and S3 partially).  No computation.
LS, LS+, STAB are not assumed.  Sequence level only; no INV*, ordered-Olson, novelty or priority claim.

## 0. Imports (accepted; exact)
- Prerequisite verdict run review/olson-CFXT-ROW-LSII-parent-verdict-v1.md (ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0): CF (a) through erratum-1 E1 and
  CF (b) through erratum-2-prereq R4; DGM-p; the LS-threshold dichotomy (items 1, 5, 6).
- Delta verdict run review/olson-STAB-delta-parent-verdict-v1.md (ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5): LS-II' (item 1); Proposition I-small at its literal
  hypotheses and Lemma AP' with the proof D1 of erratum-1-delta-APprime.md (item 2); the greedy step of proof-LSplus-e2-v1.md Sec. 3 (C)
  (part of item 4, as used in the LS+ chain verdict with r := |U'|).
- RED (review/olson-KPS-SLZ-parent-verdict-v1.md): LS(p, kappa) fails iff some odd Y of length exactly p + 2kappa + 1 has (ZP_kappa) and a
  long zero-sum.  SLZ3 (review/olson-SLZ3-parent-verdict-v1.md 2b7b08a3ec861e953e35d2802d8deba2ae584edeed36f04350fc3a9c6fa1ae24): a SHORTEST long zero-sum T has |T| <= 3kappa + 1.
- Index-one record (run of 2026-10-16, review/olson-index-one-primary-statement-parent-v1.md e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6) at n = p,
  only where its length hypothesis is checked.  No Zeng-Yuan or Savchev-Chen statement is imported.

## 1. Setting
BASE2 cell: p = 6m - 1 prime (m >= 3: p = 17, 23, 29, 41, ...), kappa = (2p + 2)/3 = 4m = floor(2p/3) + 1, e := p - kappa = 2m - 1,
thr := p + 2kappa + 1 = 14m.  Let Y be a threshold LS counterexample: odd, |Y| = thr, (ZP_kappa), a zero-sum of length >= 2p + 2.  DGM-p
gives the dominant generator g := g0; CF data w.r.t. g: M = v_g(Y) = 2p - delta0, U the mu-multiset of the other terms (mu in [1, p - 1]),
rho(W) := sigma(W) mod p.  By LS-II' Y is in case (I) of the dichotomy: 1 <= delta0 <= e - 2 = 2m - 3 and r := |U| = p - 2e + 1 + delta0 =
2m + 2 + delta0.  As r + 2e - 2 <= 2p, CF (F) gives
  (F*) every W <= U with rho(W) <= e - 1 = 2m - 2 has |W| + 2rho(W) <= delta0 - 1.
Z0: an inclusion-maximal sub-multiset of U with sum = 0 (mod p) (possibly empty); (F*) gives |Z0| <= delta0 - 1; U' := U - Z0 is zero-sum-free;
delta' := delta0 - |Z0| >= 1; |U'| = 2m + 2 + delta'.  Applying (F*) to W' u Z0 (same residue):
  (F') every W' <= U' with rho(W') <= 2m - 2 has |W'| + 2rho(W') <= delta' - 1.
Lemma L1 (the shortest long zero-sum has length 2p + 2).  There is W* <= U with sigma(W*) = -1 (mod p) and |W*| >= delta0 + 2.
Proof.  A shortest long zero-sum T has |T| >= 2p + 2 ((ZP_kappa)), |T| <= 3kappa + 1 = 2p + 3 (SLZ3; kappa = floor(2p/3) + 1 <= p - 1), and
|T| even: |T| = 2p + 2.  Write T = g^i W*, W* <= U, i <= M.  Its g-coefficient sum i + |W*| + 2sigma_int(W*) = 2p + 2 + 2sigma_int(W*) (sigma_int: the
integer sum of the mu) is = 0 (mod 2p), so sigma_int(W*) = -1 (mod p); and i = 2p + 2 - |W*| <= M = 2p - delta0 gives |W*| >= delta0 + 2.  []

## 2. Lemma B2-1: at every BASE2 cell, delta0 = 1 is impossible
Proof.  delta0 = 1: Z0 is empty and (F*) says: no nonempty W <= U has rho(W) in [0, 2m - 2].  |U| = 2m + 3.
(a) A := Sigma(U) u {0} (Sigma: nonempty subset sums), sigma := sigma(U).  Prefix sums of the zero-sum-free U (any order) are distinct and
nonzero, so |A| >= 2m + 4.  Complementation W -> U - W gives A = sigma - A.  A avoids [1, 2m - 2], hence also [sigma - 2m + 2, sigma - 1].  As
sigma is in Sigma(U), sigma is not in [0, 2m - 2].  If sigma >= 4m - 3, the two arcs are disjoint (sigma - 2m + 2 >= 2m - 1) and lie in
[1, p - 1], so |A| <= p - (4m - 4) = 2m + 3: contradiction.  So 2m - 1 <= sigma <= 4m - 4, the arcs merge into [1, sigma - 1], and
A <= {0} u [sigma, p - 1].
(b) Put Y' := -U (termwise) and B := p - sigma, so 2m + 3 <= B <= 4m (the lower bound from |A| >= 2m + 4).  Every nonempty subset sum of
Y' lies in [1, B] (mod p); each term of Y' is identified with its representative in [1, B].  Z* := -W* (Lemma L1) satisfies
sigma(Z*) = 1 (mod p), t := |Z*| >= 3.
(c) For a proper nonempty V of Z*, sigma(V) = x in [1, B] and sigma(Z* - V) = 1 - x must lie in [1, B]: x = 1 gives 0, and for x >= 2 the
residue p + 1 - x lies in [1, B] iff x >= p + 1 - B.  So every proper nonempty subset sum of Z* lies in J := [6m - B, B]; in particular every
term of Z* lies in J.  If B <= 3m - 1, J is empty: contradiction (t >= 2).
(d) 3m <= B <= 4m - 1.  For two terms z, z' of Z*: z + z' >= 12m - 2B > B, so its residue in J forces z + z' = p + y, y in J.  If t >= 4, a
proper triple has integer sum in [18m - 1 - 2B, 3B] <= [10m + 1, 12m - 3]; subtracting p gives [4m + 2, 6m - 2], disjoint from J, and
subtracting 2p gives negative numbers: contradiction.  So t = 3, and z1 + z2 + z3 lies in [18m - 3B, 3B] <= [6m + 3, 12m - 3] and is = 1
(mod p); the candidates 6m = p + 1 and 12m - 1 = 2p + 1 lie outside: contradiction.
(e) B = 4m, J = [2m, 4m].  Two terms: z + z' in [4m, 8m] with residue in J: z + z' = 4m (z = z' = 2m) or z + z' in [8m - 1, 8m].  A proper triple
(t >= 4) has sum in [8m - 1, 10m - 1]; if one of its pairs has sum >= 8m - 1, its third term is <= 2m, hence = 2m, and 2m + z in
{4m} u [8m - 1, 8m] with z <= 4m forces z = 2m, so that pair is (2m, 2m) with sum 4m < 8m - 1: contradiction; so all its pairs are (2m, 2m)
and its sum is 6m = p + 1, residue 1, not in J: contradiction.  So t = 3 with sum 6m or 12m - 1: Z* = (2m)^3, or (pair sums 12m - 1 - z_k in
{4m} u [8m - 1, 8m]) Z* = (4m - 1, 4m, 4m).
(f) Y' has 2m + 3 >= 4 terms; let y (in [1, 4m]) be a term outside Z*.  For Z* = (2m)^3 the sums y + 2m, y + 4m, y + 6m (= y + 1) must lie in
[1, 4m] (mod p): y + 1 <= 4m gives y <= 4m - 1; then y + 4m in [4m + 1, 8m - 1] needs y + 4m >= p + 1 = 6m, i.e. y >= 2m; then y + 2m in
[4m, 6m - 1] needs y + 2m <= 4m (6m - 1 = p is 0): y = 2m.  So Y' = (2m)^(2m + 3), and five of its terms sum to 10m = p + 4m + 1, residue
4m + 1 > B: contradiction.  For Z* = (4m - 1, 4m, 4m): y + 1 <= 4m gives y <= 4m - 1; y + 4m needs y >= 2m (as before) and y + 4m != p
(automatic); y + 4m - 1 needs y >= 2m + 1 (y = 2m gives p, i.e. 0); then y + (4m - 1) + 4m = y + 8m - 1 has residue y + 2m in
[4m + 1, 6m - 1], not in [1, 4m] (6m - 1 = p is 0): contradiction.  []

## 3. Theorem B2-17: LS(17, 12)
p = 17 (m = 3), kappa = 12, e = 5, delta0 in [1, 3], r = 8 + delta0.  delta0 in {1, 2}: Proposition I-small applies (delta0 <= 2 and
4e = 20 <= p + 1 + 2delta0 = 18 + 2delta0).  delta0 = 3: (F*) says no W <= U has rho(W) in [1, 4] (|W| + 2rho >= 3 > 2), and a W with
rho(W) = 0 has |W| <= 2; so |Z0| in {0, 2}, |U'| in {11, 9}, and no nonempty W' <= U' has rho(W') in [0, 4] (rho = 0: U' is
zero-sum-free; rho in [1, 4]: (F*) as just stated).
Index one: U' is nonempty and zero-sum-free, so sigma(U') != 0 and U'(-sigma(U')) is a minimal zero-sum over C_17 (a proper nonempty
zero-sum omitting -sigma(U') would lie in U'; one containing it has a nonempty zero-sum complement in U'), of length |U'| + 1 >= 10 =
floor(17/2) + 2.  So u = x_u a (u in U'), a != 0, integers x_u >= 1 summing with the coefficient (>= 1) of -sigma(U') to 17: S' := sum x_u
<= 16.  Greedy (S' <= 16 < 18 <= 2|U'|): every s in [0, S'] is the x-sum of some W'_s <= U'.  For rho in [1, 4] the residue
s_rho := rho a^(-1) mod 17 cannot be <= S' (W'_(s_rho) would be nonempty with residue rho), so s_1, ..., s_4 lie in the arc [S' + 1, 16] of
size <= 16 - |U'| <= 7.  AP' (n = 3, 3n + 2 = 11 < 17; proof D1) gives a^(-1) in {1, 2, -1, -2}.  a^(-1) = 1 or 2 puts s_1 = 1 or 2 <= S'
(S' >= 9); a^(-1) = -2 puts s_4 = 9 <= S'; so a = -1, i.e. every u in U' is = -x_u.
- |Z0| = 2: Z0 = {z1, z2} with residues summing to 0; one of them, z, has residue nu in [1, 8].  W := {z} u W'_s has residue nu - s.  nu in
  [1, 4] (s = 0) or nu in [5, 8] (s = nu - 1 in [4, 7] <= S') gives a residue in [1, 4]: excluded.  So |Z0| = 2 is impossible.
- Z0 empty: by Lemma L1, W* <= U = U' has sigma(W*) = -s* = -1 with s* its x-sum in [1, S'] <= [1, 16], so s* = 1 and |W*| <= 1 <
  delta0 + 2: contradiction.
By RED, LS(17, 12) holds.  []

## 4. Theorem B2-23: LS(23, 16)
p = 23 (m = 4), kappa = 16, e = 7, delta0 in [1, 5], r = 10 + delta0, |U'| = 10 + delta'; (F*) with delta0 - 1 <= 4 forbids every W with
rho(W) in [2, 6], allows rho(W) = 1 only if |W| <= delta0 - 3, and rho(W) = 0 only if |W| <= delta0 - 1.
delta0 = 1: Lemma B2-1.  delta0 = 2: Proposition I-small (4e = 28 <= p + 1 + 2delta0 = 28).  So let delta0 in {3, 4, 5}.
Case delta' >= 2 (|U'| >= 12).  As in Sec. 3: U'(-sigma(U')) is a minimal zero-sum of length >= 13 = floor(23/2) + 2, so u = x_u a,
S' <= 22, and (2|U'| >= 24 > S') every s in [0, S'] is the x-sum of some W'_s, with |W'_s| >= s - E' (E' := S' - |U'|).  By (F'), a nonempty
W' with rho(W') in [2, 6] is impossible (|W'| + 2rho >= 5 > delta' - 1), and rho(W') = 1 needs delta' >= 4.  So s_2, ..., s_6 (and s_1 if
delta' <= 3) lie in [S' + 1, 22], an arc of size <= 22 - |U'| = 12 - delta'.  For delta' in {2, 3}: six points s_1..s_6 in an arc of size
<= 10 (AP', n = 5, 3n + 2 = 17 < 23); for delta' in {4, 5}: five points s_2..s_6 (difference a^(-1)) in an arc of size <= 8 (AP', n = 4,
14 < 23).  So a^(-1) in {1, 2, -1, -2}; 1 and 2 put s_2 = 2 or 4 <= S' (S' >= 12), -2 puts s_6 = 11 <= S'; so a = -1, and s_6 = 17 > S'
gives S' <= 16.
Z0 (|Z0| = delta0 - delta' <= 3): let z in Z0 have residue zeta in [1, 22].  If zeta <= S', put rho := min(zeta, 6), s := zeta - rho in [0, S']:
W := {z} u W'_s has residue rho in [1, 6], so (F*) forces rho = 1, i.e. zeta = 1.  If S' + 1 <= zeta <= S' + 6, W := {z} u U' has residue
zeta - S' in [1, 6] and |W| >= 13: excluded.  Otherwise nu := 23 - zeta is in [1, 16 - S'] <= [1, 4].  So every z in Z0 has signed
representative z~ = 1 or z~ = -nu in [-4, -1]; if q terms have z~ = 1, these q terms form a W with residue q and |W| + 2q = 3q <= 4, so q <= 1.
The signed sum of Z0 lies in [-12, 1] and is = 0 (mod 23), hence is 0.
Lemma L1: W* = W*' u Z* (W*' <= U' of x-sum s* in [|W*'|, S'], Z* <= Z0) with sigma(W*) = sigma~(Z*) - s* = -1 (mod 23), where the integer
sigma~(Z*) (sum of the z~) lies in [-12, 1]; so sigma~(Z*) - s* in [-28, 1] is -1 or -24.  If -24: s* <= 16 forces sigma~(Z*) <= -8, but the
negative part of Z0 has total |sum| <= 1 (signed sum 0, at most one +1): contradiction.  If -1: s* = sigma~(Z*) + 1 <= 2, so
|W*| <= 2 + |Z*| <= 2 + delta0 - delta' <= delta0 < delta0 + 2: contradiction.
Case delta' = 1 (|U'| = 11, |Z0| = delta0 - 1 in {2, 3, 4}).  (F') says no nonempty W' <= U' has rho(W') in [0, 6]; Lemma B2-1 (a) applied to
U' (same argument: |A'| >= 12 for A' := Sigma(U') u {0}) gives sigma' := sigma(U') in [7, 12] and A' <= {0} u [sigma', 22] <= {0} u [7, 22].
Let z in Z0 with residue zeta.  (i) W = {z} u W' (any W' <= U'): rho(W) in [2, 6] gives |W| + 2rho >= 5 > delta0 - 1; so A' avoids
[2 - zeta, 6 - zeta].  (ii) W = (Z0 - {z}) u W': |W| >= delta0 - 2 and residue -zeta + sigma(W'); rho(W) in [1, 6] gives |W| + 2rho >= delta0;
so A' avoids [1 + zeta, 6 + zeta].  As 0 is in A': zeta is not in [2, 6] by (i) and not in [17, 22] by (ii).  For zeta in [7, 16] the two arcs
remove from [7, 22] at least 6 residues (zeta = 12: [13, 18]; the other values remove 7 to 11), leaving <= 10, so |A'| <= 11 < 12:
contradiction.  Hence every z in Z0 has zeta = 1, and sigma(Z0) = |Z0| in {2, 3, 4} is not 0 (mod 23): contradiction.
(Counts, for the record: zeta = 7, 8, 9, 15, 16 remove 11; zeta = 10, 14 remove 9 and 10; zeta = 11, 13 remove 7 and 8; zeta = 12 removes 6.)
By RED, LS(23, 16) holds.  []

## 5. Scope, exact residual for S3, credit
- Proved here (candidates): LS(17, 12), LS(23, 16) (sequence level, relative to Sec. 0), and Lemma B2-1 at every BASE2 cell.
- S3 (all BASE2 cells p = 6m - 1 >= 29) is NOT proved.  Residual: case (I) with 2 <= delta0 <= 2m - 3 (delta0 = 2 is covered by I-small only
  for m <= 4).  Failing steps: index one needs delta' >= m - 2; for 2 <= delta' <= m - 3 neither index one nor the delta' = 1 symmetry argument
  applies; and for delta0 >= 6 (F*) no longer forbids every residue >= 2 for single Z0-terms, so the Sec. 4 Z0-analysis does not transfer.
- New LS cells relative to the accepted coverage: (17, 12) and (23, 16).  No LS+ or STAB statement is made at these cells.
- Credit context [INFERENCE, not imports]: the index-one and greedy inputs are classical (Savchev-Chen 2007 per the scout record); the
  complement-symmetry and interval arguments of Lemma B2-1 are elementary; no literature search was made for these cells.
