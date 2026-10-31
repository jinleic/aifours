# Review f138-hinf-finite-e2-witness-catalan-gap — review-v1

Reviewer: same-harness scientific reviewer (omp subagent). Observed clock before this write: 2026-10-29T03:47:03Z (Wed Oct 28 20:47:03 PDT 2026). Verdict and all claims below are at the **exact given-law scope** only.

## 0. Receipts

- Manifest `review-waves/f138-hinf-finite-e2-witness-catalan-gap/manifest-v1.json`: SHA-256 `f1510d1abf929aa03e4e4b4eb27c52360d9047be9c5ff2a2b0c21659e011943b`, 3304 B — matches the assigned SHA (observed 2026-10-29T03:34:15Z).
- Authority read: `contract-addendum-2-frontier-first-owner-direction-v1.json` SHA `5e18c2d4b94656fc12b5cfce4122889fa6073e24a21f1e0062c79d846b6037ce`.
- Inputs re-verified (observed 2026-10-29T03:34:29Z), all full SHA-256 / bytes / LF / CR=0 as declared, and read completely in declared order:
  1. `frontier-20261028-explicit-finite-brownian-stopping-gap.txt` `a5a2d4527f7e5ad0a24bd2865665031dd44e812dccde5bd5408cba8a166378d2` 3376 B, 65 LF (finite witness predecessor).
  2. `frontier-20261028-brownian-exit-catalan-certified-gap.txt` `9e0c703dabfc47fbb6856da91ce7a761780d27c3c4fb55dfabf586780f56a8fb` 3842 B, 54 LF (Catalan certified gap).
  3. `frontier-20261028-brownian-exit-catalan-exact-check.py` `c333ec796fbfec2d34f2054af445e37684fe529b88f19e141c1454434d825b3b` 961 B, 26 LF (author checker: **read only, never executed or imported**).
  4. `frontier-20261028-catalan-strengthened-finite-e2-witness.txt` `a8cb383f407eeba75bc6c0ab98fe553b7f838e8f0eca99168d8cb428ba94f9cb` 1751 B, 13 LF (candidate).
- Overlays/errata: none declared in the manifest; a search of the source directory, `review-waves/` and `checkpoints/` for the input names found no erratum/overlay file for any input (only cross-references from `frontier-20261028-checkpoint-adapted-gap-v1.json` and `frontier-20261028-martingale-literal-gain-stopping-bracket.txt`, which are not inputs and were not read).
- Reviewer artifacts written in this directory (all `reviewer-` prefixed, plus this file):
  - `reviewer-exact-controls-v1.py` SHA `2237006d4ee81b19782439ad9e53a77e28b2e97f16eafb028146aac2b56b1238` 18045 B; run 2026-10-29T03:42:46Z–03:42:53Z, exit 1; log `reviewer-exact-controls-v1.log` SHA `0962fc42ce353f6151c6e25936de769648db72b26116df61badcfea6bc6ca641` 5835 B: **38 PASS / 2 FAIL — both FAILs are in the non-load-bearing numerical Part C** (C3, C5), caused by a reviewer artefact (eigen-series coefficient `((-1)**k)/(2*k+1)` evaluated as a double, floor ≈1.7e-17). Parts A/B (all exact `fractions.Fraction` statements): 31/31 PASS.
  - `reviewer-exact-controls-v2.py` SHA `2fe18fe3e84a2ee108575e2437ea9c43af205703c786680f207abda9db026d94` 18213 B; diff to v1 = file-name lines plus exactly one line (coefficient made `mp.mpf`); run 2026-10-29T03:43:59Z–03:44:07Z, exit 1; log `reviewer-exact-controls-v2.log` SHA `8fcee919e9fe08a84b99ab14f372ee2ff5832478fbacf354f608dfd0e8aaef6a` 5763 B: **39 PASS / 1 FAIL**; the remaining FAIL is C5, a 1e-18 tolerance missed by the tail-integral quadrature route only (observed agreement 5.0e-18, singular 1/(2√t) endpoint at 30 digits). Parts A/B: 31/31 PASS, identical to v1.
  - `reviewer-probe-quadrature-v1.py` SHA `1ab9b818f367d1c5eba86149e66767c57ab83d657872177655c2871dcad35145` 2168 B; run 2026-10-29T03:45:21Z–03:45:30Z, exit 0; log `reviewer-probe-quadrature-v1.log` SHA `6df332ba4f9139c33fc5ac31f343b78e565927cd32c0cb7e75c7d52e2cd46086` 412 B: with the substitution t=u² (singularity removed) and 40 digits, the tail-integral route agrees with the closed form to 1.1e-41, confirming C5 was quadrature error, not a discrepancy.
- No author contact, web search, external model/paid API, Git, deletion, publication, infrastructure change, or repository build/lint/format/test suite was used. Local tools: Python 3.14.3, `fractions`, `mpmath` 1.4.1, `numpy` 2.4.3.

## 1. Fixed law, classes and norms (as reconstructed from the inputs)

- Law: $x_0=0$, $dx_t = w_t\,dW_t$, $z_t = x_t$ on $[0,T]$, $W$ a standard Brownian motion with (augmented) filtration $(\mathcal F_t)$; realized from the original structure by $u=w$ with unit control-diffusion coefficient. Finite horizon $T>h\ge 0$, preview length $h$, $S:=T-h$; disturbance support constrained to $[0,S]$. Within this given-law scope the preview enters **only** through that support constraint; the controller is fixed ($u=w$), so no preview-controller advantage is modelled.
- Norms (stated exactly, as required): $\|z\| := \big(\int_0^T x_t^2\,dt\big)^{1/2}$ and $\|w\| := \big(\int_0^T w_t^2\,dt\big)^{1/2}$, both $L^2[0,T]$ path norms; the compared quantity is the **ratio of expectations of path norms** $\;E\|z\| / E\|w\|$ ("literal expected-path gain"). It is *not* the RMS ratio $(E\|z\|^2)^{1/2}/(E\|w\|^2)^{1/2}$ — see §2.7 for why this distinction is load-bearing.
- Deterministic class: nonzero $w\in L^2[0,T]$ (support in $[0,S]$ or not — the bound below holds either way); $\gamma_{\det}:=\sup E\|z\|/\|w\|$.
- Adapted finite class ("E2" in the inputs): $(\mathcal F_t)$-progressively measurable $w$ with $E\int_0^T w^2<\infty$; the witness below additionally has $\|w\|^2\le 4096$ a.s. and support in $[0,\delta]\subset[0,S/2]$.

## 2. Independent reconstruction

### 2.1 Every deterministic input has ratio $\le\sqrt T$
For deterministic $w\in L^2[0,T]$, $x_t=\int_0^t w\,dW$ is Gaussian with $E x_t^2=\int_0^t w_s^2\,ds\le\|w\|^2$ (Itô isometry). By Jensen and Tonelli,
$E\|z\| \le (E\|z\|^2)^{1/2} = \big(\int_0^T\!\int_0^t w_s^2\,ds\,dt\big)^{1/2}\le (T\|w\|^2)^{1/2}=\sqrt T\,\|w\| = \sqrt T\,E\|w\|.$
Hence $\gamma_{\det}\le\sqrt T$ (in fact strictly $<\sqrt T$ for each nonzero $w$, since Jensen is strict for a non-degenerate $\|z\|$; the candidate only needs $\le$). **Verified.**

### 2.2 The adapted finite witness ($N=4096$, $\delta=\min(S/2,\,T/8192)$)
Define $B_s := \sqrt{N/\delta}\,W_{\delta s/N}$ ($s\ge0$): a standard Brownian motion for $\mathcal G_s:=\mathcal F_{\delta s/N}$ (variance $s$). Let $\tau:=\inf\{s:|B_s|\ge1\}$ (a $\mathcal G$-stopping time) and $\rho:=\delta(\tau\wedge N)/N\in[0,\delta]$; $\{\rho\le t\}=\{\tau\wedge N\le tN/\delta\}\in\mathcal G_{tN/\delta}=\mathcal F_t$, so $\rho$ is an $\mathcal F$-stopping time. Put
$w_t := \sqrt{N/\delta}\;\mathbf 1_{\{t<\rho\}},\qquad t\in[0,T].$
- **Adapted/nonanticipating:** $w$ is left-continuous and $\mathcal F_t$-adapted, hence predictable (progressive). ✔
- **Finite:** $\|w\|^2=(N/\delta)\rho=\tau\wedge N\le N=4096$ a.s.; $E\|w\|^2=E[\tau\wedge N]\le1$; support $[0,\rho]\subset[0,\delta]\subset[0,S/2]\subsetneq[0,S]$ (control B7 checks $\delta>0$, $\delta\le S/2$, $\delta<S$, $\delta\le T/8192$ over 30 exact $(T,h)$ cases, both branches of the min exercised; branch switch at $h/T=4095/4096$, B7b). ✔
- **State:** $x_t=\sqrt{N/\delta}\,W_{t\wedge\rho}=B_{(tN/\delta)\wedge(\tau\wedge N)}$; for $t\ge\delta\ge\rho$, $x_t=B_{\tau\wedge N}$. Hence $\|z\|^2=\int_0^T x_t^2dt\ \ge\ (T-\delta)\,B_{\tau\wedge N}^2$, i.e. $E\|z\|\ge\sqrt{T-\delta}\,E|B_{\tau\wedge N}|$, while $E\|w\|=E\sqrt{\tau\wedge N}\le E\sqrt\tau$. Therefore
$\dfrac{E\|z\|}{E\|w\|}\ \ge\ \sqrt{T-\delta}\;\dfrac{E|B_{\tau\wedge N}|}{E\sqrt{\tau\wedge N}}\ \ge\ \sqrt T\cdot\sqrt{1-\delta/T}\cdot E|B_{\tau\wedge N}|\cdot\dfrac1{E\sqrt\tau}.$ ✔ (This is the inequality the inputs attribute to "(2)–(3) of the named source"; it is re-derived here without that source.)

### 2.3 Exit-time law rebuilt
- $E\tau=1$: $B_s^2-s$ is a martingale; optional stopping at $\tau\wedge n$ gives $E[\tau\wedge n]=E B^2_{\tau\wedge n}\le1$, so $E\tau\le1$, $\tau<\infty$ a.s., $|B_\tau|=1$, and bounded convergence gives $E\tau=E B_\tau^2=1$. ✔ (Cross-checked exactly: $E\tau=\frac{32}{\pi^3}\beta(3)$ from the series below; exact enclosure $[0.9999999989,\,1.0000000000]\ni1$, control B9; numerically $=1$ to $<10^{-18}$, C6.)
- Survival function: killed generator $\tfrac12\partial_x^2$ on $(-1,1)$ has eigenfunctions $\cos\!\big((2k+1)\pi x/2\big)$, eigenvalues $\lambda_k=(2k+1)^2\pi^2/8$; expanding $\mathbf 1$: $c_k=\int_{-1}^1\cos((2k+1)\pi x/2)\,dx\big/\!\int_{-1}^1\cos^2 = 4(-1)^k/((2k+1)\pi)$. So $P_0(\tau>t)=\frac4\pi\sum_{k\ge0}\frac{(-1)^k}{2k+1}e^{-(2k+1)^2\pi^2t/8}$ — the expansion quoted in input 2. ✔ **Independent cross-check:** the reflection-principle (method-of-images) representation $P(\tau>t)=\sum_{n\in\mathbb Z}(-1)^n[\Phi((2n+1)/\sqrt t)-\Phi((2n-1)/\sqrt t)]$ agrees with the eigen-series to $5.1\times10^{-29}$ at seven times $t\in\{0.05,\dots,5\}$ (C3, v2).
- Half moment: $E\sqrt\tau=\int_0^\infty\frac{P(\tau>t)}{2\sqrt t}dt$ (valid since $E\sqrt\tau\le\sqrt{E\tau}<\infty$); $\int_0^\infty e^{-\lambda_k t}\frac{dt}{2\sqrt t}=\frac{\sqrt\pi}{2\sqrt{\lambda_k}}=\frac{\sqrt{2\pi}}{(2k+1)\pi}$; termwise integration is legitimate because $\sum_k\frac1{2k+1}\cdot\frac{\sqrt{2\pi}}{(2k+1)\pi}<\infty$ (Fubini on absolute values). Hence
$E\sqrt\tau=\frac4\pi\sum_k\frac{(-1)^k}{2k+1}\cdot\frac{\sqrt{2\pi}}{(2k+1)\pi}=\frac{4\sqrt{2\pi}}{\pi^2}\,G,\qquad G=\sum_{k\ge0}\frac{(-1)^k}{(2k+1)^2},$ ✔
  equivalently $(E\sqrt\tau)^2=32G^2/\pi^3$. **Second independent cross-check:** from the classical transform $Ee^{-\lambda\tau}=\operatorname{sech}\sqrt{2\lambda}$ and $\sqrt s=\frac1{2\sqrt\pi}\int_0^\infty(1-e^{-\lambda s})\lambda^{-3/2}d\lambda$, one gets $E\sqrt\tau=\sqrt{2/\pi}\int_0^\infty\frac{1-\operatorname{sech}u}{u^2}du$, which agrees with $4\sqrt{2\pi}G/\pi^2$ to $2.3\times10^{-19}$ (C2); the tail-integral route agrees to $1.1\times10^{-41}$ once the endpoint singularity is removed (probe). All three classical representations coincide; the closed form is not in doubt.
- **Exact enclosure (my own route, no square roots, no Machin, no alternating-tail argument for $G$):** $\pi$ via $\pi/4=\arctan\frac12+\arctan\frac13$ with strict consecutive-partial-sum brackets of the Gregory series (width $<10^{-20}$, A1); $G$ via the paired positive series $G=\sum_{m\ge0}\big[\frac1{(4m+1)^2}-\frac1{(4m+3)^2}\big]$ truncated at $M=200$ with tail $\le\frac4{(4M+1)^3}+\frac1{2(4M+1)^2}$ (A2; $G\in(0.915964812930,\,0.915965600014)$). Then
$32G_{lo}^2/\pi_{hi}^3>(9305/10000)^2$ and $32G_{hi}^2/\pi_{lo}^3<(9306/10000)^2$ (A4, A5), so $\;9305/10000<E\sqrt\tau<9306/10000\;$ and $1/E\sqrt\tau>10000/9306$ (A6, A7); 12-decimal outer bracket $E\sqrt\tau\in[0.930526981772,\,0.930527781370]$. **The candidate's imported bound $E\sqrt\tau<9306/10000$ is independently certified.** Negative controls: the same enclosure correctly refuses $E\sqrt\tau>9306/10000$ and $E\sqrt\tau<9305/10000$ (NA1, NA2); the slipped formulas $32G^2/\pi^2$ and $16G^2/\pi^3$ fall outside the bracket (NA3, NA4); an $M=2$ truncation is too loose to certify (NA5).

### 2.4 $E|B_{\tau\wedge N}|\ge 4095/4096$
On $\{\tau\le N\}$, $|B_{\tau\wedge N}|=|B_\tau|=1$; so $E|B_{\tau\wedge N}|\ge P(\tau\le N)\ge1-E\tau/N=1-1/N=4095/4096$ (Markov, $E\tau=1$). ✔ (B5; numerically $P(\tau>4096)\approx3\times10^{-2195}$, so the Markov step is crude but rigorous. The smallest $N$ for which the three certified factors exceed 1 is $N=15$, B8.)

### 2.5 $\sqrt{1-\delta/T}\ge 8191/8192$
$\delta\le T/8192$ (B7) gives $y:=\delta/T\in(0,1/8192]$ and $\sqrt{1-y}\ge1-y\ge8191/8192$ because $0<1-y<1\Rightarrow(1-y)\ge(1-y)^2$ (B6 exact grid; algebraic). ✔

### 2.6 Combination
$E\sqrt{\tau\wedge N}\le E\sqrt\tau<9306/10000$ makes the last factor **strict**; hence
$\dfrac{E\|z\|}{E\|w\|}\;>\;\sqrt T\cdot\frac{8191}{8192}\cdot\frac{4095}{4096}\cdot\frac{10000}{9306}\;=\;\frac{2329315625}{2168455168}\,\sqrt T\;=\;1.074182053368\ldots\sqrt T\;>\;\frac{107}{100}\sqrt T\;>\;\sqrt T\;\ge\;\gamma_{\det}.$
Exact: product equals $2329315625/2168455168$ in lowest terms (B1, B1b), $>107/100$ (B2), $<108/100$ and in $(1.0741,1.0742)$ (B2b, B2c). Predecessor arithmetic also exact: $\frac{8191}{8192}\frac{4095}{4096}\frac{1944}{1943}=\frac{8150741235}{8149532672}=1+\frac{1208563}{8149532672}$ (B3, B4), and its crude chain $P(\tau\le\tfrac14)\ge\varphi(2.5)>1/243$, $1-E\sqrt\tau=\tfrac12E(\sqrt\tau-1)^2\ge p/8>1/1944$ was checked by hand (true values $0.0910$ and $0.0695$ vs. bounds $0.0041$, $0.00051$). ✔

### 2.7 Scope remark (boundary, not a defect)
For **every** progressive $w$ with $E\int w^2<\infty$, Itô isometry gives $E\|z\|^2=\int_0^TE\!\int_0^tw^2\,ds\,dt\le T\,E\|w\|^2$, so the RMS ratio is $\le\sqrt T$ for adapted inputs too. The certified $>7\%$ gap therefore exists **only** for the expected-path-norm ratio $E\|z\|/E\|w\|$ (a Jensen-gap effect: the witness makes $\|w\|=\sqrt{\tau\wedge N}$ random while $\|z\|\approx\sqrt T$ is nearly deterministic). This matches the candidate's own wording ("literal ratio, not an RMS") and must travel with any citation of the result.

## 3. Negative controls (all behaved as required; v1/v2 logs)
- Wrong $\delta=T/2$ (ignores preview support): with $h=3T/4$ the support $[0,\delta]\not\subset[0,S]$ (NB1a) and the certified factor squared $(1-\delta/T)\,f_N^2f_{cat}^2<1$ — **no gap certified** (NB1b).
- Wrong $\delta=T/4096$: the stated factor $1-\delta/T\ge8191/8192$ **fails** (NB2a); honest note: with the weaker factor $4095/4096$ the product would still exceed 1 (NB2b), so the large-$\delta$ error is the one that destroys the gap.
- Wrong stopping rule = deterministic time $\sigma\equiv1$ (Jensen slack vanishes, $E|B_1|/E\sqrt1=\sqrt{2/\pi}$): $2/\pi<1$, indeed $<0.64$, so the factor is $<0.8$ — **no gap** (NB3, NB3b; Monte Carlo $E|B_1|\approx0.796$, C8).
- $N=1$: Markov factor $1-1/N=0$, certified ratio 0 — **no gap** (NB4). Untruncated stopping ($N=\infty$) would have unbounded support and could not satisfy supp $\subset[0,S]$ with probability one; the truncation is load-bearing for admissibility, not only for finiteness.

## 4. Non-load-bearing numerical plausibility (not proof)
Discretised Monte Carlo of the actual witness ($T=1,h=0$, $N=4096$, $\delta=1/8192$, Brownian step $10^{-4}$ in fast time, 20000 paths, seed 20261028): $E\|w\|\approx0.93645\ (\pm0.0026)$, $E\|z\|\approx1.00578$, ratio $\approx1.0740$ versus certified $>1.07418$ and exact limit $1/E\sqrt\tau=1.07466$; the simulated value lies within one standard error of the exact value, with the two $O(\sqrt{ds})$ overshoot biases (inflating both $E\sqrt{\tau_d}$ and $E|B_{\mathrm{stop}}|$) nearly cancelling. Plausibility only; no part of the verdict rests on it.

## 5. Findings
- **FATAL:** none.
- **MAJOR:** none.
- **MINOR-1 (dependency wording):** inputs 1, 2 and 4 attribute the scaling/adaptedness/state computation and the limiting statement $\gamma_{\mathrm{prog},2}\ge\sqrt T/E\sqrt\tau$ to the pinned source `frontier-20261028-martingale-stopping-progressive-gap.txt` (SHA `af79d012…`), which is not an input of this review. The finite-witness conclusion was re-derived here **without** that source (§2.2), so the verdict does not depend on it; the limiting/supremal statement in input 2 §1 and "approached by finite E2 stopping inputs" (input 2 §3) remain unreviewed.
- **MINOR-2 (class definition):** the precise original definition of the input class "E2" (and whether the deterministic class is $L^2[0,S]$ or $L^2[0,T]$) is not among the inputs. The witness is shown to be predictable, with $\|w\|^2\le4096$ a.s., $E\|w\|^2\le1$, support in $[0,S/2]$; the deterministic bound holds for either support convention. Any definition for which these properties suffice is covered; no other is claimed.
- **MINOR-3 (strength of the deterministic bound):** $\gamma_{\det}\le\sqrt T$ is not tight (each nonzero deterministic input has ratio strictly below $\sqrt T$), so $1.0741\ldots$ is a **lower bound** on the witness-versus-class factor; the ">7%" headline is conservative, not sharp, and the finite choice loses only $\approx0.045\%$ against the $\delta\to0,N\to\infty$ value $1/E\sqrt\tau$.
- **MINOR-4 (reviewer artefact, disclosed):** reviewer controls v1 had a double-precision coefficient in a numerical cross-check; corrected in v2 (one-line diff). Parts A/B were unaffected and identical across v1/v2. The one remaining v2 numerical tolerance miss (C5) is quadrature error, shown by the probe to vanish (1.1e-41) when the endpoint singularity is removed.

## 6. Verdict (exact given-law scope)
**VERIFIED — no FATAL/MAJOR.** For the fixed law $dx=w\,dW$, $z=x$, $x_0=0$, every finite $T>h\ge0$, with $\|\cdot\|=L^2[0,T]$ path norms and ratio $E\|z\|/E\|w\|$: the single explicit adapted input of §2.2 with $N=4096$, $\delta=\min((T-h)/2,\,T/8192)$ is predictable, has $\|w\|^2\le4096$ a.s. and support in $[0,(T-h)/2]$, and satisfies
$E\|z\|/E\|w\|>\tfrac{2329315625}{2168455168}\sqrt T>1.07\sqrt T\ge\gamma_{\det}$,
i.e. a certified $>7\%$ (exactly $>7.418\%$) gap over the entire deterministic-input class. Every fraction was re-derived exactly in reviewer code; the Catalan-type bound $E\sqrt\tau<9306/10000$ was re-certified by an independently structured exact enclosure; the exit-time law was rebuilt analytically and cross-checked against two further classical representations.

Conditional dependencies of this verdict: standard Brownian-motion facts only — Itô isometry for $L^2$ progressive integrands, optional stopping for $B_s^2-s$, and the killed-heat eigenfunction expansion of $P_0(\tau>t)$ on $(-1,1)$ (re-derived in §2.3 and numerically coincident with the reflection-principle series to $5\times10^{-29}$).

**Explicitly NOT established or implied by this verdict:** no true (optimal-control / synthesis) gain equality or value; no exact progressive gain (only a lower bound on the witness ratio); no strict E1/E2 pointwise endpoint transfer; no synthesis, positive-gain controller, or selected-reference calibration claim; no gap under the RMS criterion (§2.7 shows none exists for this law); no novelty, formal/kernel, human, or independent-family clearance — this is a same-harness review.

## 7. Unreviewed dependencies
1. `frontier-20261028-martingale-stopping-progressive-gap.txt` SHA `af79d012825ac5fd8c3be882a540d5cac37b3666de10d87c1b7f3f68aad504ba` (pinned stopping source: original scaling/adaptedness computation, limiting statement $\gamma_{\mathrm{prog},2}\ge\sqrt T/E\sqrt\tau$, the asserted "approached by finite E2 stopping inputs").
2. The original problem statement defining the input classes E1/E2, the literal gain criterion, the role of preview $h$ in the controller, and the full H∞ structure from which the fixed law is "realized by $u=w$"; this review takes the given-law scope exactly as stated in the inputs.
3. `frontier-20261028-checkpoint-adapted-gap-v1.json` and `frontier-20261028-martingale-literal-gain-stopping-bracket.txt` (reference these inputs; not read).
4. The author checker `frontier-20261028-brownian-exit-catalan-exact-check.py` was read, not executed; its bracketing logic (Machin $\pi$ with 11/10- and 2/3-term partial sums; $G$ via 201-term alternating partial sum and next term $1/403^2$) is consistent with a valid enclosure on inspection, but its PASS output is not relied upon here.
5. Novelty / literature status of the Jensen-gap witness and of the identity $E\sqrt\tau=4\sqrt{2\pi}G/\pi^2$: not assessed (no web search permitted).
