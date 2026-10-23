# v = 801 provenance (written 2026-10-16 23:43 PDT)

- Certificate: `certificates/cdf_801.txt`, SHA-256 `0a75e7d93920415f04a51967bd5a4033765f040f3b19af9f603d16b6d616186c`
  (40 blocks), copied from `runs/v801/mq4_t30_g0_lc_s21.sol` (file mtime 2026-10-16 23:41:08 PDT).
- Original run: `./bin/cdf_mq4 801 9 21 1700 runs/v801/mq4_t30_g0_lc_s21 30 0 30000000 5000000 1`, started
  2026-10-16 23:36:33 PDT; FOUND at attempt 8 after 275.12 s (log `runs/v801/mq4_t30_g0_lc_s21.log`).
- Source caveat: the binary used by the original run was compiled at about 23:36 from a version of
  `code/cdf_mq4.c` that is NOT preserved. At 23:40:29 the file was edited (a template-dump branch executed only when
  g = -999 was inserted after the stage-S block-count check) and recompiled. The original run's source bytes are
  therefore not known; no claim is made about them.
- Frozen current version (all later work forks to new files):
  `code/cdf_mq4.c` = `evidence/v801/cdf_mq4.frozen-2026-10-16.c`, SHA-256
  `68028470d65cbfb450c84a6ba354dd7bc68c3a9d9de919cc91f92adb34e1da16`; binary `bin/cdf_mq4` =
  `evidence/v801/cdf_mq4.frozen-2026-10-16.bin`, SHA-256 `b1f569853f0331bc6bf30202bfbfaa5101cb47affb6e5e5b0a9c765d412ab531`
  (`cc -O3 -march=native`, Apple clang 17.0.0, arm64).
- Reproducibility evidence (new, from the frozen version): `./bin/cdf_mq4 801 9 21 1700
  evidence/v801/replay/replay_s21 30 0 30000000 5000000 1`, result recorded below when it finishes. A byte-identical
  output establishes reproducibility from the frozen source; it does not restore the lost original snapshot.
- Validity of the certificate does not depend on any of this (lane verifier ACCEPT, `evidence/v801/verify_cdf_801.json`).
- Structure: Z_801 = Z_9 x Z_89, unit 622 = (1 mod 9, -1 mod 89). 16 blocks {(0,0),(a1,+-y1),(a2,+-y2)}, 4 blocks
  {(0,0),(0,f1),(0,f2),(a,y),(-a,y)}, 10 pairs {B, 622*B} from an exact cover over 540236 pair rows. Group action
  (`code/group_action.py`): 36 blocks to translates of base blocks (16 themselves, 10 swapped pairs), 4 to their own
  negatives: closed under 622 up to translation and negation only, not a Definition 1.2 multiplier.
- Replay result: 2026-10-16 23:46:22 PDT, FOUND at attempt 8 after 275.58 s with the same trajectory (same rowsF
  per attempt as the original log), output `evidence/v801/replay/replay_s21.sol` byte-identical (`cmp`) to
  `certificates/cdf_801.txt`. Reproducible from the frozen source; the original snapshot remains unknown.
