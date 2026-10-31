# info-6 frontier: complete three-outside-flip obstruction for published seed 1

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` observed before writing **2026-10-28T17:55:36-0700 PDT**. **NEW EXACT FINITE OBSTRUCTION, NOT YET DISJOINTLY REVIEWED OR ADOPTED.** For the first pinned published NL242 seed and its specified affine 4-flat A, every one of the `binom(496,3)=20,214,480` choices of three outside truth bits is incompatible with Walsh peak ≤28 **for every one of the 2^16 possible choices on A**. Combined with the separately checked zero/one/two-outside results, no modification with at most three changes outside A, arbitrary A values, and any affine Boolean addition is a balanced NL≥242 witness.

This is an exact result on one specified source/core class, not on all Hamming-distance-19 changes, the unrestricted Boolean problem, the other two seeds at three outside changes, or all affine cores. No witness, global no-go, source novelty, formal/kernel or independent-model claim follows.

## Complete coverage by local Walsh intervals

The same full-spectrum decomposition and exact local constraints are in the earlier `frontier-20261028-affine-core-caller-v1.md`, SHA-256 `e12099f6140b5cf487eb60dd05adbefd9d47d00b3b07f57a815a1e826bcf53ab`, 85 LF, and the one/two-outside report `frontier-20261028-outer-two-obstruction-v1.md`, SHA-256 `79162dcb01a82c811740126a83e5f88de9eb50a2c06e24fac3779b406345492d`, 60 LF. The seed/bit order is fixed there. For any chosen outside triple, the minimum/maximum oriented outside Walsh sums in each of the 16 restricted-frequency classes give necessary integer intervals for q_α=L(α)/2. Every actual choice of the 16 core bits must also satisfy

    Σ_α q_α²=64,         Σ_α q_α∈{−8,+8}.                       (1)

The full native search intersected exact bitsets representing all 65,536 local truth assignments, and found no peak≤28 table. A second C++ scan classified the sorted integer-interval profiles; a third, separately written C++ program independently reconstructed the original outside sums and checked a simpler moment certificate. Both complete scans agree on all 20,214,480 triples:

| Reason | Number of outside triples | Exact implication |
|---|---:|---|
| Some class has an empty interval | 19,579,600 | No possible local Walsh value in that class |
| All intervals nonempty; maximal possible Σq² <64 | 609,270 | Violates Parseval |
| Maximal possible Σq²=64, but largest possible Σq at that maximum is ≤−16 | 25,610 | Violates the required sum ±8 |
| Unresolved | 0 | No remaining triple |

The 634,880 nonempty cases occupy 14 sorted interval profiles, retained in the profile receipt. If an energy upper bound equals 64, equality forces every coordinate to attain its own maximum squared magnitude; the independently computed upper bound on their sum is then at most −16. This is a rigorous rejection without assuming any candidate f or selecting a local assignment. The exact local-bitset search, the 14-profile moment DP, and the direct outside/energy-bound scan use separate checks; the first two share a frozen local solver source, while the third independently constructs outside sums and uses no local-pattern bitsets.

## Evidence and verification boundary

All files are in the exclusive `balanced-nl242` root. Prefix `frontier-20261028-` is omitted. Actual byte hashes:

| File | SHA-256 | LF | Role |
|---|---|---:|---|
| `core-outer-triples.cpp` | `b8c9999dd9ae252cd24066aad52379cc74a67dba5f35c5765867bb1f13f40940` | 101 | Complete triple/local-bitset search; includes the pinned two-outside solver |
| `core-outer-triples` | `57362ec8a434926d366cb507fc407a199b710d89bf0e23acf732e90fb7259157` | — | Actual native executable |
| `core-outer-triples-seed1.json` | `944750c7a1fd604a780826582ff01036e85b1acf6d30dbe4f37d37af5f00e380` | 16 | 20,214,480/20,214,480; zero feasible |
| `outer-triple-profiles.cpp` | `af3ab2daf1048dce1dfd985d14c0d383a060e222933dcf2833461cf1c1b61c63` | 128 | Complete profile catalogue and exact moment DP |
| `outer-triple-profiles` | `c2305281c26b5fd3d93949486b785ab0365bbce1d8b0d0a7bdaa9f5a25d80a56` | — | Actual compiled executable |
| `outer-triple-profiles-seed1.json` | `6c020c84adb07f14ecfdf4eb7e31582b8143ae364899266df6eb07d500383a75` | 27 | All 14 nonempty profiles and multiplicities |
| `check-outer-triples.cpp` | `8c2497c7f3892ee4898091c855116f54df13bd61708f9f2e35e9854219f36f0a` | 127 | Separately written direct outside/moment checker |
| `check-outer-triples` | `93796ee08655ef2fbe1afab4d3daa8d73c945661ae8d2772f832779108249c33` | — | Actual compiled executable |
| `independent-outer-triples-seed1.json` | `81dd3bc2e9afecedefe9cfff1b5808ff99a2478d1ab2b15e75fbb1a6c8fa608f` | 11 | Complete independent counts, zero inconclusive |

The full bitset scan reported 16.98 s program time, the profile scan 10.09 s, and the independent interval/energy checker 0.98 s. These are finite local checks, not independent model-family review or a replacement for a written scientific review. The next unknown remains the unrestricted original balanced nine-variable witness-or-exclusion; no conclusion about four or more outside changes follows from this report. **END.**
