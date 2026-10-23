# MOQLS(8) refinement r3 first invocation: parent quarantine disposition

Parent at 2026-10-18T04:26:53-07:00. The first P1-B1 invocation (leaf P1-B1.L1.000, expected CNF `78b2857e3c8bb42b5e22c69fb7d79757864a42fa0bb76bb433e70b0a700cab84`) is **UNKNOWN**. It is not a refutation and not a proof. The fail-closed stop and quarantine were **correct**.

## Evidence

- Supervisor record: `physics/evidence/six-lane-20261016/moqls8-problem16/evidence/N8_FONE_R3.P1-B1.1792322536667751000.json`, sha256 `2b1e92e617b584cb875635d93a26d697b971507d85ea085c9551c819ebae1ec5`. supervise_r3 `0ee8f394…ec4d` tripped after 9.679 s with `unknown probe of pid 36858: {'pid': 36858, 'bsd_bytes': 0, 'errno': 1}`. It SIGTERMed the reserved group: no killpg error, no survivors, leader rc −15. Peak sampled RSS 1,942,044,672 B. The quarantine record `physics/evidence/six-lane-20261016/moqls8-problem16/evidence/N8_FONE_REFINE_R3_QUARANTINE.json` (sha256 `c5f76542ff09bbac3a4ea75a4ed2eb22787feb07a60388e8b87354d2f34c1081`) persists.
- Observed group members: python3.13 leader, `du`, `cadical`, `drat-trim`, plus pid 36858, whose BSD info read failed with EPERM.
- Root cause, verified statically: legacy R `code/k5_resplit_r2.py` (sha256 `90b6f5928058db04315534640dba556486a969441009f0e680f5de0873558484`) line 63 measures child RSS with `subprocess.run(["ps", "-o", "rss=", "-p", …])`. On this host `/bin/ps` is setuid root (`-rwsr-xr-x root wheel`). An unprivileged `proc_pidinfo` on a setuid-root process returns EPERM, and supervise_r3 correctly classifies that as unknown, hence uncertain. [INFERENCE] pid 36858 was that `ps` child; its identity could not be read, so this is the only setuid tool on the worker path, not an observed comm.
- The static controls (`cad9069e…35cf`) could not see this, because they make no native or supervise invocations, as designed.

## Decisions

1. No rerun of this leaf under the current sources. The ledger state REFINED / `STOP_OUTER_UNKNOWN` stays as written.
2. Required fix: a NEW legacy-R version that measures RSS without setuid helpers, e.g. libproc `proc_pid_rusage` as in supervise_r3's probe, or drops R's internal sampling in favour of the outer cap. Data plane, child bytes, cover and limits stay unchanged. Also scan every module on the worker path for setuid/setgid executables (`ps`, `top`, `lsof`, …) and remove them.
3. Before any further native work: (a) parent source PASS of the new R and an updated packet; (b) static controls; (c) one supervised NON-native smoke under supervise_r3 that exercises R's RSS path on a sleeping child and records zero unknown probes.
4. The quarantine file may then be retired only by a MOVE to an archive path with a manifest entry, never deleted, and only after a separate parent message naming the exact file and sha. Code never removes it.
5. Lease 7ff6aa67…e206 remains P1-B1-only. No other family.
