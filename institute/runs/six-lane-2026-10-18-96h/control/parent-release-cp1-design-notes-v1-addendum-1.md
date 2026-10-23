# Parent release CP1 — addendum 1: CP2 v2 source pin, compatibility, self-identified binding gaps (NOEXEC)

Actual `/bin/date` before this write: `2026-10-19T17:06:40-0700`.

Applies to the immutable CP1 source `RUN/control/parent_release_caller_v1.py` `4072c50ef5be021a22e72a43571550c1338ab8a4d243752d88e3b7cc71a75cae` (re-hashed 17:02:27, unchanged), notes v1 `749118731d2b9f242016bcd230291f94e6ac4ca58b8ebe8ab58412e5972672b6`, disposition v1 `15eea3af220faec54fe2f2f178e60f272e65ce321d4aff63b30f23a680ce797d`, checkpoint003 `bcbf6cee61d623a52d89b12724d42ddbe4e74fd73d92d1ce519fee44e3e5881f`. It **supersedes** only: the notes v1 §Pins row "CP2 design freeze", the notes v1 source-readiness prerequisite 3, and the disposition v1 entry `external_held_prerequisites[2]` (CP2 v1 named as the dependency). Everything else stays as written. **No import, compile, AST, exec, test, probe or model CLI**; only source reading, `shasum`/`wc`/`ls` and this exclusive write. Not source acceptance; global HOLD unchanged.

## CP2 pins (ParentIdentityCP2 IRC 2026-10-19 ~17:02; every hash re-read with `shasum` at 17:02:27)

| Object | SHA256 | Status |
|---|---|---|
| `control/parent_release_identity_v2.py` | `7b2bc4021744aa6fa55677fa4953c9efc1088f53d341fb0ba339621abdddc3ec` (84818 bytes, 1593 lines) | The only CP2 source CP1 transactions may depend on; source-only, unreviewed, unqualified |
| `control/parent_release_identity_v1.py` | `d07548e2dbff4ef6b64a3a902d3b59ed7c4abbf8dc2115e8b08ed37ee2ec14d5` | Immutable HOLD (SR-1 MAJOR: PID-only unknown incarnations closed by H7). **Forbidden** for every CP1 transaction |
| `control/parent-release-cp2-design-freeze-v2.json` | `7f46b7e5f5581a6e905efa8405381208c9481332b26ba2e2a84f1ace436a1c28` | v2 delta frozen before code; = `DESIGN_FREEZE_SHA256` in the v2 union report |
| `control/parent-release-cp2-v2-repair-scope-v1.json` | `afe35832c808cf3d6a482fb6549dc8957d57ae982b7e48e76dba5b5374bcfa98` | Parent repair scope |
| `review/parent_release_identity_v1_to_v2.diff` | `ea20bf0283a100f3ef5e98ef1ad44d1a48a177e77344190e4c0e83a7e4dbaf05` | Exact v1→v2 delta |
| `control/parent-release-cp2-design-notes-v2.md` | `ea89e043903aa5ae0a5e2afdf69749dd01758b8199369b84022ccd0e8cce3012` | States formats/API unchanged; SR-4/SR-5 MINOR unrepaired |
| `review/parent-release-cp2-source-disposition-v2.json` | `bde19a8de1a03a6f3c66de61c37bda453841726fc670bc7bb254aa0820ac4545` | CP2 self-disposition (not acceptance) |

PRT3 `161ae04ce4ee98db76bb5b9b983cdfa13c769733b10159ebb5d31b5e377bd23a` was re-hashed at 17:02:27 and is unchanged.

## Compatibility of CP1 4072c50e with CP2 v2 — verified by reading only

| CP1 use (source lines) | CP2 v2 location | Finding |
|---|---|---|
| `_union` 690–699: union `format`/`state`/`union_sha256`/`prt_identities` | `UNION_FORMAT` 64, `CLOSED` 67, `_union_report` 1411–1424 | Same names and values. `prt_identities` is the list only when CLOSED, `None` when HELD |
| `prt_identities` typed-equal `spec.identities` (order-sensitive) | `_rows` 1382–1397 | Rows `{role,pid,pgid,start_fingerprint,source}`, sorted by role priority, pid, fingerprint. The parent must copy the list verbatim into `spec.identities` |
| `_served` 683–687: `log.served_count()` | `CensusLog.served_count` 550–551 | Zero-argument method returning `len(self.served)`, an exact int. A snapshot is appended only after a successful census return (643) |
| PRT3 `census` argument passed through unchanged | `make_census` 589–646 | Returns exactly PRT3's census keys (624–628). It raises on a deadline or native failure, so no served append |
| `_endedness` 823–841: `evaluate_endedness(state.union, census_log, deadline_check)` | 1537–1583 | Signature matches. Never raises Exception; BaseException propagates. Reads the union without mutating it (`_v_union` 1489–1507 builds a new body). Keys `format`/`state`/`causes`/`union_sha256`/`endedness_sha256` match CP1's checks |
| `_detach`/`_preflight` 211–283 applied to the union and endedness reports | Report assembly 1202–1257, 1400–1435, 1573–1579 | Both reports contain only dicts with str keys, lists, str, int, finite float, bool and None. Rows and logs are rebuilt fresh and `_rows` copies its rows, so no container is shared and CP1 accepts them. CP1 `_canonical` 249–251 is byte-identical to CP2 `_canonical` 312–314. The detached union therefore keeps the same `union_sha256` under `_v_union`'s recomputation (the one CP2 residual, SR-2, assumes no int-keyed dicts) |
| New sticky `U_UNKNOWN_INCARNATION` | 1260–1283, 1327–1331 | A union with that cause is HELD. CP1 refuses it at S3b with `CP1_IDENTITY_UNION` before PRT3 is loaded or invoked. Independently, CP2 `evaluate_endedness` fires `E_UNION_HELD`, which would become `CP1_ENDEDNESS`. No CP1 path can waive it |

Conclusion: the CP1 source needs **no change to interoperate** with CP2 v2. It contains no CP2 file path or digest, so it has no path to load CP2 v1. CP2 objects are parent-supplied, and their provenance remains the named prerequisite `identity_union_census_cp2`.

## Self-identified binding gaps in CP1 v1 against the v2 pin (unrepaired; the source is immutable and a successor is outside the CP1 write scope)

- **SF1.** CP1 cannot distinguish CP2 v1 (HOLD) outputs from v2 outputs. Both emit `parent-release-identity-union-v1`. CP1 checks none of `union.module` (`parent_release_identity_v2.py`), `union.design_freeze_sha256` (`7f46b7e5…`) or `endedness.module`. CP2 v2 `_v_union` checks only the format and the digest. A CLOSED union produced by the HOLD v1 module, which can close PID-only unknowns through H7 (the SR-1 defect), would therefore pass both CP2 v2 `evaluate_endedness` and CP1 v1. The only guard today is the parent attestation `identity_union_census_cp2`. CP1 checks just its `format`/`prerequisite`/`item`/`allocation_line_sha256`/`status`, none of which names a CP2 source digest. These fields are self-declared JSON, so checking them would guard against accidental misuse, not authenticate origin. The independent reviewer should grade this gap.
- **SF2.** CP1 does not bind `union.item` to `owner.item`. This is mitigated, not closed, by the `spec.identities` equality: PRT3 binds the unique driver row to the allocation's `driver_pid`/`driver_pgid` and to the launch driver fingerprint.
- **SF3.** CP1 does not require a fresh `make_census` pair (`served_before == 0`). CP2's SR-3 note requires a fresh pair per transaction. Reusing a log can only add served snapshots, and therefore E-causes, so the effect is HELD and never an unsafe release. CP2's census refuses after 16 served snapshots per log (`MAX_SERVED`).
- **SF4 (fail-closed boundary).** The CP1 `_preflight` size estimate is an upper bound of up to about 2× the actual canonical bytes for ASCII text. The node cap is 131072 and the depth cap 256. A valid CLOSED union, or a spec, above these limits is refused with HELD even where CP2 or PRT3 would accept it. Realistic CLOSED unions (a few members, at most 128 callback rows) are far below the caps.
- **SF5 (record completeness).** CP1 retains neither the union document nor CP2's `parent_release_endedness_partial`/`parent_release_identity_partial` attachments. The receipt binds `union_sha256`, which covers the union's self-declared `module`, `design_freeze_sha256` and `item`. An auditor can verify those only against the union document that the parent itself retains.

## Interim parent obligations while CP1 v1 is the caller

Issue the `identity_union_census_cp2` attestation for a transaction only if the parent itself established all of the following:

1. The union, `census`, `census_log` and `evaluate_endedness` all came from one execution of exactly the CP2 v2 bytes `7b2bc402…`, never v1 `d07548e2…`.
2. `union.module == 'parent_release_identity_v2.py'`, `union.design_freeze_sha256 == '7f46b7e5…'` and `union.item == owner.item`.
3. A fresh `make_census` pair was created for this transaction and used for nothing else.
4. The CP2 request inputs are authentic and complete. This covers CP2's `conditions_always`; the SR-5 request-binding MINOR is unrepaired.

Extra attestation keys such as `cp2_source_sha256`, `cp2_design_freeze_sha256` and `union_sha256` are recommended. They are permitted but **not checked** by CP1 v1.

## Decision requested from the parent: a CP1 successor needs a new parent write scope

- **Option A (minimal).** `parent_release_caller_v2.py` = v1 plus:
  - claim guards: union `module`, `design_freeze_sha256` and `item`, and endedness `module`, must equal the v2 values and the owner item, and the CP2 v1 module name is refused;
  - `served_before == 0`;
  - the `identity_union_census_cp2` attestation must carry `cp2_source_sha256 == 7b2bc402…`.

  This closes SF2 and SF3, and closes SF1 against accidental misuse only (claims, not authentication).
- **Option B (stronger).** CP1 reads the CP2 v2 bytes through the original reader, verifies `7b2bc402…`, and executes exactly those bytes in a fresh namespace, as it already does for PRT3. CP1 then:
  - builds the union itself, with `build_identity_union(detached owner-supplied CP2 request, reader.read_bytes, deadline_check)`;
  - creates a fresh `make_census(deadline_check)` pair, passing its `census` to PRT3;
  - calls that module's `evaluate_endedness`.

  The owner interface would replace `identity` with a CP2 request ref. This closes SF1–SF3 at code identity. The authenticity of the CP2 request inputs and the native libproc boundary remain external.

Without a successor, the arrangement is CP1 v1 plus the interim obligations above. SF1 then stays a named HELD prerequisite.

## Updated source-readiness prerequisite 3 (replaces notes v1 item 3; items 1, 2 and 4–6 unchanged)

3. CP2 v2 `parent_release_identity_v2.py` `7b2bc402…` must be independently reviewed and finitely qualified; v1 `d07548e2…` is forbidden. CP2 SR-4/SR-5 MINORs are open. On a busy shared host a v2 union is expected to be HELD (CP2 notes v2, "Availability consequence"), so the CP1 positive F01 practically needs a quiescent host for the whole run.

## Additional consumer-visible fault expectations (frozen, NOT exercised; same notation as notes v1)

| ID | Case | Expected |
|---|---|---|
| F41 | Otherwise complete positive, but the CLOSED union carries `module:'parent_release_identity_v1.py'` or a foreign `design_freeze_sha256` (synthetic attestation) | CP1 v1 fires **no** cause for these fields (SF1). The outcome follows the other inputs (R in a fully valid fixture). Freeze as a KNOWN-GAP control, never as a desired pass |
| F42 | `identity.census_log` comes from a different `make_census` pair than the `census` passed to PRT3 | Served count unchanged → H(CP1_ENDEDNESS) |
| F43 | Reused `census_log` holding an earlier served snapshot in which a union member is alive | CP2 `E_MEMBER_ALIVE` → H(CP1_ENDEDNESS); availability only |
| F44 | A CLOSED union or a spec above the CP1 preflight caps | H(CP1_IDENTITY_UNION) or H(CP1_SPEC_BINDING); fail-closed, PRT3 not invoked |
| F45 | `union.item` ≠ owner item while `prt_identities` is typed-equal to `spec.identities` | CP1 v1 fires no item cause (SF2). PRT3 decides through its driver binding to the allocation and launch |
| F46 | Union HELD only by sticky `U_UNKNOWN_INCARNATION` (CP2 C45/C46) | H(CP1_IDENTITY_UNION); PRT3 neither loaded nor invoked |

These are source-derived expectations, not observed output. Synthetic fixtures prove predicates, not OS provenance.
