# Orthodox original sources are exactly the group-actor side

**NEW AUTHOR WRITTEN REDUCTION with exact finite controls; unreviewed/unadopted.** Native check-start observation **Wed Oct 28 19:46:22 PDT 2026**. The group conclusion concerns the ACTUAL syntactic actor; it does not say every auxiliary pure CS actor is a group or prove an embedding for arbitrary orthodox sources. The needed pure-CS property for all original sources remains the named SQ-E input.

## 1. Exact structural theorem

Let S be a regular semigroup whose actual idempotence-context quotient `q:S→D=S/τ` is onto and pure, and whose D is completely simple. Then

`E(S) is a subsemigroup   iff   D is a group`.             (1)

Thus, for an original source under the named pure-CS quotient theorem, global orthodoxy is EXACTLY the actual group-actor case; a nonorthodox source necessarily has a non-group actual CS actor. In the orthodox case the actual group map is idempotent pure, `E(S)=q^(-1)(1)`, and E(S) is a unitary subset in the usual strong E-unitary sense. This is a reduction of actor structure, not a generic embedding theorem.

## 2. Proof for an arbitrary completely simple quotient

Since q is onto and pure, `E(D)=q(E(S))`: lift any idempotent actor and purity makes its source lift idempotent. If E(S) is closed, E(D) is therefore closed.

Write `D=M[G;I,Λ;Q]`. The idempotent in cell (i,λ) is `(i,Q_(λ,i)^(-1),λ)`. Closure under multiplication gives, for every i,j,λ,μ,

`Q_(λ,i)^(-1) Q_(λ,j) Q_(μ,j)^(-1)=Q_(μ,i)^(-1)`,

hence

`Q_(λ,j)=Q_(λ,i) Q_(μ,i)^(-1) Q_(μ,j)`.                (2)

Fix i0,μ0, put `r_λ=Q_(λ,i0)` and `c_i=Q_(μ0,i0)^(-1)Q_(μ0,i)`. Equation (2) is `Q_(λ,i)=r_λ c_i`. Therefore

`ψ(i,g,λ)=c_i g r_λ`

is an onto homomorphism D→G: ψ of a product factors exactly, and every group value is obtained in any chosen row/column. It is idempotent pure because `ψ(i,g,λ)=1` iff `g=Q_(λ,i)^(-1)`, the cell idempotent. Consequently idempotence contexts in D distinguish exactly ψ: if ψ differs, an actual left context whose ψ value is ψ(d)^(-1) makes one result idempotent and the other not. Hence `τ_D=ker ψ`.

Because q is the ACTUAL quotient and is pure, lifting/reflection of idempotence contexts shows `τ_D` is equality: any two τ_D-related images lift to τ-related source elements. Thus ψ is injective. But for each h∈G every Rees cell contains an element of ψ-value h; injectivity forces |I|=|Λ|=1. Hence D itself is a group.

Conversely, if D is a group, its only idempotent is1 and purity gives `E(S)=q^(-1)(1)`, a subsemigroup. Since S is regular, S is orthodox. Further, if either se or es is idempotent for e∈E(S), applying q forces q(s)=1, and purity makes s idempotent; this is the usual unitary-kernel property.

## 3. Consequences and dependency limits

For an orthodox original source the ACTUAL physical host target is an ordinary semidirect product of a locally regular band by a group, not a general non-group CS actor. In particular, the locally finite actor reduction in `frontier-20261028-orthodox-finite-original-reduction-v1.md`, SHA `d208670ba3ceddf6f680c51198209b9e56b23421c4067e2cc166b1e69c11924f`, can be read at the pure-group scope.

Billhardt's [1998 paper](https://www.academia.edu/53871668/On_Embeddability_into_a_Semidirect_Product_of_a_Band_by_a_Group) §3 attributes a strict embedding theorem to the case of seminormal idempotent bands. The publication itself cites private communication/in-preparation work; this note has NOT independently checked that theorem or inferred that every locally regular band is seminormal. If that attributed theorem is accepted, it would apply only to its exact E-unitary/seminormal scope. The source-status and six-element left-semiregular countermodel limits are in `frontier-20261028-billhardt-1998-local-scope-v1.md`, SHA `7bee7a5ad88ac7a3a103eb3c75f46a23c8f8f58bfbbf465eb7280fe899a7c616`.

Do not apply (1) to an arbitrarily chosen auxiliary CS actor. An orthodox source may map purely onto a non-group rectangular group; only its ACTUAL syntactic quotient is forced to be a group. Nor does nonorthodoxy by itself establish a same-q R/L collapse or nonembedding.

## 4. Exact checks

`frontier-20261028-orthodox-actor-dichotomy-checker-v1.py`, SHA `b2fe68dc33f1ecdfcf7838e392aae6632b0be2fee65b1910face56abc1be5091`, ran `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 19:46:22 PDT 2026**, exit0. It exhausts every source idempotence context for three cases:

```text
orthodox source=10 E=5 actual_actor=2 globally_nonregular_E=true
orthodox rectangular-group source=8 pure auxiliary actor=8 actual_tau_group=2
nonorthodox source=45 actual_actor=18 group_order=2 and nontrivial rectangle
PASS all actual idempotence signatures; auxiliary-actor distinction retained
```

The first source has the5-element locally regular non-globally-regular band from the published-scope boundary note as E and a nontrivial C2 action. The second shows why ACTUAL actor qualification is essential. The third is the previously verified original-class nonorthodox source with an explicit local-band q-host. All checks are same-author finite evidence; the universal proof is §2 and uses ordinary Rees representation and basic group cancellation. No independent review, formal/kernel proof, novelty or full-original-source conclusion is claimed.
