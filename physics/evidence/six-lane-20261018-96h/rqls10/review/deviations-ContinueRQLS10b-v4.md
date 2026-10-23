# Deviations record, worker ContinueRQLS10b (v4; supersedes v3 d23fb301635aefca63d4493c67d1ced828b15082cf0f9e86daf90a8a850dfae9)

Recorded 2026-10-19T05:07:01-0700 (from /bin/date). D-1 to D-6 unchanged (see v2, v3).

- D-7 (late output freezes, parent instruction 04:5x): two small-probe outputs were made 0444 some minutes after the run
  instead of immediately: evidence/wh10_flat_system_v1.result.json (born 04:29:29, 0444 at 04:31:35) and
  evidence/fixedb_anchors_v1.result.json (born 04:37:34, 0444 at 04:40:33). In both cases mtime = birth time (contents
  not modified after the run); hashes 81b5c12b...deaeb and 13d6ed64...2b95 were recorded at the freeze. Later probe
  outputs (fixedb_jacobian_v1, fixedb_candidate_verify_v1 selftest) were frozen within the same minute.
- D-8 (late registration): for the same two probes the launch-record path + sha was not sent to the parent at launch;
  it was sent afterwards (04:5x) and the parent registered both as SETTLED with a late-registration note. From
  fixedb_jacobian_v1 on, launch records are sent before each run.
- D-9 (source download location): the eprint of arXiv:2507.20154 was fetched with curl into lane tmp/ (the probes'
  TMPDIR) at ~04:44 and moved with mv -n to sources/han-zang-zhang-tian-2507.20154.eprint (0444,
  3f85d5262a1ce7a12de39a4fa432de6b740209a2b3bd6ca62af7c22b0633d891); no probe was running; tmp/ was empty afterwards.
- D-10 (prior art found after a run, recorded by the parent): the WH10 single-orbit obstruction of Grassl-McNulty-
  Mista-Paterek (arXiv:1611.08962) was identified after the WH10 v2 numerical run; the run stays a scoped UNKNOWN
  observation, not a preregistered reproduction (evidence/wh10-prior-art-addendum-v1.md 888261b6...120f).
