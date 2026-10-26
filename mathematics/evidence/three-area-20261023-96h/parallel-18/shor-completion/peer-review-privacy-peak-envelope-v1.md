# Written reconstruction: all-law full-tail peak envelope and strict finite-b relaxation gap

Observed before creation: **2026-10-23T16:06:24-0700 PDT**. Reviewer MathShor, primary slot math-5. Parent assignment: `peer-review-wave-eighteen-v8.json`; its full common contract and MathShor entry were read. Only this named output is written. No arithmetic program, CAS, root solver, enumeration, numerical integration, compilation/test, CLI model or nested agent was used.

## 1. Exact source, coverage, exposure and verdict

Complete285-line source read:

    information-science/evidence/three-area-20261023-96h/parallel-18/
      privacy-diamond-mse/proof-full-peak-envelope-relaxation-v1.md

Independently observed matching SHA256:

    0bf1f46015d1da201677f6fa0700dee45d7e8d66599e0edda7e2ccf7ad8b95a0

Also read fully: actual `selection-v2-finite-epsilon.md`, actual `residual-peak-envelope-duality-v1.md`, the actual parent finite-disk disposition, the complete376-line disk source and its notation qualification. The disk source was contextual comparison, not a premise of the new proof or a newly re-certified bump/Minkowski theorem. Observed context pins:

- selection-v2: `505e2e3a92f912b83db4f785c1999777a7bf7977ebf9cf95b64f02a797b8deb2`;
- exploratory residual: `5987c7eb468566b3d2740590091fdf35ea500c918c3a09971131d7faf5a818a6`;
- prior disk source: `44b68f86550f36cc560d31683f887b188a3310c63f175ebfb0abaf7fb868c7b4`;
- disk notation qualification: `e013b011ebaaaddb365e7458a019a8037423b55caa5f0fcf3739b0bb77e6a2e4`;
- actual disk parent disposition: `bd5b7f26d69fde2aad2b1e5b8066afcf4fb636470a6f2e065830a46fae440194`.

Exposure: before this assignment I knew shared parent descriptions of the privacy packets, but had not reviewed their proof bodies. This is an ordinary supplied-proof in-harness reconstruction with shared steering, not blind/cross-vendor/human/formal review.

**Verdict: 0 FATAL / 0 MAJOR / 0 substantive MINOR at the complete stated theorem.** The all-law envelope, derived finite-cost center, exact root/certificate, uniquely optimal relaxed density, fixed-shift positive-area failure and attained original optimum imply V_b>s_b for every0<b<1. This does NOT determine V_b, its gap magnitude or an original minimizer formula, and does not confer novelty. The relaxed primal is NEVER an admissible full-DP law.

## 2. Literal original class and full envelope

The current full target is the infimum of E||X||_2² over ALL Borel probability laws with

    mu(E)≤b^(-1)mu(E+h)

for every Borel E and every h in the FULL closed unit l1 diamond D, at every finite epsilon=-log b>0. It contains no density, symmetry, mean-zero, attained-peak or one-core ansatz. The answered historical homothetic-diamond assertion is not the active unresolved target. The source preserves that distinction.

For g_b(x)=b^ceil(||x||_1), g_b(0)=1, the closed-set expansion

    g_b=(1-b)Σ_(k≥0)b^k 1_(kD)

is pointwise correct: the first included k is ceil(||x||_1), including integer-radius boundaries, while at0 every k contributes. The k0 singleton has zero effect on the integrals. Tonelli is applicable because all summands are nonnegative.

The geometric ingredients are |kD|=2k² and its Euclidean quadratic moment(2/3)k⁴. The standard geometric-series moments give exactly

    Z_g=2b(1+b)/(1-b)²,
    N_g=2b(1+11b+11b²+b³)/(3(1-b)⁴).

Every tail is included; both quantities are finite and positive for the whole open b-interval. Evenness makes the vector first moment zero, and Cauchy–Schwarz from finite mass/second moment makes it absolutely integrable. The full F_b(s) expression, including its countable nonnegative shell sum and excess-disk identity, is therefore well-defined without any numerical truncation.

## 3. All-law density, countable Tonelli steps and a genuinely derived center

For a Borel Lebesgue-null set N, integrate the measure privacy inequality over h∈D. For each fixed x, the h-section1_N(x-h) is a translated null set. Tonelli gives

    2mu(N)≤b^(-1)∫_D mu(N+h)dh=0.

Thus mu has a nonnegative Borel density p, finite a.e., without having assumed one.

For each positive integer k and each FIXED t∈kD, k repetitions of the allowed shift t/k give measure domination by b^(-k) at shift t. The Radon–Nikodym implication is p(x+t)≥b^k p(x) for a.e.x; its exceptional set may depend on t. The author correctly does NOT intersect uncountably many such sets. The bad-pair set is jointly measurable in(x,t), and for each fixed t has a null x-section. Tonelli over R²×kD yields a full-measure H_k on which the inequality holds for almost every t∈kD. Intersecting only the COUNTABLY many H_k gives H.

For c∈H, translate each k's exceptional t-set into y-space and remove their countable union. Choosing the least positive integer k containing y-c gives

    p(y)≥p(c)g_b(y-c) a.e.y.

The isolated y=c point is irrelevant. Integrating bounds p(c)≤1/Z_g on a full-measure set, so the essential supremum M is positive and finite. Near-essential-peak sets have positive measure. One can therefore choose c_n in H and the a.e.cap set p≤M with a_n=p(c_n)→M; no attained peak is smuggled in.

The actual finite-cost inequality is

    J(p)≥a_n[N_g+Z_g||c_n||²],

because translating the even full envelope eliminates the linear cross term. Eventually a_n≥M/2, so the centers are bounded. A convergent subsequence c_n→c is thus DERIVED, not assumed. On one common full-measure y-set, every selected envelope inequality holds. Away from the countable integer-l1 spheres around c, g_b(y-c_n) is eventually equal to g_b(y-c). Those boundaries are planar null sets. Passing to the limit gives the full floor M g_b(y-c)≤p(y), together with p≤M.

This proves the envelope for every finite-cost original law, without imposing c=0 or claiming p(c)=M or a privacy inequality valid pointwise simultaneously for every shift.

## 4. Unique root, strict centering and the all-law certificate

F_b(s)=∫(||x||²-s)_+g_b is finite and continuous by domination with ||x||²g_b. It is strictly decreasing: for s1<s2, outside the sqrt(s2) disk the integrand decreases by s2-s1 and g_b has positive mass there. It starts at N_g>0 and tends to0 by dominated convergence. The function pi s²/2 starts at0 and increases strictly to infinity, so there is exactly one root s_b>0.

For any s≥0, f_s(u)=(||u||²-s)_+ is convex and even. Its convolution penalty

    Fcal(c)=∫f_s(u+c)g_b(u)du

is therefore convex and even. This proves Fcal(c)≥Fcal(0). Strictness for c≠0 is also genuinely proved: the midpoint gap f_s(u+c)+f_s(u-c)-2f_s(u) is nonnegative everywhere and exactly2||c||² whenever||u||>sqrt(s)+||c||. That region has positive g_b-mass. Evenness equates the two translated integrals, so Fcal(c)>Fcal(0). No original-law symmetry is required.

For any relaxed p with cap M and floor centered at c, multiply the inside-disk cap by the NEGATIVE excess and the outside-disk floor by the POSITIVE excess. The inequality direction is exactly

    J(p)-s≥-M∫_(B_sqrt(s))(s-||x||²)dx+M Fcal(c)
            =M[-pi s²/2+Fcal(c)].

At the root this is nonnegative, giving J≥s_b for the relaxation and all original finite-cost laws. Infinite-cost laws satisfy it trivially. The argument uses the cap/floor information derived for the full original class, not a restriction of that class to translated radial or one-core laws.

## 5. Exact relaxed optimum and complete equality conditions

The proposed relaxed density equals M_b inside the Euclidean disk of squared radius s_b and M_b g_b outside. Its normalizer

    M_b^(-1)=pi s_b+∫_(outside disk)g_b

is positive and finite. Since0<g_b≤1 it has the required floor and cap, unit mass and finite second moment. Subtracting s_b gives exactly M_b[-pi s_b²/2+F_b(s_b)]=0. Hence the relaxed optimum really is s_b.

If equality holds for any relaxed density, the split inequality and strict centering force c=0. Its two slack integrals are nonnegative. Inside the disk the weight s_b-||x||² is strictly positive a.e.; outside the excess is strictly positive a.e. Thus equality forces p=M inside and p=M g_b outside, up to the circular null boundary. Unit mass fixes M=M_b. This proves uniqueness a.e. of the relaxed optimizer, not just uniqueness within a guessed radial family.

No original feasible optimizer is identified by this equality statement. In particular the point-envelope relaxed density is NOT the disk-core Minkowski-shell mechanism: the latter pays for B_R+kD, while the former only uses g_b centered at one point outside its plateau.

## 6. Fixed-shift infeasibility is on a positive-area region for EVERY b

Let R=sqrt(s_b)>0, delta=min(R/2,1/2), x0=(R-delta,0), and use the SAME permitted shift h=(1,0) for all b.

- If R≤1, delta=R/2, so x0=R/2>0 and x0+h has radius1+R/2>R.
- If R≥1, delta=1/2, so x0=R-1/2>0 and x0+h has radius R+1/2>R.

In both cases x0 is strictly inside B_R and ||x0+h||_1=R-delta+1>1. These are strict open conditions, so they persist on a nonempty open neighborhood U. For almost every x∈U,

    p_rel(x)=M_b,
    p_rel(x+h)=M_b g_b(x+h)≤b²M_b<bM_b.

The exceptional density sets and their fixed translates are null; U has positive area. Thus the necessary a.e.density inequality for this fixed shift fails and cannot be repaired by choosing different boundary values. This proves full-DP infeasibility for every0<b<1, without a root estimate, small-b limit or sampled shell corner.

The omitted plateau coupling is exactly visible: a maximum plateau of positive area requires a b-height floor on the WHOLE B_R+D, not only on the point-centered envelope.

## 7. Original attainment and strict V_b>s_b

The product Laplace density epsilon² exp(-epsilon||x||_1)/4 is a normalized feasible law for the entire diamond by the l1 triangle inequality. Its squared-Euclidean cost is4/epsilon². Thus V_b is finite, and a minimizing sequence can have uniformly bounded second moments. Markov's inequality makes it tight.

The explicit classical imports are Prokhorov weak sequential compactness on Euclidean probability laws and the positivity/regularity characterization of finite Radon measures. Their hypotheses are met; this review does not claim these standard theorems as new results or kernel-verified imports.

For a weakly converging subsequence and any ARBITRARY FIXED h∈D, phi∈C_c^+,

    ∫phi dmu_n≤b^(-1)∫phi(.-h)dmu_n

passes to the limit because both tests are bounded continuous. The same weak convergence works for every bounded continuous function; choosing h and phi arbitrarily uses no uncountable intersection of null sets or h-dependent subsequence. Positivity against all nonnegative C_c tests makes b^(-1)mu_*(.+h)-mu_* a positive Radon measure, hence gives the original all-Borel domination for every h. The probability limit is feasible.

For each L, min(||x||²,L) is bounded continuous. Its limiting integral is≤liminf J(mu_n)=V_b. Increasing L yields J(mu_*)≤V_b; feasibility yields the reverse. Thus the original infimum is attained with finite cost.

If V_b=s_b, that actual original minimizer would belong to the envelope relaxation, and its equality characterization would force p_rel a.e. Section6 forbids that. Therefore V_b>s_b for EVERY finite b. This proves strictness but NO explicit gap magnitude, exact V_b or formula for its genuine minimizer.

## 8. Prior disk disposition, imports and nontransfer

The parent disk record supports a different statement: every positive-radius disk-CORE Minkowski-shell law is feasible but strictly improvable by an explicit noncircular core, at each finite b,r. It neither gives the exact finite V nor handles a zero-radius limit or an unattained infimum over disk radii. Its original u1/nu1 mismatch is repaired by the pinned notation addendum. Nothing in this review transfers its verdict to the new peak-envelope source; the latter was reconstructed directly above.

Conversely the new peak relaxed primal is INFEASIBLE, not merely suboptimal. Conflating those two densities would erase the main logical boundary. The contextual prior disk proof was read in full but its complete perturbation constants are not being newly audited or promoted by this review.

The current selection retains classical mechanism ancestry and a bounded source screen. The cited CND comparison has extra conditions and is not a premise of the compactness proof. No prior source/novelty verdict, exact finite-V formula or mechanism-class completeness follows from this review.

## Return and limitations

- **FATAL / MAJOR / substantive MINOR:** none found at the full stated all-law/relaxation/strict-gap scope.
- **Reconstructed:** every countable Tonelli step, the derived peak center, full-tail moments, unique root, strict centering, split/equality argument, positive-area failure at a fixed shift, and original-law weak attainment/strict separation.
- **Not established:** exact V, a quantitative positive gap, an original minimizer density, a matching feasible relaxation primal, a universal convex-core reduction, priority, human or formal/kernel verification.
- **Execution:** none; all identities and inequalities were written reconstructions, not root calculations or finite samples.

The assigned bounded review is complete. I return to the mixed-length Shor RAW-SELECTOR primary; no privacy verdict transfers to it.
