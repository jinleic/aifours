# Any order-8 four-MOQLS containing a binary-character square has that square classical

**PhysicsMOQLS8-2 / physics-4. WRITTEN AUTHOR CANDIDATE with two exact finite corroborations; pending disjoint review, parent reading, novelty and formal checks.** This is a nonperturbative, all-mixture result for ONE specified member class. It is not an unrestricted four-family proof.

## 1. Original-object theorem and scope

Take V=F2^3, dot pairing, and ANY permutations f,g:V→V. A *binary-character square* is an ordinary 8×8 QLS whose entries, up to arbitrary cell phases and one member-specific output unitary, are

    ψ_(i,j)=1/sqrt(8) Σ_(x∈V) (−1)^(i·f(x)+j·g(x)) |x>,  i,j∈V.    (1)

The coordinate basis |x> may be any ONB; the other members of an ordinary MOQLS family may be completely arbitrary complex QLS and need NOT have this form.

**Theorem A.** If an ACTUAL four-MOQLS(8) family contains a member of the form (1), that member is classical. The other three members are arbitrary and may be classical or quantum.

**Stronger rank-one case.** If the normalized permutation F=f∘g^(−1),after removing its constant,has polar rank1 (defined below),its square cannot have TWO mutually orthogonal ordinary QLS mates at all. In particular it cannot occur in a three- or four-family.

**Classical-mate theorem.** For ANY nonadditive permutation F:V→V,the square (1) has no classical ordinary QLS mate. This is stronger than merely excluding a mate from the character subclass;its proof allows an arbitrary classical Latin mate.

Thus every nonclassical member of any putative ordinary four-family must lie outside (1). If any member is a nonclassical character square,all possible mixtures of its three arbitrary companions are excluded. This does not rule out four-families containing a classical character square plus nonclassical non-character members,or four nonclassical members none of which has form (1).

## 2. Normalization, physical caller and polar rank

A permutation g gives an output-basis relabel y=g(x),and produces the common-coordinate square

    ψ^F_(i,j)=1/sqrt(8) Σ_y (−1)^(i·F(y)+j·y)|y>,   F=f∘g^(−1).    (2)

This is a member-specific output unitary,so all ordinary row/column and pair-product ONBs are preserved. Replacing F by F+F(0) changes only entry phases;assume F(0)=0. Distinct rows/columns are orthogonal by character cancellation and F's bijectivity,so (2) is an ACTUAL QLS. Conversely each f,g in (1) must be a permutation for its row/column ONBs,as proved in `frontier-20261028-binary-character-pair-classicality-v1.md`, SHA256 **6a8d3189460dfaa34738d1ee9eeaebd16d4e2d56e5170ce2858bc3206f78ab41**;this previous candidate is used only for this elementary characterization,which also follows by Fourier inversion of output multiplicities.

Each output coordinate of the permutation F is balanced. The coefficient of the cubic monomial in its unique multilinear Boolean polynomial equals the sum of all eight values mod2,so is zero. Thus F is quadratic or less. With F(0)=0 define

    B_F(x,y)=F(x+y)+F(x)+F(y),   β_F:Λ²V→V, β_F(x∧y)=B_F(x,y).

This is alternating bilinear;write r=rank β_F∈{0,1,2,3}. F is additive iff r=0. If F is additive, (2)'s entries are rays in its first Fourier row,so the square is classical. Conversely classicality of (2) forces every scalar x→i·F(x) to be a linear character because the first row is a Fourier ONB and the x=0 coordinate fixes every phase;therefore F is additive. Hence the theorem reduces to excluding r=1,2,3.

## 3. Exact Walsh zero planes for ALL nonlinear components

For every row-frequency u and Fourier-coordinate v put

    W(u,v)=Σ_x (−1)^(u·F(x)+v·x).

For nonzero u, q_u(x)=u·F(x) is balanced because F is a permutation. Its polar `b_u(x,y)=u·B_F(x,y)` is either zero or a nonzero alternating form on a 3-space. The latter has rank2 and a unique nonzero radical vector t_u.

There is one LINEAR map `J:V→V`,of rank r,whose kernel is exactly the set of u with b_u=0 and whose value for each other u is t_u. In a fixed basis take

    J(u)=(b_u(e2,e3), b_u(e3,e1), b_u(e1,e2)).

The matrix of a 3D alternating form multiplied by this vector is zero;the displayed coordinate correspondence is a linear isomorphism from the three form coefficients to V. Thus rank J=rank β_F.

For u outside ker J, compute the square of the actual Walsh sum. Changing y to x+h and summing first over x gives

    W(u,v)^2 = 8 Σ_(h in rad b_u) (−1)^(q_u(h)+v·h)
             = 8[1+(−1)^(q_u(t_u)+v·t_u)].                  (3)

Nonradical h contribute zero by cancellation of a nontrivial linear character. Since q_u is balanced,W(u,0)=0; (3) forces q_u(t_u)=1. Consequently

    W(u,v)=0 iff v·J(u)=0,   and otherwise |W(u,v)|=4.             (4)

For nonzero u in ker J,q_u is a nonzero linear character,so W(u,v)=8 at its UNIQUE nonzero character label b_u and0 elsewhere. All phases/signs and zero-frequency cases are retained. Equation (3) is derived from the actual eight terms;no separate bent-function or rank-classification source is imported.

## 4. No classical mate: exact transversal and all three ranks

Suppose a classical QLS B is an ordinary orthogonal mate of ψ^F. Fix ANY one of B's basis rays. It occurs once in every row and every column. Because the B vectors at those eight cells are parallel, the pair-product ONB forces the eight ψ^F entries there to be mutually orthogonal. Thus these cells form a graph `(a,π(a))` of a permutation π:V→V. Replacing π by π+π(0) leaves all differences unchanged,so assume π(0)=0. Orthogonality is EXACTLY

    W(a+b, π(a)+π(b))=0  for all distinct a,b.                  (5)

This is a necessary actual-transversal condition for EVERY classical mate;we do not assume every abstract π extends to a classical square.

### Rank r=1

ker J is a 2-space K and im J={0,t}. If a+b lies outside K, (4) and (5) give `(π(a)+π(b))·t=0`. Any two points from distinct K-cosets therefore have the SAME value of `π(a)·t`. There are exactly two cosets,so this scalar is constant throughout V. But π is a permutation and t≠0,so the scalar takes each value four times. Contradiction.

### Rank r=2

Let ker J={0,k} and let B be the unique nonzero vector annihilating the 2-space im J under the dot pairing. For arbitrary a and any h outside ker J,apply (4)–(5) to pairs `(a,a+h)` and `(a+k,a+h)`. Their differences h and h+k have the SAME nonzero J image. Adding the two equations gives

    (π(a)+π(a+k))·J(h)=0.

As h ranges outside the kernel,J(h) ranges over all nonzero elements of im J. Since π is injective, `π(a)+π(a+k)` is nonzero and must equal B,for EVERY a.

The component q_k is a nonzero linear character, `q_k(x)=b_k·x` for a nonzero b_k. For every u outside ker J,both u and u+k are outside it,have the SAME radical J(u),and §3 gives `q_u(Ju)=q_(u+k)(Ju)=1`. Therefore `q_k(Ju)=0` for all such u;thus b_k annihilates im J and b_k=B. Its linear Walsh row has `W(k,B)=8`. But every pair `(a,a+k)` on the transversal has column difference B,contradicting (5).

### Rank r=3

J is invertible. Equation (5) with b=0 gives `π(a)·J(a)=0` for every a. Expanding (5) for any a,b then gives

    π(a)·J(b)=π(b)·J(a).                                        (6)

The equation is also trivial for a=b and for zero arguments. For arbitrary a,c,b,apply (6) twice:

    π(a+c)·J(b)=π(b)·J(a+c)
               =π(a)·J(b)+π(c)·J(b).

Since J is onto,π(a+c)=π(a)+π(c);π is an invertible linear map. Equation (6) and the diagonal zeros make `B(a,b)=π(a)·J(b)` an alternating bilinear form. It is nondegenerate because BOTH π,J are invertible. But a 3-dimensional alternating form has nonzero radical (choose a nonzero paired u,v and adjust a third basis vector to be perpendicular to both;the zero-form case is even more degenerate). Contradiction.

All r>0 cases fail;therefore ANY nonclassical binary-character square has no actual classical mate. No classical Latin completion theorem,enumeration or prior accepted k1 result is used.

## 5. Polar ranks2/3: arbitrary three mates become classical

Suppose ψ^F has r≥2 and occurs in an ACTUAL four-family with three arbitrary complex QLS mates B,C,D. Independently apply a global output unitary to EACH member so its first row is the standard labelled basis `{e_j}`. This preserves the SAME grid and every actual pair-product ONB.

For each cell (i,j) with i≠0,column orthogonality to the first-row cell (0,j) excludes coordinate j in all four members. For any coordinate k,orthogonality of each pair of members' actual product vectors at cells (i,j) and (0,k) says their kth coordinates cannot both be nonzero. Therefore the FOUR support sets at each nonfirst-row cell are pairwise disjoint subsets of the other seven coordinates.

For selected ψ^F the coefficient in first-row Fourier coordinate k is `W(i,j+k)/8`. By §3,exactly `8−2^(3−r)` row labels i have nonlinear components; every entry in each such row has support exactly4. This number is6 when r=2 and7 when r=3. In any such cell,only THREE of the seven available coordinates remain for the three mates. Each mate vector is nonzero,so each has support exactly ONE. Thus B,C,D each have at least six ENTIRE nonfirst rows of coordinate rays,plus the standard first row: at least seven coordinate-only rows.

If only one row remains,each column already contains seven mutually orthogonal coordinate rays from those seven rows. Its final unit vector,orthogonal to all seven,must be the missing coordinate ray. Hence every mate is classical. But §4 says a nonclassical ψ^F has NO classical mate. Contradiction. This is an actual common-frame and all-three-mates proof,not a generic scalar support budget or a premise that the mates were initially classical.

## 6. Polar rank1: the actual 4+4 block forces NO two mates

Let r=1. Choose nonzero k spanning im β_F and a scalar Boolean quadratic q with polar spanning that image. Then

    F(x)=Lx+k q(x)

for an additive linear L;q has nonzero alternating polar on V. Let `K={i:i·k=0}`,a 2-space of FOUR row labels. In the Fourier basis of row0:

- Every row i∈K consists of the SAME eight Fourier basis rays E (permuted and phased).
- Every row i∉K consists of the SAME eight rays F' obtained from E by the diagonal unitary `diag((-1)^q)`.

Each of the16 rays occurs exactly once in each of four corresponding rows,so multiplicity4. The cross overlaps of E and F' are Walsh coefficients of q divided by8. Its nonzero polar has a unique nonzero radical t. The same square-sum argument as §3,without requiring q balanced,shows its transform is nonzero on ONE affine plane of four labels,with magnitude4 there. Therefore the cross-overlap graph of E versus F' is exactly TWO disjoint complete `K_(4,4)` components,with every cross overlap in a component of magnitude1/2. E and F' have no common ray. Denote the two selected-square blocks by b=0,1;each block contains four E rays and four F' rays.

Now let B be ANY actual orthogonal QLS mate. For each selected-square ray v,its four occurrences are at distinct cells and the corresponding four B vectors are orthonormal,because the selected ray overlaps itself. Let X_B(v) be their 4-dimensional span.

Within one K4,4 component,every E ray overlaps every F' ray nontrivially. Therefore their B-spans are perpendicular. Since both have dimension4 in C8,each E-span is the orthogonal complement of each F'-span. All four E-spans in block0 are the SAME subspace X_B,and all four F'-spans there equal X_B^perp. Define X'_B analogously for E block1.

In ANY E-type row of the selected square,its entries are the eight E rays,with four from each block. The corresponding eight B entries form one actual B-row ONB. Four lie in X_B and four in X'_B;these two 4-dimensional subspaces must be perpendicular,so X'_B=X_B^perp. Hence in EVERY cell,using selected-square row type `a=0` for E and `a=1` for F',B's vector lies in

    X_B              if a+b=0 mod2,
    X_B^perp         if a+b=1 mod2.                              (7)

The same conclusion holds independently for ANY second mate C,with its own 4-space X_C. Every selected-square row contains four rays in each block,so there are exactly32 cells with a+b=0. At ALL of them,`B_(i,j)⊗C_(i,j)` lies in `X_B⊗X_C`,whose dimension is16. If B,C were orthogonal ordinary QLS,these32 unit product vectors would have to be mutually orthogonal. This is impossible in dimension16.

Thus a nonclassical rank-one binary-character square cannot appear with TWO mutually orthogonal mates. The argument uses actual repeated-cell multiplicities,actual ONB rows and actual product-space dimension;no scalar overlap matrix is assumed liftable, no fixed selected-unitary pattern is WLOG for arbitrary squares,and no abstract projected subspace is substituted for B or C.

## 7. Final all-mixture implication

If a character square in an actual four-family is nonclassical,its polar rank is1,2 or3. Rank1 contradicts §6 already with any two of its three mates. Ranks2/3 contradict §5 with all three mates. Therefore every character-form member of every ACTUAL ordinary four-MOQLS(8) family is classical,regardless of how many of its other members are nonclassical. This completes Theorem A at the stated character-form scope.

This is materially stronger than merely showing two character-form squares cannot form a nonclassical pair: it constrains ONE selected member against THREE completely arbitrary physical companions. It is still not a universal four-family theorem,as arbitrary QLS entries need not have the character representation (1).

## 8. Executed exact corroborations, NOT the universal proof

### Full normalized character-transversal census

`frontier-20261028-character-transversal-census-v1.cpp` SHA256 **64ad9915adba7e0f219dad70adfc87d0d49867cde83757a8e3056540ef56231f**;compiled binary SHA256 **b4ffde90f249f3f9a7d24e411887170e3cf6216a2c7ab7ecaba0273bdd584e1e**;receipt `frontier-20261028-character-transversal-census-receipt-v1.json` SHA256 **854cc626cadc0c607d6644967a266e7bdb99b2ae1b03bc4ffb020c3f7361520d**. One bounded local `clang++ -std=c++17 -O3 -Wall -Wextra` compile/run,45-second internal cap;actual program time0.042s.

The complete census enumerated all5040 normalized F and all5040 normalized π for each,checking Walsh-zero orthogonality at every pair of rows. By polar rank0/1/2/3, F counts were `[168,1176,2352,1344]`;tested normalized transversals `[846720,5927040,11854080,6773760]`;passing `[8064,0,0,0]`. Each rank0 F had48;each nonlinear F had0. All per-F Walsh row/column and spectrum checks passed. A genuine classical transversal control passed;the identity-transversal negative control was rejected. This exact census supports §4 but does NOT enumerate arbitrary quantum mates or prove Theorem A by itself.

### Independent actual rank-one ray/ONB check

`frontier-20261028-rank1-character-structure-check-v1.py` SHA256 **6e5242bd8ad669070e653d1486d76e2375ab54c27b732c09521be3108facdd41**;receipt `frontier-20261028-rank1-character-structure-receipt-v1.json` SHA256 **be152d5fe051c45ce4a9346230c98b4722ffbcf340703ec8eda60aabe7fc9ed8**. Ran once with Python standard-library integer arithmetic,0.830s;imports NO C++ search code.

For ALL1176 normalized rank1 F,it checked all1024 actual row/column Gram entries per square;the direct64 sign vectors have exactly16 rays,each multiplicity4,with four E-type and four F'-type rows. The actual nonzero cross-ray graph has degree4 and two8-vertex components,necessarily two K4,4's. It rejected both identity/rank0 and nonpermutation controls for their intended reasons. This checks the finite square structures underlying §6;it neither constructs arbitrary mates nor independently certifies the dimension argument.

Two earlier character-pair implementations directly checked all12,698,280 normalized pairs by translated-map collisions and independently by derivative-mask intersections,with4032 compatible pairs and zero involving nonlinear F;they are described and pinned in the predecessor. A separate in-kernel exploratory selection saw zero normalized transversals for one representative of each of the three nonlinear profiles BEFORE the full census. Those exploratory examples are not universal evidence.

## 9. Remaining original gap and assurance

Both §4's all-rank transversal proof and §5–§6's SAME-cell arbitrary-mate arguments are ordinary written mathematics awaiting full disjoint review. The two finite experiments check only the explicitly stated character squares/transversals and rank-one ray structure. No nonclassical four-family witness, arbitrary-Q no-go, numerical M(8), formal/kernel proof, independent-model/human review or novelty/priority claim follows.

An arbitrary ordinary QLS need not be an isotopic binary-character square. The genuine remaining original task is to handle all higher-component complex QLS outside (1),or find one actual nonclassical four-family and independently check every row,column and all six pair-product ONBs. The earlier generic local-gap theorem remains a separate candidate;none of these arguments assumes a continuous path from a classical net. Historical quarantined outcomes are not mathematical premises and are not retrospectively accepted.
