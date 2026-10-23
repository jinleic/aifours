# Deviations record, worker ContinueRQLS10b (v6; supersedes v5 f7da945f00361a93da1c95b9fdc9a4b0148b4b8f24483d0f817d2c2a035bb794)

Recorded 2026-10-19T06:27:41-0700 (from /bin/date). D-1 to D-11 unchanged (see v2 to v5).

- D-12 (authoring by copy-then-edit; disclosed for completeness). After the new-version rule (05:54), several NEW
  version files were created by copying the previous frozen version to the new path (cp -n, never onto an existing
  file) and then editing that new, not yet frozen, never cited and never run file before freezing it:
  code/owned_supervisor_v5.py (from v4), code/owned_supervisor_v6.py (from v5), code/rqls_fixedb_lm_v6.py (from v5),
  code/fixedb_q1_check_v4.py (from v3). For code/rqls_fixedb_lm_v5.py the copied v4 content was replaced by the v5
  content in one write before the first freeze. No frozen or cited file was modified; every predecessor stays frozen
  as it stood; each new file has a frozen diff against its predecessor in review/ (supervisor v3->v4, v4->v5, v5->v6;
  assay v4->v6 and v5->v6; checkers are new files). The intermediate copies were identical to the frozen predecessors.
- D-13 (static checks during the HOLD): parse-only checks (python -I -B -c "import ast; ast.parse(...)", plus an
  unbound-name scan) were run on this worker's own sources while new computational launches were on hold
  (RUN/review/runtime-guard-admission-HOLD-v1.json). They read source text only; no supervised, scientific or
  qualification code was executed. Reported to the parent with the supervisor sources.
