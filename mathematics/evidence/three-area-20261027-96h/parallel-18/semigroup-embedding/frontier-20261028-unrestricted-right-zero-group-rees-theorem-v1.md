# Unrestricted right-zero-by-group Rees sources have locally regular hosts

**NEW AUTHOR WRITTEN CANDIDATE with exact nonabelian checks; unreviewed/unadopted.** Native check-start observation **Wed Oct 28 18:54:48 PDT 2026**. This removes the fixed five-element base, every row-code/tag restriction, and the commutativity restriction. It is still a theorem for a specified Rees family, not all original sources or either entire printed question. The actual-q consequence explicitly depends on the named pure-CS actor pushforward.

## 1. Statement

Let G be ANY group acting on a nonempty set R on the left. Regard R as a right-zero band and adjoin a NEW identity `1_A` to R⋊G. Its nonidentity elements multiply as

`(r,g)(s,h)=(g·s,gh)`,

and θ maps 1_A to 1_G and `(r,g)` to g. Let I,Λ be arbitrary nonempty sets and P ANY full Λ×I A-valued matrix.

**Theorem.** If each entry of P is either 1_A or a nonidentity `(v,q)` with q≠1_G, then `S=M[A;I,Λ;P]` has an explicit faithful physical model over its natural completely-simple actor `r(i,a,λ)=(i,θ(a),λ)`, using a locally regular band with a G action. There is NO restriction on how the R-labels vary among entries with the same q, even within the same matrix row, nor on finiteness or commutativity.

If S is regular and weakly E-unitary, its P entries necessarily have exactly the preceding form. Conversely if S is regular and P has that form, S is weakly E-unitary and locally r-orthodox. Thus EVERY regular weak-E full Rees source over this A belongs to the faithful-host family. In particular, having 1_A in every P row and column suffices for regularity; it is not claimed necessary. Under the named actor-pushforward input in §5, each such source also has a faithful host over its ACTUAL q_τ, and canonical κ_q is injective with both same-q R/L separations.

## 2. Evaluation band with selectors for every group label

For each λ and q∈G\{1_G}, choose a function `f_(λ,q):I→R` such that

`f_(λ,q)(i)=q^(-1)·v` whenever `P_(λ,i)=(v,q)`.

At all other positions choose one fixed arbitrary element of nonempty R. Each cell has one actual P entry, so this is unambiguous even if the SAME row has many different R-labels at the SAME group value.

Form the disjoint union

`T={U_i:i∈I} ⊔ {V_(λ,q):λ∈Λ, q≠1_G} ⊔ {W_r:r∈R}`,

and let N consist of all V's and W's. Define products by

- `x y=y` whenever x∈T and y∈N;
- `U_i U_j=U_i`;
- `W_r U_j=W_r`;
- `V_(λ,q) U_j=W_(f_(λ,q)(j))`.

T is associative and idempotent. If the rightmost factor is in N, both bracketings equal it. If the two rightmost factors are U's, their product is the first U and `xU` is always a U or a W, fixed by right multiplication by any U. If the middle factor is in N and the rightmost is a U, both bracketings equal the middle-factor/U product, which belongs to N.

Every `U_i T U_i={U_i}∪{W_r:r∈R}` is a right-zero band with identity U_i; for every e∈N, eTe={e}. Hence T is locally regular. Set

`B=T^G`,       `(α_g F)(k)=F(g^(-1)k)`.

Direct products preserve the local-regular-band identity, and left shifts give a G action by band automorphisms. B may be infinite, including when G or R is infinite; no finiteness or finite support restriction is assumed. No action of G on the VALUES of T is needed.

## 3. Coefficients and all source products

For `s=(i,a,λ)` and g=θ(a), define `C_s∈T^G` by

- if `a=(r,g)`, then `C_s(g)=W_(g^(-1)·r)`;
- if `a=1_A` (so g=1_G), then `C_s(1_G)=U_i`;
- at every k≠g, `C_s(k)=V_(λ,g^(-1)k)`.

The actor supplies i,λ,g. At coordinate g the coefficient is either U_i for the new identity or a W that determines `g^(-1)·r`, hence r. The displayed disjointness of U and W makes the physical map `j(s)=(C_s,r(s))` injective.

For `s=(i,a,λ)`, `t=(j,b,μ)`, put g=θ(a), q=θ(P_(λ,j)), w=gq and h=θ(b). We prove the full group-weighted law

`C_(st)=C_s · α_w(C_t)`                                  (1)

coordinatewise, with NO commutativity assumption.

**b=(v,h) is nonidentity.** Every coordinate of C_t lies in N, so it overwrites the corresponding left coordinate. The source middle product is `(w·v,wh)`. At k=wh, the shifted right factor equals `W_(h^(-1)·v)`, which is the target's distinguished value since `(wh)^(-1)·(w·v)=h^(-1)·v`. At k≠wh, it is `V_(μ,(wh)^(-1)k)`, also exactly the target coefficient.

**b=1_A.** The shifted C_t has U_j at k=w and `V_(μ,w^(-1)k)` at all other coordinates. At k≠w it overwrites the left and gives exactly the target's non-distinguished value. At k=w there are two cases:

- If q=1_G then the P condition forces `P_(λ,j)=1_A`. Thus w=g. The left coefficient is U_i when a=1_A, or `W_(g^(-1)·r)` when a=(r,g); right multiplication by U_j leaves it unchanged. This is the target's distinguished coordinate.
- If q≠1_G then `P_(λ,j)=(v,q)` and w=gq≠g. The left coefficient there is V_(λ,q), so multiplying by U_j gives `W_(f_(λ,q)(j))=W_(q^(-1)·v)`. The source middle product aP has group gq and, whether a is identity or not, normalized label `q^(-1)·v`. This is exactly the target's distinguished coordinate.

The actor multiplication is the group Rees product, so (1) proves j is a physical homomorphism. Its fibre injectivity was already proved. This is a symbolic all-products proof for arbitrary G and R; it is not inferred from S3 sampling.

## 4. WEU iff the allowed matrix form, and local r-orthodoxy

If P has the stated form, the natural actor is pure. If its source value is idempotent and the diagonal P entry is 1_A, then θ(a)=1_G and a is either 1_A or an idempotent `(r,1_G)`. If the diagonal entry is `(v,q)` with q≠1_G, then a=(r,q^(-1)), and

`a (v,q) a = (r,q^(-1))=a`.

Therefore S is weakly E-unitary: a source element above an idempotent has an idempotent CS actor, since natural order on D is equality, and purity reflects idempotence.

Conversely if a matrix entry is the forbidden nonunit idempotent `(v,1_G)`, let `s=(i,1_A,λ)` at that position. Then `s²=(i,(v,1_G),λ)` is an idempotent, `s³=s²≠s`, and s²≤s, so weak E-unitarity fails. This uses only the displayed source products, not finite G or R.

For regular S, the faithful physical model gives local r-orthodoxy: the actor image of local idempotents is the identity of the local actor group; their coefficients lie in a regular band corner, and injectivity reflects closure and the regular-band identity. A itself is regular: any `(s,g^(-1))` is a mutual inverse of `(r,g)`. If every P row and column contains 1_A, those unit positions and any mutual inverse in A give a source inverse, hence regularity.

## 5. Actual source actor and canonical separation

The natural actor r is onto and pure, so source idempotence contexts satisfy `τ_S=r^(-1)(τ_D)`. The natural D can have syntactically indistinguishable rows/columns: NO equality of these two actors is assumed.

The pure onto-CS actor pushforward in `frontier-20261028-pure-actor-finite-band-pushforward-v1.md`, SHA `abdfecbfb03b7931ad8dac0e7912f6c359279fe7afd47662a4f376942b2d9057`, transports the faithful D-host to one over the ACTUAL q_τ with band `(I×Λ)×B`, using the local-group isomorphism and explicit Rees gauges. That band remains locally regular. The canonical free-V-band universal map into the physical band then makes κ_q injective; the same-q R and L obligations follow.

This clause is conditional on the named WRITTEN actor transport. If that input fails independent review, §§2–4 still prove the faithful natural-actor model and WEU classification; label the actual-q/canonical consequence **NR-PUSHFORWARD**. The theorem does not assert that arbitrary original sources have this special Rees form.

## 6. Direct nonabelian verification and scope

`frontier-20261028-unrestricted-group-rees-checker-v1.py`, SHA `0867aaa2608d79a36728a7a5962bbdaa3631dca52889033c375bc5584007a4cf`, ran `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 18:54:48 PDT 2026**, exit0. It takes the noncommutative group S3 acting naturally on R={0,1,2}, and two different3×3 P matrices with FIRST row/column identity and a row containing two distinct R-labels at the SAME group element. For each it directly constructs T (21 elements), source171 elements and group-coordinate coefficient vectors; it exhausts T associativity and all local-corner identities, source regularity/WEU/local-r, all171² physical laws and fibre injections, and all172² actual/absent contexts for every source element.

```text
collapsed=False source=171 T=21 natural_actor=54 actual_actor=54
PASS T associative/local regular; 29241 source/host products+injection; purity, regularity, WEU, local-r, 172^2 contexts/source
collapsed=True source=171 T=21 natural_actor=54 actual_actor=24
PASS T associative/local regular; 29241 source/host products+injection; purity, regularity, WEU, local-r, 172^2 contexts/source
PASS retained-rectangle host over actual q, all29241 comparisons
CONTROL all3 forbidden identity-group nonunit sandwiches give explicit WEU violation
```

The second matrix has identical group rows and columns but different R-labels, so its true q has24 elements rather than the natural54. Its retained-rectangle actual-q model is checked directly. The forbidden-entry control covers all3 nonunit identity-group values in this finite R. The direct program is same-author and does not establish novelty or independent finite-witness certification.

This note subsumes the earlier row-coded arbitrary-G theorem and the unrestricted-five-base theorem at their overlapping scopes, but does not retroactively edit or adopt those frozen records. Beyond the declared Rees family the full original R/L/SEP and printed questions remain open; no cross-model, human, formal/kernel or independent review is claimed.
