# f191: exact-certificate and scalar-envelope review

Reviewer: `ReviewF191PrivacyExact`, same harness. Native clock observed immediately before composition: `2026-10-29T09:37:02-0700 PDT`.

## Disposition and dependency boundary

**Conditional arithmetic/scalar verdict: no FATAL, MAJOR, or MINOR mathematical finding in the reviewed §§5–10.** My independent exact controls support the claimed strict width-`1/10^33` bracket, the global three-regime scalar lower bound, and the junction/parameter boxes **provided** the §§2–4 all-law measure-geometric reduction, the stated optimal-phase existence/equality conditions, and their application to the §5 core are valid. I did not review or establish that all-law reduction. In particular, the lower bracket and uniqueness for *all Borel laws* remain **INCONCLUSIVE in this review**, not accepted on arithmetic alone. The explicit feasible shell upper bound is separately supported by the distance, integration, feasibility and interval arguments below; it does not require the all-law reduction.

| Claim | Scoped disposition | Controlling evidence and dependency |
|---|---|---|
| §5 CAN and §6 distance/moment identities | No arithmetic/scalar finding, conditional on the stated symmetric compact core properties | Direct derivation below; both exact polynomial engines verify diamond and triangular specializations. I do not establish that every optimum has those core properties. |
| §7 clipping, three regimes, derivatives and boundaries | No finding in the scalar argument | Direct threshold/convexity reasoning and independent polynomial identities; interval endpoint data are exact. |
| §8.1 rational feasible upper shell and `V < λ_hi < 1/2` | No finding | Exact construction and strict positive cross-products; shell feasibility from the elementary distance Lipschitz argument. |
| §8.2 uniform diamond exclusion | No finding | Exact polynomial derivative, two-sign-change argument, four endpoint signs and positive rational lower comparison. |
| §8.3–8.4 uniform rounded/lower-clip exclusion | No finding | Exact field signs, interval tangent bound and uniform positive lower-clip derivative; coverage and endpoint matching proved below. |
| §9 stationarity, junction uniqueness and three parameter boxes | No scalar finding, conditional on existence and canonical representation of every optimal law | Exact field and corner inequalities, strict convexity, and rectangle monotonicity. The geometric implication that every original optimum is represented is not checked here. |
| Lower half of Theorem B and uniqueness for all original laws | **INCONCLUSIVE in this slice** | Require the separate all-law geometric reduction and exact correspondence of optimal phases to feasible shell cores, not supplied by the finite computations. |
| Prior-work equivalence, independent cognition, priority/novelty, formal/kernel or human verification | **INCONCLUSIVE / not claimed** | No external sources, other reviews, or formal proof were consulted. The candidate expressly discloses same-author prior LAW642 consultation. |

The exact scalar checks do not certify the measure-theoretic argument merely because the same candidate presents both. No LAW642, MDA26, f181, f158, d67, held/f161/f162, or protected-v214 body or result was used as a scientific premise. This is one same-harness review, not an independent-model-family, human, or kernel proof.

## Source order, binding, and process deviation

1. Before the manifest I read the required advisory memory summary and two workflow skill files, and I listed the `review-waves` directory to locate the assigned wave. **Process deviation:** that directory listing also exposed names and metadata of neighboring wave artifacts before the manifest. It did not open those artifacts or expose their mathematical bodies; no neighboring result was used. Thus the scientific-source order was manifest then sole candidate, but the literal "manifest first" sequencing was not met for this administrative listing. No such other administrative or scientific material was promoted to a premise.
2. Read `manifest-v1.json`, then at native clock `2026-10-29T09:31:57-0700 PDT` checked its SHA-256 against the assigned `a232531f6611ec2af301037df8eee30d156b00dcd90c8e76c90f2574b00c3011`. The sole candidate was `frontier-20261029-lawfree-lower-half-v1.md`, SHA-256 `ddd3fc87bd38475500589957e030119de451c6fa5f0b27ea54fb8e0856ea62ea`; it had exactly `34202` bytes and `495` LF lines. The first execution receipt also records no CR bytes and a terminal LF.
3. Read the entire candidate in actual raw windows, in order: 1–40, 41–80, 81–120, 121–160, 161–200, 201–240, 241–280, 281–320, 321–360, 361–400, 401–440, 441–480, and 481–495, including the ending. Only after this complete visible read did I reconstruct mathematics or write controls. I read the embedded author cell as text but never ran or imported it. The candidate's asserted author-run PASS lines are not evidence for my verdict.
4. I wrote two reviewer-owned implementations and two bounded receipt runners, then performed exactly one run of each. Each one-shot process had a `120 s` timeout; neither timed out. No web/external model/API, author contact, sibling review, Git, deletion, publication, infrastructure action, or unrelated build/lint/test/formatter was used. The reported monotonic elapsed values are timing data, not floating-point mathematical premises.
5. **Additional process deviation:** after drafting, I made an interactive `Fraction` comparison of the three coarse rational margins quoted in this report; all three returned `True`. That interactive check has no separately recorded native clock, script hash, or exit receipt, so it is **nonbinding**. The underlying exact interval bounds and strict acceptance predicates are in the two independently receipted runs; the displayed coarse-to-target comparisons are elementary rational comparisons, not an additional claimed certified run.

Disposition of these two deviations: **MINOR PROCESS**, not mathematical findings; neither supplies a scientific premise or a bound used for acceptance.

## Mathematical reconstruction and coverage

### Canonical geometry and moments, candidate lines 168–227

Assume the compact core has the symmetries and centered sections asserted upstream. With `(t,t)` its last diagonal point, the anti-diagonal segment through `(F(y),y)` contains `(F(y)+y-y',y')` for `y ≤ y' ≤ t`; monotonicity gives `0 ≤ F(y)-F(y') ≤ y'-y`, `t ≤ F(y) ≤ 2t-y`, and `F(t)=t`. This is the only core property imported into the scalar scan. Conversely, the proposed clipped and explicit upper profiles have these inequalities and form compact unconditional down-sets after the specified symmetry extension.

For sorted `x1≥x2≥0`, a nearest core point may be reflected and coordinate-clipped; sorting it preserves domination by `x`. Maximizing `k1+k2` then gives `(x1-F(x2))_+` when `x2≤t`, and `x1+x2-2t` when `x2>t`. For the latter, `(t,t)` is admissible and every core coordinate sum is at most `2t`.

Write `E_j=∫_0^t F(y)^j dy` and `E_y=∫_0^t y²F(y)dy`. Direct octant integration, including the tail, gives

```
Z = 8(E_1-t²/2)+8tm+2T2,
N = (2/3)T4+(16/3)tT3+4t²T2
    +8[T2 E_1+m(E_2+t³/3)+E_3/3+E_y-t⁴/3].
```

For the tail, with `s=p+q` and `0≤q≤s/2`, its unit-octant mass integrand is `s/2` and cost integrand is `t²s+ts²+s³/3`. Tonelli plus the geometric-series identity `∫_0^∞ b^ceil(s)s^j ds=E[G^(j+1)]/(j+1)` produces tail contributions `T2/4` and `t²T2/2+tT3/3+T4/12` before the factor 8. The remainder of the `tT3` coefficient is from the strip. The polynomial boundary control verifies the slice and both tail coefficients, and detects an omitted `T4` tail.

For an arc `F(y)=sqrt(A-y²)-m`, ending at `c` with `S=sqrt(A-c²)>c`, set `θ=atan(c/S)`. The controls separately use

```
I0=∫_0^c sqrt(A-y²)dy=(cS+Aθ)/2,
I1=∫_0^c y²sqrt(A-y²)dy=(c(2c²-A)S+A²θ)/8.
```

Their derivatives were checked by exact polynomial identities after multiplying by the positive square root. The independent evaluator expands the arc powers in `I0,I1` and integrates the facet using `x=2t-y`; it is not the author's `moments` routine. For the full facet, exact polynomial identities give `Z=2M2(2t)`, `N=(2/3)M4(2t)`.

### Clipping and every `t` regime, candidate lines 228–272

`∂_zG=(z+m)²+y²+v-λ` and `∂²_zG=2(z+m)>0` for `z≥0`, so pointwise minimization on `[t,2t-y]` is the displayed clip. On a rounded piece where `R>t`, `|R'|=y/(R+m)<1` since `0≤y≤t`; the constant and facet pieces also preserve CAN. Thus the clip is itself a feasible profile, not merely an unattainable relaxation. The shell density is feasible for every compact core because `|d_1(x+h,C)-d_1(x,C)|≤1` for every closed-diamond shift; taking ceilings changes the exponent by at most one.

For `λ>T2`, both thresholds are positive. At `R(0)=2t`, the root equation gives `λ=4t²+4mt+T2`; at `R(t)=t`, it gives `λ=2t²+2mt+T2`. Their difference at a common positive `t` is exactly `2t(t+m)>0`, so `0<t_D<t_U`. Where `R≥t`, `R(y)+y` is strictly increasing. Consequently:

* `0<t≤t_D`: the upper facet clips all `y` (D).
* `t_D<t<t_U`: there is exactly one interior upper junction (R).
* `t≥t_U`: lower clipping applies and the upper clip is absent (L).

These cases cover all positive `t`, including the boundary values by continuity. If the radicand defining `R` is nonpositive, the lower clip still applies and the root derivative is not used there.

Moving-interface terms cancel because adjoining profile values agree. Independently differentiating the `F`-independent part of `N-λZ` **and retaining the endpoint** `8G(t,t)` gives

```
B=(16/3)T3+16tT2+16mt²-8λm.
```

For an upper facet `u=t-y`, the additional derivative is `16∫_0^d [2(t²+u²)+2m(t+u)+T2-λ]du`. Substituting `λ=2t²+2d²+2m(t+d)+T2` gives exactly

```
h'/16 = C0+tv-(4d³/3+2md²+m²d),
d' = -(2t+m)/(2d+m),
h''/16 = v+(2d+m)(2t+m)>0.
```

The first equality, `P3'(d)=(2d+m)²`, and the base endpoint identity were independently checked over a sparse rational polynomial ring. In L the active lower-clip integrand is nonnegative, while `B-(16T3/3-8λm)=16tT2+16mt²≥0`. At `d=0`, the R one-sided derivative is `16(C0+tv)>0`; hence the junction to L matches and cannot hide a zero-minimum. Both boundary controls that drop the endpoint or reverse its sign were rejected.

### Exact arithmetic implementation

All original input endpoints are exact rational numbers, including `λ_lo`, `λ_hi`, `c_a`, `c_b`, the two 40-digit construction parameters, and every claimed box. Neither a rounded decimal nor a binary float is an input to an acceptance predicate. The independent code uses:

* `Fraction` for rationals and sparse polynomial coefficients;
* an explicit `a+b√D` field, with sign decided by rational signs and, when opposed, comparison of `a²` and `b²D`; incompatible fields and zero norms are rejected;
* `isqrt(floor(D·10^150))`, with rational endpoints `k/10^75,(k+1)/10^75` and checked square orientation;
* outward interval arithmetic on a rational `10^-75` grid, with floor/ceiling performed using integer division; original endpoint rationals are not rounded on input;
* the alternating arctangent series on the checked domain `0<z<1`. The 20-term even partial sum is a lower bound and that sum plus the next positive term is an upper bound. Every interval operation is outward; signs of interval coefficients need not be guessed.

The verifier works with interval **cross-products**, proving `N-λ_lo Z>0` and `λ_hi Z-N>0` with `Z>0`, rather than assuming an interval ratio or a derivative sign. The separate quadratic-field signs check the junction derivatives without numerical root finding. All enclosure endpoints in its result are exact fractions.

## Finite predicates and consequences

The result file binds the complete exact values. Selected logically sufficient predicates are recorded here; a `≥` rounded rational below is an outward lower enclosure, not a decimal approximation.

1. **Domain:** `m=1/63`, `v=64/3969`, `T2=65/3969`, `T3=1451/83349`, `T4=102635/5250987`; exact checks give `T2<1/50<4/25<λ_lo<λ_hi<1/2` and `λ_hi-λ_lo=1/10^33`. Thus all threshold roots used in the scan exist. Since `λ_hi<1/2` and `v,m>0`, `2t_D=√(λ-v)-m<1` for every `λ` in the bracket.
2. **Actual upper law:** the exact `t40,c40` are those printed in the candidate and `reviewer-run1-stdout-v1.json`. The verifier checks `0<c40<t40`, `Y=2t40-c40+m>c40`, positive `N,Z`, and both strict cross-product inequalities. In particular the outward results imply `N-λ_lo Z>27/10^35` and `λ_hi Z-N>6/10^35`. Hence the constructed shell has `λ_lo<J(P_K40)<λ_hi`; the right inequality supplies `V<1/2` independently of the lower-bound reduction.
3. **D:** for `a=3761763123/10^10`, `z=3761763124/10^10`, the derivative numerator is the displayed quintic `P`. Its coefficient signs from highest to lowest are `+,+,+,-,-,+`, exactly two changes. Exact tests give `P(0)>0`, `P(a)<0<P(z)`, and `P(1)>0`; Descartes' rule of signs and the intermediate value theorem therefore give exactly two positive simple roots, the second in `(a,z)`. The derivative sign pattern, `J(P_0)=J(P_1)`, and positive increasing `M2,M4` give the global minimum on `[0,1]` at the second root and

   `M4(a)/(3M2(z))>λ_hi`.

   The denominator is checked positive; the recorded rational lower enclosure for the difference is positive. This excludes **all** D parameters for **every** `λ` in the bracket.
4. **R at `λ_lo`:** `c_a=9274808134495397323165995922/10^30`, `c_b=9274808134495397323165995923/10^30`. Both constructed junctions have positive `d`, `c<S`, `c<t`, positive shell mass, and ordered `t_a<t_b`. Exact quadratic-field comparison proves `h'(t_a)<0<h'(t_b)`. Strict convexity makes the global R minimum lie between them, while the tangent inequality gives

   `min_R h_(λ_lo) ≥ h_(λ_lo)(t_a)-|h'_(λ_lo)(t_a)|(t_b-t_a) > 27/10^35`.

   The explicitly evaluated tangent lower enclosure is at least `2749/10^37`, which is strictly greater than `27/10^35`. No grid scan or assumption that a sampled point is a stationary point is used.
5. **L, uniformly:** the exact rational lower derivative bound at `λ_hi` is

   `451005338903901157841595228336507929 / 6251175000000000000000000000000000000 > 0`.

   It holds for all `λ≤λ_hi` in the bracket and all L parameters. L's left boundary is positive by continuity from the R minimum. Together with D and R this proves `h_(λ_lo)(t)>0` for every `t>0`, conditional only on the explicit scalar formulas.
6. **Boxes and uniqueness at a value `V` in the bracket:** over the whole rectangle `[c_a,c_b]×[λ_lo,λ_hi]`, outward rational root bounds prove `d>0`, `c<S`, and `(2d+m)²>v`. At fixed `c`, `∂_S(h'/16)=(v-(2d+m)²)/2<0`; at fixed `λ`, `dt/dc=(1-c/S)/2>0` and `h''>0`. The exact signs `f(c_a,λ_lo)<0<f(c_b,λ_hi)` therefore trap the unique stationary junction uniformly for any such `V`. Corner root enclosures imply the strict target boxes

```
9274808134495397323165995922/10^30 < c_* < 9274808134495397323165995923/10^30,
17899568185394517443007219151/10^29 < d_* < 17899568185394517443007219152/10^29,
18827048998844057175323818743/10^29 < t_* < 18827048998844057175323818744/10^29.
```

   If the upstream reduction indeed makes every optimal phase a canonical shell, then `h_V≥0` for every feasible clip, every optimum gives a zero, D and L cannot contain that zero, R has a unique strictly convex zero, and strict pointwise clipping makes the core unique. The final inference from optimal phases to **all** optimal laws remains conditional on the upstream mixture/reduction, which this slice does not certify.

## Controls, clocks, and artifact hashes

Each control runner checked the input and manifest SHA before launching the reviewer-owned process. Both completed with exit code `0`, empty stderr, and `120 s` caps. A timeout would have been `TIMEOUT_UNKNOWN`, not PASS.

| Artifact | SHA-256 / observed execution |
|---|---|
| `reviewer-exact-v1.py` | `0f73bbaa3a40179b3f6ddb4d0c535fe1c1ba066da51eefd15ae4f9f23aef04f4` |
| `reviewer-runner-v1.py` | `fc2540a783d7e838a30d73514b182d327f6acf46eb4c0ec18d0f7e11ca9e2d0b` |
| `reviewer-run1-stdout-v1.json` | `b9b575318a57015136d2951be313b1398f2cdaff102a3016a4c57867671804bf` |
| `reviewer-run1-receipt-v1.json` | 09:35:12 to 09:35:12 PDT; exit 0; `0.090894958 s` monotonic. Includes exact command, input and script/runner/output hashes. |
| `reviewer-boundary-v1.py` | `7058fb9b146c696de40f81e66be802f32ad50972c04d19241d866f291fb2a79d` |
| `reviewer-boundary-runner-v1.py` | `b66f59e1be6286992c846931b665b29728d836d14e2e6429655f799127d60b3b` |
| `reviewer-boundary-run1-stdout-v1.json` | `760e78fb3203d64221477e5512d21f5ed2e12197bf0084c6ece080121afcf3da` |
| `reviewer-boundary-run1-receipt-v1.json` | 09:36:22 to 09:36:23 PDT; exit 0; `0.034124667000000004 s` monotonic. Includes exact command, input and script/runner/output hashes. |
| Both stderr files | empty, SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

Positive controls include field signs on both sides of zero, a field inverse, exact square-root orientation, positive-domain intervals, both arc primitive derivatives, the facet and triangle formulas, endpoint derivative, thresholds, diamond shift equalities, all original strict numeric predicates, both target boxes, and whole-regime polynomial identities. The negative controls were required to raise the *named* reason, not merely any exception:

* reversed λ endpoints and width enlarged → `lambda-domain-order`, `lambda-width`;
* diamond root endpoint moved left and diamond derivative sign flipped → `diamond-right-sign`, `diamond-derivative-identity`;
* R derivative sign flipped; junction left/right endpoints displaced → `rounded-derivative-identity`, `junction-left-sign`, `junction-right-sign`;
* triangle slice term omitted, `T4` geometric tail omitted, endpoint `G(t,t)` dropped or its λ sign reversed → the respective `triangle-boundary-term`, `triangle-moment-tail`, and `base-endpoint-derivative` identities;
* reversed threshold separation and flipped junction square → `threshold-separation`, `junction-formula`;
* interval denominator crossing zero and zero quadratic norm → `denominator-positive`, `quadratic-zero-norm`;
* odd arctangent truncation, out-of-domain argument, and upper partial sum mislabeled lower → `atan-truncation-parity`, `atan-domain`, `atan-lower-orientation`;
* square-root lower endpoint mislabeled upper → `sqrt-orientation`;
* each parameter box narrowed by one `1/10^29` unit → its own `diagonal-parameter-box` or `facet-parameter-box`;
* the explicit shell's constants rounded to `1883/10000` and `93/10000` → `upper-below-upper`.

There were 17 intended-reason negatives in the first run and 5 in the second; all were rejected for the requested reason. They test the independently implemented invariants, not an altered execution of the author cell. They do not by themselves prove an implementation free of errors.

## Named mathematical inputs and exact residual

The reasoning uses elementary algebra and calculus; monotonicity of square root and arctangent; the alternating-series remainder theorem for `0<z<1`; integer square-root ordering; Fubini/Tonelli for the nonnegative shell integration; geometric series and factorial moments; the intermediate value theorem, derivative sign test, Descartes' rule of signs, and the tangent inequality for a differentiable convex function. If §§2–4 are eventually established, their named assumptions also include Prokhorov compactness, weak lower semicontinuity/Portmanteau, Lebesgue differentiation, regularity, strict one-dimensional centered-interval moment rearrangement, and Tonelli/Fubini. They were not re-proved as part of this arithmetic slice.

**Remaining gate:** independently dispose of the all-law reduction, including the phase mixture, strict equality arguments, a.e.-to-exact compact representatives, closed-shift inclusions, minimal-shell replacement, and propagation of uniqueness to arbitrary original laws. Arithmetic does not settle those points. The candidate explicitly reports consulting its author's own earlier LAW642 text; my separate implementation does not certify cognitive independence or novelty. No general-ε claim is reviewed.
