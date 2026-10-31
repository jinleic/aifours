# info-6 frontier: two independent complete four-outside-flip certificates

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` observed before writing **2026-10-28T18:03:20-0700 PDT**. **NEW EXACT FINITE OBSTRUCTION, NOT YET DISJOINTLY REVIEWED OR ADOPTED.** For the first pinned published NL242 seed and its specified affine four-flat A, **every** choice of exactly four of the 496 outside truth positions is incompatible with Walsh peak≤28, for **every** choice of the 16 values inside A. Combining the independently checked zero-through-three cases, no balanced NL≥242 function can be obtained by changing at most four positions outside this A, changing the A values arbitrarily, and adding any affine Boolean term.

This is a finite, source/core-specific result. It does not exclude other Boolean functions, other affine flats, five or more outside changes, or three/four outside changes for the other seeds. No original witness, unrestricted no-go, novelty, formal/kernel or independent-model claim follows.

## Exact certificate

For each outside choice, compute the minimum and maximum oriented outside Walsh contribution in each of the 16 restricted-frequency classes. They give an exact interval for its local Walsh coefficient L_α needed to keep **all** global magnitudes ≤28. Any actual 16-bit core signs have even L and, by Walsh Parseval,

    q_α=L_α/2 ∈ Z,          Σ_{α=0}^{15}q_α²=64.                (1)

The maximum possible q² in each interval is attained at an endpoint. Two separately written complete native programs, each on one core, scanned every `binom(496,4)=2,491,434,660` outside set in the same deterministic order. They agreed exactly:

| Classification | Outside sets | Reason |
|---|---:|---|
| At least one empty local-Walsh interval | 2,488,973,045 | One frequency class is already impossible |
| All intervals nonempty but Σ of their maximum q² <64 | 2,461,615 | Contradicts (1) |
| Boundary/inconclusive | 0 | No remaining set |

The first implementation independently computes direct outside sums and scans their 32 frequencies per class. The second independently computes the outside sums, then represents the four ±2 perturbations by 32-bit bit-sliced masks; it checks all 16 binary inputs of the bit-slice count logic before scanning. Both receipts say `complete=true`, `timed_out=false`, 2,491,434,660 tested, and 0 inconclusive. Their exact agreement is stronger than the earlier 43,465,728-set local-bitset prefix, but they share the same pinned seed and fixed affine-flat definition; this is not a cross-vendor or human review.

For zero outside changes, `frontier-20261028-affine-core-caller-v1.md` (SHA-256 `e12099f6140b5cf487eb60dd05adbefd9d47d00b3b07f57a815a1e826bcf53ab`, 85 LF) gives exactly 448 peak≤28 core restrictions and proves all are Walsh-zero-free. `frontier-20261028-outer-two-obstruction-v1.md` (SHA-256 `79162dcb01a82c811740126a83e5f88de9eb50a2c06e24fac3779b406345492d`, 60 LF) covers one/two outside changes; `frontier-20261028-outer-three-obstruction-v1.md` (SHA-256 `cbca432c7f870b89197f598dcf2fe8161c084303c997b1d9fb292c57b91770ad`, 40 LF) covers all three for seed 1. Each retains its own author/review status. Affine addition permutes/signs Walsh coefficients and therefore cannot lower an excluded peak or create a zero in a zero-free spectrum.

## Pinned evidence and actual executions

All paths below are in this exclusive `balanced-nl242` root; filename prefix `frontier-20261028-` is omitted. The source seed file is SHA-256 `116ab5a7709dd35d951ddc878af227e5e05ce269d8293e5c0c269e158bd051f2` (6 LF). Its published-source identification and exact truth-bit convention are in `frontier-20261028-two-flip-report.md` SHA-256 `375d9034c03b6b469878a4cd74435dc37e8a6f7ba450ff12d71ee0853d04314d`, 74 LF.

| File | SHA-256 | LF | Role |
|---|---|---:|---|
| `check-outer-quads.cpp` | `699a7ad78345a5af9ca719baccda02e8c62c4df4c7ff83c74f64b174a8648b4e` | 137 | Direct scalar interval/energy scan |
| `check-outer-quads` | `7354dd2f36295b03b5784b440fb205a3afa5cd5fcc0c974d96b56a4847554eec` | — | Actual compiled executable |
| `check-outer-quads-seed1-full.json` | `0512226e3d2e9f906e449931869a79be1de2e5ae17033b5e9dea9ebfc88364ea` | 14 | Complete first receipt |
| `check-outer-quads-bitslice.cpp` | `15f0cbd39037b61d56586ab5dbd0b6a134a732eb67cc1f36556cddfb2932c8dc` | 167 | Independent bit-sliced scan and controls |
| `check-outer-quads-bitslice` | `479f0e27f8f1e17257d1541373e4e1735eab9d2471a0e06ac4061b0e808efc0f` | — | Actual compiled executable |
| `independent-outer-quads-seed1-full.json` | `bdc5b29b2ba156d6431a940ac6e7d7b3f489282c27ef329d6fb505555ad2d529` | 16 | Complete independent receipt |

Both programs were compiled with `/usr/bin/clang++ -std=c++17 -O3 -Wall -Wextra`. The direct and bit-sliced complete runs reported respectively 113.026 s and 57.3657 s program time. Source/receipt hashes bind their outputs; they are finite computations, not a formal proof assistant or broad literature audit. All original rank/weight alternatives and `(24,24,2)` remain open. **END.**
