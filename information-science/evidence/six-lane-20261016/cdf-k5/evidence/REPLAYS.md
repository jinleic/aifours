# Certificate provenance and byte replays (321, 681, 621; 501 is in `evidence/v501/REPLAY.md`)

All binaries: `cc -O3 -march=native` (Apple clang 17.0.0, arm64, macOS). Searches are deterministic given the seed
(splitmix64 RNG; wall-clock only checked between attempts/configurations). Host-clock times from file mtimes.

| v | certificate (SHA-256) | producer and exact command | inputs | found | byte replay |
|---|---|---|---|---|---|
| 321 | `certificates/cdf_321.txt` 0304c61b...034b | `code/cdf_hyb3p.c` (45c5119f...), bin 2d33c441...; `./bin/cdf_hyb3p 321 1 1700 <prefix> 1 20000 50000000 evidence/gpairs/gpairs_p107_k30.txt` | `gpairs_p107_k30.txt` ec2a8040... from `./bin/gpairs 107 1000000 <file> 30` (`code/gpairs.c` e880fbb3..., bin 15d9a418...) | 23:15:55, 1.57 s | identical (`evidence/v321/replay/`) |
| 681 | `certificates/cdf_681.txt` 16af7539...f7b7 | same binary; `./bin/cdf_hyb3p 681 1 1700 <prefix> 1 20000 50000000 evidence/gpairs/gpairs_p227_k5.txt` | `gpairs_p227_k5.txt` 357cf16e... from `./bin/gpairs 227 2000000 <file> 5` (164 s, peak RSS 783 MB) | 23:23:23, 82.4 s | identical at 23:25:51 (`evidence/v681/replay/`) |
| 621 | `certificates/cdf_621.txt` 257d85f2...05f5 | `code/cdf_mq2.c` (a02dff36...), bin 79115d33... (copy `bin/cdf_mq2.pinned621`); `./bin/cdf_mq2 621 27 1 1700 <prefix> 30 3 50000000` | none | 23:32:11, 57.4 s | identical at 23:33:28 (`evidence/v621/replay/`) |

Alternate witnesses (lane verifier ACCEPT): 321 seeds 2, 3 (`evidence/v321/cdf_321_alt_seed{2,3}.txt`), 681 seed 2
(`evidence/v681/cdf_681_alt_seed2.txt`, f21fd866...).

Group action (`code/group_action.py`, output `evidence/group-action-v1.txt`): no found family is closed under its
structural unit in the Hetman-Baicheva-Topalova Definition 1.2 sense. 501/166: 20 blocks to themselves, 5 to their
negatives. 621/298: 27 blocks to translates of base blocks (5 themselves, 11 swapped pairs), 4 to their own negatives.
321/106 and 681/226: two general blocks are not mapped into the family at all (no multiplier exists for these v).

| 801 | `certificates/cdf_801.txt` 0a75e7d9...186c | frozen `code/cdf_mq4.c` (68028470...), bin b1f56985...; `./bin/cdf_mq4 801 9 21 1700 <prefix> 30 0 30000000 5000000 1` | none | 23:41:08, 275.1 s | identical at 23:46:22 (original-run source not preserved; see `evidence/v801/PROVENANCE.md`) |
| 901 | `certificates/cdf_901.txt` 06bd6ae8...56d3 | same frozen binary (run launched after the freeze); `./bin/cdf_mq4 901 17 41 1700 <prefix> 30 -11 30000000 5000000 0` | none | 23:57:41, 940.2 s | identical at 2026-10-17 00:14:19 (838.6 s; `evidence/v901/replay/`) |
