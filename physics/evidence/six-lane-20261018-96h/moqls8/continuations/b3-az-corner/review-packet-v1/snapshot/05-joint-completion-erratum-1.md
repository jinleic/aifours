# Erratum 1 to B3-JOINT-COMPLETION-CANDIDATE-v1 (immutable; mandatory review repair)

Written at 2026-10-19T17:36:18-0700. This erratum applies to candidate `B3-JOINT-COMPLETION-CANDIDATE-v1.md` (SHA256 `b19cfabb4a8fb863aa4e4e118bbe2f97d403cde0d0583b2e0e0250ca76eec3d9`), which itself stays unchanged. It responds to the Codex review [CX] (SHA256 `811ece82ccbe8eff9d70d00b6755e949c8fa688e69f85f8a337754a0b28f709e`): 0 FATAL, 2 MAJOR, 3 MINOR. The parent's transition [TR] (SHA256 `59e3fb4319f20f578e8d504682343421d82bbc094e33eace85c996b3c261a7ca`) makes this repair mandatory. Status after the erratum: CANDIDATE, LABELLED PARTIAL. It is not accepted and is not a premise for any later work.

## E1 (MAJOR 1): tables and Theorem F are necessary conditions, not an exact classification

- **Section 3 / Section 4.** Rename Theorems LC and LR to "exhaustive **mass-case tables of necessary constraints**". The nine (x,y) bins are exhaustive. The printed structures are necessary consequences only. They are not complete support-pattern classifications, and nothing in them is shown to be sufficient.
- **Section 8.** Rename Theorem F to "an exhaustive **product of support-shape schemas**". 9^4 counts tuples of support-shape codes. It does NOT count labelled joint completion patterns. Their realizability and their elimination are both unproved. The following remain unresolved obligations:
  - completion-row incidences, labelled embeddings and relative B/C intersections;
  - masses and phases;
  - the L5/L6 completion-row choices;
  - the L7-L9 incidence and cancellation patterns.

  Delete "the explicit finite list of surviving configurations" from the title and section 1. Read "remaining obligations" as "obligations attached to each schema".
- **Added necessary consequences**, with the proof inline. Put η := <e_6,q_1^3> conj(<e_7,q_1^3>). Since the B part of q_1^3 has support exactly {6,7}, |η|^2 = t(1−t) > 0. Because |q_1^2><q_1^2| + |q_1^3><q_1^3| = P_B,

      D(a) = (1−y_a)P_B + (y_a − x_a)|q_1^3><q_1^3|,  so  D(a)_{67} = (y_a − x_a)η.

  On the other hand, D(a)_{67} = sum_{r ∈ R'} <e_6,b_{r,a}> conj(<e_7,b_{r,a}>). The only nonzero terms are the rows of R_6(a) ∩ R_7(a). Hence:
  - **L7/L8** (x_a != y_a): R_6(a) ∩ R_7(a) != ∅;
  - **L9** (x_a = y_a = 0): |R_6(a) ∩ R_7(a)| != 1, because a single nonzero term cannot vanish;
  - in L2, L3, L5, L6, R_6(a) = R_7(a), as already stated.

  Dually, write p = q_1^2 and q = q_1^3. Because <p,q> = 0,

      <p,E(i)q> = (x'_i − y'_i)<p,e_6><e_6,q>.

  This entry equals sum_{c ∈ {1..5}} <p,b_{i,c}><b_{i,c},q>, whose nonzero terms are the cells of C_2(i) ∩ C_3(i). Hence C_2(i) ∩ C_3(i) != ∅ in **L7'/L8'**, and |C_2(i) ∩ C_3(i)| != 1 in **L9'**. The C-twins hold verbatim, with the mixing factor nonzero because 0 < t_C < 1.
- **Retained normalization relations.** In T8 (J_2 = {a,b}, J_3 = {a,c}), the relations x_a + x_b = 1 = y_a + y_c and x_a = y_a give x_b = y_c. The own-frame and C versions (T8', T8^C, T8^C') are retained the same way, as obligations.

## E2 (MAJOR 2): universal absorption is withdrawn

The sentence in section 8 beginning "Every J-type leaves at least one L9 column ... These flexible lines can absorb every forced pure placement ..." is **withdrawn**. Replace it by:

> Every support type leaves at least one L9 column and one L9' row. These lines admit both pure directions locally. Simultaneous placement and mass matching remain unresolved.

An L9 column still has total B-mass 2, coordinate capacities at most 3 and D = P_B. An L9' row has E = P_B and the analogous capacities. No absorption statement is claimed.

## E3 (MINOR 3): locality of O4

In (O4), replace "forces a second such cell for the same pair, both in its row and in its column" by:

> forces another cell containing the same coordinate pair (β,γ) in its row, and another in its column.

These additional cells need not lie in the joint-completion rectangle {1,6,7} × {1,2,3}, and they need not be completion cells. O3 proves a joint **row**, not a joint cell.

## E4 (MINOR 4): uniqueness in X2

In (X2), replace "A pure-e_6 cell needs the column's e_6-row, and a pure-e_7 cell needs its e_7-row" by:

> a pure-e_d cell lies in a row carrying coordinate d of that column; in case L4 this is the column's unique prescribed row.

In L7, L8 and L9 several rows may carry coordinate 6 or 7.

## E5 (MINOR 5): inline justifications

- **(AX).** For distinct squares s, u and r, d >= 1, apply H1 to the distinct cells (r,0) and (0,d), which share neither row nor column. This gives <q_s^r,Q_s(0,d)><q_u^r,Q_u(0,d)> = 0, with Q_s(0,d) = w_{s,d}e_d. So no two squares have coordinate d in their r-th axis vector. Coordinate 0 is absent because q_s^r ⊥ q_s^0 = w_{s,0}e_0 (same column).
- **A couplings, own frame.** For N_k(r,c) := |<q_1^k,Q_1(r,c)>|^2 the **row** sums 1 − δ_{rk} are integral. Apply Lemma Z to the transpose: a support-graph component has equal total row mass and total column mass, so its column total is integral. The fractional column sums 1 − |<q_1^k,e_c>|^2 occur exactly at c ∈ supp q_1^k. They are columns {1,2,3}, totalling 2, for k ∈ {1,7}, and columns {2,3}, totalling 1, for k = 6.
- **Three-number subset step.** Let u_1, u_6, u_7 ∈ (0,1) with total 2. A singleton is not an integer. A pair has sum 2 − u_r ∈ (1,2), also not an integer. So all three lie in one component. For two numbers in (0,1) summing to 1, neither alone is an integer.
- **(O5), direct proof.** O1 is not invoked for a complementary non-block subspace. Write v_a = Q_1(2,a) = λ_a q + n_a and v_b = λ_b q + n_b, with q = q_1^3 and J_2 = {a,b}. Expand q in the orthonormal row-2 basis. Its coefficients vanish except at v_a, v_b, because P_B v_j = λ_j q and <v_j,q> = conj(λ_j). This gives q = conj(λ_a)v_a + conj(λ_b)v_b. Since |λ_a|^2 + |λ_b|^2 = 1, taking non-B parts gives conj(λ_a)n_a + conj(λ_b)n_b = 0. Both coefficients are nonzero, so the two vectors span exactly span{q, n_a}, and ||n_a||^2 = 1 − |λ_a|^2 = |λ_b|^2. Row 3 and the C rows 4, 5 are identical.

## Scope after erratum

The core mathematics stands as a labelled partial, as confirmed by [CX]:
- R, K, D, E, Sc, P1, P4;
- every printed implication of LC/LR;
- X1-X5 as necessary compatibility statements;
- O1-O5;
- the local C transfer;
- the A couplings.

There is no exact classification, no absorption statement, no type elimination and no B3 no-go. GB 15/18, the UNKNOWNs and the n=8 target are unchanged.

## Sources

- [JC] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-joint-completion/B3-JOINT-COMPLETION-CANDIDATE-v1.md`, SHA256 `b19cfabb4a8fb863aa4e4e118bbe2f97d403cde0d0583b2e0e0250ca76eec3d9`.
- [CX] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-B3-jointcompletion-codex-v1.prompt.stdout.txt`, SHA256 `811ece82ccbe8eff9d70d00b6755e949c8fa688e69f85f8a337754a0b28f709e`.
- [TR] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-slot-transitions-sun5-moq-corner-20261019-1735-v1.json`, SHA256 `59e3fb4319f20f578e8d504682343421d82bbc094e33eace85c996b3c261a7ca`.
