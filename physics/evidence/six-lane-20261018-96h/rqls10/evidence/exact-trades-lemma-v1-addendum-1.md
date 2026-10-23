# Addendum 1 to evidence/exact-trades-lemma-v1.md: all orthogonal mates of the lane's 12 squares, and their trades

Recorded 2026-10-19T03:27:30-0700 (from /bin/date). Extends the note (b3eb8e1c10e1be983bf35a8966dd1398ea6034c68471869e84ab4e7e1d73dc07).
Author ContinueRQLS10b; lane-internal, unreviewed; target OPEN / UNKNOWN.

## Exact computation (stdlib, integers + Fractions; receipt below)
For each square S of the lane (Parker A, Parker B_0..B_4, A and B of the first three Z_9+1 pairs): all transversals
by backtracking (no cap hit) and all orthogonal mates M (exact covers of the 100 cells by 10 disjoint transversals,
Knuth's Algorithm X, run to completion - neither the 300-mate cap nor the 12 s limit was reached), i.e. every classical
1-RQLS(10) with resolution S up to relabelling of the vector symbols. For every mate: sigma = sum (c_(a,b) - 1).
| S | transversals | mates | sigma histogram |
|---|---|---|---|
| Parker A | 880 | 200 | 3: 184, 2: 14, 10: 2 |
| Parker B_0 | 880 | 200 | 3: 184, 2: 14, 10: 2 |
| Parker B_1 | 992 | 200 | 3: 184, 2: 14, 10: 2 |
| Parker B_2, B_3, B_4 | 880, 768, 796 | 198 each | 3: 198 |
| Z_9+1 A_0, B_0, A_1, A_2, B_2 | 728 | 10 each | 0: 10 |
| Z_9+1 B_1 | 836 | 1 | 0: 1 |
Total 1,245 classical pairs; maximum sigma = 10 (six pairs, two each for Parker A, B_0, B_1; disconnected pairs
{0,1} and {a, 9} for a = 0..8 in the mate's labelling, each split 6 + 14 - the same kind as the crossed mates of the
note). Exact trade beam search (width 12, depth 6) from the four highest-sigma pairs: classical 10 rays and 20 non-gauge
moves; best 14 distinct rays (by depth 12, 14, 14, 14, 14, 14), 0 bad Gram entries (exact).

## Consequence for the lead
Among all classical 1-RQLS(10) whose resolution is one of these 12 squares, the trade structure is poor (sigma <= 10)
and exact trades reach at most 14 rays in the searches (13 proved as the R-trade ceiling at the Parker points). Exact
trades are a correct mechanism for non-classical 1-RQLS(10) of small cardinality, not a route toward 100 from these
starting points. Not covered: classical OLS(10) with other resolutions (the order-10 Latin squares are not enumerated
here), and trades with general (non-rational) unitaries beyond the crossed mates.

## Receipt
Source code/rqls_trade_mates_v1.py sha256 b2e269b760e8a8d96fefd94239da2ccb807db8ffca249c57a7e0da067eddf641 (0444); launch record
evidence/rqls_trade_mates_v1.launch.json 14a3b840284f922d9abbdaed608e133fde60cd4773e2f3e990d72ada92f2a2e2; inputs pinned and
checked in-run (Parker 00e991d6...1c30, Z_9+1 4199ee99...7c6b). Command (cwd lane, tool timeout 0): /bin/bash -c 'echo
START ... PID $$ ...; exec /usr/bin/env -i TMPDIR=<lane>/tmp /opt/homebrew/bin/python3.14 -I -B code/rqls_trade_mates_v1.py
<inputs> evidence/rqls_trade_mates_v1.result.json'. START 2026-10-19T03:26:49-0700, PID 67158 = PGID 67158, EXIT 0, END
03:27:19 (30.3 s in-run); single process; lane tmp/ empty. Output (0444) evidence/rqls_trade_mates_v1.result.json sha256
825863beef4d6295ce601848537ffb057688d68e906a37cebb25c75441bbcd15. One implementation (no independent enumerator).
