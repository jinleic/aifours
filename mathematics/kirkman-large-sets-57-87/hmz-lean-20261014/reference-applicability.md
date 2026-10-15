# Local math references and applicability

Date: 2026-10-14 PT. These are inspected proof/formalization patterns, not imported or independently replayed openai/math results. The local reference checkout is read-only. The HMZ actor's own `references.md` records what its delivered module actually uses; this note records the owner's independent source inspection.

## Exact decomposition, not a cardinality surrogate

- `math/lean/ComparatorChallenges/CycleDecomposition.lean`, definitions `OAI.ErdosGallai.CycleOrSingleEdge` (lines15–18), `EdgeDecomposition` (lines20–24), and universal `MainStatement` (lines27–29).
- Implementation: `math/lean/OAI/Combinatorics/CycleDecomposition/Decomposition.lean`, `cycleOrSingleEdge_map` (lines33–40), `edgeDecomposition_of_indexed` (lines42–56), and `edgeDecomposition_assemble` (lines69–109).
- The assembly theorem separately requires injective embeddings, pairwise-disjoint image edge sets, complete union equality, and local decompositions. Its proof forms a sigma-indexed family, proves disjointness by splitting equal/different outer indices, proves exact coverage, and only then reindexes by a finite cardinality.
- **Transfer:** the same proof organization is appropriate for a family of fixed KTSs plus group translates of free resolved bases. A cardinality match alone cannot replace disjointness, pair coverage, or resolution. Transporting a parallel class needs a point bijection; transporting the complete triple cover needs genuine orbit uniqueness.
- **Non-transfer:** the graph theorem permits cycles of arbitrary length and singleton edges. It does not decompose a complete3-uniform hypergraph into resolvable Steiner systems, and supplies no target57/87 certificate or universal LKTS recursion. `math/lean/docs/181.md` states precisely the graph scope. No claim is made to have kernel-replayed `OAI.ErdosGallai.erdos_gallai` or its large import closure.

## Explicit finite hypergraph incidence

- `math/lean/OAI/Combinatorics/BalancedRyser/Model.lean`, `OAI.Balanced.PartiteHypergraph`, `Vertex`, `Covers`, `HasCoverNumber` (lines8–28).
- `math/lean/OAI/Combinatorics/BalancedRyser/Hypergraph.lean`, `edgeVertices`, `toHypergraph`, `IsMatching` (lines19–29). It imports `Mathlib.Combinatorics.Hypergraph.Basic` and turns a function selecting one vertex per part into an actual finite vertex set.
- **Transfer:** explicit finite block membership and actual point-disjointness, rather than uninterpreted Boolean predicates, make a certificate's semantics auditable. KTS parallel classes are perfect matchings, not merely arbitrary edge covers.
- **Non-transfer:** an r-partite edge has exactly one point per part; an LKTS on three layers necessarily also contains AAA and AAB triples. The Ryser covering-number results do not imply exact pair coverage, resolution, or an LKTS. `math/lean/docs/162.md` gives their different quantifiers. No Ryser theorem is imported or claimed verified here.

## Certificate-to-semantics discipline

- `math/lean/OAI/Combinatorics/SnakyCertificate/Main.lean`, `OAI.SnakyCertificate.Check.rowAt_eq_cached` (lines11–14), `Check.all_rows` (lines40–44), and `OAI.SnakyCertificate.certificate_correct` (lines50–58).
- `math/lean/OAI/Combinatorics/SnakyCertificate/Reconstruction.lean`, `cache_equations_range_0` (lines22–40) illustrates finite checked equations assembled into the invariant rather than accepting a host-language success flag as a proof.
- **Transfer:** a hypothetical LKTS certificate must be connected through a proved soundness theorem to faithful STS/resolution/large-set definitions; the numeric checker output alone is not a Lean proof. The broken-certificate control must fail at that semantic boundary.
- **Non-transfer:** this particular table concerns a different combinatorial object and contains no Kirkman construction. Its616-row certificate and theorem were only inspected, not compiled or imported.

The delivered Lean imports and observed axioms are authoritative in `claims.json` and the acceptance logs. The source references above are conceptual dependencies only unless the actor explicitly records otherwise. No Comparator or nanoda acceptance is asserted.
