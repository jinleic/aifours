VERDICT: ACCEPT-WITH-FIXES

**K4:** ACCEPT for the necessary vector→CNF bridge, conditional on the accepted K1–K3 results. The supplied snapshot does not declare a K4 cube cover.

**K5:** ACCEPT for the necessary vector→CNF bridge and the abstract cube/refinement partition. Certification and coverage bookkeeping require the fixes below.

All **14/14 pinned files** match their SHA-256 and byte counts. The soundness note matches `eda1860e82b983d1a8b414bdc201c86131ad3ea87b955d41823a6430619577da`.

No FATAL mathematical or clause-strengthening defect was found.

1. **MAJOR — Root-cube certification does not implement its stated strict verdict.**  
   [code/k5_split_r2.py:117](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-k4k5-parent-inputs-v1/code/k5_split_r2.py:117) sets `verified` from checker text alone after the earlier UNSAT-text/cap guard. It never requires solver exit 20, despite [README.md:196](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-k4k5-parent-inputs-v1/README.md:196), and ignores the recorded checker exit and compression/decompression exits.

   **Counterexample to the promised predicate:** UNSAT solver text, no cap trip, solver exit 0, checker exit 1, checker line `s VERIFIED` yields `verified=True`. I confirmed this using the pinned expression in memory; no subprocess was run.

   **Fix:** record and require solver exit 20, checker exit 0, the expected status lines, successful proof compression/decompression, and successful complete CNF feeds. Reject any `NOT VERIFIED` text. All failed conditions must produce UNKNOWN. This finding concerns certification policy; it is not a demonstrated false UNSAT of a SAT instance.

2. **MAJOR — Global coverage and resume provenance need an explicit ledger check.**  
   [code/k5_resplit.py:170](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-k4k5-parent-inputs-v1/code/k5_resplit.py:170) accepts an arbitrary parent list. It does not establish that this list is the complete UNKNOWN frontier, validate unique parent IDs and ancestry, or bind their literals to earlier receipts. At [code/k5_resplit.py:188](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-k4k5-parent-inputs-v1/code/k5_resplit.py:188), resume skips solely by ID; root resume has the analogous issue at [code/k5_split_r2.py:128](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-k4k5-parent-inputs-v1/code/k5_split_r2.py:128).

   **Explicit gaps:** if all 128 roots are UNKNOWN but the supplied list omits `c042`, construction emits only 127 child families without detecting the omission. A stale receipt with the same leaf ID but different base/literals also causes the current task to be skipped. Both bookkeeping examples were reproduced in memory.

   **Fix:** validate a pinned frontier ledger, retaining every certified, UNKNOWN and unstarted terminal leaf. Bind resume decisions to base SHA, ID, depth, complete literals and ancestry; reject mismatches and duplicate IDs. The parent may discharge this obligation independently, but these worker scripts alone do not establish whole-base coverage.

3. **MINOR — The opening K4 cube claim exceeds this snapshot.**  
   [review/K4K5_ENCODING_SOUNDNESS.r2.md:6](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-k4k5-parent-inputs-v1/review/K4K5_ENCODING_SOUNDNESS.r2.md:6) includes K4 in the “exactly one cube/leaf” claim. Line 65 calls K4 splitting intended and references README §9, which is absent.

   **Fix:** restrict the present K4 claim to CNF necessity, or supply its pinned base, declared variables, cube construction and ledger.

The mathematical reduction passes with the required quantifiers. The primary source permits arbitrary complex vectors, independent per-square unitaries, entry phases, and common row/column permutations. Classicality is equivalent to exactly eight rays per square. Independent standardization preserves inner products and pairwise tensor-product ONBs. Regridding need not be an isotopy: its required ONBs, tensor-product bases and ray counts are preserved.

Lemma 10 preserves existing orthogonality within the changed square, hence orthogonality to every other square simultaneously. In standard form, classical squares already have weight-one entries and remain unchanged; untouched non-classical squares retain their ray counts.

Consequently, **F3 holds for every genuine set**, including unreduced sets. If a set has \(r\in\{1,2,3\}\) non-classical squares, its reduction has \(m\le r\); A8 excludes \(m=0\), and accepted K1–K3 exclude the remaining possibilities. For K4, a square lacking weight 3 in any row or column frame could therefore be replaced alone, leaving exactly three non-classical squares—contradicting F3. This proves K4 all-frame P4 without minimality.

K5 P4 is correctly **row-0 only**, justified by the definition of the reduced class K5. It does not assert that every unreduced set with five non-classical members satisfies fivefold row-0 P4: a reduction leaving four survivors belongs to the K4 branch.

The canonical assignment extends through every audited clause family:

- **Constants/G2:** diagonal Gram entries are true; distinct common-row/common-column entries are false. All ten square pairs enforce the necessary tensor-product orthogonality condition, including square 5 in K4.
- **G3:** transitions between row/column ONBs are unitary, including intersecting frames. Nonempty support and the forbidden singleton intersections are necessary in both orientations.
- **G4:** zero Parseval terms force zero overlap; exactly one nonzero term forces nonzero overlap. Multiple terms may cancel; the code does not forbid that cancellation.
- **G5:** singleton frame support implies projective equality, hence identical overlap patterns with every other cell. The trigger clauses encode the stated equivalence.
- **P4/weight1:** every six-of-eight overlap clause implements `w3 ⇒ weight ≥ 3`; flags may take their actual defining values. K4 weight1 is at-most-one, with nonemptiness supplied by G3.
- **Auxiliaries:** `b3`/`c4` cache keys determine their operands; frame identifiers distinguish the row/column frames; variable namespaces are separate. No conflicting reuse was found.

SB2 is lossless. At the chosen weight-three cell, five disjoint nonempty supports avoid the column coordinate; \(3+1+1+1+1=7\), so they partition all seven allowed coordinates. Interpreting column permutation as old \(j\mapsto\sigma(j)\), applying the same basis permutation preserves row-0 standard form.

After SB2, common permutations of rows 2–7 provide K5 ROWLEX or the K4 classical-column sort while preserving the fixed cells and relevant P4 conditions. Auxiliary values are assigned from the resulting vectors. This argument requires no syntactic symmetry of the lex auxiliaries.

For K5, all eight declared variable lists match primary-variable allocation. All 128 root assignments form a disjoint partition; replacing a leaf by all 128 extensions preserves that partition inductively. Both runners preserve the base clause bytes and append one unit per literal, with header count \(C+|\mathrm{lits}|\), including repeated or contradictory literals. `k5_resplit.py` has the stated strict verdict conjunction; native UNKNOWN exits and RSS guard trips do not qualify as verified.

Controls actually run were read-only, in-memory Python checks:

- Both encoders: AND gates/constants, 6,220 G3 projection cases each, exhaustive lex projections through four bits, and P4/G4/G5 truth tables; K4 weight1 checked over all 256 support patterns.
- Primary-variable numbering only; 128 roots and 16,384 depth-two children with unique fixture IDs; unit/header construction in both runners.
- Symbolic examination of 53,760 `b3` and 197,120 `c4` calls without conflicting cache meanings.
- An exact complex QLS(4), with Gaussian-integer coordinates divided by five: zero G1–G5 violations, 528 Parseval identities, and 88 orthogonality edges preserved by a Lemma-10 replacement.

Peak measured RSS was below 60 MB. No production solver, checker, producer `main()`, or full CNF generator was run. No files were written; no network or delegation was used.

The upstream exclusions and their classification/certificate obligations remain conditional imports from `parent-accepted/`. Actual production CNFs, maps, cube files, frontier receipts and proofs are absent from S; their byte identity and complete certification remain parent obligations. **This audit establishes necessary-constraint soundness subject to the stated fixes. It establishes neither K4/K5 nonexistence nor a solution of Problem16. Model review is not peer review.**