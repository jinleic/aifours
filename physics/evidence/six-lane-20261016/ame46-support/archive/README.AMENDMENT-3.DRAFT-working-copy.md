# README amendment 3 (frozen): proof-free v5 exploration of the s = 49 layer

Lane `physics/evidence/six-lane-20261016/ame46-support/`. Host clock PDT, 2026-10-17. Written once, before any run it
covers. It amends README §0 and amendments 1 and 2, all of which are unchanged.

**Authority.** Parent decision (a), 16:1x: after the (24,0) proof run, freeze a new amendment and run proof-free v5
exploration of the s = 49 layer. Proof mode for s = 49 needs a separate parent GO. s = 50 is not started.

## 1. Exact case list and derivation
s = 49 means e = t − 23. The pairs are (t, t − 23) for t = 23..36. Excluded in writing:
- t ≥ 31 (L42, L46-13, L46-16);
- t = 29 (L48 Lemma 17);
- (24,1), since e = 1 is impossible (L42-7);
- (23,0), since e = 0 with t odd is impossible (L42 corollary).

The remaining cases, run in this order. Live profiles are those left after Lemma 17.

| order | (t, e) | h | profiles (live) | max product space |
|---|---|---|---|---|
| 1 | (30,7) | 6 | 2 (1) | 81 |
| 2 | (28,5) | 8 | 7 (5) | 256 |
| 3 | (27,4) | 9 | 6 (3) | 256 |
| 4 | (26,3) | 10 | 25 (24) | 625 |
| 5 | (25,2) | 11 | 22 (21) | 625 |

All have e ≥ 2, so W (Lemma 20, e = 0 only) is not used.

## 2. Engine, command, caps
- **Engine:** v5 `code/large_t_joint5.py` (e57067c247d3e5c6ca8e7f28035a6d9ec45b1a77238fe8ccd5046eff7f0033f8), specified
  in `review/ENGINE_V5.r1.md` (5393238f0aee2f37bf1641e644b0555691320ffbd4fccfdb65838b135e06bf0a).
- **Command per case:** `code/run_chunk5.sh T E 10800 --joint`, exploration only, no `--proof`. Wrapper:
  3231d8e754a8233510d80c0d3dc16f7368ea6679719310d8b95455646f548926.
- **Caps** (v5 defaults):
  - RSS 6 GiB;
  - exact-byte disk budget min(512 MiB, 10 GiB − 256 MiB − lane bytes); exploration writes only the report;
  - at most 5000 solutions per profile;
  - CaDiCaL `-t 1200`;
  - free-space floor 12e9 B, both in the engine and in `disk_floor_watch.sh`;
  - 3 h wall limit per chunk, SIGTERM only.
- **Concurrency:** one case at a time, at most 2 busy processes, and only after the (24,0) proof chunk has ended.

## 3. Stop rules and claims
- Any trip, cap, wall limit, assertion failure or solver status other than 10 or 20 makes the whole case UNKNOWN. No
  rerun with raised caps without a parent GO.
- `EXCLUDED-EXPLORATION` is not a certificate. An s ≥ 50 bound needs proof-mode runs after a parent GO.
- For e > 0, a candidate (an N passing components, moduli and closed-2×2 phase consistency) is OPEN. Phase consistency
  is only necessary at e > 0, and no reconstruction is attempted there. Its N and T are stored and the parent is told.
- Outputs: `evidence/large_t_joint5_t<t>_e<e>_explore.json`, `explore/large_t_joint5/run_t<t>_e<e>_explore.stdout.txt`
  and `evidence/chunks.log`.
