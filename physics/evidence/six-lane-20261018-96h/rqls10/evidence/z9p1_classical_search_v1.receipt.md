# Receipt: z9p1_classical_search_v1 (initial-scope stdlib probe)

Recorded 2026-10-19T00:58:44-0700. Launch record evidence/z9p1_classical_search_v1.launch.json sha256
2dc15023fb081016a4833a537e1dd5213633a788e61753fccb10c48515a550d8; source code/z9p1_classical_search_v1.py sha256
8f15576d08f343ef49608d42283dfe1852b648b4ec91cdf2c78e84102edfd96d (frozen before run).
Command: env -i TMPDIR=<lane>/tmp /opt/homebrew/bin/python3.14 -I -B code/z9p1_classical_search_v1.py
evidence/z9p1_classical_search_v1.result.json; tool timeout 0; START/END 2026-10-19T00:58:37-0700; PID/PGID 27776; EXIT=0;
0.02 s; stop MAX_HITS after 24,978 (beta_A, beta_B) pairs. Settled (single process, output closed, lane tmp/ empty).
Output (frozen 0444) sha256 4199ee995b4656c306ca1013eccb9a164a6c1c72c9e4101a783f4958d93e7c6b.

Result (exact): 20 pairs of orthogonal Latin squares of order 10, both invariant under a Z_9 automorphism with one
fixed row/column/symbol (Z_9 + 1), each re-checked on the full 10x10 arrays (verified_full true for all 20). These are
classical 1-RQLS(10) in the Z_9 + 1 ansatz (with U = shift (+) (1), whose eigen-multiplicities (2,1,...,1) are already
the Lemma-6 form), i.e. exact calibration anchors for any future Z_9 + 1 search. They carry no information about
maximal cardinality.
