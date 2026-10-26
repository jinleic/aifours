# info-3 — literal stochastic H-infinity preview synthesis

Observed freeze clock: **2026-10-23T14:02:03-0700**, `/bin/date '+%Y-%m-%dT%H:%M:%S%z'`. Agent: InfoHinfPreview. Contract-v2 and both parent errata read. Written research only; no scientific execution is admitted.

## Exact source and model

The actual page images read are `information-science/stochastic-hinf-preview-control/sources/book/pdfpage-0695.png`, `pdfpage-0696.png`, `pdfpage-0697.png`: printed pp.674–676 of the 2011 information-science volume. The book defines the **pathwise** norm first, then prints equation (3) with expectations outside those norms. The literal model (equation (1)) is continuous time:

\[
 dx_t=(Ax_t+Bu_t+Cw_{t-h})\,dt+(A_0x_t+B_0u_t)\,dW_t,
 \qquad z_t=D_0x_t+D_1u_t,
\]

where all matrices are constant and compatible, `h>=0`, and `W` is Brownian motion. The displayed information pattern (equation (2)) is `u(t)=F(x(t),w(s):t-h<=s<=t)`. Equation (3) asks for attenuation

\[
 {\mathbb E(\int_a^b |z_t|^2dt)^{1/2}\over
  \mathbb E(\int_a^{b-h}|w_t|^2dt)^{1/2}}<\gamma.
\]

The prose explicitly asks **both** bounded finite horizons and `b->infinity`. Neither discrete time nor mean-square energy is the target.

## Quantifier freeze and disclosed interpretations

For `a=0`, `x(0)=0`, `w=0` at negative times, fix `h>=0`, a horizon `T>h` or `T=infinity`, constant plant data, and `gamma>0`. Brownian future increments are independent of `F_t`. Disturbances are all progressively measurable `w` with `E integral_0^(T-h)|w|^2<infinity`; deterministic disturbances are a subset, not a replacement. The literal norm is `N1(f)=E sqrt(integral |f|^2)`. On infinite horizons the input interval is `[0,infinity)`; compactly supported inputs remain admissible. Where a result also holds for all `N1(w)<infinity`, that enlargement will be stated separately.

The target is a **necessary and sufficient, non-tautological synthesis criterion and controller** for

`exists admissible F: sup_(w!=0 adapted) N1(z_F,w)/N1(w) < gamma`.

Well-posed, nonanticipative, event-local laws with zero response to zero data are required. Finite-horizon time dependence may be explicit. An impossibility proof may enlarge the controller class to all adapted history-dependent controls, but an existence claim must supply the book's state/window form. Uniform strict induced-norm feasibility, zero initial state, and adaptedness fill omissions of the book rather than change its printed objective. Infinite-horizon internal mean-square stabilization, if assumed, is an additional conventional restriction and will never be inferred from a gain statement without proof. No arbitrary controller-memory reset is available.

## Baselines, not new discoveries

Read: current dossier README §§1–5; `work/literal_continuation.md` in full; `evidence/literal-continuation-20261014/verification.json`; and review-resolution receipt. Baselines are the candidate mean-square Riccati theory; constant-matrix finite-horizon separation at `gamma=6` (literal feasible for every adapted disturbance while every controller has mean-square gain greater than14), its control-dependent-noise extension, and the exact time-gated benchmark L3 outside the constant-matrix class. **None will be re-counted.** That continuation explicitly leaves the infinite-horizon issue open and warns that a single-pulse bound or independent-block slogan is insufficient.

Primary literature actually opened this session:

* [Wang–Fu–Zhang author manuscript, submitted 2018-12-20, published SIAM2020 DOI10.1137/18M1232942](https://www.eng.newcastle.edu.au/~mf140/home/Papers/SICON_2020.pdf): notation on manuscript p.2 defines a mean-square Hilbert sequence norm; equation(2.1) on p.3 is a **difference equation**; equation(2.4) is finite-horizon `[0,N]`. It is not an import for the literal criterion.
* [Wang–Zhang–Chen–Yu2014 DOI landing page](https://doi.org/10.11918/j.issn.0367-6234.2014.07.017): continuous-time state-dependent-noise preview; prior dossier's full-text receipt identifies finite horizon, `B0=0`, and mean-square sufficient conditions. This session's DOI and actual PDF endpoint are accessible, but its full theorem is not yet independently re-read; the old scratch PDF path no longer exists. No Riccati theorem from it is imported.
* [Liu–Seiler2026, Regret of H-infinity Preview Controllers, arXiv2602.01420v2](https://arxiv.org/html/2602.01420v2), abstract and §II equation(1): discrete-time LTI and pathwise quadratic sequence costs, not continuous-time multiplicative-noise literal synthesis.
* [Li–Hou–Zhang–Deng2026, arXiv2601.05460v1](https://arxiv.org/html/2601.05460v1), abstract and §2: finite-horizon stochastic **difference** systems, norms `sqrt(sum E||q(k)||^2)`. Its Hilbert-space Riccati result does not repair the objective mismatch.

Exact `preview|Riccati|riccati|H-infinity|H∞|Burkholder` screen of local `math/CONTENTS.md`, `math/overview.tex`, and remote `openai/math/main/CONTENTS.md` returned no matches. The live remote repository README was also read. This is a bounded catalogue screen, not a claim that every manuscript was read or that no related claim exists. Broader regex searches returned only unrelated Laughlin-text false positives.

**Open status: UNCERTIFIED-OPEN.** The book is an actual historical open statement; no matched modern resolution was located in this bounded source screen. Search silence is not proof of openness or novelty. Strongest matched literal baseline is the repository's finite-horizon separation, not a general synthesis theorem.

## Missing ingredient and consequential delta

The non-Hilbert `L1(Omega;L2(time))` norm cannot be squared into the quadratic stochastic game. Adapted input energy is random; Jensen changes the denominator and proves no uniform ratio comparison. A valid criterion must either treat the pathwise energy accumulators explicitly, or prove a genuine transfer theorem with exact information/horizon hypotheses. A complete infinite-horizon obstruction under the **literal norm**, with explicit quantified input families and no false controller resets, would be a consequential partial result beyond the finite-horizon separation. It will not be called full synthesis.

## First bounded written attack, verification, redirect

First investigate whether time-homogeneity and repeatable independent Brownian blocks force **unbounded infinite-horizon literal gain** in a positive scalar mean-square-unstable mode, although its one-pulse expected path norm can be finite. The proof must build finite-energy admissible inputs, preserve actual continuous time and any fixed preview delay, supply the positivity/no-reset argument, and justify every limit. If a full parameter criterion is possible, derive it rather than report only one numerical example. Then inspect which exact synthesis conclusions follow and where effective actuation blocks extension to arbitrary controllers.

Verification route: self-contained written derivation, exact classical imports named and primary-source checked, immutable proof snapshot and SHA256 pin for parent plus genuinely separate in-harness reconstruction. No simulator, solver, arithmetic program, compilation, Lean, or executable certificate check will run without a named parent GO. Metadata clocks, hashing and source extraction are not scientific assays. Correctness, import trust, scope, novelty and significance stay separate.

Redirect condition: a current primary source settles the literal target, or the proposed no-go is merely the old finite-horizon norm separation / a restatement of an already imported theorem. Report prior resolution to the parent and propose a distinct replacement outside the18-slot roster before changing problem. A new theorem only for a scalar or fixed-feedback subcase remains explicitly partial; it does not silently replace the frozen general target.
