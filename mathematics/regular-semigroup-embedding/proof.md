# Proofs: Problem 1 of 关于正则半群的两个嵌入问题 — what is settled here

Status of the book's Problem 1: no resolution located as of 2026-10-14, so its current status is
uncertified (see README). This file proves partial results and records negative results about
simple obstruction patterns:

* **Lemma 1.** For orthodox semigroups, weakly E-unitary = E-unitary.
* **Lemma 0′.** If a finite `S` embeds in a Pastijn or restricted product, then its least
  completely simple congruence is idempotent pure.
* **Theorem A (reduction).** For orthodox semigroups, embeddability into a Pastijn product, or into
  a restricted semidirect product, of a band by a completely simple semigroup is equivalent to
  embeddability into a semidirect product of a band (from the same variety, enlarged by
  rectangular bands) by a group. So the orthodox part of Problem 1 is exactly question Q_orth in
  §3. I found no earlier explicit statement of this reduction.
* **Section 4 (locally regular bands).** Every band with at most two D-classes is locally
  regular. A 5-element example `E5` shows locally regular ≠ regular, and 5 is the minimum order.
  `FB(3)` is locally regular. The class of left semiregular bands is not contained in the
  locally regular ones.
* **Theorem B.** Problem 1 has a positive answer for orthodox semigroups whose band is regular,
  hence for all monoids. This rests on Szendrei's 1987 theorem; its publisher abstract is in
  `sources/szendrei1987_PRSE106_abstract.txt`.
* **Theorem C.** Problem 1 has a positive answer for every orthodox member of the class whose band
  has at most two D-classes, including non-regular bands such as `E5`. The embedding is into a
  wreath product `B0 ≀ G`, with `B0` a band with at most two D-classes.
  - These semigroups are quasi-F-orthodox in the sense of Billhardt–Szendrei 1995 (Remark C.1).
    Embeddability into *some* band ⋊ group therefore already follows from their Theorem 4.1.
  - The independent reviewer also deduces that they are *generalized* F-orthodox. In that case
    BS95 Theorem 4.2 gives a band in `var(E) ⊆ L(ReB)`. I have not verified that deduction.
  - So Theorem C's conclusion may be known. What this note adds is the explicit self-contained
    construction.
* **Section 7.** Two natural necessary conditions for embeddability, (C2) and (C3), hold in every
  E-unitary orthodox semigroup, so they cannot detect a counterexample.
* **Proposition F (computer-assisted).** Q_orth holds when `S/σ ≅ Z2` and `|E| ≤ 6`.
* **Theorem X (written, parent-audited; not Lean-checked).** Every regular locally orthodox
  semigroup with a completely simple ideal has a completely simple quotient which is
  idempotent pure under weak E-unitarity. Thus ξ is pure for every finite member of P1's class.
  The complete coordinate proof is in [`hmz-lean-20261014/xi-purity.md`](hmz-lean-20261014/xi-purity.md);
  it does not prove an embedding and makes no novelty claim.
* **Lean continuation.** [`hmz-lean-20261014/Formal.lean`](hmz-lean-20261014/Formal.lean)
  formalizes the necessary direction for both adopted product readings, actual product/carrier
  constructions, and the derived-functor criterion and its converse. All 32 reported roots
  compiled with only `propext`/`Quot.sound`; their explicit hypotheses remain in
  [`claims.json`](hmz-lean-20261014/claims.json). The HMZ verdict was `done:false`, not goal acceptance.

Notation: maps are written on the left. In a band, `x R y` means `xy = y, yx = x`, `x L y` means
`xy = x, yx = y`, and `D = R∘L` (on a band, `x D y` iff `xyx = x` and `yxy = y`). `σ` is the least
group congruence, and `V(a)` is the set of inverses of `a`.

## 0. Definitions and the formal problem

Definitions follow the book (sources/book-excerpt.txt) verbatim in content:

* `S` is regular; `a ≤ b` iff `a = eb = bf` for some `e, f ∈ E(S)` (natural partial order).
* **weakly E-unitary:** `e ∈ E(S), e ≤ a ⇒ a ∈ E(S)`.
* **E-unitary:** `e, ea ∈ E(S) ⇒ a ∈ E(S)` and `e, ae ∈ E(S) ⇒ a ∈ E(S)` (standard; not defined
  in the book).
* **orthodox:** `E(S)` is a subsemigroup (a band).
* **regular band:** `efege = efge` (book). This is the identity `axya = axaya`.
* **seminormal band (book's 半正规带):** `eBe` is a regular band for every `e ∈ B`. These are
  called **locally regular** below, and their variety is written `L(ReB)`. It is a variety,
  defined by `ezexeyeze = ezexezeyeze`.
* **locally r-orthodox:** for every `e ∈ E(S)`, `eSe` is orthodox and `E(eSe)` is a regular band.
* **completely simple:** `C = M[G; I, Λ; P]`, with product `(i,g,λ)(j,h,μ) = (i, g p_{λj} h, μ)`.
* **Pastijn product.** Definition from Szendrei 2019 survey §5.2, for a normal band; for an
  arbitrary semigroup in place of `B` it is the Pastijn–Rees product with all `q_{λi} = 1`
  [Auinger–Szendrei 2005, §3, Remark 3.1]. A group `G` acts on a band `B` by automorphisms,
  written `x ↦ ^g x`, and `B ⊙ C` is `B × C` with
  `(a,(i,g,λ))(b,(j,h,μ)) = (a · ^{g p_{λj}} b, (i, g p_{λj} h, μ))`.
* **restricted semidirect product** [Auinger–Polák 1997, Def. 3.1]. `C` acts on `B` by
  endomorphisms, through a homomorphism `x ↦ φ_x` with `φ_{xy} = φ_x φ_y`. Its elements are
  `B ⊙* C = {(a,x) : φ_{xx'}(a) = a}` for some, equivalently every, `x' ∈ V(x)`, with
  `(a,x)(b,y) = (φ_{x(y∧x)x'}(a) · φ_x(b), xy)`.
  When `C` is completely simple the sandwich element `y∧x` is the idempotent of `H_{row(y),col(x)}`.
  Hence `x(y∧x) = x`, and the product is the semidirect one, `(a,x)(b,y) = (a · φ_x(b), xy)`.

**Formal Problem 1 (two readings, fixed in advance).** Is every weakly E-unitary, locally
r-orthodox regular semigroup `S` isomorphic to a subsemigroup of

* (P) `B ⊙ C`, or
* (R) `B ⊙* C`,

where `B` is a locally regular band and `C` is a completely simple semigroup?

Billhardt–Szendrei proved the analogue for locally inverse semigroups and normal bands, in the
form "restricted semidirect product, and, equivalently, Pastijn product" (abstract of BS 2003).
That restricted products and Pastijn products have the same embeddable classes, for arbitrary
regular first factors (via subsemigroups and direct powers), is due to BS 2003 and is reported in
Auinger–Szendrei 2005, p. 40.

Two broader readings are not adopted:

* the Jones–Trotter regular semidirect product `Reg(B * C)`;
* the ordinary semidirect product `B * C`, with `C` acting by endomorphisms.

Every positive result below lands in a semidirect product by a group, so it is positive in these
readings too. Theorem A and Lemma 0′ are proved here only for (P) and (R).

**Lemma 0 (necessity).** Let `B` be a locally regular band and `C` completely simple. Every
regular subsemigroup `U` of `B ⊙ C` or of `B ⊙* C` is weakly E-unitary and locally r-orthodox.
So embeddability is the only open direction.

*Proof.* Let `π` be the projection to `C`.

* *Idempotents lie over idempotents.* In `B ⊙ C`, `(a,(i,p_{λi}⁻¹,λ))² = (a·a, ·) = (a, ·)`. In
  `B ⊙* C`, this is [Auinger–Polák 1997, Lemma 3.5]. In both cases
  `π⁻¹(E(C)) = E(B ⊙ C)` (resp. `E(B ⊙* C)`).
* *Weakly E-unitary.* If `e ≤ a` in `U`, write `e = fa = ag` with `f, g ∈ E(U)`. Then
  `π(e) ≤ π(a)` in `C`. The natural order of a completely simple semigroup is equality, so
  `π(a) = π(e) ∈ E(C)`, hence `a ∈ E(U)`.
* *Locally r-orthodox.* Let `u = (b, e) ∈ E(U)`.
  - In `B ⊙ C`, the idempotents of `u(B ⊙ C)u` are the pairs `(y, e)` with `y ∈ bBb`, multiplied
    as `(y,e)(y',e) = (yy', e)`. They form a band `≅ bBb`.
  - In `B ⊙* C`, `φ_e(b) = b`. For `eye = e` we get `φ_{ey}(b) = φ_{eye}(b) = b`, so again the
    idempotents of `u(B ⊙* C)u` form a band of pairs `(z, e)` with `z ∈ bBb ∩ B_e`, and
    `(z,e)(z',e) = (zz', e)`.

  In both cases `E(uUu)` is contained in a band isomorphic to a subband of `bBb`. That band is
  regular because `B` is locally regular. So `uUu` is orthodox and `E(uUu)` is regular. ∎

**Lemma 0′ (a Kad'ourek-type necessary condition).** Let `S` be a finite semigroup that embeds
in some `B ⊙ C` or `B ⊙* C`, with `B` any band and `C` completely simple. Then the least completely
simple congruence `ξ` of `S` is idempotent pure.

*Proof.*

1. The projection computation in the first bullet of Lemma 0's proof uses only that `B` is a band.
   It shows `π⁻¹(E(C)) ∩ S ⊆ E(S)`, so `ρ := ker(π|_S)` is idempotent pure.
2. `S/ρ ≅ π(S)` is completely simple. Every nonempty `π(S) ∩ H` is a finite subsemigroup of a group,
   hence a subgroup. So `π(S)` is a union of groups, in particular regular. For idempotents `e, f`,
   `efe ∈ π(S) ∩ H_e` has an inverse in that subgroup, which gives `e ∈ π(S) f π(S)`.
3. So `ξ ⊆ ρ`, and a congruence contained in an idempotent-pure congruence is idempotent pure. ∎

For finite `S`, `ξ` is computable: it is the congruence generated by the pairs `(x, x(yx)^ω)`. The
identity `x = x(yx)^ω` characterizes finite completely simple semigroups.

Status of this condition on Problem 1's class:

* For orthodox `S` it holds automatically: weakly E-unitary gives E-unitary (Lemma 1), so
  `ξ ⊆ σ` with `σ` idempotent pure.
* For locally inverse `S` it is Kad'ourek's theorem.
* For **finite** weakly E-unitary, locally r-orthodox `S`, this condition now always holds by
  [Theorem X](hmz-lean-20261014/xi-purity.md): a regular semigroup with a completely simple ideal
  and orthodox local monoids has a completely simple quotient that becomes idempotent pure under
  weak E-unitarity. This is a complete written, parent-audited proof, **not Lean-checked**, with
  no novelty claim. It closes the finite ξ-non-purity obstruction, not the embedding problem.
* For arbitrary infinite `S` without a completely simple ideal, purity remains unresolved here.
* `work/check_xi_ideal_extensions.py` tests the family `S = K ∪ {f}`, where `K = M[H;I,Λ;P]` and
  `f` is an idempotent acting by a linked bitranslation. 355 random weakly E-unitary, locally
  r-orthodox instances, 300 of them non-orthodox, all have `ξ` idempotent pure
  (`evidence/check_xi_ideal_extensions.log`).
* *By hand (sketch, following the second reviewer).* Normalize `P` at a row fixed by `α` and a
  column fixed by `β`. Then `γ = δ = 1` on those indices. Local r-orthodoxy makes `fKf` orthodox, so
  `P` is identically 1 on `Im β × Im α`. The linking condition `p_{λα(j)}γ_j = δ_λ p_{β(λ)j}` then
  makes the corresponding whole rows and columns of `P` equal to 1. Collapsing them gives an
  idempotent-pure completely simple quotient, so `ξ` is idempotent pure. Linking alone is not
  enough: `K = M[C₂; 2, 2; (1 1; 1 g)]` with an identity adjoined satisfies linking, yet `ξ` is
  universal. That example is not locally r-orthodox.

## 1. Lemma 1 (orthodox: weakly E-unitary ⟺ E-unitary; σ ∩ H = Δ)

Let `S` be orthodox.

(⇐) Let `e ≤ a`, so `e = fa` for some `f ∈ E`. Then `f, fa ∈ E`, and E-unitarity gives `a ∈ E`.

(⇒) Let `e, ea ∈ E` and `a' ∈ V(a)`. Put `x := aa'·ea`.

* `x ∈ E`, because `aa', ea ∈ E` and `E` is a band.
* `x = (aa'e)·a`, where `aa'e ∈ E` because `S` is orthodox.
* `x = a·(a'ea)`, where `a'ea ∈ E` because, in an orthodox semigroup, `a'ga ∈ E` for all `g ∈ E`.

So `x ≤ a`, and weak E-unitarity gives `a ∈ E`. The right-hand condition is dual.

Now let `S` be E-unitary orthodox, and let `s, t` be H-related and σ-related. Choose `s'`, and
`t* ∈ V(t) ∩ H_{s'}`, with `ss' = tt* = e` and `s's = t*t = f`. Then `s't ∈ E`, because in an
E-unitary orthodox semigroup σ is a group congruence whose kernel is exactly `E` (Szendrei 2019
survey, §5.1). Also `s't ∈ R_{s'} ∩ L_t = H_f`, and the only idempotent in `H_f` is `f`, so
`s't = f`. Hence `t = et = ss't = sf = s`. ∎

## 2. Two tools for semidirect products of bands by groups

Let `φ : S → B ⋊ G` be an embedding, with `φ(x) = (β(x), γ(x))` and `G` acting by automorphisms.

**Lemma 2.** `γ(E(S)) = 1`. If `γ(s) = g` and `s' ∈ V(s)`, then `β(s) = β(ss') · ^gβ(s's)`.

*Proof.* `(b,g)` is idempotent only if `g = 1`. From `φ(ss') = (β(s)·^gβ(s'), 1)` and
`φ(s's) = (β(s')·^{g⁻¹}β(s), 1)`:

```
β(ss')·^gβ(s's) = β(s)·^gβ(s')·^gβ(s')·β(s) = β(s)·^gβ(s')·β(s) = β(ss's) = β(s).
```
∎

**Lemma 3 (derived-category criterion).** Let `S` be a semigroup, `G` a group and `σ : S → G` a
surjective homomorphism. Suppose `F` assigns to each `g ∈ G` and `s ∈ S` an element `F(g,s)` of a
band `B0` such that

* `F(g,s)·F(gσ(s), t) = F(g, st)` (functor), and
* `F(1,s) = F(1,t)` together with `σ(s) = σ(t)` implies `s = t` (faithful on hom-sets).

Then `s ↦ (f_s, σ(s))`, where `f_s(g) = F(g,s)`, embeds `S` into the wreath product `B0^G ⋊ G`,
with action `(^h f)(g) = f(gh)`. That action is by automorphisms, and `B0^G` lies in the variety
generated by `B0`.

*Proof.* `(f_s·^{σ(s)}f_t)(g) = F(g,s) F(gσ(s),t) = F(g,st) = f_{st}(g)`, and injectivity is
faithfulness at `g = 1`. ∎

## 3. Theorem A (orthodox reduction)

**Theorem A.** Let `S` be an orthodox semigroup and `V` a variety of bands containing all
rectangular bands. The following are equivalent:

* (i) `S` embeds in some Pastijn product `B ⊙ C`, with `B ∈ V` and `C` completely simple;
* (ii) `S` embeds in some restricted semidirect product `B ⊙* C`, with `B ∈ V` and `C` completely
  simple;
* (iii) `S` embeds in some semidirect product `B ⋊ G`, with `B ∈ V` and `G` a group.

They imply that `S` is E-unitary.

*Proof.*

**(iii)⇒(i),(ii).** `B ⋊ G = B ⊙ G`, taking the trivial Rees matrix representation `I = Λ = {∗}`
and `p = 1`. Also `B ⋊ G = B ⊙* G`, because `φ_{xx⁻¹} = φ_1 = id`.

**(iii)⇒ E-unitary.** If `e, ea ∈ E`, then `γ(a) = γ(ea) = 1`, so `φ(a) = (β(a),1)` is idempotent,
and `a ∈ E` by injectivity.

**(i)⇒(iii).** Let `C = M[G; I, Λ; P]`, let `π : B ⊙ C → C` be the projection, and let `T' = π(S)`.
`T'` is a regular subsemigroup and is orthodox, since by Lallement's lemma its idempotents are
images of idempotents. Let `I'` and `Λ'` be the sets of rows and columns occurring in `T'`, and let
`e_{iλ} = (i, p_{λi}⁻¹, λ)` be the idempotent of `H_{iλ}`.

1. *Every `e_{iλ}` with `i ∈ I'`, `λ ∈ Λ'` lies in `T'`.* Take `t₁ ∈ T'` in row `i` and `t₂ ∈ T'`
   in column `λ`. Then `t₁t₁*` and `t₂*t₂` are idempotents of `T'`, and so is their product
   (`T'` is orthodox), which lies in `H_{iλ}`.
2. *For `i, j ∈ I'` and `λ, μ ∈ Λ'`: `p_{λi}⁻¹ p_{λj} p_{μj}⁻¹ = p_{μi}⁻¹`.* The product
   `e_{iλ}e_{jμ} = (i, p_{λi}⁻¹p_{λj}p_{μj}⁻¹, μ)` is idempotent, so it equals `e_{iμ}`.

Fix `i₀, λ₀`. Point 2 with `j = i₀`, `μ = λ₀` gives `p_{λi} = u_λ v_i`, where
`u_λ = p_{λi₀}p_{λ₀i₀}⁻¹` and `v_i = p_{λ₀ i}`.

Let `U = π⁻¹(I'×G×Λ') ⊇ S`, let `R = I'×Λ'` be a rectangular band, and let `G` act on `B × R` by
`^h(b,r) = (^h b, r)`. Define

```
Ψ(a,(i,g,λ)) = ((^{v_i}a, (i,λ)), v_i g u_λ).
```

Then, using `u_λ v_j = p_{λj}`,

```
Ψ(x)Ψ(y) = ((^{v_i}a · ^{v_i g u_λ v_j} b, (i,μ)), v_i g p_{λj} h u_μ) = Ψ(xy).
```

`Ψ` is injective because `^{v_i}` is a bijection. So `S ↪ (B×R) ⋊ G`, with `B×R ∈ V`.

**(ii)⇒(iii).** Let `D = {(i,g,λ) : i ∈ I', λ ∈ Λ'}`, where `I'` and `Λ'` are as above for
`C' = π(S)`.

* `C' ⊆ D`, and `D` is a subsemigroup.
* `(i,g,λ) ↦ (i, v_i g u_λ, λ)` is an isomorphism of `D` onto the rectangular group `I'×G×Λ'`,
  whose product is `(i,g,λ)(j,h,μ) = (i,gh,μ)`.

Transport the action and use these coordinates. Then `S ⊆ B ⊙* D`, since inverses in `D` are
inverses in `C`.

For `i ∈ I'`:

* `φ_{(i,1,μ)}φ_{(i,1,ν)} = φ_{(i,1,ν)}`.
* So all `φ_{(i,1,μ)}` are idempotent endomorphisms with one common image `B_i = Fix φ_{(i,1,μ)}`.
* So `B ⊙* D = {(a,(i,g,λ)) : a ∈ B_i}`.

Fix `e₀ = (i₀,1,λ₀)`. Then `^g b := φ_{(i₀,g,λ₀)}(b)` is an action of `G` on the band `B_{i₀}` by
automorphisms, and `φ_{e₀} = id` there. Define

```
Ψ(a,(i,g,λ)) = ((φ_{e₀}(a), (i,λ)), g) ∈ (B_{i₀} × R) ⋊ G.
```

For `b ∈ B_j`,

```
φ_{e₀}φ_{(i,g,λ)}(b) = φ_{(i₀,g,λ)}(b) = φ_{(i₀,g,λ₀)}φ_{(j,1,λ)}(b) = φ_{(i₀,g,λ₀)}(b),
```

so `Ψ((a,x)(b,y)) = Ψ(a,x)Ψ(b,y)`.

`Ψ` is injective because `φ_{(i,1,λ₀)}φ_{e₀} = φ_{(i,1,λ₀)}` is the identity on `B_i`. Finally,
`B_{i₀}×R ∈ V`. ∎

**Corollary (Q_orth).** Since `RB ⊆ L(ReB)` and Lemma 1 holds, the orthodox part of Problem 1, in
reading (P) or (R), is equivalent to:

> **Q_orth.** Does every E-unitary orthodox semigroup whose band is locally regular embed in a
> semidirect product of a locally regular band by a group?

## 4. Locally regular bands

**Lemma 4 (criterion).** `B` is locally regular iff for all `a ≤ w` and all `x, y`:
`a x w y a = a x a y a`.

This is immediate from `a, wxw, wyw ∈ wBw` together with `aw = wa = a`.

**Lemma 5.** Let `e` be a band element. If `eBe` has at most two D-classes, then `eBe` is regular.
In particular, every band with at most two D-classes is locally regular. More generally, `B` is
locally regular whenever every element of its structure semilattice has at most one element
strictly below it.

*Proof.* Write `M = eBe = {e} ∪ K`, where `K` is a rectangular-band ideal and `e` is the identity of
`M`. Check `a u v a = a u a v a` for `a, u, v ∈ M`:

* If `a = e`, both sides equal `uv`.
* If `a ∈ K`, then `awa = a` for all `w ∈ M`, by rectangularity and `aea = a`. So both sides
  equal `a`. ∎

**Example E5.** The band `E5` on `{0,…,4}` has the following table:

| · | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 | 0 | 1 | 4 | 3 | 4 |
| 1 | 0 | 1 | 3 | 3 | 4 |
| 2 | 2 | 2 | 2 | 2 | 2 |
| 3 | 3 | 3 | 3 | 3 | 3 |
| 4 | 4 | 4 | 4 | 4 | 4 |

Its D-classes are `{0,1}` (a right-zero band) and `{2,3,4}` (a left-zero band, and an ideal).

* `E5` is locally regular by Lemma 5.
* It is not regular: `0·1·2·0 = 3 ≠ 4 = 0·1·0·2·0`.
* `L` is a congruence on `E5`, so `E5` is left semiregular.
* `R` is not a congruence on `E5`.
* `E5` with an identity adjoined is still left semiregular but not locally regular. Hence
  `LSRB ⊄ L(ReB)`, and Billhardt's left-semiregular counterexample does not answer Problem 1
  automatically.
* No locally regular non-regular band has order ≤ 4. The 604 labelled bands of order 4 were
  enumerated exhaustively, and a SAT search agrees.
* `FB(3)`, the free band on 3 generators (159 elements), is locally regular. It is neither regular
  nor left or right semiregular.

All of these are computed in `work/check_band_facts.py` (log: `evidence/check_band_facts.log`).

Hence `ReB ⊊ L(ReB)`. Szendrei's regular-band theorem does not settle Q_orth.

## 5. Theorem B (regular band, in particular monoids)

*Cited theorem* (Szendrei 1987, as stated in the survey arXiv:1909.05280, §5.1, which I opened):
an E-unitary orthodox semigroup whose band is regular embeds in a semidirect product of a regular
band by a group.

**Theorem B.** Let `S` be weakly E-unitary and orthodox, with `E(S)` regular. Then `S` satisfies
Problem 1 in both readings. In particular every weakly E-unitary, locally r-orthodox **monoid**
does.

*Proof.*

1. By Lemma 1, `S` is E-unitary.
2. The cited theorem gives an embedding `S ↪ B ⋊ G` with `B` regular, hence locally regular.
3. `B ⋊ G = B ⊙ G = B ⊙* G`, as in the proof of Theorem A.

For a monoid, `1S1 = S`, so local r-orthodoxy says that `S` is orthodox with a regular band. ∎

The result is only as reliable as the cited theorem. I could not open the 1987 paper or Grillet's
book.

## 6. Theorem C (bands with at most two D-classes)

**Theorem C.** Let `S` be an E-unitary orthodox semigroup whose band `E` has at most two
D-classes, and let `G = S/σ`. Then `S` embeds in `B0^G ⋊ G`, where `B0` is a band with at most
two D-classes, so `B0` and `B0^G` are locally regular. Hence every weakly E-unitary orthodox
semigroup whose band has at most two D-classes satisfies Problem 1 in all readings.

*One D-class.* Then `S` is a rectangular group `R × G'`, and `G' ≅ G` because σ is injective on
H-classes and surjective. It embeds in `R ⋊ G`, with `G` acting trivially. Take `B0 = R` and
`F(g,(r,h)) = r`.

*Two D-classes.* Write `T` for the top class and `D` for the bottom class, which is an ideal of `E`.

**Step 1 (S is a union of two rectangular groups).**

*(a) `T` and `D` lie in different D-classes of `S`.* Suppose `aa' = e ∈ T` and `a'a = d ∈ D`.

* `dEd = {d}`, since `D` is a rectangular ideal.
* `x ↦ axa'` maps `dEd` onto `eEe`: for `f ∈ eEe`, `f = a(a'fa)a'` with `a'fa ∈ dEd`.
* So `eEe = {e}`.
* But `ede ∈ eEe ∩ D` and `ede ≠ e`, a contradiction.

So `J_T := D_S(T)` and `J_D := D_S(D)` partition `S`, with `J_T ∩ E = T` and `J_D ∩ E = D`.

*(b) `J_D` is an ideal.* Let `x ∈ J_D` and `s ∈ S`, and take `(sx)' = x's'`, which is an inverse
because `S` is orthodox. Then `(sx)(sx)' = s(xx')s' = s d₁ s'`, where `d₁ := s's·xx'·s's ∈ D`
(`D` is an ideal of `E`). The map `y ↦ sys'` is an isomorphism `s'sEs's → ss'Ess'` sending `s's`
to `ss'`.

* *Case `s's ∈ D`.* Then `s'sEs's = {s's}` and `ss'Ess' = {ss'}`, and `ss' ∈ D` by (a). So
  `s d₁ s' = ss' ∈ D`.
* *Case `s's ∈ T`.* Then `d₁ ≠ s's`, and `s'sEs's = {s's} ∪ K` with `K = D ∩ s'sEs's` its ideal of
  non-identity elements. By (a), `ss' ∈ T`, so the image of `K` is the non-identity part of
  `ss'Ess'`, which is `D ∩ ss'Ess'`. Hence `s d₁ s' ∈ D`.

In both cases `sx ∈ J_D`. The case `xs` is dual: use `(xs)'(xs) = s'(x'x)s`.

*(c) `J_T` is a subsemigroup.* Let `x, y ∈ J_T`, and choose inverses `x'` and `y'`. Then
`x'x, yy' ∈ T`, and `T` is a rectangular band, so `x'x·yy'·x'x = x'x`. Hence

```
(xy)(y'x') = x·yy'·x' = x·(x'x·yy'·x'x)·x' = x·x'x·x' = xx'.
```

So `xx' ≤_R xy ≤_R x R xx'`, which gives `xy R xx'` and `xy ∈ J_T`.

*(d) Both are rectangular groups.* Each of `J_T` and `J_D` is a regular semigroup whose idempotents
form one rectangular band. Such a semigroup is bisimple with primitive idempotents, hence
completely simple; being orthodox, it is a rectangular group.

By Lemma 1 (σ ∩ H = Δ) the group coordinates can be taken in `G`, with `σ` equal to the
group-coordinate projection:

* `J_T = I₁ × H₁ × Λ₁`, where `H₁ ≤ G`;
* `J_D = I₂ × H₂ × Λ₂`.

`σ(J_T)σ(J_D) ⊆ σ(J_D)` gives `H₁ ⊆ H₂`, and surjectivity of σ gives `H₂ = G`.

**Step 2 (cross products).** For `x = (r,h,λ) ∈ J_T` and `z = (i,k,j) ∈ J_D`:

```
xz = (Φ_x(i), hk, j),      zx = (i, kh, Ψ_x(j)).
```

Here `Φ : J_T → End(I₂)` is a homomorphism and `Ψ : J_T → End(Λ₂)` an anti-homomorphism.

* The column of `xz` is `j`: compare `z'(xz)` and `(z'x)z` in `J_D`.
* The row of `xz` depends only on `x` and `i`: compare `(xz)z'` and `x(zz')`.
* Associativity gives `Φ_{xx'} = Φ_xΦ_{x'}`.

**Step 3 (normal form).** Put `φ_{rλ} = Φ_{(r,1,λ)}`. These satisfy (F):
`φ_{rλ'} = φ_{rλ}φ_{r'λ'}`. Consequently:

* `Im φ_{rλ} = J_r` does not depend on `λ`.
* `p_λ := φ_{r₀λ}` are retractions onto `J := J_{r₀}`.
* `π_r := φ_{rλ}|_J : J → J_r` is a bijection that does not depend on `λ`.
* `p_λπ_r = id_J`.
* `Φ_{(r₀,h,λ₀)}|_J =: σ_h` defines a homomorphism `H₁ → Sym(J)`.

Writing `(r,h,λ) = (r,1,λ₀)(r₀,h,λ₀)(r₀,1,λ)` gives

```
Φ_{(r,h,λ)} = π_r ∘ σ_h ∘ p_λ.
```

Dually, `Ψ_{(r,h,λ)} = π'_λ ∘ σ'_h ∘ p'_r`, with `p'_rπ'_λ = id_{J'}` and `σ'` an
anti-homomorphism.

**Step 4 (the band `B0`).** Fix a left transversal, writing each `a ∈ G` as `a = t_a k_a` with
`k_a ∈ H₁`. Then `k_{ah} = k_a h` for `h ∈ H₁`.

`B0` has:

* top D-class `(I₁×G) × (Λ₁×G)`, a rectangular band;
* bottom D-class `(I₂×G) × (Λ₂×G)`, a rectangular band.

For a top element `x = ((r,a),(λ,b))`, the action on a bottom row `(i,c)` and a bottom column
`(j,c)` is

```
x·((i,c),·) has row  φ^0_x(i,c) = π^0_{(r,a)}(p^0_{(λ,b)}(i,c)),
     p^0_{(λ,b)}(i,c) = σ_{k_c}(p_λ(i)) ∈ J,
     π^0_{(r,a)}(y)    = (π_r(σ_{k_a}⁻¹ y), a),

(·,(j,c))·x has col  ψ^0_x(j,c) = π'^0_{(λ,b)}(p'^0_{(r,a)}(j,c)),
     p'^0_{(r,a)}(j,c) = σ'_{k_c}⁻¹(p'_r(j)) ∈ J',
     π'^0_{(λ,b)}(y)   = (π'_λ(σ'_{k_b} y), b).
```

Products inside a D-class are rectangular.

A 2-chain structure `B = T ∪ D` with `xz = (φ_x(i), j)` and `zx = (i, ψ_x(j))` is a band iff:

* (F) `φ_{(r,λ')} = φ_{(r,λ)}φ_{(r',λ')}`, and
* (G) `ψ_{(r,λ')} = ψ_{(r',λ')}ψ_{(r,λ)}`.

*Lemma 6 (2-chain model).* Let `T = I_t × L_t` and `D = I_b × L_b` be rectangular bands and put
`B = T ⊔ D`, multiplied rectangularly inside `T` and inside `D`, and across levels by
`xz = (φ_x(i), j)` and `zx = (i, ψ_x(j))` for `x ∈ T`, `z = (i,j) ∈ D`. Then `B` is a band iff
(F) and (G) hold.

*Proof.* Idempotency is clear. The associativity cases are:

* `(xx')z = x(x'z)`: this is (F).
* `z(xx') = (zx)x'`: this is (G).
* `(xz)x' = x(zx')`: both sides are `(φ_x(i), ψ_{x'}(j))`.
* All cases with two or three factors from `D`: these hold automatically because `D` is
  rectangular. ∎

Any maps of the form `π_ρ∘p_μ` with `p_μπ_ρ = id` satisfy (F), because
`π_ρ p_μ π_{ρ'} p_{μ'} = π_ρ p_{μ'}`; dually they satisfy (G). Here

```
p^0π^0 = σ_{k_a}p_λπ_rσ_{k_a}⁻¹ = id.
```

So `B0` is a band with two D-classes.

**Step 5 (the functor).** Put

```
F(g,(r,h,λ)) = ((r,g),(λ,gh)),      F(g,(i,k,j)) = ((i,g),(j,gk)).
```

Products inside one level are rectangular, so the functor law holds there. For top·bottom, using
`k_{gh} = k_g h`:

```
row of F(g,x)F(gh,z) = (π_r σ_{k_g}⁻¹σ_{k_gh} p_λ(i), g) = (π_rσ_hp_λ(i), g) = (Φ_x(i), g),
```

which is the row of `F(g,xz)`. The columns agree, being `(j, ghk)`. Bottom·top is dual, using
`σ'_{k_{gk}h} = σ'_hσ'_{k_{gk}}`.

Faithfulness holds because `F(1,s)` recovers all coordinates of `s`. Lemma 3 now gives
`S ↪ B0^G ⋊ G`, and `B0^G ∈ L(ReB)` by Lemma 5. ∎

**Remark C.1 (relation to Billhardt–Szendrei 1995).** In the setting of Theorem C, `S` is E-unitary
and has property (R) of [BS95, Prop. 3.3]: every σ-class `g ≠ 1` contains `r_g` with
`s r_g s = s` for all `s ∈ σ⁻¹(g⁻¹)`.

* If `g ∈ H₁`, take `r_g = (r₀, g, λ₀) ∈ J_T`. For top `s`, `s r_g s = s` is rectangular-group
  multiplication. For bottom `s = (i, g⁻¹, j)`, `s r_g = (i, 1, Ψ_{r_g}(j))` and
  `(s r_g)s = (i, g⁻¹, j) = s`.
* If `g ∉ H₁`, every element of `σ⁻¹(g⁻¹)` is a bottom element, and any `r_g ∈ J_D ∩ σ⁻¹(g)`
  works.

So `S` is quasi-F-orthodox [BS95, Prop. 3.3], and BS95 Thm 4.1 already embeds it in *some*
band ⋊ group. Problem 1 needs the band to be locally regular. That follows from BS95 Thm 4.2
(band in `var(E)`) if `S` is generalized F-orthodox, as the reviewer deduced
(`evidence/codex_review.md`); I have not checked that deduction. Theorem C proves the locally
regular conclusion directly.

**Machine checks of Theorem C** (`work/check_two_chain_theorem.py`,
`work/check_two_chain_generic.py`) verify, by brute force:

* the semigroup axioms for `S`, E-unitarity and the two D-classes;
* that `B0` is a locally regular band;
* the functor law, and that `S → B0^G ⋊ G` is an injective homomorphism.

The generic checker also verifies the normal form of Steps 2–3 on its inputs.

Inputs:

* 350 randomly generated instances with groups `Z1, Z2, Z3, Z4, Z2×Z2, S3`: 200 unrestricted (11
  with non-regular `E`) and 150 forced to have non-regular `E` (99 with non-trivial actions σ,
  σ′). The generator builds these from the normal-form data, so they test the construction, not
  the necessity of the normal form.
* 7 Z2-graded semigroups found by the generic SAT enumerator (`work/enum_extensions.py`), which
  does not assume the normal form. These are all Z2-graded extensions, up to isomorphism, with
  the given numbers of odd elements:
  - `E5` with 3 or 5 odd elements;
  - `E_A` with 4 or 6;
  - `E_C` with 6.

  The enumerator ran to exhaustion, since the SAT solver became UNSAT, in each listed case. The
  `E_C` case with 8 odd elements timed out and is excluded.

Logs are in `evidence/`.

## 7. Negative results on simple obstructions

Let `S ⊆ B ⋊ G` with `φ(x) = (β(x), γ(x))`, and write `S_g = γ⁻¹(g)`.

* For `s ∈ S_g`, `t ∈ S_{g⁻¹}` and any inverses `s'`, `t'`, Lemma 2 gives

  ```
  β(st) = β(ss')·^gβ(s's·tt')·β(t't).
  ```

* For `s, t ∈ S_g` with `s's D_E t't`, let `α_s : s'sEs's → ss'Ess'` be `f ↦ sfs'`, and let
  `θ_{e,f} : fEf → eEe` be `x ↦ exe` for `e D_E f`. Then Lemma 2 gives
  `α_t = θ_{tt',ss'} ∘ α_s ∘ θ_{s's,t't}`.

These yield two necessary conditions:

* **(C2)** Let `s, s₁ ∈ S_g` and `t, t₁ ∈ S_{g⁻¹}` (same σ-classes), with inverses
  `s', s₁*, t', t₁*`. If `ss' = s₁s₁*`, `t't = t₁*t₁` and `s's·tt' = s₁*s₁·t₁t₁*`, then
  `st = s₁t₁`.
* **(C3)** Let `s, t ∈ S_g` (same σ-class), with inverses `s', t'`. If `p := s's D_E t't =: q`,
  then `q(t's)q = q`.

Both hold in **every** E-unitary orthodox semigroup, and the σ-hypotheses are needed. In the group
`C₂ = {1, g}`, the choices `s = s₁ = t = 1`, `t₁ = g` break (C2) without them, and `s = 1`,
`t = g` break (C3).

*(C2).* Write `p = s's`, `p₁ = s₁*s₁`, `q = tt'`, `q₁ = t₁t₁*`, and put `u = s's₁`,
`v = t₁t'`. Both are idempotents (σ-trivial).

* Using `ss' = s₁s₁*`: `s₁ = ss's₁ = su`.
* Using `t't = t₁*t₁`: `t₁ = t₁t't = vt`.
* `pu = u` and `u·(s₁*s) = s'(ss')s = p`, so `u R p`.
* `up₁ = u` and `(s₁*s)·u = s₁*(ss')s₁ = p₁`, so `u L p₁`.
* In a band, `R_p ∩ L_{p₁} = {pp₁}`, so `u = pp₁`. Likewise `v = q₁q`.

Hence `s₁t₁ = s·pp₁q₁q·t = s·p(pq)q·t = s(pq)t = st`, using `p₁q₁ = pq`.

*(C3).* Since `qt' = t'tt' = t'`, we have `q(t's)q = t'(sq)`.

* *`ss' D_E tt'`.* `a := st'` and `b := ts'` are idempotents (σ-trivial), and
  `ab = s(t't)s' = s·pqp·s' = ss'` (using `s = sp`, `s' = ps'`, `pqp = p`). Likewise `ba = tt'`.
  In a band `ab D ba`.
* Green's lemma, with `pq ∈ R_p ∩ L_q` and `s ∈ L_p`, gives `sq ∈ R_s ∩ L_q`.
* `L_{t'} ∩ R_{sq} = L_{tt'} ∩ R_{ss'}` contains the idempotent `ss'·tt'`.
* By Clifford–Miller, `t'(sq) ∈ R_{t'} ∩ L_{sq} = H_q`.
* `σ(t'sq) = 1`, so `t'(sq)` is an idempotent of `H_q`, hence equal to `q`.

SAT searches over **Z2-graded** semigroups `S = E ⊔ A` (`E` a band, `A` the odd part), on the
exact grids `(|E|,|A|) ∈ {(3,3),(4,4),(5,4),(6,4)}` for (C2) and (C3) (so `|S| ≤ 10`), and
`{(3,3),(4,3),(5,3)}` for the walk identity (I1) (so `|S| ≤ 8`), found no violation
(`evidence/sat_search_*.log`). These are not searches over all semigroups of those orders.

This rules out (C2), (C3) and (I1) as obstructions; it does not rule out other local obstructions.
Independently, Theorem C shows that a counterexample to Q_orth needs a band with at least three
D-classes, for every group.

**Proposition F (finite verification of Q_orth, group Z2, `|E| ≤ 6`).** Let `S` be an E-unitary
orthodox semigroup with `S/σ ≅ Z2` whose band `E` is locally regular and has at most 6 elements.
Then `S` embeds in `B ⋊ Z2` with `B` a locally regular band.

*Proof (computer-assisted).* Cases on `E`:

* *`E` regular.* Theorem B.
* *`E` non-regular with at most two D-classes.* Theorem C.
* *`E` non-regular with at least three D-classes.*
  1. *The bands.* SAT enumeration of all labelled locally regular non-regular bands of orders 5 and
     6 (`work/enum_locreg_bands.py`, `evidence/enum_locreg_bands.log`):
     - order ≤ 4: none (§4);
     - order 5: 120 labelled, all with two D-classes;
     - order 6: 9360 labelled in total. Of these, 5760 (per the second reviewer's count) have at
       least three D-classes. They form exactly 10 isomorphism classes, listed in
       `evidence/ext/locreg6_3D.json`.
  2. *The number of odd elements.* For these bands, `D_S` restricted to `E` equals `D_E`. In
     general `D_S` on `E` can be coarser: in `B ⋊ G`, `(a,1)` is D-related to `(^g a, 1)`. But
     D_S-related idempotents have isomorphic local submonoids, via `x ↦ a'xa`, and for each of the
     10 bands the three D_E-classes have pairwise non-isomorphic local submonoids
     (`work/odd_bound_3d.py`, `evidence/odd_bound_3d.log`).
     - *Every H-class of `S` contains an idempotent.* For `s ∈ S` and `s' ∈ V(s)`, `e = ss'` and
       `f = s's` lie in one rectangular D_E-class, so `ef` is an idempotent H-related to `s`.
     - Hence `S` has exactly `|E|` H-classes.
     - σ is injective on H-classes (Lemma 1), so `|A| ≤ |E| = 6`.
  3. *The extensions.* `work/enum_extensions.py` enumerated all Z2-graded extensions with
     `|A| = 1,…,6`, exhaustively (every run ends with an UNSAT call, `exhausted=True`): 48
     semigroups up to isomorphism.
  4. *The embeddings.* For each of the 48, `work/embed_generic_sat.py` found a band `B` of order
     ≤ 7, an involutive automorphism and a map giving an embedding `S ↪ B ⋊ Z2`. The
     certificate was re-checked by `work/verify_embedding_certificate.py`, which also confirms
     that `B` is locally regular (`evidence/pipeline_3d.log`,
     `evidence/pipeline_3d_certificates.log`). ∎

Trust base: the completeness claims rest on CaDiCaL's UNSAT answers, which are not
proof-logged. The embeddings themselves are independently verified certificates.

*Correction of a first run.* The first version of `embed_generic_sat.py` demanded that `β` be
injective on all of `S`, but only `x ↦ (β(x), σ(x))` needs to be injective. That made spurious
"no embedding with |B| ≤ 10" outputs for several extensions (archived in
`evidence/ext/archive/3d_first_run_overstrict_injectivity/`). After the fix, all 48 embed.

## 8. What remains open

No resolution of Problem 1 has been located. Within the orthodox members it is Q_orth for bands
with at least three D-classes. The non-orthodox members are those whose local submonoids are
orthodox but `S` itself is not; the locally inverse ones among them are settled by
Billhardt–Szendrei. [Theorem X](hmz-lean-20261014/xi-purity.md) now proves, in a written
parent-audited argument, that ξ is idempotent pure for every **finite** member of P1's class
(indeed for every finite weakly E-unitary locally orthodox regular semigroup). This theorem is
not Lean-checked. The remaining issue is constructing the required embedding from the pure
completely simple quotient; purity alone does not suffice. For infinite semigroups lacking a
completely simple ideal, the ξ-purity question also remains unresolved.
