# Short reflection-run selector — independent bounded replay and selector-count consequence

Owner **MathOlson-2-2**, original math-2. Native `/bin/date` before this write: **Wed Oct 28 17:43:10 PDT 2026**.
This is an ADDITIVE record for the immutable74LF candidate `frontier-20261028-dihedral-short-run-selector-v1.md`, SHA256 `1ecac435f4c31dc20ed1c36d67ec7f61d748d8258c1e927a22d47364b0d81e20`.
Its statement that the independent checker had not yet run was true at its original17:37:05 observation; that pinned historical statement is not edited or backdated.

## 1. Independent check actually run

The producer `frontier-20261028-dihedral-short-run-experiment.py`, SHA256 `a2669f75a2a8a0e405385bf8b8a2e185e6c828a8d13f904359652e52e335b7e6`, had already completed its single bounded run before the f42 priority review, saving `frontier-20261028-dihedral-short-run-results.json`, SHA256 `d5f8392f4adcfa056202bcc581385dc07d4ca9bef96d83e13da03300c2cd0a6d`.
After f42 was actually returned, I wrote `frontier-20261028-dihedral-short-run-checker.py`, SHA256 `263a4ebea6fadfbea87ba2c85a3b74cfe5ed2f5f306f72e97d4fbe0c155ffc3e`, independently and without importing producer code, then ran:

```text
python3 -B frontier-20261028-dihedral-short-run-checker.py frontier-20261028-dihedral-short-run-results.json
```

Actual output: `PASS_INDEPENDENT_SHORT_RUN_REPLAY`, input SHA equal to the saved result above; **1,200** random full original words replayed, **659** qualifying actual selectors directly verified, and **4** structured actual-family instances verified.
The seed is2026102806; p=3,5,7,11 and EVERY R from2p−2 through3p−2 are sampled,40 per (p,R). These are diagnostic samples, not a probability estimate or a proof for all words.

For each saved candidate the checker independently reconstructs maximum disjoint unequal rotation-pair count from multiplicities, every qualifying contiguous reflection run and its actual directed difference set. It checks the saved exact t omissions, s pair choices, any fixed omissions, the2p DISTINCT increasing original indices, and directly multiplies the actual D_(2p) word.
The four structured family specializations also independently fail the named earlier fixed-I two-reflection, same-gap, long-run and saturated-separated-packet certificates as stated in the saved result.

Three deliberately corrupted records were rejected for their intended reasons: `bad selector indices`, `rotation pair reuse or order`, and `not an actual qualifying reflection run`.
No producer output was rerun or overwritten. This checker is separately written but same-harness; it is not a formal proof, human/cross-model review, or novelty determination.

## 2. Additional exact selector-count consequence

Retain the ACTUAL notation/hypotheses of the source theorem. Fix the chosen s disjoint unequal-rotation pairs and fixed t−s outside omissions. Let Σ be the set of actual sums of the retained2p−2 rotations and D_H the directed reflection-difference set from the actual contiguous run.

For each distinct `v∈Σ∩D_H`, choose ONE actual omission pattern realizing v and ONE actual ordered reflection pair realizing v. The source's original-order multiplication proves these choices give a valid2p-occurrence identity selector.
Different v values cannot arise from the SAME chosen rotation index set, so they give DISTINCT original selector index sets even if arbitrary witnesses are chosen.
Consequently, under the source theorem's hypothesis, the number of distinct actual selectors obtained by this mechanism is at least

`|Σ∩D_H| ≥ |Σ|+|D_H|−p ≥ min(p,s+1)+|D_H|−p >0`.

This is a written lower bound conditional on the SAME fixed word/run/pairs, not a count of all selectors or an assertion that its hypotheses hold for every word.

## 3. Remaining scope

The original odd-prime dihedral and all-finite-group problems remain unresolved. This addendum does not turn a sampled run, a selected reflection run, or the sufficient support inequality into an unrestricted theorem.
No original avoiding word, novelty/priority, formal/kernel, human or independent-model-family acceptance is claimed.
The latest owner direction authorized bounded local checks; no external model/API, secret, Git push, deletion, publication or infrastructure mutation was used.

**END — independent short-run check and exact conditional count.**
