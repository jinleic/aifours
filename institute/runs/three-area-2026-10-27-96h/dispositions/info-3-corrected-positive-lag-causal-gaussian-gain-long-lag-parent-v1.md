# Positive-lag fixed stochastic law: corrected causal extension and exact long-lag reduction

**Disposition: same-harness written support for the CORRECTED composite, with two distinct independently authored exact finite-interface scenarios run by parent.** This concerns exactly one scalar Brownian driver, finite-dimensional real matrices P,B,C, zero input prehistory, one original usual filtration and progressive input:

\[dx_t=Px_t\,dt+B w_{t-\tau}\,dW_t,\qquad x_0=0,\quad z_t=Cx_t.\]

The literal gain is \(L_\tau=\sup E\|z\|_{L^2[0,T]}/E\|w\|_{L^2[0,T]}\), with expectations OUTSIDE path norms. It is NOT the RMS ratio. Set H=(T−tau)_+, \(G(u)=B^T\int_0^u e^{P^Tv}C^TCe^{Pv}\,dv B\), \(c_H=\sqrt{\lambda_{max}G(H)}\), and \(\kappa=\sqrt{2/\pi}\). Inputs remain \(\mathcal F_s\)-progressive at physical INPUT time s; the shifted noise filtration does not give disturbance preview.

Two distinct named imports are retained from the adopted [zero-lag actual-law disposition](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-3-matrix-e1-causal-extension-and-fixed-law-composition-parent-v1.md): its E2 weighted expected-path-norm upper inequality with constant r, and its separate exact zero-lag gain \(L_0=r c_T\), including lower sharpness. This record does not reprove the imported Bellman/generalized-Itô antecedent or derive zero-lag sharpness merely from the upper bound.

## 1. Mandatory additive correction and historical finding

The original [f494 author](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f494-stochastic-hinf-positive-lag-adapted-operator-frontier/review-v1.md) Section6.1 asserted a shrinking actual Brownian burst converges in original-space L2 to a SINGLE fixed Gaussian vector. **That assertion is false and is WITHDRAWN**, not silently edited. [The additive moving-Gaussian erratum](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f494-stochastic-hinf-positive-lag-adapted-operator-frontier/parent-moving-gaussian-burst-limit-erratum-v1.md) is operative. Original f549 reports0F/0M/1m; f550 reports0F/1M/0m; f551 also flags the SAME issue as minor. Parent conservatively records **one MAJOR mathematical proof-assertion defect**, not three distinct defects; the historical reviewer counts remain immutable.

For the actual width-dependent \(Z_\delta=(W_{\tau+\delta}-W_\tau)/\sqrt\delta\), Hilbert Itô isometry gives

\[E\|Y_\delta-F_0aZ_\delta\|^2=\delta^{-1}\int_0^\delta\|(F_s-F_0)a\|^2\,ds\to0.\]

Each \(Z_\delta\) has the same normal LAW, so EXPECTED norms converge to \(\kappa c_H\), giving the original lower-bound consumer. For nested widths, \(E|Z_\delta-Z_\epsilon|^2=2(1-\sqrt{\epsilon/\delta})\); at a fixed nonunit ratio the family is not L2-Cauchy. No fixed original-space strong limit, new coupling or anticipative input is claimed. Two fresh full-composite reviews f563/f564 report0F/0M/0m for the CORRECTED composite only; they do not backdate or erase the original defect.

## 2. Causal E1 extension, upper bound and zero cases

Let E1 be inputs with \(E\|w\|_T<\infty\), E2 those with \(E\|w\|_T^2<\infty\). Pointwise progressive cutoffs \(w1_{|w|\le k}\) converge in L1 of the time-L2 norm. The named weighted E2 import makes their outputs Cauchy in L1 of the output Hilbert norm. Bracket localization plus Doob’s inequality identifies that limit with the ACTUAL local Itô solution, not a surrogate. Therefore E1/E2 literal gain suprema agree, and

\[E\|z\|_T\le r\,E\left(\int_0^H w_s^T G(H-s)w_s\,ds\right)^{1/2}.\]

If H>0 and c_H>0, analyticity of \(Ce^{Pv}Ba\) makes the weighted-clock bound STRICT for every nonzero input: its ratio is strictly below \(r c_H\). This excludes attainment of that UPPER BOUND, not necessarily attainment of the actual supremum or a uniform margin there.

With zero history, tau≥T gives L_tau=0. For0<tau<T, L_tau=0 iff c_H=0 iff \(CP^kB=0\) for k=0,…,n−1. An uncharged prescribed prehistory is a different problem: it makes the ratio infinite only under the stated positive finite expected prehistory-output norm hypothesis, not merely because the history is nonzero.

## 3. Exact compact Gaussian deterministic gain and long-lag theorem

Define \((F_sa)(u)=1_{u\ge s}Ce^{P(u-s)}Ba\) in the output Hilbert space and, for a probability measure on \([0,H]\times S^{m-1}\), \(Q_\mu=\int(F_sa)\otimes(F_sa)d\mu\), \(J(\mu)=E\|Z_\mu\|\) for the centered Gaussian of covariance Q_mu. The compact-image/finite-dimensional-tail argument makes J continuous and its maximum **D_H** attained as a MEASURE. Atomic measures are approximated by actual deterministic L2 energy bursts; therefore D_H is exactly the deterministic-input supremum. Existence of a maximizing measure does NOT prove representability by an actual maximizing profile.

For c_H>0, compactness and strict Jensen give \(D_H<c_H\). A second noncollinear impulse direction gives an infinite positive right derivative of the two-atom Gaussian expected norm, proving \(\kappa c_H<D_H\); this is a written covariance-law argument, not a pathwise identity between two Gaussian representations. Thus all positive-lag gains satisfy \(D_H\le L_\tau\le r c_H\).

If **T/2≤tau<T**, then H≤tau: the whole actual input profile is \(\mathcal F_\tau\)-measurable, while the applied Brownian increments after tau are independent. Conditioning makes its output Gaussian with its ACTUAL profile covariance. Taking expectations proves \(L_\tau\le D_H\), and deterministic profiles give the reverse inequality:

\[\boxed{L_\tau=D_H,\qquad \kappa c_H<L_\tau<c_H<r c_H}\quad(c_H>0).\]

The endpoint T=2tau is included. This is an exact variational reduction, not a closed-form evaluation of D_H, and disproves transferring the unrestricted zero-lag value \(r c_H\) to all long positive lags.

## 4. Genuinely causal lower bursts, lag regularity and attainment

For N tau<T, choose delta>0 with N(tau+delta)<T and input burst starts \(s_j=(j-1)(\tau+\delta)\), applied starts \(t_j=s_j+\tau\). Then \(t_j+\delta=s_{j+1}\): the next bounded-Borel amplitude uses only increments observed by its INPUT time. Inputs and applied-noise intervals are separately disjoint. Own input and its applied interval may overlap if delta>tau; this is allowed because its amplitude was fixed at s_j. No claim of own-interval disjointness is needed.

The corrected multi-burst comparison keeps \(Z_{\delta,j}\) and \(h_j(Z_{\delta,<j})\) width-dependent. Its Itô-isometry error against the actual output vanishes, while their joint law is width-independent. This yields the stated actual adapted lower family, not an optimized gain or a claim that these particular bursts improve D_H.

The actual gain is nonincreasing and right-continuous in tau. It tends to0 as tau rises to T; as tau falls to0, it tends to \(r c_T\) using the SEPARATE exact-zero-lag import. If c_T>0, sufficiently small positive lags satisfy \(L_\tau>c_H>D_H\); this is an existence statement, not an explicit lag threshold or optimized burst.

Strict feasibility at the ACTUAL critical value \(\gamma=L_\tau\) holds iff the actual supremum is NOT attained; a uniform positive margin requires \(\gamma>L_\tau\). In the long-lag regime, an attaining random input exists iff a maximizing Gaussian measure is represented by an actual deterministic L2 profile with no wasted tail. This representation/attainment question remains unresolved. The distinct E2 RMS gain is c_H and is nonattained for positive c_H, but that does not determine the literal expected-path-norm gain.

## Evidence and limits

[Original immutable author](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f494-stochastic-hinf-positive-lag-adapted-operator-frontier/review-v1.md) · [operative additive correction](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f494-stochastic-hinf-positive-lag-adapted-operator-frontier/parent-moving-gaussian-burst-limit-erratum-v1.md) · [original f549 review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f549-positive-lag-causal-e1-and-long-lag-conditioning-written-review/review-v1.md) · [original f550 review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f550-positive-lag-gaussian-variational-strictness-and-causal-bursts-review/review-v1.md) · [independent finite source/report](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f551-positive-lag-exact-causal-timing-and-gaussian-covariance-controls/review-v1.md) · [f563 fresh corrected Gaussian review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f563-corrected-positive-lag-gaussian-limit-and-long-lag-written-review/review-v1.md) · [f564 fresh corrected causal/consumer review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f564-corrected-positive-lag-causal-extension-and-all-consumers-review/review-v1.md) · [actual two-scenario parent receipt](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f551-positive-lag-exact-causal-timing-and-gaussian-covariance-controls/parent-independent-finite-run-v1-receipt.json). Parent displayed all701 original, the complete35-line erratum,281/368 original reviews,242/230 fresh reviews and811 independent finite-report/source logical lines. The new whole-composite reviews each report0F/0M/0m with the two named imports retained; the original one-MAJOR finding is NOT cleared.

After full static read and GO, parent ran the independently authored 103-line standard-library Fraction source for TWO DISTINCT declared scalar timing cases, once each: short lag(T,tau,delta,N)=(3,1,1/8,2) and long lag(3,2,1/8,1). Both exit0 with empty stderr, combined observed0.0334s. Exact output records physical input/applied endpoints, observation timing, impulse Gram/covariance trace and determinant, rectangular covariance moments, and nested standardized increment covariance1/2 and squared L2 distance1. No Gaussian expectation, D_H, adapted gain, controller or optimum was computed. A parent variable-name typo occurred AFTER both successful executions and their outputs were written; the receipt was reconstructed from retained actual process results, with NO rerun.

General short-lag adapted gain, closed D_H evaluation, actual optimizer representation/nonattainment, critical feasibility, coefficient-level source equivalence and controller synthesis remain unpaid. No general state noise, multiple Brownian drivers, feedthrough or infinite horizon is inferred. All held episodes AND consumers remain NONINPUT; no independent-family,human,formal/kernel,novelty or original-target completion is claimed.
