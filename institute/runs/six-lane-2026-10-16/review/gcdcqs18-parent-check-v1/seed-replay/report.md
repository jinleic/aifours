# Seed/action replay: gcDCQS(18^4:2)

Recorded 2026-10-17T23:39:17.654603-07:00. **PASS** under `python3 -B` and `python3 -O -B`. Lane code was neither imported nor executed. This replay supports the explicit certificate only; it gives no verdict on §4(3), the gate, the bridge, or novelty.

## Inputs and code

- Certificate (parent pinned copy): `1382d572f8024c9b93ff6f5cf8aff942a9538119e8462ba54b02b6f160da282e`
- Seed `seed-v1.json` (pinned in `input/`): `1831510f69d8610bf5496ecaed166ac86f8df768fd7c8a996a4c31cde59475f4`
- Read-only lane files: `receipt-v1.json` `a4d56f56573ee3cbd4badb5ce9080bffda01c07838efd99133a2589892bc2590`, `seed_gcdcqs18.py` `4228507443f5451892cd26c2004d0eabc7c99930891f96694e2dc9554f034a01`, README at read time `352f9505cc6028e6b500e45806e7a844e59659baa3ac727b6d1ed40fe69c0eaf`
- `replay_seed.py` `ab3a90ce1aa60ab040fde8bc6d8c88a9bf28ef7b74fb989d7d23a181e25b4f1a`; supervisor `run_seed_replay.py` `7780b67ee38b883b7a0e11f06930df94a109103037a79d2aec0233b8a95f14ef`
- Imported parent code: Format S parser `11fa08bc…cba5` and resource sampler `23647fc9…33d4`

## Results

| Check | Result |
|---|---|
| Group built with this replay's own GF(9) arithmetic | S = ×(1+i): order 8 and transitive on GF(9)*. S² sends (z1,z2) to (z2,−z1). Generator orders: t8 8, t31 3, t32 3, S² 4. |
| Group order | **288**. The translations form a group of order 72, regular on the 72 group points and normal in G. They meet ⟨S²⟩ trivially. Stab(0) = ⟨S²⟩, order 4. |
| Point partition | All 288 elements preserve {S, G0..G3}. t8 cycles the groups 0→1→2→3→0 and swaps 72↔73; the other generators fix every group and both stems. |
| Seed generator arrays | All four are identical to the described generators. The two generated groups are equal as sets of permutations. |
| Block-set invariance | Holds for every block (15,066) under each described generator and each seed generator. |
| Expansion of 65 representatives | Orbit sizes 288×44, 144×13, 72×7, 18×1 (stabilizer orders 1, 2, 4, 16). The orbits are pairwise distinct with no overlap. **The expanded multiset of 15,066 blocks equals the certificate multiset exactly:** 0 blocks missing, 0 extra. The seed's orbit-size claim matches. |
| Colouring transport | Seed point-0 classes equal certificate POINT 0 (37 classes, 819 triples). Least-element transport equals the certificate's ordered classes at **72/72** group points. All **288/288** elements carry the point-0 partition onto the certificate partition. Exactly 72 of them preserve class numbers: these are the least elements. |
| Stem frames (supplementary) | The kernel ⟨t8⁴,t31,t32⟩ has order 18 and equals the seed's frame group. At each stem point its orbits are 36 parallel classes (9 per omitted group). These equal the certificate frames. |

## Negative controls

Both controls replace t8 with the near-miss map a↦a+1 that **fixes** both stems. In each control the group still has order 288 and preserves the partition. Both modes reject both controls at the intended `action.block_invariance` check:

- `--wrong-t8-fixes-stems`, which changes the described generator: condition `action_description`.
- `fixtures/seed-v1.t8-fixes-stems.json` (`d1bc2d758d9116816d997ff2f92824b7a60560f7ee5514f65db8e9a66badcdb6`), which changes the seed array: condition `action_seed`.

In both controls, 1,296 blocks are not mapped to blocks. All of them contain a stem.

## Timing and resources

- In-process time for the positive run: 0.584 s with `-B` and 0.574 s with `-O -B`. Parsing takes 0.354 s, expansion 0.023 s and colouring transport 0.134 s.
- Six executions, run one at a time: 3.00 s of child wall time. The suite took 60.02 s in total, mostly spent on the lane/process sampling done before each launch.
- Peak child RSS was 63,160,320 bytes. Free disk before each launch was at least 13,551,509,504 bytes, above the 12.2e9 floor. Before each launch the sampler found 0 busy math-1 processes.

## Limits

- The labelling p = 9a+3z1+z2 was learned from the seed format and checked against the certificate groups.
- Byte-identical regeneration was not attempted. All comparisons are exact set and multiset equalities.
- The frame check is supplementary.
- The replay imports the parent's own hash-pinned parser.

Details: `result.json`, `runs/`, `provenance.json`.
