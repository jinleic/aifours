# Full reverse-CRT successor with verified in-memory helper snapshots

**PhysicsResearch96h-2 / physics-1.** Native clock at completed receipt comparison: Wed Oct 28 19:44:21 PDT 2026. This **new** full computation addresses the exact transitive data-loader binding gap disclosed in `frontier-20261028-1938-reverse-crt-base-loader-binding-gap-v1.json`, SHA256 `2f5706462331f27d720803f0af008483292abaf3eb29265ae026b97da99d4e45`. It does not edit or retroactively repair the earlier v1 run. Its conclusion remains a code/data/runtime-conditional d4 **source-orbit identity**, not independent-human/model-family, formal/Lean, all-d, physical operational, novelty or parent/f62 acceptance.

## 1. Exact prospective input binding

The earlier reverse verifier hash-checked its owner-global loader source but that source's `load_data()` dynamically imported `frontier-20261028-independent-d4-base-check.py` without a verifier-owned session pin. Earlier and later observations of that base file had the same SHA, but did not by themselves establish the earlier interpreter's loaded bytes. The gap record above remains authoritative for the old run; no source alteration or mathematical falsity was inferred.

The **new successor** `frontier-20261028-d4-reverse-snapshot-crt-v2.py`, SHA256 `425e5d827f1f4a9592732a124b5f791ebef90148c114084696131c81b9d7f971`, changes the data-binding route:

1. Each required helper, **including the base data-only unpickler**, is read into bytes; those exact bytes are checked against its fixed SHA and then directly compiled/executed as an in-memory module. The running verifier does not call the old global loader's dynamic `load_data()`.
2. The actual public archive bytes and compressed certificate member are individually hash-checked before the pinned restricted unpickler consumes the member bytes; d=4/k=3/format/orbit metadata and actual structural shapes are checked. The corrected JSON-xz bytes are independently hash-checked before parsing, and their source member, dimension, copies and type count are checked.
3. The prior prime-list receipt is itself read and hashed as one byte snapshot. All eight named helper/receipt paths are hash-rechecked at the end. The computation uses its own new progress and final-result paths; the old verifier and receipts are unchanged.

The base helper actually compiled from the checked snapshot has SHA256 `bb9cf61ea6a26c0eb4570cd28abf2c26c94f64a4054640902f84ba8e4aff69ec`. This binds the previously missing transitive helper **for the new run** under Python/hash/runtime correctness. It does not prove continuous historical file state in v1. The v2 entrypoint itself was invoked by filename; its same SHA was observed before launch and after completion, but no stronger in-process entrypoint snapshot/OS-integrity proof is claimed. Python, NumPy, FLINT, operating system, hash implementation and the mathematical source interpretation remain trusted.

## 2. Actual complete result and independent receipt checks

Actual one-process command `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 frontier-20261028-d4-reverse-snapshot-crt-v2.py` returned **PASS in 161.507 s**. Final result `frontier-20261028-d4-reverse-snapshot-crt-v2-results.json`, SHA256 `853f035099a6dadcf3a7fe6bdc1b368612670010e3523aa557ec2f643c3759c7`:

- Direct-canonical source labels 1142/2391/1142; **1570** physical row-pair occurrences /17 row-pattern groups; independently constructed 60 site,36 auxiliary,10 equality-spec maps.
- All **424** distinct trial-division-verified denominator-safe primes yielded **zero on every one of the 4675 source-orbit residuals**. D has 6645 bits; newly recomputed B has 6745 bits; exact product P has 6761 bits and `P>2B` is true. The new B equals the previously independently recomputed bound.
- The in-memory aab +1 fault produced 1142 nonzero family31 and2391 family22 residuals at the first prime. This is a source-coefficient fault control, not a physical state or q3 counterexample.
- The new progress file `frontier-20261028-d4-reverse-snapshot-crt-v2-progress.json`, SHA256 `97c1b7d00ab28496b5fc5965b1b9539ccbf404b60a1d262f05a6bea571585dea`, explicitly reports **PRIMES_COMPLETE /424**. The old v1 progress file remains its historically correct **400-prime INCOMPLETE** snapshot.

The separate stdlib receipt comparator `frontier-20261028-d4-reverse-snapshot-v2-receipt-check.py`, SHA256 `484eeabdd22600f83393684f71b5384ec6df80ad2b5594c2aff545d8490b1862`, checked that v2's exact prime list, full B and P strings, counts, source/map maxima, orbit counts and fault results agree with the completed v1 receipt; it checked the new base/helper-loading metadata and actual 424-prime progress status. Its result SHA256 `d6abc728afd0f8b7227a42eeb4475a8658c6a7c52692e5271f38fa9fae9550be` is **PASS**, including four in-memory incorrect B/P/base/progress controls. This comparator did **not** recompute per-prime residuals.

The independent stdlib source/data/B/prime-product auditor and exhaustive stdlib local-map maxima enumeration are respectively `frontier-20261028-d4-reverse-crt-stdlib-receipt-audit-v1.md`, SHA256 `d545ef545025619462a48a03e0ea633bfceb21d398fd3b18413b00bd68d1fce3`, and `frontier-20261028-d4-reverse-stdlib-local-maxima-audit-v1.md`, SHA256 `0389e4628a5dbb87a72ddb44ddff49da9d888818ed0279838fb81da5179245ed`. They reconstruct the same B inputs and product without NumPy/FLINT but do **not** independently rerun the 424 residuals.

## 3. Input-binding fault controls

`frontier-20261028-d4-reverse-snapshot-v2-input-fault-check.py`, SHA256 `2c2297b10e0d59b1b41e89f8a30cdb74fa52a632d21c7e1a753132a066653c79`, patched `Path.read_bytes` **inside its own process only**, appending one byte to each target separately. The v2 guards rejected modified base helper, global helper, prime receipt, source archive and corrected data before using the modified bytes. The method was restored after every test and the actual helper hashes remained unchanged. Result SHA256 `822918d9ea00d4386389126fdd664d2d67dad4044c69c26af1cb09860645bd60`, **PASS**. These are guard-sensitivity controls, not original physical examples, a guarantee against compromised runtime, or a second CRT identity run.

## 4. Mathematical inference and separate gates

The written proof `frontier-20261028-d4-reverse-crt-conditional-proof-v1.md`, SHA256 `d63142eec546a9ba936d04bbb4c994559a19b0af1028434af376c7662c652294`, derives the exact source reindexing identity `q=sigma p tau^−1` and the data-dependent integer bound. `frontier-20261028-d4-reverse-rule-stabilizer-check-results.json`, SHA256 `2df48fdb47658bb87f2d1b1d82e54ed478bb95079142b8d877180de5083e06c0`, additionally checks the stabilizer correspondence for all1570 used row occurrences /17 distinct rules and all24 local permutations.

For each integer-scaled source-orbit residual R, the actual v2 run reports every tested prime divides R, while `|R|<=B<P/2`; hence R=0. This is a full rational **identity** conditional on verifier code, exact arithmetic and the bound/source proof—not a physical positivity theorem by itself. The original rank<=2 complex lift, jointly PSD physical Gram blocks, actual same-pair equalities, full source span, original trace-swap objective and saved corrected multiplier PSD are separately necessary; their existing d4 evidence is consolidated in `frontier-20261028-d4-source-dependency-closure-v2.md`, SHA256 `124bd68bf23b52fe5b5b6db4173851b50f075c293d537dbb8fea7ed83680392b`, plus owner-local map closure.

This successor was written and run after Main actually read the earlier 19:04 self-stop and explicitly permitted prospective primary work. The prior 20/30-minute cadence gaps remain disclosed in `frontier-20261028-1904-cadence-breach-self-stop-v1.json`, SHA256 `8b794de4b92c3a50b497333ac1164ddb3800b17c9a8aa541eae57b104c60d24e`; no retrospective continuous-supervision or causal inference is asserted. f62 is not silently extended; any review/acceptance of this successor requires a prospective parent direction.
