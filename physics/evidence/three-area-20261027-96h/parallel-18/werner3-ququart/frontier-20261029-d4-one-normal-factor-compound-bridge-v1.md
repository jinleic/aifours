# The compound Perron certificate with one normal factor: exact structural classes and an open sufficient region

**PhysicsResearch96h-2 / physics-1. WRITTEN all-variable candidate; UNREVIEWED.** This is the one proof/obstruction packet following the seven-line proposal `frontier-20261029-2006-one-normal-factor-compound-proposal-v1.txt`, SHA256 `5a4a004fd503ceb68cbb96f9d98ffc36f68a67c2dd7dc4cc046ae72d7048d676`. It proves `η(A,B)<=2L` for substantial classes with **one normal factor and the other arbitrary or nonnormal**, strictly larger than the previously supported normal-pair class and the f274 open seed. It also gives an explicit basis-invariant sufficient test on the entire one-normal domain and discloses the remaining simultaneous-basis inequality.

It does **not** prove or refute `η<=2L` for all one-normal pairs; failure of any displayed sufficient test is not a counterexample. It makes no general T2/T3/Z2, global equality, certificate-necessity, novelty, independent-family/human/formal/Lean/operational or parent/reviewer adoption claim. No selected physical q-value, held episode/consumer/guidance, invalid unrestricted-T bound, unverified literature premise, or numerical diagnostic is used.

The complete f274 parent disposition `dispositions/physics-1-werner-d4-t2-additive-compound-perron-certificate-and-open-complement-parent-v1.md` was read after the proposal and before the present mathematics. It records 0F/0M/0m same-harness written support, not global η≤2L or certificate necessity; its provenance qualification is INCONCLUSIVE. No f274/f215/f198/f196/f168 scope changes here.

## 1. Original quantities and the normal-factor block identity

Let A,B∈M_4(C) be traceless, `X=A⊗I+I⊗B`, `L=||A||F²+||B||F²`, and H=X†X. Let K(H) be the additive second compound on `wedge² C^16`; its largest eigenvalue is exactly `S2(X)=σ1(X)²+σ2(X)²`. The adopted f274 certificate uses

`η(A,B)=min_(U,V∈U4) ρ(|K(H_(U,V))|)`,

where `X_(U,V)=(UAU†)⊗I+I⊗(VBV†)` and the modulus is entrywise in the canonical 120 pair basis. It always satisfies `S2(X)<=η(A,B)`, and η≤2L is sufficient, not known necessary, for T2.

Assume A is normal. Locally diagonalize it as `A=diag(a_1,…,a_4)`; `Σa_i=0`. For a common site-2 unitary V define

`H_i(V)=V(B+a_iI)†(B+a_iI)V†` (PSD 4×4),
`r_i(V)=ρ(|H_i(V)|)`, `f_i(V)=ρ(|K(H_i(V))|)`.

The 16×16 H is `⊕_i H_i(V)`. Its exterior square decomposes into four 6-dimensional same-block sectors and six 16-dimensional cross sectors. In a corresponding permutation of the pair basis, the **exact** modulus radius is

`ρ(|K(H)|)=max{ max_i f_i(V), max_(i<j)[r_i(V)+r_j(V)] }`.          (1)

Indeed `K(H)` restricts to K(H_i) on the same-block sectors and to `H_i⊗I+I⊗H_j` on a cross sector. Since H_i,H_j are PSD, their diagonal entries are nonnegative, and the two Kronecker-sum offdiagonal contributions occupy distinct matrix entries. Thus its entrywise modulus is exactly `|H_i|⊗I+I⊗|H_j|`, a nonnegative symmetric Kronecker sum whose Perron root is r_i+r_j.

Minimizing (1) over V produces a **restricted-basis upper bound** on η, because A-diagonal bases are allowed. It need not equal η: another U mixing A's eigenbasis could lower the fully optimized value. Consequently, failing any restricted-basis test below cannot refute η≤2L.

## 2. Exactness for path-forest blocks, including irreducible B

Call a Hermitian matrix's offdiagonal support graph a **linear forest** if it is a disjoint union of simple paths and isolated vertices.

**Lemma 2.1 (single block).** If H≥0 has a linear-forest offdiagonal graph, then

`ρ(|H|)=λ_1(H)`, `ρ(|K(H)|)=λ_1(H)+λ_2(H)`.                        (2)

*Proof.* Independently permute its vertices so each path is consecutive. A diagonal unitary removes the edge phases by starting at one endpoint of each path and proceeding along it; the transformed H is entrywise nonnegative. Such vertex permutations and diagonal gauges induce pair permutations/diagonal gauges on K and do not alter the spectra of their entrywise moduli.

For two particles occupying ordered distinct vertices of a path, a nonzero one-edge move cannot pass the other particle without colliding. The same is true for disjoint paths made consecutive: particles in separate components cannot exchange components. Thus every offdiagonal sign in the wedge-basis formula for K is positive after the one-particle gauge. Its diagonal entries are sums of nonnegative H diagonals, so K is entrywise nonnegative. H and K are Hermitian PSD; a real symmetric entrywise-nonnegative matrix has spectral radius equal to its largest eigenvalue. This proves (2). ∎

**Theorem 2.2.** Let A be normal. If a single site-2 basis V makes the offdiagonal graph of **each** H_i(V) a linear forest, then

`η(A,B)=S2(X)<=2L`.                                                   (3)

The four H_i may have different path graphs and phases: permutations and diagonal gauges in Lemma 2.1 are only devices for calculating each block's invariant radius, not fictitious independently chosen physical V's.

*Proof.* By (1) and Lemma 2.1, the radius for this actual common V is the maximum of (i) the sums of the two largest eigenvalues **within** one H_i and (ii) the sums of the largest eigenvalues of two **different** H_i. This is exactly the sum of the two largest eigenvalues of H=⊕H_i, namely S2(X). Since every admissible compound modulus radius is at least S2(X), the minimum η equals S2(X).

For the final `S2(X)<=2L`, diagonalize the normal factor A. The two top right singular vectors of X can be chosen in at most two site-1 eigenspaces, so their span has a ≤2D leg at that **one site**. The qualified f168 one-supported-site lemma gives the inequality. Its one-site proof follows directly by compressing the local factor `I−|Ω><Ω|/2` to that 2D leg, using the positive product Haar decomposition and the rank≤2 trace inequality on the remaining site. No arbitrary-T 4×2 norm estimate is used. ∎

**Concrete consequences, with no block-trace restriction.**

1. If B is unitarily reducible into blocks of dimensions at most2, each H_i has a disjoint union of one- or two-vertex paths. Thus (3) holds even if the two 2×2 blocks of B are **not separately traceless**; only Tr B=0 globally is assumed.
2. If B is unitarily similar to an upper or lower bidiagonal matrix, then both B and B†B are tridiagonal in that basis; hence every `H_i=B†B+bar a_i B+a_iB†+|a_i|²I` has a path graph and (3) holds. This class includes unitary-irreducible nonnormal B. For example, any nonzero scalar multiple of the length-four nilpotent shift is irreducible: an orthogonal projection commuting with the shift and its adjoint commutes with all matrix units they generate. This is an all-scalar structural statement, not a physical q-value.
3. More generally the displayed H_i-graph condition applies directly, whether or not B itself is bidiagonal or reducible.

These classes are strictly larger than the previously supported normal-pair class. They are distinct from the f274 open seed requiring both squares nonnormal: here A is normal. They do not exhaust arbitrary B.

## 3. An all-variable PSD4 bound and an explicit open sufficient region

**Lemma 3.1.** For every PSD 4×4 H, with `t=Tr H` and `h=||H||F`,

`ρ(|K(H)|) <= min{ 3t/2, 2h, t/2+sqrt(3) sqrt(h²−t²/4) }`.          (4)

The first bound is sharp on auxiliary rank-one PSD matrices whose vector has four equal-modulus coordinates.

*Proof.* The f274 hard-core symmetric compression, applied to H≥0, gives `ρ(|K(H)|)<=2ρ(|H|)<=2h`, since |H| is real symmetric nonnegative and `|| |H| ||F=h`.

For the 3t/2 bound first take H=uu†. Then |H|=ss^T with s_i=|u_i|. A real Perron vector of |K(H)| corresponds under the hard-core symmetric embedding to a real symmetric zero-diagonal 4×4 matrix W with `||W||F=1`. Its Rayleigh quotient is `2||Ws||²`. W is traceless, so its largest absolute eigenvalue obeys `||W||op²<=3||W||F²/4`, by Cauchy–Schwarz on the remaining three eigenvalues. Thus the quotient is at most `3||u||²/2`. For general PSD H, use its nonnegative spectral decomposition, entrywise triangle inequality, monotonicity of Perron roots for nonnegative symmetric matrices, and subadditivity of λmax. Uniform-modulus u gives equality: the six-vertex Johnson graph J(4,2) has degree four.

For the centered bound, write H=αI+C with α≥0, C Hermitian. Formula (1) for the additive compound gives `|K(C)|<=J_+†(|C|⊗I+I⊗|C|)J_+` entrywise: for a diagonal pair use `|c_ii+c_jj|<=|c_ii|+|c_jj|`. Hence `ρ(|K(C)|)<=2||C||F` and `ρ(|K(H)|)<=2α+2||H−αI||F`. Minimizing over α≥0 gives `α=t/4−sqrt(h²−t²/4)/(2sqrt3)>=0`, since H≥0 implies h≤t, and yields the final expression in (4). ∎

For normal A=diag(a_i), define

`t_i=Tr H_i=||B||F²+4|a_i|²`, `h_i=||H_i||F`, `L=||A||F²+||B||F²`.

By (1), `ρ(|H_i|)<=h_i`, and Lemma 3.1, the following basis-invariant condition is sufficient for **the actual optimized certificate**, without assuming B reducible:

`max_i min{3t_i/2,2h_i,t_i/2+sqrt3 sqrt(h_i²−t_i²/4)} <=2L`,
`max_(i<j)(h_i+h_j) <=2L`.                                           (5)

The upper bound is valid in **every** B-site basis; no common diagonalization is assumed. For direct computation let `b=||B||F²`, `p=Tr[(B†B)²]`, `u=Tr(B†B B)`, `v=Tr(B²)`. Expansion gives

`h_i²=p+4|a_i|²b+4|a_i|⁴+4 Re(bar a_i u)+2 Re(bar a_i² v)`.        (6)

**All equal eigenvalue moduli.** If A is normal with all `|a_i|=r`, then `||A||²=4r²`, every t_i=L, and `h_i<=t_i=L` since H_i≥0. Both inequalities in (5) hold for **every** traceless B. If the four a_i are distinct and L>0, the inequalities are strict: at most one H_i can have rank1, since two rank≤1 matrices `B+a_iI`, `B+a_jI` cannot differ by a nonzero scalar I of rank4. Thus every cross sum h_i+h_j is <2L, while every same-block term is ≤3L/2<2L. Consequently `η<2L` for this class and all B.

**A relative-open irreducible region.** At any nonzero normal traceless A with four distinct equal-modulus eigenvalues and B=0, (5) is strict. It remains strict for nearby A within the normal simple-spectrum stratum and nearby traceless B. Unitarily reducible matrices and unitarily bidiagonalizable matrices each form a proper closed nowhere-dense subset of traceless M4: for a k-dimensional reducing subspace the Grassmannian-plus-block parameter count is `30−2k(4−k)<30`; bidiagonal matrices plus U(4) use at most `16+12=28<30` real parameters. Closedness follows from compactness of projections/unitaries and Frobenius-bounded blocks, and the named smooth-image/Sard theorem gives empty interior. Thus this strict region contains unitarily irreducible B that are not unitarily bidiagonalizable, and can be chosen with B² nonnormal. This extends η≤2L beyond both the normal-pair class and the path/reducible classes, without claiming an open subset of all pairs in the ambient space (A is required normal).

## 4. Disclosed auxiliary diagnostics and exact unpaid step

**Branching tree diagnostic.** Linear-forest exactness cannot be extended to all trees by the same argument. For the auxiliary PSD family `H=tI_4+s Adj(K_{1,3})`, real s≠0 and `t>=sqrt3|s|`, the eigenvalues are `t+sqrt3|s|,t,t,t−sqrt3|s|`. Hence `λ1+λ2=2t+sqrt3|s|`. The six pair configurations form a cycle C6 after taking the modulus of the additive compound, so `ρ(|K(H)|)=2t+2|s|>λ1+λ2`. This is an exact symbolic auxiliary PSD-family diagnostic, not a selected physical C/q value or an η counterexample.

**A sufficient-test limitation.** For any rank-one P and nonzero scalar s, the normal pair `A=B=s(4P−I)` has η=40|s|²<2L=48|s|² by f274. In an A-eigenbasis, the block associated with a_i=3s has `t_i=48|s|²`, `h_i=8sqrt21|s|²`, so the same-block sufficient upper expression in (5) is `72|s|²>2L`. Thus (5) is not necessary; the exact path/bidiagonal theorem, or the fully optimized η, can succeed when this bound fails. Again this is an all-P symbolic dual-family check, not a physical q-value.

**Centering diagnostic.** For every rank-one P and nonzero scalar s, take `A=s(4P−I)`, B=0. In an A-eigenbasis the 3s block has `t=36|s|²`, `h=18|s|²`. The uncentered bounds `min{3t/2,2h}=36|s|²` exceed `2L=24|s|²`, while the centered bound is exactly `t/2=18|s|²`; all cross-block bounds also satisfy (5). This explains the use of the centered term. It is an all-P symbolic dual-family calculation, not a physical q-value.

**Unpaid step.** For arbitrary traceless B not satisfying a common H_i linear-forest condition, and normal A outside (5), the exact A-diagonal-basis quantity is the minimax over a **single** V of the maximum in (1). The four 4×4 PSD blocks generally do not commute and their entrywise Perron roots must be controlled simultaneously. We have neither a proof that this minimax is ≤2L nor a basis-independent lower bound >2L; even the latter would not refute η≤2L unless all local A-basis choices were covered. No selected physical q-value, unverified source theorem, finite counterexample search, or unreported diagnostic is used.

## 5. Provenance and exact scope

The normal-factor, path, PSD4 and Frobenius arguments above are source-independent written mathematics using f274's adopted compound definition and f168's qualified one-supported-site fact. No f198/f215 review body, held episode/consumer/guidance, false arbitrary-T norm estimate, source certificate or executable verifier is used. The parent f198/f215/f274 dispositions remain at their exact same-harness qualifications; no global T2/T3, certificate necessity, full one-normal result, global equality, novelty, parent/reviewer or formal/human/family/operational acceptance follows.
