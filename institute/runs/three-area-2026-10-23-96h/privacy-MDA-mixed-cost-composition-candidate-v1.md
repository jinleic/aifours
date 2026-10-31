# Planar additive DP: a conditional mixed-cost composition

Parent clock last observed before writing: **2026-10-27T09:07:47-0700 PDT**, when [scope v252](privacy-MDA-mixed-cost-composition-parent-scope-v252.json) was frozen. This is a **new parent-written, UNREVIEWED candidate**, not an adoption or a claim that all initial reasoning was preregistered. No selected-parameter diagnostic, numerical root or scientific execution is used.

## Claim and exact inputs

Fix any finite `epsilon>0` and the full closed diamond `D={z:||z||_1<=1}`. Let `P_D` be **all Borel probability laws** satisfying the additive pure-DP shift inequality for every Borel event and every shift in `D`. Put

`V = inf_{mu in P_D} E_mu ||Z||_2²`,
`V1 = inf_{mu in P_D} E_mu ||Z||_1²`.

**Candidate theorem, conditional on the named adopted inputs below:**

1. `V <= (2/3)V1` for every finite `epsilon>0`.
2. Equality holds exactly when the unique Euclidean optimizer has a full diamond core. On that side, every feasible law satisfies `E||Z||_2² >= (2/3)V1`, with equality **only as a law** at the unique Euclidean optimizer `mu_*`.
3. With the separately adopted v241 threshold, equality holds exactly for `epsilon<=epsilon_t`; for `epsilon>epsilon_t` the inequality is strict in the opposite direction: `V < (2/3)V1`.
4. On the diamond side, `mu_*` itself is an all-law minimizer of the `l1²` cost. Any `D`-radial `l1²` minimizer is the same law `mu_*`. No uniqueness is claimed for arbitrary nonradial `l1²` minimizers.

**Named inputs and nonclaims.** [LAW642](privacy-all-law-self-contained-parent-v1.md) supplies a unique all-law squared-Euclidean optimizer for this same model. The separate [MDA26 per-cost theorem](privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md) supplies an actual `D`-radial staircase attaining the all-law infimum for the **matching-norm** cost `phi(r)=r²`. The [v241 separated threshold](privacy-v241-separated-threshold-and-norm-gap-entire-parent-v1.md) identifies the diamond/rounded regimes at its LAW642/NORM148 inputs. All three remain at their actual same-harness written import boundaries; their ordinary foundations are not newly formalized here.

This composition does **not** show that MDA26 alone proves the mismatched Euclidean-cost optimum. It uses LAW642's all-law Euclidean optimum and uniqueness. It does not authenticate an omitted publication version, establish worldwide source equivalence or priority, prove a nonadditive channel result, evaluate the root, or excuse any process violation. The original threshold-v2 manuscript and v214-A verdict remain HELD under [v227](privacy-v214-selected-input-checks-process-quarantine-v227.json); their selected checks and every consumer remain ZERO.

## Written argument

### 1. Model match and existence

`D` is a compact centrally symmetric genuine norm ball with nonempty interior. Its gauge is `||z||_1`, and `phi(r)=r²` is nonnegative and nondecreasing. MDA's per-cost theorem therefore applies to exactly `P_D` and supplies an actual feasible `D`-radial staircase law `nu1` satisfying `E_nu1 ||Z||_1²=V1`. A product Laplace law is feasible with finite squared cost, so `V1<infinity`; the supplied staircase minimizer also has finite cost. No assertion about all other `l1²` minimizers is used.

### 2. The radial identity

For any `D`-radial density `f(||z||_1)`, on each quadrant write `z=(r(1-t),rt)`, with the appropriate coordinate signs, `r>0` and `0<t<1`. The absolute Jacobian is `r`. The radial factor depends only on r, and

`integral_0^1 [(1-t)²+t²]dt = 2/3`.

Tonelli or truncation gives `E||Z||_2²=(2/3)E||Z||_1²`, including extended values. This is a **radial-law identity**, not a pointwise identity for arbitrary z or a statement about arbitrary nonradial laws.

### 3. Universal comparison

The MDA minimizer `nu1` is a legal competitor for `V`, so

`V <= E_nu1 ||Z||_2² = (2/3)V1`.

If equality holds, `nu1` attains the original Euclidean infimum. LAW642's uniqueness of the optimum as a probability law gives `nu1=mu_*`, hence `mu_*` is `D`-radial. The adopted core/homothety criterion then forces its actual core to be a full diamond. This direction uses actual attainment of `nu1`, not an unattained infimum or a presumed uniqueness of `l1²` minimizers.

### 4. Diamond side and equality

Conversely, if the optimal core is a full diamond, LAW642 gives a `D`-radial `mu_*`. For every feasible `D`-radial law `nu`, LAW642's all-law Euclidean optimality and the radial identity give

`(2/3)E_mu_* ||Z||_1² = V <= E_nu ||Z||_2² = (2/3)E_nu ||Z||_1²`.

Thus `mu_*` minimizes `l1²` on the radial subclass. MDA supplies a radial all-law minimizer, so the radial subclass has the same `l1²` infimum as all of `P_D`. Therefore `V=(2/3)V1`, and `mu_*` is itself an all-law `l1²` minimizer. If another `D`-radial law has `l1²` cost `V1`, its Euclidean cost is V, so LAW uniqueness makes it `mu_*` as a law. For any feasible law, radial or not, LAW gives `E||Z||_2²>=V=(2/3)V1`, with equality only at `mu_*`.

### 5. Threshold and residual

The accepted v241 separated proof says the core is a full diamond iff `epsilon<=epsilon_t`, including equality; it is rounded otherwise. Applying the preceding equivalence gives all candidate conclusions. Above the threshold, the actual optimum itself witnesses the strict inequality `V<(2/3)V1`; that is an assertion about an adopted law, not a selected numeric test or a new finite witness.

## Review and process boundaries

This candidate and its complete hypothesis-matched composition require a separately frozen written review and parent disposition. It cannot retroactively expand v241, whose frozen packet did not include the MDA per-cost theorem. The prior author/parent/reviewer findings, [v227](privacy-v214-selected-input-checks-process-quarantine-v227.json), [v242](v241-parent-preACK-privacy-topic-disclosure-qualified-release-v242.json), all ZERO quarantines, HOLD, N4 UNKNOWN with historical child exit unestablished, auxiliary214 STOP, original science cutoff and delivery deadline remain. No formal/kernel/human/configured-family/executable/novelty or round-closeout claim.
