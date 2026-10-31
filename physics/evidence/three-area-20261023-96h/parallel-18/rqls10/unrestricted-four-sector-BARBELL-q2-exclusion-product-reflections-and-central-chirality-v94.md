# RQLS10 v94 — BARBELL(2,1,2) with q = 2 has NO original MAX1 resolution

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 20:27:28 PDT 2026**. AUTHOR-WRITTEN CANDIDATE, not machine/kernel checked. Written two-projection/tensor/Pauli-commutant/row-column arguments only; no scientific Eval/interpreter/CAS/program/enumeration/solver/replay, approximate scout, chosen angle/state/control/probe or newGO.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption or verdict inheritance.

## 1. Domain and inputs

BARBELL(2,1,2) (v82): circuits X (route r1,r2,z), A (r1,r2), Y (t1,t2,z), B (t1,t2). X/A and Y/B are repeated pairs, hence interior-isoclinic (v79); v84 §5 forces the bridge X/Y at z to be interior-isoclinic and gives, in ANY full TEN-class resolution, q classes in PA∩PB = {A-pair, B-pair}, 4-q in PA\PB = {A-pair, Y-pair}, 4-q in PB\PA = {B-pair, X-pair} and 2+q NEITHER classes. Each NEITHER class is {x+ tensor nu, x- tensor nu, y+ tensor nu-perp, y- tensor nu-perp} in the X/Y frame P_X = |x+><x+| tensor I, P_Y = |y+><y+| tensor I, with its X-cells at r1,r2 and its Y-cells at t1,t2; the z X-cells lie only in PB\PA and the z Y-cells only in PA\PB; q <= 2. S_z = I tensor |omega><omega|. A length-two circuit pair in one class lies at ONE vertex in two rows (v93 §1). This manuscript treats q = 2 completely; q in {0,1} is NOT treated.

Vertex forms (v84 §5, derived): S_r = |x+><x+| tensor Pi_r + |x-><x-| tensor V_A* Pi_r V_A at r = r1,r2, with Pi_r = |pi_r><pi_r|, and the analogous S_t with V_B, Pi'_t on the Y/B side. MAX forces pi_2 not in {pi_1, pi_1-perp}, and likewise for pi'.

## 2. Product reflections at all four repeated-pair vertices

With q = 2, the 2+q = 4 NEITHER classes use all eight r X-cells and all eight t Y-cells. The three-cycle X has one column directly joining r1 and r2, with X+ at its tail and X- at its head, so these never pair. Hence every NEITHER X-pair is a same-vertex pair in two rows. Sharing nu forces x- tensor V_A* pi_r-perp to be x- tensor pi_r, i.e. V_A pi_r is proportional to pi_r-perp, for r = r1 and r2. Then V_A* Pi_r V_A = |pi_r-perp><pi_r-perp| and

    2S_r - I = R_X tensor sigma_r,   2S_t - I = R_Y tensor sigma'_t,

with sigma_r = |pi_r><pi_r|-|pi_r-perp><pi_r-perp| and the same argument on the Y side. The four NEITHER second factors are pi_1, pi_1-perp, pi_2, pi_2-perp, and their Y-cells use pi'_t or pi'_t-perp. Hence the two axes {n'_1, n'_2} on the Bloch sphere of K2 equal {n_1, n_2}.

## 3. lambda_XY = 1/2 and the commutant normal forms

PB\PA consists of the two z X-pair classes {x+ tensor omega, x- tensor omega-perp} and {x+ tensor omega-perp, x- tensor omega}. The complement W_z = span(x+ tensor omega-perp, x- tensor omega) is spanned by an opposite-row B-pair at some t, so it is invariant under R_Y tensor sigma'_t. Exactly as in v93 Lemma U, R_Y x+ = r11 x+ + r21 x- with r21 nonzero forces r11 = 0. Hence lambda_XY = 1/2, and ω is unbiased to pi'_t. Choose phases with R_X = sigma_z tensor I and R_Y = sigma_x tensor I.

R_A commutes with sigma_z tensor sigma_1 and sigma_z tensor sigma_2, where n_1 is not ±n_2. Their algebra contains I tensor N, with N = n_N.sigma and n_N along n_1 x n_2. Its commutant is

    span{I, sigma_z tensor I, sigma_x tensor N, sigma_y tensor N},

so R_A = a sigma_z tensor I + b sigma_x tensor N + c sigma_y tensor N. Likewise R_B = a' sigma_x tensor I + b' sigma_y tensor N + c' sigma_z tensor N, because the t axes equal the r axes and N' = ±N.

PA\PB consists of the two z Y-pair classes. The complement W'_z = span(y+ tensor omega, y- tensor omega-perp), with 2Pi-I = sigma_x tensor sigma_omega, is spanned by an A-pair. P_A-invariance gives

    [R_A, sigma_x tensor sigma_omega] = 2i(a sigma_y tensor sigma_omega + b I tensor (n_N x n_omega).sigma - c (n_N.n_omega) sigma_z tensor I) = 0,

so a = 0, b(n_N x n_omega) = 0 and c(n_N.n_omega) = 0. The analogous B computation on W_z gives a' = 0, b'(n_N.n_omega) = 0 and c'(n_N x n_omega) = 0. Therefore either

    (I)  n_omega = ±n_N,  R_A = ±sigma_x tensor N,  R_B = ±sigma_z tensor N,  or
    (II) n_omega orthogonal to n_N,  R_A = ±sigma_y tensor N,  R_B = ±sigma_y tensor N.

## 4. Theorem: q = 2 is impossible

Case (I). On W'_z, sigma_x tensor N acts on y+ tensor omega by (+1)(s) and on y- tensor omega-perp by (-1)(-s), where N omega = s omega. So R_A is the scalar s on W'_z, which therefore cannot contain both the A+ and the A- cell of its A-pair. Contradiction.

Case (II). Then P_B is P_A or I-P_A. Take a PA∩PB class; q = 2 gives two. Its A-pair at r' spans Q, and its B-pair at t' spans Q-perp. Q is invariant under sigma_z tensor sigma_r', sigma_x tensor sigma'_t' and R_A = ±sigma_y tensor N. Since n_r' and n'_t' are orthogonal to n_N, R_A commutes with both reflections, so it is central for this algebra. Q cap rangeP_A is the A+ line of the pair, invariant under both reflections restricted to rangeP_A. On rangeP_A their anticommutator is ∓2 sin(angle(n_r', n'_t')) times I.

* If n'_t' is not orthogonal to n_r', the two restricted reflections do not commute. Two noncommuting reflections on C2 have no common invariant line. Contradiction.
* If n'_t' is orthogonal to n_r', the restricted reflections agree up to sign, so the A+ cells at r' are eigenlines of S_t' inside rangeP_A. These are the B+ cells at t' if P_B = P_A, or the B- cells if P_B = I-P_A. These are duplicated rays, contradicting MAX.

Both cases fail. Hence NO original MAX1 array of BARBELL type has a full resolution with q = 2. This holds for ALL cyclic orders, orientations, row labels, frames, angles and labelings. No candidate or numerical case was chosen or tested.

## 5. Scope and frontier

New paid result: BARBELL with q = 2 excluded, through Lemmas in §§2-3 (product reflections, lambda_XY = 1/2, commutant normal forms). BARBELL with q in {0,1} remains OPEN. So do THETA(1,2,2), the five-cycle C5, dense d in {2,3,4,5}, other sector placements, minimal-rank-3 and higher-rank families, complementH6, actual100 distinct rays and the SAME TEN-class resolution. All original irreducible10, 4+6 and 5+5 branches remain OPEN.

Imports: v79 repeated-pair isoclinicity; v82 topology list; v84 §5 BARBELL class pattern, isoclinic bridge and vertex forms; v86 BARBELL addendum; v93 §1 length-two pair rule and Lemma U argument; elementary Pauli and two-projection algebra; the actual primary TEN-transversal/CLASSICAL-mate interface. No NR/classifier/Butson/Gaussian/code premise, measure genericity or chosen frame. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S94, retaining ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including the disclosed v29 parallel-intent minor, the v30 dangling-reference defect and the v34 capture retry.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
