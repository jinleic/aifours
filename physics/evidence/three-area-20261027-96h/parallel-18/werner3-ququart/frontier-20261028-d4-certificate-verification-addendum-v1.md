# d=4 certificate verification — standalone-data and mutation-control addendum

**Observed native clock before writing:** Wed Oct 28 17:24:01 PDT 2026. This is an ADDITIVE update to `frontier-20261028-d4-certificate-bridge-and-independent-identity-v1.md`, SHA256 `cc9a354a16b9d3abf6ac1ef8ff6fcc6e2041a88d435216b9d9b326a85f348a66`. That earlier file's pending-control/pending-saved-PSD statements were accurate when written and are not edited. The following are the actually completed results.

## 1. Standalone exact PSD bound to SAVED corrected bytes

Input `frontier-20261028-d4-corrected-multipliers-and-equalities.json.xz`, SHA256 `c70c12a06273faa34bed204268188ee8c6b1732f07b2ceda453f163676024f94`, was reopened directly and hash-verified. Script `frontier-20261028-independent-saved-d4-psd-check.py`, SHA256 `7e564331021ed9358d760b70d3491d7f7a2e212d19d63adabec41f247a912969`, independently parsed each rational numerator/denominator and ran exact FLINT fmpq symmetric Schur elimination, with explicit zero-pivot/nonzero-row detection. It imported no author verifier/global checker. Result `frontier-20261028-independent-saved-d4-psd-check-results.json`, SHA256 `90ede7f3ccf9bf65936beea96ca92ec49cabb367581cd0e384abb564bf34871a`:

- **1237/1237 symmetric positive definite**, zero PSD failures, zero singular PSD matrices.
- Actual elapsed **27.434s**, one process.

This supplies a direct binding between the PSD check and the same saved bytes used by the independent full identity checker. It is distinct from the earlier Python Fraction Schur check on the pre-serialization in-memory matrices, and from the author's characteristic-polynomial test; all are exact but share ordinary Python/FLINT arithmetic trust.

## 2. Before/after helper-byte-bound full exact identity replay

`frontier-20261028-d4-bound-independent-identity-replay.py`, SHA256 `8d93ffa48e1d829194dbbc95b9f7c8511179402cf80eb4313cd02330380f2d76`, checked SHA256 of the independent global script, its own independently authored base and local-map helper scripts, the downloaded public archive and corrected JSON **before and after** the exact computation. Every observed hash matched. The actual result `frontier-20261028-d4-bound-independent-identity-result.json` SHA256 `f806c12f6101662467c5ae936a2d1f7be413585aed203ca29bdf864cb5221270`; receipt `frontier-20261028-d4-bound-independent-identity-replay-receipt.json` SHA256 `eafbdac6dc650147a8c48658d7a2c4195f966be9e68e73ad4ff57f8f11c49914`.

Result: **zero exact residuals on all4675 orbit sums**, independently regenerated family counts1142/2391/1142, denominator6645 bits; actual receipt elapsed **70.059s**, one process. This repeats the **same** independently written implementation for artifact binding; it is not represented as a third independently developed verifier or a proof-assistant replay.

## 3. Actual deliberate fault controls

All faults below were applied **in memory only after verifying the original corrected-data hash**; no pinned source or certificate bytes were changed. A detected failure is an expected **checker-sensitivity control**, not a negative physical C or a counterexample to q3.

1. **All multipliers and equality coefficients zeroed:** independent global checker found **1137 nonzero family31** orbit residuals, expected FAIL. Control script SHA256 `ab1ebfbc0d13e173d205cce6e81af640e62c38460f9de221591627deff7fb72f`; receipt SHA256 `827c790535ede3f5ff91ba032b54c0bc27964ddadf8ec1ec1108eb765ecce522`.
2. **One single-row corrected 1×1 multiplier increased by1:** found **996 nonzero family31** residuals, expected FAIL. Control script SHA256 `b6d11ca7c8706fd638d4b2b2e29d19ea5bf3cccabda300f3b44aeee48c3ced5f`; receipt SHA256 `8874506ac65280b68aa25fd71bb35dc61a9b7fe6ef0dd210a93332295334ae51`.
3. **One coupled-Gram multiplier diagonal increased by1:** found **143 nonzero family31** residuals, expected FAIL. **One aab equality coefficient increased by1:** found **1142 nonzero family31 and2391 nonzero family22** residuals, expected FAIL. Both used the complete independently rebuilt4675-orbit identity, sequential one-process runs68.353s and68.394s. Typed-control script SHA256 `197369e00544352d6d287c4c63a4598a04a7250a521536308c91d93319d1d392`; receipt SHA256 `a12e0a9423408ddd19579a64d7141a61bbe983b46ed1affd657731d5b9c31612`.
4. **Physical trace/swap convention changed deliberately from S to its complement:** the separate formal coefficient checker found **32256 mismatched coefficients in EACH of eight subsets**, expected detection. Control script SHA256 `7ede0ec73080b813b8cd98ebfb3148d70264326f26a6f4fcd5059cfede45020e`; receipt SHA256 `a45c45bd0cf5c7f3647447703ee444e1f100b9ef4439106a00bf141db29731db`.
5. **PSD guard faults:** negative first 1×1 diagonal rejected, a zero-diagonal/nonzero-row symmetric matrix rejected, and the zero matrix accepted as PSD but not positive definite. Script SHA256 `d7bb7a241d526473eb2007c9095d8a774f3d57c2e310c48af8eca6a1feb29a03`; receipt SHA256 `9ee562b8bd740d42ee0540d5bdc6fbb49fc0be5dec0ec843fc4ae00e2958dd91`.

These controls test distinct positive-block, coupled-block, equality, objective/normalization and PSD-guard paths. They do **not** certify absence of every possible implementation error or replace independent mathematical review.

## 4. Current scoped mathematical evidence

The original q3 is unchanged: arbitrary complex C on `(C^4)^tensor3`, rank<=2, unnormalized partial traces. The conditional proof bridge, exact source-word identity and PSD witness are in the pinned preceding document. The evidence now includes independently implemented EXACT all-orbit identity on the same saved corrected data, exact PSD checks on every saved multiplier, validated physical trace/swap normalization, and the fault controls above.

If the named Schur–Weyl/source-validity arguments and trusted exact runtime behave as written, that concrete finite certificate proves the published d4 inequality. This is **computer-assisted written support**, not independent human/configured-family review, formal Lean/kernel acceptance, parent adoption, a new-discovery claim or verification of Tomar's all-dimensional/physical-distillability conclusions. The paper's V17 d3/d4 multiplier-count inconsistency is documentary only, as separately recorded. Earlier held outcomes remain historical/unvalidated; none supplies a premise.
