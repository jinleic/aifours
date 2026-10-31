# f94 privacy peak–floor universal chain — same-harness scientific review

Native `/bin/date` clock observed immediately before creation: **2026-10-28T19:11:16-0700 PDT**. Reviewer: PrivacyPeakFloorReview. Binding manifest: `manifest-v1.json`. This is a same-harness written-math review, **not** a second model family, human or formal/kernel review, novelty determination, or parent adoption.

## Input identity and scope

All six manifest inputs were SHA-256 checked against both `sha256` and `expected`, and byte and LF counts checked; all matched. They were read completely in manifest order in exact raw windows, before these verdicts. Full names below are relative to `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/`.

| ID | Pinned input | SHA-256 | Bytes / LF |
|---|---|---|---|
| d440 | `frontier-20261028-peak-floor-low-privacy-universal-v1.md` | `d44029e458b8af871d2d849e2a5159e1885e99402d615a88eabe39d89ab4ad43` | 10378 / 171 |
| 62e4 | `frontier-20261028-universal-low-privacy-tail-profile-v1.md` | `62e4ec81de4b8fd2c2155e61a1a32917e860847c844e8c44948c46adf6e35275` | 6502 / 114 |
| 7abb | `frontier-20261028-uniform-joint-weight-low-privacy-v1.md` | `7abb1357b8df031f840ef2bf29c8226cad01d9f3d65670126211fb47e5197676` | 8773 / 121 |
| fa39 | `frontier-20261028-peak-floor-first-norm-universal-v1.md` | `fa39d7bdc125da7c8f7424d5976309227d8101a58b15efea919e8eb8376f04ea` | 8979 / 127 |
| 35fc | `frontier-20261028-near-optimal-overlap-rate-counterexample-v1.md` | `35fc483bd111c805e2c43d434a956b2217fed9fd2e22bf049da060e9d6219f3d` | 6503 / 84 |
| a740 | `frontier-20261028-near-optimal-overlap-sharp-exponent-v1.md` | `a740508d8398e36da2e6e1369991f4640dba6c540a3b76ebb70663dca2781ec3` | 7272 / 119 |

**Process finding:** no pinned input hash, byte-count, or LF-count mismatch. The unpinned discussion of the earlier `7307a4883179087691cb5265ece87a7ae0ddee906be88839b2ef4a6e439920da` exact-optimizer candidate (35fc:7) and its own inputs was not used or reviewed. No held, withdrawn, or quarantined body was used.

## Verdicts and explicit dependency graph

Counts are **FATAL / MAJOR / MINOR**; zero means no defect found in this written review, not formal certification.

| Candidate | Verdict | Actual dependency and scope |
|---|---:|---|
| **d440** | **0 / 0 / 0** | Fixed finite lambda: nonasymptotic lower bound, leading value, full-law TV limit, and non-W2 conclusion have no prior research-candidate premise. Standard measure theory/geometric calculus only. |
| **62e4** | **0 / 0 / 0** | `d440 -> 62e4`: imports the peak, location, and bathtub-deficit conclusions. Tail L1 and weak cost-measure arguments check out given those facts. |
| **7abb** | **0 / 0 / 0** | `d440 -> 7abb`: imports the cap/floor/bathtub method, and separately extends it uniformly to moving theta including the pure squared-l1 endpoint. The uniform O-term is for the **normalized** cost. |
| **fa39** | **0 / 0 / 1** | Its first-norm lower bound, leading value, scaled TV, tail, cost-measure and non-W1 results are independent of d440 and prior research artifacts, subject to the explicit normalization correction below. The separate cross-objective corollary is `d440 + fa39 -> fa39:114–116`. |
| **35fc** | **0 / 0 / 0** | `d440 + fa39 -> 35fc` for the first-order-near-optimal labels and general TV-to-one statement. Its mixture privacy, exact-budget construction, and overlap lower bounds hold directly. The comparison with 7307 is an unverified contextual claim, not a premise of the counterexample. |
| **a740** | **0 / 0 / 1** | `d440 + fa39 -> a740`: the squared peak cap and first-norm deficit drive the universal exponent; both predecessors and the explicit shells drive sharpness. The undefined `Q_B` notation in the lower bound needs repair below. The proof does not depend on 35fc. |

The authors labeled d440 and fa39 **unreviewed on entry**. This assignment has now examined their pinned proofs in the **same harness**, with the fa39 minor noted; it does not grant independent-family, human, formal or parent acceptance. Hence successor verdicts remain explicitly **conditional on these predecessor proofs/status**, rather than pretending the imports were already accepted. Within this assignment I found no additional unreviewed research theorem necessary for the six main mathematical conclusions. In particular, `d440 -> fa39` is **only** the cross-objective corollary, not the first-norm main theorem; neither 62e4 nor 7abb is a hidden prerequisite for the last two candidates.

## Findings

### MINOR 1 — fa39:65–70, shell normalization is not specified consistently

The text describes the normalized law using the kernel `b^k`, where `k=min{j:x in (q+j)D}`, and then writes `Z=2M2`. For this kernel the exact layer-cake identity is

```
b^k = (1-b) sum_{j>=0} b^j 1_{(q+j)D},
integral b^k dx = (1-b) 2M2.
```

Thus if `Z` is the normalizer of the written kernel, the missing factor is `1-b`. Alternatively `Z=2M2` can denote the normalizer **after** stripping that common factor, but then the normalized density must be specified as `(1-b)b^k/Z`; the current text does not say this. At an exact point satisfying the candidate's own `q^3=2b`, namely `b=1/16`, `q=1/2`, independently computed `M2=353/900`, the displayed `2M2=353/450`, whereas `integral b^k=353/480`; dividing `b^k` by `2M2` gives mass `15/16`, not one. See `normalizer-check-v1.py` and `.txt`.

**Repair:** say `p=b^k/[(1-b)2M2]`, or explicitly define the adjusted `Z=2M2` and `p=(1-b)b^k/Z`. The common factor cancels in the displayed `(2/3)M3/M2` expectation, and the correctly normalized shell remains full-D private, so this is a repairable normalization/notation defect rather than a failure of the leading theorem. The pinned candidate was not changed.

### MINOR 2 — a740:98–102, undefined measure in overlap lower bound

The proof defines the intermediate law as `B_b` and defines `Q_b=E_b`, but then writes `w_b Q_B(q_b D)` without defining `Q_B`. The needed expression is

```
integral_{q_b D} min(p_P,p_E) >= w_b B_b(q_b D) = w_b(1-o(1)).
```

On that core `p_P>=w_b p_B` and eventually `p_E>=w_b p_B`; the top-core probability of **B_b**, not `Q_b=E_b`, tends to one. Indeed the latter's probability of this smaller core tends to zero. Replacing the undefined symbol by `B_b` restores the literal statement; no change to the derived exponent is needed.

## Independent reconstruction of load-bearing steps

### Common peak/floor and squared-cost chain (d440:45–98, 107–153)

For an arbitrary feasible probability measure, integrate the all-event inequality over the full closed diamond. Tonelli gives `2 mu(A) <= b^(-1)|A|`; consequently the law is absolutely continuous and its density is bounded by `1/(2b)`. Taking limsups of averages over shrinking balls gives a representative bounded pointwise by its essential supremum `M` and satisfying `p(y)>=b p(x)` for **every** `x,y` with `||x-y||_1<=1`: the event inequality compares the balls for each fixed shift, so no uncountable union of null exceptions is used. A `(1-eta)M` point creates the stated floor on its translated diamond. Removing that floor leaves `0<=g<=M` and mass `1-2b(1-eta)M`.

For `c_lambda`, even convexity minimizes the translated diamond integral at 0, and its Euclidean part improves this to `F(x)>=C_D+2||x||_2^2`. Homogeneity gives sublevel area `A t` and cost integral `A t^2/2`. Subtracting the threshold times equal masses verifies the bathtub bound `integral c g >= h^2/(2AM)`. Letting `eta->0`, with `x=bM<=1/2`, I obtain exactly

```
E c >= C_D x + b(1-2x)^2/(2 A x)
    >= sqrt(2b C_D/A+4b^2/A^2) - 2b/A.
```

The matching **normalized** geometric-shell law has a core of scale `s=b^(1/4)`. Its core cost moment and first privacy layer each contribute `C_D b`; the core normalizer is `A C_lambda s^2`, and higher layers and the first layer's boundary error are controlled as claimed. Its index changes by at most one for every `h in D`, giving all-event privacy. This yields the lower/upper leading constant and error stated in d440.

Near equality in the floor/bathtub sum forces `y=s^2 M -> y0`, translated peak `x->0`, and nonnegative deficit `Delta->0`. With `T=h/(A y)`, subtraction from `y 1_{c<=T}` gives exactly `||g#-g0||_1 <= Delta/d+2Ayd`; the scaled floor mass vanishes. This establishes the all-near-optimal TV limit. The rescaled cost limit is `C`, whereas the uniform cost-body law has cost `C/2`; TV convergence does not imply W2 convergence. These arguments use no optimizer existence or symmetry.

### Tail profile (62e4:40–103) and changing weights (7abb:43–107)

Using the d440 conclusions and `c(z)>=||z||_2^2`, the residual mass outside any fixed original radius `r` divided by `s^2` is at most `Delta/(r^2-s^2 T)`. Its cost outside that radius is at most `Delta+T` times the scaled residual tail mass. The floor coefficient tends to `y0`, its translated indicator tends to `1_D` in L1, and its cost measure tends to `y0 c 1_D dx`. The residual cost measure has total mass `C/2` and concentrates at 0. This reconstructs both 62e4 limits and the Euclidean disk subtraction for `r<1/sqrt(2)`.

For 7abb, `c_theta=||x||_2^2+2 theta |x1 x2|`; hence `||x||_2^2<=c_theta<=2||x||_2^2`, giving parameter-independent geometry and shell bounds. The quadratic bathtub minimizer `f_theta(y)=C_D(theta)y+1/(2 A_theta y)` is uniformly strongly convex on the common compact interval of attainable `y`; the band-area bound remains uniform. Thus moving `theta_n` needs no convergent subsequence assumption. For `theta_n->theta0`, uniform bounded second moments also control the difference between `c_theta_n` and `c_theta0`, establishing the stated non-W2 result. The rapidly growing `lambda` interpretation is through `H_theta=H_lambda/(1+lambda)`: no lambda-independent additive error for the *unnormalized* `H_lambda` is claimed here.

### First-norm chain (fa39:40–112)

The diamond's area and first-norm integral are `2r^2` and `4r^3/3`. For remaining mass `h` and cap `M`, the strict bathtub optimum is `(2/(3sqrt(2)))h^(3/2)M^(-1/2)`. Together with the floor this gives fa39 (5). The tangent bound `(1-2x)^(3/2)>=1-3x` yields

```
F_b(x) >= (4/3)x + [2/(3sqrt(2))]sqrt(b/x) - sqrt(2bx).
```

The first two terms minimize to `C b^(1/3)` at `x=y0 b^(1/3)`, with `C^3=2`, `y0^3=1/32`. If `x<=2b^(1/3)`, the subtracted term is at most `2b^(2/3)`; otherwise the original nonnegative floor is already at least `(8/3)b^(1/3)>C b^(1/3)`. This verifies the all-b lower bound. The correctly normalized diamond shell has ratio `(2/3)M3/M2` and gives the matching leading value.

The exact scaled deficit yields `y->y0`. For the peak location, the coordinate marginal of D is `2(1-|u|)`, giving `G(a)-G(0)=2a^2-(2/3)a^3` for `0<=a<=1` and a strictly positive, coercive continuation for `a>1`. Hence near equality forces `x->0`. The threshold-band argument gives uniform-on-`C D` TV convergence, while the scaled first-norm cost splits into core `2C/3` and floor `C/3`, proving the stated tail/cost measures and non-W1 conclusion. The cross-objective TV-to-one corollary additionally uses d440's `b^(1/4)` scaling: the first-norm core's `b^(1/3)` scale is asymptotically smaller.

### Mixture and sharp exponent (35fc:27–68; a740:35–102)

For any laws L,E and `0<=w<=1`, `TV((1-w)L+wE,E)=(1-w)TV(L,E)`, so the overlap is at least `w`. The squared shell has first norm `O(b^(1/4))` by Cauchy–Schwarz; `b^(1/8)` contamination contributes `O(b^(3/8))=o(b^(1/3))`. With `w=b^(1/12)/log(1/b)`, the contribution is instead `O(b^(1/3)/log(1/b))`. Both give the claimed counterexamples once the two peak-floor value bounds are imported.

The exact-epsilon assertion is not merely convexity: sufficiently far in the positive quadrant, the diamond-core index is `ceil(x1+x2-q)` and the disk-core index is `ceil(x1+x2-sqrt(2)R)`. An open rectangle can be chosen away from all shell boundaries; translating it by `e1` raises every component's index by exactly one. All components, and hence their mixture, lose the common factor b on the same event, proving the privacy budget is attained.

For a740, the first-norm bathtub deficit gives `P_L(B_2(r)^c)<=O(b^(1/3))+2 b^(1/3) Delta/r` once `r>=2K b^(1/3)`, and d440 gives `P_J(B_2(r))<=C b^(-1/2)r^2`. At `r=max(b^(5/18)Delta^(1/3),2K b^(1/3))` the leading bound is `b^(1/18)Delta^(2/3)` plus `b^(1/6)+b^(1/3)`, hence little-o for each near-optimal sequence. For sharpness, the extra diamond core has `q=b^(5/18)`, `q^3>>b`, and `w=b^(1/18)/log_2(1/b)`, so its mean contamination is `o(b^(1/3))`. It lies inside the squared shell's core, and `w p_B ~ b^(-1/2)/(2 log_2(1/b))` is eventually below the squared-shell density there; its own top-core mass tends to one. After the notation correction above, this gives the stated lower overlap and excludes every stronger fixed power.

The little-o is quantified **for each admissible near-optimal pair of sequences**; these arguments do not provide a single sequence-independent little-o modulus without a common quantitative near-optimality assumption. The explicit pair itself disproves every exponent `1/18+eta`, so that sharpness conclusion does not require such a modulus.

## Own exact constants and exponent checks

`exact-fraction-check-v1.py` and its exclusive-created `.txt` receipt are my own code/output, not an author replay. The script exited 0 and uses `fractions.Fraction` throughout its rational algebra. It integrates monomials over four reflected simplices, independently obtaining `|D|=2`, `integral_D ||x||_2^2=2/3`, `integral_D ||x||_1^2=1`, and `integral_D ||x||_1=4/3`. Thus `C_D(lambda)=2/3+lambda` and `C_D(theta)=(2+theta)/3`.

Independently, substituting `t=tan(phi)` in the quadrant polar integral gives

```
A_lambda = 2 integral_0^infinity dt / [(1+lambda)(1+t^2)+2lambda t]
         = 2/sqrt(1+2lambda) * [pi/2-arctan(lambda/sqrt(1+2lambda))],
A_theta  = 2 arccos(theta)/sqrt(1-theta^2),  A_1=2,
A_lambda = A_theta/(1+lambda),  theta=lambda/(1+lambda).
```

The exact Fraction checks of the rational coefficients, retaining pi and sqrt(3) symbolically, give `A_0=pi`, `A_(lambda=1)=2pi/(3sqrt(3))`, `A_(theta=1/2)=4pi/(3sqrt(3))`; and

```
C_0^2=4/(3pi),  C_(lambda=1)^2=5sqrt(3)/pi,
C_(theta=1/2)^2=5sqrt(3)/(4pi),  C_(theta=1)^2=1.
```

The script also checks the lambda-zero `y0` squared identities, the first-norm density normalization `2 y0 C^2=1`, the `1/3 : 2/3` floor/core split, translated-norm polynomial, and exact geometric shell moments at rational parameters. Its Fraction exponent checks include

```
1/8+1/4=3/8>1/3;  1/12+1/4=1/3;  1/8-1/6=-1/24;
1/3-5/18=1/18;  -1/2+2(5/18)=1/18;
1/18+5/18=1/3;  5/18-1/4=1/36;  3(5/18)=5/6<1.
```

The exact scripts are bounded arithmetic checks, not a numerical proof of arbitrary-lambda transcendental identities, privacy, asymptotic limits, or independent-family acceptance; the latter were analyzed in the written reconstruction above. The PMLR objective-attribution remark (fa39:34), the older 7307 exact-optimizer rate (35fc:7), and any LAW642, v241, MDA, f68 or external-publication/priority claims were **not** independently verified and are not imported as premises. No author contact, external-model call, source-priority claim, or publication action occurred.
