# RQLS10 v95 — BARBELL(2,1,2): q = 1 excluded, and q = 0 excluded when both repeated pairs flip

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 20:37:20 PDT 2026**. AUTHOR-WRITTEN CANDIDATE, not machine/kernel checked. Written two-projection/tensor/Pauli-commutant/row-column arguments only; no scientific Eval/interpreter/CAS/program/enumeration/solver/replay, approximate scout, chosen angle/state/control/probe or newGO.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption or verdict inheritance.

## 1. Domain and inputs

Same BARBELL setting and imports as v94 §1: circuits X (r1,r2,z), A (r1,r2), Y (t1,t2,z), B (t1,t2); X/A, Y/B, X/Y interior-isoclinic; in ANY full TEN-class resolution the classes are q PA∩PB, 4-q PA\PB = {A-pair, Y-pair}, 4-q PB\PA = {B-pair, X-pair} and 2+q NEITHER classes. v94 excluded q = 2. Here q is 0 or 1. X/Y frame: P_X = |x+><x+| tensor I, P_Y = |y+><y+| tensor I, S_z = I tensor |omega><omega|. At X/A vertices S_r = |x+><x+| tensor Pi_r + |x-><x-| tensor V_A* Pi_r V_A, so the X+ cells at r are x+ tensor pi_r, x+ tensor pi_r-perp and the X- cells are x- tensor V_A* pi_r, x- tensor V_A* pi_r-perp; Bloch vectors n_1, n_2 of pi_1, pi_2 are not parallel or antiparallel (MAX). The Y side is analogous with V_B, pi'_t, n'_t. Same-vertex pairs lie in two rows; the X column joining r1 and r2 forbids pairing the tail X+ with the head X-; take X+ at r1 to sit on that column (orientation reversal swaps names only).

The opposite-row A-pair at r spans a plane with reflection ±R_A(2S_r-I); the opposite-row B-pair at t spans a plane with reflection ±M'_t, M'_t = R_B(2S_t-I). This is the identity P(I-S)+(I-P)S = (I - R(2S-I))/2 for commuting P,S.

## 2. Lemma ROT: PA\PB at both r forces V_A to be a rotation about one axis

For q <= 1, PA\PB contains A-pairs at BOTH r1 and r2 (it has at least three of the four A-pairs). Their complements are Y-pair planes, so R_Y commutes with R_A(2S_r1-I) and R_A(2S_r2-I). In the X/A product frame U = |x+><x+| tensor I + |x-><x-| tensor V_A*, where R_A = sigma_z tensor I, R_X = (cos theta sigma_z + sin theta sigma_x) tensor I and these reflections are sigma_z tensor sigma_r, the commutant of the two gives

    R_Y = a sigma_z tensor I + (b sigma_x + c sigma_y) tensor N,   N = n_N.sigma,  n_N along n_1 x n_2.

X/Y isoclinicity makes {R_X,R_Y} scalar, which forces b sin theta = 0, so b = 0. Projections commuting with R_X and R_Y then pair x+ tensor mu with x- tensor R mu, where R is the rotation about n_N by a fixed angle psi. In the X/Y frame these projections are I tensor |nu><nu|, so V_A acts on the Bloch sphere as this rotation. The Y side gives V_B as a rotation about n'_N (orthogonal to n'_1, n'_2) by psi'.

Consequences. A same-vertex NEITHER X-pair at r means V_A pi_r is proportional to pi_r-perp. Since n_r is orthogonal to n_N, this happens exactly when psi = pi. Then 2S_r-I = R_X tensor sigma_r for BOTH r, and every X- cell at r has Bloch vector ±n_r. A cross NEITHER pair (X+ at r2, X- at r1) would then need ±n_2 = ±n_1, which is impossible. So psi = pi forces all NEITHER X-pairs to be same-vertex.

## 3. Lemma PB: flipped Y side normal form

Assume psi' = pi. Then 2S_t-I = R_Y tensor sigma'_t, and R_B = beta R_Y + beta' (u_B.sigma) tensor N' with u_B orthogonal to the Bloch vector of R_Y. Here beta' is nonzero, since otherwise P_B is P_Y or I-P_Y, contradicting strict Y/B angles (v80). Each PB\PA X-pair plane is the complement of a B-pair plane, hence a ±1 eigenspace of M'_t, which must commute with R_X. Writing out

    M'_t = beta I tensor sigma'_t - beta' ((u_B x r_Y).sigma) tensor (k'_t.sigma),   k'_t = n'_N x n'_t,

commutation with sigma_z tensor I forces u_B x r_Y to be parallel to the z axis. Hence r_Y is orthogonal to it, so lambda_XY = 1/2, R_Y = sigma_x tensor I and u_B = ±y. Then M'_t restricted to rangeP_X is m'_t+.sigma and to kerP_X is m'_t-.sigma, with m'_t± = beta n'_t ± beta' k'_t. The PB\PA classes at t pair an X+ cell with Bloch eps m'_t+ and an X- cell with Bloch eps m'_t-. The A side is symmetric when psi = pi: R_A = alpha sigma_z tensor I + alpha' sigma_y tensor N, and the PA\PB Y-cells at r have Bloch ±(alpha n_r ∓ alpha' k_r), k_r = n_N x n_r.

## 4. Theorem: q = 1 is impossible

NEITHER has three classes, but at most two cross pairs exist (only two X+ cells at r2). So some NEITHER pair is same-vertex and psi = pi; symmetrically psi' = pi. All three NEITHER pairs are same-vertex, so their rays cover both axes n_1,n_2, and their Y-cells force the t axes to equal the r axes; thus n'_N = ±n_N.

PB\PA has three classes: both B-pairs at some t_a and one at t_b. Its X+ Bloch vectors are ±m'_ta+ and one eps m'_tb+; its X- Bloch vectors are ±m'_ta- and one eps m'_tb-. All four z X-cells lie in PB\PA and have Bloch vectors ±n_omega for both signs. An antipodal pair meeting {±n_omega} equals it, so {±m'_ta+} = {±n_omega} = {±m'_ta-}. Hence m'_ta- = ±m'_ta+, so beta' = 0 (excluded) or beta = 0, and then m'_t± = ±k'_t. The t_b class has an r X+ cell, so k'_tb = ±n_r for some r. As n'_tb is a t axis, it is ±n_r'' with r'' different from r, and then n_1 is orthogonal to n_2. Now n'_ta is ±n_1 or ±n_2, so n_omega = ±k'_ta lies in {±n_1, ±n_2}, and x+ tensor omega duplicates an r X+ cell. Contradiction.

## 5. Theorem: q = 0 with psi = psi' = pi is impossible

PB\PA has four classes, both B-pairs at t1 and both at t2. Its four X+ cells are the two z X+ cells and two r X+ cells, with Bloch pairs ±m'_t1+ and ±m'_t2+. A mixed orthogonal pair (z, r) would duplicate rays, so one t (t_z) carries the z X+ pair and the other (t_r) an orthogonal r X+ pair, which must be both X+ cells of one vertex r*.

If the z X- pair sat at t_r, the column rules would force t_z classes to be (z X+, r2 X-) and t_r classes to be (r1 X+, z X-). NEITHER would then consist of X+ at r2 with X- at r1, i.e. cross pairs, impossible by Lemma ROT. So {±m'_tz-} = {±n_omega} = {±m'_tz+}, and as in §4 beta = 0. Then t_r carries X+ and X- Bloch pairs ±k'_tr = ±n_r*, i.e. both cells of r*. NEITHER consists of the same-vertex pairs at the other vertex r**, and their Y-cells force n'_t** = ±n_r** for the t carrying them. Since n_r* = ±k'_tr and n_r** are both orthogonal to n'_N, n'_N = ±n_N. The symmetric A-side argument gives alpha = 0. Hence R_A = ±sigma_y tensor N and R_B = ±sigma_y tensor N = ±R_A.

As in v94 Case II, on rangeP_A the restrictions of 2S_r*-I = sigma_z tensor sigma_r* and 2S_tr-I = sigma_x tensor sigma'_tr have anticommutator ∓2 sin(angle(n_r*, n'_tr)) I. Since k'_tr = n_N x n'_tr = ±n_r*, n'_tr is orthogonal to n_r*, so these restricted reflections agree up to sign. Then the A+ cells at r* coincide with B cells at t_r inside rangeP_A, a duplicated ray. Contradiction.

## 6. Scope and frontier

New paid results: Lemma ROT, Lemma PB, BARBELL with q = 1 excluded, and BARBELL with q = 0 and psi = psi' = pi excluded. Remaining BARBELL case: q = 0 with all NEITHER X-pairs cross (psi not pi) or, symmetrically, all NEITHER Y-pairs cross. Its frames are pinned further in working notes but it is NOT closed here. THETA(1,2,2), C5, dense d in {2,3,4,5}, other sector placements, minimal-rank-3 and higher-rank families, complementH6, actual100 distinct rays and the SAME TEN-class resolution remain unpaid. All original irreducible10, 4+6 and 5+5 branches remain OPEN.

Imports: v94 BARBELL setup, product-reflection and Case II duplicate arguments; v84 §5 and v86 §6 BARBELL patterns; v79 isoclinicity; v80 strict angles; elementary Pauli/two-projection algebra; the actual primary TEN-transversal/CLASSICAL-mate interface. No NR/classifier/Butson/Gaussian/code premise, measure genericity or chosen frame. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S95, retaining ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including the v29 and v40 parallel-intent minors, the v30 dangling-reference defect and the v34 capture retry.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
