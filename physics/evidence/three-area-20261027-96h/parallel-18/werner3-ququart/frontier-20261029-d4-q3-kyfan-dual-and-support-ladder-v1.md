# Exact negative-space Ky Fan dual and support-ladder reduction of the original q3 target

**PhysicsResearch96h-2 / physics-1. WRITTEN, source-independent, all-variable; UNREVIEWED.** This packet proves two exact *equivalences* about the original target. It uses no source-certificate premise and is not a source-conditional variant. It does **not** prove the full original q3 inequality, the two-copy statement T_2 defined below, or either zero-leg class Z_2, Z_3. It makes no claim about the literature status of any of them, no novelty or priority claim, and no parent/f62/f153/human/family/formal/Lean/physical-operational acceptance. No selected target operator, state or numerical q value is used.

## 1. Setting and the statements compared

For d≥2 and n≥0 put `H_n=(C^d)^tensor n` and, for any complex operator C on H_n, take

`q_n(C) = Σ_(S⊆{1..n}) (−1/2)^|S| ||Tr_S C||HS²`,

with unnormalized partial traces and `Tr_∅ C=C`. For n=0, C is a scalar c and `q_0(c)=|c|²`. The original functional is q_3 at d=4.

`T_n` (for fixed d) is the statement that `q_n(C)>=0` for every complex C on H_n of rank≤2. The **original target** is `T_3` at d=4. `T_0` is trivial. `T_1` holds for every d, because `|Tr X|≤σ1+σ2≤sqrt2||X||HS` when rank X≤2.

**Legs.** At site i, the *output leg* of C is the smallest subspace E⊂C^d with `(P_E)_i C=C`. Equivalently it is the range of the site-i reduction of CC†. The *input leg* is the output leg of C†. A leg is *k-supported* if its dimension is ≤k. `Z_n` (for fixed d) is the statement that `q_n(C)>=0` for every rank≤2 C on H_n all of whose 2n legs have dimension ≥3.

## 2. The exact negative-space Ky Fan dual (d=4)

Write `vec C=Σ_(x,y) C_xy |x>⊗|y>`, regrouped by site. Let `Ω_i=Σ_j |j>⊗|j>` on site i's output/input pair, and `K_i=I−|Ω_i><Ω_i|/2`. Because `(<Ω_i|⊗I)vec C=vec(Tr_i C)`, expanding the product gives the original all-subset identity

`q_n(C) = <vec C,(K_1⊗…⊗K_n) vec C>`.

This identity is also recorded in `frontier-20261028-d4-positive-map-all-subsets-addendum-v1.md`, SHA256 `8cd42f794b79fec63fd8d607b41554891b3b6409d75efb7278ac29c962cbf500`.

At d=4, `||Ω_i||²=4`, so `K_i=I−2P_i` with `P_i=|Ω_i><Ω_i|/4` a projection; K_i is a reflection. With `Π_T=⊗_(i∈T)P_i⊗_(i∉T)(I−P_i)`, the product is `⊗K_i=Π_+−Π_−`, where `Π_−=Σ_(|T| odd)Π_T`. Hence

`q_n(C) = ||vec C||² − 2||Π_− vec C||²`.                                 (1)

Let `V_−=ran Π_−`. In operator language `V_−=vec(W_odd)`. Here W_odd is spanned by operators carrying an identity factor on an odd set T of sites and traceless factors on the other sites, because `vec(I_i)=Ω_i` and traceless matrices are orthogonal to `I_i`. So `dim V_−=Σ_(|T| odd)15^(n−|T|)`, which is 30 for n=2 and 676 for n=3.

**Theorem 1 (exact dual).** At d=4, `T_n` holds iff every vector φ∈V_− satisfies

`λ_1(φ)+λ_2(φ) <= ||φ||²/2`,                                          (2)

where `λ_1≥λ_2≥…` are the squared singular values of the operator X with vec X=φ (its squared Schmidt coefficients across the output|input cut). Equivalently, `σ1(X)²+σ2(X)²<=||X||HS²/2` for every X∈W_odd. Explicitly:

- **n=2:** `X=A⊗I+I⊗B` with `A,B∈sl_4(C)`; the condition reads `σ1²+σ2²<=2(||A||²+||B||²)`.
- **n=3:** `X=cI+I_1⊗Y_23+I_2⊗Y_13+I_3⊗Y_12`, each `Y_jk∈sl_4⊗sl_4` placed at sites j,k; the condition reads `σ1²+σ2²<=32|c|²+2Σ||Y_jk||²`.

*Proof.* Vectors vec C with rank C≤2 are exactly the vectors of Schmidt rank ≤2. By (1), `T_n` is equivalent to `sup ||Π_−ψ||²<=1/2` over unit ψ of Schmidt rank≤2. Now `||Π_−ψ||=sup_(φ∈V_−,||φ||=1)|<φ,ψ>|`. For a fixed unit φ, the von Neumann/Eckart–Young inequality gives `sup |<φ,ψ>|²=λ_1(φ)+λ_2(φ)` over unit ψ of Schmidt rank≤2. This supremum is attained by `ψ=φ_(2)/||φ_(2)||`, where φ_(2) is the sum of the two leading Schmidt terms. Exchanging the two suprema proves the equivalence, and both suprema are attained by compactness. The explicit forms follow from the orthogonal sector decomposition: the components are mutually orthogonal, and `||cI||²=64|c|²`, `||I_i⊗Y||²=4||Y||²` at n=3, `||A⊗I||²=4||A||²` at n=2. ∎

**Two-sided use, unconditional.** If some unit φ∈V_− has `λ_1+λ_2>1/2`, then `ψ=φ_(2)/||φ_(2)||` is an explicit rank-2 operator with `q_n(ψ)<=1−2(λ_1+λ_2)<0`. This follows from (1) and `||Π_−ψ||²>=|<φ,ψ>|²=λ_1+λ_2`. If `λ_1+λ_2=1/2`, the same ψ has `q_n(ψ)<=0`. Conversely, under `T_n`, a nonzero rank≤2 C satisfies `q_n(C)=0` iff `ψ=vec C/||C||` has `||Π_−ψ||²=1/2`. In that case the normalized φ=Π_−ψ attains equality in (2), and ψ is a maximizer of `|<φ,·>|` over unit vectors of Schmidt rank≤2. Thus, under T_n, equality operators are exactly best-rank-2 directions of Ky-Fan-extremal vectors of V_−.

**Single-sector instances.** If `X=I_i⊗Z` for any Z on the other sites (this covers each one-identity sector, together with the scalar sector), then the singular values of X are those of Z, each repeated four times. Hence `σ1(X)²+σ2(X)²=2σ1(Z)²<=2||Z||²=||X||²/2`, with equality iff Z has rank1. This quantifies the earlier unreviewed negative-space rank theorems. The open content of (2) lies in superpositions across different sectors.

## 3. Exact one-leg contraction identity

**Lemma 2 (factorization).** For operators C′ on m sites and D on k further sites, `q_(m+k)(C′⊗D)=q_m(C′)q_k(D)`. Every subset splits as `S=S′⊔S″`; then `Tr_S(C′⊗D)=Tr_(S′)C′⊗Tr_(S″)D`, norms multiply and the coefficients factor. For a unit local u, `q_1(|u><u|)=1−1/2=1/2`.

**Lemma 3 (exact contraction identity).** Let E⊂C^d be two-dimensional, with orthonormal bases {e_a} of E and {f_b} of E⊥, and normalized Haar measure μ on the unit sphere S(E). For u∈S(E), let u⊥∈E be a unit vector orthogonal to u; its phase is immaterial. For local vectors α,β write `<α|C|β>_i=(<α|_i⊗I)C(|β>_i⊗I)`, an operator on the other n−1 sites. If `(P_E)_i C=C` (output leg at site i inside E), then

`q_n(C) = 3∫_(S(E)) q_(n−1)(<u|C|u⊥>_i) dμ(u) + Σ_(a,b) q_(n−1)(<e_a|C|f_b>_i)`.   (3)

If instead `C(P_E)_i=C` (input leg inside E), then

`q_n(C) = 3∫_(S(E)) q_(n−1)(<u⊥|C|u>_i) dμ(u) + Σ_(a,b) q_(n−1)(<f_b|C|e_a>_i)`.   (4)

*Proof.* Consider the output case. Since vec C lies in the range of `(P_E⊗I)` at site i, K_i may be replaced by its compression

`(P_E⊗I)K_i(P_E⊗I)=P_E⊗I−|Ω_E><Ω_E|/2`, with `Ω_E=Σ_a e_a⊗ē_a`.

Haar invariance and the three-dimensional symmetric subspace of E⊗E give `∫|u><u|^tensor2 dμ=(P_E⊗P_E+F_E)/6`. Partial transposition of the second factor gives `∫|u><u|⊗|ū><ū| dμ=(P_E⊗P̄_E+|Ω_E><Ω_E|)/6`. Also `∫|u><u|dμ=P_E/2` and `|ū⊥><ū⊥|=P̄_E−|ū><ū|`. Together these give

`P_E⊗I−|Ω_E><Ω_E|/2 = 3∫|u><u|⊗|ū⊥><ū⊥| dμ + P_E⊗(I−P̄_E)`,

with `I−P̄_E=Σ_b|f̄_b><f̄_b|`. For any rank-one product term `|α><α|⊗|β̄><β̄|` at site i, direct index contraction gives `(<α|⊗<β̄|⊗I)vec C=vec(<α|C|β>_i)`. Its contribution is therefore `<vec X,(⊗_(j≠i)K_j)vec X>=q_(n−1)(X)` with `X=<α|C|β>_i`. This proves (3). For the input case, `vec(CP_E)=(I⊗P̄_E)vec C`, and the same calculation with the roles exchanged, `I⊗P̄_E−|Ω_E><Ω_E|/2=3∫|u⊥><u⊥|⊗|ū><ū| dμ+(I−P_E)⊗P̄_E`, gives (4). These are exact identities, not only inequalities. They also cover legs of dimension0 or1, by extending to an arbitrary 2D E. ∎

Contraction never increases rank: `rank <α|C|β>_i<=rank C`. It also preserves every output/input leg inclusion at the other sites, because the site-i contraction commutes with projections at other sites.

## 4. The support ladder

**Theorem 4 (ladder equivalence).** Fix d≥2, n≥s≥0, a set L of s distinct sites, and at each i∈L a choice of output or input leg. Then the following are equivalent:

(a) `q_n(C)>=0` for every rank≤2 C whose chosen leg at every i∈L is 2-supported;
(b) the same for every rank≤2 C whose chosen legs at L are 1-supported;
(c) `T_(n−s)`.

Moreover, for s=n, (a) holds for C of **every** rank.

*Proof.* (c)⇒(a): apply Lemma 3 successively at the s sites of L. After the s contractions, q_n(C) is a positive-weight integral and sum of values `q_(n−s)(X)` with rank X≤2, so it is nonnegative by T_(n−s). If s=n, each X is a scalar and `q_0(X)=|X|²>=0` for any rank of C. (a)⇒(b) is immediate. (b)⇒(c): for any rank≤2 C′ on the sites outside L, put `C=C′⊗⊗_(i∈L)|u_i><u_i|`. It has rank≤2 and 1-supported legs at L. By Lemma 2, `q_n(C)=2^(−s)q_(n−s)(C′)`. ∎

**Corollaries (all source-independent).**

1. **Nesting.** `T_n ⇒ T_m` for every m≤n and every d. In particular the original target T_3 (d=4) implies the complete two-copy rank-2 statement T_2 (d=4). By Theorem 1, T_2 is the inequality `σ1²+σ2²<=2(||A||²+||B||²)` for every `A⊗I+I⊗B` with A,B∈sl_4. Any proof of the original target must therefore also prove T_2.
2. **One-leg stratum.** At d=4, n=3, the class of rank≤2 C having at least one 2-supported leg (any site, output or input) is exactly as hard as T_2: positivity on it is equivalent to T_2.
3. **n−1 legs suffice, for every n and d.** If at least n−1 distinct sites carry a 2-supported leg (orientation chosen per site), then `q_n(C)>=0` for rank≤2 C, since T_1 and T_0 hold. This generalizes the two-leg n=3 theorem of `frontier-20261028-d4-source-independent-local-support-consolidated-v1.md`, SHA256 `0ccc096a2eb7309bb6398872660cc24ad8213119d88eb917110fec8ab238c01c`, to arbitrary n and mixed orientations. If **every** site carries a 2-supported leg, `q_n(C)>=0` for C of any rank.
4. **Exact stratification.** `T_n ⇔ T_(n−1) ∧ Z_n`. Every rank≤2 C either has some 2-supported leg, which is handled by Theorem 4 with s=1 given T_(n−1), or lies in the Z_n class; the converse uses Corollary 1. Since T_1 holds, induction gives

`T_n ⇔ Z_2 ∧ Z_3 ∧ … ∧ Z_n`.

For the original problem, `T_3 (d=4) ⇔ Z_2 ∧ Z_3 (d=4)`: the full target is exactly the conjunction of the two-copy and three-copy classes in which every leg has dimension ≥3.
5. **Equality inheritance.** Assume T_(n−s) and let C be in the s-leg class of Theorem 4(a). By (3)/(4), nonnegative continuous integrands and full Haar support, `q_n(C)=0` iff every contraction X occurring in the iterated identities has `q_(n−s)(X)=0`. This includes every u∈S(E) and every finite term. For s=n−1 this means each one-site contraction is 0 or a scalar multiple of an orthogonal rank2 projection.

Corollary 4 is consistent with the earlier dense-boundary lemma `frontier-20261028-d4-dense-local-support-boundary-extension-v1.md`, SHA256 `4e6fe20463ddba8ebf32fba9cfd9139d058837b05a618732cc0b85eb91bffff3`. By continuity, positivity on the open dense full-local-support set already implies T_3, and hence T_2; the ladder identifies the low-support boundary strata **exactly**, rather than by a limit.

## 5. What remains and provenance

Neither Z_2 nor Z_3 (d=4) is proved here. Equivalently, the cross-sector Ky Fan inequality (2) for n=2 and n=3 remains unpaid by source-independent argument. The separate source-conditional packets are neither used nor changed, and no new conditional bound is introduced. The proofs use only the original trace functional, vectorization, an elementary Haar second-moment identity, rank monotonicity under contraction and the Eckart–Young/von Neumann inequality. No elected HELD/ZERO/NONINPUT episode, its consumers or its guidance is used. No selected target operator or value is evaluated. Historical process findings and the frozen f153/f62 boundaries are unchanged.
