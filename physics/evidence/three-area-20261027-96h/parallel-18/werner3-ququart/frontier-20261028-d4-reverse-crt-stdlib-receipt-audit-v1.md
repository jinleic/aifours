# Independent standard-library audit of the d4 reverse-CRT bound and receipt

**PhysicsResearch96h-2 / physics-1.** Native clock at completed hash observation: Wed Oct 28 19:33:24 PDT 2026. This is an independent **input, integer-height, prime and CRT-receipt audit**, not an independent recomputation of the 424 orbit residuals. It supplements the actual reverse-CRT run and preserves its exact trust boundaries.

## 1. Independent actual input parsing and arithmetic

`frontier-20261028-d4-reverse-crt-stdlib-receipt-check.py`, SHA256 `42739c7337f31e71f09bd99479d8d5c65e50d46003b6d328d5d5935753441455`, uses **only Python's standard library**: tar/xz/JSON, exact integers, trial division and its own data-only `pickle.Unpickler` that rejects every global/class lookup. It imports no NumPy, FLINT, author source, owner global checker or reverse verifier code. It hash-pins the actual public archive/member, the corrected rational data, both prior and reverse CRT receipts and the reverse code bytes.

From the actual restricted source member and corrected-data bytes it independently reconstructed all 1237 type shapes and all 329 corrected lambda entries; the common denominator D; maxima of the scaled corrected multiplier/equality numerators; Wmax; `Cblock=Σ k_t² r_t² n_t²`; and `Ceq=Σ_e number_of_signed_parts(e)`. It independently computed the exact cycle-count objective bound Cobj on all24 local permutations. It uses **Amax=256 and Emax=24 as separately checked inputs** from the pinned literal local-map and reverse-verifier audits; it does not independently rebuild those maps here.

It then computed the full integer bound

`B=24^4[Cblock·Zmax·Wmax²·Amax⁴
        +Ceq·Lmax·Emax⁴+Cobj·(D/2^31)]`

from those actual inputs. The entire exact B matched **both** earlier and reverse-CRT receipts. The separate written derivation of this bound and of the family stabilizer reindexing is `frontier-20261028-d4-reverse-crt-conditional-proof-v1.md`, SHA256 `d63142eec546a9ba936d04bbb4c994559a19b0af1028434af376c7662c652294`.

## 2. Exact actual receipt result

Actual `python3 frontier-20261028-d4-reverse-crt-stdlib-receipt-check.py` returned **PASS in 0.692 s**. Result `frontier-20261028-d4-reverse-crt-stdlib-receipt-check-results.json`, SHA256 `7bce133f03f197080706134867b13c514d994f9b9e3a29cb302657be2b2862b3`:

- **1237** source/corrected types and **329** corrected lambda coordinates; D has **6645 bits**.
- Fresh exact source factors: `Cblock=278530617`, `Ceq=433`, `Wmax=771160`, `Cobj=1438646272`; separately checked inputs `Amax=256`, `Emax=24`.
- Fresh B matches both pinned receipts exactly and has **6745 bits**.
- All **424** listed moduli are distinct trial-division primes and do not divide D. Their independently multiplied exact product P matches the reverse receipt, has **6761 bits**, and satisfies **P>2B**.
- In-memory **duplicate-prime, composite-prime, incorrect reported-bound, incorrect product and insufficient-product** controls were each rejected by the same corresponding receipt guards. No physical state or certificate file was changed.

The program checks that the pinned reverse receipt actually reports zero bad primes, zero first-prime residual counts and PASS. It does **not** recompute the 424 reported residuals. Thus this second stdlib audit independently supports the **integer bound and CRT inference**, but the full zero identity still depends on the actual pinned reverse verifier's per-prime computations, its independently constructed local maps/group sums, and the source-to-physical PSD/equality/lift arguments. The historical reverse progress JSON stopped at400 primes; the distinct final reverse receipt records all424.

## 3. Physical and process limits

The actual full reverse-source run is `frontier-20261028-d4-reverse-independent-crt-proof-v1.md`, SHA256 `4bbf5516fd7da524a301b4b5793a91cc0beb0c0e879cc9b33efb685c185efa82`; original d4 physical/source/PSD dependencies are in `frontier-20261028-d4-source-dependency-closure-v2.md`, SHA256 `124bd68bf23b52fe5b5b6db4173851b50f075c293d537dbb8fea7ed83680392b`, plus the newer owner-local map closure. This note does not establish a broader all-d theorem, a physical operational/distillability implication, a new discovery, human/other-model-family review, Lean/kernel proof, or parent/f62 acceptance.

This audit was performed after Main actually read the prior self-stop and explicitly released prospective primary work. The earlier observed cadence gaps remain recorded in `frontier-20261028-1904-cadence-breach-self-stop-v1.json`, SHA256 `8b794de4b92c3a50b497333ac1164ddb3800b17c9a8aa541eae57b104c60d24e`; no retrospective continuous supervision, causal explanation or automatic mathematical rejection is asserted. Historical held outcomes are not premises.
