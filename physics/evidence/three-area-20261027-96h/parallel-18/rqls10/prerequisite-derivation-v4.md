# RQLS10 — exact final-row defect obstruction and an actual uniform-overlap completion theorem

Owner **PhysicsRQLS10-2**, original physics-5. Actual `/bin/date` BEFORE this write: **Tue Oct 27 15:13:10 PDT 2026**. **WRITTEN AUTHOR CANDIDATE**, not reviewed/adopted, machine/kernel checked or novelty-cleared. Continued inside the SAME S1 definition-first scope after the assigned w7 review was actually returned; no approval sought per algebraic step and no review theorem imported.

## 1. Input and full original-object scope

Inputs remain the actual QLS/resolution/ray-cardinality definitions, the frozen definition/control packet SHA `10445b20cea55ecf5abb2e35393281a4c43492cfae6d91b4d3dc9b60e7de3863`, and elementary orthogonal-projection/trace/finite linear algebra. The primary definition/status read is exactly as v1: arXiv2608.29201v2 abstract/definitions/main-theorem statements ONLY;10 is explicitly a possible exception, not a settled order in that statement. No new primary proof, construction or legacy body was opened.

Let X=[n]×[n] and let L range over ALL Latin incidence labelings of n transversal blocks. The original n=10 target still requires the SAME n² pairwise nonparallel rays and all three ONB partitions, without a selected pattern being WLOG. Results below hold for arbitrary actual partial arrays at any n>=3; the uniform-overlap completion corollary assumes n>=4. No physical array/parameter/control is numerically chosen or evaluated.

A valid k-row partial array means actual unit rays in those rows, row ONBs, mutual orthogonality within each currently occupied column and each currently occupied L-transversal. Strict global distinctness is retained separately where needed. The earlier partial-lift source v3 is immutable (109LF SHA `182d50700cb4464e4074ef7780a72539f6cd3d655e7b297ac4c46cecedf0d1c7`); all facts needed here are proved directly rather than presumed adopted.

## 2. Defect projectors carry the SAME-array coupling

Write P_(r,j) for the actual rank-one projectors in the k occupied rows. For each column j and each transversal label ell define

`C_j=I−sum_(occupied r) P_(r,j)`,

`T_ell=I−sum_(occupied r) P_(r,k_r(ell))`,

where k_r(ell) is the UNIQUE actual column in row r with label ell.

Each sum consists of k mutually orthogonal rank-one projectors, so C_j and T_ell are orthogonal projectors of rank d=n−k. Summing over j or ell and using each occupied row ONB gives the exact global identities

`sum_j C_j=dI`, `sum_ell T_ell=dI`.

For an unfilled row s and tau(j)=L(s,j), the actual allowed subspace for its cell j is

`S_j=range(C_j) intersect range(T_tau(j))`.

This is an intersection of two ACTUAL defect subspaces. It is NOT generally the range of their product, and no commutation of the two projectors is assumed. Independent column/transversal defects cannot simply be identified.

## 3. Theorem D — complete last-row obstruction/recovery

Suppose exactly n−1 rows are occupied by a valid actual partial array. Then:

1. Both {C_j} and {T_ell} are rank-one ONB projector families.
2. The partial array has a completion as a1-resolvable QLS with its SAME L iff

   `C_j=T_tau(j)` for EVERY j.

3. It has a MAXIMAL-cardinality completion iff those equalities hold AND

   `tr(C_j P_x)<1` for EVERY j and EVERY earlier actual ray x,

   assuming the earlier rays were already pairwise nonparallel.
4. Whenever completion is possible, the last-row ray projectors are uniquely determined as P_(s,j)=C_j. Vector representatives remain free only up to their individual phases.

**Proof.** Here d=1. Each defect family has n rank-one projectors summing to I. Factoring them as unit-vector columns gives a square matrix U with UU*=I; thus it is unitary and each family is an ONB. A new ray must lie in both one-dimensional ranges C_j and T_tau(j), so it exists iff those two projectors are equal. If all equalities hold, use C_j as the missing cell projectors. They form the required row ONB and are orthogonal to all earlier rays in both their actual columns and transversals. Conversely any completion must use those unique column defects, giving the equalities. Pairwise nonparallelity of unit rays is precisely strict projector overlap<1; the last-row ONB already ensures mutual distinctness within that row. This proves all claims. QED.

This is not a necessary-only spectral interface: equality of the two ACTUAL defect families really constructs the missing rays. It also does not drop cardinality: an aligned defect that repeats an earlier non-collinear-position ray would complete a lower-cardinality object, not the original target.

## 4. Exact overlap score and its actual original caller

Choose unit representatives of the two defect ONBs and put

`A_(j,ell)=tr(C_j T_ell)`.

A is the entrywise squared modulus of their actual change-of-basis unitary, hence is nonnegative and doubly stochastic, with entries at most one. The required last-row alignment is equivalent to

`sum_j A_(j,tau(j))=n`,

because each of the n terms is at most one and equality of a rank-one overlap to one means equality of the rays. A strict deficit therefore forbids completion of THIS actual partial array at this SAME prescribed L. An arbitrary permutation matching the defect bases is insufficient unless it is the required tau.

This score is computable algebraically from OLD ACTUAL overlaps without a phase choice for the missing row. Let k_r(j) be the old-row column carrying tau(j). Expansion gives

`A_(j,tau(j))=2−n+sum_(r,t occupied) tr(P_(r,j) P_(t,k_t(j)))`.

Since tau(j)=L(s,j), every k_r(j) differs from j, so terms with r=t are zero by the occupied row ONB. Consequently every valid actual n−1-row partial array obeys

`n−2 <= sum_(r!=t occupied) tr(P_(r,j) P_(t,k_t(j))) <= n−1`.

The upper endpoint is REQUIRED for completion, at EVERY j, together with the distinctness test in Theorem D. These inequalities are consequences of actual rank-one defects, not sufficient conditions for an abstract scalar overlap table to have such defects.

A proof that every eligible partial array necessarily has a strict score deficit or a repeated defect would be an unrestricted no-completion mechanism at the final-row interface; NO such universal proof is provided. A deficit for one partial array alone is not a global no-go, since other earlier-row choices and L remain available.

## 5. Theorem U — actual uniform-overlap partial arrays automatically finish

Let n>=4. Suppose a valid ACTUAL n−1-row partial array has the following squared overlaps for EVERY pair of its distinct cells:

- zero if the cells share an occupied row, column or L-transversal;
- `1/(n−2)` otherwise.

Then its unique last-row defects complete it to a maximal-cardinality1-resolvable QLS(n), and the FULL n²-cell squared-overlap matrix has exactly that same pattern. No phase-lift assumption for the last row is left unpaid.

**Proof of defect alignment.** In §4's off-diagonal-row sum, there are (n−1)(n−2) terms. For r!=t, cells (r,j) and (t,k_t(j)) have different rows and different columns (k_t(j)!=j). Their L-labels differ as well: the latter has tau(j), which does not appear in column j in any occupied row. Thus every such term is `1/(n−2)`. Their sum is n−1, giving A_(j,tau(j))=1 for every j. Theorem D therefore supplies the actual missing row, with correct columns and resolution labels.

**Proof of all new overlaps and cardinality.** For any earlier cell (r,k),

`tr(C_j P_(r,k))=1−sum_(t occupied) tr(P_(t,j) P_(r,k))`.

If k=j, the result is zero by the column defect; if L(r,k)=tau(j), it is zero by the now-equal transversal defect. Otherwise k!=j and L(r,k)!=tau(j). In the old column-j sum there are exactly TWO zero contributions: t=r (same row), and the unique t whose column-j label equals L(r,k) (same transversal). That second t is an occupied row, not s, since L(r,k)!=tau(j); it differs from r by the Latin row property. All remaining n−3 contributions have the prescribed nonzero overlap. Thus

`tr(C_j P_(r,k))=1−(n−3)/(n−2)=1/(n−2)`.

This is strictly below one because n>=4. The earlier partial rays were also distinct by their assumed0-or-strictly-below-one overlaps, and the new row is an ONB. Hence the full array has n² distinct rays and the stated complete overlap pattern. QED.

**Forward/converse branch caller.** A full physical lift of the formal uniform-overlap matrix from v2 restricts to an actual n−1-row partial array satisfying Theorem U. Conversely ANY such actual partial array supplies its FULL physical lift by the explicit defect formula. This is an exact equivalence for that equality branch, over every L; it is not an assertion that every original witness has uniform overlaps or can be normalized to them.

No actual n−1-row partial array with these properties is supplied. In particular the sparse two-row lift of v3 is NOT claimed to meet this uniform-overlap hypothesis, nor does its pairwise matching proof create the required n−1-row data. Scalar M_* feasibility from v2 also does NOT supply those actual partial rays.

## 6. Exact remaining original-level step and continuation

This packet gives a genuine actual-object coupling: once n−1 rows are ACTUAL, column and transversal defects each automatically form an ONB, and their prescribed alignment plus strict distinctness is NECESSARY AND SUFFICIENT for the missing row. Within the universal uniform-overlap equality branch, all final-row phase/recovery issues are explicitly paid by those actual partial data.

The original question still requires either a FULL actual rank-one lift (for some L, not necessarily uniform), or a no-lift proof covering ALL admissible overlaps, L and actual earlier choices. No such object or universal exclusion is established. A proof of failure for the uniform branch alone would not cover nonuniform solutions; a formally feasible scalar overlap table is not an actual partial array.

Next admitted original-level work is to attack actual multirow/defect compatibility, not merely repackage scalar feasibility: either construct the requisite actual partial rows and aligned defects, or derive a universal defect obstruction that retains all original choices. No concrete excluded guide or numerical/selected-state experiment is used to choose or fill this missing step.

All source/proof/method STOPs outside S1, S98–S138 HELD, S73–S97 not certified clean, ENTIRE selected episode and every consumer ZERO, process/cadence/contact/clock histories, N4UNKNOWNhistoricalexitunestablished and aux214STOP persist. No oldbody/source expansion. No scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/build/test/typechecker, chosen numeric/control/boundary/decimal probe, nested agent/modelCLI/paidAPI, Git/delete/publication/contact/infra action. Universally quantified exact WRITTEN algebra only; no novelty/stronger verification/adoption claim. Same18/newOWN/deadline2026-10-31T21:23:27.000Z/substantive20min target and truthfulgap if>30min.

**END — exact final-row obstruction and conditional physical completion; full actual partial-row existence/universal exclusion remains open.**
