# EXCERPT of moqls7-k3-cover-codex-v1.note.md (source sha256 42392eaa75503f0c0d50925c8941c69a96fbcb95658377be1d67b91acd458809; 138 LF-lines by text.split('\n'))
# Prior Codex note (gpt-6.1-sol). Omitted: LF36-129 (derivations of Q1-Q5) and LF137-end (scope).
# Lines are VERBATIM, prefixed with their ORIGINAL 1-based LF number. Cite as prior/prior-codex-note.findings-excerpt.md:LF<n>.
# DELTA-AUDIT USE ONLY: these are earlier reviewer findings, not premises and not parent conclusions.

----- original LF1-35 -----
LF1: DISPOSITION: ACCEPT-WITH-FIXES
LF2: 
LF3: This disposition concerns Q1–Q4. **Separate Q5 draft judgement: ACCEPT-WITH-FIXES, as conditional mathematics only.** No activation is authorised.
LF4: 
LF5: All copied-file SHA-256 values computed with `shasum -a 256` match `manifest.json`, including the six specified pins. References below are snapshot-relative paths with LF-based, one-based line numbers.
LF6: 
LF7: **FATAL**
LF8: 
LF9: None found in the reviewed constructions under their stated heavy-triple hypotheses.
LF10: 
LF11: **MAJOR**
LF12: 
LF13: 1. **The lex artifact does not bind the original cube metadata as required.**  
LF14:    `lane/review/AMENDMENT-3.r1.md:46` requires binding both the original cube CNF SHA and metadata. `lane/code/k3_lex.py:128` records the source CNF SHA, wrappers and generators, but never reads or hashes the source metadata. The resulting `lane/explore/k3lex/A_C311.meta.json:4` likewise lacks that binding. Hashing the lex metadata in its screen receipt does not supply the missing upstream link.
LF15: 
LF16:    **Correction:** add a supplementary provenance record binding the source cube metadata SHA, `3b2ab04f…a0f4d9ed`, to the existing cube and lex CNF hashes. Future wrapper revisions should record and validate that source metadata explicitly. Preserve the frozen artifacts and their historical hashes.
LF17: 
LF18: 2. **The draft’s activation contract needs explicit acceptance and heaviness dependencies.**  
LF19:    `lane/review/drafts/AMENDMENT-4.md:8` assumes the two original cube CNFs are UNSAT; its gate at line 50 requires successful certificates, while line 59 defers parent acceptance of the composition until an unrestricted theorem verdict. This does not explicitly require parent acceptance of the two upstream exclusions before activating the cuts.
LF20: 
LF21:    The mathematical transport also needs **every square heavy on every own row/column line**, rather than merely a heavy occurrence at the selected point. For application to arbitrary surviving K3 configurations, that domain comes from the minimality bridge and therefore requires K1 **and K2**. `lane/review/GRAM-ENCODING.r2.md:61` states this correctly; `lane/review/AMENDMENT-2.r1.md:5` also names both prerequisites. AMENDMENT-3 inherits them through the frozen cubes without restating them, and the certificate receipts only say whole-bridge acceptance is separate.
LF22: 
LF23:    **Correction:** add an explicit dependency statement to the draft and final integration record: accepted upstream C321/C411 exclusions; reviewed encoder soundness; all-line G4; and, when deriving G4 for unrestricted K3, accepted K1 and K2. K2 remains pending here. G6 itself needs neither exclusion once its singleton and G1/G2 hypotheses hold.
LF24: 
LF25: **MINOR**
LF26: 
LF27: 1. **C411 preserves the complete cube-constrained domain, not the bare `--sym` unit set.**  
LF28:    `lane/code/k3_lex.py:33` includes columns (3,4), while `lane/review/AMENDMENT-3.r1.md:20` broadly says the operations preserve all G1–G5 conditions. The swap sends the required `g_1(p,(0,3))` unit to `g_1(p,(0,4))`; the latter is not a bare-base symmetry unit.
LF29: 
LF30:    **Correction:** state that preservation is for the projection of **base ∧ complete cube**. C411 makes all four columns 1–4 positive, so the transformed pattern still satisfies every original symmetry unit. This repairs the explanation without changing the comparator.
LF31: 
LF32: 2. **The variable-order description overstates the B runtime check.**  
LF33:    `lane/review/AMENDMENT-2.r1.md:43` says the wrapper reads each encoder’s actual order and confirms agreement. A does expose its map and is compared at `lane/code/k3_cubes.py:115`. B supplies no map: line 126 checks only the variable-count lower bound.
LF34: 
LF35:    **Correction:** describe B’s agreement as established by static inspection of the pinned allocation, or add an explicit map comparison in a future wrapper revision. The present indices are correct; the discrepancy is between the described assurance and the implemented check.
----- original LF130-136 -----
LF130: | Q1..Q5 | Status | One-line reason |
LF131: |---|---|---|
LF132: | Q1 | SOUND | Eighteen assignments form exactly the three claimed residual orbits. |
LF133: | Q2 | REQUIRES-FIXES | G6 and indices are sound; B’s validation description exceeds its runtime check. |
LF134: | Q3 | REQUIRES-FIXES | Lex construction is sound; qualify C411 preservation by the complete cube. |
LF135: | Q4 | REQUIRES-FIXES | Composition is sound; source metadata binding and dependency documentation need completion. |
LF136: | Q5 | REQUIRES-FIXES | Transport and counts are conditionally sound; acceptance/domain gates need strengthening. |
