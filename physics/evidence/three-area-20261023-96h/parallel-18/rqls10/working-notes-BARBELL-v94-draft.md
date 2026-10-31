# WORKING NOTES (not a manuscript, not a claim) — BARBELL(2,1,2) attack after v93

Owner PhysicsRQLS10-2. Started after actual clock Mon Oct 26 20:01:11 PDT 2026. Written reasoning only; no scientific execution.

## Setup (imports v84 §5, v86 §6)
Circuits X (route r1,r2,z), A (r1,r2), Y (t1,t2,z), B (t1,t2). X/A, Y/B repeated (isoclinic, v79); bridge X/Y at z forced isoclinic (v84).
Classes: PA∩PB = {A-pair,B-pair} (q), PA\PB = {A-pair,Y-pair} (4-q), PB\PA = {B-pair,X-pair} (4-q), NEITHER = {X-pair at r's, Y-pair at t's} (2+q), q<=2.
z X-cells only in PB\PA; z Y-cells only in PA\PB. Length-two circuit pairs (A,B) are same-vertex opposite-row pairs.
X/Y frame: P_X=|x+><x+|⊗I, P_Y=|y+><y+|⊗I, S_z = I⊗|ω><ω|. NEITHER class = {x+⊗ν, x-⊗ν, y+⊗ν⊥, y-⊗ν⊥}.

## Case q=2 (rigid)
PB\PA = the two z X-pair classes {x+⊗ω, x-⊗ω⊥}, {x+⊗ω⊥, x-⊗ω}; complements W_z=span(x+⊗ω⊥,x-⊗ω) and W_z⊥, each spanned by a B-pair at some t (one cell in S_t, one in S_t⊥).
PA\PB = the two z Y-pair classes; complements W'_z=span(y+⊗ω, y-⊗ω⊥) and W'_z⊥ spanned by A-pairs at some r.
NEITHER (4 classes) use all 8 r X-cells and all 8 t Y-cells. PA∩PB (2 classes).

(continuing)
q=2 derived so far:
- NEITHER X-pairs use all r X-cells; column r1->r2 forbids (X+ at r1, X- at r2), so all NEITHER X-pairs are same-vertex; sharing nu forces V_A pi_r ~ pi_r-perp for r=r1,r2. Hence S_r = |0><0|⊗Π_r + |1><1|⊗V_A*Π_rV_A has 2S_r-I = R_X⊗sigma_{pi_r} (product reflection). NEITHER nu's = {pi_1,pi_1⊥,pi_2,pi_2⊥}.
- Same for t's: V_B pi'_t ~ pi'_t⊥, 2S_t-I = R_Y⊗sigma_{pi'_t}; {pi'_t, pi'_t⊥} pairs = {pi_r, pi_r⊥} pairs as sets.
- W_z S_t-invariant (t hosting a PB\PA B-pair) => lambda_XY = 1/2 and omega unbiased to pi'_t; W'_z S_r-invariant => omega unbiased to pi_r (r hosting PA\PB A-pair).
- If both PB\PA B-pairs at one t: R_B = ±(R_Y⊗sigma_{pi'_t})(R_X⊗sigma_omega) = ±sigma_y⊗(m·sigma), m = n_{pi'_t} x n_omega. If both PA\PB A-pairs at one r: R_A = ±sigma_y⊗(m'·sigma), m' = n_{pi_r} x n_omega.
- Remaining: different-vertex hosting subcases; PA∩PB classes {A-pair at r', B-pair at t'}; find contradiction.

q=2 subcase SAME-HOSTS (both PA\PB A-pairs at r1, both PB\PA B-pairs at t1):
- R_A commutes with S_r2=sigma_z⊗sigma_{pi_r2} => m' ⟂ n_{pi_r2}; m' ⟂ n_{pi_r1}, n_omega => n_{pi_r2} in span(n_{pi_r1}, n_omega). Same for B.
- NEITHER set equality: axes {pi'_t1, pi'_t2} = {pi_r1, pi_r2}. If pi'_t1 ~ pi_r2 axis then omega unbiased to pi_r1 AND pi_r2 and n_{pi_r2} in span(n_{pi_r1},n_omega) => n_{pi_r2}=±n_{pi_r1}, duplicate X-cells. So pi'_t1 ~ pi_r1, pi'_t2 ~ pi_r2 axes, m=±m', R_B=±R_A.
- PA∩PB class: A-pair span Q at r2 invariant under sigma_z⊗sigma_{pi_r2}, sigma_x⊗sigma_{pi_r2} (S_t2), R_A. Product gives sigma_y⊗I. R_A = sigma_y⊗(m'·sigma) is CENTRAL in the generated algebra; on range P_A, sigma_y⊗I and sigma_z⊗sigma_pi restrict to two anticommuting reflections => irreducible => Q∩rangeP_A cannot be a 1-dim invariant line. CONTRADICTION. SAME-HOSTS closed.
- Remaining q=2: split hosts (A-pairs of PA\PB at r1 and r2, or B-pairs of PB\PA at t1 and t2). Then omega ~ n1 x n2 axis etc.

GENERAL q=2 (any hosts), with lambda_XY=1/2, R_X=sigma_z⊗I, R_Y=sigma_x⊗I:
- R_A commutes with S_r1,S_r2 (sigma_z⊗sigma_1, sigma_z⊗sigma_2, n1≠±n2) => R_A in commutant span{I, sigma_z⊗I, sigma_x⊗N, sigma_y⊗N}, N = unit Pauli along n1 x n2. R_A = a sigma_z⊗I + b sigma_x⊗N + c sigma_y⊗N.
- R_B in span{I, sigma_x⊗I, sigma_y⊗N', sigma_z⊗N'}; NEITHER set equality => N' = ±N.
- W'_z = span(y+⊗ω, y-⊗ω⊥) (2Pi-I = sigma_x⊗sigma_ω) P_A-invariant => a=0, b(n_N x n_ω)=0, c(n_N·n_ω)=0.
- W_z = span(x+⊗ω⊥, x-⊗ω) (2Pi-I = -sigma_z⊗sigma_ω) P_B-invariant => a'=0, b'(n_N·n_ω)=0, c'(n_N x n_ω)=0.
- So EITHER (I) n_ω ∥ n_N: R_A=±sigma_x⊗N, R_B=±sigma_z⊗N; OR (II) n_ω ⟂ n_N: R_A=±sigma_y⊗N, R_B=±sigma_y⊗N (P_B in {P_A,I-P_A}).
- PA∩PB class Q (A-pair at r', B-pair at t') invariant under sigma_z⊗sigma_r', sigma_x⊗sigma'_t', R_A, R_B.
  (II): R_A central; on rangeP_A the two S-reflections have anticommutator ∓2s (s=|n_r' x n'_t'|) => irreducible unless n'_t' ⟂ n_r'. Need n'_t' ⟂ n_r', so n'_t' = ±n_r'' and n1 ⟂ n2. (continue)
  (I): generated algebra has commutant span{I, sigma_y⊗K'}, K' along n_N x n'_t'; Q invariant also under I⊗K_r (K_r along n_N x n_r') => need n'_t' ∥ n_r' and Q = eigenspace of sigma_y⊗K'. (continue)

q=2 CLOSED:
- (I) n_ω ∥ n_N: R_A=±sigma_x⊗N acts on W'_z=span(y+⊗ω,y-⊗ω⊥) as the SAME scalar s (sigma_x y±=±y±, Nω=sω, Nω⊥=-sω⊥) => W'_z cannot contain both an A+ and an A- cell. CONTRADICTION.
- (II) n_ω ⟂ n_N: R_B=±R_A=±sigma_y⊗N central for Q; if n'_t' not ⟂ n_r' the restricted reflections on rangeP_A are noncommuting => no invariant line Q∩rangeP_A; if n'_t' ⟂ n_r' they coincide up to sign on rangeP_A (anticommutator ∓2) => A+ cells at r' equal B± cells at t' (P_B = P_A or I-P_A) => duplicate rays. CONTRADICTION.
- So q=2 has no original MAX1 resolution.

NEXT: q in {0,1}: PB\PA has 4-q>=3 classes (4 z X-cells + 4-2q r X-cells), NEITHER 2+q, v86: A/Y and B/X interior-isoclinic or degenerate.

q<=1 FRAMEWORK (X/Y frame, x-basis Paulis sigma):
- PA\PB A-pairs at BOTH r (q<=1) => R_Y commutes with both A-pair plane reflections => V_A = rotation about n_N (n_N ⟂ n_1,n_2) by psi. Same for V_B about n'_N by psi'.
- R_A = alpha sigma_z⊗I + alpha'(cos(psi/2) u·sigma⊗I + sin(psi/2) u'·sigma⊗N) type; NEITHER same-vertex X-pair <=> psi = pi (V_A flip). q=1: 3 NEITHER need >=1 same-vertex pair (only 2 X+ at r2) => psi = psi' = pi; NEITHER rays => {n'_t axes} = {n_r axes}, N' = ±N.
- With psi=psi'=pi: PB\PA X-pair planes = eigenspaces of M'_t = R_B(2S_t-I), must commute with R_X => lambda_XY=1/2 (R_Y=sigma_x⊗I), R_B = beta sigma_x⊗I + beta' sigma_y⊗N; similarly R_A = alpha sigma_z⊗I + alpha' sigma_y⊗N.
- M'_t on rangeP_X = m'_t+ ·sigma, on kerP_X = m'_t- ·sigma, m'_t± = beta n'_t ± beta' k'_t, k'_t = n_N x n'_t. X+ cells in PB\PA at t have Bloch ±m'_t+, X- cells ±m'_t-; a class pairs eps m'_t+ with eps m'_t-.
q=1 CLOSED: PB\PA = 2 classes at t_a (both eigenspaces) + 1 at t_b. z X+ cells (Bloch ±n_omega) need {±m'_ta+} = {±n_omega} (else <=1 z X+). z X- likewise need {±m'_ta-} = {±n_omega} => m'_ta- = ±m'_ta+ => beta'=0 (P_B=P_Y or I-P_Y, contradicts strict Y/B angle) or beta=0. beta=0: m'_t± = ±k'_t; t_b gives r X+ cell Bloch eps k'_tb = ±n_r with n'_tb = ±n_r'' => n_1 ⟂ n_2; then n_omega = ±k'_ta in {±n_1,±n_2} => z X-cell duplicates an r X-cell. CONTRADICTION.
q=0 PLAN: PB\PA X+ = one t (t_z) with z X+ pair, other t (t_r) with same-vertex r X+ pair at r*; NEITHER uses X+ at r**≠r*. Subcases: (a) psi=pi; (b) both NEITHER pairs cross (X+ r2 with X- r1), psi≠pi possible.

q=0 subcase (a)+(a') [psi=psi'=pi]: same normal forms R_X=sigma_z⊗I, R_Y=sigma_x⊗I, R_A=alpha sigma_z⊗I+alpha' sigma_y⊗N, R_B=beta sigma_x⊗I+beta' sigma_y⊗N'.
- X- side Option 2 (t_z hosts r X- pair) forces mixed PB\PA pairs (zX+,r2X-),(r1X+,zX-), hence NEITHER cross pairs, impossible when V_A is a flip (X- at r has Bloch ±n_r, cross needs n_2=±n_1). So Option 1: {±m'_tz-}={±n_omega} => beta=0. Symmetric => alpha=0.
- Option 1 gives k'_tr=±n_r* and NEITHER Y+ at t** with n'_t**=±n_r** => n'_N=±n_N => R_B=±R_A=±sigma_y⊗N; n'_tr ⟂ n_r* => restricted S reflections on rangeP_A agree => A-cells at r* duplicate B-cells at t_r. CLOSED.
q=0 subcase (b) [both NEITHER X-pairs cross: X+ at r2 with X- at r1]: PB\PA pairs all mixed (zX+,r2X-) at t_z, (r1X+,zX-) at t_r. M'_tz = ±(|x+><x+|⊗sigma_omega + |x-><x-|⊗sigma_rho), M'_tr = ±(|x+><x+|⊗sigma_1 + |x-><x-|⊗sigma_omega'), rho = r2 X- factor.
- (2S_tz-I)(2S_tr-I) = M'_tz M'_tr commutes with R_Y => sigma_omega sigma_1 = sigma_rho sigma_omega (if omega'=omega) => n_rho = rotation of n_1 by pi about n_omega. Combined with V_A: n_rho = ±R_{-psi} n_2 = ±R_{-2psi} n_1. Need n_1·n_omega=0 (=> psi=±pi/2, n_1⟂n_2) or n_omega ⟂ n_N. (continue; check omega' bookkeeping)

AFTER v95 (q=0, X-side cross, psi≠pi):
- From sigma_omega sigma_1 = eta sigma_rho sigma_omega and axis(rho)=R_{-2psi}(axis n_1) (rotation about n_N): (n_1·n_omega)(n_omega·n_N)=0.
  Case A: n_1⟂n_omega => psi=±pi/2, n_1⟂n_2, rho axis = n_1 axis. Case B: n_omega ⟂ n_N => B1 n_omega=±n_2 (duplicate) or B2 n_omega ⟂ n_2 in plane P⟂n_N.
- X-cross + Y-FLIP (psi'=pi): Lemma PB gives mirror pairs m'_t± about n'_t; NEITHER Y same-vertex at t** gives n'_t** axis = n_2 axis; n'_N=±n_N; Case A => n_omega in P, ⟂n_1 => n_omega=±n_2 duplicate; Case B2 => bisector condition at t** forces psi=±pi/2 => n_omega=±n_1 duplicate. EXCLUDED.
- X-cross + Y-cross: commutant of {M'_tz, M'_tr} = {[[a, bW*],[cW, d]]} (W intertwiner, W n_omega=n_rho, W n_1 = eta n_omega). R_B = b_z sigma_z⊗I + Re/Im beta_c terms. (2S_t-I) commuting with R_Y gives W* = e^{i phi} sigma_omega W sigma_omega (so W axis ⟂ n_omega; axis ∥ n_omega gives rho=omega duplicate) and 2 gamma conj(beta_c) W* = gamma' b_z (I + sigma_omega sigma_rho): gamma=0 => b_z=0; gamma≠0 => W = minimal rotation n_omega->n_rho. beta_c≠0 (else rho=omega-perp duplicate). (continue: combine with Y-side mirror + NEITHER Y cross)

(continuing)
