# README amendment 1 (frozen): proof-free guarded exploration toward s ≥ 49

Lane `physics/evidence/six-lane-20261016/ame46-support/`. Host clock PDT, 2026-10-17. Written once, before any run it
covers. It amends README §0; the original §0 and its archived byte copy are unchanged.

**Authority.** Parent IRC, after the LOWER48 r1 freeze: v3 may be frozen and smoke-tested; after that, and after this
amendment, proof-free guarded exploration of the additional s ≥ 49 cases is allowed. Proof mode on these cases needs
a fresh parent go after resource estimates.

## 1. Exact case list and its derivation

s ≤ 48 forces t ≥ 24 and e ≤ t − 24 (s = 72 − t + e, e ≥ 0). The following are already excluded:
- t ≥ 31, by LOWER42 r2, L46-13 and L46-16;
- every e = 1, by L42-7;
- e = 0 with t odd, by the LOWER42 r2 corollary;
- t = 29, by Lemma 17 of `review/SUPPORT_LOWER48.r1.md`;
- all of s ≤ 47, by LOWER48 r1.

The remaining cases, run in this order:

| order | (t, e) | profiles | excluded by Lemma 17 | max product space | max est. CNF memory |
|---|---|---|---|---|---|
| 1 | (30, 6) | 2 | 1 | 81 | 4.4 MiB |
| 2 | (29, 5) | 1 | 1 (redundant case, run as a check) | 81 | 4.4 MiB |
| 3 | (28, 4) | 7 | 2 | 256 | 24.8 MiB |
| 4 | (27, 3) | 6 | 3 | 256 | 24.8 MiB |
| 5 | (26, 2) | 25 | 1 | 625 | 115.7 MiB |
| 6 | (24, 0) | 158 | 5 | 1296 | 445.1 MiB |

No other case is run under this amendment.

## 2. Engine, command and caps

- **Engine v3:** `code/large_t_lex3.py`, 139681a2c8457c5b9b59915e5e9e87287b525b48c1c29a93606b78622c3737e0. Its
  specification and smoke receipt are `review/ENGINE_V3.r1.md`,
  fd7c7447d7140d934d3311a27e2e368dd1167334cf370bf7e8b3ddac1bd74449.
  - That file repeats one bullet in §4, lines 75–76. The duplicate is cosmetic.
- **Command per case:** `code/run_chunk.sh T E 10800 --officer-prefilter`. There is no `--proof`, so the run is
  exploration only.
  - `run_chunk.sh` (25eb702f444bc60537cc77aa36aa0e3f94b9c6a7854fc94383ba884066c11161) attaches
    `code/disk_floor_watch.sh` (159f2af4fe080bf1695f51598485c7596c3bc80ebbca6c6607859dbea120c8de) with a
    12,000,000,000 B free-space floor.
  - It enforces a 3 h wall limit per chunk. At the limit the engine gets SIGTERM with a bounded 30 s wait and no
    SIGKILL, it writes no report, and the case is UNKNOWN.
  - Controls at 13:50:19–13:50:29: a 0 s limit gave rc 143 and no report; (30,0) under a 600 s limit gave
    EXCLUDED-EXPLORATION.
- **Caps** (v3 defaults, unchanged):
  - RSS watchdog 6 GiB on the engine plus its live child;
  - exact-byte disk budget min(512 MiB, 10 GiB − 256 MiB − lane bytes). Exploration stores only the report;
  - free-space floor 12,000,000,000 B, checked at start and every second;
  - at most 5000 solutions per profile;
  - CaDiCaL `-t 600` per call;
  - pre-bounds product space ≤ 1296 and estimated CNF memory ≤ 2 GiB.
- **CPU:** cases run sequentially. At most two busy processes: the solver, plus the engine's own Python work between
  calls.

## 3. Stop rules and claims

- Any guard trip, cap hit, solver status other than 10 or 20, or wall limit makes the whole case UNKNOWN. A partial
  enumeration is never used.
- A case whose outcome is `EXCLUDED-EXPLORATION` is NOT a certificate, and no bound is claimed from it. A bound needs
  a later proof-mode run, after a fresh parent go and its own receipt.
- `NOT EXCLUDED (open candidates)` would be reported with the open N lists. It is not evidence of existence: the
  checks are necessary conditions only.
- Checkpoints go to README §1 at most every 30 minutes. Outputs: `evidence/large_t_lex3_t<t>_e<e>_explore.json`,
  `explore/large_t_lex3/run_t<t>_e<e>_explore.stdout.txt` and `evidence/chunks.log`.
