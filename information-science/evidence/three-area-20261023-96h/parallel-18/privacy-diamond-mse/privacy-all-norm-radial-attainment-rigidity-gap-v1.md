# All norms and ALL radial profiles: attainment, two-level rigidity, and the exact core-conditioned MSE gap

Owner InfoResearch96h-2, original info-1/privacy diamond MSE.
Actual `/bin/date` BEFORE this write: **Mon Oct 26 11:52:12 PDT 2026**.
Status: **NEW AUTHOR-WRITTEN CANDIDATE. No independent acceptance, novelty or parameter-region claim.**

## 0. Authority, ancestry and proof cut

This follows ACTUAL v142-A RETURN, NEW whole-primary ACK `116920a6256610ae466738d1077b0d142f56d404b9a88236257c6bc19b089c44` written/sent, Main's actual complete read, and explicit future-only original-primary direction v89 (`32fba021bc6817d703eaefeeeedd4f7494aaac561dc146e0ca2f424df7388569`). I read ALL72LF of v89 FIRST before primary source/proof work. Checkpoint121 at11:49:56 saves the current all-variable proof.

The support-function rigidity QUESTION was already held in checkpoint109, not first discovered here. This paper now supplies a complete proof, plus a prospective ALL-profile compact-attainment theorem. The prior checkpoint096 concerned only norm-EXP densities. Here the radial profile is arbitrary and may have discontinuities, infinitely many levels, nonmonotonicity, and arbitrary centre. This paper does not repeat an EXP-only result as a new discovery.

Entire cp102 AD33 and checkpoint108 probe/branch-range/consuming guidance remain ZERO. This proof assigns NO epsilon or b to a rounded/diamond parameter region; no root-location comparison or trial is used. The general closure theorem is about ALL norm-radial probability densities with a positive-density weak limit. The rigidity theorem is about ALL convex Minkowski cores. Their proofs use no quarantined formula, value or result. This is explicit source/dependency separation, not a retrospective private-history or timestamp-based noninfluence certificate. Auxiliary214 remains strict STOP.

**Named correctness input LAW642:** `privacy-all-law-optimum-self-contained-v1.md`, SHA `957cab2bcf3eff1860ff9f4b5a1e5838708aceaf894a97fdc2c5244c3e7d8e53`, entire642LF for a whole dependency gate. Current source reads in this continuation: LF19–55,57–78,421–439,549–606,623–642. No fresh entire642LF read is claimed. The exact exports used are:

1. Every full-closed-diamond-private law has a density positive a.e.; the feasible probability class is weakly closed; squared cost is weakly lower semicontinuous; the feasible Laplace law has cost4/epsilon² (LF57–78).
2. A unique optimal probability law exists. For 0<b=e^-epsilon<1 it has the representative `p_*(x)=Z^-1 b^n(x)`, `n(x)=min{k>=0:x∈S+kD}`; D is the closed unit-l1 diamond, S is a compact convex centrally symmetric body with0 in its interior (theorem LF19–55 and LF501).
3. `S={|x|_1<=2t, |x|_2²+2m|x|_infinity+T2<=lambda}`, with t>0 and m=b/(1-b)>0. Its screened alternatives are a full diamond facet, or an arc of positive length followed by the facet (LF421–439,549–606).

Ordinary inputs named explicitly: planar polar integration/Tonelli, Radon–Nikodym, finite-moment Markov/Jensen, Prokhorov/Portmanteau, weak convergence of products and the continuous-mapping argument off a null discontinuity set; elementary convex support/radial functions; Blaschke selection for compact convex subsets of a fixed ball (equivalently Arzela–Ascoli on their uniformly Lipschitz support functions). No source-specific theorem about a matched norm is used. None of these general facts is claimed formal/kernel-verified here.

## 1. Entire class and theorem

Fix ANY finite epsilon>0. Let D be the full closed unit-l1 diamond. A law is private if `mu(E)<=e^epsilon mu(E+h)` for EVERY Borel E and EVERY h∈D, exactly the registered model. Write `J(mu)=∫|x|_2² dmu` and V for its unrestricted infimum.

A genuine norm body K is compact, convex, centrally symmetric, with0 in its interior. Write its gauge as `g_K(x)=||x||_K`. Let `N_epsilon` be ALL feasible laws of finite J having some density

`p(x)=phi(g_K(x-a))` a.e.,

for SOME genuine K, SOME centre a∈R² and SOME nonnegative Borel function phi. No monotonicity, staircase, finite-parameter, continuity, bounded radial support or predefined relation between K and D is imposed. Let `V_N(epsilon)=inf_(mu∈N_epsilon) J(mu)`.

**Theorem N.**

- N_epsilon is nonempty, its infimum is finite, and this infimum is ATTAINED by an actual law in the SAME entire class.
- The registered unique optimum mu_* belongs to N_epsilon **iff** its actual core S is homothetic to D.
- Consequently `V_N=V` in the full-diamond case, while `V_N>V` when the actual core has a genuine rounded arc. This is a positive gap for EACH such fixed epsilon, not an evaluated or uniform gap.

No existence of a rounded-core epsilon region, transition value or numerical branch range is asserted by this theorem.

## 2. Polar product structure for arbitrary radial profiles

Put `u(theta)=(cos theta,sin theta)`, and let `R_K(theta)>0` be K's continuous Euclidean radial function. Then `g_K(r u(theta))=r/R_K(theta)`. For a centred norm-radial density, substitute `r=s R_K(theta)` into ordinary polar integration:

`dx = r dr dtheta = s R_K(theta)^2 ds dtheta`.

Since `∫R_K(theta)^2 dtheta=2|K|`, unit total mass gives `2|K| ∫_0^infinity s phi(s)ds=1`. Therefore under the measurable bijection outside0

`T_K(x)=(g_K(x), x/|x|_2)`,

the law is EXACTLY the PRODUCT

`rho(ds) ⊗ nu_K(dtheta)`,

where `rho(ds)=2|K| s phi(s)ds` and `nu_K(dtheta)=R_K(theta)^2 dtheta/(2|K|)`.

Thus radius and direction in these coordinates are independent, and the angular law depends ONLY on K, not on phi. This holds for arbitrary Borel phi by Tonelli, including nonmonotone/discontinuous profiles. No extra symmetry or radial monotonicity is silently assumed.

Scaling K changes phi but not the represented class or angular law. Hence normalize EVERY K below to Euclidean circumradius1.

## 3. Closure lemma at a nondegenerate positive-density limit

**Lemma C.** Suppose mu_j are centred norm-radial probability laws, each with a density, and mu_j converge weakly to a law mu with density positive a.e. Then some genuine norm K and Borel phi represent mu as `phi(g_K(x))dx`.

### 3.1 The limiting body cannot collapse to a line

Normalize circumradius(K_j)=1. Blaschke gives a subsequence K_j→L in Hausdorff distance; L is compact convex and centrally symmetric, with circumradius1. If L has empty interior, it is the segment `[-v,v]` for a unit v, not a point.

Choose v_j∈K_j of Euclidean norm1 and pass to a further subsequence so v_j→v (changing v's sign if needed). Let `w_j=max_(z∈K_j)|det(v_j,z)|`. Hausdorff convergence to the segment gives w_j→0. Each w_j is strictly positive because K_j is genuine.

Pick z_j attaining this maximum. The inscribed parallelogram `conv{v_j,-v_j,z_j,-z_j}` has area2w_j. Therefore `|K_j|>=2w_j`.

For ANY fixed delta>0, directions with `|det(v_j,u(theta))|>=delta` have `R_Kj(theta)<=w_j/delta`. The angular product formula consequently gives the ALL-variable bound

`nu_Kj(those directions) <= (2pi*w_j²/delta²)/(2|K_j|) <= pi*w_j/(2delta²) ->0`.

So every weak angular limit is supported on the two directions ±v. On the other hand, x↦x/|x| is continuous off0 and mu({0})=0. Thus these angular laws converge weakly to the actual angular law of mu. That law gives positive mass to every nonempty open arc, because mu has positive density a.e. (integrate over any nontrivial annular sector). This contradicts two-direction support. Hence L has interior and is a genuine K.

### 3.2 Product structure survives the limit

Let K=L. Its inradius is positive. Hausdorff convergence plus this inradius yields multiplicative inclusions between K_j and K with factors tending to1: use `K_j⊂K+eta B_2` and `K⊂K_j+eta B_2`, with both inradii bounded below eventually. Hence gauges converge uniformly on bounded sets, radial functions converge uniformly on the unit circle, areas converge, and `nu_Kj→nu_K` even in their continuous angular densities.

The varying maps `T_Kj(x)=(g_Kj(x),x/|x|)` converge uniformly on compact annuli to T_K. Tightness controls the tails; mu({0})=0 controls the excluded small ball. The continuous-mapping argument therefore gives

`(T_Kj)#mu_j -> (T_K)#mu` weakly.

Its radius marginals rho_j also converge, to some probability rho. Each joint law equals `rho_j⊗nu_Kj` by §2. Products of weakly convergent probabilities converge weakly (first for products of bounded continuous tests, then by compact approximation and tightness). Consequently

`(T_K)#mu = rho⊗nu_K`.

Finally planar Lebesgue measure in the SAME coordinates is `2|K| s ds nu_K(dtheta)`. Since mu is absolutely continuous and has no atom at0, rho is absolutely continuous with respect to s ds on s>0. Taking its Radon–Nikodym derivative, set `phi(s)=d rho/ds /(2|K|s)` for s>0, with any Borel value at0. The last product identity gives exactly `mu(dx)=phi(g_K(x))dx`. This proves Lemma C with no assumed profile regularity or pointwise convergence of the profiles.

## 4. Attainment for the WHOLE private norm-radial class, including translated centres

The product Laplace density from LAW642 is centred l1-norm-radial, feasible and of finite cost, so N_epsilon is nonempty and `V_N<=4/epsilon²`.

Choose a minimizing sequence mu_j∈N_epsilon with costs uniformly bounded. It is tight by Markov. If a_j is a chosen radial centre, symmetry about a_j and finite first moment imply `a_j=∫x dmu_j`; Jensen gives `|a_j|²<=J(mu_j)`. Pass to a subsequence with a_j→a and mu_j→mu weakly.

LAW642's ALL-shift weak closedness makes mu feasible. Portmanteau gives finite `J(mu)<=liminf J(mu_j)=V_N`. LAW642's density consequence makes its density positive a.e. No fixed h-dependent subsequence or density-exception intersection is introduced here.

Translate mu_j by -a_j. These centred laws converge weakly to the translate of mu by -a, which still has positive density a.e. Lemma C supplies a genuine K and arbitrary Borel phi for that translated limit. Thus mu itself belongs to N_epsilon, centred at a. Since V_N is an infimum over exactly that class, the reverse inequality J(mu)>=V_N holds. Equality follows: an ACTUAL class minimizer exists.

This is compactness of the represented LAWS, not compactness of an arbitrary parametrization phi, not a bound on all norms a priori, and not an assumption that a finite-dimensional staircase family suffices.

## 5. Two-level homothety rigidity for ANY Borel radial profile

**Lemma H.** Let S,D be compact convex bodies with0 in their interiors, and consider a density with levels `S+kD` and distinct geometric heights `C b^k`, 0<b<1. If the law is norm-radial about0 in ANY genuine K with ANY Borel profile, then S and D are homothetic to that same K. Conversely, when S=rD with r>0, the density is radial in D.

Only the top TWO levels are needed. For i=0,1 fix any threshold strictly between Cb^(i+1) and Cb^i. Its strict superlevel agrees a.e. with `K_i=S+iD`; boundaries of these convex bodies have zero area. If `p(x)=phi(g_K(x))` a.e., its threshold indicator is some common Borel function psi_i(s) of s=g_K(x).

Polar Fubini says that for a.e. theta this psi_i agrees a.e. in s with the interval indicator

`1_[0,a_i(theta)](s)`, where `a_i(theta)=R_Ki(theta)/R_K(theta)`.

Indeed K_i meets each ray in its full interval from0 to R_Ki(theta). Two such intervals agree a.e. only if their endpoints agree. Fixing one good direction shows a_i(theta) is constant for a.e. theta. The radial functions are continuous, so the equality extends to EVERY direction. Thus

`S=a_0 K`, `S+D=a_1 K`.

Taking support functions gives `h_D=(a_1-a_0)h_K`. Since h_D,h_K are positive on nonzero covectors, a_1-a_0>0. Support functions determine compact convex bodies, so `D=(a_1-a_0)K` and S is a positive homothet of D. This proves the necessity without assuming phi is nonincreasing or its other superlevels are balls.

For the converse, S=rD gives `n(x)=max(0,ceil(g_D(x)-r))` (the exact closed-boundary convention fixes only a null set), an explicit D-radial Borel profile.

For the registered optimum, arbitrary translated radial centres add no escape. A norm-radial finite-MSE law has mean equal to its centre. The D4-symmetric optimum has mean0, so any such centre must be0. Its core S has all hypotheses of Lemma H by LAW642. Hence mu_* belongs to N_epsilon iff S is homothetic to D.

## 6. Entire-class equality/gap dichotomy, with NO epsilon branch allocation

By §4 choose an actual minimizer mu_N of the entire norm-radial class. Feasible-class inclusion gives `J(mu_N)>=V`.

- If S=rD, §5 places the UNIQUE original optimum in N_epsilon, so `V_N=V`.
- If S is not homothetic to D, §5 excludes mu_* from N_epsilon. If J(mu_N)=V, LAW642's uniqueness of the original optimal LAW would force mu_N=mu_*, contradiction. Thus `V_N>V`.

The attained-class argument is essential: nonmembership alone would not give a positive infimum gap. Theorem N gives a strict positive gap for each fixed nonhomothetic-core epsilon, not a numerical lower estimate, not a uniform-in-epsilon constant, and not a uniquely identified norm-class minimizer.

The printed CLIP/core formulas identify the geometric alternatives without any new parameter test. In the full-facet case S=2tD, so equality holds. In the rounded case c=t-d>0 and its free octant profile on0<y<c is

`F(y)=sqrt(A-y²)-m`, `A=lambda-v`, `A-c²=(t+d+m)²>0`.

Its exact second derivative is `F''(y)=-A/(A-y²)^(3/2)<0`. A diamond's corresponding profile is affine `2t-y`. Thus a positive free arc cannot be a homothetic diamond, so the strict gap conclusion applies. At c=0 the same geometric core is the D boundary, not a second law or an alleged new branch. These are ALL-variable consequences of the supplied screens; NO b/epsilon is assigned to either side.

## 7. What this adds, source applicability and exact nonclaims

The prior norm-EXP compactness lead restricted phi to an exponential. This theorem instead handles EVERY Borel radial profile, EVERY genuine norm and EVERY translated centre; it proves actual class attainment and the two-level homothety criterion. The support-function question itself was an already-held pre-event lead. These are mathematical representations and conditional strict gaps, not a new mechanism, improved value of V, fresh all-law proof or discovery-count/priority claim.

If a source theorem supplies only densities radial in some norm, it cannot supply the registered optimum WHEN the actual core has a positive arc, even allowing its norm and profile to vary freely. Conversely the full-diamond case is in that broad radial class. Neither implication authenticates any particular source's hypotheses, says every source law is private for D, or clears worldwide novelty. Origin-box ideal/Minkowski-core source families that are NOT norm-radial are not excluded by this theorem. Nonadditive/data-dependent channels remain outside the registered target and this comparison.

FIRST remaining acceptance: freeze/read this ENTIRE new body with ENTIRE LAW642 (and its actual parent/adoption/errata boundaries) for separate mathematics AND dependency/application/trust verdicts. No favorable component review or old EXP result automatically accepts it. In particular the convex-body selection/degenerate-angular-limit/product-closure proof needs its own complete check. No formal/kernel/human/configured-family/executable/novelty status follows from this same-author packet.

All own firstFIVE/SIXTHv111B/SEPARATE077/cp102/v128cadence/checkpoint108postv60+prepin/v69 histories remain individually named. No orthogonal-review fact is a privacy premise. Entire cp102/cp108guidanceZERO; auxiliary214STOP. No source/frozen/shared edit, Git/deletion/publication/externalmodel/scientificinterpreter/Eval/calculator/program/CAS/enumeration/solver/replay/buildtest/CLI/nestedagent/newGO or chosen-parameter/control/state/boundary/magnitude/decimal trial occurred. No identity was machine-checked. Same18/originalprimary/OWN/HOLD/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/actual30minsubstantiveincludingblocked/noearlypark or round closeout.
