# K62-FULL-erratum-v1: one diagnostic-pointer correction in the mutation checks of K62-FULL-v1 (no statement or proof change)

- **Written:** `/bin/date` read at 2026-10-19T13:19:18-0700, immediately before this exclusive write.
- **Overlays:** `K62-FULL-v1.md` (this directory), sha256 fabf04dd6abb1d3ec7e71b1cc3d459e008e9a96b5186b5a1f571fedac1312e5b, which stays frozen and byte-identical. Read the
  candidate first, then this erratum.
- **Source:** parent IRC of 13:2x relaying Codex review 9bf84a11 of the pending M13X packet (two MINOR diagnostic pointers,
  "if repeated in the full K62 packet"). Only the first recurs here; the second (M13X mutation 7, apex t in FB (vi)-(vii)) has no
  counterpart in K62-FULL-v1. Checked by me against the frozen text: the Old block below occurs exactly once (line 271).
- **Scope:** a pointer inside a thought-experiment remark of section 10. No lemma, case split, inequality, premise or claim
  changes. CANDIDATE_UNVERIFIED status unchanged.

## F1: section 10, mutation check (2): where DEG at t is used
**Old** (line 271):
```text
  Lemma 2 in SG: at t a multiplier 3 is possible, R4S/CIS at t fail, and DEG at t (used in FB (vii) and Step 1) is lost. (3) Drop
```
**New:**
```text
  Lemma 2 in SG: at t a multiplier 3 is possible, R4S/CIS at t fail, and DEG at t is lost; DEG at t enters through DEG (c) (no
  K4, no bowtie: used in FB (ii) and, with DEG (a), in TRI) and through DEG (a) for c4, c5 in Step 1 of Theorem K62X. FB (vii)
  does not use it there: in case (c) t lies in Q, so the isolated fifth vertex of O is not t. CIS/EQS at t are used by ONE and
  T16 whenever t is an apex (for example in FB (v) when t is c or q). (3) Drop
```

## Unchanged
Everything else in K62-FULL-v1. No K7, Sun(7), novelty, Lean or human-review claim. Sun(5)/Sun(6) remain computer-assisted
transitive imports.
