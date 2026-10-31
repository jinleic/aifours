**Slice B review — f264-guessing-checker-static-assurance (read-only, no execution)**

**Pre-checks (all passed):** manifest-v1 SHA-256 `e88658c9…7952`, 9180 B. All 18 declared inputs matched SHA/bytes/LF (`shasum`/`wc`/`tr` run above). Inputs read completely in declared order: errata 01–05 → spine 06–15 → declaration (685/685) → `checker-v4.py` (1–1274) → `projection-checker-v1.py` (1–520). No archive body, no code executed/imported, no files changed.

## Findings

**F — none.** No path found where either checker returns a success status on the pinned archive without the claimed finite check having run; all exception classes map to `REJECT`/`UNKNOWN` (v4: `checker-v4.py:1262-1267`; projection: `:514-518`), success codes are set only after full completion, and every consumed byte stream is hashed against constants or a constant-pinned manifest (v4 `:1093-1094, :1114-1115, :819-820, :1136`; projection `:452-470`).

**M1 — `checker-v4.py`: visibility-row acceptance is wider than visibility-applicability enforcement (crafted-scope false pass in plane binding).**
`row_vector` accepts `['syndrome-neighborhood', v]` for any `v` in the *union* `visibility_required ∪ {syndrome_visibility_vertex} ∪ visible(syndrome_plane)` (`:491-497`), and `validate_system` permits all three fields together (`:552-561`). But applicability consumers each honour only one source: `validate_actions` group-invariance only for `visibility_required` (`:598-599`); `required_visibility` returns `visibility_required` and ignores `syndrome_visibility_vertex` when both exist (`:912-923`); `certificate_actions` returns plane-transport actions and ignores both others when `syndrome_plane` is present (`:931-934, :943`); applicability mode uses `visibility_required` only (`:732-741`).
Reproducer (descriptive): scalar n11 record, `scope={'visibility_required':[6],'syndrome_visibility_vertex':7,'group':[identity]}`, actions `[identity]`, rows include `['syndrome-neighborhood',7]` → identity VALID; `verify_plane_roster`/`verify_applicability` bind it to any plane with `6 ∈ visible` even when `7 ∉ visible`, so `H(S|Y_N(7))=0` is consumed without the injectivity premise → `VALID_ARCHIVE_FINITE_REPLAY_CONDITIONAL` / `VALID_APPLICABILITY_CONDITIONAL` with an unmet premise. Variant: `syndrome_plane` + `visibility_required=[v]`, `v ∉ visible(source plane)`. Whether the real archive's scalar scopes combine fields is **not determinable here** (bodies unread) — code path is unconditional. Fix: make the three declarations mutually exclusive, or derive `declared` in `row_vector` from the same function used by `certificate_actions`/`verify_applicability`.

**M2 — `checker-v4.py`: noncover binding cannot represent the delete-1 three-colour proof → bulk replay must REJECT for a checker-side reason (false reject / misattribution, not false pass).**
`verify_plane_roster` forces every `noncover` plane (category computed by the checker itself, `:1038`) to bind to a verified 9-variable certificate with `scope.missing_vertex == rep` where `proper_actions[aid][rep-1]==missing` (`:1050-1056`). Planes missing only vertex 1 exist (e.g. directions `a=factors{4,5,6}`, `b=factors{7,8,9,10}`; triangle union = {2..10}); automorphisms preserve degree so `rep ∈ {1,8}`. Per the declaration inventory the only n9 records are two (`cmi 456 = 186+270`, `fd 18`, `conditional_entropy 2` — exactly source 06's k=2 and k=3) → no certificate with `missing_vertex ∈ {1,8}` → `REJECT NONCOVER_PROOF_BINDING`. `proper_delete_1_color` is validated (`:866-870`) but never bound. [INFERENCE on archive content from inventory arithmetic; code path certain.] A REJECT from a bulk run would misread as an archive defect.

**m (minor), checker-v4.py**
- m1 `:615-616, :884-885`: `source_index` accepts int, digit-string and `None`; dedupe key `json.dumps` treats `3` and `"3"` as distinct locations, so two certificates may bind one source record; `None` permits a certificate with no source location. Projection checker requires int (`:262`). Suggest `type(...) is int`.
- m2 `:1183, :1262-1270, :1170-1179`: signals delivered after the `except` block or inside `output_exclusive` raise `Unknown` outside any handler → traceback, possibly a partially written O_EXCL file; rerun then returns 73. Fail-closed but result lost.
- m3 `:1201`: `INVALID_RESOURCE_CAP` exits 2 (same as REJECT) with no output file.
- m4 `:808` docstring says pin is verified "before exhaustion"; it runs after the last line (`:819-820`). Covered in archive mode by the pre-hash loop (`:1112-1115`); doc nit.
- m5 `:1157-1159`: r382 mode binds the record to itself (no packet-index binding); status string is truthful (`R382_IDENTITY_CONDITIONAL`) — note only.

**m (minor), projection-checker-v1.py**
- m6 `:67`: no `parse_float`/`parse_constant` rejection and `json.loads(bytes)` auto-detects UTF-16/32. All numeric use-sites type-check (`integer`, `read_vector :194-205`, `rational :74-76`), so no false pass found; strictness gap vs v4.
- m7 `:76`: no canonical-form check on rationals (`'2/4'` accepted); comparisons are by `Fraction` so correct; `identical_multiplier_spellings` is informational only.
- m8 `:467-472, :504`: record read at hard-coded offset 43967; the prefix is never checked to be exactly one LF-terminated line, so "record index 1" is manifest-asserted (honestly disclosed). Record bytes are SHA-pinned so content is bound. Cheap fix: `prefix.endswith(b'\n') and prefix.count(b'\n')==1`.
- m9 `:474-476`: TOCTOU detection is fstat metadata, not a re-hash (v4 re-hashes `:1136`). Low practical risk.
- m10 `:480-481, :515`: timeout raises `Reject('cap.exceeded')` → same label/exit as definite rejections (`UNKNOWN_OR_REJECTED`, 2); SIGINT/SIGTERM unhandled → traceback, no JSON (fail-closed).
- m11 `:442, :463`: unbounded `read_bytes()`/`member.read()` before size check; bounded in practice by pinned manifest sizes and zip header `file_size` [INFERENCE on zipfile truncation].

## Confirmed sound (Slice B)
Strict JSON (duplicate keys, floats/NaN rejected, `type is int` excludes bool) `:88-104, :109-112`; canonical rationals `:115-123`; bounded pinned reads `:128-140`; manifest/declaration binding `:145-176`; member path/duplicate guards `:825-843`; row-cap/plane-cap/time-limit → `UNKNOWN` throughout; default caps make archive mode `UNKNOWN` unless explicitly raised (`:1089-1091, :1193`); no extraction/deletion/network; output O_EXCL 0600.

## Coverage / uninspected
Full line coverage of both code files and all 16 non-code inputs. Not inspected (not declared): f257 `manifest-v1.json` (expected `2db2c570…`), f258 `manifest-v1.json` (`78644091…`), archive `3bde5418…` bodies, R382/source member bytes, predecessor v2/v3. CPython `zipfile` behaviours (seek, `readline(limit)`, truncation at `file_size`, CRC at EOF) are [INFERENCE], not executed. `controls()` outcomes are read-only inferences.

## Verdict
M1, M2 + minors; **no F**. No bulk-replay GO: M2 predicts a checker-side REJECT on the pinned archive, and M1 is a latent applicability false-pass path whose real-archive exposure cannot be settled without archive bodies. Nothing here is a theorem or source-projection claim.
