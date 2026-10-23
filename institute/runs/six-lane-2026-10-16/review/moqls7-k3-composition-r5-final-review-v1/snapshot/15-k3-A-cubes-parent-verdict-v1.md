# MOQLS(7) K3 encoder-A cube replay disposition

Parent at 2026-10-18T02:43:24-07:00: **two exact encoder-A CNFs are accepted UNSAT**, based on fresh native parent replays. This does not meet the full A+B K3 standard, accept encoder-B cubes, settle C311, or determine M(7).

| Case | Exact CNF SHA256 | Parent receipt SHA256 | Solver/checker |
|---|---|---|---|
|A/C321|d598507d84a8d7595b30a100d528dca08bc0ce1aa71978583f09aac188298388|cbd7f02f5b2850cae2814c641f283633abf5405b87035bac3043a1541502efa8|20 /0 /exact s VERIFIED|
|A/C411|2b92f5b15cd641e4a07ecec241b7957deac972aa3c7333056ff3e739e46addf2|308e255ee1ec4c687f1b79db4157a44c3c3ae9fc1b8cffa24b976f8690707442|20 /0 /exact s VERIFIED|

Evidence: [RESULT](moqls7-k3-cube-parent-replay-v1/RESULT.json), `8b6f57b7cc9f14071849d916fcfa5001ed7dac43e6d0b5d2673adefb1431ca9b`; use [REPORT.r2](moqls7-k3-cube-parent-replay-v1/REPORT.r2.md), not its retained abbreviation-typo predecessor. The parent independently re-hashed every native receipt, pre-execution/launch binding and raw solver/checker log, checked exact bytes after removing only CR, all native return codes, full successful CNF pipe writes, regenerated/expected hash equality and absence of safety stops ([audit](moqls7-k3-A-parent-receipt-audit-v1.json), `97c1e0e4dde7b188e447f40e76cb6935ebb9f8f7060a32ff9e96ebef8dbfc234`). This audit adds no new solver run.

Each replay used pinned encoder-A/cube functions in a separate composition driver, rather than the producer's file-writing wrapper. Output equaled the exact pinned input SHA. Parent drat-trim is `a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37`; CaDiCaL is the same producer binary `601c9fa8…d1fa`, not an independent solver. Script hashes were observed before execution, binaries at spawn and after; no backfilled script pin. Three transport self-checks passed, with SAT and wrong-CNF proof rejection; previous checker controls are reused, not rerun.

A/C321 took2137.989s, A/C4113479.385s; peak sampled own RSS1,360,969,728 /1,643,446,272B. Native limits5400/7200 differ from producer3600/3600; both actual runs completed inside3h. Regeneration used isolated Python3.9.6. No CNF/proof copy or retained proof; proof bytes were not hashed, so matching producer/checker statistics do not prove proof-byte identity. CNF feeds were pre-hashed immutable buffers with successful complete writes, not separately hashed write streams. Desk deviations remain explicit in [deviations](moqls7-k3-cube-parent-replay-v1/deviations-v1.json).

The [A+B decision](moqls7-amendment4-parent-disposition-v1.md) still requires independently certified/replayed B/C321 and B/C411 before G1/G2 are accepted for the full K3 composition, plus A/B C311+cuts and the final bridge. The formula facts here supply only the A side. No new gate.
