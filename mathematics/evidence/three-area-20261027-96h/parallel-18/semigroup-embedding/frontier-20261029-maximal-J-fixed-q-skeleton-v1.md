# A normal-band skeleton over the specified actor, injective on maximal J-classes

**NEW AUTHOR WRITTEN lemma with exact finite controls; UNREVIEWED / UNADOPTED.** This is a direct fixed-q construction. It does not invoke or repair the canonical-host/Q1 equivalence rejected at f164, does not use Fact1, and does not separate the lower ideal. Original Q1/Q2 remain OPEN; no novelty or formal verification is asserted.

## 1. Statement

Let S be a **finite regular** semigroup, and let q:S→D=M[G;I,Λ;P] be an onto idempotent-pure homomorphism. There is a normal band B with G acting by automorphisms and a map β:S→B satisfying

`β(st)=β(s) · ^(g_s p_(λ_s,i_t))β(t)`

such that β is injective on the union of S's maximal J-classes. Every nonmaximal J-class is sent to zero. In particular every same-q R-related idempotent pair in a maximal J-class is separated.

The associated physical product is exactly B×D with

`(b,(i,g,λ))(c,(j,h,μ))=(b · ^(g p_(λ,j))c,(i,g p_(λ,j)h,μ))`.

Thus the coefficient equation supplies a homomorphism s↦(β(s),q(s)) over this same specified q. It is not claimed injective on all of S. No local-regularity assumption on S is needed for this layer result.

## 2. Coordinates and the purity-controlled zero pattern

Named ordinary import: for a finite regular semigroup, a J-class has completely 0-simple principal factor (with an optional formal zero if its products never leave the class), hence Rees coordinates T^0=M^0[H;J,L;Q]. For each maximal J-class T choose a nonzero base cell (ℓ0,i0), normalize Q_(ℓ0,i0)=1, and put

`a_i=(i,1,ℓ0)`, `b_ℓ=(i0,1,ℓ)`, `h_0=(i0,h,ℓ0)`.

These satisfy `(i,h,ℓ)=a_i h_0 b_ℓ`, all displayed intermediate products staying in T. Homomorphism q has D-row ι(i) on T-row i and D-column κ(ℓ) on T-column ℓ. Set

`p0=p_(κ(ℓ0),ι(i0))`,

`u_i=g_(a_i)`, `v_ℓ=p0 g_(b_ℓ)`, `φ(h)=p0 g_(h_0)`.

The restriction to the base maximal subgroup shows φ:H→G is an injective group homomorphism: if its image is 1, purity makes h_0 an idempotent, hence the subgroup identity. Write N=φ(H), a subgroup, **not assumed normal**. The source factorization gives

`g_(i,h,ℓ)=u_i φ(h) v_ℓ`.                                      (1)

For each junction (ℓ,j), set `r_(ℓ,j)=v_ℓ p_(κ(ℓ),ι(j)) u_j`. Then

`Q_(ℓ,j)≠0  ⇔  r_(ℓ,j)∈N`.                                  (2)

*Proof.* If Q is nonzero, b_ℓ a_j is the base-group element Q_(ℓ,j), so r_(ℓ,j)=φ(Q_(ℓ,j))∈N. Conversely, if Q_(ℓ,j)=0 and r∈N, choose h∈H with φ(h)=r^(-1). Then t=(j,h,ℓ) has

`g_t=u_j r^(-1) v_ℓ=p_(κ(ℓ),ι(j))^(-1)`,

so q(t) is idempotent. But t² leaves T because its junction is zero; hence t is not idempotent, contradicting purity. This proves (2). □

## 3. The band of coset-labelled rectangles

Use left cosets G/N. For each γ∈G/N set

`R_γ={(a,i)∈G×J : a u_i N=γ}`,

`C_γ={(b,ℓ)∈G×L : b v_ℓ^(-1) N=γ}`.

Take the disjoint union of the rectangular bands R_γ×C_γ, for all cosets and all maximal J-classes T (retain a T-tag), and adjoin a common zero 0. Within one tagged rectangle multiply by taking the left row and right column; between distinct rectangles return 0. Call the band B.

Associativity and idempotence follow directly from these rules. It is normal: xyzx=xzyx=x if x,y,z lie in one rectangle, and both products are 0 otherwise; zero cases are immediate. Equivalently every nonzero local monoid is {x,0}, a two-element semilattice. Therefore B is also RIGHTSN.

G acts by left multiplication on a,b and on γ, preserving tags and fixing 0. This is a band-automorphism action; normality of N was not used.

For t=(i,h,ℓ) in a maximal class T put

`β(t)=(((1,i),(g_t,ℓ)))` in its tagged rectangle,

and put β(s)=0 on all nonmaximal J-classes. Equation (1) ensures the row coset u_iN equals the column coset g_t v_ℓ^(-1)N, so β(t) is an allowed band element.

## 4. Checking every product

The nonmaximal elements form an ideal: multiplication can only decrease J-order. Also a product of elements in two different maximal J-classes lies below both, hence is nonmaximal. In these cases both sides of the coefficient equation are zero.

For s=(i,h,ℓ) and t=(j,k,m) in the same maximal class T, put w=g_s p_(κ(ℓ),ι(j)). The two band factors have component cosets

`u_i N`, `w u_j N=u_i φ(h) r_(ℓ,j) N`.

They agree if and only if r_(ℓ,j)∈N, equivalently Q_(ℓ,j)≠0 by (2).

- If Q=0, st is nonmaximal and both coefficient sides are 0.
- If Q≠0, the rectangle product has row (1,i) and column (w g_t,m), exactly β(st), since g_(st)=w g_t and T-products retain the first row and last column.

These exhaust S², proving the stated equation. The T-tag, row i, column ℓ and label g_t determine t uniquely by (1) and injectivity of φ. Thus β is injective on the maximal classes, including between different classes. □

If G is finite, a maximal class T contributes |G|·|T| band elements: each coset rectangle has |N||J| rows and |N||L| columns, and there are |G|/|N| cosets. B has cardinality `1+|G|·sum_T |T|`.

## 5. Boundary relevant to the same-fibre bridge

This handles maximal layers even when their products fall into the ideal, unlike the closed-CS-top completion. It does **not** split the zero into different lower-ideal columns. For an R-pair in a nonmaximal class J, applying the same construction to the ideal generated by J only gives a host for that ideal; extension of its coefficient map to the rest of S is not automatic. That is precisely where row-dependent column actions and their globalization remain needed.

For S45 the skeleton has two 3×3 rectangles and a zero (19 elements); all nine relevant lower R-pairs collapse to zero. The known 306-element RIGHTSN host resolves that zero into its lower rectangular layer. This lemma explains the upper skeleton, not that resolution.

## 6. Exact controls

`frontier-20261029-maximal-J-fixed-q-skeleton-checker-v1.py`, SHA 3172d1ff6cdb999c6063e8546d73b789688b4fae82c2085742921c5050e69f9b, ran with python3.14 starting Thu Oct 29 09:35:21 PDT 2026, exit 0. All arithmetic is integer table work.

|Source|Maximal class sizes|Base-group sizes|Normal-band size|Maximal same-fibre R-pairs separated|Lower R-pairs collapsed|
|---|---|---|---:|---:|---:|
|56-element closed-CS-top source|8|2|17|2|28|
|S45, nonclosed top|9|1|19|0|9|
|12-element source with two incomparable maximal classes|4,4|2,2|17|2|1|

For each source the checker reconstructs the maximal J-classes and coordinate factorizations, verifies the subgroup image and the exact zero/coset criterion, then checks all final band associativity and normal identities, the C2 action, every source-host equation and the claimed R-pair separation. A purity-negative control forgets S45's C2 label: it remains a homomorphism, but three top nonidempotents now map to idempotents and all three zero cells are wrongly predicted nonzero by subgroup membership. This is an intended-reason control for the use of purity in (2).

The arbitrary finite-source statement is WRITTEN; these finite controls are not a formal proof, a canonical-freeness certificate or adoption.
