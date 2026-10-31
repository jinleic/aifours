# Full Rees sources over a regular-band-by-group base

**NEW AUTHOR WRITTEN CANDIDATE with exact finite check; unreviewed/unadopted.** Native check-start observation **Wed Oct 28 19:03:12 PDT 2026**. The band base in this note can have multiple D-classes and need not be rectangular. The theorem concerns A=B⋊G **without adjoining a new external identity**; it does NOT settle the latter extension or the original all-source problem. Its actual-q/canonical clause imports the named pure-actor pushforward.

## 1. Exact result and intrinsic sandwich set

Let B be ANY nonempty globally regular band, G ANY group acting on B by automorphisms, and `A=B⋊G`. Define the intrinsic set

`K(B)={p∈B : b p b=b for EVERY b∈B}`.

K may be empty; it is invariant under every automorphism of B. Let I,Λ be nonempty and P ANY full Λ×I matrix over A, writing `P_(λ,i)=(p_(λ,i),q_(λ,i))`. Set `S=M[A;I,Λ;P]` and natural actor `r(i,(b,g),λ)=(i,g,λ)` in `D=M[G;I,Λ;Q]`, `Q_(λ,i)=q_(λ,i)`.

**Theorem.** S is weakly E-unitary **iff** every band component `p_(λ,i)` lies in K(B). In that case S is automatically regular and locally r-orthodox and has an explicit faithful physical model over r with a locally regular band. Its actual-q/canonical κ is faithful, under the named pure-actor pushforward in §6.

The K condition is literal; no D-class classification, top element, finite semigroup or published band-structure theorem is assumed. In particular, if K is empty, the nonempty full P cannot satisfy the condition and S is not weakly E-unitary. The theorem does not say an arbitrary original semigroup is such a Rees source.

## 2. Weak-E characterization and automatic regularity

Fix a P entry `(p,q)`. For any b∈B let `a=(b,q^(-1))` and `x=(i,a,λ)` at that cell. Put t=q^(-1)·p. The A band component of `a P_(λ,i) a` is `b t b`; its group coordinate is still q^(-1). In every band,

`b t b t b = b t b`,

because bt is idempotent. Thus `x³=x²`. If `b t b≠b` then x² is an idempotent strictly below the nonidempotent x, contradicting weak E-unitarity. Hence weak E forces q^(-1)·p∈K(B), equivalently p∈K(B) by automorphism invariance.

Conversely, if all P band components lie in K, then the natural actor r is pure. At a source diagonal, an idempotent actor forces `a=(b,q^(-1))`; the source square has band component `b (q^(-1)·p) b=b`, so the source element is idempotent. The CS actor's natural order is equality; purity transfers weak E-unitarity.

Regularity is automatic. Take `s=(i,(b,g),λ)` and choose ANY j∈I, μ∈Λ. Write `P_(λ,j)=(p,q)` and `P_(μ,i)=(p',t)`. Let

`c=(gq)^(-1)·b`,       `h=q^(-1)g^(-1)t^(-1)`,
`x=(j,(c,h),μ)`.

Using p,p'∈K, both of which remain in K under the action, direct multiplication gives `s x s=s`: its middle group is `gq h t g=g`, and its band part reduces successively by `b (g·p) b=b` and `b (t^(-1)·p') b=b`. The standard replacement x↦x s x is a mutual inverse. Thus no unit row/column premise is needed for this theorem.

## 3. A locally regular evaluation Rees band

Choose any `z∈K(B)`; it exists when the full matrix satisfies §1. Let T be the full Rees semigroup over B with row set `I×G`, column set `Λ×G`, and sandwich matrix

`H_((λ,t),(j,u)) = t^(-1)·p_(λ,j)` if `q_(λ,j)=t u^(-1)`,
`H_((λ,t),(j,u)) = z` otherwise.                           (2)

Every H entry lies in K. Consequently EVERY element `((i,k),b,(λ,t))` of T is idempotent, since `b H b=b`; T is a band. Associativity is the ordinary Rees product over the associative band B.

Every local corner of T embeds into a regular-band corner of B. For an idempotent `e=(row,a,col)`, write p=H_(col,row), d=ap. Since `a p a=a`, d²=d. Every x∈eTe has the same row/column and middle b satisfying `b=a p b p a`; map it to bp. This map preserves products because `(b p c)p=(b p)(c p)`, is injective because `b=(a p)(b p)a`, and lands in dBd because `bp=(ap)(bp)(ap)`. Since B is globally regular, dBd and all its subbands satisfy the regular-band identity. Hence T is locally regular.

Set `C=T^G` with G acting by left shifts `(α_w F)(k)=F(w^(-1)k)`. It is a locally regular band; infinite powers are allowed.

## 4. Explicit physical host

For `s=(i,(b,g),λ)` define, at each k∈G,

`β_s(k)=((i,k), k^(-1)·b, (λ,g^(-1)k)) ∈ T`.           (3)

Let `t=(j,(c,h),μ)`, let `P_(λ,j)=(p,q)`, and put w=gq. In `α_w β_t(k)=β_t(w^(-1)k)`, the T row is `(j,w^(-1)k)` and its middle is `(k^(-1)w)·c`. The left T column is `(λ,g^(-1)k)`. With `t0=g^(-1)k`, `u0=w^(-1)k=q^(-1)t0`, the selector condition in (2) reads `t0 u0^(-1)=q`, so the inserted T sandwich is

`t0^(-1)·p = (k^(-1)g)·p`.

The resulting middle is exactly

`(k^(-1)·b) ((k^(-1)g)·p) ((k^(-1)gq)·c)`
`=k^(-1)·(b (g·p) (gq·c))`,

and the resulting column is `(μ,h^(-1)q^(-1)g^(-1)k)`. These are precisely (3) for st. Thus `β_(st)=β_s α_(gq)(β_t)` for every pair, with multiplication in the displayed noncommutative order.

The natural actor supplies i,λ,g; β_s(1_G)'s middle is b. Hence `s↦(β_s,r(s))` is injective. It is a faithful physical model with locally regular band C, so for the automatically regular source every local idempotent set is an orthodox regular band. This gives the required original local-r property without invoking an abstract all-source embedding theorem.

## 5. Finite example beyond a rectangular base

`frontier-20261028-regular-band-base-rees-checker-v1.py`, SHA `02465075fea0f1e3d613df53f286f09e9b28ecf85dd3210c28829ff46852a290`, ran `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 19:03:12 PDT 2026**, exit0. Its B is an8-element rectangular band times a two-element semilattice, with a nontrivial C2 action, and its K/top D-class has4 elements. This B is not rectangular and has no identity; A has16 elements. A full2×2 top-sandwich source has64 elements and actor8; the evaluation band T has128 elements.

```text
base regular band=8, top rectangular D-class=4, group=C2; source=64 actor=8 T=128
PASS all128 T elements idempotent, all T associativity and local-corner regularity
PASS all4096 source/actor/host products+injection, regularity, WEU, local-r, actual tau
CONTROL lower-D sandwich yields explicit s^3=s^2!=s
```

The verifier exhausts all128³ T associativity checks and all its local-corner regular-band identities, every64² host/source product and fibre comparison, the source hypotheses and actual idempotence contexts. Its lower-component mutant gives an actual weak-E violation, not merely failure of the model. These are same-author finite checks; the general K criterion, regularity and host law above are written symbolically.

## 6. Actual q and dependency limit

The natural actor r is onto and pure, so `τ_S=r^(-1)(τ_D)`. In general D need not already be its syntactic quotient. The explicit pure onto-CS actor pushforward in `frontier-20261028-pure-actor-finite-band-pushforward-v1.md`, SHA `abdfecbfb03b7931ad8dac0e7912f6c359279fe7afd47662a4f376942b2d9057`, transports the faithful natural-actor host to one over ACTUAL q_τ, adding only a rectangular band factor and transporting the group action through a local-group isomorphism. The band remains locally regular. The canonical free-V-band universal map into that host makes κ_q injective and pays both same-q R and L obligations for this family.

If the named actor-transport input fails independent review, retain §§1–5's faithful natural-actor host and K classification, and mark actual-q/canonical consequences **NR-PUSHFORWARD**. This note concerns A=B⋊G and does NOT adjoin a new external identity to a nonunital B⋊G. The full original R/L/SEP and printed Q1/Q2 remain open; no independent witness/review, formal/kernel proof or novelty clearance is claimed.
