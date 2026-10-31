# Rees sources over a locally regular-band-by-group base

**NEW AUTHOR WRITTEN SUCCESSOR with exact finite check; unreviewed/unadopted.** Native check-start observation **Wed Oct 28 19:05:56 PDT 2026**. The preceding `frontier-20261028-regular-band-base-rees-theorem-v1.md`, SHA `5c883d3fb81b68af93a9848b3fc0c58acb19766c169375787c18bff0cea4e8aa`, assumed its base band globally regular. Its actual proof only needs local regularity; this new note removes that restriction and does not edit the predecessor. The semigroup base remains A=B⋊G **without adjoining a new external identity**. This is not an all-original-source solution or novelty claim.

## 1. Theorem and exact scope

Let B be ANY nonempty locally regular band, G ANY group acting on B by automorphisms, and A=B⋊G. Define

`K(B)={p∈B : b p b=b for every b∈B}`.

Let I,Λ be nonempty, and P any full Λ×I matrix over A, with entries `P_(λ,i)=(p_(λ,i),q_(λ,i))`. Set `S=M[A;I,Λ;P]`.

**Theorem.** S is weakly E-unitary iff every `p_(λ,i)∈K(B)`. When this condition holds, S is automatically regular, locally r-orthodox and admits an explicit faithful physical host over the natural CS actor `r(i,(b,g),λ)=(i,g,λ)`. Under the named pure-CS actor-pushforward input in §5, the model transports to the ACTUAL q_τ; canonical κ_q is injective and both same-q R/L separation obligations hold.

The result allows B itself to fail global regularity. If K(B)=∅, the equivalence says that no such nonempty full-matrix S is weakly E-unitary. No top-D-class classification is assumed. Adding a fresh identity to a nonunital A, or treating arbitrary original sources, is outside this note.

## 2. Weak-E equivalence and regularity use only the band law

K is invariant under automorphisms. For a matrix entry `(p,q)`, arbitrary b∈B and `a=(b,q^(-1))`, the source `x=(i,a,λ)` has `x³=x²`: writing `t=q^(-1)·p`, its middle band coordinates are `b t b` for x² and `b t b t b=b t b` for x³. If `b t b≠b`, x² is an idempotent strictly below nonidempotent x. Thus weak E-unitarity forces p∈K. Conversely p∈K at every entry makes the natural CS actor pure by the same calculation; equality of natural order in the CS actor then implies weak E-unitarity.

Regularity likewise needs only K, not global regularity. Given s=(i,(b,g),λ), choose j,μ arbitrarily and write `P_(λ,j)=(p,q)`, `P_(μ,i)=(p',t)`. For

`x=(j,((gq)^(-1)·b, q^(-1)g^(-1)t^(-1)),μ)`,

both group and band products simplify to sxs=s, using `b (g·p)b=b` and `b (t^(-1)·p')b=b`. Replacing x by xsx yields a mutual inverse.

## 3. The evaluation band only needs local regularity of B

Assume the K condition and choose `z∈K(B)`. Form a full Rees semigroup T over the band B with rows I×G, columns Λ×G and sandwich

`H_((λ,t),(j,u)) = t^(-1)·p_(λ,j)` if `q_(λ,j)=t u^(-1)`, and z otherwise.

All H values lie in K; hence `b H b=b` for all b, so T is a band. For e=(row,a,col), let p=H_(col,row), d=ap. Then d is an idempotent of B. Every x=(row,b,col)∈eTe satisfies `b=a p b p a`. The map

`x ↦ b p`

is a homomorphism into dBd; it is injective because `b=(a p)(b p)a`. Moreover `bp=d(bp)d`. Local regularity of the BASE B says dBd is a regular band, and so is its subband. Thus eTe is regular for every e; T is locally regular even when B is not globally regular. This is the exact strengthened point.

Set `C=T^G` with left shifts `(α_wF)(k)=F(w^(-1)k)`. Products preserve the local-regular identity; no finite support is imposed.

## 4. Complete physical host law

For `s=(i,(b,g),λ)` set

`β_s(k)=((i,k), k^(-1)·b, (λ,g^(-1)k))`.

For `t=(j,(c,h),μ)`, `P_(λ,j)=(p,q)` and w=gq, the Rees sandwich inserted when multiplying β_s(k) by `(α_wβ_t)(k)` is `(k^(-1)g)·p`: the selector's two group labels are `g^(-1)k` and `(gq)^(-1)k`, whose quotient is q. The resulting middle is

`k^(-1)·(b (g·p) (gq·c))`,

and the column is `(μ,h^(-1)q^(-1)g^(-1)k)`, exactly β_(st)(k). Thus the physical law holds for all pairs in noncommutative group order. The natural actor supplies i,λ,g and β_s(1_G) supplies b, so the host is faithful.

S is regular by §2. Its local idempotents map into the identity of the corresponding local CS actor group and the appropriate regular band corner of C; injectivity reflects idempotent closure and the regular-band law. Therefore S is locally r-orthodox.

## 5. Actual q and exact finite evidence

The natural actor is onto and pure, so `τ_S=r^(-1)(τ_D)`. The named explicit pure onto-CS actor pushforward `frontier-20261028-pure-actor-finite-band-pushforward-v1.md`, SHA `abdfecbfb03b7931ad8dac0e7912f6c359279fe7afd47662a4f376942b2d9057`, produces a faithful physical model over ACTUAL q_τ with an added rectangular band factor. Local regularity survives the product. The canonical free-V-band universal map into that physical band makes κ_q injective and proves the scoped R/L separations. If this WRITTEN actor input fails independent review, retain §§1–4's faithful natural-actor result and mark the q/canonical clause **NR-PUSHFORWARD**.

`frontier-20261028-local-band-base-rees-checker-v1.py`, SHA `ff7775d9d1dcb6f305e29be2400f3cc87811ff19efd7f5259eb2538cfb37ce1e`, ran `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 19:05:56 PDT 2026**, exit0. Its base is the5-element locally regular but globally nonregular band from `frontier-20261028-local-band-four-term-countermodel-v1.md`, SHA `7be9d26f0941fc37728b7305dc9451c1b3586e442e87a5c976be13f2ad8dd72f`, with K={1,3} and a nontrivial involutory action. The source has40 elements, natural/actual actor8 and evaluation band T80.

```text
base=5 locally regular but globally nonregular; K=[1, 3] source=40 actor=8 T=80
PASS all80 T idempotence, associativity, local corners; all1600 source/actor/host laws and fibre injection
PASS regularity, WEU, local-r, actor purity and 41^2 contexts/source
CONTROL outside-K sandwich gives explicit s^3=s^2!=s
```

The sample exhausts the base and T band/corner identities, source laws and every41² actual/absent context per source element. It is a proper non-globally-regular instance, not an independent review of the symbolic theorem. No cross-model, human, formal/kernel or independent witness certification, novelty, added-identity-base or all-original-source conclusion is claimed.
