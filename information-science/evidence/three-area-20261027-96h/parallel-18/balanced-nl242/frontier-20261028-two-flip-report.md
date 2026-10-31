# info-6 frontier: exact two-flip neighborhoods of three published NL-242 functions

Native `/bin/date` observed before writing: **2026-10-28T17:05:49-0700 PDT**. Original target: an actual balanced f:F₂⁹→{0,1} with max|W_f|≤28, equivalently nonlinearity ≥242, or a universal no-go. **Result: a separately checkable exact finite-neighborhood obstruction and three actual balanced NL-240 functions; neither solves the unrestricted target.** No novelty, exhaustive-global-search, formal/kernel, independent-model or external-human-review claim is made.

## Source and normalization

The input is the three 512-bit hexadecimal tables in §3.1 of Kavut and Yücel, [*9-variable Boolean Functions with Nonlinearity 242 in the Generalized Rotation Class*](https://arxiv.org/html/0808.0684v1), arXiv:0808.0684v1. They report unbalanced NL-242 functions and explicitly note that their presented spectra have no zero. Our local input preserves the printed table bytes, reads hex left-to-right with the high bit first, and labels the resulting truth bits f(0),…,f(511). This exact bit convention is explicit; we do not infer any unverified equivalence of alternate encodings.

For every seed, the independent verifier computed **all 512 Walsh coefficients twice**: direct 512×512 character sums and iterative FWHT, then checked the exact 512-entry Boolean inverse and Parseval. Results:

| Seed | Weight | W(0) | max |W| | NL | Walsh zeros | Absolute Walsh histogram |
|---|---:|---:|---:|---:|---:|---|
| 1 | 250 | 12 | 28 | 242 | 0 | {4:30, 12:46, 20:226, 28:210} |
| 2 | 250 | 12 | 28 | 242 | 0 | {4:30, 12:46, 20:226, 28:210} |
| 3 | 242 | 28 | 28 | 242 | 0 | {4:30, 12:46, 20:226, 28:210} |

Thus none is balanced, and no affine addition alone balances it: W_{f⊕(a·x+c)}(0)=(−1)^cW_f(a).

## Complete two-flip/affine-neighborhood result

For **each** seed, exhaustively inspect all 130,816 unordered pairs of distinct truth positions; complement those two bits, then consider **every** affine linear term a·x and either affine constant. The deterministic search reports:

| Seed | Pairs inspected | Pairs admitting a balance-making affine twist | Pair/twist incidences | Minimum peak among balanceable pairs | Pairs meeting peak≤28 |
|---|---:|---:|---:|---:|---:|
| 1 | 130,816 | 130,772 | 994,590 | 32 | 0 |
| 2 | 130,816 | 130,702 | 994,590 | 32 | 0 |
| 3 | 130,816 | 130,782 | 994,590 | 32 | 0 |

Each balanceable pair in these complete neighborhoods has peak **exactly 32**. Counts of pair/twist incidences are not claimed to be counts of inequivalent functions. The bound is only on these three named finite neighborhoods; it does **not** exclude any other Boolean function, affine class, larger-distance modification, rank or weight type.

Proof of the search reduction: if signs at two distinct truth positions x,y are flipped, every Walsh value changes by

    W'(a) = W(a) − 2s(x)(−1)^{a·x} − 2s(y)(−1)^{a·y}.

The change lies in {−4,0,4}. Since each input spectrum is zero-free and divisible by 4, a new zero can occur only at one of its original |W|=4 frequencies. Every such zero is checked; each yields a balanced function by the affine twist indexed by that frequency, and the twist merely permutes the full Walsh spectrum. Conversely every balancing affine twist corresponds to such a zero. A one-bit flip changes all seed coefficients from 0 mod 4 to 2 mod 4, so no affine twist can make it balanced; zero flips have no spectral zero. Therefore the finite computation covers **all** modifications of at most two bits plus all affine additions, not only the emitted examples.

The C++ search computes each spectrum by FWHT, checks the stated preconditions, uses the exact two-flip update, and computes the full resulting spectrum for each balanceable pair. A separately written Python implementation recomputes each seed spectrum by direct character sums and recounts **every** pair using independent 512-bit zero/violation masks. All reported counts and histograms agree exactly. For a peak-28 seed, a pair can exceed 28 only at an original peak; the checker also computes the full peak whenever no peak-violation mask is present. Neither implementation uses a prior candidate's spectral result as its seed input.

## Three actual balanced examples, independently checked

For each seed, the search emitted the first minimum-peak pair and one balancing affine twist. The emitted 512-bit tables were independently checked by the direct-sum/FWHT verifier, including all Walsh values and exact inverse. A separate relation checker reconstructed each table from its source, both flip positions and twist; an in-memory one-bit corruption was rejected for the intended relation-mismatch reason.

| Candidate | Flips | Twist frequency | Weight | W(0) | Peak | NL | Walsh-zero count |
|---|---|---:|---:|---:|---:|---:|---:|
| seed 1 neighbor | (0,1) | 155 | 256 | 0 | 32 | 240 | 6 |
| seed 2 neighbor | (0,1) | 54 | 256 | 0 | 32 | 240 | 8 |
| seed 3 neighbor | (0,1) | 2 | 256 | 0 | 32 | 240 | 10 |

These are genuine balanced Boolean tables, **not** NL≥242 witnesses. Their full Walsh vectors and per-table digests are preserved in the separate audit JSON files below.

## Reproducible evidence and scope

All paths below are in this exclusive `balanced-nl242` root. SHA-256 values were obtained from the actual written bytes. All receipts refuse overwriting.

| Artifact | SHA-256 | Role |
|---|---|---|
| `frontier-20261028-published-seeds.txt` | `116ab5a7709dd35d951ddc878af227e5e05ce269d8293e5c0c269e158bd051f2` | Exact printed source inputs and convention |
| `frontier-20261028-verify.py` | `3eab1464d222b017034ee709fb163fe216047533f4f164342bdd1126e8c4a8ca` | Full direct/FWHT/inverse checker |
| `frontier-20261028-published-seeds-audit.json` | `9da2d8be33f025e1446d2424d51bd58622bbedc51038c9d766ec4331621863ee` | All source spectra and checks |
| `frontier-20261028-two-flip-search.cpp` | `a223b6e627edcae410dbaa5759818e86a1d513cc5535bc61f736f0715493e009` | Full finite search source |
| `frontier-20261028-two-flip-search` | `4c847c3ec12879e1895e799b782af6312e66c058dcc707bf5e36e15292c09efc` | Actual native compiled binary |
| `frontier-20261028-two-flip-results.json` | `ff1b7677bb7c33abe204da29883fb93f68e88c43434024b690132438d17204b8` | Counts and complete peak histograms |
| `frontier-20261028-check-neighborhood.py` | `0a28a7e6bfe6512ad2986d042a2dcfd1dd120b691252ac9e4eb10eaa9e26ae31` | Independent direct/bit-mask recount |
| `frontier-20261028-independent-neighborhood-audit.json` | `a90ce7406db14f0ae5067cea2419da4b89dadda10d8d510c7dbcd745af058d1e` | Recount: zero mismatches |
| `frontier-20261028-check-candidate-relation.py` | `905a9b0b6d3ab4f496b95c09f136ddb9b88c2051b98b8a52bf4ac6f4406400da` | Independent relation/mutation checker |
| `frontier-20261028-candidate-relations-audit.json` | `7dc840a73743ae73d169691736150b6dd3a50e431998973c146e172b859822eb` | Three relations plus negative controls |
| `frontier-20261028-best-seed1.json` | `e9c627063ecb63d3bdd13c1fe5fcc4805c5c47f9127498ea8548b11d9fcbb6bd` | First balanced truth table |
| `frontier-20261028-best-seed1-audit.json` | `a3809e9834d9dba744d8daafbb200973d4da2bd19c7e6c84c96263d6bc534bf3` | Its 512-Walsh verification |
| `frontier-20261028-best-seed2.json` | `5cb86accf72485f05d4030c4bb329e8f0a685c01e7b7dc3cc6a127b182fa94cc` | Second balanced truth table |
| `frontier-20261028-best-seed2-audit.json` | `e5a72ea406206cdd6dd56e6d8bd63ffb20067d9729dbf52f0522b775ac475016` | Its 512-Walsh verification |
| `frontier-20261028-best-seed3.json` | `1a5edc131241c76b3b30380aa8cbcfdd13ec0353035400262b502351ee89ef96` | Third balanced truth table |
| `frontier-20261028-best-seed3-audit.json` | `bf76fcaea3b8490b36279df147141cd88cf987b4ec1990c5de00fa0af198b945` | Its 512-Walsh verification |

The native search was built with Apple clang++ `-std=c++17 -O3 -Wall -Wextra`; the bounded run inspected 392,448 distinct pairs in total and returned in 1.35 s. Python source/neighbor audits, independent bit-mask recount, and three intended-reason relation mutation controls all completed successfully. The source-only published claim, finite computation, actual balanced tables, and original unresolved existence are distinct. Previously quarantined outputs were not treated as accepted premises. Owner-approved scientific work resumed only at the actual **17:00:27 PDT** observation; no continuity across the preceding gap is inferred.
