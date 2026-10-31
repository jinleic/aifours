# Actual-pair erasure layers: exact three-erasure bound and k3 reduction

**Scope.** Independently derived ordinary written mathematics, not a formal proof, novelty claim or validation of any historically held result. Every \(\rho\) below is an actual four-qubit density and \(P\) is one actual complex rank-three orthogonal projector. The final all-parameter original k3 problem is **not solved**: two named layer inequalities remain unproved. A violation of a single proposed layer bound would invalidate this sufficient certificate, not automatically refute original-channel majorization.

## Definitions and exact sufficient certificate

For site \(i\), put \(E_i(X)=\frac{I_i}{2}\otimes\operatorname{Tr}_iX\), with the factors restored to the original site order, and \(E_S=\prod_{i\in S}E_i\). These conditional expectations commute. For fixed \((\rho,P)\), define
\[
T_m(\rho)=\sum_{|S|=m}E_S(\rho),\qquad
 t_m(\rho,P)=\operatorname{Tr}[P T_m(\rho)],\quad m=0,1,2,3,4.
\]
For \(0\le p\le1\), the original local depolarizing map satisfies \(\Phi_p=(1-p)\operatorname{Id}+pE_i\), so the SAME physical \(\rho,P\) obey
\[
\operatorname{Tr}[P\Lambda_p(\rho)]
=\sum_{m=0}^4(1-p)^{4-m}p^m t_m(\rho,P).\tag{1}
\]
The exact product reference has one fixed rank-three projector that maximizes it for every such \(p\): take \(\rho_*=|0000\rangle\langle0000|\) and \(P_*\) onto \(|0000\rangle,|1000\rangle,|0100\rangle\). For each \(|S|=m\),
\[
\operatorname{Tr}[P_* E_S(\rho_*)]
=2^{-m}(1+\mathbf 1_{1\in S}+\mathbf 1_{2\in S}),
\]
so
\[
t_m(\rho_*,P_*)=2^{-m}\!\left[{4\choose m}+2{3\choose m-1}\right]
=(1,3,3,5/4,3/16)_m.\tag{2}
\]
The two one-bit reference outputs lie in the second-largest degenerate eigenspace; \(p=0,1\) are covered by continuity or direct eigenvalues. Therefore \(\operatorname{Tr}[P_*\Lambda_p(\rho_*)]=R_3(p)\).

For every actual pair, \(t_0\le1\), \(t_4=3/16\), and the theorem below gives \(t_3\le5/4\). Thus the following TWO as-yet-**unproved** inequalities would be sufficient for the full original k3 bound on \([0,1]\):
\[
 t_1(\rho,P)\le3,\qquad t_2(\rho,P)\le3.\tag{3}
\]
Both must hold for the same arbitrary physical pair, not for independently optimized marginals. Multiplying the five inequalities by the nonnegative coefficients in (1) would give the reference expression (2). The separate exact parameter-mirror proposition `frontier-20261028-01-spectral-mirror.md` then extends such a proof to the entire physical interval \([0,4/3]\), with a deterministic bijection of actual projectors. Conversely, the original k3 statement does not imply each of (3): (3) is a stronger, coefficientwise sufficient condition.

## Theorem: universal \(t_3\le5/4\)

For each single-qubit marginal \(\rho_i=\operatorname{Tr}_{\bar i}\rho\), write its eigenvalues as \((1\pm r_i)/2\), where \(0\le r_i\le1\). Relabel for this calculation so \(r_1\le r_2\le r_3\le r_4\). Since all but one site are erased,
\[
T_3(\rho)=\frac18\sum_{i=1}^4\rho_i\otimes I_{\bar i}.
\]
The four terms act on disjoint tensor factors and commute. Diagonalize them with a product unitary. Their sixteen eigenvalues, including multiplicities, are
\[
\lambda_{\varepsilon}=\frac{4+\sum_{i=1}^4\varepsilon_i r_i}{16},\qquad\varepsilon_i\in\{+1,-1\}.
\]
The three largest values are the all-plus value and those obtained by flipping the signs associated with the two smallest \(r_i\); ties, including zero \(r_i\), cause no difficulty. By the Ky-Fan variational principle,
\[
 t_3(\rho,P)\le\frac{12+3\sum_i r_i-2(r_1+r_2)}{16}
 =\frac{12+r_1+r_2+3r_3+3r_4}{16}\le\frac{20}{16}=\frac54.
\]
This proof does not assume pure inputs, real entries, nondegenerate eigenvalues or independent marginals. Equality is possible for a product pure input and the stated \(P_*\). If equality holds, all four \(r_i=1\); each marginal is pure, which forces \(\rho\) to be a pure product: a positive density with a pure local marginal is supported on that one-dimensional local factor, and iteration over all four sites gives the claim. Thus the bound is exact, with equality at least at the exhibited actual pair; no complete classification of equality projectors is asserted.

## Bounded auxiliary experiments (not proofs)

Native clock after script hashes: **Wed Oct 28 17:05:36 PDT 2026**. `frontier-20261028-05-erasure-layers.py` SHA256 `dc429de6d48309f126e89d13713692e1c7b951bea75faaec22354be47233c031` imports `frontier-20261028-04-erasure-probe.py` SHA256 `9f82ccaa5c60ee71ba5614b77cb9f6e0ca471e376eaa04e757b736bf23b6fd19`, which imports `frontier-20261028-02-physical-seesaw.py` SHA256 `73d4befebd61820df000ef49c3f768844828e7cb137cb4caa5a0510337ec7587`. Run under `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1` with seed 2026102805, 60 random complex pure starts per layer and at most100 alternating actual-state/projector steps; exit0. Direct independently constructed Pauli-mixture recomputation used the actual final state/projector. Reference layers were measured with the SAME \(\rho_*,P_*\).

|m|reference|largest numerical final score|direct Pauli projector trace|candidate above reference by >1e-9?|
|---|---:|---:|---:|---|
|1|3.0|2.9999999999999503|2.999999999999951|no|
|2|3.0|3.000000000000006|3.0000000000000053|no|
|3|1.25|1.2500000000000036|1.250000000000003|no|

Largest direct-vs-partial-trace entry error among the three best pairs was `9.992007221626409e-16`; largest projector idempotence error was `5.551115123125783e-16`; reported state minimum eigenvalues ranged down to `-1.6466330316179833e-16` at floating precision. The small positive values are roundoff-scale, not exact witnesses. A separate seed-2026102804 one-erasure run, 100 starts and ≤120 steps, found best direct trace `2.9999999999999467` versus reference3, with Pauli/partial-trace maximum entry disagreement `2.220446049250313e-16`. Neither finite experiment proves (3), and neither demonstrates an original-channel violation.

No quarantined mathematical result is imported as a premise; no claim is made that existing historical process findings were cured or that the author has no prior context. No external-model, human, kernel, independent-family or novelty review has been performed for this new reduction.
