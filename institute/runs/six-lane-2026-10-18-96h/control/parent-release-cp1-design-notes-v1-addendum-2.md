# Parent release CP1 — addendum 2: CP2 v3 source pin after the SF1 repair (NOEXEC)

Actual `/bin/date` before this write: `2026-10-19T17:12:11-0700`.

This addendum applies to the immutable CP1 source `RUN/control/parent_release_caller_v1.py` `4072c50ef5be021a22e72a43571550c1338ab8a4d243752d88e3b7cc71a75cae`, re-hashed at 17:11:55 and unchanged. It builds on addendum 1 (`RUN/control/parent-release-cp1-design-notes-v1-addendum-1.md` `8ba571f24de04cf5c88b0b39fc35c8c4126f6ef28fdbc1c3da8ee8f200d2ca0b`). It **supersedes** five parts of addendum 1:

- the CP2 pin table;
- the CP2 values in the interim parent obligations 1–2;
- updated prerequisite 3;
- the pin values in decision Option A;
- the source and lines cited for SF1.

Everything else in notes v1 and addendum 1 stands. **No import, compile, AST, exec, test, probe or model CLI** was used; only source/diff reading, `shasum`/`wc`/`grep` and this exclusive write. This is not source acceptance, and the global HOLD is unchanged.

## CP2 pins (ParentIdentityCP2 IRC ~17:10; hashes re-read with `shasum` at 17:11:55)

| Object | SHA256 | Status |
|---|---|---|
| `control/parent_release_identity_v3.py` | `f21b4296ae52778fe31677f749a871d8982c31c6d5133609dc1d0b0e0fe58b38` (86499 bytes, 1617 lines) | The **only** CP2 source a CP1 transaction may depend on. Source-only, unreviewed, unqualified |
| `control/parent_release_identity_v2.py` | `7b2bc4021744aa6fa55677fa4953c9efc1088f53d341fb0ba339621abdddc3ec` | Superseded by the SF1 repair. **Forbidden** for CP1 transactions |
| `control/parent_release_identity_v1.py` | `d07548e2dbff4ef6b64a3a902d3b59ed7c4abbf8dc2115e8b08ed37ee2ec14d5` | Immutable HOLD. **Forbidden** |
| `control/parent-release-cp2-v3-repair-scope-v1.json` | `0b7b3b7c8ebb3b8ae88ad04472cc7e16a4d2ea8ee718706a6408d714303d2421` | Parent SF1 repair scope |
| `control/parent-release-cp2-design-freeze-v3.json` | `033cb30dcde31ec94acbb0f8576f436e14bfaae980c8bff34e76932dd894cb5a` | Equals `DESIGN_FREEZE_SHA256` (v3 line 63) |
| `review/parent_release_identity_v2_to_v3.diff` | `25819afb23afb6ad95091f00294c13821555e05f93020b25f88be051ee688afd` (82 lines) | Read in full |
| `review/parent-release-cp2-controls-v3.json` | `d87dfd4d657481f70c88ae56ff74e6401091b724a3c4239ef961a43fae9c9bf2` | CP2 frozen expectations |
| `review/parent-release-cp2-finding-sf1-v1.json` | `b52ab85fa4def5c75328fed083ac5fee2764a11eaef11d3e9abd0f3b0c00c099` | CP2 record of the joint SF1 gap |

The exact values in a v3 union report (lines 69, 63 and 1420) are:
- `module:'parent_release_identity_v3.py'`;
- `design_freeze_sha256:'033cb30dcde31ec94acbb0f8576f436e14bfaae980c8bff34e76932dd894cb5a'`;
- `scheme:'sv19-incarnation-v1'`;
- `producer_sha256:'cb828a78367dc2023bfc6e330696745f186f186811752361472747e5fe547e93'`.

The endedness result also carries `module:'parent_release_identity_v3.py'` (line 1597).

## What the v3 delta changes for CP1 (verified by reading the diff; nothing exercised)

The only behaviour change is the new `_union_version` (lines 1498–1508). It requires exact str equality of the union's `module`, `design_freeze_sha256`, `scheme` and `producer_sha256` with v3's own constants, and refuses when any is absent. It runs first in `_v_union` (line 1510), and therefore in `spec_identities_match` (line 1610, which returns False). In `evaluate_endedness` (line 1559) it runs as a separate guard *before* any status use; failure fires `E_UNION_VERSION`, which is first in `E_CAUSES` and makes the result HELD. Formats, public names, signatures, `served_count()` and the keys CP1 reads are unchanged.

- **Compatibility:** CP1 4072c50e still needs no change. The detached union CP1 passes to `evaluate_endedness` keeps all four fields byte-identical, so a genuine v3 union passes `_union_version`. Every finding in addendum 1's compatibility table carries over.
- **SF1 joint gap — closed at the CP2 evaluator:** a union built by v1, v2 or any other module, evaluated by the v3 `evaluate_endedness`, is HELD with `E_UNION_VERSION`. CP1 v1 then refuses with `CP1_ENDEDNESS` (expected-outcome row F47).
- **SF1 residual at CP1 (unrepaired; the source is immutable):** CP1 v1 checks neither `union.module`/`design_freeze_sha256`/`scheme`/`producer_sha256` nor `endedness.module`. It also cannot tell which module's `evaluate_endedness` the parent passed in `identity`. So if the parent supplies a v2 (or v1) evaluator together with that module's union, CP1 v1 accepts the result (F48, KNOWN-GAP). Only the parent attestation guards this today.
- **SF2–SF5:** unchanged from addendum 1.

## Interim parent obligations (replaces addendum 1, obligations 1–2; obligations 3–4 unchanged)

1. The union, `census`, `census_log` **and** `evaluate_endedness` all came from one execution of exactly the CP2 v3 bytes `f21b4296…`. The v1 `d07548e2…` and v2 `7b2bc402…` modules were not used for this transaction.
2. The union's `module`, `design_freeze_sha256`, `scheme` and `producer_sha256` equal the four v3 values above. `endedness.module` equals `parent_release_identity_v3.py`, and `union.item` equals the owner item.

Recommended extra attestation keys are `cp2_source_sha256 = f21b4296…`, `cp2_design_freeze_sha256 = 033cb30d…` and `union_sha256`. CP1 v1 permits them but does **not check** them.

## Updated prerequisite 3 (replaces notes v1 item 3 and addendum 1's update)

3. CP2 v3 `parent_release_identity_v3.py` `f21b4296…` must be independently reviewed and finitely qualified. CP2 v1 and v2 are forbidden. CP2 SR-4/SR-5 MINORs remain open. A v3 union is expected to be HELD on a busy shared host, as with v2, so F01 practically needs a quiescent host for the whole run.

## Decision still requested (Option A values updated; Option B unchanged except for the pin)

A CP1 successor `parent_release_caller_v2.py` needs a new parent write scope.

- **Option A:** pin independently, with no wildcard, exactly the four v3 union values plus `endedness.module`, `union.item == owner.item` and `served_before == 0`. The `identity_union_census_cp2` attestation must carry `cp2_source_sha256 == f21b4296…`.
- **Option B:** CP1 loads and executes the verified CP2 v3 bytes `f21b4296…` itself, as it does for PRT3.

Both close the SF1 residual against accidental misuse. Only Option B binds code identity; under Option A the self-reported fields stop cross-version use, not forgery. Without a successor, SF1's residual stays a named HELD prerequisite, covered only by the parent attestation.

## Additional fault expectations (frozen, NOT exercised; notation of notes v1)

| ID | Case | Expected |
|---|---|---|
| F47 | v3 `evaluate_endedness` given a union whose `module`, `design_freeze_sha256`, `scheme` or `producer_sha256` is absent or not the v3 value; v3 census pair; otherwise complete positive | CP2 `E_UNION_VERSION` (HELD) → H(CP1_ENDEDNESS). No receipt |
| F48 | The parent supplies the v2 or v1 module's union **and** evaluator; all else valid; synthetic attestation | CP1 v1 fires no cause for these fields (SF1 residual). The outcome follows the other inputs. Freeze as a KNOWN-GAP control, never as a desired pass |

F41 in addendum 1 is now refined into F47 (v3 evaluator) and F48 (non-v3 evaluator). These are source-derived expectations, not observed output.
