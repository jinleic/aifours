# f261 slice A: independent review of the twice-corrected privacy optimizer

## Verdict and boundary

**0 FATAL / 0 MAJOR / 0 MINOR; no INCONCLUSIVE in the claims expressly listed below.** This is a written, same-harness review of existence, the all-shift density and measurable optimal-phase mixture, and the corrected Steiner/essential-support geometry. It is not a human, independent-model-family, formal/kernel, novelty, or parent-acceptance result. In particular, this review does **not** assess the one-level perturbation arguments, tail cutoff, finite-profile minimum, cap, or optional f245 insufficiency example. No conclusion from slice B or an earlier review is used.

Verdict key: **P** means 0 FATAL, 0 MAJOR, 0 MINOR and not INCONCLUSIVE for that row, with precisely the qualifications stated here; it is not a claim beyond that row. A FATAL would refute the corrected claim, a MAJOR would identify a material proof gap, and a MINOR would identify a nonmaterial wording gap.

| Claim independently assessed | Verdict |
|---|---|
| Feasibility, weak closedness for all closed-D shifts, lower semicontinuity, attainment and V>0 | P |
| Bounded Borel density representative satisfying the privacy inequality for every point and every h in closed D | P |
| Positive density, positive E_0 area, measurable exact phase mixture and optimality of almost every component | P |
| Finite area/moment of each good phase level and the second correction's literal boundedness of every such level | P |
| Borel Steiner construction and exact full-D inclusion with empty zero fibers, closed positive finite fibers and whole-line infinite fibers | P |
| Finite-fiber moment equality only up to one-dimensional null sets; no infinite-fiber uniqueness | P |
| Four separate optimality comparisons, including existence and privacy of each symmetrized phase | P |
| Double-axis down-set, corrected two-boundary-point argument and planar null boundary | P |
| Essential-support equality a.e.; centered sections, D4 symmetry and positive interior | P |
| Area bound, compactness and exact closed-D inclusion between supports | P |
| Necessary D4 profile geometry (10), including the distinction between an actual optimizer level and the degenerate t=0 profile | P |
| First author fiber convention, second author geometry/fiber corrections, and parent zero-fiber clarification, within this slice | P |

The original uncorrected one-point boundary assertion and unqualified infinite-fiber uniqueness are false. The first and second author corrections are treated as prospective propositions and checked below, not presumed valid. No arithmetic controls were run; the counterexamples and reconstructions below are written arguments, not formalized or computational certificates.

## Frozen inputs and actual read sequence

The manifest's full SHA-256 was measured as `66b77dd60b4a5ca5e69004806b1bcda5731f62f26a53a79bdd23271c49f6ce5d`. Before displaying **any** input body, all five files were checked against its SHA-256, byte count, and LF count, decoded as UTF-8, and found to end in LF with no CR. All bodies were then displayed completely in the following declared order, in raw windows of at most 15 lines, including each ending; mathematical review began only after the final candidate line.

| Order and scope | Full SHA-256 | Bytes | LF displayed |
|---|---|---:|---:|
| First author fiber erratum | `6b8af7b2d672b470290f3673b5f799ac4ca8b5e015276f287bcdbe1a23a52e27` | 4541 | 1–48 |
| Second author geometry/cap correction | `89f91e9004c9563caf3d4cc831b1101c4e4ade8a138b006b5af7f00c1fddbb14` | 8688 | 1–77 |
| Prospective parent zero-fiber clarification | `3abe7a865335863704f5720f70af3abba39d8ad2d74c41db8df9791020986d6b` | 1522 | 1–17 |
| f245 disposition, optional-example scope only | `a5005ac8173be0b0c05bb5eb3cb82678ac22b1ae90de2c4d4a418f301d98a711` | 3662 | 1–24 |
| Original candidate, interpreted after the two corrections | `4263cf17acd50a6e1167d7c8b62560cd7c634c2d8711a808de70733cac659b43` | 22545 | 1–274 |

The f245 disposition was read because the manifest requires the whole ordered packet; **none** of its mathematical claims is a premise of this slice. The original candidate's owner code/PASS was not executed or imported. No f161/f162/held material, earlier f250/f256 review body, sibling result, linked source, external model/API, or Git was used. The prior reviews are not retroactively altered.

**Exact mathematical imports:** standard Markov tightness and Prokhorov; weak convergence against bounded continuous functions and regularity of finite Borel measures; Radon–Nikodym and the Lebesgue differentiation theorem; Tonelli/Fubini and monotone convergence for nonnegative Borel functions; inner compact approximation for one-dimensional Lebesgue measure; countability of discontinuities of a real monotone function on a finite interval; elementary Euclidean invariance/scaling of Lebesgue measure. No preceding research theorem or optional example is imported.

## Reconstruction and claim-specific checks

### 1. Existence and the everywhere-private representative — P

The product-Laplace density `p(x)=(ε²/4) exp(-ε||x||_1)` integrates to one, has second moment `4/ε²`, and satisfies `p(x+h)≥b p(x)` for every `h∈D` by the triangle inequality. A minimizing sequence can be chosen with uniformly bounded second moment, giving tightness by Markov. For each **fixed** `h∈D`, passage to a common weak subsequential limit in the inequality against nonnegative bounded continuous functions gives the same measure inequality; closed-set approximation and Borel regularity extend it to every Borel event. Since the limit subsequence is independent of h and h was arbitrary, this proves all shifts, including the boundary, without intersecting uncountably many exceptional sets. The cost is weakly lower semicontinuous as the supremum of the bounded continuous truncations `min(|x|²,R)`. Thus an optimum exists and is finite. Its cost cannot be zero: the only zero-cost probability is `δ_0`, which violates privacy for `{0}` and any nonzero `h∈D`.

Integrating `b μ(A)≤μ(A+h)` over D and applying Tonelli yields `2b μ(A)≤|A|` for Borel A. Hence the Radon–Nikodym density is bounded by `1/(2b)` a.e. The rational-radius limsup of ball averages is Borel, has this bound **at every point**, and is a density a.e. Comparing the two shifted balls at every radius, then taking limsups, gives `f(x+h)≥b f(x)` for **each** x and **each** closed-D shift h. Some value is positive by differentiation and total mass one; a finite chain of D-shifts then makes every value positive. Its supremum `M` lies in `(0,1/(2b)]`.

### 2. Phase identity, measurable kernel and component optimality — P

For `a∈(bM,M)`, `E_i(a)={f>ab^i}` is jointly Borel in `(a,x)`; the strict inequality and the all-point privacy bound imply the exact inclusion `E_i(a)+D⊆E_(i+1)(a)`. Positivity of f makes the levels increase to all of `R²` at every point. The minimum index `n_a(x)` and `u_a(x)=b^n_a(x)` are jointly Borel, and the level inclusion yields `u_a(x+h)≥b u_a(x)` pointwise.

If `f(x)>a`, some small ball average exceeds a, so the a.e. density exceeds a on a positive-area subset of that ball. Thus every E_0(a) has positive area. For a direct phase-identity check, choose the integer `k≥0` with `Mb^(k+1)<f(x)≤Mb^k` and set `θ=f(x)/b^k∈(bM,M]`. Except at the single threshold `a=θ`, the index is k for `a<θ` and k+1 for `a>θ`; hence

`∫_(bM)^M u_a(x) da = b^k(θ-bM)+b^(k+1)(M-θ) = (1-b)f(x)`.

Tonelli makes `Z_a=∫u_a` and `N_a=∫|x|²u_a` measurable extended-valued functions, with integrals `1-b` and `(1-b)J(μ)`. Therefore for Lebesgue-a.e. a, `0<Z_a<∞`, `N_a<∞`, and `P_a(dx)=u_a(x)dx/Z_a` is a Borel probability kernel satisfying every original shift constraint. The weight `Z_a/(1-b)` gives the exact law mixture and is positive on those good parameters. For an optimal μ, the integral of the nonnegative difference `J(P_a)-V` is zero, so almost every such phase is optimal. On the exceptional null parameter set one can define the kernel to be any one already-existing good optimal phase, preserving measurability and making the entire chosen kernel optimal. No pointwise choice of canonical K_i(a) is needed for the kernel: each K-phase has the same law as its original measurable phase.

For a good phase, `u_a≥b^i 1_(E_i)` proves finite area and second moment of every E_i. The additional literal-boundedness argument in the second correction is also valid: if E_i were unbounded, choose infinitely many points at pairwise distance greater than 1. The disjoint open radius-1/4 balls about them lie in `E_i+D⊆E_(i+1)`, contradicting its finite area. This uses only containment in the Borel next level, not measurability of the Minkowski sum.

### 3. Steiner fibers and literal closed-D inclusion — P

For a Borel A, Fubini/measurable integration makes its section-length function `ℓ_A(p)` Borel. The first erratum's rule therefore gives a Borel symmetrized set: the fiber is empty if `ℓ=0`, the closed centered interval if `0<ℓ<∞`, and the whole line if `ℓ=∞`. It preserves length even at zero and infinity.

Let `A+D⊆B` literally, fix a transverse p and `(q,v)∈D`, and write the D fiber at q as `[-δ,δ]`. If `ℓ_A(p)=0`, there is no source point. If it is positive finite, for each nonempty compact subset H of the A fiber, the B fiber contains H and its two outward δ-intervals; these have total length at least `|H|+2δ`. Inner compact approximation gives `ℓ_B(p+q)≥ℓ_A(p)+2δ`, also valid at the singleton D fiber `δ=0`. The closed endpoints give `|w+v|≤ℓ_A(p)/2+δ≤ℓ_B(p+q)/2` whenever the target length is finite; an infinite target fiber is all of R. If the source length is infinite, the B fiber contains a translate of it and is infinite, including when `δ=0`. Therefore `S_e A+D⊆S_e B` holds **as a literal set inclusion**, also for the diamond's boundary.

For a finite length `ℓ`, let `I=[-ℓ/2,ℓ/2]`. Since `|A\I|=|I\A|`, the integrand `(1_A-1_I)(w²-(ℓ/2)²)` is nonnegative and is strictly positive off the two interval endpoints wherever the sets differ. Thus I uniquely minimizes the second moment up to a one-dimensional null set; the `ℓ=0` case is the empty set up to null sets. No analogous uniqueness exists at infinite length. For a finite planar area and moment set, Fubini gives finite lengths and finite line moments for almost every transverse p; the nonnegative moment differences then vanish fiberwise almost everywhere when the planar moments are equal. The second correction accurately limits the conclusion to those fibers. In the present good phases, the stronger literal boundedness just proved actually makes **every** original fiber finite, but it still does not make equality hold on every fiber.

### 4. Four independent symmetrizations — P

Apply one of the four S_e to **all** levels of a fixed good optimal phase. The exact inclusion in §3 preserves the level constraints and 0∈D preserves nesting. For each transverse p, the original nested fibers increase to R, so their lengths increase to infinity. Consequently the symmetrized levels also increase to all of R at **every** point, and their index defines a pointwise private phase. Each level's area is unchanged; its moment does not increase. Its normalizer is positive and unchanged, and the new moment is finite. Optimality of the original phase therefore makes the sum of nonnegative weighted moment reductions zero, hence each level's reduction is zero. The finite-fiber equality argument gives `E_i=S_e E_i` a.e. separately for each of the four directions. This does not assume that successive symmetrizations commute or literally preserve previously obtained symmetries.

### 5. Double-axis boundary, essential supports and D4 geometry — P

Symmetrization respects a.e. equality of Borel sets: Fubini gives equal section lengths for almost every transverse coordinate, and the remaining transverse null set times R is planar null. Thus applying horizontal then vertical symmetrization to E_i yields a set T equal to E_i a.e. The horizontal centered sections are nested as `|x|` decreases, so the vertical section-length function is even and nonincreasing in `|x|`; T is a coordinate down-set under the stated zero/finite/infinite convention.

T has finite area. For `x≠0`, its vertical half-height H(x) is finite: an infinite value away from the axis, by monotonicity, would produce infinite area. Away from the countably many jump coordinates of H, continuity implies at most one boundary point in the open upper half-plane and at most one in the open lower half-plane. There may therefore be **two** boundary points on a full vertical line. The coordinate axes and the vertical lines through jump coordinates are planar null; Fubini applied to the remaining fibers gives `|∂T|=0`. Since `T Δ supp_ess(T)⊆∂T`, and T and E_i agree a.e., `K_i=supp_ess(E_i)` agrees with E_i a.e. This establishes the second correction's boundary repair rather than the original one-point assertion.

For any of the four directions, `E_i=S_e E_i` a.e. makes their essential supports equal. A positive contraction along the symmetrized fibers maps S_e E_i into itself and scales area by its positive determinant; the image of a sufficiently small ball is contained in a ball around the contracted point. Thus it maps essential-support points to essential-support points. Reflection does likewise, and closedness permits contraction to zero. Every K_i section is consequently a closed centered interval, possibly empty, a singleton, or unbounded. The four reflection directions give D4 symmetry.

Every E_i has positive area, so K_i contains some point with both coordinates nonzero. Coordinate contractions and reflections then give a rectangle around zero contained in K_i, hence `0∈int K_i`. For any x∈K_i, let `s=||x||_1`. After coordinate reflections, the anti-diagonal centered section contains the midpoint `(s/2,s/2)` between the point and its coordinate swap. The axis contractions/reflections contain the square `[-s/2,s/2]²`, giving `s²≤|K_i|=|E_i|<∞`. K_i is closed and bounded, hence compact. Because K_i=E_i a.e., it is also its own essential support.

Finally, for x∈K_i, h∈D, and every r>0, the translate `(E_i∩B_r(x))+h` has positive area and lies inside `E_(i+1)∩B_r(x+h)`. Thus `x+h∈K_(i+1)` and `K_i+D⊆K_(i+1)` **exactly**, with no invalid pointwise substitution of a.e.-equal representatives into a Minkowski sum. This argument covers all boundary shifts as well as interior shifts.

### 6. Necessary profile geometry and degeneracy — P

For an actual K_i, compactness and positive interior give `t=max{s≥0:(s,s)∈K_i}>0`. Axis sections make the maximal horizontal coordinate F(y) nonincreasing, and the square from `(t,t)` gives `F(y)≥t` for `0≤y≤t`. The anti-diagonal centered section would produce a diagonal point larger than t if `F(t)>t` or if `F(y)+y>2t`, so `F(t)=t` and `F(y)≤2t-y`. For `y≤y'≤t`, the same anti-diagonal segment gives `F(y')≥F(y)+y-y'`; hence F is 1-Lipschitz and F(y)+y is nondecreasing. These are the geometric necessities in (10).

The abstract t=0 profile is `{0}` and is a permissible degenerate set for a separate profile construction, but it is **not** an actual optimizer essential-support level here: it has zero area, its essential support is empty, and it has no interior. This review makes no judgment about the later profile formulas or the variational minimum.

## Hostile controls: exact counterexamples to tempting upgrades

These are illustrative mathematical counterexamples, not claims that each example is itself an optimal phase.

1. **All-point privacy is not a property of an arbitrary a.e. density version.** Change the product-Laplace density only at the origin to zero. It represents the same private probability, but the pointwise inequality fails when shifting a nearby positive point to zero. The ball-average representative is needed; neither individual-a.e. inequalities nor an uncountable union of exceptional sets supplies (2).
2. **Weak convergence does not make second moments continuous, even within the privacy class.** Let P be the centered product-Laplace law and `P_n=(1-1/n)P+(1/n)(P shifted by (sqrt(n),0))`. Each P_n is private and converges weakly to P, but `J(P_n)=J(P)+1`. The proof needs lower semicontinuity, not equality of limiting costs.
3. **Zero fibers must not become singletons under the chosen convention.** For `A=B=∅`, replacing every zero-length section by `{0}` creates an entire transverse axis; adding D creates points off that axis, while the purported symmetrized B is only the axis. Empty zero fibers avoid this. Closed positive finite fibers and the whole-line infinite convention cover boundary shifts as checked above; the argument does not claim that this is the only possible valid convention.
4. **Infinite-fiber moment equality is not unique.** `[0,∞)` and R both have infinite length and infinite quadratic integral but differ by positive length. Finite planar area/moment alone can still hide an infinite fiber on a null set of transverse coordinates: add `{3}×[0,∞)` to a square. The actual good levels avoid even this exceptional infinite fiber by the independent literal-boundedness argument.
5. **Global equality does not imply equality on every finite fiber or literal set equality.** Let `A=[-1,1]² ∪ ({3}×[0,1])` and symmetrize vertically. Its area and planar moment are unchanged and all fibers are finite, but at x=3 the section `[0,1]` is replaced by `[-1/2,1/2]`, a positive one-dimensional change. Separately, deleting one point from a square also leaves the moment unchanged while literal equality with its symmetrization fails. Only a.e. statements are warranted.
6. **One full boundary point per vertical fiber is false.** For `[-1,1]²`, each x in `(-1,1)` has both `(x,1)` and `(x,-1)` on the boundary. At the jump coordinate x=1, an entire vertical segment is boundary. Two open-half-plane points plus separate jump/axis treatment are necessary.
7. **Finite area and moment alone do not give E=supp_ess(E) a.e.** In `(0,1)²`, take a union of small open balls centered at a dense countable set, with total area below 1/4. Its essential support is the closed unit square, while its complement in the square has positive area. The null-boundary/down-set argument is genuinely needed.
8. **Axis symmetry and D4 alone do not give compactness or the diagonal area bound.** The closed set `K={min(|x|,|y|)≤exp(-max(|x|,|y|))}` is a D4-symmetric coordinate down-set, has positive finite area and finite moment, equals its essential support, and contains both entire coordinate axes. Indeed its first-octant area is at most `∫_0^∞ exp(-x)dx`; weighted polynomial moments are likewise finite. It is unbounded and fails the anti-diagonal centered-section property: `(R,0)` and `(0,R)` are in K, but their midpoint is not for large R. Thus the diagonal directions do real work. Positive area is also needed for an interior conclusion: `{0}` has none.
9. **A.e. replacement cannot be made pointwise inside a Minkowski sum.** `(0,1)²` and `(0,1)²∪{(10,0)}` agree a.e., but adding D to the latter adds a positive-area diamond far away. Even for well-behaved supports, with `E_0=B°(0,1)` and `E_1=E_0+D`, `(1,0)∈supp_ess(E_0)` and `(2,0)∈supp_ess(E_1)` but `(2,0)∉E_1`. The translated-positive-area proof, not literal equality E_i=K_i, gives the support inclusion.
10. **Sequential Steiner operations need not commute.** For two disjoint horizontal unit-height strips, one with x-range `[0,2]` and one with x-range `[2,4]`, horizontal-then-vertical symmetrization gives `[-1,1]²` a.e., while vertical-then-horizontal gives `[-2,2]×[-1/2,1/2]` a.e. The four independent optimality comparisons are essential.

The stated review is limited to the corrected claims above; these negative examples do not establish or refute the unreviewed optimizer complementarity, tail, or profile-minimization conclusions.
