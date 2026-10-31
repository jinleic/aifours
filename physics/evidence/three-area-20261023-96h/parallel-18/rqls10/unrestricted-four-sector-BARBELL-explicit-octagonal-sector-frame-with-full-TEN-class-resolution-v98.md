# RQLS10 v98 — An EXPLICIT octagonal BARBELL four-sector frame with a complete TEN-class sector resolution (written candidate)

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 21:03:24 PDT 2026**. AUTHOR-WRITTEN CANDIDATE, verified only by the written exact algebra below. Not machine/kernel/formal checked, not independently reconstructed. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay. During the search the author made private mental decimal sanity estimates; they receive ZERO credit and every claim below is stated and proved with exact surds and angles.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. What this is and is not

v94-v97 pushed BARBELL toward exclusion and left only octagonal cross-cross candidates. This manuscript writes ONE such candidate explicitly. It is a sector object: forty pairwise distinct rays in C4 forming the BARBELL row and column ONBs of the v76/v82 five-row-type placement, together with ten disjoint four-cell sector classes. Each class is an ONB of C4 with distinct rows and columns. If correct, the ALL-SPARSE four-sector analysis can NOT exclude the 4+6 branch by itself. It is NOT a maximal 1-RQLS(10). No complementary H6 sector, no extension of the class labeling to a classical Latin square of order ten, and no 100-ray array is supplied.

## 1. Exact data

K1 = C2 with basis x+ = (1,0), x- = (0,1) and Paulis sigma_x, sigma_y, sigma_z. Put

    c = (2 - sqrt2)^(1/2),  s = (sqrt2 - 1)^(1/2),  y+ = c x+ + s x-,  y- = s x+ - c x-,
    gamma = c^2 - s^2 = 3 - 2sqrt2,  gamma' = 2cs = 2(3sqrt2 - 4)^(1/2),  gamma^2 + gamma'^2 = 1.

Write tau_z = gamma sigma_z + gamma' sigma_x, tau_x = gamma' sigma_z - gamma sigma_x and tau_y = -sigma_y. These are the Paulis of the basis y±.

K2 = C2 with basis |0>,|1>, sigma_3 = diag(1,-1). For an angle theta put |theta> = (|0> + e^{i theta}|1>)/sqrt2 and sigma_theta = 2|theta><theta| - I = cos theta sigma_1 + sin theta sigma_2. |theta+pi> is |theta>-perp.

Constants: K = sin(pi/8), S = cos(pi/8), b = sqrt2 - 1, beta = (2sqrt2 - 2)^(1/2). Then b^2 + beta^2 = 1, and the key identity is

    gamma beta = gamma' b K.   (squares: both equal 58sqrt2 - 82)

Circuit reflections (R_C = 2P_C - I):

    R_X = sigma_z ⊗ I,                         R_Y = tau_z ⊗ I,
    R_B = (b sigma_z + beta K sigma_x) ⊗ I - beta S sigma_y ⊗ sigma_3,
    R_A = (b tau_z + beta K tau_x) ⊗ I - beta S tau_y ⊗ sigma_3.

Block-diagonal plane reflections, with w = 3pi/4:

    M_t1 = |x+><x+| ⊗ sigma_{3pi/4} + |x-><x-| ⊗ sigma_{3pi/2},   M_t2 = |x+><x+| ⊗ sigma_0 + |x-><x-| ⊗ sigma_{3pi/4},
    M_r1 = |y+><y+| ⊗ sigma_{3pi/4} + |y-><y-| ⊗ sigma_{3pi/2},   M_r2 = |y+><y+| ⊗ sigma_0 + |y-><y-| ⊗ sigma_{3pi/4}.

Vertex projections:

    S_t = (I + R_B M_t)/2 (t = t1,t2),   S_r = (I + R_A M_r)/2 (r = r1,r2),   S_z = I ⊗ |3pi/4><3pi/4|.

Placement (v82 ribbon data): X has the cyclic order r1 -> r2 -> z, A the order r1 -> r2, Y the order t1 -> t2 -> z and B the order t1 -> t2. Each oriented column carries the + plane at its tail and the - plane at its head. Cells follow the v82 §4 product formulas: at each vertex, one row takes its first-circuit cells inside S_v and its second-circuit cells inside S_v-perp, and the other row the opposite. The first circuits are X at r, Y at t and X at z.

## 2. Operator identities, all exact

(I1) W = exp(-i (3pi/4) sigma_3/2) rotates equatorial Bloch angles by 3pi/4, and the block-off-diagonal part of R_B is beta(|x-><x+| ⊗ W + |x+><x-| ⊗ W*). W maps the angle 3pi/4 to 3pi/2 and 0 to 3pi/4. Hence R_B intertwines the two diagonal blocks of M_t1 and of M_t2, so [R_B, M_t] = 0. Explicitly, writing M_t1 = K I ⊗ sigma_m + S sigma_z ⊗ sigma_{m-pi/2} with m = 9pi/8, the two surviving commutator terms are -2i beta K S sigma_y ⊗ sigma_{m-pi/2} and +2i beta K S sigma_y ⊗ sigma_{m-pi/2}. They cancel. The same computation holds for t2 with m = 3pi/8. So S_t is a projection commuting with P_B.

(I2) [R_B M_t, R_Y] = 0. Expanding with r_Y = (gamma',0,gamma), the commutator is σ_y ⊗ [i gamma' b S^2 (σ_ω+σ_ρ) + v gamma σ_3 (σ_ω-σ_ρ)] + (gamma σ_x - gamma' σ_z) ⊗ [u_x(σ_ω-σ_ρ) + i v σ_3(σ_ω+σ_ρ)], where u_x = beta K, v = -beta S, and (σ_ω,σ_ρ) are the block Paulis. Using σ_ω+σ_ρ = 2Kσ_m, σ_ω-σ_ρ = 2Sσ_{m-pi/2} and σ_3σ_theta = iσ_{theta+pi/2}, the second bracket is 2(S u_x + K v)σ_{m-pi/2} = 0. The first is 2iS(gamma' b S K + v gamma)σ_m = 0 by gamma beta = gamma' b K. Hence S_t commutes with P_Y.

(I3) The mirror computations, with x± replaced by y± (the coefficients of x+ in y± are the same c, s), give [R_A, M_r] = 0 and [R_A M_r, R_X] = 0. So S_r commutes with P_A and P_X. S_z commutes with P_X and P_Y because both are first-factor projections.

(I4) Compressions. Let C+ be the compression of R_B M_t1 to y+ ⊗ K2. In the block form, C+ = b(c^2 σ_ω - s^2 σ_ρ) + 2cs beta σ_ρ W, with σ_ω = σ_{3pi/4} and σ_ρ = σ_{3pi/2}. As an equatorial vector this is e^{i(3pi/4 + 3pi/8)} b (K/gamma - iS). Here K/gamma = sin(pi/8)(3+2sqrt2) and S/(K/gamma) = cot(pi/8)/(3+2sqrt2) = sqrt2 - 1 = tan(pi/8). So arg(K/gamma - iS) = -pi/8, and b|K/gamma - iS| = (sqrt2-1)(sqrt2+1) = 1, since K^2/gamma^2 + S^2 = 3+2sqrt2. Thus C+ = σ_pi: the Y+ cells at t1 are y+ ⊗ |0> and y+ ⊗ |pi>. The y- compression is -b(K/gamma + iS) e^{i 9pi/8}, i.e. σ along angle 5pi/4: the Y- cells at t1 are y- ⊗ |pi/4> and y- ⊗ |5pi/4>. At t2 the same bracket with base angle 0 gives Y+ axis pi/4 and Y- axis pi/2. The mirror gives X+ axis 0 and X- axis pi/4 at r1, and X+ axis pi/4 and X- axis pi/2 at r2. Hence S_t and S_r have rank two and trace one against every incident circuit projection.

(I5) Pairwise anticommutators are scalar: {R_X,R_Y} = 2gamma, {R_X,R_A} = {R_Y,R_A} = {R_Y,R_B} = {R_X,R_B} = 2(sqrt2-1), and {R_A,R_B} = 2(1-sqrt2). The R_A/R_B value equals 2γ'^2K^2 + γ^2 - γ'^2K^4 - γ'^2K^2S^2/γ, computed with γ'^2K^2 = 10sqrt2-14, as 1-sqrt2. All are strictly between -2 and 2, so no two circuits share an eigenvector.

By (I1)-(I4) every vertex projection commutes with its two circuit projections and has trace one against each. The v82 §5 forward proof therefore makes every one of the ten rows and ten columns an ONB of C4.

## 3. The forty cells and MAX40

X cells (second factors): r1 X+ |0>,|pi>; r1 X- |pi/4>,|5pi/4>; r2 X+ |pi/4>,|5pi/4>; r2 X- |pi/2>,|3pi/2>; z X+ and X- |3pi/4>,|7pi/4>. The Y cells, with y in place of x, are: t1 Y+ |0>,|pi>; t1 Y- |pi/4>,|5pi/4>; t2 Y+ |pi/4>,|5pi/4>; t2 Y- |pi/2>,|3pi/2>; z Y± |3pi/4>,|7pi/4>. The A cells are the joint eigenlines of R_A with S_r1 and with S_r2, and the B cells those of R_B with S_t1 and S_t2.

Distinctness. X cells are distinct among themselves by their listed (sign, angle) pairs, and likewise Y cells. X versus Y holds because x± is not parallel to y±. Any coincidence between different circuits would be a common eigenvector of two circuit reflections, excluded by (I5). In the X/A product frame, S_r1 and S_r2 are I ⊗ (projections at the different non-orthogonal axes 0 and pi/4), so A cells at r1 and r2 differ; B is the same. All forty rays are pairwise distinct.

## 4. The complete TEN-class sector resolution

    N1 = {x+|pi/4>, x-|pi/4>, y+|5pi/4>, y-|5pi/4>},   N2 = {x+|5pi/4>, x-|5pi/4>, y+|pi/4>, y-|pi/4>},
    B1 = {x+|3pi/4>, x-|3pi/2>} + B-pair at t1,         B2 = {x+|7pi/4>, x-|pi/2>} + other B-pair at t1,
    B3 = {x+|0>, x-|3pi/4>} + B-pair at t2,             B4 = {x+|pi>, x-|7pi/4>} + other B-pair at t2,
    A1 = {y+|3pi/4>, y-|3pi/2>} + A-pair at r1,         A2 = {y+|7pi/4>, y-|pi/2>} + other A-pair at r1,
    A3 = {y+|0>, y-|3pi/4>} + A-pair at r2,             A4 = {y+|pi>, y-|7pi/4>} + other A-pair at r2.

The N classes are ONBs by orthogonality of second factors. In B1, the X-pair spans the +1 eigenspace of M_t1. The −1 eigenspace is invariant under R_B by (I1), and R_B is not scalar there, since b and beta are nonzero in the commutant Pauli decomposition. On that eigenspace 2S_t1 - I = -R_B, so its two R_B eigenlines are a B+ and a B- cell at t1 lying on opposite sides of S_t1, i.e. in opposite rows. B2 uses the complementary eigenspaces, B3 and B4 do the same with M_t2, and A1-A4 are the mirror. Each class is therefore an ONB.

Every cell is used exactly once: the twelve X cells are split as listed, and likewise the Y cells; B1-B4 use all eight B cells and A1-A4 all eight A cells. Rows: the only same-vertex pairs are the opposite-row A/B pairs, and all other cells lie at distinct vertices. Columns: with X ordered r1 -> r2 -> z, the used X-pairs occupy the column pairs (r2->z, z->r1), (z->r1, r1->r2) and (r1->r2, r2->z). None repeats a column, and Y is the same. A/B pairs use their two different columns. Hence each class has distinct rows and distinct columns.

## 5. Consequences and remaining gap

If confirmed, BARBELL admits an explicit octagonal ALL-SPARSE four-sector frame with a full TEN-class sector resolution. The 4+6 branch therefore cannot be closed by four-sector arguments alone, and v94-v97's exclusions are sharp around this octagonal survivor. To reach an original maximal 1-RQLS(10) one still needs, for the SAME placement: (i) a classical Latin square of order ten extending the ten-class labeling of these forty cells; (ii) a complementary H6 sector with 60 distinct rays, row/column ONBs and six-ray ONBs for the same ten labels; (iii) all 100 rays distinct, which is automatic across sectors. None of these is claimed. Independent exact verification of every identity above is required before any acceptance.

Imports: v76/v77 placement and local frames; v82 product formulas and the forward proof; v79/v80; v84/v86 BARBELL class pattern; v94-v97 derivations (motivation only, not premises of the verification); elementary Pauli algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S98, retaining ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including the v29 and v40 parallel-intent minors, the v30 dangling-reference defect, the v34 capture retry and this manuscript's disclosed zero-credit private mental decimal estimates.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
