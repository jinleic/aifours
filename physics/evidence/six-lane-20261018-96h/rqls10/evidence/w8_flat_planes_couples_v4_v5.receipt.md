# Receipt: w8_flat_planes_couples_v4 and v5 (initial-scope stdlib FLOAT explorations; evidence only)

Recorded 2026-10-19T02:36:42-0700 (from /bin/date). Owner ContinueRQLS10b. Both: cwd lane, tool timeout 0, wrapper
/bin/bash -c '...; exec /usr/bin/env -i TMPDIR=<lane>/tmp /opt/homebrew/bin/python3.14 -I -B <source> <output>'; single
process; lane tmp/ empty afterwards; outputs frozen 0444.

## v4 (independent re-run, seed 20261021; reporting by type)
Source code/w8_flat_planes_couples_v4.py 8d0c715e889e63d436a74593aa085f08fd027fa356f38fe5424bd5a4657b64e9; launch record
evidence/w8_flat_planes_couples_v4.launch.json 4a6082594b2c850b9d55f0e7fae1bed78c06ff32f478192954ff8c20371a60f7. START
2026-10-19T02:29:44-0700, PID 51828 = PGID 51828, EXIT 0, END 02:31:38 (114.7 s). Output
evidence/w8_flat_planes_couples_v4.result.json 039ea5e537447aa922eacae60e8df205b9fff0849b39435f6b9b6feb61141c9d.
Results: 9,153 starts all converged (4,359 MUB-pair, 4,794 exotic endpoints); the SAME 100 exotic planes (minimum
Frobenius distance to MUB-pair 1.0128132585841068, as v3); 130 planes WH-closed, 10 orbit representatives. Strict
rule: 867 K4 assignments, ALL of type MUB-MUB-MUB-MUB, all failing the frame test (remaining couple residual between
0.12360679774997903 and 0.4000000000000006); no assignment involving an exotic plane passes the six pairwise tests.

## v5 (same seed as v4; diagnostics of the compatibility threshold)
Source code/w8_flat_planes_couples_v5.py 09ea8ab1cf979a4797c9a6b21958f514ce6595ad5117d29093b2d2cfccfe0f73; launch record
evidence/w8_flat_planes_couples_v5.launch.json 9d55893a25fa034d76e5aac44652996a281f466a2c8cb8b8f720212add26f7d0. START
2026-10-19T02:34:36-0700, PID 52166 = PGID 52166, EXIT 0, END 02:36:30 (114.8 s). Output
evidence/w8_flat_planes_couples_v5.result.json 0e20ee96cf60a2d2f76aa1e38c3810c4bebb927e50b996095f8b282bf4cf68fd.
Results: same search outcome (9,017 starts, 100 exotic planes, same minimum distance). All 3,360 couple tests that
involve an exotic plane: relative smallest eigenvalue lambda_1 of M^* M is either <= 10^-16.2 (60 tests; 47 exactly 0;
all with second eigenvalue >= 10^-0.36 and unitary defect <= 3.4e-14) or >= 10^-0.96 (3,300 tests): a gap of 15 orders.
The strict rule of v3/v4 (lambda_1 < 1e-18) therefore UNDERCOUNTED compatible pairs (deviation D-4). Relaxed rule
(lambda_1 < 1e-10 and (lambda_2 < 1e-10 or defect < 1e-3)), which sits inside the gap: compatible orbit-representative
tests MUB-MUB 90/90/90 and exotic-exotic 20/20/20 in Z/X/T (each exotic plane has 5 exotic partners per basis), MUB-exotic
0; relaxed K4 scan: 2,250 assignments, ALL MUB-MUB-MUB-MUB (no frame test in this scan; these are covered by the written
Theorem A); NO K4 assignment containing an exotic plane, even pairwise.
Corrected reading of v3/v4: their K4 statements remain true for the assignments they list; their compatible-pair counts
are undercounts; the absence of exotic K4 assignments is confirmed with the gap-justified rule.
