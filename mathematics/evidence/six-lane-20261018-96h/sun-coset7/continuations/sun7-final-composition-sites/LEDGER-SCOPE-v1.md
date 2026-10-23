# LEDGER-SCOPE-v1 — frozen scope for the closed interface ledger and module graph (written-only, throttled)

- **Written:** `/bin/date` read at 2026-10-20T00:23:33-0700, immediately before this exclusive create; frozen BEFORE reading the census outputs,
  the final candidate or the final review. Owner SunM13MixedFibres, math-1. Previous checkpoint: checkpoint-010-final-v1 at
  2026-10-19T22:49:18-0700 (then parked).
- **Authority:** `RUN/control/written-sun7-closed-interface-ledger-transition-v1.json` sha256
  50ba9d9c2aec544983a246bd435221b6d7a74a608fc81d320fa2af7d9a948cd1 (read in full) and the parent IRC announcing it. RUN :=
  /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h. Not runtime authority.
- **Pre-freeze exposure (disclosed):** only the transition file was read. The input files it names were hashed (metadata
  only); every pinned sha256 matched (final candidate 9f7a60c2…, candidate erratum 00b9749d…, final review output e12c4c80…,
  final disposition b1466297…, census outputs ROOTS 18e12f90…, ROWS-K63 fc258a63…, RICH-A1 702aacb1…, R2-A2 c33c441d…,
  K62 27485e5f…, census index 3700b22a…, RW a6272c5b…). Earlier in this session I wrote FCS-SITES-v1, CUT-v3 (+erratum),
  FINAL-BC-repair-v1, FINAL-EXPOSURE-v1 and FINAL-EXPOSURE2-v1 in this directory; they are prior work, cited only by path and
  hash, and are not premises of the ledger. The eval kernel was re-created (metadata helpers only).

## Target (fixed now; from the transition's "target")
1. **Closed interface ledger.** For EVERY live incoming interface listed by each of the five census reviews (ROOTS,
   ROWS-K63, RICH-A1, R2-A2, K62) and by the final candidate (with its erratum): exact statement/scope (literal LF
   citation), governing correction, and discharge: (a) the censused proof body that proves it (which census, which
   source LF), or (b) permitted classical Zhu Sun(3)/Sun(4), or (c) an accepted S5W/S6W statement at a named site.
2. **Explicit closed module graph:** nodes = retained modules, edges = the ledger interfaces; replaces the numbered
   "01-17, 24, RW, 18-23, 25-79" assertion of the final candidate; with an explicit acyclicity order (topological list in
   which every edge goes forward).
3. **Sun(5)/Sun(6) site binding:** every live Sun(5)/Sun(6) site bound to S5W/S6W with ambient subgroup, coset side and
   inversion, and piece count.
4. **Residuals:** any interface whose proof body was NOT censused is listed as an exact residual (source, LF, what is
   missing), never silently discharged.

## Method and rules
- Bookkeeping only: literal LF citations; no theorem re-derivation and no new mathematical claim; every ledger row is
  CANDIDATE_UNVERIFIED. Where a census output, the census index or a parent disposition already records a discharge, cite
  it; where none does, the row is a residual.
- Sources: exactly the transition's inputs, the parent census dispositions, and the accepted source bodies and verdicts they
  cite (read-only). Census outputs are read in full.
- Deliverable: `LEDGER-v1.md` (ledger, graph, Sun-site table, residuals); at most two review packets, each <= 100 KB package
  plus selected source, with {path, sha256, start, end} manifests whose hashes re-check; a metadata receipt; checkpoints
  <= 1800 s apart; exclusive-create files only in this directory; then park.
- Not claimed: completeness certification, acceptance, full Sun(7), novelty, Lean, human review, runtime authority.
