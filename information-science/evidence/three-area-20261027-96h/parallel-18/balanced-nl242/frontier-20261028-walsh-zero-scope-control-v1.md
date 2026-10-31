# info-6 frontier: actual balanced counterexample to dropping the peak hypothesis

Native `/bin/date` observed before writing **2026-10-28T18:08:07-0700 PDT**. This is an exact finite scope control for the author candidate `frontier-20261028-walsh-zero-structure-v1.md`, SHA-256 `5af3cf5e021e44211e566bce858752f6dbb1706181e001cc962a17d50d930937`, 70 LF. It does **not** refute that candidate under peak≤28, establish the best possible threshold, provide a target witness, or imply novelty.

The bounded SplitMix64 balanced-table generator (seed `20261028`) produced an actual Boolean table at its first draw with the following independently recomputed properties, using the explicit index convention a∈{0,…,511} as 9-bit vectors:

- truth weight **256**, W(0)=0: balanced;
- max|W|=**72**, nonlinearity **220**, 39 Walsh zeros: outside the peak≤28 hypothesis;
- XOR of all nonzero-Walsh frequencies is **286**, not 0;
- the |W|=16 layer has **49** frequencies and XOR **483**, so neither its size nor its XOR has the target theorem's claimed form.

Thus balance alone cannot replace the peak hypothesis in either of the two zero-structure conclusions. This single actual example says nothing about whether any balanced peak≤28 function exists.

The independent verifier computed all 512 Walsh values by direct character sums and by FWHT, compared them, and checked the full Boolean inverse and Parseval; the diagnostic checker separately XORed the **recorded direct-verified spectrum** and reproduced both stated frequency-set values. A mutated reported XOR was rejected for the intended mismatch.

| Artifact in this root | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-balanced-support-probe.cpp` | `1e0600cac15db3ba75b6279658786b2f6a012df0a3fd87b42d4a4481dded3f4d` | 79 |
| `frontier-20261028-balanced-support-probe` executable | `81383bd0d136769f3297bdba8739c78a5da4d9e890089503303dc0b707e75e19` | — |
| `frontier-20261028-balanced-support-probe-candidate.json` | `3d06a48205a8aaa76213b1bafa912e83f3432270f1a4aad76afbcc3df4c475f6` | 5 |
| `frontier-20261028-balanced-support-probe-result.json` | `230f5183dad7ad3b90c2e0ef1eb8a724011b2fd03bde377c1f1ce45f4e6e9347` | 12 |
| `frontier-20261028-balanced-support-probe-audit.json` | `c4cda3e6528c9c316966086868ad502831eeac7b8800a80f3a7f0b8af6d6caba` | 603 |
| `frontier-20261028-check-support-diagnostic.py` | `ae7d8cdc87056c41fd7801bdcfa7000c2d67eff88f0435dfbd0c397d0f942a9c` | 66 |
| `frontier-20261028-balanced-support-diagnostic-audit.json` | `f1e155c701c30e5195df220b08a87a0c0e9730843aa7429cadf254003e073f5a` | 13 |

The full-spectrum checker is `frontier-20261028-verify.py`, SHA-256 `3eab1464d222b017034ee709fb163fe216047533f4f164342bdd1126e8c4a8ca`, 114 LF. The two checks are local implementations, not a human, Lean/kernel or independent-model review. **END.**
