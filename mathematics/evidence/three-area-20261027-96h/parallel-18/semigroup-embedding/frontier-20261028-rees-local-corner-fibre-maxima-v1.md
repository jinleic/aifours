# Regular Rees corners embed in actual base corners; inverse-base fibres have maxima

**NEW WRITTEN AUTHOR CANDIDATE; unreviewed and unadopted.** Native prewrite observation **Wed Oct 28 18:09:48 PDT 2026**. This extends the reverse-fibre WE-condition theorem `frontier-20261028-rees-reverse-fibre-weu-v1.md`, SHA `96b34ec43125dabe1e9cc33cdc7055c37b0933a1f5c81a424913b5dd5230f52b`, to a complete local-r source test when the base idempotents form a regular band, and gives an exact inverse-semigroup interpretation. No novelty or general original embedding is claimed.

## 1. The general local-corner embedding

Let A be ANY semigroup, let I,Λ be nonempty, P an arbitrary A-valued matrix, and let the FULL Rees semigroup `S=M[A;I,Λ;P]` be **regular**. Take any actual idempotent `e=(i,a,λ)` of S and put `p=p_(λ,i)`. Then `a p a=a` and `f=a p` is an actual idempotent of A.

Every x in eSe has row i and column λ; write x=(i,b,λ). Because e is the identity of its actual local monoid,

`a p b=b=b p a`.                                            (1)

Define

`Φ_e:eSe→fAf`,     `Φ_e(i,b,λ)=b p`.

The source product at those fixed indices is `(i,b,λ)(i,c,λ)=(i,b p c,λ)`, so Φ_e respects multiplication. Its image lies in fAf: `f(b p)=(a p b)p=b p` and `(b p)f=(b p a)p=b p`. It is injective: if b p=c p, multiply on the right by the actual a and use (1) to obtain b=c. Thus Φ_e is a genuine embedding of the ENTIRE local monoid into the actual base corner fAf. No inverse of p, cancellation, common identity, finite index set or chosen source representation is used.

The source local eSe is regular because S is regular: for x=exe and x'∈V_S(x), the actual element ex'e is a mutual inverse in eSe. This fact applies to every local idempotent, including singleton and nonunital global cases.

## 2. Universal local-r and local-inverse consequences

Assume E(A) is a **regular band**, i.e. is closed under product and obeys `x y x z x=x y z x`. This DOES NOT require A itself to be regular or to have an identity. For any actual source local corner, its Φ_e image is a regular subsemigroup of A. Its idempotents are contained in E(A); the product of two such idempotents is an idempotent in A and stays in the image. Hence its idempotents form a band. As a subband of E(A), they satisfy the regular-band identity. Injectivity of Φ_e transports both facts back to eSe.

Therefore **every regular FULL Rees semigroup over an A with regular-band E(A) is locally r-orthodox**, for arbitrary P. No p is assumed a unit, idempotent, tight or invertible.

If A is an inverse semigroup, each Φ_e image is a regular subsemigroup of an inverse semigroup. Every element has a mutual inverse within the image, and that inverse must be the unique inverse in A; hence the image is inverse and so is eSe. Therefore every such regular Rees source over an inverse base is **locally inverse**. The uniqueness argument is internal to the image; it does not claim the whole Rees source is inverse or globally orthodox.

## 3. Complete original-class test for pure-group/regular-band bases

Assume in addition θ:A→G is an onto idempotent-pure group homomorphism. The preceding reverse-fibre theorem proves, for the FULL Rees source whether or not it is regular, the exact equivalence between the printed weak-E condition and

`a p_(λ,i) a=a` for EVERY λ,i and EVERY `a` with
`θ(a)=θ(p_(λ,i))^(-1)`.                                    (RF)

Combining that equivalence with §2 gives the following precise source characterization:

> If E(A) is a regular band and S is regular, then S is an original weakly E-unitary locally r-orthodox regular source **iff every actual P entry satisfies (RF)**.

The actor `r(i,a,λ)=(i,θ(a),λ)` is then an onto pure map to the completely simple Rees actor, and the actual syntactic actor is its pure τ-quotient as in the predecessor. This characterization pays only the **original source hypotheses**, not faithful canonical embedding. It makes no claim that regularity or (RF) can be dropped or that every original source has a Rees model over such an A.

For example, the earlier exact tight-sandwich theorem gives a sufficient host for some RF-good P; it is NOT assumed here. The remaining source-to-host problem is to decide whether arbitrary RF-good regular P admit an all-derivation separating V-band/action invariant, or to construct a genuine original-class obstruction.

## 4. In an inverse base, (RF) means the sandwich is the maximum of its group fibre

Let A be an inverse semigroup with onto idempotent-pure θ:A→G; no identity or finite group is assumed. Write x^{-1} for the unique inverse. For any p∈A with θ(p)=g:

**Lemma.** `(RF)` for p holds iff p is the greatest element of the natural partial order among all x with θ(x)=g.

**Forward.** For any such x put a=x^{-1}; then θ(a)=g^{-1}, and RF gives `a p a=a`. Both ap and pa are idempotent by θ-purity; idempotents commute in an inverse semigroup. Right-multiplying the equation by a^{-1} gives `(ap)(aa^{-1})=aa^{-1}`, hence

`(a^{-1}a)p = a^{-1}(ap)=a^{-1}(aa^{-1})(ap)=a^{-1}`.

Left-multiplying the equation by a^{-1} gives `(a^{-1}a)(pa)=a^{-1}a`; commuting those idempotents and multiplying by a^{-1} on the right gives `p(aa^{-1})=a^{-1}`. Thus x=a^{-1} has the printed natural-order witnesses

`x=(a^{-1}a)p=p(aa^{-1})`,

so x≤p.

**Reverse.** Let a satisfy θ(a)=g^{-1} and put x=a^{-1}. Maximality gives x≤p, so x=p f for some actual idempotent f. In an inverse semigroup, `x^{-1}x=f p^{-1}p f=f p^{-1}p` and `p x^{-1}x=p f p^{-1}p=p p^{-1}p f=p f=x`, since idempotents commute. Substituting x=a^{-1} into `x=p a x` and multiplying by a on the left and right gives `a=apa`. This establishes RF for every a.

Consequently, for an inverse base with a pure onto group quotient, the Rees source's WE-condition holds exactly when **each sandwich entry is the maximum of its own group fibre**. If that FULL Rees source is regular, §2 shows it is locally inverse and hence an original-class source. A fibre maximum need not be preserved by multiplying two maxima: the explicit finite control in `frontier-20261028-tight-subset-obstructions-v1.md`, SHA `3abb2c0f33f49edb606fe3188ad460df330bb1fe5b8b7c698c7dd582920a7f2e`, contains the three-element inverse submonoid `{1,z,p}` with p²=z<1, where p and1 are their fibre maxima. No global group-section homomorphism is silently inferred.

## 5. Exact finite checks and what they do not show

`frontier-20261028-rees-local-fibre-checker-v1.py`, SHA `0f4df82d01037f19b84f90d1e91df2e922d711be987eb1f39b08ccdff0613645`, was run at **Wed Oct 28 18:09:29 PDT 2026**, timeout60s, exit0. It imports the same author's pinned finite-base multiplication and exhaustively reports:

```text
RF_good_matrices=16 regular=7 nonregular=9
regular_sources_nonorthodox=4 nonlocally_inverse=7
PASS all regular source corners orthodox with regular idempotent bands
inverse_submonoid_size=3 theta_fibre_maxima=[(None, 1, 0), (None, 0, 1)]
PASS exact RF iff maximum in both group fibres for all inverse-submonoid elements
```

The seven regular cases are all original-class by the separately checked RF/WE-condition and now directly tested local-r corners; four have nonclosed global idempotents, all seven have a noninverse local corner. The nine nonregular matrices demonstrate why regularity remains a separate hypothesis. The inverse-base part checks all three elements and their actual natural-order witnesses, not a heuristic rank or approximate multiplication.

This is a same-author finite test of one base and its three-element inverse submonoid, not an independent verifier or proof of arbitrary semigroups. The source-class count is an exact fact of that finite experiment, not a complete classification of original sources.

## 6. Imports, remaining gap and review boundary

Section1–2 are direct semigroup calculations. Section3 explicitly uses the prior unreviewed reverse-fibre equivalence, which is fully written and separately identified. Section4 uses standard inverse-semigroup facts—unique mutual inverses, closure of idempotents and their commutativity—at exactly the displayed algebraic steps; no external embedding, F-inverse classification, groupoid construction or novelty claim is imported.

The all-variable class remains a **Rees-model subclass**. RF + regularity + regular-band E(A) proves the original source hypotheses, not faithful separation in B_q. The central remaining question is whether EVERY such original source has an actual same-q separating host, or whether an eligible P gives a genuine all-host collapse. No counterexample to the embedding question or universal positive solution has been supplied. Full proof/finite-witness/priority review remains required before adoption.
