# RQLS10 v29 — FULL-array A5-duad reduction: all spinorial QLSs fail; any maximal resolvable ordinary candidate must be intrinsicallyIRREDUCIBLE10

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE writing this NEW manuscript: **Mon Oct 26 08:30:26 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact character/fixed-cell/commutant/Gram reasoning only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO/private approximate scout/backconversion. No machine/kernel/formal/configured-family/human/priority/novelty/full-witness acceptance.

## 1. FULL-array symmetry hypothesis, with NO assumed invariant-sector decomposition

Rows and columns of the original10x10 complex-ray array are labeled by the ten duads of{1,2,3,4,5}. Suppose simultaneous even permutations act projectively covariantly on ALL hundred cell rays through a unitary physical representation. The designated ten-transversal resolution need NOT be covariant. In contrast with v26–v28, a common invariant4-sector is NOT assumed here.

The physical action is either an honest representation of A5, or a representation of2.A5 with center acting-I10. All projective unitary A5 actions are included only conditionally on the explicitly named NOT_RECONSTRUCTED classical J-A5-SCHUR fromv28; the two stated linear-cover formulations do not need that optional classification import.

**Full-array theorem.**

1. In the nontrivial-central/spinorial case, no covariant QLS10 exists AT ALL: simultaneous row and column ONBs are inconsistent. This does not even require maximality or a resolution.
2. In the ordinary case, the physical10-representation MUST be one of the four types in section3. If the array is a maximal1-RQLS10, the parent's complete sector theorem plus ENTIREv26/v27 force its common-projector commutant to be SCALAR. Both proper4+6 and5+5 branches are excluded WITHIN THIS symmetry model, even though invariant sectors were not hypothesized.
3. The surviving ordinary candidates are genuinely intrinsicallyirreducible10 arrays. Their GROUP representations are reducible; that is NOT the same as a common sector. A dense irreducible residual for one whole representation type is given in section5.

This is not A5-WLOG for the original problem, not an unrestricted irreducibility theorem, and not a maximal100-ray construction or unrestricted no-go. Outside this symmetry model all three original intrinsic branches remain OPEN; inside it the ordinary irreducible10 case remains OPEN.

## 2. A THREE-CELL trace contradiction excludes ALL spinorial full arrays

Take disjoint duads a={i,j},b={k,l}. Let t=(ij)(kl), fixing exactlyTWO duads a,b in the ten-duad action. Let g=(ik)(jl), which swaps a,b. Their lifts x,y to2.A5 satisfy x^2=z and xy=z*yx as in the quaternionic inverse image Q8. In the spinorial physical representation,

    U(x)^2=-I10,         U(y)^-1 U(x)U(y)=-U(x),

so trU(x)=0, and its only eigenvalues are+i,-i. This trace fact holds in ANY odd-central representation, with no dimension-specific spin-character classification.

The diagonal ray q_(a,a) has an x-eigenvalue lambda=+-i. By covariance q_(b,b) is proportional to U(y)q_(a,a), so its eigenvalue is-lambda. The offdiagonal ray q_(a,b) has some x-eigenvalue mu=+-i, since t fixes that cell.

Now use the FULL row a ONB as a basis for U(x). Since t fixes row a, it permutes its ten ray lines. Its only fixed column-duad labels are a,b. Every nonfixed pair contributes zero diagonal entry to this monomial matrix, regardless of its phases. Therefore

    0=trU(x)=lambda+mu.                           (ROWTRACE)

The FULL column b ONB gives the SAME operator trace, with its only fixed row labels a,b, so

    0=trU(x)=mu-lambda.                           (COLTRACE)

Together these force2lambda=0, impossible. This excludes ALL spinorial full-array representations—including reducible10-dimensional ones—before maximality, a third partition, any sector or any phase ansatz.

## 3. ALL possible ordinary10-dimensional representations

For an honest physical A5 representation, fix a diagonal row a. Its stabilizer is S3. An order3 element h cycling the complementary triple fixes exactlyONE column-duad, namely a. The diagonal ray affords a one-dimensional ordinary S3 character, trivial or sign, whose value at h is1. The same monomial-trace argument therefore forces

    trU(h)=1.                                    (TRACE3)

Using the complete ordinary character table inv27, write a=n3+n3prime,b=n4,c=n5,r=n1. The dimension and TRACE3 equations are

    r+3a+4b+5c=10,       r+b-c=1,
    a+b+2c=3,           r=1-b+c>=0.

The COMPLETE nonnegative-integer solutions are

    I:   1 + W3 + W3 + W3,
    II:  W4 + W3 + W3,
    III: 1 + 1 + W3 + W5,
    IV:  1 + W4 + W5,

where EACH W3 can independently be3 or3prime, W4 is the unique ordinary irreducible4 and W5 the5. The proof is immediate from c=0or1: if c0,b0or1; if c1,b0or1. No other10-dimensional ordinary representation survives.

At t=(ij)(kl), the same character table gives trU(t)=-2 in typesI/II and+2 in typesIII/IV. Row a's two fixed ray eigenvalues are its diagonal and disjoint-cell values, each+1or-1. Hence BOTH are-1 inI/II and BOTH+1 inIII/IV. In particular the apparently possible zero trace and opposite-character branch is absent after the full dimension/TRACE3 constraints. This is an exact necessary character restriction, not a construction or sufficiency assertion.

## 4. Common-sector invariance is a CONSEQUENCE, not a new ansatz

Import the parent's ENTIRE adopted unrestricted v15/v16 theorem: at maximal100 distinct complex rays the common-projector commutant has minimal-sector patterns ONLY{10},{4,6},{5,5}, with the full support-graph/commutant identification. Every common d-sector contains exactly10d actual cells, wholly in that sector, by the context trace count.

Covariance of the HUNDRED-RAY ROSTER makes U(g) normalize that commutant: conjugating an operator commuting with all cell projectors still commutes with all of them because the cell rays are permuted. This does NOT require g to preserve the given transversal partition. Thus it permutes the primitive common-sector projectors.

### 4.1 The5+5 pattern is impossible by orbit sizes

An action of A5 on the two primitive sectors is a homomorphism to S2 and must be trivial: A5 has no index2 subgroup. Hence each5-sector is individually invariant under U(g), and its fifty-cell roster is invariant under the simultaneous ten-duad action. But that action has exactly the three ordered-pair cell orbits of sizes10(diagonal),60(intersecting),30(disjoint). No union of these has size50. Contradiction.

The invariance was derived from the FULL commutant theorem. We did not assume a preferred5-sector or identify group irreducible components with common-ray sectors.

### 4.2 The4+6 pattern is impossible by the WHOLE v26/v27 union

The two primitive sectors have different ranks4,6, so normalization cannot exchange them. The4-sector is individually invariant and its forty-cell roster must be the union of diagonal10 and disjoint30. The restriction U|E4 is an HONEST ordinary4-dimensional unitary representation in the present ordinary case. ENTIREv26+v27 excludes precisely every such invariant/covariant4-sector, even with a NONCOVARIANT third partition.

Thus no proper common sector remains; the common-projector commutant is scalar. A full union review must reconstruct the entire v26/v27 ordinary-representation theorem AND the parent's v15/v16 unrestricted input before adopting this full-array consequence. A review of the spinorial trace contradiction alone does NOT accept this ordinary irreducibility conclusion.

## 5. A concrete dense remaining geometry for representation typeI

This section demonstrates explicitly why a fixed vector of the GROUP is NOT the rank1 common-sector obstruction and gives necessary original-resolution constraints on the surviving irreducible10 family.

In typeI, the group-fixed space F is one-dimensional, say Ce0. By section3 the diagonal and disjoint-cell rays have stabilizer eigenvalue-1 under a suitable half-turn. The fixed vector has eigenvalue+1, so ALL forty of those rays are orthogonal to F. The sixty intersecting-duad cells form ONE regular A5 orbit (their ordered-pair stabilizer is trivial), so ALL have the SAME squared F projection. In each actual row there are six such cells and four F-orthogonal cells; the row ONB gives total F projection1. Therefore EACH intersecting cell has squared F projection EXACTLY1/6.

Consequently the ORIGINAL arbitrary designated transversal must contain EXACTLYSIX intersecting-duad cells and FOUR diagonal/disjoint cells: its ONB also has total F projection1. This balanced pattern is necessary even though no covariance of the transversal resolution is assumed.

Choose the phase of each of those sixty ray representatives so

    q=e0/sqrt(6)+w,       w in F-perp.

For the six intersecting cells in ANY row,column or designated transversal, orthonormality gives the complete exact Gram identity

    <w_i,w_j>=delta_ij-1/6.

Hence their six w's form a regular simplex of norm squared5/6, span dimension5 and sumZERO; equivalently the six q's span Ce0 plus that5-space and sum sqrt(6)*e0. The other four rays of that context lie in its orthogonal4-dimensional complement. These4-spaces may VARY with the context; no common4+6 decomposition follows. In fact section4 says a maximal candidate inside this symmetry model MUST avoid making them common.

The fixed-line projector has diagonal expectation0 on forty rays and1/6 on sixty, NOT binary0/1. Thus it does NOT commute with all the rank-one cell projectors, and applying the adopted common-rank1 obstruction here would be a false no-go. This is a genuine dense irreducible group-orbit/simplex residual, not an accepted witness or a selected all-sparse ansatz.

## 6. Whole-scope assurance and exact remaining task

The direct spinorial full-array contradiction(section2) uses only trace invariance, the two fixed duads of a double transposition, and Q8 anticommutation in the binary cover. The ordinary physical-character classification(section3) uses the complete v27 character table. The intrinsic-sector elimination(section4) imports the parent's complete unrestricted v15/v16 theorem plus ENTIREv26/v27. The new typeI simplex/resolution condition(section5) is proved directly and retains arbitrary designated transversals. The optional all-projective terminology additionally needs NR J-A5-SCHUR; do not backdate that classical import as reconstructed.

This whole chain requires a JOINT union/application gate; no selected trace, character-table or one-branch return covers it automatically. All statements remain AUTHOR-WRITTEN candidates. No executable finite-witness/checker/control/vendor/priority gate has occurred. No scientific interpreter or private approximate arithmetic is hidden in the exact written trace/Gram argument.

The next original-model task inside this symmetry family is an actual ordinary intrinsicallyirreducible10 construction/exclusion in typesI–IV, including a full permitted resolution and100 distinct rays. TypeI's six-cell simplex balancing supplies a concrete representation for that task. Outside the family the arbitrary10/4+6/5+5 original branches all remain OPEN. No100-ray witness, unrestrictedno-go, formal/kernel/family/human/current-openness/novelty promotion. All old process/math findings, v9/v14 withdrawals, frozen histories and ZERO-credit quarantines remain permanent. Original18/exclusive-root/HOLD/cadence/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38, no early pending-gate park.
