# Eight-zero rank-two residual: common atom placement and sign compatibility

**UNREVIEWED AUTHOR CANDIDATE.** Native clock observed before writing: **2026-10-29T15:11:59-0700**. This is a written, cross-fibre obstruction in one actual residual of the adopted f244 scope. It is not a complete exclusion of that residual, the `(0,4,8)` case, rank two, or the original target; it is not a witness, formal proof, independent review or novelty claim. No scientific computation, solver, test, model CLI, Git, deletion or publication was performed in this continuation.

This successor-round packet is stored in the author's explicitly permitted Oct-23 owner root; that storage does not reopen the closed round. The invalid P1 profile roster, f239/CR7, old roster-based completeness claims, and all held or withdrawn episodes are **NONINPUT**.

## 1. Scope and result

Assume the exact original-object hypotheses of the adopted f244 disposition: f is balanced on F₂⁹, `max|W_f|≤28`, the even polar B has rank 2, there are exactly eight Walsh zeros, `m=116`, and, after labelling the three nonzero fibres, `(e₁,e₂,e₃)=(0,4,8)`. Take its explicit residual **`(G₃,H)=(1,0)`**. As in f244, `K=R⊕F₂²`, R is the six-dimensional polar radical, and the q-zero fibre is s=0.

For s=2,3 write

`v_s(r)=k(r,s)/2=σ_s(r)(3−2·1_{A_s}(r))`, `σ_s:R→{±1}`,

where `A_s={r:|k(r,s)|=2}`. Thus `|A₂|=4`, `|A₃|=8`, and the signed atom function is `τ_s=σ_s·1_{A_s}`. The two supports lie in the **same chosen R coordinates**. Put `X_s=⊕_{a∈A_s}a` and `Π_s=∏_{a∈A_s}σ_s(a)`.

**Candidate necessary conditions.**

1. `X₂=X₃≠0` and `Π₂=Π₃`.
2. The unique affine relation among the eight A₃ atoms is a four-point plane P. For every `t∈R`,

   `|(A₂+t)∩A₃|≤2`.                                              (C)

   Thus no translate of the four-atom fibre shares any three atoms with the eight-atom fibre. In particular `A₂` is not the four-atom complement of P in A₃.
3. For each `t∈R`, set `d_t(r)=[σ₂(r+t)−σ₃(r)]/2∈{−1,0,1}`. Then

   `Σ_r d_t(r)≡0 (mod 4)` and `⊕_{r:d_t(r)≠0}r=0`.              (S)

These are constraints on **actual atom placements and signs across both fibres**, not a new class-count relaxation. They do not prove that any remaining placement extends to a common ternary inverse, the full caller, or a Boolean target. Conversely, they do not eliminate every abstract placement; §7 gives a concrete limited control.

## 2. Adopted f244 input and common transform notation

The f244 parent disposition supplies, at same-harness written-support scope, the exact residual counts

`A₁=16`, `C₂=4`, `C₃=6`, `D₁=18`, `G₂=2`, `G₃=1`, `H=0`, `O=17`.

It also supplies the following facts at this residual:

- A₂ has affine rank 3. For `t₂=Walsh₆(τ₂)`, its zero set is `H₂\F₂`, where H₂ is an affine 5-flat and F₂⊂H₂ is an affine 3-flat; `F₂={c:|t₂(c)|=4}` and `H₂={c:t₂(c)≡0 (mod 4)}`.
- A₃ has affine rank 6 and exactly one affine relation, of weight 4 and even sign syndrome. Its relation is the plane P, and the product of the four τ₃ signs on P is +1.
- Let `B₃={c:t₃(c)≡0 (mod 3)}`, `t₃=Walsh₆(τ₃)`. Its size is 23. Every affine hyperplane has at most 19 points of B₃; the unique hyperplane with 19 is the even-parity hyperplane H_* in the normal coordinates below.
- The even inverse u has 64 four-point blocks. For their local transforms U_s,

  `16U_s(c)=3Walsh₆(σ_s)(c)−2t_s(c)` and `U_s(c)≡t_s(c) (mod 3)`.      (1)

These are the actual common-fibre definitions, not arbitrary independent transforms. We restate the normal form and the small geometric calculations required by this packet; no P1 roster is imported.

Choose a base atom a in P and write, with six independent vectors `p,q,b₁,b₂,b₃,b₄∈R`,

`P={a,a+p,a+q,a+p+q}`, `A₃\P={a+b₁,a+b₂,a+b₃,a+b₄}`.

After an affine change of block coordinates and an irrelevant overall character, we may use `u=(p·c,q·c)∈F₂²`, `v=(b₁·c,…,b₄·c)∈F₂⁴` with affine sign offsets absorbed, so that

`t₃(c)= ±χ_a(c)[4·1_{u=0}+Σ_{i=1}⁴(-1)^{v_i}]`.

The ± character may vary with c but has no effect on the zero sets or absolute values. In these coordinates

`B₃={(u,v):u≠0, |v|=2} ∪ {(0,v):|v|=1 or 4}`,
`H_*={v:|v| even}`.

There are 19 points of B₃ in H_* and 23 in total. This is the signed-plane-plus-four-independent-characters structure, not an assumption that any full spectrum exists.

## 3. The two fibre hyperplanes coincide

The zero sets of U₂ and U₃ meet exactly in the H and O block classes. At `(G₃,H)=(1,0)` there are 17 O blocks and no H blocks, so

`|B₃∩(H₂\F₂)|=17`.

Thus H₂ contains at least 17 B₃ points. For completeness, a character indexed by `(α,β)∈F₂²×F₂⁴` has

`Walsh(1_{B₃})(α,β)=(3 if α=0 else −1)K₂(|β|)+K₁(|β|)+K₄(|β|)`,

where the two sequences for `|β|=0,1,2,3,4` are `K₂=(6,0,−2,0,6)` and `K₁+K₄=(5,1,1,−3,−3)`. The only nontrivial coefficient with absolute value at least 11 is +15 at `(α,β)=(0,1111)`. Since `2·17−23=11`, the unique possible H₂ is **H_***, which contains 19 points of B₃. Consequently

`H₂=H_*`, and `|F₂∩B₃|=19−17=2`.                            (2)

This is a geometry statement coupling the two actual fibre transforms.

## 4. Equal support XOR and sign product

For either s=2 or 3, the atom count e_s is even. If `n_s^-` is the number of negative τ_s atoms, expanding each character modulo 4 gives

`t_s(c)/2 ≡ n_s^- + X_s·c (mod 2)`.                            (3)

For s=2, the zero set of the right-hand side is H₂. For s=3, in the normal coordinates it is exactly H_*, because the plane contribution is divisible by 4 and the four outer character signs have even weight precisely there. By (2) the two nonconstant affine Boolean functions have the same zero set. Therefore their linear parts and constants agree:

`X₂=X₃≠0` and `n₂^-≡n₃^- (mod 2)`, hence `Π₂=Π₃`.           (4)

The common XOR is nonzero: the relation plane P has XOR 0, and the remaining four atoms have XOR `b₁+b₂+b₃+b₄`, which is nonzero because the six displayed vectors are independent.

## 5. A geometric line in the common hyperplane

Let `d∈R*` be the unique block-space direction with

`p·d=q·d=0`, and `b_i·d=1` for i=1,2,3,4.

In the normal block coordinates it is `(Δu,Δv)=(0,1111)`. We prove that the two points of `F₂∩B₃` differ by d.

Inside H_* let `V_even={v:|v| even}` and `L={0,1111}`. Then

`B₃∩H_* = ((F₂²\{0})×(V_even\L)) ∪ {(0,1111)}`.             (5)

Let F be any affine 3-flat in H_* with `|F∩B₃|=2`; examine the dimension of its u-projection.

- Dimension 0: the V_even fibre is all eight points. The intersection has size 1 when u=0, or 6 when u≠0, so size 2 is impossible.
- Dimension 1: if both projected u values are nonzero, each four-point fibre contains at least two points outside L, giving at least four B₃ points. Therefore one value is 0 and the other nonzero. For exactly two B₃ points, the nonzero-u fibre is an affine 2-flat containing L, and its two points outside L form a line parallel to L; the zero-u fibre avoids `(0,1111)`.
- Dimension 2: each of the four u-fibres is a two-point line, all with the same direction K. If K is not parallel to L, each of the three nonzero-u fibres meets L in at most one point, giving at least three B₃ points. Hence K is parallel to L. Every nonzero-u fibre either equals L and contributes zero, or is disjoint from L and contributes two; the zero-u fibre contributes at most one. Exact intersection size 2 therefore comes from one disjoint nonzero-u line, parallel to L.

In every possible case `F∩B₃` is a two-point line in direction d. Applying this to F₂ and (2), `d∈dir(F₂)`.

Since F₂ is the set where all four signed A₂ characters align, for any two atoms x,y∈A₂ their ratio character is constant on F₂. Thus `d∈dir(F₂)` forces

`x·d=y·d` for all `x,y∈A₂`.                                   (6)

The four plane atoms in A₃ all have value `a·d`, while its four outer atoms all have value `a·d+1`. Hence A₂ can intersect P or `A₃\P`, but **not both**.

## 6. Excluding intersections of three or four atoms

If A₂ contains three points of P, their differences span `⟨p,q⟩`. Because all signed A₂ characters align on F₂, both u coordinates are fixed there. Thus F₂ has zero-dimensional u-projection, but the first bullet of §5 shows such a flat cannot have `|F₂∩B₃|=2`. Hence `|A₂∩P|≤2`.

If A₂ contains three points of the outer set, the equality of XORs in (4) forces its fourth point to be the fourth outer atom. More generally, if `A₂⊂A₃`, then `⊕(A₃\A₂)=0`; the unique affine relation in A₃ makes the four-point complement exactly P. Thus

`A₂⊂A₃  ⇒  A₂=A₃\P`.                                          (7)

We now exclude this remaining placement with signs included. On P the τ₃ sign product is +1; (4) then says that the product of the four τ₂ signs equals the product of the four τ₃ signs on the outer set. In the normal coordinates, this means the `|t₂|=4` flat would have

`F₂=F₂²×{v₀,v₀+1111}` for some even-weight v₀.

If `v₀∈{0,1111}`, it meets B₃ in exactly one point. If `v₀` is any other even vector, it and its complement both have weight 2, and the flat meets B₃ in six points. Both contradict (2). Thus `A₂≠A₃\P`, and `|A₂∩(A₃\P)|≤2`.

Together with the no-mixed-intersection conclusion of (6), **`|A₂∩A₃|≤2`**.

Finally, change the chosen complement `F₂²→K` by a linear shear that shifts the s=2 R-coordinate by any prescribed t and fixes the s=3 R-coordinate. The two nonzero labels 2 and 3 are independent in F₂², so such a shear exists for every t∈R. It translates A₂ to A₂+t and leaves A₃ fixed. On block transforms it only multiplies each U_s(c) by a character, preserving all class counts, the residual `(G₃,H)=(1,0)`, and all hypotheses above. Repeating the argument in the sheared coordinates gives (C) for every t. ∎

## 7. A further common-sign constraint

From (1), t₂ and t₃ are even, and `Walsh₆(σ_s)` is divisible by 4. Dividing the congruence modulo 8 by 4 gives

`Walsh₆(σ_s)(c)/4 ≡ t_s(c)/2 (mod 2)`.

The two right-hand bits have the same zero hyperplane H₂=H_*, hence are equal. Thus

`Walsh₆(σ₂)(c) ≡ Walsh₆(σ₃)(c) (mod 8)` for every c.        (8)

Let `d₀=(σ₂−σ₃)/2`. Its transform is divisible by 4. At c=0 this gives `Σd₀≡0 (mod 4)`. For arbitrary c, using `(-1)^{c·r}=1−2(c·r)` modulo 4 gives

`0≡Walsh₆(d₀)(c)≡Σd₀−2Σ_r d₀(r)(c·r) (mod 4)`.

Therefore `Σ_r d₀(r)(c·r)` is even for all c. On its support d₀ is ±1, so this is exactly `⊕_{r:d₀(r)≠0}r=0`. Applying the same complement shear as in §6 proves (S) for all t, with `d_t(r)=[σ₂(r+t)−σ₃(r)]/2`. ∎

## 8. A limited placement/sign control, not a witness

Take independent `p,q,b₁,b₂,b₃,b₄` in R and set

`A₃={0,p,q,p+q,b₁,b₂,b₃,b₄}`, all τ₃ signs +;
`A₂={0,p,q+b₁+b₂,p+q+b₃+b₄}`, with τ₂ signs `(+,+,−,−)` in that order.

Then both support XORs equal `n=b₁+b₂+b₃+b₄`, the sign products are +1, and the displayed supports meet in exactly two atoms. In the normal `(u,v)` coordinates, F₂ is

`u₁=0`, `u₂+v₁+v₂=1`, `v₁+v₂+v₃+v₄=0`.

It meets B₃ in the two points `u=(0,1)`, `v=0011` and `1100`; so `|B₃∩(H_*\F₂)|=17`. This verifies the **specific support/zero-set geometry** discussed above, not existence of a full f.

For a sign-only extension, take σ₃=+1 everywhere and let σ₂ be −1 exactly at

`q+b₁+b₂`, `p+q+b₃+b₄`, `b₁`, `p+b₂+b₃+b₄`.

It agrees with τ₂ on A₂ and τ₃ on A₃. The four sign-disagreement positions have XOR 0, and their signed imbalance is −4; translating the first sign field preserves both facts. Hence this **formal sign extension** also satisfies (S).

It is intentionally not a block or Boolean realization: at c=0, `Walsh₆(σ₂)=56` and `t₂=0`, so (1) would demand `U₂=168/16`, not even an integer. Likewise `Walsh₆(σ₃)=64`, `t₃=8` would demand `U₃=11`, outside the four-point range. This control separates the new cross-fibre constraints from the still-missing ternary block compatibility and full caller.

## 9. Residual, dependencies and verification boundary

This packet constrains only `(G₃,H)=(1,0)` in the adopted f244 `(0,4,8)` case. The other six adopted class-count pairs, and placements satisfying (C) and (S) within this pair, remain open. The next unproved step is to enforce the signed local equations (1) and the remaining nonzero-shift caller equations **simultaneously** for such atom placements, or exhibit an actual target. No conclusion follows for the f248 m=114 case or for other ranks/fibre patterns.

`P=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/`.

| Input | SHA-256 | LF | Exact role |
|---|---|---:|---|
| `P/info-6-nl242-rank2-eightzero-116-fibre-048-obstruction-parent-v1.md` | `18403a17269311682255e3bb9823a89a0a69cd7344a66ad02bdd841bcc52f912` | 24 | f244 counts, four/eight-atom structures and B₃ hyperplane, at adopted conditional scope |
| `P/info-6-walsh-caller-and-mod4-coupling-parent-v1.md` | `721222262af91bc768227ce8bfae563cabf5a102437ac55e6583de38ec2d3c9d` | 23 | original Boolean caller, common frequency domain |

The new cross-fibre deductions, universal shear, geometric-line lemma and the limited control have not been disjointly reviewed, computationally replayed, formally checked or novelty-audited. They are not parent dispositions. All standing STOP/HOLD/ZERO/NONINPUT controls remain binding.
