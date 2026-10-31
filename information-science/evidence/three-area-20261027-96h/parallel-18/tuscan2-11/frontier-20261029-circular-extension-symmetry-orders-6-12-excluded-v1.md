# The circular extension of a T2(11) has automorphism group 1, Z₂, Z₃ or Z₄

Owner **InfoRecursiveMDS18-2**, info-4. Native clock before the run: **Thu Oct 29 08:36:52 PDT 2026**; after the run: **08:37:11 PDT**.

**NEW author candidate, unreviewed.** It combines WRITTEN arguments with an **exhaustive exact search** in the owner's harness: plain Python, no SAT or DRAT. The search took 20 s on one thread. It continues `frontier-20261029-circular-extension-free-automorphisms-v1.md` (SHA `6fd41a2a7dc09d0dbbb2daaa42b0a5034b4bce5e668cbc52636f3afdb877ae7e`).

The key lemma is T1(p) asymmetry: every T1(p) for odd prime p has trivial symbol-automorphism group. It is adopted at same-harness scope as Theorem A of the parent disposition `dispositions/info-4-tuscan-odd-prime-symbol-asymmetry-and-orbit-counts-parent-v1.md` (SHA `20b187f303624afe0423fb4042b34a028f4cbdd3cc5577759bb709765e42d5eb`). No formal, independent-model or novelty claim is made.

## 1. Statement

Let A be any T2(11). Let D be its circular extension: eleven directed Hamiltonian cycles of K₁₂*, obtained by joining every row through a new point ∞. Let H = Aut(D). Then H is trivial or isomorphic to Z₂, Z₃ or Z₄, and acts freely on the 12 points. Every other option is excluded:

| H | reason |
|---|---|
| any group with a fixed point | previous packet, Theorem A: such an automorphism would be a symbol automorphism of a T1(11) cut, impossible by the adopted asymmetry lemma |
| Z₂×Z₂ | §2 (written parity) |
| Z₆, S₃ (order 6) | §3: D would be 2-perfect and Z₆/S₃-invariant; exhaustive search finds none |
| Z₁₂, Z₆×Z₂, D₁₂, Dic₃, A₄ (order 12) | §3: same search, all five regular actions exhausted. This also independently confirms the written exclusion in the review-corrected circular-regular packet. |

Groups whose order does not divide 12 are already excluded because the action is free.

## 2. Z₂×Z₂ (written)

H permutes the eleven cycles. The stabilizer of a cycle acts freely on its twelve vertices by rotations, so it is cyclic. Z₂×Z₂ is not cyclic, so every cycle orbit has size 2 or 4. Their sizes would then sum to an even number, but the total is 11. ∎

## 3. Orders 6 and 12: exact cover

By the previous packet (Theorem B, item 3), |H| ≥ 5 forces D to be **2-perfect**: every ordered pair of distinct points occurs exactly once at cyclic distance 1 and exactly once at cyclic distance 2. Conversely, a 2-perfect D cut at any point gives a T2(11). So these cases ask whether a 2-perfect decomposition of K₁₂* exists that is invariant under a free action of a given group G of order 6 or 12.

**Model (written, both directions).** A free action of G on 12 points is isomorphic to left multiplication on V = G × {0, …, 12/|G|−1}.

- **Types.** The *type* of a pair ((g₁,a),(g₂,b)) is (a, b, g₁⁻¹g₂). Each type is one G-orbit of |G| pairs. There are 22 types for |G| = 6 and 11 types for |G| = 12.
- **Cycle orbits.** Each cycle has a cyclic stabilizer ⟨k⟩ of some order s. The generator k acts as rotation by L = 12/s, so the cycle has the form x₀…x_{L−1}, x_{j+L} = k·x_j, where x₀, …, x_{L−1} is a transversal of the ⟨k⟩-orbits. The G-orbit of this cycle covers exactly the types of its first L arcs and the types of its first L distance-2 pairs, each completely.
- **Equivalence.** G-invariant 2-perfect decompositions correspond exactly to collections of such base cycles whose arc types partition all types and whose distance-2 types partition all types.
- **Free cycles.** A cycle with trivial stabilizer covers 12 types, so at most one is possible for |G| = 6 and none for |G| = 12.

**Search** (script `frontier-20261029-free-action-exact-cover-v1.py`, SHA `a194164d28f86bbaaba23db774087ac64a48833a4b14f69cbc1f1ac01b329e3d`; receipt `frontier-20261029-free-action-exact-cover-run-01.json`, SHA `9ce3e4b711eb363041cfbb0c3b79645891e1504a9dfb62d10de0ced5676000a3`):

- **Stabilized base cycles.** All of them are enumerated, giving 336 signatures for Z₆ and 1,062 for S₃. A self-check rebuilds each signature's full cycle orbit and confirms its arc and distance-2 type accounting: 336/336 and 1,062/1,062, 0 failures.
- **Free base cycles.** They are enumerated depth-first from the normalized start (e,0), which is reached by rotating the cycle and then translating. After each free cycle, the residual types are tested by exact cover.
- **Results.** Z₆: **exhausted**, with 2,799,414 nodes and 36,432 complete free cycles, none extendable. S₃: **exhausted**, with 2,703,810 nodes and 36,504 complete free cycles, none extendable. All five groups of order 12: **exhausted**; no stabilized-cycle cover exists and free cycles are impossible.
- **Controls.**

| control | expected | observed |
|---|---|---|
| Z₅ regular on 5 points (polygonal, 2-perfect) | found | found; witness rebuilt with D1 and D2 exact |
| Z₇ regular on 7 points (polygonal, 2-perfect) | found | found; witness rebuilt with D1 and D2 exact |
| Z₃ free on 9 points (Hamiltonian decomposition only) | found | found; two free cycle orbits; D1 exact |
| Z₅ free on 10 points (Hamiltonian decomposition only) | none | exhausted |
| Z₈ regular (Hamiltonian decomposition only) | none | exhausted |
| D₈ regular (Hamiltonian decomposition only) | none | exhausted |

The three negative controls have written reasons:

- Z₅ on 10 points: the 8 within-orbit arc types need a free cycle with 8 within-orbit arcs. That cycle contains a Hamiltonian path in Z₅ whose 4 differences would be all of Z₅∖{0}, with sum 0, contradicting telescoping.
- Z₈ regular: the even types {2, 4, 6} need a stabilized cycle with L = 4 whose four types sum to 4 (mod 8), but those types would have odd sum.
- D₈ regular: every L is even, but 7 types must be covered.

## 4. Consequence and exact remaining gap

Combined with the previous packet, every T2(11) satisfies:

- its rows have no symbol symmetry;
- its 12-point circular extension has automorphism group 1, Z₂, Z₃ or Z₄;
- that group acts freely;
- every distance-2 coincidence of D contains the whole orbit of ∞, of size |H| ∈ {1, 2, 3, 4}.

In the Z₄ case, every coincidence has vertex set exactly that orbit, so both ends and both middles lie in the 4-point orbit of ∞.

**Open:** the classes H ∈ {Z₂, Z₃, Z₄}, where D need not be 2-perfect, and the asymmetric case H = 1, which is the general problem. Plain Python cannot search these exhaustively: they allow up to 5, 3 and 2 free cycle orbits respectively. They would need a frozen request and authorization. No witness and no unrestricted no-go: **T2(11) remains OPEN.**
