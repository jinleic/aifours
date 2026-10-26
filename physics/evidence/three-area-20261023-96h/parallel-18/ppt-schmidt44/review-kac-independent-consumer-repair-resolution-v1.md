# Kac independent consumer — bounded static repair confirmation

Observed record clock: `2026-10-23T16:19:55-07:00`. Reviewer: **PhysicsPPT44**. This immutable note is the parent-assigned follow-up to `review-kac-independent-consumer-v1.md`, SHA-256 `da52aa57f696147e8d81034b75e3e5956058b5189f0eae3e933302d7d8f6c932`.

**Verdict: both original MAJOR findings M1/M2 and original MINOR m1 are CONFIRMED CLOSED at the new pinned static-source/request scope. No remaining blocking defect identified in this bounded repair audit.** One nonblocking request-count wording residual is identified below. This is not a runtime pass, certificate reconstruction, proof-kernel verdict or execution GO.

## Actual read coverage and observed identities

The following files are under `information-science/evidence/three-area-20261023-96h/parallel-18/guessing-rminus/`, relative to `/Users/jinleic/repos/aifours`:

| File | Observed SHA-256 | Read coverage |
|---|---|---|
| `kac_level4_consumer_v3.py` | `f4c61e1fde2ddce3a7f6ea1902c27b749de8e7fa335d0f55723c46101b9c647b` | All **577** lines, not merely changed hunks |
| `kac_level4_definitions_v1.py` | `21819efb0f8564adbd408ff0d507262f3e5f624a40263d718c1f36f20b94e4de` | All **557** lines freshly read again; unchanged from original audit |
| `kac-level4-independent-admission-v2.json` | `4988489e82d513097d807fae15820c60e0051e32e598e764459113f547445749` | Complete raw JSON body |

Thus all **1134** current source lines were read. I also read all 52 lines of the author's `kac-level4-static-review-resolution-v1.md`. Snapshot hashes were independently obtained through metadata-only SHA-256 commands. Start observation: `2026-10-23T16:16:31-07:00`.

Exposure is explicit: I read the parent's proposed closure arguments before conducting this follow-up. This is a separate full static source reconstruction by the original audit author, not a blind review or independent runtime implementation.

## M1 — verified loaded core, not a later sibling-path hash: CLOSED

Consumer lines 7–18 import standard-library modules only; `m` starts as `None` at line 22. `ConsumerError`, `guard` and `require` at lines 36–60 are trusted local definitions and do not delegate authentication to an unverified core.

`load_verified_core` at lines 63–89 binds the exact nonsymlink sibling path, captures source bytes once, hashes that capture, and rejects a wrong expected digest at line 77. Only after that gate does it construct a fresh `types.ModuleType`, explicitly set `__file__`, compile the **same captured bytes** at line 82 and execute those authenticated bytes at line 83. No normal import, `sys.path` core lookup, cached core bytecode or source re-read lies between authentication and loading. The resulting loaded-file/hash binding is recorded and checked again at lines 477–480 before the core guard is configured or its mathematical consumers are used.

The consumer and interpreter source-pin gates at lines 471–476 are likewise local, before core delegation. Their trust still presumes the parent externally authenticates the admitted consumer/interpreter and exact command before launch; a self-check is not a substitute for that parent preflight.

The additional planned control at lines 435–438 invokes the **actual loader** with an intentionally wrong expected core digest and requires `DEFINITION_CORE_PIN`. The local source ordering places that rejection before compilation. This is a meaningful prepared bootstrap regression, not an observed rejection: no control or loader was run during this review.

## M2 — claimed-output initialization and truthful settlement: CLOSED

At lines 453–459, the deadline/minimal state exists before any output claim. The encompassing `try` begins at line 460; nonthrowing SIGTERM/SIGINT handlers are installed inside it at lines 462–463, before exclusive `mkdir`. Identity observations, path resolution and consumer/interpreter/core authentication now occur inside this protected region and **before claiming output**.

The explicit phases distinguish preclaim initialization, output claim, owned initialization and reconstruction. A preclaim pin failure, interruption, startup error or existing-output refusal has its own status/ownership treatment at lines 511–527. An existing directory is never written into. After successful exclusive `mkdir`, `claimed` is set without an intervening fallible initialization operation; subsequent guard, launch writing and reconstruction are all inside the protected region.

Finally handling at lines 528–572 does not call a deadline/core guard. It attempts an exclusive settlement file only when this process claimed output. Informational RSS/finish-clock errors are exposed in `metadata_errors` and cannot retain successful final status. `file_written` becomes true only after JSON writing and file close succeed. A settlement I/O exception instead records `SETTLEMENT_IO_ERROR`, emits a full stdout fallback and makes the final return nonzero. A partial or unavailable settlement file is therefore not represented as settled success.

Nonthrowing signal handling remains active through settlement, so repeated cooperative signals do not inject exceptions into this lifecycle. Recovery from forced termination, unavailable native I/O or loss of both filesystem and stdout capture is not promised. Those limitations are now expressly bounded by the request; they are not evidence that any interruption/settlement path has actually been exercised.

## m1 — implemented resource strategy accurately described: CLOSED

Fresh core reading confirms lines 315–320 assemble one weighted reduced-coproduct constraint dictionary and pass the whole system to one `LinearSpan`/Gauss–Jordan computation. Request v2's `resource_basis` now says exactly that: multiset components imply mathematical sparsity, **not an implemented explicit block-partition/solve loop**. It also labels RAM/output as estimates, file-size checks as post-read rather than pre-allocation bounds, native RSS as informational and 600 seconds as a cooperative cutoff rather than a measured completion guarantee. No mathematical algorithm redesign is required to close this original wording finding.

## Nonblocking residual and future consumption requirements

The request's `positive_control` prose still says “all15 actual intended-reason mutation controls.” This is the original mathematical/parser/coverage set; the new bootstrap regression makes the complete planned set **16**. The actual `real_consumer_controls` list, `control_count: 16` and consumer line 508 consistently require 16. This is a residual wording ambiguity, not a bypass or changed acceptance rule. A future parent consumption must require **64 reconstructed records plus all 16 actual intended-reason controls**, never only 15. No new source edit, test or execution is requested by this note.

The mathematical core is byte-identical, and the complete consumer read retains the original audit's explicitly scoped mathematical/import boundaries. This repair confirmation does not establish that the implementation terminates within its resource estimates, that any of the 64 certificates is correct, or that any of the 16 controls rejects as intended.

## Decision boundary

- Original **M1 CLOSED; M2 CLOSED; m1 CLOSED** for the exact snapshots above.
- No consumer/core import, compile, test, smoke, numerical/algebraic execution or mutation-control execution was performed. Only source/document reads, clocks, hashes and this owned-root note were produced.
- No author/shared file, Git state, environment, scheduler or runtime was changed.
- This note clears the **original audit's static repair objection only**. Parent must still freshly authenticate exact pins/command/interpreter/input metadata and aggregate resources, then independently decide whether to issue a new exact named GO.
- **Stage 2 remains NOT PERFORMED.** Stage 3 lower-level/invariant/written-import composition remains separate and incomplete. No full band, original book conjecture, formal/kernel acceptance or novelty clearance is granted.
- PhysicsPPT44's primary P44 target and normalized-N4 request remain independently unresolved/HOLD; this temporary review grants neither of them execution permission.
