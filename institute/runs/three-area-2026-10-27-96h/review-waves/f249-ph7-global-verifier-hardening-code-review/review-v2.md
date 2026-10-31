# F249 PH7 GLOBAL verifier hardening — same-harness code and process review

## Step 0 — exposure screen, before declared input bodies

In this fresh reviewer context I have not seen any serialized held, withdrawn, or ZERO body, formula, guide, or consumer of the phase-type math-1 slot or the f161/f162 held episodes. I have not opened `review-v1.md`; the parent reassignment describes its status only. This screen concerns the accessible reviewer context and is not a claim about inaccessible model training or other agents' histories. Held math-5 episodes are ZERO/NONINPUT.

## Disposition and scope

**Do not treat the unqualified hardening claim as established.** In the visible entrypoint and process evidence I find **0 demonstrated FATAL, 2 MAJOR, and 1 MINOR** issues, plus material **INCONCLUSIVE** points below. Zero demonstrated FATAL is not a finding that the omitted modules are free of fatal defects. The existing parent **NO GO** remains in force; the mathematical supremum remains **NOT_PROVED**. This review does not authorize an assay or adopt any global result.

This is a **fresh same-harness reviewer**, not a human review, independent-model-family review, formal/kernel verification, or novelty review. The manifest freezes only the parent NO GO, the author report, and the entrypoint source. The runtime, gate, environment guard, source binding, obligation engine, local wrapper, synthetic tests, mutation harness, and result files named in the report were **not** declared inputs and were not opened. Consequently, descriptions of their internal behavior and the reported test counts are author claims, not independently inspected or replayed evidence.

For compact citations below, `NO-GO`, `REPORT`, and `ENTRY` mean the first, second, and third frozen inputs respectively.

## Actual measurement and reading sequence

1. Opened `manifest-v1.json` first. Its long scope line was reread raw; that reread and the manifest SHA computation were requested in parallel. Full SHA-256: `7704d4153c1e1e5872e47fb8823dff252529bcac6a98651c48c6d31238ca5295`, matching assigned prefix `7704d4153c1e`.
2. **Before opening any declared input body**, ran SHA-256 measurement of all three paths and then `wc -c -l` for bytes and LF counts. Every measurement matched the manifest:

   | Input, in manifest order | SHA-256 | Bytes | LF |
   |---|---|---:|---:|
   | `institute/runs/three-area-2026-10-27-96h/review-waves/f203-ph7-local-to-global-schur-bridge-robustness-review/parent-no-go-and-caller-availability-v1.json` | `f0afb377ad352ef05a4a9249e8762eadd2737152ee0000348924350f45bd3108` | 4054 | 40 |
   | `mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/frontier-20261029-ph7-verifier-hardening-report-v1.md` | `2ffa3784f2dfb59383d6491a70e5ddaae7dbdaeff3e94e24a13d98287ae48d65` | 12862 | 53 |
   | `mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/frontier-20261029-ph7-global-verifier-v1.py` | `a77e8f0ad246ef4dd3c5a1a33eea40d385ba232fd75f2e8435219e5448d69ae7` | 10669 | 160 |

3. Read `parent-reviewer-reassignment-v1.json`, consulted the applicable local review guidance, and wrote the Step 0 exposure screen above **before** reading any declared input body. The reassignment retains the original status-only `review-v1.md` and explicitly substitutes `review-v2.md`; the former was neither opened nor modified.
4. Read all declared bodies in manifest order, in exact raw windows of at most 15 lines, including each final line:
   - `NO-GO`: `1-15`, `16-30`, `31-40`, scope only.
   - `REPORT`: `1-15`, `16-30`, `31-45`, `46-53`.
   - `ENTRY`: `1-15`, `16-30`, `31-45`, `46-60`, `61-75`, `76-90`, `91-105`, `106-120`, `121-135`, `136-150`, `151-160`.

No author verifier, test, obligation, or imported scientific engine was executed, imported, or compiled. No standalone fixture was run. No external search/model/API, Git, deletion, or infrastructure mutation was used. The only intended output is this review. **Deviation from the original manifest output name:** the parent reassignment required `review-v2.md` instead of `review-v1.md`; this is not a change to the frozen manifest or inputs.

## Findings

### M1 — Ambient interpreter and startup/import state is outside the demonstrated pin boundary

`ENTRY:9-15` imports `argparse`, `hashlib`, `json`, `os`, `sys`, `time`, and `pathlib` before any GO or environment admission. `ENTRY:32-42,46-48` then uses that already-running interpreter and its `hashlib` to hash and execute the runtime and gate components. Only later, at `ENTRY:83-98`, does it pin `sys.executable` and call the environment guard for the local dependency directory before importing SymPy. `REPORT:29` describes the inventory of local SymPy/mpmath package directories and a separately pinned Python executable, not a complete pinned Python standard library, startup hooks, import path, loaded modules, or native runtime.

A pinned interpreter executable and package subtree do not by themselves establish the provenance of Python startup/import state or all modules already used to perform the checks. A tainted or unintended ambient startup/import can affect the hash/checking machinery before the dependency guard runs. This is conditional on the actual launcher/environment; the unseen gate or external controls may impose further restrictions, but the frozen evidence does not establish them. The report's acknowledged pre/post package TOCTOU warning is important but does not by itself establish this broader bootstrap trust boundary.

**Required before relying on the claim:** parent-admit a trusted, isolated launcher and read-only interpreter/stdlib/dependency snapshot, including controlled startup, import paths and relevant native runtime; independently verify that admission before any untrusted startup/import can affect checking. Add negative controls for ambient module/startup contamination. No such specific test or mutant is named in `REPORT:40-41`.

### M2 — The recorded self hash need not be the bytes Python already loaded

`ENTRY:55-60` reads `__file__` from disk after the interpreter has already loaded the executing script, hashes those current bytes, and passes that value as the expected author-verifier hash to the gate. `ENTRY:119-120` later re-pins the then-current path against that same computed value. Unlike the component bootstrap at `ENTRY:32-42`, this does **not** establish that the bytes Python executed initially equal the bytes subsequently read and recorded. With a source replacement between script loading and the first read, the GO can bind one on-disk version while another version is running; an unchanged later read does not close that gap. This is a concurrency/isolation issue, not an assertion that such replacement occurred in this review.

**Required before relying on executed-code binding:** launch the exact verified bytes through a trusted pinned bootstrap, or ensure an appropriately immutable snapshot before the interpreter first opens the entrypoint, and bind that launch to the GO. The report acknowledges observed-byte/TOCTOU limitations for dependencies (`REPORT:29`) but does not identify a test or mutant for the entrypoint-load-versus-later-self-read case.

### m1 — A success-looking result may precede, or outlive, its terminal receipt

`ENTRY:121-130` writes and fsyncs a result whose own status is `AUTHOR_GLOBAL_COVERS_COMPLETE_UNADOPTED`; only afterward does it perform another guard check, set the success status, and settle a separate receipt (`ENTRY:130-153`). An interruption or failure between these steps can leave a success-looking result with no terminal receipt or with an `INCOMPLETE` receipt. `REPORT:33` explicitly warns that a partial result is not a verdict without the matching terminal receipt and that SIGKILL/power loss/fsync failures need not yield a complete receipt. This is an integration hazard, not a demonstrated erroneous adoption: no downstream consumer is in scope.

The parent/consumer must enforce, rather than merely assume, an authoritative terminal receipt with successful status and matching result name/hash, GO and scope bindings; an orphan result or missing/unreadable/INCOMPLETE receipt must be UNKNOWN. No named test or mutant in `REPORT:40-41` establishes rejection by a downstream consumer of such an orphan or mismatched pair.

### INCONCLUSIVE 1 — Parent GO authentication and no-GO refusal

`NO-GO:33-38` explicitly stops GLOBAL execution pending a separately frozen GO. In the visible entrypoint, `ENTRY:48-61` reads a GO path under the round via delegated helpers, accepts its expected SHA from `--go-sha256`, and calls the pinned but unseen `gate['validate']` before the explicit obligation-engine bootstrap and `GlobalVerifier` construction at `ENTRY:105-107`. The visible ordering is supportive, but `ENTRY:48` also executes the runtime and gate components before validation; their bodies are outside scope.

A SHA supplied with a path demonstrates byte agreement only if the reader works correctly; it does not by itself identify the parent as issuer. The gate may enforce further controls, and the parent may control the round directory, but neither an authenticated issuer/trusted independent GO digest nor their effectiveness can be established from these three inputs. `REPORT:25,40-42` describes schema/review controls, a GO-authorization mutant, and an author-run nonexistent-GO refusal; those are not an independently read gate or replay. In particular, the evidence does not establish how an otherwise valid, self-hashed record not issued by the parent is rejected. Before any execution, inspect/freeze the gate and independently enforce the parent-only authority and complete GO bindings; do not infer that this review grants a GO.

### INCONCLUSIVE 2 — Missing, malformed, duplicate, and prefix-conflicting paths

The entrypoint parses the bundle through unseen `strict_json` (`ENTRY:80-84`) and delegates the whole bundle to unseen `GlobalVerifier.verify_bundle` (`ENTRY:105-108`). Its only visible postcondition is that the **keys** of the returned `counts` equal the obligation-name set (`ENTRY:107-108`); actual path parsing, duplicate detection, prefix conflicts, binary completeness and rejection on any failed leaf therefore depend on the unseen engine raising or otherwise failing closed. Key-set equality alone does not prove successful leaf verification or validate returned per-obligation values.

`REPORT:19,40-41` asserts prefix-free binary-complete trees and describes missing/duplicate/prefix tests and a `binary coverage` mutant. This is plausibly relevant but does not show the implementation, fixtures, or whether an invalid-path mutant was killed for the intended reason. The report itself warns that a removed tree guard can die through a secondary error (`REPORT:41`). No specifically identified test or mutant for malformed path types/alphabet is reported. Duplicate JSON keys and duplicate leaf paths are distinct protections.

### INCONCLUSIVE 3 — Exact predicates and float diagnostics

No visible scientific float predicate occurs in `ENTRY`; `time.time()` at `ENTRY:70,137` supplies receipt timestamps, not a visible scientific inequality. But `ENTRY:105-108` delegates all scientific predicates and leaf validation to the unseen obligation engine, and the local replay is also delegated (`ENTRY:99-104`). Therefore the frozen source does **not** prove exact rational/interval arithmetic throughout, nor rule out a path from floating diagnostics to a completed cover.

`REPORT:19,31,40-41` describes exact arithmetic, coefficient/split/face controls, and exact-floor/common-basis mutants; these are relevant but insufficient to establish that every predicate is exact or that floats cannot certify a cover. A specifically identified float-substitution/diagnostic-to-verdict mutant and corresponding negative test are not reported.

### INCONCLUSIVE 4 — Caps, timeouts, signals, and UNKNOWN

`ENTRY:64-70,72-75,109-120,130-150` installs delegated cooperative guards/latches, defaults to `INCOMPLETE`, catches `BaseException` inside settlement, checks the signal latch, and delegates terminal receipt settlement. A caught exception is not promoted by this visible code. The literal non-success status is `INCOMPLETE`, not `UNKNOWN`; the required UNKNOWN is a **consumer interpretation**, especially for absent receipts and failed launches. The implementation of guard timing, RSS measurement and settlement is not in scope.

`REPORT:33-35,40-41` says caps are cooperative, that a single large operation may evade timely checking, that certain hard failures need not leave a receipt, and that the signal test injects a latch rather than delivering an OS signal. The described deadline, RSS, signal and receipt-signal mutants are relevant but do not establish correct actual OS signal delivery, SIGKILL/hard-timeout/crash handling, durable settlement under storage failure, or downstream UNKNOWN on missing receipt.

## Explicit test and mutant coverage inventory

The **48 tests** and **24/24 killed mutants** are only the author's report (`REPORT:40-41`); their source, exact assertions, shadow changes and logs were not in the manifest. “Not named” below means **not explicitly identified in that report**, not a claim that an unexamined test or mutant definitely does not exist. No GLOBAL scientific obligation was run here or, according to `REPORT:7,21,48`, in the reported evidence.

| Protection | What the report explicitly describes | Assessment of the described coverage |
|---|---|---|
| Leaf paths and binary coverage | Missing/duplicate/prefix tree tests; `binary coverage` mutant; strict JSON and duplicate-JSON mutant. | Relevant to coverage and duplicates, but no separate identified mutant for duplicate-leaf and prefix-conflict rejection, and no identified malformed path-type/alphabet test or mutant. JSON object-key duplicates do not substitute for leaf duplicates. |
| Exactness and face semantics | Exact affine/compact coefficients, both split branches, parameter endpoint, internal/outer face, non-strict zero, sorted equality, exact floor, and common-basis tests; mutants for admissible-face strictness, sorted equality, exact floor and common basis. | Useful synthetic controls, but no expressly identified float-predicate or float-diagnostic-to-verdict test/mutant, nor separately identified mutants for every split, parameter-endpoint, non-strict-zero or excluded-outer-face protection. |
| Input SHA, paths and environment | Strict JSON, missing/altered/unlisted/symlink inputs and source-order tests; hash, root-containment, missing/unlisted dependency, source-order and local-engine-pin mutants. | Generic hash coverage cannot establish every binding. No separately identified mutants for symlink rejection, each GO/bundle/source/environment/interpreter/component pin, pre-success rechecks, or executed-entrypoint-versus-on-disk bytes; no named startup/stdlib contamination test or mutant. |
| Parent authority and review gates | Admission/review tests; GO authorization, historical verdict, face review, distinct checker and hardening-review mutants; author-reported nonexistent-GO refusal. | Relevant schema/refusal evidence, but no identified negative test or mutant proving issuer authentication against a fabricated self-hashed GO, nor independently checked immutable parent approval. |
| Caps and interruption | Bounded stop and INCOMPLETE local receipt tests; deadline, RSS, signal and receipt-time-signal mutants; synthetic latch injection during receipt write. | Useful cooperative controls. No actual OS-delivered signal test is reported; no named SIGKILL/hard-timeout, storage-failure, orphan-result consumer, or missing/mismatched terminal-receipt rejection test/mutant. |
| Seven named obligations and scientific construction | All-seven-cover-names and binary-coverage mutants; toy polynomials and trees. | Name-set coverage is not correctness of seven polynomial constructions, scaling, per-leaf signs, full real GLOBAL covers or definition-first agreement. No tests of the real seven GLOBAL obligations are reported; no per-obligation semantic-construction mutant is identified. This is an intentional NO-GO boundary, not a request to run them. |
| Optimized Python behavior | Optimized-assert conversion test and mutant. | Relevant to the reported local-wrapper protection; wrapper and mutation remain uninspected here. |

**Priorities before a separately authorized future gate:** resolve M1/M2 and make the terminal receipt contract enforceable; freeze and review the actual gate/runtime/engine and test/mutant bodies in an appropriately screened new scope; add the explicitly missing controls above; require independent definition-first checking, admitted resources and a recorded parent GO. None of these prerequisites is satisfied or authorized by this review.
