# Extension-source package integration contract v1 (2026-10-19T08:06:57-0700)

Written only. The package implements the exact EXT(D) question of ext-search-spec-v2.md
(sha2566d94c7a2c299e61659453933b05acb425807796072b67b5e7994116e5321c0ae). Corrected R1's normalized beta-row is
(f-D0) modq. The producer uses raw g=f modq, which differs by the KNOWN column function D0 modq; this is only
representation, not a wider family. Its old mod3 rows are fixed by accepted LemmaU/R1 equivalence.

## Proven bridge
For n=3q, gcd(3,q)=1 and base DM D, a function f has D[x]-f a permutation iff, for every x,t in Zq, the set
T(x,t)={c:(D[x][c]-g[c]) modq=t} has3 columns and the three residues D[x][c]-h[c] mod3 on that set are distinct.
Here g=f modq,h=f mod3, f=CRT(h,g). This follows because each pair (s,t) in Z3xZq must occur exactly once.
On a 3-column fibre, distinctness is exactly the three binary inequalities
h[c]-h[d] != (D[x][c]-D[x][d]) mod3 (one per unordered pair); no linear relaxation is mistaken for sufficiency.

## Programs
Beta v2: column-MRV multiplicity cover, supply pruning, then exact ternary binary-difference DFS per complete g.
Independent joint checker: separate author, direct Zn exact cover over row-value items, item MRV. No CRT split and
no producer imports. It both enumerates its own set and directly checks all reported functions.
A final controls gate compares actual COMPLETE sets, not search-node counts. It verifies every f directly.
A negative target claim would require independent COMPLETE exhaustion with exact chunk coverage; no such job is
currently admitted or automatically queued.

## Raw telemetry, launch, roots
Narrowed parent contract: rqls10-supervisor-v10-scope-parent-decision-v1.json
(e441d8585228c2976700cba2c3397acfa1e544bc3dfe7af919205581572af22b). No helper process, exec, fork, subprocess,
multiprocessing or thread in an algorithm. Entry module loading by Python compile/exec is IN-PROCESS; it is not an
OS process launch. No child produces human-readable timestamps. Only elapsed monotonic wall_s, counts and hashes.
GO entrypoints reuse the separately frozen startup/root template: <=3 GO token bytes (+1 extra-byte probe), finite
120s select deadline, silent97 on no-GO, algorithm hash binding, O_NOFOLLOW job-root walk, owner/mode checks, fchdir.
A qualified supervisor must independently enforce spawn/GO deadlines, resource/cancel/settlement evidence. No
particular supervisor version's unreviewed behavior is presumed.
Each job needs fresh exact parent GO and parent admission. No autochain, no polling, no timeout/ulimit/SIGKILL.
Only one process per job. Child argv python3.14 -I -B ENTRY --job-root ABS ... ; TMPDIR inside lane, no bytecode.
Outputs fixed names under fresh parent/supervisor-created job root. Source/witness errors stop, never reclassified
as scientific negatives.

## Parent audit schema
Each previous job has a parent-owned <audit_dir>/<item>.audit.json before the next GO:
exact keys format,item,plan_sha256,verdict,settled,exit_code,declared_output_sha256,receipt_sha256,auditor,at,notes.
format='ext-search-job-audit-v1'; verdict='AUDITED_PASS'; settled=true; exit_code is exact expected int;
declared_output_sha256 maps EXACT declared output names to parent's actual hash observations. Parent audits raw
supervisor evidence/GO argv/pins/roots, not child self-hashes. Strings auditor/at/notes and receipt digest are
provenance. Parent renders at only after /bin/date. No such shared record is created by the worker.
Gate requires all audits and hashes actual files under anchored real base/job directories, no-follow regular/nlink1.
Missing/incomplete/mismatched evidence prevents controls qualification. Prior gate artifacts also belong to the prefix.
The gate always reports target_claim='UNEVALUATED'; its qualified flag ONLY means the control suite passed.

## Calibration and later search
A future separate GO may admit seeded256-probe,240s informational calibrations for each tree on the anchor m0.
These do not establish absence, correctness of an absolute runtime forecast, or permission for a full search.
Incomplete/retention stops are UNKNOWN. Any verified f, including during estimation, triggers immediate stop/pinning
and the exact raw7-row DM goes through definition checkers A/B/C and parent verification before any claim.
No full-target search is included in the control plan. Work/resource note gives exact combinatorial upper bounds
and explicit reference-storage projections, NOT measured seconds or exact RSS.
