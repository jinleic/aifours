# Nonperturbative obstruction: all binary-character pairs at order 8 are classical

**PhysicsMOQLS8-2 / physics-4. WRITTEN AUTHOR CANDIDATE, independently corroborated by two bounded exact finite searches; not yet peer/parent reviewed, formalized or novelty-cleared.** This establishes an entire explicit subclass, not the unrestricted four-family order8 target.

## 1. Exact scope and result

Let V=F2^3 with ANY nondegenerate bilinear pairing `< , >` into F2. For maps f,g:V→V define unit vectors

    ψ^(f,g)_(i,j) = 8^(−1/2) Σ_(x∈V) (−1)^(<i,f(x)>+<j,g(x)>) |x>,
    i,j∈V.                                                        (1)

Each square may independently choose f,g, its output ONB, an output unitary, and arbitrary entry phases; all squares retain the SAME actual row/column labels i,j and SAME cell pairing. No shared physical output basis is assumed. By direct character orthogonality, (1) is a QLS exactly when f and g are permutations (§2).

**Theorem.** Any TWO ordinary mutually orthogonal QLS(8), each of the form (1) with its own permutations f,g and independent output unitary/cell phases, are BOTH classical. Consequently every ordinary m-family of this class for m≥2 is classical, in particular every four-family in this class.

This is an all-functions nonperturbative result for the specified character subclass. It does not assert that every QLS or MOQLS can be put in this form, nor exclude a nonclassical pair/four-family outside the class. It uses the original physical pair-product ONB, not a QOA or entangled-cell analogue.

## 2. Physical QLS and pair-product equivalences

For any f,g, distinct cells in a fixed row have inner product `(1/8)Σ_x (−1)^<j+j',g(x)>`. These all vanish for distinct j,j' iff the output multiplicities of g have vanishing nontrivial Fourier coefficients, i.e. g is a permutation. The column condition similarly says f is a permutation. Thus (1) is an actual QLS iff BOTH maps are permutations; no other hypothesis is implicit.

For each member separately, relabel its output basis by `y=g(x)`; this is a unitary because g is a permutation. Then (1) has the same projective entries as

    ψ^F_(i,j)=8^(−1/2) Σ_y (−1)^(<i,F(y)>+<j,y>) |y>,
    F=f∘g^(−1).                                                    (2)

Independent output relabellings are allowed by ordinary MOQLS isotopy and do not change any inner product or pair-product ONB. Normalize F(0)=0 by subtracting F(0); that only multiplies each cell in row i by one phase. Hence the problem reduces WITHOUT LOSS INSIDE THIS SUBCLASS to normalized permutations F:V→V,one for each square. This normalization is NOT a WLOG statement about arbitrary QLS.

For two normalized permutations F,G, the same-cell tensor products in (2) form an ONB iff

    H_(F,G)(x,y)=(F(x)+G(y), x+y) is a bijection V²→V².          (3)

Indeed the 64×64 product-vector matrix has entries `8^(-1)(−1)^(<i,F(x)+G(y)>+<j,x+y>)`: it is the Fourier character matrix of V² with coordinate rows indexed by H. If H is bijective it is a permutation of a unitary Fourier matrix. If H repeats a coordinate, two rows are identical, so it is not unitary. This proves both directions using the full ordinary product list.

For h≠0 write `D_h F={F(x+h)+F(x):x∈V}`. Condition (3) is equivalent to

    D_h F ∩ D_h G = empty,  for EVERY nonzero h∈V.              (4)

To see this, write z=x+y. The map x→F(x)+G(x+z) fails injectivity iff, for some h≠0 and x, `F(x+h)+F(x)=G(x+h+z)+G(x+z)`. As z ranges over V, the second base point is arbitrary. Thus every derivative-set intersection is exactly a collision of an actual coordinate map, and conversely. Since F,G are permutations, 0 belongs to no D_h.

If F is additive, it is invertible linear and (2) uses only the Fourier ONB rays: `<i,F(y)>=<F* i,y>`. Conversely, if (2) is classical, its i=0 row is a Fourier ONB, so for every i the vector at (i,0) is a phase times one first-row vector. Their y=0 coefficients are the same positive real number because F(0)=0; the phase is1. Therefore every `<i,F(y)>` is linear in y, and nondegeneracy makes F additive. Thus the statement that BOTH F,G are additive is exactly memberwise physical classicality for this class.

## 3. Every permutation of F2^3 has degree at most two

A Boolean function in three binary variables has a unique multilinear polynomial representation over F2: expand the indicators of its eight input points. The coefficient of the cubic monomial is the sum of its eight values mod2. Each output coordinate of a permutation F has four ones, hence cubic coefficient0. Thus every coordinate has degree≤2; for F(0)=0,

    B_F(h,x)=F(h+x)+F(h)+F(x)

is a V-valued alternating bilinear form, with a linear map `β_F: Λ²V→V` satisfying `B_F(h,x)=β_F(h∧x)`. The derivative set is the affine coset

    D_h F = F(h)+B_F(h,V),                                       (5)

of size1,2 or4. These are exact formulas for ALL permutations, not a selected truth table or an imported classification. F is additive iff β_F=0.

Call nonzero h a *linear structure* of F if B_F(h,V)=0. Since F is a permutation, `F(h)≠0` for h≠0.

## 4. A nonlinear permutation with a linear structure has NO compatible mate

Suppose F is nonadditive and has nonzero linear structure h. Let k=F(h)≠0. Applying the SAME invertible linear change of input variables and the SAME invertible linear transformation to both output functions F,G preserves (4). Choose them so h and k become `(0,0,1)`.

The identity `F(x+h)=F(x)+k` makes the first two output coordinates constant on the four input h-cosets. Since F is bijective, their induced map F2²→F2² is a permutation fixing0. Every such permutation is invertible linear: it permutes the three nonzero vectors, and the sum of any two is the third. Apply an invertible output transformation on those two coordinates. The third coordinate has the form `w+q(u,v)`, with q(0,0)=0. Every Boolean function q on two bits is `αu+βv+γuv`; remove the linear terms by an invertible output shear. Nonadditivity forces γ=1. Thus the universal normal form is

    F(u,v,w)=(u,v,w+uv).                                          (6)

This is a proved equivalence for the entire structural case, not an assumption about arbitrary MOQLS or a test on one permutation.

For h=(a,b,c) with `(a,b)≠(0,0)`, the third coordinate of `D_hF` takes both values as u,v vary, and its first two coordinates are fixed at (a,b). Thus

    D_hF = {(a,b,0),(a,b,1)}.                                    (7)

Suppose a permutation G obeys (4). For ANY input points x,y with different first-two-coordinate projections πx≠πy, equation (7) forbids `π(G(x)+G(y))=π(x+y)`. Hence the values

    J(x):=πG(x)+πx

for points from two DIFFERENT π-fibres are distinct. There are four nonempty fibres and only four possible J values. Their image sets are pairwise disjoint, so every fibre's image set is a singleton. Therefore πG(u,v,w) is independent of w.

For every x, the difference `G(x+(0,0,1))+G(x)` has zero first two coordinates; it is nonzero because G is a permutation, so it equals `(0,0,1)`. But D_hF is the same singleton at h=(0,0,1), contradicting (4). Thus **no compatible permutation G exists** whenever F is nonlinear and has a nonzero linear structure. All input/output changes above act on BOTH functions, preserving the physical collision criterion.

## 5. Two nonlinear permutations without linear structures cannot be compatible

Suppose F is nonlinear and has NO nonzero linear structure. For each nonzero h, the plane h∧V has dimension2. If rank β_F were1, B_F would be a nonzero scalar alternating form times one output vector; an alternating form on a three-space has nonzero radical. Explicitly choose u,v with B(u,v)≠0, and modify a third basis vector by suitable multiples of u,v to make it perpendicular to both. This contradicts the absence of linear structure. Hence rank β_F is2 or3.

- If rank3, β_F is injective and every h∧V has 2-dimensional image. All seven nonzero h give `|D_hF|=4`.
- If rank2, ker β_F is a line in the three-dimensional space Λ²V. Every nonzero bivector in Λ²V is decomposable: the seven two-dimensional subspaces of V have seven distinct nonzero wedge generators, exhausting Λ²V\{0}. Let the kernel generator be u∧v,with P=span(u,v). For exactly the three nonzero h∈P, h∧V contains ker β_F and has image dimension1; for the other FOUR nonzero h, its intersection with the kernel is0 and its image has dimension2. Therefore at least four h have `|D_hF|=4`.

If F,G are both nonlinear without linear structures, each has at least four such directions among the SAME seven. Their direction sets intersect. At a common h, D_hF and D_hG are four-element subsets of the SAME seven nonzero output values, so they cannot be disjoint. This violates (4).

Combined with §4, every compatible pair has at least ONE additive member. This uses no enumerated derivative-profile table and includes all ranks/linear-structure alternatives.

## 6. Elementary 3-bit complete-mapping lemma

**Lemma.** If K:V→V fixes0 and BOTH K and `K+I` are permutations, then K is additive linear.

Proof. On the seven nonzero points K has no fixed point: otherwise (K+I) would repeat its zero value at0. It has no 2-cycle, because the two cycle points would have the same (K+I) value. Thus its cycle type is either a 7-cycle or a 3-cycle plus a 4-cycle.

For each nonzero x, the three distinct points `{x,K(x),x+K(x)}` form a line of the binary projective plane. Every nonzero point occurs exactly once as x, once as K(x), and once as (K+I)(x). Let m_l be the multiplicity of each of the seven lines in this construction. The 7×7 point-line incidence matrix B satisfies `B B^T=2I+J` (three lines through a point, one through each distinct point pair), so B is invertible over R. Since `B m=3·1=B 1`, every line occurs exactly once. In particular consecutive cycle triples never lie on the same line.

A 3-cycle cannot be collinear, or two of its adjacent pairs would give the same line. If its points a,b,c are independent, the three already-used (K+I) images are the nonzero vectors of the plane `H={0,a+b,b+c,c+a}`. The other four domain points are `H\{0}` plus `a+b+c` outside H and form the 4-cycle. A 4-cycle on those four vertices has an edge joining two of the three H points; its endpoint sum lies in H\{0}, duplicating an already-used (K+I) image. Contradiction. Hence K has one 7-cycle.

Write its first three consecutive points a,b,c. They are linearly independent: otherwise c=a+b and the first two adjacent pairs yield the same line. For ANY three consecutive independent cycle points x,y,z, the next point must be either x+y or x+z. Indeed the four remaining nonzero vectors relative to that basis are x+y,x+z,y+z,x+y+z; choosing y+z repeats the line of (y,z), while choosing x+y+z repeats the (K+I) value x+y from the edge (x,y).

If the fourth point is a+b, the next two-choice rule, excluding already visited points, forces the remaining sequence

    a,b,c,a+b,b+c,a+b+c,a+c.

This is exactly the orbit of the linear map sending `a→b,b→c,c→a+b`.

If the fourth point is a+c, the next point cannot be b+c, because then its preceding edge has sum a+b, already the first edge's (K+I) value. It is therefore a+b+c; the two-choice rule and no-repeat then force

    a,b,c,a+c,a+b+c,a+b,b+c.

This is exactly the orbit of the linear map sending `a→b,b→c,c→a+c`. In each case the linear map agrees with K on all seven nonzero vectors and at0. The lemma follows. ∎

## 7. Complete pair proof and actual-family caller

Take any compatible normalized permutations F,G. By §§4–5 at least one is additive; suppose it is F=A, an invertible linear map. Postcompose BOTH maps with A^(−1), preserving (4). The first becomes I and the second becomes K=A^(−1)G. At h-level, (4) entails that K+I is a permutation: equality `(K+I)(x)=(K+I)(y)` for x≠y would give `D_(x+y)K` the value x+y,which is in `D_(x+y)I`. K itself is a permutation and fixes0. By §6, K is additive. Therefore G is additive as well.

Conversely, if F=A and G=B are invertible additive maps, `D_hF={Ah}` and `D_hG={Bh}`. Their pair is orthogonal iff `(A+B)h≠0` for every h≠0, i.e. A+B is invertible. This is the full pair classification within (1), with arbitrary constants handled by the per-cell phase normalization.

Thus every actual pair in this character subclass has two classical members, even if their originally written f,g and physical output frames differ. Any m-family with m≥2 has every member in some pair, hence every member classical. No selected numerical character function and no assumed family connectivity are used in the written proof.

## 8. Two independent bounded exact corroborations

These computations preceded the written proof and motivated the structural argument; they are not treated as the proof of an unrestricted theorem.

**C++ search:** `frontier-20261028-covariant-character-search-v1.cpp`, SHA256 **55b757caa3dcdd6736c7f9e2ea684ff3794464d182cac598bb38b9cb45d56a3b**; compiled binary SHA256 **ffa51fe21082ff629eaaf421e589498dd829fc6329b795145604cd8c2ec0641c**; receipt `frontier-20261028-covariant-character-search-receipt-v1.json`, SHA256 **439c45cb94f4d0b2c803ef04a83ec8803811b592f0762944c4ef2e9d63fcf8cb**. Executed `clang++ -std=c++17 -O3 -Wall -Wextra ... -o ... && ./... --output ...`, with one 45-second internal cap. It directly checks (3) by all translated coordinate-map values, enumerates all5040 normalized permutations/12,698,280 unordered pairs, and finds4032 compatible pairs,16,128 triples and6720 four-cliques, with ZERO four-cliques containing a nonlinear permutation. Search completed in0.040s as measured by the program. Its independent positive classical four-family FULL physical check has0 errors among4096 row/column and24576 pair-product Gram entries; duplicate-square negative control has448 pair-product Gram errors.

**Independent Python check:** `frontier-20261028-derivative-covariant-independent-v1.py`, SHA256 **92bbd82753ded198bbb8ff314ed94769a89bc71e80831bd9f537cd79894091b0**; receipt `frontier-20261028-derivative-covariant-independent-receipt-v1.json`, SHA256 **4159f69e3445f0ef78c3d4b1b68409a2d4075f9016e74cada2494c8ddc6a4c87**. It imports NO C++ code and tests (4) via derivative-value bitmask intersections, with Python set intersections for cliques. All12,698,280 pairs completed in3.02s. Compatible pair counts by 0,1,2 nonlinear members are **[4032,0,0]**; triple counts **[16128,0,0,0]**; four counts **[6720,0,0,0,0]**. The two implementations use independently formulated collision criteria but the same finite class/normalization; they are not independent model-family reviews or formal proof.

A separate exploratory in-kernel census found normalized derivative-size profiles/counts `(1,1,1,1,1,1,1):168`, `(1,2,2,2,2,2,2):1176`, `(2,2,2,4,4,4,4):2352`, `(4,4,4,4,4,4,4):1344`. The proof above DOES NOT rely on those counts; §§3–5 derive the structural alternatives directly. The exploratory cell is not an independent verifier of the whole result.

## 9. Scope versus the original target

This result rules out nonclassical families formed by the given binary-character construction, including independent input permutations f,g, memberwise output frames and cell phases. The classical seed check and repeated-square control validate only their stated finite inputs. General complex QLS entries need not have the constant-modulus character form (1), so this is **NOT** an unrestricted four-family no-go and does not narrow an arbitrary quantum family by an unproved WLOG conversion.

The independent source Ball–Simoens, *Large sets of mutually orthogonal quantum Latin squares*, arXiv:2607.12933v2, §4 Definition11 gives a related single-permutation character construction and §2.2–2.3 supplies the actual QLS/MOQLS definitions. I read the public primary page on this continuation. The double-permutation reduction and the all-pair obstruction above are proved here at the stated scope; no claim of historical novelty, source priority or exhaustion of other published constructions is made. The exact original unrestricted task remains: find an actual nonclassical ordinary four-family with all six full product ONBs, or prove an all-mixture classicality bridge without restricting its amplitudes/supports to (1).

All scientific computations above are local, bounded and explicitly reported. There is no human/configured-family/Lean/kernel certification or independent-model review, and no claimed finite nonclassical witness requiring a triple-check protocol. Earlier quarantined outcomes remain historical, not accepted premises.
