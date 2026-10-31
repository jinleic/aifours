# f27 — Full review: causal endpoint obstructions and physical conditional curvature

Reviewer **MathSun8-2**. **WRITTEN same-harness scientific review**, with a separate bounded exact/numerical check; not formal/kernel/human/configured-family/novelty acceptance. Actual native prewrite clock **Wed Oct 28 17:26:28 PDT 2026**. Completed-review pin clock is separately observed and returned.

## 1. Verdict and exact scope

**NO_SUBSTANTIVE_DEFECT AT EXACT STATED SCOPE: 0 NEW mathematical FATAL / 0 NEW mathematical MAJOR / 0 NEW mathematical MINOR.** All three full candidate bodies were reconstructed:

1. An actual progressive Brownian E1-only input attains the common literal endpoint of a bounded linear progressively-output prefix-causal operator, while EVERY nonzero progressive E2 input is strictly below it. The operator is ensemble-nonlocal and therefore is NOT the registered physical SDE law.
2. A second actual progressive E1-only input attains the endpoint of a pathwise-contractive, stopping-time-causal, revealed-event-local operator while EVERY nonzero E2 input is strictly below it. Its deterministic zero-history response retains Brownian prehistory, so it too is NOT any registered deterministic-coefficient finite-dimensional SDE/controller.
3. For any actual SAME-law E1 endpoint attainer with finite positive E1 gain, the conditional curvature inequality (CK) is necessary at EVERY bounded stopping time, separately. Its proof needs bounded progressive variations and actual revealed-event locality, but no independent input/output, no inverse-output integrability or global E2 moment.

The first two are exact counterexamples to the specified ABSTRACT functional/causality implications, not physical endpoint counterexamples. The third is a necessary condition, not sufficient and not a proof or refutation of the original E2-to-E1 physical strict-transfer question. No novel/source-book/general-synthesis claim follows. Physical admissibility here is precisely the finite-horizon, local-pathwise-L2 law below, not an unstated stronger global state/control E1 class.

## 2. Exact inputs, earlier familiarity and validation scope

Frozen assignment was read first. All candidate hashes matched, and all lines including endings were read:

|Label|Candidate|SHA256|Lines/bytes|
|---|---|---|---|
|C1|`frontier-20261028-causal-operator-endpoint-obstruction.txt`|`edc472a40728dbe89acd7ab3feb2db94337f58f32cad43297f3aa0b1626d2a18`|103/8845|
|C2|`frontier-20261028-event-local-causal-endpoint-obstruction.txt`|`82c1b5902676a90d01d69ad606acf4905905fdc3db31238efa00d013c19a7514`|91/9971|
|C3|`frontier-20261028-endpoint-conditional-curvature-candidate.txt`|`1cd3e16efac53df8cee13be8bdeb92e7deba12fd7023d5a96a4261426cba623c`|86/7722|

Read the complete registered linear-preview definitions `info-3-linear-preview-class-definitions-v1.md`, SHA256 `9b72aca5c3434827f43bc81e3fcd3cfc5f72d4ddbf4c7df3943444f10e9151cd`, and the complete89LF output-only finite/infinite-domain source `output-only-E1-E2-literal-domain-equality-v1.md`, SHA256 `857ec99cc1be5d4ce2cd204fd7b0b01983d8bb8b3c8e633854b75370fb78da28`. The finite-horizon actual-SDE/localization portion used here is reconstructed below; its other stronger/unrelated statements are not newly adopted as a whole.

I previously reviewed this author's w21 fixed-law preview candidate and w105 E1/E2 pointwise endpoint candidate; the old review familiarity is disclosed, not called blindness. I did not contact the author or use its numerical runs as independent evidence. Historical held/quarantined bodies are not invoked as mathematical premises or retroactively validated; no cognition-reset or priority claim is made. My separately written checker and actual outputs are in Section9.

## 3. Original physical law and the Brownian E1-only input

The registered law fixes compatible real matrices and deterministic K,L0,Lh,H with H∈L2([0,h]), zero initial state/history, finite T>h>=0, and input J=[0,S] with S=T−h. The original equations are

    dx=[Ax+Bu+Cw(t−h)]dt+[A0x+B0u]dW,
    z=D0x+D1u,
    u=Kx+L0w(t)+Lh w(t−h)+∫_0^h H(r)w(t−r)dr,

with zero extension outside J. For h=0 taps combine and the kernel vanishes. E1 means `E||w||_J<infinity`; E2 means `E||w||_J²<infinity`; both use progressive inputs and the literal expectation of the L2 path norm. The comparison admits actual local pathwise-L2, nonexplosive controls. The filtration is the COMPLETED USUAL NATURAL Brownian filtration, so F_(0+) is trivial. This filtration hypothesis is load-bearing for strict E2 nonattainment; it is not asserted for an enlarged initial-randomness filtration.

For the abstract constructions C1/C2, take EVERY S>0, EVERY T>S, h=T−S and any c with `1/(4S)<c<1/(2S)`. Let

    w_*(t)=exp(c W_t²), 0<=t<=S,
    R=(∫_0^S w_*² dt)^(1/2).

Brownian continuity on [0,S] makes w_* progressive, R finite and strictly positive a.s. With M=sup_{t<=S}|W_t|, `R<=sqrt(S)e^(cM²)`. Reflection plus Gaussian tails gives `P(M>x)<=4 exp(−x²/(2S))`. Integrating the tail of exp(cM²), e.g. via `E e^(cM²)=1+∫_0^infinity 2cx e^(cx²)P(M>x)dx`, proves ER<infinity at the strict upper bound c<1/(2S).

For each deterministic t>0, direct integration against the N(0,t) density gives

    E exp(2c W_t²) = (1−4ct)^(-1/2) if 4ct<1,
                         infinity if 4ct>=1.

At equality the exponential integrand no longer decays, so the integral is infinite. Because the lower c bound is strict, `[1/(4c),S]` contains a positive-length interval; Tonelli gives ER²=infinity. The endpoint equality c=1/(4S) is deliberately not used as a divergence argument. Thus w_* is a genuine progressive E1-only input. No claim depends on simulating a tail divergence from finitely many Brownian paths.

For comparison, the actual physical law u=w, dx=w dW, z=x, h=0, has a local solution for the analogous input by pathwise finite energy. If F'(x)=exp(cx²), Itô's formula gives

    x_t=F(W_t)−c∫_0^t W_s exp(cW_s²)ds.

Both sup|F(W_t)| and the drift term are bounded by a constant times M exp(cM²); choosing a slightly larger exponent still below1/(2S) and applying the same tail bound proves E||x||<infinity. This physical comparison is not an attainment or strictness proof.

## 4. First abstract operator — C1 LF37–87

Define p_t=w_*(t)/R and `Phi(v)=E∫_0^S p_t v_t dt` for progressive E1 v. R uses the whole path, so p need NOT be progressive at t<S; this is expressly disclosed. Nevertheless p is measurable and `||p||_J=1` pathwise. Cauchy–Schwarz gives `|Phi(v)|<=E||v||`, so Phi is a genuine bounded REAL linear functional on the progressive E1 domain, with all integrals finite.

Let g(t)=h^(-1/2) on (S,T] and0 before, and `Tv=g Phi(v)`. T is linear, its output is deterministic and progressive, its expected output norm is |Phi(v)|, and its E1 operator gain is <=1. At every deterministic prefix t<S it outputs zero; at t>=S it depends only on the input equivalence class on J=[0,S]. This is the exact PREFIX-process causality claim made by C1, not a claim of samplewise event locality or general random-stopping-time locality. For v=w_*, `Phi(w_*)=ER`, giving gain1 and actual E1 attainment.

If nonzero E2 v satisfied `|Phi(v)|=E||v||`, equality in the triangle/expectation and pathwise Cauchy–Schwarz bounds implies `v_t=lambda w_*(t)` for dt×P-a.e. (t,omega), with an a.s. finite scalar lambda and a consistent sign on nonzero paths. A measurable choice is `lambda=(∫w_*v)/R²`. Because w_*>0 and v/w_* is progressively measurable, Fubini gives a deterministic full-measure set of times at which lambda equals an F_t-measurable ratio almost surely. Choose times decreasing to0 in this set; the completed canonical right-continuous filtration gives lambda∈F_(0+), so lambda is a deterministic constant a.s. If nonzero, E||v||²=lambda² ER²=infinity; if zero, v is the zero input. Therefore every nonzero E2 input is strictly below1.

For actual energy stops `tau_N=inf{t:∫_0^t w_*²>=N}` capped at S, each `w_*1_{t<tau_N}` is progressive E2, converges to w_* in E1 by dominated convergence, and is eventually pathwise identical on finite-energy paths. The bounded Phi therefore sends the stopped inputs and denominators to their E1 values; for sufficiently large N denominators are positive, and their ratios approach1. The E2 supremum equals1 without any finite E2 attainer.

For physical nonrealizability, fix ANY deterministic t0∈(0,S), `A={W_t0>=0}`, and deterministic v=1_[t0,S]. Then `1_A v` is progressive, and `Phi(1_Av)>0` is a deterministic constant because p>0 and P(A)>0. But `1_A Phi(v)` is a random variable that is0 on A^c of positive probability; hence `T(1_Av) != 1_A T(v)` as actual outputs. In the original zero-start linear SDE, the same event factor is revealed at t0 while v is zero before t0; it can be moved through the deterministic window, time and Itô integrals, and local uniqueness gives `Z(1_Av)=1_AZ(v)`. Thus the counterexample does not represent the registered physical map. C1 does not claim that it does.

## 5. Event-local pathwise operator — C2 LF26–82

With the SAME positive w_*,R,p,g, define

    (T_loc v)(t,omega)=g(t) ∫_0^S p_s(omega)v_s(omega)ds.

For progressive E1 v the integral is F_S-measurable: it is the time integral of a jointly measurable F_S-measurable path function. The output is0 for t<=S and F_S-measurable for t>S, hence progressive. Although p itself anticipates at early times, it is not used to emit output until the integral's information is available.

For a stopping time tau<=T, suppose two inputs agree through tau on each relevant path. If tau<S, both outputs are zero up to tau. If tau>=S, their input integrals over all of J agree on that path, so their outputs also agree up to tau. This pays the claimed samplewise stopping-time causality, including the tau=S boundary (single time values do not alter L2 paths).

For A∈F_tau and v supported after tau, `1_Av` is progressive and actual input; the fixed pathwise kernel gives `T_loc(1_Av)=1_AT_loc(v)`. Indeed the equality is algebraic for any event for which the product is admissible. Thus it retains the revealed-event locality whose failure ruled out C1.

Pathwise Cauchy–Schwarz and ||p||=||g||=1 give `||T_loc v||<=||v||`. Consequently T_loc is bounded E1->E1 and E2->E2. For w_* its output norm equals R on every path, so gain1 is attained in E1. If a nonzero E2 v attained literal ratio1, its nonnegative pathwise norm deficit would vanish a.s., so pathwise Cauchy–Schwarz equality gives `v=lambda w_*` dt×P-a.e. The Fubini/F_(0+) argument of Section4 makes lambda deterministic, and ER²=infinity excludes nonzero E2 v. The energy-stopped w_* inputs again make E2 supremum1 without an E2 attainer. No interchange of a terminal cutoff event with an anticipative Itô integral is used.

### 5.1 Actual physical nonrealizability, not just event-locality

Take a deterministic t0∈(0,S) and v=1_[t0,S]. Any registered physical fixed law has zero state/control/output before t0: the input and its causal delayed/window forcings are zero and the homogeneous zero-start linear SDE has unique zero solution. After t0 all input/window forcings are deterministic. Solving the deterministic-coefficient SDE from zero at t0 using the Brownian increments `W_(t0+s)−W_t0` gives a solution measurable in their completed future-increment filtration; strong uniqueness identifies it with the SAME original physical output. Thus the entire physical output path is future-increment measurable, not merely its expectation.

The abstract operator's post-S scalar is instead

    F = [∫_(t0)^S exp(cW_s²)ds] / [∫_0^S exp(2cW_s²)ds]^(1/2).

Condition on a future increment path q, continuous with B=sup|q|<infinity. Future increments are independent of F_t0. For any delta>0, the past small-ball event `sup_{s<=t0}|W_s|<delta` has positive probability. On it, the numerator is at least S−t0 and the denominator is at most

    [t0 exp(2c delta²)+(S−t0)exp(2c(B+delta)²)]^(1/2),

so F>=ell_B>0. Pick ANY nonempty interval [a,b] inside(0,t0). Brownian path full support on continuous paths starting0 gives positive probability to a path that stays above M on [a,b] while returning to `|W_t0|<delta` (a small open tube around a continuous excursion-and-return path suffices). On that event the same fixed q gives

    F <= (S−t0)exp(c(B+delta)²)/(sqrt(b−a)exp(cM²)).

For each fixed q, choose M so this upper bound is <ell_B/2. Both past events have positive probabilities conditional on q by independence, so the conditional distribution of F is not a point mass for almost every continuous future path. Hence F is not measurable in the future-increment sigma field. This uses the named standard Brownian full-support and independent-increment facts; it does not assume strong Markov at a random time. Therefore no member of the original zero-start deterministic-coefficient physical class realizes T_loc on all its inputs, despite event-locality and pathwise contraction.

This separation requires absence of extra controller memory/private Brownian history and deterministic coefficients; it is not asserted for arbitrary stochastic/adaptive controllers outside the registered class. It proves an abstract obstruction, not the existence of a physical E1-only attainer.

## 6. Actual E1 linearity and first-order normal equation — C3 LF7–28

Assume the SAME physical law's E1 gain is finite gamma>0 and an actual nonzero E1 w attains it: `E V=gamma E U`, where

    U=||w||_J,  V=||Z(w)||_I,
    u=w/U on U>0 and0 otherwise,
    p=Z(w)/V on V>0 and0 otherwise.

All inequalities here use the true E1 gain as a hypothesis. The finite-horizon output-only source obtains E1/E2 SUPREMUM equality by causal energy stops, strong E2 linearity, and L1(L2) completeness: stopped inputs converge in E1; finite gain makes actual stopped outputs Cauchy; on each finite-energy path the stop eventually disappears and uniqueness identifies the Banach limit with the actual local output. This is the SAME-object output result, not an assumed global state/control moment. The curvature result itself needs the finite E1 bound, not the equality of domains or any strict-E2 premise.

Let alpha be ANY bounded progressive real scalar process, v=alpha w and z_v=Z(v). Then `||v||<=M U`, where M bounds alpha, so v is E1. Actual E1 linearity follows from localized linear-SDE uniqueness and the original deterministic law; finite gain makes E||z_v||<infinity. For sufficiently small real d, w+d v remains an admissible E1 input with a positive expected denominator: pathwise it is bounded below by `(1−|d|M)U`.

Set `F(d)=gamma E||w+d v||−E||Z(w)+d z_v||`. It is nonnegative and F(0)=0. One-sided Hilbert-norm quotients are dominated by ||v|| and ||z_v||, both integrable. On U=0, v=0 pathwise; on V>0 the output derivative is `<p,z_v>`, while on V=0 the right and left derivatives are respectively `+||z_v||` and `−||z_v||`. The right derivative of F at its minimum is >=0 and the left derivative <=0. Subtracting these two inequalities forces `E[1_{V=0}||z_v||]=0`, hence `z_v=0` a.s. on V=0; the remaining equality is

    E<p,z_v> = gamma E<u,v>.

This is the candidate's (N), newly reconstructed rather than imported from its earlier variation note. No E2 strictness, random-shape independence, inverse V moment, or assumption V>0 a.s. is needed.

## 7. Second-order curvature and conditional stopping-time caller — C3 LF30–61

For every bounded alpha, define

    C_in=(||v||²−<u,v>²)/U on U>0, else0,
    C_out=(||z_v||²−<p,z_v>²)/V on V>0, else0.

Cauchy–Schwarz gives nonnegativity. On V=0 the actual z_v=0 was proved in Section6, not assumed.

The input symmetric norm quotient

    [||w+d v||+||w−d v||−2U]/d²

converges pathwise to C_in. On U>0 and |d|M<=1/2, the intermediate norms are at least U/2 and the Hilbert-norm second derivative is at most `2||v||²/U<=2M²U`. The symmetric quotient is its average with the usual triangular weights, so it is dominated by `2M²U`, an integrable random variable. On U=0 it is0 because v=0. Dominated convergence gives convergence of expected input quotients.

The analogous output quotient is nonnegative by norm convexity. On V>0 it tends to C_out; on V=0 it is identically0 because z_v=0 there. Add the nonnegative actual gain deficits F(d)+F(−d), divide by d², and use Fatou on the output quotients. This proves

    E C_out <= gamma E C_in < infinity.                           (K)

No interchange of a potentially unbounded output second derivative with expectation, no E[1/V] or E||z_v||² assumption, and no hidden independence is used. The result is a NECESSARY inequality for the SAME actual law and attainer.

Now let tau be ANY bounded stopping time with tau<=S, and let `w_tail=w 1_{t>=tau}`. With

    a²=∫_0^tau |w|²dt,    b²=∫_tau^S |w|²dt,    U²=a²+b²,

the variation v=w_tail has `||v||²=b²` and `<u,v>=b²/U` on U>0. Therefore

    C_in,tau = a² b²/(a²+b²)^(3/2),

with0 when a=b=0. The exact inequality `a²b²<=U⁴/4` gives `C_in,tau<=U/4`, including either zero part.

For every A∈F_tau, `alpha=1_A1_{t>=tau}` is bounded/progressive, `1_Aw_tail` is an actual E1 input, and the tail's pre-tau forcing/state are zero. Revealed-event factoring through deterministic window/time/Itô integrals and local uniqueness gives `Z(1_Aw_tail)=1_AZ(w_tail)`. Applying (K) for A and also proving z_tail=0 on V=0 from the alpha=1_tail normal equation gives

    E[1_A C_out,tau] <= gamma E[1_A C_in,tau]  for EVERY A∈F_tau.

Both sides are integrable: input by U/4, output by (K) with A=Omega. The defining property of conditional expectation therefore yields, for EACH tau,

    E[C_out,tau | F_tau] <= gamma E[C_in,tau | F_tau]  a.s.

No independence of tau, w, output, alpha or Brownian past is used. No COMMON null set over all stopping times is claimed. At tau=0, a=0 and the tail equals w, so output curvature is0; at tau=S, b=0 and tail/output are0. Paths with U=0 also contribute0. This pays the zero/endpoint boundaries and the candidate's exact (CK).

## 8. Conditional example: actual Volterra norm, without E2 strictness

The candidate's h=0 example `u=w`, `dx1=w dt`, `dx2=w dW`, `z=x1` is realizable with finite deterministic matrices in the registered class. x2 is unobserved. Its input-output map is the deterministic Volterra operator `z(t)=∫_0^t w(s)ds` pathwise. For y(0)=0, the sharp mixed-boundary inequality

    ∫_0^1 y² dt <= (4/pi²)∫_0^1 |y'|² dt

follows by putting `v(t)=sin(pi t/2)`, `y=v f` and integrating the nonnegative `∫v²|f'|²`; the endpoint term at1 vanishes because v'(1)=0, and the t↓0 term vanishes for H1 y with y(0)=0 by Cauchy–Schwarz. Equality occurs for y proportional to v. Thus the pathwise operator norm, and also the literal expected norm gain, is gamma=2/pi. The deterministic progressive E2 input w(t)=cos(pi t/2) attains it, so the example deliberately does NOT meet any hypothesis that every E2 input is strictly below the endpoint. It is a curvature-control example only.

## 9. Independent bounded exact/numerical check

I wrote the independent standard-library source `frontier-20261028-curvature-independent-check.py`, SHA256 `6562ce0de1e82f4c8e42eb3d7a2658fc8a39baa9e7df38c882289a1f334a4b38`,59LF/1975B. It imports no author code. The first part uses integer square roots and `fractions.Fraction` to check the exact split-curvature identity and `C_in<=U/4` for all54 nonzero Pythagorean integer pairs in its explicit 0..20 bounds, including zero-part cases. The second part uses 20,000 deterministic midpoint samples to independently evaluate the Volterra tau=0.4 curvature quantities from the analytic input/output functions; it is numerical illustration only, not a universal or stochastic proof.

Actual execution:

```text
/opt/homebrew/bin/python3 frontier-20261028-curvature-independent-check.py
exact_pythagorean_split_cases: 54
exact_split_identity_and_U_over_4_bound: PASS
volterra_midpoint_n: 20000
input_curvature: 0.147714795115
output_curvature: 0.00811576058276
gamma_Cin_minus_Cout: 0.085922398659
volterra_curvature_example: PASS (numerical illustration only)
Wed Oct 28 17:25:50 PDT 2026
```

The finite exact cases do not prove the all-variable algebra; Section7 did. The float midpoint values are not error-certified, do not test a heavy-tail E1 attainer, and do not establish physical E2 strictness. No Monte Carlo author output was reused as independent evidence.

## 10. Claim-by-claim disposition and unpaid gates

- **C1 LF13–36:** arbitrary positive S/h, actual progressive Brownian input, Gaussian/reflection moment ranges and E1-only status reconstructed; no substantive defect.
- **C1 LF37–87:** deterministic-output bounded prefix-causal linear operator, exact E1 endpoint, ALL-nonzero-E2 strictness by canonical-F0/Fubini, E2 supremum by causal stops, and event-local physical separation reconstructed; no substantive defect. Its causality is not silently promoted to samplewise event-locality.
- **C2 LF18–57:** fixed nonprogressive p with output only after S, pathwise contraction, stopping-time causality, revealed-event locality, exact E1 attainment and strict E2 nonattainment reconstructed; no substantive defect. E1/E2 common gain does not decide the physical target.
- **C2 LF59–75:** future-increment measurability of every registered deterministic-input zero-history physical response, and positive-probability excursion-return/small-ball conditional separation, reconstructed at named Brownian full-support/independent-increment and strong-SDE imports; no substantive defect.
- **C3 LF7–28:** finite E1 gain, SAME actual physical solution, bounded progressive variation, first-order zero-output handling and normal equation paid independently; no substantive defect. E1/E2 gain equality is not needed for the curvature implication once finite E1 gain is assumed.
- **C3 LF30–61:** exact symmetric second-order input bound, OUTPUT Fatou (not unlicensed dominated convergence), bounded stopping-time/locality/conditional-expectation step and zero cases paid; no substantive defect. No extra independence or inverse-moment premise found.
- **C3 LF63–86:** physical Volterra example is at an E2-attained endpoint and is only a necessary-condition illustration; no reported simulation constitutes a proof or strict-E2 example.

**FATAL0 / MAJOR0 / MINOR0 at exact scope.** **NR-PHYSICAL-E1-ONLY-ATTAINER / NR-UNIVERSAL-PHYSICAL-STRICT-TRANSFER / NR-GENERAL-SYNTHESIS / NR-STRONGER-BOOK-ADMISSIBILITY / NR-NOVELTY** remain. The event-local counterexample shows that even prefix causality, stopping-time causality, pathwise contraction and revealed-event factoring alone are insufficient; it supplies no original physical counterfamily. Brownian full support, reflection/Gaussian integration, finite-horizon linear-SDE existence/local uniqueness/linearity, Fubini/Tonelli, dominated convergence and Fatou are named standard imports, not formally checked here. Main must read all three candidates and this full review before adoption.
