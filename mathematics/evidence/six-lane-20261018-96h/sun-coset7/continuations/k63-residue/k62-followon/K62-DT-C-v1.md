# K62-DT-C-v1: Part C — the edge-class budget in the generic sub-case G [CANDIDATE]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T06:34:08-0700.
- **Author:** Sun63Successor; single author, unreviewed, written only (HOLD in force; nothing run).
- **Labels.** C1 uses only accepted K62-E3 (Lemma 2, C2 sub-claim (a), C2 in both orientations, valid in G because
  (alpha_(d i*), alpha*_(d i*)) = (1, 1)). C2 uses (R4) of `K62-DT-B-v1.md` (sha256
  51960d44d60fa50901a3201143410f935750852d1ccd4c6e116f81a9c601604f; 5/6 bound of `K62-CAP-v1.md`, candidate). C3 is
  **CONDITIONAL ON DG** (through B5).

## C1. Budget lemma (G)
The ten O-pairs carry joint values (alpha, alpha*) in J_O (K62-E3 Lemma 2, C2 sub-claim (a)). Write
A, B, C, D, E, F, G, H for the numbers of pairs with joint value (4,1), (4,2), (1,4), (2,4), (1,1), (1,2), (2,1), (2,2).
**Then 2A + 2C + 5E + 3F + 3G + H <= 6.**
*Proof.* K62-E3 C2 for alpha* (orientation alpha_(d i*) = 1) and for alpha (alpha*_(d i*) = 1): n_4(alpha) >= 2 n_1(alpha) + 2 and
n_4(alpha*) >= 2 n_1(alpha*) + 2, i.e. A + B >= 2(C + E + F) + 2 and C + D >= 2(A + E + G) + 2. Adding:
B + D >= A + C + 4E + 2F + 2G + 4; insert B + D = 10 - (A + C + E + F + G + H). QED
Consequences: E <= 1; if E = 1 then A = C = F = G = 0 and H <= 1; F + G <= 2.

## C2. Minimum degree (G)
Every v in O has degree >= 1 in H_alpha and in H_alpha* (graphs of the pairs with alpha = 4, resp. alpha* = 4).
*Proof.* Otherwise all four O-entries of that row lie in {1, 2}: (R4) of Part B. QED
With B1 (degree <= 3): A + B <= 7, C + D <= 7, A + B >= 3, C + D >= 3.

## C3. With B5 (CONDITIONAL ON DG)
Some family has a non-tight 4-pair, so **A + C >= 1**, and C1 leaves exactly:
- A + C = 1: E = 0, F + G <= 1, H <= 4 - 3(F + G);
- A + C = 2: E = F = G = 0, H <= 2;
- A + C = 3: E = F = G = H = 0 (so B + D = 7).
In every case at least 6 of the 10 O-pairs are tight 4-pairs ((4,2) or (2,4)), entries 1 occur on at most three
O-pairs, and (E = 0) no O-pair has alpha = alpha* = 1.

## C4. Status
These are necessary conditions inside G only. The residual G-patterns of Part B section 4 now also satisfy C1-C3.
Not yet derived: a contradiction for them (candidates for the next step: the i*-rows, where B2 and (R3) force even
entries at every vertex of 4-degree 1 or 3, together with K62-SH and the 11/12 bound when f* = 1; and the exact weights
of Theorem DG for the forced deep triples). Marked sub-cases and the (1,3) orientation are untreated. Full K6.2*
(e_d >= 4) and full Sun(7) remain OPEN.
