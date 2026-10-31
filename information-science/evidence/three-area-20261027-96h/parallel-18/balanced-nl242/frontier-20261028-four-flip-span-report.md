# info-6 frontier: complete four-flip neighborhoods and a 512-table local span

Native `/bin/date` observed before writing: **2026-10-28T17:20:19-0700 PDT**. This continues the three precisely encoded published seeds and checks in `frontier-20261028-two-flip-report.md` (SHA-256 `375d9034c03b6b469878a4cd74435dc37e8a6f7ba450ff12d71ee0853d04314d`, 74 LF). **Exact finite-neighborhood result plus a general one-flip lemma; no unrestricted NL242 solution, global no-go, novelty or formal/kernel acceptance.** The unrelated f6 review was completed before this report.

## 1. General analytic one-flip obstruction

For any nine-variable Boolean f, not necessarily balanced, suppose every W_f(a) is divisible by 4 and max|W_f|=28. Put k=W_f/4, P={a:|k(a)|=7}, n=|P|, and L=Σ_{a∉P}|k(a)|. If

    7n−L >128,                                                   (1)

then **every** one-bit flip has Walsh peak exactly 30. More precisely it makes at least

    ceil[(7n−L−128)/14]                                         (2)

original peak coefficients increase in absolute value.

Proof: for each truth position x, inverse orthogonality gives Σ_a k(a)(−1)^{f(x)+a·x}=128. If b_x peak signs are opposed to the modulating sign, the peak contribution is 7(n−2b_x), while the entire nonpeak contribution is at least −L. Hence 128≥7(n−2b_x)−L, proving (2). A flip changes each W by ±2; an opposed peak becomes magnitude 30, and no coefficient can exceed 30. ∎

The independently recomputed source histogram is n=210 and L=30+3·46+5·226=1298, so 7n−L=172>128 and the lemma gives at least four worsening peaks for **each** one-bit flip of any Boolean function with that same absolute Walsh histogram. It is not an unrestricted bound for all nine-variable Boolean functions. Separate exhaustive measurements on the three named seeds found minimum worsening-peak counts 76, 77, 76 and minimum pairwise common-worsening counts 22, 22, 22; these exact minima are single-implementation measurements. A second independently written per-peak checker separately verifies that every one of the 512 one-flips has peak 30 and every one of the 130,816 two-flips has peak 32 for each seed.

## 2. Exact four-flip hypergraph certificate

For an original peak a and a truth position x, call a **bad for x** if flipping only x moves W(a) outwards from ±28. Define B_x as all bad original peaks. If four distinct positions Q are flipped, an original peak increases beyond 28 exactly when it is bad for **at least three** positions of Q. Each named input has all nonpeak magnitudes at most 20, so after four flips no originally nonpeak coefficient can exceed 28. Therefore

    Q preserves peak≤28  iff  every three-subset T⊂Q has ⋂_{x∈T}B_x=∅.  (3)

This is an exact equivalence for these inputs, not a heuristic. The condition says Q is a four-clique in the hypergraph whose edges are the uncovered triples. Every four-clique is found by taking its three smallest vertices as one such edge and checking its larger fourth vertex. This proves completeness over all binom(512,4)=2,829,877,120 possible four-flip sets per seed without actually iterating over all those quadruples.

| Seed | All triples checked | Triples with empty bad-peak intersection | Fourth-vertex extensions checked | Peak≤28 four-flips | Of these, with any Walsh zero |
|---|---:|---:|---:|---:|---:|
| 1 | 22,238,720 | 195 | 26,319 | 45 | 0 |
| 2 | 22,238,720 | 195 | 23,882 | 45 | 0 |
| 3 | 22,238,720 | 195 | 26,245 | 45 | 0 |

The complete lists of the 195 triples and 45 four-flips for each seed are in the pinned C++ result. The previously run independent Python checker recomputed the source spectra by direct character sums, reconstructed **all** triple sets, checked exact set equality with the C++ output, independently enumerated the four-cliques, recomputed every coefficient of each resulting 45-table set, and reproduced 45/0 in all three cases. Deleting a listed triple in memory was rejected for the specified set-mismatch reason.

An independent Python triple histogram also counted exactly 195 uncovered triples for each seed. The two-flip certificate proves every pair has a common bad peak. Consequently each uncovered triple has new peak 30, whereas each other triple has a common bad peak at all three positions and new peak 34; these are statements about these inputs only. Because each original spectrum is 0 mod 4 and zero-free, an **odd** number of truth flips makes every Walsh value 2 mod 4 and cannot be balanced by any affine twist. Combining this with the complete two- and four-flip checks: no Boolean function obtained from any of the three named seeds by **at most four truth-bit flips plus an arbitrary affine Boolean term** is both balanced and NL≥242.

## 3. All combinations of the 45 local generators

For each seed, the 45 peak-preserving four-flips use 15 truth positions of affine rank 4; every four-position set has XOR 0. As binary incidence vectors on the 512 truth positions, their span has rank 9, hence exactly 512 members. We exhausted **every** span member, including combinations whose intermediate states might leave the peak≤28 class. The exact same census was obtained for all three seeds:

| Peak | Number of the 512 span tables |
|---:|---:|
| 28 | 256 |
| 32 | 240 |
| 40 | 16 |

All 256 peak-28 tables have **no Walsh zero**, so no affine twist of any span member is an original balanced NL≥242 witness. This is the complete 512-table affine truth-space slice generated by the particular 45 local moves for each particular seed; it says nothing about modifications outside that slice or about the full function space.

The first implementation used Gaussian elimination and FWHT. An independently written second implementation formed the entire vector space by set closure, then computed each Walsh coefficient directly as `512−2·popcount(truth XOR linear-character-mask)` for all 512 frequencies of all 512 tables. It matched every span size and peak histogram and found zero targets; a modified expected target count was rejected for the intended mismatch. The two methods share the pinned seed and 45-move list, whose complete correctness was independently checked in §2.

## 4. Evidence and explicit boundaries

All artifacts are in this exclusive `balanced-nl242` root and were hashed from their actual bytes. The prefix `frontier-20261028-` is omitted below.

| Artifact | SHA-256 | LF | Scope |
|---|---|---:|---|
| `published-seeds.txt` | `116ab5a7709dd35d951ddc878af227e5e05ce269d8293e5c0c269e158bd051f2` | 6 | Three published tables, explicit bit order |
| `peak-plateau.py` | `f61ea884af755478d4e9e9e13837b96563e7c8964c9028442b59165962c4a01f` | 84 | Complete two-flip peak masks |
| `peak-plateau-results.json` | `dbc295f5700fc209034cda2a6786290ca2dbf338af11aef9aa34e7c07a1b36d2` | 30 | Zero preserving two-flips, all seeds |
| `check-plateau.py` | `f67df6fa767dfc8a12c7f7e0ef0fbe1b4902ae64c4f6d6c333631917ebafe407` | 81 | Independent per-peak 1/2-flip check |
| `independent-plateau-audit.json` | `663bce8c772c8461cf900d1fbd1b8b9f7db51f20eecb309bf9ba93211ccf97c2` | 46 | All 512 singles and 130,816 pairs per seed |
| `peak-robustness.py` | `c8de225f7984372311981f9612995e49401f4b3f171ae076aa3d745bf25205f8` | 70 | Exact bad-set intersection histogram |
| `peak-robustness-results.json` | `cb499c39cb578f1404dd1207509dcd7243a676af5e76756168e44ec2bdd810fa` | 212 | Observed individual/pair margins |
| `triple-cover.py` | `91457e075a8e3bff863a7259a559d8181b3252d754d30eb109a07037fe15dbcc` | 77 | Complete independent triple histogram |
| `triple-cover-results.json` | `247fccaf58c84d063b36ff1ea170e96f591cb68d086d0680677d26c166e9d403` | 158 | 195 uncovered triples per seed |
| `four-flip-hypergraph.cpp` | `27e2f1e805e97a85c7bf058e06a3e4bb1b7e74762d530bf9c82e321af20643aa` | 214 | C++ complete hypergraph/quad search |
| `four-flip-hypergraph` | `9e5d0aed8160d48766ec93837eee39d973fbc329887a7b9f95bfab3dd6cf79b9` | — | Actual compiled executable |
| `four-flip-hypergraph-results.json` | `2adc6c54fe8dffb6930fd60d9c9b159a58855a79c47a7c0ed1a024b0d9c30e4b` | 8 | Complete triple and quad lists |
| `check-four-flip.py` | `967bafb60be6aeb1bd11158ff60618dfab0f5213bc78877bfa7f4801bcefb9d4` | 123 | Independent full set/quad check |
| `independent-four-flip-audit.json` | `d21957fc026b51f56a3927a6925af2e98edecbc12e132297dbdad3f4d7b2f555` | 31 | Counts agree; deletion controls reject |
| `flip-span.py` | `d386d785ca1027bd5f48eaea5939ea9fa4ae6ab74c39a4297028327e89e9c1e1` | 132 | Gaussian span and full FWHT census |
| `flip-span-results.json` | `c2df2c084a8cd62b066a7ec93780505c87aef9dea28cc9b656b366be1fdd06ae` | 121 | Three complete 512-table censuses |
| `check-flip-span.py` | `5a9a96c99ce7fb04ebe67d9ba6144c2fb263f5194d2fd468fc872e0d17529d54` | 119 | Independent closure/parity-mask checker |
| `independent-flip-span-audit.json` | `51694124da3b85125a8b46407f266e5229bfe8a963416be3ccb0268557170949` | 65 | Full agreement and mutation controls |

Compiled C++ was run with `clang++ -std=c++17 -O3 -Wall -Wextra`; Python scripts used `/opt/homebrew/bin/python3 -B`. The bounded exact triple scan completed in 8.23 s, and the independent full four-flip check in 3.48 s. Every 512-table span was exhaustively checked twice by the distinct stated transforms. No search failure or count above is promoted to global nonexistence, novelty, or a target witness; previously quarantined outcomes are not treated as accepted premises.
