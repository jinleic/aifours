# RQLS10 v96 — BARBELL q = 0: a cross side with a flipped side is impossible; the cross-cross residual is coplanar

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 20:45:56 PDT 2026**. AUTHOR-WRITTEN CANDIDATE, not machine/kernel checked. Written two-projection/tensor/Pauli-commutant/rotation arguments only; no scientific Eval/interpreter/CAS/program/enumeration/solver/replay, approximate scout, chosen angle/state/control/probe or newGO.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption or verdict inheritance.

## 1. Domain

BARBELL with q = 0, after v94 (q = 2 excluded) and v95 (q = 1 and q = 0 with both flips excluded). Notation and imports as in v95: Lemma ROT gives V_A as a rotation about n_N (orthogonal to n_1,n_2) by psi and V_B about n'_N by psi'. A side is CROSS when both NEITHER pairs of that side are cross pairs; otherwise it flips (psi = pi, resp. psi' = pi). By v95 at least one side is cross; by the X/Y mirror symmetry of BARBELL take the X side cross, so psi is not pi.

## 2. Exact cross-side structure

X side cross: NEITHER uses X+ at r2 (both rows) with X- at r1 (both rows). Hence V_A* maps the axis of pi_1 to that of pi_2. The column rules then force PB\PA to consist of (z X+, r2 X-) classes at one t_z and (r1 X+, z X-) classes at the other t_r. Their X-pair planes give

    M'_tz = ±(|x+><x+| tensor sigma_omega + |x-><x-| tensor sigma_rho),
    M'_tr = ±(|x+><x+| tensor sigma_1 + eta |x-><x-| tensor sigma_omega),

with rho the r2 X- factor; its axis is V_A* of the axis of pi_2. Since R_B commutes with both S operators, M'_tz M'_tr = (2S_tz-I)(2S_tr-I) commutes with R_Y. As R_Y mixes x+ and x-, the two diagonal blocks agree:

    sigma_omega sigma_1 = eta sigma_rho sigma_omega,

so the axis of rho is the pi-rotation of the axis n_1 about n_omega. As an axis, rho is also R_{-2psi}(n_1), with R about n_N. Hence (n_1.n_omega)(n_omega.n_N) = 0. This gives two cases. Case A: n_omega is orthogonal to n_1, forcing psi = ±pi/2 and n_1 orthogonal to n_2. Case B: n_omega is orthogonal to n_N; then either n_omega = ±n_2, a duplicated X+ ray, or (B2) n_omega lies in the plane P orthogonal to n_N and is orthogonal to n_2.

## 3. Theorem: X cross with Y flipped is impossible

Let psi' = pi. v95 Lemma PB gives lambda_XY = 1/2, R_B = beta sigma_x tensor I + beta' sigma_y tensor N', and PB\PA X-cells with Bloch pairs eps m'_t± = eps(beta n'_t ± beta' k'_t). These are mirror images about the axis n'_t in the plane orthogonal to n'_N. The data of §2 give m'_tz+ = ±n_omega, m'_tz- = ±n_rho, m'_tr+ = ±n_1 and m'_tr- = ±n_omega. With psi' = pi the NEITHER Y-pairs are same-vertex at one t**, with axis n'_t** equal to the axis n_2. Thus n_1 and n_2 are orthogonal to n'_N, so n'_N = ±n_N and n_omega lies in P.

* Case A: n_omega in P is orthogonal to n_1, and n_1 is orthogonal to n_2, so n_omega = ±n_2, a duplicate.
* Case B2: put n_1, n_2, n_rho, n_omega in P at angles 0, -psi, -2psi, -psi+pi/2. The axis n'_t is a bisector, mod pi/2, of its mirror pair: -psi/2+pi/4 at t_r and -3psi/2+pi/4 at t_z. Requiring the bisector at t** to equal -psi mod pi/2 forces psi ≡ pi/2 (mod pi) in both cases. Then n_omega = ±n_1, again a duplicate.

The mirror statement (Y cross, X flipped) holds by symmetry. Hence in BARBELL with q = 0 BOTH sides are cross.

## 4. Coplanar normal form of the cross-cross residual

Assume both sides are cross. The commutant of {M'_tz, M'_tr} is {[[a, b W*],[c W, d]]} in x± blocks, where W intertwines (sigma_omega, sigma_1) with (sigma_rho, eta sigma_omega). Thus

    R_B = b_z sigma_z tensor I + conj(beta_c)|x+><x-| tensor W* + beta_c |x-><x+| tensor W.

beta_c is nonzero: otherwise R_B = ±R_X, and commutation with R_Y forces rho = omega-perp, a duplicate. Commutation of R_B M'_t with R_Y gives W* = (beta_c/conj(beta_c)) sigma_omega W sigma_omega, so the rotation axis w of W is orthogonal to n_omega. If w were parallel to n_omega, rho = omega would be a duplicate. Since R_B also has the Y/B form in M2 tensor span{I, N'}, the nonzero w.sigma component forces w to be parallel to n'_N. W fixes n'_N components and maps n_1 to ±n_omega and n_omega to n_rho, so n_1, n_omega and n_rho are orthogonal to n'_N. The NEITHER Y+ cells at t2 give n'_2 = ±n_2. Hence

    n'_N = ±n_N,   n_omega in P,   Case B2 on both sides.

With W = exp(-i Delta N/2) a rotation by Delta about n_N: beta_c is real, and gamma beta_c = gamma' b_z cos(Delta/2), where gamma = {R_X,R_Y}/2 and gamma' = (1-gamma^2)^(1/2). The compressions <y+|(2S_t - I)|y+> have axes n'_tz and n'_tr whose difference is the angle from n_omega to n_1 (mod pi), since the same W and coefficients occur at both t. Writing the Y axes as n'_2 = n_2 (angle -psi) and n'_1 at angle -psi+psi', and applying the mirror relation on the A side, one obtains

    psi' ≡ psi + pi/2   or   psi' ≡ -psi + pi/2   (mod pi),

with psi not in {0, pi/2} mod pi by MAX. These are NECESSARY conditions only. Existence or exclusion of a cross-cross BARBELL resolution, including the remaining matching of the X/A and Y/B forms of R_A and R_B, all forty-ray distinctness checks and the A/B cell placements, is NOT decided here.

## 5. Scope and frontier

New paid results: BARBELL with q = 0 and exactly one cross side is impossible. The cross-cross residual is reduced to a coplanar normal form with n'_N = ±n_N, Case B2 geometry, beta_c real, gamma beta_c = gamma' b_z cos(Delta/2) and psi' ≡ ±psi + pi/2. BARBELL is therefore OPEN only in this cross-cross residual. THETA(1,2,2), C5, dense d in {2,3,4,5}, other sector placements, minimal-rank-3 and higher-rank families, complementH6, actual100 distinct rays and the SAME TEN-class resolution remain unpaid. All original irreducible10, 4+6 and 5+5 branches remain OPEN.

Imports: v94/v95 BARBELL lemmas; v84 §5 and v86 §6; v79/v80; elementary Pauli/two-projection/rotation algebra; the actual primary TEN-transversal/CLASSICAL-mate interface. No NR/classifier/Butson/Gaussian/code premise, measure genericity or chosen frame. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S96, retaining ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including the v29 and v40 parallel-intent minors, the v30 dangling-reference defect and the v34 capture retry.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
