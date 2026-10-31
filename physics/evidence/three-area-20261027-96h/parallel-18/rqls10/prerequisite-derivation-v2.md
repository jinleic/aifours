# RQLS10 — universal feasibility of the incidence/projector-overlap relaxation, and the exact missing physical lift

Owner **PhysicsRQLS10-2**, original physics-5. Actual `/bin/date` BEFORE this write: **Tue Oct 27 14:55:15 PDT 2026**. **WRITTEN AUTHOR CANDIDATE**, not reviewed, adopted, formal/kernel checked or novelty-cleared. Additive next definition-only step; `prerequisite-derivation-v1.md` (117 LF, SHA `bd44c7c95d646f130c00307212fdea16a8281518d5dd732d096660bf740d018d`) remains immutable.

## 1. Exact scope and input cut

The primary-definition/PRIOR-CLAIM screen and literal quotes are in v1: Zhang–Cao arXiv:2608.29201v2, abstract/definitions/main-theorem statements ONLY. Order10 is one of Theorem1.3's possible exceptions; no order10 settlement or worldwide-current-openness conclusion was established. No paper proof/construction/example or old research body was opened for this continuation.

Inputs are the same frozen35LF definition/control packet SHA `10445b20cea55ecf5abb2e35393281a4c43492cfae6d91b4d3dc9b60e7de3863`, the permitted original definitions, and elementary real/Hermitian finite linear algebra. The necessary actual-projector identities needed from v1 are restated below; that author candidate is not assumed parent-adopted. No S73–S138 source, selected-probe output, protected guide, old sector graph, phase theorem or method-selection consumer is a premise.

**This is an all-variable FORMAL-relaxation theorem**, for every integer n>=4 and every admissible incidence-label Latin square L. It selects no physical array, numerical state, field tuple, parameter trial or finite control. A formal overlap matrix is NOT an actual vector/projector witness. The point is to prove exactly why a proposed necessary-condition obstruction does not yet address the original target.

## 2. The relaxation being tested

Let X=[n]×[n], N=n², and let L label n actual row/column transversals. Rows, columns and L-classes give three parallel classes, each partitioning X into n blocks of size n; distinct classes intersect in one cell. L ranges over ALL such labelings, not one chosen incidence pattern.

For an actual1-resolvable maximal QLS, P_x=ψ_xψ_x* and M_xy=tr(P_xP_y) give the following necessary scalar constraints:

1. M is real symmetric positive semidefinite, with M_xx=1.
2. M_xy=0 for distinct cells sharing any of the three blocks; for every other distinct pair, `0<=M_xy<1`.
3. M b_B=1 for every block indicator b_B, and M1=n1.
4. For W spanned by u_B=b_B−1/n·1, W⊆ker M and `rank M<=n²−3n+3`.

Indeed an actual ONB block has sum P_y=I, so `(M b_B)_x=tr(P_x)=1`; M is a Hilbert–Schmidt Gram matrix. Summing blocks gives M1=n1. The centred indicators then lie in its kernel. Their within-class inner products are nδ−1, their between-class inner products zero, so dim W=3(n−1). This reproduces every necessary identity being used, without an old proof import.

**Theorem R.** For EVERY n>=4 and EVERY such L, ALL four necessary conditions above have a formal solution, including the strict off-diagonal bound and the full rank constraint. Therefore inconsistency of these scalar conditions cannot be an unrestricted RQLS10 no-go. Existence of a PHYSICAL Schur/Gram lift is not asserted.

## 3. Exact all-variable construction and positivity proof

Let B be the 3n×N incidence matrix whose rows are the block indicators. This is a symbolic incidence matrix of the universally quantified L, not data from a constructed quantum state. Let J=11^T.

The space W is the orthogonal direct sum of the three centred class spaces, each dimension n−1. It is orthogonal to 1. Write U=(span{1}⊕W)^perp. Then

`dim U = n²−1−3(n−1) = (n−1)(n−2)`.

Put `P_1=J/n²`. For each parallel class, the sum of outer products of its centred block indicators acts as n times the orthogonal projector onto its centred class space: their Gram matrix is nI−J and their sole linear relation is their zero sum. Summing all three classes gives

`B^T B = n P_W + 3n P_1`.

There is no action on U. Thus

`P_U=I−P_W−P_1=I−B^T B/n+2J/n²`.

Define the FORMAL matrix

`M_*=n P_1 + n/(n−2) P_U`

`    =(nI−B^T B+J)/(n−2)`.

Both displayed spectral coefficients are strictly positive for n>=4. Since P_1 and P_U are orthogonal projections, M_* is real symmetric PSD, annihilates W, and has rank

`1+dim U = n²−3n+3`.

Moreover M_*1=n1. Since each b_B is u_B+(1/n)1, it follows immediately that M_* b_B=1 for EVERY block.

For entries, `(B^T B)_xx=3`. For distinct x,y it is one if they share a block, zero otherwise: two distinct cells cannot share two of the three block types, by transversal/Latin incidence. Consequently

- diagonal: `(M_*)_xx=(n−3+1)/(n−2)=1`;
- same-block distinct pair: `(M_*)_xy=(-1+1)/(n−2)=0`;
- all remaining pairs: `(M_*)_xy=1/(n−2)`, strictly between zero and one because n>=4.

Every required condition is met, for the FULL universally quantified incidence class. No numerical test, chosen prime/count/graph, sampling, limiting instance or program calculation is involved. QED.

This does not construct the P_x used to motivate the relaxation. A real PSD matrix is an abstract Euclidean Gram matrix, but the Euclidean vectors need not be positive rank-one n×n projectors of trace one. Replacing that physical requirement by arbitrary Gram factors would be an invalid converse.

## 4. Sharp aggregate overlap constraint — conditional equality is exactly this relaxation

The coupling also gives an exact scalar inequality for any ACTUAL object, not a new numerical band or a feasibility conclusion. Each cell has exactly 3(n−1) distinct forced-orthogonal neighbours. Hence there are

`d=N−1−3(n−1)=(n−1)(n−2)`

other cells per cell which are not forced orthogonal by incidence. Let these be A_x. Since M1=n1, its off-diagonal row sum is n−1. All forced entries are zero. Real Cauchy–Schwarz therefore gives

`sum_(y in A_x) M_xy² >= (n−1)²/d = (n−1)/(n−2)`.

Summing over x and adding the diagonal yields

`tr(M²) >= n²[1+(n−1)/(n−2)]`.

Equality holds iff, in EACH row, all its d entries on A_x equal the same row mean, namely `1/(n−2)`. Thus equality for an actual object would force its overlap matrix to be exactly M_*. Conversely the formal M_* attains the displayed aggregate scalar bound. This proves sharpness WITHIN THE RELAXATION, not physical attainability. No actual extremal object or a proof that equality is physically possible/impossible is supplied.

## 5. Exact failure mechanism and the next missing premise

Theorem R makes the failed inference precise: even positivity, all three families of actual-basis-sum identities, forced zeros, strict scalar distinctness and the strongest kernel/rank count derived above are jointly feasible as abstract overlaps, for every original order10 incidence labeling. Hence a contradiction using ONLY those conditions cannot establish the original no-go. Adding the aggregate bound of §4 does not fix this: M_* meets it exactly as a formal matrix.

The remaining physical prerequisite is still an actual Hermitian G such that

`G_xx=1; G_xy=0 on forced pairs; |G_xy|²=M_xy; G²=nG`,

with strict |G_xy|<1 at distinct cells, for some full admissible L. By v1's fully proved actual-object caller, such a lift supplies the original witness; excluding ALL such lifts over ALL L would supply a genuine obstruction. The existence/nonexistence of that lift for M_*, or for any other admissible M, is **NOT_ESTABLISHED** here. No formal matrix is labelled an actual ray array, and no unproved uniform-overlap ansatz is imposed WLOG on the original problem.

In particular this is NOT a claim that M_* is unliftable. A proof of unliftability for M_* alone would exclude only a special equality branch, not arbitrary nonuniform overlap solutions. The original irreducible10/4+6/5+5 alternatives remain OPEN; the old sector theorem is not used as a new premise in this proof.

**Precisely blocked continuation:** a further genuine original-progress step requires a NEW all-variable physical-lift compatibility condition or an actual lift/whole-class exclusion, not another necessary scalar count or a renamed old protected phase/sector guide. None is claimed established. If Main supplies an independently screened admissible source or review duty at that interface, it needs its own exact release; no legacy lookup or source-mining is performed to fill this gap.

## 6. Results, nonclaims and control frontier

Together v1 and v2 deliver: (i) the exact original complex Gram/transversal caller; (ii) the actual three-partition projector-span/kernel coupling; (iii) a universal formal-feasibility proof refuting the attempted scalar-relaxation inconsistency route; (iv) a sharp relaxation-only aggregate bound with exact equality condition. They are written candidates/failed-implication analysis, not novelty-cleared scientific acceptances or a resolution of the original target.

This is not selected-control method testing: every assertion is universally quantified in n and L and algebraically proved, with no physical numerical state or measured viability outcome. No scientific interpreter/calculator/Eval/CAS/enumeration/solver/replay/buildtest/typechecker, selected arithmetic/boundary/decimal probe, modelCLI/paidAPI/nestedagent/Git/delete/publication/contact/infra action. Only permitted definitions, ordinary linear algebra and current OWN writing/metadata.

All v189/S98episode+ALLconsumingguideZERO/S98–S138HELD/S73–S97unclean/oldSTOPs outside this narrow definition task, N4UNKNOWNhistoricalchildexitunestablished, aux214STOP and process histories persist. Old roots/closed run and v1 bytes are unchanged. No clean-cognition/noninfluence claim. Main must read complete new sources and full-scope review returns before adoption. SAME18/newOWNroot/actualsubstantive<=20min target and truthfulgap if>30min/deadline2026-10-31T21:23:27.000Z.

**END — scalar relaxation is universally feasible; the actual phase-compatible rank-one-projector lift/exclusion is still the unpaid interface.**
