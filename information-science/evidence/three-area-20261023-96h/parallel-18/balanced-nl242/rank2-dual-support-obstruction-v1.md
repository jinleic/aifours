# Rank-two nonfull-dual-support obstruction: balanced type(2,192) needs L>=12

Observed before creation: **2026-10-24T03:29:26-07:00**. Author: InfoBalancedNL242, retained info-6. **CANDIDATE WRITTEN PROOF**, with no scientific executable, arithmetic interpreter, Walsh replay, solver, enumeration or formal kernel.

This is one genuine simultaneous S/R dual-support argument for the lower-rank branch. It is not an application of a full-rank formula to a rank-two quadratic, a scalar-feasibility vector treated as a function, or another full-rank per-defect appendix. The preceding assigned AME review was completed and returned before this primary work.

## 1. Literal theorem and scope

Let K_g,K_h be genuine canonical spectra of odd-weight Boolean functions on V=F_2^8. Write

`S=K_g+K_h`, `R=K_g-K_h`, `p=R/8`, `D=p mod2`,

and assume `|K_g|+|K_h|<=28` pointwise. Suppose D has polar rank2 and weight192. Define

`L=#{a in V:|S(a)| in {4,12}}`.

**Theorem P2 (candidate).** If R has at least one zero, then `L>=12`.

The zero hypothesis is explicit. A balanced nine-variable peak<=28 target of the intrinsic type(2,192) supplies it, and the complete target bridge is rederived in §8. In that application L counts **all512 original Walsh coefficients of magnitude4 or12**. Thus every such target in this entire residue type must have at least12 of them.

The type itself is NOT excluded: L>=12 remains open. No balanced242 truth table, unrestricted ceiling240, changed best attaining balanced value or full book solution is claimed.

In fact the proof excludes L=0,4,8 even before using R's zero except to force L to be a multiple of4. No gate from the pending earlier smaller-L chain is needed for Theorem P2.

## 2. Exact sources and checked finite-support import

The canonical identities are those in the actual historical source

`information-science/evidence/hard-continuation-20261015/proof.md`,

observed SHA256 `d2c1605d8ee20423e137066b62b3dac31406bd4380d075c1b85064c01cf6dff9`, §§2,4. The corrected balanced split was freshly read in `quadratic-distance/PROOF.md` §6, observed SHA256 `caf7db55c93a6b3fc73d461fd4dc018f387ec510adf29417605ee4e3e71730b5`; it is also fully spelled out here.

The only previously checked nontrivial support-code input is the **universal signed-eight-point affine-dimension/relation tables**, in

`joint-profile-realizability-v1.md`, SHA256 `5bbe53363d8a485d3cd9b4f3840d8691433e8cd1aef414eb9902b86f0ea32822`,

with erratum `28fad30f9393ba907c8ef24f002d0990221aa958eb9a0e87502c19e4168fbd47`, actual reconstruction `a389df9df8ab1858fd59e3770d0c0ea2f7817ebf39d2cbf0599532699c3eb9a7`, and operative parent record `585e5e2b934e3bc3953cd33c83078fab7ba73320f2b9946dc3c0e216ada7ba85`.

**I do not import the full-polar-rank m=224 boundary into this rank-two problem.** I use only the auxiliary signed-eight-point spectrum restrictions, valid for every signed eight-point support, independently of D's rank. The four-point signature used here is proved afresh in §6. All inputs retain written-check, nonformal, novelty-uncleared boundaries; none pre-accepts the new argument.

## 3. Actual Boolean transforms, magnitudes and parity

Let H be the unnormalized256-point Walsh transform. Genuine canonical spectra satisfy

`K_g=K_h=2 mod8`, `H K_g,H K_h in {+256,-256}` pointwise.

Their squared low bits are quadratic, so D is quadratic. More explicitly write K_g=2+8t_g,K_h=2+8t_h; then `D=t_g-t_h mod2=J_g+J_h`. It follows that

`S=4+8D mod16`, `R=8D mod16`.

The cap makes R belong to0,±8,±16,±24. Put

`z=#{R=0}`, `c=#{|R|=8}`, `u=z+2c`, `d=wt(D)=192`,

`Gamma=sum_a (-1)^D(a) S(a)`.

Exactly as integers,

`sum R^2=65536+320d-256u=126976-256u`.

Also H S and H R have complementary supports and their nonzero values are±512. Therefore

`w_R=|supp(H R)|=sum R^2/1024=124-u/4`,

`w_S=|supp(H S)|=132+u/4`.                                (1)

If R(a_0)=0, Fourier inversion gives

`0=R(a_0)=2 sum_x ((H R)(x)/512)(-1)^(a_0.x)`.

Every nonzero summand is±1, so w_R is even. Equation(1) consequently forces

`u in 8Z`.                                               (2)

This is where the zero hypothesis is used; it is not a conclusion from a count vector alone.

For chi=(-1)^D, put T=chi*S. Its four actual values are-28,-12,4,20. Hence

`T^2+8T=560-512*1_{|S| in {4,12}}`.

The two genuine Boolean Parseval identities give `sum(S^2+R^2)=262144`. Summing the displayed identity and substituting sum R^2 yields

`Gamma=1024-64L-32u`.                                    (3)

Because D has polar rank2, its quadratic spectrum W_D=H chi has exactly FOUR nonzero coefficients, each of magnitude128. Thus

`Gamma=(1/256)sum_x W_D(x)(H S)(x) in256Z`.

Together with(2),(3), this proves

`L in4Z`.                                                (4)

These identities retain arbitrary signs, positions and nonnormalizations of the four-point quadratic Walsh support. They do not assume a convenient cofactor or fixed truth-table half.

## 4. The nonfull quadratic-dual support must be treated correctly

Let `U=supp W_D`, so |U|=4, and define

`q=phi(W_D)=-W_D/128` on U, with q=0 outside U,

where phi selects0,±1 modulo3. The minus sign is essential because128=-1 modulo3. Unlike the full-rank situation, **q is zero at252 positions**.

Define the signed defect function delta by

- delta=chi where T=-12;
- delta=-chi where T=4;
- delta=0 otherwise.

Then delta has exactly L nonzero entries±1, and `S=-chi+delta mod3`. Set

`b=phi(H delta)`, `m=wt(b)`, `B=(H S)/512`.

Since512=-1 modulo3, and B already lies in0,±1, the actual transformed congruence gives

`B=phi(q-b)`.

Outside U, this is `B=-b`. Inside U, q=±1 and the three cases are

`b=0 -> B=q`, `b=q -> B=0`, `b=-q -> B=-q`.

Put

`alpha=#{x in U:b(x)=q(x)}`, `nu=#{x in U:b(x)=-q(x)}`.

Thus `alpha,nu>=0`, `alpha+nu<=4`, and the number of nonzero B entries inside U is4-alpha. Counting the actual outside support gives

`m=w_S-4+2alpha+nu`.                                     (5)

The quadratic correlation is now

`Gamma=-256 sum_(x in U)q(x)B(x)`

`=-256(4-alpha-2nu)`.

Equating this with(3) gives the exact occupancy relation

`alpha+2nu=8-L/4-u/8`.                                   (6)

Finally combine(1),(5),(6):

`m=144-L/2-3nu`.                                         (7)

This is a simultaneous, common-coordinate Fourier-support identity. It is not the old full-rank m formula, not a mere scalar Parseval relaxation, and not a choice of b signs independent of a genuine S/R pair. It tracks the252 positions where the quadratic transform is actually zero.

## 5. L=0 is impossible

If L=0 then delta=b=0 and m=0. On U both alpha and nu are0. But(7) gives m=144. This contradiction excludes L=0.

## 6. All signed four-point spectra, and exclusion of L=4

For a signed four-point delta on F_2^8, the support has affine dimension2 or3.

- At dimension2 it is a full affine plane. If the four signs have positive product, they form an affine sign character, so the local transform has exactly one coefficient±4 and three zeros. The ambient ternary support has size64. If the product is negative, the local sign has its nondegenerate quadratic term on the binary two-space; all four local Walsh values have magnitude2. The ambient ternary support has size256.
- At dimension3 the four points are affinely independent. Affine sign modulation removes every sign pattern because affine-character restrictions have rank4 on those four points. With one point translated to0, the local transform is1 plus three independent signs. Its eight values are4-2j with binomial multiplicity binom(3,j), j=0,1,2,3. Only j=2 is zero modulo3, so five of the eight are nonzero modulo3. Ambient repetition by32 gives160.

Therefore the exact necessary signature is

`wt(phi(H delta)) in{64,160,256}` for four support points. (8)

This argument covers every affine placement and all sign patterns and is written finite character algebra, not an executable enumeration.

At L=4, equation(6) and u>=0 give `2nu<=7`, so nu is at most3. Equation(7) then puts m in the outer set

`{142,139,136,133}`,

which is disjoint from(8). Thus L=4 is impossible.

## 7. Checked eight-point signatures and exclusion of L=8

The previously checked signed-eight-point tables give the following **outer necessary set** of m values, not an assertion that every listed value is attainable:

`M_8={32,80,104,116,128,152,164,170,176,188,200,224}`.         (9)

For transparency this set is obtained from the exact affine-dimension cases as follows:

- dimensions3/4: m is a multiple of16, m<=256, and Parsevalmod3 gives m=2 mod3; the resulting outer list is32,80,128,176,224;
- dimension5: the four even-relation weight triples and every sign character give104,128,152,176,200,224;
- dimension6: one even relation of weight4/6/8 and both signs give116,152,164,176,188,224;
- dimension7: no even relation gives170.

Only the universal signed-support tables are used here. In particular **m=224 is NOT assumed for the rank-two pair**.

At L=8, equation(6) and u>=0 give `2nu<=6`, hence nu<=3. Equation(7) requires

`m in{140,137,134,131}`,

none of which is in(9). Thus L=8 is impossible for every actual placement/sign configuration.

Now(4) says L is a nonnegative multiple of4, and §§5–7 exclude0,4,8. Therefore **L>=12**, proving Theorem P2. This conclusion does not depend on acceptance of the earlier generic L>=4 proof or the full-rank smaller-L chain.

## 8. Complete bridge to balanced nine-variable functions

Let f:F_2^9->F_2 be balanced with peak<=28 and support XOR s. The elementary support expansion gives

`W_f(a)=4(a.s) mod8`.

For completeness s is nonzero: if s=0, W_f is divisible by8 everywhere. The integer character expansion makes `q=W_f/8 mod2` quadratic. Indeed every integer multilinear coefficient of degree>=3 has an extra factor16, and pointwise divisibility by8 also makes its lower coefficients divisible by8. Since q(0)=0, the nonzero quadratic1+q has weight at least128 (the elementary degree-two minimum-weight argument). At least128 Walsh values would then have magnitude<=16, and all others magnitude<=24, contradicting

`sum W_f^2<=128*16^2+384*24^2=253952<262144`.

Choose a normal v with v.s=1, V=ker(v), and any linear basis map B_0:F_2^8->V. Use s as the complementary-coset origin and put

`g(y)=f(B_0y)`, `h(y)=f(B_0y+s)`.

The parity of h's support is v.s=1, so h has odd weight; balance makes g odd too. The global support XOR equation is

`s=B_0(sigma_g+sigma_h)+(wt(h) mod2)s`,

so the eight-coordinate half-support XORs agree: sigma_g=sigma_h=sigma.

Their canonical phases are opposite because their weights sum256:

`epsilon_h=-epsilon_g`, `epsilon_j=(-1)^((wt(j)+1)/2)`.

Consequently canonical normalization gives

`K_g=eta G`, `K_h=-eta H_half`, `eta(b)=epsilon_g(-1)^(b.sigma)`.

The full peak cap is equivalent to `|G|+|H_half|<=28` at every half-frequency, so it supplies the cap in Theorem P2. For a in s-perp and b=B_0^T a,

`R(b)=eta(b) W_f(a)`,

`S(b)=eta(b) W_f(a+v)`.

Here v is THIS specific split normal. The restriction map is bijective: its kernel in the nine-dimensional dual is span(v), while v is not in s-perp. The first identity gives R(0)=epsilon_g W_f(0)=0. The second covers the other256 original frequencies. Coefficients on s-perp are multiples of8 and contribute no magnitudes4 or12, so L in Theorem P2 is exactly the count over **all512** original coefficients.

Finally D=R/8 mod2 is the intrinsic W_f/8 residue on s-perp, up to that proved linear coordinate map; signs do not change its parity. Thus an intrinsic type(2,192) balanced peak28 target satisfies every theorem hypothesis, without fixing a half table, and must have **at least12** original Walsh coefficients of magnitude4 or12.

## 9. Exact archived profile consequence and current residual

The actual preserved `remaining-types/result.json`, freshly read at its `(2,192)` statistics and observed SHA256 `5548853b6be9c2af0d251afe2ca4101c4b70437fdda19e1d5c21977e4aa16d2c`, records

`z=40`, `c=0`, `L=8`, `w_R=114`, `Gamma=-768`.

Its actual canonical count vector is in `results/explore.json.gz`, SHA256 `1e1470a7d5380bb61ac5ebb95221f531c44fdd67f53a3463fe7e4fc3c98d5136`, member `explore.json`. No producer/audit was rerun.

For any genuine realization of those multiplicities, u=40, so(6) gives alpha+2nu=1, forcing alpha=1,nu=0. Equation(7) forces m=140, excluded by(9). Thus the exact archived rank-two vector is impossible in every genuine spatial placement, independently of treating its scalar-audit PASS as Boolean evidence.

More importantly, the proof excludes the entire balanced type(2,192) L<=8 boundary, not merely that vector. If this new packet passes actual reconstruction, the earlier four archived vectors not eliminated by the joint-profile check would reduce to three not eliminated by this argument: `(6,112),L17`; `(6,128),L17`; `(8,120),L10`. These are count vectors, not functions or an exhaustive feasible universe.

**Seven entire types remain unexcluded**, including(2,192) with L>=12. The other lower-rank types and all larger L values remain open. The full-rank exactly-L8 obstruction retains its own separate parent disposition, and no L>=9 consequence is promoted without its separate smaller-L gate. No unrestricted balanced maximum or literal512-bit242 witness is supplied.

This is one new lower-rank joint-dual-support proof, not several independent discoveries counted from its identities, auxiliary signatures and profile corollary. Worldwide novelty, significance, formal/human/cross-vendor proof and parent acceptance are unestablished. Actual separate reconstruction at the fixed bytes is required next; no scientific execution or new native admission is authorized or queued.
