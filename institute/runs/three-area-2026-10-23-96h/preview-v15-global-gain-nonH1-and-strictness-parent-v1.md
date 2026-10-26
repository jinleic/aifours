# Preview v15 — finite global output gain, non-H1 control and strictness endpoints

Actual returned `/bin/date` before this disposition: **2026-10-26T04:11:25-0700 PDT**. Parent read the complete255-line v15, complete191-line scalar dependency, complete173-line v14 context, complete17-line model-source boundary and BOTH actual252/284-line review bodies through their endings BEFORE this write. Parent also NOW directly viewed the whole printed675 raster through its visible bottom, not merely its hash or OCR.

## Three separate supported claims

Both full reviews report **0 new mathematical FATAL / MAJOR / MINOR** for each claim and its dependency/application. Parent supports them as ordinary WRITTEN results at the exact classical SDE/analysis interfaces below, not as a general synthesis solution or a process-clean verdict.

1. **All-input admissibility, full-state EMS and exact positive finite global gain.** For EVERY positive a,b,c,k,d,sigma, every finite h>=0 and every canonical progressive expected-L2 input, the SAME stationary left-tap law in the actual two-state plant is strongly nonexplosive, locally PATHWISE-control-L2, uniformly same-input state-local Lipschitz, and internally full-state mean-square stable on zero window. Its two output gains are exactly G1=G2=kappa=dc/a.
2. **Per-law counterexample to control-integrability/mean inference.** A legal deterministic pulse from ZERO state gives infinite expected control path-L2 norm on EVERY positive interval after the DELAYED pulse ends, and a false full-state drift-only mean equation, despite the finite GLOBAL output gains and internal EMS above. Local pathwise control energy remains finite. This is not merely one-input finite output or the old scalar law’s unproved global gain.
3. **All-controller optimum and two distinct strictness readings.** The visible subsystem is uncontrollable, so the optimum is kappa for all admissible competing controllers and is attained by stronger-admissible u=0. Uniform strict gain G1<gamma is feasible iff gamma>kappa. Pointwise strict ratio for EACH nonzero input, without a uniform gap, is feasible iff gamma>=kappa. These are INFINITE-horizon statements.

**Not controller-existence separation:** u=0 attains the same optimum while meeting stronger expected-control admissibility. No general optimal replacement impossibility, arbitrary-plant same-gamma theorem, linear optimality, finite-horizon result or full-book N&S follows.

## Actual plant and source interpretation

```text
dx = (-a x + c v) dt,
dy = (-b y + k v) dt + sigma u dW,
z = d x,  v(t)=w(t-h),
u = -y^2/sigma * 1_(v=0).
```

The diffusion actuator, hidden forcing and visible output are genuinely nonzero. B=0 means control enters diffusion, not that the actuator vanishes. The SAME law uses current state and one allowed fixed left tap; it has no controller clock, reset, extra memory or future noise. Its input discontinuity is explicit; its state-local constant on radius R is2R/sigma uniformly for the SAME input tuple. Fixed translation preserves dt-times-probability equivalence of input versions.

The actual page675 shows current-state/window F, expectation OUTSIDE each path norm, `<gamma`, h nonnegative, and a finite/infinite horizon distinction. It shows NO supremum symbol. The two strictness conventions above are explicitly different research readings, not an invented printed supremum. The single image is not a whole-book proof or general admissibility theorem.

## Parent hand reconstruction

- **All inputs:** the hidden log Lyapunov function log(1+y^2) has generator at most1+k|v|. Localized martingales are legitimately integrable; expected-L2 input gives finite expected prefix integral of|v|. The exit estimate divided by log(1+R^2) rules out explosion. Path continuity then gives local pathwise control-L2, without taking its expectation. This argument covers arbitrary allowed progressive inputs, not just the pulse.
- **Scalar law and EMS:** the radius of3D Brownian motion has reciprocal Y solving dY=-Y^2 d beta; the auxiliary3D process derives the LAW of the actual one-Brownian equation, not extra physical noise. The deterministic time change theta_b(t)=(1-exp(-2bt))/(2b) yields y_t=exp(-bt)Y_theta. The explicit inverse-square Gaussian split gives E Y_s^2<=100q^2 for all s; reflection covers negative starts and0 is absorbing. Together with visible exponential decay this gives full-state EMS100 exp(-2min(a,b)t). No control H1 is assumed.
- **Strict mean and non-H1:** the actual radial Gaussian integral gives E y_t=exp(-bt)q P(|N(0,theta_b(t))|<=1/q), STRICTLY less than exp(-bt)q for t>0,q>0. If the square-root bracket expectation were finite, the ordinary nonsharp H1/BDG-localization implication would make the diffusion integral true/UI mean-zero. State moment bounds permit drift Fubini, giving the contradictory exponential mean. The displayed good-lambda argument supplies a nonsharp64/7 bound; no optional sharp norm-transfer theorem is used.
- **Actual zero start:** a positive input q on[0,S] leaves hidden state(kq/b)(1-exp(-bS))>0 at t0=h+S, because the SAME left-tap law has u=0 during delayed forcing. Thereafter the same law becomes the reciprocal-Bessel diffusion. The contradiction therefore applies on every positive post-t0 interval; later deterministic starts use conditional restart and positivity. “Post-pulse” does NOT mean before delayed forcing clears when h>0.
- **Global output gains:** the visible output is the exact convolution. Weighted Cauchy and Tonelli give the PATHWISE norm bound ||z||<=kappa||w||; finite delay preserves the full infinite-time norm. Taking either expected norm or expected squared norm gives both upper bounds, without a hidden-state mean. Finite deterministic pulses satisfy ||z||^2=(dcq/a)^2[L-(1-exp(-aL))/a], and their ratios tend to kappa. Hence both global gains equal kappa on ALL inputs.
- **Endpoint distinction:** x and xprime lie in time-L2 and x(0)=0. The integrable derivative of x^2 gives its limit0 at infinity. Thus c^2||v||^2=||xprime||^2+a^2||x||^2. Every nonzero path has a strictly positive derivative term, so its output ratio is strictly less than kappa although the supremum is kappa. For random nonzero input, the norm defect is integrable, nonnegative and positive on a positive-probability event, so its EXPECTATION is strictly positive. There is no uniform gap across inputs. Since u=0 is an internally stable stronger-admissible realizer and no controller changes the visible convolution, both iff endpoint statements follow.

## Dependencies, residual and permanent qualifications

Named ordinary inputs are progressive local-state-Lipschitz SDE existence/uniqueness/localization, stopped Itô and exit estimates, Brownian harmonic annulus/radial calculus/time change, Gaussian integration, ordinary H1/BDG localization, Cauchy/Fubini/Tonelli and Sobolev integration by parts. Their specialized hypotheses and actual plant ties are reconstructed; this is not formal verification of probability foundations. The optional sharp Geiss–Scheutzow/Lenglart result remains NOT_RECONSTRUCTED and unused. No Riccati synthesis theorem or hidden expected-control-L2 restriction is imported. Complete v14 is comparison/context, NOT a correctness premise of v15’s direct convolution proof. Other linked old book pages/author libraries are not freshly claimed read from their hashes.

The general original gap remains prescribed-gamma literal N1 synthesis and actual printed-window realization for unmatched stochastic forcing, arbitrary ranks and state/control tradeoffs, plus general optimal replacement, controller regularity/memory/filtration and finite horizons. This exact family settles a per-law integrability shortcut and its own optimum only. Classical mechanism/hidden augmentation has no novelty clearance.

All FOUR preview-owner findings remain distinct: earlier private exactness, post-return/pre-primary-ACK order, post-body/pre-ACTUAL-return live primary interleaving, and false receipt counts. Corrected actual receipts154/106 do not license166/118 or nonexistent extra coverage; the reported failures were not rerun. Reviewer Olson’s two exactness majors, AME’s earlier pre-ACK/exactness/read-order findings, later header-exposure disclosure and every parent/other-owner history remain. New parent v17/v18/v19 findings remain separate. No mathematical0 count is process cleanliness, uninterrupted activity or a global cognition/runtime census. N4 stays UNKNOWN with unestablished historical child exit; auxiliary214 stays UNADMITTED/STOP.

No scientific interpreter/calculator/program/CAS/enumeration/solver/replay/build/test/modelCLI/newGO or frozen-source edit occurred in this adoption. Same original18 owners, science cutoffOctober27 11:05:38 and deadline12:35:38 PDT remain; no configured-family/human/formal/kernel/executable/triple/novelty or96-hour-closeout claim.

## Live binding after complete reading

|Source|LF|Bytes|SHA256|
|---|---:|---:|---|
| `information-science/evidence/three-area-20261023-96h/parallel-18/stochastic-hinf-preview/literal-preview-synthesis-consolidated-v15-finite-gain-nonH1-controls.md` | 255 | 22506 | `b7a2984a8ee1985c5c1a38c4d78e729fdef82a35a4a9fb1deabf99c481b7a571` |
| `information-science/evidence/three-area-20261023-96h/parallel-18/stochastic-hinf-preview/literal-preview-synthesis-consolidated-v8-Rdef-integrability.md` | 191 | 15416 | `b19dcd670bfbf99d79d8abdaa3948a50c84e8b99923596680b4d5990acd341e1` |
| `information-science/evidence/three-area-20261023-96h/parallel-18/stochastic-hinf-preview/literal-preview-synthesis-consolidated-v14-sequential-probability-buffers.md` | 173 | 16601 | `d956c0827df54c7e9e1c5a63a0af00673208ec24c7c6bd4d4d44cd0f4395a8c8` |
| `mathematics/evidence/three-area-20261023-96h/parallel-18/ordered-olson/peer-review-v110-C-v1.md` | 252 | 41547 | `581a4883b99b2412293cab3550ab3b68f8d8da62a8ebf41f7d2de050ac443ac6` |
| `physics/evidence/three-area-20261023-96h/parallel-18/ame46-support/peer-review-v110-D-v1.md` | 284 | 34005 | `2a38c347d768464783bda4d66320aead6bbb54760bebd51f2d5d1e4101e0d0bf` |
| `institute/runs/three-area-2026-10-23-96h/preview-v3-model-source-boundary-v1.md` | 17 | 2636 | `c66113762df23694d3446fa48d716da9bc0c6a5e953d115cd706694017fef78a` |
| `information-science/stochastic-hinf-preview-control/sources/book/pdfpage-0696.png` | image | 454740 | `f2e84bd77d6e38d23b3f598edacdebcd7648a37ba8148f9207be87b8ed70624b` |
