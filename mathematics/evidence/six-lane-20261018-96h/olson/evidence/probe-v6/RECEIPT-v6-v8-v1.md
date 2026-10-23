# RECEIPT: probes v6, v7, v8 (BAL-forall falsification / necessity / sharpness aids), v1

Owner ContinueOlson.  Written after /bin/date 2026-10-19T01:11:31-0700.  All three are aids, never premises.  Launched through
code/lane_launcher_v2.py (c10c28555bb6829206e2b6778948085155662844061b195c609950f48780aef4): exclusive pre.json with PID,
PGID, argv/source hashes written before the stdin gate byte; settlement post.json after reap.  Plans sent to the parent
before each launch.  Self-budgeted; no external timeouts; stdout only.

| probe | script sha256 | pid | rc | wall s | pre / post / stdout sha256 |
|---|---|---|---|---|---|
| v6 falsification | c24471e0b5b2c22541763ecac7bdd9153dc1963c76e6805990068b2fe4fcc8da | 28203 | 0 | 213.9 | 3435fdeffcfa7a37eba711077fa25ff707653717a90e13d8136f85d1f10b8b40 / a77126d85e7d72340d9a5b203891afeedc7ea76f72c34659b885c23cbe3e9f03 / aaa08e913d0e8c61302bd87fd7bdb15ec0c5de25ef3a8524383f024085e25e54 |
| v7 examples | 746ba804453c7b8c777b95fdd92eecd8d50cecbe958cf3ea918b2daaae340201 | 28669 | 0 | 0.027 | 7ee8ca4da91c461289c4e89d2b5ac33ec335d1b6e0107110aa5196c347683f91 / 2dc4b8ca9f5bcf88cf8ef4491c350a9917ca90f2582a5955291951dad122715b / 5fdabe2b2d080c561a951b93fd4b9cc1a51d148d1c0349bf8546ac345dddea71 |
| v8 sharpness | 7325a7228bf40ff22e4b54a7c4b5edf8dc7b6e090c7998c68fa16385deb4864f | 28709 | 0 | 140.0 | b2fb1d1e9aa8f3565f88bba3cbf9a5084ad8553f87577499799517358e90f686 / a9cc9afb7eb371843d2e4a8e83b892a40344136c9d94a169f65c3d6b234b64ef / 2382b49f1d0316735e07354ba6de981ce1808689fce4ab812a57b3574f93838f |

Results.
- v6 Part A (p = 7, EXHAUSTIVE over all multisets of odd elements of C_14 of size R = 10..17, 334,664 multisets, all
  complete; tested = those with L >= p + 1): 0 unbalanced (Z, g) with L >= 2t + 1; 0 ZSTRUCT-shape violations; 0
  unbalanced with L = 2t.  v6 Part B (random structured, p = 11/13/17/19; 260,844/125,628/48,709/26,066 sequences tested):
  0 unbalanced with L >= 2t + 1; 0 ZSTRUCT violations; 0 with L = 2t; 14,592/7,617/3,454/1,955 unbalanced with L < 2t.
- v7: the v6 'L < 2t' class is DEGENERATE (all three extracted witnesses have 2t > 2p and S(N) = n+ - 2p, e.g. p = 11,
  Y = g^42 (-g), Z = g^23 (-g)); outside (S') (there t <= kappa < p and the proof's j >= 1).  Not a positive control for
  the hypothesis L >= 2t + 1 (correction sent to the parent).
- v8 (directed search inside t <= p - 1, p + 1 <= L <= 2t, forced S(N) = n+ + 2p, exact DP for 'Z longest'): p = 11:
  1,085,943 feasible constructions, p = 13: 840,265; NO construction made Z a longest zero-sum.  Sharpness of
  L >= 2t + 1 inside t < p is therefore not observed (suggests, without proof, that balance may hold more widely).
