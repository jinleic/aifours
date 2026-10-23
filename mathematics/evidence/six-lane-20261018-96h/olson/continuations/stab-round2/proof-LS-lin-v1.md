# Theorem LS-lin: LS(p, kappa) whenever p >= 6(p - kappa) - 10 (case (I) closed via a zero-sum-free core), v1

Owner OlsonSTABSuccessor (Slice A).  Written after /bin/date 2026-10-19T05:58:53-0700.  Status: CANDIDATE, written proof [W], UNREVIEWED.
Dependencies (exact):
- accepted Corollary RED (proof-SLZ-EXT-v2.md + erratum 1; review/olson-KPS-SLZ-parent-verdict-v1.md): LS(p, kappa) fails iff some
  odd Y of length p + 2kappa + 1 has (ZP_kappa) and a long zero-sum;
- Lemma CF (proof-CF-XT-v1.md aa602d45e154a7787ac3f0270a3c26deb5e8c6a70736cf4a82c700f5368c191f), Lemmas RS, DGM-p, ROW and the LS-threshold dichotomy (proof-ROW-v1.md
  a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d), read through erratum-1-CF-XT-ROW-range.md (767fe8f8605019b3b3b7aa1ff6a610f088279ede30b9b3429544d4c8487c1db7) and
  erratum-2-prereq-consolidated.md (fb136e6ef71f7250774c3102a35c88a9709fee827091df84f67b433fb13106d5);
- Theorem LS-II' (unconditional exclusion of case (II)): proof-LS-caseII-v2.md (3df159ff61784cb3345b27a6cf9da873900051df92dbb3be019e846578d73a43) Steps 1-4
  + proof-LS-caseII-v2-addendum-1.md (c289db226c86ea7703af4a23c4a93dce543669cb911d36b5845e70aad2c98718) Step 5', Lemma AP read through erratum-2 R6 -- CANDIDATE;
- the index-one theorem exactly as in the parent import record (run of 2026-10-16, review/olson-index-one-primary-statement-parent-
  v1.md, e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6), with n = p prime.
Not used: S1-sharp, SH, SLZ3, AP', LS-small, any LS/LS+/STAB hypothesis.  No computation.

## 0. Statement
Theorem LS-lin.  Let p be prime and kappa an integer with floor(2p/3) + 1 <= kappa <= p - 2, e := p - kappa.  If e >= 3 and
p >= 6e - 10, then every odd sequence over C_(2p) with (ZP_kappa) and |Y| >= p + 2kappa + 1 satisfies (S1_kappa), i.e. LS(p, kappa).
(For e = 3 the condition is automatic: the range forces p >= 11.  With e = 2 covered by proof-LSplus-e2-v1.md and by
proof-LS-caseI-smalldelta-v1.md, LS holds in every cell with p - kappa <= (p + 10)/6, i.e. kappa >= (5p - 10)/6 -- relative to the
candidates above.)

## 1. Proof
Step 1 (case (I)).  By RED let Y be odd, |Y| = 3p - 2e + 1, (ZP_kappa), with a long zero-sum.  DGM-p gives g := g0 with M >= 2kappa + 3;
CF data delta0 = 2p - M <= 2e - 3, U with r = |U| = p - 2e + 1 + delta0.  Case (II) is impossible (LS-II'), so every mu-value has
multiplicity <= K := p - 2e + 1, and ROW gives r <= p - e - 1, i.e. delta0 <= e - 2 (so e >= 3).
Step 2 ((F*)).  If W <= U has rho(W) <= e - 1 then |W| + 2rho(W) <= r + 2e - 2 <= p + e - 3 <= 2p, so CF (F) gives
    (F*)  every W <= U with rho(W) <= e - 1 has |W| + 2rho(W) <= delta0 - 1.
Step 3 (core).  Let Z0 be an inclusion-maximal sub-multiset of U with sum 0 mod p (possibly empty).  (F*) (rho = 0) gives
|Z0| <= delta0 - 1 <= e - 3.  U' := U - Z0 is zero-sum-free over Z_p (a zero-sum in U' would enlarge Z0).  Put delta' := delta0 - |Z0| >= 1;
|U'| = p - 2e + 1 + delta'.  Applying (F*) to W' u Z0 (same residue, size |W'| + |Z0|):
    (F')  every W' <= U' with rho(W') <= e - 1 has |W'| + 2rho(W') <= delta' - 1.
Step 4 (index one).  U' (-sigma(U')) is a minimal zero-sum over C_p of length |U'| + 1 >= p - 2e + 3 >= floor(p/2) + 2 (p >= 4e - 3, which
follows from p >= 6e - 10 for e >= 4 and from p >= 11 for e = 3).  So u = x_u a (u in U') with a != 0, integers x_u >= 1 and
S' := sum x_u <= p - 1.  Put E' := S' - |U'| >= 0; then delta' + E' <= 2e - 2.  As 2|U'| >= p + 1, the greedy argument of
proof-LSplus-e2-v1.md Sec. 3 (C) shows every integer in [0, S'] is an x-sum of a sub-multiset of U'; a sub-multiset with x-sum s has
at least s - E' elements.
Step 5 (a = -1).  For rho in [1, e - 1] let s_rho in [1, p - 1], s_rho = rho a^(-1) (mod p).  If s_rho <= S', a sub-multiset with x-sum
s_rho has residue rho and at least s_rho - E' elements, so (F') gives s_rho <= delta' + E' - 1 - 2rho <= 2e - 3 - 2rho.  Otherwise
s_rho >= S' + 1.  With signed representatives: s~_rho is in [1, 2e - 3 - 2rho] or in [-(p - 1 - S'), -1], where
p - 1 - S' = 2e - 2 - delta' - E' <= 2e - 3; all s~_rho lie in [alpha, beta] := [-(2e - 3), 2e - 5].  Put x~ := s~_1.  For rho <= e - 2,
(s~_rho + x~) - s~_(rho+1) is = 0 (mod p) and lies in [2alpha - beta, 2beta - alpha] = [-(6e - 11), 6e - 13]; as p >= 6e - 10 it is 0.  So
s~_rho = rho x~ (integers) for 1 <= rho <= e - 1.  If x~ > 0, s~_(e-1) > 0 would lie in [1, -1]: impossible.  So x~ < 0 and
(e - 1)|x~| <= p - 1 - S' <= 2e - 3 < 2(e - 1): x~ = -1, a = -1, and delta' + E' <= e - 1 (so E' <= e - 2 and p - S' <= 2e - 2).
Every u in U' is = -x_u (mod p).
Step 6 (Z0 is small).  For z in Z0 let zeta_z in [1, p - 1] be its residue.  If zeta_z <= S', then {z} u W' with W' <= U' of x-sum zeta_z has
sum 0 (mod p) and at least 1 + zeta_z - E' elements, so (F*) gives zeta_z <= delta0 + E' - 2 <= 2e - 6: put z~ := zeta_z ('positive').
Otherwise z~ := zeta_z - p in [-(p - 1 - S'), -1] ('negative').  For Z'' <= Z0 let zeta~(Z'') := sum of z~ (an integer = sigma(Z'') mod p).
(6a) The positive z~ sum to <= e - 2.  Else add them one at a time; the first partial sum zeta~ >= e - 1 has zeta~ <= 3e - 8.  For that Z''
     and W'' <= U' of x-sum zeta~ - (e - 1) in [0, 2e - 7] <= [0, S'], W := Z'' u W'' has integer sum e - 1 (residue e - 1) and
     |W| + 2(e - 1) >= 1 + zeta~ - (e - 1) - E' + 2(e - 1) >= e + 1 > delta0: against (F*).
(6b) The negative z~ sum to >= -(p - S') + 1.  Else add them one at a time; the first partial sum zeta~ <= -(p - S') has
     zeta~ >= -2(p - S') + 2 >= -(4e - 6).  For that Z'' and W'' <= U' of x-sum p + zeta~ in [p - 4e + 6, S'] <= [0, S'], W := Z'' u W'' has
     integer sum -p (residue 0) and |W| >= 1 + p - 4e + 6 - (e - 2) = p - 5e + 9 >= delta0 (p >= 6e - 11): against (F*).
So zeta~(Z'') is in [-(p - S') + 1, e - 2] for every Z'' <= Z0.
Step 7 (no long zero-sum).  By CF (b) (M <= 2p - 1) a zero-sum of length >= 2p + 2 needs W* <= U with rho(W*) >= 1 and
|W*| + 2rho(W*) >= 2p + delta0 (as in proof-LSplus-e2-v1.md Sec. 3 (E)).  Write W* = W' u Z'' (W' <= U' of x-sum s in [|W'|, S'],
Z'' <= Z0), and sigma~ := zeta~(Z'') - s, an integer = sigma(W*) (mod p) with -p + 1 <= sigma~ <= e - 2.
- sigma~ >= 0: rho(W*) = sigma~ and |W*| + 2rho(W*) <= s + |Z''| + 2zeta~ - 2s <= (e - 3) + 2(e - 2) < 2p.
- sigma~ <= -1: rho(W*) = p + sigma~ and |W*| + 2rho(W*) <= 2p + |Z''| + 2zeta~ - s.  If this were >= 2p + delta0, then with s >= zeta~ + 1,
  zeta~ >= delta0 + 1 - |Z''| >= 2 (|Z''| <= delta0 - 1); then W := Z'' has residue zeta~ in [2, e - 2] and |Z''| + 2zeta~ >= zeta~ + delta0 + 1
  > delta0, against (F*).
So Y has no zero-sum of length >= 2p + 2: contradiction.  []

## 2. Scope and remaining LS gap
Sequence level only; relative to the listed candidates and imports.  LS remains open (in this lane's candidates) exactly for
floor(2p/3) + 1 <= kappa with p - kappa >= 5 and p < 6(p - kappa) - 10 (the band (p + 10)/6 < p - kappa <= (p - 1)/3), where the
present argument fails at: index one (p >= 4e - 3), the no-wrap step (p >= 6e - 10) and (6b).  LS+ / STAB are not addressed here.
