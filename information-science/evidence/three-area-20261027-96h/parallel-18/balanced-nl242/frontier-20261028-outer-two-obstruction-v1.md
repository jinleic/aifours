# info-6 frontier: exact exclusion of one/two outside changes with an arbitrary 16-cell core

Owner **InfoBalancedNL242-2-2**, original info-6 slot. Native `/bin/date` observed before writing: **2026-10-28T17:52:55-0700 PDT**. **NEW EXACT FINITE OBSTRUCTION, NOT YET DISJOINTLY REVIEWED OR ADOPTED.** For each of the three pinned published NL242 inputs and its discovered affine 4-flat A, **no** Boolean table obtained by changing one or two of the other 496 truth positions and changing the values on A arbitrarily has Walsh peak ≤28. With zero outside changes, the independently checked core caller has exactly 448 peak-28 tables and none has a Walsh zero. Therefore, after **any** affine Boolean addition, no table in the full class with at most two outside changes and arbitrary values on A is a balanced NL≥242 witness.

The class contains exactly `(1+496+binom(496,2))·2^16` truth tables before affine additions for each fixed seed/core; it is not the set of all Boolean functions or all Hamming-distance-18 modifications. This does not prove a global no-go, a witness, novelty, formal/kernel acceptance or any result about other outside assignments.

## 1. Exact local interval certificate

Use the notation and verified outside sums from `frontier-20261028-affine-core-caller-v1.md`, SHA-256 `e12099f6140b5cf487eb60dd05adbefd9d47d00b3b07f57a815a1e826bcf53ab`, 85 LF. The 16-dimensional local Walsh vector L of any actual choice of 16 core signs satisfies

    Σ_α L(α)²=256,        Σ_α L(α)=±16.                          (1)

For every frequency a, the global coefficient is the original outside sum plus the local coefficient in the corresponding one of 16 restricted-frequency classes, up to a sign. After choosing the outside flips, the minimum and maximum outside values in each class impose an exact integer interval on L(α). Put `q_α=L(α)/2`; q_α is integral, and (1) becomes

    Σ q_α²=64,            Σ q_α=±8.                              (2)

All 496 single outside flips and all 122,760 pairs were scanned for each seed. Their **sorted 16-interval profiles** were independently recounted from direct outside character sums. All three inputs have the same complete profile multiset: one single-flip profile and 11 pair-flip profiles. Every profile is rejected using only (2):

| Outer changes | Number | Exact uniform reason |
|---|---:|---|
| one | 496 | All 16 q lie in [−2,0]. Energy 64 forces every q=−2, whose sum −32 is not ±8. |
| two, ordinary profiles | 119,040 | At most two q intervals extend beyond [−1,1], and all lie in [−3,1]; energy is at most `2·9+14=32<64`. |
| two, exceptional profile | 3,720 | Eight q are fixed at −1, and eight lie in [−3,1]. To have total sum +8 the latter eight would need sum 16, impossible. To have total sum −8 they need sum 0 and energy 56, but q²≤3−2q on [−3,1] makes that energy at most 24. |

The table exhausts all singles/pairs **for each** seed, and no case uses a chosen local truth vector. All statements here refer to actual Boolean core signs, not a relaxed histogram as a witness. The interval/moment argument is only a necessary-condition rejection; it would not certify a solution if a profile survived.

## 2. Independent finite checks

The C++ program `core-outer-search` precomputes the local Boolean Walsh values and exact bitsets for all 65,536 local restrictions, intersects all 16 class intervals and checks every possible zero frequency. It completed **all** singles and pairs for all three seeds, with 0 peak≤28 local restrictions after either one or two outside changes. Per-seed pair runs reported 0.581–0.635 s program time.

A separately written Python checker computes local Walsh values by Hamming-character parity masks rather than the C++ FWHT, reconstructs outside sums directly, and independently intersects the full local-pattern masks. It matched every single/pair count for all three seeds; its zero-outside positive control produced **448 peak≤28 / 0 balanceable** local tables, and a duplicate-basis mutation was rejected for the expected reason. A second independent Python program recomputed **every** outside interval profile and checked the elementary three-case proof above; it matched the complete C++ profile catalogue for all three seeds. This is not a cross-vendor or formal proof.

## 3. Pinned evidence

All files are in this exclusive `balanced-nl242` root; prefix `frontier-20261028-` is omitted. Hashes are from actual bytes.

| File | SHA-256 | LF | Role |
|---|---|---:|---|
| `core-outer-search.cpp` | `a1cd5207f2bcaf975998250002fb735717cd88625d5a304f4ae76d02d680652e` | 295 | Complete C++ outer/local solver |
| `core-outer-search` | `ea1545742ed341222dd59cff92715505a563ba9a048e85a2c27983a2004a45f9` | — | Actual compiled executable |
| `core-outer-single-seed1.json` | `742f0407f5888e213f171b1a94447fe5e6177a20c0d02225fcb367654bbde541` | 19 | 496/496, zero valid |
| `core-outer-pair-seed1.json` | `a1235f102c2b853692fb7ab15fe60a8f157b74b7850dcd418fb7c28beed4933b` | 19 | 122,760/122,760, zero valid |
| `core-outer-single-seed2.json` | `a244d0ff75d6e036f4e0406088d8b6d3fb9c14036334ccc2bd4cc52476f07f44` | 19 | 496/496, zero valid |
| `core-outer-pair-seed2.json` | `3fca0a2df3f75aa5ff967af0faa724b49171b1fc2a5fbafbc56ecedf5db09402` | 19 | 122,760/122,760, zero valid |
| `core-outer-single-seed3.json` | `831141ef2a4662199cb8d6f41e8ea62fe8155e604bccf393598bfa863b7cb900` | 19 | 496/496, zero valid |
| `core-outer-pair-seed3.json` | `88ce139e47951e87222aca4633f3411d10c5e322cc76e6ce271869c178961abd` | 19 | 122,760/122,760, zero valid |
| `check-core-outer.py` | `97514544c3b6d97019184b31792ac515267fcdd77a170fafb42968dd28bc5504` | 167 | Independent full local-bitset solver |
| `core-outer-independent-seed1.json` | `6a17c13814c4851a40e26452a83fd02958ff99d9b16aea53699ba572f7e45adb` | 27 | Full recount / positive and negative controls |
| `core-outer-independent-seed2.json` | `2e3ae1b4e7a6260ba0d3cfff3d8b532e7797fa05a4728dabf17de5b727d80cf3` | 27 | Same |
| `core-outer-independent-seed3.json` | `58a768e65061e3cd4ddee2093b30983841ec7d82c54c7c0c1b10f1fe32736d89` | 27 | Same |
| `outer-energy-bound.cpp` | `5af3d7442b82e4416c19f3d4028c61dafefc44a1c148a466171586dcccbffa71` | 138 | Parseval-only rejection |
| `outer-energy-bound-results.json` | `cea80ecb60c942561d342aa6ac25666f5abdfbe9f335c0eb5bb59107c181e412` | 8 | 119,040 pairs rejected; 3,720 need more |
| `outer-moment-bound.cpp` | `208331c594584b9d6e94d6bca2d1975998b03196aede5aea7fdec1672a9c95f4` | 114 | Exact sum/energy DP by profile |
| `outer-moment-bound-results.json` | `95b34031a54d38086bbfca9a4438bd3da96fbdb16e1b716f25ca640a0f8e9f7d` | 8 | All singles/pairs rejected; 12 profiles |
| `outer-moment-profiles.cpp` | `9b8536911e85f2fb2819a338fea339fb2e2384dacb08e05eedec30d73cd4cd92` | 87 | Complete profile catalogue |
| `outer-moment-profiles-results.json` | `3c06338c1c6755d63722a88b0b9f6c5d068871f5f362e52cf713d14c335b8e5d` | 8 | All intervals and multiplicities |
| `check-outer-profiles.py` | `d1d974ecf972f8923bdea7cf18764039b4c04f871d4dc4a36c4f9dda93f5924a` | 131 | Independent profile recount and written inequalities |
| `independent-outer-profiles-audit.json` | `a42c28064a2c4e66d538670efb1e1b5bbff2f8874335a9ff2024b0abd64e1bd8` | 32 | 3× complete agreement |

The source table and exact bit order are pinned in the core-caller report; all local and global sign arrays in these programs are actual binary truth values. Runs used bounded native C++ and standard-library Python, not a remote service. The original all-variable problem, every rank/weight alternative, source priority/novelty, formal/kernel and independent-model/human gates remain open. Historical quarantined outcomes were not taken as accepted premises. **END.**
