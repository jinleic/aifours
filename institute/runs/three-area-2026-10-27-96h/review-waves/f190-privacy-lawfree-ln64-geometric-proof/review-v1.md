# f190: geometric review of the all-law ln(64) candidate

Review drafting clock observed before this write: `2026-10-29T16:36:56Z` (`/bin/date -u`). This is a same-harness written review, not a human review, an independent-model-family review, or a formal/kernel verification. It is not a novelty, priority, source-equivalence, or general-epsilon determination.

## Disposition and exact boundary

**No FATAL, MAJOR, or MINOR mathematical defect was identified in the reconstructed measure-geometric argument in §§1–9. The numerical bracket, three very narrow optimizer boxes, and the resulting unconditional optimum/uniqueness claim are INCONCLUSIVE in this slice**, because their finite transcendental interval predicates are deliberately not certified here. The results below are conditional on every predicate in §8 of this review, not on the author's execution report or any sibling review. I did not execute or import the candidate's embedded cell.

An independent, exact rational feasible construction does establish the weaker prerequisite **V < 1/2**, without the arc certificate: for the core `(1/2)D`, the closed-shift-private shell law has

`J = 12549035/71140356 < 1/2`.

Consequently the minimal-shell reduction is not conditional on the narrow value certificate. The first unresolved exact step on the candidate's **tight bracket** route is the strict numerical comparison `J(P_K40) < λ_hi` in candidate §8.1, after the analytically verified feasibility and the rational domain checks. The lower endpoint additionally needs the diamond and whole-rounded-interval inequalities listed below; uniqueness and boxes additionally need the stated sign/enclosure predicates. Failure to certify these in this slice is not a finding that they are false.

| Claim under review | FATAL / MAJOR / MINOR findings | INCONCLUSIVE dependency |
|---|---|---|
| Existence, all-point density and all-law phase mixture (§§1–2) | None found. | None within the stated classical imports. |
| Four separate Steiner equalities; exact support/closed-shift representatives (§§3–4.3) | None found. | None within the stated classical imports. |
| Minimal shells for the attained optimum (§4.4) | None found. | None for this ε: the separate exact rational law above proves `V<1/2`. |
| Octant geometry, slope constraint, distance and all Z/N terms (§§5–6) | None found. | None within the stated classical imports. |
| Clip, D/R/L regimes and moving-boundary formulas (§7) | None found. | Application of strict numerical sign assertions is conditional on §8 below. |
| Value bracket and transition to every original Borel law (§8) | No FATAL/MAJOR/MINOR geometric defect found. | **INCONCLUSIVE:** upper arc-law and lower D/R/L finite inequalities. |
| Unique optimizing law and stated parameter boxes (§9) | No FATAL/MAJOR/MINOR geometric defect found. | **INCONCLUSIVE:** bracket, endpoint signs and root/arc enclosures in §8 below. |
| Self-contained status, comparison to prior results, novelty and general ε | No such conclusion is made. | Not within this review's authority or input. |

A 'none found' entry is the result of this bounded written reconstruction, not a declaration that the argument is formalized or independently accepted.

## 1. Input, sequencing and disclosure

The sole scientific input was `frontier-20261029-lawfree-lower-half-v1.md`, SHA-256 `ddd3fc87bd38475500589957e030119de451c6fa5f0b27ea54fb8e0856ea62ea`, **34,202 bytes, 495 LF**. The manifest's measured SHA-256 was `53f99fabcf3355ce967f5fcb986e62c2d6658e3b90125f0e10f418b880246570`. The manifest hash was checked at `2026-10-29T16:31:56Z`, then the complete manifest was read. The candidate hash and `wc -cl` were checked at `2026-10-29T16:32:03Z`, before its content was read. Every line 1–495, including the complete embedded code and ending, was visibly read in raw windows of 25 lines, except the final 20-line window; there was no elision. Window calls were issued in ascending four-window batches, but calls within a batch were parallel, so no stronger intra-batch temporal order is asserted. All batches returned through line 495 before the mathematical reconstruction or control calculations began.

Administrative memory/skill instructions and the run-directory listing were read before the manifest; they were not mathematical inputs. No prior LAW642, MDA26, f181/f158/d67, reviewer, held/f161/f162/protected214 scientific body was opened as a premise. The candidate itself discloses the author's earlier LAW642 consultation; the present review does **not** claim unaffected or independently clean cognition for that author. Within this review the candidate's prior-result references were treated only as provenance, not as proof inputs.

Process notes: a `python3 -c 'import sympy; print(sympy.__version__)'` dependency probe returned exit 1 (`ModuleNotFoundError`); its command's chained clock did not run, and a separate `/bin/date` at `2026-10-29T16:33:54Z` is only a post-failure bound. No package was installed. A first report-write attempt misspelled the home-directory component, returned ENOENT, and wrote no file; this report is at the assigned path. The actual controls use only the Python standard library and are separately clocked, hashed and receipted below. No other source-order/process deviation is known.

## 2. Classical inputs and all-law reduction

Imports used, explicitly: Prokhorov's tightness/weak-compactness theorem on Polish spaces; regularity of finite Borel measures on `R²`; weak convergence against bounded continuous functions and lower semicontinuity for nonnegative continuous cost via bounded truncations; Tonelli/Fubini and monotone/dominated convergence; Lebesgue differentiation for finite measures/densities; inner regularity of Lebesgue measure on Borel subsets of a line; countability of a Euclidean base and of discontinuities of a monotone real function; elementary one-variable integral/Leibniz and continuous/convex calculus; Descartes' rule of signs and the intermediate value theorem; and the alternating-series bound for arctangent **only as a conditional numerical input**. The centered-interval inequality and its equality case are proved directly below, not imported as an unspecified rearrangement theorem. No measurable-selection theorem is used.

Write `b=1/64`, `m=b/(1-b)=1/63`, `v=m(1+m)`, and `D={h: ||h||_1≤1}`. Set `T2=m+2m²`, `T3=m+6m²+6m³`, `T4=m+14m²+36m³+24m⁴`; these are moments of `G` with `P(G=k)=(1-b)b^k`. For a compact nonempty core, `u_C=b^ceil(d_1(.,C))`, with exponent 0 on C. Since the distance changes by at most one under **every** closed-D shift and `|ceil(r)-ceil(s)|≤1` when `|r-s|≤1`, normalization gives an actual DP law. Its geometric shell tails have finite mass and second moment.

The product Laplace law supplies a finite feasible objective. A minimizing sequence has bounded second moment and is tight. Weak convergence preserves each fixed-h inequality against nonnegative bounded continuous functions. Applying that argument for an arbitrary h in the same fixed weak limit, then closed-set approximation and Borel regularity, preserves **all** shifts and all Borel events; no countable-shift substitution is made. Lower semicontinuity gives an attained optimum.

For any feasible μ and Borel A, integrate the inequality over D: `2b μ(A)≤∫_D μ(A+h)dh≤|A|`. Thus μ has a bounded density. The rational-radius ball-limsup representative `f` is Borel, is the density a.e., is bounded everywhere, and obeys `f(x+h)≥bf(x)` for **every** x and h in D. It is positive somewhere by its a.e. density property and everywhere by a finite chain of D-shifts. Let `M=sup f`.

For `a∈(bM,M)` define `E_i(a)={f>ab^i}`. Strict thresholds and the all-point inequality give the actual set inclusion `E_i+D⊆E_{i+1}`; `E_0` is nonempty even if it has zero area. All indices are finite. For each x, partitioning the a-interval by the geometric thresholds gives exactly

`∫_(bM)^M b^{min{i:x∈E_i(a)}} da = (1-b) f(x)`.

The integrand is jointly Borel in `(a,x)`, since the threshold sets are Borel and the index is countable. Tonelli gives measurable mass/moment functions and finite mass and moment for a.e. a. The mass is strictly positive: a nonempty `E_0` makes `E_1` contain a translate of D. Normalizing produces a genuine mixture with weights `Z_a/(1-b)`; hence a.e. phase of any optimum is itself optimal. If `|E_0|=0`, reindex to `E'_i=E_{i+1}`: outside the null `E_0` the new unnormalized density is the old one divided by b, so the normalized law is unchanged and the new initial level has positive area. This argument is phase-by-phase; the final uniqueness implication does not select a core measurably as a function of a.

## 3. Four strict symmetrizations and null-set attacks

For any one of the two coordinate and two diagonal unit directions, replace each fiber by its centered open interval of the same length; preserve infinite fibers as whole lines. For a finite fiber with equal-length competitors, the pieces removed from the centered interval have `w²≤(ℓ/2)²` and added pieces have `w²≥(ℓ/2)²`, with equality only on the two endpoint points. Thus the fiber second moment strictly improves unless the fiber agrees a.e.; integration gives the strict equality criterion for finite moment. Fiber lengths are Borel, so all symmetrized sets are Borel.

The inclusion is an actual closed-shift inclusion, not merely a.e. Fix a fiber of A of positive length and a transverse displacement q. The matching fiber of B contains that A-fiber plus the interval `[-δ(q),δ(q)]`, where δ is the diamond fiber half-width. A nonempty compact subset of the fiber contributes its own measure and two exterior endpoint segments, giving length at least `|C|+2δ`; inner regularity and then arbitrary compact length prove the same bound for the fiber, including infinite length. Strict interior of the centered A-fiber leaves `w+v` strictly inside the corresponding centered B-fiber even when the shift h lies on the boundary of D. Hence `S_e A+D⊆S_e B` exactly.

Apply each of the four symmetrizations **separately to the original optimal phase**, not successively with a silent preservation claim. All normalized symmetrized phases are feasible, have the same mass, and have no larger moment. Optimality forces equality; each nonnegative weighted level difference therefore vanishes. Thus every level equals each of its four centered symmetrizations a.e. The strict equality assertion is genuinely needed to recover all four symmetries of the same original levels.

For the representative construction one cannot generally claim `supp_ess(A)=A` a.e. merely because A is measurable: choose a dense open subset E of `(0,1)` whose complement has positive measure, and take `A=E×(0,1)`; its essential support is the square and differs from A by positive area. Here the candidate supplies the extra needed property. Double coordinate symmetrization has the form `B={(x,y): |y|<L(x)/2}`, where L is even and nonincreasing in `|x|`. Finite area implies L is finite away from at most the axis; at continuity points of this monotone height the vertical boundary is finite, and its jump x-values are countable. Fubini gives a planar null boundary. Since `int(B)⊆supp_ess(B)⊆closure(B)`, the support and B agree a.e.; the two symmetrizations and the earlier equalities show `K_i:=supp_ess(E_i)=E_i` a.e.

Independently, for each of the four directions K_i is the essential support of a set with centered interval fibers. For `0<α≤1`, contraction of the along-fiber coordinate maps that set into itself, maps balls into balls, and has positive Jacobian; it therefore maps K_i into K_i. Closedness handles α=0. The corresponding reflection preserves the support, so **every** line section of K_i is a closed centered interval, including exceptional lines. The generated reflections give D4 symmetry. Positive area and coordinate sections give a centered rectangle and `0∈int K_i`. For any x∈K_i, reflection and anti-diagonal convexity put `(||x||_1/2,||x||_1/2)` in K_i; coordinate sections then contain a centered square of area `||x||_1²`. Finite area therefore bounds K_i, which is compact.

For every x∈K_i and h∈D, `(E_i∩B_r(x))+h` has positive measure and is contained in `E_{i+1}∩B_r(x+h)`. This proves `K_i+D⊆K_{i+1}` for **every** boundary shift. The isolated-point control below illustrates why merely replacing a set by an a.e.-equal representative before taking a Minkowski sum would be invalid.

## 4. Minimal shells and octant geometry

Let `C=K_0` and `C_i=C+iD`. Exact closed inclusion gives `C_i⊆K_i`; C contains 0, so `iD⊆C_i`. For i≥1, every point in `K_i\C_i` lies outside D and has `|x|²≥||x||_1²/2>1/2>V`. The shell sequence `(C_i)` is feasible with finite moment and mass. Its signed functional `H_V=Σ b^i(M-VA)` is nonnegative by optimality and no larger than the zero functional of `(K_i)`. The levelwise differences have nonnegative integrands, strictly positive away from a null set; therefore every `K_i=C+iD` a.e. Countability of levels gives equality of the two normalized phase densities a.e. This proves the reduction for every optimal phase, not just one chosen law.

For a resulting compact D4 core, set `t=max{s:(s,s)∈C}>0` and `F(y)=max{x:(x,y)∈C}` for `0≤y≤t`. Coordinate sections imply the octant is exactly `y≤x≤F(y)` and F is nonincreasing. The anti-diagonal segment joining `(F(y),y)` and its swap implies, for `0≤y≤y'≤t`, `F(y')≥F(y)+y-y'`; also `F(t)=t`, since otherwise this segment would meet the diagonal above t. Hence

`0≤F(y)-F(y')≤y'-y`, `t≤F(y)≤2t-y`, and `F(t)=t`.

In particular F is continuous and 1-Lipschitz. Conversely these inequalities define a compact D4 coordinate down-set by sign and swap extension; that much, plus compactness, is all that feasibility and the distance calculation require. Degenerate `t=0` is excluded for an optimal phase by the positive-area rectangle. The later clipping construction is nevertheless meaningful for every `t>0`, including its facet-only and flat-endpoint cases.

For an unconditional coordinate down-set, reflecting and truncating a nearest core point coordinatewise never increases the l1 distance. Sorting an admissible point also preserves admissibility when `x1≥x2≥0`. The slope condition makes `F(y)+y` nondecreasing, so maximizing the core coordinate sum under the coordinatewise constraint yields

`d_1(x,C)=(x1-F(x2))_+` when `x2≤t`, and `d_1(x,C)=x1+x2-2t` when `x2>t`.

Both formulas include the junction as a limit; boundaries do not affect integrals.

## 5. Area and moment reconstruction, including the triangle

For the shell density, integrating one octant and multiplying by 8 gives

`Z=8∫_0^t(F-y)dy+8tm+2T2`,

`N=(2/3)T4+(16/3)tT3+4t²T2 + 8∫_0^t[T2 F+m(F²+y²)+F³/3+y²F-4y³/3]dy`.

Indeed, for a fixed strip ordinate y the line mass is `F-y+m`, and its moment is `(E(F+G)^3-y³)/3+y²(F-y+m)`. In the **separate tail triangle**, write `(x1,x2)=(t+s-q,t+q)` with `0≤q≤s/2`. Its line area is `s/2` and direct integration gives `t²s+ts²+s³/3`. The elementary geometric-sum identity `∫_0^∞ b^ceil(s) s^j ds=E G^(j+1)/(j+1)` supplies triangle contributions `T2/4` to Z/8 and `t²T2/2+tT3/3+T4/12` to N/8. This recovers every term above, with no omitted triangle or boundary mass.

For `F=2t-y`, set `g=2t`, `M2(g)=g²+2mg+T2`, and `M4(g)=g⁴+4mg³+6T2g²+4T3g+T4`. Direct substitution gives `Z=2M2(g)`, `N=2M4(g)/3`, and `J=M4/(3M2)`. The `g=0` and `g=1` normalized laws coincide a.e. because their unnormalized densities differ by the factor b outside the origin. Substituting `g=1/2` yields the rational law in §2 and proves V<1/2 without any arc integration.

For the candidate's arc/facet formula, the following antiderivatives explain exactly where arctangent enters. Put `S(y)=sqrt(A-y²)`, `Y=S(c)>0`, `θ=arctan(c/Y)`, and

`I0=(cY+Aθ)/2`, `I1=[c(2c²-A)Y+A²θ]/8`.

On `[0,c]`, `F=S-m`, so the integrals of `F,F²,F³,y²F` are respectively `I0-mc`, `Ac-c³/3-2mI0+m²c`, `(A+3m²)I0-I1-3m(Ac-c³/3)-m³c`, and `I1-mc³/3`. On `[c,t]`, the corresponding facet integrals are `2t(t-c)-(t²-c²)/2`, `((2t-c)³-t³)/3`, `((2t-c)⁴-t⁴)/4`, and `(2t/3)(t³-c³)-(t⁴-c⁴)/4`. Substitution in Z/N makes both affine in θ. These identities establish the form to which the conditional interval arithmetic applies; they do not certify its narrow inequalities.

## 6. Clipping and the three complete regimes

For fixed `t,λ`, the F-dependent part of `N-λZ` is eight times the integral of

`G_λ(z,y)=z³/3+mz²+(T2+y²-λ)z`, with `G''=2(z+m)>0` for z≥0.

The unique pointwise minimizer on `[t,2t-y]` is `F_cl=min(2t-y,max(t,sqrt(max(λ-v-y²,0))-m))`. Where the root is active above t, its slope magnitude is `y/(root+m)≤t/(t+m)<1`; elsewhere slopes are 0 or -1. Hence the clip satisfies all canonical slope and endpoint inequalities. Its compact down-set gives a genuinely feasible shell law. Strict convexity yields equality in the clipping lower bound only if F equals the clip a.e.; continuity upgrades this to pointwise equality.

For `λ>T2`, put `t_D=(sqrt(λ-v)-m)/2` and let `t_U>0` solve `2t_U²+2mt_U+T2=λ`; then `0<t_D<t_U`. The increasing nature of `R(y)+y` wherever the root R is above t proves that there are no additional regimes:

* D: `0<t≤t_D`, entire upper facet `F=2t-y`;
* R: `t_D<t<t_U`, root on `[0,c]` and upper facet on `[c,t]`, with `0<c<t`, `d=t-c`, and `λ=2t²+2d²+2m(t+d)+T2`;
* L: `t≥t_U`, `F=max(t,R)` with no upper-clipped portion.

At `t_D`, c tends to 0 and the arc disappears; at `t_U`, d tends to 0 and the upper facet disappears. A later transition inside L to a completely flat profile merely empties the root-active interval and is already covered. The clipped integrand is continuous at moving joins, and at a root/clip join its z-derivative vanishes, so Leibniz boundary terms cancel. The upper and lower constraint motions contribute `16∫upper ∂_zG` and `8∫lower ∂_zG`, respectively; the endpoint plus F-independent terms give

`B=(16/3)T3+16tT2+16mt²-8λm`.

For R use `u=t-y`: the upper integrand becomes `2(u²-d²)+2m(u-d)` on `[0,d]`, with integral `-4d³/3-md²`. Put `C0=T3/3-mT2/2=m/3+(3/2)m²+m³` and `P3(d)=4d³/3+2md²+m²d`. Junction differentiation and the integral give

`h'_λ/16=C0+tv-P3(d)`, `d'=-(2t+m)/(2d+m)`,

`h''_λ=16[v+(2d+m)(2t+m)]>0`.

In L, the lower-clipped integrand is nonnegative, so `h'_λ≥(16/3)T3-8λm`. At the R/L boundary the derivative equals `16(C0+t_Uv)>0`. These are analytic identities/inequalities; whether the final lower bound is strictly positive throughout the target λ interval is listed as a finite predicate below.

## 7. Conditional all-law conclusion and uniqueness

Assume all predicates in §8. In D the exact derivative numerator of `J(P_g)` is `2P(g)`, where

`P=g⁵+5mg⁴+(2m+12m²)g³+(12m³-2m)g²-m(1+2m)(1+6m)g+m²(1+2m)`.

The coefficient signs and bracket signs give exactly two simple positive roots by Descartes plus the intermediate value theorem. The second root lies in `(aJ,zJ)`, the endpoint laws are equal, and `J(P_g)` is bounded below by `M4(aJ)/(3M2(zJ))>λ_hi` for `g∈[0,1]`. The target D regime has `g<1`, so its signed objective is positive.

At `λ_lo`, parametrize an R junction by `S=sqrt(λ_lo-v-c²)`, `t=(S+c-m)/2`, `d=(S-c-m)/2`. The endpoint predicate places the two tested junctions inside R, makes `dt/dc=(1-c/S)/2>0`, and puts `h'` on opposite sides of zero. Strict convexity places the unique R minimizer between them; the tangent bound in §8 makes its value strictly positive over the **entire** R interval. The L derivative bound is positive and the R/L boundary is positive by continuity, so L is positive too. For an attained optimum, the already established minimal core therefore has `(V-λ_lo)Z=N-λ_lo Z≥h_λlo(t)>0`. Its finite positive mass gives `V>λ_lo`; the actual arc law supplies the conditional `V<λ_hi`.

At `λ=V`, feasibility of the clip makes `h_V(t)≥0`, while an optimal core forces equality and matches the clip. The diamond predicate excludes D. L cannot begin at zero because its matching derivative is strictly positive: a zero there would force a negative value immediately to the left. Thus the zero lies in open R, and strict convexity gives a single zero-minimizing t and one clipped profile. Every optimal phase is the same normalized shell law and the joint mixture then forces every original optimal Borel law to be that law. This argument includes all optimizing laws, not merely symmetric starting laws.

For the boxes let `f(c,λ)=h'_λ(t(c,λ))/16`. The conditional rectangle bounds imply `c<S`, `d>0` and `(2d+m)²>v`; hence `dt/dc>0`, `∂_S f=[v-(2d+m)²]/2<0`, f increases with c and decreases with λ. The stated endpoint signs bracket the unique zero; monotonic square-root bounds then give the displayed d/t intervals. This reasoning is conditional and does not itself establish the interval endpoints.

## 8. Complete list of finite predicates still conditional here

All following author-asserted finite predicates are **conditional** pending the separate arithmetic slice, even where this review's narrower independent rational spot controls agree. Let

`λ_lo=163006627735070347894185905345794/10^33`, `λ_hi=λ_lo+10^-33`,

`t40=1882704899884405717532381874371113060926/10^40`, `c40=92748081344953973231659959220098184342/10^40`, and `Y=2t40-c40+m`, `A=Y²+c40²`.

1. **Domain and upper profile:** `T2<1/50<4/25<λ_lo<λ_hi<1/2`; `0<c40<t40`, `0<c40/Y<1`; and, using the actual arc/facet moments above and rigorous bounds for `θ=arctan(c40/Y)`, `λ_lo<J(P_K40)<λ_hi`. Only the right inequality is necessary for the tight upper bound. The lo/hi ratios require positive Z throughout the arctan enclosure. The simple rational law in §2 proves only `V<1/2`, not this comparison.
2. **Diamond regime:** at `aJ=3761763123/10^10`, `zJ=3761763124/10^10`, the exact coefficient sequence has two sign changes, `P(0)>0`, `P(aJ)<0<P(zJ)`, `P(1)>0`, and `M4(aJ)/(3M2(zJ))>λ_hi`. Positivity of the moment denominator and `2t_D<1` are also needed. Our control independently checked the domain chain and the four indicated P signs, but did not certify the last ratio in this review.
3. **Whole R regime at λ_lo:** let `ca=9274808134495397323165995922/10^30` and `cb=9274808134495397323165995923/10^30`. The square roots at both endpoints must be real, the resulting `0<ca<t(ca)<t_U`, `0<cb<t(cb)<t_U`, `ca<S(ca)` and `cb<S(cb)` must put both points in R and preserve their order, and `h'_λlo(t(ca))<0<h'_λlo(t(cb))`. Most importantly the outward-enclosed tangent comparison must be `h_λlo(t(ca))-|h'_λlo(t(ca))|[t(cb)-t(ca)]>27/10^35`. This is the finite predicate that makes the lower scan global; a float, grid or capped run would not prove it.
4. **L regime:** `(16/3)T3-8λ_hi m>0`. This rational inequality was independently spot-checked, but it remains listed with the other candidate predicates rather than substituting that spot check for the designated complete arithmetic slice.
5. **Optimizer rectangle and boxes:** `f(ca,λ_lo)<0<f(cb,λ_hi)`; on the entire rectangle the radicand is positive, `c<S`, `d>0`, `(2d+m)²>v`; and outward square-root enclosures imply

   `9274808134495397323165995922/10^30 < c_* < 9274808134495397323165995923/10^30`,

   `17899568185394517443007219151/10^29 < d_* < 17899568185394517443007219152/10^29`,

   `18827048998844057175323818743/10^29 < t_* < 18827048998844057175323818744/10^29`.

   The c bounds require the signs plus monotonicity; the d/t bounds require valid outward corner enclosures, not just rounded displayed decimals.
6. **Transcendental enclosure applicability:** `0<z<1` for every arctangent input; an even 20-term alternating sum is a lower bound and adding its next term is an upper bound; square-root bounds enclose the correct positive root; field sign comparisons and interval products are exact; and endpoint ratios are taken only with positive denominators. These are applicable analytic methods, but their actual finite evaluations and claimed outputs have not been accepted here.

## 9. Independent exact controls and limits

The following were implemented independently from definitions, not copied, imported or executed from the candidate cell. Each command had a 120-second cap; a timeout would be UNKNOWN. Scripts and retained stdout/receipts are inside this wave only:

* `reviewer-geometry-controls-v1.py` SHA-256 `683f761250b55c41179bf83b4a2fd68f4b79ff6c0a927770a90ffa7312c59b5d`; output SHA-256 `f048dd64e2efed2c91f33397609b9a51d1b927f037f8eeb24fb1d90ea96400a6`; `/bin/date` start and end `2026-10-29T16:34:50Z`, exit 0, no timeout. Its receipt is `reviewer-geometry-controls-v1.receipt.json`.
* `reviewer-rational-upper-v1.py` SHA-256 `23294439b1c22839948e1b70eaaa2fa00143f5d493f2fd87947249472bd3a098`; output SHA-256 `f441f5cce930dd516db435b8e7e0ba6bf347b3d704b6814475aca034fb9e53ea`; start `2026-10-29T16:35:58Z`, end `2026-10-29T16:35:59Z`, exit 0, no timeout. Its receipt is `reviewer-rational-upper-v1.receipt.json`.

The geometry control uses its own sparse rational polynomial ring to check coefficientwise the strip moment, tail triangle, full diamond Z/N, moving endpoint B, upper-facet R derivative/curvature factor, and diamond derivative numerator; it also checks rational phase-mixture examples, domain and derivative signs. Intended-reason negatives reject, respectively, strict improvement for an identical centered set; a null singleton being harmless under a Minkowski sum (its extra closed diamond is disjoint and has area 2); a phase identity without the factor `1-b`; omission of the triangle cubic or triangle area; omission of upper-facet motion or the diamond derivative's `g²` term; reversal of the indicated diamond/LC signs; and a shell exponent doubled so a closed unit shift changes the exponent by two. The square-core closed-shift grid covers 6,929 exact rational point/shift pairs including boundary shifts, but is a **finite diagnostic**, not an all-shift proof. The rational upper control confirms the exact fraction and rejects using that simpler law as the claimed tight upper bound.

These controls and the written argument do not reproduce or certify the author's narrow sqrt/arctan interval computations. Their successful exits are neither a formal proof nor a substitute for separate arithmetic certification or parent disposition.
