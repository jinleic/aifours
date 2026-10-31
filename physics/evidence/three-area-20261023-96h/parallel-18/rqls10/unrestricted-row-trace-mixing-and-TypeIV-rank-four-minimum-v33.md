# RQLS10 v33 — UNRESTRICTED QLS row-trace mixing bound; the TypeIV master needs rank>=FOUR from EVERY scalar

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE writing this NEW manuscript: **Mon Oct 26 09:02:45 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact Parseval/Cauchy/unitary-spectral/integer proof only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO/private approximate scout/backconversion. No machine/kernel/formal/configured-family/human/priority/novelty/finite-witness acceptance.

## 1. A genuinely UNRESTRICTED necessary condition

For ANY QLS(n), choose ANY fixed ambient ONB e1..en and ANY phases of all its normalized cell representatives. Let V_a be the unitary whose b-th column is the ACTUAL cell vector q_(a,b). No covariance, resolution, maximality or common sector is assumed.

Column b is an ONB, so Parseval at e_b gives

    sum_a |(V_a)_(bb)|^2=1.

Summing over b and applying Cauchy to EACH row's diagonal,

    sum_(a,b)|(V_a)_(bb)|^2=n,
    sum_a |trV_a|^2 <= n*sum_(a,b)|(V_a)_(bb)|^2=n^2.       (TRACEBOUND)

**General low-rank consequence.** Suppose for EVERY row a there is a unit scalar lambda_a such that

    rank(V_a-lambda_a I)<=r,     r<=n/2.

A unitary of that scalar-deviation rank has eigenvalue lambda_a with multiplicity at least n-r. After dividing by lambda_a, its other at most r unit eigenvalues have total modulus at most r. Thus

    |trV_a|>=n-2r.

TRACEBOUND forces

    n*(n-2r)^2<=n^2,
    n-2r<=sqrt(n).

At n10, r<=3 would give |trV_a|>=4 in every row and hence sum_a|trV_a|^2>=160>100, contradiction. Therefore in ANY phase choice of an ACTUAL QLS10, at leastONE row unitary has

    rank(V_a-lambda I)>=4 for EVERY unit scalar lambda.

This is not an impossibility of QLS10, nor a cardinality bound. It is a necessary ambient-basis mixing condition ruling out simultaneous low-rank-per-row deformation constructions. One cannot change the ambient basis separately for each row, since that would destroy the original column problem; the theorem explicitly uses ONE fixed basis. Arbitrary choices of cell phases and individual scalar comparisons are ALLOWED, so this is not a phase convention artifact.

## 2. ENTIRE covariant TypeIV master: every row has the same bound

In v31's complete TypeIV master, all V_a are conjugates of ONE V0 by the natural duad permutation representation. Thus their trace and diagonal energy are identical. The unrestricted Parseval identity now gives

    sum_b |(V0)_(bb)|^2=1,
    |trV0|^2<=10.                                         (COVTRACE)

If rank(V0-lambda I)<=3 for some unit lambda, the spectral argument gives |trV0|>=4, contradicting10<16. Therefore the whole master satisfies the stronger necessary condition

    rank(V0-lambda I)>=4 for EVERY unit scalar lambda.     (RANK4)

This strengthens, and does NOT withdraw, v32's rank>=3 theorem. It is independent of a particular standard-copy phase gate, real entries, diagonal idempotence, or a selected resolution. It uses the actual column ONBs and exact trace, not a comparison of parameter counts.

## 3. Literal diagonal-energy identity in the FULL19-parameter master

In the normalized S3-orbit decomposition of v31/v32, write the commutant blocks T inU3,eta inU1 and I2 tensor S with S inU3. Use multiplicity indices0,1,2 for the trivial orbit basis(diagonal,disjoint,intersecting), and for S use N(the standard copy from the3 disjoint duads) and two standard copies from the six intersecting duads.

The diagonal entries of V0 are constant on those three H-orbits, because V0 commutes with H. Their values can be obtained just by traces on each orbit coordinate subspace:

    D0=T_(00),
    D1=[T_(11)+2S_(NN)]/3,
    D2=[T_(22)+eta+2S_(SS)+2S_(AA)]/6.

The latter two labels S,A denote any fixed orthonormal multiplicity basis supplied by the symmetric/antisymmetric pair-triples; their diagonal sum is the trace on the two-copy intersecting standard sector, hence basis-independent within that sector.

The FULL column condition therefore implies the exact necessary equation

    |D0|^2+3|D1|^2+6|D2|^2=1,

together with

    trV0=D0+3D1+6D2=trT+eta+2trS,
    |trT+eta+2trS|^2<=10.

This is a concrete coupled condition on the WHOLE unitary master, NOT permission to replace its columns/resolution/maximality by one scalar inequality. S being nonscalar remains separately necessary by v32.

## 4. The idempotent-diagonal special case is even more constrained

Suppose additionally q_(a,a) is the coordinate ray e_a for all a in this covariant master. The exact diagonal coefficient is one common unit phase lambda; normalize V0 by it. All actual diagonal cell vectors are then e_a. Every other cell q_(a,b) in column b is orthogonal to that column's diagonal e_b. Hence the diagonal of EACH V_a has its own a entry1 and all other entries0, so

    trV0=1.

If rank(V0-I)<=4, its trace has modulus at least10-8=2, contradiction. Therefore

    rank(V0-lambda I)>=5

for the scalar lambda actually used by the coordinate diagonal. This does NOT claim the rank>=5 bound for every other scalar, nor for a non-idempotent TypeIV solution. It explains why deformations supported only in the nontrivial H representations, which leave the reference e_a fixed, cannot furnish the lowest-rank construction.

## 5. Exact lowest-rank ordinary TypeIV cases still open

Combine RANK4 with v32's complete scalar-standard-block exclusion. If rank(V0-lambda I)=4 for some unit lambda, the block-rank sum

    rank(T-lambda I)+rank(eta-lambda)+2rank(S-lambda I)=4

requires rank(S-lambda I)=1 or2;0 is excluded by v32.

If it is2, the other blocks are scalar lambda, so the seed leaves e_a in its original coordinate ray; section4's idempotent rank>=5 excludes this case. Thus a rankFOUR candidate must have exactlyONE nontrivial standard multiplicity direction(dimension2 physically) plus two dimensions of trivial/sign deviation. The possibilities are:

    rank(T-lambda I)=2, eta=lambda;
    OR rank(T-lambda I)=1, eta!=lambda.

The trivial block cannot leave the reference coordinate vector FIXED with the SAME comparison phase lambda: then section4 excludes rank4. It may instead MOVE that ray OR rephase it by a DIFFERENT scalar lambda_prime. The latter is NOT excluded by section4, whose rank>=5 bound is relative to lambda_prime, not automatically to lambda. NONE of these remaining rankFOUR families has been proved to solve or fail the full master. All higher-rank/multistandard cases also remain OPEN.

This is an exhaustive description of the minimum-rank remainder under the stated scalar comparison, not an unproved claim that every TypeIV solution has rank exactly4 or is WLOG low-rank.

## 6. Full scope, dependency and assurance ceiling

TRACEBOUND and its unrestricted n10 low-rank consequence(section1) use ONLY the ACTUAL row/column QLS axioms, arbitrary fixed ONB and arbitrary cell phases. The covariant strengthening/diagonal formulas/minimum-rank residual use ENTIREv31's iff TypeIV master plus v32's complete scalar-standard theorem, not a selected gate. The new inequalities/rank reductions do not provide any actual100-ray witness or exclude a general dense remainder.

The third full allowed Latin resolution and maximal cardinality conditions of v31 remain UNSOLVED, not dropped after proving easier column constraints. No A5-WLOG, unrestrictedno-go, formal/kernel/family/human/current-openness/novelty or finite-witness checker/control/vendor/priority promotion. All computations are exact WRITTEN reasoning, NOT machine-checked. All old process/math findings, v9/v14 withdrawals, frozen histories and ZERO-credit quarantines remain. Original18/exclusive-root/HOLD/cadence/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38; primary continues actual remaining rankFOUR/higher TypeIV or other open geometry, no early pending-review park.
