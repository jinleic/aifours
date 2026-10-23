# Receipt: rqls_exact_trades_v1 and v2 (initial-scope stdlib EXACT probes, fractions.Fraction)

Recorded 2026-10-19T03:23:25-0700 (from /bin/date). Owner ContinueRQLS10b. Note: evidence/exact-trades-lemma-v1.md
(b3eb8e1c10e1be983bf35a8966dd1398ea6034c68471869e84ab4e7e1d73dc07). Inputs (sha checked in-run, exit 9 otherwise):
evidence/parker_z7p3_classical_v1.result.json 00e991d6...1c30, evidence/z9p1_classical_search_v1.result.json 4199ee99...7c6b.
Both runs: cwd lane, wrapper /bin/bash -c 'echo START ... PID $$ PGID ...; exec /usr/bin/env -i TMPDIR=<lane>/tmp
/opt/homebrew/bin/python3.14 -I -B <source> <inputs+shas> <output>' (PID printed before compute), tool timeout 0,
single process, lane tmp/ empty afterwards, outputs frozen 0444. One implementation (exact rational arithmetic, real
rational vectors; parallel iff equal up to sign; Gram matrices compared to I exactly).

1. v1: source code/rqls_exact_trades_v1.py 4f8347e98352a3b6368e5429b23e0afadf071101c99e812675ba0d76324f2967; launch record
   evidence/rqls_exact_trades_v1.launch.json c303290884aa61338e1a4c81f0855aebe55dc6f2b2cb1c71b22bdd90c20a3637. START
   2026-10-19T03:14:52-0700, PID 64841 = PGID 64841, EXIT 0, END 03:14:55 (2.35 s in-run). Output
   evidence/rqls_exact_trades_v1.result.json 0d69a99cc911e560a284f978c7e929493cf9c5e91cd65952b2f26fb923714e75.
   Results: all 25 pairs orthogonal; Parker (5 pairs x 2 roles): sum (c - 1) = 3 everywhere (pairs {7,8}, {7,9}, {8,9},
   components 6 + 14); Z_9+1 (20 x 2): 0 everywhere. Each Parker start: classical 10 rays, 0 bad Gram entries, 6
   non-gauge moves (0 with finite-symbol cells); one trade 12 rays / 0 bad; commuting pair (14 + 6 cells, different
   planes) 13 rays, both orders identical, 0 bad; beam width 6 depth 5: best 13 (0 bad; parker0/QA best by depth 12, 13,
   13, 13, 13); 0 moves containing finite-symbol cells.
2. v2: source code/rqls_exact_trades_v2.py 999ff603adad6a4979180e776594013018425339c4137fe947f5f388f7fa56ad; launch record
   evidence/rqls_exact_trades_v2.launch.json 0f5656e97b885949db58cc8522b8c29cceaf8f3b57866d503414ae7909682591. START
   2026-10-19T03:19:28-0700, PID 65803 = PGID 65803, EXIT 0, END 03:19:58 (29.5 s in-run). Output
   evidence/rqls_exact_trades_v2.result.json caa7f7f7d49775ca96965ca32810100bc4db1e2754dbc2386f756338d4bbd0ca.
   Results: 60 crossed mates (5 pairs x 2 roles x 6 corner relabellings), all orthogonal mates; 58 with only the three
   inf-inf pairs disconnected, 2 (parker2, vectors from B with resolution A, corner maps (7,9,8) and (9,7,8)) with all
   seven {a, 8} (a finite) also disconnected (components 6 + 14; one 6-cell component is a K_(3,3) on rows 0, 3, 8,
   columns 0, 4, 9 and classes 7, 2, 5). 60 starts: classical 10 rays / 0 bad; one trade 12 / 0 bad; commuting pair 13
   (58) or 14 (2), both orders identical, 0 bad; beam width 12 depth 6 (3,312 states expanded, 15,580 children): best
   13 at 58 starts, 14 at the 2 special starts (finite-cell moves occur only there: 142 each), all best states 0 bad.
No 100-ray (or near-maximal) configuration arose; nothing to freeze under the candidate rule.
