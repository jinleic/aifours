# RQLS10 v28 — the spinorial4-dimensional A5-duad cases ALSO fail, by a row/column stabilizer incompatibility

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE writing this NEW manuscript: **Mon Oct 26 08:24:10 PDT 2026**. AUTHOR-WRITTEN CANDIDATE, not accepted. Exact finite character/stabilizer/eigenspace proof only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO/private approximate scout/backconversion. No machine/kernel/formal/configured-family/human/priority/novelty or accepted finite-witness claim.

## 1. Exact scope and union boundary

Keep v26/v27's simultaneous A5 action on ten-duad row/column labels, invariant40-cell common-sector hypothesis and arbitrary possibly symmetry-breaking third partition. The forty positions are necessarily(a,a) or(a,b)with a,b disjoint, from the three orbit sizes10,60,30.

Here the physical representation is an HONEST4-dimensional unitary representation of the binary icosahedral group G=2.A5 in which the central element z of order2 acts as -I4. This includes ALL the nontrivial-central-character4-dimensional representations of this double cover, not only one selected spin3/2 model. The ray action descends projectively to A5.

**Theorem.** No such projectively covariant40-cell assignment has simultaneous4-dimensional row and column ONBs. Consequently no such ACTUAL common4-sector is possible, before considering a third partition or6-sector continuation.

Combined with ENTIRE v26/v27 for central action+I4, this excludes all4-dimensional representations of the binary double cover that act SCALARLY on its center, at the exact ten-duad/invariant-sector/covariance hypothesis. No unrestricted A5-WLOG or original4-sector no-go is asserted.

OPTIONAL larger-language corollary: to say this covers EVERY projective unitary representation of A5 additionally uses the classical Schur-multiplier statement H^2(A5,U(1))=C2, represented by this double cover. Name this import **J-A5-SCHUR**, NOT_RECONSTRUCTED here. The double-cover theorem itself does not require that import. A full projective-representation union therefore has exactly this named classical import; it must NOT be silently labeled import-free or already parent-adopted.

## 2. Complete spin-character exhaustion in dimension4

Let phi=(1+sqrt5)/2 and r=phi-1=1/phi. Use the standard binary icosahedral subgroup of SU(2), order120, with quotient A5. This ordinary classical realization supplies a fundamental2-representation. Its trace at a chosen lift of the quotient classes1,2A,3A,5A,5B can be chosen2,0,1,phi,r, respectively; the negative lift negates every odd-central-character trace. The quotient class sizes are1,15,20,12,12. These values follow from the rotation angles, with the two lifts retained; no600-cell coordinate catalogue is being invoked.

The four following odd-central-character representations have trace table:

| representation | 1 | 2A | 3A | 5A | 5B |
|----------------|---|----|----|----|----|
| 2 | 2 | 0 | 1 | phi | r |
| 2prime | 2 | 0 | 1 | -r | -phi |
| 4spin | 4 | 0 | -1 | 1 | -1 |
| 6spin | 6 | 0 | 0 | -1 | 1 |

Here2prime is the algebraic conjugate of the fundamental representation under sqrt5->-sqrt5 (at the binary icosahedral quaternion coordinates, this is an honest finite-group representation and remains unitarizable). The4spin and6spin are Sym^3(2) and Sym^5(2). If t is the fundamental trace, their characters are

    t^3-2t,                 t^5-4t^3+3t,

so the displayed entries follow from phi^2=phi+1,r^2=1-r. For character inner products, the two lifts cancel their common sign, leaving exactly the quotient class weights divided by60. The four rows are orthonormal: for example the2/2prime cross product is4+20-24phi*r=0, and the4spin/6spin cross product is24-12-12=0. Norms are60 before division, using phi^2+r^2=3. The other cross products reduce to phi-r=1. These are exact written equalities, not executed character calculations.

Their dimension-square sum

    4+4+16+36=60

fills the entire odd-central-character half of the regular representation: the central+1 half consists of the ordinary A5 irreducibles of total dimension-square60(v27), and |G|=120. Hence these are ALL odd-central irreducibles. In dimension4 the possibilities are exactly

    4spin;       2+2;       2+2prime;       2prime+2prime.

This removes the risk of treating4spin as WLOG among reducible spinorial actions. The named standard group-theoretic input is the binary icosahedral SU2 double cover/order/class lift data; the operative trace rows, irreducibility orthogonality and exhaustion have been printed rather than imported from an unseen table.

## 3. Exact lifted duad stabilizers

For a diagonal duad a, its quotient stabilizer is S3. Its inverse image is the binary dihedral group of order12, with generators h,x and relations

    h^6=1, h^3=z, x^2=z, x h x^-1=h^-1.

Here h is a lift of the order3 complement cycle and x a lift of one of the three half-turns. If a projective ray is fixed by the quotient stabilizer, its line affords a ONE-dimensional character chi of this preimage. The relation forces chi(h)=chi(h)^-1, so chi(h)=+1 or-1. Since chi(z)=-1 and h^3=z, necessarily

    chi(h)=-1,       chi(x)=+i or-i.              (DIAG)

For an ordered disjoint pair a={i,j},b={k,l}, with remaining index m, its quotient stabilizer is the order2 element t=(ij)(kl). Choose lift x with x^2=z. A ray there must be an x-eigenline with eigenvalue+i or-i.

An even permutation g=(ik)(jl) swaps a,b and, with t, generates a Klein4 subgroup of A5. Choose a lift y of g. In the binary SU2 cover, distinct commuting quotient half-turns lift to quaternionic half-turns about perpendicular axes, so

    xy=z*yx,      equivalently xy=-yx in any odd-central representation.

This is also the Q8 inverse image of that Klein4, and is the only anticommutation fact used in the row/column contradiction.

## 4. ALL reducible2+2 cases fail already at a diagonal cell

In either2 or2prime, h has eigenvalues exp(+i*pi/3),exp(-i*pi/3), since its fundamental/conjugate trace is1 and h^3=-I. Neither is -1. Therefore no nonzero vector can satisfy DIAG. The same is true of ANY direct sum of those2-dimensional representations: its h-spectrum still has no -1.

Thus NONE of2+2,2+2prime,2prime+2prime admits even the required projectively invariant diagonal ray. This is a diagonal-stabilizer obstruction, not a statement that all projective A5 actions lack invariant lines in general.

## 5. The4spin restriction: a precise local rank obstruction

Realize4spin as Sym^3 of the fundamental2-space. Choose coordinates for the binary dihedral stabilizer so h has fundamental eigenvalues exp(+-i*pi/3). Its four symmetric-cube weights give

    eigenvalues(h)=-1, exp(+i*pi/3), exp(-i*pi/3), -1.

Let H be its2-dimensional -1 eigenspace (the highest/lowest cubic weights), and L the2-dimensional space of the middle weights. Both are invariant under h and x. On EACH of H and L, x exchanges the opposite weights and has eigenvalues+i,-i, one each. In particular:

- the two DIAG character lines are the+i and-i x-eigenlines INSIDE H;
- for a prescribed x-eigenvalue lambda in{+i,-i}, the full4-space x-eigenspace is the direct sum of ONE line in H and ONE in L.

**Local lemma.** Suppose an offdiagonal cell in a given row has the SAME x-eigenvalue as that row's diagonal ray. Orthogonality to the diagonal ray then removes the unique H-line in that eigenspace, forcing the offdiagonal ray into L. Its other two offdiagonal row rays are its orbit under h (the three disjoint complementary duads are cycled by the order3 quotient element). Since L is h-invariant, ALL THREE lie in L, dimension2. Together with the diagonal ray they span at most3 dimensions. The row cannot be a4-dimensional ONB.

The identical statement applies to a column's own lifted S3 stabilizer. It uses only orthogonality and covariance; no assumed equal amplitudes, guessed phase, numerical overlap or generic-rank argument enters.

## 6. ENTIRE row/column contradiction for4spin

Take a disjoint pair(a,b) and the chosen shared half-turn lift x. Let the diagonal ray q_(a,a) have x-eigenvalue lambda=+i or-i. Since y swaps the two duads, projective covariance makes q_(b,b) proportional to U(y)q_(a,a). Anticommutation gives

    U(x)U(y)q_(a,a)=-U(y)U(x)q_(a,a)
                    =-lambda U(y)q_(a,a).

Hence the column's diagonal ray q_(b,b) has the OPPOSITE x-eigenvalue -lambda. This conclusion is independent of phase choices of all rays and of which lift sign is chosen for x.

The offdiagonal ray q_(a,b), being fixed projectively by x, has eigenvalue EITHER lambda OR-lambda. If it is lambda, it matches its ROW's diagonal eigenvalue, and the local lemma says that row fails. If it is-lambda, it matches its COLUMN's diagonal eigenvalue, and the local lemma says that column fails. There is NO third eigenvalue and no third stabilizer-character branch.

Therefore no4spin assignment satisfies both row and column ONBs. This completes every odd-central dimension4 case. It also explains why constructing a seemingly orthogonal row orbit alone would be a false completion: the column necessarily lies in the rank-deficient stabilizer branch. No partial40-ray simultaneous row/column construction is claimed for this spinorial case.

## 7. Full union, exact imports and original remaining problem

ENTIREv26 covers the ordinary irreducible4, ENTIREv27 covers ordinary1+3/1+3prime/trivial and exhausts ordinary representations, and the present ENTIREv28 covers all nontrivial-central dimension4 representations of2.A5. The JOINT candidate theorem is: no simultaneous-ten-duad-covariant invariant40-cell sector under ANY central-scalar4-dimensional representation of the binary cover can be an actual maximal1-RQLS10 sector, even if the third partition breaks symmetry. In the spinorial case it fails before any third partition.

To state instead ALL projective unitary A5 representations, add ONLY the explicitly named NOT_RECONSTRUCTED classical import J-A5-SCHUR. The literal group/cocycle classification should be independently supplied/read before that optional terminology is parent-promoted. The original-array application itself also uses the literal complex-ray model/common-sector trace count/context intersection retained by the parent's complete v15/v16 adoption and later modern-source identity; no historical NR-BOOK-IDENTITY is backdated.

An entire union gate must reconstruct ALL three files' representation exhaustion, stabilizer cases, local-rank and cross-axis conclusions; a4spin or ordinary-character-table spotcheck is not that gate. No quantum/600-cell/graph catalogue is an operative premise. Standard binary-icosahedral group facts are named explicitly rather than described as kernel-checked. Exact written trace computations are NOT machine-checked. No executable finite-witness/independent-checker/control/vendor/priority gate has been performed or passed.

This is still a symmetry-model result, NOT arbitraryA5-WLOG, not arbitrary40C4 rays, not a6-sector impossibility and not an unrestricted maximal100-ray solution. All original intrinsic10/4+6/5+5 branches remain OPEN. Primary must leave this now-closed covariant family for a genuinely different remaining construction/geometry. All old process/math findings, v9/v14 withdrawals, frozen histories and ZERO-credit quarantines remain permanent. Original18/exclusive-root/HOLD/cadence/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38, no early pending-review park.
