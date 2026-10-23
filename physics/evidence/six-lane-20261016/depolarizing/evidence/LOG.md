# Lane log (phys-1 depolarizing), times PDT from `date` (file mtimes), never guessed

## 2026-10-16 18:31–19:00 PDT (section written 19:00:43 PDT) — sources, evaluators, controls

- Sources read: 2608.15870v2 (KG), 2609.39747v2 (Ahmed et al., incl. supplement Thm II.3/II.9, IV.2–IV.6),
  2605.09138v2 abstract/results, 2607.27449 abstract, 2610.02176 abstract. arXiv API search 2026-10-17T01:40Z:
  nothing newer on the threshold.
- `code/gauss.py`: thermal-attenuator (A_G∘L_T) evaluator. Checks: vacuum → thermal state with mean
  (1−η)/(2η) to 3e-17; Fock 5 mean photon η·5+(1−η)N_E exact; hashing crossing 0.18929 reproduced.
- `code/finite.py`: exact finite-M sector evaluator (loss/add Horner recursion, Schwinger picture).
  `code/brute.py` brute force on 2^M: agreement ≤ 2e-15 for M = 1..7 (random rank-two real inputs, random η;
  mod-3 inputs), and M = 1 equals the hashing formula at p = 0.18929, 0.15, 0.25.
- Key structural observation (float64, exploration): for mod-3 rank-two codes the finite-M deficit is
  *relative*, not additive. Code (μ=20, w=6, q=½ Gaussian comb) at η=0.737 (p=0.19725): Gaussian I_c=3.72e-6;
  finite M: 150 → 2.81e-7 (ratio 0.075), 300 → 2.10e-6, 600 → 2.93e-6, 1200 → 3.33e-6, 2400 → 3.53e-6
  (1−ratio ≈ 125/M). Hence explicit finite-M witnesses near the Gaussian frontier need only M ~ 10²–10⁴.
- Large-photon-number plateau: cat-like combs give I_c → 0 (both signs, |I_c| ~ 1e-11 at μ=56) at every η;
  margins near the frontier are exponentially small (I_c^G ≈ 1.3e-5 @p=0.19725, 7.7e-7 @0.19875,
  4.1e-9 @0.20025 after partial optimization), consistent with Ahmed et al.'s 1e-12 at 0.2029161.

## 2026-10-16 19:00–20:05 PDT — rigorous pipeline, p = 1/5 certificate (candidate)

- `code/dd.py` (double-double on nonnegative operands), `code/cert.py` (DD Horner recursion + Arb
  Ostrowski/Gershgorin entropy enclosures), `code/combine.py`; proofs `review/PROOFS.md`.
- Controls: `evidence/test_cert_small_v2.log` 15/15 brute-force values inside rigorous enclosures (M = 4, 6, 7;
  mod-3 nonnegative, signed real, complex; both signs incl. p = 1/4). KG state R (Agarwal repo n_45_ens.pt, payload
  SHA-256 9a94606d… = KG's R) rigorously reproduced inside both KG intervals (`evidence/controls/`).
- Code optimization: `evidence/gauss/g3_k3_r01_eta0.7330000.pt` (Gaussian-limit Ic 8.89e-9 at eta = 0.733, K = 300).
  Its high-photon "noise-like" tail (|a| ~ 1e-3, n = 75..300, mixed signs) is essential: truncating it to n <= 150
  gives Ic = -1.0e-7 (float, Gaussian limit); clamping negative amplitudes to 0 also destroys positivity.
- Float finite-M (M = 2000, D = 440) of that state: p = 1/5: +1.1412e-8; p = 0.2005: +1.87e-9; p = 0.201: -7.67e-9.
- Rigorous run 19:30:40–20:00:27 PDT (4 workers, ~27-32 s/sector, ~0.5-0.7 GB RSS each): 220/220 sectors;
  combined enclosure [1.1288547919e-8, 1.1436444146e-8] -> POS (`evidence/cert/M2000_p1_5_TOTAL.json`).
  Per-sector values are negative near the center (N ~ 1450: -3.9e-8) and positive for large N; total positive.
- Ky Fan lowest-cluster refinement added afterwards (v2 code, `evidence/cert/code_snapshot_v2_kyfan/`): sector
  N = 1452 width 1.37e-10 -> 6.4e-11; small-M regression unchanged (15/15).
- 20:01:36 PDT Codex (gpt-6.1-sol, max, read-only, packet `review/codex-packet-M2000-p1_5/`) hostile review launched.
- 20:04:17 PDT same-state negative control launched at p = 201/1000 (v2 code).

## 2026-10-16 20:05–20:40 PDT — sign control, Codex review, wrap-up

- Same-state NEGATIVE control (v2 code, snapshot evidence/cert/code_snapshot_v2_kyfan/, cert.py ff9ebb72…):
  p = 201/1000, M = 2000: I_c ∈ [−7.70905e−9, −7.64967e−9] -> NEG (`evidence/cert/M2000_p201_1000_TOTAL.json`;
  219/220 sectors computed, sector N = 1234 (p_N ~ 1e−13, outside the worker ranges) bounded by ±S(ρ)·p_N).
  Together with the p = 1/5 POS certificate the state's positivity boundary lies in (0.2, 0.201) at M = 2000.
- Codex hostile review (gpt-6.1-sol, max, read-only): accept-with-fixes, no fatal issue; fixes recorded in
  review/PROOFS_v2.md A3 (flush-budget arithmetic 1.2e−257, π DD representation error ~1e−32 not 1e−40,
  provenance fields); receipt review/codex-review-M2000-p1_5.receipt.json (exit code UNKNOWN: wrapper subshell
  died; output complete and schema-valid). Delegate could not execute the Arb path (no python-flint).
- Code v3 (not yet used for any certificate): per-sector provenance (witness + cert.py SHA-256, ptail, pitail),
  combine.py provenance checks; optional C kernel code/ddkern.c (bit-equivalence to numpy path NOT yet tested).
- T2 (beyond 0.2029161) not started beyond scripts: evidence/gauss/T2_queue.sh (K = 450 continuation),
  evidence/gauss/T2_structures.sh (rank-3 mod-3, mod-4, mod-5 tests). No result.

## 2026-10-16 20:36–21:45 PDT — T1 review fixes (v3), provenance-bound rerun, discriminating controls

- Frozen code v3 `evidence/cert/code_snapshot_v3/` (cert.py 81d50d97…, dd.py cbfb39f4… (unchanged), combine.py
  4f39221a…, replay.py 67af6573…): C fast path removed from cert.py (C kernel `code/ddkern.c` unused, untested,
  not part of any certificate); every sector record carries witness canonical-JSON SHA-256, cert.py/dd.py SHA-256,
  M, p, D, ptail, pitail; combine.py rejects with named reasons; replay.py recomputes sectors bitwise.
- Proof text: PROOFS_v3.md (integrated Codex fixes), PROOFS_v4.md (= v3 + parent bridge-review exposition F1–F6,
  SHA-256 91b66ab9…). PROOFS.md (v1, pinned) and PROOFS_v2.md unchanged.
- v3 rerun p = 1/5 (workers 20:36:39–21:06, driver script died before combine; combine/replay rerun manually
  21:37–21:43): I_c ∈ [1.1373755593e−8, 1.1432769065e−8] POS (`evidence/cert/v3/p1_5_TOTAL.json`), inside the v1
  interval; 220/220 sectors; replay of 4 random sectors (seed 20261016: N = 1304, 1608, 1522, 1498) bitwise identical.
- Discriminating controls `evidence/cert/v3/mutation_tests.json`: 17/17 expected outcomes (witness_hash, cert_hash,
  dd_hash, param_mismatch ×4 incl. wrong ptail at combine, duplicate, missing, allow-missing bound, order, nonfinite,
  unexpected_sector; consistent numeric tampering passes combine (documented limit) and is caught by replay).
  Run 1 (inconsistent shift caught by `order` instead) kept as `mutation_tests_run1_inconsistent_shift.json`.
- Provenance `evidence/cert/v3/PROVENANCE.json`: raw-file vs canonical-JSON witness hashes recorded separately.
- p = 201/1000 v3 rerun (3 workers from 21:38, ranges covering all 220 selected sectors incl. N = 1234) and the
  Codex re-review (wrapper with exit capture) are queued in bg; see next entry.

## 2026-10-16 21:45–22:26 PDT — sign control v3, Codex re-review, full replay

- p = 201/1000 v3 (3 workers 21:38–22:14): I_c ∈ [−7.708902770e−9, −7.649813449e−9] NEG, 220/220 sectors
  (`evidence/cert/v3/p201_1000_TOTAL.json`), replay of 4 random sectors identical. Same state therefore has its
  positivity boundary in (1/5, 201/1000) at M = 2000.
- Codex re-review of frozen PROOFS_v4.md + code v3 + v3 results: wrapper `review/run_codex_rereview.sh`,
  receipt `review/codex-rereview-v3.receipt.json`: exit_code 0, header model gpt-6.1-sol, effort max, sandbox read-only,
  finished 22:24:54 PDT, output SHA-256 87d7d534…. Vendor relation: cross-vendor relative to this worker
  (Claude-family) and to the parent at commissioning time of the first review; same-vendor relative to the current
  (gpt-6.1-sol) parent. Disposition: accept-with-fixes; previous issues 1–5 fixed; no invalidating error; exact
  rational aggregation reproduces both intervals and classifications. Remaining minor tooling issues (not affecting
  either certificate): replay.py lacks combine-level validation and rejects nothing on an empty selection; "bitwise"
  wording should read "exact decoded-value equality of 19 fields"; combine.py does not name-reject malformed
  record shapes/diagnostic fields (empty/3-element ic_trunc, negative eps_tail, effective D, non-finite pN). Open
  for code v3.1. Issue 6 (reviewer could not run Arb) remains a stated limitation.
- 22:25:15 PDT full replay of all 220 p = 1/5 sectors launched (4 processes, same code v3).
- 22:25–23:06 PDT full replay (same code v3, 4 processes, one fresh certify() per sector incl. its own loss-chain
  descent): 220/220 p = 1/5 sector records reproduced with exact decoded-value equality of 19 fields
  (`evidence/cert/v3/p1_5_full_replay_SUMMARY.json`). This satisfies the §6 replay protocol for p = 1/5; it is NOT an
  independent implementation (that is the parent's float reproduction). p = 201/1000: 4 sampled sectors replayed only.

## 2026-10-16 23:11–23:37 PDT — v3.1 tooling + review errata; headroom assay beyond 0.2029161 (float only)

- v3.1 tooling `evidence/cert/code_snapshot_v3_1/` (cert.py 81d50d97…, dd.py cbfb39f4… unchanged; combine.py 06c82721…,
  replay.py c9395870…, tests 472dcf59…): replay validates via combine and rejects empty selections, full/sampled mode
  reported, wording "exact decoded-value equality"; combine name-rejects malformed records (ic_trunc shape, non-number
  fields, domains, effective D, pN mismatch, unparsable lines), validates witness premises explicitly (no assert),
  recomputes sector UPPER bounds in Arb (m1). Mutation controls 27/27 expected (`evidence/cert/v3_1/mutation_tests.json`).
  Recombined v3 records with v3.1: p = 1/5 POS [1.1373755593e−8, 1.1432769065e−8]; p = 201/1000 NEG
  [−7.708902770e−9, −7.649813449e−9]; Arb upper recomputation never looser than records (shift 0.0).
  Errata m1–m3 / M1 in `review/PROOFS_v5.md` (SHA-256 c0a9821e…).
- Headroom assay (Gaussian limit, float64, NOT certificates; `evidence/gauss/assay_lane{A,B}.jsonl`), eta = 0.7294
  (p = 0.20295 > 0.2029161), deterministic grid init (mu 10..90, w 3..30, q {0.4,0.45,0.5}; rank-3 q {0.34,0.4,0.5}),
  25 L-BFGS iterations, K = 220, D = 320: mod-3 (0,1) −9.8e−15; rank-3 mod-3 (0,1,2) −1.7e−14; mod-4 (0,1) −9.8e−15;
  mod-4 (0,2) −1.2e−14; mod-5 (0,1) −7.5e−15; mod-2 (0,1) −4.4e−15; mod-6 (0,2) −2.3e−14 (all at the float noise
  floor: no positive signal; optimizer stuck on the large-photon plateau). Warm start from the eta = 0.733 optimum
  padded to K = 450 (seed 1, noise 1e−4), 30 iterations: −2.33e−7 -> −4.67e−10 (negative).
  Conclusion: NO HEADROOM FOUND beyond 0.2029161 for these ansaetze/optimizer budgets. This is an optimizer-limited
  negative result, not a no-go theorem; multi-mode/concatenated variants were NOT tested (cost). Stop per protocol.

## 2026-10-17 00:42–00:46 PDT — closeout: p = 201/1000 full replay receipt; assay state

- p = 201/1000 full same-code replay (2 processes launched ~23:11:21 PDT from code_snapshot_v3_1; logs finished
  00:37:31 and 00:38:08 PDT): **220/220 selected sectors replayed exactly once, all equal on the 19 compared fields**
  (selected set N = 1234..1672 even, recomputed from p_N with ptail = 1e−13; record set = selected set; no missing,
  extra or duplicate sectors). Receipt `evidence/cert/v3_1/p201_1000_full_replay_RECEIPT.json` (SHA-256 e36579b0ea8edb6b…), reconstructed
  read-only by `code/replay_receipt.py` from the retained logs because the harness waiting job (3600 s limit) exited
  before the replay finished and never wrote its SUMMARY. Process exit codes were NOT captured (Popen, never
  waited); completion is inferred from each log being exactly one final JSON line with no REJECT/traceback.
  Provenance gap recorded in the receipt: the pre-validation step imported combine.py c0574c11… (first v3.1
  revision, bytes not retained after the 23:27:31 overwrite by 06c82721…, which accepted the same records at 23:29);
  recomputation (cert.py 81d50d97…, dd.py cbfb39f4…) and comparison (replay.py c9395870…) code are byte-preserved.
  code_snapshot_v3 still matches its SHA256SUMS (v3 certified code byte-identical).
  Both T1 runs (p = 1/5 POS, p = 201/1000 NEG) now have complete same-code replays (not an independent implementation).
- **State of the beyond-0.2029161 assay (FRONTIER_METHOD §5): NEEDS-NEW-REPRESENTATION, scoped — not a no-go.**
  Scope of the negative: one bosonic mode, M → ∞ thermal-attenuator evaluator (float64), η = 0.7294 only;
  rank-2 mod-k codes (k = 2..6; residue pairs as listed 23:11–23:37) and rank-3 mod-3; deterministic comb-grid
  starts + 25 L-BFGS iterations at K = 220, D = 320; one warm start (K = 450, seed 1, 30 iterations). Untested:
  multi-mode / non-symmetric inputs, concatenated or degenerate-code constructions, other optimizers, larger budgets,
  other η. Stopped on parent instruction; no new target self-selected (parent scout selects the next physics-1 target).
