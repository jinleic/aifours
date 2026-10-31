# Corrected d=4 three-copy certificate: actual replay and independent PSD check

Observed native clock before writing: **Wed Oct 28 17:16:25 PDT 2026**. Original physical target: arbitrary complex C of rank<=2 on `(C^4)^tensor3`, unnormalized partial traces, and

`q3(C)=||C||HS²−(1/2)Σ_i||Tr_i C||HS²+(1/4)Σ_(i<j)||Tr_ij C||HS²−(1/8)|Tr C|²`.

The public Tomar v3 paper claims this entire inequality. This note records an ACTUAL bounded computation on its d4 data and explicitly distinguishes author-code replay from independently implemented predicates. It is **not** Lean-kernel/human/configured-family verification, a parent adoption, a new discovery, or an independent implementation of the entire orbit identity.

## Reproducible inputs

- Public primary package: [Zenodo record 23682914](https://zenodo.org/records/23682914), `release_ep3.tar.gz`; local `frontier-20261028-tomar-release-ep3-v3.tar.gz`, SHA256 `2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3`. Package MD5 `704bae52c2083bf81b5c11332415b3d4` matched the public record.
- Archived package member `release_ep3/certs/ep3_perd_d4.pkl.xz`, SHA256 `0eccbad8fc2f65954a6a7038094e7c6deb9259852aef3c406f5421a4a649194f`.
- Author `ep3core.py` SHA256 `0f0d84a9ce257edbf9b0b6cbbff2690041fbd6aad18d139c8845e8edf547d450`; author `verify_perd.py` SHA256 `98311b321bad13d2c2ea7d4b5469cc7c3ca519b96da17f78d74118297e7e1d62`.
- Harness `frontier-20261028-d4-author-replay-and-independent-psd.py`, SHA256 `886bfabbf2a7b40fa44abdf67e1be52358059d54fbda512937f0c884296fa720`.
- Exact exported corrected multipliers/equality coefficients `frontier-20261028-d4-corrected-multipliers-and-equalities.json.xz`, SHA256 `c70c12a06273faa34bed204268188ee8c6b1732f07b2ceda453f163676024f94`, **3,824,508 bytes**. All entries are decimal numerator/denominator strings, not floating point.
- Machine-readable results `frontier-20261028-d4-author-replay-and-independent-psd-results.json`, SHA256 `de4a897846fcd76ec27820d539ebc65cd18f55f2e405dd89e284c4c6341b27d7`.

Python3.14.3 / numpy2.4.3 / python-flint0.9.0; one verifier worker, `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`; total wall output **438.40 s**, result's own elapsed **438.241 s**. Public code was first inspected, then executed from the SHA-checked archive. The harness forbids pickle global/class loading, intercepts access to the single in-memory pinned certificate, and adds only a capture call at the original verify-function return. The source's certificate generation/construction code was not executed.

## Actual author-verifier execution

The pinned author verifier, running locally rather than merely reading a published log, reported:

1. d=4, **1237** block types, **272** initial equality multipliers and **2634** selected correction rows/coordinates.
2. The approximate base-certificate residual was reported as `9.728e-34` in a diagnostic float print. This is not evidence of exact identity.
3. The exact selected-column reconstruction used three primes with author-computed height bound2^69; the exact rational correction has **2634** coordinates and maximum denominator bit length **6609**.
4. After correction, the author code recomputed **all 4675** source-orbit residuals using exact rational arithmetic: **0 nonzero**.
5. Its exact characteristic-polynomial test reported **0 failed out of1237** corrected multipliers and `EXACT CERTIFICATE AT d=4: PASS`.

The corrected equality dictionary contains **329** entries after the correction, rather than the272 initial stored entries. This is reported as the observed post-correction count; it does not by itself establish a discrepancy in the source.

## Independent final PSD calculation

After the author computation, and before producing the saved result, the harness passed **all 1237 final corrected rational matrices** to the independently written `Fraction` Schur-complement elimination in `frontier-20261028-independent-d4-base-check.py`, SHA256 `bb9cf61ea6a26c0eb4570cd28abf2c26c94f64a4054640902f84ba8e4aff69ec`.

For an exactly symmetric rational matrix: a negative diagonal fails PSD; a zero diagonal with any nonzero row fails PSD; a positive diagonal pivot leaves PSD equivalent to its exact rational Schur complement. Iterating includes zero/singular pivots and performs no eigenvalue rounding. The actual independent final check took **314.693 s**, found **zero failures**, and agreed with all1237 author characteristic-polynomial outcomes. The exact same final matrices and329 equality coefficients were serialized after this check in the pinned xz artifact above.

This **resolves the previously missing final-PSD predicate for these computed rational matrices**, subject to correctness of Python's exact integer/Fraction operations and the script. It does not, by itself, establish the certificate identity or physical validity.

## Independent support already exercised

The companion report `frontier-20261028-d4-source-data-audit-v1.md`, SHA256 `1240320c5357e34d75c1206056aa072b3758e461c948398fe4e6264b1b1aa566`, records actual independent checks of all used d4 site, auxiliary and equality local maps, all objective words and the complete source-orbit partition. The source-level aggregation reconstruction is in `frontier-20261028-d4-global-aggregation-source-walkthrough-v1.md`, SHA256 `a8e81561b71e18b30b7e52ce082d7ffad2e90673cec39088ab2fe9a63af01185`. These are separate from the author-code residual execution above.

The full original trace/swap polynomial caller was additionally checked coefficientwise on every subset and all mixed factor-column entries: script SHA256 `fc70405ca23ebb76ca08d4539ff0251db4760a4614b0a3367995cb7c0086b5f6`, result SHA256 `ea9eff59833ccdd487a1ca4ace3b56f05c54a2b7711e1d09b7e8b5bfa130bf99`; 131072 formal term occurrences, no mismatch. That check verifies normalization/identity, not nonnegativity.

The paper's AppendixA V17 multiplier-count description remains a documentary inconsistency for d3/d4 as detailed in the companion report; it is not a falsification of this actual d4 check.

## Residual trust and pending independent identity

The **author's** exact global orbit-residual code produced zero on all4675 rows; it is not described as independently reimplemented here. Site/equality/objective/orbit finite comparisons and the mathematical source walk-through reduce, but do not erase, that shared-code trust boundary. The exact source-space/physical-moment validity argument, proper Gram/equality class matching, runtime libraries and code are still subject to independent scientific review. No statement about d≠4, general physical distillability, global source priority, Lean rebuild or theorem adoption follows from this computation.

A separate one-worker checker independently reconstructing the full exact global orbit identity from the pinned corrected values, literal local maps and an independent orbit partition is now running with a fixed time bound. Its status is **pending**, not passed or failed at this note's timestamp. Previously held records remain historical/unvalidated; none was used as a premise or relabeled successful.
