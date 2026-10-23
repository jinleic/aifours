# K3 cover / G6 / lex / AMENDMENT-4: static review desk result (M7K3CoverReviewDesk), 2026-10-18 PT

Scope: two static CLI reviews plus a desk static reading of pinned snapshot `snapshot/` (manifest `836c336a…a47d`; 48 files;
all six requested pins match; draft AMENDMENT-4 still `d9794b9d…47d7ee`, unchanged). No native replay, solver, CNF
generation or mathematical script was run by the desk or by the reviewers. **No K3 or M(7) verdict.** The parent owns
dispositions.

| Review | Model (reported) | Time | Disposition | FATAL | MAJOR | MINOR | Note SHA-256 |
|---|---|---|---|---|---|---|---|
| `moqls7-k3-cover-codex-v1` | gpt-6.1-sol, effort max, read-only sandbox | 373 s | ACCEPT-WITH-FIXES (Q1–Q4); Q5 ACCEPT-WITH-FIXES as conditional mathematics | 0 | 2 | 2 | `42392eaa…8809` |
| `moqls7-k3-cover-claude-v1` | claude-opus-5-5, no tools, 124 KB inline packet | 1154 s | ACCEPT-WITH-FIXES | 0 | 2 (both Q5) | 15 | `7ab7de84…79b3` |

Codex provenance: `codex-command-provenance.json` lists 48 shell commands. One was `pwd` in R; the rest were cat, nl, rg and
shasum, all inside the snapshot. No interpreter, write or outside path appears.

## Per-step status (consolidated)
| Step | Codex | Claude | Desk | Consolidated |
|---|---|---|---|---|
| Q1 cover | SOUND | SOUND | SOUND | **SOUND**; wording nit only |
| Q2 G6 + variable map | REQUIRES-FIXES (doc) | SOUND | SOUND | **SOUND**; documentation erratum for the B map |
| Q3 lex leaders | REQUIRES-FIXES (doc) | SOUND | SOUND | **SOUND**; invariance statement and T(X) definition need fixes |
| Q4 composition/bindings | REQUIRES-FIXES | REQUIRES-FIXES | SOUND (CNF bytes); binding gaps | **REQUIRES FIXES** (provenance/documentation only; no soundness defect found) |
| Q5 draft AMENDMENT-4 | REQUIRES-FIXES | REQUIRES-FIXES | sound in principle | **REQUIRES FIXES before any freeze**; mathematics conditionally sound |

## Agreed verified content (all three readings)
- **Q1.** CUBES matches the AMENDMENT-2 table, and all 18 signed units are emitted.
  - S_a ⊆ {1..6} is nonempty by unit norm plus G1 on (0,0), and at Boolean level by G3.
  - The S_a are disjoint by G5, and S_1 ⊇ {1,2,3} by the --sym units.
  - There are exactly 18 assignments (64−27−27+8). They split into three disjoint 6-orbits under S3(4,5,6)×⟨(2 3)⟩, and each orbit's stabiliser is that cube's extra lex generator.
  - No case is missed (|S_1| ≥ 5 is impossible).
  - The residual operations preserve G1–G5, G4 with (1,row0) fixed, and the --sym units.
  - The --sym WLOG holds for every all-line-heavy triple.
- **Q2.** The same-ray argument holds for arbitrary phases. The G1/G2 derivation covers every t case, including absent and diagonal predicates.
  - Encoder A and encoder B clause families reduce exactly to the G6 implications.
  - The 70-clause pattern per singleton (5+5+12·5) gives 158/88/158, matching the bytes.
  - Indices 1..2646 agree for A (asserted at runtime) and for B (by static reading of `gram_encB.py:113-118` only).
- **Q3.** All 22 generators are involutive predicate bijections that preserve the signed cube units and G6.
  - Comparator semantics: an assignment of the prefix auxiliaries exists iff X ≤lex X∘σ. This holds with shared pairs, skipped fixed positions and fresh auxiliaries.
  - X∘σ is the pattern of a transformed actual configuration, so involution is not needed.
  - Counts: 6·4156 + 6676 = 31612 clauses and 10535 auxiliaries, giving header 107513/659168 (bytes match).
  - Coverage: a common lex-minimal H-orbit member satisfies every comparator. No invariance is assumed.
- **Q4.** Both wrappers copy the base/cube text unchanged and only append clauses with recomputed headers.
  - The certificate driver r2 regenerates with the frozen wrapper and asserts the screen CNF SHA (`k3_cube_certify_r2.py:49-50`).
  - Desk SHA-256 checks of all 9 lane CNFs match every metadata, screen and receipt binding.
  - The checker logs show 96978 variables with 627486/627556 clauses and an exact `s VERIFIED`. These are producer records, not parent replay.
  - No four-square lemma is used: LEMMAS W is the three-square bound.
- **Q5 (conditional).** Transport works for every own row/column frame and every off-line point:
  - transpose first if the frame is a column;
  - ρ: ℓ↦0, row(p)↦1;
  - κ: col(p)↦0, with the supports sent to the cube columns;
  - squares relabelled a,b,c → 1,2,3.

  The image satisfies the exact 18 literals, the --sym units, every base G4 constraint and G6. So (4,1,1)→C411 and (3,2,1)→C321, and every surviving weight≥3 occurrence in a row/column frame is (3,1,1).

  Direct clause consequences: 588·3·15 = **26460** at-most-three clauses plus 588·6·20·3 = **211680** mixed clauses, **238140** in total. They are distinct, need no auxiliaries, and the overlapping cases are implied by G5. The cut family is invariant under all row, column and square permutations and under transposition, hence compatible with the AMENDMENT-3 lex group.

  No arbitrary-ONB or classical-symbol-line transport is valid. The old C321/C411 proofs certify nothing about a strengthened C311 CNF.

## Findings to act on (parent decides; frozen artifacts must not be rewritten, so fixes go to new versions or sidecars)
**MAJOR**
1. *(Codex M1; Claude m6; desk.)* `AMENDMENT-3.r1.md:46` requires binding the source cube metadata. `k3_lex.py:128-132` and `explore/k3lex/A_C311.meta.json:4-7` bind only the source CNF SHA (and an in-process control "PASS"), not the source cube metadata `3b2ab04f…` or the control receipt SHA.
   - Values cross-check (the bound CNF SHA equals the cube metadata and screen receipt).
   - Desk view: a provenance deviation, not a soundness defect.
   - Fix: a sidecar binding record.
2. *(Codex M2; Claude D1.)* The draft (`AMENDMENT-4.md:8, :23, :28`) never states the G4 bridge prerequisite.
   - Transport needs the source triple heavy on every own row/column line for all squares. That holds only for a minimal triple, i.e. with K1 accepted and **K2 parent-accepted** (K2 is pending).
   - Fix: add an explicit hypothesis paragraph covering K1/K2, the encoder bridge, K3 only (14 row/column lines, no L lines), and minimal configurations only.
3. *(Claude D2; Codex M2.)* `AMENDMENT-4.md:3-4, :20, :22-23, :33-34, :50-51` treats producer certificates as exclusions ("contradicting its UNSAT certificate", "previously checked cube exclusions").
   - The §3.1 gate only asks for "successful … certificate receipts".
   - Fix: gate on parent-ACCEPTED exclusions of the exact CNFs C321 `d598…8388` and C411 `2b92…ddf2`, under a stated A-only or A+B standard, with K2 accepted.

**MINOR**
- Q2 / B map *(Codex m2; Claude m2; desk).* `AMENDMENT-2.r1.md:43-45` says the wrapper reads and confirms each encoder's map. For B it checks only `int(nv) >= 2646` (`k3_cubes.py:126`).
  - Index equality holds by static reading.
  - The byte-identical A/B appended blocks are tautological (same vmap), not evidence.
  - Fix: an erratum, plus a runtime oracle before relying on any B certificate. Claude suggests driving B's `--fix-json` branch, `gram_encB.py:203-215`.
- Q3 invariance *(Codex m1; Claude m4; desk).* C411's column (3,4) swap (`k3_lex.py:33`) sends the --sym unit g_1(p,(0,3)) (var 109) to var 145. That is a C411 cube unit, not a base unit.
  - Invariance holds for the base∧cube g-projection only.
  - Fix: reword `AMENDMENT-3.r1.md:10, :20`.
- Q3 *(Claude m5; desk).* Define T(X)_v = X_{σ(v)} at `AMENDMENT-3.r1.md:25-28`.
- Wording *(Claude m1, m3; desk).*
  - `AMENDMENT-2.r1.md:10, :31`: add that the (0,0) coefficient is zero by G1.
  - `G6-G2-DERIVATION.r1.md:5-6/:8`: (0,0) is absent by G1, not fixed by the cube.
  - `G6-G2-DERIVATION.r1.md:12`: for collinear (p,t), read "G1+G2 forbid count 1 so g(q,t)=0".
- Stale binding *(Claude m7).* `AMENDMENT-3.bindings.r1.json:16-18` names `k3_cube_certify.py` with 1800/3600 caps, but the receipts pin `k3_cube_certify_r2.py` with 3600/3600.
  - Desk check: `K3-CERTIFICATION-DRIVER-DELTA.r2.json` (frozen_at 21:39:20, mtime 21:39:40) and the r2 driver (mtime 21:38:35) predate the A/C321 start at 21:39:49. The delta's driver SHA `49677766…` equals the receipts' pin.
  - Fix: bind the delta explicitly.
- Chronology *(Claude m8; desk mtimes).*
  - AMENDMENT-3: text 21:20:38 < controls 21:20:47 < lex CNF 21:20:58 < bindings 21:21:50 (frozen_at 21:21:39) < first lex screen 23:06:05.
  - AMENDMENT-2: text 19:32:24 < coverage 19:33:49 < CNFs 19:33:50 < bindings 20:13:32 < screen 20:13:35.
  - The binding records postdate input generation but precede search. g6_controls (20:15:24) postdates the first screen start and is not load-bearing.
  - Mtimes are filesystem facts, not attestations.
- Dependency text *(Claude m9; Codex M2; desk).*
  - The K2 prerequisite is absent from AMENDMENT-3 and from the receipt scope fields.
  - `AMENDMENT-2.r1.md:5` cites GRAM r1, whose G4 pointed to K1 §8. That was corrected in `GRAM-ENCODING.r2.md:52-65` and `LEMMAS.md:69-78`.
- Status wording *(Claude m10).* `GRAM-ENCODING.r2.md:136-138` implies certification alone makes an exclusion.
- AMENDMENT-4 polish *(Claude m11–m14; desk).*
  - `AMENDMENT-4.md:33` and the title "all-frame": qualify as "own row/column frames".
  - `AMENDMENT-4.md:18-23`: write out the full maps, including squares b→2, c→3.
  - `AMENDMENT-4.md:13`: justify w_a ≥ 1.
  - `AMENDMENT-4.md:61`: name the C311 instance (original or lex) and state the H-invariance of the cuts.
  - §3.3 should also check clause distinctness and the per-encoder literal map.
  - Missing spaces at `AMENDMENT-4.md:37, :44-45`.
- Non-issue, resolved by the desk *(Claude m15).* The two A_C311 screen solver logs share SHA `8fba55ce…` because both are exactly `c UNKNOWN\n` (10 bytes).

## What a final use of AMENDMENT-4 would require (both reviewers agree)
1. K1 accepted and K2 parent-accepted (so G4 holds for K3).
2. Accepted encoder bridge(s), plus the B-map erratum and oracle if B is used.
3. Accepted cover and --sym WLOG.
4. Parent-accepted C321/C411 exclusions of the exact CNFs.
5. A reviewed transport lemma, corrected as above.
6. A frozen, reviewed cut generator: exact 238140 distinct clauses, per-encoder literal map, output SHA bound, and the §3.3 control.
7. If combined with lex, an explicit H-invariance statement.
8. A new regenerated DRAT-checked UNSAT of the exact strengthened C311 input on the protocol's independent route(s).
9. A parent review of the full composition: K1∧K2 ⇒ G4 ⇒ --sym ⇒ three cubes ⇒ {C321, C411 accepted; transport ⇒ cuts; C311+cuts certified}.

## Desk file erratum
`desk-analysis.md` (written during the runs) has four code line references off by a few lines. Correct:
- `k3_cubes.py:126` (not 121);
- `gram_encB.py:113-118` (not 118-124);
- `k3_lex.py:128-132` (not 121-125);
- `k3_cube_certify_r2.py:49-50` (not 45-46).

The file is left unmodified, per the no-overwrite rule.

## Artifacts (all new; nothing overwritten)
- Prompts, notes, receipts and stdout/stderr: `R/moqls7-k3-cover-{codex,claude}-v1.*`.
  - Codex prompt: `a6c8e061…a249`.
  - Claude prompt: `4483882d…9dea`.
- Desk directory `R/moqls7-k3-cover-review-v1/`: `snapshot/`, `desk-analysis.md`, `codex-command-provenance.json`, `checkpoint-01.json`, `checkpoint-02.json`, `RESULT.md`, `RESULT.json`.
- Empty `tmp-codex/` and `tmp-claude/` were the reviewers' TMPDIRs.
- Pre-launch disk gate at 23:49:39: 13,927,656 KiB free, above 12.2e9 bytes plus about 5 MB projected (PASS).
