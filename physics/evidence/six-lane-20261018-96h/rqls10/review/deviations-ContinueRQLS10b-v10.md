# Deviations record v10 — ContinueRQLS10b

Recorded 2026-10-19T08:48:52-0700 after /bin/date. Extends immutable v9 (00b7d4ed...99e); earlier D1–D22 retained.

- D23 — Parent withdrew v10 narrowing e441d858 before runtime via binding correction fabe57ab...4155a2: helper removal
  and relaxed unlinked ownership lacked owner approval. Worker preserved v10 and package unexecuted and produced ONE
  new v11 restoring /bin/date, known+unproved ownership, mixed-UID fail-closed behavior and explicitly GO'd negative
  controls. The earlier parent decision is historical only. No source-scoping exception is claimed as acceptance.
- D24 — Precautionary diff-provenance false alarm: worker briefly warned Main that an eval snapshot might omit last
  helper evidence fields. A fresh static read and diff recomputation proved frozen full source f43c7add and ALL three
  diff hashes unchanged/identical. Main was immediately told omitted-hunk list EMPTY, no actual packet defect and no
  restart/replacement needed. Redundant v2 diff files preserved/frozen. No source mutation or fabricated missing hunk.
- D25 — Additional source-only integration limitations disclosed, not hidden or used to relax tests: fast clean child
  may exit/clear before first sample; every helper/retry observation is enforced but extrema provenance is not fully
  retained; go_unlisted final date helper can add an unrelated failure. Package checker retains strict FAIL/HOLD and
  the current source remains immutable while its review runs. No probe was executed to confirm these static paths.

New source authoring used existing patterns, AST-only parsing and static config AST equality checks; no modules were
imported/executed. New plans/records are requested deliverables. Every earlier file stays unchanged.
