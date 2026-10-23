# c2/invstar: INV*(p), rigid-rotation half (b) -- frozen target

Owner OlsonParity2 (Main's request (2), 18:2x PDT; ownership checked with OlsonRunCount5: nobody owns INV*).
Directory created with exist_ok=False; this README frozen at host clock 2026-10-17T18:33:42-0700 before any computation here.
Labels: [W] written proof (unreviewed), [F] exact computation (aid only), [W+F] theorem with finitely verified
hypotheses, [I] inference.  Limits: <= 1 busy process, native CPU limits (ulimit), no kill signals, files mode x.

## 1. Frozen target

INV*b-rig(p): every word w of length 4p-2 over D_(2p) whose rotation letters all lie in one set {rho_x, rho_-x}, x != 0,
and which has no identity 2p-subword, has every maximal cyclic reflection run constant.
(Half (b) of INV*(p) restricted to rigid rotations; c2/obligations-after-PAR.md Sec. 4.)

## 2. Frozen representation (Lemma GR0, to be written with proof in proof-GR0.md before use)

Normalise x = 1.  Cut every maximal reflection run at each change of letter into maximal constant blocks; w is a cyclic
alternation R_1 S_1 ... R_k S_k of rotation runs R_i (a_i rho_1, b_i rho_-1, possibly EMPTY: a_i = b_i = 0) and
constant blocks S_i = sigma_(y_i)^(l_i), l_i >= 1, with y_(i-1) != y_i whenever R_i is empty.  Claim (GR0): Lemma GR
(../../../../proof-GR.md Sec. 2) and Lemma WAS hold verbatim for this decomposition.  Then INV*b-rig(p) says: no avoider of
length 4p-2 has an empty rotation run (theta_i = y_(i-1) - y_i != 0 at every empty run i).

## 3. Frozen plan

P1 write Lemma GR0 (+ the pair-removal and segment-merge reductions that stay valid) with proofs; P2 [F] check GR0 against
the raw ordered-product DP (../../../../code/was_verify.py dp_has) on random generalised words with empty runs; P3 [F] exact
search for generalised avoiders with an empty run (C++ WAS DFS over theta, every pattern P, value-independent filters
proved for every avoider): controls p = 5, N = 18 (must find none: all 3,730 D10 avoiders are RGR, olson/README.md 5.1),
p = 5, N = 17 (positive control: report what exists, each candidate re-verified by raw DP), mutation (shrunken windows ->
spurious candidates rejected by raw DP); then p = 7, N = 26 for k up to the feasible bound (chunks <= 30 min); any
candidate avoider is reported only after raw-DP verification of the explicit word.  P4 written analysis of what the
search shows (no all-p claim without a proof).

## Progress / closeout (2026-10-17T19:35:15-0700)

Overdue log: the first Main checkpoint gap (18:31 to 19:07) exceeded 30 minutes; no earlier README progress
entry was written.  Written results and exact scope are now frozen in results.md; proof-GR0-r1.md and
proof-sharpness.md are the current [W] files.  p5 controls passed; p7 NF k<=9 found no avoider, k>=10 open;
all new native jobs finished, no busy processes.  No edits to the four files under parent hostile review.
