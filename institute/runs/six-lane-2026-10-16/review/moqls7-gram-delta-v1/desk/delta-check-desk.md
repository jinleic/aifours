# moqls7 Gram delta and complete-K2 audit: desk part (M7GramDeltaDesk)

Written 2026-10-18T00:02:40.556718-07:00 (host clock). This is an independent desk audit, written before either delegate note was read. **No theorem verdict.** Paths below are relative to `moqls7-gram-delta-v1/pin/`; line N is element N of `text.split('\n')`.

## 1. Pin and hashes
- **Pin.** `pin/MANIFEST.json` (`b53df0157d3c4debb21723f2b9db6b45fca31ec97270af116287d62e5d4e10cc`) lists 1013 copied files, 1,540,708 bytes, created by `desk/pin_build.py` (`33a2cb22…1221`).
  - Every copy re-hashed equal to its source, and every source mtime was unchanged after copying.
  - Not copied: 301 FIFOs, never opened. Also not copied: 52 review-control CNFs and SAT-model logs; their hashes are checked in `desk-digests/review-controls-r1-file-checks.json`.
- **Assignment hashes.** All match:

| File | SHA-256 | Note |
|---|---|---|
| GRAM-ENCODING.r2.md | `c6c506a7…d6c7` | |
| LEMMAS.md | `4bddc9d4…0c9` | |
| K2-THEOREM.r1.md | `e846e1d9…f05b` | |
| gram_enc.py | `b2c206d8…8833` | byte-identical to the old snapshot copy |
| gram_encB.py | `c7583efe…2b45` | byte-identical to the old snapshot copy |
| gram_certify_r4.py | `ec540a87…a18a` | |
| review_controls_r1/summary.json | `6ce1ddc2…d685` | |
| transport_controls_r2/summary.json | `34a69ae6…95e6` | |

- **Other bindings.**
  - REVIEW-CORRECTIONS.r2.json: `5105a686…0770`
  - K2-CLASSIFICATION-SOURCE.r1.json: `eb7f7b46…16ff`
  - LS147 REPORT.md: `49b75c2c…d8bf1`; result.json: `da16c149…3dd32`
  - K1 parent verdict: `1cd0603c…dfb8`
- **Not in the assignment list.** `review/K2-THEOREM.r2.md` (`a73a9007…32cd`, 21:42) exists with `K2-REVIEW-DELTA.r2.json`, and `review/GRAM-ENCODING.md` is byte-identical to r2. Both are pinned.

## 2. Exact old→new Gram text diff
- **Gram r1→r2.** `desk-digests/diff__review_GRAM-ENCODING.r1.md__to__review_GRAM-ENCODING.r2.md.diff` (`9ef42686…d10b`). Re-applying it to r1 reproduces r2 byte-for-byte.
  - Unchanged: the statements and proofs of G1, G2, G3, G5 and the G4 proof (r1 LF28-55 = r2 LF35-62); K3 symmetry (r1 LF67-71 = r2 LF88-92); the old controls table.
  - Changed:
    - status and header (r2 LF3-6);
    - driver pin, now r4 (LF11-16);
    - sym/K1-§8 note (LF25-27);
    - §1 conventions (LF30-34);
    - a three-line G4 addendum (LF63-65);
    - §3 normalisation proof, Egan–Wanless binding and the LS147 result (LF71-87);
    - §4 old-split relabel and the 26 new controls (LF106-126);
    - new §5-§7 (LF128-170).
  - r2 drops r1's pin lines for the controls and decoders (r1 LF20-21). See DM-4.
- **K2 r1→r2.** `diff__review_K2-THEOREM.r1.md__to__review_K2-THEOREM.r2.md.diff` (`30a72ea2…f85b`). It changes the status text, the K1-r3 and Gram-r2 references, the Egan–Wanless/LS147 binding, the solver-provenance wording and the checker-control replacement, and adds the post-K2 control paragraph. The proof objects and inventories are unchanged.
- **Driver chain.** `gram_certify.py` → r2 → r3 → r4, also diffed; see `diffs.json`.
  - r3→r4 changes only two things: proof transport (FIFO → stdin `-i`) and kissat `-f`. This matches CERTIFY-DRIVER-DELTA.r4.json.

## 3. Chronology (from receipts, recorded_at/frozen_at fields and mtimes; `desk-digests/chronology.json`)

| PDT, 2026-10-17 | Event |
|---|---|
| 19:02:40 | Old review snapshot pinned |
| 19:05:49–19:06:18 | Frozen-code control rerun: `controls_code_sha256.txt`, `gram_controls{A,B}_frozen.json`. The JSONs are byte-identical to the 18:25/18:40 exploratory outputs, and B scratch files carry 19:06:17–18 mtimes. |
| 19:15:22 | LS147 parent result created |
| 19:16:11 | Old Codex note returned. MAJOR-4 asks for component controls "before production". |
| 19:28:00–19:30:55 | Driver deltas r2–r4 frozen |
| **19:31:09–20:12:37** | All 294 K2 producer certificates; no A/B interval overlap |
| 20:14:20 | K2-THEOREM.r1.md written |
| 20:24:51 | Old Claude v2 note returned |
| **21:24:52–21:25:09** | 26 matched component controls |
| 21:27–21:42 | LEMMAS, K1 r3, transport controls r2, Gram r2, K2 r2 |
| 21:36:23 | Rejected `/dev/fd` transport trial r1 |
| **21:38:40–21:38:43** | Transport controls r2, on the new `proof_stream.py` |
| 21:39:20 | K3 driver delta r2 frozen. The K3 C321 certificate starts 21:39:49 (LOG.md:85-90). |

- **Honest reading.**
  - The 26 matched controls started 4335 s after the last K2 certificate. They are post hoc for K2, not retroactive preregistration, and they preceded K3 certification.
  - The transport controls r2 test the new K3 transport, 37 s before the K3 delta froze. They are prospective for K3 and do not exercise the r4 transport used for K2.
  - The Codex request for pre-production controls predates production by 898 s.
- **Texts that state this correctly.** GRAM r2 LF102, 107-108, 124 and 157; REVIEW-CORRECTIONS.r2.json:21; K2-REVIEW-DELTA.r2.json:11; K3-CERTIFICATION-DRIVER-DELTA.r2.json:14.
- **Imprecise.** `lane/review/K2-THEOREM.r2.md:130`. See DM-1.
- **Protocol deviation.** `lane/README.md:91` requires pre-production admission of matched genuine controls. For encoder A's K2-shape positive this was met only after production. See DM-2.

## 4. Production-domain claim (T2): CONFIRMED for the actual production calls
- **Calls.** `lane/code/gram_certify_r4.py:87-112`:
  - unknown kinds and indices are rejected (`:89-93`);
  - L is `square_from_key(rows[idx][0])` (`:94`), with rows the nonempty class-file lines (`:186`);
  - A calls `gram_enc.build(2|3, L|None, True, kind=="k3A", None)` (`:99-100`): sym only for K3 with L None, fix always None;
  - B is called as `--squares 2 --net-L L --heavy` for K2, or `--squares 3 --heavy --sym` for K3 (`:104-109`), never with `--fix-json`.
- **Validity of L.** All 147 L are reduced Latin squares: LS147 `latin_reduced_all` PASS, and the parent replay's own decoder check (`classfile.all_keys_reduced_latin`). So the 21 lines form a 3-net: two lines from different classes meet exactly once.
- **Counts.**
  - 3-net, point p off frame line ℓ: p's two other lines meet ℓ in two distinct points, giving exactly 5 structurally possible neighbours. Two off-line points exclude at most 4 points of ℓ, or 3 when they are collinear on a line meeting ℓ. Common candidates: ≥3.
  - 2-net (K3): 6 neighbours each; common candidates ≥5.
  - Transitions: r ∈ ℓ1∖ℓ2 has 5 (3-net) or 6 (2-net) candidates on ℓ2∖ℓ1. The point excluded by r's third-class line is never the meeting point s, or two lines would share two points.
- **Consequences.**
  - B's `counter2` returns `s2=None` only for a one-item list (`lane/code/gram_encB.py:46`). The malformed `B.clause(-s1, s2)` (`gram_encB.py:151`) therefore never occurs.
  - The empty clause `B.clause()` (`gram_encB.py:168-169`) is unreachable, and so are A's `F.add(nb)` with nb empty (`lane/code/gram_enc.py:106`), A's unguarded empty `at_least` (`gram_enc.py:48`; skipped at `:132`), and an empty guard list (`:137`).
  - The sym units at `gram_enc.py:125` and `gram_encB.py:193` concern (1,0)–(0,r), which share no row or column, so they are well-formed in the K3 2-net.
  - The permissive B `fix-json` path (`gram_encB.py:203-215`) is never invoked.
- **General-API hazard (context only, not production).** For *every* reduced L, cells (1,0) and (0,1) both carry symbol 1. So `--sym` combined with a net would emit a `None` literal in both encoders. Production never makes that call. The review-control harness asserts `not (sym and L)` (`lane/code/gram_review_controls.py:51`), Latin L (`:48-49`), G1-valid fixed supports (`:56`), and no `None` or empty clause (`:163-164`).
- **No production counterexample exists.** The desk byte scan of the 26 control CNFs found no `None`, no empty clause and consistent headers.

## 5. Complete K2 bridge (T3): no gap found (desk re-derivation)
1. **Straightening and (C1).** Take any K2 triple {Ψ1, Ψ2, L} of complex MOQLS(7) with Ψ1 and Ψ2 non-classical.
   - Apply phases and a unitary U to L alone. Then (I⊗U) maps each tensor ONB {ψ_p⊗l_p} to an ONB, and L becomes |L(p)⟩ with L Latin (`lane/review/LEMMAS.md:8-14`).
   - ⟨ψ_p⊗|L(p)⟩, ψ_q⊗|L(q)⟩⟩ = G(p,q)[L(p)=L(q)], so Ψ_a ⊥ L iff Ψ_a is an ONB on all 7 symbol lines (`LEMMAS.md:16-21`).
   - Hence each Ψ_a is an ONB-assignment on the 21-line 3-net N(L).
2. **Transport to a representative.**
   - Paratopy classes are exactly 3-net isomorphism classes: parallel classes are the classes of disjoint lines.
   - Carry both Ψ_a by the same point bijection N(L)→N(R_i). The new rows, columns and symbol lines are old ONB lines, so the QLS axioms and (C1) hold. The 49 tensor vectors are only re-indexed, so Ψ1'⊥Ψ2'. Ray multisets are unchanged, so both stay non-classical (C0).
   - R_i is the canonical representative of L's main class. LS147 shows the 147 keys cover all 16942080 reduced squares with distinct canonical keys (`parent/moqls7-ls147-parent-v1/REPORT.md:3-9,26-39,77-84`).
3. **Necessary Gram conditions.**
   - G1 holds on the ONB lines.
   - G2 follows from the frame expansion G(p,q)=Σ_r conj(G(r,p))G(r,q).
   - G3: transition matrices are unitary, with U[s,s]=1 at a meeting point.
   - G5 is exact: G_1·G_2=0, i.e. the two supports are edge-disjoint (`lane/review/GRAM-ENCODING.r2.md:38-51`).
4. **G4 heavy on all 21 own lines, for both squares.**
   - Suppose Ψ1 is light in some ONB B. Rotate Ψ1 alone so that B becomes the standard basis; all its Gram entries are unchanged.
   - Lemma 10 then applies (`lane/sources/2607.12933v2.layout.txt:178-192`; arbitrary-basis, all-partners form at `LEMMAS.md:54-67`). The desk re-derived it:
     - two weight-≤2 vectors overlapping in one coordinate have a nonzero inner product, so every zero Gram entry survives the rotation of the {a,b}-support entries;
     - rows and columns stay ONBs, and the number of weight-2 entries strictly drops;
     - the end result is classical;
     - every partner product G_Ψ·G_Φ keeps its former zero factor, so orthogonality to Ψ2 and to L holds simultaneously.
   - Undoing the rotation gives {Ψ1'', Ψ2, L} with exactly one non-classical square. This contradicts parent-accepted K1 (`parent/moqls7-k1-parent-verdict.md:5`), so the replacement leads to a contradiction directly; no minimisation step is needed for K2.
   - Own-line weight is #{r∈ℓ: g(p,r)} and on-line points have weight 1. So each of the 21 lines has an off-line point with ≥3 neighbours, for both squares.
5. **Both encoders are necessary.**
   - **Encoder A.**
     - Variables are exactly the non-collinear pairs (`lane/code/gram_enc.py:66-71`).
     - h ↔ AND (`:75-85`).
     - G2: g→OR h (`:96`), and h_x∧¬others→g; for collinear pairs this forbids a count of exactly 1 (`:99`).
     - G3: neighbour required (`:106`); a unique neighbour excludes the reverse neighbours (`:107-114`).
     - G5 pairwise (`:115-118`).
     - G4: guard w→≥3 via (n−2)-subsets, OR(guards) (`:119-137`). Extension: g from the genuine supports, h by definition, w_p true exactly when p has ≥3 neighbours.
   - **Encoder B.**
     - `counter2` is a full equivalence (`lane/code/gram_encB.py:41-57`).
     - G2 (`:136-157`), G3 (`:158-183`) and G5 (`:184-187`) as in A.
     - `counter_ge3` is one-directional (`:60-89`), so heavy is OR over p (`:188-202`). Extension: c[i][k] := [≥k among the first i], t := [≥3].
   - Neither encoder has a clause stronger than G1–G5 plus G4. So a genuine configuration yields a model of each CNF.
6. **Class decoding and coverage.**
   - The driver decodes `square_from_key(rows[i][0])` (`lane/code/k2_classes.py:22-33`; `gram_certify_r4.py:94,186`). This is the same row-major 36-digit convention LS147 validated (`REPORT.md:83-84`) and the parent replay independently re-decodes.
   - `desk-digests/k2-cert-r4-binding-table.json` (`93b61df6…e5c9`) binds each (encoder, i) to class key, receipt, CNF and log hashes.
   - Coverage: 147/147 indices per encoder; 147 distinct CNF hashes per encoder; all 11 static checks pass for all 294 receipts.
7. **Conclusion.** Every arbitrary-complex K2 triple yields a model of both encoders' CNFs for some i ∈ {0..146}. Valid UNSAT proofs of those 294 exact CNFs therefore exclude K2. This rests on accepted K1, LS147 coverage and the static bridge above.

## 6. References (T4)
- `lane/review/K2-THEOREM.r1.md` is the producer's frozen claim, and the parent replay is bound to it. It still cites:
  - K1 r2 (`:16`), but the accepted text is r3;
  - Gram r1 (`:27`), but the corrected text is r2;
  - solver versions the receipts do not bind (`:63,67`);
  - unreceipted checker controls (`:99-100`).
  - Its mutation sentence (`:106`) is imprecise.
- `lane/review/K2-THEOREM.r2.md` fixes all of these. Remaining minor gaps:
  - DM-1 (chronology at `:130`);
  - DM-4 (decoder pin missing);
  - DM-7 (cites the printed one-partner Lemma 10 at `:19` instead of LEMMAS).
- Other stale references: `GRAM-ENCODING.r2.md:134` → K2 r1, and `LEMMAS.md:77` → "GRAM-ENCODING.r1.md".
- None of these changes a mathematical dependency: K1 r3 states the same Theorem K1, and Gram r2's G1–G5/G4 text equals r1's. They are citation errors.
- **Recommendation.** Integrate K2-THEOREM.r2.md, with the DM fixes, as the theorem text. The replay's proof objects apply unchanged.

## 7. Acceptance conditions (T6) and the parent replay outcome
- **Required per instance.** The replay must show, for each of the 294 (encoder, i):
  - the CNF was regenerated from the frozen encoder;
  - its SHA-256 equals the producer receipt's `cnf_sha256`;
  - the class key equals class-file line i;
  - a parent-controlled checker printed exactly `s VERIFIED` (rc 0) on that exact CNF, with solver rc 20 and no safety stop.
- **Replay result.** Parent notice at 2026-10-18 ~00:00: `moqls7-k2-parent-v1/RESULT.r2.json` (`5362d6d276927ecb0ced699ea3152157ad145494ea3958dbf99c3c886a898766`) reports 294/294 PASS, 294 CNF-hash matches, 0 FAIL, 0 UNKNOWN.
  - The checker is the parent-built drat-trim (`a46c0c71…`); solvers are pinned by absolute path and binary hash.
  - Its 14 controls include SAT-plus-empty-clause and original-proof-versus-mutated-CNF rejections.
- **Desk static re-check.** `desk/replay-static-check.py` (`fd976306…067e`) wrote `desk/replay-static-check.json` (`e0873b9f…c445`). All 294 final receipts pass 13 checks:
  - key = class-file line i;
  - regenerated CNF = producer r4 CNF hash;
  - native logs re-hash to their receipt-bound values;
  - each checker log has exactly `s VERIFIED`, and its parsed formula dimensions equal the CNF header;
  - each solver log says `s UNSATISFIABLE`;
  - the checker path is the parent drat-trim and the solver paths are pinned.
  - Runs: v1 182 final, v2 111, v3 1.
- **Evidentiary limit.** Per `provenance-v1.json` (`016efb81…eb68`), the 182 final v1 receipts (A 0–146 and B 0–33, 35) have no run-time hash of the replay wrapper scripts.
  - For those receipts, acceptance rests on receipt content, hash-bound native logs showing exact status and matching parse dimensions, and agreement of the regenerated CNF with the producer's independently hashed r4 CNF. Unchanged pipeline code is an edit-log account, not observed script identity.
  - Hash-observed replays (v2/v3) exist for B only, for 112 classes (34, 36–146).
  - **35 classes (0–33, 35) have no hash-observed parent replay for either encoder.** Each still has four independent `s VERIFIED` observations: A and B, producer and parent, on two checker builds and two solvers.
  - Wrapper misreporting is excluded by the re-hashed native logs. A wrapper that fed the checker a different formula with the same dimensions is excluded only by the stated code account, not cryptographically.
- **Desk assessment.** For a computer-assisted K2 acceptance this caveat is non-blocking if it is stated verbatim. If the parent required observed script identity for every class, the minimal unobserved set is 35 classes × 1 encoder. Per the parent instruction, no rerun is proposed and no hash is backfilled.

## 8. Desk findings
DM-1 to DM-8 are in `desk/finding-map-v2.md`: seven MINOR and one cosmetic. Two of them, chronology (DM-1) and the protocol deviation (DM-2), should be fixed before integration. No FATAL or MAJOR finding.

## 9. Not checked by the desk
- Any solver or checker run. Nothing was rerun.
- Proof bytes. They were streamed and never retained.
- SAT models of the controls.
- Run-time solver binaries for the producer r4 receipts. They are bound only by command name, and not needed for soundness.
- The producer checker's binary-to-source binding.
- K3. Out of scope.
