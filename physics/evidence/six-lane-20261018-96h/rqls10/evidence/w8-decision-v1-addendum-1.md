# W8 decision note v1, addendum 1: the exotic flat planes are Clifford-symmetric; K4 forces one common stabiliser

Recorded 2026-10-19T02:45:27-0700 (from /bin/date). Extends evidence/w8-decision-v1.md (b24334cf9a255bab9fb08aa49a583f5ca6c654dcd2f776f74e2cf361fe595829).
Author ContinueRQLS10b; lane-internal, unreviewed; restricted to the W8 ansatz (H); target OPEN / UNKNOWN.

## 1. Float evidence (receipt below; one implementation; not a proof)
Probe code/w8_exotic_structure_v1.py (2c0bff3d...9ded) on the frozen v5 plane list:
- U := Q X Q F (Q = diag(zeta^(t^2)), F_(j,t) = zeta^(-jt)/sqrt5) is a Clifford unitary of projective order 3 with
  eigen-multiplicities (1, 2, 2); it maps the basis Z -> T -> X -> Z and L_1 -> L_3 -> L_2 -> L_1 (symplectically
  (a, c) -> (-c, a + c)).
- Each of the 100 exotic planes commutes with exactly ONE of the 25 conjugates U_w = W_w U W_w^* (w in Z_5^2), each
  U_w stabilises exactly 4 of them, and each such plane is (a line in the omega-eigenspace of U_w) (+) (a line in the
  omega^2-eigenspace) (trace check, deviation 8.7e-14). No MUB-pair plane commutes with any U_w.
- Exotic couple graph (gap rule; compatible lambda_1 <= 9.0e-17, incompatible >= 0.110): every exotic plane has
  exactly 5 compatible exotic partners per basis, and for EVERY compatible b-couple the stabiliser labels differ by an
  element of the line L_b (Z-couples: w_s - w_r in {(0, c)}; X-couples: in {(a, 0)}; T-couples: in <(1, 4)>).
  Exhaustive count of all-exotic K4 patterns: 0.

## 2. Exact consequences of the label rule (written, complete)
Lemma 5 (combinatorial). Suppose labels w_r in Z_5^2 (r in {00, 01, 10, 11}) satisfy w_s - w_r in L_b for every couple
(r, s) of b. Then all four labels are equal.
Proof. Put w_00 = 0, z = w_01 in L_Z, x = w_10 in L_X, y = w_11 in L_T. The X-couple 01-11 and the Z-couple 10-11 give
y - z in L_X and y - x in L_Z; since Z_5^2 = L_Z (+) L_X uniquely, z = y_Z and x = y_X (components of y). The T-couple
01-10 gives x - z in L_T. With y = s(1, 4): x - z = (s, 0) - (0, 4s) = (s, s) is in L_1, and lies in L_T = <(1, 4)>
only if s = 0. So x = y = z = 0.
Consequence. IF (a) every non-MUB-pair flat plane is U_w-invariant for some w (completeness; float evidence only) and
(b) the label rule holds for all compatible exotic couples (float evidence only), THEN in the surviving sub-case all
four representatives have planes stabilised by ONE common U_w, i.e. their planes lie among the 4 exotic planes of a
single conjugate, and W8 reduces to a FINITE exact check: 4^4 plane assignments for one U_w (by WH-translation
symmetry w = 0 suffices), each with the linear couple conditions and the frame condition V_12 V_23 V_31 = I. The float
count of such patterns is already 0 at the pairwise level.

## 3. Exact closure plan (replaces section 7 of the note; written/exact work, no numerical GO needed)
(E1) Classify the flat rank-2 projectors exactly: the 30 MUB-pair planes plus the planes l_omega (+) l_omega^2 of the 25
     conjugates U_w that are flat in Z (for U itself: two points of CP^1 x CP^1 with four real equations; four
     solutions expected), and prove there are no others (the polynomial system of section 5 of the note).
(E2) Prove the label rule, or replace it by an exact enumeration of the exotic couple graph (100 x 100 x 3 linear tests
     in a number field).
(E3) Exact check of the 4^4 assignments for U_0 (pairwise couple kernels; frames).
(E4) Proposition B without [I-H], or accept [I-H]: by the float data MUB-pair and exotic planes never couple.

## Receipt (probe run)
Launch record evidence/w8_exotic_structure_v1.launch.json sha256 e231d901db58988601f277fcead25a9546da81c35e622f37c7db8d4a452781d5;
input evidence/w8_flat_planes_couples_v5.result.json (0e20ee96...68fd, sha checked in-run: true). Command (cwd lane,
timeout 280): /bin/bash -c '...; exec /usr/bin/env -i TMPDIR=<lane>/tmp /opt/homebrew/bin/python3.14 -I -B
code/w8_exotic_structure_v1.py <input> <sha> evidence/w8_exotic_structure_v1.result.json'. START 2026-10-19T02:44:53-0700,
PID 54815 = PGID 54815, EXIT 0, END 02:45:03 (9.8 s); single process; lane tmp/ empty. Output (0444)
evidence/w8_exotic_structure_v1.result.json sha256 b13532bfea85828fee0ffe69f3200441a878e2a797c36751e0b30c92813b7ce0.
