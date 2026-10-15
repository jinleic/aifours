# Results and proof obligations

Snapshot: 2026-10-14 (America/Los_Angeles).

**Verdict: PARTIAL overall. C1-Finite and the fixed-golden-angle C1-Bulk claim have verdict COUNTEREXAMPLE.** The precisely stated comparison theorems below are settled; the unrestricted elastic-energy book problem is not. **FRONTIER_METHOD: DELIVERY-READY** for these scoped results; **NOVELTY-UNCLEAR** for publication priority. No Discovery claim is made.

## 1. Claim contract and protocol

- **Claim:** determine whether a conventional equal-area golden-angle spiral is globally optimal for identical intrinsic disks on a cone, rather than merely dynamically accessible. Also determine exactly what a reduced Fibonacci-branch model predicts about chirality.
- **Strongest comparable baseline:** the planar triangular packing theorem and the known commensurate triangular crystals on cones; Bacher's local-lattice analysis of constant-divergence phyllotaxis. See STATUS.md. The baseline is not an arbitrary random configuration.
- **Missing ingredient for the book:** a specified elastic energy, experimentally relevant cone geometry, growth/relaxation rules, and a coordinate-free definition of the allowed Fibonacci-contact class. These are not supplied by a generic disk or Riesz model.
- **Decision value:** a certified loss rules out the fixed-golden-angle ansatz as a universal explanation by densest packing, and distinguishes a kinematic alternation mechanism from physical selection.
- **Exploration disclosure:** before freezing the witness, triangular quotient disks with outer squared radii `9,16,25,36,49,64,100,144,225,400` were compared numerically with equal-area spirals. Their closest pairs often lay near the apex. The retained annulus `10<=r<=20` deliberately removes that issue. Selection after exploration is harmless for an exact existential counterexample, but is not a preregistered statistical comparison.
- **Frozen verification:** 183 integer orbit representatives, unit diameter, `beta=1/6`, annular center bounds `[10,20]`; golden indices `(4,12)`; 30-decimal rational square-root brackets; `pi<22/7`; no optimizer. Three negative controls, a six-center small-instance control, and exact Fibonacci algebra for indices 2 through 50. Diagnostics separately use 80 decimal digits, 21 asymptotic points `k=4..24`, 13 branch intervals `k=2..14`, and integer offsets `q=1..1000`. No holdout, generalization, or AI-performance claim.

## 2. Geometry and definitions

Let `C_beta` be the flat metric cone with polar coordinates `(r,theta)`, where `r>=0`, physical azimuth `theta` is modulo `2*pi`, and

`ds^2 = dr^2 + beta^2*r^2*dtheta^2`, `0<beta<=1`.

Its right-circular embedding has half-angle `alpha=asin(beta)`. Developing it gives a sector of angle `A=2*pi*beta`, with radial edges identified. Intrinsic distance is not the three-dimensional chord distance. If the minimal developed angular separation is `u=A*|| (theta_2-theta_1)/(2*pi) || <= pi`, the shortest path has

`D^2 = r^2+s^2-2*r*s*cos(u)`.

Here `||x||` denotes distance to the nearest integer. The path is the straight chord in the appropriate developed sector, except at degenerate apex cases; its angular change is at most `pi`. All pairs used below are nondegenerate and far from the apex. For `beta=1/6`, this is equivalently the quotient metric of the Euclidean plane by rotations through multiples of 60 degrees:

`D([z],[w]) = min_{j=0,...,5} |z-exp(i*j*pi/3)*w|`.

A disk means an **embedded intrinsic metric disk**, not a three-dimensional sphere touching the cone. It has area `pi*d^2/4` when its diameter is `d`. Finite comparisons constrain centers to `10<=r<=20`; disks of diameter at most 1 are contained in the physical frustum `9.5<=r<=20.5`. The metric is the ambient cone metric; the disks themselves do not leave that frustum.

A Fibonacci spiral is not defined by a visual impression here. The **fixed ansatz** uses `gamma=(3-sqrt(5))/2`, angles `theta_i=2*pi*i*gamma`, and an affine function of index for `r_i^2`. Offset `q` joins index `i` to `i+q`; in the infinite ordered index set it gives `q` residue-class chains. Local families are assigned from short offsets. The reduced model in Section 5 explicitly selects two shortest Fibonacci offsets. Arbitrary contact/Delaunay networks with Fibonacci counts form a larger class and are not classified by this work.

## 3. Finite certified counterexample: 183 centers

**Claim F.** The fixed-golden-angle configuration

`r_i^2=100+150*i/91`, `theta_i=2*pi*i*gamma`, `i=0,...,182`

is not a maximizer of minimum pairwise distance for 183 centers on `C_(1/6)` with `10<=r<=20`.

### 3.1 Competitor

Use the triangular lattice

`Lambda={a+b*exp(i*pi/3): a,b in Z}`,

whose squared norm is `Q(a,b)=a^2+a*b+b^2`. Rotation by 60 degrees acts as `(a,b)->(-b,a+b)` and preserves `Lambda`. Take one representative of each nonzero orbit satisfying

`100<=Q(a,b)<=400`.

The supplied witness has 183 representatives. Its sixfold lift contains 1098 distinct planar lattice points. For any two distinct lifted points, the squared distance is a nonzero integer of the form `Q(a,b)`, so it is at least 1. Some pairs have distance exactly 1. The same lower bound holds between distinct quotient centers. Points in the same orbit are not counted twice. The sixfold lifting also shows that each disk of radius `1/2` is embedded: the distance between distinct lifts of a single center is at least its slant radius, here at least 10. The radial triangle inequality places every disk in the specified frustum.

The count is reproducible by enumerating `-24<=a,b<=24`: the identity `Q(a,b)=(a+b/2)^2+3*b^2/4` and its symmetric counterpart imply `|a|,|b|<=sqrt(1600/3)<24` when `Q<=400`. No unenumerated lattice points satisfy the bound. The count is not needed for an optimality assertion about the lattice; it only matches the competitor and the 183-point golden configuration.

The independent verifier does not import the generator. It transforms a witness pair to scaled Cartesian coordinates `(X,Y)=(2a+b,b)`, representing `(X/2,sqrt(3)*Y/2)`, rotates using `(X,Y)->((X-3Y)/2,(X+Y)/2)`, and exhaustively checks the squared-distance numerator `(X-U)^2+3*(Y-V)^2` over every pair of lifts. Its minimum is exactly 4. Reflection `Y->-Y` also preserves the lifted witness.

### 3.2 Golden configuration obstruction

For indices `i=4` and `j=12`,

`r_i^2=a=9700/91`, `r_j^2=b=10900/91`,

and the fractional angular residual is

`8*gamma-3=9-4*sqrt(5)=delta`, with `0<delta<3/50`.

The developed angle is `x=pi*delta/3`, hence

`D^2=a+b-2*sqrt(a*b)*cos(x)`.

Let `L_5<=sqrt(5)` and `L_ab<=sqrt(a*b)` be the rational lower bounds produced by integer square roots at denominator `10^30`. Then

`x < U_x=(22/7)*(9-4*L_5)/3`,

and `cos(x)>=1-x^2/2>=1-U_x^2/2>0`. Therefore

`D^2 <= a+b-2*L_ab*(1-U_x^2/2) < 77/100 < 1`.

The final two comparisons are exact rational arithmetic, not floating-point tolerances. The rational upper bound is stored in `results/certificate.json`; its displayed decimal is approximately `0.7695431670071615`. The independent high-precision polar computation is approximately `0.769124117040865606`, but is not needed for the proof.

Thus the competitor permits unit-diameter disks, whereas the golden placement does not. Both sets have the same number of centers and the same radial bounds. The short offending chord and its midpoint are far inside the physical frustum, so this is not a boundary-clipping artifact. More directly, every point along that chord has radial distance at least `sqrt(a)*cos(x)>10`, since `a>106`, `x<0.063`, and `cos(x)>0.998`; its midpoint belongs to both radius-`1/2` balls.

This proves Claim F. It does not prove the unrestricted finite maximum separation is 1, nor that every point set with Fibonacci parastichy counts fails.

## 4. Bulk comparison, unaffected by any finite apex deletion

**Claim B1.** Fix `0<beta<=1`, `c>0`, and any integer `n_0>=1`. Put a center at

`P_n=(c*sqrt(n), 2*pi*n*gamma)`, for every integer `n>=n_0`.

If equal embedded intrinsic disks of diameter `d>0` around these centers do not overlap, their asymptotic area density is at most

`pi/(2*sqrt(5)) = 0.7024814731...`.

### Proof

Write `phi=(1+sqrt(5))/2` and Fibonacci numbers `F_0=0,F_1=1`. Induction using `phi^2=phi+1` gives

`F_k*gamma-F_(k-2)=(-1)^k*phi^(-k)`, for `k>=2`.

Also `F_k*phi^(-k)->1/sqrt(5)`, by Binet's formula (or by solving the Fibonacci recurrence). Set `q_k=F_k`, `epsilon_k=phi^(-k)`, `A=2*pi*beta`, and let `n_k` be the nearest integer to `q_k/(2*A*epsilon_k)`. Then `n_k->infinity`, `q_k/n_k->0`, and

`n_k / (q_k/(2*A*epsilon_k)) -> 1`.

For large `k` both indices `n_k,n_k+q_k` survive the finite deletion. Their separation satisfies the stable identity

`D_k^2/c^2 = (sqrt(n_k+q_k)-sqrt(n_k))^2 + 4*sqrt(n_k*(n_k+q_k))*sin^2(A*epsilon_k/2)`.

For the first term, rationalize the square roots:

`q_k^2/(sqrt(n_k+q_k)+sqrt(n_k))^2 -> A/(2*sqrt(5))`.

For the second, use `sin(u)/u->1` and `q_k/n_k->0`:

`4*sqrt(n_k*(n_k+q_k))*sin^2(A*epsilon_k/2) -> A/(2*sqrt(5))`.

Consequently `D_k^2/c^2 -> A/sqrt(5)`. Nonoverlap implies `d^2<=D_k^2` for every sufficiently large `k`, so

`d^2 <= 2*pi*beta*c^2/sqrt(5)`.

The number of centers within slant radius `R` is `R^2/c^2+O(1)`, and the cone disk has area `pi*beta*R^2`. Disks crossing the outer radius change the area sum only by `O(R)` (count centers in the radial shell `[R-d/2,R+d/2]`). Thus the limiting covered area fraction is

`density=d^2/(4*beta*c^2) <= pi/(2*sqrt(5))`.

Every step is an exact identity or elementary limit; the finite convergence table is only a control, not a proof of the limit. No assertion that the upper bound is attained is needed or made.

**Claim B2.** On `C_(1/6)`, the global maximal **upper asymptotic covered-area density** for equal embedded intrinsic disks is `pi/(2*sqrt(3))`. Here upper density means `limsup` as the centered cone-disk radius tends to infinity; an arbitrary packing need not have a density limit. The attaining construction below does have an ordinary limit.

### Proof

The quotient of `Lambda` by its 60-degree rotation symmetry, retaining only centers with `r>1`, packs embedded closed disks of radius `1/2`. Distinct lifts of one center have minimum separation `r>1`, so even the boundary of a single closed disk has no self-identification. Both the apex orbit and the unit-radius orbit are omitted: omitting only the apex would leave self-identification at two boundary points of a unit-radius center's disk. The planar fundamental parallelogram has area `sqrt(3)/2`, so the packing density is `(pi/4)/(sqrt(3)/2)=pi/(2*sqrt(3))`. Quotienting divides both disk counts and ambient area by six; bounded omissions change neither limit.

Conversely, lift any packing on this quotient cone to the plane. Outside a fixed apex neighborhood, embedded disks lift to six Euclidean disks, and the full collection has disjoint interiors. Their union is a planar packing. Centered-radius covered-area fraction is the same because area and counts both multiply by six. The planar equal-circle packing theorem bounds the `limsup` by `pi/(2*sqrt(3))`. Discarding the bounded apex region does not alter this bound. This proves B2.

B2 is an elementary application of the classical theorem, not a new packing constant. Combining B1 and B2 gives a strict separation: the triangular packing density divided by the golden-ansatz upper bound is `sqrt(5/3)>1`, approximately `1.2909944487`. This is a relative factor, not a percentage-point difference and not a claim to have computed the golden ansatz's exact density. The comparator is reflection-symmetric; its optimal density does not require a preferred handedness.

## 5. Chirality: what is established and what is not

### 5.1 Reflection degeneracy

**Claim S.** Suppose the admissible domain and boundary data are invariant under `(r,theta)->(r,-theta)`, and the energy depends only on intrinsic distances or other reflection-invariant quantities. For every disk diameter, reflection maps the set of global minimizers to itself. If a minimizer is chiral, a mirror minimizer with opposite chirality has exactly the same energy.

**Proof.** Reflection preserves `ds^2`, hence all distances, admissibility, and the stated energy. Apply it to a minimizer; any lower-energy reflected competitor would reflect back to a lower-energy competitor for the original minimizer. Reflection reverses signed winding. This argument also applies to a packing objective. It does not require a numerical experiment.

Thus scalar disk size alone cannot energetically prefer one absolute handedness in this achiral model. It can still change which *pair* of degenerate states occurs; a history-dependent branch can still alternate. The claim does not refute such alternation. Conversely, rescaling every length and the disks on an unbounded cone preserves the entire packing and its chirality, so size changes without a fixed external length scale do not compel any transition.

### 5.2 An exactly soluble local Fibonacci-family model

**Claim T (reduced, conditional model).** Let `t>0` and `A=2*pi*beta`. For each `k>=2`, define the squared local separation

`L_k(t)=F_k^2/(4*t)+A^2*t*phi^(-2*k)`.

This is the radial/tangential linearization of the golden spiral at radial index `t`, divided by `c^2`. It is taken here as the **definition of the reduced model**, not an equality to the finite cone's distance. Its candidate families are the Fibonacci offsets only. Define the two active parastichy families to be the two distinct `k` with smallest `L_k(t)`, with ties reported rather than arbitrarily assigned. Then the active unordered pair progresses through

`(F_2,F_3), (F_3,F_4), (F_4,F_5), ...`.

The signed winding of the family with `F_k` chains is `(-1)^k`, when direction is measured with increasing radius. Therefore the sign of the larger-count family changes at every consecutive pair transition. This observable matches the book's *relative parastichy* chirality convention, not ontogenetic chirality.

### Proof and exact thresholds

Multiplying by `t>0` converts the comparison to affine functions of `x=t^2`, with intercepts `F_k^2/4` increasing and slopes `A^2*phi^(-2*k)` decreasing. Neighboring functions cross at `t=tau_k`, where

`tau_k^2 = (F_(k+1)^2-F_k^2)/(4*A^2*(phi^(-2*k)-phi^(-2*(k+1))))`

`           = phi^(2*k+1)*F_(k-1)*F_(k+2)/(4*A^2)`.

The second equality uses `F_(k+1)^2-F_k^2=F_(k-1)*F_(k+2)` and `1-phi^(-2)=phi^(-1)`. These thresholds strictly increase for `k>=2`. For `tau_(k-1)<t<tau_k`, consecutive comparisons telescope to show `L_k<L_j` for every `j!=k`. For the initial interval `0<t<tau_2`, `L_2` is smallest.

In an interval where `k>=3` is smallest, every `j<k-1` has `L_j>L_(k-1)` and every `j>k+1` has `L_j>L_(k+1)`, by those same adjacent comparisons. The second-smallest family is therefore either `k-1` or `k+1`. Those two cross once, at

`sigma_k^2 = (F_(k+1)^2-F_(k-1)^2)/(4*A^2*(phi^(-2*(k-1))-phi^(-2*(k+1))))`, `k>=3`.

This squared threshold is a strictly weighted average of `tau_(k-1)^2` and `tau_k^2`, with weights given by the positive consecutive slope differences. Hence `tau_(k-1)<sigma_k<tau_k`, and the `sigma_k` are strictly increasing. Set `sigma_2=0`. The two smallest families are `(k,k+1)` for `sigma_k<t<sigma_(k+1)`, including `k=2`. At `sigma_k` the shortest family is `k`, and the two possible second-shortest families tie; the chirality assignment is therefore not unique exactly at the transition.

The residual identity from Section 4 gives opposite winding signs for adjacent offsets. For pair `(k,k+1)`, the larger count is `F_(k+1)` and its sign is `(-1)^(k+1)`, proving alternation. At fixed physical radius `r`, choosing a scale `c` gives `t=(r/c)^2`; changing `c` monotonically crosses the same thresholds in reverse order. If a disk diameter is assumed proportional to `c`, the conclusion transfers conditionally to that rescaled ansatz. Diameter proportionality is an assumption, not a solved growth law.

A scan that skips an even number of transitions can show no sign change. At a tie no unique larger-family sign is selected. A reflected seed reverses every sign. Non-Fibonacci branches or defects are outside this restricted model. Therefore this result supplies a checkable mechanism and transition criterion, **not** a universal answer to C2.

## 6. Evidence, novelty, and verification ledger

| ID | Evidence label | Exact claim and novelty status | Verification | Review disposition |
|---|---|---|---|---|
| F | Certification | Finite 183-point strict counterexample to the fixed golden ansatz. Novelty not established; commensurate lattice construction is known. | `python code/verify.py`; proof in Section 3 | Reviewer independently reconstructed and accepted the witness and rational bound. |
| B1 | Certification | Upper density bound for a fixed golden Fermat spiral on a cone after arbitrary finite prefix deletion. Elementary continued-fraction/local-linearization corollary; no priority claim. | Section 4 proof; `python code/diagnostics.py` controls the formula, not its universal quantifier | Accepted; finite deletion and boundary-shell argument checked. |
| B2 | Certification | Global upper asymptotic density for the 60-degree quotient cone. Classical planar packing theorem plus lifting, not a new optimum. | Section 4 proof; finite lattice checked by `python code/verify.py` | Accepted with boundary and density-definition corrections, both applied. |
| S | Certification | Reflection degeneracy for an explicitly achiral model. Standard symmetry argument, no novelty claim. | Section 5.1 proof; witness reflection checked by `python code/verify.py` | Accepted with the existing physical-scope caveat. |
| T | Certification | Consecutive pair transitions and relative-chirality alternation in the specified Fibonacci-family linearized model. Standard phyllotaxis mechanism, not novel physical selection. | Section 5.2 proof; 49 exact algebra controls in `python code/verify.py` | Accepted; weighted-average threshold identity checked. |
| E | Empirical evidence | Independent polar pair value, 21 large-index limits, and one sampled point in each of 13 analytically specified phases, checking offsets 1..1000. No interval-wide numerical verification. | `python code/diagnostics.py` | Accepted with sample-coordinate clarification, applied. |

Actual command run from this folder:

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/reproduce.py
```

Observed output:

```text
GENERATED: 183 orbit representatives
PASS: N=183, 1098 planar lifts, exact minimum distance squared=1
PASS: golden pair (4,12) squared distance < 0.77 (rational upper bound approx 0.769543167007)
PASS: 6-orbit control; reflection; 3 rejected negative controls; 49 Fibonacci identities
EMPIRICAL: golden pair squared distance=0.769124117040865606
EMPIRICAL: density upper bound=0.7024814731040726, lattice=0.9068996821171089
EMPIRICAL: 21 asymptotic controls; 13 consecutive chirality phases, q=1..1000
```

The finite verifier uses only Python integer arithmetic and `fractions.Fraction`; floating values are printed after certification and never decide acceptance. Its negative controls reject a repeated orbit, an exterior point `(25,0)` outside the allowed annulus, and diameter `101/100`. The exterior-point control was strengthened after review: unlike an apex point, it has six distinct lifts and would otherwise pass the distance check, so it specifically exercises the radial constraint. Generator and verifier share the mathematical lattice definition, but use different coordinate representations and share no implementation functions. The mpmath check uses a stable sine-squared polar distance formula rather than the verifier's cosine lower bound. Each reported phase interval is analytic; only its recorded `sample_t` is numerically tested, against Fibonacci indices 2..24 and integer offsets 1..1000. Both codes run under the same Python runtime; they are not formal kernel verification.

## 7. Independent review

The saved prompt is `review/codex-prompt.md`; the immutable response is `review/codex-review.md`. The run used Codex CLI 0.162.1, model `gpt-6.1-sol`, reasoning effort `max`, read-only sandbox, ephemeral session, no web, and a 3600-second command timeout. It exited 0. `review/codex-stderr.log` records the actual identity; `review/receipt.json` binds the reviewed input hashes. The original response remains unchanged after corrections.

**Reviewer verdict: correct-with-fixes.** It independently reconstructed the 183 orbits/1098 lifts, the finite rational upper bound, diagnostic constants and sampled phases. It accepted F, B1, S and T and accepted B2 with the explicit repair below. All findings were examined:

1. **Closed-disk boundary self-identification in B2 — accepted and fixed.** At a center `z=1`, the boundary points `(1+exp(+-i*pi/3))/2` are related by the quotient rotation. They are distinct before quotienting. The construction now retains `r>1`, not merely nonzero centers. Then self-image separation is strictly greater than the diameter. This removes finitely many centers and leaves the density unchanged.
2. **Density may not have a limit for arbitrary packings — accepted and fixed.** B2 now uses upper covered-area density (`limsup`). The triangular construction has an ordinary limit; the lifting upper bound applies to the `limsup`. B1's limit already exists by its explicit counting formula.
3. **One sample per phase, not an interval-wide scan — accepted and fixed.** Diagnostics now store `sample_t`, label the interval as analytically derived, and record both finite scan ranges. No new numerical scan was claimed as proof.
4. **F independent reconstruction — confirmed.** The referee supplied a separate quotient-center distance calculation and found a unit-separated pair at lattice representatives `(-10,0)` and `(-11,0)`, both in the annulus. Its rational expression agrees with the stored certificate.
5. **B1/B2 proof assessment — confirmed.** The radial and tangential limits each equal `A/(2*sqrt(5))`; the density ratio is against an upper bound, not an attained golden density. B2's corrected construction and lifting argument are the ones the referee expressly endorsed.
6. **S/T proof assessment — confirmed.** The pair-crossing squared threshold is a positive weighted average of adjacent squared thresholds. Reflection does not prohibit history dependence, and T does not prove all-offset or physical-growth selection.
7. **Citation/scope assessment — retained with limitation.** The referee found no statement exceeding its declared reading level but did not independently fetch external sources. It is not literature verification or novelty clearance.

The proof correction and reporting fixes were applied by the author, not by the read-only referee. The final changed-path reproduction was rerun after these corrections; the output is the same transcript displayed above. The proofs are not considered formally kernel-certified merely because a model agrees.

## 8. Exact remaining blocker and next action

Nothing here establishes that the actual Ag/silica experiments reach global elastic minima, or that every Fibonacci-contact packing is inferior. A full answer requires the strain/bending/substrate energy, geometry and stress history, defect costs, boundaries, and allowed rearrangements. A scalar Riesz energy or intrinsic hard-disk model is not automatically that functional. No sequential packing experiment has been substituted for a proof of C2.

The single most valuable next action is to obtain or derive the experimental bilayer elastic functional and a mathematically explicit Fibonacci-contact competitor class, then certify an energy comparison with a seam-bearing crystal at an experimental cone angle. Until that contract is fixed, more unconstrained numerical searches would answer a different question rather than close this blocker.

## 9. Approved scoped target: sharp tail separation and density

**Verdict: ALREADY-SOLVED density mechanism; Certification of an elementary cone-tail transfer.** Theorem 1(2), equation (12), of [Graiff Zurita–Kane–Oishi-Tomiyasu, arXiv:2106.12333v8](https://arxiv.org/html/2106.12333v8) already gives the Lagrange-spectrum density law for deformed lattices. The golden limiting spacing is also explicit in [Sadoc–Rivier–Charvolin 2012, §IV.3](https://arxiv.org/html/1201.1432v2). This continuation does not count as solving a previously open selection.

### 9.1 Exact statement

Fix `0<beta<=1`, `c>0`, `alpha in R`, and put `P_n=(c*sqrt(n),2*pi*n*alpha)` for integers `n>=1` on the intrinsic cone of §2. Define

`s_N=inf_(m>n>=N) D(P_n,P_m)`, `d_tail=lim_(N->infinity) s_N`,

`mu(alpha)=liminf_(q->infinity) q*||q*alpha||`.

The limit defining `d_tail` exists because `s_N` is nondecreasing. Then

`d_tail^2=2*pi*beta*c^2*mu(alpha)`.

Include diameter zero as a convention when taking the supremum over equal embedded disks centered at every point of some tail. That supremal covered-area density is

`Delta_sup(alpha)=pi*mu(alpha)/2`.

Every `0<d<d_tail` is feasible after some finite prefix deletion; no `d>d_tail` is feasible. Equality need not be feasible. If `mu=0`, no positive diameter works on any tail. The maximum of these **supremal densities**, as a function of divergence, is the classical `pi/(2*sqrt(5))`, achieved as a value of `Delta_sup` at a golden divergence. This does not assert that a physical packing attains the endpoint density.

### 9.2 Exact geometric lower bound

Write `A=2*pi*beta`, `q=m-n`, `epsilon=||q*alpha||`, `u=A*epsilon`, and `h=2*n+q`. The cone-distance formula gives

`D^2/c^2 = h-cos(u)*sqrt(h^2-q^2) = F_q(h,u)`, with `0<=u<=pi`.

For `0<=u<=pi/2`, Cauchy–Schwarz applied to vectors `(cos(u),sin(u))` and `(sqrt(h^2-q^2),q)` gives the **exact** lower bound

`F_q(h,u)>=q*sin(u)`.

For `pi/2<=u<=pi`, `F_q(h,u)>=h>=q`. These are inequalities for actual distances, not for a linearized model. When `0<u<pi/2`, equality in the first bound occurs at the continuous radius parameter `h_*=q/sin(u)`.

Suppose `alpha` is irrational and a sequence of pairs with `n->infinity` has bounded `D^2`. The radial inequality `D/c>=sqrt(n+q)-sqrt(n)` implies `q=O(sqrt(n))` and `q/n->0`. The stable distance formula then implies `epsilon->0`: its angular term is `4*sqrt(n(n+q))*sin^2(A*epsilon/2)`, and the sine argument lies in `[0,pi/2]`. Moreover `q->infinity`, since any finite nonzero set of offsets has a strictly positive minimum residual for irrational `alpha`. Thus along every such bounded sequence,

`D^2/c^2 >= A*q*epsilon * sin(A*epsilon)/(A*epsilon)`,

so its `liminf` is at least `A*mu(alpha)`. If a tail infimum were smaller, choosing pairs within `1/N` of the infimum for each `N` would give precisely a bounded sequence contradicting this bound. This proves the lower inequality; when `mu=0` it is simply nonnegativity.

### 9.3 Matching upper bound, including zero and rational cases

For irrational `alpha`, choose `q_j->infinity` with `q_j*epsilon_j->mu(alpha)`. Such a subsequence with bounded products exists by Dirichlet's approximation theorem; hence `epsilon_j->0`. Choose `n_j` to be the nearest integer to `q_j/(2*A*epsilon_j)`. Then `n_j->infinity`, `q_j/n_j->0`, and `n_j/(q_j/(2*A*epsilon_j))->1`. Rationalizing the radial term and using `sin(x)/x->1` gives

`D(P_(n_j),P_(n_j+q_j))^2/c^2 = A*q_j*epsilon_j*(1+o(1)) -> A*mu(alpha)`.

The relative estimate is valid even when `mu=0`: each of the two nonnegative terms divided by `A*q_j*epsilon_j` tends to `1/2`. Both indices survive every fixed prefix deletion. This proves the upper inequality. For rational `alpha=a/b`, use the fixed offset `q=b`: the angle residual vanishes and

`D(P_n,P_(n+b))^2/c^2 = b^2/(sqrt(n+b)+sqrt(n))^2 <= b^2/(4*n) -> 0`.

Also `mu(alpha)=0` because all multiples of `b` have zero residual. The exact identity therefore covers every real divergence.

### 9.4 Embedded disks, density and endpoint

For fixed `beta>0`, an embedded Euclidean disk of some radius `kappa_beta*r` exists about every point of slant radius `r`, with `kappa_beta>0`: develop a sufficiently small neighborhood of a point at `r=1`, then use cone homothety and rotational symmetry. Therefore, after a finite prefix deletion, all disks of any prescribed finite diameter are embedded, including their boundaries. This argument works for arbitrary cone angles; it does not pretend that every cone is a finite rotation quotient.

For `d<d_tail`, some `s_N>d`, so disks have disjoint interiors after also imposing the embedding cutoff. Their ordinary covered-area density exists and equals `d^2/(4*beta*c^2)` by the exact radial counting law and the `O(R)` boundary-shell estimate of §4. Conversely, feasible diameter `d` implies `d<=d_tail`. Taking a supremum proves the density formula. For `mu=0` the diameter-zero convention gives supremum zero; it is not a positive-radius packing.

Hurwitz's sharp theorem gives `mu(alpha)<=1/sqrt(5)` for irrational `alpha`. At the golden divergence `gamma`, the Fibonacci products approach `1/sqrt(5)`. For the matching lower bound, if `p` is nearest to `q*gamma` and `delta=q*gamma-p`, the nonzero integer

`(q*gamma-p)*(q*(3+sqrt(5))/2-p)=q^2-3*p*q+p^2`

has absolute value at least 1. Hence `1<=sqrt(5)*q*|delta|+delta^2`; on a bounded-product subsequence `delta->0`, proving `mu(gamma)>=1/sqrt(5)`. Thus varying a constant divergence cannot improve the golden supremal density, and cannot reach the `pi/(2*sqrt(3))` triangular density of the commensurate cone.

The golden endpoint is **not attained on any tail**. For even Fibonacci index `k`, set `q=F_k`, `epsilon=phi^(-k)`, so `q*epsilon=(1-epsilon^2)/sqrt(5)`. At the continuous minimizer, `F_q(h_*,u)=q*sin(u)<A*(1-epsilon^2)/sqrt(5)`. Choose the allowed integer `h=2*n+q` nearest to `h_*`, so `|h-h_*|<=1`. For `u<=1/4`, `h_*>=4q`; along this unit interval `sqrt(h^2-q^2)>=h_*/4`. Since

`d^2 F_q/dh^2 = cos(u)*q^2/(h^2-q^2)^(3/2)`,

Taylor's theorem bounds the rounding increase by `32*sin(u)^3/q <=32*A^3*epsilon^3/q`. This is smaller than `A*epsilon^2/sqrt(5)` whenever `160*A^2*epsilon^2<1-epsilon^2`, which holds for all sufficiently large even `k`. The resulting integer-index pair has **normalized** squared distance `D^2/c^2` strictly below `A/sqrt(5)` (equivalently, `D^2<c^2*A/sqrt(5)`), and its indices tend to infinity. Every tail therefore contains an overlap at the endpoint diameter. No finite convergence table establishes or is needed for this conclusion.

### 9.5 Proof controls and review boundary

The lower-bound identity can independently be checked by expanding
`(h-C*w)^2-q^2*S^2=(w-C*h)^2` under `w^2=h^2-q^2`, `C^2+S^2=1`; for `C,S>=0` it gives the same lower bound. The rational-offset identity above is an exact negative control against a positive-density formula for rational divergences. The even-Fibonacci construction is an infinite negative control against confusing supremum with attainment. These are written exact arguments, not numerical certificates of an infinite assertion. Independent review of this addendum is saved separately under `review/tail-*`; the initial review and receipt remain historical evidence.

The additional standard-library-only command

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/verify_tail.py --write
```

ran successfully and printed:

```text
PASS: exact Cauchy equality and false-linearization negative control
PASS: rational-divergence zero-tail control
PASS: golden endpoint rounding bounds for every even k>=10 and 0<beta<=1
```

`results/tail-controls.json` stores the exact fractions. At `h=5,q=3,C=4/5,S=3/5`, the distance expression equals `9/5=q*sin(u)` with `u=arcsin(3/5)>3/5`, so the stronger finite inequality `D^2/c^2>=A*q*epsilon` would be false. This is why the lower proof takes a limit. For endpoint rounding, `phi>8/5` and `A<44/7` imply the sufficient conditions uniformly for every even `k>=10`; the two required rational inequalities are checked without floating-point decisions. No infinite statement is inferred from merely sampling Fibonacci values.

### 9.6 Independent addendum review

`review/tail-review.md` records a separate read-only Codex `gpt-6.1-sol:max` review (CLI 0.162.1, exit 0). Its verdict was **correct-with-fixes**. Finding 1 identified a missing `c^2` in the final wording of the golden endpoint paragraph; the preceding derivation was normalized throughout. The sentence now explicitly states `D^2/c^2<A/sqrt(5)`. Findings 2–6 accepted, respectively, the arbitrary-cone lower bound, matching upper bound including both zero cases, embedding/density supremum, golden extremality, and endpoint rounding constants. Finding 7 accepted the limited scope and stipulated prior-art classification, without independently authenticating external sources. All findings are accepted; there is no remaining mathematical correction requested by that review. The initial cone review and all original artifacts remain unchanged. This written argument and model review are not a formal kernel proof.
