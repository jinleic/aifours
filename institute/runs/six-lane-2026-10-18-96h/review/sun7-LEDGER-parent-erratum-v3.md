# Closed ledger parent erratum v3 — dependency-arrow notation

Recorded 2026-10-20T01:36:20-0700 (`/bin/date`). Read after LEDGER-v1.md (fb8699b77370efcc838be0c4474cf3ba7024ced1a5b909ae4f13511c4daac5de), worker erratumv1 (92131060b0bfdc00b6e4fa3ea8875aedc52120430f9889092b4f318fe7a2fd57) and parent erratumv2 (01c855b9469df84d7c73e2bfca0621ca3db93724a07526f2dc849f717fe259f4). Responds to CI62 Codex MINOR m2 (/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-CI62-codex-v1.prompt.stdout.txt, SHA256 5d9cb1b099c16e219f91896db7962ef216668ab02531d0def9f7cf4295f48dba).

In parent erratumv2 LF6, replace the explanatory phrase "N57→N16 remains the capping dependency" by **"N16→N57 (equivalently N57←N16) remains the capping dependency"**. Arrows denote provider→consumer throughout, as in erratumv2 LF5 and LEDGER LF274, where N16 is an input of N57. No edge N57→N16 exists; the graph stays acyclic and forward in N01–N59 order.

Notation only: CI62, the conservative edge N57→N58, the DG export list and every other interface are unchanged. CI62 and the repair remain CANDIDATE_UNVERIFIED pending the second-family review and parent verdict; full Sun7 remains UNACCEPTED.
