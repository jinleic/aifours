# RQLS10 — primary-definition screen, exact Gram caller and a universal three-partition projector coupling

Owner **PhysicsRQLS10-2**, original physics-5. Actual `/bin/date` BEFORE this write: **Tue Oct 27 14:51:34 PDT 2026**. **WRITTEN AUTHOR CANDIDATE**, not independently reviewed, parent-adopted, machine/kernel checked or novelty-cleared. This is the narrowly released definition-first prerequisite, not a blanket restart of the old primary.

## 1. Admission, actual inputs and primary PRIOR-CLAIM screen

Read the complete controls FIRST, then release, wrote/pinned/SENT the actual pre-body exposure ACK **before definitions or derivation**: `pre-body-exposure-ack-v1.json`, SHA `a7872019e79bb1602b54840d26215577611b8e5d9d9fa599706ce2ae7de4fdaf`, 13 LF, pin14:47:40 PDT. Then read the ENTIRE35LF frozen packet including both source endings and the entire equality receipt.

- Controls SHA `47674caca8ff652264f5e48fe05c6ea1fcaa42eb035a7c4a47c758b4e572b38c`.
- Release SHA `45d4ef9a986e870153e063773bd3513141344b9e5de18c7c5117b7db54b75f4b`.
- Packet SHA `10445b20cea55ecf5abb2e35393281a4c43492cfae6d91b4d3dc9b60e7de3863`, 35 LF/5024 B; receipt SHA `7f973200ccb32e362bc3bcc99c72658160ad788ebdc0eee80e499b78ba91622a`.

The packet permits Zhang–Cao **arXiv:2608.29201v2**, *Resolvable quantum Latin squares with maximal cardinality*, ONLY for abstract, definitions and main-theorem statements. Actual reads: [abstract](https://arxiv.org/abs/2608.29201v2), then the [HTML introduction/definitions/Theorems1.2–1.3](https://arxiv.org/html/2608.29201v2) reader lines1–58 and the continuation through Theorem1.4/next-section heading (reader requested59–64, returned through67). No construction, proof, example or further section was opened. This is a version/section citation, **not a whole-primary byte pin or verbatim-book authentication**.

### Literal primary wordings

The prose below is quoted, with mathematical notation rendered once in TeX instead of the reader's duplicated Unicode-plus-TeX display.

> “A quantum Latin square of order \(v\) is a \(v\times v\) square, denoted as \(\mathrm{QLS}(v)\), whose entries are unit column vectors from \(v\)-dimensional Hilbert space \(\mathcal H_v\), and such that each row and column forms an orthonormal basis of \(\mathcal H_v\).”

The phase convention is explicit in the primary: two unit vectors are regarded as identical if one is a global phase multiple of the other. The literal cardinality sentences are:

> “The cardinality \(c\) of a \(\mathrm{QLS}(v)\) is the number of distinct vectors in the array.”
>
> “In particular, a \(\mathrm{QLS}(v)\) with maximal cardinality implies \(c=v^2\).”

> “A transversal in a \(\mathrm{QLS}(v)\) is a set of \(v\) elements, each located in a distinct row and a distinct column, that forms an orthonormal basis of \(\mathcal H_v\). Two transversals in a \(\mathrm{QLS}(v)\) are called disjoint if they have no common cells.”

**Definition1.1** says:

> “Let \(t\) be a positive integer. A \(\mathrm{QLS}(v)\) is called \(t\)-resolvable, denoted by \(t\text{-}\mathrm{RQLS}(v)\), if it admits \(t\) sets of mutually disjoint transversals \(\mathcal T^{(r)}=\{T_i^{(r)}:i\in[v]\}\), \(r\in[t]\), such that \(|T_i^{(r)}\cap T_j^{(s)}|=1\) for all \(r,s\in[t]\) with \(r\ne s\) and all \(i,j\in[v]\).”

For t=1 the between-resolution condition is vacuous; its one collection consists of v disjoint transversals and partitions the v² actual cells. Thus the supplied registered target matches these definitions at the stated occurrence/phase scope.

### Verbatim status statements and their exact consequence

The abstract states: “We determine the existence of a maximal-cardinality \(1\text{-}\mathrm{RQLS}(v)\) with \(17\) possible exceptions based on the established research result”. **Theorem1.3** states:

> “For any integer \(v\geq7\) and \(v\notin\{10,14,18,22,26,30,34,38,42,46,54,58,62,66,74,82,94\}\), there exists a \(1\text{-}\mathrm{RQLS}(v)\) with maximal cardinality.”

**Order10 is explicitly an exception to this theorem; this version's stated main theorem does not settle it.** This last sentence is my scope conclusion, not a fabricated quotation saying worldwide openness. Theorem1.4 concerns a different n²-order two-resolvable family, not a supplied order10 settlement. No PRIOR-CLAIM STOP is triggered by the statements actually read; no claim that all later literature has been checked.

## 2. Universal statement and actual resolution incidence

The following derivation is for arbitrary n>=3 and then applies to the original n=10. It chooses no array, field tuple, parameter, numerical state or control. Let X=[n]×[n] be the ACTUAL cell labels and N=n². A particular resolution, if an object exists, labels its transversals by a map L:X→[n] that uses every label once in each row and column. Thus L is an incidence-label Latin square. **It is variable over ALL such L**, not a fixed classical construction or a claim that the quantum entries are computational basis vectors.

There are three parallel classes of n blocks: rows, columns and L-transversals. Blocks in the same class partition X; blocks in different classes intersect in one cell. The latter follows from the actual row/column/transversal incidence, not a quantum ansatz.

Ordinary inputs used below: finite-dimensional Hermitian spectral factorization, Hilbert–Schmidt inner products, Cauchy–Schwarz including its equality case, and elementary linear algebra of indicator vectors. No old trine/Weyl/sector/Gram/deformation proof, S73–S138 claim or legacy method guide is a premise. Prior exposure remains disclosed, not erased or certified uninfluential.

## 3. Exact quadratic Gram caller — both directions, same actual cells

**Theorem G.** For every n>=3, a maximal-cardinality1-resolvable QLS(n) exists iff there are an incidence label L as above and an N×N matrix G satisfying ALL of:

1. G is Hermitian and G_xx=1 for every actual cell x.
2. G_xy=0 whenever distinct x,y share a row, column or L-transversal.
3. G²=nG.
4. |G_xy|<1 for every pair of distinct cell labels.

No real, separable, symmetric, fixed-seed or sparse subclass is imposed.

**Forward.** Choose unit representatives ψ_x of the actual rays and put V=[ψ_x], G=V*V. Summing the n row ONBs gives VV*=nI. Therefore G²=V*(VV*)V=nG. Diagonal and prescribed zeros are the actual ONB facts. Distinct rays give |G_xy|<1 by the equality case of Cauchy–Schwarz. L labels the original supplied resolution, so no occurrences or transversal choices have changed.

**Converse.** Hermitian G with G²=nG has only eigenvalues0,n, hence is positive semidefinite. Its trace is N, so its rank is N/n=n. Spectral factorization gives an n×N matrix V with G=V*V. Every column is unit. Each row/column/L-transversal block has its n×n Gram submatrix equal to I, so its SAME labelled columns form an ONB of C^n. The given L blocks really are disjoint row/column transversals partitioning X. Strict off-diagonal modulus excludes every parallel pair, so cardinality is N. Thus the recovered columns satisfy the original object, not an unlifted scalar relaxation. QED.

The factorization is unaffected by zero overlaps or repeated nonzero eigenvalues. Arbitrary per-cell phases only conjugate G by a diagonal unitary and do not change the recovered rays. The strict modulus is essential: dropping it permits repeated rays and changes the original target.

This equivalence alone is an encoding, not a feasibility result. The next theorem supplies an additional simultaneous projector-span constraint which any exact Gram completion must obey.

## 4. Universal three-partition projector coupling

For an actual object define P_x=ψ_xψ_x* and M_xy=tr(P_xP_y)=|G_xy|². Let 1 denote the all-one vector in R^N, and for each block B let b_B be its indicator and u_B=b_B−1/n·1.

**Theorem C (necessary coupling).** The following hold simultaneously for ALL three parallel classes:

- M is a real positive-semidefinite Hilbert–Schmidt Gram matrix, with diagonal1, the prescribed row/column/transversal zeros, and strict M_xy<1 for distinct labels.
- M b_B=1 for EVERY row, column and transversal B, and M1=n1.
- The spaces spanned by the centred row indicators, centred column indicators and centred transversal indicators are mutually orthogonal, each of dimension n−1. Their direct sum W therefore has dimension3(n−1), and **W⊆ker M**.
- Consequently `rank M <= n²−3n+3`. Equivalently, the real linear span of ALL100 ray projectors at the original order has this same general bound with n=10. The span of their traceless parts has dimension at most `n²−3n+2`.

**Proof of the operator coupling.** Every block is an actual ONB, so `sum_(y in B) P_y=I`. For every x,

`(M b_B)_x = tr(P_x sum_(y in B)P_y)=tr(P_x)=1`.

Summing this over the n blocks of any one parallel class gives M1=n1. Hence M u_B=1−(1/n)n1=0. This is a coupling across the SAME projectors in all three classes, not three independently fitted collections.

**Proof of the dimension.** Within one class,

`<u_B,u_C>=n·delta_(B,C)−1`.

The centred indicators sum to zero, and this Gram matrix has rank n−1. Between different classes their block intersection has size one, hence

`<u_B,u_C>=1−1−1+N/n²=0`.

Thus the three spaces are orthogonal with the stated dimensions. They are contained in ker M, giving the rank bound. Since M is exactly the Hilbert–Schmidt Gram matrix of the actual P_x, its rank equals the dimension of their real linear span. That span contains I (the sum of any ONB block), and subtracting I/n from each P_x separates its scalar-I direction from the traceless span. The traceless dimension bound follows. QED.

No coefficient field, projector-entry normalization, commutant, representation irreducibility, old sector decomposition or flatness theorem is assumed in this proof. It is a universal necessary constraint on the actual rays, including unsymmetrized arrays and every allowed resolution incidence.

## 5. What this changes — and the exact failed implication

The written deliverable is an exact original-object Gram caller PLUS the simultaneous three-partition Hilbert–Schmidt kernel/span lemma. It does not exhibit G, rule it out, settle irreducible10/4+6/5+5, or constitute a new maximum-cardinality construction. No novelty beyond prior literature is asserted.

In particular, the rank bound on the LINEAR SPAN OF PROJECTORS is not a bound on the number of distinct rays. It does not force a repeated ray or a nontrivial common sector. Also a scalar matrix M satisfying the displayed positivity/zero/basis-sum/kernel/rank conditions is not automatically a Schur-modulus lift of a physical G.

**Exact unpaid implication:** one still needs a Hermitian phase-compatible G with `|G_xy|²=M_xy`, G²=nG and all three block orthogonalities, or an all-variable proof that no such lift exists over every incidence L. Neither entrywise positivity, the projector-span dimension nor the incidence kernel supplies that lift or exclusion. Treating independent row/column/transversal overlaps as a common physical array would omit precisely this coupling.

**Next genuinely admitted step:** within these SAME definition-only inputs, determine whether the necessary overlap constraints themselves are ever inconsistent, or whether there is a universally feasible FORMAL overlap relaxation. That is an exact logical test of the failed implication, not a selected physical state/parameter or numerical viability probe. Any resulting formal matrix must be kept distinct from an actual Gram lift and original witness.

## 6. Source/STOP/history and acceptance boundary

The primary reads were restricted to abstract/definitions/main-theorem statements; no theorem proof/construction/example was used. Main-authored definitions alone were not labelled primary/book authentication. The permitted supplied final-report statements were not needed as mathematical premises here. No old proof/review/park/checkpoint/scout/map/held body was opened; no S98–S138 or S73–S97 result, selected-probe output or consuming guide is imported.

This release does not clear v189 outside its exact definition-first scope. ENTIRE protected episode and ALL consumers remain ZERO; S98–S138 HELD, S73–S97 not certified clean, all old findings/early-park/cadence/reciprocal/source/clock qualifications permanent. N4 UNKNOWN historical child exit unestablished, aux214 STOP, HOLDv2 unchanged.

No scientific interpreter/calculator/Eval arithmetic/CAS/program/enumeration/solver/replay/build/test/typechecker, selected numeric/control/boundary/decimal probe, nested agent/modelCLI/paidAPI, Git/delete/publication/contact/infra action. Metadata clocks/hashes only. Original target remains OPEN; written result needs frozen full-scope reviews and Main's complete reads before adoption. Same18/newOWNroot/deadline2026-10-31T21:23:27.000Z/substantivecycles<=20min target and honestgap if>30min. No final park or96hcompletion claim.

**END — exact caller and necessary actual-projector coupling; physical Schur lift/exclusion remains unpaid.**
