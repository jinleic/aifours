# Deviations record v9 — ContinueRQLS10b

Recorded 2026-10-19T08:17:48-0700 after /bin/date. Extends immutable v8 (2601b1a8...f331); D1–D18 unchanged.

- D19 — Additional read-only design evidence, no guard/science execution: downloaded Apple's public kern_exec.c into
  lane tmp/xnu_kern_exec.c, SHA256 89531d33618b8361064236189212c3c96be1b32e098690b17802b6b15d932d1a, frozen0444.
  Read lines7096–7104 (exec changes idversion), read libproc/XNU PID-path semantics; a passive /bin/ps real/effective UID
  listing found persistent login ruid501/euid0 processes. Read-only binary metadata/strings found the Homebrew Python
  framework bin/python3.14 launcher uses posix_spawn/re-exec into Python.app; qualification pins the actual Python.app
  executable. No numerical module was imported and no qualification probe was executed.
- D20 — Scope supersession, NOT a repeated clock-policy violation: parent binding decision e441d858...af22b explicitly
  removes helpers and forbids ALL human-readable supervisor timestamps. V10 records raw labelled clocks only; parent
  GO/audit/release retain the /bin/date obligation. V8's earlier Python-rendered timestamps remain rejected.
- D21 — Prior package-v5 drafts were snapshot-cited and are frozen exactly as recorded in README-addendum-4. New
  v10-bound child/config/checker filenames preserve those files. New source authoring was followed by AST-only parse
  and unresolved-name checks; an authoring syntax error in checker v6 was corrected before its first freeze. No frozen
  or cited file was edited.
- D22 — Static v10 integration caveat disclosed before runtime: full_census can discard an incomplete retry's resource
  observation before caller enforcement. Main was notified; v10 and its qualification plan remain held, source
  correction/disposition pending. No attempt was made to conceal the issue or bypass a resource check.
