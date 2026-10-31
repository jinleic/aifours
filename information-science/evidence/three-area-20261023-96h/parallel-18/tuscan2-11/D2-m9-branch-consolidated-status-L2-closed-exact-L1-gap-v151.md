# Original Tuscan-2(11), entire m = 9 distance-two branch: consolidated status after the closure of L2 (k = 3), and the exact remaining gap (L1)

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It supersedes the status sections of v119 and v131 for the m = 9 branch. All pins below were derived live with `shasum -a 256` at writing time.

This is written reasoning only. No interpreter, enumeration, solver or search was used. Nothing here is reviewed, formal, kernel-checked or novelty-cleared.

## 1. Status of the three m = 9 families (parent direction v143)

| Family | Status | Where |
|---|---|---|
| L4-B (W1) | **CLOSED** | v112–v113 |
| L2 with k = 3 | **CLOSED**: every type (A, B, C, E) and every cell (n1, n2, n3, nΛ) | v114–v116, v120–v130, v132–v150 |
| L1 | types 5 and 6 **CLOSED** (v118); **types 1–4 and 7–12 OPEN** | v117, v118 |

## 2. The exact D2 coupling gap

The only open part of the m = 9 branch is L1, types 1, 2, 3, 4, 7, 8, 9, 10, 11 and 12. In each of these types the following are free:
- every (n1, n2, n3, nΛ) with sum 2;
- every position of v's cut;
- every u = 10 − t;
- every b6-corner offset subject to (L-a)–(L-e) of v117 §3, together with the OL windows and the arm table.

The tools that closed L2 have not yet been applied to these ten types:
- pure-row double passes, DP-1 and DP-2 (v114);
- row coverage RC with the face-group anatomy (v134);
- D2Q (v125) and R3-pair (v130), which use (R3);
- slot and cover lemmas, of the kind in v147 (Lemma Λ2) and v149 (Lemma S).

**So the statement "every eligible original T2(11) array with support 9 is impossible" is NOT made.** Every m in 10..110 remains unresolved.

## 3. Where (R3) enters the L2 closure

Distance two enters through two lemmas:
- **D2Q** (v125 §1): three or four Q-labels on a row-path need at least 6 or 8 vertices, and only the two special pairs may stand at distance 2.
- **R3-pair** (v130 §1): a neighbour pair around a non-cut 2-vertex cannot recur.

These lemmas are cited where used, for example in v125–v130, v134–v137, v139, v141 (R3-pair), v142 (d = 4), v143, v146 (δ3 = 4), v148 (δ = 4) and v150 (δ3 = −4). Other closures use only (E), (C), (X), RC, DP-1 and DP-2. Examples are:
- v140 (type E, d = 6);
- v144 and v145 (type B (0,2,0,0), δ ∈ {6, 5, −4, −5, −6});
- v147 (Lemma Λ2 and type B (0,1,1,0));
- v149 (Lemma S and type A (0,2,0,0)).

**Errata.** The ℓ1 ≤ 4 sub-cases omitted from the written proofs of v143, v144 and v146 are repaired by the addendum in v147 §3. The conclusions are unchanged.

## 4. Pins (live SHA-256)

| Packet | SHA-256 |
|---|---|
| v110 original-T2-D2-frontier-parity-equivariant-K-exclusions | 6bf459e45faf661b5de6523ec80e4b70ecf09968a8ab0b15b6957aa1ecc89db6 |
| v111 original-T2-turn-system-equivariance-group-order-at-most-2 | 1f6160c89ff07796d5e4359386756cf1e96e58f18a8d9a0403a4e3450ae8d99d |
| v112 lonely-pair lemma, L4-B W1 structure | 3323be46b5c839c3ff817face278399317fbad23d4ff2a523a4a40695c2ee3d0 |
| v113 L4-B closed | a561978485912ece66908d9a41fa2689cf4cab510d50eff2c076837a8964d575 |
| v114 double-pass lemma | e5b74dd0bb1a4064811de2578b9fcc607a6d89c9a09e89c8cec90dd0c15ee4d0 |
| v115 OL thresholds | fd3f5d8b4a391c885a758f22a9d7864a5cde45ae225b5db27c2ba1af63775a2d |
| v116 offset parametrization | dcaca8479d52bc975f319f4e8aae7b6ae35f821f4f9eae7ff233f6d85e29b335 |
| v117 L1 types and constraints | 77faa481d25f322fffd2d68fc12f9441ae52bbc1e315a9a52685f72378842e96 |
| v118 L1 types 5–6 closed | 5987287dda6ca7a1446058e3c045a25eea00d855953ffbe37b73d28f8594306d |
| v119 consolidated status (old) | 866b9f9a8eb99bc504c6eac64a9007f3053bb5a5b1742a886c194f14e12b7334 |
| v120 K4 saturation | ba738109b9b466f62661d0794a0061a67964f5192606adbeaa9af313b9d29e31 |
| v121 type A b3 closed | 870aaefea5dc2f3b7151dc3f312b937e670b10ff728b82014febfdc2213229ab |
| v122 type A b4 loop-V cells | f180fe11530aca9c61cfc03b0797b6d346e864fe62aa721ef6eea2f5957935c0 |
| v123 type B b2 cells | fd1654f56dff6a3b75477eed1a3c9a8250c4c7bfbd27ec28010833b16a610294 |
| v124 nΛ = 2 dead | bcef74d17513f60b8b0405dd5696ef39cd2271d7983899a983b30ab5310eed25 |
| v125 D2Q lemma | 85fcc86caa10a2ae94a8297a211a4d5577f034ffd30acbe69a1ec056b3847ec0 |
| v126 | 94a97cf4bb6b37bc34c45889f5f4e89f40a8b1a3609ba1660dbc24ed46c32845 |
| v127 ARM-C | c9d8952ee4f9d636d39c929cf63f81407c05bbaa97b11dde15c6f694fadd8027 |
| v128 ARM-C+ | 56686ab733c139ff0cd108f691d23cfdf5fcc0ee2eabb5557617dc9151ac9a35 |
| v129 | 13bd2fed9b2caa79cd31fe75a7a44087ad218e21b9527eb466e54ad3b08087e3 |
| v130 R3-pair | e157ac98ece98e2388cae72eca7a9dac699e29534099ccf268a8e517537b07f2 |
| v131 consolidated status (old) | 5df681745478e6184c539012cd1c695a046a54b37a5251920aba7f5d0cfda417 |
| v132 | d1f51603a7728e7efca3be8e171cfd390511b7ea6294ce78ebab110b9616df1c |
| v133 | ffb46131b119660a8e40742c63d987c0ba0a40d88a70e67fd28ca677606c20f9 |
| v134 RC lemma | 3a08db2db1d83bd8f44720d826978215cfea8f3909151f08b8104f3239558579 |
| v135 | 900fccab4153f7df50b33ef0e4dfb03653f5b3a5b347d045720276118f928379 |
| v136 | 642135bc8060949872b6203c831304bd84d4f0cba17e7a45eb8de36a66b27953 |
| v137 | 2c3383e18cf486da3deeedf05ea83cbca4d0496319d13e4f4caadb39cd9ef603 |
| v138 | 5e38a4e0493efd71ecbaa865b52fd39f2395b5f7229f6d5d25a6ec125bc076bb |
| v139 | c3f83e7f3677dcd53f7eeb28a249dae1ebb360cfd822f6532458aca405943cc3 |
| v140 | d509d049f6141e8efdc0c1cb53fec4d117840b4c34bc66390d09243e8f95125c |
| v141 type E closed | f1ea7890aea810b28117d9ab89ab802402d4919501ceb658ddf8aa9df53e80de |
| v142 type C closed | 57be8ae451f595247f9516f1a89997665820b1dea859babd20bfd6fed9548894 |
| v143 | 56d58c824eec5be0b3072f555121e3aa7fd529116ad9bd7ad099ab000c9dbb27 |
| v144 | 2fdd8c287c44c36ad1fe14e9d97411decbbe4890bf0b89010a9c4743628086c9 |
| v145 | b702f402dd2dc61a70338ffcb12a9ada07d2a86c414aef9fd1accfad7a5a651f |
| v146 | 9c3083006e5b8535f7a95e5ea5404e6903c3b8b4b987edfd2109f10522afedb2 |
| v147 type B closed | 14f049df17d412ab14b22bbab20bfd3f02ca50e775ad10d29704c0bcb871f5b8 |
| v148 | b49584adf1f302e0d3918195518f6a9e2cff3f579d867c15f32af6cbfe9c0687 |
| v149 | 733bc33fb9cda5468a13e91d15dd2191822526dd4bbc4b84abc2148a8a4854a7 |
| v150 type A closed, L2 closed | 005eb8c88733ee4aca30929675c77ab00b3cc852f4a887402b7f77f7e5252a8a |

## 5. Scope

**WRITTEN, with the imports named in each packet:**
- L2 (k = 3) is closed in the m = 9 branch.
- L4-B is closed.
- L1 types 5 and 6 are closed.

None of this is a formal proof, a kernel check, a cross-vendor review or a novelty clearance. Each packet needs its own complete source-bound gate.

**The original target is UNMET.** There is no literal unrestricted Tuscan-2 square of order 11, and no all-array contradiction.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
