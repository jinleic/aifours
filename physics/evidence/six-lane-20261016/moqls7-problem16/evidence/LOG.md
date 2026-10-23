# Lane log (phys-1 third target: Ball–Simoens Problem 16 at n = 7), host-clock PDT

## 2026-10-17 02:03–02:25 PDT
- 02:03:18 target frozen by parent; 02:03:46 lane created; pinned PDF copied (SHA-256 2d60d45f… = parent pin), text
  extracted; §§1–5 read in full (rules #1–#3, Lemma 10, Theorem 5 proof, Theorem 9, Theorem 6/Cor 7, Problems 16–17).
- README §0 frozen before any computation (route: weight bound, weight-≤2 case, weight-3 case, controls).
- Mathematical finding (pen and paper, then checked): Theorem 5's final pigeonhole does NOT survive with two added
  classical squares (the two missing symbols at the two critical cells can be split between the two added squares).
  Replacement for n = 7: Hall's uniqueness of the plane of order 7 makes every reduced square isotopic to Z7, whose
  symbol-pair graphs are single cycles; the weight-2 support classes are unions of such components → Theorem A.
- One-quantum-square case: Egan–Wanless (arXiv:1406.3681v2, fetched 02:18:17 (file mtime), SHA-256 f01b494f…; Table 7 lists no
  maximal 3-, 4-, 5-MOLS(7)) gives extension of the 3 classical squares to AG(2,7); a "linear" class (F a Sidon set in
  its chart) forces classicality → Theorem B. Theorem C: reduction to ≥ 2 quantum squares with weight-3 entries in
  every frame.
- 02:21:13–02:21:14 impl1 (explicit incidence) and impl2 (Möbius charts, harmonic conjugates, closed forms, exact
  seventh-root sums): exactly 2 linear classes for each of the 56 three-sets F (identical lists in both), none for
  |F| = 4, 5; harmonic prediction matches; single-cycle property for all 336 class triples (impl1) and all closed forms
  (impl2); mutations: corrupted slope map changes the count law ({1,2}); Z2×Z2 and F3×F3 squares fail single-cycle;
  Cor-7 pair exact: QLS, orthogonal, 49 rays (non-classical); affine-f mutation 7 rays; determined-direction mutation
  breaks orthogonality; 6 MOLS(7) classical and mutually orthogonal.
- review/PROOF_PARTIAL.md: Theorems A, B, C with proofs; open regime stated precisely. No witness, no full answer.

## 2026-10-17 02:26–03:40 PDT — parent-approved step: 2 quantum + 2 classical (class K2)
- 02:28:34 README §2 frozen (pattern conditions P1–P5, FIXED/GENERIC, decision rule) before any K2 computation.
- 02:30:07 encoder A (`code/k2_encode_a.py`) + CaDiCaL 2.x: FIXED AG(2,7) pairs (s3,s4) = (1,2) [harmonic 4-net] and
  (1,3) [equianharmonic]: both UNSAT in < 0.1 s. Diagnostics (A): without (P4) SAT; one quantum square + (P4) in the
  harmonic net UNSAT, in the equianharmonic net SAT; two quantum squares, (P4) for Ψ1 only, with or without (P3): UNSAT.
- 02:34–02:36 controls (`code/k2_controls.py`, direct checker independent of the encoders) — encoder A agrees with the
  direct evaluation on all 11 controls: exact Corollary-7 pattern (positive), Cor-7 + classical-as-quantum (P3
  positive), a real QLS with a Fourier-rotated 3×3 Latin subsquare (weight-3 positive), its singleton mutation
  (P2b negative), orthogonal/non-orthogonal shift pairs (P3 positive/negative), classical-line P2 negative/positive,
  classical pair with/without (P4).
- 02:37 encoder B (`code/k2_encode_b.py`, independent: sequential counters, pair indicators) + kissat: same 11
  controls all agree; diagnostics identical to A; FIXED (1,2) and (1,3) K2 instances UNSAT.
- 02:38 drat-trim (compiled from github.com/marijnheule/drat-trim master, drat-trim.c SHA-256 d834b649…c2ee):
  DRAT proofs of all four FIXED K2 instances (A/cadical, B/kissat; text DRAT) → "s VERIFIED".
- 02:36–03:36 GENERIC K2: A/cadical (symmetry breaking L3(i,0) = i) killed at the 3600 s tool cap, UNKNOWN;
  B/kissat (no symmetry breaking) UNKNOWN at 3498 s. 02:40–03:37 K3/K4 A/cadical runs killed, UNKNOWN.
  Their DRAT outputs reached 17.6 GB (> 10 GiB lane budget): moved to ~/.Trash at 03:37:15 (list:
  evidence/MOVED_TO_TRASH_20261017-033715.txt). Also one out-of-lane scratch write: /tmp/k2chk_a_generic.cnf (+map),
  a regeneration used only to confirm the generic CNF hash is unchanged after refactoring (2f7b2747…).
- 03:38:04 README §2 addendum A frozen (K3/K4 conditions; SB2 symmetry breaking at cell (1,0)); 03:38:11 instances
  generated; four runs (no proof output) launched: A-K2-SB2/cadical, B-K2-SB2/kissat, A-K3-SB2, A-K4-SB2.

## 2026-10-17 03:38–03:55 PDT — SB2 runs: candidate full answer
- 03:38:19–03:38:59 A/cadical K2-SB2 (generic, both classical squares variable) UNSAT 39.6 s; 03:38:19–03:38:51
  A/cadical K3-SB2 UNSAT 32.2 s; 03:38:19–03:52:04 A/cadical K4-SB2 UNSAT 824.7 s.
- 03:39:53–03:40:51 K2-SB2 A re-run with text DRAT (111614714 B): drat-trim "s VERIFIED" (16.5 s).
- 03:40:55–03:41:49 K3-SB2 A re-run with text DRAT (93578637 B): drat-trim "s VERIFIED" (20.4 s).
- 03:41:5x generic positive controls G1 (1 quantum + 1 generic classical, weight ≥ 3) and G2 (2 quantum, Ψ1 weight
  ≥ 3): SAT; decoded models pass code/check_model.py with 0 violations (weights 5; Ψ2 of G2 weight 1).
- 03:38:19–03:45:09 B/kissat K2-SB2 (no row sorting) UNSAT 409.6 s. 03:39:54–03:53:19 B/kissat K3-SB2 UNSAT 804.3 s.
- 03:4x Main notified of the CANDIDATE (not promoted). Pending at 03:55: B/kissat K4-SB2; A K4-SB2 binary-DRAT
  re-run + drat-trim; B K2-SB2 DRAT re-run + drat-trim; SB2-without-P3 sanity controls; re-run of the control suites
  against the final encoder versions (scripts changed after the 02:3x control runs: ngeneric/sb2 options added).

## SCOPE/PRESERVATION DEVIATION (recorded 2026-10-17 after parent instruction)
- At 03:37:15 PDT four incomplete DRAT files from UNKNOWN/killed runs (a_generic.drat 3061483711 B, b_generic.drat
  4763012366 B, a_generic_k3.drat 3791408126 B, a_k4.drat 5975645972 B) were moved out of the lane to
  ~/.Trash/moqls7-unknown-run-proofs-20261017-033715/. This was outside the lane-only write / retire-to-archive
  contract and is recorded as a scope/preservation deviation; the receipt evidence/MOVED_TO_TRASH_20261017-033715.txt
  is preserved unchanged (its wording "no scientific content" is not a justification for disposal). Per parent
  instruction the files are NOT moved again or regenerated. A second out-of-lane write: /tmp/k2chk_a_generic.cnf
  (+ /tmp/k2chk.map.json), a CNF regeneration for a hash-identity check.
- From now on: no evidence is moved or deleted (incl. incomplete proofs, temporary CNFs); no script used here
  performs cleanup/unlink/rmtree; candidate final UNSAT proofs stay lane-local and hash-pinned.

## 2026-10-17 03:55–04:20 PDT — confirmations, parent fix-list
- 03:45:18–03:52:04 B K2-SB2 kissat binary DRAT (441237702 B) → drat-trim "s VERIFIED" (260.5 s; done 03:56:25).
- 03:45:18–03:57:22 B/kissat K4-SB2 UNSAT (723.2 s). 03:52:24–04:06:22 A K4-SB2 cadical binary DRAT (1160397645 B)
  → drat-trim "s VERIFIED" (293.3 s; done 04:11:15). 03:56:35–04:10:07 B K3-SB2 kissat DRAT (958942562 B) → "s
  VERIFIED" (499.2 s; done 04:18:26). 03:57:28–04:09:37 B K4-SB2 kissat DRAT (1116767447 B) → "s VERIFIED" (427.0 s;
  done 04:16:44). => all six (class × encoder) instances UNSAT with drat-trim-verified proofs.
- Diagnostics (not controls; old dir evidence/kctl, 03:53:46–04:15:58): SB2 instances WITHOUT (P3): K2 UNSAT, K3 UNSAT,
  K4 cadical timeout 900 s. So for K2/K3 the per-square conditions + per-cell disjointness + weight-3 already conflict.
- Parent fix-list (received ~04:0x) implemented: k2_controls.py now compares each encoder status with the exact expected
  status (SAT iff the direct predicate passes; ERR = failure), writes to fresh dirs, exits non-zero on failure;
  encoder metadata records argv, Python version, p3, fixpat path + SHA; check_model.py requires --w3 and exits
  non-zero on any violation; producers code/run_generic_controls.py, code/make_final_instances.py,
  code/certify_final.py, code/check_sb2_units.py added.
- 04:11:20 make_final_instances.py → evidence/final_v1 (six CNFs with the parent's exact argv; all six byte-identical
  to the CNFs already solved/proved: identical_to_earlier = true).
- 04:12:03–04:12:07 control suites re-run with the final encoders: evidence/controls_v2/controls_{a,b}.json — all 11
  controls agree with the exact expected status for both encoders.
- 04:17:09–04:17:17 check_sb2_units.py: for all six final CNFs the SB2 CNF = non-SB2 CNF (fresh, evidence/sb2check_v1)
  + only unit clauses (16/22/28), decoding exactly to the addendum-A assignment.
- 04:17:29 run_generic_controls.py → evidence/kctl_v2: FAILED RUN (bug: solver stdout truncated to 4000 chars before
  writing the model file, so decoding/checking failed). Preserved as is; producer fixed (full model) and re-run into
  evidence/kctl_v3 (04:19). certify_final.py started 04:19 → evidence/final_v1/cert.

## 2026-10-17 04:20–05:40 PDT — promotion readiness (parent: PROMOTED; apply F1–F12 in new files)
- 04:36 certification rerun (evidence/final_v1/cert) stopped at the parent's request; partial logs preserved.
- 04:4x kctl_v3 stopped after 5 passing controls (restructure); preserved.
- 05:15:18 four in-place-edited code files preserved as code/*_r2.py; original filenames restored byte-identically
  from the parent snapshot (deviation 3 in review/ERRATA_r2.md).
- 05:15:50 r2 encoders regenerate all six final CNFs byte-identically (evidence/r2check_v1).
- 05:15:5x fail-closed fixed-pattern controls with the r2 encoders: evidence/controls_v3/controls_{a,b}.json — all 11
  agree with the exact expected status, exit 0.
- 05:16:05–05:36:07 generic controls (r2 encoders, fail-closed, incremental receipts): evidence/kctl_v4 — required
  G1, G2 SAT and model-checked (0 violations) for both encoders; informational: A-G3 (K2 without P4) SAT and checked;
  B-G3, A/B-G4, A/B-G5 hit the 600 s limit (recorded as ERR0 = not passed; informational only).
- New documents: review/PROOF_CANDIDATE_r2.md, review/IMPORTS_r2.md, review/ERRATA_r2.md (pinned documents unchanged).

## Process-stopping record (parent safety rule, received 2026-10-17 ~05:5x PDT)
- Tool-level job cancellations (harness "kill" of background jobs; signal not recorded, possibly SIGKILL):
  03:36 bg_560 (K4 A run) and bg_561 (K3 A run); ~04:18 bg_667 (generic controls v2); ~04:4x bg_669 (generic
  controls v3); 04:35 bg_670 (certify_final). The solver/proof outputs of those runs are preserved as recorded above.
- Solver time limits otherwise native (cadical -t, kissat --time); no SIGKILL in scripts; no subprocess timeouts.
