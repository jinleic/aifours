# f3 — Scientific review of exact-privacy smoothing and stability obstruction

Reviewer **MathSun8-2**. **WRITTEN same-harness review with one independent bounded exact rational convolution calculation; not formal/kernel/human/configured-family/novelty acceptance.** Actual native observation before this review write: **Wed Oct 28 17:08:31 PDT 2026**. Completed-file pin clock is separately returned.

## 1. Exact verdict and imported boundary

**NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE; 0 NEW mathematical FATAL / 0 NEW mathematical MAJOR / 0 NEW mathematical MINOR.** Conditional on the exact prior LAW642 theorem below, the full finite-positive-epsilon smoothing candidate's assertions A–C are reconstructed: full closed-diamond ALL-event privacy at the SAME epsilon, an actual event and boundary shift attaining epsilon for every t>0, exact cost increment, smooth/continuous-class infimum and nonattainment, an all-t TV upper bound, a small-t TV lower bound, the construction's W2 bound, and failure of all local universal TV exponents >1/2. The paper's explicit bounds and quantifiers are preserved; this is not a general TV upper-stability theorem or a new original optimum proof.

**LAW642 is an explicit prior theorem/import, not independently re-proved here.** I read the actual theorem source, not only its summary: `privacy-all-law-optimum-self-contained-v1.md`, SHA256 `957cab2bcf3eff1860ff9f4b5a1e5838708aceaf894a97fdc2c5244c3e7d8e53`, lines19–55, plus its convex-core conclusion lines477–501. Its parent disposition `privacy-all-law-self-contained-parent-v1.md`, SHA256 `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`, was read completely through its limits. The source asserts, for every finite epsilon>0 and ALL Borel laws with full CLOSED D event shifts, a unique optimal LAW, finite V and an a.e. density `Z^-1 b^n` with the exact S below. Its shape/equality are genuine named inputs; those 642 source lines and their parent audits were NOT completely re-reviewed here. **NR-LAW642-PROOF/FULL-PRIOR-AUDITS:** no new full-source or formal proof verification is claimed. The cited import's equality is equality of laws, not equality of every pointwise density version.

**NR-PRIORITY / NR-ALL-LAW-STABILITY:** no literature-firstness, global openness, optimal upper TV modulus for arbitrary near-optimizers, stronger verification, broad nonadditive-channel/book claim, or source-exhaustive comparison follows. The exact polygon experiment below evaluates a SYNTHETIC staircase, not the registered optimizer or LAW642. Earlier historical quarantines are not used as premises or retrospectively validated.

## 2. Actual inputs, clocks, familiarity and scope

The frozen assignment was read first. The COMPLETE217LF candidate `frontier-20261028-smooth-exact-privacy-stability-v1.md` SHA256 `40651c034f1800091c1daeb17ea9490fcf9e745fe4c74494381869b5e3626eec`,15624B, was read raw windows1–60,61–120,121–180,181–217 through ending; its live hash matched at **Wed Oct 28 17:07:03 PDT 2026**. LAW642 source/disposition hashes matched at17:07:54. I had previous general privacy/quantum/preview written-review exposure; this was not a blind or cognition-reset review. No author was contacted. The prior source's full proof is a conditional import, not a shortcut silently counted as reconstructed.

A named fact needed by the candidate is now stated explicitly: for a finite-perimeter set K in R2 and y in R2,

    ∫ |1_K(x−y)−1_K(x)| dx <= |y|_2 P(K).

For compact planar convex bodies A,B, their Euclidean perimeters satisfy `P(A+B)=P(A)+P(B)`; for the unit l1 diamond D, `P(D)=4 sqrt(2)`. These are the candidate's explicitly NAMED standard BV-translation and planar convex-perimeter imports, not claims from the rational experiment. Other standard inputs are Tonelli/Fubini, dominated convergence, compact-smooth-kernel convolution/translation of L1 derivatives, elementary Euclidean moment/coupling facts and the elementary flat bump. If either geometric fact is not admitted, the particular displayed upper-TV constant is NOT reconstructed independently by this review; the privacy/cost/lower-bound conclusions do not use these two imports.

## 3. Imported optimizer shape and elementary core properties

Fix ANY finite epsilon>0 and set b=exp(−epsilon), so 0<b<1. The original feasible family F consists of Borel probability laws with

    mu(A)<=b^(-1)mu(A+h)  for EVERY Borel A and EVERY h in D,
    D={h: |h1|+|h2|<=1}.

J is the actual squared Euclidean second moment. The exact LAW642 statement gives a UNIQUE optimal probability law mu_* of finite cost V, with a density version

    p_*(x)=Z^(-1)b^n(x),
    n(x)=min{k>=0 integer: x in S+kD},
    S={x: |x|_1<=2t_*, |x|_2^2+2m|x|_infinity+T2<=lambda_*},
    m=b/(1−b), T2=m+2m^2, t_*>0, lambda_*=V>T2.

Both displayed inequalities define closed convex sets, so their intersection S is convex and closed; its l1 bound makes it compact. Since t_*>0 and lambda_*>T2, continuity of the two defining functions gives a neighbourhood of0 in S: S has nonempty interior and contains0. No numerical parameter value or assumed diamond core is needed. Each S+kD is a compact convex body, is nested, and the sets exhaust R2 because0∈S. Consequently n is a finite Borel integer function, `0<p_*<=1/Z` for the chosen canonical version at EVERY point, and the imported law is represented by that version. The proof below never assumes its arbitrary other density representatives agree at boundaries.

## 4. Convolution, ALL-event privacy, regularity and exact moment — candidate LF22–73

Let phi be ANY nonnegative probability density supported in [-1,1]^2 with phi(u)=phi(−u), finite positive `kappa=E|U|_2^2`, and positive `alpha=P(U1+U2>1)`. Let X have the imported law, take U independently, and define Y=X+tU for ANY t>0. Symmetry and bounded support give EU=0; no symmetry or centering of X is required. The density of Y is the actual convolution `q_t(x)=∫p_*(x−tu)phi(u)du`, by Tonelli. Since the canonical p_* is positive everywhere and phi has total mass1, q_t(x)>0 for EVERY x, not merely almost everywhere.

For ANY fixed Borel event A and ANY fixed h in the FULL CLOSED diamond, independence and Tonelli give

    mu_t(A)=∫mu_*(A−tu)phi(u)du
            <= b^(-1) ∫mu_*(A+h−tu)phi(u)du
            = b^(-1)mu_t(A+h).

The imported event inequality applies to each translated event for the SAME h; no common uncountable exceptional set of density versions is needed. The reasoning works for every A,h, including boundary shifts, and all t, including large t. Thus the SAME epsilon upper privacy guarantee is preserved, not a weakened epsilon or an RMS surrogate.

The candidate's product flat bump is normalized, nonnegative, symmetric and supported in [-1,1]^2; it is positive on the open square, so alpha>0 and kappa>0. Its elementary flatness at ±1 gives a C-infinity compactly supported kernel. For its scaled kernel, every derivative lies in L1. Convolution of bounded p_* with each translated L1 derivative yields a continuous derivative because L1 translations are continuous; iterating proves q_t∈C-infinity for each t>0. If phi is merely an arbitrary probability density satisfying the four listed properties, smoothness is NOT asserted. For the triangular product kernel its first weak derivatives are L1, giving C1 after convolution; it is not asserted C-infinity.

Since E|X|²=V<infinity, E|X|<infinity. Independence, bounded U and EU=0 justify the cross-moment and give, for every t>0,

    J(mu_t)=E|X+tU|²=V+2t EX·EU+t²E|U|²=V+kappa t².

The explicit coupling (X,X+tU) has quadratic transport cost kappa t², hence `W2(mu_t,mu_*)<=sqrt(kappa)t`. Both laws have finite second moments. The cost is squared EUCLIDEAN, not a first-l1 or squared-l1 claim. No statement that mu_t is centered or that EX=0 is needed.

## 5. Actual event attaining exact epsilon for every t — candidate LF74–99

Choose B strictly larger than both coordinate suprema of compact S. Put `c=max_{s∈S}(s1+s2)`, attained by compactness. If both coordinates of y exceed B, then for EVERY s∈S, `|y1−s1|+|y2−s2|=y1+y2−(s1+s2)`, and the maximizer gives

    dist_1(y,S)=y1+y2−c,   n(y)=ceil(y1+y2−c).

The distance is positive in this quadrant. The minimal nonnegative integer in the CLOSED sets S+kD is precisely that ceiling; integer boundaries are handled correctly, not by an open-shell approximation.

Choose h=(1,0)∈D. For ANY t>0 and every x with x1,x2>B+t, the kernel support ensures x−tu and x+h−tu both lie in that quadrant for every u in its support. Ceiling commutes with adding1, so

    p_*(x+h−tu)=b p_*(x−tu)  for all such x,u,
    q_t(x+h)=b q_t(x).

Take any nonempty bounded open rectangle E wholly in that quadrant. It is Borel, has positive Lebesgue measure, and q_t is strictly positive everywhere, so mu_t(E)>0. Integrating the displayed equality gives `mu_t(E+h)=b mu_t(E)`. Together with Section4's ALL-event upper guarantee, this is an ACTUAL positive-mass event and allowed shift attaining ratio b^(-1); every smaller epsilon would fail that same inequality. For each large or small t the rectangle may be chosen farther out; the proof does not claim a common fixed rectangle for all t. This works also for the triangular kernel.

## 6. Smooth and continuous nonattainment — candidate LF100–116

For the actual smooth bump, every mu_t has a strictly positive C-infinity density and exact epsilon, and its cost is V+kappa t². Letting t↓0 gives infimum <=V, while the original feasible-family definition gives infimum >=V. The same pair of inequalities applies to the larger continuous-density privacy-at-most-epsilon class, which includes these smooth laws. No positive smooth/continuous infimum gap remains under LAW642.

For nonattainment, choose an integer k so large that c+k>2B+8. There is a nonempty open diagonal segment of the line x1+x2=c+k in the far quadrant with open sets accumulating from each side. In a sufficiently narrow neighbourhood, the canonical density is the constant `Z^-1 b^k` just below and `Z^-1 b^(k+1)` just above. The constants differ because0<b<1. If a continuous function were another density of the SAME law, it would equal each constant almost everywhere on the corresponding open region, and hence everywhere on that region by continuity. The two limits at a common boundary point disagree. Thus no continuous representative of mu_* exists even though density versions may differ on null sets.

The imported uniqueness is uniqueness of the optimal LAW. Therefore any feasible continuous-density law attaining V would equal mu_* as a law, impossible by the preceding a.e.-version argument. In particular the smooth exact-epsilon class does not attain V. This independently pays the nonattainment edge used from the candidate's old S20 note, without accepting S20 as an extra theorem. The choice of k is existential, not a numerical value for the actual optimum.

## 7. All-t TV upper bound — candidate LF117–137

For K_k=S+kD, nestedness and the canonical n imply the POINTWISE level identity, including level boundaries,

    p_*=(1−b)/Z Σ_{k>=0} b^k 1_{K_k}.

Indeed at a point of first membership n, the tail geometric series begins at n. Each K_k is a compact convex body and has finite perimeter. By the explicitly stated BV-translation import, triangle inequality/Tonelli and the perimeter import,

    ∫|p_*(x−y)−p_*(x)|dx
      <= (1−b)|y|_2/Z Σ b^k [P(S)+4 sqrt(2)k]
      = |y|_2/Z [P(S)+4 sqrt(2)b/(1−b)].

Averaging y=tU, using `E|U|<=sqrt(kappa)`, and the density convention `TV(mu,nu)=1/2 ∫|p−q|`, gives the candidate's exact all-t upper bound

    TV(mu_t,mu_*) <= t sqrt(kappa)/(2Z) [P(S)+4 sqrt(2)b/(1−b)].

The bound may exceed1 for large t; that does not invalidate it. Its constant is finite for each fixed epsilon and fixed phi. It is a bound for THIS constructed family only, not a universal neighbourhood statement for arbitrary feasible near-optimizers.

## 8. Small-t TV lower bound and exponent limitation — candidate LF138–160

Use the k chosen in Section6 and 0<t<1/4. In coordinates `(x1,u)` with `u=x1+x2−c−k`, take

    |x1−(c+k)/2|<1/2,     0<u<t.

The k margin puts both x coordinates, and all x−tU coordinates, in the same far quadrant. Since U is supported in [-1,1]^2, `−2t < u−t(U1+U2) < 3t`; the t bound puts this displacement strictly between−1 and1. Apart from a kernel-null boundary, the only possible shell indices are k and k+1. The unshifted p_*(x) is `Z^-1 b^(k+1)`. Thus direct integration gives

    q_t(x)−p_*(x)
      = Z^-1 b^k(1−b) P(U1+U2>u/t)
      >= Z^-1 b^k(1−b) alpha >0.

Because phi is a two-dimensional density, each affine line has probability0, so the shell-boundary exception is harmless. Since 0<u/t<1, the event `U1+U2>1` is contained in the event in the displayed bound. The coordinate Jacobian has absolute value1, the x1 interval has length1 and the u interval has length t. Therefore the strip has area t and the standard `TV=1/2 L1` yields

    TV(mu_t,mu_*) >= [b^k(1−b)alpha/(2Z)] t.

This is a POSITIVE constant for fixed epsilon/phi, even if tiny. The all-t upper bound and this small-t lower bound yield `TV=Theta(t)=Theta(sqrt(J(mu_t)−V))` along this family, since kappa>0. The upper bound's constants may depend on epsilon/phi; none is asserted uniform in epsilon.

For any a>1/2 and any proposed finite C on a positive cost-gap neighbourhood, the ratio of the lower bound to `C(kappa t²)^a` tends to infinity as t↓0. Hence that bound fails on sufficiently small members of THIS smooth, strictly positive, exact-epsilon class. This does not imply a TV exponent1/2 upper bound for all feasible near-optimal laws, nor a global W2 stability theorem.

## 9. Independent bounded exact rational check — candidate LF161–210

I wrote the NEW standard-library checker `frontier-20261028-privacy-convolution-independent-check.py`, SHA256 `27e47fd1ec4ad707a35d90004b1b5e71cf2a9aef7336fdb848fd30648f7f37cc`. It does not import or call the author's code. It clips rational polygons in the four triangular-kernel quadrants and directly integrates `(1−|u|)(1−|v|)` and the two actual staircase shell regions by exact triangular polynomial moments. It uses `fractions.Fraction` and integers only; the tested source is complete before execution.

Actual command, run with a20-second deadline:

```text
/opt/homebrew/bin/python3 mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/frontier-20261028-privacy-convolution-independent-check.py
kernel_mass: 1
polygon_tail_mass_sum_gt_one: 1/24
independent_polygon_q: 25/18432
independent_polygon_q_shift: 25/36864
exact_shift_ratio: 1/2
PASS: direct rational polygon integrals and shifted density agree
Wed Oct 28 17:08:14 PDT 2026
```

The two density values are independently INTEGRATED on the synthetic S=D, b=1/2 staircase at the candidate's t=1/4 location and shifted location; they are not obtained by inserting the author's stated rise formula. Their ratio is exactly b. This check supports the normalization/alpha/synthetic calculation at those explicit inputs only; it does NOT verify the registered optimum, all-event privacy or the full smoothing theorem. It is not an independently validated finite witness for an open problem.

The remaining triangular cost constant is separately elementary: `∫_{-1}^1 s²(1−|s|)ds=2(1/3−1/4)=1/6`, so the two-dimensional kappa is1/3. Together with the independently integrated alpha=1/24, the displayed cost gap `t²/3` and lower-TV coefficient `b^k(1−b)/(48Z)` follow directly from Sections4 and8. The triangular density is C1 after convolution, not claimed C-infinity.

## 10. Claim disposition and remaining limits

- Candidate LF7–20: exact target, named unique-law/shape import and source ceiling match the actual theorem statement, subject to **NR-LAW642-PROOF/FULL-PRIOR-AUDITS**. Convexity/compactness/interior follow from the source's explicit S, not an unverified arbitrary-core assumption.
- LF22–60: all listed kernel hypotheses, smooth-bump existence, actual-event epsilon, exact cost, nonattainment, two-sided family-TV/W2 and exponent scope are consistent, at the stated epsilon/t quantifiers.
- LF61–116: full-event convolution, bounded-kernel smoothness, all-t quadratic moment/coupling and actual far-quadrant event, plus a.e.-version discontinuity/unique-LAW use, are paid above.
- LF117–160: exact nested-level representation, geometric/BV imports, all-t upper and small-t lower constants/Jacobian and exponent contradiction are paid above. No missing shell or endpoint is silently counted; the lower strip states t<1/4.
- LF161–210: triangle constants and synthetic rational check are consistent with the independent direct-polygon check. Neither the author's calculation nor mine proves the general theorem or LAW642.
- LF211–217: source, prior-result, stronger-verification and novelty limits are correctly retained.

**New findings FATAL0 / MAJOR0 / MINOR0 at the stated conditional scope.** Complete original optimum/uniqueness proof and named general geometric facts remain explicit imports, not retrospectively checked by the finite arithmetic. The unique-optimizer assumption is indispensable to the nonattainment conclusion; the smooth upper/lower estimates are for the constructed staircase law, not arbitrary near-optimizers. Review is scientific written support only; Main must review the complete candidate, this return and relevant source/import scope before adoption.
