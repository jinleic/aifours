# Plan v1 addendum 2 — W1 outcome and W1b GO request (2026-10-19T02:21:16-0700)

W1 outcome (cp-001 18b0bdc9…): label encoding sym_dm_cnf_v1 qualified on J1-J4 (n=13) and J6 (exact anchor
reproduction with row 0 fixed); J5 (anchor model from scratch, 1800 s) and J7 (DM35 with the involution fixed, 600 s)
UNKNOWN. Interpretation: the label encoding's variable label permutation + transport clauses are hard for CDCL; no
statement about existence. J8/J9 not launched (authorized-unused).
New engine path: code/orbit_dm_cnf_v1.py (2f9349fc…). Orbit representatives with one-hot coordinates, stabiliser
equalities, slot variables for each coset image and pair-orbit representative, exactly-one per difference value; no label
or transport variables; 0.55-1.5 M clauses (vs 2.1-2.5 M). Soundness controls (stdlib): c6 (anchor, z13 linear
G6/M1, DM35 gauged satisfy all clauses; non-invariant inputs rejected at decomposition) and c7 (G-invariant non-DM
mutants built by code/make_orbit_mutant_v1.py violate exactly the 'dm' family). Models:
evidence/controls-v3/orbit-models-manifest.json (4674a203…).
W1b request (controls/calibration only, no Z39 seven-row target): spec evidence/wave-w1b-spec-v1.json (d5c01b92c6250ff0294eb718ad880a5aed18cabbcf3c822734fb8173ec169b8a).
 A. stdlib CNF writes (orbit encoder) for z13_g6_orb, z13_m1_orb, z39_g6six_orb, z35_m1_orb (largest ~19 MB).
 B. configs via make_sup_configs_v1.py (884268f4…) pinned to the new GO; supervisor/gate/shim unchanged.
 C. K1, K2 (cadical, n=13 orbit controls, 60 s) sequential; then K3 cadical z39_g6six_orb || K4 cadical z35_m1_orb
    (1800 s each); then K5 kissat z35_m1_orb || K6 kissat z39_g6six_orb (1800 s each); every job after its own fresh
    stability_gate_v2 PASS; busy <= 2.
 D. verify_solution_v1.py (1723e8f6…) with the ORBIT encoder path/sha (same decode/evaluate CLI) + checker A.
Decision value: K3/K6 SAT qualifies from-scratch search in the anchor model; K4/K5 SAT is the decisive calibration
(the published DM35 mechanism found from scratch). Only after that would a Z39 seven-row target wave be requested.
