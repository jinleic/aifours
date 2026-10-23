# phys-2 written slice: WH_5 (x) C^2 orbit ansatz (W8) - scope freeze v1, written BEFORE the derivation

Recorded after actual `/bin/date`: 2026-10-19T16:33:12-0700. Author ContinueRQLS10b. Lane-internal, single author.
Authority: RUN/control/six-slot-written-resumption-20261019-1603-v1.json
(sha256 ac09b46532a233c6d9ce1b227c3dffecee9655bd83413d96d3a403065a0ef0f8), slot phys-2, plus the parent IRC of the same
transition. Global runtime HOLD unchanged; this slice has no launch authority. The frozen guard package v9 / full
matrix / supervisor19 stay immutable and NOEXEC and are not touched here.

## Frozen target (verbatim from the transition)
"Written analytical W8 WH5 tensor C2 ansatz: exact row/column/transversal ONB and ray-distinctness equations; attempt
symbolic witness or ansatz-wide no-go, never unrestricted no-go. Read existing W8 setup and do not duplicate old sampled
work."

## Hypotheses (H) - exactly the W8 ansatz
zeta = e^(2 pi i/5); on C^5: X e_t = e_(t+1), Z e_t = zeta^t e_t (t in Z_5). Rows, columns and symbols are
Z_5 x Z_2 (= Z_10 by CRT); B(i, j) = i + j (Cayley table). Cell ((i1,i2),(j1,j2)) carries
q = (X^i1 Z^j1 (x) I_2) x_(i2 j2), x_r in C^5 (x) C^2, written as 5 x 2 matrices X_r, r in {00, 01, 10, 11}.
Requirement: every row, every column and every B-class ("transversal") of the 10 x 10 array is an orthonormal basis of
C^10; the target is maximal cardinality (100 pairwise non-parallel cell rays). Inputs re-read for this freeze:
setup evidence/w8-wh5-c2-orbit-ansatz-setup-v1.md (bedfe9a7b35771f4c4e119c8431535d839c87180170bc67523fee6c6c5ce6471),
its addendum 1 (213f2fa7115d84c47b42c0237165a44c7d579d1f577498450ef97c092edc2fc9), evidence/w8-decision-v1.md
(b24334cf9a255bab9fb08aa49a583f5ca6c654dcd2f776f74e2cf361fe595829) and its addendum 1
(716051d982f4e6ceed6664148cd0ce5077701dda9264a8952e34c5c4123797f5), R11 (30b3a3a0f68e78f455160d111615aeb14c8ee9c85b86270b7439f5b64c3fc469),
evidence/wh10-flat-planes-v1.md (52a4536a211cb05e1d63b6f37c2b07fb12331bcb386b26157a662dc501c835b3, notation only) and
the parent W8 LM audit RUN/review/rqls10-w8-lm-parent-audit-v1.json (444fe891f6477746f2aca8ead5b379b01d6444c247bd6673d3977a72fbe040fc).

## Deliverables (frozen)
D1. Exact row / column / transversal ONB conditions reduced to the four representatives, with a complete proof (explicit
    eigenbases and phases of Z, X and X Z^-1; character orthogonality on Z_5), in row-vector form and in Gram /
    flat-plane form (Gram lemma re-proved inside the package, not imported).
D2. Exact ray-distinctness: a complete characterisation of all coincidences among the 100 cell rays, the possible
    cardinalities, and the exact list of inequations equivalent to maximal cardinality.
D3. Any further exact reformulation used by the attempt (each with proof inside the package).
D4. Attempt, with exactly one outcome class:
    WITNESS - explicit exact X_r with every reduced equation and every distinctness inequation verified in writing;
    ANSATZ_NO_GO - complete written proof that (H) has no solution (any cardinality, or maximal cardinality only,
      whichever is proved, stated exactly);
    UNRESOLVED - the exact remaining equation system, stated so that it is equivalent to (H), plus every restricted
      result that is completely proved inside the package (each with its exact restriction).

## Non-goals and constraints
No statement about unrestricted 1-RQLS(10) (target stays OPEN / UNKNOWN). No numerical search, computation, CLI
tool, import, test, compile or nested agent; only reading, writing, hashing and actual `/bin/date`. Old sampled /
float W8 work (z5_flat_rank2_projectors_v1, w8_flat_planes_couples_v3-v5, w8_exotic_structure_v1, rqls_w8_lm_v2) is
cited as evidence only, never as a premise, and is not re-done. Earlier lane theorems (Theorem A, Lemmas 2-5,
Proposition B) are single-author and unreviewed: they may be cited as context but are premises of a new claim only
if re-proved inside the package. Named mathematical imports allowed: character orthogonality on Z_5, the Gauss-sum
modulus |sum_t zeta^(a t^2)| = sqrt5 (a != 0), elementary facts on antiunitary operators; any further import must be
named at the point of use. Package <= 100 KB, new files with exclusive creation, frozen 0444, full SHA-256 receipt;
checkpoints <= 1800 s (target 1200 s); park after delivery.

## Disclosure of prior sketches (made while reading, 16:05-16:33, before this freeze; nothing written elsewhere)
1. Re-derivation of the Gram lemma X_r^* X_r = I/2 from the six K4 couples (as in the setup addendum).
2. A reformulation: a solution is equivalent to one flat plane P (rank-2 projector with diagonal 2/5 in Z, X, T) and
   three antiunitary involutions A = D_1 K_Z, B = D_2 K_X, C = D_3 K_T (D_b diagonal unitary in basis b) such that APA,
   BPB, CPC are flat and diag_Z(BPC) = diag_X(APC) = diag_T(APB) = 0; explicit matrix forms A v = D_1 conj(v),
   B v = C_2 Pi conj(v) (C_2 circulant), C v = Q C_3 Q Pi conj(v) (Q = diag(zeta^(2t^2)), C_3 circulant).
3. Ray distinctness: intra-orbit coincidences impossible by rank 2; cardinality in {25, 50, 75, 100}; 120 inequations.
4. Triangle relation Theta V = V J with Theta a product of three couple antiunitaries, hence Theta^2 = -1 on the plane;
   in odd dimension the (-1)-eigenspace of the square of an antiunitary has even dimension (2 or 4 here).
5. Scalar couple maps (every D_b a scalar) give Theta^2 = +I, contradicting item 4.
6. Clifford-diagonal couple maps make Theta^2 a Clifford unitary (possible restricted analysis).
7. Pluecker-coordinate form of the compatibility of two flat planes in one basis.
8. Reduction idea for configurations symmetric under an order-3 Clifford cycling Z -> T -> X.
9. Expectation (from the cited float evidence, not a premise): no witness exists; a complete no-go probably needs the
   exact flat-plane classification (closure items E1-E4 of the decision-note addendum).
All of these are unverified until written with complete proofs in the package; any that fails is reported as failed.
