# README amendment 2 (frozen): proof-free (24,0) exploration with engine v4

Lane `physics/evidence/six-lane-20261016/ame46-support/`. Host clock PDT, 2026-10-17. Written once, before the run it
covers. It amends README §0 and `README.AMENDMENT-1.md`; both are unchanged.

## 1. Why
Under amendment 1, (24,0) was stopped with SIGTERM and is UNKNOWN (14:19:14). In profile 0, {6,6}{2⁶}³, the v3
lex-leader enumeration yielded 980 solutions without finishing.
- Exploration probes, 14:20–15:30, are logged in `evidence/LOG.md`.
- The joint officer model (J) plus the e = 0 doubled-triangle clauses (W, Lemma 20) enumerated that profile completely
  in 418 s: 42 solutions, all excluded by phase certificates.
- Most other (24,0) profiles finished in seconds with J alone.

## 2. Exact run
- **Case:** (24,0) only, all 158 profiles in `large_t_e0.profiles(12)` order.
- **Engine:** v4 `code/large_t_joint4.py` (42d6e510582d8f5e46ed8b348c1fb57ed8d28e6a0fb4e1f77ac54242345426a9),
  specified in `review/ENGINE_V4.r1.md` (fd1d47f2c6361e4d467369bb914e16b587b27bb5d9e3d660d38400b74b258c12).
- **Command:** `code/run_chunk4.sh 24 0 10800 --joint --triangles`, exploration only, no `--proof`.
  `run_chunk4.sh` (e2fb3296b301e8e660878e9e37fc862b0f9b9a6ddcca786173dea9fa7290d2d2) is `run_chunk.sh` with the engine
  path replaced. It uses the same free-space floor
  watchdog (12,000,000,000 B), a 3 h wall limit and SIGTERM-only stops.
- **Caps** (v4 defaults):
  - RSS 6 GiB;
  - exact-byte disk budget min(512 MiB, 10 GiB − 256 MiB − lane bytes); exploration writes only the report;
  - at most 5000 solutions per profile;
  - CaDiCaL `-t 1200` per call;
  - product space ≤ 1296, estimated CNF memory ≤ 2 GiB.
- **CPU:** one engine process with one solver child, so at most 2 busy processes.

## 3. Stop rules and claims
- Any trip, cap, wall limit or solver status other than 10 or 20 makes the case UNKNOWN. Partial enumerations are not
  used.
- `EXCLUDED-EXPLORATION` is not a certificate. A bound s ≥ 49 needs proof-mode runs of (24,0), (26,2), (27,3),
  (28,4) and (30,6) after a fresh parent go, with resource estimates; (29,5) is excluded by Lemma 17.
- A CANDIDATE (an N passing components, moduli and phase in the joint model) gets exact reconstruction, its N, T and
  θ are preserved, and the parent is told immediately. Nothing is claimed before full raw verification.
- Outputs: `evidence/large_t_joint4_t24_e0_explore.json`, `explore/large_t_joint4/run_t24_e0_explore.stdout.txt` and
  `evidence/chunks.log`.
