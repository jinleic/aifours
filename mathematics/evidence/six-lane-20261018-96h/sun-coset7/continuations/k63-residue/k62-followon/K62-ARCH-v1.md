# K62-ARCH-v1: one finite certificate architecture for the K6.2* residue e_d >= 4, e* = 2 (PROPOSAL; not implemented, not run)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T06:15:30-0700.
- **Author:** Sun63Successor. Planning document only. Nothing here is a premise or a result. No computation was run;
  the parent HOLD `RUN/review/runtime-guard-admission-HOLD-v1.json` (sha256 6c1d8440…) is in force, and any execution
  needs a new exact parent item GO, a frozen universe/coverage/certificate contract, two independently authored
  checkers and parent replay. The frozen exploratory source `probe-survivor-map-v1.py` (sha256
  8569f726069766bd7ee0b284b5ded2396c0615e5fa14754bfe7211dff55d81be) is NOT part of this architecture and is unrun.

## 1. Why a finite architecture is plausible, and why it is not yet a proof
Written single-vertex tests do not close the residue (`K62-STATUS-v2.md`); the coupled 2-adic grid at d
(`K62-DG-v1.md`, candidate) excludes the worked pattern P_ob only after the shared triangle quotients tau are used at
three apexes. Every rule involved is a predicate on finitely many integers once exponents are capped. Whether all
patterns die is **unknown**; the architecture can only certify what it finds.

## 2. Universe U62 (pattern = everything the rules read)
1. Marker placement class: 3-marker on i*, on one O-vertex, or absent; 5-marker on d, i*, one O-vertex (possibly the
   3-marked one), or absent; with S5 acting on O only up to the marked vertices.
2. d-i* entries (alpha, alpha*) in {(1,1), (1,3), (3,1)} (K62-E3 Lemma 1; (1,3)/(3,1) only with a 3-marked O-vertex);
   d-O entries (1,1).
3. O-O joint entries in J_O = {(a, b) in {1,2,4}^2 : a + b <= 6} (K62-E3 Lemma 2 and C2 sub-claim (a)).
4. i*-O joint entries in {(a, b) in {1,...,5}^2 : a + b <= 6}, minus values excluded by the T rule on {d, i*, c}.
5. One tau-value per triangle and per family (alpha, alpha*): every triangle inside C and every triangle through d,
   ranging over multiples of tau_min in [tau_min, tau_max] (rules-k7-v1 L1).
6. Capped exponents: e_d in {4, 5, ..., 9, >= 10} (rules read e_d only through min(e_d, v2 T) with v2 T <= 9 for
   intersections of O-subgroups by the chain bound 1 + 2*4), f and h capped at 2 as in rules-k7-v1 Lemma CAP.

## 3. Rules (each must be a parent-accepted written lemma before use)
- R1 rows at O-vertices and at i* (LFC/VFC with the granularity bound of the chain lemma at that vertex; plain bound
  where the chain hypothesis fails);
- R2 T rule (L1) and the apex measures mu(U_y(U_x cap U_z)) = tau/(gamma_y alpha_xz), with forced equalities and
  containments by equal measure (finite sets) and K2-type non-containments;
- R3 vertex atom systems: at each vertex, the Boolean atoms of the X-sets, their grids (1/6 at O-vertices under the chain
  lemma, 1/12 at i* when f* = 1, 2^(-min(e_d, v2 T)) at d by DG-1), tightness D = Y, and allowed sets by (V3)/LFC (c);
  feasibility of the atom system as an exact rational LP (RPLP-type) with the tau-derived pair and triple bounds;
- R4 d-system of K62-DG (DG-1..DG-4, Theorem DG) and K62-SH in each family to which it applies.

## 4. Certificates and checking
Per canonical pattern: either a kill record (rule id; for LP kills an exact dual vector; for forced-relation kills the
ordered chain of forced equalities/containments ending in a violated allowed-set or measure inequality; for d-system
kills the integer inequality chain), or a SURVIVOR record. Coverage: a canonical enumeration of U62 with an
independently recomputed orbit count. Two checkers written independently from the frozen rule texts (not from the
producer), each recomputing every derived quantity (types, allowed sets, tau ranges, grids) and verifying every
certificate exactly; parent replay; mutation controls (a deliberately weakened rule must leave survivors; a known
survivor of the single-vertex tests, e.g. P_ob without R2/R4, must be reported as such).

## 5. The lemma that would make it complete
**CAP-62 (to be written and accepted first):** every configuration of the residue determines a pattern in U62 (all
entries, tau-values and capped exponents in the stated ranges), and every rule R1-R4 holds or fails for the
configuration exactly as it holds or fails for its pattern. With CAP-62 and the soundness of R1-R4, "no survivor in
U62" implies that the residue is empty. Without CAP-62 (in particular the e_d cap and the tau-range representation),
no exhaustive count would close anything. If survivors remain, the residue is not closed by these rules, and the
survivors are the exact targets for further written or group-theoretic work.
