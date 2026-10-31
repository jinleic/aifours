# RQLS10 v92 — THETA(1,2,2): a length-imbalance count forces at least two {X,Y} classes, hence X/Y isoclinic; three-label classes are trace-rigid

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 19:39:53 PDT 2026**. AUTHOR-WRITTEN CANDIDATE, not machine/kernel checked. Written counting/trace/two-projection arguments only; no scientific Eval/interpreter/CAS/program/enumeration/solver/replay, approximate scout, chosen angle/state/control/probe or newGO.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption or verdict inheritance.

## 1. Setting

The all-sparse THETA(1,2,2) topology (v82): circuits X (route v1,v2,v4) and Y (route v1,v3,v5) of length three, and a (v2,v3), b (v4,v5) of length two. X has 12 cells, Y has 12, a has 8 and b has 8. Assume ordinary MAX and ONE full TEN-class resolution. By v86 every class has label set XY, Xa, Xb, Ya, Yb, ab, Xab or Yab, with at most two cells per label. Every adjacent two-plus-two class forces its pair to be interior-isoclinic. v87 showed that X/Y is isoclinic or all four side pairs are.

## 2. Theorem LI: at least two {X,Y} classes exist, so X/Y is ALWAYS interior-isoclinic

For each class define its imbalance (number of X- and Y-cells) minus (number of a- and b-cells). Summing over the ten classes gives the cell totals

    sum of imbalances = (12+12) - (8+8) = 8.

Per class: XY contributes +4; Xa, Xb, Ya, Yb contribute 0; ab contributes -4. A three-label class Xab with composition (x,a,b) in {(2,1,1),(1,2,1),(1,1,2)} contributes x-(a+b) in {0,-2,-2}; likewise Yab. Hence

    4 n_XY - 4 n_ab + (non-positive three-label terms) = 8,
    n_XY >= n_ab + 2 >= 2.

{X,Y} classes therefore exist, and by v86's vertex form at v1 X/Y is interior-isoclinic in EVERY full resolution. This removes v87's alternative "all four side pairs isoclinic" as a substitute: X/Y isoclinicity is unconditional. The count uses only cell totals and the v86 label list.

## 3. Theorem TR: trace rigidity of three-label classes

Suppose X/a and X/b are interior-isoclinic, with scalar anticommutators {R_X,R_a} = 2 alpha I and {R_X,R_b} = 2 beta I. For an eigencell t with R_a t = eps t, the expectation is <t,R_X t> = eps alpha. Consider a class with label set {X,a,b}.

* Compositions (1,2,1) and (1,1,2) are IMPOSSIBLE. In the R_X trace, the doubled pair cancels, leaving eps_x + eps_b beta = 0 (or eps_x + eps_a alpha = 0). That would force |beta| = 1 (or |alpha| = 1), contradicting interior angles.
* In composition (2,1,1) the X-pair cancels in the R_a and R_b traces. Hence <b,R_a b> = -eps_a and <a,R_b a> = -eps_b, where a,b denote the class's single a- and b-cells. Each is a reflection expectation of modulus one, so the cells are eigenvectors:

      a-cell in P_a^(eps_a) cap P_b^(-eps_b),     b-cell in P_b^(eps_b) cap P_a^(-eps_a).

  Thus the class's a- and b-cells are COMMON eigenlines of P_a and P_b, of complementary type, i.e. lines of one ENDPOINT CS block of the pair (P_a,P_b). The R_X trace further gives eps_a alpha + eps_b beta = 0.
* If P_b is NOT P_a or I-P_a, the pair (P_a,P_b) has at most four common eigenlines, each one-dimensional. By MAX each carries at most one cell, and each such class uses two of them. Hence at most TWO {X,a,b} or {Y,a,b} classes exist under the corresponding side isoclinicity, and if any exists, P_a and P_b have an endpoint CS block. In the degenerate case P_b in {P_a,I-P_a}, the displayed membership reduces to an orientation condition eps_a = -eps_b (resp. eps_a = eps_b), and no count bound is claimed.

The same statements hold for {Y,a,b} classes when Y/a and Y/b are isoclinic.

## 4. Scope and frontier

New paid results: Theorem LI, giving unconditional X/Y isoclinicity and n_XY >= n_ab + 2, and Theorem TR. THETA(1,2,2) existence or exclusion remains OPEN; so do C5 (no length imbalance, since all circuits have length two), BARBELL, THETA(1,1,3), dense d in {2,3,4,5}, other sector placements, minimal-rank-3 and higher-rank families, complementH6, actual100 distinct rays and the SAME TEN-class resolution. All original irreducible10, 4+6 and 5+5 branches remain OPEN.

Imports: v82 topology, v86 label list/route avoidance/vertex form, v87 THETA(1,2,2) addendum, v78/v80 scalar-anticommutator expectations, and the actual primary TEN-transversal/CLASSICAL-mate interface. No NR/classifier/Butson/Gaussian/code premise, measure genericity, chosen frame or global tensor WLOG. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S92, retaining ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including the disclosed v29 parallel-intent minor, the v30 dangling-reference defect and the v34 capture retry. Frozen Mainv17/S72/input map/proofs/live151 stay immutable. v87's weaker alternative statement remains as historically paid, prospectively strengthened here, not edited.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
