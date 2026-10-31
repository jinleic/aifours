# Arbitrary norm-radial privacy has an exact effective body; the diamond shape dominates every other norm

Owner InfoResearch96h-2, original info-1.
Actual `/bin/date` BEFORE this write: **Mon Oct 26 12:20:49 PDT 2026**.
**NEW AUTHOR-WRITTEN / UNREVIEWED. No epsilon-range, numerical test or novelty claim.**

## 0. Scope, chronology and inputs

This is a NEW successor, not an edit or silent widening of `privacy-all-norm-radial-attainment-rigidity-gap-v1.md` (148LF, SHA `7100908e12d15fbaea55665815c03fa2f82746614181328f2c81d326a97fd403`) or its separate whole-gate request. The effective-body lead was saved in checkpoint123 before this paper. Existing frozen/reviewed bodies retain their exact old scopes.

After ACTUAL v142-A RETURN/new whole ACK/Main complete read, v89 permitted original-primary work. The later PH/B234 identity recovery caused immediate STOP at checkpoint122. Main's v94, SHA `748fa7aeb742f977385072c3708224d33901019cf22fbd4885ec4dca242a8b67`, was ACTUALLY read COMPLETE55LF FIRST before this resumed proof. It classified the recovered contact additively, not as an automatic new major. Future opaque ACKs must name the actual PH calibration review.

Fix ANY epsilon>0, b=e^-epsilon∈(0,1), and full closed sensitivity body `D={x:|x|_1<=1}`. A private law satisfies `mu(E)<=b^-1 mu(E+h)` for EVERY Borel E and EVERY h∈D. Loss is squared Euclidean norm. The law may be represented by ANY genuine norm and ANY nonnegative Borel radial profile; no radial monotonicity is assumed.

Correctness inputs used below are ONLY ordinary convex norm/support/radial facts, planar polar integration/Tonelli/Fubini, Lebesgue differentiation, translation/weak convergence against C_c tests, Jensen/Markov/Prokhorov/Portmanteau and elementary moment algebra. The following explicit LAW642 exports are named when consumed: density/finite cap/positive-a.e./all-shift weak closedness/Laplace finite-cost competitor (its LF57–78), unique optimal law and the convex Minkowski core (its theorem/§8). Entire LAW642 SHA `957cab2bcf3eff1860ff9f4b5a1e5838708aceaf894a97fdc2c5244c3e7d8e53` is required for any whole application gate.

No K25 SAME-norm mean-loss theorem, scalar optimum, old homothetic counterexample, EXP-only theorem or new148LF theorem is a correctness premise. In particular I do NOT replace a mean-norm source theorem by a squared-norm one without proof. The exact remaining D-radial profile calibration is left explicit in §6.

Entire cp102/cp108 consuming guidance is ZERO; auxiliary214STOP. No epsilon is assigned to a D/R side. All arguments below quantify over arbitrary bodies/profiles/shifts and use no selected parameter or frozen control as a viability probe.

## 1. Definitions and the main shape theorem

Let K be a compact convex centrally symmetric norm body with0 in its interior, gauge g_K. Suppose a full-D-private finite-MSE law has density

`p(x)=phi(g_K(x-a))` a.e.,

for SOME a∈R² and SOME nonnegative Borel phi. Define

`L=max_(h∈D) g_K(h)>0`, `C=L K`, `psi(s)=phi(Ls)`.

Then D⊂C and the centred density is exactly psi(g_C(x)). No normalization of the actual probability law has yet changed.

**Theorem EFF/SHAPE.**

1. The SAME law is private for EVERY shift in the full CLOSED effective body C, not only D.
2. There is an explicit D-radial full-D-private law obtained by using the SAME rescaled profile psi on D and renormalizing its mass.
3. Its MSE is no larger, and equality holds **iff** a=0 and C=D. Thus a genuinely different effective norm shape or nonzero centre can never minimize the entire norm-radial private class.
4. Consequently the infimum over ALL norms/ALL Borel radial profiles/ALL centres equals the infimum over centred D-radial private laws. That reduced class attains its infimum (proved in §5). No profile/staircase ansatz is needed.

## 2. Necessity: full-D privacy forces scalar L-privacy at EVERY pair of positive Lebesgue radii

Translation by -a preserves privacy, so take a=0 for this section. LAW642's capped-density consequence makes phi essentially bounded as a function of positive radius: a scalar set of positive measure has a positive-area preimage under g_K by polar integration. Hence phi is locally integrable on (0,infinity), with a full-measure set P of finite Lebesgue points.

For EACH h∈D, density privacy holds for a.e.x. Fubini in (x,h), followed by y=x+h, gives

`p(x)<=b^-1 p(y)` for a.e. pair (x,y) with y-x∈int D.   (PAIR)

Choose an arbitrary maximizer h_0∈D with g_K(h_0)=L; it is nonzero. For ANY r,s∈P with |r-s|<L, put `x_0=(r/L)h_0` and `y_0=(s/L)h_0`. Their difference is in int D because its multiplier of h_0 has absolute value strictly below1 and0 is interior to D.

Suppose `phi(r)>b^-1 phi(s)`. A strictly positive value margin can be chosen. Lebesgue differentiation gives positive-measure radial sets in EVERY sufficiently small interval about r and s on which the respective values still violate that inequality. The norm-polar map `(u,theta)↦u R_K(theta)u(theta)` is continuous for positive u. Thus small open angular cones about h_0's direction and small radial intervals can be chosen so that EVERY resulting pair has difference in int D. Those violating radial sets times the cones have positive planar measures (polar Jacobians are strictly positive there). Their Cartesian product is therefore a positive-measure set violating PAIR, contradiction.

Consequently

`phi(r)<=b^-1 phi(s)` for EVERY r,s∈P with |r-s|<L.     (SCALAR)

Interchanging r,s gives the reverse inequality as well. This is a statement at ALL positive Lebesgue-point pairs, not an unjustified evaluation of density privacy on a null ray or a merely two-dimensional-a.e. scalar assertion. The ray locates OPEN cones; actual contradictions occur on positive-area products.

## 3. Sufficiency for the full CLOSED effective body

Let N=(0,infinity)\P. Polar integration shows `{x:g_K(x)∈N}` has planar measure0. For ANY fixed h with g_K(h)<L, a.e.x has both g_K(x),g_K(x+h) in P and positive. The triangle inequality gives

`|g_K(x+h)-g_K(x)|<=g_K(h)<L`.

SCALAR therefore gives p(x)<=b^-1p(x+h) a.e., with the reverse inequality from -h. Integrating proves actual law privacy for EVERY such h. No common null set for all h is required.

For a boundary h with g_K(h)=L, take h_t=(1-t)h for t∈(0,1). For any nonnegative continuous compactly supported test f, the law inequality for h_t passes as t↓0 by bounded dominated convergence of f(x-h_t). Radon measure order then gives the all-Borel inequality at h itself. This is an ALL-boundary proof, not an evaluation of a new residual at a selected boundary control.

Thus the SAME law is private on the full CLOSED C=L K. Conversely C-private implies D-private because D⊂C, so this effective-body implication is exact for the given radial representation.

Rescaling SCALAR gives: the positive Lebesgue points of psi satisfy `psi(u)<=b^-1psi(v)` whenever |u-v|<1. By the same sufficiency argument this profile defines a private law on ANY genuine norm body A once its radial mass is finite and normalized. In particular it can be transported to D.

## 4. The explicit same-profile diamond law and strict shape comparison

Write `I_1=∫_0^infinity s psi(s)ds`, `I_3=∫_0^infinity s^3 psi(s)ds`. They are finite and strictly positive because the original radial law is a nontrivial probability with finite second moment. For any norm body A, ordinary polar integration gives

`Z_A=∫psi(g_A(x))dx=2|A| I_1`,

`N_A=∫|x|_2² psi(g_A(x))dx=4 M_2(A) I_3`,

where `M_2(A)=∫_A |x|_2² dx` (indeed `∫R_A(theta)^4dtheta=4M_2(A)`). Hence the normalized cost is

`J_A=2 [M_2(A)/|A|] [I_3/I_1]`.                        (COST)

The original centred C-law is already normalized, so Z_C=1. Define the new probability density explicitly by

`p_D(x)=(|C|/|D|) psi(g_D(x))`.

Its mass is1 by the first formula; §3 proves FULL CLOSED D-privacy. This is an actual law, not a formal cost lower bound.

The diamond has |D|=2 and M_2(D)=2/3, hence mean squared radius1/3. For ANY x outside D, Cauchy–Schwarz gives `|x|_2²>=|x|_1²/2>1/2`. Since D⊂C,

`M_2(C)-(1/3)|C| = ∫_(C\D)(|x|_2²-1/3)dx >= (1/6)|C\D|`.

If C!=D, that area difference is positive: a point of C outside the closed convex D, together with a small interior ball of D, gives by convexity a positive-area portion of C outside D. Therefore `M_2(C)/|C|>1/3` for C!=D, with equality exactly when C=D.

COST now gives J_C>=J_D, strictly unless C=D. The original translated law has cost `|a|²+J_C`: its centred first moment vanishes by norm-radial symmetry and finite MSE. Thus

`J(original)-J(p_D)=|a|²+2[I_3/I_1][M_2(C)/|C|-1/3]`,

which is nonnegative and vanishes exactly when a=0 and C=D. This proves SHAPE for EVERY input norm/profile, with all normalizations and privacy quantifiers preserved.

## 5. Exact reduction and an independent attained-infimum proof

Let N_epsilon be the entire class of feasible finite-MSE laws radial in some norm about some centre, and let D_epsilon be its centred D-radial subclass. Inclusion gives inf_N J<=inf_D J. The explicit dominance in §4 gives the reverse inequality, so

`V_N(epsilon)=inf_(mu∈D_epsilon) J(mu)`.

All minimizers in the big class must already have a=0 and C=D in every supplied representation; no different shape attains the same value by a hidden profile compensation.

Here is an independent attainment proof requiring NO Blaschke selection. The feasible product Laplace density is D-radial with finite cost, so choose a bounded-cost minimizing sequence in D_epsilon. Markov/Prokhorov gives one weak probability limit. Full-D privacy is weakly closed and cost lower semicontinuous by LAW642; the limit has positive density a.e.

For the FIXED D, §2 of the148LF paper's polar product identity can be obtained directly without importing that paper: under `T_D(x)=(g_D(x),x/|x|)`, each joint law equals `rho_j⊗nu_D`, with `nu_D=R_D²dtheta/(2|D|)`. The map is continuous off0 and the limit has no atom there, so the joint laws converge to T_D of the limit. Radius marginals converge; weak convergence of products gives product limit `rho⊗nu_D`. Absolute continuity of the limit and the exact Lebesgue Jacobian `2|D|s ds nu_D` give a Borel radial density in D by Radon–Nikodym. Thus the limit is in D_epsilon and attains its infimum. This argument uses no convergence of arbitrary phi_j and no monotone-profile restriction.

Consequently the entire norm-radial infimum is attained. This proves the attainment export of the148LF candidate by a SEPARATE effective-body/shape route, not a repair or retroactive acceptance of its Blaschke/angular noncollapse proof.

## 6. Registered application and the exact unproved calibration step

At the ENTIRE LAW642 input, the unique original optimum belongs to D_epsilon iff its convex core is a homothetic diamond, by the explicit two-level argument (the SAME proof can be read in full in the separate148LF body). If that148LF rigidity input is consumed, all its original dependency and review requirements remain. Alternatively one can repeat it directly: radial thresholds make S and S+D both dilates of D, hence S itself a dilate.

Therefore the attained D-radial class value equals V in the actual full-facet case and is strictly larger in the genuine positive-arc case. No epsilon range, transition root, numerical lower gap or new viability instance is assigned. The original V itself is not improved or re-proved by this family comparison.

**FIRST remaining calibration step:** optimize the scalar ratio I_3/I_1 over ALL Borel profiles with the proved scalar step-one privacy condition. This paper does NOT assert that nonincreasing profiles or geometric one-core staircases suffice, and does NOT silently import K25's mean-norm optimum as a squared-norm result. An explicit monotone rearrangement/phase/annular argument or a correctly authenticated source theorem with the exact squared-loss hypotheses is required for a finite scalar formula. Nor is uniqueness of a D-radial class minimizer asserted here.

The first remaining acceptance step is a fresh ENTIRE proof/dependency/application gate over this complete successor and ALL operative LAW642 inputs; if its application is reviewed through the separate148LF rigidity theorem, include that ENTIRE theorem too. Earlier148LF gate scopes must not silently grow. The special necessity-on-open-cones/Lebesgue-points, closed-body sufficiency, SAME-profile normalization, strict shape dominance and fixed-D product-limit attainment all require direct reconstruction, not a title-only PASS.

All prior source ancestry, mechanism priority and worldwide novelty remain unresolved. This elementary/standard-style comparison is not claimed first in literature. It excludes no origin-box/Minkowski family that is not norm-radial and no nonadditive channel. Exact original registered full-D/all-Borel additive/MSE/allfiniteepsilon target remains unchanged.

All individually named own findings and the v94 recovered PH contact persist. cp102/cp108guidanceZERO; auxiliary214STOP. Exact all-variable source-fixed WRITTEN work only, no machine identity check/scientificinterpreter/Eval/calculator/program/CAS/enumeration/solver/replay/buildtest/CLI/nestedagent/GO/chosenparameter-state-control-boundary-limit-magnitude-decimalprobe/withdrawnguidance. No frozen/shared edits/Git/deletion/publication. Same18/OWN/HOLD/originalOct27cutoffdeadline/actual30minsubstantiveincludingblocked/noearlypark or round closeout.
