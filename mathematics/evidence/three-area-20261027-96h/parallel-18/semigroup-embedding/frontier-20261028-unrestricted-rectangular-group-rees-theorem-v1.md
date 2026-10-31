# All weak-E regular Rees sources over a rectangular-band-by-group base

**NEW AUTHOR WRITTEN CANDIDATE with exact nonabelian finite check; unreviewed/unadopted.** Native check-start observation **Wed Oct 28 18:57:42 PDT 2026**. This extends the unrestricted right-zero-base theorem to arbitrary rectangular bands, but it still concerns a specified Rees family, not every original source. The actual-q/canonical consequence names the prior pure-actor pushforward. No novelty, independent review, or printed-question resolution is asserted.

## 1. Exact theorem

Let K=L×R be ANY nonempty rectangular band, `(ℓ,r)(ℓ',r')=(ℓ,r')`, and let ANY group G act on K by automorphisms. Such an action preserves the two Green coordinates and induces actions on L and R; write the action on R as `g·r`. Adjoin a NEW identity 1_A to `K⋊G`. Its nonidentity multiplication is

`(ℓ,r,g)(ℓ',r',h)=(ℓ,g·r',gh)`.                            (1)

Let I,Λ be arbitrary nonempty sets and P ANY full Λ×I matrix over A. Write θ(1_A)=1_G, θ(ℓ,r,g)=g.

**Theorem.** If every P entry is either 1_A or a nonidentity `(ℓ,r,q)` with q≠1_G, then the full Rees semigroup S=M[A;I,Λ;P] has an explicit faithful physical model over its natural completely-simple actor `r(i,a,λ)=(i,θ(a),λ)`, with a locally regular band and G action. There is no row-code, group-commutativity, finiteness or placement restriction.

For regular S, weak E-unitarity is equivalent to precisely that form of P. In this case S is automatically locally r-orthodox and lies in the declared original class. Under the named pure-actor pushforward in §6, the model transports to the ACTUAL q_τ, making canonical κ_q injective and establishing both same-q R and L idempotent separation for this family. If every P row and column has 1_A then S is regular; that sufficient condition is not claimed necessary.

The preceding unrestricted right-zero theorem is the case |L|=1. The new left-band coordinate below pays the missing rectangular L information directly; it is not assumed that arbitrary original sources have this Rees form.

## 2. Two locally regular evaluation bands

Fix a default `r_*∈R` and `ℓ_*∈L`. For each matrix column i, row λ and q≠1_G, define selectors:

`f^R_(λ,q)(i)=q^(-1)·r_p` when `P_(λ,i)=(ℓ_p,r_p,q)`, otherwise r_*;

`f^L_(i,q)(λ)=ℓ_p` when `P_(λ,i)=(ℓ_p,r_p,q)`, otherwise ℓ_*.

There is no conflict for repeated group labels because the selector keeps the entire opposite index.

Build right evaluation band T_R as the disjoint union of `U^R_i`, `V^R_(λ,q)` and `W^R_r`; the V symbols use q≠1_G. Let N_R be the V and W symbols. Its products are

`x n=n` for n∈N_R; `U^R_i U^R_j=U^R_i`; `W^R_r U^R_j=W^R_r`; `V^R_(λ,q) U^R_j=W^R_(f^R_(λ,q)(j))`.

Build left evaluation band T_L analogously from `U^L_λ`, `V^L_(i,q)` and `W^L_ℓ`, using f^L in the final product. In each case associativity follows by considering a rightmost N element, two rightmost U elements, or a middle N followed by U. Each U-corner is U plus a right-zero band of all W symbols; each N-corner is a singleton. Hence T_L and T_R are locally regular. The opposite of a locally regular band is locally regular: reversing `xyxzx=xyzx` and swapping y,z restores the same identity.

Define

`B_L=(T_L^op)^G`,       `(α^L_g F)(k)=F(k g)`,
`B_R=T_R^G`,            `(α^R_g F)(k)=F(g^(-1) k)`,
`B=B_L×B_R`, with componentwise G action.

Both shifts are genuine actions by automorphisms: in the left case `α^L_g α^L_h F(k)=F(kgh)`; the right case is the standard left shift. Direct products preserve local regularity. No finite support is assumed.

## 3. Right coefficient and its full product law

For `s=(i,a,λ)` and g=θ(a), let the R coefficient `C^R_s∈B_R` be

- at k=g: `U^R_i` if a=1_A, or `W^R_(g^(-1)·r)` if a=(ℓ,r,g);
- at k≠g: `V^R_(λ,g^(-1)k)`.

For `t=(j,b,μ)` set q=θ(P_(λ,j)), w=gq. The same coordinate proof as in the independently written right-zero theorem gives

`C^R_(st)=C^R_s α^R_w(C^R_t)`.                              (2)

Explicitly, if b is nonidentity, every coordinate of C^R_t lies in N_R and the right factor overwrites the left; `(wh)^(-1)·(w·r_b)=h^(-1)·r_b` handles a noncommutative group. If b=1_A, every shifted coordinate except w overwrites. At w, a unit sandwich leaves the distinguished U/W unchanged, while a sandwich `(ℓ_p,r_p,q≠1)` produces `V^R_(λ,q)U^R_j=W^R_(q^(-1)·r_p)`, exactly the target normalized R-label. Neither case uses any same-label row condition.

## 4. Left coefficient and its full product law

Define `C^L_s∈B_L` by

`C^L_s(1_G)=U^L_λ` if a=1_A, and `C^L_s(1_G)=W^L_ℓ` if a=(ℓ,r,g);

`C^L_s(k)=V^L_(i,k)` for k≠1_G.

For the same s,t and w=gq, the physical law is

`C^L_(st)=C^L_s α^L_w(C^L_t)` in `(T_L^op)^G`.              (3)

At k≠1_G, the right argument in the underlying T_L multiplication is `V^L_(i,k)∈N_L`, so the result is that V, exactly the target whose source row is i. At k=1_G:

- If a is nonidentity, the underlying T_L right argument is `W^L_ℓ`, so the result is W^L_ℓ. Formula (1) says the source product retains the LEFT label of a, regardless of p and b.
- If a=1_A and p=1_A, then w=1_G. The shifted t coefficient at1 is U^L_μ for b=1_A, or W^L_(ℓ_b) otherwise. Multiplying either on the right by U^L_λ yields the same element, which is exactly the target.
- If a=1_A and p=(ℓ_p,r_p,q) with q≠1_G, then w=q. The shifted t coefficient at1 is `C^L_t(q)=V^L_(j,q)` regardless of b. In the underlying T_L, `V^L_(j,q)U^L_λ=W^L_(f^L_(j,q)(λ))=W^L_(ℓ_p)`, the left label of p b.

This proves (3) directly for arbitrary noncommutative G; no opposite-host transport is assumed.

## 5. Faithfulness, weak-E and the source class

Map `s↦((C^L_s,C^R_s),r(s))` into P(B,D), where D=M[G;I,Λ;θ(P)]. Equations (2)–(3) give every physical product. If two images agree, the actor supplies i,λ,g. At coordinate1_G the left coefficient distinguishes a=1_A from a nonidentity and recovers ℓ; at coordinate g the right coefficient distinguishes the identity and recovers `g^(-1)·r`, hence r. Thus the map is injective.

The natural actor is pure. At a source diagonal, if the sandwich is 1_A then an idempotent actor has θ(a)=1_G and a is either 1_A or the idempotent `(ℓ,r,1_G)`. If the sandwich is `(ℓ_p,r_p,q)` with q≠1_G and actor is idempotent, then `a=(ℓ,r,q^(-1))`; by (1),

`a (ℓ_p,r_p,q) a=(ℓ,r,q^(-1))=a`.

Hence the stated matrix form implies weak E-unitarity. Conversely, if some sandwich is a nonidentity `(ℓ,r,1_G)`, that sandwich is idempotent. At its cell let `s=(i,1_A,λ)`; then `s²` is idempotent, `s³=s²≠s`, and `s²≤s`, contradicting weak E-unitarity.

A is regular: ANY `(ℓ',r',g^(-1))` is a mutual inverse of `(ℓ,r,g)`, by (1). If each P row and column has 1_A, inserting those unit sandwiches and a mutual inverse in A makes every source element regular. For any regular source with allowed P, the faithful physical host transfers orthodoxy and the regular-band law from its local band corners to each E(eSe), so S is locally r-orthodox.

## 6. Actual q and named dependencies

The natural CS actor is onto and pure, so `τ_S=r^(-1)(τ_D)` by lifting/reflection of idempotence contexts. It need NOT itself be the actual actor: identical group rows or columns can collapse.

The explicit pure onto-CS actor pushforward `frontier-20261028-pure-actor-finite-band-pushforward-v1.md`, SHA `abdfecbfb03b7931ad8dac0e7912f6c359279fe7afd47662a4f376942b2d9057`, changes the target band only by an additional rectangular factor I×Λ and transports the action through the local-group isomorphism. The resulting band remains locally regular. Composing the faithful natural-actor host with this map gives a faithful physical host over ACTUAL q_τ; the canonical free-V-band universal map then makes κ_q injective, including both same-q R/L obligations.

This actual-q/canonical clause explicitly depends on the named WRITTEN pushforward. If it fails review, retain the independently constructed natural-actor host and weak-E characterization in §§2–5 and mark the q/canonical claim **NR-PUSHFORWARD**. No equivalence with the entire printed original question is assumed.

## 7. Exact nonabelian finite check

`frontier-20261028-rectangular-group-rees-checker-v1.py`, SHA `482a7d7cb7286f2945ae61c1f4aab2deacc8725f3fc95a5a0e47603f0d6d737c`, ran `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 18:57:42 PDT 2026**, exit0. It uses noncommutative S3, a 2×3 rectangular band, the natural nontrivial S3 action on R and a trivial action on L. The 2×3 P matrix has the first row/column 1_A and two distinct rectangular labels at the SAME nonidentity group value in its remaining row. The full source has222 elements; its group actor has36 but its ACTUAL syntactic quotient only24.

```text
group S3 noncommutative; rectangle 2x3; source=222 natural_actor=36 actual_actor=24
TR=16 TL=19 source_idempotents=40
PASS both evaluation bands associative/local regular; all49284 left/right host product laws and actor-fibre injection
PASS source regular/WEU/local-r, purity, retained rectangle, 223^2 contexts/source
CONTROL all6 forbidden identity-group nonunit sandwiches violate WEU
```

The program constructs both evaluation bands from the concrete P, exhausts their associativity/local corners, both physical laws and fibre injection for all222² source pairs, and all223² source contexts per source element; it separately checks the retained-rectangle actual-q model. The six forbidden controls cover each nonidentity idempotent of the finite rectangular base. These checks are same-author finite evidence, not cross-model/independent or formal verification; the arbitrary-index/group proof is the written §§2–5.

This candidate subsumes the earlier right-zero and five-element Rees families at their overlapping scopes, without editing or retroactively adopting them. All-original-source R/L/SEP, the printed Q1/Q2 outside this special family, human review and novelty remain open.
