# Uniform partial-Parseval obstruction, its fixed physical consumer, and the general-rank-two gap

**NONBLIND GENERAL-AUTHOR CANDIDATE; UNADOPTED.** I independently derive the larger-class obstruction of packet S1, including its numerical energy and parity equalities, and apply it to every compatible `y` for the single corrected physical `x` of S1/S2. I also construct a *different*, actual four-distinct-D0, all-U0-capped `x` with a physical `J=1` completion for which the four graph-character restrictions are **all distinct**. That completion fails U3, so it is a counterconfiguration to automatic applicability of the lemma, **not** a U0/U3 witness or a refutation of a possible separate global no-go. A complete no-J1/all-U3-caps proof is claimed only for the one corrected S1/S2 `x`, not for this other `x`, any whole branch, V, or the original Boolean problem. This written candidate needs a full parent read and separate disposition.

## 1. Exact larger-class lemma and notation

All vector spaces are over F2. Put `j,b in F2^2`, `h,ell in F2`; let `f_j in F2` be arbitrary with `sum_j f_j=1`. Let real `y` on the 64 points satisfy, for signs `sigma_j,d_{j,b}` and covectors `kappa_j in (F2^2)*`,

* `y(1,f_j,j,b)=g_j(b)=sigma_j (-1)^{kappa_j(b)}` for all 16 graph points;
* `y(1,1+f_j,j,0)=0` and `y(1,1+f_j,j,b)=2 d_{j,b}` for `b != 0`;
* every `kappa` occurs an even number of times among the four rows;
* `sum_c y(c)^2=128`, and every unnormalized Walsh coefficient `yhat(xi)=sum_c y(c)(-1)^{xi(c)}` is congruent to 4 modulo 8.

No form is imposed on the `ell=0` values except what these global assumptions imply; in particular, this is not a hidden enumeration of the original 24-sign system. **Claim:** the 64 inequalities `|yhat(xi)|<=12` cannot all hold.

For `s in F2`, `alpha,beta in (F2^2)*`, set

`A_l(s,alpha,beta)=sum_{h,j,b} y(l,h,j,b)(-1)^{s h+beta(j)+alpha(b)}`.

The two full coefficients over a fixed triple are `A_0+A_1` and `A_0-A_1`. Thus, for real `A_0,A_1`, their larger absolute value is exactly `|A_0|+|A_1|`; their being two distinct frequencies matters throughout the counting below.

## 2. Independent proof, including every slice and extremal case

Let `n` count negative `d_{j,b}` among the 12 mate signs. The graph contribution to `A_1` is `4` times a signed sum over the rows with `kappa_j=alpha`, hence is divisible by 8 by the even-multiplicity assumption. In the mate sum, the product of the 12 character signs is `(-1)^s`: `sum_j 3j=0`, `sum_{b!=0} 4b=0`, and `sum_j 3(1+f_j)=1` in F2. Therefore the negative mate-term parity is `n+s`, and

`A_1(s,alpha,beta) = 4(n+s) (mod 8)`.                                      (2.1)

The two full coefficients are each 4 modulo 8. Their half-sum and half-difference therefore give `A_0,A_1 in 4 Z` with opposite residues modulo 8: in the slice `s=n (mod 2)`, `(A_1,A_0)=(0,4) (mod 8)`; in the other slice they are `(4,0) (mod 8)`. If all full caps hold, `|A_1|<=12`; consequently the first slice has `A_1 in {0,+8,-8}` and the second has `A_1 in {+4,-4,+12,-12}`. These ranges follow from the actual pair of full coefficients, not from assigning either partial transform freely.

Full Walsh Parseval gives `sum_xi yhat(xi)^2=64*128=8192`. Under the residue and cap every coefficient has absolute value 4 or 12. If `K` coefficients have magnitude 4, then `16K+144(64-K)=8192`, so **K=8**. Let `E` be the number of the 16 triples in the first slice with `|A_1|=8`, and `O` the number in the second with `|A_1|=4`. For an E-triple, the cap and `A_0=4 (mod 8)` force `|A_0|=4`, and exactly one of its two full coefficients has magnitude 4. For an O-triple, `A_0=0 (mod 8)` and `|A_0|<=8`, so one or both full coefficients have magnitude 4. Pairs for distinct triples are disjoint. Hence

`E+O<=8`, with `0<=E,O<=16`.                                                 (2.2)

The ell=1 energy is `16*1^2+12*2^2=64`. Partial Parseval over its 32 frequencies says `sum_{s,alpha,beta}(A_1/4)^2=32*64/16=128`. The two slice value sets give

`4E+O+9(16-O)=128`, i.e. `O=2+E/2`.                                         (2.3)

Thus E is even, `E<=4`, and the lower bound is not a vacuous choice of an empty slice. To obtain the opposite bound, write

`C=sum_{j,b!=0} g_j(b)d_{j,b}`, a sum of twelve signs.

For fixed s, first take the h transform of each ell=1 row. It is `(-1)^{s f_j}[g_j(b)+2(-1)^s d_{j,b} 1_{b!=0}]`. Sixteen-point Parseval in `(j,b)` yields

`sum_{alpha,beta}(A_1(s,alpha,beta)/4)^2 = 64+4(-1)^s C`.

At `s=n`, the left side is `4E`, whence

`E=16+(-1)^n C >= 4`.                                                       (2.4)

The lower and upper bounds force `E=4`, `O=4`, and equality in (2.4) forces *each* of its twelve summands to be minimal:

`d_{j,b}=-(-1)^n g_j(b)` for every `j` and `b!=0`.                           (2.5)

Taking the product of (2.5), and using `sum_{b!=0} b=0`, gives

`(-1)^n = product_j sigma_j`.                                                 (2.6)

Now use the other slice `s=1+n`. The factor `(-1)^s d_{j,b}` equals `g_j(b)`, so after the h transform the row has value `g_j(0)` at b=0 and `3g_j(b)` elsewhere. Its b transform is

`v_j [12*1_{alpha=kappa_j}-2]`, where `v_j=sigma_j(-1)^{s f_j}`.

By (2.6), odd `sum f_j`, and `s=1+n`, `product_j v_j=-1`. These four signs retain product -1 after multiplication by any `(-1)^{beta(j)}`.

There are exactly two even-multiset cases. If all four `kappa_j` are equal, choose that alpha: every term has weight 10, the four signed values have odd negative parity and sum `+2` or `-2`, so `|A_1|=20`. Otherwise exactly two distinct kappa values occur twice. Choose either active alpha and choose beta so the two active signed values agree: this is possible because their distinct j labels have nonzero difference and a linear functional can take either value on it. Odd total product makes the other two signed values opposite; their weight `-2` contributions cancel, leaving `A_1=+20` or `-20`. Both cases contradict `max(|A_0+A_1|,|A_0-A_1|)>=|A_1|` and the cap 12. This proves the lemma as stated, without imposing any `ell=0` sign, site, or additional spectrum condition.

## 3. Corrected actual consumer and the specified carried balance

Use `0=(0,0)`, `p=(1,0)`, `q=(0,1)`, `r=(1,1)`. The phase is called `R` to distinguish it from vector r. In the actual inverse, with the same graph and fixed a,g,

`u(c,w)=[x(c)+3a(c)chi_1(w)+g(c)chi_2(w)+y(c)chi_3(w)]/4`,

`S={(1,f_j,j,b)}`, `f_j=j_0 j_1`, `R(j,b)=j dot b`, `a=1_S (-1)^R`, and `g=(-1)^{1+b_0 b_1}` on S, minus twice that on its e-mates, 4 on the two F blocks, -2 on the six other E-row blocks, and 0 on the Z blocks. The same physical graph condition is `y=-agx`. The prescribed `t` is the actual image of original DC under the common gauge; it is not selected to be zero. Define `X=(-1)^t x`, `Y=(-1)^t y`.

First construct the weighted reference `X_*`: on S take `2*1_{b=j}-1`; at `D_j=(1,1+f_j,j,0)` take +2; and at the six Z points take

| j | h | b | X_* |
|---|---:|---|---:|
| p | 1 | q | +2 |
| p | 1 | r | -2 |
| q | 1 | p | -2 |
| q | 1 | r | +2 |
| r | 0 | p | +2 |
| r | 0 | q | -2 |

All other values are zero. This has the required four D0 and six Z2 points and energy 56. The rank of `f` is 2; `f+1+b_0b_1` is bent as a direct sum of two nondegenerate binary quadratics. For both R and R+f, summing the Walsh transform over b fixes j, giving magnitude 4. The radical lift H is the b-plane and `L=H+<e>`.

For `Z_{ell,j}(s,alpha)=(1/4) sum_{h,b} X_*(ell,h,j,b)(-1)^{s h+alpha(b)}`, the zero column vanishes. If alpha is nonzero, direct graph/D0 summation gives

`Z_{1,j}(s,alpha)=(-1)^{s f_j}[(-1)^{alpha(j)}+(-1)^s]/2`.                (3.1)

The ell=0 entries are the differences of the two displayed signed Z2 points. This independently yields the following complete corrected table; unlisted entries are zero and e.g. `p+` means value +1 at j=p.

| eta | ell=0 | ell=1 |
|---|---|---|
| lambda | none | 0-, p-, q-, r+ |
| b0 | p+, r- | 0+, q+ |
| b0+lambda | p-, r- | p-, r+ |
| b1 | q-, r+ | 0+, p+ |
| b1+lambda | q+, r+ | q-, r+ |
| b0+b1 | p-, q+ | 0+, r+ |
| b0+b1+lambda | p+, q- | p-, q- |

The lambda row follows from the same sum at alpha=0, s=1. Each nonzero row has four entries, affine-flat support and sign product -1. The character sum of four signs of odd product on an affine 2-flat has absolute value 2 at every quotient frequency. Thus the quotient Fourier identity gives `X_*hat in {0,+8,-8}`, exactly eight zeros, and `X_*hat(0)=0`. For the prescribed t, `x_t=(-1)^t X_*` has all 64 U0 caps, all U0 divisibilities and the specified `x_t_hat(t)=0`; this is the actual t, not an after-the-fact choice. These are all profiles of the same x.

On that x the graph y is forced. A direct multiplication gives

`Y(1,f_j,j,b)=sigma_j(-1)^{kappa_j(b)}`,

with `(sigma_0,sigma_p,sigma_q,sigma_r)=(+,-,-,-)` and `(kappa_0,kappa_p,kappa_q,kappa_r)=(b0+b1,0,0,b0+b1)`. The covectors therefore occur twice each, and `sum_j f_j=1`. Every local physical completion has 12 graph D3 mates of amplitude 2, four D0 zero mates, and the fixed total y energy 128; the physical local forms also give 18 D3, 6 Z2, one Z4, and 17 Z0.

The J-to-residue import is verifiable here without changing the fixed a,g. For `xi=(nu,s,beta,alpha)`, summing over b gives

`ahat(xi)=4(-1)^{nu+s f(alpha)+beta(alpha)}`.

For g, `sum_b (-1)^{1+b_0b_1+alpha(b)}=-2(-1)^{alpha_0 alpha_1}`. At s=0 the ell=1 contribution is a multiple of 8 and the ell=0 E-row contribution is 4 modulo 8; at s=1 the ell=0 contribution is zero and the ell=1 contribution is ±12. Therefore `3 ahat=ghat=4 (mod 8)` for every xi. For a ternary u, the transform of `4u(c,0)` is `4J (mod 8)` because the signs and characters do not change its parity. Since `x_t_hat` is divisible by 8,

`yhat(xi)=4J (mod 8)` for every xi.                                          (3.2)

Accordingly any physical completion with J=1 meets every hypothesis of Section 1 after untwisting by t: modulation translates the Walsh spectrum, preserves energy and residue 4, and preserves the graph relation. The lemma proves **no common y for this x has J=1 and all 64 U3 caps**. This is a uniform written proof over the actual signs and sites, not an inference from sampled signs.

For nonvacuity of the physical local construction, set `Y_*=-agX_*` on S, +2 on all 18 D3 and 6 Z2 points, +4 at `(0,0,0,p)`, and zero on F, D0, and the remaining Z points. The actual w=0 graph nonzero counts at `b=(0,p,q,r)` are `(1,2,2,4)`, total 9: for instance, when rho=-1 the zero condition is `a=+1,X_*=-1`, while at b=r the alternative zero condition never occurs. Off graph the F/D0/D3/Z2/Z4 counts are `(2,4,8,3,1)`, total 18. Thus J=27 mod 2=1. The graph y sum is -8, hence `Y_*hat(0)=-8+36+12+4=44`, so this particular physical y is not U3-capped. For any given t, `y_t=(-1)^t Y_*` retains the local ternary inverse; (3.2), applied first at t=0 and then to the translated spectrum, proves J=1 again. This does not modulate the fixed `3a` or g terms or assert that the whole u is a character modulation.

## 4. The same 24-sign system, not a collection of independent spectra

For this fixed X_*, all compatible Y have 12 signs `d_{j,b}` on graph D3 mates, six `e_{j,h}` on ell=0 E-row D3, six `z_{d,b}` on the displayed Z2 points, and a sign `k` at one of the 18 remaining physical Z sites for Z4. Relative to the just-constructed reference, flipping a D3 or Z2 sign toggles exactly one w=0 nonzero; changing the Z4 sign or site leaves its w=0 count one. Thus J=1 is exactly even parity of the 24 negative signs.

Put `B_p={q,r}`, `B_q={p,r}`, `B_r={p,q}`, `h_p=h_q=1`, `h_r=0`, and let the single Z4 site be `(0,h_*,j_*,b_*)`. The partial transforms of this **same** Y are

`A_1=sum_j (-1)^{beta(j)}[4 sigma_j (-1)^{s f_j} 1_{alpha=kappa_j}+2(-1)^{s(1+f_j)} sum_{b!=0}d_{j,b}(-1)^{alpha(b)}]`,

`A_0=2 sum_{j!=0}(-1)^{beta(j)} sum_h e_{j,h}(-1)^{s h} + 2 sum_{d!=0}(-1)^{beta(d)+s h_d} sum_{b in B_d}z_{d,b}(-1)^{alpha(b)} + 4k(-1)^{beta(j_*)+s h_*+alpha(b_*)}`.

For the physical frequencies `t+nu ell*+s h*+beta+alpha`, the values are `A_0+(-1)^nu A_1`, so **all** 64 caps are equivalent to `|A_0|+|A_1|<=12` for every one of the 32 triples, using the same signs and same site in every inequality. If `n_j` counts negative d signs in row j and `n=sum_j n_j`, the two necessary checks `|A_1|<=12` at `(s,alpha,beta)=(0,0,0)` and `(1,0,0)` give respectively

`A_1=16-4n`, `1<=n<=7`; and `A_1=-20+4(n_0+n_p+n_q-n_r)`, `2<=n_0+n_p+n_q-n_r<=8`.

These two bounds alone do not establish the contradiction; Section 2 does. Neither 1,800 sign/site samples nor 240 signs would be an exhaustive `2^24` sign search.

## 5. What changes for a general actual four-distinct-D0 configuration

Here the adopted location theorem S6 and the actual f/R imports of S7 are used only at their stated conditional scopes. The following derivation identifies the precise obstruction to extending Section 2 by saying its hypotheses are automatic.

Let `K=rad(B_f)`. Since its projection to b is an isomorphism, write `k(b) in K` for the unique radical vector with b-coordinate b, and write every z uniquely as `(i,0)+k(b)`, `i in F2^2`. The derivative `d(b)=f(z+k(b))+f(z)` is independent of z and linear. With `h'=h+d(b)`, the graph is `h'=F(i)` where `F(i)=f(i,0)`. The plane b=0 is a complement of K and the restriction of B_f to it is nondegenerate, so `sum_i F(i)=1`.

The physical bentness of R and R+f also makes each row `R_i(b)=R((i,0)+k(b))` affine in b, and its linear covectors `lambda_i` are a bijection of the four covectors. Here is the proof without assuming R itself quadratic. For fixed alpha let `v_i=sum_b(-1)^{R_i(b)+alpha(b)}`. The i-Walsh transforms of v and of `((-1)^{F(i)}v_i)` both have all magnitudes 4: the latter is the R+f transform at the appropriately shifted b-covector. Parseval gives `sum_i v_i^2=16`. A two-bit Boolean row is either affine, giving Walsh values one ±4 and three zeros, or non-affine, giving four values ±2. If even one row were non-affine, the energy 16 forces all four entries of v to be ±2. Their signs must then have product -1 for the first i-transform to be flat; multiplication by `(-1)^{F(i)}` reverses that product, so the second transform cannot be flat. Hence all rows are affine. For every alpha, energy 16 now forces exactly one row to have linear covector alpha. The resulting bijection `i -> lambda_i` is affine, with invertible linear part T, since every bijection of a binary affine 2-plane is affine.

Let the actual D0 anchor in row i have b-coordinate `b_i`, and let the location theorem's exception offset, projected from H to b, be `Delta_i`. Thus the exceptional graph point has b-coordinate `gamma_i=b_i+Delta_i`, and the weighted graph sign is `epsilon_i(2*1_{b=gamma_i}-1)`. S6 makes `i -> Delta_i` affine in either its 1+1+1 or 2+1 alternative. In fixed common b coordinates, multiplication of this sign by `-(-1)^{R_i(b)}(-1)^{1+b_0b_1}` shows that the forced graph Y has H-character

`kappa_i=lambda_i+(1,1)+J gamma_i`, where `J(v_0,v_1)=(v_1,v_0)`.             (5.1)

The overall row signs do not affect kappa. Equation (5.1) is intrinsic to the physical H directions: translating the origin to an actual D0 anchor only changes the row sign, not its H-covector. The derivation uses the **actual** anchors; it does not identify their coordinates with the abstract delta map or choose t.

Since lambda and Delta are affine, `sum_i kappa_i=J sum_i b_i`. A function from a binary 2-plane to a binary 2-plane is affine exactly when the XOR of its four values is zero. Therefore:

* If `i -> b_i` is non-affine, the four kappa values have nonzero XOR, so their multiplicities cannot all be even. Moreover `b'=b+b_i` is then not a global affine coordinate change, so the full physical Walsh cap and mod-8 residue cannot simply be transported into the lemma's aligned-coordinate spectrum.
* If `b_i=B i+b_0` is affine, the global affine change `b'=b+b_i` aligns all D0 mates at b'=0 and preserves Walsh magnitudes; its possible affine translation changes only signs, which do not change the residue class 4 modulo 8. Write `Delta_i=D i+Delta_0` and `lambda_i=T i+lambda_0`. Then `kappa_i` is affine with linear part

  `T+J(B+D)`.                                                                (5.2)

  Its four multiplicities are even **iff** this matrix has rank 0 or 1; rank 2 gives all four covectors once. Odd `sum F` is automatic, but even kappa multiplicity is an additional condition. This condition is sufficient for invoking the lemma, provided the actual energy, J/residue and all other lemma assumptions also hold. It is not supplied merely by the location theorem.

## 6. A physical all-U0-capped counterconfiguration to automatic even multiplicity

Use the *same* physical f and R as Section 3 and define the invertible linear shear

`P(ell,h,j,b)=(ell,h,j,b+j)`, `X'(c)=X_*(P c)`.

The graph still has h=f_j. On it `X'=2*1_{b=0}-1`; its four D0 points are `(1,1+f_j,j,j)`, each with value +2. Its six Z2 values are

| j | h | b | X' |
|---|---:|---|---:|
| p | 1 | q | -2 |
| p | 1 | r | +2 |
| q | 1 | p | +2 |
| q | 1 | r | -2 |
| r | 0 | p | -2 |
| r | 0 | q | +2 |

No value is moved onto an ell=0 E row. The three pairs have directions p,q,r in distinct L-cosets. Their actual D0 anchors have `b_j=j`, while the actual exception offsets relative to those anchors have `Delta_j=j`; thus the 1+1+1 location map is the affine identity and `epsilon_j=+1`. In particular these are actual D0 anchors, not chosen representatives masquerading as anchors.

Because P is an invertible linear shear, `X'hat(xi)=X_*hat(P^{-T}xi)`; by the independently checked table in Section 3 it has all U0 caps and divisibilities and vanishes at zero. For **every specified** t, `x'_t=(-1)^t X'` therefore satisfies `x'_t_hat(t)=0` and the same caps. The graph values force

`Y'(1,f_j,j,b)=(-1)^{(j+(1,1)) dot b}`.

Thus the four intrinsic H-covectors `kappa_j=j+(1,1)` are all distinct. In the actual globally aligned coordinates `b'=b+j`, the scalar factor is `(-1)^{(j+(1,1)) dot j}=1`, so the same four distinct kappa values remain. Here `T=I`, `B=D=I`, and (5.2) has rank 2. This is an actual admissible four-distinct-D0 all-U0 x for which the lemma's even-multiplicity assumption fails, not merely an abstract choice of four representatives.

It has a physical J=1 completion as well: take the forced graph Y', +2 on every D3 and Z2 except set `Y'(0,0,p,0)=-2` instead of +2, take +4 at `(0,0,0,p)`, and zero on F, D0 and the other Z sites. Directly at t=0 the w=0 counts are: graph 12, F 2, D0 3, graph D3 mates 9, E-row D3 1, Z2 3, Z4 1, total **31**, so J=1. The local forms give support 116 and energies 56 and 128. The graph Y' sum is 4; the 18 D3 sum is 32, the Z2 sum 12 and the Z4 sum 4, so `Y'hat(0)=52`. Consequently this particular completion **fails U3**. For any given t, use `x'_t=(-1)^t X'` and `y'_t=(-1)^t Y'`; the same fixed inverse is ternary, and the Section 3 modulo-eight identity plus spectral translation shows J=1. This does not assert a capped y for X'.

The exact unpaid global step is therefore to handle actual anchors and their graph-character patterns beyond (5.2)'s rank-at-most-one case, including non-affine anchor arrays where alignment itself is not affine. It remains logically possible that an additional all-U3/J hypothesis supplies a different contradiction or forces a restriction, but neither is derived here. There is no exclusion of all actual f/R/x, all D0 allocations, a common V, or the original Boolean caller.

## 7. Frozen failure, scope, and chronology

The parent disposition classifies the three f689 profile-row double-sign errors and its wrong per-b graph census as **one AUTHOR EXPLICIT-EXAMPLE MATH MAJOR**, not an entire-episode hold and not automatic falsity of the unrelated location theorem. The actual f710 v1 one-shot run **FAILED** exit 1 with 193 failed checks; its intermediate positive checks did not make it a PASS. The subsequent corrected v2 was a separate, one-shot `PASS_BOUNDED_PHYSICAL_SIGN_INTERFACE_ONLY`: one fixed x, 64 transports and 1,800 sampled sign/site cases. The sample is not all `2^24` signs, and neither run supplies an all-cap U3 witness, V, the original caller, or a retrospective old-gate clearance. The corrected rows and `(1,2,2,4)` census are used above without rewriting the original bytes or backdating the correction.

Coverage: after direct PREBODY ACK to Main, I read the sole frozen packet part in ascending serial RAW windows of at most 20 LF, all LF 1–636 through its ending, containing complete S1 LF 1–194, S2 LF 1–231, S3 LF 1–17, S4 LF 1–42, S5 LF 1–55, S6 LF 1–30 and S7 LF 1–37. Before ACK I read manifest LF 1–314, freeze receipt LF 1–152, final binding LF 1–218, prepared metadata LF 1–282, actual dispatch LF 1–42 and all 24 listed controls through their endings; controls were permissions/status only. Observed metadata SHA256: manifest `fbbb4e80e4278c897cb2c3d2b06a66bdeb4520f3154a0bf751fddda7878eaddc`, freeze `cdcd7f732115db3e25fb12a6fd214da56acc6f2a767568c3c6017a43984a2d56`, final binding `8aefb39f48e5bc8c4c7b95249fa755b28fb47fb7760a171b6a802bd9695c1f2b`, packet `d83069d70d2f15f1da84f4c0cbe735b54834aeacc1a2a60777d5f34ff40aa2e8`. Native clock observed during work: `2026-10-30T16:52:38-0700 PDT`; this is not a claimed exact file-creation time.

All held episodes and all proof/method/selection/planning/verification/reporting/confidence/downstream consumers were NONINPUT. No outgoing link, held history, old code, sibling proof, external model, install, Git operation, deletion, or live infrastructure was used. **CHILD SCIENTIFIC EXECUTION NOT RUN:** all mathematical arguments and examples here are written derivations; no CAS, solver, scientific program, test, build, linter, formatter or finite search was run by this author. Metadata observation and this exclusive file creation are not scientific verification. No independent-model-family, human, kernel, novelty, source-identity, parent-acceptance or original-global-closure claim is made. Any independent finite source, parent full read, GO of at most 55 seconds, run and disposition are separate prospective steps.
