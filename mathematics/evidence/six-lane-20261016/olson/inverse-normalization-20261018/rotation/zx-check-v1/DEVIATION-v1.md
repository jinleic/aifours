# zx-check-v1: disclosed deviation (CPU-limit backstop), v1

Written after host clock 2026-10-18T11:53:11-07:00 by OlsonRotationRigidity, at the parent's instruction (IRC at about
11:52).

## Deviation

run1 was launched at 11:48 via ../code/gate_v1.sh inside a bash subshell that first set `ulimit -t 9300`.  The
command was:
  (ulimit -t 9300; ../code/gate_v1.sh 100000000 python3 -B code/zx_check_v1.py out/run1.jsonl ...)
This is PLAN-v1.md Sec. 5 ("CPU: ulimit -t 9300 as a native backstop").

- A hard CPU limit is enforced by the kernel with SIGXCPU and then SIGKILL.  It is therefore an automatic kill
  backstop, which the frozen continuation contract does not allow.  The plan's statement "no kill" was wrong in this
  respect.
- The script's own budget (BUDGET_S = 9000 s of wall-clock time, checked every 4096 enumeration nodes) ends before the
  9300 s CPU limit can be reached: CPU time cannot exceed wall time for this single-threaded process.  So the backstop
  is not expected to fire.
- If it did fire, the run would end without a DONE or DONE_PARTIAL line; every item without an ITEM line would then be
  UNKNOWN.
- As instructed, the running process is not stopped, and no signal is sent to it.

Earlier runs of this slice used the same `ulimit -t` pattern.  At the time it was this slice's README protocol
(README L75).  Disclosed here as the same deviation:
- zs-check-v1 run1: ulimit -t 3000; it finished normally in 878 s.
- p5o4-v1 stages G, D and C, fixtures and mutcheck: ulimit -t 3600 / 3600 / 300 / 600 / 900 / 300 / 1800; all exited 0
  normally.
- The 04:17-04:44 S-family runs: S(7,25,7) was stopped by its CPU limit (ulimit -t 900, SIGXCPU) at 04:44:17 and was
  recorded as UNKNOWN (README L142).

## Rule from now on

For any future launch: no ulimit and no timeout backstop.  The script's own self-budget is the only bound.  A stop,
if ever needed, is an owned SIGTERM with a bounded wait.  Results remain aid only.
