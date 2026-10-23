# Old Gram findings → new evidence (desk M7GramDeltaDesk; independent of the two delegate audits)

Paths are given relative to `moqls7-gram-delta-v1/pin/`, with line N = element N of `text.split('\n')`. The old notes are `parent/moqls7-gram-review-codex-v1.note.md` (Codex) and `parent/moqls7-gram-review-claude-v2.note.md` (Claude).

Status words:
- **RESOLVED**: fixed in the new text or evidence.
- **BY-DOMAIN**: the frozen bytes are intentionally unchanged and the finding is closed by a checked production-domain or overlay argument.
- **POST-HOC**: resolved by evidence produced after the K2 certificates.
- **PARTIAL**: resolved except for a residual that is not about soundness.

| Old finding | Status | New evidence | Residual or reason |
|---|---|---|---|
| Codex MAJOR-1 (LF9–11): class-list provenance | RESOLVED | `parent/moqls7-ls147-parent-v1/REPORT.md:3-9,41-62`; `result.json` main_checks all PASS; `lane/review/K2-CLASSIFICATION-SOURCE.r1.json:8-19`; `lane/review/GRAM-ENCODING.r2.md:71-87`; `lane/review/K2-THEOREM.r2.md:55-63` | The producer binary and seed provenance is still unrecorded. It no longer matters: the parent validated the list content directly and reused its own full 16942080 count. |
| Codex MAJOR-2 (LF13–15): frozen-control rerun and code-hash record | PARTIAL | Rerun files `lane/evidence/gram/gram_controls{A,B}_frozen.json` (19:06:14/18) and `controls_code_sha256.txt` (19:05:49) predate the first certificate at 19:31:09. Receipt pins: `lane/code/gram_certify_r4.py:179-184`. Desk binding table: 294/294 receipts bind the 7 expected pins. Classfile hash: `gram_certify_r4.py:182`, `gram_cert_summary.py:59` | The rerun JSONs are byte-identical to the 18:25/18:40 exploratory outputs and carry no CNF or log hash. Receipts do not bind the control results. The class key is implicit (index plus classfile hash); `desk-digests/k2-cert-r4-binding-table.json` makes it explicit. |
| Codex MAJOR-3 (LF17–21): bounded protocol, FIFO lifecycle, SAT retention | RESOLVED (liveness residual) | `gram_certify_r4.py:61-83` (RSS, floor and wall SIGTERM; no SIGKILL), `:103,:112,:142` (native caps), `:134-144` (logs to files), `:147-149` (strict acceptance), `:173-176` (caps ≤3600 s); `lane/review/CERTIFY-DRIVER-DELTA.r2/r3/r4.json`; `GRAM-ENCODING.r2.md:155-157` | `open(fifo,"rb")` at `gram_certify_r4.py:141` blocks forever if a solver exits before opening its proof path. This is fixed only prospectively, in `proof_stream.py` for K3. All 294 K2 runs completed. |
| Codex MAJOR-4 (LF23–25): sym/heavy+sym, sym-distinguishing negative, A's K2-shape control, "before production" | POST-HOC | `lane/evidence/gram/review_controls_r1/summary.json` (26/26). Desk re-hash: `desk-digests/review-controls-r1-file-checks.json`. `GRAM-ENCODING.r2.md:106-126`; `K2-THEOREM.r2.md:130-139` | The first control receipt is 21:24:52, 4335 s after the last K2 certificate. Codex had asked for these controls *before production* at 19:16:11, 898 s before the first certificate. They are not preregistration. |
| Codex MINOR-1 (LF29): encoder A docstring cites K1 §8 | BY-DOMAIN | `GRAM-ENCODING.r2.md:25-27,63-65`; `LEMMAS.md:69-78`; `REVIEW-CORRECTIONS.r2.json:18,25` | The frozen docstring at `gram_enc.py:15-16` is unchanged on purpose. |
| Codex MINOR-2 (LF31): Gram conventions | RESOLVED | `GRAM-ENCODING.r2.md:30-34` | — |
| Codex MINOR-3 (LF33): status text, split sentence, unversioned filename | RESOLVED | `GRAM-ENCODING.r2.md:3-6`. The canonical `review/GRAM-ENCODING.md` is byte-identical to r2 (`MANIFEST.json` unversioned_canonical_alias; `REVIEW-CORRECTIONS.r2.json:9`). | The alias file is mutable; cite r2 by hash. |
| Codex MINOR-4 (LF35): B validation and malformed branch | BY-DOMAIN | `GRAM-ENCODING.r2.md:141-152`; `REVIEW-CORRECTIONS.r2.json:26`; production calls at `gram_certify_r4.py:96-112`; harness checks at `gram_review_controls.py:48-55,140-142` | Desk T2 check confirms the branch is unreachable in production (see delta-check §4). |
| Codex MINOR-5 (LF37): hash abbreviations | RESOLVED | `lane/review/K1-THEOREM.r3.md:82` gives the full `…e113` hash; `lane/README.md:7` now reads `…a3ff2` | README is a mutable lane file; the old snapshot keeps the old text. |
| Codex MINOR-6 (LF39): manifest LF convention | RESOLVED (desk erratum) | `desk/lf-erratum.md` and `.json`: 14/18 rows one low; all 223 citations unchanged | The parent-owned manifest is not rewritten (`REVIEW-CORRECTIONS.r2.json:27`). |
| Claude MAJOR-1 (LF85–104): class completeness unbound | RESOLVED | As Codex MAJOR-1, plus the normalisation proof at `GRAM-ENCODING.r2.md:73-78` | The suggested rebuild from pinned source and seeds was not done. Direct parent validation supersedes it. |
| Claude MAJOR-2 (LF106–132): driver (a)–(e) | PARTIAL | (a) caps: `gram_certify_r4.py:103,112,142`. (b) SAT output kept in `*.solver.log` (`:134-136`). (c) code, classfile and checker SHAs: `:179-184`. (d) rc20, rc0 and exact status: `:147-149`. (e) logs go to files. | Solver binaries and versions are unbound (`K2-THEOREM.r2.md:75-77`). The producer did not bind the drat-trim binary to its source; the parent replay uses its own checker. The FIFO-open hang path is as in Codex MAJOR-3. Nothing is decoded via vmap, and no SAT result occurred. |
| Claude MAJOR-3 (LF134–161): controls (i)–(v), GC4, B mutants, unbound JSONs, 4×4 | POST-HOC; (v) PARTIAL | (i)–(iv): `review_controls_r1` (26/26). GC4 is relabelled as G5-only at `GRAM-ENCODING.r2.md:106-107` and `K2-THEOREM.r2.md:123-124`. The 4×4 control is explained at `GRAM-ENCODING.r2.md:125-126`. | (v) The end-to-end FIFO negatives ran on the new K3 transport (`transport_controls_r2`), not on the r4 path. They use the same checker binary `111b0405…` but different transport code. The r4 path has 294 positive end-to-end runs. The old frozen JSONs are still unbound. |
| Claude MINOR-1 (LF165–168): G4 cites K1 §8 | BY-DOMAIN | as Codex MINOR-1 | `AMENDMENT-1.r1.md:18` is frozen and unchanged. |
| Claude MINOR-2 (LF170–173): stale references and status | RESOLVED | `GRAM-ENCODING.r2.md:3-6` plus the canonical alias | No code docstring changed, so the code pins still hold. |
| Claude MINOR-3 (LF175–180): latent malformed or vacuous output | BY-DOMAIN | Desk T2 (delta-check §4); `gram_review_controls.py:48-55,140-142` | The encoders were not hardened. The general hazard is concrete, though: for every reduced L, cells (1,0) and (0,1) share symbol 1, so `--sym` with a net would emit `None` at `gram_enc.py:125` and `gram_encB.py:193`. Production never makes that call. |
| Claude MINOR-4 (LF182–185): A/B fix-json differences | BY-DOMAIN | Production never passes `fix` (`gram_certify_r4.py:100`, `:104-109`). The harness asserts that fixed supports are G1-valid (`gram_review_controls.py:51`). | — |
| Claude MINOR-5 (LF187–190): status parsing and unknown IDs | RESOLVED | `gram_certify_r4.py:89-96` rejects unknown kinds and indices; `:145-149` requires exact-line equality after CR→LF | The driver still strips all whitespace, not just CR. Exact-line equality keeps this unambiguous. |
| Claude MINOR-6 (LF192–194): exploration results in claim documents | RESOLVED | Exploration is labelled at `GRAM-ENCODING.r2.md:129,136-139`; the ≤23.5 s claim is gone | The frozen AMENDMENT-1 is historical. |
| Claude MINOR-7 (LF196–200): wording | RESOLVED (cosmetic residual) | `GRAM-ENCODING.r2.md:43-44,61-62`; `LEMMAS.md:75-78` | Transposition is still listed at `GRAM-ENCODING.r2.md:88`, though it is unused. `AMENDMENT-1.r1.md:29` is frozen. |
| Claude MINOR-8 (LF202–205): hashes | RESOLVED | `GRAM-ENCODING.r2.md:9-12`; `K1-THEOREM.r3.md:82`; `README.md:7` | `GRAM-ENCODING.r2.md:15-16` still abbreviates the two K3-only hashes; the full values are in `K3-CERTIFICATION-DRIVER-DELTA.r2.json:4-5`. |

**Are all previous MAJORs resolved?** Not all of them completely. None of the residuals touches soundness: the static bridge, class coverage (LS147) and the separately replayed proofs carry the theorem.
- Codex MAJOR-1 and Claude MAJOR-1 are resolved.
- Codex MAJOR-3 is resolved except for the startup-liveness path, which is acknowledged.
- Codex MAJOR-4 and Claude MAJOR-3 are resolved post hoc, after K2.
- Codex MAJOR-2 and Claude MAJOR-2 are partial: run-time binding of the frozen-control rerun and of solver binaries is still missing.
- Claude MAJOR-3 (v) was exercised on the new transport only.

## Desk findings on the new texts
- **DM-1 (MINOR, chronology).** `lane/review/K2-THEOREM.r2.md:130` says the matched controls were requested "After K2 production". The Codex note's request (Codex LF23–25: "before production") was returned at 19:16:11, 898 s before the first certificate at 19:31:09 (`desk-digests/chronology.json`).
  - Fix: say the request preceded production, production went ahead without the controls, and they ran at 21:24–21:25.
- **DM-2 (MINOR, protocol deviation).** `lane/README.md:91` (frozen §0.5) requires every encoding to admit all matched genuine controls before production. Encoder A's K2-shaped classical positive first ran after production (`review_controls_r1`, 21:24:52).
  - The new texts give the timing (`GRAM-ENCODING.r2.md:115,124`) but do not call it a deviation from README §0.5.
  - Fix: add one explicit deviation sentence.
- **DM-3 (MINOR, references).** Two texts point at superseded versions:
  - `GRAM-ENCODING.r2.md:134` points to `K2-THEOREM.r1.md`.
  - `LEMMAS.md:77` says it justifies G4 "in GRAM-ENCODING.r1.md". The G4 text is the same in r2.
  - The pinned claim `K2-THEOREM.r1.md` has these stale points: `:16` cites K1 r2 instead of the accepted r3; `:27` cites Gram r1; `:63,:67` give solver versions the receipts do not bind; `:99-100` cite unreceipted checker controls; `:106` states the mutation count imprecisely.
  - Fix: integrate `K2-THEOREM.r2.md` (`a73a9007…32cd`), which corrects all of these, as the theorem text. The CNFs, receipts and inventories are unchanged between r1 and r2, so a replay bound to r1 still applies.
- **DM-4 (MINOR, trust boundary).** `code/k2_classes.py` (`b49099e4…b891`; `square_from_key`) is in the production chain and bound in every receipt. GRAM r2 dropped its pin line (r1 LF21), and K2 r2 never names it.
  - Fix: cite it in K2 r2 §3/§4.
- **DM-5 (MINOR, clarity).** `GRAM-ENCODING.r2.md:142` says "Every production L is a validated Latin square". The r4 driver does not validate L.
  - Fix: cite the actual sources, LS147 (`latin_reduced_all` PASS) and the parent replay's decoder check.
- **DM-6 (MINOR, provenance).** Receipts hash the reused scratch CNF (`gram_certify_r4.py:119,128`); the solver and checker then re-read the same path.
  - The binding assumes no concurrent writer. No overlapping A/B intervals were observed.
  - The parent replay's independent regeneration and hash comparison closes this.
- **DM-7 (MINOR, citation).** `K2-THEOREM.r2.md:19` cites the printed Lemma 10 (source LF178–192), which is stated for one partner Φ. The arbitrary-basis, all-partners form actually used is `LEMMAS.md:54-67`.
  - Fix: cite LEMMAS.md there.
- **DM-8 (cosmetic).** Two small text issues in GRAM r2:
  - `GRAM-ENCODING.r2.md:6`: "This file did not exist…" has an ambiguous antecedent.
  - `GRAM-ENCODING.r2.md:136-138`: the K3 status is as of 21:41; out of K2 scope.
