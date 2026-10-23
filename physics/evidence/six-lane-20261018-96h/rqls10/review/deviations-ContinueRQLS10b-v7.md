# Deviations record, worker ContinueRQLS10b (v7; supersedes v6 a8c34dff084a63ceea9fcb43841d315e8715c59661a47acffc6a33b4c1331aa3)

Recorded 2026-10-19T07:06:03-0700 (from /bin/date). D-1 to D-13 unchanged (see v2 to v6).

- D-14 (checkpoint cadence): checkpoint 024 was due by about 06:57 (30 min after 023 at 06:27) and is written at 07:06,
  about 9 minutes late, while the supervisor v7 and assay/checker successors were being authored.
- D-15 (network reads into the lane): public XNU source files were downloaded with curl from
  raw.githubusercontent.com/apple-oss-distributions/xnu (main) into lane tmp/ (xnu_kern_exit.c, xnu_kern_fork.c,
  xnu_kern_proc.c, xnu_proc_info.c, xnu_proc_info_private.h, xnu_libproc.c; sha256 in
  review/rqls10-owned-supervisor-v7-disposition-v1.json) to cite kernel semantics; files are 0444 and kept. Read-only
  inspection of the installed NumPy (numpy/__config__.py, otool -L of two extension modules) and of the SDK header
  vecLib thread_api.h was used for the runtime-identity design; nothing was imported or executed.
- D-16 (authoring by copy-then-edit, continued from D-12): code/owned_supervisor_v7.py, code/rqls_fixedb_lm_v7.py and
  code/fixedb_q1_check_v5.py were written as new files and edited before their first freeze; code/guard_qual_child_v5.py,
  code/guard_qual_configs_v4.py, code/guard_qual_check_v4.py and the plan v4 were created as copies of their frozen
  predecessors (cp -n) and edited before freezing. No frozen or cited file was modified.
