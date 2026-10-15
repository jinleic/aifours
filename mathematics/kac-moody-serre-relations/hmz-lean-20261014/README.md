# Actual HMZ, partial Lean formalization, and structural family progress

Date: 2026-10-14 (America/Los_Angeles).

**Full original goal solved: no. HMZ/RLAR accepted: no.** The goal remains J=tau for every generalized Cartan matrix in characteristic zero with its full Cartan realization. No exact characteristic-zero counterexample was found.

## Terminal workflow evidence

| Item | Observed result |
|---|---|
| Frozen baseline | `8928b66f44ce3a2def1657d316250f29727a38d1` |
| Runtime revision | `3d3e21b0da89ef5f6247cd7b3f88ad178fbac94a` |
| Official flowverse revision | `2c37d06df3e356807adb93b5a9fdca170a5d0be8` |
| Actor / reviewer | codex `gpt-6.1-sol:max` / claude `claude-opus-5-5:max`, from the unchanged shared pairing |
| Configured / observed wall duration | 3600 / 3600.54881854204 seconds |
| Process result / terminal journal | 143 / `ended how:stopped` |
| Completed reviewer verdict | Round 1: `done:false`; universal theorem unresolved |
| Latest reviewer attempt | Interrupted before a second verdict |
| Frozen TASK and checker hashes | Both unchanged |
| Final process snapshot | Zero exact scratch-repository-path matches; not a global process absence claim |

Evidence is preserved in [`hmz-evidence/process.json`](hmz-evidence/process.json), [`terminal-summary.json`](hmz-evidence/terminal-summary.json), the copied epic/resume journals, wrapper output, and the actual [`reviewer-round1.txt`](hmz-evidence/reviewer-round1.txt). The full original scratch repository remains at `/Users/jinleic/jinleic-workspace/scratch/ai4s-math-hmz-20261014/kac-moody`, including incremental failures and development logs. The flow used the authorized full-access permission mode, not an OS sandbox. There was no competing reviewer CLI or nested HMZ.

The first reviewer independently recompiled both Lean files, accepted their stated partial scopes, and checked the coefficient-three argument and the level-four invariant line. It correctly did not accept the universal goal. The actor then completed the four remaining level-four primitive cells, but the next reviewer was cut off. **The final four-cell continuation has exact checker evidence, not a completed final HMZ reviewer verdict.**

## What was achieved

1. **Eight actual Lie-algebra Lean roots**, in [`Formal.lean`](Formal.lean), with full names, assumptions, statements and axiom lists in [`claims.json`](claims.json). They formalize raising weights, the minus-sign lowering recurrence, the leading-index Serre-string consequence, the nonpositive integral primitive-weight argument, Cartan/raising propagation of recursive kernels, generator stability, and equality of generator closure with an actual generated Lie ideal. These are existing structural arguments formalized in Lean, not J=tau assumed as a field or a finite-dimensional relabeling.
2. **A(r,s), r,s>=1, equality throughout alpha_3<=3**, where A(r,s)=[[2,-1,-1],[-1,2,-1],[-r,-s,2]]. The written proof uses finite-Levi semisimplicity, no trivial constituent in L3(ad sl3), and the previously accepted uniform height-seven theorem. Both HMZ and the enclosing worker obtained the same structural reduction independently.
3. **A(r,s), r,s>=4, equality throughout alpha_3<=4.** Exact original-row lowering certificates detect the unique invariant line and the four remaining primitive multiplicity spaces. This is a written theorem with computational finite premises, not a Lean formalization or an all-level result.
4. **Generic fixed-level full rank in the regime r,s>=k.** Symmetrizable diagonal specialization proves the ideal of maximal minors is nonzero and misses the allowed integer diagonal. A proper algebraic failure locus need not be empty off the diagonal; this does not prove universal injectivity.

The actor's mathematical arguments, reference audit and recorded commands are in [`STRUCTURAL.md`](STRUCTURAL.md), [`REPORT.md`](REPORT.md) and [`REFERENCES.md`](REFERENCES.md). No novelty claim is made. The existing 45/89 general height-eight gaps and A_one's next candidate (4,4,6) remain unchanged. Height thirteen was not rerun.

## Exercised verification and trust boundary

- Frozen `python3 verify.py`: `Formal.lean` exited 0; `NegativeControl.lean` exited 1 at its deliberately false final theorem. Exact commands, hashes and timings are in [`verification.json`](verification.json).
- All eight positive roots printed only subsets of `propext`, `Classical.choice`, `Quot.sound`. The negative control constructs an actual rational sl2 matrix module, proves the necessary hypotheses and disproves the changed sign before the invalid proof application is rejected. The final error is a type mismatch, not a missing import.
- The actor's separately implemented word-deletion and primitive-space checkers passed, with source hashes and coefficient/coverage rejection controls: [`level4-independent-check.json`](level4-independent-check.json), [`level4-cells-independent-check.json`](level4-cells-independent-check.json).
- The enclosing worker's independent tensor checker passed: dimension 168, weight-zero dimension 18, joint rank 18, exact minor 288, altered-coefficient/missing-vector rejection, and rank 13 when either lowering is omitted. See [`levi-independent-check.json`](levi-independent-check.json) and [`degree3-certificate-notes.md`](degree3-certificate-notes.md). Its explicit degree-four Levi primitive is a rejection control for an invalid all-level mechanism, not a Serre counterexample.
- No Comparator, nanoda, full Lean proof of the family band, full realization construction, or universal Serre theorem was checked. The parent's independent replay is separate from these delivered observations.

## Reproduction without overwriting receipts

From this directory:

    python3 reproduce.py --output /ABS/NEW/REPLAY-DIRECTORY

This copies the relevant sources/certificates to a new directory, uses the shared cached Lean runtime read-only, runs the frozen Lean checker, the finite character and independent level-four checks, and the independent degree-three checker serially. It preserves all original receipts. The reproduction wrapper itself has not been executed by the enclosing worker; the constituent exercised commands and outputs are documented above. The parent should run it for an independent snapshot replay.

The direct Lean command is `/Users/jinleic/.elan/bin/lake env lean /ABS/PATH/Formal.lean`, with cwd `/Users/jinleic/jinleic-workspace/scratch/rh-quasi-lean-2026-10-07/lean`; the toolchain is Lean 4.34.1. Its 23 patched-dependency warnings are expected. No cache rebuild or dependency update is required.

## Reference and integration provenance

The audited local math corpus supplied genuine free-Lie, quotient/ideal, bracket-induction and exact-sequence patterns. No OAI theorem was imported or assumed to solve Gabber-Kac. Exact symbol applicability and direct Mathlib dependencies are in `REFERENCES.md` and `source-evidence.json`.

Additional enclosing-worker audit: cached `Mathlib/Algebra/Lie/SerreConstruction.lean`, SHA-256 `1b0b87261bcbf88de9eb18b1a44b7b59707fcae120e3222fba4721f0c50defc2`, defines `Matrix.ToLieAlgebra` using exactly the indexed H_i,E_i,F_i generators. It does not add the full extra Cartan directions for singular matrices or define the maximal Cartan-disjoint ideal tau. Its actual Lie quotient API is relevant, but the definition alone would not match the full book target. It is not imported by the delivered proof.

Actor artifacts were copied byte-for-byte; [`integration-copy-manifest.json`](hmz-evidence/integration-copy-manifest.json) binds those copies. The actor's source ledger hashes the pre-integration dossier. Its original README/proof bytes are preserved in `hmz-evidence/input-README.md` and `input-proof.md`; the enclosing worker then intentionally updated the live target README/proof. The actor's reports remain historical snapshots of its own run, not assertions that the live dossier stayed unmodified during later integration.

## Remaining mathematical obstruction

Prove injectivity of the **actual omitted lowering** on every surviving Levi-lowest multiplicity space at every level, including higher Serre summands and repeated/trivial Levi constituents. For the universal quantifier, also handle GCMs without a symmetrizable single-node complement. None of the formal propagation lemmas, fixed-level finite certificates, or generic-rank statement supplies that missing theorem.
