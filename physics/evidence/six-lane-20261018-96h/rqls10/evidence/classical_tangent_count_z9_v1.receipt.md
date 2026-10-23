# Receipt: classical_tangent_count_z9_v1 (initial-scope stdlib probe)

Recorded 2026-10-19T00:59:22-0700. Launch record evidence/classical_tangent_count_z9_v1.launch.json sha256
47703d71048d9a64226141bd538d0b2c81f98bb13b45f9a70111db0653f1f744; source sha256 22e8d017212f113a878047a923de3200055be1a1598d609a7ef5d514a0691bb6.
Command: env -i TMPDIR=<lane>/tmp python3.14 -I -B code/classical_tangent_count_z9_v1.py evidence/z9p1_classical_search_v1.result.json
evidence/classical_tangent_count_z9_v1.result.json; tool timeout 0; START/END 2026-10-19T00:59:14-0700; PID/PGID 27848; EXIT 0;
0.065 s. Settled. Output (0444) sha256 ee6f70c1c1dc613edaac6a79614013027b8ff4fe6a25b14a03018e2bfdaa5cb7.

Result (exact combinatorics; theory evidence/classical-tangent-theory-v1.md): all 40 cases (20 classical
Z_9 + 1 pairs x 2 roles): every pair graph G_(a,s) is connected, unsymmetric excess 0 and Z_9 + 1 symmetric excess
2*5 - 10 = 0 ({'(0, 0)': 40}). Hence each of these classical 1-RQLS(10) is locally rigid
(isolated modulo U(10) and cell phases) in the FULL unsymmetric solution set: no non-classical 1-RQLS(10) of any
cardinality lies near them. Local statement about these 40 points only.
