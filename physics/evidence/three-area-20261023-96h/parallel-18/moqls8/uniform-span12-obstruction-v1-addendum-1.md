# Uniform packet v1 — operative consolidated refinement: U3-6 is forced to a local real form

This is PartII of the SAME uniform-proof/obstruction packet, not a new problem or independent result count. Read after immutable `uniform-span12-obstruction-v1.md`, SHA256 `2b075f0d737b623904691e762b4fd2956a60e29c5371266d6bb7bed21e168601`. Its first unproved COMPLEX case is refined below by a new necessary theorem; its earlier reductions remain unchanged.

**AUTHOR-WRITTEN CANDIDATE. Uniform>=12 is STILL NOT PROVED.** No scientific program, arithmetic cell, enumeration, solver, Lean, tests, compilation, CLI or nested agent. All phases remain arbitrary until a real form is DERIVED. The four other squares are never assumed or proved real.

## 1. Full physical U3-6 setting

Assume exactly the full U3-6 case from v1 §10: Q_1,...,Q_5 are full physical MOQLS8; Q_1 has a globally isolated complex three-space A containing24actual cell vectors with a real Hermitian projector span S_A of dimension6; its complement is five fixed orthogonal rays. Every actual row/column contains an A-ONB triple. Every A-ray has multiplicity at most4 by v1 §11.

The claim proved here is:

> There is an orthonormal triple in A in which EVERY one of those24actual A-cell rays admits REAL coordinates after its own phase. Thus S_A becomes Sym(3,R). This is forced by the full physical equations, not a real-only ansatz.

The residual is named **U3R-6**: the SAME full physical family, with that derived real form for Q_1 only. No U3R-6 witness or exclusion is supplied.

## 2. Orthogonal-compression dimension at an ACTUAL ray

For an actual A-ray P=vv*, put B=A intersect v-perp, and

    S_B={H in S_A: H is supported on B}.

Since v occurs in an actual ONB line, its two line partners give two independent orthogonal rank-one projectors in S_B. Hence2<=dim_R S_B<=4.

### Dimension4 is impossible

If dim S_B=4, it is ALL Herm(B). Together with the actual P it supplies a five-dimensional block-diagonal subspace of S_A. The cross image from B to Cv therefore has real dimension1: zero would keep all of S_A within the five-dimensional block-diagonal algebra, and total dimension is6.

Every mixed cell across B/Cv has cross rank1 on this same real line, so both its physical factor rays are fixed. It lies in one two-space span(b,v), b in B. All other Q_1 cells are B-pure or B-perp (including the five fixed complement rays). If a B-pure actual ray outside{b,b-perp} occurs, ONE-CHANNEL gives a contradiction at8<12.

If no such actual ray occurs, the actual local generators lie in span{P_b,P_(b-perp),P_v,D_cross}, of dimension at most4. Mixed projectors have only P_b/P_v diagonal parts and the one-real-dimensional cross part. They cannot generate a six-dimensional S_A. This is the other contradiction. Thus dim S_B cannot be4.

### Some actual ray must have dimension3

Suppose instead every actual A-ray had dim S_B=2. For a chosen actual ONB triple{v,w,z}, the supported space at v is precisely span{P_w,P_z}. Its only rank-one rays are w,z. Thus every actual ray orthogonal to v is one of that SAME pair. The same applies to the other two rays.

The actual orthogonality classes are consequently disjoint ONB triples. Different classes have ALL cross overlaps nonzero. Each class occupies m actual rows and m actual columns, with m occurrences of each ray. Repeated rays force dimensions at least m in each other square; different classes give orthogonal spans; their row counts sum to8 and saturate all dimensions. Any two ray matchings of a class are ONBs of the same m-space. MATCH gives m>=6 for each class. At least two classes are needed because dim S_A=6>3. This would require at least12rows.

Therefore there exists an ACTUAL A-ray v for which

    dim_R S_B=3.                                          (1)

No cone point absent from the physical array was selected to obtain it.

## 3. The cross plane is exactly two-real-dimensional

Fix that actual v and B. Because P_v belongs to S_A, every block-diagonal member of S_A splits as a scalar multiple of P_v plus an element of S_B. Hence the kernel of the B/Cv cross map is exactly R P_v direct_sum S_B, of dimension4. Its real cross-image dimension is therefore6-4=2.

Write the image as

    { z v*: z in E },

where E is a real two-dimensional subspace of the complex two-space B. Actual mixed cell vectors can be independently phased as

    q=z+gamma v,       gamma>0 real, z in E, z!=0,

because their cross image is gamma z v*, and division by the positive real gamma preserves E.

If E has complex dimension1, both physical factor rays are fixed, giving the one-channel geometry with arbitrary relative phases. If there is an actual B-pure ray outside its pair beta, ONE-CHANNEL excludes it. Otherwise all pure B-generators use only beta, mixed projectors lie in Herm(span(b,v)) and S_A has dimension at most2+1+2=5. This contradicts6. Thus

    dim_C span_C E=2.                                     (2)

## 4. Its imaginary-inner-product form must vanish

On E let omega(z,w)=Im<z,w>, a real alternating form. If it is nonzero, it is nondegenerate on the real2-plane. Two orthogonal mixed vectors have omega(z,w)=0, so their B factors are real-dependent.

Every actual mixed row/column has at least two mixed cells to cancel its nonzero cross-block sum. Their orthogonality forces one B-factor real line, hence one two-space F_j=span(b_j,v), and at most two vectors. They are exactly two, forming an ONB of F_j. Distinct real lines in E have nonzero imaginary inner product, so their B-ray-pairs beta_j={b_j,b_j-perp} are distinct and their channel rows cannot overlap.

Let k_j count channel-j rows/columns and m_alpha count nonmixed pure-B pair rows. Then

    8=sum_j k_j+sum_alpha m_alpha.

Pure-B class beta_j has m_beta_j copies of b_j and m_beta_j+k_j copies of b_j-perp. Other classes have m_alpha copies of each ray. In each OTHER square, different pure-B pairs give orthogonal spans and those repeated-ray lower bounds sum to8. All bounds saturate.

Channel-j entries of each other square then lie in its k_j-space after removing the m_beta_j pure-b_j span. Its F_j orthonormal-pair classes again have row sizes summing to k_j and saturate this space. MATCH gives k_j>=6 for every nonempty channel. There are at least two channels because the ACTUAL cross images span E of complex dimension2. Their disjoint row sets contradict8.

Thus omega is identically zero. The Hermitian inner product on E is real-valued; real Gram–Schmidt gives a real basis e,f in E that is orthonormal over C. Every mixed actual ray is therefore REAL, up to its allowed phase, in the local orthonormal triple(v,e,f).

This establishes reality only for the mixed rays at this stage. Pure-B rays have not been silently assumed real.

## 5. A nonreal pure-B ray contradicts the repeated-v basis

Suppose an ACTUAL B-pure ray w is not phase-real in E. Then it overlaps EVERY nonzero z in E. Indeed if w were orthogonal to a nonzero real z in the real orthonormal plane E, its unique complex orthogonal ray in B would be the real perpendicular direction, making w phase-real after all.

Consequently w has nonzero overlap with EVERY actual mixed Q_1 ray. Product orthogonality forces Q_s(w) to be orthogonal to all mixed entries of Q_s, for each s=2,...,5.

Let m be the actual multiplicity of ray v, and K_s the m-dimensional span of Q_s entries at those occurrences. Weighted product-ONB completeness at v, proved in v1 §4, gives

    sum_(mixed cells x) |<v,Q_1(x)>|^2 P_(s,x)=P_(K_s-perp). (3)

The weights are positive exactly at the mixed A-cells; B-pure cells and the five complement rays have zero overlap, and the v-occurrences give P_(K_s). A sum of positive rank-one operators resolves the displayed projection, so the mixed entries span ALL of K_s-perp, not merely a projected subspace.

Thus Q_s(w) lies in K_s. Since w overlaps every mixed ray, its actual row and column contain NO mixed A-vectors. Each is an A-ONB consisting of w, its B-orthogonal partner, and a v-ray. Let p_row and p_col be these two v-occurrence cells. They are different: a cell sharing both w's row and column would be w itself, not a v-cell.

In each other square, the v-occurrences form an ONB of K_s. The transition row from the UNIT vector Q_s(w) in K_s has zeros at p_row and p_col and is nonempty. The FOUR other-square supports are disjoint by the physical tensor equations. Therefore

    4<=m-2,       m>=6.

But v is an actual A-ray in U3-6, whose multiplicity is at most4. Contradiction. There is NO actual nonreal pure-B ray.

All actual A-rays are now phase-real in(v,e,f): v itself, every mixed ray from §4 and every B-pure ray from this argument. Their projectors lie in Sym(3,R); their real span has dimension6, exactly the dimension of that real-symmetric space. Hence S_A=Sym(3,R) in this derived basis. This proves the claimed real-form reduction.

## 6. Exact first unproved case after the refinement

The remaining case is **U3R-6**:

- a full physical five-MOQLS8 family, with ALL64cells/ONBs/product equations retained;
- one selected member has24sectorcells in a globally isolated three-space and five fixed orthogonal complement rays;
- that member's sector rays are real after a PROVED unitary/entry-phase normalization and span Sym(3,R);
- each sector ray has multiplicity at most4, and the weighted-overlap and orthogonality constraints in v1 §11 remain necessary;
- the other four squares remain fully arbitrary COMPLEX arrays, with no fixed classical member or support restriction;
- no sector-cell board, finite palette or continuous angle is dropped.

A real orthogonal assignment on the sector's cubic bipartite incidence graph alone is NOT a physical counterexample: it omits the four mate squares and their complete tensor-product constraints. Conversely choosing a three-edge-coloring of that board only proves a classical assignment EXISTS, not that every given complex/real assignment is classical or has the required mates. No such substitution is made.

U3R-6 is neither excluded nor constructed here. Uniform a_s>=12 is still OPEN. If a later proof excludes it after this consolidated reduction is validated, the14budget would remove K4/K5 without T16/F14/native imports; old K12/K3 would remain explicit for full classicality. The original mixed assembly, old A10/A11/threeUNKNOWNs and runtime HOLD statuses are unchanged.

This supplement and v1 form ONE uniform proof/obstruction packet. The compression, isotropy and weighted-span steps here are new AUTHOR CANDIDATES requiring actual reconstruction, not independent discoveries, formal checks, or a prior-art-cleared reality theorem.
