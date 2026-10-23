# Sun5/Sun6 second-checker no-tools review prompt sets: frozen plan and exposure v1

- Written: 2026-10-19T17:53:07-0700 (host /bin/date immediately before writing). Preparer: SunCheckerPackets (task subagent of Main; packaging only, not an author or reviewer of any subject). Write scope: this directory only, every file created with exclusive mode `x`; corrections only as new numbered files.
- Authority: `RUN/control/native-repair-and-second-checker-review-packaging-v1.json` sha256 03980aa42cb0e315b1b73eb349a8890a7d60fb191b4adca08764c4dceca70352 (group `second_checker_packets`). Entry points: Sun5 `07-manifest-v1.json` 356fb271c0965dbd7c130c6224407cbcdbd3397e0fcdcb8dfa632114358795c1; Sun6 `SOURCE-REVIEW-PACKET-v1.md` 4fd862dc7a92562e79c0ec5db0f7d0cc2bf2f1c3b0a46988a6f54878b1898bbb (both recomputed from bytes, equal).
- Status: SOURCE_ONLY, GLOBAL RUNTIME HOLD. Nothing is executed, imported, compiled, AST-parsed, tested, linted or formatted. No review is launched; no model CLI, nested agent, /tmp, deletion or external action. Packaging = file reads, SHA-256, physical-LF line slicing and JSON metadata parsing of the frozen author/plan files only (never of scientific DATA: the pinned inputs and the 37 Sun5 fixture TSVs are hashed only).

## 1. Exposure frozen before drafting

Read in full or in part (sha256 recomputed for each): the authority control file; Sun5 manifest, Sun5 packet v2 (structure grep, lines 1-25 and 3866-3934, byte-level binding check of all 17 embedded bodies), map addendum 1, controls plan lines 1-143 and 1125-1212; Sun6 packet lines 1-50 (+ section grep), INPUT-PINS, READLOG, SHA256SUMS, CONTROLS-PLAN lines 1-123, SCOPE-DESIGN headings; named authorities: source scope 6cc055bc..., full-gate ruling 4818f1ca..., Sun5 parent verdict 2cf02436... (full); grep hits only in Sun6 entry verdict efe1d849... and ACCEPTANCE-AMENDMENT (input pins); heading greps of CERT-FORMAT-k6-v3, rules-k6-erratum-v3, ACCEPTANCE-AMENDMENT; text greps of top-level `def`/`class` lines of the three new code files. Format conventions only: key lists/format fields of two existing packet indexes in RUN/review and grep lines of `RUN/control/run_codex_review_v1.py` / `run_prompt_review_v1.py` (prompt path must be inside RUN; outputs written beside the prompt; Claude runs with `--tools ''`).
Will read for construction: exact bytes of every file listed in section 3 (slice/hash/number only).
Never read: any earlier Sun5/Sun6 engine, lane checker, bridge/labelled verifier, earlier independent checker, old controls source, parent auxiliary implementation, replay reports; any fixture/input content beyond hashing.

## 2. Pre-construction binding checks already performed (preparer checks, not parent verification)

- Sun5 packet v2 (183916 B, 8f7c36ea...): all 17 FILE bodies equal the on-disk files byte-for-byte between `~~~~~` fences, stated sha256/bytes equal disk; the two DATA files (survivors.json, run.json) have no final LF on disk and the packet adds exactly one LF before the closing fence. Packet framing = 6415 B.
- Sun6 packet v1 (94906 B): checker (lines 51-1492), controls harness (1498-1968) and MATH-BRIDGE (1973-2071) embedded byte-exactly; framing 5307 B; it lacks CONTROLS-PLAN, INPUT-PINS, RESOURCE-LIFECYCLE-PLAN, SCOPE-DESIGN, READLOG and all nine mathematical sources.
- All nine Sun6 math sources and the five Sun5 math sources + two Sun5 DATA files hash to the values in the authors' read logs / packet.

## 3. Slices (one prompt text per slice; byte-identical Codex and Claude copies)

Rendering: code and bridge/map files as `<physical line>|<exact line text>` per LF line; all other files raw. Every block is wrapped in `<<<BEGIN <block-id> ...>>>` / `<<<END <block-id>>>>` with path, role (OWNED or CONTEXT), inclusive physical line range, byte range [x,y), range_sha256, file_sha256, file_bytes, file_lines, render mode. Hard limit: each prompt < 220000 B. Optional CONTEXT blocks are appended in the listed priority order only while the prompt stays <= 216000 B; every optional block not included is a declared omission.

### S5FULL (Sun5; single slice, no split needed)
OWNED: `code/sun5_second_checker_v1.py` L1-1021 (numbered); `01-proof-to-code-map-v1.md` (numbered); `01-proof-to-code-map-v1-addendum-1.md` (numbered); `02-scalar-schema-v1.md` (numbered); `controls/04-controls-plan-v1.json` (P0, 37 fixture controls, 7 interface controls, acceptance rules, settlement); `controls/fixtures-manifest-v1.json`; `05-input-resource-plan-v1.json`; `00-scope-design-v1.md`; `03-independence-declaration-v1.md`; `03-read-log-v1.json`; packet v2 lines 1-15 (author checklist/claims).
CONTEXT (mandatory): proof-v4.md, rules-v1.md, rules-v1-erratum-v3.md, README.md, README-addendum-v4.md, DATA survivors.json and run.json (untrusted), source scope, full-gate ruling. CONTEXT (optional, priority 1): Sun5 parent verdict 2cf02436 (routes only).

### S6A checker + mathematical bridge (Sun6 split is necessary: all Sun6 author files + nine sources > 270 kB)
OWNED: `code/sun6_second_checker_v1.py` L1-1442 (numbered); `MATH-BRIDGE-v1.md` sections 0-10 (numbered); `INPUT-PINS-v1.json`; Sun6 packet lines 1-46 (author independence statement, file table, attack list, deliberate choices).
CONTEXT (mandatory): the nine named sources README.md, proof-k6-v3.md, proof-k6-lemmas-v1.md, rules-k6-v1.md, rules-k6-v2.md, rules-k6-v3.md, rules-k6-erratum-v3.md, CERT-FORMAT-k6-v3.md, ACCEPTANCE-AMENDMENT-v1.md; source scope; full-gate ruling. CONTEXT (optional, priority order): entry verdict efe1d849; RESOURCE-LIFECYCLE-PLAN-v1.json; SCOPE-DESIGN-v1.md.

### S6B controls harness + controls plan + lifecycle plan + design/independence records
OWNED: `code/sun6_second_checker_controls_v1.py` L1-471 (numbered); `CONTROLS-PLAN-v1.json` (header clauses + all 124 controls); `RESOURCE-LIFECYCLE-PLAN-v1.json`; `SCOPE-DESIGN-v1.md`; `READLOG-v1.json`; `SHA256SUMS-v1.txt`.
CONTEXT (mandatory): full checker alias (numbered, identical bytes to S6A's owned block); MATH-BRIDGE alias; source scope; full-gate ruling. CONTEXT (optional, priority order): rules-k6-erratum-v3.md; CERT-FORMAT-k6-v3.md; INPUT-PINS alias; Sun6 packet lines 1-46 alias; rules-k6-v1.md.

## 4. Ownership rule

Every physical line of the three code files, every heading-delimited clause of the two bridges (Sun5 map + addendum, Sun6 MATH-BRIDGE), every top-level key and every control entry of the two controls plans, and every top-level key of the two resource/lifecycle plans has exactly one OWNED slice. Code units are contiguous text blocks starting at a column-0 `def`/`class`/decorator line (module text before the first unit is its own unit); clause units are heading-delimited line ranges; control units are the JSON entry line ranges. CONTEXT copies are byte-identical and never owned. The index records the per-unit owner and verifies disjoint, complete coverage.

## 5. Review content required in every prompt

No tools; static source review only; no runtime or qualification inference; no acceptance authority. Attack list covering strict parsing, full-universe/orbit set equality, FH alternatives (Sun5 FH2 both H2 alternatives for the same pair; Sun6 FH5 domains/placements), exact rational arithmetic and unbounded-cofactor (sup-gcd / saturation) reasoning, intended-reason control expectations, lifecycle limits, and import gates (stdlib-only code imports, harness pinning, mathematical imports Zhu/L0.6/R0/R1/minimality, Sun6's Sun(5) import). Fixed reply format: line 1 `VERDICT: <HOLD|READY_WITH_FIXES|READY> | FATAL=<n> MAJOR=<n> MINOR=<n> | SCOPE=<slice> | SUBJECT=<sha8 list>`; then findings with owned-unit citations, joins relied on, coverage statement, remaining empirical obligations, and a no-grant sentence.

## 6. Joins, omissions and boundaries (finalised in the index)

Joins: S6A<->S6B checker semantics / harness interface / lifecycle limits; external: fixture and pinned-input bytes (not embedded), shared owned guard + parent five-part release, written lemmas and imports (common-mode for both checkers), Sun6's Sun(5) import gate vs the separate Sun5 second-checker gate. Declared omissions: Sun5/Sun6 checkpoints, Sun5 packet v1 (superseded), Sun5 manifest, Sun6 packet framing outside lines 1-46, input/fixture DATA, any optional context not fitting. Boundaries: one author per checker package (checker, controls and plans are shared-author), common written sources with the original checkers, single preparer for all prompts, family independence only between Codex and Claude.

## 7. Deliverables

`sun5-2nd-S5FULL-{codex,claude}-v1.prompt.txt`, `sun6-2nd-S6A-{codex,claude}-v1.prompt.txt`, `sun6-2nd-S6B-{codex,claude}-v1.prompt.txt`, `prompt-index-v1.json` (whole-file hashes, block maps with prompt byte offsets, ownership map, joins, omissions, boundaries, preparer checks, launch note), `SHA256SUMS-v1.txt`, checkpoints (<= 1800 s apart, target 1200 s). Preparer read-back checks: recover every block's bytes from the written prompt and compare range_sha256; ownership coverage; size limit. Parent verifies and launches; nothing here is launched.
