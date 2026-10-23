# Receipt: wh10_flat_system_v1 (initial-scope stdlib EXACT probe, Q(zeta_5) with Fraction coefficients)

Recorded 2026-10-19T04:31:35-0700 (from /bin/date). Owner ContinueRQLS10b. Run after the parent's WH10 v2 run had settled
(parent IRC allowed initial-scope stdlib probes again). Source code/wh10_flat_system_v1.py
55413a59d45b7c2f1326a126a94973f4a0bb396bbfdc1181a523c14ccd0407eb (0444); launch record evidence/wh10_flat_system_v1.launch.json
6f2e0b126506a2ce7331350ac3678b35e7245af11d1723d741e0b86c4070689a. Command (cwd lane, tool timeout 0): /bin/bash -c 'echo START
... PID $$ ...; exec /usr/bin/env -i TMPDIR=<lane>/tmp /opt/homebrew/bin/python3.14 -I -B code/wh10_flat_system_v1.py
evidence/wh10_flat_system_v1.result.json'. START 2026-10-19T04:29:28-0700, PID 81837 = PGID 81837, EXIT 0, END 04:29:29
(0.64 s in-run); single process; lane tmp/ empty. Output (0444) evidence/wh10_flat_system_v1.result.json
81b5c12b71062ec8b63461f2b1e98f07989f78a1aa3aab04d0c33b48887deaeb. One implementation.

Results (exact): D_u D_v = tau^(-<u,v>) D_(u+v) and D_u^* = D_(-u) for all 625 pairs; c(1) = c(4) = -phi, c(2) = c(3) = 1/phi;
at 40 random Hermitian coefficient sets all 25 claimed components equal the exact components of S^2 - S/5 - 6I/25, and
U1-U6 equal phi times the corresponding components; the 30 MUB-pair planes of lines 1, 3, 4 are rank-2 projectors in
the normal form and satisfy the whole system; a perturbed coefficient set violates it; the one-block lemma's ratio sets
cover Z_5^* for every pair and both triples (WH_10 {inf, 0, 2} and W8 {inf, 0, 4}); the three equations printed in
evidence/w8-decision-v1.md section 5 coincide exactly with phi times the components at w = (0, s), (s, 0), (s, 4s).
Context: the WH_10 route was stopped right after this run because of a prior published obstruction
(evidence/wh10-prior-art-addendum-v1.md); this receipt documents correctness of the written system only.
