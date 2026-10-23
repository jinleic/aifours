# MOQLS(8) P1 Boolean normal form — parent verdict v1 and certification-contract amendment

Parent at 2026-10-18T06:11:00-07:00. **CORRECTNESS-ACCEPTED as a conditional Boolean lemma** (partial; no n=8 theorem, no K4/K5 exclusion, no gate).

## Accepted statement

The text is [P1_COLUMN0_BOOLEAN_NORMAL_FORM.r2.md](../../../../physics/evidence/six-lane-20261016/moqls8-problem16/review/P1_COLUMN0_BOOLEAN_NORMAL_FORM.r2.md) (sha256 `8ae0ac01de7ea5883111e8dcc4f84246813d8599b1e8af782e0498104a449e8f`). r1 is `5c748dd8…faa4`. The r1→r2 diff, read in full, changes only the 3×3 classification paragraph: it lists unrestricted full K33 and excludes it by the already-proved degree bounds (row 6, column 1 ≤ 2), which is the Codex MINOR.

Fix one of the four exact WMAN inputs B_C = F_one ∧ C, with C ∈ {P1-B1, P1-B2, P1-B3, P1-B5} (WMAN `355b3380…fc74`). **Every Boolean model of B_C yields a Boolean model of B_C ∧ M_s** for some s in the listed representatives: {2} for B1, {2,4} for B2, {2} for B3, {2,3} for B5. Here M_s is the 126 negative binary clauses ¬g_s((0,c),(i,0)) ∨ ¬g_s((0,d),(i,0)), with i=2..7 and 1≤c<d≤7. Hence UNSAT of all six exact strengthened inputs implies Boolean UNSAT of the four B_C. This is a model transformation (primary relabelling under the template stabilizer, recomputation of the forced AND/prefix auxiliaries, explicit w3), not a CNF automorphism. It uses only G2/G3 support facts: no unitary, phase or rank realization.

## Evidence

1. [Codex](moqls8-p1-boolean-normalform-codex-v1.note.md), `030f92a826ab4d85e6d7fd0d9a7e5538986facf897afb6e81f7cb902ad714e30`: ACCEPT-WITH-FIXES, 0 FATAL, 0 MAJOR, 1 MINOR. The MINOR (K33 premise accounting) is fixed in r2.
2. [Claude](moqls8-p1-boolean-normalform-claude-v1.note.md), `a1a8eb7d1ad6223c2d12bc39c0ca8936f511645deb560f1e43bfd3a41a563805` (prompt `7d6d46c64eaf9e715b6f67693ad182de2b58ea7151c8c5253c96fd4e65ec759f`, no tools): ACCEPT-WITH-FIXES, 0 FATAL, 0 MAJOR, 10 MINOR. It independently audited:
   - the (A)/(B)/(C) support lemma and the 25-form 3×3 classification;
   - k ≤ 3, the ≥9-ones bound and the permutation-count bounds;
   - G2–G5 invariance;
   - completeness of the auxiliary families (7,840 g + 94,080 b3 + 376,320 c4 + 31,360 u5 + 280 w3 + 35 lexeq = 509,915);
   - the P4/SB2/ROWLEX extension, the unit decoding, the stabilizers and orbits, and the meaning of M_s.
3. Parent finite/format check ([RESULT](moqls8-p1-normalform-parent-v1/RESULT.json), `e075aff8…cbc2`): all 512 3×3 patterns, the template stabilizers and orbits, and 126 clauses per square: PASS.
4. Parent check, this verdict, against name map `7b4dd597…b197`:
   - all 245 IDs g_s((0,c),(i,0)), s=1..5, c,i=1..7, equal 1568(s−1)+49c+7i−6;
   - Claude's SB2 cross-check (Q2 row 1, coordinate 4) decodes to 1765;
   - the four canonical M_s tails rebuilt from the map reproduce the parent fingerprints for s=2..5;
   - the map's argv is generic mode, ngeneric 0, `--p4 12345 --sb2 --g5 --rowlex`, with no all-rows P4 and no fixg. This confirms the instance-flag premises of Claude MINOR 5.
5. Parent strengthened-formula binding ([BINDING.json](moqls8-strengthened-parent-replay-v1/BINDING.json), `5e1116e8311bfe4b2e06554edd0c77fc564574b06c1320334373648171f5f98c`): all six parent-composed inputs (header +126, body unchanged, tail appended) equal the worker r2 hashes. Formula identity only; no refutation yet.

## MINOR dispositions

- **Wording only:** 1 (undefined A → "fixes 0,1,2,3 pointwise"), 2 (SB2 vs template attribution), 3 (orientation X_sᵀ), 7 (B5 distinct labels, identity case), 8 (F_one scope, untouched leaves).
- **Discharged by the evidence above:** 4 (Claude's own call-site enumeration plus the bound header count), 5 (argv check), 6 (parent finite stabilizer check), 9 (ID formula, cross-check, fingerprints and independent six-hash binding).
- **10 (transfer versus contract):** handled by the amendment below.

## Certification-contract amendment (n8 lane)

The [unified disposition](moqls8-unified-parent-disposition-v1.md) item 3 required qualifying refutations of all sixteen exact WMAN inputs. **Amended:** the four inputs P1-B1/B2/B3/B5 may instead be discharged by this accepted lemma together with qualifying, parent-replayed refutations of **all six** strengthened inputs, including both of B2's and both of B5's. Each must meet the unchanged F4 strict predicate:
- measured complete solver and checker feeds whose hash equals the bound strengthened hash;
- solver rc20 with exact `s UNSATISFIABLE`;
- parent drat-trim rc0 with exact `s VERIFIED` after CR removal only;
- no NOT VERIFIED or TIMEOUT.

The twelve direct inputs keep their accepted exact refutations. A final full-composition verdict with hostile assembly reviews remains mandatory before any n=8 statement. Any SAT, UNKNOWN or binding mismatch among the six leaves the corresponding template open.
