# Errata r2 (2026-10-17 PDT) — applies to the pinned lane documents; none of them is edited

Review findings (Claude CLI complete-claim review, institute/runs/six-lane-2026-10-16/review/
moqls7-claude-complete-claim-review.note.md):
- F1 PROOF_CANDIDATE.md "Status"/§5: "PENDING" and "NOT independently reviewed" are stale; hash prefixes only.
  Replaced by PROOF_CANDIDATE_r2.md §0/§5 (full SHA-256, argv, solver and drat-trim hashes, lane and parent checks;
  the logic needs one verified UNSAT per class).
- F2 PROOF_PARTIAL.md status line ("Problem 16 at n = 7 is NOT solved") and §5 ("No witness and no exclusion is
  claimed for this regime"): superseded — the open regime of PROOF_PARTIAL §5 (≥ 2 quantum squares) is excluded by
  the K2/K3/K4 certificates (PROOF_CANDIDATE_r2).
- F3 PROOF_CANDIDATE.md §5.3 "agrees" claims for evidence/k2/controls_{a,b}.json: withdrawn (the pinned
  k2_controls.py counted solver ERR as agreement for negative controls). Replaced by the fail-closed rerun
  evidence/controls_v3 (exact expected status; ERR/timeout = failure; exit status non-zero on failure).
- F4 PROOF_CANDIDATE.md Status (a) "human proofs": read "model-authored written arguments" (not human peer-reviewed).
- F5 PROOF_CANDIDATE.md §2/§4: S′ need not be isotopic to S; (SB2) acts on the vectors of S′ before Lemma P; encoder
  A's extra row sort belongs to (R6). Done in PROOF_CANDIDATE_r2 §2.
- F6 IMPORTS.md I1: same-or-disjoint justification added and "unchanged up to phase" corrected to "unchanged"
  (IMPORTS_r2 I1).
- F7 pinned k2_encode_a.py docstring: "(P1)-(P5)" should read "(P1)-(P4) + (SB2)"; "full equivalences" is false for the
  one-way weight flags w3. Corrected in code/k2_encode_a_r2.py (docstring/metadata only; byte-identical CNFs).
- F8 pinned k2_encode_b.py: classical labels start at 3 regardless of the quantum labels (K3: classical square
  "L3" in B = L4 in A/proof; separate dicts, no aliasing); docstring "symmetry breaking default OFF … does not rely on
  the row-permutation argument" — the certified runs use (SB2) but not the row sort; metadata lacked p3/fixpat.
  Corrected in code/k2_encode_b_r2.py (docstring/metadata only; byte-identical CNFs, evidence/r2check_v1).
- F9 B's counter() emits tautologies/duplicate literals for constant ±TRUE inputs: legal DIMACS, semantics
  unchanged; not changed (would alter the certified CNFs).
- F10 PROOF_PARTIAL.md §0 cites Egan–Wanless "Table 7" for maximal sets: read Table 5 (IMPORTS_r2 I2).
- F11 concerns the parent's proof-check receipt (drat-trim command line, concurrency, host): parent item, not lane.
- F12 index conventions: PROOF_PARTIAL uses 1..7 (row 1 reference), everything else 0..6 (row 0 reference); mapping
  stated in PROOF_CANDIDATE_r2 §1.
- N1 (LRAT + verified checker) not done. N2 (A and B share one specification) acknowledged. N3 (no SAT control for
  the (SB2) path): relaxed (SB2)-without-(P3) runs were UNSAT (K2, K3) / timeout (K4), so only the static unit-clause
  check evidence/sb2check_v1 exercises (SB2). N4 (Theorem C's every-frame claims unused) acknowledged.

Also: PROOF_PARTIAL.md §0 "Imported results" lists Hall/Shrikhande/Bose as used; on the accepted route they are
redundant (IMPORTS_r2 I3). IMPORTS.md I5 says "Table 7 … (layout.txt:782–804) has the same n = 7 rows": Table 7's
n = 7 rows (layout.txt:790–792) are k = 1, 2, 6 as stated; Tables 5 and 7 agree, Table 5 is the one used.

Process deviations (all recorded in evidence/LOG.md):
1. 03:37:15 four incomplete DRAT files of UNKNOWN/killed runs (17.6 GB) moved to ~/.Trash (outside the lane-only /
   no-disposal contract). Receipt evidence/MOVED_TO_TRASH_20261017-033715.txt preserved; files not moved again.
2. Out-of-lane scratch write /tmp/k2chk_a_generic.cnf (+ /tmp/k2chk.map.json).
3. After the parent's 03:58:43 snapshot, code/k2_encode_a.py, k2_encode_b.py, k2_controls.py and check_model.py were
   edited in place (metadata, fail-closed controls). At 05:15:18 the edited contents were preserved as
   code/*_r2.py and the four original filenames restored byte-identically from the parent snapshot (SHA-256
   b935bb11…, 097c62f8…, 270a8237…, 82ef5240…). Receipts written between those times (evidence/controls_v2,
   evidence/final_v1, evidence/sb2check_v1, evidence/kctl_v2, kctl_v3) record the edited (= r2) hashes.
4. evidence/kctl_v2: failed run (producer truncated solver output to 4000 characters before writing the model file,
   so decoding failed); preserved. evidence/kctl_v3: stopped by me after its first five controls passed (to restructure
   with incremental receipts); preserved. evidence/final_v1/cert: certification rerun stopped at the parent's request
   (partial logs preserved: fresh UNSAT for A-K2/K3/K4 and B-K2, drat-trim VERIFIED for A-K2, A-K3, B-K2).
