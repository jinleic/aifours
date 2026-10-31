# f263 independent Boolean-caller and cross-fibre review

Observed native clock before composing this review: **2026-10-29T15:56:47-0700 PDT**. Same-harness review; no human, independent-model-family, formal/kernel, or novelty claim.

## Verdict and exact scope

**Corrected composite:** no FATAL or MAJOR mathematical defect found at the explicit scope below. **Two MINOR findings:** (m1) the base's general even-atom parity formula is false, but the mandatory additive correction fixes it and both actual fibre sizes are unaffected; (m2) the frozen f244 disposition is credited with more explicit four-atom/class-table detail than its 24 LF actually state. The missing four-atom facts are derived below. The correction explicitly identifies `H` with the local `U0`-peak count; the 24-LF disposition names H without defining that class in the displayed record. Therefore the theorem is established under the correction's explicit local meaning of H; identity with any different, undisplayed historical class convention is **INCONCLUSIVE**, not silently imported.

Under that explicitly defined original-Boolean residual, the equal nonzero XOR, equal atom-sign product, all-translation intersection bound, and all-translation sign-mismatch restrictions **do follow as necessary conditions on the original Boolean function**, not merely on two assumed local systems. This is not a construction, exclusion of the residual, acceptance of any Boolean witness, or proof of the other six f244 pairs. Formal placement and exact controls below do not change that status.

| Claim | F/M/m/INCONCLUSIVE disposition | Exact dependency or limit |
|---|---|---|
| Boolean half-caller, both inverses, Fourier constants, parity of k | F=0, M=0, m=0 | Directly derived from f, balance, and the f244-adopted `T≠0`; no unprovided caller is imported. |
| Shared 64 blocks, local Parseval, `16U_s=3W(σ_s)−2t_s` | F=0, M=0, m=0 | Direct inverse on the **same** dual coordinates and even-fibre q values. |
| `U_s=0` iff `t_s=0 (mod 3)` for s=2,3; 24/23 zero counts | F=0, M=0, m=0 | Local ternary shape and independently derived four-atom rank; 23 uses f244's `20+3G3` count at `G3=1`. |
| 17 common zeros | F=0, M=0, m=0 mathematically; see m2 | Requires the explicit residual definition `H=#{|U0|=4}=0`, which correction supplies but f244 does not spell out as a definition. |
| Eight-atom form, unique hyperplane, and two-point flat direction | F=0, M=0, m=0 | Import f244's weight-four/even-syndrome relation; derive affine rank six from the odd 23 count, and reconstruct the geometry below. |
| General atom parity | m1 in unchanged base; corrected in composite | For even e the missing term is `e/2`; it is even for e=4,8. |
| Equal nonzero XOR and sign product | F=0, M=0, m=0 | Original Boolean caller, common zero count, signed-atom geometry and corrected parity; not a free-standing placement hypothesis. |
| Intersection ≤2 for every translation | F=0, M=0, m=0 | Geometry plus a genuine change of complement for the same Boolean object, including the sign obstruction for the outer four. |
| Sign-mismatch conditions for every translation | F=0, M=0, m=0 | Divisibility in the same local system and the same complement shear. |
| Source attributions / residual class meaning | m2; historical-label equivalence INCONCLUSIVE | The full Boolean inverse and four-atom facts are reconstructed here. H is explicitly defined as the local `U0`-peak count in the correction; f244 alone does not give its block-class table. |
| Existence, exclusion of residual, six other pairs, all other patterns, global target, novelty | INCONCLUSIVE | These are outside the proven necessary-conditions statement. No formal placement is promoted to a witness. |

No f255 verdict is a premise. The correction includes a historical exposure statement, but its verdict and prior execution claims are not adopted here.

## Frozen input and read discipline

Manifest `manifest-v1.json`: SHA-256 `a226dfeab1f9d13612c1c68d6ee6e2ebe1a20bd71e80e614e57c8ea6f5834c6a`, verified before reading the manifest. Before any mathematical input body was displayed, all three source hashes, byte counts and LF counts were verified, in manifest order:

1. `institute/runs/three-area-2026-10-27-96h/dispositions/info-6-nl242-rank2-eightzero-116-fibre-048-obstruction-parent-v1.md`: `18403a17269311682255e3bb9823a89a0a69cd7344a66ad02bdd841bcc52f912`, 4,246 bytes, 24 LF.
2. `information-science/evidence/three-area-20261023-96h/parallel-18/balanced-nl242/successor-20261029-f255-boolean-local-normalization-correction-v1.md`: `e0c3f4807732d6cd70d47485f1692366c0f77abfd1c5169e7a5782114bfddcf4`, 12,388 bytes, 151 LF.
3. `information-science/evidence/three-area-20261023-96h/parallel-18/balanced-nl242/successor-20261029-f244-residual-cross-fibre-placement-v1.md`: `686dd9177d6ff8788b6463d8d4e444e8bda4231ce7060a76ad0cfdea5f39144c`, 13,894 bytes, 183 LF.

All three bodies, including final lines, were read completely in that order in raw windows of at most 15 LF, correction before base and before mathematical reasoning. The named but unprovided caller disposition, f255 review, linked author sources, held/withdrawn materials and author code were not opened. Source-hash verification is not a claim that their prior reviews were independently replayed.

## 1. Full original Boolean inverse and caller

Let `S={x:f(x)=1}`, `s(x)=(-1)^f(x)`, `T=⊕_{x∈S}x`, and let `W(a)=Σ_x s(x)(−1)^(a·x)`, `k(a)=W(a)/4`. Balance gives `|S|=256`. Put `N_a=#{x∈S:a·x=1}`. For all `a∈F2^9`, including zero,

`W(a)=512·1_{a=0}−512+4N_a`, hence `k(a)≡a·T (mod 2)`.

Thus `K=T^⊥` is exactly the even-k half. The target uses the f244-adopted `T≠0`, so dim K=8. Choose `a0·T=1`, set `V=a0^⊥`, and write every x uniquely as y or y+T for y∈V. Define **both** pair functions

`u(y)=(s(y)+s(y+T))/2`, `v(y)=(s(y)−s(y+T))/2`.

They are ternary and satisfy `u(y)^2+v(y)^2=1`, `u(y)v(y)=0`, `s(y)=u(y)+v(y)`, `s(y+T)=u(y)−v(y)`. For the actual target, `Σ_y u(y)=0`, `Σu²=m=116`, `Σv²=140`. Identifying K with V* and using **unnormalized** transforms,

`Walsh_V(u)(a)=W(a)/2=2k(a)`,
`Walsh_V(v)(a)=W(a0+a)/2=2k(a0+a)` for all a∈K,

and the complete inverse, with no omitted factor, is

`u(y)=(1/128)Σ_{a∈K} k(a)(−1)^(a·y)`,
`v(y)=(1/128)Σ_{a∈K} k(a0+a)(−1)^(a·y)`.

Equivalently `s(x)=(1/128)Σ_{a∈F2^9} k(a)(−1)^(a·x)`. In particular the exact full-spectrum Boolean caller, obtained by squaring this inverse, is

`Σ_{a∈F2^9} k(a)k(a+b)=2^14·1_{b=0}` for every b.

This explicitly includes all nonzero shifts; it is not inferred from the separate fibre conditions. If trying to construct f from u and v, one must also preserve their complementary pointwise supports, balance, the Walsh cap on **both** halves, and that the reconstructed XOR is the selected T. For example, since `Σu=0` and `m=116`, the 58 negative u-pairs and the 140 split pairs give

`⊕_{x:f(x)=1}x = (⊕_{y:u(y)=0} y) + (58+#{y:v(y)=1} mod 2)T`.

The left side must equal T. This is a caller constraint, not a claimed new solution.

For completeness, the original quadratic can also be reconstructed without reading a caller file. On K set `q(a)=k(a)/2 mod 2`. Its polar is

`B(a,b)=Σ_{x∈S}(a·x)(b·x) mod 2`,

because `N_{a+b}=N_a+N_b−2#{x∈S:a·x=b·x=1}`. It is alternating on K since `B(a,a)=a·T=0`. The exact f244 scope supplies rank B=2, `q|R=0` and z=64 q-zero positions; because dim R=6 this forces `q^{-1}(0)=R`. Choosing a linear complement P yields K=R⊕P and q=1 on each of the three nonzero P fibres. The bound |k|≤7 gives k∈{0,±4} on R and k∈{±2,±6} on nonzero fibres; the eight W-zero positions are in R. Relabel the nonzero fibres so `(e1,e2,e3)=(0,4,8)`.

## 2. One shared local system and its constants

Use the single dual decomposition `V=R*⊕P*`; write y=(c,z). For every `s∈P`, define `U_s(c)=Σ_{z∈P*}u(c,z)(−1)^(s·z)`. Then, for the same 64 c in **every** fibre,

`u(c,z)=(1/4)Σ_s U_s(c)(−1)^(s·z)`,
`Σ_s U_s(c)^2=4Σ_z u(c,z)^2`,
`Σ_c U_s(c)(−1)^(r·c)=2k(r,s)`.

For nonzero s, define `A_s={r:|k(r,s)|=2}`, `σ_s(r)=sign k(r,s)` and `τ_s=σ_s 1_{A_s}`. Then `k(r,s)=2σ_s(r)(3−2·1_{A_s}(r))`; with `t_s=Walsh_R(τ_s)`, 64-point inversion yields

`U_s=(12 Walsh_R(σ_s)−8t_s)/64`, hence `16U_s=3 Walsh_R(σ_s)−2t_s` and `U_s≡t_s (mod 3)`.

Here neither `σ2` nor `σ3` has an independently chosen transform domain. Parseval with these exact constants gives `ΣU0²=56` and `ΣUs²=144−2e_s`, namely 144, 136, 128 for s=1,2,3.

Since e1=0, `U1≡0 mod 3`; its ternary four-point range is [−4,4]. Thus U1 is 0 or ±3, and energy gives exactly 16 nonzero blocks. In a ±3 block there are exactly three nonzero ternary entries and `|U0|=|U2|=|U3|=1`. In each of the other 48 blocks U1=0 and the transform has one of the three forms: all zero; exactly two entries ±2; or exactly one entry ±4. Consequently neither U2 nor U3 can be ±3, and their allowed values imply

`U_s(c)=0  ⇔  t_s(c)≡0 (mod 3)` for s=2,3.

## 3. Four-atom structure and 17 common zeros without an unstated table

Four distinct A2 atoms have affine rank 2 or 3. If they form a plane and their sign product is +1, t2 has 48 zeros and 16 values of magnitude 4. All 48 U1=0 blocks would then have U2=0, because the 16 U1≠0 blocks have |U2|=1; this contradicts `ΣU2²=136`. If the plane sign product is −1, t2 has magnitude 2 at all 64 points, so U2 is nonzero everywhere; the 48 even blocks contribute at least 192 and the 16 odd blocks contribute 16, again contradicting 136. Hence A2 has affine rank 3. Its transform has 24 zeros, 32 values of magnitude 2 and eight values of magnitude 4. Define

`H2={c:t2(c)≡0 mod 4}`, `F2={c:|t2(c)|=4}`.

Then H2 is an affine hyperplane, F2 is an affine 3-flat contained in it, and `{U2=0}=H2\F2`. This derives the four-atom result rather than assuming the f244 disposition literally displays it.

At the frozen G3=1 scope f244 states `#{U3=0}=20+3G3=23`. With the 16 magnitude-one blocks and the even-block shapes, the energies and zero counts force two |U2|=4 peaks and one |U3|=4 peak. Among the 48 U1=0 blocks let a,b,c count pairs of ±2 in slots (0,2),(0,3),(2,3); let d count |U0|=4 peaks and o all-zero blocks. The energies and block count give

`a+b+4d=10`, `a+c=22`, `b+c=24`, `a+b+c+d+o+2+1=48`,

so `a=4−2d`, `b=6−2d`, `c=18+2d`, `o=17+d`. A common U2/U3 zero is exactly a U0 peak or an all-zero block, so there are `d+o=17+2d`. The correction explicitly identifies the residual class count H with d. Therefore for its H=0 residual there are **17** common zeros. This is the exact local definition used throughout the review; f244's 24 LF use H as a class name without displaying its defining table (m2).

## 4. Eight atoms, unique hyperplane, parity and XOR/sign equality

The 23 U3 zeros give 23 zero-mod-3 t3 positions. If the affine rank of A3 were <6, translation by its nonzero difference-space annihilator would preserve the zero-mod-3 set, forcing its size even. Hence A3 has affine rank 6. Eight points then have a unique nontrivial affine relation. The f244 scoped fact imported here is that this relation has weight 4 and even sign syndrome. Consequently one may choose a base atom a and independent `p,q,b1,b2,b3,b4` with

`P={a,a+p,a+q,a+p+q}`, `A3\P={a+b1,a+b2,a+b3,a+b4}`,

and product of the four signed atoms on P equal to +1. After absorbing sign offsets into affine block coordinates `u=(p·c,q·c)`, `v=(b1·c,...,b4·c)`, and an irrelevant overall ± character,

`t3(c)=±χ_a(c)[4·1_{u=0}+Σ_i (−1)^{v_i}]`.

Thus

`B3={t3≡0 mod 3}={(u,v):u≠0, |v|=2} ∪ {(0,v):|v|=1 or 4}`,
`H*={|v| even}`, `|B3|=23`, `|B3∩H*|=19`.

For the unnormalized transform of 1_B3 at (α,β), the coefficient equals `(3 if α=0 else −1)K2(|β|)+K1(|β|)+K4(|β|)`, where `K2=(6,0,−2,0,6)` and `K1+K4=(5,1,1,−3,−3)`. Its sole nontrivial coefficient of magnitude ≥11 is +15 at `(0,1111)`. A hyperplane containing ≥17 B3 points needs coefficient magnitude ≥`2·17−23=11`. The 17 common zeros lie in `H2\F2`, so H2 must be H*, and `|F2∩B3|=19−17=2`.

For **any even** number e of signed atoms, let n− be the number of negative signs and X the atom XOR. Expanding the signs and characters modulo 4 gives the corrected identity

`t(c)/2 ≡ e/2+n−+X·c (mod 2)`.

For e=4 and e=8, e/2 is even. Hence the zero set of this parity expression is H2 for fibre 2 and H* for fibre 3. They are equal nonconstant affine hyperplanes, so their linear and constant parts agree: `X2=X3` and `n2−≡n3− mod 2`. Equivalently `Π2=Π3`. Further `X3=b1+b2+b3+b4≠0`, since P XORs to zero and the six differences are independent. For the intended-reason negative, two positive atoms at c=0 have t/2=1 but the base's shortened expression gives 0; this is m1, repaired by the correction.

## 5. Geometric line and every translated overlap

Let `d∈R*` be the direction `(Δu,Δv)=(0,1111)`, and write `L={0,1111}` inside the even-weight v-space. There,

`B3∩H*=((F2²\{0})×(V_even\L)) ∪ {(0,1111)}`.

Let F be any affine 3-flat of H* meeting B3 in exactly two points. If its u-projection has dimension 0, its single eight-point fibre meets B3 in 1 or 6 points. If the projection has dimension 1 and neither u value is 0, both four-point fibres contribute at least two points. Otherwise the nonzero-u four-point fibre must contain L, and its two other points differ by 1111. If the projection has dimension 2, its four fibres are parallel lines; a direction other than L forces at least one B3 point in each of the three nonzero-u fibres. With direction L, the two points must be one nonzero-u fibre disjoint from L. Thus in every possible case the two intersection points differ by d, so `d∈dir(F2)`.

All four signed A2 characters align on F2. Their pairwise ratio characters are constant on F2, so all A2 atoms have the same dot product with d. The plane P atoms have value a·d, and the four outer atoms have value a·d+1. Thus A2 cannot meet both groups. Three plane atoms would fix both u coordinates on F2, contradicting the dimension-0 case. If A2 contains three outer atoms, equal XOR forces its fourth atom to be the fourth outer atom. In that remaining possibility, the product of A2 signs equals the product of the outer A3 signs, since the plane sign product is +1. Its alignment flat is `F2²×{v0,v0+1111}` with v0 even. It meets B3 in 1 point if v0∈L and 6 otherwise, contradicting `|F2∩B3|=2`. Therefore `|A2∩A3|≤2`.

For an arbitrary t∈R choose the linear map L:P→R with `L(2)=t`, `L(3)=0`, and replace P by its graph. This changes coordinates on the **same** k and same f:

`k'(r,s)=k(r+L(s),s)`, `A2'=A2+t`, `A3'=A3`,
`σ2'(r)=σ2(r+t)`, `σ3'=σ3`, `U_s'(c)=(−1)^{L(s)·c}U_s(c)`.

The corresponding dual z-coordinate is translated by the functional `c∘L`. Thus the ternary blocks are only permuted, all |U_s| and zero conditions, e-values, m and the local G3/H residual are unchanged. Applying the just-proved geometric argument after this actual shear establishes

`|(A2+t)∩A3|≤2` for **every** t∈R.

## 6. All-translation sign-mismatch conditions

For s=2,3, t_s is even. The identity `16U_s=3W_s−2t_s`, with `W_s=Walsh_R(σ_s)`, first gives `W_s≡0 mod 4`; reduction modulo 8 then gives `W_s/4≡t_s/2 mod 2`. Because the latter parity bits have the same zero hyperplane, they agree everywhere, so `W_2≡W_3 mod 8` at every c.

For `d0=(σ2−σ3)/2`, its Walsh transform is divisible by 4. At c=0 this yields `Σ_r d0(r)≡0 mod 4`. Reducing the character sum modulo 4 at arbitrary c shows `Σ_r d0(r)(r·c)` is even for all c. On its support d0 is ±1, therefore the XOR of that support is 0. Applying the same actual shear gives, for every t,

`d_t(r)=[σ2(r+t)−σ3(r)]/2`,
`Σ_r d_t(r)≡0 (mod 4)`, `⊕_{r:d_t(r)≠0}r=0`.

## 7. Formal placement, independent controls, and remaining gap

The author's formal placement has A3=`{0,p,q,p+q,b1,b2,b3,b4}` with positive signs and A2=`{0,p,q+b1+b2,p+q+b3+b4}` with signs `(+,+,−,−)`. The displayed F2 equations really give two B3 intersections; the independent control checks all 64 translates and the sign extension. But the proposed sign extension has `Walsh(σ2)(0)=56`, t2(0)=0, forcing `U2(0)=168/16`, and `Walsh(σ3)(0)=64`, t3(0)=8, forcing `U3(0)=11`. The former is nonintegral and the latter exceeds the four-point range. It is **not** a local-block or Boolean realization.

Own final bounded control: `reviewer-control-v1.py`, SHA-256 `f6a5b724a9f0e47ea7c9546fe6df26c38e9b2c30466677e4126ca78e1dfb8176`; Python 3.14.3; native start `2026-10-29T15:55:48-0700 PDT`, end `2026-10-29T15:55:49-0700 PDT`, real process exit **0**, `/usr/bin/time` real 0.08 s, 110-second in-process alarm and 120-second outer deadline. It used no author code, solver or linked sources. It checked all 81 ternary blocks and 324 block relabellings; all 32 sign patterns on independent/plane four-atom controls; the 23-point B3 and unique ≥11 Fourier coefficient; all 620 affine 3-flats of H* (intersection histogram `{1:2,2:18,3:57,4:228,5:90,6:210,7:6,8:9}`), including all 18 two-point cases; and all 64 translates of the formal support/sign placement. Intended negatives caught the missing general parity offset, the four-outer-atom overlap, and the noninteger/out-of-range U values. A separate constructed balanced Boolean with `T=256`, m=116 checked both 256-point inverses, shared block transforms and all 512 full-caller shifts; its max |W| was **276**, so it is explicitly not a bounded target or witness. Synthetic fibre arithmetic also checked the 16U normalization at all 64 characters.

**First remaining mathematical gap:** determine whether any placement satisfying these necessary conditions extends simultaneously to a common ternary u, the local equations and an odd-half v satisfying the full Boolean caller, XOR consistency, all Walsh bounds, eight-zero/rank/fibre constraints. Neither that existence nor nonexistence follows here. Parent adoption also needs to keep the displayed H definition explicit and resolve historical-label equivalence if relying on an undisplayed class table; no such table was read in this review.
