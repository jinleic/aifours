# Parent release CP1 caller v2 — source-review candidate, NOEXEC

Actual `/bin/date` before this write: `2026-10-19T17:18:20-0700`.

Source `RUN/control/parent_release_caller_v2.py`: SHA256 `9f3d158bd80a31d6ce2d964e216244d5095eb9422782bc448dc3a671d81e4cb4`, 1409 lines, 71594 bytes. It is built from v1 `4072c50ef5be021a22e72a43571550c1338ab8a4d243752d88e3b7cc71a75cae`, which stays immutable.

- **Authorization:** `RUN/control/written-slot-transitions-moq-cp1-20261019-1714-v1.json` `5b34fc67350bc137dcd7ec885859a6b35d15ff395c31b4a7351c378bdf055b4f`, key `cp1_v2`.
- **Replacement list:** frozen before editing in `RUN/review/parent-release-cp1-checkpoint-006-v1.json` `9cd2966f89a5ce85e02d56fdf2e137a33af288f74e196410105b67a115243651`.
- **Exact diff:** `RUN/review/parent-release-cp1-caller-v1-to-v2.diff` `99ee5dbe30582c8353d0464a0f3110a5398dbb13e24e67c6eba086941ad9de15` (83 lines; Python `difflib.unified_diff`, n=3).

**No import, compile, AST, exec, test, probe or model CLI** was run on any subject. Python was used only for byte reads, positional substitution of the frozen list, difflib, hashing and exclusive writes. This is not source acceptance; the global HOLD is unchanged.

## Exact delta

Each replacement was applied exactly once, by position, against the original v1 text. Every old string occurred exactly once, and no two spans overlap.

| ID | v1 → v2 lines | Change |
|---|---|---|
| R1 | after 16 → 17–26 | Module docstring: authorization, CP2 v3 re-pin and caller-side version binding |
| R2 | 24 → 34 | `MODULE = 'parent_release_caller_v2.py'` (the receipt/outcome/account `module` value) |
| R3 | 29 → 39 | `CALLER_PATH` → `RUN/control/parent_release_caller_v2.py` |
| R4 | after 41 → 52–56 | `CP2_UNION_VERSION`: `module` `parent_release_identity_v3.py`, `design_freeze_sha256` `033cb30dcde31ec94acbb0f8576f436e14bfaae980c8bff34e76932dd894cb5a`, `scheme` `sv19-incarnation-v1`, `producer_sha256` `cb828a78367dc2023bfc6e330696745f186f186811752361472747e5fe547e93` |
| R5 | 96 → 111 | `CAUSES`: new `CP1_UNION_VERSION`, ordered immediately before `CP1_IDENTITY_UNION` |
| R6 | after 689 → 705–719 | New non-raising predicate `_union_version` |
| R7 | after 691 → 722–725 | In `_union`, the version check directly after `_detach` (721) and before the first status read (727) |

The CP2 v3 source `RUN/control/parent_release_identity_v3.py` `f21b4296ae52778fe31677f749a871d8982c31c6d5133609dc1d0b0e0fe58b38` is **recorded only**. CP1 v2 never loads CP2 bytes, so it cannot verify that digest. What it checks is the four self-reported union fields.

## Behaviour

- **Version check before any status use.** `_union_version` (705) requires the union's `module`, `design_freeze_sha256`, `scheme` and `producer_sha256` to be exact `str` values equal to `CP2_UNION_VERSION`.
  - If a field is absent, not a `str` or a different value, or the union is not an object, `CP1_UNION_VERSION` fires. The evidence names the first failing field, its observed value (truncated to 80 characters) or its type name, and the pinned value.
  - `_union` then returns without setting `state.union`. No union `format`, `state`, `union_sha256` or `prt_identities` is read, and no served count is taken.
- **HELD at the pre-invocation gate.** As in v1, the independent S4–S6 steps still run and their causes accumulate: PRT3 bytes are read, hash-verified and their definitions executed, then source pins and attestations are checked. PRT3 `decide_and_commit` is **never invoked**. Nothing is written.
- **Detach failures are unchanged.** A non-JSON value, cycle, NaN or cap overflow still fires `CP1_IDENTITY_UNION` (F44), because the version check needs the detached object.
- **Where the check runs.** It runs only where v1 runs `_union`, that is once the spec has detached and the identity shape is valid. Otherwise the earlier causes stand alone.
- **Owner input change.** `sources.caller` must be `{path: RUN/control/parent_release_caller_v2.py, sha256: 9f3d158b…}`. The v1 path is refused with `CP1_OWNER_INVALID`; v1 bytes under the v2 path are refused with `CP1_SOURCE_PINS`.
- **Schemas unchanged.** Receipt, outcome and account schemas, all format strings, `RECEIPT_PREFIX`, `SCOPE_SHA256` and `DESIGN_CHECKPOINT_SHA256` (base design `565a29ed…`) are unchanged. The v2 delta is bound through `MODULE`, through the docstring path to checkpoint 006, and through the declared caller digest that S5 verifies and the receipt carries in `sources_declared`.

## Not changed (not authorized; still open)

- **No `endedness.module` check.** A CP2 v2 evaluator given a v3 union is not detected. v2 and v3 evaluators differ only in the evaluator-side version check, which CP1 v2 has already applied to the union itself.
- **SF2:** `union.item` is not bound.
- **SF3:** no fresh-log requirement (`served_before == 0`).
- **SF4:** the preflight caps stay fail-closed.
- **SF5:** the union document is not retained.
- **Attestations:** fields beyond `format`/`prerequisite`/`item`/`allocation_line_sha256`/`status` are not checked.
- **CP2 bytes are not loaded or verified.**
- The four fields are self-reported. They stop cross-version use, not forgery; the parent attestation `identity_union_census_cp2` remains the provenance guard.

## Correction to addendum 1

Addendum 1 says "before PRT3 is loaded or invoked" (compatibility table) and "PRT3 neither loaded nor invoked" (F46). Both are wrong for v1 and for v2. On every pre-invocation refusal, PRT3 is **loaded at S4 but not invoked**.

## Fault expectations for v2 (frozen, NOT exercised)

Notation as in notes v1; causes are listed in v2 `CAUSES` order.

| ID | Case | Expected |
|---|---|---|
| V01 | Complete positive with a genuine CP2 v3 union, census pair and evaluator | R (= F01) |
| V02 | Union lacks any one of `module`/`design_freeze_sha256`/`scheme`/`producer_sha256` | H(CP1_UNION_VERSION). No union status read; PRT3 loaded, not invoked |
| V03 | CLOSED union built by CP2 v2 (`parent_release_identity_v2.py`, freeze `7f46b7e5…`) | H(CP1_UNION_VERSION) |
| V04 | Union built by CP2 v1 | H(CP1_UNION_VERSION) |
| V05 | `scheme` or `producer_sha256` differs, or a field holds a bool/int/list/None | H(CP1_UNION_VERSION) |
| V06 | v3 union HELD (e.g. sticky `U_UNKNOWN_INCARNATION`) with correct version fields | H(CP1_IDENTITY_UNION) (= F46, wording corrected) |
| V07 | Union HELD **and** a wrong version field | H(CP1_UNION_VERSION) only; status never consulted |
| V08 | Detached union is a JSON list or str, not an object | H(CP1_UNION_VERSION) |
| V09 | Union not detachable (cycle, NaN, caps) | H(CP1_IDENTITY_UNION) (= F44) |
| V10 | Correct v3 fields, `prt_identities` ≠ `spec.identities` | H(CP1_IDENTITY_UNION) (= F10) |
| V11 | Spec invalid **and** wrong union version | H(CP1_SPEC_BINDING) plus any independent S4–S6 causes. No CP1_UNION_VERSION, because `_union` does not run |
| V12 | Owner declares the v1 caller path, or the v1 digest under the v2 path | H(CP1_OWNER_INVALID) or H(CP1_SOURCE_PINS) |
| V13 | KNOWN-GAP: forged union carrying all four v3 values | The source cannot detect it; the outcome follows the other inputs. Provenance rests on the parent attestation |
| V14 | KNOWN-GAP: v3 union with a CP2 v2 evaluator | Not detected (no `endedness.module` check was authorized); the outcome follows the evaluator result |
| F41 (amended) | CLOSED union with a non-v3 `module` or design freeze | H(CP1_UNION_VERSION) |
| F47 (amended) | Non-v3 union, v3 evaluator | Refused earlier: H(CP1_UNION_VERSION) before PRT3 invocation; the evaluator is never reached |
| F48 (amended) | v2 or v1 union with the matching evaluator | H(CP1_UNION_VERSION); the only remaining residuals are V13/V14 |

All other F01–F46 and A01–A10 expectations stand, now ordered with the new cause.

## Source-readiness prerequisites for v2

1. PRT3 `161ae04c…` independent review and finite qualification.
2. Independent hostile review of CP1 v2 (this source plus the exact diff), then separately admitted finite controls F01–F48, V01–V14 and A01–A10, with synthetic faults labelled.
3. CP2 v3 `f21b4296…` independent review and qualification. CP2 v1/v2 must not be used; CP1 v2 refuses their unions by self-reported fields only. On a busy shared host the CP2 union is expected to be HELD.
4. All seven parent attestations; none exist. `identity_union_census_cp2` must establish that the union, census, log and evaluator come from executing exactly the CP2 v3 bytes, that `union.item` is the owner item, and that the census pair is fresh.
5. The original `EvidenceReader` built from `1fc8f00c…` with the original deadline, a qualified owned-date helper, and a nonrenewing deadline predicate.
6. A single-writer registry premise and a receipt directory; later late audits must declare receipts.

CP1 v1 `4072c50e…` stays immutable and should not be used for any transaction: it accepts non-v3 unions.

## Impossible-to-certify boundaries

These are unchanged from notes v1:
- Native calls and callbacks can stall; there is no hard-real-time guarantee.
- In-process forgery and restarts are outside what the source can prevent.
- `exec` of verified PRT3 bytes trusts the interpreter.
- Hashes authenticate bytes, not origin.
- An omitted historical identity is undetectable here; CP2 is conditional.

In addition, the four union version fields are self-reported claims.
