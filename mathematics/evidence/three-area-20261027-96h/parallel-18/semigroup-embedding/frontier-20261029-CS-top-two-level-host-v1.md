# A fixed-actor RIGHTSN separation construction: a closed completely simple top over a completely simple ideal

**NEW AUTHOR WRITTEN theorem with exact finite controls; UNREVIEWED / UNADOPTED.** This extends the group-top construction by replacing its top group with an arbitrary completely simple subsemigroup. It is a direct statement over the specified actor q; it uses neither Fact1 nor the challenged canonical-host/Q1 equivalence. Parent's f164 qualification is binding (`frontier-20261029-f164-parent-direction-intake-v1.json`, SHA d6e9f56f7ff864418e3a6061c9a3c380b84ffb54b304e70d7145d818d12797a2). No arbitrary-actor transfer, Q1 solution, novelty, adoption or formal verification is asserted.

## 1. Statement and conventions

Suppose S is the disjoint union T ⊔ K, where T is a nonempty completely simple subsemigroup and K is a nonempty completely simple ideal. Let q:S→D=M[G;I,Λ;P] be an onto idempotent-pure homomorphism. Write q(s)=(i_s,g_s,λ_s) and w(s,t)=g_s p_(λ_s,i_t).

Then there is a band B, with G acting by automorphisms, and β:S→B such that

`β(st)=β(s) · ^(w(s,t))β(t)`

and β separates every pair of distinct R-related idempotents with the same q-value. Every local monoid of B is a right regular band (xyx=yx): B is RIGHTSN. No local-regularity hypothesis on S is needed for this restricted separation statement.

For clarity the physical product used here is B×D with

`(b,(i,g,λ))(c,(j,h,μ)) = (b · ^(g p_(λ,j))c, (i,g p_(λ,j)h,μ))`.

The displayed β equation says exactly that s↦(β(s),q(s)) is a homomorphism. Only its stated R-idempotent separation, not full injectivity, is claimed.

## 2. Elementary imports and real points

Named ordinary import: Rees' coordinate description of a completely simple semigroup as M[H;J,L;Q]. The only translation fact needed is explicit: for t=(i,h,ℓ), left multiplication maps each H-class H_(j,ℓ′) bijectively onto H_(i,ℓ′), because its group-coordinate map is u↦h Q_(ℓ,j)u.

Let J,L be the R- and L-class index sets of T. Write r(t),c_T(t) for its row and column. Because q preserves Green relations within T, i_t depends only on r(t), written ι(r(t)), and λ_t depends only on c_T(t), written κ(c_T(t)).

Purity makes q injective on every H-class of T: restriction to that maximal subgroup is a group homomorphism; an element mapping to its image identity is idempotent by purity, hence is that subgroup's identity.

Let ColK be the L-classes of K, write c_K(k) for a column, and write μ(c) for the D-column of a K-column c. The right action c·t=c_K(kt) is well defined for t∈T. Also c_K(sk)=c_K(k) for s∈S,k∈K: choose f∈E(K) with fk=k; then sk=(sf)k with sf∈K, so the CS product retains k's column.

The real points are W=G×ColK. Put C=G×L. For ω=(m,c) and a T-row i∈J define the entry label

`a_i(ω)=m p_(μ(c),ι(i))`.

Call ω *fixed* if c·e=c for some e∈E(T). This condition depends on c only.

## 3. Partial functions that replace hand-indexed orbits

For each ω=(m,c)∈W and i∈J define a partial function F_(ω,i):C⇀W:

`F_(ω,i)(b,ℓ)=(b,c·t)`

if there exists t∈T with r(t)=i, c_T(t)=ℓ and g_t=a_i(ω)^(-1)b. Such t is unique by H-class injectivity, so this is well defined. Each function has nonempty domain, since any t in row i supplies b=a_i(ω)g_t.

**Key property.** If ω′=F_(ω,i)(b,ℓ) is defined, then ω′ is fixed and

`F_(ω′,j)=F_(ω,i)` for every j∈J,

as partial functions, including equality of domains.

*Proof.* Let t give the displayed value. Choose f∈E(T) in t's L-class with tf=t. Then (c·t)·f=c·t, so ω′ is fixed. To evaluate at a new column (b′,ℓ′), left multiplication by t is a bijection H_(j,ℓ′)→H_(i,ℓ′). For u∈H_(j,ℓ′),

`a_i(ω) g_(tu) = a_i(ω)g_t p_(λ_t,ι(j))g_u = b p_(κ(ℓ),ι(j))g_u = a_j(ω′)g_u`.

Consequently the defining label equation for tu at ω holds if and only if the defining label equation for u at ω′ holds. The output columns agree by c·(tu)=(c·t)·u. Bijectivity proves both existence directions and output equality. □

**Fixed-point consequence.** For a fixed ω all F_(ω,i) agree; write the common function F_ω. Indeed, choose an idempotent e fixing c and put i=r(e), ℓ=c_T(e). Then μ(c)=λ_e and a_i(ω)g_e=m, so F_(ω,i)(m,ℓ)=ω. The key property gives independence of i.

Let ℱ be the set of distinct functions F_(ω,i), with identical partial functions identified literally. Thus every defined value of F∈ℱ is a fixed real point ω′ with F_(ω′)=F.

## 4. Completing the rectangular action without identifying real points

The top band A=(G×J)×C is rectangular:

`((a,i),ξ)((a′,i′),ξ′)=((a,i),ξ′)`.

The point set Ω is the following disjoint union:

- all real points W, retained as distinct elements;
- orbit phantoms [F,ξ] for F∈ℱ and ξ∉dom(F);
- moved phantoms [ω,(a,i),ξ] for a nonfixed ω, a≠a_i(ω), and ξ∈C.

Define Γ_F(ξ)=F(ξ) if defined and Γ_F(ξ)=[F,ξ] otherwise. Define the right A-action by:

1. If ω is fixed, `ω·((a,i),ξ)=Γ_(F_ω)(ξ)` for every row (a,i).
2. If ω is not fixed and a=a_i(ω), `ω·((a,i),ξ)=Γ_(F_(ω,i))(ξ)`.
3. If ω is not fixed and a≠a_i(ω), `ω·((a,i),ξ)=[ω,(a,i),ξ]`.
4. `[F,ξ]·((a′,i′),ξ′)=Γ_F(ξ′)`.
5. `[ω,(a,i),ξ]·((a′,i′),ξ′)=[ω,(a,i),ξ′]`.

**Act law.** For every π∈Ω, π·((a,i),ξ)·((a′,i′),ξ′)=π·((a,i),ξ′). In cases 1–2 the first value is Γ_F(ξ). If real, the key property makes it fixed with function F; if phantom, rule 4 applies. Both give Γ_F(ξ′). Cases 3 and 5 retain the original moved row; case 4 again gives Γ_F(ξ′). These exhaust the disjoint point types. In particular no quotient identifying real points was taken.

G acts by left multiplication on all group labels. Explicitly ^u(m,c)=(um,c), ^u(b,ℓ)=(ub,ℓ), and (^uF)(ξ)=^u(F(^(u^(-1))ξ)) on the transported domain. Since a_i(^uω)=u a_i(ω), this sends F_(ω,i) to F_(^uω,i), preserves fixedness and mismatch, and transports each phantom label. Every rule above is equivariant.

## 5. The band B and the source coefficients

Take B=A ⊔ Ω, make Ω right zero (ππ′=π′), and define mixed products xπ=π, πx=π·x. The act law proves associativity; all elements are idempotent. The equivariant action above is by band automorphisms.

For x∈A, its local monoid is {x}∪(Ω·x), a right-zero band with identity x adjoined. It is right regular. For π∈Ω, πBπ={π}. Hence B is RIGHTSN.

Set

`β(t)=((1,r(t)),(g_t,c_T(t)))` for t∈T,

`β(k)=(g_k,c_K(k))∈W` for k∈K.

Verify all source products:

- t,t′∈T: the rectangular product takes row (1,r(t)) and column (w(t,t′)g_(t′),c_T(t′)), exactly β(tt′).
- s∈S,k∈K: multiplication by a right-zero point returns its translate. The K-column is unchanged under left multiplication, and g_(sk)=w(s,k)g_k, giving the equation.
- k∈K,t∈T: with ω=β(k), i=r(t), the row of ^(w(k,t))β(t) is (a_i(ω),i). Its column is (w(k,t)g_t,c_T(t)), where F_(ω,i) is defined by t and gives (g_(kt),c_K(kt)). Rules 1 or 2 return precisely β(kt).

These cases cover S² and establish the claimed physical-product homomorphism.

## 6. R-idempotent separation and exact boundary

An R-related idempotent pair cannot straddle T and K: ef=f and fe=e would put both in K if either were in K. For a pair lying in T or lying in K, these same two intrinsic products already certify its common row in that completely simple subsemigroup.

Distinct R-related idempotents inside a completely simple semigroup have different L-columns (one H-class has only one idempotent). In T these columns occur literally in β's top C-coordinate; in K they occur literally in its distinct real points. Thus β separates them; in particular it separates those with equal q-values. □

The theorem is only for a *closed* completely simple top over a completely simple ideal. It does not handle S45's top J-class, whose products can drop into K; it does not handle more levels or arbitrary regular sources. Its direct construction is unaffected by the unproved actor-transfer step flagged by f164, but it does not repair that step.

## 7. Exact finite controls

Checker `frontier-20261029-CS-top-two-level-host-checker-v1.py`, SHA ea5ad4a4903d64c4c62512f9a70ccd48c24eb9afc90044e3a2658b42a0d705e0, uses exact integer tables and C2. At Thu Oct 29 09:24:20 PDT 2026 its first three cases completed with exit 0; the fourth added case alone completed in the retained eval kernel before Thu Oct 29 09:26:21 PDT 2026. The final whole script was not rerun after adding case four; the cases were exercised separately.

|Source|Source size|Top rows × columns|Real / orbit-phantom / moved-phantom points|Band size|Same-fibre R-pairs separated|
|---|---:|---|---|---:|---:|
|Earlier group-top source|14|1×1|6 / 0 / 4|14|2|
|Product with RB22, actor ignores that factor|56|2×2|12 / 0 / 32|60|30|
|Physical source with genuinely varying top actor rows|48|4×4|8 / 0 / 0|72|12|
|Inflated idempotent source ×RZ2; proper top-group image|18|1×2|8 / 4 / 16|36|5|

For every case the checker verifies the source partition, CS eggboxes, purity and actor products; the key partial-function identities; all final band associativity and RIGHTSN identity substitutions; the C2 automorphism; all source-host equations; and every same-fibre R-pair. The fourth case exercises both phantom types, and the second separates R-pairs in the top as well as the ideal. These finite controls are same-author evidence, not a machine proof of the arbitrary-group theorem.
