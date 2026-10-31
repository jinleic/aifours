# RQLS10 v97 — BARBELL cross-cross residual is OCTAGONAL: psi, psi' ≡ pi/4 (mod pi/2) and |gamma| = 3 - 2 sqrt 2

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 20:53:26 PDT 2026**. AUTHOR-WRITTEN CANDIDATE, not machine/kernel checked. Written Pauli/rotation/trigonometric identities only; no scientific Eval/interpreter/CAS/program/enumeration/solver/replay, approximate scout, chosen angle/state/control/probe or newGO.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption or verdict inheritance.

## 1. Domain and inherited normal form

The ONLY open BARBELL case after v94-v96 is q = 0 with both sides cross. v96 §4 gives: n'_N = ±n_N; all relevant Bloch vectors lie in the plane P orthogonal to n_N (Case B2 on both sides). In the x-basis of K1, with R_X = sigma_z tensor I, R_Y = (gamma sigma_z + gamma' sigma_x) tensor I, gamma' = (1-gamma^2)^(1/2) > 0,

    R_B = (b_z sigma_z + beta_c K sigma_x) tensor I + beta_c sin(Delta/2) sigma_y tensor N,
    gamma beta_c = gamma' b_z K,   K = cos(Delta/2),   b_z^2 + beta_c^2 = 1,

where W = exp(-i Delta N/2) maps n_omega to n_rho. In P, with angles mod pi: n_1 = 0, n_2 = -psi, n_omega = -psi + pi/2, n_rho = -2psi. Hence Delta ≡ -psi - pi/2 (mod pi). The compressions of 2S_t - I to rangeP_Y give psi' ≡ psi + pi/2 or psi' ≡ -psi + pi/2 (mod pi). The A side is the exact mirror, with Delta' ≡ -psi' - pi/2 (mod pi) and the same gamma.

## 2. Lemma: gamma, b_z and K are nonzero

If gamma = 0, then b_z K = 0. If K = 0, Delta = pi maps n_omega to -n_omega, so rho = omega-perp and the r2 X- cell duplicates a z X- cell. If b_z = 0, the Y/B decomposition below gives cos(psi'/2) = 0, i.e. psi' = pi, contradicting the cross Y side. So gamma is nonzero. If b_z = 0, then beta_c = 0 and R_B = 0, impossible. If K = 0, the same duplicate occurs. So b_z, K and gamma are all nonzero.

## 3. Lemma TAN: the Y/B form pins psi' from Delta and gamma

R_B also has the Y/B form beta R_Y + beta' N_B with N_B = cos(psi'/2)(t_x.sigma) tensor I + sin(psi'/2)(t_y.sigma) tensor N'. Here t_x, t_y are orthogonal to r_Y = (gamma', 0, gamma), and the N-terms force t_y = ±y. Take t_x = ±(-gamma, 0, gamma'). Projecting the I-part vector (beta_c K, 0, b_z) of R_B gives

    beta = beta_c K gamma' + b_z gamma,
    beta' cos(psi'/2) = ±(b_z gamma' - K gamma beta_c) = ±gamma' b_z sin^2(Delta/2),
    beta' sin(psi'/2) = ±beta_c sin(Delta/2).

Using beta_c = gamma' b_z K / gamma,

    |tan(psi'/2)| = |cot(Delta/2)| / |gamma|.

The mirror gives |tan(psi/2)| = |cot(Delta'/2)| / |gamma|.

## 4. Theorem: octagonal rigidity

Put T = |tan(psi/2 + pi/4)| and T' = |tan(psi'/2 + pi/4)|. From Delta/2 ≡ -psi/2 - pi/4 (mod pi/2), |cot(Delta/2)| is T or 1/T. Both branches psi' ≡ ±psi + pi/2 give |tan(psi'/2)| in {T, 1/T}. Lemma TAN therefore gives |gamma| in {1, T^2, T^-2}. Interior X/Y angles exclude |gamma| = 1, so T ≠ 1 and |gamma| = min(T^2, T^-2). Symmetrically |gamma| = min(T'^2, T'^-2), so T' is T or 1/T. Also T' is |tan(psi/2)| or |cot(psi/2)| in either branch, since psi'/2 + pi/4 ≡ ±psi/2 (mod pi/2). With tau = tan(psi/2):

    |(1+tau)/(1-tau)| = |tau|^(±1).

Each sign region of tau reduces this to tau^2 - 2tau - 1 = 0, tau^2 + 2tau - 1 = 0 or the impossible tau^2 = -1. So tau is in {1±sqrt2, -1±sqrt2}, i.e. psi ≡ pi/4 (mod pi/2). By the branch relation also psi' ≡ pi/4 (mod pi/2). Then T is (1+sqrt2) or its inverse, and

    |gamma| = (sqrt2 - 1)^2 = 3 - 2 sqrt2,   so   lambda_XY = (1 ± (3 - 2sqrt2))/2.

All Bloch axes of §1 and of the mirrored A side (n_1, n_2, n_omega, n_rho, n'_1, n'_2, n_rho') lie at multiples of pi/4 in P. Hence the residual is reduced to FINITELY many explicit octagonal discrete candidates. These are branch, sign and orientation choices with fixed gamma, psi and psi'.

## 5. Scope and frontier

New paid result: the BARBELL cross-cross residual is octagonal-rigid, with gamma, b_z, K nonzero, Lemma TAN, psi, psi' ≡ pi/4 (mod pi/2) and |gamma| = 3 - 2sqrt2. Existence or exclusion of the finitely many octagonal candidates is NOT decided; no candidate was built or tested. With this, BARBELL is reduced to a finite exact check. THETA(1,2,2), C5, dense d in {2,3,4,5}, other sector placements, minimal-rank-3 and higher-rank families, complementH6, actual100 distinct rays and the SAME TEN-class resolution remain unpaid. All original irreducible10, 4+6 and 5+5 branches remain OPEN.

Imports: v94-v96 BARBELL lemmas and normal forms; v84 §5/v86 §6; v79/v80; elementary Pauli/rotation/trigonometric identities; the actual primary TEN-transversal/CLASSICAL-mate interface. No NR/classifier/Butson/Gaussian/code premise, measure genericity or chosen frame. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S97, retaining ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including the v29 and v40 parallel-intent minors, the v30 dangling-reference defect and the v34 capture retry.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
