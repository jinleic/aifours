# Erratum 1 to review/rqls10-fixedb-GO-request-v2.md (cbc89a55f7592f81fbf2753e7894121ed08d6fcb752d3b6216324d4b6866d6cd)

Recorded 2026-10-19T05:27:55-0700 (from /bin/date; written shortly after). Requester ContinueRQLS10b. The request file is
unchanged; this note corrects the Q1 pass criteria against the actual code of code/owned_supervisor_v2.py
(1fece595...15aa) and discloses two risks. No code or config changes; nothing has been run.

- E1 (wrong label). After a DEADLINE trip owned_supervisor_v2 sends ONE identity-checked SIGTERM to the process group;
  the next poll that finds the child gone records status "EXITED" (lines 116-119). "EXITED_AFTER_SIGTERM" is set only
  on the finally path (line 177). Corrected criterion (b): supervisor receipt status EXITED, returncode 5,
  trips[0].trip = "DEADLINE", sigterm_sent true, identity_ok_at_signal true, settlement SETTLED, group_members_after [],
  and exit latency receipt.wall_s - trips[0].t <= 7 s (5 s plus one 2 s sample period); child stop receipt status
  TERMINATED_UNKNOWN with stage "WD"; at most one WD run record after the trip, with st = "TERMINATED".
- E2 (stage windows). Stage ends are absolute (t0 + cumulative plan); each stage starts when the previous one finishes.
  W therefore starts when KP completes (probably well before 360 s) and runs until about 612 s. Corrected criterion (a):
  exactly one W run record has st = "DEADLINE", it is the last W run record, a W SKIPPED_TIME record follows, and the W
  summary has 612 <= elapsed_s <= 614.
- E3 (risk, no change made). KP perturbs every chart coordinate by amp * N(0,1), so the perturbation norm is about
  amp * sqrt(P): at amp = 1e-2 about 0.16 (v = 7, P = 252), 0.20 (v = 8, P = 392) and 0.28 (v = 10, P = 810), versus
  about 0.045 in rqls_wh10_lm_v2 (P = 20). Recovery at this size is untested in this model (lane precedent: the v7
  forced-Z7+3 LM recovered 16/16 near-anchor starts up to amp 0.1, a different model). If KP_near_anchor fails, Q1 ends
  with exit 3 before W and is inconclusive for (a)/(b). Option for the parent: accept the risk, or request a v5 that
  gates only amp = 1e-3 (norm <= 0.03) and records amp = 1e-2.
- E4 (throughput estimate, not measured). A v = 10 LM iteration assembles an 810 x 810 normal matrix (45 pair blocks of
  180 x 180 from 40 x 180 real Jacobian blocks) and solves it (about 0.35 GFlop per solve; estimated 0.05-0.2 s
  single-threaded), so a 300-iteration v = 10 run may take tens of seconds and Phase 1's W / WD / KR-Parker10 windows may
  complete only a few to a few tens of v = 10 runs (unstarted runs are recorded as SKIPPED_TIME). Phase 1 records mean_s
  for sizing Phase 2.
- Checker for the criteria: code/fixedb_q1_check_v1.py (stdlib, reads the Q1 outputs only; written, not run).
