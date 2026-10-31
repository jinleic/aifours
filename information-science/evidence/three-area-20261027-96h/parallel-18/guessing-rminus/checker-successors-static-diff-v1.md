# Static successor diff summary: checker v5 / projection v2

**Delivery scope:** the requested code successors for a new diff-focused static review. Neither successor has been executed. No real archive or R382 replay, synthetic controls, tests, compilation, linting or formatting was run. This document is not a GO or a mathematical verdict.

## Source pins

| New file | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `checker-v5.py` | `8258ab4935e3f42ca74e9dc8e2287b6e31a7ddbcffdfb06fc085a62bdc6f7a06` | 72863 | 1328 |
| `projection-checker-v2.py` | `b60b85b65fd1b355132e6dbd7a14b0fe6ec9f8e71d76bd99a432b13b06ab72b4` | 31429 | 629 |

Immutable predecessor v4: `43e44f78a012573674d31b0d03696c282f7378f5e192c58c19099451bab86020` (/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f257-guessing-declaration-bound-streaming-checker/checker-v4.py).
Immutable predecessor PJv1: `20fe0113842da67c8209962d324d1a4bd74f0b68e1d86e054bcf7563aea87495` (/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f258-guessing-r382-source-projection-audit/projection-checker-v1.py).
Both predecessors and the archive/declaration/common-local-information submission were left untouched. All three new deliverables are in the exclusive owner root.

## MAJOR 1: one complete visibility contract

- `checker-v5.py:927-957` now constructs one set from the explicit list, the singleton declaration and its scope-group orbit, and the intrinsic plane visibility. Explicit declarations must be a subset of visible(plane) before that intrinsic set is added (`DECLARED_VISIBILITY_NOT_VISIBLE_IN_PLANE`). No branch silently drops a declaration.
- Row acceptance: `checker-v5.py:425-504`; scope validation: `checker-v5.py:534-561`; action closure: `checker-v5.py:562-602`; direct applicability: `checker-v5.py:724-775`; source-to-client transport: `checker-v5.py:958-979`. They all consume that same helper. The old early plane-transport return was removed, so plane transports also enforce the full visibility set.
Validity of any actual-law visibility premise remains a separate written scientific obligation; the new code only aligns its declared guards and transport consumers.

## MAJOR 2: deletion-1 colour proof is actually consumed

- `checker-v5.py:857-863` is shared by graph-metadata validation and noncover use.
- `checker-v5.py:1056-1140` accepts the frozen `D1-color`/representative-1 route by transporting the validated proper-delete-1 colouring through the declared proper graph action, checking its exact target domain and every induced edge. It no longer requires a nonexistent n9 matrix for the {1,8} deletion orbit.
- `checker-v5.py:1141-1195` passes the already validated `proper_delete_1_color` data into that route. Missing proof categories produce named UNKNOWN reasons (`MISSING_NONCOVER_DELETE_ONE_COLOR_ARGUMENT` / `MISSING_NONCOVER_ARGUMENT_CATEGORY`) rather than an unexplained archive-defect rejection.
An invalid available n9 proof binding still rejects. The written three-colour entropy argument and fibre lift are not promoted by this finite graph check.

## Source-location typing: exact numeric positions, no coercion

- `checker-v5.py:603-623` is shared by identity/binding admission and index dedupe (`checker-v5.py:624-692`; `checker-v5.py:888-904`). Every array position is an exact nonnegative int; bools and numeric strings are not array indices.
- The immutable export has seven deliberately non-array locations. The one named n9 dictionary member permits only literal keys `"2"`/`"3"`, bound to the exact-int missing vertex. The five named standalone scalar members permit only a root-object `null` locator. Those cases are explicitly typed, not converted into array indices; other member kinds cannot borrow them. This is the informed compatibility choice reported to Main, because blindly rejecting all seven would prevent the frozen real inputs from being admitted.
- Class-map source positions are independently exact-int checked in `checker-v5.py:980-1018`. Typed locators prevent mixed-spelling aliases from surviving dedupe.
No all-source projection claim is made: source/export equality beyond the separately scoped projector remains UNKNOWN.

## Projection successor v2

- `projection-checker-v2.py:128-198` covers `aux-determined` and `functional-local-fd`; the latter requires exactly one selected incident colour and the actual selected-component local set. Unsupported source/certificate layouts return explicitly named UNKNOWNs in `projection-checker-v2.py:260-343`; the admitted real scope is still the single pinned R382/recovered-source format, not a bulk projector.
- `projection-checker-v2.py:519-524` requires the exact 43967-byte prefix to be one LF-terminated line with no CR. `projection-checker-v2.py:525-579` reads/checks it before the record and retains the pinned record-byte check. The preceding line is not parsed as a mathematical input.
- `projection-checker-v2.py:494-504` and `projection-checker-v2.py:505-518` bound allocations/stream reads before consuming inputs. Source/member sizes are admitted before reads. The same open archive handle is hashed both before and after consumption, in addition to fstat checks.
- `projection-checker-v2.py:72-91` explicitly decodes UTF-8 and rejects floats/NaN; `projection-checker-v2.py:92-101` requires canonical exact fraction spellings.
- `projection-checker-v2.py:580-584` raises UNKNOWN for deadlines/interruption. The final envelope (line 617 onward) reports UNKNOWN/exit3 separately from REJECT/exit2; the alarm is cleared in its finally path. The manifest record index is exact-int checked.
- `projection-checker-v2.py:390-489` includes new descriptor, JSON, prefix and timeout cases. They are authored but NOT executed. The editor reported an intermediate syntax error from placing two fixture entries inside the multiline gate literal; that placement was corrected. No interpreter/compiler was invoked to confirm it.

## Other narrowly related changes / retained boundaries

- The n9 inner `name.multiplier` is now typed provenance only, not required to equal or multiply the authoritative top-level coefficient. This follows the frozen declaration. The stream docstring now correctly says its digest is checked after the final line.
- Both relocated sources use explicit paths to the original frozen input manifests, so owner-root placement does not accidentally select a nonexistent/different adjacent manifest.
- The frozen written-source gate bookkeeping is not edited. No unsupported n11 gate alias was invented. The inherited identity-mode duplicate-descriptor policy and exclusive-output signal edge cases are not claimed repaired or assured by this focused change.
- Existing fail-closed `UNSUPPORTED_SCOPE_FIELDS` / unsupported-source-layout boundaries remain. No claim that every real archive metadata layout has been exercised or admitted is made; no real-data compatibility test was run.

## Exact textual change locations

Ranges below come from a textual diff only, not code execution. An empty old/new span denotes an insertion/deletion gap.

### checker-v5.py

| Change | Predecessor lines | Successor lines |
|---|---:|---:|
| replace | 2-2 | 2-2 |
| replace | 29-29 | 29-38 |
| replace | 491-497 | 500-501 |
| replace | 553-561 | 557-557 |
| replace | 597-597 | 593-593 |
| insert | 607-606 | 603-623 |
| replace | 614-619 | 631-632 |
| replace | 655-655 | 668-669 |
| replace | 732-735 | 746-747 |
| replace | 808-808 | 820-820 |
| insert | 845-844 | 857-863 |
| replace | 866-870 | 885-885 |
| replace | 884-884 | 899-899 |
| replace | 913-917 | 928-939 |
| replace | 920-923 | 942-956 |
| delete | 931-934 | 964-963 |
| replace | 936-936 | 965-967 |
| insert | 940-939 | 971-972 |
| insert | 963-962 | 996-996 |
| replace | 964-964 | 998-998 |
| replace | 1022-1022 | 1056-1056 |
| replace | 1055-1056 | 1089-1109 |
| replace | 1131-1131 | 1184-1185 |

### projection-checker-v2.py

| Change | Predecessor lines | Successor lines |
|---|---:|---:|
| replace | 2-2 | 2-6 |
| replace | 15-15 | 19-19 |
| insert | 18-17 | 22-23 |
| insert | 45-44 | 51-57 |
| insert | 66-65 | 79-80 |
| replace | 67-67 | 82-85 |
| replace | 76-76 | 94-99 |
| replace | 112-112 | 135-136 |
| replace | 133-133 | 157-161 |
| insert | 146-145 | 174-180 |
| insert | 226-225 | 261-262 |
| insert | 240-239 | 277-278 |
| insert | 361-360 | 400-401 |
| insert | 419-418 | 460-461 |
| insert | 428-427 | 471-486 |
| insert | 435-434 | 494-524 |
| replace | 436-436 | 526-526 |
| replace | 439-439 | 529-530 |
| replace | 442-442 | 533-534 |
| replace | 444-444 | 536-536 |
| insert | 449-448 | 541-541 |
| replace | 451-454 | 544-545 |
| insert | 459-458 | 550-551 |
| replace | 461-461 | 554-556 |
| replace | 463-464 | 558-559 |
| replace | 467-469 | 562-565 |
| replace | 472-472 | 568-572 |
| replace | 481-481 | 581-582 |
| replace | 486-486 | 587-588 |
| replace | 492-492 | 594-594 |
| replace | 504-504 | 606-606 |
| insert | 512-511 | 614-614 |
| insert | 514-513 | 617-619 |
| replace | 515-516 | 621-622 |
| replace | 518-520 | 624-629 |

## Next authority boundary

Main should first freeze the requested two-slice diff-focused static review against the unchanged declaration/spine. Only after explicit later permission should synthetic controls and any separately pinned one-record diagnostic be exercised. Full real archive replay remains NO GO. No prior PASS or receipt is adopted or retroactively repaired.
