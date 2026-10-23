# Stage A receipt (EXPLORATORY under the parent GO of 13:35 PDT; not a premise until reviewed)

- **Engine:** `code/core7_engine_v1.py`, sha256 e7b4f039ba02c9e8ab5c39579c0d21d3ce4e1d3aba13ec2813129eda67a4288d (frozen 13:34:29 PDT; recorded in `README-addendum-v1.md` before the run).
- **Readiness check:** statvfs free 25,672,237,056 B at 13:35:02 PDT, against the required 12,216,777,216 B.
- **Command (one process at a time, TMPDIR inside the lane, no external timeout):**
  `for U in "X1 120" "MSP45 20" "CORE5 90" "CONTROLS 60"; do set -- $U; /usr/bin/time -l python3 code/core7_engine_v1.py $1 evidence/stageA-$1 $2; done`
- **Wall clock:** 13:35:02 → 13:35:05 PDT (all four runs; total self-budget 290 s).
- **Peak RSS** (`/usr/bin/time -l`): 40.6 MB, 28.5 MB, 32.1 MB, 24.9 MB.
- **Disk:** the minimum free reading inside the runs was 25,672,237,056 B.

## Results

| universe | status | profiles | nodes | closed (T / VFC / K-partial) | leaf orbits (rule) | survivors |
|---|---|---|---|---|---|---|
| X1 = (3r_1,3r_2,6r_3,6r_4,6r_5), r_1, r_2 odd, r's pairwise coprime | COMPLETE | 115 | 8,805 | 7,772 / 2,517 / 5,811 | 157 (PB 130, RPLP 27) | **0** |
| MSP45 = (2r_1,4r_2,4r_3,4r_4), r_1 odd (control: Prop 4.5) | COMPLETE | 135 | 751 | 270 / 384 / 173 | 0 | 0 |
| CORE5 = (4r_1,…,4r_5) (control: Core(5)) | COMPLETE | 71 | 19,568 | 28,766 / 5,361 / 5,080 | 0 | 0 |

**Realisable controls (exact data from explicit permutation groups).** For each family:
- the cosets are disjoint;
- every actual triangle τ satisfies τ_min | τ ≤ τ_max;
- no rule kills it (K, P, VFC at every vertex, RPLP).

| family | α data |
|---|---|
| A5 (6,6,6,10,15) | all α = 1 |
| C2×S4 (4,6,6,6,6) | α_13 = α_14 = α_23 = α_24 = α_34 = 2, others 1 |
| C2×S4 (6,6,6,6,16) | α_01 = 4; α_02 = α_03 = α_12 = α_13 = α_23 = 2; α_04 = α_14 = α_24 = α_34 = 1 |
| C6: six cosets of the trivial subgroup (indices 6,…,6) | all α = 1 |

## Meaning (exploratory; independent replay and reviews pending)

- **X1 has no surviving pattern under rules-k7-v1.** Every K5.3 configuration contains an X1 subfamily: both D-vertices and any three C-vertices, with the coprimality from README P0–P1. So this run, if confirmed, removes class **K5.3**.
- The run only re-certifies the family of Menon's Thm 4.2 inside this lane. Menon's proof via M-S Lemma 4.6 is **not** used.
- The Prop 4.5 and Core(5) controls are fully killed by the same engine, and all realisable families survive.
- Controls are sanity checks only; they do not gate anything.

## Output hashes (files chmod a-w at 13:36:03 PDT)

```
0e226f4441bfb9d3f63fe987aad33a6a40b4522695fa51a36796c3c89c4439d9  stageA-CONTROLS/controls.json
74420f89d2d2a4256b5b578f1c2a01dd2b605f9aca4905db839d008cfd29cac0  stageA-CORE5/leaves.jsonl.gz
de83b28fc3aa4539ae2da90ba4ea22c298acd8016c0b72244f755d3bf3f59ca5  stageA-CORE5/lp_duals.json.gz
1676fb74a3464472c4247272d9c7d71ac442ef749d8401cd738b31b7c1b9f48c  stageA-CORE5/run.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  stageA-CORE5/survivors.json
dcc1b2ffb8e9778fb8c166f52de55722090e54a57ff9345546f5523d9c4d9e5b  stageA-CORE5/vfc_killed.json.gz
74420f89d2d2a4256b5b578f1c2a01dd2b605f9aca4905db839d008cfd29cac0  stageA-MSP45/leaves.jsonl.gz
62aeb75891652b309f0c2a24245be4c98d2bdfce26057fb23fc5e21468ac280d  stageA-MSP45/lp_duals.json.gz
74a00dfb0c35d6595e9a8b0a9fa8a4ad0c374cfe2cf50c7bacee553f0d9c057d  stageA-MSP45/run.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  stageA-MSP45/survivors.json
c8fd962c677f81b60204ab01b9136e236edbe18f296b9d6191f99f48e8f5c29b  stageA-MSP45/vfc_killed.json.gz
5d85710cd05af16d7af7e6a0c231493436244d6046fdd811916e3101f9f2e917  stageA-X1/leaves.jsonl.gz
8dbd8f636e90275900b921163f44dc0e7037dd184198618f2cd30151e6671af1  stageA-X1/lp_duals.json.gz
6de28d19333974fb8aef7e2284cbb05a25c8f764f4009cc012f86b1d499687ba  stageA-X1/run.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  stageA-X1/survivors.json
a220e5666a8f5cf1346ff6faa2af85c3240a07d91dd0d5dacf4d6cb6110beceb  stageA-X1/vfc_killed.json.gz
```

## Certificate-format caveat (for the independent replay)

v1 stores:
- the killed VFC star signatures (`vfc_killed.json.gz`);
- exact duals keyed by LP key (`lp_duals.json.gz`);
- one line per leaf orbit with its witness (`leaves.jsonl.gz`).

It does **not** store per-node prefixes. A checker must re-walk the tree and apply T, VFC (by signature lookup and dual verification) and K itself. A leaf that the checker reaches but the engine pruned by K-partial is killed at the leaf by the same K witness. A frozen CERT-FORMAT-k7 text has not been written yet.
