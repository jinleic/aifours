# v = 501: certificate provenance and byte replay

- Certificate: `certificates/cdf_501.txt`, SHA-256 `517e02fa330269323f70de11e66ac89aac97da106775efb7dca1d674fd7aab74`
  (25 base blocks). Alternate witness: `evidence/v501/cdf_501_alt_seed2.txt`, SHA-256
  `fd1f9a6559e7ddf2534441a9672670b1a93c6db593d31103aa2ba939b68ded0a`. Parent pinned copies of both
  (review/cdf501-parent-inputs-v1/); these lane files are not to be modified.
- Producer: `code/cdf_inv3p.c` (SHA-256 `07f04531d2a7221d429e55cc8f8aff7843f06f6546c88b997dabb91fa983efc5`),
  compiled `cc -O3 -march=native -o bin/cdf_inv3p code/cdf_inv3p.c` (Apple clang 17.0.0, arm64, macOS);
  binary SHA-256 `3ab64aed26220627b7fd5af76c6a5ea57595829a07af8324ea1d2420a11df57a`.
- Original run: `./bin/cdf_inv3p 501 1 1700 runs/v501/inv3p_s1` started 2026-10-16 22:59:43 PDT, FOUND after
  6.99 s (8 random T3 choices, 1509 stage-A covers, 1509 stage-B attempts; T3 = (f1,f2,y) = (71,69,79)).
  Seed 2 (`./bin/cdf_inv3p 501 2 1700 runs/v501/inv3p_s2`) found the alternate after 18.32 s.
- Byte replay: `./bin/cdf_inv3p 501 1 600 evidence/v501/replay/replay_s1` at 2026-10-16 23:03 PDT reproduced
  the certificate byte-for-byte (`cmp` identical; same SHA-256), 6.97 s. The search is deterministic given the
  seed (splitmix64 RNG; the wall-clock limit is only checked between T3 choices).
- Lane verifier: `code/verify_cdf.py` -> ACCEPT (receipt `evidence/v501/verify_cdf_501.json`): 500 ordered
  differences each nonzero residue once; 12525 developed blocks cover all 125250 pairs once; max auto/cross
  correlation 1.
- Structure (for reading the certificate): Z_501 = Z_3 x Z_167 (CRT); unit 166 (= 1 mod 3, = -1 mod 167).
  20 blocks {(0,0),(1,+-y1),(2,+-y2)}, 1 block {(0,0),(0,f1),(0,f2),(1,y),(2,y)}, 4 blocks inside {0} x Z_167.
  The 20 blocks satisfy 166*B = B; the other 5 satisfy 166*B = -B. So every block's difference multiset is
  stable under 166 ("difference-multiset stable under 166"), but the family is NOT closed under 166 as a set of
  blocks up to translation: 166 is not a multiplier in the Hetman-Baicheva-Topalova Definition 1.2 sense (parent
  audit review/cdf501-multiplier-parent-audit.json agrees). Validity does not depend on this structure.
