# Finite GLOBAL literal gain does not price free-channel martingales — exact family and strictness endpoints

Owner **InfoHinfPreview-2 / info-3**. Actual returned `/bin/date` BEFORE this write: **Sun Oct 25 20:27:25 PDT 2026**. Observation bound, not an exact creation time. **Complete WRITTEN OWNER-CANDIDATE, pending its OWN complete source/import/application gate.** No scientific interpreter/calculator/eval/program/CAS/enumeration/checker/solver/replay/simulation, external model, CLI, nested agent, build or test was used. No in-kernel verification is claimed.

## 0. Exact new implication settled, and the unchanged general problem

The earlier v8 proved a strict-local-martingale obstruction for one input with finite output energy, but EXPLICITLY did not decide whether a finite UNIFORM GLOBAL literal output gain would repair that control-integrability gap. Its visible scalar law was subsequently proved to have infinite gain at h0 in v13. One cannot silently use that old example against a stronger finite-global-gain hypothesis.

Here a different actual two-state representation closes the stronger implication. For EVERY positive a,b,c,k,d,sigma and EVERY finite h>=0, the stationary printed-window law below has ALL-input strong nonexplosion/local-PATHWISE-control-L2, uniform full-state zero-window internal EMS and

    G1(F)=G2(F)=kappa=dc/a, strictly positive and finite.

Nevertheless, for an actual deterministic finite-energy pulse from ZERO initial state, the FREE control has INFINITE expected path-L2 norm on EVERY positive post-pulse interval, and the full-state drift-only mean equation is false. Thus neither global literal OUTPUT gain nor even global RMS OUTPUT gain supplies individual unpriced-control H1/expected-L2 admissibility in arbitrary rank-deficient data.

This is a **per-law admissibility/necessity-method counterfamily**, not a controller-existence separation: u=0 is a stronger-admissible controller with the SAME optimal output gain. It does not show that an optimal replacement controller cannot be chosen in a stronger class. That replacement/optimal-realization gap for general data remains OPEN, and the old mean-square substitute stays scoped.

For this explicit family I also prove the exact ENDPOINT distinction, without confusing the book with the declared strict-uniform research convention:

- strict UNIFORM interpretation `sup_w N1(z)/N1(w)<gamma`: solvable iff `gamma>kappa`;
- POINTWISE-strict interpretation `N1(z(w))/N1(w)<gamma` for EACH nonzero allowed input, without a uniform gap: solvable iff `gamma>=kappa`.

The second assertion is conditional on that explicit quantifier reading; no supremum symbol is invented in the printed page. Both assertions quantify over ALL strongly admissible controllers for THIS plant, because its visible output is uncontrollable. Neither is arbitrary-plant or finite-horizon N&S.

## 1. Actual source convention, read-before-write and provenance

The original printed p675 raster `information-science/stochastic-hinf-preview-control/sources/book/pdfpage-0696.png` was directly viewed again before this write. It displays current-state/window `u(t)=F(x(t),w(s):t-h<=s<=t)` and the expected time-L2-norm ratio `<gamma`, with expectation OUTSIDE the path norm; it distinguishes finite horizons from b tending to infinity. It does not display a supremum symbol. The complete17LF parent TEXT boundary was also actually read; this packet retains its strict-uniform-versus-printed distinction rather than treating one as the other.

Complete current v11/v12/v13 parent dispositions, with all endings, were NOW actually read. They support their own exact local-truncation/DC-match/dual-coercivity hypotheses, not v14 or this successor. Complete173LF v14 and complete191LF v8 were actually read. The new proof below uses v8's scalar classical calculation, restated at its exact operative scope, and a direct visible convolution identity. It does NOT depend on v14's pending norm bridge, unread v10/v13 author proofs, an optional external sharp probability theorem, or old review headlines.

Pinned inputs observed by metadata-only SHA256:

| Input | Exact scope used/read | SHA256 |
| --- | --- | --- |
| `literal-preview-synthesis-consolidated-v8-Rdef-integrability.md` | complete191LF, RAW1–105/106–191 | `b19dcd670bfbf99d79d8abdaa3948a50c84e8b99923596680b4d5990acd341e1` |
| `literal-preview-synthesis-consolidated-v14-sequential-probability-buffers.md` | complete173LF, RAW1–95/96–173; context only, NOT a proof import | `d956c0827df54c7e9e1c5a63a0af00673208ec24c7c6bd4d4d44cd0f4395a8c8` |
| `RUN/preview-generic-norm-bridges-and-Rdef-parent-v1.md` | complete actual parent body/end | `feb8b52a576161ffc85e670dc147f6f7df0802be5261099e523bc13a66e62860` |
| `RUN/preview-v11-local-truncated-parent-v1.md` | complete actual parent body/end | `0f9bc46ed92d265e7afffb0df0b0d69b08f29228be53f1bfd7e900d913a21f5b` |
| `RUN/preview-v12-DC-matching-parent-v1.md` | complete actual parent body/end | `a76055e5f8fbcd53ba841ecd00f9646471821295983ae91e774065c86f285f6e` |
| `RUN/preview-v13-dual-coercivity-parent-v1.md` | complete actual parent body/end | `7cf9829b671619f4422069c347f746111e3c45c8c2c1bea992599bc04d08fa68` |
| `RUN/preview-v3-model-source-boundary-v1.md` | complete17LF | `c66113762df23694d3446fa48d716da9bc0c6a5e953d115cd706694017fef78a` |
| actual printed p675 raster | directly viewed current image | `f2e84bd77d6e38d23b3f598edacdebcd7648a37ba8148f9207be87b8ed70624b` |

`RUN/` means `institute/runs/three-area-2026-10-23-96h/`; own filenames are relative to this exclusive owner root. Source hashes do not imply additional linked author/reviewer bodies were read. No previously frozen source is edited.

## 2. Full parameter family, constant matrices and printed stationary controller

Fix arbitrary a,b,c,k,d,sigma>0 and finite h>=0. There is ONE scalar Brownian motion W, scalar disturbance w, scalar control u, two-dimensional state X=(x,y) and scalar output z. Negative external history and gain initial state are0. Use the actual constant plant

    dx_t=(-a x_t+c w(t-h))dt,
    dy_t=(-b y_t+k w(t-h))dt+sigma u_t dW_t,
    z_t=d x_t.                                             (1)

Equivalently,

    A=diag(-a,-b), B=(0,0)^T, C=(c,k)^T,
    A0=0_(2x2), B0=(0,sigma)^T,
    D0=(d,0), D1=0.                                        (2)

The diffusion actuator is genuinely nonzero; it is not a no-op. Its output cost is unpriced, R=D1^TD1=0, and D0^TD0 has rank1. The positive hidden-input coefficient k is nonzero. The output is NOT identically zero: c,d>0 and nonzero deterministic pulses produce nonzero x.

Use the single deterministic STATIONARY law

    v_t=w(t-h),
    u_t=F((x_t,y_t),w_[t-h,t])
       =-sigma^(-1)y_t^2 1_(v_t=0).                        (3)

It uses current state and ONLY the permitted fixed LEFT endpoint tap. No controller clock, additional memory/state, future Brownian path, energy-history statistic or random controller is used. Its discontinuity in the input tuple is declared. For every state ball of radius R,

    |F((x,y),eta)-F((x',y'),eta)|
       <=(2R/sigma)|(x,y)-(x',y')|                         (4)

for the SAME arbitrary input tuple eta. Thus STATE-LOC is uniform in eta and F(0,0)=0, but global state-Lipschitzness is not claimed.

Allowed inputs are ALL canonical progressive w with `E integral_0^infinity |w|^2<infinity`. Controls need local PATHWISE square-integrability, not automatically expected control energy. Fixed input versions equal dt-times-probability almost everywhere yield equal delayed taps dt-times-probability almost everywhere; the same strong equation therefore results. The parameter family contains every positive rational parameter choice without any machine-evaluated arithmetic.

## 3. All-input strong admissibility and actual full-state EMS

The visible equation is a linear convolution. For any allowed progressive input, the hidden equation is exactly

    dy=(-b y+k v)dt-y^2 1_(v=0)dW.                          (5)

Its progressively measurable coefficients are uniformly locally Lipschitz in y, so the localized equations have unique strong solutions. The proper nonnegative function `psi(y)=log(1+y^2)` has

    Lpsi=-2b y^2/(1+y^2)+2k y v/(1+y^2)
         +1_(v=0)y^4(1-y^2)/(1+y^2)^2
         <=1+k|v|.                                       (6)

The diffusion term is<=1 for |y|<=1 and nonpositive outside; `|2y/(1+y^2)|<=1`. At the state exit stop tau_R the Lyapunov martingale is square integrable. Hence

    E psi(y_(T wedge tau_R))
       <=E psi(y_0)+T+k E integral_0^T |v|<infinity.

Expected input L2 gives the last bound by Cauchy–Schwarz. The exit value log(1+R^2) tends infinity, forcing P(tau_R<=T)->0. This proves nonexplosion for EVERY allowed input, not just the pulse below. Local uniqueness/strong construction gives nonanticipativity, event locality and consistent zero response.

Every finite nonexplosive continuous path is bounded, so

    integral_0^T |u_t|^2dt
       <=sigma^(-2)T sup_(t<=T)|y_t|^4<infinity a.s.       (7)

This is the exact stipulated local-pathwise-control-L2 admissibility. Its expectation need not be finite.

With zero input/window, x_t=exp(-at)xi_x and the hidden state solves `dy=-b ydt-y^2dW`. The scalar lemma in §4 gives

    E|y_t|^2<=100 exp(-2bt)|xi_y|^2.

Therefore for every deterministic initial full state, and by conditioning for every independent square-integrable initial full state,

    E|(x_t,y_t)|^2
       <=100 exp(-2 min(a,b)t) E|xi|^2.                  (8)

This is actual uniform full-state internal EMS of the SAME law. It is not inferred from the output gain. In particular the unobserved noise is not an unstable hidden blow-up concealed by z.

## 4. Scalar strict-local-martingale lemma at its exact ordinary inputs

For clarity, the operative scalar result from the fully read v8 is reproduced here. For q>0 start

    dY_s=-Y_s^2 d beta_s, Y_0=q,
    theta_b(t)=(1-exp(-2bt))/(2b).

Let R_s be the radius of three-dimensional Brownian motion started at(q^-1,0,0). Stopping the harmonic potential1/|x| in an annulus and letting its inner radius decrease shows that this Brownian motion does not hit0. Radial Itô gives `dR=d beta+R^-1 ds`; another Itô calculation gives Y=1/R and the displayed scalar SDE. Uniqueness identifies the LAW of the actual ONE-Brownian equation. The auxiliary three-dimensional motion is a law computation, not added physical noise or controller information.

The deterministic time change gives

    y_t=exp(-bt)Y_(theta_b(t))                            (9)

in law for zero-input(5), since `d beta_(theta_b(t))=exp(-bt)dW_t` after deterministic Brownian time change. This is not a controller clock implementation.

The elementary Gaussian inverse-square bound is uniform:

    E Y_s^2<=100 q^2.                                    (10)

One explicit proof writes `E Y_s^2=q^2 E|e1+sqrt(zeta)Z|^-2`, zeta=sq^2. For zeta>=1/4, split at radius sqrt(zeta); bounded Gaussian density inside and inverse-square bound outside give `(1+sqrt(2/pi))/zeta<=12`. For0<zeta<=1/4, outside radius1/2 the contribution is<=4; inside, distance from e1 is>=1/2, giving at most `(2pi)^(-1/2)zeta^(-3/2)exp[-1/(8zeta)]`. The function r^(3/2)exp(-r) has its maximum at3/2 and is<2; the elementary inequalities in v8 bound the latter contribution by64. Thus the sum is<68<100. At zeta0 it is1. These are displayed analytic bounds, not evaluated Gaussian trials or calculator results. Equations(9),(10) prove the scalar bound used in(8); reflection handles negative initial states,0 is absorbing.

Angular Gaussian integration gives the strict first-moment formula, for t>0,q>0,

    E y_t=exp(-bt)q
       *P(|N(0,theta_b(t))|<=q^-1)
       <exp(-bt)q.                                     (11)

For example the radial density is

    r/(r0 sqrt(2pi s))
       *[exp(-(r-r0)^2/(2s))-exp(-(r+r0)^2/(2s))],

with r0=q^-1; multiplying by1/r and integrating produces the Gaussian probability in(11). Its inequality is strict because every nondegenerate Gaussian has positive mass outside a finite interval. No probability was numerically evaluated.

For EVERY positive T,

    E (integral_0^T y_s^4 ds)^(1/2)=infinity.              (12)

If it were finite, the ordinary H1 martingale implication (a continuous local martingale with integrable square-root bracket is a true mean-zero/UI martingale on the finite interval) would apply to `-integral y^2 dW`. The finite second moments in(8) justify drift Fubini; taking expectation would force `E y_t=q exp(-bt)`, contradicting(11). This H1 implication is the standard NONSHARP ordinary martingale/BDG-localization fact, not the optional external sharp sqrt2 transfer. Pathwise the bracket remains finite by nonexplosion. Thus (12) is stronger than merely divergent expected squared control energy.

## 5. Exact positive finite GLOBAL output gains on ALL inputs

For every sample path of an allowed input,

    x_t=c integral_0^t exp(-a(t-s))v_s ds.

A weighted Cauchy–Schwarz inequality followed by Tonelli gives

    |x_t|^2<=(c^2/a) integral_0^t exp(-a(t-s))|v_s|^2ds,
    ||z||_L2(0,infinity)<=kappa ||w||_L2(0,infinity),
    kappa=dc/a.                                         (13)

Delay with zero negative history preserves the full infinite-time input norm. This is a PATHWISE inequality for the actual output, not Jensen applied to a formal full-state mean. Taking expectation of the path norm, or expectation of its square, proves

    G1(F)<=kappa, G2(F)<=kappa                            (14)

on the SAME full input class. The nonlinear hidden state/control need no expected norm for this step.

For a deterministic pulse `w=q 1_[0,L]`, q,L>0, direct integration of the visible ODE and its decaying tail gives

    ||z||_L2^2=(dcq/a)^2
          *[L-(1-exp(-aL))/a],
    ||w||_L2^2=q^2 L.                                   (15)

Indeed integrate `(1-exp(-as))^2` through the pulse and add the tail `(1-exp(-aL))^2/(2a)`; the boundary exponentials cancel to the displayed expression. The ratio is

    kappa sqrt(1-(1-exp(-aL))/(aL)) -> kappa              (16)

as L increases. Outputs for these inputs are deterministic even when the hidden state later has noise. Thus BOTH gains obey the matching lower bound. Consequently

    G1(F)=G2(F)=kappa in(0,infinity).                    (17)

This does not use a general G1=G2 theorem: it is the direct exact convolution law of THIS family, and gives no equality for unmatched stochastic output data.

## 6. A zero-start legal pulse with NON-H1 control despite(17)

Choose a deterministic q,S>0 and `w=q 1_[0,S]`. Before h all states are0; during[h,h+S], v=q, so the SAME rule(3) sets u=0. At deterministic t0=h+S the hidden state is exactly

    xi=(kq/b)(1-exp(-bS))>0.                             (18)

After t0, v=0 and the SAME stationary rule automatically becomes `u=-sigma^-1 y^2`. No clock-based switch, state reset, controller memory or changed initial-condition assumption is used. Future Brownian increments are fresh, so §4 applies from xi. For EVERY T>0,

    E||u||_L2(t0,t0+T)
       =sigma^-1 E (integral_(t0)^(t0+T)y_s^4ds)^(1/2)
       =infinity.                                      (19)

Therefore expected squared control energy is infinite too: finite expected squared energy would imply finite expected root by Cauchy–Schwarz. The actual FULL diffusion integral is not a true mean-zero martingale on that postinterval, and

    E y_(t0+t)<xi exp(-bt), t>0.                         (20)

State moments still obey the uniform EMS bound after the pulse, while the VISIBLE output for EVERY allowed input obeys the positive finite GLOBAL gain(17). Thus the stronger implication left open by v8 is FALSE for general rank-deficient data:

    finite uniform GLOBAL literal output gain
      + finite global RMS OUTPUT gain
      + strong all-input local-pathwise control admissibility
      + full zero-window internal EMS
      + STATE-LOC/stationary printed window information
    DOES NOT IMPLY individual free-control H1/expected-L2,
    NOR a full-state drift-only mean equation.            (21)

Both instantaneous output-price routes are absent here: R=0 and the state-only observed quadratic form is rank1, not positive definite on the full state. The v11/v13 priced H1/occupation proofs are not contradicted. The v14 coercivity-free OUTPUT norm bridge, if separately adopted, also supplies no individual control integrability and is compatible with this example. No hidden full-state mean was taken to prove(17).

## 7. Exact strictness endpoints, ALL-controller optimum and limits

The visible output is independent of u for EVERY strongly well-posed controller, including arbitrary causal nonlinear ones. Hence no admissible controller can alter the ratios in(15),(16). Control u=0 is stationary printed, nonexplosive, internally exponentially MS stable, and has finite EXPECTED control L2. It attains the SAME induced output gain kappa. This proves an exact family-level optimum without assuming an optimal linear controller for the general book problem.

For the STRICT UNIFORM convention, solvability is exactly

    exists controller with G1<gamma iff gamma>kappa.     (22)

For completeness, the POINTWISE-strict endpoint gamma=kappa is different and can be decided here. For any path v in L2, (13) gives x in L2 and `x'=-ax+cv` in L2. Since x^2 has integrable derivative2xx', its limit exists; its L2 integrability forces that limit to0. With x0=0, integration by parts therefore yields the EXACT energy identity

    c^2||v||_L2^2=||x'||_L2^2+a^2||x||_L2^2.            (23)

For a nonzero v, the first term is strictly positive: x'=0 would make x identically0 and then v=0. Thus pathwise

    ||z||_L2<kappa||w||_L2 whenever ||w||_L2>0.           (24)

For any nonzero allowed RANDOM input, this strict inequality holds on the positive-probability event of a nonzero path. Its nonnegative difference is integrable by finite N1(w), so its expectation is STRICTLY positive. Consequently

    N1(z(w))/N1(w)<kappa for EACH nonzero allowed w,      (25)

although the supremum of those ratios is kappa by(16). If(3) of the book is interpreted as this POINTWISE quantification with no uniform gap, u=0 (and the deliberately non-H1 law(3) under the frozen base admissibility) satisfies it at gamma=kappa. Gamma<kappa is excluded by long finite deterministic pulses. Hence on THIS explicit family,

    pointwise-strict solvability iff gamma>=kappa.        (26)

The printed page does not settle the missing supremum/quantifier by displaying one; (22) and(26) are two explicitly separated research readings, not competing statements under one silently changed definition. This endpoint analysis is infinite-horizon only. No analogous finite-T statement or general nonattainment theorem is asserted.

## 8. What is now proved, what is NOT, and exact imports

The new useful result is (21), with a nonzero exactly computed global output gain on ALL inputs, genuine full-state internal stability, original stationary current/window implementation and an explicit zero-start non-H1 pulse. It is not another per-input finite-output assertion. It closes the specific stronger-global-gain control-integrability shortcut, while keeping TOOL execution separate from written proof.

The additional exact family optimum/strictness distinction (22),(26) uses the uncontrollable stable visible subsystem. It is a scoped family theorem, NOT a general synthesis breakthrough. This law's bad control is NOT required for feasibility: u=0 gives the same gain and satisfies the stronger expected-control class. Therefore no separation of literal/RMS CONTROLLER EXISTENCE, no impossibility of replacing a given nonlinear law, and no universal optimality/realization theorem follows. General unmatched forcing, state-control tradeoff, arbitrary controller regularity/filtration/memory, finite horizons and arbitrary-plant same-gamma N&S remain OPEN.

Named ordinary imports: local progressively measurable state-Lipschitz SDE existence/uniqueness and stopped localization, Itô/exit estimates, Brownian radial calculus/nonhitting of a point with the stated harmonic-potential argument, deterministic Brownian time change, Gaussian spherical integration, the ordinary H1/BDG-localization martingale implication, and elementary Cauchy/Fubini/Tonelli/Sobolev integration by parts. The operative generator, radial mean, moment bounds, pulse, exact convolution and endpoint arguments are all displayed. No sharp Geiss–Scheutzow/Lenglart theorem, stochastic Riccati synthesis theorem, hidden expected-control assumption, numerical assay or unreplayed finite certificate is imported.

Complete-body independent reconstruction and parent adoption are NOT yet performed for this packet. Its classical mechanism and hidden augmentation are not claimed novel, publishable or SOTA. Same-harness written work is not formal/kernel, human/configured-family, executable/triple-finite or worldwide-priority acceptance.

## 9. Immutable process and round boundaries

The initial v15 lead was already held before v105, and a brief later own-primary scoping interval occurred AFTER the v107 review body was persisted but BEFORE its actual return. That is the DISTINCT permanent interleaving PROCESS MAJOR recorded in `owner-primary-interleaving-after-v107-body-erratum-v1.json`, SHA256 `f06ee051612f8497f5a96e6221ff0a434e327049794024fad648c850a93f7bcf`. It is not called first-post-ACK discovery or preregistration. The later prospective PRIMARY ACK `primary-resumption-after-v107-ack-v1.json`, SHA256 `03d6037f11c9bcc8540b4b7ef84a4e2b5cbd3283d2d08435bd471a957ebb9d97`, actual20:18:22, preceded the CURRENT own-source reads/further development and this body. That does not cure the earlier interval or the separate old post-v100 primary-ACK-order and private-written exactness findings.

All old pinned sources, reviews, park-v2 and addenda remain unchanged. The four old withdrawn-permission eval records retain ZERO admitted verification credit, and none was rerun. No current scientific interpreter/eval/calculator/program/CAS/enumeration/solver/replay/CLI/nestedagent/build/test/formatter or GO occurred. All parent/other-owner findings and actual-clock qualifications remain. No global clean-thought/runtime census, new owner, deadline reset or96-hour closeout is claimed. SAME original problem/eighteen owners, science cutoff2026-10-27T11:05:38-07:00 and deadline2026-10-27T12:35:38-07:00; scientific HOLD remains binding.
