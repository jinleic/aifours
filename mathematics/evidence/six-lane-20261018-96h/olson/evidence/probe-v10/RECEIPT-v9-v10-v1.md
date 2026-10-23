# RECEIPT: probes v9 (T-MAX route) and v10 (Lemma FB falsification), v1

Owner ContinueOlson.  Written after /bin/date 2026-10-19T02:03:28-0700.  Aids only, never premises.  Launched through code/lane_launcher_v2.py
(c10c28555bb6829206e2b6778948085155662844061b195c609950f48780aef4): exclusive pre.json (PID, PGID, argv/source hashes)
written before the stdin gate byte; settlement post.json after reap.  Launch plans sent to the parent before each launch.
Self-budgeted; no external timeouts; stdout only.

| probe | script sha256 | pid | rc | wall s | pre / post / stdout sha256 |
|---|---|---|---|---|---|
| v9 T-MAX route | 6f85d56dd31c9b4379f09fe4ca828e5de8347b430f9070997bac0033f8f16ba6 | 39058 | 0 | 265.1 | 91f0a9587733e105e6ef499ab986ded25a53a58eaaa35c4e75d4bc4dbe60361b / 779bec0f2a24d2baeff28e8eab82d16a8f6678003b3ae488beb26a85af4833e2 / 3790fc11537932417680835cecb22380770f2cc1dd0edf9c27ca8a9d4d2c85a0 |
| v10 FB falsification | 4ac48bf1234396be1d4f9a88b9aba8e25bb89b9de106c3a6fd77c0ff29ef9c2a | 43834 | 0 | 280.0 | cea67fe23c7b15381fd614d949c50da1c12d5b31fb828a02310f80a6bc9f886a / 7e73c9ef4f788784486af06e71a91c2050652a0382f83f9715a927a0c3bf235f / 37e546f21a27062be8a7213ce745af07f2da8577b595d19600767a51de31fce9 |

v9 (scope evidence/TMAX-scope-v1.md 858d9a3e...568f).  p = 7 cells (6,4), (6,5): exhaustive over all 74,613 / 134,596
multisets; (T) contains 2 / 1 sequences up to automorphism, all with ROUTE true; the normalized (ZSTRUCT, g = 1) enumerator in
full mode returned exactly the same canonical sets (control).  p = 11 (all 7 high cells), p = 13 (all 10 high cells), p = 17
(9 of 19 high cells complete, (15,12) partial, 9 skipped by budget): every normalized form not already routed by c = 1
(i.e. every form with S(N) >= n+ + 2p, or balanced with e' + 2n+ >= 2p) was DP-checked: none had its Z longest.  So 0
ROUTE-false sequences and 0 unbalanced longest Z in (T) in the completed cells.
v10 (Lemma FB, evidence/proof-FB-v1.md 339dcadc...cc6b).  Part A, p = 7, exhaustive over all multisets of size R = 10..18
(469,260 multisets, all complete; every longest Z with 2t < 2p and L >= p + 1, every index-<1 g): 0 FB violations
(S(N) > slack), 0 ZSTRUCT violations, 0 unbalanced, 0 with W + n+ > 2p - 1.  Part B (random ZSTRUCT-shaped constructions
with S(N) = n+ mod 2p and S(N) >= 2p - W, p = 11/13/17/19/23: 476,967/411,971/297,192/255,565/188,346 built): 0 had Z longest.
Positive control (S(N) = n+ <= slack): 171,990/122,379/66,588/51,667/32,737 built, ALL had Z longest.  The control is
consistent with a trivial converse (if W + n+ <= 2p - 1 and S(N) = n+, every zero-sum X N0 has A(X) = S(N0) and length
<= S(N0) + |N0| <= 2t), so the FB shape characterizes longest zero-sums with complement >= p + 1 (written remark, not a premise).
