**VERDICT: ACCEPT-WITH-FIXES.** No FATAL or MAJOR findings; 5 MINOR. Every fix is wording or labeling in the package soundness section. No representative set, formula, flag, hash or counting rule needs to change. I took the hash identities as parent-rehashed and did not re-derive any accepted lemma.

### (1) Coverage: exact

| C | Accepted reps R(C) | Admitted inputs |
|---|---|---|
| P1-B1 | {2} | `gb:P1-B1.M2:a1` (s=2) |
| P1-B2 | {2,4} | `gb:P1-B2.M2:a1` (s=2), `gb:P1-B2.M4:a1` (s=4) |
| P1-B3 | {2} | `gb:P1-B3.M2:a1` (s=2) |
| P1-B5 | {2,3} | `gb:P1-B5.M2:a1` (s=2), `gb:P1-B5.M3:a1` (s=3) |

- **Pairs:** the six entries cover six distinct (C,s) pairs, 1+2+1+2. None is missing, extra or duplicated, and no other template appears.
- **Labels:** each key's `.M<s>` matches its stated integer s.
- **Digests:** all six are well-formed 64-hex and pairwise distinct (a syntactic check only). So B2's two inputs are different files, and so are B5's.
- **Package agreement:** the package `coverage_table` names the same six. The verdict's count of 18 (12 direct + 6 strengthened) also agrees.

### (2) GB_{C,s} is what the bridge requires

The bridge ends with a moved genuine configuration. It is genuine, in U/T16 normal form and in the SAME template C. By necessity, its actual supports plus canonical GB auxiliaries satisfy GB_C (the flagged base plus 42 own-GB-name units). It also has a permutation support matrix in some s ∈ R(C). GB_C ∧ M_s is exactly what that assignment is then guaranteed to satisfy:

- **Permutation implies M_s.** M_s contains only negative binaries over primary g_s((0,c),(i,0)). A permutation matrix has at most one 1 in every row and column, so each clause holds in either orientation; the X_sᵀ wording issue does not matter here. Restricting to i = 2..7 only weakens the tail.
- **No new variables.** The tail adds no auxiliary or new variable, so the canonical assignment extends unchanged. There are no at-least-one clauses, no i = 1 rows and no auxiliaries, so nothing needs justification beyond "permutation ⟹ at-most-one". The nonemptiness remark is not used in this direction.
- **Template units are licensed.** Using GB_C with its template units, rather than the bare base, is justified because the moves preserve the SAME template.
- **Separate files are equivalent.** One file per s is equivalent to GB_C ∧ ⋁_{s∈R(C)} M_s. That matches "for some representative s", where s may depend on the configuration.

The description is correct provided the tail uses GB's own numbering, 1568(s−1)+49c+7i−5. This differs by one from GA's −6 formula: Q2, row 1, coordinate 4 maps to 1766, not 1765. The parent's decode against the GB map establishes this, but the package text does not state it (MINOR-3).

### (3) Consequence: no overreach

The package's consequence restates the GB verdict's implication at that verdict's scope. Parent-qualified UNSAT of every GB_{C,s} with s ∈ R(C) implies there is no genuine five-MOQLS(8) in the accepted U/T16 normal form with template C. The statement has three limits:
- It is conditional on qualification, and none has happened yet.
- It applies per template, and each template needs all of its representatives.
- It holds at the genuine level only.

It does not establish, and must not be recorded as, any of the following:
- Boolean UNSAT of GB_C or of GA's B_C;
- a transformation of Boolean GB models;
- equivalence to GA;
- a GA-side discharge under the NF contract amendment;
- independent support for the representative sets;
- any n=8 conclusion.

Moving from all genuine configurations to normalized ones, template exhaustiveness and the final composition all remain outside this step. "No new lemma, no CANDIDATE frozen" is accurate.

### Findings

**FATAL:** none. **MAJOR:** none.

**MINOR-1 (authority roles).** The package lists the NF verdict (`4748f023…`) and erratum 1 (`da050a74…`) next to the GB verdict without saying what each is for. Both govern the GA/WMAN Boolean chain. Erratum 1's discharge sentence concludes "Boolean UNSAT of the original B_C" and explicitly calls the GB genuine-level bridge a separate obligation. Fix:
- Label `f529224e…` as the sole authority for this implication and for GB counting ("Exactly 18 GB inputs are counted").
- Label the NF verdict as the source of the shared §1/§4 imports only.
- Label erratum 1 as GA context, not a GB discharge rule.

**MINOR-2 (shared-import caveat missing).** Carry over the GB verdict's statement that GB and GA share U/T16, WMAN, NF §1 combinatorics and §4 stabilizers/representatives. For these four templates, the sets {2}, {2,4}, {2} and {2,3} are one shared import. GB UNSATs give no independent check of them, so a composition must not present GB as independent evidence on that point.

**MINOR-3 (make GB_{C,s} self-contained).** Replace "header +126" with the full definition:
- variable count unchanged, clause count +126;
- body byte-identical to GB_C;
- tail ¬g_s((0,c),(i,0)) ∨ ¬g_s((0,d),(i,0)) for i = 2..7 and 1 ≤ c < d ≤ 7, under GB IDs 1568(s−1)+49c+7i−5.

This prevents a tail built from the GA map from being taken as equivalent.

**MINOR-4 (bind coverage to identities).** `coverage_table` lists bare names, while the TABLE uses `gb:…:a1` keys. Give each cell its key and SHA256 (or GBBINDING entry), so the coverage check runs against bound bytes, not names.

**MINOR-5 (qualification, failure wording and paraphrase).** "Parent-qualified" should point to the GB verdict's full predicate, not the NF verdict's short F4 bullets. That predicate requires:
- feeds matching GBBINDING SHA/bytes;
- a contemporaneous proof digest/count and the checker consumed count;
- exact self-exit/status lines and raw-log hash binding;
- own controls, clean settlement and all guards.

The section should also state:
- Worker PASS observations do not count.
- The spent-FIFO deviation is recorded separately.
- Any SAT, UNKNOWN, mismatch or missing replay leaves that C open; B2 and B5 each need both inputs.
- A SAT result on some GB_{C,s} is not evidence that a configuration exists.

Because the status claims to restate an accepted implication, quote it verbatim. The current paraphrase drops the (A)–(C) premise and turns "would exclude" into "excludes".
