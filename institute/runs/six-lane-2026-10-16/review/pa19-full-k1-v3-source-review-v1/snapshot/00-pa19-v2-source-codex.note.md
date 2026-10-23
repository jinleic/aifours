**DISPOSITION: HOLD. V2 should not run production yet.**

All 25 supplied snapshot files match their stated SHA-256 values and byte counts. This review used only static reads and hashes inside the snapshot; no source, controls, or native programs were executed.

The original incomplete-CNF acceptance hole is closed in the positive predicate. Production remains blocked by retry classification, binary binding, safety-veto handling, and incomplete cleanup/admission guarantees.

1. **BLOCKER — Tier-2 eligibility is not fail-closed.**  
   [SOURCE17:317–329](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v2-source-review-v1/snapshot/17-src-m2_supervised_runtime_v2.py:317), `SOURCE05:277–305`, `SOURCE19:117–125`.

   The classifier recognizes one RSS-shaped `trip_reason`, but that does not establish **sole RSS**:

   - The supervisor checks RSS before floor, wall, and external signals in an `elif` chain. Concurrent violations disappear from the receipt.
   - A native report containing `status=UNKNOWN`, `lifecycle_error`, and `halt_production=True` can pass: those anomaly fields are not rejected. The owner then explicitly clears `halt_production`.
   - Missing, malformed, or wrong-schema worker reports can also take this fallback.
   - The classifier checks `stop['kill_error']`; the actual supervisor emits **`killpg_error`** (`SOURCE05:234–237`). Recorded SIGTERM errors therefore escape that check.

   **Required repair — blocking production:** record all concurrent stop conditions and require affirmative evidence that RSS was the only condition. Reject lifecycle errors, existing halt requests, corrupt reports, and the actual `killpg_error` field. Missing observations must deny retry unless separate reviewed evidence establishes the exclusions. Apply the corrected predicate to admission and final reading, and re-pin any changed supervisor.

2. **BLOCKER — Attempt-time binary hashes replace the frozen binary authority.**  
   [SOURCE19:94–110](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v2-source-review-v1/snapshot/19-src-m2_item_owner_v2.py:94), `SOURCE19:148–156`, `SOURCE23:67–82`.

   The owner reads the **current** solver/checker hashes into the job, then constructs its qualification expectations from those same job values. Its binary comparison is consequently self-consistent rather than contract-bound.

   M6 never compares the installed binaries with its frozen `solver_sha256` and `checker_sha256` before executing. M9 checks them only during initialization (`SOURCE15:113`), leaving later attempts exposed to drift. The worker’s check at `SOURCE18:351` only confirms the newly sampled job hashes.

   Thus a changed checker can produce a published `status=UNSAT`, `checked=True` receipt under the original contract. The later contract-aware reader can reject it, but that does not repair production admission or the already-published claim.

   **Required repair — blocking production:** pass the contract’s binary hashes into the owner and job; use those frozen values for qualification. Reject drift after capacity waits and immediately before each native spawn.

3. **MAJOR — An ordinary UNKNOWN can erase a supervisor safety trip.**  
   [SOURCE19:129–140](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v2-source-review-v1/snapshot/19-src-m2_item_owner_v2.py:129), `SOURCE12:110–117`.

   `ordinary` requires bounded-UNKNOWN/proof-cap metadata and known cleanup, but does not exclude supervisor floor, wall, or external-signal trips. That branch precedes the nonclean-supervisor branch and sets `halt_production=False`.

   For example, a completed bounded-UNKNOWN report followed by a final sample below **12,000,000,000 B** can become an ordinary unqualified result without a persistent safety veto. After free space recovers, subsequent work may resume.

   **Required repair — blocking production:** make supervisor safety causes dominate ordinary outcome classification. Whitelist only explicitly permitted bounded-stop cleanup reasons; persist all other safety holds before releasing capacity.

4. **MAJOR — Post-grace quiescence does not explicitly reap the owned leader.**  
   [SOURCE17:279–314](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v2-source-review-v1/snapshot/17-src-m2_supervised_runtime_v2.py:279), `SOURCE05:343–350`, `SOURCE05:200–210`.

   The supervisor polls its `Popen` once after the bounded stop. If the leader survives that grace and exits later, `_settle()` performs only kernel probes. Zombies are excluded from live membership, and the owner can mark capacity safe without another `poll()`, `wait()`, or `waitpid()`.

   Live-child containment is substantially improved; the promised “retain ownership through reaping” lifecycle is still incomplete.

   **Required repair — blocking production:** retain the owned `Popen` or explicitly reap the owned leader during settlement. Require both known group quiescence and completed leader reaping before releasing flocks.

5. **MAJOR — The additional-data admission check still trusts a start-of-chunk envelope.**  
   [SOURCE17:148–155](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v2-source-review-v1/snapshot/17-src-m2_supervised_runtime_v2.py:148), `SOURCE15:121–129`, `SOURCE23:151–155`.

   Free space and RSS are freshly measured, but additional-data usage is not. Each later gate only validates the old envelope’s shape and value. The whole-plan bound is conservative for its planned outputs, but no shared reservation or writer exclusion establishes that it remains an upper bound over current lane data.

   **Required repair — blocking production:** refresh current accounting after waits, or implement a shared reservation mechanism covering every permitted writer and retained output. Unknown accounting must refuse admission. This leaves part of v1 BLOCKER 3 unresolved.

6. **MAJOR — Failed delivery and nonaccepting verdicts do not consistently become scientific UNKNOWN.**  
   [SOURCE18:191–235](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v2-source-review-v1/snapshot/18-src-m2_native_staged_v2.py:191), `SOURCE24:286–296`.

   Short/write/close failures and several missing, duplicate, or unexpected verdicts produce `INVALID`, whereas this commission requires UNKNOWN. They correctly cannot qualify as UNSAT; this is a result-contract mismatch.

   **Required repair — blocking production:** use scientific `UNKNOWN` for incomplete or unsuccessful certification, with separate integrity/veto metadata preserving the required persistent stop for invalid proofs or corrupted evidence. Update the controls that currently require `INVALID`.

7. **MAJOR — The required lifecycle controls contain an incorrect expectation.**  
   [SOURCE24:183–188](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v2-source-review-v1/snapshot/24-src-check_m2_ms09_k1.py:183), `SOURCE05:287–288`.

   The exceptional-start controls require `rec['uncertain'] is True`. A positively observed native surviving its leader produces a definite “group member alive after leader exit” trip; that supervisor branch does **not** set uncertainty. Successful bounded cleanup can therefore fail the control’s assertion.

   Retry controls also construct the incorrect `kill_error` key (`SOURCE24:455–466`).

   **Required repair — blocking production:** distinguish a definite nonclean stop from measurement uncertainty, use the real supervisor schema, and add simultaneous-cause, lifecycle-error-plus-RSS, missing-report, and late-leader-reaping controls. The frozen pack explicitly reports controls **NOT_RUN** and `observed_receipt=null` (`SOURCE01:4,133–138`).

The five v1 findings resolve as follows:

| SOURCE00 finding | Actual v2 assessment |
|---|---|
| BLOCKER 1: exceptional cleanup ownership | **Partially fixed.** Outer process-group supervision and capacity retention address live survivors and receipt failures (`SOURCE17:249–300`; `SOURCE05:343–369`). Explicit late leader reaping remains missing: finding 4. |
| BLOCKER 2: measured CNF delivery | **Fixed for UNSAT qualification.** Both feeds measure successful writes, bytes, SHA-256, close success, completion, and errors (`SOURCE18:76–105`). Both must match the bound input (`SOURCE20:103–108`). Classification still needs finding 6’s repair. |
| BLOCKER 3: complete admission gate | **Partially fixed.** Post-lock and immediate native gates now check fresh growth/free-space, RSS/headroom, COUNT, markers, and deadlines (`SOURCE17:136–188,249–259`; `SOURCE18:263–290`). Accounting remains envelope-based: finding 5. |
| MAJOR 1: exact solver UNSAT line | **Fixed.** Completed collectors remove only CR and require exactly `['s UNSATISFIABLE']`, rc 20, and self-exit (`SOURCE18:38–72,208–230`; `SOURCE20:97–102`). |
| MAJOR 2: invalid-proof veto propagation | **Fixed for observed invalid verdicts.** NOT VERIFIED becomes a persistent veto and survives inspection/inventory/resume (`SOURCE18:195–199`; `SOURCE19:30–50,147–157`; `SOURCE12:101–117`; `SOURCE13:337–372`). Safety-trip suppression in finding 3 is a separate remaining gap. |

Other requested checks:

- **Truncated CNF, exceptions, and early exits:** I found no short-feed path through the final measured-v2 UNSAT predicate. Incomplete threads cause a lifecycle UNKNOWN (`SOURCE18:271–272,298–304`); recorded failed feeds fail qualification even with nominal success output. Both CNF measurements and complete proof replay are rechecked by `SOURCE20:103–114`. Early solver/checker exit cannot substitute for completed delivery.

- **Acceptance:** the positive predicate requires exact singleton solver/checker verdicts, rc 20/0, successful completed collectors, both complete CNF feeds, and matching complete proof delivery. NOT VERIFIED and TIMEOUT cannot qualify. Solver rc 10 or the exact SAT verdict triggers a review stop (`SOURCE18:193–194`). Finding 6 concerns the required UNKNOWN classification of rejected outcomes.

- **Process safety:** the active v2 route has no SIGKILL, `Popen.kill()`, or `subprocess.run(timeout=...)`. It uses SIGTERM, a 60-second grace, then capacity-held settlement (`SOURCE17:258–300`; `SOURCE05:213–264`). Native groups do not invoke `ps`; the legacy helper at `SOURCE10:384–389` is bypassed by v2. STOP/veto markers block subsequent admissions, rather than being continuously watched in-flight (`SOURCE17:143–147`). FIFOs are retained; exceptional daemon threads terminate with their worker process. Finding 4 prevents an unconditional lifecycle PASS.

- **Two tiers:** tier 1 acquires one of at most two tokens; each worker stages solver and checker serially. This provides at most two pipelines/four compute processes. Tier 2 acquires all eight existing token flocks plus bigmem (`SOURCE17:221–241`). Thresholds are correctly **3.5 GiB** and **7 GiB**, with an **8 GiB admission headroom check**, and are honestly described as sampled guards rather than instantaneous hard caps (`SOURCE17:2–7,25–29,156–169`). The ownership scheme passes; retry eligibility fails finding 1.

- **Contracts and old outcomes:** static counts confirm **4,995 primary entries + 14 validations**, covering **5,008 intervals plus one direct input**. M9 reconstructs exact B100 partitions and validates identities/order (`SOURCE13:105–170`). Final coverage consumes new qualified v2 receipts; withdrawn historical/calibration outcomes remain separate (`SOURCE13:334–392`). M6 contains **106 rows: 24 old UNSAT, four old UNKNOWN, and 78 unattempted**. Its pending queue excludes all old records, including UNKNOWN **68, 73, 162, 77** (`SOURCE23:67–82,159–160`). Final M9 readiness also requires formula regeneration and retains B3’s separately bound parent-mathematics classification.

- **Evidence preservation:** scientific publication uses exclusive temporary creation and no-replace hardlinks, with pin/commit preceding the primary (`SOURCE13:60–75`; `SOURCE15:83–87`; `SOURCE18:364–367`). No active scientific-evidence unlink/delete path was found. Unattempted claims are moved into an archive with a manifest (`SOURCE15:36–44`). Token/COUNT files remain mutable coordination state.

Production requires the blocking repairs above, newly frozen hashes/contracts, and passing corrected controls. This static review supplies no observed control PASS.