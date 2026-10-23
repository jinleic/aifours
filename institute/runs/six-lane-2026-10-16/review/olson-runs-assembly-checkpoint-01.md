# olson-runs-assembly checkpoint 01 (2026-10-18T00:40:33-0700, host clock)

Owner OlsonRunsAssembly.  New exclusive files only (prefix olson-runs-assembly-); lane O untouched.
* Assembly: olson-runs-assembly-proof-v2.md sha256 0b78850fa232f61c6f45e01c5e8e9f3e2582e96572c3a4fa810fe357ac324abb (target sent to reviewers).
  v1 (153dff8a82786d04f8a9184f1f42cedee6dc6517b606593d91e1c90cb01b7bef) superseded before any review (Remark (2) wording).
* Codex snapshot: olson-runs-assembly-inputs-v1/ (29 byte-identical files + manifest.json, 353,409 bytes; parent GC spot note NOT included).
* Prompts: olson-runs-assembly-codex-v1.prompt.txt (d962b813bff102d8a10da1da4ea08c80d2e2433e048ffbdeec98eedf81ec899b, 6,081 B);
  olson-runs-assembly-claude-v1.prompt.txt (6a36c252d363f1a837f2df9ea3cb78357a7bf4cc4e8f624104aeb87942c223d1, 173,739 B <= 180 KB, one packet).
* Gate before launches: free 17,779,748,864 B at 00:39:59 and 17,776,291,840 B at 00:40:15 (>= 12.2e9 + ~3e6 projected);
  math-2 reviewers running at launch: 1 (GC desk Claude); after launch 3 (<= 4).
* Launched (bash async, TMPDIR = olson-runs-assembly-tmp/): Codex runner ~00:40:0x, Claude runner ~00:40:2x; runner timeout 2400 s
  + 60 s grace (SIGTERM only).  No verdicts yet.  No parent theorem/gate verdict is made here.
