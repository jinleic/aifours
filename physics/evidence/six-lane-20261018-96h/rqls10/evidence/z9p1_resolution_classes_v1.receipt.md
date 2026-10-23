# Receipt: z9p1_resolution_classes_v1 (initial-scope stdlib EXACT probe)

Recorded 2026-10-19T02:29:00-0700 (from /bin/date 02:27:18 + writing). Owner ContinueRQLS10b.
Source code/z9p1_resolution_classes_v1.py sha256 f2dcfead7ca8bd5efdecc66029b8d740411c673055e0ac22fa448c65ce247186 (0444, frozen before
run; z9_all_betas, z9_canon, z9_config are AST-identical to code/rqls_assay_v9.py e9079686...64db). Launch record
evidence/z9p1_resolution_classes_v1.launch.json sha256 9e11e2332d9bb92fcf51dbdfa11dc1ab2722e718c1d8187a6d63eabd972f601d.
Input evidence/z9p1_classical_search_v1.result.json sha256 4199ee995b4656c306ca1013eccb9a164a6c1c72c9e4101a783f4958d93e7c6b.
Command (cwd lane, timeout 120): /bin/bash -c '...; exec /usr/bin/env -i TMPDIR=<lane>/tmp /opt/homebrew/bin/python3.14 -I -B
code/z9p1_resolution_classes_v1.py evidence/z9p1_classical_search_v1.result.json evidence/z9p1_resolution_classes_v1.result.json'.
START/END 2026-10-19T02:27:11-0700; PID 51627 = PGID 51627; EXIT 0; 0.18 s; single process; lane tmp/ empty.
Output (0444) evidence/z9p1_resolution_classes_v1.result.json sha256 23ebb08a9418427198803282abc694242e8fcc19e597a91a9fcef082338a93f8.

Result (exact integer enumeration, one implementation): 2,025 betas on D_fin = {1..8} with beta and beta - id
injective (every one gives a Latin Z_9+1 square, re-checked on the 10x10 array: 0 bad); 24 classes under symbol
translation, multipliers u in Z_9^* and transposition (class sizes 9 x1, 18 x2, 36 x1, 54 x4, 108 x16); the 40 known
classical resolutions (20 pairs x 2 roles, column-translated to D_inf = {0}) fall into 12 of the 24 classes.
