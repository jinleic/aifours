# Erratum 2 (consolidated) to the prerequisite package: proof-CF-XT-v1.md, proof-ROW-v1.md, note-STAB-range-v1.md,
# erratum-1-CF-XT-ROW-range.md, proof-LS-caseII-v2.md

Owner OlsonSTABSuccessor.  Written after /bin/date 2026-10-19T05:56:09-0700.  Disposes BOTH reviews of the package frozen in run
review/olson-CFXT-ROW-LSII-review-freeze-v1.json: Codex run review/olson-CFXT-ROW-LSII-codex-v1.prompt.stdout.txt
(d049d5316f73b9f7ba2beb46e40f7f81daf1856262a97b99fd66902c21f9b3e9; 0 FATAL / 2 MAJOR scope / MINORs) and Claude run review/olson-CFXT-ROW-LSII-claude-v1.prompt.note.md
(8decff2928613d01d646faa519b40d209dd1e43e6bf2025d2215aecc01ac3239; 0 FATAL / 1 MAJOR scope / MINORs).  Frozen sources (not edited): proof-CF-XT-v1.md aa602d45e154a7787ac3f0270a3c26deb5e8c6a70736cf4a82c700f5368c191f,
proof-ROW-v1.md a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d, note-STAB-range-v1.md 5b8faa3ab578c373e6fa01be32b10b476950f450f93a00580dd082366a630115, erratum-1-CF-XT-ROW-range.md
767fe8f8605019b3b3b7aa1ff6a610f088279ede30b9b3429544d4c8487c1db7, proof-LS-caseII-v2.md 3df159ff61784cb3345b27a6cf9da873900051df92dbb3be019e846578d73a43.  Read the sources through erratum 1 and then this erratum; where
they differ this erratum governs.  Editorial repairs add no theorem scope; every statement below is the source statement or a
restriction of it, except E5 of erratum 1, which is relabelled (item R9).  The separate delta package (proof-LS-caseII-v2-
addendum-1.md, proof-LS-caseI-smalldelta-v1.md, proof-STAB-base-p1mod3-v1.md, proof-LSplus-e2-v1.md) is NOT covered by these
reviews; item R6's corrected AP proof governs wherever Lemma AP is cited.

## R1 (Codex MAJOR = Claude XT MINOR 1): XT 'In particular' restricted
proof-CF-XT-v1.md Sec. 2, the sentence 'In particular the only three-term extensions are E2(kappa - 1) h^3 = E2(kappa) and
E3(kappa - 1) h^3 = E3(kappa).' is replaced by: 'In particular, for kappa0 + 1 <= kappa <= p - 2 the only three-term
(ZP_kappa)-extension of E2(kappa - 1) is E2(kappa - 1) h^3 = E2(kappa); and, ONLY for kappa0 + 2 <= kappa <= p - 2, the only
three-term (ZP_kappa)-extension of E3(kappa - 1) is E3(kappa - 1) h^3 = E3(kappa).'  The unrestricted E3 reading is false at
kappa = kappa0 + 1: for p = 1 (mod 3), E3(kappa0) = (3h)^(2p-1) and Z = (-3h)^3 is admissible (Codex).
## R2 (Claude XT MINOR 2): XT Remark
The Remark of proof-CF-XT-v1.md Sec. 2 is replaced by direct computations (the S1-sharp route is withdrawn): E2(kappa0) w.r.t.
g = h has delta0 = 3p - 3kappa0 - 2 in {p - 1, p}, U = 1^(p-1); a long zero-sum needs W = 1^w with 3w >= 2p + delta0 >= 3p - 1, i.e.
w >= p > p - 1: none.  E3(kappa0) w.r.t. g = 3h has delta0 = 1 and |U| = 3kappa0 - 2p + 2 <= 1; a long zero-sum needs
|W| + 2rho(W) >= 2p + 1 with |W| <= 1, i.e. rho >= p: none.  So (ii) is not needed at kappa = kappa0 + 1.  Unused downstream.
## R3 (Claude TR MINORs 3, 4): STAB wording and 'long' in TR
STAB(p, k) is read exactly as frozen in STAB2-scope-v1.md (c98182632eb9ef39904c43ef75815919b56142ade2137f30c5d99482dcaa4e89) and evidence/proof-LSplus-partials-v2-addendum-MAX-v2.md:
'every odd Y with |Y| = 3k + 1, (ZP_k) and a zero-sum of length > 2k equals E2(k) or E3(k) for some generator h' (no automorphism
clause); the Proposition's proof uses exactly this.  In TR and the Proposition, 'long' for Y means length >= 2kappa + 2 (>= 2p + 2
under (ZP_kappa)); for the deleted V (with (ZP_kappa) and no zero-sum of length 2kappa) any zero-sum of length >= 2kappa has length
>= 2p + 2, so both readings coincide.  TR stays OPEN; the base kappa0 + 1 is not covered by the Proposition.
## R4 (Claude CF editorial): (L)
In CF (b), (L) characterises 'a zero-sum of length >= 2p + 2', which equals 'long' only under (ZP_kappa); proof-ROW-v1.md Sec. 5's
phrase 'the long zero-sum condition (L)' is read 'condition (L) (the long zero-sum condition under (ZP_kappa))'.  The clause
'sigma(W) + j >= p' in (L) is redundant (k >= 2 is automatic) and harmless.
## R5 (Codex RS(b), Claude RS editorial): RS
Lemma RS(b) is stated for an INTEGER K >= 0 and a sequence with all terms nonzero mod p (the dummy 0 of each B_i is not an
occurrence).  In the proof of RS read 'the k-th listed occurrence (k = 0, ..., T - 1) goes to row (k mod n) + 1'.
## R6 (Codex AP MINOR = Claude AP MINORs 1, 2): corrected proof of Lemma AP (proof-LS-caseII-v2.md Sec. 2; statement unchanged)
Let d := |x~| in [1, (p - 1)/2] (signed representative).  The n distinct points a + rho x (1 <= rho <= n) lie in I n (I + x), so
|I n (I + x)| >= n, and for an arc of l < p consecutive residues |I n (I + x)| = max(0, l - d) + max(0, l - p + d).
(i) d >= 2n: then l <= 2n <= d and l - p + d <= 2d - p < 0, so I n (I + x) is EMPTY, contradicting n >= 1 points.
(ii) p - 2n < d < 2n: each nonzero term is < n (l - d < 2n - (p - 2n) = 4n - p < n; l - p + d < 4n - p < n) and if both are
positive their sum is 2l - p <= 4n - p < n; so |I n (I + x)| < n: contradiction.
(iii) Otherwise d <= p - 2n and d < 2n, so l - p + d <= 0 and n <= l - d: d <= l - n <= n.
Lifting (induction on rho).  Let L = [alpha, alpha + l - 1] be an integer interval mapping onto I, y_0 in L the lift of a, and
y_rho := y_0 + rho x~.  If y_rho is in L, then y_(rho+1) is in [alpha - n, alpha + l - 1 + n] <= [alpha - n, alpha + 3n - 1] and
its residue lies in I, so y_(rho+1) is in L + mp for some integer m; m >= 1 is impossible (alpha + p > alpha + 3n - 1 as p > 3n - 1)
and m <= -1 is impossible (alpha + l - 1 - p < alpha - n as l + n - 1 <= 3n - 1 < p).  So y_(rho+1) is in L, and by induction
y_0, y_n are in L: n d <= l - 1 <= 2n - 1, d = 1, x = +-1.  []
## R7 (Codex SH = Claude SH MINORs 1, 2): SH parity and occurrences
In SH(a): z = |Z| is even (Z is a nonempty zero-sum of odd elements), so kappa' = kappa - z/2 is an integer, kappa' >= kappa - e =
p - 2e > 0 and kappa' < kappa.  The excluded EVEN lengths [2kappa + 2 - z, 2p - z] and [2kappa + 2, 2p] together contain every even
length in [2kappa' + 2, 2p] because 2p - z >= 2kappa (the only uncovered integer can be the odd 2kappa + 1); zero-sums have even
length.  'Meets' and 'disjoint' are occurrence-level throughout.
## R8 (Codex c' MINOR = Claude LS-II MINORs 1, 2, 3): LS-II Step 5 spelled out (proof-LS-caseII-v2.md, conditional on H'(kappa))
Step 5 is read: 'Let T be a long zero-sum.  For an occurrence of g and an occurrence of -g, the pair is a zero-sum of length 2 <= 2e,
so by SH(a) T contains one of the two occurrences.  If T missed an occurrence of g and an occurrence of -g, that pair would be
disjoint from T; hence T contains all M occurrences of g or all v1 occurrences of -g.  If T contains an occurrence of g and one of
-g, removing these two occurrences leaves a zero-sum of length |T| - 2: for |T| = 2p + 2 this is 2p (excluded by (ZP_kappa)); for
|T| >= 2p + 4 it is long and disjoint from the removed pair, contradicting SH(a).  A T with no occurrence of g lies in (-g)^(v1) R'
and has length <= r <= p - 2.  So T contains all M occurrences of g and no -g: T = g^M W' with W' a sub-multiset of R' (so Step 4
applies to W').  If W' contained a negative x = -c'g, then c' <= 2e - 5 < 2p - 2e + 3 <= M (as 3e <= p - 1), so c' occurrences of g in T
and x form a zero-sum of even length c' + 1 in [4, 2e - 4] inside T, contradicting SH(b).  So W' is tiny and Step 4 gives
|W'| <= (delta0 - 1)/3 < delta0 + 2: contradiction.'  Dependency note: Steps 1-5 use only 'some mu-value has multiplicity >= K + 1'
(then s <= delta0 - 1); 's <= e - 2' and the uniqueness of mu1 are not used; ROW enters only in Sec. 4.  Codex's shorter completion
(after Step 2: M + s <= 2p - 1, so a long T contains -g; v1 + s <= p - 2, so it contains g; then g(-g) <= T contradicts SH(b)) is
recorded as a valid alternative; no statement change.
## R9 (Claude E5 MINOR 1; parent): relabelling of erratum 1
Erratum 1's header description '(wording/scope; no statement strengthened)' is WITHDRAWN for item E5: E5 is a NEW, strengthened
endpoint statement (extension of STAB to kappa = p - 1 fails for every prime p >= 7; p = 5 undecided) with its own full proof,
which is retained at exactly that scope.  E1-E4 remain wording/scope repairs.
## R10 (Claude E5 MINORs 2, 3, 4): range note
note-STAB-range-v1.md: (a) 'LS+ at kappa = p - 1 is classical (s_(2p)(C_p) = 3p - 1), as recorded by the parent' is replaced by: 'At
kappa = p - 1, Theorem U of proof-ROW-v1.md (stated range (p - 3)/2 <= kappa <= p - 1) gives |Y| <= 2p + kappa - 1 = 3kappa + 1 for
every (ZP_(p-1)) odd sequence; the classical value s_(2p)(C_p) = 3p - 1 is context, not an import.'  (b) 'STAB is stated (and only
ever used) for ...' is replaced by 'STAB's intended scope, as frozen in evidence/LSplus-scope-v1.md, addendum MAX v2 and
STAB2-scope-v1.md, is floor(2p/3) + 1 <= kappa <= p - 2.'  (c) The closing Remark is replaced by: 'The family Y_(a,b) (and erratum 1
E5's family) shows that at kappa = p - 1 there are length-(3kappa + 1) (ZP)-sequences with a long zero-sum other than E2/E3; no
classification is claimed.'  (d) In the proof read 'a 2p-term subsequence (1, a)^(2p-j) (1, b)^j has 1 <= j <= p - 1'.
## R11 (Codex U MINOR = Claude U MINORs 1, 2; Claude DGM informational)
proof-ROW-v1.md Sec. 3: '(at kappa = 0 it is D(C_(2p)) - 1)' is outside the theorem's range and is withdrawn (not claimed); the
s_(2p)(C_p) sentence is a comparison only (Theorem U at kappa = p - 1 itself gives 3p - 2); the 'Use for LS' paragraph is heuristic,
not a claim.  DGM-p is vacuous at kappa = p - 1 (its hypotheses would force M >= 2p + 1); the DeVos-Goddyn-Mohar name is attribution
only, not a premise.
## R12 (Codex MAJOR 2 = Claude MAJOR): length-(3kappa + 2) dichotomy restricted
The paragraph 'Dichotomy at length 3kappa + 2 (LS+)' of proof-ROW-v1.md Sec. 4 (and its line in erratum 1 E4) is restricted to:
p >= 7 prime, floor(2p/3) + 1 <= kappa <= p - 2 (so K = p - 3e + 2 >= 3), Y odd with (ZP_kappa) and |Y| = 3kappa + 2, and the
HYPOTHESIS that some generator g has v_g(Y) >= p - e (then r <= 2p - 2e + 2, so r + 2e - 2 <= 2p, and r - delta0 = K >= 0, so ROW
applies).  The hypothesis is not supplied by DGM-p (3kappa + 2 < p + 2kappa + 1) or by anything in this package.  The unrestricted
reading is false (Claude: kappa = 0, Y = g^2).  In this package the dichotomy is not an LS+ reduction step.
## R13 (Claude LS-threshold informational)
The LS-threshold dichotomy does not use the long zero-sum; it holds for every (ZP_kappa) odd Y of length p + 2kappa + 1 with
g = g0; RED only translates it to LS(p, kappa).
## What is not concluded
No LS, LS+, STAB or ordered-Olson statement follows from this package.  The conditional LS-II excludes only case (II) under
H'(kappa); TR remains open; the dichotomy at length 3kappa + 2 remains conditional on a generator with v_g >= p - e.
