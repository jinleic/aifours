# Independent-input lift and the canonical adapted-input obstruction

**WRITTEN, UNREVIEWED; elementary coupling result and exact failed implication.** Actual native prewrite clock: **Tue Oct 27 14:51:48 PDT 2026**. New append-only continuation of `prerequisite-derivation-v1.md` (SHA-256 `f38fa78a0d1747771dbcafd18320cc593c1a90faf25fa6b862d52754f9097672`), not a repair or an expansion of its noise-free conclusion. The same pre-body ACK/input boundary applies. No new source, program, selected arithmetic, controller realization or energy method is used.

## 1. Problem and actual-object boundary

Keep the exact dimensions/matrices, original output, horizon/zero-extension, zero initial condition, deterministic full-information law and progressive E2 interpretation stated in v1, but now allow arbitrary A0 and B0. Let E=L2(J) be the separable Hilbert space of full disturbance paths, and let Omega_W be the canonical continuous Brownian path space through the relevant horizon (compact-open topology on the infinite horizon), with Wiener probability P.

For a fixed law F and a deterministic input v, suppose the physical problem has a well-defined output Z_F(v) and write

`e_F(v)=E_P ||Z_F(v)||_I`.

No universal pathwise stochastic solution map is presumed just from these separate deterministic-input solutions. When using a joint nonnegative measurable functional `f_F(v,omega)`, there are TWO distinct physical caller obligations:

- **Product caller:** f_F represents the actual original output norm for independently randomized input v and Brownian path omega. Joint measurability and a parameterized strong well-posed solution/lift are required, not inferred solely from separate almost-sure deterministic-input identities.
- **Adapted caller:** for the actual canonical input V=Phi(W), one must additionally establish that `f_F(Phi(W),W)` is the actual output norm for that coupled input. Product-a.e. identification alone does not establish this.

The lemmas below are elementary for a given f. Application to the original physical plant is conditional on the respective actual caller; no artificial response functional is passed off as a realizable controller or plant output.

## 2. Exact independent-mixture lift

Let f:E x Omega_W->[0,infinity] be measurable, put `e(v)=integral f(v,omega) P(domega)`, and assume e(0)=0. Define the deterministic-input expected-norm threshold

`H=sup_(v!=0) e(v)/||v||`.

Let mu range over all input-path distributions with `integral ||v||^2 mu(dv)<infinity` and `integral ||v|| mu(dv)>0`, independently coupled to W. Tonelli gives

`integral f d(mu x P)=integral e(v) mu(dv)`.

Therefore

**Theorem B.** The supremum of the independent-mixture expected-norm ratios equals H, including H=0 and H=infinity. Pointwise-strict feasibility at gamma is likewise equivalent to e(v)<gamma||v|| for every nonzero deterministic v, with e(0)=0. Uniform-strict feasibility requires H<gamma instead. These assertions preserve the identical common law F whenever the product caller holds.

Proof: if H is finite, e(v)<=H||v|| for all v including zero, hence integrate the inequality. Deterministic point-mass mu give the reverse supremum inequality. If H is infinite, those point masses already give an unbounded supremum. For pointwise strictness the integrable nonnegative difference gamma||v||-e(v) is positive on the positive-mu-measure set of nonzero inputs; its integral is positive. No attained maximizer or common strict margin is needed.

If e(0)>0, independent randomization between zero and any nonzero deterministic input, with nonzero-input probability tending to zero, makes the independent-mixture supremum infinite. This is a statement about the **comparison independent-mixture model**. To realize nontrivial independent input paths probabilistically, one may use a product extension with input and Brownian histories; this is NOT an assertion that such extra initial randomness is part of the original canonical controller/disturbance model. On the canonical Brownian space itself, an input both measurable with respect to the entire Brownian path and independent of it is almost surely deterministic.

Thus testing deterministic disturbances is sufficient for this independent comparison, but it has not yet addressed the original adapted disturbances.

## 3. A density bridge, and exactly what it would require

For a joint law Q of (V,W) with first marginal mu, suppose a finite constant M satisfies the measure domination

`Q <= M (mu x P)`.

If the adapted caller for the physical response holds and e(v)<=H||v||, then elementary integration of nonnegative functions gives

`E_Q f <= M integral f d(mu x P) <= M H E_mu ||V||`.

This is only a conditional bridge. It neither proves the domination for an adapted input nor gives sharp physical performance. An unbounded density gives no finite M by this argument. The original deterministic-input expected bound is an average over P, not a pointwise-in-W bound.

The next result precisely characterizes this proposed coupling premise on the canonical probability space. It is all-input-law, not a chosen plant/state probe.

## 4. Graph-law theorem for every canonical adapted input

An original canonical progressive E2 input is, as a full E-valued random variable, measurable with respect to the full Brownian path. Up to null sets write V=Phi(W), with a measurable version Phi on the standard Borel Wiener space. This uses separability of L2 and the ordinary measurable-factorization fact for canonical random variables. Let mu be the law of V, R=mu x P, and Q the joint law of (Phi(W),W).

Let D={v:mu({v})>0}, the at-most-countable set of atoms. Let Gamma be the measurable graph `{(v,omega):v=Phi(omega)}`.

**Theorem C (exact atomic/continuous decomposition).**

1. On values outside D, the graph has R-measure zero but Q-measure `mu(E\D)`. Consequently if mu has a nonzero nonatomic component, Q is not absolutely continuous with respect to R. If mu is entirely nonatomic, Q and R are mutually singular.
2. On the atomic part, enumerate atoms v_i with masses p_i>0. The absolutely continuous part of Q has R-density

   `r(v,omega)=sum_i 1_(v=v_i) 1_(Phi(omega)=v_i) / p_i`.

   Its total mass is `sum_i p_i`. There is no additional absolutely continuous part on nonatom values.
3. Hence Q is absolutely continuous with respect to R iff mu is purely atomic. A finite domination constant M exists iff mu has **finite support**; its least possible value is `1/min_i p_i`. An infinite atomic law has an unbounded density and no finite domination constant.

**Proof.** For each omega, the R-conditional mass of its graph point is `mu({Phi(omega)})`. On nonatom values this is zero. Tonelli therefore makes that portion of the graph R-null, while the actual joint law puts mass `P(Phi(W) notin D)=mu(E\D)` on it. This is a singular component, proving item 1.

For a nonnegative measurable test function g, integrate the displayed r against R. Its i-th term is

`p_i (1/p_i) integral_(Phi(omega)=v_i) g(v_i,omega) P(domega)`,

which equals the Q integral on {V=v_i}. Summing the countable nonnegative terms proves item 2. Each displayed nonzero density level 1/p_i occurs on an R-set of positive measure. The density is bounded iff the positive atom masses are bounded below, which for a probability law is equivalent to finitely many atoms. Combine with item 1 to prove item 3. No probability values, plant parameters or numerical witness were selected.

The theorem includes degenerate deterministic input laws (one atom), countably infinite atomic laws and mixtures with a nonatomic component. It does not require control/state integrability beyond the definitions needed to make V an E-valued random variable.

## 5. Second obstruction: separate versions do not identify the diagonal caller

When mu is nonatomic, each fixed deterministic slice Gamma_v has P-measure `P(Phi(W)=v)=mu({v})=0`. Thus a property that holds almost surely for **every separately fixed v** can still fail everywhere on the actual graph of the random input, which has Q-measure one. This is the precise invalid interchange of quantifiers: `for each v, for P-a.e. omega` does not imply `for P-a.e. omega, at v=Phi(omega)`.

In particular, a product-a.e. measurable version of a family of deterministic-input stochastic responses can be altered on that graph without changing any deterministic-input almost-sure statement. This observation does NOT license changing a physical output. It proves only that deterministic-input versions do not identify the actual coupled-input response on the graph. The original stochastic equation and a lawful common solution/lift must identify it separately.

In v1's noise-free theorem this caller was explicitly secured by robust deterministic pathwise well-posedness and the samplewise ODE lift. There was no product-null stochastic-integral version step. For the general A0/B0 plant, I do not assert an analogous universal solution map from unsupplied regularity or imports.

## 6. Consequence for the literal synthesis inference

The proposed inference

`deterministic-input expected-norm bound -> condition on entire progressive input -> same Wiener average -> original adapted literal bound`

has two exact unpaid steps:

- **NR-COUPLING:** conditioning on the entire adapted input generally does not leave the Brownian law equal to P. The graph-law theorem shows no finite product-law domination at all for nonatomic canonical inputs, not merely a missing numerical constant.
- **NR-DIAGONAL:** deterministic-input a.s. response identities do not themselves identify the response at a random input sharing the same Brownian path.

These are obstructions to that proof route, **not** a physical counterexample to a correctly stated synthesis theorem. Singularity alone does not force a large gain; v1's noise-free reduction demonstrates that a structural pathwise bound can avoid needing any density estimate. No general noisy-plant condition is refuted merely from measure singularity.

What is changed: the independent-mixture reduction is proved exactly and the attempted extension to the original adapted domain has an explicit, all-law obstruction and an actual-object version gap. What remains OPEN: a legal structural mechanism that pays the coupling/diagonal requirements for the full noisy original plant and one common controller, or an actual original-scope obstruction. The supplied S2 definitions alone do not contain such a theorem.

## 7. Imports, STOP and next prerequisite

Named ordinary facts used: Tonelli for nonnegative measurable functions, strict positivity of integrals, regular measurable factorization on standard Borel canonical path spaces, countability of atoms of a probability measure, and the definition of absolute continuity/singular decomposition. No Girsanov/change-of-measure theorem, stochastic-flow identity, stochastic-integral construction, Riccati/storage/Gramian or controller realization is imported. The physical joint solution/lift is an explicitly unpaid premise, not a named external theorem silently assumed.

The branch that would certify the general physical diagonal response or convert it into a controller is **STOPPED at NR-DIAGONAL/NR-COUPLING**, rather than supplied with an invented import or a legacy method. A next source/written disposition must either provide a safely stated joint well-posedness/coupling prerequisite for a specified original controller class, or authorize another elementary original-object obstruction. It cannot revive any C1–C3/R4/v209 or ZERO guidance. The unrelated NR-SOURCE/book-equivalence limit also persists. All findings and HOLD/N4 UNKNOWN/aux214 STOP remain; no source/model CLI/compute/selected check or stronger acceptance occurred.
