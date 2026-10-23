# Census run receipts (E15b / E15c), written after host clock 2026-10-18T12:12:35-0700

Owner OlsonReflectionRigidity.  These are factual run records.  The census is a finite aid and not a premise.
Process-policy deviation, recorded explicitly: every census run below was launched with a HARD CPU backstop (`ulimit -t N`).  Main's
policy of 12:0x PDT prohibits these (kernel SIGXCPU/SIGKILL); all new runs use self-budgets or cooperative SIGTERM only.  No new run
after that message uses ulimit.

| job | command cells | limits | outcome | status of cells |
|---|---|---|---|---|
| bg_2099 | e15b_census.py 4:15 5:17 6:19 4:14 | ulimit -t 3300; tool timeout 3500 | exit 152 (SIGXCPU) during (5,17) | (4,15) DONE (out/e15b_4_15.json); (5,17) UNKNOWN; rest not started |
| bg_2141 | e15b_census_v2.py 4:13 4:12 | ulimit -t 1700; tool timeout 1800 | completed | (4,13), (4,12) DONE |
| bg_2142 | e15b_census_v2.py 4:9 4:10 4:11 4:14 5:13 5:11 5:12 6:13 5:17 5:16 6:19 | ulimit -t 3500; tool timeout 3600 | exit 143 (external SIGTERM, 09:25:49 event; cause not mine) during (5,17) | 8 cells DONE; (5,17) UNKNOWN (2nd attempt); (5,16), (6,19) not started |
| bg_2162 | e15c_census.py 4:15 5:17 6:19 5:16 | ulimit -t 3000; tool timeout 3200 | exit 152 (SIGXCPU) during (6,19) | (4,15) cross-check DONE; (5,17) DONE (3rd attempt); (6,19) UNKNOWN (actual SIGXCPU); (5,16) not started |
| bg_2213 | e15c_census.py 5:16 5:15 5:14 | ulimit -t 10000; tool timeout clamped to 3600 | my owned SIGTERM after 33 s, to relaunch without the tool deadline | (5,16) UNKNOWN (attempt 1) |
| bg_2214 | e15c_census.py 5:16 5:15 5:14 6:18 6:17 | ulimit -t 10000; tool timeout 0 | my owned SIGTERM at 12:11:46 after Main's policy message (elapsed 1:52:46) | (5,16), (5,15), (5,14) DONE; (6,18) UNKNOWN; (6,17) not started |

For bg_2214, the last progress line observed for (6,18) before the stop was "6:18 6000 21002 900295966 0 5892": 6000 of 21002
data processed, 900,295,966 nodes, 0 leaves after pruning, 5892 s.  This is NOT a completed cell.

Completed cells (p = 7, B = 0), all with 0 full avoiders:
- (3,13) [E15];
- (4,9), (4,10), (4,11), (4,12), (4,13), (4,14), (4,15) [E15b; (4,15) also by E15c];
- (5,11), (5,12), (5,13) [E15b];
- (5,14), (5,15), (5,16), (5,17) [E15c];
- (6,13) [E15b].
UNKNOWN or not run: (6,14), (6,15), (6,16), (6,17), (6,18), (6,19).  They will not be attempted before 17:30: none could finish.
Positive control: code/e15_control_pos.py (not yet run natively; run informally in the eval transcript, where it found the known
length-(4p - 3) avoider and an independent DP agreed).
