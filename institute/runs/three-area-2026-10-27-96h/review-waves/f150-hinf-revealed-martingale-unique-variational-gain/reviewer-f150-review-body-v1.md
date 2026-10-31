# f150 — Independent same-harness mathematical review

## Verdict and exact scope

**CORRECT at the assigned scope; 0 FATAL / 0 MAJOR / 0 MINOR mathematical findings, no load-bearing step left INCONCLUSIVE.** This is a same-harness written-mathematics review with independently authored local exact controls, not human review, independent-model-family review, formal/kernel verification, novelty verification, or parent acceptance.

The scope is precisely the scalar law

\[
 dx_t=w_{t-h}\,dW_t,\quad z_t=x_t,\quad x_0=0,\qquad T>h\ge S:=T-h>0,
\]

with canonical Brownian filtration, progressive inputs supported on \([0,S]\), path norm \(\|w\|=(\int_0^S|w_s|^2ds)^{1/2}\), output path norm on \([0,T]\), and literal ratio \(E\|z\|/E\|w\|\). Here E1 means \(E\|w\|<\infty\), and E2 means \(E\|w\|^2<\infty\); nonzero means \(E\|w\|>0\). These integrability assumptions, finite horizon, the support constraint, and Brownian independent increments are load-bearing. In particular, E1 does NOT silently become an E2 assumption in the proof.

The reviewed conclusion is

\[
 \gamma_1=\gamma_2=\sqrt S\,\kappa,\quad
 \kappa=\max_{\nu\in\mathcal P[0,1]} E\sqrt{\int B_s^2\nu(ds)},
\]

where the relaxed maximizer is unique, its support has a positive gap above zero and has supremum one, no nonzero physical E1/E2 input attains the gain, and **the original universal pointwise strict criterion holds at \(\gamma=\sqrt S\kappa\)**. Neither the optimizer nor a numerical/closed value of \(\kappa\) has been determined. No synthesis, arbitrary-matrix, general-law, \(h<S\), or literal/RMS-equivalence conclusion is reviewed or granted.

The **original epsilon-log proof passes on its own merits**, without the optional alternative. The separately admitted optional two-pulse alternative also passes after an independently implemented exact rational quadrature. It is additional support for the strict lower step only, not a replacement for any other dependency.

## 1. Frozen inputs, read coverage, receipts

Authority: `contract-addendum-2-frontier-first-owner-direction-v1.json`, SHA-256 `5e18c2d4b94656fc12b5cfce4122889fa6073e24a21f1e0062c79d846b6037ce`, read completely. The current authority permits fresh checking but does not promote historical held outputs into mathematical premises; none is used here.

- Frozen original manifest: `manifest-v1.json`, SHA-256 `af53e4c3bc55b46b90186b15293e57cfd2404bd0875532bd9fb7eecff0a62221`, 4088 bytes, 51 LF.
- Parent-admitted optional supplement: `manifest-v2.json`, SHA-256 `04b3e2fd0f81456070c150e5ca358c126bc9b758bf267cb2901bd7d8bed9730c`, 6092 bytes, 80 LF. Its five original inputs are identical to v1; its optional inputs were read only after recording an assessment of the original epsilon-log proof.

All paths in the following table are under `information-science/evidence/three-area-20261027-96h/parallel-18/stochastic-hinf-preview/`. Hash/byte/LF checks passed before the corresponding complete content reads, in manifest order. Original inputs total 294 LF. Optional inputs were read in overlay/candidate/checker order. All eight inputs have CR=0 in the run receipt.

| ID | Full basename | SHA-256 | Bytes / LF |
|---|---|---|---:|
| I1 | `frontier-20261028-full-input-revelation-strict-endpoint.txt` | `592d9a3710ddde08794554cd66d6a2144b3543100da694c2b341b5395a4f3abc` | 4156 / 46 |
| I2 | `frontier-20261028-revealed-martingale-strict-literal-rms-gap.txt` | `f5196dbcbcf326b4b97a802ad8092318ed6d04ab24343cfc8a602f9f7e8b60c3` | 4236 / 67 |
| I3 | `frontier-20261028-revealed-martingale-exact-unique-variational-gain.txt` | `018f2343aad2734da58ebe9180d39619a86b44a2291b4a3a84638aea59380cb1` | 8027 / 89 |
| I4 | `frontier-20261028-revealed-martingale-endpoint-kkt-proof-detail.txt` | `4e00f3eec9f41ea46c2de22749fca5eeea76c8b5d79fdb5242ef44f8eeea9671` | 5407 / 67 |
| I5 | `frontier-20261028-revealed-martingale-optimizer-support-endpoints.txt` | `4a2355d2dec6774dcfecfb43fe678114f37691ac6987c0783056d952c184bb8c` | 2087 / 25 |
| O1 | `frontier-20261028-f150-strict-lower-alternative-note-v1.txt` | `64f1795c07f6f3e8fb4b1b4c276d3f86c146e1eaad46eaf3f228ce5c1edbaf39` | 1814 / 7 |
| O2 | `frontier-20261028-revealed-martingale-certified-two-pulse-gain.txt` | `5b852b3e6ff210fe662b8156396fe5c625d7b54609fea793f97d13bfd19244d2` | 4376 / 58 |
| O3 | `frontier-20261028-brownian-mixture-rational-quadrature.py` | `312bc67154518e23fc21b4bcb08d30fa4c01bd92d32897b6b109b26a152c235b` | 2073 / 56 |

**O3 was read and hashed only, never imported or executed.** Author claims of prior PASS/refinement count are not evidence for this review.

Observed executions (Python 3.14.3, mpmath 1.4.1):

1. `reviewer-f150-independent-controls-v1.py`, run by `reviewer-f150-run-controls-v1.py`: 2026-10-28T22:00:40-0700 to 22:00:41-0700 PDT, actual exit 1, **35 PASS / 1 FAIL**. The failure was my diagnostic overreach: I required the strict improvement also at epsilon=0.1, whereas the source claims it only for sufficiently small epsilon. The diagnostic correctly found F-c<0 there; the lower-bound chain itself and every exact check passed. This is NOT a source defect. The script, failed log, and receipt are preserved.
2. Additive `reviewer-f150-control-correction-v2.py` leaves all v1 artifacts unchanged, separates the chain inequality from the small-e sign, and makes epsilon=0.1 an intended-reason negative control.
3. `reviewer-f150-independent-controls-v2.py`, run by `reviewer-f150-run-controls-v2.py`: 2026-10-28T22:01:13-0700 to 22:01:13-0700 PDT, actual exit 0, **40 PASS / 0 FAIL**. Receipt: `reviewer-f150-run-receipt-v2.json`; stdout: `reviewer-f150-independent-controls-v2.log`.

The final control SHA is `c1bea769463cb2793a20d01d951e65c4849b0d8a19b92376f2a878b5062e54c1` (8863 B, 178 LF); final log SHA is `8273dac3d88e6bef4071a5995cf75d8f0fa39b6d1d72ab0ea91ee8b9cb5f3e00` (2760 B, 46 LF). Native clock observations, complete source fingerprints, runner hash, prior failed receipt binding, and correction hash are recorded in the v2 receipt.

`reviewer-f150-original-assessment-v1.txt` (SHA `124886a3d6f8174f4ce45c7e7626633c8b2aa735d2ea72471bb72999cc3e3019`) records the original epsilon-log reasoning before opening O1-O3. An earlier exploratory control draft remained in local scratch and was never executed or used as evidence. No Monte Carlo or numerical optimizer was run. Numerical quadrature checks are diagnostics, not substitutes for the analytic proof or exact rational certificate.

Process/provenance disclosure: during setup, a format-sample read displayed the prefix of the prior f138 `review-v1.md`, including unrelated mathematics. None of that material is a premise or evidence in this review. A non-scientific copy test also created `local://f150-cp-test.txt` and `/tmp/f150-cp-test.txt`, outside the assigned output directory; this was an output-location deviation. A command containing removal was rejected by tool policy before execution, so no deletion occurred. No sources were edited. Subsequent persistent review/control outputs are only this file and `reviewer-`-prefixed files in this directory. No Git, author contact, web search, external model/paid API, publication, infrastructure mutation, repository build/lint/test/formatter, or author-code execution was performed.

## 2. Input revelation: VERIFIED independently for the assigned law

I1's broader arbitrary-matrix claims and its separate all-matrix bound are **not** accepted as black-box premises. For the present law everything needed can be reconstructed directly.

A progressive, pathwise L2 input restricted to [0,S] is an \(\mathcal F_S\)-measurable random element of the separable space \(L^2[0,S]\): progressive joint measurability gives measurable integrals against a countable dense family of deterministic L2 test functions. Since \(S\le h\), the entire L2-valued input is \(\mathcal F_h\)-measurable. The state is zero before h, and

\[
 x_{h+t}=\int_0^t w_s\,d\widetilde W_s,\qquad
 \widetilde W_s=W_{h+s}-W_h,\quad 0\le t\le S,
\]

where \(\widetilde W\) is independent of \(\mathcal F_h\). Freezing the whole random path—not merely an amplitude—therefore gives its conditional Gaussian stochastic-integral law. This follows first for finite simple L2-valued inputs and then by L2 approximation and localization on the \(\mathcal F_h\)-measurable events \(\{\|w\|\le n\}\). Thus no second-moment assumption on the original E1 input is needed.

For deterministic v set \(g(v)=E\|\int_0^\cdot v_s d\widetilde W_s\|_{L^2[0,S]}\). Direct Itô isometry and Jensen imply

\[
 g(v)\le\left(\int_0^S(S-s)|v_s|^2ds\right)^{1/2}\le\sqrt S\|v\|,
\quad |g(v)-g(u)|\le\sqrt S\|v-u\|.
\]

In particular g is Borel, g(0)=0, and the conditional identity \(E[\|z(w)\|\mid\mathcal F_h]=g(w)\) is integrable in E1. Consequently the actual ratio is the \(\|w\|\)-weighted average of deterministic ratios. Deterministic inputs are E2, so both E1/E2 suprema equal the deterministic supremum.

The strictness/attainment transfer is also valid: if \(d(v)=\gamma\|v\|-g(v)>0\) for every deterministic nonzero v, then d(w) is integrable, nonnegative, and strictly positive on the positive-probability event \(\{\|w\|>0\}\). Hence \(E d(w)>0\), even without a uniform gap. Conversely a violating deterministic vector is an E2 counterexample. Equality in the weighted average at the supremum would force equality on its nonzero paths, so a random maximizer would supply a deterministic maximizer. This proves the exact transfer needed later.

**Dependencies:** separable-space measurability, Brownian independent increments, deterministic Wiener integral / conditional freezing, local Itô construction for pathwise-square-integrable progressive integrands, Itô isometry, Jensen, and elementary expectation positivity. No held output, unreviewed all-matrix estimate, or RMS substitution is needed.

## 3. Literal-versus-RMS bracket: VERIFIED

For a unit deterministic v put \(m=S^{-1}\int_0^S s|v_s|^2ds\), and write \(X=x_{h+S}\sim N(0,1)\), \(c=E|X|=\sqrt{2/\pi}\). Itô isometry gives exactly

\[
 E\|x\|^2=S(1-m),\qquad E\|x-X\|^2=Sm.
\]

Jensen and the L2 triangle inequality give the two simultaneous bounds \(E\|x\|\le\sqrt S\sqrt{1-m}\) and \(E\|x\|\le\sqrt S(c+\sqrt m)\). Their decreasing/increasing crossing is

\[
 K_{\rm up}=(c+\sqrt{2-c^2})/2<1.
\]

The strict comparison follows exactly from \((2-c)^2-(2-c^2)=2(1-c)^2>0\), since \(0<c<1\). I distinguish this upper-bound constant from the actual variational \(\kappa\). Early unit pulses give literal lower limit \(c\sqrt S\). The revelation reduction transfers the literal upper bound to E1 without using \(E\|w\|^2\).

For E2 only, Itô isometry gives \(E\|z\|^2=E\int_0^S(S-s)|w_s|^2ds\le S E\|w\|^2\); early deterministic pulses approach equality, so the separate RMS gain is \(\sqrt S\). This proves a genuinely strict gap between literal and RMS gains, not their equivalence.

The same bracket holds directly on every relaxed measure: with \(m=\int(1-s)\nu(ds)\), Jensen gives \(F(\nu)\le\sqrt{1-m}\), while the pathwise triangle inequality relative to constant \(B_1\), followed by Jensen, gives \(F(\nu)\le c+\sqrt m\). Thus the relaxed upper bound does not require a circular appeal to the gain formula.

**Dependencies:** §2 for physical E1 transfer; Itô isometry, Gaussian absolute mean, triangle inequality, Jensen, Tonelli. Exact piecewise-constant controls C0-C2 verified both second-moment identities and the clock mean.

## 4. Relaxation, density, compactness and weak continuity: VERIFIED

For any deterministic nonzero v, normalize \(\|v\|=1\). Set \(A(u)=\int_0^{Su}|v_t|^2dt\). It is nondecreasing AC with A(0)=0, A(1)=1. The deterministic-integrand Gaussian process has covariance \(A(u\wedge u')\), so \((x_{h+Su})_u\) has law \((B_{A(u)})_u\), including flat parts of A. Therefore its literal ratio is \(\sqrt S F(A_\#\mathrm{Leb})\).

Conversely the correctly time-scaled input \(v(t)=\sqrt{A'(t/S)/S}\) realizes any such clock and has unit L2 norm. On the unit physical interval this is simply \(\sqrt{A'}\).

For any probability measure, choose a nondecreasing quantile Q. Interpolate its interior grid values monotonically and impose endpoints 0 and 1. The resulting AC, piecewise-linear A_j converge at every interior continuity point of Q, hence a.e.; changes forced at endpoints occupy vanishing physical measure. For every bounded continuous test function, dominated convergence yields \((A_j)_\#\mathrm{Leb}\Rightarrow Q_\#\mathrm{Leb}=\nu\). Atoms, endpoint atoms, and gaps in support cause no failure of this density argument.

For a fixed Brownian continuous path, weak convergence of measures gives \(Y_{\nu_j}=\int B_s^2\nu_j(ds)\to Y_\nu\). The square roots are bounded by \(\sup_{s\le1}|B_s|\), integrable by Doob's L2 bound. Thus F is weakly continuous, not merely upper semicontinuous. The weakly compact space \(\mathcal P[0,1]\) supplies an attained relaxed maximum, and density identifies it with the physical supremum. Combined with §2 this proves the exact variational formula for both E1 and E2.

**Dependencies:** deterministic-integrand Gaussian covariance/time change, Brownian scaling and continuity, quantile representation, dominated convergence, Doob integrability, compactness of probabilities on a compact metric space, and §2. No physical maximizer is inferred from compactness of the relaxation.

## 5. Strict concavity and uniqueness via the variance identity: VERIFIED

For \(\eta=\nu_1-\nu_2\), finite signed-measure Fubini and the Gaussian fourth-moment identity give

\[
 \operatorname{Var}\!\left(\int B_s^2\eta(ds)\right)
 =2\iint \min(s,t)^2\eta(ds)\eta(dt)
 =4\int_0^1 r\,\eta([r,1])^2dr.
\]

Here \(\min(s,t)^2=\int_0^1 2r\mathbf1_{r\le s}\mathbf1_{r\le t}dr\); the sign-changing measure causes no issue since the total variation is finite and the Brownian fourth moments are uniformly bounded. If the last integral were zero, the bounded-variation, left-continuous tail would vanish at every positive r, not just a.e. Thus eta is supported at 0; its total mass zero then forces eta=0. For distinct probabilities the variance is strictly positive. Their nonnegative quadratic functionals differ with positive probability, so the strict pointwise concavity of the square root remains strict after expectation. The compact maximum is consequently unique.

**Controls:** 300 exact rational signed-measure cases (297 positive and 3 identically zero), the hand value 15/32, a wrong-kernel negative, and eta=delta_0 showing precisely why the total-mass-zero hypothesis is necessary. Eta=delta_0-delta_(1/3) correctly restores positivity. These controls corroborate, rather than replace, the all-measures proof.

**Dependencies:** Gaussian squared covariance \(2\min(s,t)^2\), signed Fubini, tail regularity, strict concavity of square root, §4 existence.

## 6. Original epsilon-log strict lower: VERIFIED WITHOUT the optional alternative

This addresses I3 §5, especially LF68, and I4 §3, especially the LF38 strict-improvement clause, on their own merits.

For \(\nu_e=(1-e)\delta_1+e\delta_{1/2}\), the Gaussian quadratic form has trace \(1-e/2\) and determinant \(e(1-e)/4\). Its larger eigenvalue is at least the diagonal entry 1-e and at most its trace, which is at most one. Hence the smaller is at least the determinant. In independent normal coordinates, with \(s=\sqrt e/2\),

\[
 F(\nu_e)\ge\sqrt{1-e}\,E\sqrt{X^2+s^2Z^2}.
\]

On \(1\le|Z|\le2\), \(s\le|X|\le1\), rationalization gives the claimed increment lower bound \(s^2/[(\sqrt5+1)|X|]\). Independence and normal-density lower bounds \(\phi(2)\), \(\phi(1)\) give exactly

\[
 E[\sqrt{X^2+s^2Z^2}-|X|]
 \ge C s^2\log(1/s),\quad
 C=\frac{2e^{-5/2}}{\pi(\sqrt5+1)}>0.
\]

In particular, using \(\sqrt{1-e}\ge1-e\), for \(0<e\le1/2\),

\[
 F(\nu_e)-c\ge e\left[-c+\frac{(1-e)C}{4}\log(2/\sqrt e)\right].
\]

The bracket is positive whenever \(\log(2/\sqrt e)>8c/C\). Such positive e exist. This is the precise comparison behind the epsilon-log sentence; it is not an unsupported exchange of asymptotics and expectation. Its explicit sufficient e is extremely conservative, but there is no claim that a moderate fixed e satisfies it.

Therefore \(\kappa>c\), and all single-positive-time measures, with value \(c\sqrt t\le c\), are excluded. An atom of mass p>0 at 0 is excluded separately: moving it to 1 increases Y by \(pB_1^2>0\) a.s. Hence the optimal measure has no mass at 0 and at least two distinct positive support points. These conclusions do not use O1-O3.

**Controls:** exact covariance traces/determinants at four rational e; mpmath diagnostic confirmation of each inequality in the lower-bound chain; the correctly factored small-e deficit; negative controls that the crude bound does not certify a moderate e and that epsilon=0.1 actually fails the strict improvement. The latter is why the reviewer v1 diagnostic was corrected; it does not contradict the author's sufficiently-small-e statement.

**Dependencies:** 2D Gaussian diagonalization, elementary eigenvalue bounds, normal-density bounds and independence, square-root rationalization, elementary logarithmic divergence. No numerical κ value or optimizer is used.

## 7. Inverse moments: VERIFIED, with the rank-two dependency essential

Choose \(I_1,I_2\) of positive optimal mass \(p_1,p_2\), with \(0<a_1\le b_1<a_2\le b_2\), possible from §6. For \(Z_i=p_i^{-1}\int_{I_i}B_s\nu^*(ds)\), Jensen gives

\[
 Y^*\ge p_1Z_1^2+p_2Z_2^2.
\]

These are Gaussian linear functionals of B. The first has positive variance (at least a_1). The second can be written \(B_{b_1}+H\), where H averages increments after b_1, is independent of \(\mathcal F_{b_1}\), and has variance at least \(a_2-b_1>0\). Thus the pair is genuinely nondegenerate; correlation of its older-noise part with Z1 does not eliminate this independent variance.

A nondegenerate 2D Gaussian has bounded density locally. Since \((z_1^2+z_2^2)^{-3/4}\) has radial integral \(\int_0^1 r^{-1/2}dr<\infty\), the displayed lower bound proves \(E(Y^*)^{-3/4}<\infty\). It also proves Y*>0 a.s. and \(E(Y^*)^{-1/2}<\infty\) (split at Y*=1).

This step would be false for a single atom: Y=B_t² gives both \(EY^{-1/2}=E|B_t|^{-1}=\infty\) and \(EY^{-3/4}=E|B_t|^{-3/2}=\infty\). The finite moment \(E|B_t|^{-1/2}\) is a different statement and is not used. Controls explicitly distinguish the exponents and reject the rank-one case.

**Dependencies:** §6 for two separated positive-mass intervals, Jensen, Gaussian linear-functionals/independent increments, bounded nondegenerate Gaussian density, polar integrability in dimension two. There is no circular use of the support gap to establish this inverse moment.

## 8. Directional derivative, KKT and support gap: VERIFIED

Define \(f(t)=E[B_t^2/\sqrt{Y^*}]\). Hölder with exponents 3 and 3/2 and §7 imply finiteness. For the feasible direction \((1-e)\nu^*+e\delta_t\), the exact quotient is

\[
 \frac{\sqrt{Y^*+e(B_t^2-Y^*)}-\sqrt{Y^*}}e
 =\frac{B_t^2-Y^*}{\sqrt{Y^*+e(B_t^2-Y^*)}+\sqrt{Y^*}}.
\]

Its absolute value is bounded by \((B_t^2+Y^*)/\sqrt{Y^*}\), an integrable function by Hölder and E sqrt(Y*)<infinity. Dominated convergence therefore gives the finite right derivative \((f(t)-\kappa)/2\). Maximality implies f(t)<=kappa for every t, not only a.e.

Tonelli gives \(\int f\,d\nu^*=E\sqrt{Y^*}=\kappa\), so equality holds nu*-a.e. The stated continuity bound is exactly the same Hölder pairing:

\[
 |f(t)-f(s)|\le (E|B_t^2-B_s^2|^3)^{1/3}(E(Y^*)^{-3/4})^{2/3}\longrightarrow0.
\]

The first factor tends to zero by Gaussian increment moments (or by dominated convergence with the integrable sixth moment of the Brownian maximum). Continuity promotes equality to the **entire topological support**. Since f(0)=0 and kappa>0, there is deterministic a>0 with f<kappa on [0,a), forcing \(\operatorname{supp}\nu^*\subset[a,1]\).

The converse characterization also holds at its stated integrability: the pointwise square-root tangent inequality gives

\[
 F(\mu)-F(\nu)\le\tfrac12\left[\int f_\nu(t)\mu(dt)-F(\nu)\right]\le0
\]

when the asserted bound on f holds everywhere and Y is positive a.s. (as required by the inverse moment). Tonelli justifies the integral, and strict concavity gives uniqueness. No unjustified differentiation through a divergent single-atom inverse moment occurs.

**Dependencies:** §7 inverse-3/4 moment, Hölder, dominated convergence, Tonelli, Gaussian moments/Brownian path continuity, global maximality, and §5 strict concavity for the converse uniqueness.

## 9. Upper support endpoint: VERIFIED

If a positive-value probability is supported in [0,b] with 0<b<1, pushing forward by s->s/b yields

\[
 F((s\mapsto s/b)_\#\nu)=b^{-1/2}F(\nu)>F(\nu)
\]

by equality of Brownian finite-dimensional laws under scaling, extended to continuous paths. A zero-support measure has value zero, so cannot maximize. Thus \(\sup\operatorname{supp}\nu^*=1\). Support is closed, hence 1 belongs to it, and §8 gives \(E[B_1^2/\sqrt{Y^*}]=\kappa\). Neither an atom at 1 nor finite support is established or needed.

**Dependencies:** Brownian scaling, positive optimum, maximality; the endpoint KKT relation additionally needs §8 continuity/equality on support. A two-time numerical scaling diagnostic agrees, but the scaling proof itself is exact.

## 10. Physical clocks, nonattainment and strict-at-gain conclusion: VERIFIED

For any physical normalized nonzero deterministic input, its AC clock is continuous, A(0)=0, A(1)=1. For every a>0, continuity at zero supplies a nonzero physical-time interval [0,d) on which A(u)<a. Consequently

\[
 (A_\#\mathrm{Leb})([0,a))\ge d>0.
\]

The d can depend on the particular input: **no uniform lower mass bound is asserted**. In contrast nu* has zero mass on [0,a) for the a from §8. Hence no physical clock equals nu*. By uniqueness, every physical deterministic ratio is strictly below the relaxed maximum. By §4 density, these strict ratios still approach the maximum as a supremum.

Finally §2 transfers this pointwise strict deficit to every nonzero progressive E1/E2 input. It follows that no input attains the gain and

\[
 E\|z(w)\|<\sqrt S\,\kappa\,E\|w\|\qquad\text{for every nonzero admissible E1/E2 }w.
\]

Thus the **original strict criterion holds at the gain itself**, not only for larger gamma. This does not contradict the definition as a supremum: there is no common positive margin. Every smaller positive gamma is defeated by some deterministic approximating clock.

**Dependencies:** §4 exact physical/relaxed supremum and density, §5 uniqueness, §8 support gap, continuity at zero of physical clocks, §2 literal strictness/attainment transfer. §9's upper support endpoint is an independently verified additional restriction, not a necessary premise for nonattainment.

## 11. Optional alternative: separately VERIFIED by fresh exact arithmetic

O1-O3 do not repair a failed original step: §6 already passes. They supply an independently checkable finite alternative proving only the strict lower and the stated physical two-pulse threshold.

### 11.1 Gaussian/Laplace and monotonicity reconstruction

For \(\nu=(99/100)\delta_1+(1/100)\delta_{1/2}\), Gaussian diagonalization gives

\[
 E e^{-u^2Y}=(1+199u^2/100+99u^4/10000)^{-1/2}.
\]

The square-root Laplace representation, after t=u² and Tonelli, yields

\[
 F(\nu)=\pi^{-1/2}\int_0^\infty g(u)du,
\quad g(u)=\frac{1-Ee^{-u^2Y}}{u^2},\quad g(0)=EY=199/200.
\]

For y>=0, \((1-e^{-u^2y})/u^2=\int_0^y e^{-u^2r}dr\) is nonnegative and decreasing in u, so g has that property. These analytic identities were reconstructed, not taken from a checker PASS.

### 11.2 Independent exact certificate, different from the author's checker

My implementation uses a **fixed projective mesh**, not the author's adaptive heap: \(u_i=i/(N-i)\), i=0,...,N-1, N=32768. Right-Darboux monotonicity gives a lower bound on [0,32767]; the omitted tail is nonnegative. At each endpoint, an integer square root at scale 10^30 bounds the square root of the exact rational determinant from below, hence bounds g from below. Each complete interval contribution is rounded down to a multiple of 10^-18 before integer summation. All bounds and the final comparison use exact integers/rationals; the numerical quadrature diagnostics do not participate.

Observed exact result:

\[
 \int_0^\infty g(u)du\ \ge\
 \frac{1415408001884884001}{10^{18}}
 \ >\ \frac{283}{200}.
\]

The intended-reason negative control N=32 yields only \(157380890337159283/125000000000000000<283/200\), so the verifier correctly refuses certification from an inadequate mesh.

Independent Machin alternating bounds give

\[
 157/50<281476/89625<\pi
 <670143059704/213311234375<22/7.
\]

Exact rational comparisons in the executed control are

\[
 (283/200)^2(7/22)-(7981/10000)^2=118779/1100000000>0,
\]
\[
 (7981/10000)^2(157/50)-2=328677/5000000000>0.
\]

Therefore this alternative, independently of §6's epsilon-log argument, proves \(F(\nu)>7981/10000>\sqrt{2/\pi}\) and hence kappa>c. A deliberately lower threshold 79/100 correctly fails the comparison with c.

O3's printed gain comparison is weaker (399/500) than O2's separately stated 7981/10000 comparison. That is not an invalidation: the actual integral threshold 283/200 is strong enough for 7981/10000, as the fresh exact calculation shows. Its historical reported run/refinement count was not replayed and is not certified here.

### 11.3 Physical witness transfer

The ideal step clock jumps to 1/2 at physical time zero, then to 1 at epsilon=1/100. O2's normalized finite input has two energy-1/2 pulses on [0,delta] and [epsilon-delta,epsilon], delta=10^-10. Its AC clock agrees with the step clock outside those two intervals. Coupling the same B and using reverse triangle followed by Jensen gives

\[
 |F(\nu_v)-F(\nu)|\le
 \left(\int E|B_{A(u)}-B_{A_0(u)}|^2du\right)^{1/2}
 =\left(\int|A(u)-A_0(u)|du\right)^{1/2}
 \le\sqrt{2\delta}<1/50000.
\]

Thus \(F(\nu_v)>7981/10000-1/50000=2494/3125\), with a genuinely finite deterministic E2 input and the correct factor sqrt(S) after physical rescaling. This supports exactly the optional stated threshold and failure of strict feasibility at or below it. It determines no sharp gain and is unnecessary to the original endpoint proof.

**Dependencies:** explicit two-time Gaussian covariance, Gaussian Laplace determinant, square-root Laplace identity, monotonicity/Tonelli, independently executed exact outward rounding, Machin identity/alternating arctangent bounds, Brownian coupling/isometry, §4 physical scaling. No author checker, numerical optimization, or held source is used as independent proof.

## 12. Step-by-step disposition and dependency ledger

| Step | Disposition | Load-bearing inputs / reconstructed dependencies |
|---|---|---|
| Full-path revelation and E1/E2 literal reduction | VERIFIED at this law | I1 at in-scope specialization; §2 direct bound/freezing/localization; S<=h |
| Literal/RMS strict bracket | VERIFIED | I2; §3 Itô/Jensen/triangle, §2 E1 transfer |
| AC-clock representation and density | VERIFIED | I3 §2 / I4 §1; deterministic time change, correct S-rescaling, quantiles |
| Relaxed compactness and weak continuity | VERIFIED | I3 §2 / I4 §1; compact [0,1], Brownian maximum domination |
| Strict concavity / unique maximizer | VERIFIED | I3 §3 / I4 §2; signed variance identity, total mass zero |
| Original epsilon-log strict lower | VERIFIED on its own | I3 §5 / I4 §3; §6 detailed bound, no optional premise |
| No atom at 0 / two positive support points | VERIFIED | strict lower, moving zero-time mass to 1 |
| Inverse-3/4 and inverse-half moments | VERIFIED | two separated positive-mass intervals, rank-two Jensen lower bound |
| KKT derivative, equality on full support, gap at 0 | VERIFIED | inverse-3/4 moment, Hölder/DCT/Tonelli, continuity |
| Sup support = 1 and endpoint KKT equality | VERIFIED | I5; positive value and Brownian scaling, KKT continuity |
| Every physical clock has mass near 0 | VERIFIED | AC implies continuity at 0, A(0)=0; no uniform d required |
| No deterministic/random E1/E2 attainment | VERIFIED | physical-clock obstruction + uniqueness + revelation |
| Strict original criterion at gamma=sqrt(S) kappa | VERIFIED | nonattainment, actual supremum identity, integrable positive deficit |
| Optional strict-lower alternative / finite pulses | VERIFIED separately | O1-O3 read only; independent exact mesh certificate and coupling |

**Overall correctness: correct. Confidence: 0.95.** There is no request for source edits. This review establishes only the scoped mathematical chain and its stated dependencies; it is neither a parent adoption nor a certification of novelty, an explicit optimizer, an exact numerical kappa, or any broader synthesis/theory.
