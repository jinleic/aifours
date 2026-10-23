# PA19FinalBridgeDesk report: static bridge, code and acceptance audit of the PA(19,8,6) M1-complete candidate

Recorded 2026-10-18 02:45 PDT (host clock), from static reading only. This report is **not** a verdict and **not** parent acceptance. PA(19,8,6) remains undecided until the gate in §9 closes.

**Paths and pins**
- R = `institute/runs/six-lane-2026-10-16/review`; LANE = `information-science/evidence/six-lane-20261016/packing-array19`.
- Pinned candidate: LANE/`cycle2/m1-complete-candidate-20261018T012523.json`, sha256 `cf3e87c5fd8201286aa7a2b1e09999733cab7e5018a7e49c738f91ff13d1d791`, recomputed at 01:27.

**Provenance of the desk and the reviews**
- This desk and the Claude reviewer are both Claude-family (claude-opus-5-5), so the Claude review is a same-vendor second reading. Codex (gpt-6.1-sol) is the cross-vendor review.

## 0. Bottom line

**No FATAL finding.**
- No reachable path was found by which a counted UNSAT is unsound, or by which a valid 19×8 array escapes the cover.
- The mathematical bridges are:
  - valid PA19 → one of 10 profile multisets (total excess ≤ 3);
  - then either E0 (one of 486 quad graphs) or A2 (one of 5,577 skeletons);
  - then the matched CNF, a complete placement cover with batches, or the s00468 six-cell units;
  - then checked UNSAT.
- Both bridge reviews returned `DISPOSITION: ACCEPT-BRIDGES-WITH-RESIDUALS` with no FATAL finding:
  - Codex gpt-6.1-sol: rc 0, 694.8 s.
  - Claude claude-opus-5-5: rc 0, 2,127.8 s.
- The desk concurs, conditionally.

**The candidate is not the final gate.** Four evidence-chain residuals stay open:
- **CNF delivery into drat-trim (§3 F-A).** 238 M1 cases carry no positive evidence that drat-trim consumed the full CNF. drat-trim's early-EOF path is undefined behaviour that plausibly prints `s VERIFIED`.
- **Aggregation is not fail-closed (§3 F-B).**
- **Formula/list binding is producer-only or sampled for most split records (§3 F-C).**
- **M2 is incomplete, and no parent native replay has been done (§3 F-D, F-E).**

## 1. Inputs and pins

**Candidate and status**
- The candidate's `strict_snapshot` embeds STATUS15 sha `b0dac6b0…45f3`, which is its `snapshot_source_sha256`.
- `snapshot/lane/STATUS15.json` (sha `56062773…`, written 01:33:25) is a later regeneration. Its M1 fields are identical. It has one more M2 ms06 case (ms06_s00101), so 165 M2 cases are open.

**README**
- The snapshot copy has sha `320b2217…`, 848 lines, copied 01:41:37.
- The live file grew afterwards with a byte-identical prefix. `snapshot-supp3/lane/README.md` is 855 lines, sha `266872f1…`. It adds the structural-empty-cover amendment of 01:45:39.

**Snapshot contents**
- `snapshot/`: 328 byte-exact files. The manifest is `SNAPSHOT-MANIFEST.json` (sha `84555ac6…`) and `snapshot/SHA256SUMS` (sha `6de01c64…`). `shasum -c` returned rc 0.
- `snapshot-supp1/`: the b3 list, the ms09_s00003 and ms06_s00468 records, and R5 rows.
- `snapshot-supp2/`: the parent b3 microproof `R/pa19-ms09-b3-structural-parent-v1.md`, sha `f311d68d…6466`.
- `snapshot-supp3/`: post-pin README, `aggregate16.py` (`3994ac71…`), `summarize16.py` (`e9127efe…`), `freeze_ms09_batch_denominators_v2.py`, and the worker JSON `structural-ms09-b00003-proof.json` (`25b7df6a…`).
- `derived/`:
  - hash-only digests of 15 record trees and of the binaries;
  - summaries of the large parent receipts (R5, R8, R7).
- Total about 6.5 MB, under the 10 MB cap. No CNF or proof bytes were copied. Tree digests do not expose record contents.

**Binaries (sha256)**

| Binary | sha256 |
|---|---|
| drat-trim | `111b0405…` (equals the parent tool-hash receipt) |
| kissat | `05d6f3e9…` |
| cadical | `601c9fa8…` |
| geng | `ad2f68ad…` |
| genbg | `63822426…` |
| labelg | `0be70bdb…` |

**Proof map:** `PROOF-MAP-v4.md`, sha `82b2524c8beacf2b3167bae7d114bf3faf693f4e31fa52aa8b25fce68d492c51`. v1, v2 and v3 are superseded drafts. Two unused, never-launched prompt drafts were moved, unchanged, to `superseded-drafts/`; see `LOG.txt`.

## 2. Reviews (actual identities and receipts)

| Review | Prompt | Note | Receipt | Identity | Duration | Disposition |
|---|---|---|---|---|---|---|
| `R/pa19-final-bridge-codex-v1` | `8e7d46fa…` (8,225 B; file access to this directory, read-only sandbox) | `d6c1c0bb…5a87` | `25bb35aa…` | gpt-6.1-sol / openai / sandbox read-only / effort max | 694.8 s, rc 0 | ACCEPT-BRIDGES-WITH-RESIDUALS |
| `R/pa19-final-bridge-claude-v1` | `f31ffdf8…` (253,245 B, all load-bearing texts inlined and LF-numbered; built by `build_claude_prompt_v4.py`; 0 numbering mismatches on 4 spot-checked files) | `504b51d3…` | `68ae8610…` | init model claude-opus-5-5, firstParty; no tools | 2,127.8 s, rc 0 | ACCEPT-BRIDGES-WITH-RESIDUALS |

- Both reviewers read only their pins and ran nothing. Their notes remain `NOTE_RETURNED_UNVERIFIED` until the parent reads them.
- Claude listed what it could not check:
  - stream_check revisions 1-4 and 11-14;
  - rerun5;
  - encode_skel_b v1 `build`/`build_part`;
  - record contents;
  - most receipts.

## 3. Merged findings (desk adjudication)

Classification: **S** = mathematical or evidence soundness, **O** = operational or provenance.

**F-A: CNF delivery is unacknowledged, and drat-trim has an early-EOF hazard.** S (evidence chain), MAJOR, not FATAL.
- Sources: Claude MJ-1 (S, MAJOR) and Codex N2 (O, MINOR). The desk adopts S.

*What the code does*
- Streamed and staged pipelines write the CNF to drat-trim through a FIFO.
- `_writer` swallows OSError and records no completion (`stream_check5.py:42-47`, `stream_check15.py:376-381`).
- On an early CNF EOF, drat-trim breaks out of the parse loop and reads no proof (`drat-trim.c:1128-1149`).
- `S->formula` entries for the missing clauses stay uninitialised (malloc at :1085, filled only at :1218).
- `init()` then dereferences every entry and treats `clause[0]==0` as "formula contains empty clause", returning UNSAT (:725-729). `main` then prints `\rs VERIFIED` and returns 0 (:1481, :1500).

*Desk reading, beyond both reviews*
- `EXTRA`=4, `ID`=-1, `PIVOT`=-2, `MAXDEP`=-3 (:36-39). The first clause therefore occupies `DB[3]`, and `DB[0]` is its MAXDEP slot, which parse never writes.
- `DB` (4 MB) and `formula` (8 B × clauses) are large fresh mallocs, which macOS typically zero-fills [INFERENCE].
- So a truncated CNF stream would very plausibly yield a **false `s VERIFIED` with rc 0, regardless of the proof**. CNF-delivery integrity is load-bearing.

*Why it is not FATAL*
- A partial blocking write to a live FIFO reader requires a writer-side exception. The realistic one is EPIPE, which means the reader is already gone and cannot print a verdict. CPython retries EINTR.
- No instance is demonstrated.

*Mitigation by route.* Census: `delivery-exposure-census-v1.json`, sha `baf3cee6…`. Input: PA19FinalReceiptAudit's `M1-manifest-compact.tsv`. Read-only metadata.

| Class | What counts as evidence | M1 coverage |
|---|---|---|
| FILE | Route a and E0-M1 read the CNF from files | 2,490 cases plus E0 486 |
| LRAT | Rev 1-4 also required lrat-check to accept drat-trim's own LRAT; the early-EOF path writes no LRAT, and lrat-check prints VERIFIED only after an empty-clause step (`lrat-check.c:479-490`) | route b 2,709 cases, d 17,437 indices, e 359,460 indices |
| REPLAY | Rev 11-15 with proof > 64 KiB: feeder completion implies drat-trim read the proof, so it had parsed every declared clause. Assumes macOS pipe capacity ≤ 64 KiB | c5 49 cases, cell 6 units, e 878,712 indices |
| NONE | Rev 5 or rev 9 streamed checks carry no positive evidence | see below |

The NONE class covers **238 cases**:
- route b: 198 (ms08 170, ms09 28);
- c5: 37 ms06;
- d: 1 (ms01_s03171, index 1788, f01788_r3);
- e: 2 — ms06_s00150 with all 49,902 indices at rev 9, and ms09_s00010 with 100 indices from a rev-5 `_r3` batch.

*Independent M2 coverage of those 238 cases.* Source: `delivery-exposure-m2-overlap-v1.json`, live at 02:43.
- 191 have M2 coverage with REPLAY evidence (189 direct, 2 split).
- 1 is the structural b3 row (ms09_s00003).
- 46 are M2-open: 20 ms06 (including ms06_s00150 ↔ b162) and 26 ms09.

*Remedy*
- Either finish M2 on staged revisions, or replay those 46 (or all 238) from on-disk CNF files with a parent drat-trim.
- Patch the harness to retain drat-trim's `c parsing input formula with V variables and C clauses` line, `read N bytes from proof file`, and the absence of `early EOF`.

**F-B: The aggregator is not a fail-closed acceptance checker.** MAJOR.
- Sources: Codex M1 (S) and M2 (S); Claude MJ-2 (O), mn-1, mn-8.

*What aggregate15/summarize15 (and the post-pin aggregate16/summarize16) do not do*
- Validate a record's tag, multiset or b_index against its path, or its filename against its indices.
- Validate placement-list, encoder or CNF identity.
- Reject unknown revisions: they fall through to the legacy predicate `drat_trim_verified and checked`.
- Drop the `multiset` + 2-entry range heuristic.
- Count E0 per index: they count files, with 486 hard-coded.
- Veto coverage on a SAT claim: SAT records are only listed.
- Reject an M1 split with n = 0: it is accepted vacuously in both aggregate15 and aggregate16. aggregate16 fails closed for M2 empty lists only.

*Mitigation for M1 at this time*
- PA19FinalReceiptAudit did an independent all-case metadata pass: `R/pa19-final-receipts-v1/RESULT.json` sha `797e4cd6…94b7` and `REPORT.md` sha `8aaa0bd6…fc09`, disposition `ALL-M1-RECEIPTS-QUALIFY (metadata only)`.
- It found:
  - 5,577/5,577 A2 cases and 486/486 E0 graphs covered;
  - no holes, no SAT, no drift, no empty M1 list (`A2_EMPTY_COVER_NOT_ACCEPTED` 0);
  - 94/94 parser controls passing.
- Its census of counted records:

| Route | Records by revision and solver |
|---|---|
| a | cycle1 2,490 |
| b | rev4 2,709, rev5 198 |
| c5 | rev5 37, rev12 48, rev13 1 |
| d | rev4 17,437 kissat + rev5 1 cadical |
| e | rev4 8,183, rev9 500, rev12 6,830, rev14 587, rev15 1,376, + cadical rev5/12/15 one each |
| cell | rev13 5, rev14 1 |
| E0 | 486 |

*Claude mn-1 is resolved by the desk.*
- At the pin, the b3 list did not exist: its `ext.json` mtime is 01:38:58, and the pin is 01:25:23.
- The pinned M2 ms09 "partbatch-drat: 1" is ms09_b00002. It has two certified rev-14 batches, 0-99 and 100-143, written 23:58.
- aggregate15 would count b3 vacuously after 01:38:58; aggregate16 does not.

**F-C: Formula and list binding is producer-only or sampled.** MAJOR.
- Sources: Codex M3 (S) and Claude MJ-3 (O).
- R5 binds all 5,577 M1 base CNFs: a 2,490, b 2,907, c5 86.
- Split records: 34,379 of the 34,917 counted split records are formula worker-only. 538 are parent-bound by R8. A well-formed but wrong `cnf_sha256` outside R8 cannot be detected from metadata.
- Placement lists:
  - 31 ms01 and 43 ms09 M1 lists are parent-regenerated (R6).
  - ms06_s00150 is semantically replayed (`pa19-ms06-placement-binding-v2`).
  - The other **18 ms06 lists are worker-only**. 15 match the worker's own extend receipts. s00204, s00212 and s00214 were generated inline by run_hard12 and have no receipt.
- E0 CNFs (encode_q0 and encode_q0b) have never been rebuilt from graph6 by a parent. The M2 direct `build_v2` CNFs and post-R6 M2 lists are producer-only.

**F-D: One checker and harness, and no native replay.** O, MAJOR for acceptance.
- Sources: Claude MJ-4 and Codex B10/B11.
- M1 and M2 share one drat-trim binary (no build record) and the staged harness.
- No parent native proof replay exists for any route.
- Path-a DRAT files are retained. Staged proofs are not.

**F-E: M2 is incomplete.** O, a contract blocker.
- 166 cases were open at the pin and 165 at 01:33.
- M2 routes are still changing. InfoPacking19 IRC ~02:2x reports ms06 b68/b73 direct UNKNOWN → extend_b/build_partbatch, plus two Kissat-on-B calibration batches outside the coverage trees.

**Minor findings.** None is load-bearing for soundness.
1. Historical substring verdicts: route a, E0-M1 and rev 1-2 have no rc or self-exit gate; rev 3-5 gate on rc and use a substring.
   - drat-trim prints `s VERIFIED` only after verification, or for a parse-time empty clause (rc 1), which is a genuinely UNSAT formula. M1 encoders never emit an empty clause.
   - Rev 4 and rev 5 records lack exact s-lines. Exact s-lines exist only for rev ≥ 9.
2. Codex N4: two smoke-control summary flags are wrong (the rev-3 D2 timeout expectation, and the rev-5/9 `ABC_expected` that omits D). Inspect individual outcomes instead.
3. Codex N3: historical process deviations. These are the cycle-1 SIGKILLs (all recorded UNKNOWN), early CPU accounting, `/tmp` files, smoke-output rewrites, and a checkpoint gap. None makes a certificate false.
4. Claude mn-3: the s00468 cell runner changed from rev 13 (`run_s00468_cell.py`) to rev 14 (`run_s00468_cell14.py`, an import-only margin variant documented at README:791-797). s00-s04 are rev 13 and s05 is rev 14. This is benign, because summarize15 reconstructs every subcase CNF. PA19FinalReceiptAudit independently recomputed the six subcase SHAs from the base bytes plus one unit and confirmed the ALO clause is present.
5. Claude mn-6: R8's census lists 16 `_exact` records. Only `ms01_s02573/f00012_exact` is load-bearing (PA19FinalReceiptAudit).
6. Claude mn-5 (cover Minor-7, contested): the help excerpt does not state which class each `#:#` value applies to. The reading (first:second class) is corroborated by the R3 geng/genbg bijection. Cite the nauty manual.
7. Claude mn-7, code nits that cannot be reached in production:
   - build_v2 treats n = 0 as n = 1;
   - build_partbatch drops n = 1 (guarded by a P1 assert);
   - `extend_b.compatible` is dead code.
8. SAT listing is not a universal census across all trees (Claude mn-4, Codex).

## 4. Bridge verdicts (desk, merging both reviews)

- **B1 (profiles and multisets): PASS** (both reviews).
  - 235 partitions, 6 profiles, 10 multisets, including every non-balanced one.
  - L = 3 − excess. Every profile has 6 nonzero parts.
- **B2 (E0): PASS-WITH-RESIDUAL** (both).
  - The quad-graph lemma and the 486-graph list (geng plus atlas bijection R2) hold.
  - encode_q0 and encode_q0b impose necessary constraints only, and their symmetry breaking is simultaneously valid.
  - Residual: no E0 CNF rebuild; E0 is counted by file.
- **B3 (A2 skeletons): PASS-WITH-RESIDUAL** (Codex PASS, Claude PASS-WITH-RESIDUAL).
  - Every pruning is a necessary condition: tmax, hmax as a union bound, exact matching filters, linearity via -Z1, degree 4, at most 19 rows, h ≤ 2c0.
  - Dedup merges only coloured-incidence isomorphisms.
  - Residual: trust in nauty and networkx; the shared formulas.
- **B4 (encoders): PASS.**
  - Completeness holds by setting auxiliaries to their exact unary or prefix meaning.
  - All lex-leader breaking uses one row-major order within the fixed-structure stabiliser.
  - M2 v1 P0 fixing is a per-column relabel, composed with special-cell-only lex constraints.
  - Degenerate branches cannot be reached: 0 ≤ target < 18 ≤ len(o); weighted cap ≥ 6 + L; every n ≥ 1; Σl = 38 − 4c0 − 6ns = 2L.
- **B5 (splits): PASS-WITH-RESIDUAL.**
  - History-class prefixes; extend_b count vectors with brute-force Aut(S) × A/B swap; batch selector semantics.
  - `_exact` is a sound strengthening. rerun_batch12/15 enforce equality with the original CNF. rerun5 builds from spec + ext directly and has no check against the original record.
  - Residual: F-C.
- **B6 (s00468 cell cover): PASS.**
  - x[8][6][s] = 1 + 48·8 + 6·6 + s = 421 + s. The six positive units exhaust the ALO clause.
  - summarize15 reconstructs the subcase bytes. The base is bound by R5. PA19FinalReceiptAudit recomputed the subcase SHAs.
- **B7 (acceptance): PASS-WITH-RESIDUAL.**
  - Revision predicates are as stated in PROOF-MAP-v4 §7.
  - Residuals: F-A, F-B, minor item 1.
- **B8 (ms09 b3): PASS as a STRUCTURAL row only.**
  - Parent microproof `f311d68d`: 5·21 + 3·22 = 171 = C(19,2), so the array is saturated and t + Σe = 2.
  - The universal row h must sit in all three P1 pairs. Nonempty rows already meet h, and empty rows cannot be in a pair. So h has no partner.
  - extend_b reproduces raw = 0: h is forced into P, and `ok_row(0,−1)` fails for the empty class.
  - It is never DRAT and never a generic 0/0. It counts on the M2 side only. The M1 mate ms09_s00003 is DRAT-checked via route b at rev 5.
- **B9 (controls): PASS, not load-bearing.**
  - Controls are diagnostic and mostly post hoc. Post hoc controls stay post hoc. See the Codex table at note:79-92.
- **B10 (old gaps): PASS-WITH-RESIDUAL.** See §6.
- **B11 (trust base): PASS-WITH-RESIDUAL.** See §7 and §8.
- **B12:** see §9.

## 5. Structural versus proof-checked counts

**M1 at the pin: 5,577 A2 + 486 E0 = 6,063 cases. All are proof-checked by drat-trim-verified UNSAT records; 0 are structural.**

| Route | Cases |
|---|---|
| a | 2,490 |
| b | 2,907 |
| c5 | 86 |
| d | 31 |
| e | 62 |
| cell | 1 |
| E0 | 486 |

- Routes d and e (93 cases) and the cell route (1) additionally rest on structural reductions that are not proof-checked:
  - completeness of the placement enumerators;
  - the selector, unit or cover semantics.

**M2**
- At the pin: 486 E0 + 5,411 A2 proof-checked.
- Post-pin structural: ms09_b00003 (↔ ms09_s00003), parent-checked hand proof plus a complete empty list. It must be reported as its own row.
- Open at the pin: 166.

## 6. Old scout gap dispositions (final)

### Cover scout (`R/pa19-cover-scout-audit-v1.md`)

| Gap | Disposition | Reason |
|---|---|---|
| Major-1, unfinished cases | M1 CLOSED (producer candidate); M2 OPEN | 166 at pin, 165 at 01:33 |
| Major-2, pass-1 CNF binding | RESOLVED | R5, all 5,577 |
| Major-2, split binding | PARTIAL | R8 538 parent-bound of 34,917 counted |
| Major-2, manifests | PARTIAL | cycle-2 manifest at 12:18 plus PA19FinalReceiptAudit hashes |
| Major-2, open-list cut | RESOLVED | — |
| Major-2, E0 hard-coded 486 | STILL OPEN | files counted, not indices |
| Minor-3, shared formulas / nauty / networkx | ACCEPTED as trust base | formulas re-derived by three readers |
| Minor-4, stale README | RESOLVED | [STALE] notes at :47, :83, :137, :262 |
| Minor-5, range heuristic | STILL PRESENT | aggregate15:92-93 and aggregate16; benign today |
| Minor-6, controls | STILL TRUE | PA18 uses an empty skeleton; gen_skel_b is fixed to (19,8,6) |
| Minor-7, genbg flags | PARTIAL | flags logged, but the `#:#` class order is not stated in the excerpt; corroborated by R3 |
| ms01_s02573 f00012 | RESOLVED | f00012_exact (encode_full2) checked; the only load-bearing `_exact` |

### Encoder scout (`R/pa19-encoder-scout-audit-v1.md`)

| Gap | Disposition | Reason |
|---|---|---|
| F1, lrat-check | RESOLVED for acceptance | No counted record depends on lrat-check. m2q0b and the `_r2`/CaDiCaL-LRAT records are listed as uncertified. E0-M2 is recertified by m2q0c rev 5. |
| Missing control receipts | PARTIAL | control13-v5 covers the direct/batched functions; no native receipt for the build_v2g identity |
| Uncontrolled production encoders | PARTIAL/OPEN | full/full2 are generalised to q=6 identically; E0 encoders have no positive control |
| Weak binding | PARTIAL | F-C |
| One checker | OPEN | F-D |
| 64 KiB stalls | RESOLVED | kept UNKNOWN, then recertified |
| Deterministic FIFO names | RESOLVED for rev ≥ 5 | rev 1-4 also carry the lrat conjunct (F-A) |
| SAT listing | MOSTLY RESOLVED | no universal census and no veto |
| Range heuristic | STILL PRESENT | both reviewers contest any "resolved" grouping |
| Weak or no-op controls | CONFIRMED, non-load-bearing | count-changing PA18 mutations; the `non_digit_token` wrong-reason rejection; vacuous (7,2,2) |
| Code nits | NON-LOAD-BEARING | — |

## 7. Representations bound only by the producer or a parent sample (not all-case)

**Producer-only**
- E0 M1 and M2 CNF bytes. Graph identities are R2-bound.
- 18 ms06 M1 placement lists. Three of them (s00204, s00212, s00214) have no worker extend receipt.
- All M2 lists produced after R6, and all M2 `build_v2` direct CNFs.
- `binding_pass1` in the candidate is a worker sample (step 50, 940 split results), not a parent check.
- drat-trim binary ↔ source `d834b649`: there is no build record. The binary hash equals the parent tool-hash receipt.

**Parent sample only**
- Split-record CNF identity: 34,379 of 34,917 counted split records rest on the producer alone. R8 covers a frozen 374-record sample plus inc-001 (253 ms06_s00150 batches).

**Metadata only, no formula identity**
- R7 (14:39) and PA19FinalReceiptAudit (02:18) bind record metadata.

**Parent all-case bindings that do exist**

| Receipt | Binds |
|---|---|
| R1 | profiles |
| R2 | 486 graph identities |
| R3 | both skeleton lists and the 9 maps |
| R4 | 5,577 specs |
| R5 | 5,577 base CNFs |
| R6 | 74 hard lists at 13:58, plus M2 counts |
| ms06-v2 | ms06_s00150 list |
| PA19FinalReceiptAudit | all M1 records (metadata) and the six cell subcase SHAs |

## 8. Trust base (exact)

1. The mathematics of PROOF-MAP-v4 §§1-6 and §8, re-derived independently by both reviewers and the desk.
2. nauty geng/genbg: complete enumeration with the documented options and class semantics.
3. networkx 3.7: graph6 parsing, `is_isomorphic` soundness, and atlas completeness. WL hashing only buckets candidates, so a collision cannot merge classes.
4. CPython (3.14.3), json, hashlib, zstd, and the OS and POSIX FIFO/pipe semantics. This includes:
   - a blocking FIFO write to a live reader is never left partial without an exception;
   - pipe capacity ≤ 64 KiB, which the REPLAY evidence relies on.
5. The drat-trim binary `111b0405…` from upstream 2e3b2dc0. It must correctly decide whether the formula it actually parsed is UNSAT. It is the single checker for M1 and M2.
6. The stream_check revisions 1-5, 9 and 11-15, check_proofs and run_proofpass.
7. aggregate15/summarize15, cross-checked by PA19FinalReceiptAudit.
8. Record integrity: genuine, correctly labelled producer executions. Each recorded `cnf_sha256` must be the intended formula of its case and indices, with no forgery.
9. M2 only: the parent-checked structural b3 argument.

Solvers (kissat 4.0.4, CaDiCaL 3.0.1) are not trusted; they only produce proofs. The PA18 lower bound additionally needs the CPro1 witness bytes, `data/cpro1-pa-18-8-6.txt`, to be verified by the parent; no parent receipt for this was found.

## 9. Residuals before any final "optimum 18" claim (ordered)

1. **Independent M2 completion** under the frozen strict predicate.
   - 165-166 cases open, including ms06 b68/b73 now routed to the split, and the ms09 one-column lists.
   - Count b3 only as the separately pinned structural row (`f311d68d`). Any other empty list needs its own parent proof.
   - Keep direct, split and structural counts distinct.
2. **Close F-A.** Show positive CNF-delivery evidence for every case, by at least one of:
   - M2 coverage on staged revisions with proof > 64 KiB (191 of the 238 exposed M1 cases already have it; 46 are M2-open);
   - a parent native replay from on-disk CNF files for the remaining cases, starting with ms06_s00150 (rev 9, 49,902 indices; M2 b162 open) and the other M2-open exposed cases;
   - a harness patch recording drat-trim's parsed clause count, proof bytes read, and any `early EOF` warning.
3. **A parent fail-closed final aggregator and ledger** on a frozen snapshot. It must:
   - reject n = 0 on both M1 and M2, except accepted structural rows;
   - reject unknown revisions;
   - verify or drop the range heuristic;
   - check filename/index/identity fields;
   - verify E0 per index (g000-g485 ↔ graph6);
   - veto on any SAT;
   - report structural and proof-checked counts separately.
4. **All-case formula binding.**
   - Rebuild split CNFs in memory from (spec, ext.json, indices) for every counted record (no solver).
   - Do a parent replay of the 18 ms06 lists (extend_p1q) and of the post-R6 M2 lists (extend_b).
   - Rebuild E0 CNFs from graph6 for both methods, and the M2 `build_v2` CNFs.
5. **Parent native proof replay sample** across routes a (stored DRAT), b, c5, d, e, cell and M2, with an independently built drat-trim or a second checker.
6. **PA18 witness**: parent verification of the exact witness bytes before combining the lower bound 18 with nonexistence at 19. The contract's PA18 positive control is met only in empty-skeleton form; the cover's positive controls are the (13,5,4) runs.
7. **Documentation**:
   - the s00468 runner revision change;
   - the 16 `_exact` records, of which only f00012 is load-bearing;
   - the genbg `#:#` semantics;
   - the M1 vacuous-n = 0 rule.

## 10. What this desk did not do

- No solver, checker, generator, encoder, verifier or CNF construction was run.
- No proof was read or replayed, and no CNF or proof was copied. This desk does not establish that the snapshot contains any unread large proof.
- No lane file was modified.
- The two census scripts only read small JSON records and PA19FinalReceiptAudit's manifest.
- No parent acceptance is implied.
