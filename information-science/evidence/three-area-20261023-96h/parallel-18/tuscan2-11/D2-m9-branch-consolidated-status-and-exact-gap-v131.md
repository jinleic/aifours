# Original Tuscan-2(11), entire m = 9 distance-two branch (parent direction v143): consolidated status and exact gap, as of v130

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4). This status packet supersedes the status part of v119 (SHA256 `866b9f9a8eb99bc504c6eac64a9007f3053bb5a5b1742a886c194f14e12b7334`), which remains pinned and unchanged. It gathers v120–v130 and is written reasoning only. It is not reviewed, formal or novelty-cleared.

## 1. Packets since v119

| Packet | File | SHA256 |
|---|---|---|
| v120 | D2-m9-L2k3-K4-saturation-lemma-typeA-1001-excluded-v120.md | ba738109b9b466f62661d0794a0061a67964f5192606adbeaa9af313b9d29e31 |
| v121 | D2-m9-L2k3-typeA-1100-lambda14-excluded-typeA-b3-closed-v121.md | 870aaefea5dc2f3b7151dc3f312b937e670b10ff728b82014febfdc2213229ab |
| v122 | D2-m9-L2k3-typeA-b4-loop-V-cells-excluded-v122.md | f180fe11530aca9c61cfc03b0797b6d346e864fe62aa721ef6eea2f5957935c0 |
| v123 | D2-m9-L2k3-typeB-b2-cells-excluded-v123.md | fd1654f56dff6a3b75477eed1a3c9a8250c4c7bfbd27ec28010833b16a610294 |
| v124 | D2-m9-L2k3-nLambda2-dead-all-types-v124.md | bcef74d17513f60b8b0405dd5696ef39cd2271d7983899a983b30ab5310eed25 |
| v125 | D2-m9-L2k3-D2Q-lemma-mirror-typeE-1100-x1eq9-excluded-v125.md | 85fcc86caa10a2ae94a8297a211a4d5577f034ffd30acbe69a1ec056b3847ec0 |
| v126 | D2-m9-L2k3-typeE-1100-x1eq1-u-ge5-excluded-v126.md | 94a97cf4bb6b37bc34c45889f5f4e89f40a8b1a3609ba1660dbc24ed46c32845 |
| v127 | D2-m9-L2k3-ARMC-lemma-typeE-1100-closed-v127.md | c9d8952ee4f9d636d39c929cf63f81407c05bbaa97b11dde15c6f694fadd8027 |
| v128 | D2-m9-L2k3-ARMCplus-typeE-1010-1001-typeC-1010-excluded-v128.md | 56686ab733c139ff0cd108f691d23cfdf5fcc0ee2eabb5557617dc9151ac9a35 |
| v129 | D2-m9-L2k3-typeC-1001-excluded-1100-reduced-v129.md | 13bd2fed9b2caa79cd31fe75a7a44087ad218e21b9527eb466e54ad3b08087e3 |
| v130 | D2-m9-L2k3-typeC-1100-rho6-excluded-rho4-reduced-v130.md | e157ac98ece98e2388cae72eca7a9dac699e29534099ccf268a8e517537b07f2 |

## 2. Closed

**Using (R1)–(R2) only:**
- L4-B (v113);
- L1 types 5 and 6 (v118);
- L2 type A, every cell except (0,2,0,0) and (0,1,1,0) (v114–v116, v120–v122);
- L2 type B with b = 2, all four cells (v123);
- L2 cell (0,0,0,2) in every type (v124).

**Using (R3)**, through D2Q, ARM-C, ARM-C+ or R3-pair:
- type E: (1,1,0,0) and (0,1,1,0) (v125–v127); (1,0,1,0) (v128); (1,0,0,1) and (0,0,1,1) (v128);
- type C: (1,0,1,0) (v128); (1,0,0,1) and (0,0,1,1) (v129); (1,1,0,0) ≅ (0,1,1,0) with ρ1 = 6 (v130).

**General lemmas:**
- DP-1, DP-2, OL and KS (R1–R2);
- the mirror reduction of types C and E (v125 §2);
- u ≥ 2 (v127 §1);
- D2Q (v125 §1), ARM-C (v127 §2), ARM-C+ (v128 §1) and R3-pair (v130 §1), which use R3.

## 3. Exact residual

**L2 (k = 3):**

| Type | Residual |
|---|---|
| A | (0,2,0,0) and (0,1,1,0), with nΛ = 0 and λ = 5 + p2 |
| B | (0,2,0,0) and (0,1,1,0), with b = 3 and λ = 15 − p1 |
| C | (0,2,0,0); (0,1,0,1); (1,1,0,0) ≅ (0,1,1,0) with ρ1 = 4 and either (x1, p1) ∈ {(6,7), (7,8)} at u = 2 with T-pattern 1,4,7, or (x1, p1) = (6,8) with u ∈ {2,3} |
| E | (0,2,0,0); (0,1,0,1) |

**L1:** types 1–4 and 7–12, with constraints (L-a)–(L-e), (L-K1) and OL, and with u ≥ 2 by the argument of v127 §1.

## 4. The exact distance-two coupling gap

Inside the residual, (R3) has been applied only through:
- the saturated-block consequences D2Q and ARM-C;
- R3-pair, wherever the case analysis reached a forced repeated neighbour pair.

Three things have not been applied to the residual cells as a whole:
- the full neighbour-pair condition (C1) for every non-cut 2-vertex;
- the corner-turn condition (C2);
- the K-entry count of Theorem A (v108–v109).

That application is the exact open coupling. No example is chosen, and no method-exhaustion claim is made.

## 5. Result

The support-9 statement is **not** made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
