# Shor raw signed factors — a forced negative coefficient and an all-degree one-sided obstruction

Owner MathShor-2. Actual `/bin/date` before composing: **Mon Oct 26 05:24:58 PDT 2026** (earlier observation bound). WRITTEN/unreviewed; exact symbols, fractions and integer products only. No scientific execution, numeric candidate trial, CAS, enumeration, replay or new GO.

This continues `shor-raw-signed-factor-top-layer-and-gap-balance-v1.md`, SHA256 `9dadb66e10d752e228ab2d7bc68aea6d6e165ed6a221f73ae1c5231a3b1ee14b`. It adds a Shor-specific RAW sign constraint and rules out ONE-SIDED signed factorizations at EVERY b-degree of the other factor. It does not settle the two-sided case or original finite-completion problem.

## 1. Literal data and named import boundary

Take FINITE integer noncommutative P,S, normalized by P(0,b)=S(0,b)=1, and suppose

    F=1+P(a+b−1)S

is a0/1 polynomial containing all sixteen literal Shor words. Assume F(a,0)=a^n, so U(a)V(a)=1+...+a^(n−1), U=P_0,V=S_0.

These are literal algebraic hypotheses. The lemmas below do NOT use Reutenauer's proof or the factorization conjecture. Applying them to EVERY hypothetical finite RAW complete UD extension uses named import I5 from the preceding packet: the published signed-factorization theorem, statement read in DeFelice2016Thm2.1, original proof **NOT_RECONSTRUCTED**. No nonnegative-factor assumption is made.

Let Y(z)=F_1(z,z) count actual one-b codewords by TOTAL a-count, and put

    H(z)=P_1(z,z)V(z)+U(z)S_1(z,z).

The exact first-layer identity is

    Y(z)=G_n(z)+(z−1)H(z),   G_n=1+...+z^(n−1).           (FIRST)

All exponents are actual nonnegative integers, not residues. Added raw words of arbitrary lengths are retained.

## 2. Forced negative coefficient at the Shor triangle

For EVERY integer K>=0, summing coefficients of FIRST through degree K gives

    [z^K]H = min(K+1,n) − sum_(d=0)^K [z^d]Y.             (CUM)

This is exact telescoping, not a probability limit or positivity assumption on H.

The five row0 Shor words have a-counts0,1,7,13,14. The four words in each of rows3 and8 have a-counts at most9 and14 respectively. The three row11 words have a-counts11,12,13. These are sixteen DISTINCT raw words, all with a-count<=14. Other one-b words can only add nonnegative counts. Therefore

    [z^14]H <= min(15,n)−16 <= −1.                        (NEG14)

Every possible signed factorization of an actual completion must realize THIS negative coefficient. In particular it cannot have all of U,V,P_1,S_1 nonnegative. This is not the assertion that every finite maximal code has positive factors; rather, the given Shor data force a precise signed defect in any factors that would exist.

For every sufficiently large K, CUM is0, because |F_1|=n and H is finite. The entire signed defect has a finite coefficient tail if a completion exists. Proving that NEG14 cannot have such a tail under ALL higher-layer positivity constraints is the remaining two-sided problem, not an assumed termination principle.

## 3. One-sided positivity lemma, with the other factor UNBOUNDED

**Lemma.** If P contains no b at all, then BOTH P and S have nonnegative coefficients. The symmetric statement holds when S contains no b.

*Proof.* Write P=U(a). The highest-b-layer purity lemma of the preceding packet applies to F: top F is U b S_q, and unique splitting at the inserted b makes every nonzero coefficient of U and S_q have the same unit sign. Since U(0)=1, this sign is positive. Thus U is a nonempty characteristic polynomial and U(1)>0.

Now fix j>=0 and a raw word v with exactly j occurrences of b. In the (j+1)-b layer,

    F_(j+1)=U b S_j+U(a−1)S_(j+1).

Sum its nonnegative coefficients over ALL possible leading a-runs, keeping v fixed AFTER the first b. For the first term the sum is U(1)(S_j,v). For the second term it is0: its leading-run polynomial is U(x)(x−1) times the appropriate finite leading-run slice of S_(j+1), and evaluation at x=1 vanishes. Therefore

    0 <= sum_(k>=0)(F,a^k b v) = U(1)(S_j,v).

The sum is finite because all factors are finite. Since U(1)>0, every coefficient of every S_j is nonnegative, including j=0. This proves the lemma. Reversing words exchanges left/right and proves the symmetric version. ∎

This is NOT a b-count cutoff: S may have arbitrarily many b-layers and arbitrary a-gaps. It is also not an inference from commutative cancellation alone; the first-b position is fixed BEFORE summing the actual raw leading-run coefficients.

**Corollary (all-degree one-sided obstruction for Shor).** Neither factor can be b-free. Otherwise the lemma makes U,V,P_1,S_1 nonnegative, contradicting NEG14. Thus any hypothetical completion's normalized signed factors must be genuinely TWO-SIDED in b.

The resulting elementary lower bound on the largest b-count is only a corollary, not a claimed solution or the purpose of this representation.

## 4. Exact top-sign control when both factors have one b-layer

Here is a bounded SUBCASE control, not an exhaustion of the two-sided residual. Suppose deg_bP=deg_bS=1. The purity lemma says P_1 and S_1 have one common sign epsilon, with unit nonzero coefficients.

**Claim.** epsilon must be positive.

If epsilon were negative, write P_1=−A,S_1=−B with A,B nonempty characteristic polynomials. Normalization P(0,b)=S(0,b)=1 implies A and B have NO pure-b word. Their least total a-counts d_A,d_B are consequently positive.

The two-b layer abelianized only in a-runs is

    F_2(z)=(z−1)A(z)B(z)−U(z)B(z)−A(z)V(z),

with U(0)=V(0)=1. At d=min(d_A,d_B), the first product contributes nothing because d_A+d_B>d. Each of the two remaining products that starts at d contributes a STRICT negative coefficient, from the corresponding constant1 of U or V. No higher coefficient of U or V can reach that first degree. This contradicts F_2's nonnegativity. ∎

Therefore in this subcase P_1,S_1 are nonnegative, and NEG14 must arise from signed U or V. This pins the sign defect to the a-only cyclotomic factors, rather than allowing an unexplained negative phase of the highest b-layer. It does NOT prove U,V nonnegative, exclude the subcase, or prove that all finite signed factors can be made positive.

## 5. Original remaining gap and next exact representation

The genuinely new all-degree exclusion here is ONE-SIDED P or S. For general finite deg_bP,deg_bS>=1, the exact TOP/PEN/BAL constraints remain. The sign-defect NEG14 must coexist with all raw nonnegative higher layers and eventual finite support. A Shor-specific contradiction would need to propagate that forced negative coefficient through the actual lower-layer repairs at EVERY finite depth, or exhibit actual finite signed factors that repair it. No such propagation or factors are supplied.

This is a changed raw representation of the finiteness/nonstabilization residual, not reuse of the known660/1320 filters, a claim that residue closure is raw STAB, or an assumption that the normal-form cyclic graph covers all realizations. All unknown arities, b-counts, delays and word lengths remain unbounded. Original Shor completion stays **NOT_PROVED** in either direction.

I3/I4 remain at their earlier proof boundaries; I5 is separately named, not authenticated from its survey statement alone. H* is FALSE/WITHDRAWN. No commutative-prefix/factorization conjecture or source hash is a correctness premise. Own permanent v109-A exactness MAJOR and all older histories remain; exact mathematics is not process cure. No source/shared/frozen edit, git/deletion/publication or stronger formal/kernel/human/family/executable/novelty acceptance. Same original cutoff and deadline; no early final park.
