# R-minus nonbalanced membership: an exact overlap budget and all-prior curvature barrier

Owner `InfoGuessingRminus`, info-5. Actual `/bin/date` before this freeze: `Sun Oct 25 04:13:16 PDT 2026`.

**WRITTEN CANDIDATE ONLY. No scientific computation, interpreter/eval, enumeration, symbolic/numerical execution, or replay was performed for this packet.** It follows the binding permission correction `noncoordinate-subcode-probe-ADDENDUM-1.md`, SHA256 `1f7bdee73415987af385c508749a9fffcd1461e51a7b36682d5e4c9ef4cf6ecf`. Earlier observed eval operations remain preserved but have no admitted execution-verification credit.

This is a substantive continuation of the next representation in `noncoordinate-subcode-probe-barrier-v1.md`, SHA256 `829befa8909eeeb43f4651baf91b2f8036541625898300eb458e78f39e4a249a`. It closes an additional all-amplitudes family of NONbalanced membership probes, without assuming uniform singleton marginals or Phi minimization. The interval remains `20/3 <= gn(R-minus) <= 1847/276`.

## 1. Exact new outcome

Let B be ANY nonconstant binary function of a finite graph law X, and let every finite W be generated stochastically from B. For each vertex put

`delta_i = TV(law(X_i|B=1), law(X_i|B=0))`.

Then, with NO graph/algebraic/uniformity assumption needed,

`3 I(W;X)-2 sum_i I(W;X_i)`

`>= [3-2 sum_i delta_i] I(W;X)`.                            (O)

Consequently, if `sum_i delta_i<=3/2`, **every** finite auxiliary in this noncoordinate membership family passes HC, at every noise amplitude and every number of output labels. This is a sufficient obstruction, not a necessary-and-sufficient characterization and not a new general guessing-number bound.

For a literal uniform code C with N words, a nonempty proper subset S of m words, ambient coordinate counts f_(i,z), and selected counts n_(i,z), define the exact integer

`D(S)=sum_(i,z) |N n_(i,z)-m f_(i,z)|`.

The complete finite-count certificate for (O) is

`D(S)<=3m(N-m)`.                                           (OC)

No logarithms, root approximations, or a scientific run are needed to state or prove this certificate. Any useful membership event MUST violate (OC). It must additionally have a changed-prior aggregate squared-correlation budget exceeding3/2, as derived in Section4. Those necessary conditions do not themselves construct a useful event.

The argument is elementary erasure domination/strong data processing, explicitly proved below. No novelty of those classical methods is claimed; the count and all-prior formulation is an additional scoped R-minus route barrier, not public novelty clearance.

## 2. Written proof by erasure domination

Write `Q_b(z)=P(X_i=z|B=b)` for one coordinate and let

`r(z)=min(Q_0(z),Q_1(z))`, `eta=sum_z r(z)`, `delta=1-eta`.

Recall `delta=(1/2) sum_z |Q_1(z)-Q_0(z)|`.

Construct an auxiliary channel E from B as follows. Independently of B and W, choose J with `P(J=1)=delta`. If J=0 output the erasure symbol; if J=1 output B with a tag distinguishing it from erasure. From E generate the coordinate output:

- at erasure, use the distribution r/eta;
- at tagged b, use `(Q_b-r)/delta`.

If eta=0 the erasure branch has probability0 and is simply omitted. If delta=0 the tagged branches have probability0 and the coordinate is independent of B. There is no division by0 in the actual construction.

For either B-value the resulting coordinate distribution is exactly

`eta*(r/eta)+delta*((Q_b-r)/delta)=Q_b`.

Thus W-B-E-X_i can be coupled as a Markov chain with the original joint law of W,B,X_i. Data processing gives

`I(W;X_i)<=I(W;E)=delta I(W;B)`.

The equality uses independence of J from (W,B). Since B is a deterministic function of the FULL X and W is a channel of B,

`I(W;X)=I(W;B)`.

Summing over the ten coordinates proves (O). This proof requires no conditional independence among the graph coordinates, nor an erasure decomposition of their JOINT channel. Coordinatewise decompositions suffice for ten separate data-processing inequalities.

## 3. Exact integer occupancies, including nonuniform ambient marginals

Let X be uniform on C, let `B=1{X in S}`, and set

`N=|C|`, `m=|S|`, `f_(i,z)=|{x in C:x_i=z}|`,

`n_(i,z)=|{x in S:x_i=z}|`.

The two coordinate conditional distributions are

`Q_(i,1)(z)=n_(i,z)/m`,

`Q_(i,0)(z)=(f_(i,z)-n_(i,z))/(N-m)`.

Therefore, exactly,

`delta_i = sum_z |N n_(i,z)-m f_(i,z)| / [2m(N-m)]`.

Substitution into (O) gives the relative unscaled margin

`3-D(S)/[m(N-m)]`.

Thus (OC) is an entirely integer-count sufficient certificate for the whole family. The normalized HC slack is one third of this unscaled expression. The D(S) criterion makes no singleton-balance assumption on either C or S, unlike the first membership packet.

Complementing S changes m to N-m and each n to f-n. The numerator `N n-m f` changes sign, while m(N-m) stays fixed. Hence (OC), its slack bound, and the obstruction are exactly complement-invariant, as a membership-family criterion should be.

A perfectly coordinate-balanced event has `n_(i,z)=m f_(i,z)/N` for all i,z, so D(S)=0. More importantly, nonbalanced tables with nonzero deviations are still excluded whenever their total absolute occupancy deviation satisfies (OC). This is not a claim that every nonbalanced event is weak or that the graph FDs force (OC).

## 4. Changed-prior curvature — a necessary test stronger than checking only the original prior

Keep the binary coordinate channels Q_(i,0),Q_(i,1) fixed, and let a=P(B=1) be the actual prior. For a possible posterior u in (0,1), put

`q_i(u)=(1-u)Q_(i,0)+u Q_(i,1)`,

`F(u)=D(Ber(u)||Ber(a))`,

`G_i(u)=D(q_i(u)||q_i(a))`,

`K(u)=3F(u)-2 sum_i G_i(u)`.

These definitions remain valid with nonuniform ambient marginals. For every finite W generated from B, the exact unscaled HC slack is the average of K at its B-posteriors. As in the first packet, all such W pass if and only if K(u)>=0 throughout [0,1]; a negative K value gives an explicit rare-output binary channel. No entropy endpoint identity is assumed for nonuniform ambient marginals.

Define the all-prior squared-correlation function

`rho_i(u)=u(1-u) sum_z [Q_(i,1)(z)-Q_(i,0)(z)]^2/q_i(u)(z)`.

Zero-probability symbols in both channel rows are omitted. For interior u every retained denominator is positive. Direct WRITTEN differentiation yields

`K''(u)=[3-2 sum_i rho_i(u)]/[u(1-u)]`.                    (C)

The quantity rho_i(u) is the squared maximal correlation for the binary input B of prior u and this coordinate channel. To see the formula without importing that terminology, Bayes' rule gives

`P(B=1|X_i=z)-u = u(1-u)[Q_(i,1)(z)-Q_(i,0)(z)]/q_i(u)(z)`.

Its variance divided by `u(1-u)` is exactly rho_i(u). Since the input is binary, every nonconstant centered input function is a scalar multiple of B-u, so this is also the usual squared maximal correlation.

The same erasure coupling from Section2 gives, for EVERY u,

`rho_i(u)<=delta_i`.                                      (CE)

Indeed, conditional expectation through B-E-X_i cannot increase variance. At E the conditional mean of B equals u on erasure and equals B on reveal, so its variance is exactly `delta_i*u(1-u)`. Dividing the contracted variance by u(1-u) proves (CE). No numerical spectral calculation is used.

There are two useful consequences:

1. If `sum_i rho_i(u)<=3/2` for every interior u, then K is convex. Since K(a)=K'(a)=0, it is nonnegative everywhere. This excludes the entire finite membership family even when the simpler total-variation certificate (OC) does not apply.
2. Conversely, if K(u0)<0 anywhere, the positive-weight integral of K'' between a and u0 must be negative. Hence at some interior changed prior u between a and u0,

   `sum_i rho_i(u)>3/2`.

Thus a useful finite-amplitude event cannot be certified merely by testing correlations at the original prior a. It MUST cross the aggregate3/2 threshold at SOME changed prior. It also necessarily has `sum_i delta_i>3/2` by (CE). Neither condition is sufficient for negative K; integration and the actual prior still matter.

This is the precise distinction between an original-law infinitesimal soft probe and an all-amplitudes membership mechanism. The earlier ribbon packet's local quadratic condition is not being promoted to a sufficient criterion for all auxiliaries.

## 5. Scope and exact surviving representation

For uniform code inputs, every term in rho_i(u) is a rational function of u and the literal integer counts. A proof that its sum stays at most3/2 can be made by clearing positive denominators and proving a polynomial sign. No polynomial signs were calculated or asserted for an unprovided code here.

The ambient graph remains the literal R-minus in `inputs-v1.json`, SHA256 `bdc4cd14d20e2401971a7354c2a6239106fbe2be158b50921d5c486c6a086be6`. The new generic overlap/curvature barrier uses no I2, T300, group classification, or finite-certificate import. Any use of the first packet's graph-specific corollaries retains its separate named ordinary-written imports and assurance limitations.

The next candidate now has explicit necessary structural requirements:

- a genuinely nonbalanced multiword occupancy profile, unless its balanced selected subcode already has lower Phi than the negative ambient code;
- `D(S)>3m(N-m)` for uniform code inputs;
- a changed-prior u at which `sum_i rho_i(u)>3/2`;
- and, decisively, an actual negative value of K at some posterior, or an actual negative-Phi winning-law construction giving a lower-bound improvement.

The latter decisive condition is UNPROVED. Neither the graph FDs nor the negative-global-minimum premise has been shown to force such a subcode or posterior. In fact any actual minimizer passes all posterior probes until an additional graph-specific contradiction is established. This is the exact barrier, not a missing computation to be silently assumed.

No certified numerical interval reduction, negative law, general all-auxiliary exclusion, fresh source/status/novelty clearance, independent review, formal/kernel verification, or admitted executable check is claimed. This packet was produced entirely by written mathematical reasoning under the corrected HOLD.
