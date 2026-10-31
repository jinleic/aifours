# F550 — Written review of the positive-lag fixed-law candidate

**Disposition: 0 FATAL / 1 MAJOR / 0 MINOR mathematical findings.** The compact Gaussian characterization, strict deterministic bounds, long-lag reduction, admissible adapted-burst lower bounds, and lag-regularity conclusions are supported at their stated given-law scope by the reconstruction below. However, §6.1 contains a false fixed-\(L^2\) convergence assertion and requires an additive correction before adoption.

**Materialization:** No repository file was written. The write device refused the attempted reviewer-prefixed process receipt because it permits only device transport and session scratch. This is the complete review body for parent materialization; no alternative filesystem-writing route was used.

## 1. Binding, chronology, and evidence limits

The review is bound to:

- Manifest: `5283031e662fa2ca094cf6bbd6ce170882a8d26157bf28808d9d65d3d4f03919`.
- Freeze receipt: `cfe4994ec9eccc59c89a09e54baf7e0fb755b9807836071ef464dca2a6e13bd8`.
- Literal packet: `dfb1d613c848ffee8c91570c46835d1a57a22f50b23ddb87d5c5470dab365f0b`.
- S1 candidate: `89baa76a5e641fec4d3c4bf243ad430048c35a18642bae601087b18e39e9890a`.
- S2 adopted zero-lag disposition: `3fd8129086f29c1d44469ba976d5e9fa35e26be537c49f19dd098b44ef4ee3ba`.

These are **supplied parent observations**, not child-recomputed hashes. The supplied clock `2026-10-30T13:07:49-0700 PDT` is not represented as this review’s completion time.

Before reading the mathematical packet, I completely read the manifest, freeze receipt, dispatch receipt, parent metadata supply, and all twelve required status-only controls through their endings. I then sent the direct administrative pre-body ACK to `agent://Main`.

After that ACK, I read the complete packet sequentially in raw, nonoverlapping windows of at most twenty lines, through the final `S2|25` ending at packet line 728. Coverage comprises **S1 labels 1–701 and S2 labels 1–25**. The manifest reports S1 LF 700; the packet contains the final logical label `S1|701`, which was read. No independently executed newline count is claimed. Subsequent direct checks were confined to the admitted S1 source lines 320–339 and 544–563.

All quarantined episodes and their proof, method, selection, planning, confidence, reporting, and other consumers remained **NONINPUT**. No excluded link, sibling review, author code, public-source continuation, or held mathematical payload was opened.

**Execution: NOTRUN.** No shell, Git, scientific program, interpreter, CAS, solver, enumeration, build, test, lint, formatter, external CLI, installation, deletion, credential operation, or infrastructure mutation was performed. No new selected mathematical instance or numerical parameter probe was used.

## 2. Finding M1

**Title:** Replace the fixed \(L^2\) burst limit with a moving Gaussian comparison  
**Priority:** P2  
**Confidence:** 1.00  
**Severity:** MAJOR — local false convergence assertion; not a falsification of the intended gain bound  
**File:** `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f494-stochastic-hinf-positive-lag-adapted-operator-frontier/review-v1.md`  
**Lines:** 329–333

When \(c_H>0\), the shifted outputs in §6.1 do not converge in \(L^2(\Omega;\mathcal H)\) to a fixed \(F_0aZ\) on the original probability space. The displayed error is instead the error against \(F_0aZ_\delta\), where \(Z_\delta=(W_{\tau+\delta}-W_\tau)/\sqrt{\delta}\). For \(0<\varepsilon\le\delta\), these comparisons satisfy \(\mathbb E\|F_0a(Z_\delta-Z_\varepsilon)\|^2=2c_H^2(1-\sqrt{\varepsilon/\delta})\), so they are not \(L^2\)-Cauchy as both widths tend to zero. Replace the asserted fixed strong limit by the valid moving comparison and use its invariant normal law to obtain convergence of expected norms. The claimed lower bound survives this correction, but the stated convergence assertion does not.

The required repair is additive because the candidate is frozen.

## 3. Actual law, E1 extension, and general bounds

**Claims reviewed:** S1 23–252.  
**Disposition:** SUPPORTED, conditional on the explicitly imported S2 zero-lag weighted inequality.

Let
\[
H=T-\tau>0,\qquad
v_t=w_{t-\tau}\mathbf1_{\{t\ge\tau\}}.
\]
This delayed coefficient remains progressive in the original filtration. Applying the imported zero-lag weighted inequality to \(v\) gives
\[
\mathbb E\|z(w)\|_T
\le
r\,\mathbb E
\left(\int_0^H w_s^\top G(H-s)w_s\,ds\right)^{1/2}.
\]
This imports an **upper inequality**, not unrestricted shifted-filtration sharpness.

For E1 inputs, the candidate’s pointwise cutoffs
\[
w^{(k)}_s=w_s\mathbf1_{\{|w_s|\le k\}}
\]
are progressive and E2. Their differences converge in \(L^1(\Omega;L^2)\) by pathwise dominated convergence, without assuming \(\mathbb E\|w\|^2<\infty\). The imported inequality therefore makes the actual cutoff outputs Cauchy in \(L^1(\Omega;L^2)\).

The identification with the actual local solution is valid. Since an E1 input has finite path energy almost surely, its local martingale
\[
M_t=\int_\tau^t e^{-Pr}B w_{r-\tau}\,dW_r
\]
exists. The bracket of the cutoff difference is bounded by a deterministic constant times \(\|w-w^{(k)}\|^2\), tending to zero almost surely. Stopping at bracket level \(\delta\) gives the stated probability estimate; taking \(k\to\infty\), then \(\delta\downarrow0\), yields uniform convergence in probability of the actual cutoff solutions. Thus the Banach-space limit is the actual local output, not a surrogate on another probability space.

The weighted norm satisfies
\[
|Q_H(u)-Q_H(v)|\le c_H\|u-v\|_T.
\]
Passing to the limit establishes the E1 bound. Both expectations in each nonzero cutoff ratio converge, proving equality of the E1 and E2 suprema.

For \(c_H>0\), the strict clock inequality is also valid. If, for \(s>0\) and \(a\ne0\),
\[
a^\top G(H-s)a=c_H^2|a|^2,
\]
equality in both intervening PSD inequalities forces
\[
\int_{H-s}^H|Ce^{Pv}Ba|^2\,dv=0.
\]
Analyticity then forces this kernel to vanish identically in direction \(a\), contradicting \(a^\top G(H)a=c_H^2|a|^2>0\). Consequently,
\[
Q_H(w)<c_H\|w\|_T
\]
on every nonzero input path, including paths whose energy is entirely in the unused tail. Taking expectations proves the strict \(r c_H\) bound for every nonzero input.

This proves nonattainment of that **upper bound**, not nonattainment of the actual supremum.

## 4. Compact Gaussian characterization of deterministic gain

**Claims reviewed:** S1 294–395.  
**Disposition:** SUPPORTED; the erroneous fixed strong-limit sentence is excluded.

### 4.1 Continuity and Gaussian existence

For
\[
(F_sa)(u)=\mathbf1_{\{u\ge s\}}Ce^{P(u-s)}Ba,
\]
one has
\[
\|F_sa\|_{\mathcal H}^2=a^\top G(H-s)a.
\]
The change of support has vanishing measure, and the exponential kernel is uniformly continuous on the remaining compact region. Because the input dimension is finite, this proves operator-norm continuity of \(s\mapsto F_s\).

Hence
\[
\mathcal C=\{F_sa:(s,a)\in[0,H]\times S^{m-1}\}
\]
is compact in \(\mathcal H\). Each
\[
Q_\mu=\int(F_sa)\otimes(F_sa)\,d\mu
\]
is positive trace class, with trace at most \(c_H^2\). A centered Hilbert Gaussian with this covariance exists: its spectral series has summable second moments. Its expected norm depends only on its covariance law.

### 4.2 Continuity of the objective and existence of a maximum

For every \(\epsilon>0\), compactness of \(\mathcal C\) supplies a finite-dimensional subspace \(V\) such that
\[
\sup_{v\in\mathcal C}\|(I-\Pi_V)v\|\le\epsilon.
\]
Therefore
\[
\mathbb E\|(I-\Pi_V)Z_\mu\|^2\le\epsilon^2
\]
uniformly over \(\mu\), and
\[
\left|J(\mu)-\mathbb E\|\Pi_VZ_\mu\|\right|\le\epsilon.
\]

In \(V\), covariance entries are integrals of bounded continuous functions on the compact parameter space, so they vary continuously under weak convergence of measures. Positive matrix square roots are continuous, including at singular covariance matrices; applying them to a finite standard normal vector proves continuity of the finite-dimensional Gaussian expected norm.

Thus \(J\) is a uniform limit of continuous functions. Weak compactness of probability measures on the compact metric space \(K\) gives a maximum.

This finite-dimensional distributional comparison is not a claim that the physical Brownian bursts possess a fixed strong limit.

### 4.3 Equality with the actual deterministic-input supremum

A normalized deterministic active profile has covariance \(Q_{\mu_v}\), so its ratio is at most \(D_H\).

Conversely, consider a finite atomic measure. Its atoms can be represented by disjoint input intervals lying inside \([0,H]\), with lengths tending to zero and locations approaching the atom times. Repeated atom times are handled by distinct nearby intervals. At time zero the intervals approach from the right; at time \(H\) they approach from the left. An interval representing mass \(p_j\) and direction \(a_j\) carries amplitude \(\sqrt{p_j/|I_j|}\,a_j\), so total input energy is exactly one.

Its covariance tends to the atomic covariance by continuity of \(F_s\). Gaussian expected norms then converge by the continuity argument above. Finite atomic measures are weakly dense on compact \(K\), completing the reverse inequality.

Thus \(D_H\) is exactly the deterministic L2-input supremum. The existence of a maximizing **measure** does not establish its representability by an actual L2 profile.

## 5. Strict deterministic bounds

**Claims reviewed:** S1 397–441.  
**Disposition:** SUPPORTED.

### Upper bound

For every \(\mu\),
\[
J(\mu)^2\le\mathbb E\|Z_\mu\|^2=\operatorname{tr}Q_\mu\le c_H^2.
\]
If the attained compact maximum were \(c_H>0\), equality in Jensen would make \(\|Z_\mu\|\) almost surely constant. But a nonzero covariance has a nondegenerate one-dimensional Gaussian projection, which is unbounded and cannot be dominated by a constant norm. Therefore
\[
D_H<c_H.
\]
The compact maximum is essential: pointwise strictness alone would not imply strictness of the supremum.

### Lower bound

Take the author’s top eigenvector \(a\), and write \(f=F_0a\), \(g=F_sa\), with \(0<s<H\). Both are nonzero. The second vanishes before \(s\), while analyticity prevents the first from vanishing throughout that interval. They are therefore noncollinear, including when \(CBa=0\).

Write
\[
f=c_He_1,\qquad g=\alpha e_1+\beta e_2,\qquad\beta\ne0.
\]
The covariance of the two-atom Gaussian is
\[
(1-\theta)ff^\top+\theta gg^\top.
\]
Its Gaussian norm law is represented by
\[
j(\theta)=
\mathbb E\sqrt{(1-\theta)c_H^2X^2+\theta(\alpha X+\beta Y)^2}.
\]
Indeed, the displayed quadratic form has the same covariance eigenvalues; its matrix has trace
\((1-\theta)c_H^2+\theta(\alpha^2+\beta^2)\) and determinant
\(\theta(1-\theta)c_H^2\beta^2\).

For the derivative, put \(A=(\alpha X+\beta Y)^2\) and \(B=c_H^2X^2\). Concavity of the square root makes
\[
\frac{\sqrt{B+\theta(A-B)}-\sqrt B}{\theta}
\]
increase as \(\theta\downarrow0\). It is bounded below by \(-\sqrt B\). After adding that integrable bound, monotone convergence applies. The pointwise derivative is
\[
\frac{A-B}{2c_H|X|}.
\]
Its negative part is integrable. After adding \(c_H|X|\), its expectation is that of
\[
\frac{A+B}{2c_H|X|},
\]
whose expectation diverges because conditioning on \(X\) contributes the nonzero term \(\beta^2/|X|\).

Thus \(j'(0+)=+\infty\), and \(j(\theta)>j(0)=\kappa c_H\) for sufficiently small positive \(\theta\). The atomic-to-profile approximation preserves a fixed strict improvement. Consequently,
\[
\boxed{\kappa c_H<D_H<c_H}
\]
for every nonzero actual analytic kernel, without any extra nondegeneracy assumption.

## 6. Correct physical interpretation of the burst limit

This supplies the reconstruction needed to repair M1.

Let \(Y_\delta\) denote the actual shifted output of the author’s single burst and define
\[
Z_\delta=\frac{W_{\tau+\delta}-W_\tau}{\sqrt\delta}.
\]
Hilbert-space Itô isometry gives exactly
\[
\mathbb E\|Y_\delta-F_0aZ_\delta\|^2
=
\frac1\delta\int_0^\delta\|(F_s-F_0)a\|^2\,ds
\longrightarrow0.
\]
Because every \(Z_\delta\) has the same standard normal law,
\[
\left|\mathbb E\|Y_\delta\|-\kappa c_H\right|
\le
\bigl(\mathbb E\|Y_\delta-F_0aZ_\delta\|^2\bigr)^{1/2}
\longrightarrow0.
\]

This proves the lower witness and convergence in distribution to the rank-one Gaussian law. It does **not** produce a fixed \(L^2\) random-variable limit on the original space. No new coupling is necessary or asserted.

## 7. Exact long-lag reduction

**Claims reviewed:** S1 443–497.  
**Disposition:** SUPPORTED.

When \(H\le\tau\), progressive measurability makes the entire active profile, as a separable L2-valued random element, \(\mathcal F_\tau\)-measurable. The Brownian path after \(\tau\) is independent of \(\mathcal F_\tau\).

Conditional on that sigma-field, the active profile is deterministic and the output is centered Gaussian with covariance
\[
\int_0^H(F_sw_s)\otimes(F_sw_s)\,ds.
\]
Therefore
\[
\mathbb E[\|z(w)\|_T\mid\mathcal F_\tau]
\le D_H\|w\|_{L^2[0,H]}.
\]
For E1 inputs, this follows through the progressive cutoffs and conditional L1 convergence; no unconditional second moment is required.

Taking expectations and discarding unused-tail energy gives \(L_\tau\le D_H\). The deterministic approximation established above gives the reverse inequality:
\[
\boxed{L_\tau=D_H\qquad(T/2\le\tau<T).}
\]
At \(T=2\tau\), the common endpoint has no positive-duration reaction opportunity, so the same argument applies.

For \(c_H>0\),
\[
\kappa c_H<L_\tau<c_H<r c_H.
\]
The author’s stated scalar subcase follows from this theorem and \(G(H)=H\); it is not needed as a new selected diagnostic. These results refute transfer of the zero-lag formula to this long-lag regime, but do not evaluate \(D_H\) in closed form.

## 8. Adapted bursts in the original filtration

**Claims reviewed:** S1 499–588.  
**Disposition:** SUPPORTED as an expected-norm/law limit, not as convergence to a fixed original-space random vector.

The schedule satisfies
\[
t_{j-1}+\delta=s_j.
\]
Thus all variables used in \(a_j=h_j(Z_1,\ldots,Z_{j-1})\) are measurable by physical input time \(s_j\). Input intervals are disjoint, applied-noise intervals are disjoint, and the last applied interval ends at
\[
t_N+\delta=N(\tau+\delta)<T.
\]
The resulting process is progressive and E2. Its path norm is exactly the stated square root of the sum of squared amplitudes.

For clarity, retain the width dependence and write \(Z_{\delta,j}\), \(a_{\delta,j}\), and
\[
Y_\delta^*=
\sum_{j=1}^N F_{(j-1)\tau}
h_j(Z_{\delta,<j})Z_{\delta,j}.
\]
Let \(\widehat Y_\delta\) be the actual output. Itô isometry gives
\[
\mathbb E\|\widehat Y_\delta-Y_\delta^*\|^2
=
\sum_j\frac1\delta
\int_{s_j}^{s_j+\delta}
\mathbb E\|(F_s-F_{(j-1)\tau})a_{\delta,j}\|^2\,ds.
\]
Boundedness of the \(h_j\) and operator-norm continuity of \(F_s\) make this tend to zero.

For every width, the \(Z_{\delta,j}\) are independent standard normals. Hence the joint law of \(Y_\delta^*\) and the input norm is independent of the width. Expected output norms converge and the stated ratio lower bound follows.

No convergence of \(h_j(Z_{\delta,<j})\) to a fixed random variable is needed. This matters because the \(h_j\) are merely Borel and may be discontinuous.

The candidate’s §8 explicitly claims convergence of **expected norms**; with its previously defined width-dependent normals, that claim has this valid interpretation. It is not a second independent mathematical finding. No optimization of these witnesses, sharpness assertion, or positive-lag cutoff has been established.

## 9. Lag monotonicity, regularity, and short-lag adaptation

**Claims reviewed:** S1 590–634.  
**Disposition:** SUPPORTED, with the zero-lag value retained as the declared S2 import.

For \(\tau_1<\tau_2\), remove the \(\tau_2\)-unused tail and delay its input by \(d=\tau_2-\tau_1\). This input remains progressive, preserves its norm, and satisfies
\[
\widetilde w_{t-\tau_1}=w_{t-\tau_2}.
\]
The physical driving coefficient and therefore the actual output are unchanged. Thus \(L_{\tau_1}\ge L_{\tau_2}\).

For each fixed E1 input, zero-extended time translations converge pathwise in L2 and are dominated in norm by \(2\|w\|_T\). Dominated convergence yields \(L^1(\Omega;L^2)\) continuity. Applying the imported zero-lag E1 bound to differences gives continuity of its actual output in the delay.

Taking nearly maximizing inputs proves lower semicontinuity of the supremum. Together with monotonicity this gives **right continuity**. It does not establish general left continuity at interior delays.

As \(\tau\uparrow T\), the bound \(L_\tau\le r c_{T-\tau}\) tends to zero. At zero lag, using the adopted value \(L_0=r c_T\) and fixed nearly sharp inputs gives
\[
\lim_{\tau\downarrow0}L_\tau=r c_T.
\]

When \(c_T>0\), \(r c_T>c_T\). Therefore sufficiently small positive lags satisfy
\[
L_\tau>c_{T-\tau}>D_{T-\tau}.
\]
This is a genuine existence result for improvement over all deterministic profiles. It supplies neither a computed threshold nor a demonstration that the particular finite adapted-burst examples already realize that improvement.

## 10. Zero cases, history, feasibility, and remaining scope

**Claims reviewed:** S1 254–292 and 636–701.  
**Disposition:** SUPPORTED at the stated scope.

- For \(\tau\ge T\), zero prehistory gives zero output; a terminal-time integrand value contributes no Itô energy.
- For \(H>0\), \(G(H)=0\) is equivalent to vanishing of the continuous analytic kernel. Taylor expansion and Cayley–Hamilton give precisely \(CP^kB=0\), \(k=0,\ldots,n-1\). Conversely, a nonzero kernel gives positive gain through the corrected deterministic witnesses.
- An uncharged prescribed history with finite positive expected output norm makes the ratio unbounded by scaling the charged future input to zero. This is explicitly a different problem, not an extension of the zero-history theorem.
- The strict-feasibility statements follow from the supremum definition. At the actual critical value, pointwise strictness is equivalent to nonattainment; a uniform positive margin requires a strictly larger threshold.
- In the long-lag regime, equality in the conditional upper bound would require almost every nonzero realized active profile to be a deterministic maximizer, with no wasted tail. Conversely, such a deterministic profile would attain the gain. Thus the stated optimizer-representation question is the correct remaining attainment obligation.
- The E2 RMS gain follows from Itô isometry and narrow deterministic bursts. Its strict clock inequality proves nonattainment of that RMS supremum. This does not settle attainment of the literal expected-path-norm gain.

The original-source observations referenced in the candidate are not independently reconstructed here: their source body is outside this wave’s mathematical inputs. The candidate’s explicit exclusion of controller synthesis, coefficient-level source equivalence, multiple drivers, state noise, feedthrough, and infinite horizon is retained.

## 11. Claim-by-claim disposition

| Claim | Status | Acceptance boundary |
|---|---|---|
| Actual causal E1 extension and equality of E1/E2 suprema | **SUPPORTED** | Conditional on the adopted S2 weighted inequality |
| Strict per-input \(r c_H\) upper bound | **SUPPORTED** | Not sharpness or actual-supremum nonattainment |
| Complete zero classification | **SUPPORTED** | Zero prehistory and stated finite dimensions |
| Fixed original-space \(L^2\) single-burst limit | **REFUTED** | M1, S1 329–333 |
| Single-burst expected-norm limit and lower bound | **SUPPORTED** | Moving Gaussian comparison |
| Compact Gaussian characterization of deterministic gain | **SUPPORTED** | Measure maximum; profile attainment not inferred |
| \(\kappa c_H<D_H<c_H\) for every nonzero kernel | **SUPPORTED** | Analytic finite-dimensional given law |
| \(L_\tau=D_H\) for \(T/2\le\tau<T\) | **SUPPORTED** | Original filtration and zero prehistory |
| Adapted-burst lower bounds | **SUPPORTED** | Width-dependent comparison and invariant joint law |
| Monotonicity and right continuity | **SUPPORTED** | No general interior left-continuity claim |
| Zero-lag limit and sufficiently-short-lag adaptation advantage | **SUPPORTED** | Exact zero-lag gain imported from S2 |
| General short-lag exact gain and actual attainment | **INCONCLUSIVE / NOT ESTABLISHED** | Correctly left unpaid |
| Closed-form evaluation of \(D_H\) | **INCONCLUSIVE / NOT ESTABLISHED** | Variational characterization only |
| General controller synthesis or source equivalence | **NOT ESTABLISHED** | Outside this review’s accepted scope |

## Overall correctness

**incorrect**

The frozen candidate contains a false fixed-\(L^2\) convergence assertion in §6.1 and needs an additive repair. The intended gain conclusions listed as supported above admit the written reconstructions given here, using moving comparisons rather than invented original-space limits and retaining the exact zero-lag import boundary.

**Confidence:** 0.99.

This is same-harness written review only. It provides no independent-family, human, formal/kernel, novelty, priority, or general source-equivalence certification.