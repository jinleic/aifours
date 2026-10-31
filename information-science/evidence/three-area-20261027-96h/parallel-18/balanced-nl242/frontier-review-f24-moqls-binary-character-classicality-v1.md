# f24 disjoint scientific review — binary-character pairs at order 8

Reviewer **InfoBalancedNL242-2-2**, separate info-6 owner; author PhysicsMOQLS8-2. Actual native review-start observation **2026-10-28T17:24:27-0700 PDT**; native `/bin/date` observed before this write **2026-10-28T17:27:40-0700 PDT**. Assignment was read before the candidate. No author contact, nested agent, external-model CLI or paid API was used.

## Verdict and exact limits

**NO_SUBSTANTIVE_DEFECT AT THE STATED SCOPE: 0 FATAL / 0 MAJOR / 0 MINOR.** The physical pair-product criterion, both nonlinear impossibility branches, three-bit complete-mapping lemma, pair/family conclusion, and reported finite counts are reconstructed below. In particular, any ordinary orthogonal pair in the specified binary-character subclass is memberwise classical, even with independent output bases/unitaries and cell phases; consequently every member of any such family of size ≥2 is classical.

This does **not** show arbitrary complex QLS or arbitrary four-families have this form, construct a nonclassical family, prove unrestricted order-8 four-family classicality, settle M(8), establish literature novelty, or constitute formal/kernel, human or independent-model acceptance. Main must make its own adoption decision.

## 1. Inputs and physical definition

- Assignment `review-waves/f24-moqls-binary-character-classicality/assignment-v1.json`, SHA-256 `7d45cfa2de780f5d9c1a2b7c9f7c4fe41cc8c86a33d988c0a1cacebdb822315f`, 22 LF, read first.
- Candidate `frontier-20261028-binary-character-pair-classicality-v1.md`, SHA-256 `6a8d3189460dfaa34738d1ee9eeaebd16d4e2d56e5170ce2858bc3206f78ab41`, 138 LF / 16,731 bytes, read completely in raw windows 1–46, 47–92 and 93–138 through its ending.
- Registered `physics-4-four-family-definitions-v1.md`, SHA-256 `ebfd79fe2fba3aab2d4b61b29688e66199718ff789a3a922c8bc2e38277bdfee`, 9 LF. Primary [Ball–Simoens, arXiv:2607.12933v2](https://arxiv.org/html/2607.12933v2), §§2.2–2.3 and §4 Definition 11/Lemmas 12–13, was read for the actual row/column, product-ONB, isotopy/classicality and related character construction. Retained HTML pin is `f2ef2a3f2493585ce22e022eca571f9c5e2268fd166f6599f3820afdf1b6d5ad`, 1,315 LF. Only those source passages, not the whole paper or latest-status literature, were reviewed.

A QLS has an ONB in each row and column; ordinary orthogonality requires its 64 SAME-cell product vectors to be an ONB. A member is classical if its entries are rays from one global ONB, up to phases/unitary; family isotopy permits a separate output unitary for each member. Thus independent output bases and phases in the candidate cannot alter any relevant Gram entry.

## 2. Full character caller and classicality

Let V=F₂³, χ_u(x)=(−1)^{<u,x>} for any nondegenerate bilinear pairing. The fixed-row inner products in the stated ψ^(f,g) are averages of χ_{j+j′}(g(x)); all nontrivial ones vanish iff the multiplicities of g are uniform, hence g is a permutation. Columns similarly require f a permutation. Conversely both permutations give both ONBs.

For each member, the output relabelling y=g(x) is unitary and yields the normalized form with F=f∘g⁻¹. Subtracting F(0) gives only a row-dependent phase. These are exact equivalences **inside this subclass**, not a WLOG reduction for arbitrary QLS. Independent output relabellings of the two physical factors do not change their product Gram matrix.

For normalized F,G, the 64×64 physical product matrix is a character matrix indexed by

    H(x,y)=(F(x)+G(y),x+y).

If H is a bijection its rows are exactly the 64 distinct characters of V²; if it is not, repeated coordinate labels give identical rows and the matrix cannot be unitary. For any h≠0, a collision at common second coordinate is exactly an intersection between `D_hF={F(x+h)+F(x):x∈V}` and `D_hG`; varying the common address makes both derivative base points arbitrary. Thus the original physical pair-product ONB is equivalent to disjoint derivative sets for **every** nonzero h, not just a necessary or scalar condition.

For one normalized F, additivity makes every entry a ray of the Fourier ONB. Conversely the i=0 row is that ONB. Classicality forces the entry at (i,0) to be a phase times one of its rays; comparison at y=0 fixes the phase to 1, and varying i shows every pairing with F(y) is linear in y. Nondegeneracy gives F(x+y)=F(x)+F(y). This also handles arbitrary per-cell phases and output unitaries by the preceding invariance.

## 3. Nonlinear cases and derivative-set incompatibility

Every coordinate of a permutation F:V→V has four ones. Its cubic multilinear coefficient is the parity of all eight values and is therefore zero; F(0)=0 leaves degree ≤2. Hence B_F(h,x)=F(h+x)+F(h)+F(x) is an alternating bilinear V-valued form and the derivative set is F(h)+B_F(h,V).

**Nonzero linear structure.** If B_F(h,V)=0 for some h≠0, simultaneous invertible changes of input and output coordinates for F and G preserve derivative disjointness. Taking h and F(h) to the third basis vector, the first two output coordinates induce a zero-fixing permutation on F₂², hence a linear permutation of its three nonzero points. Linear output changes/shears reduce the entire nonadditive case to `(u,v,w)↦(u,v,w+uv)`. For every input direction with nonzero first-two-coordinate projection, D_hF contains both output values with that projection. Any compatible G would make J(x)=πG(x)+πx take pairwise disjoint values on the four different π-fibres. Four nonempty images in a four-point set force each image to be a singleton. Thus G's first two coordinates are constant along the structural direction; G's derivative there is the same nonzero singleton as F's, contradiction. No selected F or G is assumed.

**No linear structure.** Write β_F:Λ²V→V for B_F. A nonzero scalar alternating form in three dimensions has nonzero radical, so absence of a linear structure rules out rank 1; the remaining ranks are 2 or 3. At rank 3, all seven nonzero h have |D_hF|=4. At rank 2 the kernel is a line in Λ²V; every nonzero bivector in this three-dimensional space is decomposable because the seven two-planes have seven different nonzero wedge generators. Exactly three h in the kernel's underlying plane have derivative-set size 2 and the other four have size 4. Thus each such nonlinear F has ≥4 size-4 derivative directions. Two such functions have a common direction among seven, and two 4-subsets of the seven nonzero outputs intersect. So two nonlinear functions cannot be compatible; together with the previous case, a compatible pair has at least one additive member.

## 4. Three-bit complete-mapping lemma and pair closure

Suppose K(0)=0 and both K and K+I are permutations. No nonzero point is fixed and no 2-cycle occurs; the seven nonzero points therefore form either one 7-cycle or a 3-cycle plus a 4-cycle. For each x≠0 form the F₂ projective line `{x,Kx,x+Kx}`. Each point appears once in each of the three roles, so the point/line incidence matrix B and line multiplicities m satisfy Bm=3·1=B1. The Fano incidence identity BBᵀ=2I+J makes B invertible over R; every line occurs exactly once.

A 3-cycle cannot be collinear, since consecutive edges would yield the same line. If its points a,b,c are independent, its K+I images are exactly the three nonzero vectors of the plane generated by a+b and b+c. The other four points form the 4-cycle; three lie in that plane and at least one cycle edge joins two of them, producing a repeated K+I image. Contradiction.

In the remaining 7-cycle, the first three consecutive points a,b,c are independent, or two consecutive edges yield the same line. For any three consecutive independent points x,y,z, the next unused point is x+y or x+z: y+z repeats the previous line, and x+y+z repeats the preceding K+I image. The two resulting possibilities force, respectively,

    a,b,c,a+b,b+c,a+b+c,a+c,
    a,b,c,a+c,a+b+c,a+b,b+c.

Each is the full orbit of the linear map determined on a,b,c by the first three transitions, so K is additive. This is a written universal proof, not merely the census below.

Now if one member is additive A, postcompose both maps by A⁻¹. Derivative disjointness says K+I is injective, hence bijective, for the other normalized permutation K. The lemma makes K additive as well. Conversely additive invertible A,B are compatible iff A+B is invertible. Every pair is therefore classical, and each member of an m-family with m≥2 belongs to a pair.

## 5. Independent exact finite checks and controls

A new reviewer C++ program imported **no author code**. It enumerated all 5,040 normalized permutations; for each, it directly computed all physical integer Gram-character sums and an independent derivative-set mask. For every one of the 12,698,280 unordered pairs, it compared the full physical-Gram nonzero-support criterion with derivative disjointness. Observed:

    linear normalized permutations: 168
    compatible pairs by nonlinear-member count: [4032,0,0]
    criterion mismatches across all pairs: 0
    compatible triples by nonlinear count: [16128,0,0,0]
    compatible four-families by nonlinear count: [6720,0,0,0,0]

For an actual four-clique, all 4,096 row/column Gram entries and 24,576 pair-product Gram entries were checked, with zero errors; the duplicate-square negative control had 448 product-Gram errors. The local program's observed runtime was 0.032965 s; its exact scope and encoding are in the receipt.

A separate reviewer Python program used `itertools.permutations`, direct derivative sets and the direct K+I permutation test. It found **48 linear and 0 nonlinear** normalized complete mappings. Independently counted derivative-size profiles were `(1,1,1,1,1,1,1):168`, `(1,2,2,2,2,2,2):1176`, `(2,2,2,4,4,4,4):2352`, `(4,4,4,4,4,4,4):1344`, agreeing with the candidate's exploratory census. These finite checks corroborate the written proof; they do not prove a theorem outside the subclass.

| Reviewer artifact (OWN root) | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-review-f24-physical-gram.cpp` | `6fc7b44ac9255dcab6829cf8af2b926fd3b77cd6ec007500f63273b720878c83` | 168 |
| Compiled `frontier-20261028-review-f24-physical-gram` | `fa14dd5675041ec81a17cdfd70f95c716cfdf664af3dded860d721f143a7407a` | — |
| `frontier-20261028-review-f24-physical-gram-result.json` | `234d0825489d4ec66183b87886ab4aeb02066f6869a811ca9d30c30c7108e3fc` | 12 |
| `frontier-20261028-review-f24-complete-maps.py` | `304315b3cccf0949659222de2b1737c39608d45c748d06c9346f1002b6bc4394` | 60 |
| `frontier-20261028-review-f24-complete-maps-result.json` | `b7cb8f420f3567b0e7eb1af93df19c59a3ae73bff7455f81e0ab91d4a072fc47` | 79 |

C++ was compiled/run with `/usr/bin/clang++ -std=c++17 -O3 -Wall -Wextra`; Python ran with `/opt/homebrew/bin/python3 -B`. Author C++/Python source, binary and receipts were hash-checked against the candidate, but their programs were neither imported nor used as independent evidence. Reviewer checks use two local implementations and the same F₂³ domain, not independent model-family review.

## 6. Provenance and original-target boundary

The public source's single-permutation character construction and memberwise classicality criterion are prior source content; the reviewed universal pair proof was reconstructed from the candidate. No claim is made that this pair statement is novel or exhaustive of published work. The original four-family problem allows all ordinary complex physical entries, including mixed classical/nonclassical members and all six same-cell product ONBs; the reviewed subclass is not an unrestricted reduction.

Reviewer previously performed a status-only documentary audit involving MOQLS/source-assurance wording and reported uncertainty about historical held-target exposure. The latest owner direction permits this disjoint reconstruction, but no blind/clean-cognition or prior-process-success claim follows. No historical quarantined result was taken as a premise. **END.**
