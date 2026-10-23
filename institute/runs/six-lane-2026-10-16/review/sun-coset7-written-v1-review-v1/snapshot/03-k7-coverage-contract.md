# FINITE-COVERAGE-k7-v1: proposed finite-coverage contract and bounded-experiment request

- **Freeze record:** host-clock time and sha256 in `evidence/freeze-v1.sha256`.
- **Status:** a proposal for the parent. **No enumeration has been run.** Nothing below starts before an explicit parent GO naming the stage(s).
- **Inputs:** `README.md` (reduction R1(7), remaining classes §5) and `rules-k7-v1.md` (rules, VFC, Lemma CAP).

## 1. What must be covered

After the written reduction, a Sun(7) counterexample (CE) lies in one of six classes (README §5): **K7, K6.2\*, K6.3, K5.2\*, K5.3, KII**. A complete proof must exclude every pattern of every class; anything left is reported as PARTIAL with the exact class (and exact surviving patterns, where enumerated).

**Universe of a class.** A pattern is (π, α):
- π assigns each vertex its role (C, D, i*, x, y as the class defines) and its capped profile (min(e,4), min(f,2), min(g,2)), subject to the class constraints listed in rules-k7-v1 §4 ("Admissible profiles by class"); the pairwise gcds computed from π must equal the class's gcd matrix;
- α assigns each pair an integer in [1, g_ij − 1] (L0.3).

By Lemma CAP every rule is a predicate on (π, α), and every CE of the class has a pattern in this finite universe. Profiles are enumerated exhaustively (redundant over-approximations, e.g. e = 3 and e = 4 when they behave identically, are allowed: they only duplicate work).

**Symmetry.** Patterns are identified under permutations of V that preserve roles and profiles (stabiliser of π). Only that group may be used for orbit reduction; roles and markers are never exchanged.

## 2. Proposed rule set (frozen in rules-k7-v1; no new rule before a new frozen version)

Applied as pruning on partial assignments, and on complete leaves:
1. **T** (L1) on every completed triangle.
2. **VFC-LP** (Corollary VFC-count) at a vertex v over the set N′ of neighbours whose edges to v are already assigned. Sound on partial assignments because the subfamily {v} ∪ N′ is itself pairwise disjoint (deletion), so VFC applies to it. Kill iff for **every** admissible q ∈ ∏_{j∈N′}[1, g_vj − α_vj] there is an exact rational y ≥ 0 with Σ_{j∈T} y_j ≤ 1 on every allowed T ⊆ N′ (all subsets checked, hereditary definition) and Σ_j y_j q_j/g_vj ≥ 1.
3. **K** (L2/L3 with K1) on a vertex and a set S whose triangles with v are all completed.
4. **P** (L4) on complete leaves (PB / Ppair).
5. **RPLP** (sun-coset6 rules-k6-v3 L12, transcribed to general γ and g by rules-k7-v1 §1) on complete leaves, with exact dual or Farkas vectors for every admissible q.
6. **FH** (L5 with L6 as the subgroup source) only when [G:W] = m ≤ 5 and every admissible m for that edge is refuted; m = 6 fibres are not attempted in v1 (cost). Omitting a rule is sound: it can only leave more survivors.

Every kill is recorded with a witness checkable from (π, α) alone; simplex output is never evidence (exact duals only).

## 3. Certificate format (to be frozen as CERT-FORMAT-k7-v1 together with the engine, before any counted run)

- **Tree coverage.** For each class and each profile assignment π (listed exhaustively), the α-assignment tree uses a fixed edge order. A node is either expanded into all g_ij − 1 children, or closed by a node certificate (prefix, rule, witness). A checker re-walks the tree: at each node it either verifies the stored witness on the prefix or expands every child. Leaves that are never closed are SURVIVE and are listed exactly.
- **Witness content** (all exact rationals as strings): T: triangle; VFC-LP: vertex, neighbour set, one dual y per admissible q (keyed by q); K: vertex and S; P: as in sun-coset6 CERT-FORMAT-k6-v3; RPLP: one 30-entry-style dual (a, b, u, l) per q, sized to |N|; FH: edge, every admissible m, and refutation counts per m (informational) — the checker re-runs the exhaustive fibre search.
- **Fail-closed clauses** of sun-coset6 CERT-FORMAT-k6-v3 §6 carry over (well-formedness, duplicate keys rejected, exact orbit/tree coverage, recomputed keys).

## 4. Staged bounded-experiment request (each stage needs its own GO)

Sizes are raw α-label counts before pruning; leaf counts after pruning are **[INFERENCE]** only.

| stage | scope | raw α-labels per profile | proposed cap |
|---|---|---|---|
| **A** | Certify the 5-vertex family X1 = (3r_1, 3r_2, 6r_3, 6r_4, 6r_5), r_1, r_2 odd, r's pairwise coprime (Menon Thm 4.2's family; kills K5.3 via README §5) — as a 5-vertex universe with all admissible profiles. Controls: the Prop 4.5 family (2r_1,4r_2,4r_3,4r_4) and the k5 Core(5) universe must be fully killed; realisable families (Menon's A5 (6,6,6,10,15), C2×S4 (4,6,6,6,6), (6,6,6,6,16), cosets of one subgroup) must survive. | X1: 2^7·5^3 = 16,000 | 5 min CPU, 1 process |
| **B** | Classes K5.2\* and KII (7 vertices, \|C\| = 5). | K5.2\*: ≈ 5^10·3^3 ≈ 2.6e8; KII: ≈ 5^10·4·2^5·3 ≈ 3.8e9 | 45 min CPU, 1 process, < 1 GiB |
| **C** | Classes K6.2\* and K6.3 (\|C\| = 6). | K6.2\*: ≈ 5^15·3 ≈ 9e10; K6.3: ≈ 5^15·2^6 ≈ 2e12 | 60 min CPU, only if B finished; may stop with exact frontier |
| **D** | K7 (all 21 pairs gcd 6). | 5^21 ≈ 4.8e14 | **not requested** in this window: needs a new representation (e.g. the α = 1 equivalence/blow-up structure, see §5) and probably native code |

Resource rules for every stage: ≤ 2 processes (planned: 1), < 1 GiB RSS, TMPDIR inside the lane, outputs ≤ 16 MiB total, fresh disk check (free ≥ 12.2e9 B plus projected growth) immediately before launch, owned SIGTERM plus bounded wait as the only stop, no SIGKILL, no tool/subprocess timeouts, no CPU ulimit. A stage that hits its cap is stopped by SIGTERM and reported UNKNOWN with its exact frontier.

## 5. What the outcome can and cannot mean

- **Stage A** success removes K5.3 (lane-certified; independent replay still required).
- **Stage B / C** success removes the named classes, conditional on independent replay by a separately written checker (the parent commissions it) and hostile reviews of rules-k7-v1.
- **K7** remains the exact missing class in this window unless a written argument closes it. Written leads (not yet proved, not frozen as rules): with no markers, the T and K rules allow only the triangle types (1,1,1), (1,2,2), (1,3,3), (1,4,4), (2,2,2), (2,2,4), (2,3,3), (2,4,4), (3,3,3), (4,4,4), (5,5,5); then α = 1 is an equivalence relation with α constant between classes, α = 5 forces α ≡ 5 (which VFC kills), and 3's and 4's cannot coexist. Markers (one vertex each for e ≥ 2, f ≥ 2, g ≥ 1) relax these locally.
- **PARTIAL definition for this transition:** the frozen reduction (README), the frozen rules, the list of classes removed with the lemma or certificate responsible, and the exact remaining classes (with exact surviving patterns where a stage completed). Never a restriction to integers, normal, abelian or solvable subgroups, bounded order, or special index tuples.
