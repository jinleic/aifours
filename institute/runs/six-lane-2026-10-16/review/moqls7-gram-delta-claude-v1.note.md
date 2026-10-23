DISPOSITION: ACCEPT-WITH-FIXES

**Abbreviations.** All paths are under `pin/`. `G2r` = `lane/review/GRAM-ENCODING.r2.md`. `K2r1`/`K2r2` = `lane/review/K2-THEOREM.r1.md` / `.r2.md`. `LEM` = `lane/review/LEMMAS.md`. `RC` = `lane/review/REVIEW-CORRECTIONS.r2.json`. `CS` = `lane/review/K2-CLASSIFICATION-SOURCE.r1.json`. `DD2/DD3/DD4` = `lane/review/CERTIFY-DRIVER-DELTA.r{2,3,4}.json`. `R4` = `lane/code/gram_certify_r4.py`. `EA`/`EB` = `lane/code/gram_enc.py` / `gram_encB.py`. `RCTL` = `lane/code/gram_review_controls.py`. `LS` = `parent/moqls7-ls147-parent-v1/REPORT.md`. `KV` = `parent/moqls7-k1-parent-verdict.md`.

## FATAL
none.

## MAJOR

**MAJOR-1 — misdated control request in the candidate theorem (K2r2:130).**
- **Problem.** The sentence "After K2 production, the static reviews requested additional matched controls" is false for the Codex review.
  - Codex asked for these controls "before production under README.md:91" (`parent/moqls7-gram-review-codex-v1.note.md:25`).
  - Its note was returned at 19:16:11 (DIGEST:D-58), 897.6 s before the first K2 certificate at 19:31:09 (DIGEST:D-62, D-87).
  - The driver deltas frozen at 19:28–19:30:55 (DIGEST:D-59..61) implement Codex MAJOR-2/3 items: caps, file logs, SHA bindings and strict gating. So production evidently began after the Codex note, without its requested controls.
  - Only the Claude v2 request (20:24:51, DIGEST:D-72) post-dates production.
  - The sentence therefore misdates the request and hides a protocol choice.
- **Impact.** None on soundness. The 26 controls test the identical frozen bytes; soundness rests on the static bridge plus the replay.
- **Correction** (new overlay; r2 bytes kept): "The Codex static review, returned 19:16:11 PDT before production began at 19:31:09, requested these controls before production; production proceeded without them. The Claude review (20:24:51) added further requests. The 26 controls ran 21:24:52–21:25:09, after all 294 certificates; they are not preregistration." If the Codex note reached the producer only later, state that relay time instead.

## MINOR

**MINOR-1 — stale pointer to K2 r1 (G2r:134-135).**
- **Problem.** G2r names `K2-THEOREM.r1.md` as the text that "states the candidate theorem". r1 still depends on K1 r2 and GRAM r1 (K2r1:16, :27). It also asserts unbound solver versions (K2r1:63, :67) and unreceipted checker controls (K2r1:99-100).
- **Correction.** Add an erratum pointing to K2r2 (a73a9007…) or its successor.

**MINOR-2 — scope of the transport controls is unstated (K2r2:112-117; G2r:165-170).**
- **Problem.** Both passages place the transport controls beside the r4 K2 evidence.
  - These controls exercised `proof_stream.py` aa0d5a0b… (DIGEST:D-43) at 21:38, prospectively for K3 (DIGEST:D-79..81).
  - With r4 they share only checker binary 111b0405 and `-i` stdin mode.
  - The evidence for the r4 path itself is the 294 positive runs plus the r3 `s NOT VERIFIED` (DD4:4).
- **Correction.** State exactly this.

**MINOR-3 — "pre-production driver revisions" (K2r2:141).**
- **Problem.** The r2 and r3 runs were failed first-batch production attempts on k2A:0 (DD3:4, DD4:4).
- **Correction.** Write "failed first-batch production attempts; no certificate accepted".

**MINOR-4 — transport wording is incomplete (K2r2:12-14).**
- **Problem.** "Unchanged under any permutation of the 49 points" covers only the tensor condition. The ONB-line conditions need a net isomorphism. Non-classicality and heaviness need the further fact that each square's entry set is unchanged.
- **Correction.** Add the content of LS:77-80.

**MINOR-5 — frozen unversioned references now resolve to a post-production text (RC:9).**
- **Problem.** RC:9 says that `GRAM-ENCODING.md`, written at 21:40:59 (DIGEST:D-82), "resolves" the unversioned references in EA:6 and EB:4. At freeze and during production, the proof text was r1 6724528a (DD2:4, DD3:14).
- **Correction.** State that the frozen references denote r1, and that the unversioned file is a post-production copy of r2.

**MINOR-6 — shared scratch path (R4:106, :119); producer-evidence integrity only.**
- **Problem.** The CNF and L scratch paths are fixed and non-exclusive.
  - The CNF is hashed at R4:128, then reopened by path by the solver (R4:137) and the checker (R4:142).
  - If two driver processes overlapped, `cnf_sha256` need not bind the bytes actually checked.
  - The A and B spans overlap from 19:31:45 to 19:39:46 (DIGEST:D-6, D-7), and D-5 records "same scratch path".
  - Zero failures make actual concurrency improbable: collisions would almost surely have caused `NOT VERIFIED`.
- **Correction.**
  - The parent checks pairwise disjointness of all 294 receipt intervals.
  - If any intervals overlap, correct K2r2:96-98 and K2r2:104-105, and treat the producer receipts as non-binding.
  - The replay is unaffected.

**MINOR-7 — control table cites exploration files (G2r:98).**
- **Problem.** G2r:98 cites `explore/gram/*_v1.json`.
- **Correction.** Cite `evidence/gram/gram_controls{A,B}_frozen.json` (a876bea8…, 6c15ef28…), as K2r2:120-126 already does.

**MINOR-8 — "K1 section 8" is unversioned (G2r:26, :65; LEM:69, :77).**
- **Problem.** These lines do not say which K1 version's section 8 is meant.
- **Correction.** Name the version. Section 8 exists in r1/r2 per DD4:15. Cosmetic.

## T1 — old findings

| id | status | new evidence | reason |
|---|---|---|---|
| Codex MAJOR-1 | RESOLVED | G2r:73-87; CS:8-19; LS:3-9,26-39 | Coverage now rests on parent-validated keys, \|Par\| and union (16942080), plus pinned EW Table 6 LF754 and Thm 3.2. Producer binary provenance is moot. |
| Codex MAJOR-2 | RESOLVED | R4:150-160,180-184; DIGEST:D-8,D-9,D-52..54 | Receipts pin both encoders, driver, decoder, classfile, and checker binary plus source. Key = classfile SHA + index + pinned parse. Frozen-control rerun ran at 19:06, before production, and is linked by identical encoder SHAs. K3 out of scope. |
| Codex MAJOR-3 | PARTIAL | R4:60-84,103,112,136-149; G2r:155-157 | Caps, file logs (no backpressure), strict gating and SAT models in logs are fixed. R4:141 `open(fifo)` still blocks forever if the solver never opens its proof; fixed only prospectively. Liveness only. |
| Codex MAJOR-4 | PARTIAL | RCTL:105-119; G2r:108-124; DIGEST:D-17..42,D-73 | Every requested control now exists on the frozen bytes and passes. "Before production" can never be met: they ran 72 min after. Chronology only. |
| Codex MINOR-1 | RESOLVED-BY-DOMAIN | G2r:26-27,63-65; LEM:69-78; RC:25 | Docstring unchanged; overlay gives the K1 + Lemma 10 argument; no code dependence. |
| Codex MINOR-2 | RESOLVED | G2r:30-34 | Conjugate-linearity, G(p,p)=1, Hermitian symmetry and symmetric off-diagonal support are stated. |
| Codex MINOR-3 | RESOLVED-BY-DOMAIN | G2r:3-6; RC:9 | Status and sentence fixed in the overlay; frozen bytes kept (see MINOR-5). |
| Codex MINOR-4 | RESOLVED-BY-DOMAIN | G2r:141-152; R4:97-112 | Branch is unreachable in production (T2). |
| Codex MINOR-5 | PARTIAL | RC:12 | Fix asserted in K1 r3. Neither K1 r3 nor README.md:7 is inlined. Cosmetic. |
| Codex MINOR-6 | UNRESOLVED | RC:27; DIGEST:D-88 | Parent-owned manifest; D-88 shows no citation is affected. Metadata only. |
| Claude MAJOR-1 | RESOLVED | G2r:73-87; CS:8-19; LS:11-39,64-73 | Normalisation/free-action proof written; both constants pinned; every key, \|Par\| and the union independently checked, so no rebuild is needed. |
| Claude MAJOR-2 | PARTIAL | R4:103,112,142,147-149,180-184; K2r2:75-77 | (a),(b),(d) fixed. (c): code, classfile and checker hashes added, but solver binaries are unbound and drat-trim 111b0405 is not build-linked to d834b649. (e): R4:141 hang remains. Provenance and liveness only. |
| Claude MAJOR-3 | RESOLVED | RCTL:84-119,163-164; DIGEST:D-17..49; G2r:106-107,125-126 | (i)–(iv) are present on the frozen bytes with hashes. (v) exists on the new transport with the same checker binary. GC4 relabelled G5-only; QLS4 declared unmatched. |
| Claude MINOR-1 | RESOLVED-BY-DOMAIN | G2r:26-27,65; LEM:69-78 | As Codex MINOR-1. |
| Claude MINOR-2 | RESOLVED-BY-DOMAIN | G2r:3-6; RC:9 | Fixed in the overlay; caveat in MINOR-5. |
| Claude MINOR-3 | RESOLVED-BY-DOMAIN | G2r:141-147; R4:97-112 | Verified in T2. Production CNFs were not scanned; the scan is added in T6. |
| Claude MINOR-4 | RESOLVED-BY-DOMAIN | R4:104-111; RCTL:56 | fix-json is never passed in production; the harness validates G1. |
| Claude MINOR-5 | RESOLVED | R4:89-96,146-149 | Unknown and malformed IDs are rejected. `strip()` is benign under exact-line match. |
| Claude MINOR-6 | PARTIAL | G2r:98-104,129,136-138; K2r2:119-128 | Runtimes removed; screens labelled exploratory. The table still cites `explore/` (MINOR-7). |
| Claude MINOR-7 | RESOLVED | G2r:43-44,61-62,68-70; LEM:75-78 | Wording repaired; the K2→K3 dependence is stated. |
| Claude MINOR-8 | RESOLVED | G2r:9-12 | Full SHAs for every K2 dependency. The abbreviations at G2r:15-16 are K3-only. |

**Are all previous MAJORs resolved? No.** What remains:
- **Codex MAJOR-3 / Claude MAJOR-2.** R4:141 still blocks forever on `open(fifo)` if the solver never opens its proof (liveness). Solver binaries are unbound, and the drat-trim binary is not build-linked to its source (provenance).
- **Codex MAJOR-4.** The controls exist but post-date production (chronology).

None of these affects soundness. The only soundness-relevant MAJORs (class coverage) are RESOLVED. A parent replay with a parent-built checker discharges the provenance residue.

## T2 — production domain: VALIDATED

**Production calls (R4:97-112).**
- k2A: `build(2,L,True,False,None)`.
- k3A: `build(3,None,True,True,None)`.
- k2B: `--squares 2 --net-L --heavy`.
- k3B: `--squares 3 --heavy --sym`.

So `fix` is never passed, which disposes of (c), and `sym` occurs only with L absent.

Every L is Latin (LS:5; decoded at R4:94; I hand-decoded D-10..12).

**Net geometry.**
- In a 3-net, a point p∉ℓ is collinear with exactly two points of ℓ. The line through p in ℓ's own class is disjoint from ℓ. Each of the other two lines meets ℓ once, at distinct points, otherwise p would share two lines with that point. So there are 5 candidates.
- In a 2-net there is one collinear point, so 6 candidates.

**(a) and (b), G2.** The common candidate set has |N(p)∩N(q)| ≥ 5+5−7 = 3, respectively 6+6−7 = 5. So `counter2` always returns s2≠None. EB:151 and EB:146-149 are unreachable, and the clauses at EA:96 and EA:99 are nonempty.

**G3.** Take r∈ℓ1∖ℓ2.
- If the lines are parallel, ℓ2 has 7 points minus 2 (resp. 1) collinear ones: 5 (6) candidates.
- If they meet at s, ℓ2∖{s} has 6 points. r is collinear with s and with exactly one more point (3-net) or none (2-net): 5 (6) candidates.
- So EA:106 and EB:168-169 never emit an empty clause.

**G4.** There are 5 (6) ≥ 3 candidates. EA:47-49, EA:132-133 and EB:63-65 are never reached, and the disjunctions at EA:137 and EB:202 each have 42 literals.

**sym.** (1,0) is not collinear with (0,1), (0,2) or (0,3) in the 2-net, so EA:125 and EB:193 receive variables.

**Conclusion.** There is no production counterexample.

**General-API hazards, context only.**
- Combining `sym` with a net yields `None`.
- EB:213-215 silently drops collinear pairs.
- A non-Latin L can produce empty clauses.

## T3 — complete K2 bridge

**(i) Straightening L and (C1).**
- LEM:9-14: entry phases plus a global unitary on L alone turn L into standard-basis labels.
- ONB rows and columns force each label to appear once per row and column, so L is a Latin square.
- Tensor inner products factor, so orthogonality is preserved.
- (C1), LEM:16-21 and K2r2:11-13: Ψ_a ⊥ L iff every symbol line of L is an ONB for Ψ_a. ✓

**(ii) Transport to a representative.**
- Every Latin square is isotopic to a reduced one, and LS:32-39 gives coverage of all reduced squares.
- A paratopism is a 3-net isomorphism σ. Define Ψ'_a = Ψ_a∘σ⁻¹ for both squares.
  - The image rows and columns are old ONB lines, so the QLS axioms hold.
  - The image symbol lines are old ONB lines, so Ψ'_a ⊥ R by (C1).
  - The product-vector family is only reindexed, so tensor orthogonality holds.
  - Each entry set is unchanged, so non-classicality and heaviness are preserved.
- ✓ The only defect is wording (MINOR-4).

**(iii) Necessary conditions, hand-checked.**
- **G1:** holds on every ONB line.
- **G2:** follows from ψ_p = Σ_r G(r,p)ψ_r.
- **G3:** By G1, U[s,q] = U[r,s] = 0, so U = 1 ⊕ (6×6 unitary). Each row has unit norm and so a nonzero entry. If |U[r,q]| = 1, column q has no other nonzero entry.
- **G5:** follows from the factorization of the tensor inner product.
- **G4** (K2r2:16-23, LEM:54-67):
  - Suppose all entries have weight ≤ 2. If x has support {a,b} and y ⊥ x has weight ≤ 2 with a different support, the supports are disjoint, since a one-coordinate overlap leaves a single nonzero term.
  - Hence U⊕I preserves every zero inner product. No support grows, and the number of weight-2 entries strictly falls.
  - Every required zero product keeps its zero factor for all partners simultaneously. V⁻¹ restores the arbitrary ONB.
  - This yields {V⁻¹Ψ'', Ψ_other, L} with exactly one non-classical member, contradicting accepted K1 (KV:5).
  - The own-line weight of p∉ℓ equals its number of neighbours on ℓ, so G4 applies on all 21 lines for both squares.
  - No circularity: K1 does not use K2.

**(iv) Satisfying assignments of both CNFs.**
- **Encoder A:**
  - h is a full AND (EA:83-85).
  - G2 at EA:96 and :99, G3 at EA:106 and :114, G5 at EA:118.
  - G4 uses w := [≥3 of nb] with the (n−2)-subset clauses at EA:136-137.
- **Encoder B:**
  - m is a full AND (EB:134), and `counter2` uses full equivalences (EB:50-55).
  - G2 at EB:148-157, G3 at EB:172 and :183, G5 at EB:187.
  - `counter_ge3` is one-directional. Setting each prefix variable to its true value and t := [≥3] satisfies EB:73-88 and EB:202.
- Every real configuration therefore extends to a model of both CNFs. ✓

**(v) Decoding and coverage.**
- R4:185-186 collects the nonempty lines; R4:94 decodes `rows[i][0]` via k2_classes.py:22-33, the same convention as LS:83-84.
- D-10 decodes to L[i][j] = i+j mod 7; D-11 and D-12 are Latin.
- Coverage: D-6 and D-7 show indices 0–146, with 147 distinct CNF hashes per encoder.

**Unstated assumptions.**
- The class file has exactly 147 nonempty lines whose first fields are the LS147 keys.
- The proofs are valid.

Both are moved to T6. I found no mathematical gap.

## T4 — references

**Stale references.**
- **K2r1:16 (K1 r2; accepted text is r3, KV:23).** Changes a dependency, since r2 is an unaccepted proof text. Fixed at K2r2:16.
- **K2r1:27 (GRAM r1).** Effectively cosmetic: K2r1 §1 already inlines the all-partners argument. Fixed at K2r2:27.
- **G2r:134 (K2r1; MINOR-1).** Cosmetic for the mathematics, but misdirects readers to withdrawn evidence.
- **CS:3 (`addendum_to` K2r1).** Cosmetic.
- **LEM:77 (G4 "in GRAM-ENCODING.r1.md").** Correct as a pointer to the frozen G4 condition.
- **Unversioned "K1 section 8" (MINOR-8).** Cosmetic.
- **Frozen EA:6, EA:15 and EB:4.** Corrected by the overlay; see MINOR-5.
- **`code/gram_cert_summary.py` (K2r2:93).** Unpinned. Cosmetic; it is an inventory reader only.

**Correct references.** All of the following agree with D-8, the inlined file headers and KV:
- K2r2:16, 27, 44-48, 56, 68-73, 88-91, 101-102, 107-108, 120-126, 132-133.
- G2r:5, 9-12, 71-72, 79-81, 132-133.

None of the stale references alters a K2 dependency once K2r2 is the integrated text.

## T5 — chronology

**Verified.**
- The 26 controls ran 21:24:52–21:25:09, after the last K2 certificate at 20:12:37 (D-68, D-73..75; gap 4335 s, D-87).
- transport_controls_r2 ran 21:38:40–43 on `proof_stream.py`, 37 s before the K3 driver delta was frozen (D-43, D-79..81).
- The frozen-code reruns at 19:06 precede production (D-53/54, D-62), so G2r:106-108 is correct.
- Deltas r2–r4 precede the first certificate (D-59..62), so G2r:13-14 is correct.
- LEM:3-4 and G2r:6 are correct (D-77, D-84).
- The non-preregistration statements are correct: G2r:124, K2r2:117, K2r2:131, RC:21, RCTL:8, RCTL:182.
- No text claims that either control set preceded K2.

**Flagged.**
- K2r2:130 (MAJOR-1).
- K2r2:113-117 and G2r:165-170 (MINOR-2): ambiguous, not misdated.
- K2r2:141 (MINOR-3).
- RC:9 (MINOR-5).
- K2r2:104-105, pending the interval check (MINOR-6).

## T6 — acceptance conditions

For each E ∈ {A, B} and i ∈ 0..146:

1. **Class file binding.**
   - The class file SHA is 898065c8…8158.
   - `rows = [l.split() for l in f if l.strip()]` has length 147.
   - key_i = rows[i][0] is a 36-digit member of the LS147-validated key set, and the 147 keys are distinct.
   - R_i = square_from_key(key_i), using k2_classes.py b49099e4…, is Latin.
2. **Pins.** Encoder, driver and decoder pins equal D-8.
3. **CNF regeneration.**
   - A: `build(2,R_i,True,False,None).text()`.
   - B: `--squares 2 --net-L json(R_i) --heavy`, with no `--sym` and no `--fix-json`.
   - The regenerated SHA-256 equals the receipt's `cnf_sha256` and the matching summary row (31aa7eb2… / ed29e3a1…). Record the interpreter version.
4. **Structural scan.**
   - The DIMACS header clause count equals the number of clause lines.
   - There is no `None` token and no empty clause, and every |literal| ≤ V.
5. **Proof replay.**
   - Run a parent-controlled solver on those exact bytes at a unique per-instance path.
   - Feed the proof to a parent-built checker from source d834b649…, recording compiler, flags and binary hash.
   - Hash the CNF again after checking.
   - Accept only if solver rc is 20, checker rc is 0, the only status line is exactly `s VERIFIED`, and there is no TIMEOUT and no safety stop.
6. **Coverage.** All 294 instances pass. No instance is accepted on producer receipts alone.

Additional conditions:

7. Run checker controls on the replay transport:
   - one tiny UNSAT CNF must verify;
   - a truncated proof must be rejected;
   - an invalid proof on a SAT CNF must be rejected.
8. Check receipt-interval disjointness (MINOR-6). This is evidential only.
9. Integrate K2r2 with the fixes above, and state K1 r3 and LS147 as explicit premises.
10. Recommended, not required: recheck one encoder's 147 instances with an independent, preferably verified, LRAT checker.

## Scope

This review was static only. I read every inlined file and checked by hand:
- the clause semantics and auxiliary-variable extensions of both encoders;
- the 3-net and 2-net candidate counts;
- the G2/G3 algebra and the Lemma 10 replacement;
- the EW factor 7!·7·3·2 = 211680;
- three class-key decodings;
- the control-fixture arithmetic: m0 = 2, M0 = {2,6}, neighbours of (1,0) = columns {1,2,3,5,6}, the 1↔4 swap, the i↦4i map and the conjugate map;
- every chronology statement against the digest.

I did not see or check:
- the receipts, logs, CNFs or class file beyond D-10..12;
- the K1 texts, the GRAM r1 text, `proof_stream.py`, README.md:7 or the K3 materials;
- solver and checker behaviour, or the receipt intervals.

Proof validity is a stated condition. I treated the digest as mechanical fact.
