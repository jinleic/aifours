# Erratum 2 (consolidated) to the delta package (delta-review-package-v1.md 23a5be43a94cc7fa39cf067769bfac2d9248aaf6f882607c0ddd9868670e861b)

Owner OlsonSTABSuccessor.  Written after /bin/date 2026-10-19T06:49:28-0700.  Disposes BOTH delta reviews: Codex run
review/olson-STAB-delta-codex-v1.prompt.stdout.txt (ade272c4b13b0ff797bd346c7633db72ebe0278820e81ef582a6b9fb1b03e705; 0 FATAL / 0 MAJOR / 2 MINOR) and Claude run
review/olson-STAB-delta-claude-v1.prompt.note.md (92752d227cba11b1058b7517f0971633b07fd21f483b19aea08e23f81f03fc0a; 0 FATAL / 0 MAJOR / 18 MINOR m1.1-m6.1).
Frozen sources (none edited): proof-LS-caseII-v2-addendum-1.md c289db226c86ea7703af4a23c4a93dce543669cb911d36b5845e70aad2c98718; proof-LS-caseI-smalldelta-v1.md
2ad172a026ee64441f00fd228b8b402a0a5f2e0d85df04512c87f0e70e5a68b1 with erratum-1-delta-APprime.md e035f8d14b6bcb57c0af0d5beb170ddf3471674490583e66b75d0d34cc90c461; proof-STAB-base-p1mod3-v1.md
8a41189cb8d2c254394c4ac44963d7a64f7f6ace00a9ad829f7e0af96def0985; proof-LSplus-e2-v1.md 2effb09ea4e28553ab0321a64b3e660c422d767ef940fcf58615dec8edc208b1; proof-LS-lin-v1.md
434a5dfd38e3f82ef596b7c23cdf528069207e35581c573e83e1613626c19aec; lemma-CTgen-v1.md 462d52aa1c6708a1071e06e0d88d0558b7f58e00c14bd42565655a123f92e5ad; addendum-credit-scope-delta-v1.md
273a871c71ab232ae788e15e53a6dbf72a40dbc585dd3a3e3d12566d9dee664b.  Read each source through erratum-1-delta-APprime.md (where it applies) and then this
erratum; where they differ this erratum governs.  Repairs are wording, citations, explicit checks and scope restrictions only: no
theorem statement is strengthened, no proof is redesigned, and the reviewers' optional simplifications are recorded, not adopted.

## Package-wide mandatory overlays
- Authority for RS(a), RS(b), CF, DGM-p, Theorem U, ROW, both dichotomies, SH and AP is the parent verdict run
  review/olson-CFXT-ROW-LSII-parent-verdict-v1.md (ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0), items 1-9, at the scopes stated there; no model review is cited as an
  acceptance authority.
- CF is read through erratum-2-prereq-consolidated.md (fb136e6ef71f7250774c3102a35c88a9709fee827091df84f67b433fb13106d5) R4 ((L) characterises a zero-sum of length >= 2p + 2; 'long'
  only under (ZP_kappa)), and Lemma AP through R6 (corrected proof).  Both are mandatory wherever CF (L) or AP is used.

## D-1  proof-LS-caseII-v2-addendum-1.md (Theorem LS-II')
m1.3 (statement).  Old: 'Theorem LS-II' (unconditional).  For p >= 7 prime and kappa0 + 1 <= kappa <= p - 2, no LS-counterexample of
length p + 2kappa + 1 lies in case (II).'  New: 'Theorem LS-II' (without H'(kappa)).  For p >= 7 prime and kappa0 + 1 <= kappa <= p - 2,
no LS-counterexample -- an odd Y with |Y| = p + 2kappa + 1, (ZP_kappa) and a zero-sum of length >= 2p + 2 -- lies in case (II) with
respect to g = g0 of DGM-p.'  Here and in the Effect paragraph 'unconditional' means only that H'(kappa) and Lemma SH are not used;
the declared imports (CF, DGM-p, ROW, the LS-threshold dichotomy, AP with R6) remain (Codex remark on the Effect paragraph).
m1.1 (Step 5'(b)).  Old: 'Each deletion shortens by c' + 1 <= 2e - 4, while the even lengths in the excluded window [2kappa + 2, 2p]
form e consecutive even values, so a shortening by at most 2e - 4 from a length >= 2p + 2 cannot land below the window without
landing in it; hence every intermediate zero-sum is long.'  New: 'Each deletion removes c' + 1 terms; c' is odd, so c' + 1 is even
and <= 2e - 4.  From a zero-sum of length L >= 2p + 2 it leaves a zero-sum of length >= 2p + 2 - (2e - 4) = 2kappa + 6 > 2kappa + 2; by
(ZP_kappa) this length is not in [2kappa + 2, 2p], so it is >= 2p + 2: every intermediate zero-sum is long.'
m1.2 (Step 5'(c)).  Old: '|T2| >= 2p + 2 and |W2| <= s <= e - 2 give a' >= 2p - e + 4'.  New: '|T2| >= 2p + 2 and |W2| <= s <= e - 2 (the
case-(II) clause of the accepted LS-threshold dichotomy, parent verdict ca6e4ca7 item 6) give a' >= 2p - e + 4'.  erratum-2-prereq
R8's dependency note ('s <= e - 2 ... not used') concerns only Steps 1-5 of proof-LS-caseII-v2.md; it does not apply to Step 5'(c),
which uses s <= e - 2 as just cited.  (Valid alternative, recorded not adopted: s <= delta0 - 1 <= 2e - 4 gives a' >= 2p - 2e + 6 > 2e - 5.)
Noted, not adopted: Claude's optional observation that Steps 1-2 and Step 5'(a) already suffice.

## D-2  proof-LS-caseI-smalldelta-v1.md (Proposition I-small, Corollary LS-small) with erratum-1-delta-APprime.md
m2.3 (dependencies).  The header is supplemented: CF, DGM-p and the LS-threshold dichotomy are parent-accepted (ca6e4ca7 items 1, 5,
6); erratum-2-prereq R4 is mandatory for (L) in (E), and R6 for Lemma AP inside LS-II' Step 1; Lemma AP' is read with the proof D1
of erratum-1-delta-APprime.md, which supersedes the v1 proof (its case (ii) 'n <= 2l - p' and its terse lifting).
m2.1 ((D), AP' hypotheses).  After 'with n := e - 2 >= 1 (e >= 3 in case (I))' read: 'Lemma AP' (proof D1) applies: n = e - 2 >= 1 and
3n + 2 = 3e - 4 < p (from 3e <= p - 1); an arc of size l = 0 is covered by case (i) of D1.'
m2.2 ((D), S >= 2).  Old: 'a^(-1) = 1 or 2 puts rho = 1 at 1 or 2 < S + 1'.  New: 'a^(-1) = 1 or 2 puts rho = 1 at 1 or 2, which is
<= S (S >= r >= (p + 1)/2 >= 4), i.e. outside [S + 1, p - 1]'.
m2.4 (Sec. 2 scope remark).  Old: 'For p - kappa >= 5 case (I) remains open (delta0 >= 3 allows zero-sums mod p of size < delta0 in
U, and for large e the zero-free part is shorter than (p + 1)/2).'  New: 'Proposition I-small does not treat p - kappa >= 5.
(Editorial: that case is treated by proof-LS-lin-v1.md for p >= 6(p - kappa) - 10, and BASE1+ covers kappa = (2p + 1)/3 for
p = 1 (mod 3); combined scope in D-5.)'

## D-3  proof-STAB-base-p1mod3-v1.md (Theorem BASE1, Corollary BASE1+)
m3.3 (Sec. 0 sharpness).  Old: 'Both E2(kappa), E3(kappa) do satisfy (ZP_kappa) and are long zero-sums (S1-sharp erratum 1, items (F1),
(F2) of the fix map for Codex 1 / Claude A-m4, read in the accepted verdict as the sharpness families).'  New: 'Both E2(kappa) and
E3(kappa) are zero-sums of length 2p + 2 (coefficient sums p + 3 + 3(p - 1) = 4p and 2p - 1 + 3c = 4p) and satisfy (ZP_kappa).  CF check
(e = (p - 1)/3): E2 w.r.t. g has delta0 = p - 3 and U = 1^(p-1), and W = 1^w with rho = w <= e - 1 has |W| + 2rho = 3w <= p - 4 < delta0;
E3 w.r.t. g has delta0 = 1 and U = (mu*)^3, and the nu-sums (nu := -3mu) of its nonempty sub-multisets are 1, 2, 3, none in
Phi = {0} u {4, 7, ..., p - 3}.  This sharpness statement is not used in the proofs.'
m3.2 (S6, S7).  S6 Old: '(the S1-sharp argument: it uses m = p + delta - |S_Q|, D <= 2delta - 2, m >= (p + 3delta)/2 >= D + 2 and the S4
bounds; all hold here).'  New: '(the S1-sharp argument: it uses m = p + delta - |S_Q|, D = 2delta - 2 = (2p - 2)/3,
m >= (p + 3delta)/2 = p + 1 >= D + 2 = (2p + 4)/3, and the S4 bounds b_min <= p - delta + 1, b <= p - delta - 2|S_Q| + 3; each checked at
these values).'  S7 Old: 'S7 A_(Q') = 2p (the S1-sharp argument ends with l <= D; here l = D + 2).'  New: 'S7 A_(Q') = 2p (the S1-sharp
argument: the witnesses g^r with r <= D < m and g^s with 1 <= s <= D + 1 <= m exist, the first crossing prefix has A_W <= 2p + D < 4p,
and the argument ends with l <= D, whereas here l = D + 2 = (2p + 4)/3 >= 2).'
m3.1 (Corollary, E3 bullet).  Old: 'If nu_y <= p - 4 these four consecutive integers lie in [1, p - 1] and contain one that is = 1
(mod 3) and in [4, p - 3] (as p - 3 = 1, p - 2 = 2, p - 1 = 0 (mod 3));'  New: 'If nu_y <= p - 4 these four consecutive integers lie in
[1, p - 1].  If nu_y = 1 they contain 4, which is in Phi (4 <= p - 3 as p >= 7).  If nu_y >= 2, the one that is = 1 (mod 3) is >= 4 (it
is not 1) and <= p - 3 (as p - 2 = 2 and p - 1 = 0 (mod 3)), hence in Phi;'

## D-4  proof-LSplus-e2-v1.md (Lemma CT, Theorem LS+2)
m4.1 = Codex MINOR 1 (RS(a) authority).  Old (first dependency): 'Lemma RS(a) of proof-ROW-v1.md (a7b73415...; Cauchy-Davenport;
scope 'any prime p, 1 <= n <= |S|', as accepted in the Codex prerequisite review run review/olson-CFXT-ROW-LSII-codex-v1.prompt.
stdout.txt d049d531...b9e9 -- a model review, not a parent verdict).'  New: 'Lemma RS(a) of proof-ROW-v1.md (a7b73415...;
Cauchy-Davenport; any prime p, 1 <= n <= |S|), parent-accepted in run review/olson-CFXT-ROW-LSII-parent-verdict-v1.md (ca6e4ca7...),
item 4.'  Second dependency: CF is read with erratum-1 E1 and erratum-2-prereq R4 (mandatory).
m4.2 (Step 0).  Old: '(SLZ3, kappa <= p - 1)'.  New: '(SLZ3, whose range floor(2p/3) + 1 <= kappa <= p - 1 contains kappa = p - 2 exactly
when p >= 7)'.
m4.3 (Steps 1 and 3(B)).  Step 1: after '>= (3p - 4) - (2p - 4) = p' read '> 0, so some value has v_x >= p - 1.  Hence ...'.  Step 3(B)
Old: 'there are a != 0 in Z_p and integers x_u >= 1 (u in U) with u = x_u a and S := sum_(u in U) x_u <= p - 1.'  New: 'there are
a != 0 in Z_p and integers x >= 1, one for each term of U(-sigma(U)), with every term equal to x a and the x summing to ord(a) = p;
the coefficient of -sigma(U) is >= 1, so S := sum_(u in U) x_u <= p - 1.'

## D-5  proof-LS-lin-v1.md (Theorem LS-lin) and the combined scope
m5.1 (Sec. 0 combination).  Old: '(For e = 3 the condition is automatic: the range forces p >= 11.  With e = 2 covered by
proof-LSplus-e2-v1.md and by proof-LS-caseI-smalldelta-v1.md, LS holds in every cell with p - kappa <= (p + 10)/6, i.e.
kappa >= (5p - 10)/6 -- relative to the candidates above.)'  New: '(For e = 3 the condition is automatic: the range forces p >= 11.
Combined with e = 2 (proof-LSplus-e2-v1.md; proof-LS-caseI-smalldelta-v1.md): for every prime p >= 7 and every integer kappa with
floor(2p/3) + 1 <= kappa <= p - 2 and p - kappa <= (p + 10)/6 (equivalently kappa >= ceil((5p - 10)/6)), LS(p, kappa) holds --
relative to the candidates above.)'
m5.3 (Step 4).  After the first sentence read: 'Here U' is nonempty (|U'| = p - 2e + 1 + delta' >= p - 2e + 2 >= 2); sigma(U') != 0 (U' is
zero-sum-free); U'(-sigma(U')) is minimal (a proper nonempty zero-sum omitting -sigma(U') lies in U'; one containing it has a
nonempty complement in U' that is a zero-sum); index one gives a != 0 and coefficients x >= 1 summing to p, and the coefficient of
-sigma(U') is >= 1, so S' <= p - 1.'
m5.4 ((6a), (6b)).  (6a) Old: 'W := Z'' u W'' has integer sum e - 1 (residue e - 1)'.  New: 'W := Z'' u W'' has signed-representative sum
zeta~(Z'') - X(W'') = e - 1 (X = x-sum), an integer congruent to sigma(W) (mod p), so rho(W) = e - 1'.  (6b) Old: 'W := Z'' u W'' has
integer sum -p (residue 0)'.  New: 'W := Z'' u W'' has signed-representative sum zeta~(Z'') - X(W'') = -p, an integer congruent to
sigma(W) (mod p), so rho(W) = 0'.
Noted (Codex), no change: the theorem keeps the no-wrap hypothesis p >= 6e - 10; (6b)'s weaker numerical need does not weaken it.
m5.2 = Codex MINOR 2 (Sec. 2).  Old: 'LS remains open (in this lane's candidates) exactly for floor(2p/3) + 1 <= kappa with p - kappa >= 5
and p < 6(p - kappa) - 10 (the band (p + 10)/6 < p - kappa <= (p - 1)/3), where the present argument fails at: index one
(p >= 4e - 3), the no-wrap step (p >= 6e - 10) and (6b).'  New: 'The cells left by LS-small and LS-lin are those with
floor(2p/3) + 1 <= kappa <= p - 2, p - kappa >= 5 and p < 6(p - kappa) - 10.  Of these, kappa = (2p + 1)/3 with p = 1 (mod 3) is covered
by BASE1+ (LS+ implies LS).  The cells unsettled by the delta package (not decided by these arguments) are exactly those with
floor(2p/3) + 1 <= kappa <= p - 2, p - kappa >= 5, p < 6(p - kappa) - 10, other than kappa = (2p + 1)/3 for p = 1 (mod 3); the smallest are
(17, 12), (19, 14), (23, 16), (23, 17).  The present argument needs index one (p >= 4e - 3), the no-wrap step (p >= 6e - 10) and (6b).'
Combined LS scope of the package (prime p >= 7, floor(2p/3) + 1 <= kappa <= p - 2), relative to its imports:
  (i) p - kappa <= (p + 10)/6 (e = 2: LS-small / LS+2; e >= 3: LS-lin);
  (ii) p - kappa <= 4 (LS-small; standalone beyond the linear bound only at (p, kappa) = (13, 9), which is also a BASE1 cell);
  (iii) kappa = (2p + 1)/3 with p = 1 (mod 3) (BASE1+).

## D-6  lemma-CTgen-v1.md
m6.1.  Old: 'Let m be the number of occurrences of p in T and W the rest of T; |W| <= N - v_p(Y) <= 2kappa + 1 < 2p.  Then |T| - 2p
is even, >= 2 and <= |T| - |W| = m;'  New: 'Let m be the number of occurrences of p in T and T° the rest of T (renamed from W, which
clashes with CF's notation); |T°| <= N - v_p(Y) <= 2kappa + 1 < 2p.  |T| is even (a zero-sum of odd elements has even length), so
|T| - 2p is even, >= 2 and <= |T| - |T°| = m;'

## Credit addendum (context only)
addendum-credit-scope-delta-v1.md: the scout's inferred classical route to LS(p, p - 2) 'for every prime p >= 5' includes p = 5, where
kappa = 3 = kappa0 lies in S1-sharp's range; the package's own claim is p >= 7 (Claude remark).  No premise changes.

## Exact conclusions after this erratum (sequence level; relative to the declared imports)
LS: the three families (i)-(iii) of D-5.  LS+: kappa = p - 2 for every prime p >= 7 (LS+2) and the BASE1 cells.  STAB: the BASE1
cells only.  Structural: LS-II' (without H'(kappa)), Proposition I-small, Lemma CT, Lemma CTgen.  Not concluded: full LS, LS+, STAB;
TR; INV*; ordered Olson.  No novelty or priority claim.
