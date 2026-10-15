# A finite idempotent-purity reduction

Date: 2026-10-14 (PT).

**Trust boundary:** this is a complete written coordinate argument derived during the HMZ run by its integration owner and **audited step by step by the parent agent**. The parent found no gap in the coordinate proof, finite corollary, or hypothesis-omission control. It is **not Lean-checked**, is not a novelty claim, and is separate from the actor's `Formal.lean` and frozen full-goal acceptance. The parent audit is not the HMZ reviewer's terminal verdict. It does not construct an embedding in a Pastijn or restricted product.

## Statement

**Theorem X (completely simple ideal).** Let `S` be a regular semigroup with a nonempty completely simple ideal `K`. Suppose every local monoid `eSe`, for `e ∈ E(S)`, is orthodox. Then there is a surjective homomorphism

`q : S → C`

to a completely simple semigroup `C`, whose restriction to `K` is idempotent pure. If, in addition, `S` is weakly E-unitary in the book's sense, then `q` itself is idempotent pure.

**Finite corollary.** Every nonempty finite, weakly E-unitary, locally orthodox regular semigroup has an idempotent-pure completely simple quotient. Consequently its least completely simple congruence `ξ` is idempotent pure. In particular this applies to every finite member of the book's locally r-orthodox class.

The corollary uses the standard fact that the minimal ideal of a nonempty finite semigroup is completely simple. The one-element zero ideal is allowed: the corresponding conclusion that `S` is a band also follows immediately from `0 ≤ s` and weak E-unitarity.

The hypotheses require **local orthodoxy**, not the stronger regular-band identity in each local monoid. They do not assert that all `S` are orthodox or completely regular.

## 1. Normalized coordinates and linked translations

Write the completely simple ideal in normalized Rees coordinates

`K = M[G; I, Λ; P]`,

with nonempty index sets, distinguished `i₀ ∈ I`, `λ₀ ∈ Λ`, and

`p_{λ,i₀} = p_{λ₀,i} = 1` for every `λ,i`.

Multiplication is `(i,g,λ)(j,h,μ) = (i,g p_{λ,j} h,μ)`. All maps below are left maps; composition acts rightmost first.

Multiplication by `s ∈ S` on this ideal gives maps `α_s : I → I`, `β_s : Λ → Λ` and group labels `γ_s(i), δ_s(λ)` such that

```
s(i,g,λ) = (α_s(i), γ_s(i)g, λ),
(i,g,λ)s = (i, gδ_s(λ), β_s(λ)).                     (1)
```

Here the same `s` acts on both sides. These formulas follow directly by factoring through normalized matrix units. For example `(i,1,λ₀)(i₀,1,λ₀)=(i,1,λ₀)`, so `s(i,1,λ₀)` has last coordinate `λ₀`; define its first two coordinates as `α_s(i),γ_s(i)`. Then multiply by `(i₀,g,λ)` to obtain the left formula in (1). The right formula is dual.

Associativity of `(k s)l = k(s l)` gives the linking equation

```
p_{λ,α_s(i)} γ_s(i) = δ_s(λ) p_{β_s(λ),i}.          (2)
```

Also

`α_{st}=α_s∘α_t` and `β_{st}=β_t∘β_s`.             (3)

Put

`a_s=α_s(i₀)`, `b_s=β_s(λ₀)`, `c_s=γ_s(i₀)=δ_s(λ₀)`.

The equality of the last two expressions follows from (2) at `(λ₀,i₀)`. Evaluating (2) first at `λ₀` and then at `i₀` yields the particularly useful identities, valid for **every** `s`:

```
γ_s(i) = c_s p_{b_s,i},
δ_s(λ) = p_{λ,a_s} c_s.                            (4)
```

No commutativity of `G` is used; multiplication order in all formulas matters.

## 2. What local orthodoxy forces for an idempotent

Fix `e²=e`. Write `α=α_e`, `β=β_e`, `γ=γ_e`, `δ=δ_e`, and set

`A=Im α`, `L=Im β`.

Since `e²=e`, we have `α²=α`, `β²=β`, and

`γ(a)=1` for `a∈A`, `δ(l)=1` for `l∈L`.             (5)

Indeed applying the left formula twice gives `γ(α(i))γ(i)=γ(i)`, and group cancellation gives `γ(α(i))=1`. The right argument is identical.

The local ideal `eKe` is exactly `A×G×L`. To see surjectivity, choose preimages of an arbitrary `a∈A` and `l∈L`; as the middle group variable in `k` varies, the middle variable in `eke` varies over all `G`. Thus `eKe` is a Rees matrix semigroup with restricted sandwich matrix `P|_{L×A}`.

It is a subsemigroup of the orthodox monoid `eSe`, so its idempotents multiply to idempotents. A Rees matrix semigroup is orthodox precisely when its sandwich matrix is of group rank one. Explicitly, fix `a∈A`, `l∈L`; for every `a'∈A`, `l'∈L`,

```
p_{l',a'} = p_{l',a} p_{l,a}^{-1} p_{l,a'}.         (6)
```

For completeness, the idempotent in coordinate `(i,λ)` is `(i,p_{λ,i}^{-1},λ)`. Closure of these idempotents under multiplication gives

`p_{λ,i}^{-1} p_{λ,j} p_{μ,j}^{-1} = p_{μ,i}^{-1}`;

multiplying on the appropriate sides gives (6), and the converse follows by substitution.

Because `a'∈A`, equation (2) and (5) give

`p_{λ,a'} = δ(λ)p_{β(λ),a'}`.

Use (6), and then (2) for `a`, to obtain, for every `λ∈Λ`,

```
p_{λ,a'}
 = δ(λ)p_{β(λ),a}p_{l,a}^{-1}p_{l,a'}
 = p_{λ,a}p_{l,a}^{-1}p_{l,a'}.                    (7)
```

At `λ=λ₀`, normalization in (7) gives `p_{l,a'}=p_{l,a}`. Substitution back into (7) shows

```
p_{λ,a'}=p_{λ,a}  for every λ∈Λ and a'∈A.         (8)
```

Thus **all columns indexed by `Im α_e` are equal as full columns of `P`**, not merely on the local submatrix.

The dual calculation is recorded explicitly. For `l'∈L`, (2) gives

`p_{l',i}=p_{l',α(i)}γ(i)`.

By (6) and (2) for `l`,

```
p_{l',i}
 = p_{l',a}p_{l,a}^{-1}p_{l,α(i)}γ(i)
 = p_{l',a}p_{l,a}^{-1}p_{l,i}.
```

At `i=i₀`, normalization gives `p_{l',a}=p_{l,a}`. Hence

```
p_{l',i}=p_{l,i}  for every i∈I and l'∈L.         (9)
```

So all rows indexed by `Im β_e` are equal as full rows.

## 3. The reduced completely simple quotient of the ideal

Declare `i≈j` if columns `i,j` of `P` agree on all `Λ`; declare `λ≃μ` if rows `λ,μ` agree on all `I`. Set

`Ī=I/≈`, `Λ̄=Λ/≃`, `p̄_[λ],[i]=p_{λ,i}`.

Equality of full rows and columns makes `P̄` well defined. Define

`C = M[G; Ī, Λ̄; P̄]`.

The map `q_K(i,g,λ)=([i],g,[λ])` is a surjective homomorphism. It is idempotent pure because

`(i,g,λ)²=(i,g,λ) ⇔ g=p_{λ,i}^{-1}`,

and the criterion is identical after applying `q_K`.

Every multiplication map from `S` descends to the quotient index sets. If columns `i,j` coincide, equation (2) has equal right-hand sides for them. At `λ₀` this implies `γ_s(i)=γ_s(j)`, and cancellation then gives

`p_{λ,α_s(i)}=p_{λ,α_s(j)}` for all `λ`.

Thus `α_s` respects `≈`. If rows `λ,μ` coincide, (2) at `i₀` gives `δ_s(λ)=δ_s(μ)`, and (2) for arbitrary `i`, followed by cancellation, gives equality of rows `β_s(λ),β_s(μ)`. Thus `β_s` respects `≃`.

Write the descended maps as `ᾱ_s`, `β̄_s`. Equations (8) and (9) say that for every idempotent `e` these maps are constant.

Now use regularity. For `s∈S`, choose `t` with `sts=s`. Then `st` and `ts` are idempotents, and (3) gives

```
ᾱ_s = ᾱ_{st} ∘ ᾱ_s,
β̄_s = β̄_{ts} ∘ β̄_s.
```

Since the left factors on the right are constant, both `ᾱ_s` and `β̄_s` are constant. Their values are respectively `[a_s]` and `[b_s]`.

This is the only passage from idempotent elements to arbitrary elements; it does not assume that `S` is completely regular.

## 4. A completely simple quotient of all of S

Define

```
q(s) = ([a_s], c_s, [b_s]) ∈ C.                   (10)
```

This is a homomorphism. For the first coordinate, (3) gives

`[a_{st}]=[α_s(α_t(i₀))]=[a_s]`.

For the last, `[b_{st}]=[β_t(β_s(λ₀))]=[b_t]`. For the middle, calculate `st(i₀,1,λ₀)` using (1) twice and (4):

```
c_{st}=γ_s(a_t)c_t=c_s p_{b_s,a_t}c_t.
```

These are exactly the three coordinates of `q(s)q(t)` in `C`.

For `k=(i,g,λ)∈K`, direct Rees multiplication gives `a_k=i`, `b_k=λ`, `c_k=g`, hence `q|_K=q_K`. This proves surjectivity of `q` and idempotent purity on `K`.

An alternative interpretation is that all descended linked bitranslations of `C` induced by `S` are inner; formula (10) names the corresponding inner element. The direct coordinate proof above avoids relying on any unquoted theorem about translational hulls.

## 5. Weak E-unitarity gives purity on S

Suppose `q(s)` is idempotent. Put `a=a_s`, `b=b_s`, `c=c_s`. By the idempotent criterion in `C`,

`c=p_{b,a}^{-1}`.                                 (11)

The following two elements of the ideal are idempotent by normalization:

`f=(a,1,λ₀)`, `g=(i₀,1,b)`.

Using (1) and the definitions of `a,b,c`,

```
fs=(a,c,b)=sg.                                    (12)
```

Let `u=(a,c,b)`. Equation (11) says `u²=u`; equation (12) says `u≤s` in the exact natural order used in the book. Weak E-unitarity now implies `s²=s`. This proves idempotent purity of `q`.

Conversely, homomorphisms always send idempotents to idempotents, so this is the full equivalence `q(s)∈E(C) ⇔ s∈E(S)`.

## 6. Consequence for ξ and scope remaining

For finite `S`, let `ξ` denote its least completely simple congruence, as in the existing dossier. Since `S/ker q ≅ C` is completely simple, `ξ ⊆ ker q`. If `s ξ e` and `e²=e`, then `q(s)=q(e)` is idempotent, whence `s²=s`. Thus `ξ` is idempotent pure.

This written, parent-audited proof rules out a **finite** refutation of P1 based only on non-purity of `ξ`. It does **not** imply any of the following:

- that P1 holds, even for finite semigroups;
- that Q_orth holds for bands with three or more D-classes;
- that a quotient map `q` lifts to an embedding into a band/completely-simple product;
- that `S` has a completely simple ideal in the infinite case;
- that the result is new in the semigroup literature.

The precise remaining step after this reduction is an embedding theorem for the relevant idempotent-pure extensions of completely simple semigroups with the prescribed local regular-band constraints. The quotient itself is not such an embedding.

## 7. Hypothesis boundary / mathematical rejection control

Local orthodoxy cannot be discarded from Theorem X. Take

`K=M[C₂;{0,1},{0,1}; [[1,1],[1,h]]]`, with `h²=1`, `h≠1`,

and adjoin an identity to obtain `S=K¹`. This is regular and weakly E-unitary: elements of `K` cannot lie strictly above another element of `K` in its intrinsic natural order, and the newly adjoined identity is itself idempotent. More explicitly, if idempotent multipliers in `K¹` witness `u≤s∈K`, replace any multiplier equal to the adjoined identity by a local left/right identity of `s` in `K`, so the witness lies inside `K` and forces `u=s`.

Any surjective homomorphism from a monoid to a completely simple semigroup has a monoid as image; a completely simple monoid is a group. Every idempotent of `K` must therefore map to the group identity. The product of the idempotents `(0,1,0)` and `(1,h,1)` is `(0,h,1)`, which is not idempotent (its sandwich entry is `p_{1,0}=1`), but its image is the group identity. No such quotient is idempotent pure. Correspondingly, `S` is not locally orthodox at its identity.

This is an exact written counterexample to omission of the local-orthodoxy hypothesis, not an executed new finite search. The actor's separate Lean negative control has its own execution receipt.
