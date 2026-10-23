# B3 A/Z corner: purity laws for the other four squares and corner Latin compatibility — CANDIDATE v1

Frozen at 2026-10-19T17:41:42-0700 under `SCOPE-FREEZE-v1.json` (SHA256 `8c2e75c50d4df3ebc28ac98292c71382939213aff49636b55804fe3950334de6`). Status: CANDIDATE written mathematics, not reviewed or accepted. Every lemma used is re-proved here. No script, assertion, enumeration, CLI or nested agent was used.

**Outcome: PROVED NEW NECESSARY CONDITIONS PLUS AN EXPLICIT UNRESOLVED BOUNDARY. No family is excluded.**

The corner is rows {1,7} of square 1 together with columns {2,3}, read in the actual interior row and column frames of all five squares. There, squares 2-5 are forced to be almost entirely **pure**:
- in each of rows 1 and 7, at least 12 of their 16 (square, U-coordinate) pairs are realized by vectors that are unit multiples of e_d;
- in each of columns 2 and 3, at least 12 of their 16 (square, own-index) pairs are realized by unit multiples of their own column-0 vectors q_s^r.

Under the further hypothesis that square 1 carries all A-content of rows 1 and 7 in the corner cells (a hypothesis, not a proved fact), squares 2-5 form two forced 4x4 Latin-type patterns of pure A-vectors in rows 1 and 7, columns 4-7, which never repeat a coordinate in any column. These statements are not in the prior notes. They sharpen that notes' slot bounds KA/KA' into purity counts and couple rows 1 and 7 through the column frames 4-7. All B3 axes, phases and general interior vectors are retained. Nothing here is claimed for Boolean models, GB, B2 or n=8.

## 1. Setting and re-proved basics

H1: Q_1,...,Q_5 are a full genuine set of pairwise-orthogonal QLS(8) ([PRIM] LF195-225). H2: Q_s(0,c) = w_{s,c}e_c. H3 (SB2). H4: the exact template [J], so that supp q_1^1 = supp q_1^7 = {1,2,3} and supp q_1^6 = {2,3}. Put q_s^r := Q_s(r,0), V_A := span{e_1,e_2,e_3}, U := {0,1,2,3} (coordinates) and O' := {0,1,6,7} (own indices).

- **(F1)** At an interior cell (i,c): coordinate c and own index i are absent, by orthogonality to Q_s(0,c) = w e_c and to q_s^i.
- **(F2)** For each coordinate d != c at (i,c), at most one square has <e_d,Q_s(i,c)> != 0, by H1 applied to (i,c) and (0,d). For each own index r != i, at most one square has <q_s^r,Q_s(i,c)> != 0, by H1 applied to (i,c) and (r,0).
- **(AX)** For r >= 1 and d >= 1, H1 applied to (r,0) and (0,d) shows that no two squares have coordinate d in their r-th axis vector. Also q_s^r ⊥ q_s^0 = w e_0. Hence, for s >= 2, q_s^1 and q_s^7 are ⊥ V_A ⊕ span{e_0}, and q_s^6 ⊥ e_0, e_2, e_3.
- **(S)** Parseval. In a full row i of square s, sum_{c>=1} |<x,Q_s(i,c)>|^2 = 1 − |<x,q_s^i>|^2 for every unit x. In a full column c, sum_{i>=1} |<x,Q_s(i,c)>|^2 = 1 − |<x,e_c>|^2.
- **(P) Purity criterion.** If a unit vector x has mass 1 along a line and is carried by a single cell of that line, then that cell's vector is ω x with |ω| = 1.

## 2. Theorem U (common-frame purity of squares 2-5 in rows 1 and 7)

Let r ∈ {1,7}. For s >= 2 and d ∈ U, put n_{s,d} := #{c ∈ {1..7} : <e_d,Q_s(r,c)> != 0}. Let σ_1 be the number of pairs (c,d) with d ∈ U and <e_d,Q_1(r,c)> != 0. Then:

    sum_{s=2..5} sum_{d ∈ U} (n_{s,d} − 1) <= 9 − σ_1 <= 4.

Every pair (s,d) with n_{s,d} = 1 is carried by a cell with Q_s(r,c) = ω e_d. Hence at least 12 of the 16 pairs (s,d) are pure basis vectors. Restricting to A-coordinates gives sum_{s>=2, d ∈ A} (n_{s,d} − 1) <= 6 − σ_1^A <= 2, where σ_1^A counts only d ∈ A. So at least 10 of the 12 A-pairs are pure.

*Proof.*
- **Slots.** Row r has U-slots (c,d) with d ∈ U \ {c}: 3 each for c ∈ {1,2,3} and 4 each for c ∈ {4..7}, so 25 in total. By (F2) each slot is used by at most one square.
- **Demand of squares 2-5.** For s >= 2, (AX) gives q_s^r ⊥ U. So by (S) each d ∈ U has mass 1 in row r, and n_{s,d} >= 1. These pairs use sum n_{s,d} slots, so sum_{s,d} n_{s,d} <= 25 − σ_1.
- **σ_1 >= 5.** The coordinate-0 mass of square 1 in row r is 1, so at least one cell carries coordinate 0. Projecting the row resolution of the identity onto V_A gives sum_c P_A|Q_1(r,c)><Q_1(r,c)|P_A = P_A − |q_1^r><q_1^r|, the projector onto P_r := V_A ∩ (q_1^r)^⊥. This has rank 2, and each cell carries mass at most 1, so at least two cells have nonzero A-part. Each such A-part lies in P_r, which contains no e_d: e_d ∈ P_r would need <e_d,q_1^r> = 0, but q_1^r has full support {1,2,3}. So each such A-part has support of size at least 2. Hence σ_1^A >= 4 and σ_1 >= 5.
- **Purity.** Apply (P) with x = e_d. Each pair with n >= 2 contributes at least 1 to the sum. The A-version is the same count with 18 slots, demand 12 and σ_1^A >= 4.
QED

## 3. Theorem U' (own-frame purity of squares 2-5 in columns 2 and 3)

Let c ∈ {2,3}. For s >= 2 and r ∈ O', put m_{s,r} := #{i ∈ {1..7} : <q_s^r,Q_s(i,c)> != 0}. Let τ_1 be the number of pairs (i,r) with r ∈ O' and <q_1^r,Q_1(i,c)> != 0. Then:

    sum_{s>=2} sum_{r ∈ O'} (m_{s,r} − 1) <= 9 − τ_1 <= 4,

and every pair with m_{s,r} = 1 is carried by a cell with Q_s(i,c) = ω q_s^r. Hence at least 12 of the 16 pairs are pure own-frame reuses.

*Proof.*
- **Slots.** These are (i,r) with r ∈ O' \ {i}, by (F1): 3 each for i ∈ {1,6,7} and 4 each for i ∈ {2,3,4,5}, so 25 in total. By (F2) each slot is used by at most one square.
- **Demand of squares 2-5.** For s >= 2 and r ∈ O', the own-r mass in column c is 1 − |<q_s^r,e_c>|^2 = 1. This holds for r = 0 because q_s^0 ∝ e_0, for r ∈ {1,7} by (AX), and for r = 6 because q_s^6 ⊥ e_2, e_3 by (AX) and c ∈ {2,3}.
- **τ_1 >= 5.**
  - Own index 0 of square 1 has mass 1 in column c, because q_1^0 ∝ e_0 ⊥ e_c.
  - Column c's A-content is P_A − |e_c><e_c|, of rank 2, so at least two cells have nonzero A-part a ⊥ e_c. For r ∈ O, <q_1^r,Q_1(i,c)> = <q_1^r,a>.
  - If such an a had a single own index r ∈ {1,6,7}, then a ∝ q_1^r with c ∉ supp q_1^r. This is impossible, because q_1^1, q_1^6, q_1^7 all contain coordinates 2 and 3. So each A-cell uses at least two own slots, and τ_1 >= 1 + 4.
- **Purity.** Apply (P) with x = q_s^r.
QED

## 4. Theorem L (corner-saturated Latin compatibility; a family statement)

Hypothesis Σ: for both r ∈ {1,7}, the nonzero A-parts of square 1 in row r lie exactly in the three corner cells (r,1), (r,2), (r,3).

Under Σ:
- (a) σ_1^A(r) = 6 for r ∈ {1,7}.
- (b) In each row r ∈ {1,7}, every square s >= 2 holds pure vectors ω e_1, ω e_2, ω e_3 at three distinct columns of {4..7}. At each cell (r,c) with c ∈ {4..7}, exactly three of the four squares hold the three pure A-vectors, and the fourth has no A-coordinate.
- (c) For each square s >= 2 and column c ∈ {4..7}, its pure A-vectors at (1,c) and (7,c), when both exist, are different coordinates.

Consequently, the two 4x4 arrays (squares × columns {4..7}, entries in {1,2,3,blank}) are Latin with one blank per row and per column, and they have no common non-blank entry at any position.

*Proof.*
- **(a).** In a corner cell the A-part lies in the line V_A ∩ {q_1^r, e_c}^⊥. Its generator has support exactly A \ {c}: a vector of span{e_a,e_b}, {a,b} = A \ {c}, orthogonal to q_1^r, which has both coordinates nonzero. So it has two nonzero coordinates, and σ_1^A = 2 + 2 + 2.
- **(b).** The A-version of Theorem U gives total excess at most 0, so every (s,d) with d ∈ A is a pure single cell. Each corner cell's two A-slots are used by square 1. The remaining 12 A-slots lie in columns 4..7, three per cell, and the 12 pure vectors fill them bijectively by (F2). A square has one vector per cell, so its three pure vectors lie in three distinct columns.
- **(c).** Column c of square s is orthonormal, and two vectors proportional to the same e_d would be parallel.
QED

Σ itself is NOT proved to hold or to fail. It requires the three corner lines to carry a tight frame of the plane P_r, which constrains the amplitudes of q_1^r.

## 5. Corner coupling of the two purity laws (cross-line, proved)

At a corner cell (r,c) ∈ {1,7} × {2,3}, consider a square s >= 2 whose vector is common-pure (ω e_d, d ∈ U \ {c}) by Theorem U and own-pure (ω q_s^{r'}, r' ∈ O' \ {r}) by Theorem U'. Then q_s^{r'} ∝ e_d. Since q_s^1, q_s^7 ⊥ U, this is possible only for (r',d) = (0,0), or for (r',d) = (6,1) when q_s^6 ∝ e_1.

So, at the four cells {1,7} × {2,3}, the purities forced by the two laws are carried by distinct squares, except for these two coincidences. Each cell has only four squares s >= 2. Hence the number of pure vectors that the two laws place at a single corner cell, counting each coincident vector once, is at most 4.

## 6. Exact unresolved boundary

**Proved:** F1, F2, AX, S, P; Theorems U, U', L; the corner coupling of section 5.

**Not proved (explicit boundary):**
- that the at-most-4 excess vectors of Theorems U and U', together with the forced pure vectors, contradict the remaining frames (rows 2-6 and 7 versus columns 4-7, and own frames of the other columns);
- whether hypothesis Σ is realizable;
- any exclusion of a family of the shape-code schemas.

In particular, no claim is made that flexible lines absorb placements, and no labelled classification is claimed. GB 15/18, the UNKNOWNs, A10/A11 and the n=8 target are unchanged.

## 7. Imports and sources

The imports are [PRIM] LF195-225 for the definitions and [J] for the template rows. The prior candidates and notes, including [ERR], are context only. Every statement used is re-proved here.

- [PRIM] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16/sources/2607.12933v2.raw.txt`, SHA256 `265851e451cc30706b0a4ea1860c5f04568d99be85896c7b049f95c995108df9`.
- [J] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-gb-parent-binding-v1/GBBINDING.json`, SHA256 `d917203deb29a13e212c290e227a001a695765d080a897141d6dc154d79fc673`.
- [ERR] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-joint-completion/B3-JOINT-COMPLETION-CANDIDATE-v1-erratum-1.md`, SHA256 `bafdfd966fb2744c3a0a1fc0772538fef7a3aba8fa5d2cb87e05317362f35c06`.
- [ADD] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-type-elimination/WORKING-NOTES-v1-addendum-1.md`, SHA256 `a4540afc691e9ca842deac5cbd90a13edeabb60ce50422b2b19608457e185983`.
- [TR] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-slot-transitions-sun5-moq-corner-20261019-1735-v1.json`, SHA256 `59e3fb4319f20f578e8d504682343421d82bbc094e33eace85c996b3c261a7ca`.
- [SC] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-az-corner/SCOPE-FREEZE-v1.json`, SHA256 `8c2e75c50d4df3ebc28ac98292c71382939213aff49636b55804fe3950334de6`.
