# Lemma U certificate package v4 — exact source-review disposition (2026-10-19T08:29:13-0700)

Answers /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/mols39-LemmaU-certificate-v3-source-codex-v1.prompt.stdout.txt, SHA2567b07cf45388d78f0e2d751d1935da40e626b32cd9e3f8902e44c5327be04e49e, HOLD.
ONE final successor package; all v1/v2/v3 sources and unreported v4 staging files are preserved. No execution,
compilation, AST/syntax checks, configs, producer/checker/mutant/expectation runs, search or validation are performed.
Only new source/text writes and source-byte hashing/comparison. GLOBAL HOLD stays in force.

## Final frozen source/index
|role|path|sha256|
|---|---|---|
|producer|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/cert_v4_producer.py|26f12c0d683dbc47c5b2955ddd8f5feb3dddd47f9ce06fcab9724dc0ad3c0cdf|
|checker I/O successor|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/cert_checker/cert_checker_v2.py|9056dccb429239686356cd44721c07255cbc7d0bf8501fd9fd2a057af4479c7d|
|mutants|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/cert_v4_mutants.py|f5d44e594c7c1eea3b53e4f0ae7b605cb94482364122b3603e1467ea10d5f007|
|expectations|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/cert_v4_expectations.py|a7d558db0099a2aff59d4ad7e33f197f89735198a8aae05233896736db84aab1|
|producer GO entry|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/cert_v4_entry_producer.py|66976b2542c993f8d3489ac168614637c396b2b3ffbc0f2c335cc15cc857b27c|
|checker GO entry|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/cert_v4_entry_checker.py|250b9b9513a891f7852e38d9dd9b1af363ff41aad4239287e62c89b47aa8a8c9|
|generator GO entry|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/cert_v4_entry_mutants.py|9e906c458b1a5f59e212409e4a94033b59314433f4d7e9a1a269ada89ff4b85d|
|expectations GO entry|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/cert_v4_entry_expectations.py|3ce56f8a91461035248d42a2d9ae00a57687d7fe3b855ffa10c569283ca9f844|
|contract overlay|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/lemmaU-cert-v4-contract-overlay-v1.md|d9783661e7d770c6d314ef76eb46377da9d6e98ca0a1775b46a6dbb98a2baeab|
|checker I/O contract|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/cert_checker/cert_checker_v2-io-contract-v1.md|f90c0c2b33ad29c689002182d1938878942cb39ec76433806c0845f902397711|
|run plan|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/lemmaU-cert-run-plan-v4.json|e398ada3f6fe2ea869ebb291ccec35c5ae07e572715e10dfc87e4c38f883699b|

The plan has18 explicit runtime-pin inventory entries: all eight algorithm/entrypoint files, actual anchor/DM21/nc9
raw inputs, nested nc9 provenance, format-v2, v4 overlay, checker I/O contract, and original certificate spec/erratum/
format-v1. Every entry is checked at runtime against actual bytes. THIS disposition map is review-only; it is not
claimed runtime-consumed. The plan's own hash is verified by the invocation. No circular self-hash assumption.

## New finding1 MAJOR — independent nc6 derivation: ADDRESSED IN SOURCE
cert_v4_expectations.py::derive_nc6 is NEW, standalone math from the definition, importing no generator, producer or
checker helper. check_generator reads actual pinned anchor bytes, hash-checks them, and passes them with actual source
certificate to apply_mutation. derive_nc6 independently:
1. parses raw G1 bytes, verifies shape/work bounds;
2. constructs every row-pair mod13 fibre in lexicographic pair/t order, each with3 columns;
3. decodes coefficient indices in base3 and reconstructs actual gauged vectors from certificate basis;
4. scans source failures in increasing order, verifies each old fibre truly fails;
5. selects the FIRST eligible point with any passing fibre and the SMALLEST passing fibre;
6. compares ALL manifest detail fields and actual mutant with this independently derived result.
The manifest's position/idx/new_fibre are NOT used as inputs to selection. The source-level counterexample
{position:0,idx:0,old_fibre:0,new_fibre:1} cannot pass: point0 is the zero vector, so all fibre differences are0,
no fibre passes, and derive_nc6 must skip it. This is proof about source, NOT an exercised test.
EXPC therefore cannot accept the old counterfeit nc6 construction. Final claim barriers remain unchanged.

## New finding2 MAJOR — actual capped checker reads: ADDRESSED AT I/O BOUNDARY
Selected repair: MINIMAL CAPPED-READ CHECKER REVISION, no snapshots or additional retained files.
Scientific checker base e7e84962... remains unchanged. New checker source /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/cert_checker/cert_checker_v2.py SHA2569056dccb429239686356cd44721c07255cbc7d0bf8501fd9fd2a057af4479c7d changes input/output
boundary only. Scientific slice FORMAT_TAG through compute_facts is byte-identical:17,671 bytes,
SHA256b2b8719207d7375189b982feacf0b8409220db14dab39d2da575f036009d9e56 in both files. This is a source-byte
comparison, not an executed checker result. Checks0..6, rank/basis/rainbow/coverage, schema, G1 and reason strings
are not altered. New imports os/stat, read_capped_input, run_checks read boundary and finish publication clock only.
- Open with O_RDONLY|O_NONBLOCK|O_NOFOLLOW; descriptor fstat must be regular before any read.
- Read <=cap+1 actual bytes in64KiB chunks; reject overflow even if the file grows after fstat.
- Path replacement after opening cannot redirect the descriptor. FIFO at opening cannot block (O_NONBLOCK) and is
  rejected by fstat, never read. Final symlink rejected. No separate stat() safety assumption.
- Hash and scientific parse consume the SAME returned bounded bytes. Raw1MiB, certificate8MiB, unchanged limits.
- Bad kind, overflow, I/O and budget errors -> ERROR2, not an intended INVALID/check1 control rejection.
- No copies retained as files; transient read buffers plus joined bytes <=2*cap payload (headers additional).
  Planned anchor cert <320000 bytes => transient reader payload <640000 bytes. Raw/supervisor overhead separately
  accounted; RSS256MiB remains independent, not a claim of measured memory.
Producer/generator/expectation pinned/raw reads also use descriptor-bound nonblocking capped readers.
Slow regular-file I/O still requires the independent supervisor deadline; no universal hard real-time promise.

## New finding3 MINOR — per-publication budgets: ADDRESSED IN SOURCE
cert_v4_mutants.py refreshes budget immediately before AND after EVERY mutant file and before/after manifest.
No later scientific output is written after detecting expiry. Producer already checked before cert; its final
report now refreshes budget before/after publication. Checker finish and expectation final result do likewise.
If expiry follows an exclusive write, never overwrite the retained evidence: return non-success, report expiry on
stdout; parent must reject any file/stdout mismatch. No artifact alone may override a nonzero exit/audit failure.
Error reports may still be attempted after an earlier failure, but never with a success status/qualification.
Regular-file I/O can stall; supervisor separately owns its wall deadline. No tests of budget paths have run.

## New finding4 MINOR — final GO cutoff: ADDRESSED IN SOURCE
All cert_v4_entry_*.py use the same template with a fresh monotonic check after EACH token read and after the final
extra-byte probe, immediately before leaving the120s gate. At/after cutoff -> silent97, before algorithm load or any
retained output. Thus readiness at119.9s followed by resumption at121s cannot authorize work.
Supervisor still owns startup deadline FROM SPAWN, including loading/GO/start; the child timer is additional, not a
substitute. The120s child wait +240s algorithm is NOT asserted to fit a300s wall allocation automatically; parent
admission and supervisor accounting include startup and enforce total300s. No unreviewed v7/v9 behavior assumed.

## New finding5 MINOR — full pin coverage: ADDRESSED IN SOURCE
Plan v4 runtime_pin_inventory is explicit. Expectations v4 derives the mandatory set (programs, top-level inputs,
format, format_overlay, nested input provenance, nc9 provenance), rejects an inventory that omits any required
path/digest or duplicates a path, then hashes EVERY inventory file. Modified provenance-v1.json or format-v2 bytes
make pin_mismatches nonempty and qualified false. Self-reported source hashes remain informational.
Runtime inventory includes checksum bindings for original spec/erratum/format, not only executable sources.

## Prior findings retained
- F1 original actual-artifact/schema/evidence safeguards unchanged; nc6 hole specifically repaired above.
- F2 fixed exact claim predicate still REQUIRED: literal anchorhash, actual cert hash, dimensions/rank,2 signs;
  qualified and final exit0 require claim true. Before anchor claim UNEVALUATED.
- M1 full prefix includes prior EXP artifacts and parent audits. No autochain. Every job needs exact GO.
  CHK-anchor GO must cite explicit parent AUDITED_PASS EXP-D audit, path+hash.
- M4 no-follow owned real job root/fchdir and fixed exclusive plain output names unchanged.
- M5 G1 grammar identical across algorithms/checker, same bytes hashed/parsed.
- m1 structured error mappings retained, abnormal outcomes never classified INVALID1 controls.
- m2 producer-only canonicalization with actual byte verification by gate retained.
- m3 nc10 retained: homogeneous basis scaling by2 passes check2 but fails check3 identity exactly.
All nc0..10 definitions, schema and intended scientific rejection reasons unchanged.

## nc9 full-review context, unchanged bytes
Raw /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/cert-controls-v1/dm39_anchor_mut_r1c0.raw
SHA256c620c0f7663f04cf0b00c7824250effb5b5bac62e893627ad505475572a26d15:
```text
0 1 38 0 0 10 29 10 29 0 0 20 19 38 1 0 0 1 38 13 26 0 0 37 2 32 7 0 0 17 22 30 9 0 0 18 21 8 31
1 16 23 4 35 0 0 4 35 23 16 0 0 8 31 13 26 0 0 16 23 5 34 0 0 7 32 12 27 0 0 38 1 11 28 0 0 15 24
0 22 17 25 14 25 14 0 0 11 28 17 22 0 0 22 17 13 26 0 0 34 5 2 37 0 0 23 16 36 3 0 0 6 33 20 19 0 0
0 17 22 13 26 22 17 9 30 4 35 31 8 33 6 20 19 37 2 20 19 17 22 23 16 1 38 15 24 26 13 28 11 29 10 24 15 26 13
0 38 1 27 12 13 26 1 38 21 18 25 14 28 11 8 31 8 31 7 32 16 23 38 1 17 22 19 20 6 33 26 13 26 13 35 4 33 6
0 23 16 16 23 3 36 13 26 19 20 24 15 10 29 34 5 11 28 11 28 38 1 22 17 23 16 26 13 31 8 18 21 21 18 26 13 14 25
```
Provenance JSON (runtime pin verified as nested provenance, not just a report label):
```json
{
 "created_at": "2026-10-19T06:43:24-0700",
 "created_by": "ContinueCFR21 kernel (data edit only; no program executed)",
 "derived_from": {
  "path": "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/controls-v1/dm39_six_anchor.raw",
  "sha256": "3c8dbe62da8705eb6e713e85dae4d2fbf303614b2254f832a7291fe2f38a882a"
 },
 "file": "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/cert-controls-v1/dm39_anchor_mut_r1c0.raw",
 "new_value": 1,
 "old_value": 0,
 "purpose": "negative control nc9_anchor_mutation for the independent certificate checker (check 1: not a difference matrix)",
 "sha256": "c620c0f7663f04cf0b00c7824250effb5b5bac62e893627ad505475572a26d15",
 "transformation": "row 1 (second line), column 0 (first token): value v -> (v + 1) mod 39; all other bytes identical"
}
```
Direct duplicate: column0=(0-1) mod39=38; column18=(38-0) mod39=38. First pair(0,1) fails, exact registered reason
"check 1: D is not a difference matrix (rows 0, 1)". No reliance on future CHK-anchor to establish this rejection.
Plan v4 also embeds these unchanged raw/provenance bytes and direct calculation.

## State
No new mathematical result or scientific scope. LemmaU remains CORRECTNESS_ACCEPTED_SCOPED_PARTIAL for the exact
anchor, computer-assisted. Corrected R1 equivalence accepted, both extension questions UNKNOWN. Six MOLS39/CFR6,39
OPEN. Certificate route unexecuted/unqualified. No producer/checker/mutant/config/EXP run; no launch permission.
Beta-route slice is PAUSED as requested, with its incomplete source state in cp-013; no beta search or calibration.
