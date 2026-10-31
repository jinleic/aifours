The `write` tool refused the repository path; no file was created. Below is the complete review verbatim for the parent to materialize at the assigned path.

# f267 Slice B — fail-closed closure, projection v2, and diff fidelity

Native `/bin/date` observed before composing: **2026-10-29T17:59:41-0700 PDT**.

## Verdict and scope

**Verdict: PARTIALLY CLOSED. FATAL: 0; MAJOR: 0; MINOR: 3 residual issues in the assigned B scope. Newly introduced, actionable code defects found: 0.** The three residual issues are the unchanged written n11-gate bookkeeping mismatch, v5 signal/exclusive-output handling, and v5 invalid-cap exit/output handling. They are inherited f264 observations, not patch-introduced findings. Duplicate-descriptor policy is also unchanged and is noted separately rather than counted in B's signal/exit slice.

The changed executable behavior is consistent with its stated finite-check boundary by static inspection. In particular, the two new projector descriptor kinds have explicit consuming branches, the prefix is checked before the pinned record is read, the archive is re-hashed before parsed source/record use, and timeout is no longer a definite rejection. This is **not** a claim that either successor has executed successfully or that every f264 observation is repaired.

**Bulk-replay recommendation: no unconditional GO from this return.** B finds no new MAJOR blocker in the changed fail-closed/projector paths, but does not grant replay authority or whole-wave clearance; the parent must combine the soundness slice, the residual dispositions, and the prospective authority boundary. No checker, control, diagnostic, archive replay, import, compilation, or test was run.

### Path abbreviations

All paths are rooted at `/Users/jinleic/repos/aifours/`:

- `E/` = `institute/runs/three-area-2026-10-27-96h/review-waves/evidence-f235-f236-v1/`.
- `W/` = `institute/runs/three-area-2026-10-27-96h/review-waves/`.
- `O/` = `information-science/evidence/three-area-20261027-96h/parallel-18/guessing-rminus/`.
- `V4` = `W/f257-guessing-declaration-bound-streaming-checker/checker-v4.py`.
- `PJ1` = `W/f258-guessing-r382-source-projection-audit/projection-checker-v1.py`.
- `V5` = `O/checker-v5.py`; `PJ2` = `O/projection-checker-v2.py`.
- `DECL` = `O/frontier-20261029-archive-row-semantics-declaration-v1.json`.
- `DIFF` = `O/checker-successors-static-diff-v1.md`.

## f264 outcome items 1–8

Items 4, 5, 7's signal/exit surfaces, and 8 are the assigned substantive B dispositions. The remaining rows record the guard changes seen in the mandatory complete reading; their full soundness disposition belongs to Slice A.

| f264 item | Disposition | Exact successor evidence and boundary |
|---|---|---|
| 1 — visibility acceptance versus applicability | **CLOSED, static guard alignment** | `V5:927–956` unions the explicit list, singleton and its scope-group orbit, and intrinsic plane visibility; `V5:953–955` requires explicit declarations to be visible in the source plane. The same helper is consumed by row admission `V5:498–502`, scope validation `V5:553–557`, action validation `V5:591–599`, direct full-visibility applicability `V5:746–754`, and certificate transport `V5:964–977`. The old plane-only early return is gone. Actual-law visibility remains a written premise, not inferred from a label. |
| 2 — delete-1 noncover category | **CLOSED for the parent-required roster repair / named-unsupported alternative** | `V5:857–862` validates the delete-1 coloring; `V5:1093–1103` consumes it specifically for representative 1 and `D1-color`, transports its complete domain, and checks every surviving graph edge. `V5:1183–1185` supplies the validated graph metadata to this consumer. Missing argument categories become named UNKNOWNs at `V5:1094–1095,1108–1109`, rather than an unexplained archive-defect REJECT. The valid n9 branch is retained at `V5:1089–1092`; a wrong binding when an applicable n9 category exists still rejects at `V5:1104–1107`. Standalone `verify_applicability('noncover')` remains n9-certificate-only (`V5:727–738`); it does not claim to expose the new coloring route. No frozen roster body was opened to confirm its literal proof IDs. |
| 3 — source-location typing/dedupe | **CLOSED for typed locations, with explicit documented exceptions** | `V5:603–622` admits exact nonnegative integer array positions, only literal `"2"`/`"3"` for the named n9 dictionary source bound to an exact-int missing vertex, and null only for the five named scalar root sources (`V5:31–38`). Identity/binding admission invokes the helper on both sides (`V5:628–632`); index dedupe uses the same typed tuple (`V5:899–900`); class-map array positions are independently exact-int checked (`V5:996–998`). `PJ2:301–302` retains exact-int `source_index`; its fixed manifest record ordinal is now exact-int checked at `PJ2:594`. The author's assertion that these are the seven actual non-array locations is not an archive observation by this reviewer. |
| 4 — missing projector kinds | **CLOSED** | `PJ2:132–138` admits both added kinds into dispatch; `PJ2:157–159` implements `aux-determined`; `PJ2:173–180` implements the singleton-color local decoder. Their formulas and premises match `V5:458–472` and `DECL:133–139,159–166`. Source/export rows actually pass through these branches at `PJ2:291–297,324–336`, not merely through an unused registry. Other source/certificate dictionary layouts explicitly produce UNKNOWN at `PJ2:261–262,277–278`. This remains a single pinned recovered-source projector, not coverage of all source layouts. |
| 5 — written n11 G_S bookkeeping | **OPEN, inherited MINOR; no new false claim** | V5's n11 descriptor schema is still only `V5:56–62`, with no gate. An n11 gate reaches `UNSUPPORTED_DESCRIPTOR` at `V5:418–419`; the sole declared gate is functional (`V5:72,441–443`) and its R382 locator is enforced at `V5:664–666,686–688`. The frozen caller still says the 219 mixed identities use G_S (`E/15-frontier-20261029-all-affine-syndrome-plane-entropy-v1.md:115`), whereas DECL inventories only the R382 functional gate (`DECL:250–263,571–585`). `DIFF:49` expressly leaves the bookkeeping unedited and says no n11 alias was invented. No new comment/status promotes G_S to an undeclared n11 premise. |
| 6 — n9 redundant inner multiplier | **CLOSED** | `V5:667–669` now types the inner multiplier as provenance without equating it to, or applying it in addition to, the top-level coefficient. The authoritative coefficient is parsed at `V5:662–663` and applied once with action averaging at `V5:684`. This matches `DECL:243,247`. |
| 7 — duplicates, signals/output, invalid caps, stream order, r382 status | **PARTIALLY CLOSED** | Stream-order wording is corrected at `V5:820`; actual digest comparison remains after the generator's last yield (`V5:830–832`), with archive pre-hashing at `V5:1163–1169`. The r382 self-binding/status boundary stays truthful (`V5:1214–1217,1281–1284`). But signal/output and invalid-cap paths remain open as detailed below. Duplicate descriptors also remain accepted in the V5 identity loop (`V5:659–684`), unlike `PJ2:249–256,319`; DIFF does not claim this was repaired (`DIFF:49`). |
| 8 — PJ parsing, framing, read caps, TOCTOU, timeout | **CLOSED for the listed f264 fixes** | Explicit UTF-8 and numeric-literal rejection: `PJ2:79–89`; canonical rationals: `PJ2:92–99`; bounded file reads: `PJ2:494–502,526–537`; source/record size admission: `PJ2:550–559`; single-LF prefix before record read: `PJ2:519–522,561–565`; same-open-handle archive re-hash before return/use: `PJ2:570–578`; distinct UNKNOWN/3 versus REJECT/2: `PJ2:580–582,617–627`. This does not promise immunity to a further asynchronous signal during exception reporting or after the envelope's try/finally. |

## Assigned B analysis

### 1. PJ2 descriptor semantics and consumer routing

For `['aux-determined', b]`, PJ2 emits `+h_b(V) − h_0(V)` with exact branch range 1–4 (`PJ2:157–159`). V5 obtains exactly that vector from `conditional_vector(1024,1023,b,True)` (`V5:458–460`, with coordinate mapping at `V5:350–359`). Neither implementation confuses this equality with an unconditional entropy bound.

For `['functional-local-fd', v, c]`, PJ2 first requires the incident selected color set to equal `{c}`, then constructs `h_(2+c)(L_J(v)∪{v}) − h_(2+c)(L_J(v))` (`PJ2:173–180`). V5 has the same singleton guard and selected-factor local set (`V5:465–472`). PJ2's additional nonempty/subset-of-neighbors check is automatically satisfied for a nonempty singleton incident set in the literal triangle graph: every other vertex in each incident triangle is a graph neighbor (`PJ2:25–33,118–125`). It does not add an incompatible scientific premise on valid declared colorings.

The added kinds reach both the source sign-validation loop and the exported-row image comparison (`PJ2:291–297,324–336`), then the full exact identity at `PJ2:597–598`. There is no unmatched dispatch, no silent drop, and no newly admitted kind that bypasses image reconstruction. Unknown dictionary layouts have explicit UNKNOWN outcomes, while an invented descriptor still correctly rejects as `descriptor.kind`; the requirement was to implement or explicitly mark the two named missing kinds, and both are implemented.

### 2. PJ2 framing, bytes, and re-hash order

- `PJ2:519–522` requires exactly 43967 prefix bytes, starts with `{`, ends in LF, has exactly one LF and no CR. `PJ2:561–565` reads and validates that prefix before reading the pinned record. The record itself must retain its declared SHA and one-line LF framing (`PJ2:565–569`). The prefix is checked for framing only, not interpreted as another mathematical certificate. `PJ2:606` accurately describes the strengthened ordinal evidence.
- `bounded_file_bytes` checks fstat size before its bounded `limit+1` read and checks the actual returned length afterward (`PJ2:494–502`). Each manifest input's admitted size is exact-int and at most 1,000,000 (`PJ2:533–534`). Source and record sizes are checked before member reads, and the ZIP metadata must cover the requested span (`PJ2:550–559`). No formerly unbounded `Path.read_bytes()` or source `member.read()` remains in PJ2.
- The archive length is checked before its initial bounded hash (`PJ2:541–545`), and `bounded_digest` limits every block and refuses overflow (`PJ2:505–516`). After the bounded source/prefix/record reads, PJ2 seeks the **same open handle** back to zero and verifies its SHA and byte count again (`PJ2:570–572`), additionally retaining the fstat comparison (`PJ2:573–576`). `pinned_inputs` returns only afterward (`PJ2:577`), and actual `loads`/projection/identity consumption occurs later (`PJ2:590–598`). Thus this is not merely fstat-only TOCTOU detection.
- These checks bind the selected source/record directly to the constant-pinned manifest, and the prefix to the constant-pinned whole archive. They are not a filesystem snapshot or a mathematical proof of any unopened source provenance bodies.

### 3. PJ2 strictness and outcomes

PJ2 explicitly decodes UTF-8 rather than handing bytes to JSON encoding auto-detection. Duplicate keys, floating-point literals, exponent-form floats, NaN and Infinity are rejected through the same parser path (`PJ2:72–89`). Canonical `Fraction` string equality rejects spellings such as `2/4`, `1/1` and `-0` (`PJ2:92–99`), matching V5's arithmetic policy (`V5:124–132`). Integer use-sites exclude bool; exported `source_index` is exact-int, not a numerically equal string or bool (`PJ2:301–302`).

The timeout/signal handler raises `Unknown`, not `Reject` (`PJ2:580–582`). The top-level consumer distinguishes UNKNOWN/exit 3 (`PJ2:617–619`) from REJECT/exit 2 (`PJ2:620–622`), maps unexpected Exceptions to UNKNOWN/3 (`PJ2:623–625`), and disables the alarm in a finally clause (`PJ2:626–627`). The success payload is returned only after controls, projection, and identity complete (`PJ2:590–600`). The authored control bodies are not observed PASS results.

This is closure of the old conflation during the protected computation, not an absolute all-signals guarantee. A further signal while an except handler or the final print is executing is outside that try's protection. No newly reachable success-with-skipped-check path was found.

### 4. V5 fail-closed surfaces: what remains open

**Residual MINOR B-R1 — retain truthful premise bookkeeping.** Item 5 remains exactly the written/code mismatch described above. The code fails closed on a hypothetical n11 gate; the changed schema/status text does not manufacture an alias or claim that the 219 n11 identities used one. This is not a new false accept.

**Residual MINOR B-R2 — signal/exclusive-output completion is not repaired.** `stop` raises `Unknown` (`V5:96–97`) and the handlers are installed before argument parsing (`V5:1237`). An interrupt during the main protected computation maps to UNKNOWN/3 (`V5:1318–1319`), but an interrupt during an except handler, before the try at `V5:1266`, or after its handlers at `V5:1322–1324` escapes that envelope. `output_exclusive` catches only OSError (`V5:1224–1233`), not Unknown. A signal or write/fsync error after successful `O_CREAT|O_EXCL` can therefore leave an empty or partial 0600 result file. On a same-path rerun, O_EXCL then fails; the function reports `OUTPUT_EXCLUSIVE_FAILED` and the caller returns 73 (`V5:1230–1232,1324`). It does not falsely treat an existing partial file as a prior PASS, but it does **not** meet the requested no-partial-file/result-completion guarantee. This is the unchanged f264 issue, expressly not claimed repaired in `DIFF:49`.

**Residual MINOR B-R3 — invalid resource caps still look like rejection at the exit-code layer.** `V5:1253–1255` prints `INVALID_RESOURCE_CAP` to stderr and returns 2 before constructing the result or calling the output writer. There is no JSON UNKNOWN result and no result file written by that branch. This remains distinct from a logical rejection only through stderr/absence of a newly written result, not through a different exit code. It is unchanged from `V4:1199–1201`.

Additional retained boundaries:

- Runtime deadline/cap exceptions inside the protected computation remain UNKNOWN/3, whereas definite `Reject` is REJECT/2 (`V5:92–97,1316–1321`). Default archive caps remain 1 certificate, 5000 rows, 5000 planes (`V5:1246–1249`), below 748/1,811,001/174,251 (`V5:787–788`); `V5:1142–1144` therefore makes an archive request UNKNOWN unless the caller explicitly raises caps. Sources are still verified first in main (`V5:1267`).
- Finite success statuses are assigned after their full verifier returns (`V5:1274–1276,1283–1284,1298–1315`), and a failed exclusive write overrides the return to 73. Exceptions raised **inside** the protected block map to REJECT or UNKNOWN; claiming this for all program phases would be inaccurate because of B-R2 and the initialization outside the try.
- R382 verifies the pinned record and then constructs its binding from the same record (`V5:1211–1217`); that is an identity diagnostic, not an independent packet-index/source projection. Its status is still exactly `R382_IDENTITY_CONDITIONAL` (`V5:1284`), and its global theorem/source-applicability boundary remains UNKNOWN (`V5:1261,1264`). This is truthful, not a repaired all-source binding claim.
- `member_jsonl` now accurately says its digest is checked after the final line (`V5:820,830–832`). Archive mode separately pre-hashes every packet-declared member before semantic consumption (`V5:1163–1169`) and re-hashes the archive before a successful return (`V5:1189–1190`). Early generator exceptions cannot reach an archive success status.
- Frozen written inputs/declaration are verified through the constant-pinned source manifest (`V5:155–177`); packet/member streams through the constant-pinned archive/packet manifest (`V5:1146–1169,810–832`); and R382 through both constant record and whole-archive hashes (`V5:1199–1220`). For arbitrary identity/planes/color/applicability inputs, the expected digests are **caller-supplied CLI pins** (`V5:1287–1299`), not predeclared constants. `checker_sha256` is an observed self-digest (`V5:1262`), not a constant comparison. Thus the blanket phrase “every consumed stream is checked against a constant” is accurate for the frozen scientific replay inputs, but not literally for every mode/self-metadata stream; this distinction is inherited and not a new trust-root claim.

## Diff fidelity and newly admitted success paths

Both native `/usr/bin/diff -U 0` comparisons were read completely: frozen V4→V5 and PJ1→PJ2. Both returned exit 1 because differences exist; this is not a checker execution or a failed test.

**Undocumented behavioral-change list: empty.** Every changed executable region is represented in `DIFF:58–120` and its substantive changes are described in `DIFF:16–50`. No new success status string, hidden new mode, archive/declaration digest change, or unlisted behavioral hunk was found.

| File | Changed regions checked against the author's list |
|---|---|
| V5 | Header and manifest/locator constants (`2,29–38`); shared visibility call sites (`500–501,557,593,746–747`) and helper/transport (`928–956,964–977`, including deletion of V4's plane-only early return at `931–934`); typed locator admission/dedupe (`603–623,631–632,899,996,998`); inner multiplier (`668–669`); stream-order docstring (`820`); delete-1 validator/call/roster integration (`857–863,885,1056,1089–1109,1184–1185`). |
| PJ2 | Header/root/caps/Unknown (`2–6,19,22–23,51–57`); JSON/rationals (`79–85,94–99`); descriptor registry and consuming branches (`135–136,157–161,174–180`); unsupported layouts (`261–262,277–278`); new authored controls (`400–401,460–461,471–486`); bounded helpers/prefix/input flow and re-hash (`494–577`); handler registration/type/ordinal/reporting/envelope (`581–582,587–588,594,606,614,617–629`). |

The sole textual-alignment qualification is harmless blank-line placement: DIFF's source-locator insertion row uses old `607–606` / new `603–623`; native diff aligns the same insertion as `-605,0 +602,21`, carrying the other adjacent blank line. All executable lines `V5:603–622` and the insertion before `verify_identity` are covered. This is an equivalent blank-boundary representation, not a missing changed region or behavioral discrepancy.

Newly admitted paths to an existing success result, absent or narrower in the predecessors:

1. **PJ2's two new descriptor families** can now pass the source→export image comparison and subsequent exact identity instead of PJ1's `descriptor.kind` rejection (`PJ2:157–180,291–336,597–600`). Whether the pinned R382 body actually exercises either added branch is not observed here.
2. **V5's `D1-color` noncover route** can now contribute to `VALID_ARCHIVE_FINITE_REPLAY_CONDITIONAL` after validating the transported coloring and finishing all remaining archive checks (`V5:1093–1103,1183–1194,1274–1276`). Missing categories instead have named UNKNOWNs. This is the documented completeness repair, not an unchecked bypass.
3. **V5 n9 rows with differing redundant inner provenance weights** no longer fail solely on that equality; the authoritative weighted identity must still cancel exactly (`V5:667–684`). This is the declared, documented relaxation of a false-reject guard.
4. **V5 full-visibility applicability with a complete singleton/orbit or intrinsic-plane declaration**, rather than necessarily a nonempty `visibility_required` list, can now succeed (`V5:746–754,927–956`). Row admission can likewise use the declared singleton's full validated scope-group orbit. All such premises are passed through the shared helper and enforced at transport; the previous omission/union discrepancy is not retained.

Typed locators, parser canonicalization, framing, and read caps otherwise narrow admission or refine UNKNOWN reporting; they do not create an additional unverified success path. No new path to a VALID status with an unmet B-scope guard was found.

## Coverage and pin receipt

The review manifest was checked **before its body was opened**: SHA-256 `f8f31c23f8840feaf99854a35431a5f6b6198b995390ab003df1aa61af15b005`, **13748 bytes / 196 LF**. All **24 declared inputs** below were then hash/byte/LF checked with `shasum -a 256` and `wc -c -l` **before any declared input body was opened**. Every value matched the manifest. Bodies were subsequently read completely in manifest order.

Window notation is exact: `P(n)` means consecutive raw windows `[1–15],[16–30],…,[15*floor((n−1)/15)+1–n]`; `C(n)` means `[1–60],[61–120],…,[60*floor((n−1)/60)+1–n]`. Each listed interval was displayed; there were no omitted middle ranges. The manifest itself used `P(196)`. Supplemental code rereads were within the same declared files and at most 60 lines.

| # | Declared input | Full observed SHA-256 | Bytes / LF | Complete raw windows |
|---:|---|---|---:|---|
| 1 | `E/01-frontier-20261028-full-source-lp-optimum-v1-erratum-1.md` | `c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9` | 2024 / 13 | P(13) |
| 2 | `E/02-frontier-20261028-mixed-plane-symmetry-erratum-v1.md` | `cdf6e55ffcfa8163007bf01b173a5a4f1103e6d9b7a70b40c0eacd288bdd2e04` | 980 / 5 | P(5) |
| 3 | `E/03-frontier-20261028-two-syndrome-local-neighborhood-erratum-v1.md` | `8ff79f6d07b935025e0b2f3de27928f030d251787724b64e05ccd9f1f012a37f` | 2873 / 9 | P(9) |
| 4 | `E/04-frontier-20261029-primal-checker-subset-coverage-erratum-v1.json` | `7194de8030505ac4ee5c13eccd4f6661988f2be50255d33623a5060ff24a2439` | 1461 / 20 | P(20) |
| 5 | `E/05-0005-prospective-review-entry.json` | `c9505f3094131c2be0071b3fee0477f77ce1993c5edfa9af9a62211b8fd4ac2b` | 8520 / 213 | P(213) |
| 6 | `E/06-frontier-20261028-conditioned-proper-subgraph-inequality-v1.md` | `c46831b9324e7e8c65009c2a27f3391db7705c370bfb63435a73b0117be3df49` | 4568 / 62 | P(62) |
| 7 | `E/07-frontier-20261028-fourfactor-plane-complete-theorem-v1.md` | `7148eb8fa7ef068743d927454c779290b0f3b4238940c7f4226b50bcb707cde5` | 4606 / 28 | P(28) |
| 8 | `E/08-frontier-20261028-fourfactor-plane-color-theorem-v1.md` | `09cb78a5bcd1d811f45d087dad567a49ce4f9f9ca898a0fcde3ef96efa0bb4ca` | 3660 / 25 | P(25) |
| 9 | `E/09-frontier-20261028-fourfactor-visibility-family-theorem-v1.md` | `ad7ee5d82f7a2ca20a21bc35f950bf1038fe660258dcbe41619bb67834cc410c` | 4044 / 20 | P(20) |
| 10 | `E/10-frontier-20261028-visibility-lattice-theorem-v1.md` | `4180f4e072d3e3e7108c66d90aeadebd169fee6b46dcf64e72b37ab10a357b50` | 5047 / 41 | P(41) |
| 11 | `E/11-frontier-20261028-mixed-visibility-theorem-v1.md` | `5c6f885b3c9ca20b6216304fe6449e8011e9c7de27eaf086becd887e3e0bdc74` | 3470 / 25 | P(25) |
| 12 | `E/12-frontier-20261029-single-functional-local-decoder-lemma-v1.md` | `77679e92b2927373e288cd5c91c647d43f606136273079bda649a89435984c61` | 3406 / 31 | P(31) |
| 13 | `E/13-frontier-20261028-triangle-code-global-obstruction-v1.md` | `bdf79fd631e8e58a734a4ef4c93f899e319f45712a219a876f527b52f1d61bb4` | 3658 / 42 | P(42) |
| 14 | `E/14-frontier-20261028-syndrome-cover-entropy-gate-v1.md` | `d6df004e025f067a14a6cc69e9aef8d9fc78a20a2fc49c4e431328120e32014b` | 3165 / 25 | P(25) |
| 15 | `E/15-frontier-20261029-all-affine-syndrome-plane-entropy-v1.md` | `9c6b11ca444122cf427a8e46f0a3cef0139f33b0615283322631c9c597c06cbd` | 13348 / 149 | P(149) |
| 16 | `DECL` | `c67ecd5bce3ef5cab01a0e9949f56a5f801d80e17209864b7b85ea51b16eea4d` | 27364 / 685 | P(685) |
| 17 | `V4` | `43e44f78a012573674d31b0d03696c282f7378f5e192c58c19099451bab86020` | 69961 / 1274 | C(1274) |
| 18 | `PJ1` | `20fe0113842da67c8209962d324d1a4bd74f0b68e1d86e054bcf7563aea87495` | 26249 / 520 | C(520) |
| 19 | `W/f264-guessing-checker-static-assurance/parent-outcome-v1.md` | `8e59b20cd2c54c4e0111d59b9df6cb26a1a92cf30961d6429f0acd897343a0ca` | 8267 / 34 | P(34) |
| 20 | `W/f264-guessing-checker-static-assurance/slice-A-return-v1.md` | `afed34bcf0504a7e35c8265da5c4ced3aabc8cb622b4717bf23cc0deb0c34ccb` | 6650 / 29 | P(29) |
| 21 | `W/f264-guessing-checker-static-assurance/slice-B-return-v1.md` | `5e7760b34c2bcae43a269aa98f28612477f741999cf39167517beca7ae09ec3a` | 7233 / 38 | P(38) |
| 22 | `DIFF` | `906ef36202e122e3d73c34780b520c074a6c3378853a8a6a0657ca12c875e06e` | 9473 / 126 | P(126) |
| 23 | `V5` | `8258ab4935e3f42ca74e9dc8e2287b6e31a7ddbcffdfb06fc085a62bdc6f7a06` | 72863 / 1328 | C(1328) |
| 24 | `PJ2` | `b60b85b65fd1b355132e6dbd7a14b0fe6ec9f8e71d76bd99a432b13b06ab72b4` | 31429 / 629 | C(629) |

In particular, frozen V4 and PJ1 still match **exactly** the two predecessor hashes required by the assignment. No predecessor mutation was observed, and this review did not modify them.

## Outside-code obligations and unobserved facts

The **written lift/tensorization, original-neighbor FD persistence in positive-probability fibres, and the k=1 delete-1 three-color entropy argument remain WRITTEN scientific obligations**. Finite graph coloring validation/transport is not adoption of the entropy reconstruction proof. The component meanings of the new local decoder also remain tied to the actual encoding, not abstract graph FDs alone.

No archive member, historical PASS/receipt body, undeclared scientific input, or source provenance body was opened. The f257/f258 manifests named in code were not opened; only their compiled-in hashes, paths, and consumers were reviewed. The archive's actual metadata layouts, literal proof IDs, row occurrence, coefficient identities, and complete category acceptance were not observed by running or inspecting archive bodies. Prior slice/outcome documents were read only because they are declared review inputs, not used as execution evidence.

**Final disposition:** changed code is statically consistent in B's scope; required projector closures are present; the three inherited residual MINOR issues are not closed. No new patch-introduced false-accept path is established. This return is not theorem acceptance, source-projection replay, a PASS receipt, or bulk-replay authority. Static-review confidence: **0.93**.
