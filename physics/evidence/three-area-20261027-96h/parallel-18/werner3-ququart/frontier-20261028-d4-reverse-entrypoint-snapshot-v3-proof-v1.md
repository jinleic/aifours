# Full reverse-CRT identity from a verified entrypoint byte snapshot

**PhysicsResearch96h-2 / physics-1.** Native clock at receipt-comparison observation: Wed Oct 28 19:50:48 PDT 2026. This new same-target run binds the verifier entrypoint itself as well as its transitive helpers/data to the bytes actually passed to `compile`, subject to the explicit shell/Python/hash/OS/runtime trust boundary. It is not a human/other-model-family review, formal/Lean proof, physical operational consequence, all-d theorem, novelty claim or parent/f62 adoption.

## 1. Exact observed launch and byte chain

The earlier v2 full run separately verified helper/data byte snapshots but its own entrypoint was launched by filename; matching pre/post hashes alone did not prove which bytes Python read. That limitation remains disclosed in the immutable v2 proof `frontier-20261028-d4-reverse-snapshot-crt-v2-proof-v1.md`, SHA256 `9a75a1f50adb28aedf493f1f764cf378bcf6522398c9b9d4da9cfe1de9872d66`. The new v3 launch takes a different, prospective route; it does not retroactively alter v2 or the earlier unpinned v1 data-loader record.

The **actual** one-process invocation in the owner root was:

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -c 'import hashlib,pathlib,sys; p=pathlib.Path("frontier-20261028-d4-reverse-entrypoint-snapshot-v3-launcher.py").resolve(); b=p.read_bytes(); h=hashlib.sha256(b).hexdigest(); h=="dc5f3f4609b037f51b81155cbcdc7c7c6ca9ed5d8178b83eca50dbd7cddb697e" or sys.exit("launcher snapshot mismatch"); d={"__name__":"__main__","__file__":str(p),"__launcher_snapshot_sha__":h}; exec(compile(b,str(p),"exec"),d)'
```

Thus the **actual command text** first reads the launcher bytes, verifies SHA256 `dc5f3f4609b037f51b81155cbcdc7c7c6ca9ed5d8178b83eca50dbd7cddb697e`, and passes those same bytes to `compile`. That pinned launcher in turn reads and verifies the exact v2 entrypoint snapshot SHA256 `425e5d827f1f4a9592732a124b5f791ebef90148c114084696131c81b9d7f971`, compiles **those bytes**, overrides only its output/progress paths to new v3 names and invokes its `main`.

The v2 code itself loads every mathematical helper, including the previously unpinned data-only base helper SHA256 `bb9cf61ea6a26c0eb4570cd28abf2c26c94f64a4054640902f84ba8e4aff69ec`, from individually hash-checked in-memory byte snapshots. It also reads and checks the public archive/member, corrected-data bytes and prime-list receipt before using those snapshots. Its post-run helper-path rechecks and the launcher's post-run entrypoint-path check passed. These checks bind **the actual bytes provided to compile** under the recorded invocation, assuming the shell, Python, hashing and runtime execute the displayed code correctly; they are not external attestation, independent human review, or proof that the OS/runtime is uncompromised.

## 2. Exact full run and distinct receipts

The program's actual wall-time receipt reports start `2026-10-28T19:47:38-07:00`, finish `2026-10-28T19:50:17-07:00`, return code0. The v3 mathematical computation reported **158.607 s**; the prior filename-launched v2 result reported 161.507 s. The v3 launcher/outer command wall result was 158.76 s.

- Launch receipt `frontier-20261028-d4-reverse-entrypoint-snapshot-v3-launch-receipt.json`, SHA256 `8c92e424d87c9b372bb4ba5a303b07401642db69a9e491162f262030f1910350`.
- Full mathematical result `frontier-20261028-d4-reverse-entrypoint-snapshot-v3-results.json`, SHA256 `50f53a57e59eda9f40bb28ba2df1feb9ace8ce43e3a2d60530b1db8a34c95687`.
- Final progress `frontier-20261028-d4-reverse-entrypoint-snapshot-v3-progress.json`, SHA256 `5e7b5b7ce715a27e132d54844e895550509d78d7adaefbbb6898384275618810`, explicitly **PRIMES_COMPLETE /424**.

The new run recomputed all **4675 source-orbit residuals for each of 424 distinct trial-verified denominator-safe primes**, with zero nonzero residues. The exact common denominator D has 6645 bits, fresh bound B has 6745 bits, product P has 6761 bits, and the exact integer comparison `P>2B` passed. The in-memory aab coefficient +1 control produced 1142/2391 nonzero residuals in its two affected families. This used the same alternate-row-matching/direct-canonical/reverse-axis implementation as v2, now with the entrypoint bytes snapshot-bound; it was not a new independent algorithm and not the earlier one-prime/two-projection diagnostic.

The standard-library receipt comparator `frontier-20261028-d4-reverse-entrypoint-v3-receipt-check.py`, SHA256 `bea6916036664d7b086d6407955087fa09ec7095e3613fdae2e5d1d5e16ab65e`, checked exact v3 versus v2 prime list, full B/P strings, source/map/count/zero-result fields and the v3 launch/progress binding; **all matched**. Result SHA256 `4af4bc3557aa563b38cb0fea2bb9a51732a211f9f8bd9f10b715f86cb9845752`, PASS; five incorrect B/P/base/entrypoint/progress controls were detected. This comparator did not rerun any residue.

## 3. Snapshot guard controls and exact inference

Before the v3 launch, `frontier-20261028-d4-reverse-entrypoint-snapshot-v3-fault-check.py`, SHA256 `79ad0ef4bc01b5fb522de6d26ba68dbd2648356d2f45cf1b0ac78161abbef583`, checked that the real v2 snapshot is accepted while modified launcher/v2 bytes and a caller lacking the verified-launch marker are rejected; actual source hashes remained unchanged. Result SHA256 `94550dfaeec9878f075806d2689011b9ed2f1d697049b257e2c2f03158a8b909`, PASS. Earlier v2 input guards separately rejected modified base/global/prime-receipt/archive/corrected-data byte reads, result SHA256 `822918d9ea00d4386389126fdd664d2d67dad4044c69c26af1cb09860645bd60`. These are in-memory guard controls, not physical examples and not a runtime-integrity proof.

The exact row-stabilizer reindexing and integer-height inequality are proved in `frontier-20261028-d4-reverse-crt-conditional-proof-v1.md`, SHA256 `d63142eec546a9ba936d04bbb4c994559a19b0af1028434af376c7662c652294`; all 17 source row rules /24 local permutations were independently checked in result SHA256 `2df48fdb47658bb87f2d1b1d82e54ed478bb95079142b8d877180de5083e06c0`. The B inputs, including all local maxima, were separately reconstructed using standard-library-only source/data code in the pinned stdlib CRT receipt and local-maxima audits.

For each integer-scaled source-orbit residual R, all 424 verified primes divide R and `|R|<=B<P/2`, so R=0. This conclusion is conditioned on the written source/group/bound reasoning, correctly executed pinned code and Python/NumPy/FLINT/hash/OS semantics. It is a full d4 **source functional identity**, not on its own an original physical theorem. The original complex-rank<=2 lift/trace objective, true jointly PSD physical Gram blocks, exact same-pair equality bindings, local commutant/source span and 1237 corrected PSD multipliers remain separate necessary inputs.

## 4. Review and process boundary

This new invocation occurred after Main actually read the prior cadence self-stop and explicitly gave prospective primary-work direction. The earlier 20/30-minute gaps, unknown cause and no continuous-supervision claim remain disclosed in `frontier-20261028-1904-cadence-breach-self-stop-v1.json`, SHA256 `8b794de4b92c3a50b497333ac1164ddb3800b17c9a8aa541eae57b104c60d24e`. No previous file is changed, and no future f62/reviewer scope is presumed. Same source data, independent local-reference helpers, Python/NumPy/FLINT and mathematical proof assumptions remain shared across our computations; this is neither independent model-family/human review nor a Lean/kernel proof, and does not establish all-dimensional or physical distillability claims. The pre-existing public paper already claims the target, so no novelty is asserted.
