# Parent disposition — physics-3-minimum-face-sign-cases-and-negative-margin-parent

Observed clock before writing: **2026-10-27T17:20:24-0700 PDT**. Same-harness written disposition; not formal/kernel, human, configured-family, executable or novelty acceptance. Independent-model CLI review not performed.

## Inputs read completely by Main

- Author [unfiltered-budget-minimum-face-v1.md](/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ppt-schmidt44/unfiltered-budget-minimum-face-v1.md), SHA256 `499cedbd21a8540b0f4d178919f45c4f604742602e45ec2fb9b64a4a951b69c3`, 159 LF: raw 1-60, 61-120, 121-159.
- Author [unfiltered-budget-minimum-face-v1-addendum-1.md](/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ppt-schmidt44/unfiltered-budget-minimum-face-v1-addendum-1.md), SHA256 `a812bdfb52311c9ab9316c645bbe6e1d82c14fb1744ecec7e5749264fc8f3e5f`, 104 LF: raw 1-60, 61-104.
- Review [w83 (PhysicsRQLS10-2)](/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/rqls10/review-w83-physics-3-unfiltered-minimum-face-union-v1.md), SHA256 `ef4bbdb5ac9093239a85414082b81ace95b838a8a23e0b1004ed7dd9d628eff5`, 160 LF: raw 1-55, 56-110, 111-160. Verdict 0 FATAL / 0 MAJOR / 0 MINOR at exact scope.
- Used dependency [prerequisite-derivation-v1.md](/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ppt-schmidt44/prerequisite-derivation-v1.md), SHA256 `7d00196376108da34c416b8e80f815adfc337d01cb24191f8ad40f6a47d8cdc4`, 208 LF, read completely by Main for the earlier [physics-3 complement adoption](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-3-ppt-complement-cone-and-reconstruction-barrier-parent-v1.md); only its PPT upper inequality and double-complement identity are used, and w83 reconstructs both.
- Release [physics-3-unfiltered-budget-minimum-face-release-v1.json](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/written-releases/physics-3-unfiltered-budget-minimum-face-release-v1.json), SHA256 `e7064ab24f10a1228c22b9d9c7c2e9a6868b4aee3d2818eaf2c422ec9ec300ff` (status, not proof).

## Adopted at exact written-support scope

On the original C^4 tensor C^4, let W be any nonzero Hermitian operator that is nonnegative on every vector of Schmidt rank at most two. Put A = Tr_B W, B = Tr_A W, tau = Tr W, let alpha and beta be the minimum eigenvalues of A and B, and let E_A and E_B be their minimum eigenspaces. Let rho be any positive trace-one operator whose range lies in E_A tensor E_B.

1. **Product-zero rigidity.** If a product vector x has <x|W|x> = 0, then Wx = 0. Consequently tau > 0.
2. **Zero minimum.** If alpha = 0 then E_A tensor C^4 lies in ker W (symmetrically for beta = 0), so W rho = 0. PPT is not needed.
3. **Small eigenspace.** If dim E_A <= 2 or dim E_B <= 2, then Tr(W rho) >= 0. PPT is not needed.
4. **Minimum face.** For every density rho, Tr[(A tensor I + I tensor B - tau I) rho] >= alpha + beta - tau, with equality exactly when range rho lies in E_A tensor E_B, and alpha + beta < tau.
5. **Exact residual.** Z = tau I - I tensor B - A tensor I + W is positive semidefinite, and on the face Tr(W rho) = Tr(Z rho) - (tau - alpha - beta). The favorable sign is equivalent to Tr(Z rho) >= tau - alpha - beta.
6. **Negative-margin bound.** With c = min(alpha, beta) and kappa = max(min(dim E_A, dim E_B) - 2, 0): Tr(W rho) >= -kappa c for every positive face rho, and Tr(W rho) <= c when rho is also PPT. Any negative eligible pair on the face therefore has 0 < -Tr(W rho) <= kappa c.

## Not adopted and not claimed

- The case alpha > 0, beta > 0, dim E_A >= 3 and dim E_B >= 3 remains OPEN at NR-UNFILTERED-MINIMUM-FACE-SLACK. No negative pair, sharpness, attainment or physics-3 (P44) closure is claimed.
- Excluding all minimum-face negative pairs would exclude only this construction route, not all PPT states.
- The author's disclosed initial release-metadata open before the S0 reread remains an order qualification. The reviewer's disclosed 24m31s gap before this review remains a cadence record.
- Novelty UNCLEAR: no literature comparison was performed for these statements.
- All STOP/HOLD/ZERO boundaries persist, including the w30, JL and L1 consumers; N4 remains UNKNOWN with its historical child exit unestablished; auxiliary214 remains STOP.
