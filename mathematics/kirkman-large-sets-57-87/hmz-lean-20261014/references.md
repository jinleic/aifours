# References and exact applicability

All new files belong to this scratch repository. Existing target evidence and `math/` were inspected read-only. No OAI module is imported, built or replayed. The local Lean source imports only nine already-cached Mathlib modules, listed at the start of `Formal.lean`.

## Frozen target and input

- `/Users/jinleic/jinleic-workspace/scratch/ai4s-math-hmz-20261014/CONTRACT.md` and this repository's immutable `TASK.md`, `ACCEPTANCE.md`, `verify.py`. The universal quantifier remains every integer t>=1 and v=6t+3. Orders57/87 and conditional certificates are partial scope.
- `/Users/jinleic/jinleic-workspace/ai4s/kirkman-large-sets-57-87/README.md` and `proof.md`: definitions, dated unresolved status, exact scope of previously excluded symmetries. No previous proof of a restricted obstruction is promoted to nonexistence of an unrestricted LKTS.
- Same target's `sources/c19-search-notes.md`, especially sections1-3: actual fixed constituent has one translated19-class starter orbit and nine fixed transversal classes. Its starter satisfies 3u+w=27, u+w+z=19, so z=2u-8 and 4<=u<=9. All six counts are allowed in this joint attempt; earlier fixed-u searches are not repeated.
- `sources/extended-group-analysis.md`, section4: at87 the surviving resolved C29 pattern is27 fixed constituents and two free29-orbits. A fixed constituent needs14 fixed transversal classes plus one29-class orbit. The starter has A+B+C=29 and 3A+B=42, with A>=7; per-layer constraints give A<=12. This reference supplies compatibility conditions, not the missing27 constituents or bases.
- `sources/recursion-notes.md`: source hypotheses and limitations for the product/tripling and finite-field recursions. q=v-2 is55/85, neither a prime power; tripling would need inadmissible KTS orders19/29. No universal recursion is imported or asserted.
- `evidence/c19-paircover-notes.md`: the completed7200-second portfolio remains read-only and is not rerun. Its UNKNOWN outcomes provide no negative mathematical conclusion.
- Frozen packing: target `evidence/c19-17-staged.frozen-packing.json`, SHA256 `6515e4041991d0c857df9c5d5752613f8d958d4ee76296cbbc24c024b807d714`; plain certificate `evidence/c19-partial17.txt`. All17 JSON constituents were expanded and checked through the existing independent interface before retaining zero-based0..15 and releasing16.

## Existing implementation interfaces actually reused

Absolute directory: `/Users/jinleic/jinleic-workspace/ai4s/kirkman-large-sets-57-87/work/`.

- `c19_search.py`: `inventory`, `fixed_model(data, forbidden, aaa_count, cp_model)`, `extract_fixed`, `write_certificate`. The returned replacement row `(orbit_id, shift)` means a starter placement for shifts0..18, or a fixed ABC seed for shift=-1. Its first57 exact-one columns cover starter points; the next84 cover pair orbits. Calling with aaa_count5 generates every ABC starter row; the local returned model's final linear domain is broadened from[5,5] to[4,9]. Original source is unchanged. A positive candidate would be sliced to the original fixed-variable prefix before using `extract_fixed`.
- `c19_verify.py`: `key` enumerates all19 shifts, `shifted`, `verify_inventory`, `check_fixed`. Used to check the actual triple orbits and expanded fixed KTSs independently of the searcher's shortcut canonicalization.
- `c19_staged_completion.py`: `cp_solve`, and conditional positive branch `resolve`. The latter labels classes by the28 blocks through0, allows every disjoint placement of other blocks, and checks the resulting genuine resolution. No symmetry of a free base's chosen resolution is assumed. The previous frozen-complement constructor is not called: this model couples a variable replacement to the free rows from the outset.
- `check_lkts.py`: `parse_certificate`, `check`, and CLI were inspected. It demands55 systems for57,28 exact point partitions per system, each pair once, block-disjointness, and equality with every triple. It is called only in the positive fully resolved branch; no certificate was fabricated for this check.
- `check_partial_packing.py` was inspected for the `PACKING v k` convention and its explicit partial status; it is not confused with the full checker.

Exact source snapshots and hashes of these helpers are in `evidence/joint57/` and its manifest. `audit_joint.py` rechecks every saved variable row and constraint column using the saved independent helper. It performs no solver call and is not an independent human/model review or a kernel proof of the Python implementation.

## Local math reference: exact decomposition discipline

- Challenge `/Users/jinleic/jinleic-workspace/math/lean/ComparatorChallenges/CycleDecomposition.lean`: `OAI.ErdosGallai.CycleOrSingleEdge`, `OAI.ErdosGallai.EdgeDecomposition`, `MainStatement`, `erdos_gallai`.
- `/Users/jinleic/jinleic-workspace/math/lean/ComparatorChallenges/CycleDecomposition.json` names solution module `OAI.Combinatorics.CycleDecomposition.Main` and theorem `OAI.ErdosGallai.erdos_gallai`.
- Actual source `/Users/jinleic/jinleic-workspace/math/lean/OAI/Combinatorics/CycleDecomposition/Decomposition.lean`: `edgeDecomposition_of_indexed` assumes a finite index type, every part is a cycle/single edge, pairwise disjointness, and union equals the graph edge set; it reindexes by Fin. `edgeDecomposition_assemble` assumes finite external indices, injective graph homomorphisms, pairwise disjoint images of their entire edge sets, exact image-edge union, and actual decompositions of all component graphs. It concludes a decomposition with the summed number of parts. This exact-union/disjointness and injective transport discipline is the pattern transferred to actual triples and actual resolutions, including `lkts_fin`.
- Actual terminal source `.../CycleDecomposition/Main.lean`: `main_cost_bound`, followed by `erdos_gallai : MainStatement`, obtains an absolute positive linear decomposition bound for every simple graph on Fin n. No conclusion of that graph theorem proves any triple-system existence statement. Its proof and imports were inspected as source only. The challenge's intentional incomplete proof body was not used.

## Local math reference: finite incidence, with different semantics

- `/Users/jinleic/jinleic-workspace/math/lean/ComparatorChallenges/BalancedRyser.lean`: `OAI.Balanced.PartiteHypergraph`, its `Covers`, `Intersecting`, `Nonisolated`, `HasCoverNumber`, `BalancedCounterexample`, and `MainResult`. Here an edge is a function Fin r -> Fin n, and a cover is a set of vertices meeting each edge; `HasCoverNumber` states an attained size and a lower bound for all covers.
- `BalancedRyser.json` identifies `OAI.Combinatorics.BalancedRyser.Main` and `OAI.Balanced.main_result`. The actual `.../BalancedRyser/Main.lean` is an import assembly. The matching definitions are in `.../BalancedRyser/Model.lean`; the terminal theorem is `.../BalancedRyser/Results.lean`, `main_result : MainResult`, assembled through `mainResult_of_selectedDeletion_corePencil_local_deterministic` from the deterministic, deletion, core-pencil and local ingredients. `MainResult` quantifies sufficiently large prime q and asserts an intersecting nonisolated (q+1)-partite example with cover number q+1.
- This supplies only the representation discipline of explicit finite incidence and quantified coverage. A hitting set for r-partite edges is not exact pair coverage in unordered triples, and says nothing about resolutions. No Balanced Ryser conclusion, underlying asymptotic/probabilistic theorem or field construction is used mathematically in `Formal.lean`. The challenge's incomplete proof template was not copied.

## Public primary sources checked in this run

Both linked arXiv **abstract pages were fetched live** during the initial actor turn using the web tool: `https://arxiv.org/abs/1307.3019` and `https://arxiv.org/abs/2607.21521`. Those observations concern the live abstract pages, not newly downloaded full papers. The dated statement about57/87 remaining unresolved was read in the target README and its research notes. The dossier also preserves `sources/wang-2607.21521.txt` and `sources/status-search-20261014.md`; this actor did not replay that status search or claim a fresh full-text retrieval from those references.

- Chen Wang and Cong Shi, [Large sets of Kirkman triple systems with order q^n+2](https://arxiv.org/abs/1307.3019), submitted2013-07-11. The primary abstract specifies the prime-power q=6t+1 input and an LKTS(q+2); this does not supply either missing target input.
- Chen Wang, [A new recursive construction for large sets of Kirkman triple systems](https://arxiv.org/abs/2607.21521), submitted2026-07-23. The primary abstract gives LKTS(q+2) plus cubic orthomorphism implies LKTS(7q+2), with the stated product-of-prime-powers condition. This run does not invert that construction or claim an exhaustive current literature review. The existing dossier's dated unresolved attestation remains just that, not a formal proof that no later solution exists.

## Lean runtime and trust

Runtime cwd `/Users/jinleic/jinleic-workspace/scratch/rh-quasi-lean-2026-10-07/lean`; `lean-toolchain` is `leanprover/lean4:v4.34.1`. Command:

```sh
/Users/jinleic/.elan/bin/lake env lean /Users/jinleic/jinleic-workspace/scratch/ai4s-math-hmz-20261014/kirkman/Formal.lean
```

No lake update, dependency download, corpus rebuild, OAI import or source replacement was performed. The successful elaborations print the actual statements and transitive axiom lists of every named theorem. Only `propext`, `Classical.choice`, `Quot.sound` occur. No Comparator or nanoda acceptance is claimed. The unavailable `openai-math-lean-verification` skill was searched for in the local skill roots and plugin cache; the frozen task's stronger explicit verification requirements were followed directly.

## Concrete action extension: cached Mathlib sources actually used

No previously confirmed OAI reference or primary-source search was rerun. The new action proofs use these cached Mathlib definitions and lemmas directly:

- `Mathlib/Logic/Equiv/Fin/Basic.lean`: `finProdFinEquiv : Fin m x Fin n ≃ Fin(m*n)`, instantiated at m=3. Its implementation encodes a pair by `coord + n*layer`; `pointEncoding_val` checks agreement with `n*layer+coord`.
- `Mathlib/Data/ZMod/Basic.lean`: `ZMod.finEquiv n` under `[NeZero n]` identifies Fin n with ZMod n; `ZMod.val_add` gives modular addition of coordinate labels; `ZMod.isUnit_iff_coprime (m n)` states `IsUnit(m:ZMod n) iff Nat.Coprime m n` and is applied with m=3. No finite field or primality theorem is needed.
- `Mathlib/Data/ZMod/Defs.lean`: `ZMod.card n` gives the actual finite cardinality n. Together with `Fintype.card_fin`, it discharges17+2*19=55 and27+2*29=85 inside the two concrete corollaries.
- `Mathlib/Algebra/Group/Units/Basic.lean`: `IsUnit.mul_left_cancel` cancels multiplication by3 in ZMod n after the coordinate-sum identity. It needs an actual unit proof, supplied by coprimality.
- `Mathlib/Algebra/BigOperators/Group/Finset/Defs.lean` and `Basic.lean`, imported through `Mathlib/Algebra/BigOperators/Ring/Finset.lean`: additive sum-map, sum-add-distribution and constant-sum lemmas. These transport the sum along the actual finite triple relabeling; triple cardinality3 turns the extra constant sum into3*g.

The three added explicit imports are `Mathlib.Data.ZMod.Basic`, `Mathlib.Logic.Equiv.Fin.Basic`, `Mathlib.Algebra.BigOperators.Ring.Finset`. They use the already cached runtime; no corpus rebuild, download, OAI import or dependency modification occurred. `evidence/action-reference-hashes.json` records the exact cached source contents used for this extension.
