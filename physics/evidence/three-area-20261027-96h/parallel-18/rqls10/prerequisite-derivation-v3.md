# RQLS10 — an actual nonparallel two-row lift for every resolution incidence, and the exact remaining row-extension/purity obstruction

Owner **PhysicsRQLS10-2**, original physics-5. Actual `/bin/date` BEFORE this write: **Tue Oct 27 15:05:27 PDT 2026**. **WRITTEN AUTHOR CANDIDATE**, unreviewed/unadopted, not machine/kernel checked or novelty-cleared. Returned assigned w7 SPR review before this own-work resumption; no SPR theorem or review verdict is a mathematical premise here.

## 1. Scope, original caller and allowed inputs

Same narrow S1 definition-first release and primary definitions as v1: actual order10 means100 nonparallel rays, all row/column ONBs and one full partition into ten transversal ONBs. The supplied primary version lists10 among Theorem1.3's exceptions, not as a settled order. No new paper proof, construction/example or legacy body was opened.

The derivations below use only that actual-object definition and elementary finite linear algebra, a finite bipartite matching argument proved inline, and finite-dimensional compactness. No S73–S138, selected-probe/phase/sector guide, old seed/deformation/Weyl/trine result, external mathematical source or protected consumer is an input. Prior exposure is disclosed, not certified absent or uninfluential.

Main's continuation asks for a genuine original-level all-lift obstruction or actual rank-one-projector lift, not another scalar encoding. This packet supplies an **ACTUAL partial lift**, uniformly for ANY resolution incidence and ANY given first-row ONB, and identifies exactly why its constructive step does not produce a complete array. It does not pretend two rows are the full original witness.

Let n be any even integer at least8, then apply to n=10. Let L:[n]×[n]→[n] be ANY Latin incidence labeling for the proposed resolution. All L are retained; the quantum entries are not assumed classical. Let a first actual row r have arbitrary ONB e_1,...,e_n. Fix another row s. For each column k, let sigma(k) be the unique column in row r whose L-label equals L(s,k). Sigma is a permutation without fixed points, since columns of L also have distinct labels.

## 2. Theorem P — uniform actual two-row lift

For EVERY such n,L,r,s and arbitrary first-row ONB, there is a second-row ONB u_1,...,u_n such that:

- u_k is orthogonal to e_k (same actual column) and e_sigma(k) (same actual transversal);
- no u_k is parallel to ANY e_j;
- consequently these two rows have2n distinct actual rays, with all currently required column/transversal cross-orthogonalities.

The proof constructs actual vectors/projectors, not only a feasible squared-overlap matrix. It makes no claim of extension to the other rows or WLOG normal form for an arbitrary full solution.

### 2.1 Matching two available columns to each coordinate pair

Seek an n×n unitary W with entries W_jk=0 at j=k and j=sigma(k). Its columns in the basis e give u_k. These are two disjoint forbidden permutation matchings: each column and each coordinate row has exactly two forbidden positions.

Partition the n coordinate rows into ANY n/2 pairs P. For each P let A_P be the columns forbidden at NEITHER row of P. The union of the two rows' forbidden column sets has size at most four, so

`|A_P|>=n−4`.

Each column is forbidden in exactly two coordinate rows, hence belongs to the complement of A_P for at most two disjoint coordinate pairs. Thus the union of A_P over ANY three or more pairs is ALL n columns.

Make two identical left copies of each pair P, each with neighbours A_P, and one right vertex per column. Hall's condition holds:

- one pair's copies have at least n−4>=4 neighbours, enough for its at most two copies;
- two distinct pairs' copies have at least n−4>=4 neighbours, enough for their at most four copies;
- for k>=3 distinct pairs, the union is all n columns, and there are at most2k<=n copies.

Any subset of copies has the same neighbourhood as its underlying distinct pairs and no larger cardinality than the bound above. Therefore a matching assigns two distinct columns C_P to every pair, with the C_P partitioning all columns.

For completeness, the finite matching implication is elementary: choose a maximum matching; if a left vertex is uncovered, its alternating reachable left/right sets A,B satisfy N(A)=B, every right vertex in B is matched (otherwise augment), and its matched partner is in A. With the original unmatched left vertex this gives |A|=|B|+1, contradicting Hall. This is a proof, not an executed matching search or enumeration.

### 2.2 Actual unitary and rank-one projectors

On each 2-by-2 rectangle P×C_P put ANY real unitary block

`H_P=(a_P²+b_P²)^(-1/2) [[a_P,-b_P],[b_P,a_P]]`,

where a_P,b_P are ARBITRARY strictly positive real symbols. Set all other entries of W to zero. Each C_P lies in A_P, so no forbidden entry is used. Disjoint row/column pairs and the displayed block identity give W*W=WW*=I. Every nonzero entry has modulus strictly between zero and one; none of the symbolic parameters is numerically chosen/evaluated.

Define `u_k=sum_j W_jk e_j`. This is an ONB, obeys both required forbidden orthogonalities, and |<e_j,u_k>|<1 for EVERY j,k, so every cross-row ray pair is nonparallel. The actual projectors u_k u_k* therefore give the claimed two-row partial lift. QED.

This establishes that a no-go mechanism involving only ONE pair of row bases and its column/transversal matchings cannot refute the original order10 target: every such incidence pair has an actual nonparallel quantum completion. The full multirow coherence remains essential.

## 3. Exact all-variable row-extension interface

The next row is NOT obtained by independently repeating the matching step. Suppose k<n actual row ONBs have already been chosen, with all mutual column/transversal orthogonality and all their kn rays pairwise nonparallel. Let s be an unfilled row, with the SAME full incidence L. For each new column j define S_j to be the orthogonal complement of the span of:

- the k existing rays in column j;
- the k existing rays carrying label L(s,j), one from each earlier row.

The two rays from each earlier row are distinct by the Latin property. All actual complex dependencies across different earlier rows remain; no independence or dimension equality is assumed. A next row is exactly an ONB u_j with u_j∈S_j and all u_j nonparallel to every earlier ray. This is necessary and sufficient for extending that actual partial array by one row, without changing old cells or resolution labels.

An immediate valid obstruction is

`dim(sum_(j in J) S_j)<|J|`

for some collection of new columns J: no orthonormal selection could fit those |J| independent vectors. No such violation is exhibited here, nor is the converse inferred merely from this necessary dimension condition.

After two rows the S_j are generally not coordinate-exclusion sets for one common anchor basis. A finite matching of coordinates no longer proves that its selected vectors can be made orthonormal simultaneously inside these actual subspaces. This is the precise failed step in iterating Theorem P; the existing two-row construction is not a complete rank-one lift.

## 4. Complete compact purity criterion, with strict distinctness retained

There is an exact test of that failed implication which does not relax rank-one purity silently. Let P_x range over ALL earlier actual ray projectors. For an arbitrary real delta>0, define C_delta as the tuples of Hermitian matrices E_1,...,E_n satisfying:

1. E_j is positive semidefinite and tr(E_j)=1;
2. range(E_j)⊆S_j;
3. sum_j E_j=I;
4. tr(E_j P_x)<=1−delta for EVERY j and EVERY earlier ray x.

All support/sign/row-sum/overlap conditions are closed and convex in E at fixed actual prior data and delta. Positive semidefinite trace-one matrices are bounded, so C_delta is compact, possibly EMPTY. No delta or matrix tuple is numerically selected.

Define `F(E)=sum_j tr(E_j²)`. Each E_j has nonnegative eigenvalues summing to one, so tr(E_j²)<=1, with equality iff E_j is rank one. Therefore

`F(E)<=n`, with equality iff ALL E_j are rank one.

If C_delta is nonempty, its maximum F is attained. Such a maximum equals n **iff** the given actual partial array has a next-row completion with the stated positive nonparallelity margin delta.

**Forward from equality.** Write E_j=u_j u_j* with unit u_j∈S_j. Then sum E_j=I says UU*=I for the SQUARE matrix U=[u_1,...,u_n]; hence U is unitary and these are an actual next-row ONB. The overlap inequalities give |<u_j,psi_x>|²<=1−delta<1, excluding every old ray. Thus this is the original next-row object, not a collection of independent effects.

**Converse from an actual extension.** Take its rank-one E_j. The finite set of new-versus-old squared overlaps is strictly below one. Its maximum is below one, so some common delta>0 satisfies all the inequalities. (With no earlier rows, that condition is vacuous.) The tuple lies in C_delta and F=n. QED.

Thus extension exists iff **there is some delta>0 with nonempty C_delta and maximum F=n**. Infeasibility of one particular margin excludes only that margin, not all possible strictly nonparallel extensions. A nonempty fractional/effect tuple alone does NOT supply rank-one projectors, and compactness alone does NOT prove its maximum purity is n.

The full original object would require actual compatible choices through every remaining row, for the SAME L and previously chosen rays. Independently feasible extension fibres for unrelated prior data cannot be composed. Conversely an actual full object provides those fibres and choices. Both directions retain all original occurrence labels, values, complex inner products and strict ray distinctness.

## 5. Exact result and current original-level obstruction

Theorem P is a uniform ACTUAL two-row construction, not a scalar relaxation. It shows pairwise row/transversal zero-pattern feasibility is not the missing global obstruction at order10. The row-extension/purity theorem pays a complete actual-object caller for the next step and identifies precisely what a fractional or matching argument would fail to prove.

**Still unpaid:** either supply a genuinely coherent full n-row rank-one lift for one complete L, or prove an obstruction covering ALL possible L and actual prior choices. In the extension representation, this requires actual purity attainment with a strict common overlap margin, or a universal no-completion mechanism; neither the two-row construction, mere nonempty effect fibres nor necessary subspace dimensions pay it. No particular partial-row failure would imply unrestricted nonexistence, because another earlier-row choice might extend.

No actual100-ray witness, all-M/all-L no-lift theorem, original10/4+6/5+5 closure, new numerical band or novelty claim is delivered. The next genuinely admitted question is whether the actual subspaces S_j arising from valid partial arrays force purity attainment, or can be shown to obstruct every possible continuation; that remains unproved. No old protected phase/sector method is reconstructed to fill it.

All source/proof/method STOPs outside S1, S98–S138 HELD, S73–S97 not certified clean, ENTIRE selected episode and all consumers ZERO, old process/exposure/cadence history, N4 UNKNOWN historical exit unestablished and aux214 STOP persist. Old files and earlier new candidates remain immutable. No scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/build/test/typechecker, selected state/count/control/parameter/boundary/decimal probe, nested agent/modelCLI/paidAPI, Git/delete/publication/contact/infra action. All constructions are universally quantified WRITTEN algebra, not evaluated instance checks. Same18/OWN/researchdeadline2026-10-31T21:23:27.000Z/substantive20min target and honestgap if>30min. Needs complete frozen-scope reviews and Main's full reads before adoption.

**END — actual two-row lift established in writing; complete multirow rank-one/purity coupling remains unresolved.**
