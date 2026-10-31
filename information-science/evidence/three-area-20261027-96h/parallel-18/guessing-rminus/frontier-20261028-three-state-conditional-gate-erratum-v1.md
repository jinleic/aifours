# REQUIRED BEFORE SOURCE: two-syndrome-dependent three-state gates

**Status: correction; no frozen source edits.** Read the erratum `frontier-20261028-two-syndrome-local-neighborhood-erratum-v1.md` SHA-256 `8ff79f6d07b935025e0b2f3de27928f030d251787724b64e05ccd9f1f012a37f` before any use of the purported global two-syndrome theorem. Its unrestricted proof has a missing local-neighbourhood hypothesis.

Consequently:

* In `frontier-20261028-three-syndrome-indicator-obstruction-v1.md` SHA-256 `789cc5d89adab8c4bea659837012a93380466f8dd3dd6d4b7d1143103214b6ac`, the four gated conditional bounds in formula (28) are **hypothetical premises**, not currently established necessary constraints for actual three-syndrome laws. The exact 14-variable polymatroid and its arithmetic checking remain valid as a countermodel to that precisely stated hypothetical gate system.
* The same qualification applies to `frontier-20261028-three-syndrome-exclusion-obstruction-v1.md` SHA-256 `22ade8c73049b9482123ca2a2277a6eb95e518585461bc5f712733886fbfc783` and its additive sandwich obstruction; their exact counterpolymatroid checks are unaffected.
* The sentence in `frontier-20261028-three-state-exclusion-entropy-v1.md` SHA-256 `9c5ee203ba255776702e93e90b958663e98a43ebfb3b522b97898381116785e7` stating that indicator split gates are valid is conditional on a future proof of the withdrawn two-syndrome theorem. The one-hot inequality itself and its KL proof make no use of that theorem and are unaffected. The upper-bound addendum is likewise independent.
* The first equivalence in `frontier-20261028-cubic-alphabet-syndrome-reduction-v1.md` SHA-256 `65db6316c76bfb0ef382c78dfb59f831ba450d5183e0c5121d0b3035b81c063f` remains valid after **removing** the `>=3 syndromes` conjunct: amplification and alphabet embedding use no two-syndrome bound. The strengthened three-syndrome equivalence is unproved.

Do not treat any of these corrections as a proof of the negation, or as an adoption, novelty clearance or formal verification.
