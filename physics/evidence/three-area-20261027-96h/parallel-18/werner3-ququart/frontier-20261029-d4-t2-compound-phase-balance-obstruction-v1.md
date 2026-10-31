# An all-variable phase-balance obstruction for the d4 compound certificate

**PhysicsResearch96h-2 / physics-1. WRITTEN source-independent candidate; UNREVIEWED.** This packet continues the original complex-traceless-pair dual at the genuine both-squares-nonnormal frontier. It proves an exact graph characterization of when the adopted f274 compound majorant is tight, and a positive, explicit fixed-basis overestimation bound on a generic set. It identifies a precise all-product-basis premise that would yield a genuine **certificate nonnecessity** result at an original dual equality pair.

It does **not** produce a pair with η>2L, an original T2 counterexample, or a proof of T2/T3/Z2. Fixed-basis certificate failure or overestimation is never treated as a physical counterexample. No selected physical q-value, held episode/consumer/guidance, invalid arbitrary-T bound, source certificate, external model or finite numerical search is used. No novelty, global equality, parent/reviewer/human/family/formal/Lean or operational claim is made.

The parent f274 and f281 dispositions were read in full before the present reasoning and remain at their exact qualified same-harness scopes. The later f281 normal-factor result is not a premise for a new normal-class claim here. The former stale-authority owner checkpoint at 19:12 was additively corrected and disclosed at 19:13; no continuous work is inferred for that interval.

## 1. Original dual and the compound graph

For any traceless complex A,B∈M_4(C), set

`X=A⊗I_4+I_4⊗B`, `L=||A||F²+||B||F²`, `H=X†X>=0`.

The two-copy dual target is `S2(X):=σ1(X)²+σ2(X)²<=2L`. The f274 compound K(H) is `H⊗I+I⊗H` restricted to `wedge² C^16`; in the i<j pair basis, it is a 120×120 Hermitian PSD matrix with

`K_(ij),(kl)=h_ik δ_jl+h_jl δ_ik−h_il δ_jk−h_jk δ_il`,
`λ_max K=S2(X)`.

For any local-product basis define `R=|K|` entrywise, a real symmetric nonnegative matrix. The f274 all-basis optimized majorant is

`η(A,B)=min_(U,V∈U4) ρ(R_(U,V)) >= S2(X)`.

The minimization is attained by compactness and continuity. Define the **optimized modulus inflation**

`δ_*(A,B)=η(A,B)−S2(X)>=0`.                                          (1)

No statement that η≤2L or that δ_* vanishes is assumed.

## 2. Exact phase-balance criterion, including disconnected graphs

For an arbitrary Hermitian PSD matrix K, put R=|K| entrywise. Its support graph has vertices the pair coordinates and an undirected edge i—j whenever i≠j and R_ij>0; diagonal entries are retained as vertex weights. A connected component is **phase-balanced** when the product of the unit phases `K_ij/R_ij` around every oriented cycle is1. Equivalently, a diagonal unitary makes the component of K entrywise nonnegative: choose a root and propagate vertex phases along a spanning tree; the cycle condition makes the result path-independent. A one-vertex component is balanced vacuously.

**Theorem 2.1.**

`λ_max K = ρ(R)` iff **at least one** phase-balanced connected component of R attains the global maximum Perron radius.                                  (2)

*Proof.* Both K and R split along the support components. For a connected nonnegative symmetric component R_c with radius r>0, choose its strictly positive Perron vector p. For every vector z,

`z†K_c z <= |z|^T R_c |z| <= r ||z||²`.

Equality in the second inequality forces |z| to be a Perron vector; connectedness makes every coordinate nonzero. Equality in the first then forces all edge phases, relative to z_i/|z_i|, to be nonnegative real, giving the diagonal gauge and cycle balance. Conversely a balanced component is diagonally unitarily similar to R_c and has top eigenvalue r. Taking the maximum over components proves (2). If R=0 the statement is immediate. ∎

**Corollary 2.2 (exact original-pair criterion).**

`η(A,B)=S2(X)` iff there exist local unitaries U,V for which at least one maximum-Perron component of `|K(H_(U,V))|` is phase-balanced.                         (3)

The strict alternative follows without a uniform-graph assumption: if no such basis exists, then η>S2, because the continuous function `ρ(|K(H_(U,V))|)−S2` is strictly positive on compact U(4)² and attains its minimum.

## 3. A universal quantitative fixed-basis obstruction

Assume H is 16×16 PSD and **every offdiagonal entry is nonzero** in the chosen product basis. Then the support graph of R=|K(H)| is the Johnson graph J(16,2): two unordered pairs are adjacent exactly when they share one index. It is connected with diameter2. Let p>0 be its unit Perron vector, and define the strictly positive, explicitly computable quantity

`m(H)=min_(i<j, R_ij>0) R_ij p_i p_j`.

**Theorem 3.1.** In this fixed basis,

`ρ(|K(H)|)−λ_max K(H) >= m(H)/7 > 0`.                                (4)

*Proof.* Write `K_ij=R_ij exp(iθ_ij)` on edges. Since K_ii=R_ii≥0 and Rp=ρp, for any z and `w_i=z_i/p_i` the exact magnetic-graph identity is

`ρ||z||²−z†Kz = Σ_(i<j) R_ij p_i p_j |w_i−exp(iθ_ij)w_j|²`.        (5)

Choose any a<b<c<d among the 16 one-particle indices. In the wedge basis, the triangles `{ab,ac,bc}` and `{ad,bd,cd}` have normalized cycle products `−ξ` and `+ξ`, respectively, where `ξ=h_ab h_bc h_ca/|h_ab h_bc h_ca|`. Their flux defects sum to4: `|1−ξ|²+|1+ξ|²=4`. One triangle therefore has `ω:=|1−phase|²>=2`.

Let a vertex of that triangle be the root and let `S` be the sum of the unweighted squared differences on all edges. Telescoping around the triangle and Cauchy–Schwarz give `ω|w_root|²<=3S`. Every graph vertex is within distance2 of the root; a path telescoping inequality gives `|w_v|²<=2|w_root|²+4S`. Since `Σ_v p_v²=1`,

`||z||²=Σ_v p_v²|w_v|² <= (6/ω+4)S <=7S`.

The right side of (5) is at least m(H)S. Taking the infimum over unit z proves (4). ∎

This is a bound on **fixed-basis overestimation**, not a claim that η>2L. A different local product basis may remove edges, alter components or achieve phase balance. It does not contradict f274's exact normal-pair result.

## 4. Relation to an original-domain certificate failure

Equations (1)–(3) give the exact all-variable identity

`η(A,B)>2L  iff  δ_*(A,B)>2L−S2(X)`.                                (6)

In particular, if a traceless pair is independently proved to satisfy `S2(X)=2L`, then

`η(A,B)>2L  iff  NO local-product basis has a balanced maximum-Perron component`.  (7)

Thus a valid original-domain proof that the f274 certificate is **not necessary** would consist of: (i) a pair in the unpaid both-squares-nonnormal complement with independently established S2≤2L, preferably equality; and (ii) a proof of the all-product-basis graph obstruction in (7), or the stronger margin comparison in (6). No such pair or all-basis obstruction is supplied here. Failure of a single basis is not enough, and a pair with S2>2L would instead be a genuine T2 counterexample, not merely certificate nonnecessity.

## 5. Where the fixed-basis theorem applies, without overclaiming the complement

For arbitrary A,B, the entries of H in a product basis are

`h_(ij),(kl)=(A†A)_ik δ_jl+δ_ik(B†B)_jl+bar A_(ki) B_jl+A_ik bar B_(lj)`.

For every offdiagonal index pair, this is a nonzero real polynomial in the real and imaginary coordinates of traceless A,B: if both local indices differ, the monomial `bar A_(ki)B_jl` is available; if only one differs, an offdiagonal entry of that factor times a freely adjustable traceless diagonal entry of the other is available. Their finite common nonvanishing set is therefore open dense in `sl_4(C)×sl_4(C)`. On this all-variable set, Theorem 3.1 applies in the fixed coordinate basis. It also intersects the previously supported f274 open both-squares-nonnormal region, but this does **not** establish an example outside the full f274 certified set or any failure of η.

The **first unpaid premise** for extending this to an actual f215/f274 complement obstruction is an original pair plus an all-local-basis lower bound satisfying (6) or (7). Completeness of H in one coordinate basis, genericity, the strict gap (4), or failure of one tested basis alone cannot replace it. The full T2, T3, Z2 and global equality obligations remain unpaid.

## 6. Provenance and diagnostics

This packet uses only the original compound definition and compactness from the adopted f274 disposition, elementary Perron/Rayleigh equality, a displayed exact graph identity and ordinary polynomial nonvanishing. The paired triangle calculation is an all-index symbolic identity; **no selected physical C/q diagnostic or finite search** is performed. No invalid unrestricted-T block estimate, f198/f215/f281 review body, source certificate or held guidance is a premise. The parent f198/f215/f274/f281 dispositions and their same-harness limitations remain unchanged. The 19:12 stale owner status checkpoint was additively corrected and disclosed at 19:13; no continuous work is inferred for that interval.
