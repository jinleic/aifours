# moqls7 Gram delta and complete-K2 audit: final desk report (M7GramDeltaDesk)

Written 2026-10-18T00:35:17.052517-07:00 (host clock). This report gives a delegated disposition of the delta and of the evidence only. **No theorem verdict.** It establishes nothing about K3 or M(7).

## Disposition: DELTA-ACCEPT-WITH-FIXES
- **Repaired G1–G5 proof** (`GRAM-ENCODING.r2.md` c6c506a7…d6c7, `LEMMAS.md` 4bddc9d4…0c9) and **actual K2 production** (frozen encoders b2c206d8…8833 and c7583efe…2b45; driver `gram_certify_r4.py` ec540a87…a18a; 294 receipts):
  - No FATAL finding, and no gap affecting soundness. The desk and both static reviewers reached this independently.
- **Complete K2 bridge.** It holds: an arbitrary complex K2 triple leads to the 3-net of one of the 147 representatives, which carries two edge-disjoint Gram supports satisfying G1–G5 with G4 heavy on all 21 own lines, which give a model of both CNFs.
  - G4 uses the Lemma 10 replacement in an arbitrary ONB, preserving all partners, together with the accepted K1.
  - The bridge is conditional on accepted K1 r3, LS147 coverage, and valid proofs of the 294 exact CNFs.
  - Desk §5; Codex T3; Claude T3.
- **Proof condition.** The parent replay reports 294/294 PASS, each with a matching CNF hash (`moqls7-k2-parent-v1/RESULT.r2.json` 5362d6d2…8766).
  - The desk static re-check binds all 294 replay receipts to class-file keys, to the producer r4 CNF hashes, and to native logs that re-hash correctly.
  - Evidentiary limit: §4.
- **Previous MAJORs.** Not all are fully resolved; the desk and both reviewers agree.
  - The residuals are r4 startup liveness, the pre-production timing of the component controls, and solver/checker-binary provenance in the producer receipts.
  - None is a soundness objection once the replay succeeds.
  - Both MAJORs about class coverage are resolved.
- **Production-domain argument** (GRAM r2 §6): **confirmed by the desk and both reviewers.**
  - Encoder B's malformed one-candidate branch, every empty-clause or `None`-literal branch, and the permissive fix API cannot be reached by any production call.
  - Valid 3-nets give ≥3 common candidates and valid 2-nets ≥5. Transition and heavy sets have 5 or 6 candidates. `sym` occurs only with L absent, and `fix` is never passed.
  - No production counterexample exists.
  - General-API hazard, for context only: `--sym` with any reduced L would emit a `None` literal, because cells (1,0) and (0,1) share symbol 1.

## Reviewer dispositions
| Review | Disposition | FATAL | MAJOR | MINOR | Run | Identity |
|---|---|---|---|---|---|---|
| [Codex](../moqls7-gram-delta-codex-v1.note.md) | ACCEPT-WITH-FIXES | 0 | 2 | 2 | 23:52:53→00:01:19, 506 s | gpt-6.1-sol, openai, max (stderr header) |
| [Claude](../moqls7-gram-delta-claude-v1.note.md) | ACCEPT-WITH-FIXES | 0 | 1 | 8 | 23:54:00→00:31:51, 2271 s | claude-opus-5-5 (init model and modelUsage) |

- **Codex MAJORs.**
  - D-MAJOR-1: r4 blocks in `open(fifo)` before its watchdog starts (`gram_certify_r4.py:141`). This is a liveness defect; no certificate is affected.
  - D-MAJOR-2: the added controls ran after K2 production, which deviates from the protocol at `README.md:91`.
- **Codex MINORs.**
  - D-MINOR-1: `K2-THEOREM.r2.md:130` misdates the review requests.
  - D-MINOR-2: the r4 status parser calls `strip()` rather than stripping CR only. The parser contract should say so.
- **Claude MAJOR-1.** The same misdating at `K2-THEOREM.r2.md:130`. Claude rates it MAJOR as a matter of honesty; soundness impact is none.
- **Claude MINORs.**
  1. `GRAM-ENCODING.r2.md:134` still points to K2 r1.
  2. The transport controls' scope is unstated: they exercised `proof_stream.py`, not r4.
  3. `K2-THEOREM.r2.md:141` calls r2/r3 "pre-production". They were failed first-batch production attempts.
  4. The transport wording at `K2-THEOREM.r2.md:12-14` is incomplete.
  5. `REVIEW-CORRECTIONS.r2.json:9` says the alias "resolves" the frozen references. Those references denoted r1, and the alias is a post-production copy of r2.
  6. The scratch path is shared and not exclusive. Claude asked for a check that receipt intervals are disjoint. **Closed by evidence:** the desk found 0 overlapping A/B receipt intervals (order A0, B0, A1–146, B1–146, with B1's FIFO created 55 s after the A146 receipt), the parent's `bind-v1.json` reports `overlapping_neighbours=[]`, and the replay regenerated every CNF.
  7. `GRAM-ENCODING.r2.md:98` cites exploration files.
  8. "K1 section 8" carries no version. Cosmetic.
- **Citation spot checks.** The desk re-read 25 Codex citations and 43 Claude citations (27 digest line ids, 16 file:LF). All exist and support the claims.
- **Records:** `desk/delegate-review-codex-v1.json` and `desk/delegate-review-claude-v1.json`.
- **Note on an LRAT recheck.** Claude suggests one as optional. Caution from workspace memory, not re-verified here: the upstream drat-trim `lrat-check` printed VERIFIED for an empty clause on a SAT CNF. Any LRAT route needs a sound checker and negative controls.

## Old findings: desk, Codex and Claude status
| Old finding | Desk (`desk/finding-map-v2.md`) | Codex | Claude |
|---|---|---|---|
| Codex MAJOR-1 | RESOLVED | RESOLVED | RESOLVED |
| Codex MAJOR-2 | PARTIAL | RESOLVED | RESOLVED |
| Codex MAJOR-3 | RESOLVED (liveness residual) | PARTIAL | PARTIAL |
| Codex MAJOR-4 | POST-HOC | PARTIAL | PARTIAL |
| Codex MINOR-1 | BY-DOMAIN | RESOLVED-BY-DOMAIN | RESOLVED-BY-DOMAIN |
| Codex MINOR-2 | RESOLVED | RESOLVED | RESOLVED |
| Codex MINOR-3 | RESOLVED | RESOLVED-BY-DOMAIN | RESOLVED-BY-DOMAIN |
| Codex MINOR-4 | BY-DOMAIN | RESOLVED-BY-DOMAIN | RESOLVED-BY-DOMAIN |
| Codex MINOR-5 | RESOLVED | RESOLVED | PARTIAL |
| Codex MINOR-6 | RESOLVED (desk erratum) | RESOLVED | UNRESOLVED |
| Claude MAJOR-1 | RESOLVED | RESOLVED | RESOLVED |
| Claude MAJOR-2 | PARTIAL | PARTIAL | PARTIAL |
| Claude MAJOR-3 | POST-HOC; (v) PARTIAL | PARTIAL | RESOLVED |
| Claude MINOR-1 | BY-DOMAIN | RESOLVED-BY-DOMAIN | RESOLVED-BY-DOMAIN |
| Claude MINOR-2 | RESOLVED | RESOLVED-BY-DOMAIN | RESOLVED-BY-DOMAIN |
| Claude MINOR-3 | BY-DOMAIN | RESOLVED-BY-DOMAIN | RESOLVED-BY-DOMAIN |
| Claude MINOR-4 | BY-DOMAIN | RESOLVED-BY-DOMAIN | RESOLVED-BY-DOMAIN |
| Claude MINOR-5 | RESOLVED | PARTIAL | RESOLVED |
| Claude MINOR-6 | RESOLVED | RESOLVED | PARTIAL |
| Claude MINOR-7 | RESOLVED (cosmetic residual) | RESOLVED | RESOLVED |
| Claude MINOR-8 | RESOLVED | RESOLVED | RESOLVED |

Notes on the disagreements:
- **Codex MAJOR-2.** Desk PARTIAL; both reviewers RESOLVED. The frozen-control rerun outputs are byte-identical to the exploratory outputs and carry no run-time CNF or log binding.
- **Codex MAJOR-3 and MAJOR-4.** The desk records the same residuals as the reviewers but uses different labels.
- **Claude MINOR-5.** Codex PARTIAL because `strip()` is still used.
- **Codex MINOR-5.** Claude PARTIAL only because K1 r3 and README were not inlined in its packet. The desk verified `K1-THEOREM.r3.md:82` (full `…e113`) and `README.md:7` (`…a3ff2`).
- **Codex MINOR-6.** Claude UNRESOLVED because the parent-owned manifest is unchanged. The desk erratum (`desk/lf-erratum.md`) closes it without rewriting the manifest.

## Consolidated text fixes before integration
No frozen bytes are to be changed; each fix goes into a new overlay.
1. Correct the chronology at `K2-THEOREM.r2.md:130`. The Codex request predated production by 898 s; the Claude request came after it; the 26 controls ran at 21:24:52–21:25:09, after all 294 certificates. Not preregistration.
2. State explicitly that the `README.md:91` pre-production control rule was not met for the added controls, including encoder A's K2-shape positive.
3. Integrate `K2-THEOREM.r2.md` (a73a9007…32cd) as the theorem text instead of r1. r1:16 cites K1 r2, r1:27 cites Gram r1, r1:63 and r1:67 assert unbound solver versions, and r1:99-100 cite unreceipted controls.
   - Repoint `GRAM-ENCODING.r2.md:134` and `LEMMAS.md:77`.
   - The replay's proof objects are identical for r1 and r2.
4. Scope the transport controls (they test the new K3 transport), and say "failed first-batch attempts" for r2/r3.
5. Complete the transport wording at `K2-THEOREM.r2.md:12-14` and the alias wording at `REVIEW-CORRECTIONS.r2.json:9`.
6. Smaller fixes:
   - cite the decoder `k2_classes.py` b49099e4…b891;
   - cite where L is shown Latin (LS147, replay decoder);
   - cite `LEMMAS.md:54-67` for the all-partner form of Lemma 10;
   - document r4's status normalisation;
   - point the control table to the frozen files;
   - give K1 §8 a version.

Residuals that do not block, carried as stated caveats:
- r4 startup liveness. No K2 instance was affected.
- r4 receipts do not bind solver binaries. Solvers are not a soundness premise.
- The producer's drat-trim binary is not linked to its source build. The replay uses the parent-built checker.
- The frozen-control rerun lacks run-time binding.
- The parent replay's v1 wrapper scripts were not hashed (§4).

## 4. Parent K2 replay: evidentiary limit (per parent notice, ~00:00 PDT)
- **Replay.** `RESULT.r2.json` (5362d6d276927ecb0ced699ea3152157ad145494ea3958dbf99c3c886a898766) reports 294/294 PASS, 294 CNF-hash matches, 0 FAIL and 0 UNKNOWN.
  - Checker: the parent-built drat-trim (a46c0c71…).
  - Solvers: pinned by absolute path and binary hash (cadical 601c9fa8…, kissat 05d6f3e9…).
  - 14 controls. The 10 with stated expectations matched them. The 4 observational ones showed: dropping one G5 clause still gives UNSAT, and the original proof against the mutated CNF gives NOT VERIFIED, so a proof binds its exact CNF.
- **Desk static re-check** (no rerun): `desk/replay_static_check.py` (fd976306…067e) wrote `desk/replay-static-check.json` (e0873b9f…c445). All 294 final receipts pass 13 checks:
  - the key equals class-file line i;
  - the regenerated CNF hash equals the receipt field and the producer r4 receipt's CNF hash;
  - the checker and solver logs re-hash to the bound values;
  - each checker log has exactly `s VERIFIED`, and its parsed formula dimensions equal the CNF header;
  - each solver log says `s UNSATISFIABLE`;
  - the checker is the parent drat-trim, and the solver paths are pinned.
  - Runs: v1 182 final, v2 111, v3 1.
- **Limit.** `provenance-v1.json` (016efb81…eb68) states that the v1 wrapper scripts were not hashed at run time.
  - Hash-observed replays cover B only, for 112 classes (34, 36–146).
  - **35 classes (0–33, 35) have no hash-observed parent replay for either encoder.**
  - For those classes the evidence is: receipt content; native logs bound by hash, with exact status and matching parse dimensions; regenerated CNFs equal to the producer's independently pinned r4 CNFs; and two encoders, each verified by producer and parent with two checker builds and two solvers.
  - Wrapper misreporting is excluded by the re-hashed logs.
  - Feeding a different formula with identical dimensions is excluded only by the edit-log account of the unchanged `pipeline()`, not cryptographically.
- **Assessment.**
  - Adequate for computer-assisted acceptance if the caveat is stated verbatim.
  - If observed wrapper identity were ever required per class, the minimal gap is 35 classes × 1 encoder.
  - No rerun is proposed and nothing is backfilled.
  - The producer r4 command names do not establish solver binary identity. This does not affect soundness, because proofs are checked against exact CNF bytes.

## 5. Chronology (honest reading)
Sources: `pin/desk-digests/chronology.json` and the receipts.

| PDT | Event |
|---|---|
| 19:05:49–19:06:18 | Frozen-control rerun |
| 19:16:11 | Old Codex note |
| 19:31:09–20:12:37 | All 294 K2 certificates; no overlapping receipt intervals |
| 20:24:51 | Old Claude v2 note |
| 21:24:52–21:25:09 | 26 matched component controls, after K2 by 4335 s |
| 21:38:40–21:38:43 | Transport controls r2, on the new `proof_stream.py`; prospective for K3; 37 s before the K3 driver delta froze |

Neither control set is retroactive preregistration. GRAM r2:124 and REVIEW-CORRECTIONS:21 state this correctly; K2 r2:130 does not (fix 1).

## 6. LF erratum (parent-owned manifest not rewritten)
- **Table.** `desk/lf-erratum.md` and `desk/lf-erratum.json`.
- **Scope.** 14 of the 18 entries in `moqls7-gram-review-inputs-v2/manifest.json` are LF-terminated and record `lines_split_LF = lf_count`, one below `len(text.split('\n'))`. The corrected value is `lf_count + 1`. The 4 entries without a final LF are correct.
- **Citation check.** All 223 citations in the two old notes point to nonempty lines in 1..lf_count. 5 bare references were resolved by hand to `code/gram_certify.py`. None targets the extra empty element. No cited line moves.
- **Other manifests.** The superseded, unused inputs-v1 manifest has the same 14 rows. The K1 review manifest has none.

## 7. Files (all exclusive-create, under the prefix `moqls7-gram-delta-`)
- **Pin.** `moqls7-gram-delta-v1/pin/` (`MANIFEST.json` b53df015…10cc; 1013 files, 1.54 MB; no FIFO opened, no CNF copied).
  - Desk digests: `pin/desk-digests/` (`DIGEST-MANIFEST.json`), with exact diffs of Gram r1→r2 (9ef42686…d10b), K2 r1→r2 (30a72ea2…f85b) and the driver chain.
- **Prompts, notes, receipts and logs.** `moqls7-gram-delta-codex-v1.*` and `moqls7-gram-delta-claude-v1.*` in R.
- **Desk files.**
  - `desk/delta-check-desk.md`: independent audit, written before either delegate note was read.
  - `desk/finding-map-v2.md`: supersedes v1, whose code line ranges were approximate.
  - `desk/lf-erratum.*`.
  - `desk/replay-static-check.*`.
  - `desk/delegate-review-*.json`.
  - `desk/launch-provenance.json`.
  - `checkpoints/ckpt-01…06`.

## 8. Deviations (none affects the evidence)
- `desk/launch-provenance.json` guessed the Claude launch time as "23:57". The job's echo line gives 23:54:00, and the Codex launch was 23:52:53. Corrected in ckpt-03 and here.
- `finding-map.md` v1 cited some code line ranges a few lines off. v2 machine-checks 164 references. v1 is kept unchanged.
- `pin_build.py` created subdirectories with `exist_ok=True`, but only below the freshly created `pin/` root. Every file was created with `open(..., 'x')`.
- The desk ran three stdlib scripts, read/hash/diff only, from bash: `pin_build`, `digest_build` and `replay_static_check`. It ran no solver, encoder, checker, compiler or network call. The CLI reviewers ran with TMPDIR set to the desk's `tmp-*`. Their CLI-internal state outside the desk was not controlled.
