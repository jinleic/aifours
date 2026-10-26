# Sharp all-type ceiling when at most three Walsh magnitudes are4 or12

Clock observed before creation: **2026-10-23T14:34:03-07:00**. Author: InfoBalancedNL242, info-6. **CANDIDATE WRITTEN COROLLARY** of the pending sparse-defect manuscript, not a separately accepted theorem. No scientific execution, formal verification or novelty clearance.

## 1. One literal all-type statement

For every balanced Boolean function `f:F_2^9 -> F_2`, define the count over **all512 frequencies**

`L(f)=#{a in F_2^9: |W_f(a)| in {4,12}}`.

Then the proposed theorem is

`L(f)<=3  ==>  NL(f)<=240`.                                (1)

Moreover the upper bound is attained with L=0, so

`max {NL(f): f balanced on nine variables, L(f)<=3}=240`.    (2)

There is no fixed half, symmetry, support-XOR assumption, chosen residue type, zero-set shape or local-neighborhood restriction in this statement. It handles all seven remaining types simultaneously. However the multiplicity condition L<=3 is a **real restriction**: (1) is not the unrestricted balanced maximum.

This is the direct contrapositive/sharpness packaging of the same mod3 sparse-defect mechanism, not an independent discovery to count alongside it.

## 2. Upper bound, with every quantifier preserved

Suppose f is balanced and L(f)<=3. Every W_f is divisible by4: for a!=0, the linear function a.x has weight256, so

`W_f(a)=512-2 wt(f+a.x)=4 |supp(f) intersect {a.x=1}|-512`,

and W_f(0)=0. Thus NL(f)=256-(1/2)max|W_f| is an even integer. If (1) failed, NL(f)>240 would imply NL(f)>=242 and hence peak<=28.

Let `s=XOR_{x:f(x)=1}x`. Such a hypothetical peak28 target has s!=0 by the elementary balanced Parseval argument reproduced in `modular-saturation-protocol-v1.md` §3. Choose a split normal v with v.s=1, use coset origin s, and canonically normalize the two odd halves as in the corrected map in `zero-geometry/PROOF.md` §1. This creates S and the quadratic D, with

`|S|<=28`, `H_8 S in {0,+512,-512}`, `S=4+8D mod16`.

The reviewed residue bound in `quadratic-distance/SHARPER.md` plus D(0)=0 excludes polar rank zero. The sparse-defect manuscript, SHA256

`0325f3cf3d9131c8e11f524552a715e4ba47e2ff66eabc1010341f136af6c413`,

then gives at least four points with |S|=4 or12, at every possible positive polar rank.

The corrected spectral correspondence is

`S(b)=eta(b) W_f(a+v)`, `a in s-perp`, `b=B^T a`.

This bijectively covers the complementary256 frequencies. On s-perp the original coefficients are multiples of8, so none has magnitude4 or12. Therefore

`#{b: |S(b)| in {4,12}}=L(f)`,

contradicting L(f)<=3. This proves (1) subject to the actual independent reconstruction of the pinned sparse-defect proof and its stated imports.

## 3. Exact attaining function, proved symbolically

Use input coordinates `(x_0,...,x_7,t)` and define

`q(x)=x_0x_1+x_2x_3+x_4x_5+x_6x_7`,

`f_0(x,t)=q(x)+t` over F_2.

Each fixed x gives one output0 and one output1 as t varies, so f_0 is balanced. For each pair,

`sum_{u,v in F_2}(-1)^(uv+alpha u+beta v)=2(-1)^(alpha beta)`.

Multiplying the four independent pair sums gives

`W_q(a)=16(-1)^(a_0a_1+a_2a_3+a_4a_5+a_6a_7)`.

The t sum vanishes at frequency0 and equals2 at frequency1. Hence

`W_f0(a,0)=0`, `W_f0(a,1)=32(-1)^(a_0a_1+a_2a_3+a_4a_5+a_6a_7)`.

Thus f_0 has exactly256 Walsh zeros and256 coefficients of magnitude32, has L(f_0)=0, and has nonlinearity `256-32/2=240`. This is an exact classical bent-concatenation control, not this round's new construction. No executable Walsh check is used in this derivation.

Equations (1) and this attaining function yield the exact class maximum (2).

## 4. Stronger rank-eight corollary and exact residual union

The three pending small-defect manuscripts together say that a hypothetical balanced peak28 target must satisfy

| Intrinsic residue type | Necessary L(f) from these candidates |
|---|---:|
| (2,192) | >=4 |
| (4,160) | >=4 |
| (6,112) | >=4 |
| (6,128) | >=4 |
| (6,144) | >=4 |
| (8,120) | >=7 |
| (8,136) | >=7 |

The rank-eight extension therefore gives NL<=240 as well for a balanced f with nonzero s whose intrinsic quadratic `W_f/8 mod2` on s-perp has polar rank8 and L(f)<=6. No attainment for that narrower full-rank class is supplied here.

**The exact unresolved target is the union of all seven rows with the indicated lower multiplicities.** Neither the all-type condition L>=4 nor the rank8 condition L>=7 makes that union empty. The existing scalar slack/correlation constraints have no general upper bound L<=3 (or <=6 in rank8) that could complete the contradiction. Consequently:

- this packet gives a single sharp, all-type **multiplicity-constrained** ceiling240;
- it does **not** lower the unrestricted balanced maximum from {240,242};
- all seven residue types remain unexcluded as entire families;
- seven-defect full-rank support geometry is a genuine next obligation, not a consequence of this corollary.

## 5. Review and priority boundary

Parent explicitly requested this packaging while the mod3 packets are queued for review. The upper bound inherits their pending correctness gate; the elementary attaining function is proved above, not empirically tested. No source inspection clears novelty of the multiplicity threshold. This is one mechanism and one scoped contribution, with a classical sharpness control, not multiple new solved-problem counts.
