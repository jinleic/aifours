# f14 — independent written review of the fixed-Lipschitz privacy cap

**Verdict: NO_SUBSTANTIVE_DEFECT AT THE CANDIDATE'S STATED AT-MOST-ε SCOPE; 0 FATAL / 0 MAJOR / 0 MINOR.** An **exact-minimal-privacy-parameter minimizer** is separately **NOT_RECONSTRUCTED / NOT CLAIMED**: the explicit smoothing witness has exact ε, but the paper explicitly does not assert that every or any attained H_L minimizer has exact parameter ε. If the assignment's phrase “exact-eps laws” demands equality for the minimizer rather than the standard ε-DP inequality, that stronger scope is not supplied; this is a scope boundary, not a fabricated defect in the author's expressly narrower claim.

Actual native prewrite observation: **Wed Oct 28 17:16:59 PDT 2026**. Review by InfoHinfPreview-2 (info-3) of InfoResearch96h-2 (info-1): disjoint slot, same track and same harness. Prior topic/context familiarity is not denied; no blindness, independent-model, formal/kernel, human or novelty acceptance is claimed. No author contact.

## 1. Exact sources, registered scope and conditional import

- Assignment `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f14-privacy-lipschitz-cap/assignment-v1.json`, SHA `4ffd0cd68f0250f58bb98f754b0b4558c968ffe6bb344fe5ea940314c73f3e0e`, read completely FIRST.
- Complete candidate `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-lipschitz-cap-attainment-v1.md`, SHA `733d2b2761c86e6f349535578f45e753686d62367c24cb84d583285f04856842`, all 157 LF read in raw windows 1–55,56–110,111–157 through ending.
- Registered info-1 intake envelope SHA `06a76efd7573f3d67971560f0609f97d9af6872e5286aa46abf69fe2ce84d0b`, entire object: the registered model is query-output-independent planar additive noise, every shift in the full CLOSED unit-l1 diamond, finite ε>0, squared EUCLIDEAN cost, all Borel laws. No squared-l1 or nonadditive objective is substituted.
- Named LAW642 parent disposition `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/privacy-all-law-self-contained-parent-v1.md`, SHA `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`, read lines 1–40. It supplies a finite optimum V and UNIQUE all-law optimizer with `p_*(x)=Z^(-1)b^n(x)`, `n(x)=min{k>=0:x in S+kD}`. It is an explicit **conditional same-harness written import** here; I did not independently reread/reprove its 642-LF source. Its explicit S definition makes S compact convex with nonempty interior: its two continuous convex inequalities are strict at zero because `t_*>0` and `lambda_*>T2`. No stronger source/novelty/formal gate is inferred.

Every body/pin above was observed as stated. My prior knowledge of privacy/preview reviews is not a mathematical premise; earlier quarantined results are not silently revived. The verification below independently reconstructs this candidate's used steps conditional on LAW642.

## 2. Statement ledger and privacy-parameter boundary

For each finite ε>0 put b=e^(−ε) in (0,1), D={|h1|+|h2|<=1}, and F_ε the laws satisfying `μ(A)<=b^(-1)μ(A+h)` for every Borel A and every h in the FULL closed D. For every fixed L>0, H_L consists of laws in F_ε having a globally L-Lipschitz Euclidean density version. The actual candidate claims:

1. H_L is nonempty, the minimum V_L of the squared Euclidean objective is attained, and `V_L>V`.
2. `0<V_L−V<=2/(3Z²L²)`, with a **separately exhibited** C¹ witness whose smallest privacy parameter is exactly ε.
3. For an actual positive jump height w depending on ε and all sufficiently large L, `w²/(8L)<=inf_(H_L) TV(μ,μ_*) <=[P(S)+4sqrt(2)b/(1−b)]/(sqrt(6)Z²L)`.

The minimum in item 1 is over **at-most ε privacy**. Candidate LF21–23 explicitly says it does not assert exact privacy for its minimizer. The full-shift saturation of one witness pays its exactness, not the minimal parameter of an arbitrary minimizer. Therefore all three statements above are supported conditional on LAW642; an attained optimizer restricted to laws of *exact* smallest privacy parameter ε remains NR if that is independently required.

## 3. Constructive all-shift privacy, C¹ cap and cost

For the independent triangular product kernel `phi(u)=(1−|u1|)_+(1−|u2|)_+`, each one-dimensional triangle integrates to one, has zero mean and second moment 1/6; the two-dimensional U has `E|U|²=1/3`. Thus for X~μ_* independent of U, `J(X+tU)=V+t²/3`: the cross term vanishes, and finite V pays first-moment integrability. This is the original squared Euclidean objective.

For EVERY h in the closed diamond, integrate μ_*(A−tu)<=b^(-1)μ_*(A+h−tu) over u. Tonelli gives the same Borel-set inequality for μ_t. There is no reduction to a finite set of shifts. The kernel is nonnegative, normalized and supported on the square; q_t=p_* * phi_t is a density.

For each coordinate the weak derivative of the scaled kernel has integral zero and L1 norm 2/t. With `0<=p_*<=1/Z`, write its integral against the signed derivative using the positive and negative parts, each having mass 1/t. This gives `|partial_i q_t|<=1/(Zt)`, not the larger unbalanced L1 estimate. Translations of an L1 kernel are continuous, so both convolved derivatives are continuous; hence q_t is C¹. The Euclidean gradient bound is sqrt(2)/(Zt). Choosing t=sqrt(2)/(ZL) gives an actual H_L witness and exact cost increase `2/(3Z²L²)` for EVERY L>0.

## 4. Exact ε for the witness, including shell boundaries

Choose B larger than both coordinate suprema of S and let `c=max_(s in S)(s1+s2)`. If x1,x2>B, compactness of S gives the exact l1 distance `x1+x2−c`; closed S+kD then gives `n(x)=ceil(x1+x2−c)`. For x1,x2>B+t and u in the kernel support, both x−tu and x+(1,0)−tu are in this quadrant and their distance parameters differ by exactly one. Thus the ceiling identity gives

`p_*(x+(1,0)−tu)=b p_*(x−tu)`

including shell-boundary points; after convolution `q_t(x+(1,0))=b q_t(x)`. An actual nonempty bounded open rectangle E in that quadrant has positive q_t mass. Its Borel ratio `μ_t(E)/μ_t(E+(1,0))=1/b=e^ε` shows that the witness's smallest valid privacy parameter is ε. The boundary shift (1,0) lies in the specified CLOSED D. This is not an assertion of exactness for the H_L minimizer.

## 5. Weak closure, tightness, attainment and strict gap

For any nonnegative globally L-Lipschitz probability density, q(x)=M forces q>=M/2 on the disk of radius M/(2L), so `1>=πM³/(8L²)`. This provides the claimed uniform bound even without an attained global density maximum. A continuous density version which is nonnegative only almost everywhere is nonnegative everywhere, since a negative value would give a negative open ball.

For a weakly convergent sequence in H_L, that global bound and common Lipschitz constant give locally uniform convergence along a diagonal subsequence by Arzelà–Ascoli. Integrals against C_c tests identify the SAME weak limit as q(x)dx, a probability law; the limit q is globally L-Lipschitz and nonnegative. Thus no mass is lost or invented in the density identification.

For a fixed arbitrary h in D, the Borel privacy inequality is equivalent to `∫f dμ<=b^(-1)∫f(x−h)dμ(x)` for nonnegative C_c f. Both sides pass through the SAME weak limit, and Radon measure order returns the full Borel inequality. Because h was arbitrary and no h-dependent subsequence was selected, ALL shifts hold for the one limit law. A uniformly bounded second moment makes minimizing sequences tight; weak lower semicontinuity of |x|² and weak closure give an actual minimizer. The witness gives finite upper value.

For strictness choose any sufficiently far integer shell diagonal from LF78–84. On the two adjacent open sides the density takes different constants a and ab. A continuous representative agreeing a.e. with p_* would equal those constants everywhere on the respective open sides, contradicting continuity at their common boundary. By LAW642 uniqueness of the all-law minimizing PROBABILITY LAW, no law in H_L has cost V. Since the H_L infimum is actually attained, V_L>V; lack of attainment cannot be hidden in that step. No positive gap over the union of all L or all continuous densities is claimed.

## 6. Every strip constant and total-variation lower bound

Let k be large enough that the paper's far-quadrant condition holds and put `a=b^k/Z`, `w=a(1−b)>0`. In orthonormal coordinates `r=(x1+x2−c−k)/sqrt(2)`, `s=(x1−x2)/sqrt(2)`, the Jacobian is one. On |s|<1/2 and |r|<d0=1/(4sqrt(2)), the stated choice of k puts both coordinates above B; also |sqrt(2)r|<1/4, so the strip meets only the one integer shell boundary. The values are a on r<0 and ab on r>0, ignoring the zero-area line.

For any L-Lipschitz probability density q, on paired positions the Euclidean separation is 2r, so

`|q(s,−r)−a|+|q(s,r)−ab|>=w−2Lr`.

For `L>=w/(2d0)=2sqrt(2)w`, choose d=w/(2L)<=d0. Integrating on the tangent interval of length ONE and 0<r<d yields `∫|q−p_*|>=w*d−L*d²=w²/(4L)`. Total variation of probability densities is half that L1 integral, giving `TV>=w²/(8L)`. This lower bound uses NO privacy of q and applies to every probability law possessing such a density version. Small L is explicitly outside this lower-rate range.

## 7. Perimeter/translation estimate and TV upper constant

The nested sets K_j=S+jD give the exact nonnegative a.e. expansion `p_*=(1−b)Z^(-1) sum_(j>=0)b^j 1_(K_j)` by a geometric series. For any planar compact convex K and translation y=re, slice by lines parallel to e. Each intersection is an interval, whose translated symmetric difference has length at most 2r. Integration over the transverse projection gives `||1_K(.−y)−1_K||_1<=2r width_K(e_perp)<=r P(K)`; the last inequality follows because the total variation of the transverse coordinate around the boundary is twice its width. This reconstructs the stated BV shift bound for the actual convex sets without assuming differentiability of their boundaries.

The ordinary planar convex Cauchy perimeter formula expresses P as the integral of directional widths. Width is additive under Minkowski sums, so `P(S+jD)=P(S)+jP(D)=P(S)+4sqrt(2)j`; the diamond's four sides each have length sqrt(2). Thus

`TV(μ_t,μ_*) <= [t E|U|/(2Z)] [P(S)+4sqrt(2)b/(1−b)]`.

Cauchy-Schwarz gives E|U|<=1/sqrt(3). Inserting the SAME cap-satisfying t=sqrt(2)/(ZL) yields exactly the candidate's `1/(sqrt(6) Z² L)` coefficient. Combined with the strip lower bound this proves the fixed-ε Θ(1/L) TV statement conditional on LAW642. It does not prove any corresponding lower COST rate.

## 8. Independent exact checks actually run

The reviewer wrote and ran once `frontier-review-f14-privacy-check.py`, SHA `1b6bcfa8e4bf132c6240e0764da412b3a43d99b4e423a706864de0e3d678633d` (81 LF / 3515 bytes), using Python 3.14.3 and `fractions.Fraction`. Command from the reviewer root: `python3 frontier-review-f14-privacy-check.py`.

Observed output: triangular mass `1`, two-dimensional variance `1/3`, derivative L1 norm per coordinate `2`; independent paired-strip identity `PASS` (synthetic jump 5/37, L=11/7, integral 175/60236 and TV 175/120472). For a separate SYNTHETIC square-plus-diamond geometry, four side-length squares were 16/49 and four were 50/9, matching `8a+4sqrt(2)j`. For a SYNTHETIC diamond-core staircase with b=2/3, 400 exact rational quadrature points gave shifted q1=b q0 exactly, q0=81064/2460375, q1=162128/7381125, ratio=3/2.

These chosen cores/parameters are NOT claimed to be LAW642's actual optimum. The quadrature equality concerns the finite rational quadrature, not an independent exact evaluation of the full continuous convolution. The checks do not establish uniqueness, weak closure, all-variable strictness or the theorem; those are the written reconstruction and stated LAW642 import above. No author checker output was used as independent evidence.

## 9. Exact remaining scope

Subject to LAW642 and the named ordinary compactness/convex-geometric facts, no substantive mathematical defect was found in the candidate at its actual at-most-ε model and all L>0. The exact-ε witness is genuine; exact-parameter ε of an attained H_L optimizer is neither proved nor claimed. No assertion of unique H_L minimizer, sharp lower COST rate, unrestricted book/general-channel solution, ε endpoint, SOURCE-MATCH-U1 or worldwide novelty follows. Scientific computations are the explicitly reported bounded checks only; no configured-family/external-model, formal/kernel, human or parent scientific acceptance is conferred. All historical quarantine/process records remain historical and no held result is accepted by association.
