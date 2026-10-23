# Lane log (host clock, PDT, 2026-10-17)

## Setup
- Parent IRC at about 10:24: new target, AME(4,6) minimum support. Contract SHA 1baee483…5f15 (read).
- 10:37:21 lane created (`mkdir`, no -p) with code/, evidence/, review/, archive/, explore/ and sources/.
- 10:37:52 (mtime) README §0 frozen before any computation, SHA b1fccb53…dafe. A byte copy is in
  `archive/README.protocol-frozen-2026-10-17T103752.md`.
- 10:37:58 sources copied with `cp -n` from the parent screen; their SHAs match the manifest. Open-status web searches
  at about 10:40 found nothing newer.

## Positive control
- 10:39:26 first run failed on an IndentationError (edit slip). Fixed; then 10:39:39–10:39:40
  `code/pandya_control.py` gave all_required_true = true:
  - six marginals 72ρ = 2I over Z[√2];
  - s = 60, t = 12, e = 0;
  - components 12×(1×1) + 12×(2×2) per reshaping;
  - RCM C1–C4 hold;
  - five mutations rejected.

## SAT exploration (not evidence)
- 10:47–10:49 `code/ame_e0_cnf.py` (e = 0 full model). The fixed-Pandya CNF is SAT under kissat at 10:47:57.
- 10:49:07–11:19:07 t = 14 with SB2 τ ∈ {3, 4, 6}: kissat, native --time=1800, three processes. All UNKNOWN.
- 11:21:19–11:41:19 large t, τ = 6:
  - t = 30: UNSAT at 727 s (kissat, no proof);
  - t = 28 and t = 26: UNKNOWN at 1200 s.
- 11:45:14–11:45:26 N-only model `code/ame_e0n_cnf.py` at t = 30. The generator file had an edit slip that dropped
  the SB normal form (fixed afterwards), so the CNF was a weaker relaxation. It was SAT, and the solution N
  (12 elements, coordinate-4 twins) has a consistent full phase system (exact HNF). So the t = 30 obstruction is in
  the classical completion.
- `code/lratcheck.c`, an independent LRAT checker (RUP only), accepts a CaDiCaL PHP(6,5) proof and rejects a
  corrupted copy (11:24).

## Partial result s ≥ 42
- About 11:48: parent IRC asks for a frozen s ≥ 42 file with definitions, every reduction, the Fourier
  classification, an explicit phase obstruction and a pinned replay set.
- 11:49:48–11:50:18 `code/verify_lower42.py` (9106089a…182b), stdlib only, gave all_required_true = true:
  - F1: exactly 10 of the 12870 8-subsets of {0,1}^4 have uniform 2-marginals, the parity sets;
  - F2: two 2×2 blocks per reshaping;
  - F3: a verified signed three-block obstruction for each set;
  - F4: all 50625 subcubes.
  Outputs: `evidence/verify_lower42.json` (caee2f5e…1eaa) and `.stdout.txt` (e62cb4ee…00cc).
- 11:52:42 (mtime) FROZEN `review/SUPPORT_LOWER42.r1.md`, SHA-256
  54880341b045b18fac6b60394c9ad12ae778de40945f2454fa04142c079bb2ad, 259 lines. The draft was moved with `mv -n` to
  `archive/SUPPORT_LOWER42.r1.DRAFT-working-copy.md`, byte-identical. The only citation is Tarry, for t = 36.

## Large-t engines and the s ≥ 46 package
- 11:53–12:00 `code/large_t_e0.py` and `code/large_t_gen.py` written. (30,0) excluded. Positive and negative controls
  in `code/engine_control.py`.
- 12:03 C LRAT checker strictness diagnosed: CaDiCaL emits already-satisfied hints. `code/lratcheck_py.py` (an
  independent checker) agrees. Both now skip satisfied hints, which is sound.
- 12:08:10 FROZEN `review/SUPPORT_LOWER42.r2.md` (1db90164…1418), after the Codex and Claude fixes. New cross-check
  `code/verify_lower42_r2.py`. r1 unchanged.
- 12:13 sympy 1.14 lpmax gave a wrong optimum on a test LP. The moduli LP was removed from the exclusion logic.
  12:25 replaced by an exactly verified Stiemke certificate, with controls (`evidence/moduli_cert_tests.json`).
- 12:23:46 LRAT soundness tests N1–N7, P1, P2 pass for both checkers.
- 12:25–12:35 final engine 28c0c1f9… regenerated (30,0), (30,2), (30,3), (29,2) and (28,0), all excluded. The e = 0
  cross-check engine agrees on (30,0) and (28,0).
- 12:35:20–12:38:49 and 12:40:16–12:44:04 receipt `evidence/lower46_receipt.json` (05729155…f3fe): 18 pairs,
  verified by both checkers. 6 satisfied hints in two t28_e0 proofs; those two fail the strict mode.
- 12:45:12 FROZEN `review/SUPPORT_LOWER46.r1.md` (d5b076ba…fc83).
- **12:39 RESOURCE VIOLATION.** (26,0) with the frozen engine materialised orbits of a group of order 20,736,000. It
  reached about 35 GiB RSS (8 GiB cap) and a 1.96 GB CNF. It was stopped with SIGTERM at 12:39:39 (exit 143).
  Outcome UNKNOWN.
- 12:45:56 (28,3) stopped with SIGTERM for disk; outcome UNKNOWN. Older-code exclusions (27,2), (28,2), (29,3),
  (29,4), (30,4) and (30,5) are uncertified, and are not claims.
- 12:48:31 exact byte accounting: du 9,334,255,616 B. 1,134,727,168 B remain under 10 GiB minus 256 MiB headroom.
  Parent decision: option (c). Pause orbit-materialising searches; freeze a resource guard first.
- 12:49–13:01 resource guard.
  - CaDiCaL reads the CNF from stdin and writes a .gz LRAT stream; FIFO-plus-pipe checking tested on PHP(6,5).
    An attempt that backgrounded a shell FIFO writer hung in the tool environment and was abandoned. A Python thread
    feeding the FIFO works.
  - `code/large_t_lex.py` (v2) and `code/guard_smoke.py` written. Smoke S1–S9 all match (13:00:52–13:00:56).
  - 13:01:16 FROZEN `review/ENGINE_V2_GUARD.r1.md` (d5733a7366c6d7fb3c197829ed6232abcb74c27f7250fa556cc59f34a3a273fd).
- 13:02–13:51 s ≥ 48 package and engine v3.
  - v2 proof runs of the 7 small cases at 13:02, and of (26,0) at 13:24–13:43; all EXCLUDED.
  - Receipt r2 at 13:44–13:45, all OK.
  - 13:47:22 FROZEN `review/SUPPORT_LOWER48.r1.md` (0457570502535eb3bb6aaa8002f81ca640451c8364079c9e0f4cc9413fb49f95).
  - 13:49:36 FROZEN `review/ENGINE_V3.r1.md` (fd7c7447…4449). It was frozen immediately after an edit that left a
    duplicated bullet at lines 75–76, which is cosmetic.
  - 13:51:01 FROZEN `README.AMENDMENT-1.md` (47f8e5c1…d061); exploration chunks started.
  - Parent messages, folded in:
    - the explicit phase-certificate format;
    - the LOWER46 r2 dependency chain stays unchanged;
    - Lemmas 17 and 18 go into LOWER48;
    - the LOWER48 §3 symmetry wording is to be fixed in r2;
    - the run-wide 12e9 free floor.
- 13:52–14:20 reviews, r2 freezes and (24,0).
  - Both the Codex and the Claude reviews of LOWER48 flagged the false clause-set symmetry claim and gave the
    realizable-support repair. The Claude review of LOWER46 found 4 MAJOR record gaps and 8 MINOR items.
  - LOWER46 r2 frozen at 14:12:01 (fac5242b…f35b), with the parent's binding receipts pinned. The parent then accepted
    s ≥ 46.
  - Guard erratum frozen at 14:16:05 (6cb1fd8c…ab65). LOWER48 r2 frozen at 14:16:50 (70daac01…f60e).
  - (24,0) exploration was stopped with SIGTERM at 14:19:14 and is UNKNOWN: profile {6,6}{2⁶}³ had 980+ solutions.
- 14:20–14:50 method experiments on the hard (24,0) profiles (exploration only).
  - Profile 0, {6,6}{2⁶}³:
    - N-only enumeration: 270 solutions in 240 s, of which 269 are phase-excluded and 1 is phase-consistent with
      completion UNSAT (`explore/reconstruct_t24_p0.json`).
    - Stronger lex sets (all transpositions; pairwise products) do not finish.
    - Officer-first decomposition: ≥942 officer representatives in 150 s; the first 460 hole patterns admit no N.
    - Joint N+officer CNF: 68 solutions in 150 s, not finished.
  - Profiles 1–3 ({6,4,2}, {6,3,3}, {6,2,2,2} with {2⁶}³) are joint-CNF UNSAT in 7–9 s. Most other profiles finish in
    seconds.
  - Parent instruction (14:4x): an e = 0 support that is phase-consistent with a SAT completion must be reconstructed
    exactly, with |6ψ| = 1/√2 on N and 1 on T, phases from the exact solution over R/2πZ, and exact checks of all three
    reshapings.
    - Tool: `code/reconstruct_e0.py`. A theta-key parsing bug on the SAT path was fixed in place before that path was
      ever exercised; the one recorded candidate had completion UNSAT.
    - Controls: `code/reconstruct_controls.py` gives `evidence/reconstruct_controls.json`, all_required_true. Pandya's
      60-term state, with the Hermite θ (denominators 1, 2), passes the exact check of all three reshapings; a phase
      shift, a removed officer and a point moved onto an officer line are all rejected.
  - **14:4x parent: s ≥ 48 CORRECTNESS-ACCEPTED** (partial), per `review/ame46-lower48-parent-verdict.md`.
  - Lex-prefix clarification for future texts: at k = 1 substitute q0 = true and drop the tautological clause
    (`review/ame46-lower48-lex-prefix-clarification-v1.md`).
- 15:13 INVALID exploration run (discarded): exp_triangle.py ran with a broken z2 filter left by an edit slip (if-body 'pass' instead of 'continue'), adding 466,560 clauses, many unsound; it reported 'COMPLETE' for (24,0) profile 0 in 2.4 s. The result is void. Filter restored; the run is repeated.
- 15:29 the joint model + triangle clauses enumerated (24,0) profile 0 completely in 418 s (42 solutions), in an
  exploration probe.
- 15:33:10 FROZEN `review/ENGINE_V4.r1.md` (fd1d47f2…8c12); v4 `code/large_t_joint4.py` (42d6e510…26a9). Controls:
  `evidence/guard_smoke4.json` (e0eff74b…e208).
  - An edit slip in `code/guard_smoke4.py` cut the wrong lines; the run crashed with a NameError and produced no
    result. The lines were restored and the controls rerun.
- 15:33:22 FROZEN `README.AMENDMENT-2.md` (31be56f5…aa56). 15:37:22 FROZEN `review/V4_PROOF_SCHEMA.r1.md`
  (f558e75b…b986).
- 15:33:22–15:57:41 (24,0) v4 exploration: EXCLUDED-EXPLORATION (`evidence/large_t_joint4_t24_e0_explore.json`
  b2887b51…ba1f). 158 profiles; 42 solutions, all in profile 0 and all phase-excluded; no candidate, no trip; peak RSS
  3,565 MiB.
- Parent bound the W generator: PASS. Codex and Claude v4 reviews: ACCEPT-WITH-FIXES (mathematics accepted). Fixes
  went into v5.
- 15:55:38–15:56:26 v5 controls K1–K7, all true (`evidence/guard_smoke5.json` 1d9c3cb0…a0).
- 15:59:07 FROZEN `review/ENGINE_V5.r1.md` (5393238f…bf0a); v5 `code/large_t_joint5.py` (e57067c2…33f8). Proof-mode
  go requested for s ≥ 49, with resource estimates.
- Tool-policy note: at 15:3x the v4 spec draft's placeholders were filled by a small python string-replace in bash
  rather than with the edit tool. The content was checked afterwards (no placeholders left), and the file was then
  frozen.
- 16:22:41 schema_regen_check: all 34 final CNFs (four e>0 s=48 cases + (30,0) W smoke) regenerated from review/V4_PROOF_SCHEMA.r2.md text match (stdout explore/large_t_joint5/schema_regen_check.stdout.txt 265418d1906a5edb3036b6c35929fa2e255c80f3a631c2377d95d72ed462680b). 16:04:48-16:21:57 (24,0) v5 proof UNKNOWN (disk guard; report evidence/large_t_joint5_t24_e0.json 43476468b7b1f55933f1fc2b38b8de35e0b234edf3cb41a51f867412e1606c8c). 16:22:57 amendment 3 frozen (0ef73324e6373234e30592daace76e810d7ef4e6c2e01081c69f86dea9988a6d); s=49 exploration (30,7),(28,5),(27,4) EXCLUDED-EXPLORATION; stopped on parent decision (i) at 16:23; SIGTERM also reached the tool job-runner PID 61118 of that background job (exit 143), no other effect. 16:24:01-16:24:39 v6 controls all true (evidence/guard_smoke6.json 94b7daad2fc80a58841491a41622ddfaa4f8dec282ac1e2ca18be365a4a31365). 16:25:03 FROZEN review/ENGINE_V6.r1.md (7c997fc87a9b8036105c8d4b1217b9f5ab039bd0a7e8db7b5eef2e044184eb68). Unfrozen LOWER49 draft archived (not claimed). Compute stopped; handoff in README §2.
