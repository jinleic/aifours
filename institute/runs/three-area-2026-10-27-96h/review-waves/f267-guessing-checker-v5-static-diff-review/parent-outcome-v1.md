# f267 parent outcome: static diff review of checker-v5.py and projection-checker-v2.py

**Outcome: both f264 gating MAJORs are CLOSED in the successors; no patch-introduced false-accept defect found; four residual MINORs remain open (all inherited, none gating). Bulk archive replay is authorized in principle but NOT yet executed; a frozen execution protocol and explicit resource budget are required first.** Native clock before composing: **2026-10-29T18:29:49-0700 PDT**.

Manifest /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f267-guessing-checker-v5-static-diff-review/manifest-v1.json SHA-256 **f8f31c23f8840feaf99854a35431a5f6b6198b995390ab003df1aa61af15b005** (13748 B, 196 LF). Both reviewers refused-filesystem-write and returned complete reviews as tool output; the parent materialized them verbatim: slice-A-return-v1.md SHA-256 **29428089614d1b93ea83087adf752c84258cd55be6415ab4d8d7f001277a6ac0** (172 LF), slice-B-return-v1.md SHA-256 **60972d0726055c460bc77fea4194bd681eac968ef9e6dba299ff4abc45a87738** (147 LF). Both verified all 24 input pins before reading, read all bodies completely (prose ≤15-LF raw windows, code ≤60), and used read-only diff only.

## f264 disposition table (successor evidence)

| f264 item | Disposition | Evidence |
|---|---|---|
| 1 visibility union/enforcement (MAJOR) | **CLOSED** | One shared visibility set V5:927–956 consumed at row admission :498–502, scope validation :552–557, action invariance :592–600, applicability :746–754, transport :964–977; plane-declared vertices must be visible in the source plane (:953–955). Both f264 exploit forms blocked (descriptive witnesses (18,288,306) and (8,1008,1016) traced). |
| 2 noncover binding (MAJOR) | **CLOSED for archive/roster** | Delete-1 colouring validated (:857–863), transported with full domain and induced-edge checks (:1093–1103), graph metadata consumed (:1183–1185); missing categories → named UNKNOWN (:1094–1095, :1108–1109); wrong binding to an available n9 still REJECTs (:1104–1107). Standalone verify_applicability remains n9-only by design (:727–738). |
| 3 typed source locations | **CLOSED, closed-world exceptions** | Exact-int array positions only; literal "2"/"3" only for the frozen n9 dictionary member bound to exact-int missing_vertex; root null only for the five named scalar sources (:30–38, :603–623); one locator drives record, binding, dedupe (:628–632, :899–901, :996–998). Exception sets are code constants, not archive fields. |
| 4 PJ descriptor kinds | **CLOSED** | PJ2:135–137 registers aux-determined and functional-local-fd; :157–180 reconstructs/consumes both; images and identity include them (:324–359, :597–598). |
| 5 n11 gate premise bookkeeping | **OPEN (minor)** | Written caller still lists G_S; DECL/V5 carry no n11 gate; code fails closed. B-R1. |
| 6 duplicate row descriptors | **OPEN by author decision (minor)** | V5:659–685 admits duplicates (PJ2 rejects); algebraically harmless per v4 analysis; explicitly not fixed (diff summary LF49). |
| 7 signal/exclusive-output completion | **OPEN (minor)** | Signals in except-handler/final phases escape the envelope; a signal or fsync error after O_EXCL open can leave a partial 0600 file; rerun exits 73 (OUTPUT_EXCLUSIVE_FAILED). Not falsely treated as PASS. B-R2. |
| 8 invalid-cap exit | **OPEN (minor)** | INVALID_RESOURCE_CAP prints to stderr, returns 2, writes no result; distinguished from rejection only by stderr/absence. B-R3. |

PJ2 strictness closures: UTF-8 decode (no auto-detection), duplicate keys/floats/NaN rejected, canonical Fraction spellings, exact-int source_index and record ordinal, single-LF prefix check at the pinned offset (:594), bounded reads with re-hash before use (:494–577), timeout→UNKNOWN/3 vs REJECT/2 (:580–627).

Diff fidelity: both full diffs read; **undocumented behavioural-change list is empty**; author diff summary matches all hunks (one blank-line alignment difference only); frozen v4 (43e44f78…) and PJ1 (20fe0113…) unchanged.

New VALID admissions relative to v4/PJ1, all documented and justified: (1) archive/roster D1-colour noncover route; (2) n9 rows with unequal redundant inner provenance multiplier (top-level rational remains authoritative per DECL); (3) singleton-group-orbit rows and full-visibility applicability from singleton/plane declarations (all premises enforced through the shared helper); (4) PJ2's two descriptor families. No path to VALID with an unmet guard was found.

## Parent ruling

1. The f264 gating requirements (visibility closure, noncover closure, exact-int locators, PJ kinds/prefix/timeout separation) are **statically satisfied**. checker-v5.py and projection-checker-v2.py are the checker versions of record for any future archive work; v4/PJ1 stay frozen and unused.
2. **No bulk replay is executed by this outcome.** Before any run: (a) a frozen execution protocol (explicit caps above the declared 748/1,811,001/174,251 counts, expected UNKNOWN categories, output paths, time budget, receipt requirements including per-phase exit codes); (b) explicit owner authorization for the resource budget, since a full-archive replay is a heavy run under the standing ask-first rule; (c) unchanged SHA pins of archive, declaration, spine and checkers re-verified at run time.
3. Residual minors 5–8 stay open as recorded; none is a false-accept path. The scientific premises outside code (written lift/tensorization, FD persistence in fibres, the k=1 delete-1 colouring entropy argument) remain WRITTEN obligations; a successful replay would certify the archive against the declaration, not the theorem.
4. Historic f236 UNKNOWN is unchanged; no theorem, source-projection or novelty claim follows.

Both slice returns are the reviews of record; this outcome consolidates them without altering their text.
