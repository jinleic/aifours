# Additive correction: moving Gaussian burst comparisons, not a fixed strong limit

**Native parent observation before composition: 2026-10-30T13:17:52-0700 PDT.** This additive erratum corrects the frozen [f494 author](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f494-stochastic-hinf-positive-lag-adapted-operator-frontier/review-v1.md), SHA89baa76a5e641fec4d3c4bf243ad430048c35a18642bae601087b18e39e9890a. The original body is retained unchanged. Its Section6.1 assertion of convergence in L2 on the original Brownian probability space to one fixed F0a Z is **FALSE and WITHDRAWN**. No adopted positive-lag result exists yet; the corrected composite still requires its own parent disposition. [f549](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f549-positive-lag-causal-e1-and-long-lag-conditioning-written-review/review-v1.md) records0F/0M/1m and [f550](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f550-positive-lag-gaussian-variational-strictness-and-causal-bursts-review/review-v1.md) records0F/1M/0m for the SAME error; parent conservatively records one MAJOR mathematical proof-assertion defect, not two distinct defects. Neither review refutes the intended expected-norm lower bound.

## Corrected single-burst statement and proof

Keep the original assumptions, H=T−tau>0, Hilbert output space L2([0,H];R^p), top unit vector a of G(H), cH=norm(F0a), and actual deterministic input w_delta(s)=delta^−1/2 a on[0,delta]. Let Y_delta be its ACTUAL shifted output on the original probability space. Define the WIDTH-DEPENDENT random variable

Z_delta=(W_(tau+delta)−W_tau)/sqrt(delta).

The exact Hilbert Itô-isometry comparison is

E norm(Y_delta−F0a Z_delta)^2 = delta^−1 integral_0^delta norm((Fs−F0)a)^2 ds → 0.

Every Z_delta has the standard-normal LAW. Thus, with kappa=sqrt(2/pi),

abs(E norm(Y_delta)−kappa cH) ≤ sqrt(E norm(Y_delta−F0a Z_delta)^2) → 0.

This proves the claimed positive-gain witness and lower bound L_tau≥kappa cH. It also gives convergence IN DISTRIBUTION to the rank-one Gaussian law. It does NOT produce convergence in L2 to any fixed original-space Gaussian. Indeed for0<epsilon≤delta, E norm(F0a(Z_delta−Z_epsilon))²=2cH²(1−sqrt(epsilon/delta)); for cH>0 and any fixed ratio in(0,1), this fails the Cauchy criterion as both widths vanish. No extra coupling or change to the admissible filtration is introduced.

## Explicit interpretation of the adapted multi-burst limit

The original Section8 correctly states convergence of EXPECTED norms. Make its width dependence explicit: Z_delta,j is the actual normalized increment on[t_j,t_j+delta], a_delta,j=h_j(Z_delta,<j), s_j=(j−1)(tau+delta), t_j=s_j+tau. Since t_(j−1)+delta=s_j, all amplitude arguments are observed at the original physical INPUT time. The h_j are bounded Borel functions and may be discontinuous; no convergence of their values to a fixed random variable is assumed.

For fixed N with N tau<T, compare the actual Hilbert output Yhat_delta with the moving random vector Ystar_delta=sum_j F_((j−1)tau) h_j(Z_delta,<j) Z_delta,j. Hilbert Itô isometry gives

E norm(Yhat_delta−Ystar_delta)^2 = sum_j delta^−1 integral_(s_j)^(s_j+delta) E norm((Fs−F_((j−1)tau)) a_delta,j)^2 ds → 0.

Bounded amplitudes and operator-norm continuity of Fs justify the limit. The joint law of(Ystar_delta, sqrt(sum_j norm(a_delta,j)^2)) is independent of delta, because the Z_delta,j have the same independent standard-normal joint law for every admissible width. The stated expected-norm ratio therefore converges to the displayed finite Gaussian-law expression. There is no fixed original-space strong-limit claim and no anticipative amplitude.

## Consumer and import boundary

The intended Section5 positive-gain implication, Section6 expected-norm lower bound and deterministic measure approximation, Section7 long-lag equality, Section8 causal lower family and Section10 bounds use expected norms/covariance laws, not the withdrawn strong limit. They must be read with this erratum. The compact Gaussian maximum, strict deterministic inequalities, conditional long-lag reduction, delay continuity and strict-feasibility claims are not broadened by this correction. The weighted E2 inequality and exact zero-lag gain remain TWO separately named imports. General positive-lag exact gain, evaluation/attainment of D_H, original-source equivalence and controller synthesis remain unpaid.

This is a written additive repair, not a new executed experiment, final acceptance, novelty, independent-family/human/kernel assurance or rehabilitation of any held episode. Original f494 and both reviews remain immutable historical evidence; their original finding counts are not overwritten.
