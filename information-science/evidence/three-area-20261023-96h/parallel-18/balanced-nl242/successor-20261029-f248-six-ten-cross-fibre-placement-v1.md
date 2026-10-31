# Rank-two m=114: cross-fibre atom constraints in the (0,6,10) residual

**UNREVIEWED AUTHOR CANDIDATE.** Native clock observed before writing: **2026-10-29T15:25:46-0700**. This is a written placement-and-sign obstruction on actual remaining f248 configurations, not a class-count-only reduction, not a complete exclusion, not a Boolean witness, not a formal proof and not a novelty claim. No scientific computation, solver, test, model CLI, Git, deletion or publication was performed in this continuation.

The successor packet is stored in the author's explicitly permitted Oct-23 owner root; this does not reopen the closed round. The old P1 profile roster, f239/CR7, the separate f244/f255 m=116 chain, all roster-based completeness claims and all held/withdrawn episodes are **NONINPUT**.

## 1. Scope and candidate result

Assume the original-object hypotheses in the adopted f248 disposition: f is balanced on F₂⁹, `max|W_f|≤28`, its even polar has rank two, there are exactly eight Walsh zeros, `m=114`, and the three nonzero q-fibres have `(e₁,e₂,e₃)=(0,6,10)` up to permutation. In the f248 four-point-block notation take its residual **`y=N(G₂)=1`**. Thus the six signed small-coefficient atoms in fibre 2 have affine rank 5.

For s=2,3 let `A_s={r∈R: |k(r,s)|=2}`, `τ_s(r)=σ_s(r)1_{A_s}(r)`, and `t_s=Walsh₆(τ_s)`, with `|A₂|=6`, `|A₃|=10`. Both sets use the same chosen six-dimensional radical coordinates. Let `B_s={c:t_s(c)≡0 (mod 3)}`. Put `g=N(G₃)` and `h=N(H)`.

The affine-difference span of A₂ is a hyperplane in R; let `d∈R*` be its unique nonzero annihilator. Split the ten **signed** fibre-3 atoms according to their d-values into groups `A₃⁰,A₃¹`, with sizes k and `10−k`.

**Candidate necessary conditions.**

1. If the split is nontrivial, then `2≤k≤8`. If g is odd, the split must be nontrivial. The signed partial Walsh transforms satisfy the exact fractured-pair criterion and table in §3.
2. In the actual f248 residual `(y,g,h)=(1,1,2)`, the split sizes, in either order, are limited to **2+8, 4+6, or 5+5**. If a side has exactly two atoms a,b, then `a+b=⊕A₂`; moreover their signed characters are equal at the unique d-coset where `|t₂|=6`. These constraints concern actual placements **and signs** across both fibres.

No one of the listed splits is asserted realizable. The original `(0,6,10)` case, all 21 f248 class-count triples, and the balanced target remain open. The proof imports the f248 disposition only at its exact same-harness scope; standard character orthogonality and elementary affine counting are written out below. No P1 profile list, period condition or 7-variable covering-radius theorem is used.

## 2. The six-atom zero set is eleven parallel pairs

By f248, y=1 forces A₂ to be six distinct affinely independent points. Choose a base atom a and write

`A₂={a,a+p₁,…,a+p₅}`, with `p₁,…,p₅` linearly independent.

The unique nonzero d annihilates every p_i. After multiplying by an irrelevant overall character and choosing affine block-coordinate offsets that absorb the six signs,

`t₂(c)=±χ_a(c)[1+Σ_{i=1}⁵(-1)^{v_i}]`, `v_i=p_i·c+const_i`.

Each `v∈F₂⁵` corresponds to exactly one d-pair `{c,c+d}`. Since `1+Σ_i(-1)^{v_i}=6−2|v|`, the zero-mod-3 set B₂ is the union of the eleven pairs labelled by

`X={0} ∪ {v∈F₂⁵:|v|=3}`.                                  (1)

Thus `|B₂|=22`. Its unique quotient point with `|t₂|=6` is `v=0`, the **alignment pair**; all ten weight-3 quotient points have `t₂=0`.

## 3. The exact fractured-pair condition

Define the signed partial transforms

`P(c)=Σ_{a∈A₃⁰}τ₃(a)χ_a(c)`, `Q(c)=Σ_{a∈A₃¹}τ₃(a)χ_a(c)`.

Then `t₃(c)=P(c)+Q(c)` and `t₃(c+d)=P(c)−Q(c)`. Over F₃, a d-pair has:

- **two** B₃ points iff `P=Q=0`;
- **one** B₃ point iff both P and Q are nonzero;
- **no** B₃ points iff exactly one of P,Q is nonzero.

The statement is independent of which point of the d-pair is used as representative: changing representatives only changes the sign of Q.

By the f248 class equations, on y=1 the U₂-zero set is B₂ and the U₂/U₃ common zeros are exactly H and O blocks. Their number is

`p:=|B₂∩B₃|=16+g+2h`.                                        (2)

Let J be the number of the eleven B₂ d-pairs with exactly one B₃ point. Then

`J = #{v∈X: P(v)≠0 and Q(v)≠0 in F₃}`,
`J≡p≡g (mod 2)`, and `0≤J≤22−p=6−g−2h`.                     (3)

Here P(v),Q(v) mean evaluation at any representative of the quotient point. Equation (3) is a common-placement **and sign** condition: it is not implied by the separate class counts alone.

All nine y=1 f248 residuals have p≥16. Among eleven pairs there are therefore at least `p−11≥5` pairs with two B₃ points. If either nonempty atom group had size 1, its partial transform would be ±1 at every c and could never vanish on such a pair. Hence a nontrivial split has `2≤k≤8`. If all ten atoms had the same d-value, B₃ would be d-periodic and p even. Therefore odd g forces a nontrivial split.

For clarity, the complete J possibilities at this level are:

| `(g,h)` | `p=|B₂∩B₃|` | possible J |
|---|---:|---|
| (0,0) | 16 | 0,2,4,6 |
| (0,1) | 18 | 0,2,4 |
| (0,2) | 20 | 0,2 |
| (1,0) | 17 | 1,3,5 |
| (1,1) | 19 | 1,3 |
| (1,2) | 21 | 1 |
| (2,0) | 18 | 0,2,4 |
| (2,1) | 20 | 0,2 |
| (3,0) | 19 | 1,3 |

This is a table of consequences only: it does not assert the listed values are achievable with ten atoms or an actual Boolean function.

## 4. The extremal residual (1,1,2)

For `(y,g,h)=(1,1,2)`, (2) gives p=21 and (3) gives J=1. Therefore **ten** quotient points in X have `P=Q=0`, and the remaining unique quotient point has both partial transforms nonzero.

We now exclude a 3+7 split and derive an exact condition on a 2+8 split.

### 4.1 A 2+8 split has a forced difference and sign

Suppose one side has just two atoms a,b. Its transform modulo 3 vanishes exactly where their signed characters are opposite; this is an affine hyperplane of F₂⁵ because a≠b and `(a+b)·d=0`. It contains ten of the eleven points of X and misses the exceptional point.

For a nonzero linear form `ℓ(v)=w·v`, the numbers of X points on which ℓ=1, for `|w|=1,2,3,4,5`, are respectively

`6,6,4,4,10`.

This counts 3-subsets with odd intersection with the support of w; v=0 contributes zero. Taking the complementary affine hyperplane replaces each count by `11−count`. The **unique** affine hyperplane containing ten X points is `|v| odd`, and its one excluded point is v=0. Its normal is the all-ones character.

Consequently the two atoms obey

`a+b=p₁+⋯+p₅=⊕A₂`,                                         (4)

because six copies of the base a in `⊕A₂` cancel. At any c in the alignment pair v=0, their signed characters agree (their partial transform there is nonzero). Equation (4) and this alignment are invariantly stated: they do not depend on which representative c of the d-pair is chosen.

### 4.2 A 3+7 split is impossible

Suppose one side instead has three distinct atoms. Its partial transform is a sum of three ±1 characters, and it is 0 modulo 3 exactly when all three signed characters agree. It must vanish on ten X quotient points. Therefore each of two distinct character-ratio equality hyperplanes contains those same ten points of X. By §4.1 both would have to be the unique odd-parity hyperplane, so their nonzero normals would be equal. That forces two of the three atoms to coincide, a contradiction.

Together with §3, the remaining split sizes are `2+8`, `4+6`, or `5+5`. The 2+8 case also has the forced placement/sign condition (4). No feasibility is claimed for any of them. ∎

## 5. Limited control and what it does not prove

Choose independent `p₁,…,p₅,r_*∈R`, with `p_i·d=0`, `r_*·d=1`, and `h=p₁+⋯+p₅`. Take the six A₂ atoms `{0,p₁,…,p₅}` with all signs +. Form a **formal** ten-atom A₃ as follows, also all signs +:

- d=0 side: `{0,h}`;
- d=1 side: `{r_*+b,r_*+b+h : b∈{0,p₁,p₂,p₃}}`.

The ten atoms are distinct. At every weight-3 point of X, `χ_h=−1`, so **both** partial sums vanish; at the alignment point v=0 they are 2 and 8, both nonzero modulo 3. The two d-representatives then give t₃ values 10 and −6, exactly one divisible by 3. Thus this construction satisfies the eleven-pair condition of §4 and its 2+8 placement/sign conclusion.

It is **not** a model of the f248 residual: t₃ is zero at every odd-parity v, at least 32 of the 64 block points, whereas `(g,h)=(1,2)` requires `#{U₃=0}=21+3g=24`. Nor are the ternary block equations, other correlations or Boolean inversion supplied. This intended-reason failure shows the eleven-pair constraints alone do not close the case.

## 6. Residual and inputs

Within y=1, all nine f248 residuals remain open. For the extremal one `(1,1,2)`, a complete next step must treat the `2+8`, `4+6`, and `5+5` splits under the exact signed constraints, the full 24-point B₃ count, common ternary-block equations and all remaining nonzero-shift correlations, or construct an actual target. The y=3 f248 residuals, other fibres, m-values, ranks and the original problem are unaffected.

`P=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/`.

| Input | SHA-256 | LF | Exact scope |
|---|---|---:|---|
| `P/info-6-nl242-rank2-eightzero-114-sixatom-0610-obstruction-parent-v1.md` | `b46ebb966b0ba183d0b43d2ddba57c4c1bbdc7a174b3ccb83e50d836e01f1a23` | 24 | adopted f248 six-atom/class-count facts, including both mandatory errata |
| `P/info-6-walsh-caller-and-mod4-coupling-parent-v1.md` | `721222262af91bc768227ce8bfae563cabf5a102437ac55e6583de38ec2d3c9d` | 23 | original Boolean caller and common frequency space |

The cross-fibre pair criterion, hyperplane count, 3+7 exclusion, 2+8 placement/sign condition and limited control are author deductions requiring a fresh disjoint review. No computational replay, independent-model-family review, human check, formal verification, or novelty audit was performed. All historical STOP/HOLD/ZERO/NONINPUT controls remain binding.
