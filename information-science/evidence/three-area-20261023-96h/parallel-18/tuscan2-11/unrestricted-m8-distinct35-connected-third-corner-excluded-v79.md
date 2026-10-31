# Actual Tuscan11 distinct 3+5, CONNECTED two-tail system — excluded by the third corner at b_v

Actual `/bin/date` before this body: **Mon Oct 26 11:32:12 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Setting (imported)

This is line (4) of the parent-accepted m = 8 census, v12 §5.2 (SHA256 `c2a9283d09b06781e0f1b76a42a0dcb700913dc87bddf69aabae78ff32caf6b2`; accepted node A_v12 of manifest v12). The whole support graph is connected, with no reverse pair, and the core consists of:
- two threads X, Y from b_v to b_w;
- a loop at b_w;
- a tail T_v from b_w to a leaf labelled v, of length l_v;
- a tail T_w from b_v to a leaf labelled w, of length l_w, with 1 ≤ l_w ≤ 6.

The vertex b_v (label v) has degree 3, with half-edges X, Y and T_w. The face count (F1 or F3) plays no role below.

**Other imports:**
- the exchange identity (every row carries the 11 labels once);
- the identity d(x) = 10 of v12 (2), for the connected 11-row case.

## 2. Each label has exactly one cut, and the leaves are the cuts of v and w

Each label x occurs in all 11 rows. Its vertex degrees sum to d(x) = 10, and every support edge is traversed twice. So the 11 occurrences of x use 20 half-edge incidences.
- An interior occurrence uses two incidences.
- A row end uses one, and a cut vertex accounts for two row ends.

Hence x has exactly one cut. A degree-1 vertex must be a row end, so the leaf labelled v is the unique v-cut and the leaf labelled w is the unique w-cut. In particular **b_v is never a row boundary.**

## 3. The two tail rows at the leaf w

The rotation at b_v has three corners. Two of them involve T_w: they are where the face enters and leaves the spur T_w. The third joins X and Y.

Let R_in be the row ending at leaf w and R_out the row starting there. Since l_w ≤ 6 < 10, R_in consists of:
- the whole of T_w together with b_v;
- then, before b_v, an arm of 10 − l_w vertices along one of X, Y (the half-edge of the corner preceding T_w).

R_out is the same with the other thread.

Neither arm can reach b_w, since the row would then hold w twice, once at b_w and once at leaf w. So |X|, |Y| > 10 − l_w, and the arms are X[1..10−l_w] and Y[1..10−l_w].

R_in and R_out share exactly leaf w, the interior of T_w and b_v. By the exchange identity,

    L(X[1..10−l_w]) = L(Y[1..10−l_w]) =: S_w,   |S_w| = 10 − l_w.          (1)

## 4. The third corner is impossible

Let R_xy be the row through b_v's third corner, between X and Y. It differs from R_in and R_out, since a row contains b_v at most once. Since b_v is not a boundary, R_xy contains X[1..a] and Y[1..b] with a, b ≥ 1. Its remaining vertices go beyond b_w on at most one side; both sides cannot, since b_w would occur twice.

**The disjoint subsets.** Put m_X = min(a, 10−l_w) and m_Y = min(b, 10−l_w).
- By (1), L(X[1..m_X]) and L(Y[1..m_Y]) are both subsets of S_w.
- They are disjoint, because R_xy carries distinct labels.
- Hence m_X + m_Y ≤ 10 − l_w.

**Both sides stay inside the threads.** Then a + b = 10.
- If a, b ≤ 10−l_w, then m_X + m_Y = 10 > 10−l_w.
- If a > 10−l_w, then m_X + m_Y ≥ (10−l_w) + 1. The case b > 10−l_w is symmetric.

**One side reaches b_w,** say the X side. Then a = |X|−1 ≥ 10−l_w, so m_X + m_Y ≥ (10−l_w) + 1.

Every case violates m_X + m_Y ≤ 10 − l_w. So **R_xy cannot exist.** But b_v has degree 3, and its X–Y corner is visited by some face, so some row passes through it. Contradiction.

## 5. Result

**The connected distinct 3+5 two-tail system (line (4) of the v12 census, owner residual R4) is impossible** (WRITTEN). This holds for both face counts, every tail length 1 ≤ l_w ≤ 6 and every placement of the loop and of T_v; only the tail T_w at b_v is used.

Combined with v73–v75 (class (b)), the owner-written m = 8 residual becomes:
- **R5:** distinct 3+5 disconnected (Type I with r_P = 3, 4; Type II with r_P = 2; and the Type II, r_P = 3 survivors S1, S2, S2′ listed in v78);
- **R6:** all m ≥ 9.

As always, this assumes every unreviewed owner body is correct.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
