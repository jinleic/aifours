# Exact fixed-basis phase balance for the d4 compound certificate

**PhysicsResearch96h-2 / physics-1. WRITTEN all-variable candidate; UNREVIEWED.** This self-contained successor replaces `frontier-20261029-d4-t2-compound-phase-balance-obstruction-v1.md`, SHA256 `edbc9cf90d879a5974c05c7304b03a4f8336a113bccd402553852a74e00ffd79`, only as the owner's proposed review candidate. V1 and every independently frozen scope remain unchanged.

The new result gives a **complete graph/phase characterization** of fixed-basis exactness when the one-particle support graph is connected, extending the adopted f281 path case to π-flux cycles and proving a phase-independent branching obstruction. It is an all-variable method obstruction and an exact first unpaid premise for certificate nonnecessity on the original dual domain, not a new closed family of physical states.

It does **not** exhibit η>2L, a T2 counterexample, a fully optimized η result on arbitrary inputs, T3/Z2/global equality, novelty, parent/reviewer/human/family/formal/Lean or operational acceptance. Failure of a restricted basis is never treated as a physical counterexample. No selected physical C/q-value, source certificate, f198/f215/f281 review body, invalid arbitrary-T norm lemma, or held episode/consumer/guidance is used.

## 1. Original dual and exact phase-balance criterion

For traceless A,B∈M_4(C), put `X=A⊗I+I⊗B`, `L=||A||F²+||B||F²`, `H=X†X>=0`. The original two-copy dual is `S2(X):=σ1(X)²+σ2(X)²<=2L`.

The additive second compound K=H^[2] is the restriction of `H⊗I+I⊗H` to `wedge² C^16`. In the canonical pair basis |i∧j>, i<j,

`K_(ij),(kl)=h_ik δ_jl+h_jl δ_ik−h_il δ_jk−h_jk δ_il`,
`λ_max K=S2(X)`, `K>=0`.

For a fixed local-product basis, set R=|K| entrywise. Its support graph has one vertex per unordered pair, an edge at each nonzero offdiagonal R entry, and retains R's nonnegative diagonal vertex weights. For a connected component, call the K edge phases **balanced** if their oriented product is1 around every cycle. Equivalently a diagonal unitary makes that component entrywise nonnegative; a one-vertex component is balanced vacuously.

**Theorem 1.1 (all variables, all components).** `λ_max K=ρ(R)` iff at least one balanced support component of R has the maximum Perron radius among all components.

*Proof.* On each component, `z†Kz<=|z|^T R|z|<=ρ(R)||z||²`. When equality holds at a connected component's Perron radius, the positive Perron vector has full support and equality in the triangle inequality aligns every edge phase with the phases of z; this is exactly a gauge/balanced-cycle assignment. Conversely such a gauge identifies the component with its nonnegative modulus. Both matrices are block diagonal over support components; take their maxima. R=0 is immediate. ∎

The f274 optimized quantity `η(A,B)=min_(U,V∈U4)ρ(|K(H_(U,V))|)` is continuous and its minimum attained. Thus

`η(A,B)=S2(X)` iff some product basis has a balanced component attaining the maximum Perron radius; otherwise `η(A,B)>S2(X)`.                (1)

The last strictness follows from compactness, not from an assumed uniform graph margin.

## 2. Connected one-particle support: exact path/cycle classification

Let H≥0 be N×N with N≥3 and connected offdiagonal support graph G. Its two-token graph T₂(G) has unordered pairs of vertices as vertices, and moves one token along a G edge to an unoccupied vertex. By the displayed formula for K, T₂(G) is exactly R's offdiagonal support graph.

**Lemma 2.1.** T₂(G) is connected.

*Proof.* Use a spanning tree of G and fix a leaf ℓ. From any pair, choose the token nearer to ℓ; its path to ℓ has no other token, so move it there. Configurations containing ℓ are connected by moving the second token in the tree with leaf ℓ removed, which remains connected. ∎

**Theorem 2.2 (complete connected-graph criterion).** For connected G,

`ρ(|H^[2]|)=λ_1(H)+λ_2(H)`

iff G is a path, or G is a simple cycle whose oriented product of normalized H edge phases is −1. If G has a branching vertex (degree≥3), the inequality is strict independently of its edge phases.

*Proof: branching.* Pick a center o and three distinct neighbors a,b,c. The two-token graph contains

`{o,a}→{a,b}→{o,b}→{b,c}→{o,c}→{a,c}→{o,a}`.

It is a simple six-cycle. Reorder the one-particle indices for this calculation so `o=0<a=1<b=2<c=3`; such reordering only permutes the pair basis up to phases. The six K entries are `−h_02, h_10, −h_03, h_20, h_01, −h_30`. Their product is `−|h_01 h_02 h_03|²<0`, so the cycle is unbalanced regardless of edge phases. By Lemma 2.1 the whole R graph is connected; Theorem 1.1 gives strictness.

*Proof: no branching.* A finite connected simple graph of maximum degree≤2 is a path or a simple cycle. On a path, first gauge the one-particle edge phases to positive and order vertices along the path. Two hard-core particles cannot cross without colliding, so every nonzero K offdiagonal is nonnegative after the induced diagonal pair gauge. Hence K is balanced, recovering the adopted f281 path argument.

On a simple cycle, label the cyclic order 0,…,N−1 and gauge the edges 0—1,…,N−2—(N−1) positive, leaving oriented boundary holonomy `g`, |g|=1. All internal two-token hops have positive phase. A hop across N−1—0 passes the other particle once, adding a fermionic minus sign. The closed two-token walk

`{0,1}→{0,2}→⋯→{0,N−1}→{1,N−1}→{0,1}`

has normalized product −g (or its conjugate under the opposite orientation). If g≠−1 it is unbalanced. If g=−1, every internal and boundary hop is nonnegative in the displayed gauge, so K is balanced. Lemma 2.1 and Theorem 1.1 finish the proof. ∎

All graph phases concern a **fixed basis** for H. Reordering a basis to analyze a graph is only a pair-coordinate similarity and is not claimed as an allowed physical local-unitary transformation.

## 3. Explicit positive fixed-basis gap for branching graphs

For connected G with a branching vertex, let D be the diameter of the connected two-token graph, p>0 the Euclidean-unit Perron vector of R and

`m=min_(i<j,R_ij>0) R_ij p_i p_j >0`.

**Theorem 3.1.**

`ρ(|K|)−λ_max K >= m/(3+2D) >0`.                                     (3)

*Proof.* Write `K_ij=R_ij exp(iθ_ij)` on edges. For every vector z and `w_i=z_i/p_i`, the Perron equation gives the exact magnetic identity

`ρ||z||²−z†Kz = Σ_(i<j) R_ij p_i p_j |w_i−exp(iθ_ij)w_j|²`.        (4)

Choose the negative-product six-cycle of Theorem 2.2 and one vertex as root. Telescoping around the cycle and Cauchy–Schwarz give `4|w_root|²<=6 S`, where S is the unweighted sum of squared edge differences. A path of at most D edges to any vertex gives `|w_v|²<=2|w_root|²+2D S`. Since `Σ p_v²=1`, `||z||²<= (3+2D)S`. The right side of (4) is ≥mS; take the infimum over unit z. ∎

For the generic fixed basis where **all** H offdiagonals are nonzero, G is complete, T₂(G) is the Johnson graph J(N,2) of diameter2, and (3) specializes to `m/7`. This fixed-basis strictness does **not** imply η>2L or a physical counterexample; an allowed local basis can change the graph.

## 4. The precise remaining all-basis obstruction

For any original traceless A,B, (1) is an exact criterion for η=S2. Therefore, if an original dual equality pair `S2(X)=2L` is independently established, then

`η(A,B)>2L` iff **no** local-product basis has a balanced maximum-Perron component of `|H^[2]|`.                                                (5)

In particular, an all-basis proof that H's support graph is connected and branching would suffice by Theorem 2.2, but is not necessary: disconnected H can also yield no balanced maximal compound component. Compactness then gives a strict optimized gap even if no uniform combinatorial edge bound is known in advance.

The **first unpaid premise** for a genuine f274-certificate nonnecessity example in the both-squares-nonnormal complement is: exhibit an independently established original dual equality pair there and prove the all-local-basis condition in (5). More generally `η>2L` iff `η−S2>2L−S2`, so for a strictly positive T2 gap one needs a quantitative all-basis modulus-inflation lower bound exceeding that gap. We prove neither existence nor the all-basis premise. The global T2, T3, Z2, η≤2L and equality classification remain open here.

## 5. Scope, provenance and diagnostics

This proof uses f274's adopted compound definition, f281's path insight, Perron/Rayleigh equality, ordinary exterior-product signs and connected-graph algebra. The six-cycle product is an all-index symbolic identity; no selected physical C/q-value, executable search or unreported diagnostic is used. No f198/f215/f281 review body, source certificate, false arbitrary-T estimate, held episode/consumer/guidance, literature-status or novelty claim is a premise. Parent dispositions remain at their exact same-harness qualifications.

The earlier stale 19:12 owner status checkpoint was additively corrected in `frontier-20261029-1913-post-disposition-stale-checkpoint-correction-v1.json`, SHA256 `34aa2cfbea94707c5bc8b0423947942a3d1d2801101650cecd4f2d8c0b171525`, and disclosed to Main; no continuous work is inferred for that interval. No frozen f196/f198/f215/f274/f281/f153/f62/f168 review scope or source bytes are altered.
