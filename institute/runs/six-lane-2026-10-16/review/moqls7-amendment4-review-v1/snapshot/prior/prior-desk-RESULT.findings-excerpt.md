# EXCERPT of moqls7-k3-cover-review-v1/RESULT.md (source sha256 0f80460c1059a10fe6f3c614e55a5fdd7fd2af6606cc0b8b80781cc8d89eef84; 133 LF-lines by text.split('\n'))
# Prior delegated desk RESULT (K3 cover review). Omitted: LF24-58 (agreed verified content / derivations) and LF125-end (artifact list).
# Lines are VERBATIM, prefixed with their ORIGINAL 1-based LF number. Cite as prior/prior-desk-RESULT.findings-excerpt.md:LF<n>.
# DELTA-AUDIT USE ONLY: these are earlier reviewer findings, not premises and not parent conclusions.

----- original LF1-23 -----
LF1: # K3 cover / G6 / lex / AMENDMENT-4: static review desk result (M7K3CoverReviewDesk), 2026-10-18 PT
LF2: 
LF3: Scope: two static CLI reviews plus a desk static reading of pinned snapshot `snapshot/` (manifest `836c336a…a47d`; 48 files;
LF4: all six requested pins match; draft AMENDMENT-4 still `d9794b9d…47d7ee`, unchanged). No native replay, solver, CNF
LF5: generation or mathematical script was run by the desk or by the reviewers. **No K3 or M(7) verdict.** The parent owns
LF6: dispositions.
LF7: 
LF8: | Review | Model (reported) | Time | Disposition | FATAL | MAJOR | MINOR | Note SHA-256 |
LF9: |---|---|---|---|---|---|---|---|
LF10: | `moqls7-k3-cover-codex-v1` | gpt-6.1-sol, effort max, read-only sandbox | 373 s | ACCEPT-WITH-FIXES (Q1–Q4); Q5 ACCEPT-WITH-FIXES as conditional mathematics | 0 | 2 | 2 | `42392eaa…8809` |
LF11: | `moqls7-k3-cover-claude-v1` | claude-opus-5-5, no tools, 124 KB inline packet | 1154 s | ACCEPT-WITH-FIXES | 0 | 2 (both Q5) | 15 | `7ab7de84…79b3` |
LF12: 
LF13: Codex provenance: `codex-command-provenance.json` lists 48 shell commands. One was `pwd` in R; the rest were cat, nl, rg and
LF14: shasum, all inside the snapshot. No interpreter, write or outside path appears.
LF15: 
LF16: ## Per-step status (consolidated)
LF17: | Step | Codex | Claude | Desk | Consolidated |
LF18: |---|---|---|---|---|
LF19: | Q1 cover | SOUND | SOUND | SOUND | **SOUND**; wording nit only |
LF20: | Q2 G6 + variable map | REQUIRES-FIXES (doc) | SOUND | SOUND | **SOUND**; documentation erratum for the B map |
LF21: | Q3 lex leaders | REQUIRES-FIXES (doc) | SOUND | SOUND | **SOUND**; invariance statement and T(X) definition need fixes |
LF22: | Q4 composition/bindings | REQUIRES-FIXES | REQUIRES-FIXES | SOUND (CNF bytes); binding gaps | **REQUIRES FIXES** (provenance/documentation only; no soundness defect found) |
LF23: | Q5 draft AMENDMENT-4 | REQUIRES-FIXES | REQUIRES-FIXES | sound in principle | **REQUIRES FIXES before any freeze**; mathematics conditionally sound |
----- original LF59-124 -----
LF59: ## Findings to act on (parent decides; frozen artifacts must not be rewritten, so fixes go to new versions or sidecars)
LF60: **MAJOR**
LF61: 1. *(Codex M1; Claude m6; desk.)* `AMENDMENT-3.r1.md:46` requires binding the source cube metadata. `k3_lex.py:128-132` and `explore/k3lex/A_C311.meta.json:4-7` bind only the source CNF SHA (and an in-process control "PASS"), not the source cube metadata `3b2ab04f…` or the control receipt SHA.
LF62:    - Values cross-check (the bound CNF SHA equals the cube metadata and screen receipt).
LF63:    - Desk view: a provenance deviation, not a soundness defect.
LF64:    - Fix: a sidecar binding record.
LF65: 2. *(Codex M2; Claude D1.)* The draft (`AMENDMENT-4.md:8, :23, :28`) never states the G4 bridge prerequisite.
LF66:    - Transport needs the source triple heavy on every own row/column line for all squares. That holds only for a minimal triple, i.e. with K1 accepted and **K2 parent-accepted** (K2 is pending).
LF67:    - Fix: add an explicit hypothesis paragraph covering K1/K2, the encoder bridge, K3 only (14 row/column lines, no L lines), and minimal configurations only.
LF68: 3. *(Claude D2; Codex M2.)* `AMENDMENT-4.md:3-4, :20, :22-23, :33-34, :50-51` treats producer certificates as exclusions ("contradicting its UNSAT certificate", "previously checked cube exclusions").
LF69:    - The §3.1 gate only asks for "successful … certificate receipts".
LF70:    - Fix: gate on parent-ACCEPTED exclusions of the exact CNFs C321 `d598…8388` and C411 `2b92…ddf2`, under a stated A-only or A+B standard, with K2 accepted.
LF71: 
LF72: **MINOR**
LF73: - Q2 / B map *(Codex m2; Claude m2; desk).* `AMENDMENT-2.r1.md:43-45` says the wrapper reads and confirms each encoder's map. For B it checks only `int(nv) >= 2646` (`k3_cubes.py:126`).
LF74:   - Index equality holds by static reading.
LF75:   - The byte-identical A/B appended blocks are tautological (same vmap), not evidence.
LF76:   - Fix: an erratum, plus a runtime oracle before relying on any B certificate. Claude suggests driving B's `--fix-json` branch, `gram_encB.py:203-215`.
LF77: - Q3 invariance *(Codex m1; Claude m4; desk).* C411's column (3,4) swap (`k3_lex.py:33`) sends the --sym unit g_1(p,(0,3)) (var 109) to var 145. That is a C411 cube unit, not a base unit.
LF78:   - Invariance holds for the base∧cube g-projection only.
LF79:   - Fix: reword `AMENDMENT-3.r1.md:10, :20`.
LF80: - Q3 *(Claude m5; desk).* Define T(X)_v = X_{σ(v)} at `AMENDMENT-3.r1.md:25-28`.
LF81: - Wording *(Claude m1, m3; desk).*
LF82:   - `AMENDMENT-2.r1.md:10, :31`: add that the (0,0) coefficient is zero by G1.
LF83:   - `G6-G2-DERIVATION.r1.md:5-6/:8`: (0,0) is absent by G1, not fixed by the cube.
LF84:   - `G6-G2-DERIVATION.r1.md:12`: for collinear (p,t), read "G1+G2 forbid count 1 so g(q,t)=0".
LF85: - Stale binding *(Claude m7).* `AMENDMENT-3.bindings.r1.json:16-18` names `k3_cube_certify.py` with 1800/3600 caps, but the receipts pin `k3_cube_certify_r2.py` with 3600/3600.
LF86:   - Desk check: `K3-CERTIFICATION-DRIVER-DELTA.r2.json` (frozen_at 21:39:20, mtime 21:39:40) and the r2 driver (mtime 21:38:35) predate the A/C321 start at 21:39:49. The delta's driver SHA `49677766…` equals the receipts' pin.
LF87:   - Fix: bind the delta explicitly.
LF88: - Chronology *(Claude m8; desk mtimes).*
LF89:   - AMENDMENT-3: text 21:20:38 < controls 21:20:47 < lex CNF 21:20:58 < bindings 21:21:50 (frozen_at 21:21:39) < first lex screen 23:06:05.
LF90:   - AMENDMENT-2: text 19:32:24 < coverage 19:33:49 < CNFs 19:33:50 < bindings 20:13:32 < screen 20:13:35.
LF91:   - The binding records postdate input generation but precede search. g6_controls (20:15:24) postdates the first screen start and is not load-bearing.
LF92:   - Mtimes are filesystem facts, not attestations.
LF93: - Dependency text *(Claude m9; Codex M2; desk).*
LF94:   - The K2 prerequisite is absent from AMENDMENT-3 and from the receipt scope fields.
LF95:   - `AMENDMENT-2.r1.md:5` cites GRAM r1, whose G4 pointed to K1 §8. That was corrected in `GRAM-ENCODING.r2.md:52-65` and `LEMMAS.md:69-78`.
LF96: - Status wording *(Claude m10).* `GRAM-ENCODING.r2.md:136-138` implies certification alone makes an exclusion.
LF97: - AMENDMENT-4 polish *(Claude m11–m14; desk).*
LF98:   - `AMENDMENT-4.md:33` and the title "all-frame": qualify as "own row/column frames".
LF99:   - `AMENDMENT-4.md:18-23`: write out the full maps, including squares b→2, c→3.
LF100:   - `AMENDMENT-4.md:13`: justify w_a ≥ 1.
LF101:   - `AMENDMENT-4.md:61`: name the C311 instance (original or lex) and state the H-invariance of the cuts.
LF102:   - §3.3 should also check clause distinctness and the per-encoder literal map.
LF103:   - Missing spaces at `AMENDMENT-4.md:37, :44-45`.
LF104: - Non-issue, resolved by the desk *(Claude m15).* The two A_C311 screen solver logs share SHA `8fba55ce…` because both are exactly `c UNKNOWN\n` (10 bytes).
LF105: 
LF106: ## What a final use of AMENDMENT-4 would require (both reviewers agree)
LF107: 1. K1 accepted and K2 parent-accepted (so G4 holds for K3).
LF108: 2. Accepted encoder bridge(s), plus the B-map erratum and oracle if B is used.
LF109: 3. Accepted cover and --sym WLOG.
LF110: 4. Parent-accepted C321/C411 exclusions of the exact CNFs.
LF111: 5. A reviewed transport lemma, corrected as above.
LF112: 6. A frozen, reviewed cut generator: exact 238140 distinct clauses, per-encoder literal map, output SHA bound, and the §3.3 control.
LF113: 7. If combined with lex, an explicit H-invariance statement.
LF114: 8. A new regenerated DRAT-checked UNSAT of the exact strengthened C311 input on the protocol's independent route(s).
LF115: 9. A parent review of the full composition: K1∧K2 ⇒ G4 ⇒ --sym ⇒ three cubes ⇒ {C321, C411 accepted; transport ⇒ cuts; C311+cuts certified}.
LF116: 
LF117: ## Desk file erratum
LF118: `desk-analysis.md` (written during the runs) has four code line references off by a few lines. Correct:
LF119: - `k3_cubes.py:126` (not 121);
LF120: - `gram_encB.py:113-118` (not 118-124);
LF121: - `k3_lex.py:128-132` (not 121-125);
LF122: - `k3_cube_certify_r2.py:49-50` (not 45-46).
LF123: 
LF124: The file is left unmodified, per the no-overwrite rule.
