# qsym-lemma-v1: the fibre count q is symmetric, which allows a coupled refutation rule (a candidate, not in use)

- **Freeze record:** host-clock time and sha256 in `evidence/qsym-lemma-v1.sha256`.
- **Labels:** [NEW] means written in this lane; it is not a novelty claim.
- **Status:** unreviewed. No computation was run. No engine or specification uses this. It removes no class.
- **Scope:** any class. The lemma holds for any family of pairwise disjoint cosets, not only for K7.

## Lemma Q-SYM [NEW]

Let g_vU_v and g_jU_j be disjoint cosets, and let g = gcd(n_v, n_j). Define q_{v→j} by

  μ(U_v·g_v⁻¹g_j·U_j) = q_{v→j}/g.

This is the q of VFC (V1) at v for the neighbour j, before translating to g_v = 1. Then q_{v→j} = q_{j→v}.

*Proof.*
1. At j, VFC uses D_v^{(j)} = U_j·g_j⁻¹g_v·U_v.
2. This set is exactly (U_v·g_v⁻¹g_j·U_j)⁻¹, because (a·x·b)⁻¹ = b⁻¹x⁻¹a⁻¹ and U_v, U_j are subgroups.
3. Inversion is a bijection of G, so the two sets have equal measure. The modulus g is symmetric in v and j.
4. Hence q_{j→v} = q_{v→j}. ∎

**Remark.** Write q_e for the common value on the edge e = {v, j}. It satisfies 1 ≤ q_e ≤ g_e − α_e, by VFC (V1) at either end.

## Corollary CQ: the coupled refutation rule (a candidate rule; not in use) [NEW]

**Definitions.** For a pattern P and a vertex v, let Surv_P(v) be the set of admissible vectors (q_vj)_{j≠v} that are refuted at v neither by:
- an (R) certificate, i.e. a Corollary VFC-count dual for that q, nor by
- a (P) certificate, i.e. an RPLP-k7 dual for that q (rules-k7-addendum-v1 §A1 with erratum W2).

**Claim.** If no symmetric edge labelling q with 1 ≤ q_e ≤ g_e − α_e has (q_vj)_j ∈ Surv_P(v) for every v, then no configuration has pattern P.

*Proof.*
- A configuration with pattern P determines its true values q_{v→j}.
- By Q-SYM they define a symmetric labelling.
- By VFC-count and RPLP-k7, each vertex's true vector is refuted by no valid certificate, so it lies in Surv_P(v).
- The hypothesis says no such labelling exists. Contradiction. ∎

**Relation to the current rules.** The per-vertex rules VFC and RPLP kill P only when Surv_P(v) = ∅ at some single vertex v. Corollary CQ also kills P when every Surv_P(v) is non-empty but no symmetric labelling is compatible with all of them. Every per-vertex kill is a CQ kill, so CQ is never weaker.

**Certificate shape (for a future specification; not frozen as a format here).**
- **Per vertex:** the refuted q-vectors at each vertex, each with its (R) or (P) dual. Equivalently: the surviving sets, plus a dual for every vector in the complement.
- **Global:** a proof that no symmetric labelling meets all the surviving sets, for example an exhaustive search with a recorded node count, replayable by a checker. This global step is a finite combinatorial check. Its correctness has to be replayed independently, like every other certificate.

## Example: the remaining unmarked all-2 pattern

This illustrates CQ; it is not a kill.

**Setting.** Take the K7 pattern with seven unmarked singletons and every α = 2, left open in K7-unmarked-lemmas-v1.

**VFC survivors at a vertex.** At any vertex v, every q_vj ∈ {1, …, 4}. The q-vectors that VFC at v does **not** refute are exactly those whose multiset is one of:

  (4,4,4,2,2,1), (4,4,4,2,2,2), (4,4,4,4,2,1), (4,4,4,4,2,2), (4,4,4,4,4,2).

Derivation:
- Group the neighbours by q. q = 1 forms singletons. The even values {2, 4} form one group, which holds at most 2 elements unless it contains two 4's, and at most one 2 once it has 3 or more elements. The q = 3 group holds at most 3.
- Every other multiset gets LP value ≥ 1. The even group contributes at least (its size)/6 unless it holds at least three 4's together with at least one 2.
- This was computed by hand; it is not machine-checked.

**What that implies.** Every vertex is incident to 3 to 5 edges with q = 4. No edge has q = 3, and each vertex has at most one edge with q = 1.

**A symmetric labelling meeting these VFC constraints exists.** For example, let the q = 2 edges form a 7-cycle, and give every other edge q = 4. Then every vertex has the multiset (4,4,4,4,2,2).

**So VFC coupling alone does not kill all-2.** Whether RPLP-k7 at each vertex refutes the surviving vectors has not been computed. That question needs a computation under a parent GO.
