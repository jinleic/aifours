# f12 scientific review — stopping-time E1 slice and endpoint normal/angle conditions

Reviewer **InfoSPR7-2**; author **InfoHinfPreview-2**. Native `/bin/date` observation immediately before this write: **Wed Oct 28 17:18:51 PDT 2026**. This is a prewrite observation, not an invented completion/RETURN time.

**Verdict: 0 FATAL / 0 MAJOR / 1 MINOR (M1).** The stopping-slice theorem, its actual E1-only example, the endpoint normal equation, strict-angle consequence and stopping-time caller are mathematically reconstructed at the stated fixed-law scope. M1 is a missing explicit bridge for the example's claim that it lies outside the ENTIRE earlier revealed-amplitude/independent-future-shape subclass; a short independent bridge is supplied in §6. It does not undermine the slice theorem or establish the full endpoint implication.

## 1. Exact scope, source reads and reviewer exposure

The assigned `f12-hinf-stopping-slice/assignment-v1.json` was read FIRST; live SHA256 `ebbea6ae06020d6fa351611780c51bce2fc3fd1ed86262f9e38a654229bfd021`. Then both COMPLETE candidates were read through their actual endings:

- **S:** `frontier-20261028-stopping-slice-endpoint-candidate.txt`, **112 LF**, SHA256 `fdd8f85dc22d901e08724766c5ac6a0f6c79b48568ef949fb0667ba706c62917`.
- **V:** `frontier-20261028-endpoint-variation-angle-candidate.txt`, **96 LF**, SHA256 `8fa91cb811cab94784480894408229a90e96c72947d869885c0206a9f820076c`.

Registered finite fixed-law model: `info-3-linear-preview-class-definitions-v1.md`, SHA256 `9b72aca5c3434827f43bc81e3fcd3cfc5f72d4ddbf4c7df3943444f10e9151cd`; literal comparison context: `info-3-literal-criterion-packet-v1.md`, SHA256 `888307a4a094bc5fa7aca45484334f8a12b75e9fb3e86259d81acf31cad629f3`. The finite-law class is an explicit comparison interpretation; this review does not independently authenticate book pixels or enlarge it into the full printed synthesis problem.

I also read the COMPLETE used dependency bodies and exact parent scope records:

- output-only E1/E2 literal gain equality `output-only-E1-E2-literal-domain-equality-v1.md`, **89 LF**, SHA256 `857ec99cc1be5d4ce2cd204fd7b0b01983d8bb8b3c8e633854b75370fb78da28`;
- progressive E2 projection `e1-e2-endpoint-progressive-projection-regularizer-v1.md`, **94 LF**, SHA256 `0c9f5686e7b336fa2d910c6176a6c1271919d9cbd6ab66c3a898cd6ef0f9aa1d`;
- their parent dispositions `info-3-output-only-e1-e2-gain-equality-parent-v1.md` and `info-3-universal-progressive-e2-regularizer-parent-v1.md`, as scope/status context, not substitutes for the used proofs.

I previously authored same-harness preview reviews v220/v244 and an older preview source review; this is **serial, nonblind, same-track** familiarity, not an independent model-family review. No historical held/withdrawn outcome or author checker result was used as a mathematical premise. The prospective frontier-first direction does not retroactively validate prior quarantine records.

## 2. Claim-by-claim verdict and exact assumptions

| Claim | Verdict | Boundary |
|---|---|---|
| S LF21–45: stopping-time finite-conditional-energy slice | WRITTEN_SUPPORTED | One fixed linear law, finite T>h>=0, zero state/history, w=0 before the bounded stopping time, finite common literal gain gamma>0, strictness for every nonzero progressive E2 input, hypothesis (H). |
| S LF49–55: necessary condition on endpoint attainers | WRITTEN_SUPPORTED | For each qualifying stopping time separately, not a universal null set over an uncountable family; no attainer is constructed. |
| S LF59–83: explicit E1-only coupled-shape physical family | WRITTEN_SUPPORTED WITH M1 | Conditional moments/actual solution verified; the additional no-ALTERNATIVE-factorization bridge is supplied in §6. It is not an endpoint counterexample. |
| V LF19–39: normal equation and output-zero support | WRITTEN_SUPPORTED | Conditional on an actual nonzero E1 endpoint attainer, finite E1 bound, same linear law; bounded progressive multiplier. Path-normal vectors may be anticipative proof variables. |
| V LF41–58: exact angle budget and strict necessary inequality | WRITTEN_SUPPORTED | Uses the separately supported nonzero progressive E2 projection; no multiplier/output commutation is assumed. |
| V LF60–69: conditional tail equations | WRITTEN_SUPPORTED | For each bounded stopping time; the masked TAIL is a fresh input with zero history. No independence of future path shape from F_tau. |
| V LF71–85: Volterra physical sanity example | WRITTEN_SUPPORTED at the described illustrative scope | It has an E2 attainer and therefore does NOT satisfy the universal-strict-E2 hypothesis. Numerical check is not a proof of endpoint transfer. |

No proposed implication above proves pointwise E2-strictness transfers to ALL E1 inputs, constructs a physical endpoint attainer satisfying the hypotheses, or solves prescribed-gamma controller synthesis.

## 3. Used output-only E1/E2 dependency, reconstructed

The plant and SAME deterministic stationary linear law are
`dx=[Ax+Bu+Cw(t-h)]dt+[A0x+B0u]dW`, `z=D0x+D1u`,
`u=Kx+L0 w(t)+Lh w(t-h)+integral_0^h H(r)w(t-r)dr`.
Here T>h>=0, input J=[0,T-h] is zero-extended and output I=[0,T]; state/history are zero. H is deterministic L2. At h0 the endpoint taps combine and the integral disappears. The two symbols E1/E2 describe input integrability for the SAME literal expected-path-L2 ratio, not literal versus RMS gains.

For an E1 input, its total path energy is finite a.s. Stop at the first time its OWN accumulated energy reaches N. Each stopped input is progressive E2, because its energy is at most N. Causality of the delay/kernel map and strong uniqueness give consistency of the actual stopped solutions. On each finite-energy path the stop is eventually beyond the full input energy, so these solutions patch to the actual local nonexplosive strong solution; no global expected control-energy assertion is needed.

If the E2-domain literal gain gamma is finite, stopped input differences tend to zero in E1 by dominated convergence. Same-law linearity and the E2 gain bound make their actual outputs Cauchy in L1(Omega;L2(I)). Stopped consistency identifies that limit with the actual E1 output. Hence `E||Z(v)||<=gamma E||v||` for every E1 v and the E1/E2 literal suprema coincide. This is the used output-only dependency, not an assumption that every E1 state/control has finite expected energy.

The inequality is NONSTRICT at a supremal endpoint. Density/equality of suprema alone does not transfer pointwise strictness: this is exactly why S's extra slice hypothesis and V's necessary conditions matter. For zero input the response is zero by zero state/history and linearity.

## 4. Stopping-time event masking: adaptedness and actual output identity

Take bounded tau<=T-h and a progressive E1 w with w=0 for t<tau modulo dt×P. For any A∈F_tau the process `1_A 1_{t>=tau}` is adapted and right-continuous, hence progressive under the usual conditions. The product
`w_A(t)=1_A 1_{t>=tau}w(t)`
is an actual progressive input; it equals the shorthand `1_A w` modulo input measure. This is not multiplication of a nonzero pre-tau path by an unrevealed terminal event.

Zero input/history imply the unique actual state, control and output vanish before tau, modulo the appropriate path/input equivalences. For t>=tau, every input value in the actual current/delayed/kernel window with time before tau is zero. The F_tau-measurable factor therefore commutes with the deterministic integrals and with each stochastic integral STARTING at tau. Explicitly, it is an admissible bounded initial random coefficient for those post-tau integrals. Localize if needed; strong uniqueness then identifies the SAME original-law outputs:

`Z(w_A)=1_A Z(w)`, `Z(w_(A^c))=1_(A^c)Z(w)` as time-L2 paths.

No independence of the future shape from F_tau is involved. No general assertion `Z(alpha w)=alpha Z(w)` for an arbitrary time-dependent alpha is made. The point t=tau and shifted endpoint tap values affect at most time-null sets, not a new input at a forbidden pre-tau time.

Pathwise event support gives additivity of the whole path norm across these complementary EVENTS, not across time slices. The E1 bound makes all output norms integrable, so
`D(w)=D(w_A)+D(w_(A^c))`, `D(v)=gamma E||v||-E||Z(v)||>=0`.

## 5. Finite conditional-energy slice and ALL stopping-time necessity

For U=integral_J |w|^2 and extended nonnegative `V_tau=E[U|F_tau]`, let `A_n={V_tau<=n}`. Extended conditional expectation is the monotone limit of the expectations of U truncated at deterministic levels. It gives
`E integral |w_A_n|^2=E[1_A_n V_tau]<=n P(A_n)<infinity`.
So every masked input is E2.

Under S's actual hypothesis `P(U>0,V_tau<infinity)>0`, the increasing union of these A_n covers that event. Therefore for some n, `P(U>0,A_n)>0` and hence `E||w_A_n||>0` (E1 integrability also gives finiteness). This actual progressive E2 input is nonzero.

If the E1 input had D(w)=0, event-deficit additivity and nonnegativity would force D(w_A_n)=0, contradicting strictness for EVERY nonzero E2 input. Hence D(w)>0. The argument needs neither a common strict margin nor future-shape independence.

Its contrapositive is S LF49–53: for any hypothetical endpoint attainer under the strict-E2 hypothesis, EVERY bounded stopping time before which its input vanishes must satisfy `E[U|F_tau]=infinity` on `{U>0}`, modulo null sets. This statement is for EACH stopping time; it does not produce one null set simultaneously for all uncountably many stopping times. If tau=T-h, an input supported only at that endpoint is zero in time-L2, so the nonzero/(H) premise automatically cannot be met. No special endpoint case is missing.

## 6. M1 — explicit physical E1-only example and absence of an alternative independent factorization

**M1, MINOR, S LF83–85.** The source correctly shows that its particular natural shape `w/Y=1+alpha(Y)B` depends on Y. That observation alone does not logically exclude a DIFFERENT revealed amplitude and a different future-increment-only shape. The example says it lies beyond the earlier entire factorization subclass, so a direct no-alternative-factorization argument should be supplied. The following short bridge pays it; no source edit or new quantitative hypothesis is needed.

For arbitrary 0<t0<T, a∈[1/2,1), set P=1−Phi(W_t0/sqrt(t0)), Y=P^(−a), alpha=Y/(1+Y), w(t0+r)=Y(1+alpha B_r), B_r=W_(t0+r)−W_t0. The input has continuous paths immediately after t0 and w(t0)=Y>0. Itô's formula gives `x=Y[B_r+alpha(B_r^2-r)/2]` for the actual dx=w dW, z=x. Future increments are independent of F_t0; this independence is used HERE for this constructed example, not in the general slice theorem.

Conditional Brownian moments give `E[U|F_t0]=Y^2(L+alpha^2 L^2/2)` and `E integral |x|^2=Y^2(L^2/2+alpha^2 L^3/6)`. The cross moment vanishes by the centered Gaussian third moment; `E(B_r^2-r)^2=2r^2`. Uniform P gives E Y finite and E Y^2 infinite for the entire stated a-range. Conditional Cauchy with alpha<1 gives finite expected input/output path norms, and Tonelli gives infinite E U. The input is E1-only, with finite V_t0 a.s. and U>0 a.s.

Now suppose ANY alternative representation `w=Y' v` existed, with finite F_t0-measurable real Y' and v depending only on the post-t0 Brownian increments as a time-L2 path. Since w is nonzero on each path, Y' is nonzero a.s. The time average `epsilon^(-1) integral_0^epsilon w(t0+r)dr` tends to Y a.s. by path continuity. Dividing by Y' shows the corresponding averages of v tend a.s. to Y/Y'. Their limit is measurable both in the future-increment sigma-field and F_t0. Independent sigma-fields have only a.s.-constant common variables, so Y/Y'=c for a finite nonzero constant c.

Consequently `v=c(1+alpha(Y)B)` as a time path. The future-measurable random variable `integral_0^L v(t0+r)dr` has conditional variance `c^2 alpha(Y)^2 L^3/3` given F_t0. The variable alpha(Y) is nonconstant, whereas independence from F_t0 would make that conditional variance constant. Contradiction. This proves the stronger entire-subclass exclusion, not merely dependence of one chosen normalization. If the intended claim were only about the displayed factorization, M1 is a wording/justification precision rather than a false theorem.

The example does NOT prove its particular law has finite gamma with every nonzero E2 input strictly below gamma, or that its w attains such a gamma. It is therefore neither an endpoint counterexample nor evidence of universal strict transfer.

## 7. Exact endpoint variation, including zero paths and integrability

Assume a nonzero E1 w satisfies D(w)=0, with finite gamma>0 and the strict-E2 premise. Put U=||w||, V=||Z(w)|| and define full time-path unit vectors `u=w/U` on U>0 and `p=Z(w)/V` on V>0, zero otherwise. These are Hilbert-valued measurable proof variables and need NOT be adapted.

For any real bounded progressive alpha let v=alpha w. Then v∈E1 and, by the output-only bound, Z(v)∈L1(Omega;L2(I)). On U=0 the whole input path w and therefore v vanish. Same-law strong SDE linearity gives the actual relation `Z(w+epsilon v)=Z(w)+epsilon Z(v)`; no scalar multiplier commutation with Z is asserted.

By the gamma bound, `F(epsilon)=gamma E||w+epsilon v||-E||Z(w)+epsilon Z(v)||>=0` and F(0)=0. The reverse triangle inequality bounds the magnitude of the input/output norm difference quotients by ||v|| and ||Z(v)||, respectively, which are integrable. Dominated convergence therefore permits the two one-sided derivatives. At U>0 the input derivative is `<u,v>`; on U=0, v=0 so both one-sided derivatives are0. At V>0 the output derivative is `<p,Z(v)>`; on V=0 it is +||Z(v)|| from the right and -||Z(v)|| from the left.

Let n=E<u,v>, m=E<p,Z(v)> and q=E[1_{V=0}||Z(v)||]>=0. A minimum gives `gamma n-m-q>=0` and `gamma n-m+q<=0`. Thus q=0 and gamma n=m. Since q is the expectation of a nonnegative variable, `Z(v)=0` a.s. as an L2 time path on {V=0}. Also
`E<p,Z(v)>=gamma E integral_J alpha(t)|w(t)|^2/U dt`,
with the fraction defined to be0 on U=0. This proves V's full normal equation for EVERY bounded progressive alpha. No second moment of w, optional projection of a costate or adjoint/Hamiltonian theorem is needed.

## 8. Projection regularizer, angle budget and revealed tails

For c>0 the used progressive-projection source constructs `alpha_c=E_m[c/(c+sqrt(U_energy)) | progressive sigma-field]`, where U_energy=||w||^2 and m=dt×P. Its proof shows `0<alpha_c<=1` a.e., `v_c=alpha_c w` is nonzero progressive E2, and `E integral |v_c|^2<=c^2`. The distinction between U_energy here and the path norm U in V is retained.

Pathwise Cauchy makes
`A_c=E(||v_c||-<u,v_c>)>=0`,
`B_c=E(||Z(v_c)||-<p,Z(v_c)>)>=0`.
Both are finite: ||u||,||p||<=1 and v_c,Z(v_c) are E1. The normal equation gives EXACTLY `D(v_c)=gamma A_c-B_c`. Strictness for the actual nonzero E2 input yields `0<D(v_c)`, hence `0<=B_c<gamma A_c` and A_c>0 for each c. Equality in the input Hilbert Cauchy inequality, with positive multiplier alpha_c, is equivalent to alpha_c being constant on the |w_t|^2dt support of that path. Therefore for each c there is a positive-probability nonzero input path where that constancy fails. No common positive-probability set for every c is asserted.

For a bounded tau<=T-h let `w_tail=1_{t>=tau}w`. It is a separate progressive E1 input which starts with zero input/history before tau. For any A∈F_tau, §4's actual linear factor identity applies to the TAIL: `Z(1_A w_tail)=1_A Z(w_tail)`. Apply the normal equation to alpha=`1_A1_{t>=tau}`. The bracketed random variable in V LF64–65 is integrable: its first absolute value is bounded by gamma U and its second by ||Z(w_tail)||. Since its expectation against every F_tau indicator is zero, its conditional expectation given F_tau is zero. No independence is needed; p may depend on the WHOLE original output. The output-zero conclusion from §7 applies to that tail for each tau separately.

Combining this with §5 gives two actual necessary conditions for an endpoint counterexample; neither is sufficient, and neither constructs one.

## 9. Independent physical check — actual command and limits

I did NOT run or import the author's two checkers. I wrote a separate standard-library checker in my own root:

`frontier-review-f12-independent-check-v1.py`, SHA256 `b9e74aea1e4f9331443f6990074143890826e3bcda748d6193d57e3907e646dd`.

Actual command:

`/opt/homebrew/bin/python3 -B frontier-review-f12-independent-check-v1.py --output frontier-review-f12-independent-check-v1.json --seed 928041 --paths 6000 --steps 160`

The output receipt SHA256 is `5b837656499b3a568a552218b29bdd643fed79ae2961143f5cb70a2c88c9e07f`. The checker used actual fixed law `u=w`, `dx1=w dt`, `dx2=w dW`, `z=x1`, T1/h0, with deterministic `w=cos(pi t/2)` and independently chosen tau3/8. This law has an E2 attainer and deliberately VIOLATES the all-E2-strict premise; it is a sanity check of the identities, not an endpoint counterexample.

Observed output:

- gamma `0.6366197723675814`; normal-equation residual `2.7755575615628914e-17`; angle-budget residual `1.3877787807814457e-17`.
- Unmasked tail input angle `0.17277196993816668`, output angle `0.012453423340808012`, deficit `0.09753662883272629`.
- Independent midpoint-quadrature versus closed-form maximum discrepancy `5.905054223376283e-11`.
- Seeded event fraction `0.5031666666666667` versus exact probability1/2. Shared-increment discrete x1/x2 slice residuals were both0.0.

These floats and a finite Brownian discretization are NOT exact proof of the all-input theorem. The proof above uses the actual equations and named ordinary stochastic facts, not numerical agreement. The separate symbolic Volterra identity for the unmasked tail follows for every tau from the elementary integrals in the checker; no numerical value is used as a theorem premise.

## 10. Remaining gap and final review disposition

**Mathematics:** 0 FATAL / 0 MAJOR / 1 MINOR (M1 at S LF83–85, with the no-alternative-factorization bridge in §6). The complete conditional statements and both actual-law callers are supported in ordinary written mathematics, including local E1 solutions, all integrability/zero-path cases, nontrivial F_tau events, no hidden future-shape independence in the general theorem, h0/h>0 and finite output tails.

**Not established:** the universal E2-pointwise-strict → E1-pointwise-strict implication without (H); a physical E1-only endpoint attainer with infinite conditional energy on all revealed starts; impossibility of such an attainer; a general stationary controller or original prescribed-gamma synthesis criterion; full book/domain equivalence, source/novelty/priority or formal/kernel/human/independent-model verification. The physical examples are scoped as stated, not counterexamples to the main conditional theorem.

This is a serial same-harness supplied-source reconstruction and one bounded independent sanity run, not parent adoption. Historical quarantines/records remain historical; no unvalidated held claim is imported and no inference of clean cognition follows. Candidate source bytes are immutable; M1 should be handled additively or by an explicit review qualification. After actual RETURN, resume the original septic shared-numerator research as instructed.
