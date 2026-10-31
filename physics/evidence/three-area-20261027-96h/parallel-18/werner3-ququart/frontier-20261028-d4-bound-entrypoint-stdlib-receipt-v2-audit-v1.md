# Snapshot-bound standard-library audit of the v3 CRT receipt

**PhysicsResearch96h-2 / physics-1.** Native clock at completed observation: Wed Oct 28 20:03:52 PDT 2026. This is an additive standard-library arithmetic/receipt audit of the entrypoint-bound d4 reverse-CRT run. It does **not** recompute the 424 per-prime orbit residuals, prove physical q3, or constitute parent/f62, formal/kernel, human/other-model-family, all-d or novelty acceptance.

## 1. Precise improvement over the earlier stdlib auditor

The earlier `frontier-20261028-d4-reverse-crt-stdlib-receipt-check.py`, SHA256 `42739c7337f31e71f09bd99479d8d5c65e50d46003b6d328d5d5935753441455`, checked input files by SHA before and after, but separately re-read some paths when parsing corrected data and receipts. Its pinned source-member bytes were themselves hash-checked; nevertheless the exact bytes of each separately read corrected/receipt path were a runtime/input-binding assumption. Its original result remains unchanged and should not be retroactively described as consuming one indivisible set of verified snapshots. No source alteration, falsity or failed old arithmetic is inferred.

The new `frontier-20261028-d4-bound-entrypoint-stdlib-receipt-v2.py`, SHA256 `7c879e1c5968ccd367e21ee8589cd93c4bd951af615478c8ed321a69039dbec3`, obtains one byte snapshot for **each** pinned input, verifies those exact bytes, and parses the archive/member, corrected JSON-xz and all receipts **from those verified bytes** using only Python's standard library and a data-only unpickler. It also checks the pinned v3 launch receipt binds its actual v2 verifier bytes and v3 result/progress hashes, with 424 completed primes, before auditing the CRT arithmetic. Input paths are rehashed after computation.

## 2. Actually observed exact arithmetic

Actual `python3 frontier-20261028-d4-bound-entrypoint-stdlib-receipt-v2.py` returned **PASS in 0.704 s**. Result `frontier-20261028-d4-bound-entrypoint-stdlib-receipt-v2-results.json`, SHA256 `6cd369e8eec8ff69bcd248b66ed02ef5a3c596149f400fd68553076a6ea3dce5`:

- independently parsed **1237** source/corrected types and **329** corrected lambda entries from the verified snapshots;
- recomputed full integer D (6645 bits), `Wmax=771160`, `Cblock=278530617`, `Ceq=433`, corrected coefficient maxima and independent cycle objective `Cobj=1438646272`;
- with separately checked `Amax=256`, `Emax=24`, recomputed the **entire exact 6745-bit bound B**, matching both pinned CRT receipts;
- independently trial-divided all **424 distinct** primes, checked D-coprimality, recomputed the exact **6761-bit** P from the full list and verified `P>2B`;
- detected duplicate/composite primes, wrong bound/product, an insufficient product and an in-memory altered corrected-byte snapshot using the actual guards.

The separately authored stdlib all-local-entry scanner in `frontier-20261028-d4-reverse-stdlib-local-maxima-audit-v1.md`, SHA256 `0389e4628a5dbb87a72ddb44ddff49da9d888818ed0279838fb81da5179245ed`, independently supplies `Amax=256` and `Emax=24` from the source member bytes, which it itself hash-checks before unpickling. It scans all reverse-rule 60 site/36 auxiliary/10 equality specs and includes in-memory compression faults. Together the two stdlib computations independently reconstruct all stated B inputs, conditional on their code, literal-source interpretation and Python/hash runtime.

## 3. Exact inference and remaining assumptions

The audited B/P/prime calculations make the CRT implication rigorous **if** the full source-orbit residues are zero for every listed prime. This audit checks that the pinned v3 receipt reports that outcome but does **not** re-execute those residues. The actual source-bound full computation and its exact entrypoint/helper/data chain are `frontier-20261028-d4-reverse-entrypoint-snapshot-v3-proof-v1.md`, SHA256 `55cb4fe7ed7a950a8c78e6209d5ead4cfa7bbf3bf41efd02afb55da516753926`.

The present stdlib audit itself was launched by filename, and its own program/OS/runtime execution remains trusted; the source-to-physical complex rank<=2 lift, true PSD Gram blocks, original objective, same-pair equalities, commutant/source span and saved corrected multiplier PSD remain separate mathematical/computational prerequisites. No cross-family/human or Lean/kernel review, all-d result, physical operational consequence, novelty or parent/f62 adoption is inferred.

The v2 audit is prospective after Main actually read the 19:04 self-stop and allowed primary resumption. The earlier observed 20/30-minute cadence gaps, unknown cause and no continuous-supervision inference remain in `frontier-20261028-1904-cadence-breach-self-stop-v1.json`, SHA256 `8b794de4b92c3a50b497333ac1164ddb3800b17c9a8aa541eae57b104c60d24e`. No prior file is overwritten and no frozen f62 scope is silently changed.
