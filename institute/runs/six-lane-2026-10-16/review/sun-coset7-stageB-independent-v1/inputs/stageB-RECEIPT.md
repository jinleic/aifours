# Stage B receipt (EXPLORATORY under the parent GO of 13:35 PDT; not a premise until reviewed)

- **Engine:** `code/core7_engine_v1.py`, sha256 e7b4f039ba02c9e8ab5c39579c0d21d3ce4e1d3aba13ec2813129eda67a4288d (unchanged since Stage A). Certificate format: `CERT-FORMAT-k7-v1.md`, sha256 2c0e4830…1545 (frozen 13:38:43 PDT, during this stage, before its outputs were read).
- **Readiness checks:** statvfs free 25,665,146,880 B (13:37:15 PDT, before K52) and 25,665,052,672 B (before KII), against the required 12,216,777,216 B.
- **Command (one process at a time, TMPDIR inside the lane, no external timeout):** `/usr/bin/time -l python3 code/core7_engine_v1.py K52 evidence/stageB-K52 900`, then `… KII evidence/stageB-KII 2698` (2698 = 2700 s minus K52's 2 s elapsed).
- **Wall clock:** 13:37:15 → 13:45:02 PDT.
- **Peak RSS:** 32.0 MB (K52); 149.2 MB (KII).
- **Disk minimum during runs:** 24,767,062,016 B (KII). Free space fell by about 0.9e9 B during the stage; the lane's own outputs total under 0.3 MB.

## Results

| class | status | profiles | nodes | closed (T / VFC / K-partial) | leaves (orbits) | leaf rule | survivors | seconds |
|---|---|---|---|---|---|---|---|---|
| K52 (K5.2 incl. the D2′ case; README §5) | COMPLETE | 171 | 3,316 | 174 / 1,333 / 0 | 0 | — | **0** | 2.0 |
| KII (a = 2) | COMPLETE | 132 | 1,524,276 | 3,693,180 / 1,555,848 / 736,332 | 1,584 (528) | RPLP 528 | **0** | 465.1 |

No UNKNOWN in this stage.

## Meaning (exploratory; independent replay and reviews pending)

If confirmed, classes **K5.2\*** (together with the D2′ case) and **KII** are removed, in addition to **K5.3** (Stage A, X1).

The classes still open after Stages A and B are:
- **K7** (all 21 gcds = 6; Stage D, not requested);
- **K6.2\*** and **K6.3** (Stage C, not authorised).

This is not a k = 7 result.

## Output hashes (files chmod a-w at 13:45:15 PDT)

```
74420f89d2d2a4256b5b578f1c2a01dd2b605f9aca4905db839d008cfd29cac0  stageB-K52/leaves.jsonl.gz
1dde125d179b2e9c915be887d5d6df5110d0889bdb2948533623d8c5e1d412f9  stageB-K52/lp_duals.json.gz
9b840aea6e0cba47043810e0f7a67619909d2e2377792b30e2ef8f26c8042859  stageB-K52/run.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  stageB-K52/survivors.json
ef9d83e36c830599677ea8fcf81a3602c067b235a66b2a97d99d96e1b3f8dfc2  stageB-K52/vfc_killed.json.gz
abcac773ee16452e7f01ef147e4bf8e2c1b9abf1a6398539d5624bce06af363d  stageB-KII/leaves.jsonl.gz
fd371438cef20d34cc56e24a698866f0547b7b615465ccad0b64ac8e29d073bc  stageB-KII/lp_duals.json.gz
9b75892e493832d98d72f9c590141aea327fe90c528b87f01d2d5050478608bb  stageB-KII/run.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  stageB-KII/survivors.json
7ae750f52138e9d931912944bc6493854ffda4ca000ea9fcb8cce439998ee867  stageB-KII/vfc_killed.json.gz
```
