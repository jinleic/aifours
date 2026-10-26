# v29-E — RQLS RT analytic/definition bridge: written reconstruction only

Reviewer: `InfoGuessingRminus-2` / owner `InfoGuessingRminus`, cross-domain from information science. Author: `PhysicsRQLS10`. Actual metadata-only `/bin/date` before this review: `Sun Oct 25 04:20:44 PDT 2026`.

## 1. Disposition — do not read this as an RT+ certificate verdict

**Assigned ANALYTIC/DEFINITION BRIDGE: RECONSTRUCTED in writing, with 0 FATAL / 0 MAJOR / 0 substantive MINOR findings at that scope.**

**The full236-core/52-kernel finite certificate and Theorem RT+ as a universal residual theorem: NOT_RECONSTRUCTED by this review.** They are NOT accepted, independently replayed, finite-certified, or cleared by the analytic disposition. The192560-byte JSON body was deliberately NOT read or reconstructed; only its metadata SHA-256 was observed. The source's census and individual finite basis/minor/lambda identities remain explicit obligations in Section10.

The source-level bridge is valid CONDITIONALLY: complete genuine-input coverage, nonzero minors, full two-dimensional kernel bases, and nonzero-total annihilating norm witnesses of the stated kind WOULD prove RT+ for the covered inputs. This review reconstructs that implication, its actual index/phase conventions, the normalization/predicates, and Appendix B's model. It does not establish that every required finite witness is correct or that the covered set has the claimed236 members.

No actual analytic/indexing mismatch was found. In particular, the parent's withdrawn transpose and four-ones-row objections are NOT findings against the author.

## 2. Pins, complete reading and exposure

The frozen assignment is v29-E in `institute/runs/three-area-2026-10-23-96h/peer-review-wave-eighteen-v29.json`, observed SHA256 `fd47c873613f88a299c4cf170fdabba86125d03e592e02c40651b9f24d3504e8`.

Binding `parent-evidence-erratum-v7.md`, observed SHA256 `d5e1911bba6549684c93b2e910fac66eb44c353ae5dea2a8d1555516946e8d05`, was read before substantive review. The metadata packet receipt was also read; it records literal-render equality, which is metadata, not mathematical verification.

Literal source packet: `peer-review-wave-v29-rqls-rt-analytic-bridge-sources-v1.md`, observed SHA256 `4cb913c732544bced37494573550de89043b48adbbcb6583a2e026879cb033a7`.

The COMPLETE packet was read in explicit raw ranges1–113,114–245,246–390,391–510,511–630,631–750,751–858. Thus all declared source lines, including the full Appendix A table and Appendix B program text, were actually read without line elision. The raw reread of1–113 replaces the earlier header preview; no truncated source line is left unread.

Source abbreviations used below refer to ORIGINAL source LF numbers printed in that literal packet, not packet wrapper line numbers:

- **R:** `physics/evidence/three-area-20261023-96h/parallel-18/rqls10/rt-residual-torus-obstruction-v1.md`, complete LF1–370, observed SHA256 `2d9563539a7abdc2dd6cdf0218822edbfb49b6d8f55e37e87682477c972b61be`.
- **C:** `physics/evidence/three-area-20261023-96h/parallel-18/rqls10/off-axis-consolidated-orientation-v1.md`, complete LF1–474, observed SHA256 `9f1c469002abb6cc0c7bf5cb8bf9a7ca664773b6c4b70276516a565e6a3750c7`.
- **J, REFERENCE ONLY:** `rt-residual-exact-algebra-certificate-v1.json`, observed metadata SHA256 `7c2122d71c77e30db513f3fc2939406f5bf4ab636866226b643f3e37656c2504`; declared192560 bytes/14136LF. Its BODY WAS NOT READ and is not part of this reconstruction.

ACK/exposure record: `peer-review-rqls-rt-analytic-bridge-ack-v1.json`, observed SHA256 `769a48136c0d67374f6b7ad58cb8f0dad1656744385a4721bcfaef203870864a`.

This is a supplied-proof, same-harness, cross-domain review, not blind, cross-vendor, configured dual-family, human, formal/kernel, or novelty acceptance. The reviewer saw the parent's checker objections only as explicitly withdrawn errors and did not inherit either them or the author's confidence. A historical RQLS family review exists in this root from the earlier owner context; it was not reopened here and no verdict transfers from it. No CLI, nested agent, scientific eval/interpreter, enumeration, symbolic program, or certificate replay was used for this review. Only written reasoning and metadata clocks/hashes were performed.

Under v7, R:L3,142–153,370 describe historical unadmitted author computations and candidate claims, not admitted verification credit. Their outputs are preserved; this review does not retroactively authorize them or accuse the owner of contradicting the erroneous permission it was given.

## 3. Literal core and the row-i/column-t operator — reconstructed

References: R:L9–28,50–59,269–280,316–322; C:L13–24,41–45.

The literal character matrix has zero diagonal, +1 for distinct rook-neighbours in the3×3 grid, and -1 otherwise. The ordered pairs are H=(4,5), J=(3,6), U=(1,7), V=(2,8), with rho fixing0 and interchanging those endpoints. These are the SAME literal pairs in both sources and in Appendix B.

The definition

`M_(i,t)=conjugate(C_(t,i))*C'_(t,rho(i))`

has **row i and column t**. Its right-kernel variable is delta_t. The physical output zero at (i,rho(i)) is a sum over t. It is not the transpose operator obtained by making t the outer matrix row.

For a nonmasked position let a=Q0(t,i), b=Q1(t,rho(i)). Since the literal core denominator is sqrt8,

`4 M_(i,t)=[(1-s a)(1+s b)]/2`

`=(1+7ab)/2+s(b-a)/2`, using s²=-7.

When a=b this is4. When a=-b it is -3+s or -3-s. At t=i the first core is zero; at t=rho(i) the second is zero. These are the only masks because p is a bijection. This proves R:L50–59 directly and matches C:L45's entries0,1,(-3+s)/4,(-3-s)/4 after dividing by4.

Appendix B has i as the OUTER loop and t as the INNER loop (R:L317–322). Its signs use `a=q(t,i)`, `b=q(p[t],p[rho[i]])`, exactly the declared operator. Thus the source does not exhibit the parent's withdrawn transposition mistake.

The six upper-triangle values of the literal A0, in pair order HJ,HU,HV,JU,JV,UV, follow directly from the four-sign endpoint differences:

`0,0,0,1,1,2`.

For example, JU gives `[-1-(-1)-(-1)+1]/2=1`, and UV gives `[1-(-1)-(-1)+1]/2=2`. Every entry involving H cancels. This reconstructs R:L28/C:L57 and the `odd(identity)` convention in R:L277–280. On distinct pairs all four endpoints differ, so each character value is ±1 and the numerator is even; Appendix B's integer division by2 is exact, not a truncation model.

The rook description also reconstructs the character identity analytically: writing A for rook adjacency gives Q0=2A-J+I, A has degree4, adjacent pairs have one common neighbour, and nonadjacent pairs have two. Hence Q0 has row sum0 and Q0²=9I-J, as used in C:L41–43 and the static control at R:L275–276. No enumeration/program was used to evaluate this identity.

## 4. Independent physical D/E quantifiers — reconstructed at the declared interface

References: C:L19–26; R:L38,61–81.

For independent unit diagonal matrices D,E, the relevant product entry at the necessary-zero interface is

`(C* D C' E)_(i,rho(i))`

`=E_(rho(i),rho(i)) * sum_t conjugate(C_(t,i))*D_(t,t)*C'_(t,rho(i))`.

Here C* denotes conjugate transpose. The outer E entry is nonzero and therefore cancels from THIS zero equation. Taking delta_t=D_(t,t) leaves the full nine independent unit phases in M delta=0. No pair equality, conjugation symmetry, phase-field assumption, or reality restriction follows from the cancellation. E has not disappeared from other nonzero modulus equations, and the necessary-zero equation has not become sufficient for a conference matrix or global QLS.

A basis V in physical nine-coordinate order merely parametrizes all delta in ker_C M as Vz with arbitrary z in C²; its column/free-row normalization is not a physical phase normalization. In particular its norm rows must be interpreted as the nine PHYSICAL delta_t coordinates, not the even/odd frame with its separate metric weights. R's finite norm construction uses physical rows and does not insert an even/odd metric in place of the physical moduli.

This reconstructs the phase quantifiers of the STATED local necessary interface. The original derivation of that interface from the full H0/ray-array construction and any broader WLOG classification is not provided or cleared here; C:L9–26 and474 explicitly limit that scope.

## 5. All-source normalization and exact residual predicates — reconstructed as definitions

References: R:L85–98,277–309; C:L175–203,433–465.

### 5.1 Normalization does not transport a different right kernel

A translation of the second grid preserves rook-neighbour character values. Thus replacing every p(i) by p(i)-p(0) produces a bijection with p(0)=0 and leaves the ENTIRE Q1 table exactly unchanged. It is stronger than a symmetry-equivalence claim: C', M, and their right kernel are literally unchanged.

All normalized p occur in `(0,)+permutations(1,...,8)`. The36 upper-triangle entries determine the whole real symmetric zero-diagonal Q1. Therefore deduplicating by that key loses no genuine second core. `setdefault` in the lexicographically ordered permutation iteration chooses the stated lexicographic representative. There is no implicit transpose, phase transport, or quotient of unknown physical solutions.

The5040 distinct-table count can also be reconstructed in writing, independently of the unadmitted census: the only3-cliques of the rook graph are its rows/columns (a third vertex outside the row of two distinct same-row vertices cannot share a column with both). Automorphisms therefore either preserve or exchange the two families of three maximal cliques. All row and column permutations and their interchange are realized, giving `(S3 x S3) semidirect C2`. Its stabilizer of0 has order8. Two normalized permutations yield the same literal table exactly when their relative permutation is such a stabilizer automorphism. Hence the number of distinct tables is8!/8=5040. This analytic count DOES NOT reconstruct the236-element filtered residual census.

### 5.2 R0/R1/R2 agree with the frozen residual definitions

Appendix B computes A1 from literal source characters, then rank_F7(A0+A1), then the H degree and actual edge magnitudes. It does not accept arbitrary signed support tables (R:L277–299).

- **R0:** H degree0 plus magnitude multiset[1,1,2] means precisely a211 triangle on the other three pair vertices. Rank_F7 L=2 excludes L=0 and the leading-rank>=3 case. A nonzero triangle determinant is2abc over F7, so at least one leading triangle edge must vanish. Every individual possible leading entry lies strictly between-7 and7, so such an entry vanishes exactly over the integers. This matches C:L457's cancellation/not-all-cancellation formulation and excludes axis222.
- **R1:** H degree1 and four nonzero edges force a paw: the three remaining edges form the triangle on the other three vertices. Let k be the H-neighbour, b its nonzero leading edge, and e the opposite leading edge on the other two vertices. The determinant of the corresponding zero-diagonal4×4 matrix is b²e². Leading rank2 forces e=0; then the remaining leading support is a star at k, of rank2 because b is nonzero. This reconstructs the cancellation in C:L458. The code retains all genuine heavy/tag placements rather than testing only one.
- **R2:** H degree2 with neighbours i,j forces the leading i-j edge to vanish, otherwise the H,i,j principal triangle has nonzero determinant. With k the non-neighbour, L is bipartite between {H,k} and {i,j}, with cross block `[b_i b_j;c_i c_j]`. Its rank is2 exactly when the nonzero cross block has rank1, equivalently `b_i*c_j-b_j*c_i=0 mod7`. This matches C:L459. Appendix B's F7 elimination retains nonzero INTEGER multiples of7; it does not replace the modular condition by integer determinant zero.

Thus the source generator and predicates model the frozen residuals correctly. This does NOT independently reconstruct the full raw second-grid support catalogue or all other branch proofs in C:L175–203/288–431. Those are separate imports/gates, and the finite membership/count of the filtered predicate set remains NOT_RECONSTRUCTED.

## 6. Full complex kernel and Hermitian norm witness implication — reconstructed

References: R:L61–79,102–118,323–356; C:L155–173.

### 6.1 Rank and scalar extension

An8-minor nonzero under the ring map Z[s] to F11 with s mapped to2 implies that the original algebraic minor is nonzero: the defining relation is preserved since2²=-7 mod11. Thus a supplied nonzero8-minor proves rank_K B>=8 and cannot meet RT+'s rank7 premise.

For a claimed rank7 input, a nonzero7-minor gives rank at least7. Two exact independent K-null columns give rank at most7. The specified two physical rows equal to the2×2 identity indeed make them independent. Since K embeds in C, algebraic ranks are unchanged under scalar extension; the same two columns span the COMPLETE complex kernel. This is why two K-valued basis columns do not restrict physical phases to K.

These are conditional certificate implications. No individual finite minor or B V identity was reconstructed from J in this review.

### 6.2 Norm form, including its sign and real domain

Let a physical row of V be (v,w), and set

`v*conjugate(w)=c+d s`, c,d in Q.

Every Hermitian2×2 matrix has the unique form

`X=[p, a+b s; a-b s, q]`, p,q,a,b real,

because s=i sqrt7 spans the purely imaginary line over R. For physical X=z z*, the coordinate norm is the row quadratic V_t X V_t*. Its cross term is

`(c+d s)(a+b s)+(c-d s)(a-b s)=2ca-14db`.

Therefore the exact real coefficient row is

`F_t=(|v|²,|w|²,2c,-14d)`.

This checks the critical -14 sign in R:L67 and Appendix B:L348–350. Both norm squares are rational because conjugation restricts on K to s mapped to-s. There is no restriction a,b to rational numbers for the physical Hermitian variable.

If lambda is any real (in particular integer) vector satisfying

`F^T lambda=0`, `lambda^T 1_9 !=0`,

then F x=1_9 is impossible: multiplying by lambda yields0=lambda^T1_9. Consequently no Hermitian X, and a fortiori no PSD rank-one physical X=z z*, achieves unit coordinates. The source is using AFFINE INCONSISTENCY, not inferring no rank-one point merely from a deficient or feasible PSD relaxation.

F has NINE rows and FOUR columns. The equivalent affine-rank question uses `[F | 1_9]`, adjoining a COLUMN of nine ones. Appending a row of four ones is a different matrix and does not test this implication. Appendix B avoids that mistake by checking the lambda identities directly. Positivity of individual lambda entries is unnecessary; only their nonzero total matters.

The simple displayed special-core norm relation can be checked CONDITIONALLY on R:L128–136's kernel formula: delta0=-(7/6)B and delta1=-(1/2)B give `-9|delta0|²+49|delta1|²=0`, with coefficient total40. But that formula's membership in the actual whole kernel is a separate finite identity not reconstructed here; this calculation is not a verdict on that core or a replacement for the other51 kernels.

## 7. Relationship to the frozen RT and the rank/norm-span interfaces

References: C:L75–94,155–173,448–474; R:L30–46,116–120,153,368–370.

The frozen RT region adds norm-span<=3 to the genuine leading-rank2, actual-rank7 R0/R1/R2 predicates (C:L450–451). RT+ claims an affine norm obstruction for ALL actual-rank7 residual inputs, without that norm-span subfilter. Therefore a correct COMPLETE RT+ certificate would imply the frozen RT no-go. It would not by itself certify C's new family-S/M/Herm14 arguments, all-P orientation decomposition, any broader first-profile WLOG, or the unrestricted QLS target.

For completeness, the relevant general projective-K interface in C:L88–94 can be reconstructed in writing. Reduction at s=0 over F7 gives the universal N. If S is the total coordinate sum, Nz=0 gives z0=S and every rho-pair sum equal to S. Summing gives S=5S, hence S=0 over F7 and z0=0; the reduced kernel is exactly four-dimensional rho-odd space.

If a coordinate-unit complex vector were projectively K-valued, clearing rational denominators would give integral a_t+b_t*s with a common positive integer norm c. If7 divides c, all a_t are divisible by7 and division by s gives the integral word `b_t-(a_t/7)s` with common norm c/7. Repetition ends at a common norm not divisible by7. Reducing that integral kernel word via N nevertheless makes its fixed-coordinate real coefficient divisible by7, forcing the common norm divisible by7: contradiction. This validates the projective-K obstruction, not a projective-K assumption for arbitrary multidimensional complex kernels.

Similarly, if the rational9×4 norm matrix F has rank4 and a physical X=z z* solves F x=1_9, its unique four coordinates are rational. If z2 is nonzero, `z1/z2=X12/X22` is in K; if z2 is zero the kernel vector is a scalar multiple of one K basis column. Thus the physical vector is projectively K-valued and excluded. This reconstructs the first norm-span implication in C:L157. It does NOT reconstruct the later local-integral first-order determinant lift or its fourteen literal applications (C:L159–173,403–431), which belong to their separately assigned gate.

The proposed stronger R witness does not depend on this rank4 reasoning: its lambda already rejects the entire Hermitian affine system. The difference between these two mechanisms is preserved.

## 8. Appendix B static modelling review — no execution

The complete source text R:L219–366 was read. The following are WRITTEN SOURCE-LEVEL observations, not a claim that the program was run or that its data passed:

1. Quadratic multiplication and conjugation (L228–233) implement s²=-7 and s mapped to-s exactly on rational pairs.
2. The fixed q definition and pair order (L234–235,269–280) match the declared literal model.
3. Full normalized table generation and set equality (L281–309) are the right coverage condition. Rejecting duplicate entries and demanding set equality prevent an incomplete selected-core list from serving as the universal proof, IF these operations were correctly executed on the actual data.
4. The residual filters (L290–299) are the predicates reconstructed in Section5 above. No integer-rank substitute is used for F7 rank.
5. The literal B builder (L316–322) has the correct i/t order, signs and masks. Its coefficient pairs are integral for actual ±1 nonmasked characters, so conversion to int in the modular-minor expression L327 is lossless for this model; it is not silently rounding arbitrary rational kernel entries.
6. The minor index checks and modular determinant (L253–268,323–329) implement nonzero minor certificates. A7-minor alone is not called exact rank7: the code additionally checks two independent full null columns (L335–342).
7. Basis rows in L335–342 are physical delta-coordinate rows, and `B[i][t]*V[t][k]` is the correct RIGHT-kernel identity. The free-row identity proves column independence without imposing phase values on z.
8. The norm forms and annihilator (L343–353) match the full Hermitian form in Section6. A nonzero total lambda is checked separately from the four zero weighted coefficient sums.
9. The diagnostic norm rank (L354–357) is not used to exclude span4 or silently discard span<=3 inputs; all alleged rank7 entries must satisfy the stronger annihilator. Thus the source does not mistakenly prove only the old29-case subfilter while claiming52-case coverage.
10. The routine returns the census and diagnostic counts (L358–365); those reported NUMBERS are not established by reading its source. Its lack of a hardcoded236/52 comparison is not an analytic coverage hole: the decisive conditional correctness mechanism is complete predicate-set equality plus a valid certificate for every expected entry. The actual returned census remains unverified here.

No source-level modelling defect within the assigned bridge was found. This is not a software build/test/security review or a certification that the Python implementation and serialized J have actually checked every case.

## 9. Findings and non-findings

- **FATAL: 0** at the assigned analytic/definition bridge.
- **MAJOR: 0** at that scope.
- **Substantive MINOR: 0** at that scope.

The following are NOT author findings: the parent's withdrawn transpose builder, its appended four-ones row, the alleged23-failed-core split, or the resulting mixed-convention accusation. None was independently established, and the literal source reconstructed above does not reproduce those errors.

R's historical “WRITTEN-checked-in-kernel” assurance and park claim must be read under v7's binding withdrawal of execution credit. That is a mandatory assurance overlay, not a reason to silently edit a pinned source or attribute the parent's permission error to the owner.

## 10. Exact unresolved obligations — NOT_RECONSTRUCTED, not PASS

**U1 — Complete finite residual census and coverage.** R:L89–120,157–212,281–315. NOT_RECONSTRUCTED: the actual filtered236-core set; branch counts56/96/84; higher-rank counts32/80/72; rank7 counts24/16/12; norm-span distribution and29/28 diagnostics. The analytic5040-table normalization count does not prove these filtered counts.

**U2 — Every actual minor and complete basis.** R:L102–118,323–342; J body not supplied in the literal packet. NOT_RECONSTRUCTED:184 nonzero8-minors,52 nonzero7-minors, all52 B V=0 identities, free-row independence data, and therefore exact ranks of the actual finite inputs. Reading the checker schema supplies no such identity values.

**U3 — Every full-kernel norm annihilator.** R:L70–79,118,157–212,343–356; J omitted. NOT_RECONSTRUCTED: all52 lambda identities against the actual supplied kernels, nonzero totals for every entry, and diagnostic norm ranks. The printed lambda table alone cannot be checked without the corresponding full basis forms. The conditional example in Section6 does not close this obligation.

**U4 — Explicit exceptional full kernel.** R:L124–138. NOT_RECONSTRUCTED: direct substitution of the displayed special-core basis into the actual literal B and its whole-kernel rank claim. Its conditional two-coordinate norm relation was reconstructed, but that does not establish its premises.

**U5 — Separate new-family/shared local determinant gate.** C:L159–173,288–431,467–470. This review does not clear the new local basis lift, degree3 stars, complete negative/positive matching arguments, fourteen-case first-order determinants, or their exceptional kernels. The parent's v28-A assignment and any later disposition must retain their own scope; no acceptance is inferred here.

**U6 — Full all-P/QLS cutover.** C:L175–203,433–474; R:L46,153,370. The raw catalogue/family exhaustion needed for the whole orientation theorem and the global conference-modulus/ray-array obligations are not proved by this residual bridge. No unrestricted maximal1-RQLS10 theorem, all-first-orientation normalization, or global100-ray witness follows.

No review of J's exhaustive finite data was authorized or attempted. The stronger finite-witness/triple-replay gates remain unmet. No new named GO exists. All immutable source/error histories and the original deadline remain unchanged.

## 11. Parent integration sentence

**Accept only this review's WRITTEN analytic bridge: the literal i/t convention, independent phase domain, normalization/predicate model, full-kernel norm-certificate implication, and static Appendix B modelling are reconstructed with no substantive defect found. RT+ and the full236-core/52-kernel finite certificate remain NOT_RECONSTRUCTED and cannot be cleared by v29-E.**
