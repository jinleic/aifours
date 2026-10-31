# f202 — PH7 definition-first local-to-global algebra review

**Disposition: 0 F / 0 M / 1 m; INCONCLUSIVE: global exact covers and the full-target theorem; the precise applicability of the irreducibility caller; the graph-specific description of endpoint contact.** The one minor is an underspecified certificate convention, not a counterexample to an algebraic identity: §9 says “the familiar open-positive-orthant strictness rule” without specifying how strictness is checked on internal subdivision faces. The seven required global covers have not been exactly certified here, and their absence is an explicitly acknowledged, load-bearing gap, not a proved exclusion. In particular the attained supremum has **not** been established equal to `z_*`. The algebraic implications below hold under the stated necessary-reduction assumptions and if the specified exact obligations hold.

The recorded native clock before this review was written was **2026-10-29T13:23:43-0700 PDT**; this is an observed clock, not a file-creation timestamp. This review is algebra-only and is not a parent disposition or executable GO.

## Frozen inputs and actual sequence

The first *research artifact* opened was `manifest-v1.json`. Its measured SHA-256 was `d731fafc77e1b2cde341b62c840f7166af4019fc75bc5c34f68fb673aad62742`, matching the supplied prefix `d731fafc77e1`. Before any declared input body was read, all seven inputs were independently measured; their full SHA-256, byte count, and LF count matched the manifest. Then every declared input was displayed completely, in the listed order, before mathematical reconstruction or controls. The last line of each input was displayed. `D` denotes `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/`; `E` denotes `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/`.

| # | Frozen input | Measured SHA-256 | Bytes / LF | Actual raw-window requests |
|---|---|---|---:|---|
| 1 | `D/math-1-ph7-supremum-bracket-closed-endpoint-erratum-v1.json` | `a1589a464fccc010cf2ad13cd61c430e9a6032cb80407019b2d38edbc603ce97` | 2481 / 30 | 1–15, 16–30 |
| 2 | `D/math-1-ph7-algebraic-endpoint-closed-band-parent-v1.md` | `307b3823d9af55a171fa911373ae96cd9df22a019b3f4f65fa94d70e9de5cbeb` | 7236 / 24 | 1–15, 16–30 |
| 3 | `D/math-1-ph7-no-seven-states-above-83over100-parent-v1.md` | `7935d4f5ce796c9efd4a7c015066f03120a0ae8cec89d62e9231197f3da64b3a` | 5603 / 27 | 1–15, 16–30 |
| 4 | `E/frontier-20261029-ph7-joint-interlacing-y1-v1.md` | `0221e6c73440f921f127db0130038f8ab733fae65d5585f4227ba06b9fef8310` | 6695 / 90 | 1–15, 16–30, 31–45, 46–60, 61–75, 76–90 |
| 5 | `E/frontier-20261029-ph7-local-global-local-certificate-v1.json` | `8f5f9b85b1211c36114500fc61c1a35b23646e9e1cb65e6697fd0663d1b15fce` | 15085 / 188 | 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–135, 136–150, 151–165, 166–180, 181–195 |
| 6 | `E/frontier-20261029-ph7-local-global-dual-check.py` | `cb2b9ede94c117ea44b6c100ee7dbfa4cb46d38531aea9de1bd3582892e085d8` | 9057 / 180 | 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–135, 136–150, 151–165, 166–180 |
| 7 | `E/frontier-20261029-ph7-local-to-global-supremum-candidate-v1.md` | `b2b7770d8b024782c5d0c1cfbd8f6e01368892801d1f3882e7b3279b59059ca5` | 18317 / 210 | 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–135, 136–150, 151–165, 166–180, **181–210**, followed by 181–195 and 196–210 |

**Process deviation:** the first request for input 7's ending, 181–210, displayed 30 lines in one window, exceeding the approximately 15-line maximum. The same ending was subsequently displayed in the two short windows shown; this does not erase the original deviation. The general non-research memory summary was read before the manifest as runtime guidance; a generic non-research review-process skill was read after the mathematical controls. Neither is a mathematical input or premise. The author verifier was read only: it was never run, imported, or compiled. No linked research body, sibling review, outside literature/model/API, floating search result, or author contact was used as evidence.

## Per-identity and implication verdicts

`0F/0M/0m` means this reviewer found no defect in the stated identity or in the stated implication, at the indicated conditional scope. A pending exact inequality is not thereby certified. Mathematical steps are reconstructed below, rather than imported from the author certificate.

| Identity or proposition | Verdict | Basis / qualification |
|---|---|---|
| `p=e1−4` | 0F/0M/0m | `y^6` coefficient. |
| `q=e2−4e1+10−2z` | 0F/0M/0m | `y^5` coefficient. |
| `W=e3−4e2+(10−2z)e1+12z−20` | 0F/0M/0m | `y^4` residual. |
| `E3=e4−(6+2z)e2+(20+4z)e1+3z²+6z−45` | 0F/0M/0m | `y^3` residual. |
| `E2=e5−(1+z)²p−(4+4z)q` | 0F/0M/0m | `y²` residual. |
| `E1=e6−(1+z)²q` | 0F/0M/0m | `y` residual. |
| `W>=0`, `K=E3−S4W>=0`, `Y2>=0` | 0F/0M/0m | Independently reconstructed from cycle cover and interlacing, conditional on the stated irreducible matrix reduction. |
| Joint three-eigenvalue inequality and displayed nonnegative `delta` expansion | 0F/0M/0m | Coordinatewise monotonicity and exact polynomial check; the author joint lemma is not used as a premise. |
| `E1−sE2 >= W*alpha+K*B_joint−W²/2` and `Y_joint>=0` | 0F/0M/0m | All inequality directions and the nonpositive `B_joint` are essential. |
| Comparison with old `beta`, and optional 16-corner minimum | 0F/0M/0m | `Y_old−Y_joint=K(B_joint−beta_old)>=0`; with `W>=0`, the corner expression is a **maximum**, not a minimum. |
| Endpoint `W=E3=Z=K=Y_joint=0` | 0F/0M/0m | Follows from adopted root equations, independently of a graph description. |
| Claim that a particular length-five cycle complements exactly the two named `V` states | INCONCLUSIVE | Not needed for algebraic contact; the particular graph is not an expressly adopted frozen-body premise. |
| Six-rate formulas `q=A+(f1−4)x`, `W=Ax+B`, `E3=h1*x+h0`, `K=E+Dx` | 0F/0M/0m | Direct elementary-sum recursion. |
| `EA−BD=h0*A−h1*B`, `A*K−D*W=−Hpol` | 0F/0M/0m | Exact expansion; `Q,Hpol` are unscaled. |
| Constant-coefficient pair bound and `base>=W4*g` | 0F/0M/0m | Correct signs for both `3+3` and `3+4` pairs, including `P33v<=xW²/2`. |
| `g=g0−Ax`; `Y0` is cubic with `c3=−A²/2`, `Y0'''=−3A²` | 0F/0M/0m | Exact independent coefficient and derivative checks. |
| Adaptive cubic tail and lower anchor | 0F/0M/0m | Correct with **all** listed strict/weak signs and common-basis Bernstein bounds. |
| `F=Y_joint+lambda*W+mu*K` | 0F/0M/0m | Exact identity, including `W²/2`. |
| D0 and grouped-to-individual stationarity | 0F/0M/0m | Invertible determinant and factor 5 / factor 2 checked independently on the refined root box. |
| Refined root, `J`, and `I_a,I_b` | 0F/0M/0m | Own exact contraction and independent dual enclosures fit the declared intervals; `J` contains the intended `z` interval. |
| LOCAL signs, Hessian and local maximum | 0F/0M/0m | Independently recomputed by exact centered polynomial bounds and an invertible rational congruence; details and limits below. |
| `F_i−F_j=−(v_i−v_j)Phi_ij` | 0F/0M/0m | Checked for the first pair and two representative last-block pairs; follows for all by block permutation. |
| Block-averaging derivative and SB-to-mean implication | 0F/0M/0m | Valid conditional on full unsorted-box SB, including `F=0` and subdivision faces. |
| MP inner rectangle and local routing | 0F/0M/0m | Triangle inequality with `rho−r`; linked actual dual and `z>=z_*` are needed for the local branch. |
| Case (a) completed square and strict contradiction | 0F/0M/0m | Uses `f2<=5f1²/12` and all `z in J` above `3/7`. |
| Case (b) sign of `Q` including `A=0` and `f1=4` | 0F/0M/0m | Feasibility yields `Q<=0`; the `f1=4` case has `q=A<=0`. |
| Case (c) sign of `Hpol` including `D=0` | 0F/0M/0m | `−Hpol=A*K−D*W>=0`. |
| Case (d) `Abar−A=beta1²/4−beta2`, `Dbar−D=y*alpha2/6−alpha3` | 0F/0M/0m | Independent expansion and four-variable elementary-symmetric bounds. |
| `Y2` leading coefficient `S3*A`, its discriminant leaf, and `Y2v6` tail | 0F/0M/0m | Strict `A<0` gives strict concavity; derivative is taken holding six rates fixed. |
| `Y_joint` is quadratic, jointEnd and cleared multiplier endpoint signs | 0F/0M/0m | Leading coefficient `A*s*(v4+v5+v6)+A²/2`; both endpoints and denominator signs matter. |
| Compactified cube endpoints and degree-two denominator | 0F/0M/0m | Exact substitutions; all six variable degrees of `Q,Hpol` are at most two. |
| Outer strictness convention on subdivision faces | **m** | The acceptance condition is clear, but the proposed “familiar” implementation rule is not actually specified. See obligations. |
| Actual QO/HO/NB/MC/R3/SB/MP finite covers | **INCONCLUSIVE** | No exact serialized global covers or independent global replay are supplied or run. Sampled/floating closures are not certificates. |
| Irreducible seven-state caller for every relevant `z` | **INCONCLUSIVE** | The f180 disposition names an adopted caller but does not spell out that full quantified statement in the permitted bodies; linked bodies cannot fill the gap. |
| PH7 supremum equals attained `z_*` | **INCONCLUSIVE** | Requires the caller at its exact scope and all uniform global obligations; neither follows from this review. |

## Written reconstruction

### 1. Coefficients, cycle cover and the joint lemma

Let `e_k` be elementary sums of the ordered positive eigenvalues `v1<=...<=v7` of `Acal=−S`. The polynomial

`D_z(y)=y^5+4y^4+(6+2z)y^3+(4+4z)y²+(1+z)²y`.

Matching `prod_i(y+v_i)−D_z(y)(y²+py+q)` from the top gives precisely the six canonical residuals in the table. For six-rate sums `f_k` and `x=v7`, the recursion `e_k=f_k+x f_{k−1}` gives the displayed `A,B,h1,h0,D,E`; in particular `EA−BD=A h0−B h1`, and `AK−DW=AE−BD=−Hpol`.

The necessary cover expansion can be reconstructed from the determinant, conditional on the matrix reduction. For an undirected simple cycle of length at least three, the two directed cycle products `P,Q` differ from their symmetrized contribution by `omega=P+Q−2sqrt(PQ)>=0`. Grouping permutation terms by disjoint cycles yields `det(yI−G)=det(yI−S)−sum_C omega_C det(yI−S_{V\C})+sum_{disjoint C,C'} omega_C omega_C' det(yI−S_{V\(C∪C')})−...`. There are no three disjoint extra cycles in seven vertices. Thus `W=W3>=0`; at `y^3`, `E3=a1+W4`. Interlacing bounds each four-state complementary trace between `S4` and `L4`, so `W4<=K=E3−S4W` and `W4>=E3−L4W`. At `y²`, `E2=a2+b1+W5`, with `a2>=W e2(v1..v4)` and `b1>=S3 W4`; these inequalities give `Y2>=0`, including when `E3−L4W` is negative.

For any three-state complement with ordered eigenvalues `nu_i>=v_i`, set `s=v1+v2`. In `e2(nu)−s sum(nu)`, the three partial derivatives are sums of the other two variables minus `s`, all nonnegative on `nu_i>=v_i`. Equivalently, writing `nu_i=v_i+delta_i`, the increment is

`(v3−v1)delta1+(v3−v2)delta2+delta1*delta2+delta1*delta3+delta2*delta3 >= 0`.

The base value is `B_joint=v1*v2−s²<0`. Therefore `b2−s*b1>=W4 B_joint>=K B_joint`: the final inequality reverses the naive intuition because `B_joint<0` and `W4<=K`. For a four-state complement, separate interlacing gives `a3−s*a2>=W*alpha`, where `alpha=e3(v1..v4)−s e2(v4..v7)`; for a two-state complement, `c1>=sW5`. Finally `0<=P33<=W²/2` for unordered disjoint pairs of three-cycles. These give the displayed `Y_joint>=0` without using the unreviewed joint lemma as a premise.

For the optional stronger four-state bound, `e3(mu)−s e2(mu)` is multi-affine on `prod_i[v_i,v_{i+3}]`; its minimum is attained at one of 16 corners and is at least the separately obtained `alpha`. Since `W>=0`, substituting that minimum produces the **maximum** of the 16 corresponding polynomial `Y` expressions; negativity of just one corner expression does not suffice. At the adopted root, the three equations are `W=E3=Z=0`; hence also `K=Y_joint=0`. This proves tight contact independently of the unpinned graphical description.

### 2. Constant coefficient and adaptive cubic

At `y=0`, the cover expansion reads `e7=a4+b3+c2+d1+W7−P33v−P34`. Interlacing yields `a4>=W e4(v1..v4)` and `b3>=W4 v1v2v3`; all `c2,d1,W7` terms are nonnegative. Every remaining diagonal in a `3+3` pair is at most `v7=x` by the Rayleigh bound, and pair counting gives `P33v<=xW²/2`, `P34<=W W4`. Therefore

`base=e7−W e4(v1..v4)+xW²/2 >= W4*(v1v2v3−W)=W4*g`.

For `g>=0` and `W4>=E3−WL4`, this gives `Y0=base−g(E3−WL4)>=0` even if the latter lower bound is negative. Since `W=Ax+B`, `L4=v4+v5+v6+x`, `g=g0−Ax`, the only cubic contributions are `+(A²/2)x³` from `xW²/2` and `−A²x³` from the subtracted product; hence `c3=−A²/2` and `Y0'''=−3A²`.

If `A<0`, `t<=x`, `g(t)>0`, `Y0(t)<0`, `Y0'(t)<=0`, `Y0''(t)<=0`, then `g` increases and the negative third derivative forces `Y0(x)<0` for all `x>=t`, contradicting the necessary inequality. In a cell whose common Bernstein coefficients of `−A` and `Fm=f1−4` are strictly positive, `Lq=min_k (−A)_k/Fm_k` implies `A+Lq Fm<=0`. Since `q(x)>0`, `x>Lq`; also `x>=v6>=Lv6`. Thus the stated rational floor of `max(Lq,Lv6)` is a valid nonnegative `t<=x`. The four `c_i` have six-variable degree bounded by `(2,2,2,3,3,3)`; elevating to a common basis before evaluating at `t` preserves the claimed coefficientwise correlations. `g0` and `−A` are separately multi-affine. Uniform sign checking of the resulting coefficients remains a global obligation.

### 3. Root, algebraic dual and local box

The adopted endpoint is the unique root in its old box of `Wg=Eg=Zg=0`, where the spectrum is `(V,V,U,U,U,U,U)`. The independently generated exact control expands these same equations, constructs its own exact inverse of the Jacobian at the frozen refined center, bounds the Jacobian on the radius `r=10^−16` box by centered coefficient triangles, proves `||I−P J(box)||_infinity<10^−8` and `||P F(center)||_infinity+norm*r<r`, and verifies strict containment in the old uniqueness box. Thus its root is the adopted one. It independently encloses the D0 determinant away from zero and solves for `a_dual,b_dual` by interval arithmetic; its three resulting enclosures lie inside the declared determinant, `I_a`, and `I_b` intervals. The author's interval receipt is not used as proof.

Since `z_* in [z0−r,z0+r]` and `epsilon=r`, `[z_*,z_*+epsilon]` is contained in `J=[z0−r,z0+r+epsilon]`. The dual constants are fixed at the root for the local proof; independent `I_a x I_b` variation is a conservative *global cover* requirement, not a claim that arbitrary parameters solve D0.

The exact identity `F=Y_joint+lambda W+mu K` follows by substituting `K=E3−S4W`. At the root it gives `F=0`. D0 gives the two grouped partial derivatives zero at `Eg=0`; block symmetry makes each first-block derivative one half and each last-block derivative one fifth of its grouped derivative, so all seven vanish. Our second exact control independently recomputed the scalar signs and all seven strict diagonal-dominance margins of `R^T(−H_v F)R` over the rational superset with every coordinate and `z` displaced by at most `rho+r` from the respective rational center. The rational upper-unit-triangular `R` and rational dual centers were used as *numeric design data*, not as asserted proof; all bounds were recomputed from canonical polynomials, using independently enclosed linked duals. It obtained all margins `>3`, `lambda>0`, `mu>0`, and `F_z<0`. Symmetric strict diagonal dominance and invertibility of `R` imply negative definiteness of `H_v F`. Consequently, for the actual linked constants, `F(v,z_*)<=0` with equality only at `v_*`, and `F(v,z)<0` for `z_*<z<=z_*+rho` in the local spectral box. These are exact-arithmetic controls, not formal/kernel verification.

### 4. Schur barrier and mean reduction

With `s=v1+v2`, write `c=s(4+4z)−(1+z)²`. Differentiating elementary sums while holding the other variables fixed gives, for two coordinates in the same block,

`F_i−F_j=−(v_i−v_j)[e'_4−s e'_3+(b_dual−2E3)e'_2+a_dual e'_1+c−4a_dual−(6+2z)(b_dual−2E3)]`.

For the first pair, the derivatives of `s` cancel in the difference; for the last block they vanish separately. `F` and its box are invariant under permutations within each block, so SB for the displayed representative pairs applies to every same-block pair. Along `v_i(t)=mean+e^(−t)(v_i(0)−mean)`,

`dF/dt=(1/m) sum_{i<j} Phi_ij (v_i−v_j)²`.

If SB holds on the **whole unsorted** `B7`, no path starting at `F>=0` can exit that set while averaging, and a nonconstant block makes `F` strictly increase. The mean limit stays in the box. The MP local rectangle uses `|ubar−U0|,|vbar−V0|<=rho−r`, so the actual root box implies distances at most `rho`; the nonlocal MP leaves must prove strict `F_group<0`. Thus SB+MP rule out `F>=0` on `B7` for actual `z>z_*`, and at `z_*` only the exact root can attain nonnegative `F`. No preservation of `W,K,Y_joint` along averaging is required.

### 5. Case partition and leaf sufficiency

For case (a), `p=f1+x−4>0` and `f1<4` imply `x>4−f1` and `q<A−(4−f1)²`. Six-variable Cauchy gives `f2<=5f1²/12`, hence

`A−(4−f1)² <= 6/7−2z−(7/12)(f1−24/7)² < 0`.

For case (b), if `f1=4`, then `q=A<=0`. If `f1>4,A<0`, feasibility requires `x>−A/(f1−4)` and `x<=B/(−A)`, giving `Q=A²−(f1−4)B<0`; if `A=0`, `W=B>=0` gives `Q<=0`. Thus `Q>0` is a contradiction. The NB rules are sound: `E4v6` forces `W(x)<0`; `Y2v6` and `Disc` use the strictly negative leading coefficient `S3*A`; the adaptive rule is proved above. A no-sorted-point leaf must use an actual strict interval ordering obstruction, not a midpoint.

For case (c), `A>0,D<=0` and `W,K>=0` give `−Hpol=AK−DW>=0`; hence `Hpol>0` contradicts feasibility. For `A>0,D<0`, feasibility confines `x` to `[−B/A,−E/D]`. `Y_joint` has leading coefficient `A*s*(v4+v5+v6)+A²/2`, so the listed positive-leading and two strict endpoint tests make it negative throughout the interval. The SchurBlock inequalities put that interval in `[127/100,29/20]`. If `lambda=L0+L1*x` and `mu=M0+M1*x`, the listed expressions are exactly their endpoint numerators with positive denominators `A` and `−D`; positivity at both endpoints proves positivity throughout. Then feasibility gives `F>=0`, contradicted by SB+MP. Boundary `D=0` is not silently covered by a `D<0` leaf: it must be handled by the other exact MC leaves.

For case (d), let the first four rates have sum `y=alpha1` and elementary sums `alpha2,alpha3`; let `beta1=v5+v6`, `beta2=v5v6`. Ordering implies `beta1>=y/2`, so `beta1=y/2+gamma` with `gamma>=0`. Also `alpha2<=(3/8)y²`, so it can be written `(3/8)tau*y²`, `0<=tau<=1`. Direct expansion gives

`Abar−A=beta1²/4−beta2>=0`,
`Dbar−D=y*alpha2/6−alpha3>=0`.

The first is a square; for the second, `y*alpha2−6alpha3 = (1/2) sum_{i<j}(u_i−u_j)² sum_{k != i,j}u_k>=0` for the four first-block rates. Thus any feasible case-(d) point maps to the advertised three-variable strict system, which R3 must exclude on its full compactified domain.

### 6. Global shift as an algebraic implication

Independently of PH-set downward closure, suppose the necessary irreducible matrix `G` exists at `z` and let `r,l>0` be its right and left zero-Perron vectors. The positive projection `P=r l^T/(l^T r)` obeys `GP=PG=0`. For `t>=0`, `G_t=(G+t(P−I))/(1+t)` is irreducible Metzler, has spectral bound zero, and sends each nonzero eigenvalue `lambda` to `(lambda−t)/(1+t)`. Its repeated critical pair is `−1 +/- i sqrt(z)/(1+t)`, while the quadratic changes to positive coefficients `p_t=(p+2t)/(1+t)`, `q_t=(q+pt+t²)/(1+t)²`. Thus a necessary-spectrum exclusion on an interval immediately above `z_*` propagates to every larger `z` by choosing `t` appropriately. This is an algebraic matrix-relaxation argument, not an assertion that every shifted matrix realizes the original PH transfer. Existence of the original `G` for every hypothetical PH representation is the separately unresolved caller scope.

## Exact certification obligations still required

The following are obligations, not completed claims. Every polynomial must be reconstructed from the frozen definitions; parameter enclosures must be exact and uniform over all of `J`, and over the independent `I_a x I_b` wherever the dual occurs. A finite certificate must bind exact source expressions, rational boxes, split paths and leaf labels, and must check exhaustive coverage with no gaps, including equalities and all parameter/face boundaries. Strict inequalities must be strict at every admissible point, not just at sample centers.

1. **QO:** on the positive six-rate orthant outside `N6=[5/11,37/27]^6`, prove `Q>0` uniformly on `J`. Under `r_i=s_i/(1−s_i)`, clear by the positive factor `prod_i(1−s_i)^2`; treat the excluded cube `[5/16,37/64]^6` exactly. Finite `r_i>0` corresponds to `0<s_i<1`; compactification faces at infinity may only be discarded with a valid open-domain argument.
2. **HO:** analogously prove `Hpol>0` outside `M6=[7/9,5/3]^6`, with excluded compact cube `[7/16,5/8]^6`. Integerization may multiply `Q,Hpol` only by positive factors.
3. **NB:** cover *all sorted points* of `N6` with `f1<4`, `A>0`, `Q>0`, `E4v6`, `Y2v6`, `Disc`, `adaptiveY0`, or a proved absence of sorted points. Check every sign with the exact strictness in §8; in particular check the `A=0` and `f1=4` boundaries by applicable leaves or the separately proved contradiction. For adaptive leaves, verify common-basis coefficient positivity, the exact rational `Lq,Lv6,t`, the common-tensor bounds for `Y0,Y0',Y0''`, and `g(t)>0` on the **whole** cell. No separate maxima of coefficient tensors may be substituted for the correlated test.
4. **MC:** cover all sorted `M6` by `A<0`, `D>0`, `Hpol>0`, jointEnd, SchurBlock, or absence of sorted points. jointEnd must certify `A>0,D<0,d2>0` and both cleared strict endpoint negatives. SchurBlock must certify the six-coordinate block bounds, `A>0,D<0`, both crude-interval containment inequalities, and **all four** cleared positive multiplier endpoint inequalities, uniformly over `J x I_a x I_b`. Cover `D=0` with another valid rule; inequalities with `D<0` do not include it.
5. **R3:** over all `y,gamma>=0`, `tau in [0,1]`, after exact compactification of the unbounded axes, cover by `Abar<=0`, `Dbar<=0`, or `y+beta1<4`, preserving the stated weak/strict directions and all finite-domain boundaries. The relation `beta1=y/2+gamma` and the expressions for `Abar,Dbar` must be the ones proved above.
6. **SB:** on the **full unsorted** rational `B7` and all `J x I_a x I_b`, certify on each cell `F<0` or both `Phi_12>0` and `Phi_34>0`; this is a disjunction on the entire cell, not sampling. Ensure every relevant face, especially `F=0`, is covered.
7. **MP:** on the entire `(ubar,vbar)` rectangle `[127/100,29/20] x [1,11/10]`, certify on each cell either `F_group<0` uniformly on `J x I_a x I_b` or containment in the exact closed inner local rectangle `|ubar−U0|,|vbar−V0|<=rho−r`. Only for the latter branch use the *linked actual root/dual* and actual `z>=z_*`.
8. **Exact strictness and coverage:** specify and verify the “open-positive-orthant” Bernstein rule for every relative face of every subdivided cell and every parameter endpoint. For example, on a cell `[a,b]` with `0<a<b<1`, the polynomial `(s−a)/(b−a)` has nonnegative Bernstein coefficients and one positive coefficient but vanishes at the finite, admissible face `s=a`; that test alone is not a strict-positive certificate. A sufficient face-aware test is nonnegative coefficients plus a positive active coefficient on every admissible relative face, or an equivalent rigorous exact method. Check excluded-cube membership, prefix-free/full split coverage, exact boundary ownership, and the intended no-sorted-point test; a capped or incomplete cover is UNKNOWN.
9. **Root/local binding and logical bridge:** retain the exact contraction, determinant, D0 linked constants, local `lambda,mu,F_z`, congruence-invertibility and all seven strict dominance bounds; bind them to the same frozen root and inputs. The present independent local replay addresses these algebraic checks but is not parent acceptance. Separately establish the exact quantified irreducible-matrix caller for a hypothetical PH representation and the other adopted premises at their written scope. The final proof still needs the complete exact global covers and the specified parent gate; fixed-center floating counts, timeouts, `UNKNOWN`, and author PASS are not exclusions.

## Independent control receipts

All scripts below were reviewer-written under this wave directory. Each was run with `/usr/bin/python3`, no author program was run/imported/compiled, and the measured Python assertion mode was `PYTHON_OPTIMIZE 0`, `__debug__=True` at native clock `2026-10-29T13:23:25-0700 PDT`. The script that reads the author JSON uses its rational preconditioner, centers, and declared intervals only as data to compare against independently derived bounds, not as evidence that a sign holds.

| Script and SHA-256 | Native START → END, exit | Independent result and negative controls |
|---|---|---|
| `reviewer-f202-algebra-controls.py` `5128c00589d22c9f14eae3a20448195e6ebdc0bdbcf3a18d1c7e3d553be772e8` | 13:19:13 → 13:19:14 PDT, exit 0 | Exact sparse rational-polynomial identities, canonical coefficients, Schur differences, cubic degree, common tensor degrees, R3 algebra, grouped stationarity, root contraction and dual inclusion. Intended-reason negatives rejected reversed `Hpol` and Schur signs, wrong cubic sign, an omitted pair-half term, an omitted joint cross term, wrong R3 sign, a bad upper-endpoint sign, and an invalid interval. Checking the recorded local bound numerals alone was explicitly reported as arithmetic consistency, not proof. |
| `reviewer-f202-local-replay.py` `f072aaa6098fed33b052021a1450d4edec9df4604e496cee37ca7eed365b999c` | 13:20:13 → 13:20:25 PDT, exit 0 | Reuses **only the reviewer-written** preceding definitions/root calculation, then independently bounds the canonical Hessian congruence, multipliers and `F_z` on the local rational superset. All seven margins `>3`, both multipliers positive, `F_z<0`. Direct sign-comparison negatives reject zero margin, positive `F_z`, and a nonpositive multiplier; they are not mutated-matrix replay controls. |
| `reviewer-f202-rational-witnesses.py` `1ab2a0e13d6dc386614d5e08db3657866c3ef7a58b628f13a0eae1513e3d531a` | 13:20:48 → 13:20:49 PDT, exit 0 | At the rational center, 1,716 exact sorted rational tuples yielded no QO/HO counterexample; this finite sample is **not** a cover or exclusion. A deliberately outside point was rejected as an N6 member. |
| `reviewer-f202-boundary-controls.py` `d7470e011eace7afdf6c4d2120e344f1cd4d6a53b3b5ff1111c4f8e5b02bd686` | 13:22:51 → 13:22:56 PDT, exit 0 | Exact targeted rational solves found 42 sorted `A=0` and 81 sorted `D=0` sample points, with no uncovered case-(b)/(c) witness in this sample. It does **not** prove boundary coverage. A deliberately non-boundary tuple was rejected. |

## Explicit imports, remaining gaps, and review status

The only scientific imports used are the f50 disposition's explicitly stated root uniqueness/box and actual closed PH7 construction, and, when discussing seven-state necessity, its expressly conditional six-state lower barrier; the f180 disposition's conditional no-PH7 statement for `z>=83/100` supplies the already-adopted bracket `[z_*,83/100]`. The endpoint erratum forbids turning an excluded right endpoint into an open supremum bound without a positive gap. The caller is named in f180 but its full quantified irreducibility statement is not written out in these frozen bodies, so it is retained as an explicit unresolved premise rather than reconstructed from a linked source. Coefficient/cycle identities, the joint lemma, local algebra and the matrix spectral shift were independently reconstructed above. Graph-specific endpoint contact is not imported.

There is no exact global certificate here, no assertion that the PH-realizable set is downward closed, and no basis here to sharpen the adopted supremum bracket to equality. This is a **same-harness** review: it is not human review, independent-model-family review, formal/kernel verification, or a novelty/prior-art verification.
