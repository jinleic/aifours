# Independent same-harness review: f158 consolidated original-target privacy claims

## Verdict and assurance boundary

**Claim A: conditionally WRITTEN_SUPPORTED; FATAL 0 / MAJOR 0 / MINOR 0.** From the displayed formulas, I independently obtain the screened root bracket, the stated value bracket and the normalizer bracket in exact rational arithmetic. I also derive the normalizer and the identity `H_R = N − lambda Z` directly from the displayed rounded law, where `N` is its unnormalized squared-Euclidean moment. Identification of a screened root with the unique **all-law** optimizer remains entirely conditional on LAW642's stated screen-sufficiency theorem.

**Claim B: conditionally WRITTEN_SUPPORTED; FATAL 0 / MAJOR 0 / MINOR 1.** The all-positive-epsilon argument, including full-diamond privacy, strict first-cost decrease, scalar root ordering, mean-optimal existence, restricted second-cost attainment and the strict infimum gap, reconstructs. There is one local incorrect justification at candidate LF151: positivity of `J'(0)` is not the reason to exclude the equal endpoint laws. The needed fact is `J'(1)>0`, which follows immediately from the displayed and independently verified endpoint value at LF164. This changes neither theorem nor dependencies; the correct argument is supplied below.

These verdicts assume LAW642 with exactly the scope stated in the candidate dependency table. They do not establish LAW642, verify its source transcription, or make an unconditional all-law optimum claim. This is independent work within the same harness, not human, independent-model-family, formal/kernel, source-equivalence, novelty or publication acceptance. No external model, paid API, author contact, Git operation, unrelated build/test/formatter, infrastructure change or source edit was used.

## Frozen inputs and complete-read coverage

Manifest: `manifest-v1.json`, SHA-256 `f399dff9e7a72376e64e6fd3f18e0d4bb354471dae5e045256859a6a53cd1a03`, 3,050 bytes. It was read first. Both declared mathematical inputs were verified before interpretation and read completely in the prescribed order:

1. `RUN/dispositions/info-1-ln64-nonradial-staircase-gap-parent-v1.md`: SHA-256 `d67b0ac9cbde8c6d1f81f0f407106070ea3cee640984b4d166929b12d6dd6516`, 6,805 bytes, 59 LF, trailing LF; all LF1–59 read. This is supporting context only. None of its linked correction, candidate, controls or reviews was opened or used as a premise.
2. `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-original-target-consolidated-review-v1.md`: SHA-256 `37d1a560990b44e23da0a7f3c94399b8d88737b9f8276f9f667aa8a80352fa34`, 14,512 bytes, 186 LF, trailing LF; all LF1–186 read in order.

Here `RUN=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h`. The exact control reverified all input hashes/bytes/LF before computation and after its checks. I did not open the LAW642 parent/source documents, historical held mathematical payloads, or any other author candidate. Policy skills and advisory memory guidance were read; they are not mathematical premises.

## Independently authored controls actually executed

All files below are in this review directory. Neither script imports or executes author code.

- `reviewer-controls-v1.py`, SHA-256 `235fa4fd0645b138b5e1546bf29e3478d4a539bf36321863f417884c76f1d37c`.
- `reviewer-controls-v1-receipt.json`, SHA-256 `e3e816a5826f83b4b8918bf7460a0c14cda22407b874006b19d3c4eabe142455`.
- Actual run: `python3 reviewer-controls-v1.py`, Python 3.14.3; native clock before controls `2026-10-28T22:13:45-0700 PDT`, native clock before receipt write `2026-10-28T22:13:46-0700 PDT`; **341 checks, 0 failures, PASS**.
- `reviewer-geometry-identity-v1.py`, SHA-256 `0a6f9245b64ba7ce7fb6e8da53bb1f2f795bf22e78e6ca8966464a27db0c5dd2`, and `reviewer-geometry-identity-v1-receipt.json`.
- Actual run: `python3 reviewer-geometry-identity-v1.py`; both native clock observations `2026-10-28T22:15:34-0700 PDT`; **6 universal coefficient checks, 0 failures, PASS**.

Arithmetic uses only `Fraction` and integer `isqrt`, with no floating-point enclosure, optimizer, CAS or interval-library oracle. Square-root enclosures use `q0=isqrt(floor(q*10^120))`, giving `q0/10^60 <= sqrt(q) < (q0+1)/10^60`, and the squared inequalities are checked exactly. Sparse polynomial coefficient comparisons are exact rational algebra, not a formal-kernel proof.

The first control reconstructs geometric moments through Stirling/falling-factorial moments, computes the displayed primitive independently of its code block, compares it against direct Green boundary integrals, checks the root/value/normalizer intervals and screens, and uses both alternating Taylor and an independent positive Euler series for atan. It also checks the full formal Q/P/R identities, six rational positive-m parameter instances for root ordering and strict L comparison, diamond monomial integrals, square-core Minkowski radii and strict bathtub comparisons, exact geometric-tail enclosures, and shell-mixture identities including closed boundaries. There are **3,060** exact sample shift checks for constructed square-core radial laws; these are controls only, not the proof for every shift.

**Intended-reason negative endpoint control:** replace only the right endpoint by

`d_mut = 17899568185394517/10^17 + 1/10^30`.

The mutated interval remains correctly ordered, but the exact lower bound for `H_R(d_mut)` is strictly positive. It therefore fails the required negative right-endpoint sign, not an unrelated ordering test. The receipt retains the rational witness. Further negative controls detect a wrong sign for the rounded arc center, a flipped atan coefficient, a fabricated radial spacing of 9/10 permitting a two-level index jump under `(1,0)`, and the zero rather than strict bathtub difference when the core already is a centered diamond.

The universal second control verifies that the independently derived Green area and moment expressions equal the displayed normalizer and primitive as formal polynomials in `m,t,d,k`. This is not merely two-endpoint agreement; it needs the displayed lambda definition but not the cubic defining t(d).

## Claim A reconstruction

### A1. Trigonometric enclosure and sign direction

Set `v=m(1+m)`, `c=t−d`, `A=lambda−v`, `y=t+d+m`. Direct substitution into (4) gives

`A−c^2=y^2`.

On the tested interval `c>0`, `y>0` and `z=c/y` lies in `(0,1)`. Thus `asin(c/sqrt(A))=atan(z)` on the principal branches. Substitution of (5) yields `H_R=Hrat−2A^2 atan(z)` with the stated negative coefficient.

For `0<z<1`, the alternating terms `z^(2j+1)/(2j+1)` strictly decrease to zero. The sum through `j=11` ends with a negative term and is a lower bound; adding `z^25/25` gives an upper bound. The exact rational Taylor width is below `10^−35` at both endpoints, and so is the induced H interval width. Since the coefficient is negative, the **upper** atan bound supplies the **lower** H bound. This reversal was explicitly checked.

Independent cross-check: write `u=z^2/(1+z^2)` and

`atan(z) = z/(1+z^2) * integral_0^1 [1−u(1−s^2)]^−1 ds`.

Expansion into nonnegative powers gives coefficients with consecutive ratio `(2j+2)/(2j+3)`. Consequently the next term divided by `1−u` bounds the remaining tail. Twenty Euler terms give a strict enclosure inside both the 12- and 16-term alternating enclosures at each endpoint. This is not an assumption that one implementation of atan is correct.

The recorded rational witnesses in particular give the coarse exact margins

`11/10^18 < H_R(d_left) < 12/10^18`,

`−15/10^18 < H_R(d_right) < −14/10^18`.

Continuity and IVT therefore put a root strictly inside

`17899568185394517/10^17 < d_* < 17899568185394518/10^17`.

### A2. Screens and value bracket

`t'(d)=(2d+m)^2/v>0`, and `lambda'(d)=(4t+2m)t'(d)+4d+2m>0` throughout this interval. The exact endpoint inequalities verify `0<d<1/2`, `t>d`, `2t<1`, and

`T2 < lambda(left) < lambda(right) < 4m^2+4m+1/3`,

as well as `lambda(right)<100/441`. Four exponential-series terms, including the constant term, give

`1+7/10+(7/10)^2/2+(7/10)^3/6 = 12013/6000 > 2`.

Thus `ln 2<7/10`, `epsilon=6 ln 2<21/5`, and `lambda<100/441<4/epsilon^2`. No decimal logarithm is an enclosure premise.

The endpoint lambda values are enclosed, for example, by the exact terminating decimals

`0.1630066277350703144 < lambda(left) < 0.1630066277350703145`,

`0.1630066277350703899 < lambda(right) < 0.1630066277350703900`.

Monotonicity therefore establishes the candidate's wider strict value interval once the LAW642 screen identifies the root's law as the optimum:

`1630066277350703/10^16 < V_J(ln 64) < 1630066277350704/10^16`.

The independent geometry below verifies `J=lambda` at a zero; this last equality is not inferred merely from the word “screen.”

### A3. Actual law, normalization and moment identity

In the octant `0<=x2<=x1`, the rounded constraint in (7) is the circle inequality `(x1+m)^2+x2^2<=A`, intersected with `x1+x2<=2t`. The boundary switches at `(t+d,c)`, since its shifted circle coordinates are `(y,c)` and `y^2+c^2=A`. The circle's angle there is `theta=atan(c/y)`. The diagonal endpoint `(t,t)` is strictly inside that circle because the difference is `2d(d+m)>0`. The origin is interior since `lambda>T2`. This is a compact convex positive-area core with a genuine nonzero arc.

For `S+kD`, the corresponding octant boundary is the arc centered at `(k−m,0)`, followed by the straight edge from `(t+d+k,c)` to `(t+k/2,t+k/2)`. This follows by adding support points of the diamond: an arc normal in this octant adds `(k,0)`, and the diagonal normal adds the diamond edge.

Put `e=k−m`, `a=t+d+k`, `s=t+k/2`, `K=(a−c)s`. Direct Green integrals over the eight octants give

`|S+kD| = 4[A theta + e c + K]`,

`integral_(S+kD) |x|_2^2 = 2{A(2e^2+A)theta + e(e^2+3A)c + e^2 c y + K[a^2+c^2+(a+c)s+2s^2]/3}`.

The radial boundary pieces contribute zero to these Green integrals. With `Pr(N=k)=(1−b)b^k`, layer summation gives `Z=E|S+ND|` and the unnormalized objective numerator is the expectation of the second displayed integral. Using the geometric moments through order four gives

`Z=8td+4m(t+d)+2T2+4A atan(z)`

and **exactly** `N−lambda Z=H_R`. Both rational and atan coefficients were checked universally; in particular the latter difference is `−2A^2`. Therefore at a zero `J=N/Z=lambda`.

For the normalizer enclosure let `cl=t(left)−d(right)`, `cu=t(right)−d(left)` and bound the positive denominator `t+d+m` by its endpoint values. This encloses z by `cl/y_upper < z < cu/y_lower`; combine the resulting atan bounds with the positive component bounds in Z. The exact resulting bounds are even inside

`0.3398888893661231 < Z_* < 0.3398888893661235`,

and hence imply the requested

`339888889366/10^12 < Z_* < 339888889367/10^12`.

Finally, for any `h in D`, `(S+kD)+h` is contained in `S+(k+1)D`. Applying this to both h and −h proves the shell index changes by at most one. Thus the constructed density ratio is between b and 1/b for every x and every closed-D shift; integration proves the event inequality. Compactness gives integrability via polynomial volume growth and geometric shell weights. No radial approximation is used.

### A4. Exact dependencies

1. **LAW642-A, and only as a conditional research premise:** at this epsilon, the displayed R-branch equations and all the listed screens are sufficient to identify the unique all-law J-optimal law in (7). Merely knowing existence, uniqueness or stationarity would not suffice. This review does not check that the named historical record actually has precisely these hypotheses and conclusions.
2. **Independent standard steps:** geometric factorial moments/Abel summation, circle and support-addition geometry, Green's formula, principal trig identities, alternating-series remainder, nonnegative-series tail bound, continuity/IVT, elementary differentiation and rational interval arithmetic. Their relevant computations/derivations appear above and in the controls.
3. **Not required:** the adopted ln64 competitor, any MDA/matching-norm result, any phase theorem, any held historical output, or an author PASS assertion. Without LAW642-A the review still establishes a feasible rounded shell with the displayed self-consistency root and intervals, but not its global optimality or uniqueness.

## Claim B reconstruction

### B1. Brunn–Minkowski radii, privacy and strict L decrease

Assume LAW642 supplies `p_*=b^(n_S)/Z` for a compact convex positive-area core. Interpret “diamond” here as the **centered** dilate `gD`; translated diamonds differing from their centered equal-area diamond belong to the non-diamond case. Equal-a.e. compact convex positive-area cores agree as closed convex sets, so no null-set ambiguity creates a third case.

For every integer k, Brunn–Minkowski and `kD+D=(k+1)D` give

`sqrt(|S+(k+1)D|) >= sqrt(|S+kD|)+sqrt(2)`.

Thus `R_k=sqrt(|S+kD|/2)` satisfies `R_(k+1)>=R_k+1`; in particular it increases and tends to infinity. If `n_sharp(x)=k`, then `||x+h||_1<=R_k+1<=R_(k+1)` for every h in D, so `n_sharp(x+h)<=k+1`. Use −h for the reverse bound. This proves the density `b^(n_sharp)/Z` is full-closed-D private, including all intermediate directions, not just vertices.

For any nested exhausting sets `E_k`, the pointwise identity

`b^(min{k:x in E_k}) = (1−b) sum_(k>=0) b^k 1_(E_k)(x)`

holds. Tonelli gives the equal normalization in (9), since `|R_kD|=|S+kD|`. The same identity with the nonnegative cost `||x||_1` gives (10). If `S` is contained in `MD`, then its dilates are contained in `(M+k)D`, so these area and first-cost sums are bounded by geometric sums of degree-two and degree-three polynomials.

For any finite-area set E and its equal-area centered diamond RD, writing `r=||x||_1` gives the exact bathtub difference

`integral_E r − integral_RD r = integral_(E\RD)(r−R) + integral_(RD\E)(R−r)`.

The radius boundary is null. The terms are nonnegative, and the difference is strictly positive whenever the symmetric difference has positive area. Each layer difference in (10) is therefore nonnegative and the k=0 difference is strictly positive in this case. Its weight `(1−b)/Z` is positive, so `L(P_*)>L(P_sharp)>=V_L`. Brunn–Minkowski equality conditions, an L-optimality theorem, and L-optimizer radiality are not needed.

### B2. Diamond core, interior scalar optimum and root ordering

For `S=gD`, the shell identity for g>1 is exact even on closed layer boundaries. Its normalization is

`P_(g−1)=alpha P_g+(1−alpha) Uniform((g−1)D)`,

with `alpha=b Z_g/[b Z_g+(1−b)2(g−1)^2]` strictly between 0 and 1. The uniform component need not itself be private; `P_(g−1)` is private by its shell construction. For any l1-radial density, direct triangle integration gives `J=(2/3)E r^2`. Conditional on `r<=g`, P_g is uniform on gD and has `E r^2=g^2/2`; it also has positive mass outside gD. Thus its full `E r^2` is strictly larger than the uniform inner value `(g−1)^2/2`. Consequently `J(P_(g−1))<J(P_g)` and a globally J-optimal diamond core cannot have g>1.

The endpoint laws `P_0=P_1` agree as probability measures (their unnormalized densities differ by a factor b away from a null point). To exclude both endpoints, use **`J'(1)>0`**, not positivity at zero: a sufficiently close point to the left of 1 has strictly lower J. This supplies the correction to LF151 using its own LF164 endpoint calculation.

For the remaining scalar calculation let `M_j(g)=E(g+N)^j`. Direct diamond integrals give `L=(2/3)M3/M2`, `J=M4/(3M2)` and `M_j'=j M_(j−1)`. In centered coordinates `x=g+m`, `v=m(m+1)`, `tau=1+2m`, the independent moment expansions are

`M2=x^2+v`, `M3=x^3+3vx+v tau`,

`M4=x^4+6vx^2+4v tau x+v+9v^2`.

The quotient derivatives give precisely Q and P in (11), including the factor `2/(3M2^2)`. Their expanded g forms and both endpoint values agree with the candidate.

For every m>0, Q has coefficient signs `+,+,+,−,+`. P has signs `+,+,+,(either sign or zero),−,+`; in all cases there are exactly two sign changes. At `g0=sqrt(v)−m`, `0<g0<1`; `tau^2=4v+1` gives `2sqrt(v)<tau`. Substitution therefore makes both Q and P strictly negative as stated. Together with positive endpoint values, IVT gives two distinct roots in `(0,1)` for each polynomial; Descartes bounds the positive roots counted with multiplicity by two, so both roots are simple and these are all the positive roots. The larger roots are the scalar minima. In particular `g_L>g0`. The second-root minimum of J is strictly below `J(1)=J(0)`, because J is increasing between that root and 1, so the global diamond optimizer has `g=g_J in (0,1)`.

For the ordering, `P=xQ+vR` is an exact polynomial identity. At Q=0,

`xR=3(x^2−v)^2−x^2`.

Set `z=x_L^2/v>1`. The root equation gives `x_L^4+3v^2=2v tau x_L`; squaring and using `tau^2=4v+1` gives

`1/v = [(z^2+3)^2−16z]/(4z)`.

Subtract `3(z−1)^2/z` and factor to obtain exactly (12). Its right side is positive, so `3(x_L^2−v)^2<x_L^2`, hence `R(x_L)<0` and `P(g_L)<0`. The smaller P-root lies below g0 and g_L exceeds g0; P is negative only between its two positive roots. Therefore `g_L<g_J`. Since Q is positive after g_L, L is strictly increasing there, yielding

`L(P_*)=L(P_gJ)>L(P_gL)>=V_L`.

No claim that `P_gL` is a global L-optimizer is used.

### B3. Opt_L existence, restricted attainment and strict infimum gap

The product Laplace density proportional to `exp(−epsilon ||x||_1)` is feasible by the triangle inequality and has `L=2/epsilon`, `J=4/epsilon^2`. Thus both global infima are finite from above.

An L-minimizing sequence has uniformly bounded first moment, hence is tight by Markov. Prokhorov gives a weakly convergent probability subsequence. Privacy is weakly closed **for every** fixed h in the full closed D: the event inequality is equivalent to

`integral f(x) dmu(x) <= b^−1 integral f(x−h) dmu(x)`

for nonnegative bounded continuous f. Both functions are bounded continuous, so this passes to the same weak limit. Approximation of open indicators and regularity of finite Borel measures on R^2 recover the inequality for all Borel events. This argument applies to each h with no h-dependent subsequence, so the uncountability of D causes no gap.

The cost r is nonnegative continuous and therefore weakly lower semicontinuous in expectation, for example by bounded continuous truncations. The limit has `L<=V_L` and, being private, also `L>=V_L`; consequently it belongs to Opt_L. No density theorem for weak limits is needed.

Let `a=inf_(Opt_L) J`. If a is infinite, the claim follows because V_J is finite. Otherwise choose a restricted minimizing sequence with bounded J. Markov on `|x|_2^2` gives tightness; take a weak limit. Weak privacy closure applies again. Lower semicontinuity gives `L(limit)<=V_L`, hence equality, and `J(limit)<=a`, hence equality by restricted minimality. Thus the finite restricted infimum is attained. Since `a>=V_J`, equality would make this limit a global J-optimizer. LAW642 uniqueness would force it to be P_*, contradicting B1/B2's `L(P_*)>V_L`. Therefore `a>V_J`, with a strictly positive extended-real difference. No uniform lower bound in epsilon is inferred.

### B4. Exact dependencies and where more premises would be needed

1. **LAW642-B:** for each fixed finite epsilon>0, there exists a unique global J-optimal probability law, and it has the stated `b^(n_S)/Z` representation with compact convex positive-area core. The representation is used at B1/B2; uniqueness is used only in B3 to exclude equality of the attained restricted infimum. Positive area is used for the stated k=0 strictness and g>0. These are assumed parts of LAW642, not newly verified facts about its historical source. If the named premise omitted those structural statements, they would be additional necessary premises for this written proof.
2. **At B1:** Brunn–Minkowski for compact measurable planar sets, convexity/central symmetry of D, triangle inequality, Tonelli/layer summation and elementary equal-volume sublevel-set geometry. The argument does not need a matching-norm rearrangement theorem: it proves the particular private radial comparison itself.
3. **At B2:** elementary diamond triangle integrals, geometric moments, differentiation, Descartes' rule with multiplicities, IVT and exact polynomial algebra. The repair of LF151 requires only the already displayed positive P(1), not another theorem or source. No phase threshold or global L-family theorem is required.
4. **At B3:** Markov, Prokhorov on R^2, weak convergence against bounded continuous functions, regular Borel measure-order characterization and lower semicontinuity of nonnegative continuous-cost integrals. These are the standard analytic imports. The limit need not be asserted absolutely continuous, and Radon–Nikodym/Lebesgue differentiation are not needed in this reconstruction.
5. **Not used anywhere:** MDA26, v241, v253, ln64 competitor arithmetic, historical author/reviewer PASS assertions, all-law L-optimizer uniqueness/radiality, a uniform-in-epsilon gap, source equivalence, or novelty. No additional research premise beyond the explicitly scoped LAW642-A/B was needed.

## One nonblocking finding

**MINOR / P3 — Use the derivative at one to exclude the endpoint laws.** Candidate LF151, `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-original-target-consolidated-review-v1.md`. The sentence uses `J'(0)>0` to rule out `P_0=P_1` as a scalar minimum, but a positive right derivative at zero alone is compatible with an endpoint minimum. The directly applicable reason is `J'(1)>0`, already implied by the positive P(1) at LF164, which gives a lower-cost point immediately to the left of 1 and excludes both equal endpoint laws. Confidence 1.0. This is a local proof-justification correction, not a counterexample or a missing scientific premise; B2 above supplies the complete corrected argument.

## Final disposition

Both requested conditional conclusions reconstruct at their exact scopes, with the one nonblocking LF151 correction stated explicitly. The exact numerical enclosures are independently supported, and the global/uniqueness identification remains conditional on the precisely named LAW642 premise. No source-equivalence, novelty or unconditional all-law optimum conclusion is granted.
