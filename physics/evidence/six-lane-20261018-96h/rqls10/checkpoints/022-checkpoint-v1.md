# Checkpoint 022 (rqls10 continuation, successor worker)

Recorded 2026-10-19T06:13:46-0700 (from /bin/date). Owner ContinueRQLS10b. Target OPEN / UNKNOWN; no candidate. No
process of this worker running (read-only census 05:59: no fixedb/fourier/rqls/supervisor process; no process with cwd
in the lane; lane tmp/ empty). Nothing executed since 05:07 except parse-only static checks (ast.parse) of own sources.

## Events since 021
- Parent ran fourier_co_enum_v1 (2b72ec87...83a6) itself under owned_supervisor_v2 (RUN/review/rqls10-FCO-parent-run-v1/,
  receipt 10e78174...3940, audit parent-audit-v1.json f8b5a8e2...5807): 13/13 gates PASS; FCO(n) COMPLETE with no
  solution for n = 2, 4, 6, 8, 10 (n = 10: all 362,880 normalised pi, 5,420 full zero tables, 0 rho); n = 7: 198
  normalised solutions (84 maximal), n = 9: 2,916 (1,296 maximal). Parent: ONE-producer restricted negative CANDIDATE;
  independent verification being prepared by the parent; producer not to be rerun.
- Written (unreviewed): evidence/fourier-co-ansatz-v1-addendum-2.md 2e4f9124...b010 (Lemma F8: any orthonormal
  transversal of a Fourier-separable array gives an FCO(n) solution, sigma relabelling included) and addendum-3
  18933031...3b99 (F9: additive-exponent / bicharacter arrays reduce to the separable form; corrects the scope sentence
  of addendum 2). Deviations v5 review/deviations-ContinueRQLS10b-v5.md f7da945f...b794 (D-11 pre-freeze same-path
  rewrites; new-version rule from 05:54). code/fco_candidate_verify_v1.py frozen unchanged (6b7b9ccd...68ca).
- Parent SAFETY HOLD on all new computational launches (RUN/review/runtime-guard-admission-HOLD-v1.json 6c1d8440...dc1f)
  and Codex HOLD on rqls_fixedb_lm_v4 (RUN/review/rqls10-fixedB-v4-source-codex-v1.prompt.stdout.txt 14568433...802e).
  Assignment: this worker owns a new generic supervisor (v2 untouched), then assay v5. Written so far (NOT run):
  code/owned_supervisor_v3.py 4f5e61fc...601f (first draft, superseded before submission),
  code/owned_supervisor_v4.py 5d14ebc0...dfdd (diff review/owned_supervisor_v3_to_v4.diff e665b7f8...ecbf3),
  evidence/owned_supervisor_v4.config-example-v1.json 33eb5e35...348d, code/guard_qual_child_v1.py 21ff3edb...c3cb.

## Next
1. owned_supervisor_v5: v4 plus unattributed-new-lane-process rule (fast-escaping descendants reparented to launchd are
   caught via lane cwd/argv) - found while writing the qualification child.
2. Guard qualification plan + child v2 + checker (NOEXEC), then send to the parent.
3. Assay v5 (LM stop precedence, guarded initialisation, numpy after GO, same-version N/C/KP/KR gates before targets,
   telemetry, emergency witness reservation).
