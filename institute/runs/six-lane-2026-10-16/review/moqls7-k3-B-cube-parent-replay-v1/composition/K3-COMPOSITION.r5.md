# K3 composition note r5 (phys-2, lane moqls7-maximum) — FROZEN

**Status of this file: frozen r5** `R/moqls7-k3-B-cube-parent-replay-v1/composition/K3-COMPOSITION.r5.md`, created by
exclusive create on 2026-10-18 at 12:14:21 PDT (host clock) in the parent B-replay desk at the parent's request. It is
the pre-freeze draft `composition/K3-COMPOSITION.r5.final-draft-1.md` (55335a3b…94e4), which is the lane's unfrozen
draft `L/review/drafts/K3-COMPOSITION.r5.md` (0dbaefe3…2486, written from 11:10:36 PDT) plus U17–U18. Its
placeholders were filled only from the parent's raw audit `R/moqls7-B-C311cuts-parent-audit-v1.json` (024e636d…cab9)
and the parent verdict `R/moqls7-k3-B-C311cuts-parent-verdict-v1.md` (10a65127…fbd3), and the dependent status lines
were brought in line with them (U19). The exact r4→r5 diff is `composition/K3-COMPOSITION.r4-to-r5.diff`. Full
hashes are in §6. [U17] [U19]

**r5 is a status update of r4** (`review/K3-COMPOSITION.r4.md`
152e13cbd6815ba54489bdf3d62857451f51514f0b34e52b2de1a7967d777b3e). Every link statement, premise and argument is
r4's (= r3's logic). r5 refreshes the link statuses (G1, G2, H3 and the encoder-A C311+cuts verdict pinned) and adds
reference sections requested by the parent: exact A/B formulas (§12), the proof-stream boundary (§13), reused
controls and chronology (§14), the lower-bound construction (§15), all imports (§16) and the encoder-B C311+cuts
parent-replay result (§18, taken only from the parent's raw audit and verdict). The r5 fix map is §17.
Earlier fix maps: r2 §7 (Codex F1–F3), r3 §8 (Claude m1–m9), r4 §11 (S0–S10). Section numbers of r4 are kept (r4 has
no §9), so earlier references stay valid. [U0]

Statuses are those at the writing time. Later events are recorded in the lane README and LOG. [U0]

r1 was written at the parent's request: a static note giving the exact chain from the K1/K2 reduction to "no triple
with three non-classical squares", with each link's statement, files, SHA-256 and status.

**This note makes no K3 claim and no claim about M(7).** It only records which links exist and how far each one has
been accepted. Correctness, novelty and significance are separate questions; nothing here bears on priority.

Paths: `L/` = `physics/evidence/six-lane-20261016/moqls7-maximum/`; `R/` = `institute/runs/six-lane-2026-10-16/review/`.
Abbreviated hashes are expanded in §6. Every SHA-256 below was computed from the file at the writing time.

Status words:
- **ACCEPTED**: a named parent verdict or disposition accepts the statement, with that file's caveats.
- **CONDITIONALLY SOUND**: the parent adopted the mathematics, conditional on named gates.
- **PRODUCER**: a producer certificate meeting the driver predicate. That means solver rc 20, checker rc 0, exact
  status lines, the pinned input SHA and no safety stop; for C311+cuts it also needs a clean supervisor record. There
  is no parent replay yet, and a producer certificate satisfies no gate.
- **RUNNING**, **PENDING** (an open parent obligation), **UNKNOWN**.

## 1. Target, definitions and the case split

**D1. Definitions.**
- Statement: Ball–Simoens arXiv:2607.12933v2 §2.2–2.3 define QLS(7), orthogonality, set isotopy and classical sets.
  M(n) is the largest t such that a non-classical set of t MOQLS(n) exists (layout LF29–31).
- Files: `L/sources/quantum-latin-2607.12933v2.pdf` 2d60d45f…21afe; layout text df1d8b14…4219; lane README §0.1–0.2;
  contract `screening/phys-2-moqls7-maximum-contract.json` 21b1b38b…d372.
- Status: frozen definitions.

**D2. (C0) and the case split.**
- Statement: a set is classical iff every member is classical. So a non-classical MOQLS(7) triple has
  k ∈ {1, 2, 3} individually non-classical squares, giving the cases K1, K2 and K3.
- Files: `L/review/LEMMAS.md` §C0, 4bddc9d4…50c9.
- Status: ACCEPTED. LEMMAS.md is a claim document in both the K1 and the K2 verdicts.

**D3. Baseline.**
- Statement: 2 ≤ M(7) ≤ 3. Every set of four MOQLS(7) is classical. The lower bound comes from Ball–Simoens
  Corollary 7 (or Huang–Li Theorem 5.2).
- Files: `R/moqls7-parent-verdict.md` a39911fd…3ff2.
- Status: ACCEPTED.

## 2. The chain

The parent's decision 8 (`R/moqls7-amendment4-parent-disposition-v1.md` 3c9373c0…4e44), restated in
AMENDMENT-4.r4 §8:

> K1 ∧ K2 ⇒ (minimality) G4 on all own lines ⇒ `--sym` WLOG ⇒ three cubes C311, C321, C411 ⇒ {C321, C411 excluded
> on A and B (G1, G2); transport ⇒ cuts; C311 + cuts certified UNSAT on A and on B} ⇒ no K3 triple,

including the encoder instantiation (H3) and the lex-representative step.

### Link 1 (K1)
- Statement: no MOQLS(7) triple has exactly one non-classical square.
- Files:
  - `L/review/K1-THEOREM.r3.md` 2d77c637…a096;
  - verdict `R/moqls7-k1-parent-verdict.md` 1cd0603c…dfb8;
  - lane record `L/evidence/PARENT-K1-ACCEPTANCE-2356.json` 543677ad…596a.
- Status: **ACCEPTED** (computer-assisted).

### Link 2 (K2)
- Statement: no MOQLS(7) triple has exactly two non-classical squares. With K1, every MOQLS(7) triple is either
  classical or has three non-classical squares (K2 verdict, line 6).
- Files: `L/review/K2-THEOREM.r2.md` a73a9007…32cd; verdict `R/moqls7-k2-parent-verdict.md` 25ecb6ba…1242.
- Status: **ACCEPTED**: CORRECTNESS-ACCEPTED, computer-assisted, subject to the verdict's trust base and its 35-class
  provenance caveat.

### Link 3 (minimality ⇒ G4)
- Statement:
  - Minimise the number m of non-classical squares over all non-classical MOQLS(7) triples. K1 gives m ≥ 2.
  - A non-classical square that is light in some ONB can be classicalised by the basis-free Lemma 10, which
    preserves every partner orthogonality. That leaves a triple with m − 1 ≥ 1 non-classical squares, contradicting
    minimality.
  - Hence every non-classical square of a minimal triple is heavy in every ONB.
  - Given Links 1–2, every K3 triple is minimal. So each square has, on each of its 14 own row/column lines, an
    off-line point with at least three neighbours on that line.
- Files:
  - `L/review/GRAM-ENCODING.r2.md` §2 G4 (lines 52–65), c6c506a7…d7c6;
  - `L/review/LEMMAS.md` lines 54–78;
  - `L/review/K3-Q4-SIDECAR.r1.json` binding 3, 34bb5251…16e5;
  - `L/review/K3-ERRATA.r1.md` E6 and E8, 85fa93fa…c662.
- Status:
  - The G4 lemma and the Lemma 10 import are ACCEPTED as claim documents of the K2 verdict.
  - Their application to K3 (every K3 triple is minimal) is stated in the sidecar and in AMENDMENT-4 H2. It is named
    in decision 8, so it is **PENDING** in the composition review.

### Link 4 (Gram necessary conditions)
- Statement: for every quantum square of a MOQLS(7) set, the Boolean Gram supports satisfy:
  - Gram-G1: collinear pairs are zero;
  - Gram-G2: frame consistency (a count of 0 forces 0, a count of 1 forces 1);
  - Gram-G3: unitary transitions;
  - Gram-G5: for every pair of squares, g_a · g_b = 0.
- Files: `L/review/GRAM-ENCODING.r2.md` §2.
- Status:
  - **ACCEPTED** as necessary conditions (K2 verdict, role "G1–G5 necessary conditions").
  - Their instantiation in the K3 base CNFs is Link 7.

### Link 5 (`--sym` WLOG)
- Statement: by row and column permutations, transposition and relabelling of the squares, square 1 can be assumed
  heavy in the frame of row 0 at p = (1, 0), with neighbours (0,1), (0,2) and (0,3). Every condition is preserved.
- Files: `L/review/GRAM-ENCODING.r2.md` §3, K3 bullet (lines 88–92).
- Status: **ACCEPTED** within the K3 cover disposition Q1 (`R/moqls7-k3-cover-parent-disposition-v1.md`
  fbfc0e10…f369; AMENDMENT-4 H5), with the K3-ERRATA E4 wording.

### Link 6 (three-cube cover and G6)
- Statement:
  - Let S_a = {k ∈ 1..6 : g_a(p, (0,k)) = 1}. Each S_a is nonempty (Gram-G3; (0,0) is excluded by Gram-G1, erratum
    E4). The S_a are pairwise disjoint (Gram-G5), and S_1 ⊇ {1,2,3}.
  - Up to residual symmetry, exactly the cubes C311, C321 and C411 occur, and each cube fixes all 18 predicates.
  - G6 same-ray equalities are implied by Gram-G1/G2 plus the cube units.
- Files:
  - `L/review/AMENDMENT-2.r1.md` §1–2, 82ee394e…14e0; bindings 1dc0636b…16ff;
  - coverage control `L/evidence/k3cubes/coverage_r1.json` 14d00a2d…f0f3: status PASS, 18 valid assignments, three
    disjoint orbits of six, `complete_disjoint_cover` true;
  - `L/review/G6-G2-DERIVATION.r1.md` 8790e9e1…e791;
  - `L/evidence/k3cubes/g6_controls_r1.json` edd313eb…2615.
- Status:
  - Cover disposition Q1 (cover) **ACCEPTED**.
  - Q2 (G6 and variable maps) **ACCEPTED** mathematically.
  - Q2's condition was that no B-route certificate may be relied on until a runtime B-map oracle passes. It is met:
    `L/evidence/k3cubes/bmap_oracle_r1.json` 6e2bd95e…952c reports PASS, with 0 of 2646 B variables differing from
    A's map. Its pin `L/review/K3-BMAP-ORACLE.r1.json` df28f4c5…f887 was recorded before execution, and every B
    certificate below binds the oracle receipt.

### Link 7 (H3: encoder instantiation)
- Statement:
  - Every K3 triple normalised by `--sym` gives g-values that satisfy Gram-G1…G5, G4 and the `--sym` units. Its
    auxiliaries can be set as in AMENDMENT-4.r4 §8 so that every clause holds of both base CNFs,
    `gram_enc.build(3, None, True, True, None)` (encoder A) and `gram_encB.py --squares 3 --heavy --sym`
    (encoder B). [F2]
  - For encoder A, the Gram-G2 clauses contain the AND auxiliaries h. Once each h takes its defining conjunction
    g(p,r) ∧ g(q,r), those clauses hold by frame consistency (Gram-G2). This changes no auxiliary assignment and no
    CNF. [F3]
  - `--sym` alone does not yield one of the three canonical signed cube assignments. After the residual
    normalisation supplied by Link 6 (residual column permutations and the exchange of squares 2 and 3), the Gram
    values additionally satisfy the chosen cube's 18 signed units and G6. [F2]
  - No emitted clause is empty and no literal is `None` in the K3 base instantiation. In the production domain of
    `GRAM-ENCODING.r2.md` lines 141–147 (frame lines of the 2-net of rows and columns), every G2 product list has 5–6
    items, every G3 transition list has 6 candidates, and every G4 list has 6 candidates at each of the 42 off-line
    points. The degenerate branches (`gram_enc.py` lines 48, 106 and 137; `gram_encB.py` lines 65, 148, 151 with
    s2 = None, and 169) are therefore unreachable. [m7]
- Files:
  - `L/code/gram_enc.py` b2c206d8…8833;
  - `L/code/gram_encB.py` c7583efe…2b45;
  - cube wrapper `L/code/k3_cubes.py` 70c79c62…0550;
  - AMENDMENT-4.r4 §1 H3 and §8;
  - component controls `L/evidence/gram/review_controls_r1/summary.json` 6ce1ddc2…d685 (26/26).
- Status: **ACCEPTED at conditional scope** by the parent H3 verdict `R/moqls7-k3-h3-parent-verdict-v1.md`
  (edba465af496963c0cac338d4d33fbc3edd1cbc7772908a92ac8115c66eabca7, 08:06:03), on the text
  `L/review/K3-H3-INSTANTIATION.r1.md` (c3d8c05d…5cdc) read with erratum 1 (9559a54b…17b5). Scope as stated there:
  the base clause families, cube units and G6 hold for genuine normalised K3 configurations; the A-route H_311-orbit
  minimum satisfies the lex comparisons; the cuts follow only under G1–G2. It is not a K3, M(7) or certificate
  verdict. [S1]

### Link 8 (gate G1: C321 excluded on A and B)
- **A_C321** (d598507d…8388): **ACCEPTED UNSAT**.
  - Verdict `R/moqls7-k3-A-cubes-parent-verdict-v1.md` 0ba3fe4f…1f97.
  - Parent replay receipt cbd7f02f…efa8; audit `R/moqls7-k3-A-parent-receipt-audit-v1.json` 97c1e0e4…c234.
  - Producer receipt `L/evidence/k3cubes/cert_r2/A_C321.json` c3a30df3…9314.
- **B_C321** (8b7b8124…12c6): **ACCEPTED UNSAT** (parent replay PASS). [U1]
  - Parent replay B_C321-a3 **PASS**: RESULT `R/moqls7-k3-B-cube-parent-replay-v1/RESULT.B_C321-a3.json`
    4c0845ee…db9f, receipt `receipts/B_C321-a3.json` 0ba46296…b0c4, report 174255cf…8887, deviations 9bc2e569…d707.
    kissat 4.0.4 rc 20 with exactly ['s UNSATISFIABLE'] (2454 s); parent drat-trim a46c0c71…8e37 rc 0 with exactly
    ['s VERIFIED']; pipeline 4248.6 s; supervisor clean; both feeds measured complete with SHA equal to the pin.
  - Producer certificate (evidence only): `L/evidence/k3cubes/cert_B_r6/B_C321.json` 2ffc2fa8…32ac, rc 20/0,
    ["s VERIFIED"], 4035.475 s; driver `k3_direct_B_r6.py` 24fcfea8…c44d; delta r6 5beb6009…1eb8.
  - Non-contributing UNKNOWN attempts: producer r4 and r5; desk first attempt and a2b (§10).
- **Gate G1**: **ACCEPTED** by `R/moqls7-k3-G1-parent-verdict-v1.md`
  (639fbf6bfa1395ad575eef96ee2ea4715a6cba7283cdb4d79c5c4bb0e5cfb47f, 08:36:51), naming A_C321 d598507d…8388 and
  B_C321 8b7b8124…12c6. Scope: both exact C321 cube CNFs are UNSAT; that no genuine K3 triple normalises into C321
  also needs Links 3, 5–7, reconciled in the final composition verdict. [U1]

### Link 9 (gate G2: C411 excluded on A and B)
- **A_C411** (2b92f5b1…ddf2): **ACCEPTED UNSAT**.
  - Same verdict; parent replay receipt 308e255e…7442.
  - Producer receipt `cert_r2/A_C411.json` 5f117b60…a23cf.
- **B_C411** (01acf464…8bf8): **ACCEPTED UNSAT** (parent replay PASS). [U2]
  - Parent replay B_C411-p3 **PASS**: RESULT `RESULT.B_C411-p3.json` e1ef46d1…89f0, receipt `receipts/B_C411-p3.json`
    c176b738…0ab1, parent raw audit `R/moqls7-B-C411-parent-audit-v1.json` 9850fd8b…0e12; regenerated CNF
    31,379,006 B, `p cnf 461370 1629802`; kissat 4.0.4 rc 20, parent drat-trim rc 0, singleton exact statuses;
    pipeline 09:44:03–10:53:35, 4,172.606 s; checker consumed 1,072,845,839 proof bytes.
  - Producer certificate (evidence only): `L/evidence/k3cubes/cert_B_r7/B_C411.json` 644b5b23…6f75, rc 20/0,
    ["s VERIFIED"], solver log "s UNSATISFIABLE", 4181.588 s; driver `k3_direct_B_r7.py` 386bff0c…4cfa; delta r7
    55b40519…ade4.
  - Non-contributing: producer r5 and r6 UNKNOWN; desk B_C411-p1 UNKNOWN (external SIGTERM); desk B_C411-p2
    NOT_STARTED (disarmed) (§10).
- **Gate G2**: **ACCEPTED** by `R/moqls7-k3-G2-parent-verdict-v1.md`
  (d41253f6473ef78df1fa9272363674e5c90c5a0f90616c3a0d0129470e067aa7, 10:57:25), naming A_C411 2b92f5b1…ddf2 and
  B_C411 01acf464…8bf8, at formula-level scope. [U2]

### Link 10 (transport ⇒ cuts)
- Statement (AMENDMENT-4.r4 §3–§4):
  - Take any own row/column frame ℓ and any off-line point p.
  - A local type (4,1,1) maps, by transposition, row and column relabelling and square relabelling, to a K3 triple
    that satisfies every clause of A_C411 and of B_C411. That contradicts G2. The image is a K3 triple: the maps keep
    the QLS axioms and mutual orthogonality, and as cell permutations (transposition included) they leave each
    square's ray set unchanged, hence its individual non-classicality (`LEMMAS.md` lines 9–11). [m4]
  - A type (3,2,1) maps likewise into A_C321 and B_C321, contradicting G1.
  - So under H1–H5 and G1–G2 every heavy local type is (3,1,1), and the 238,140 cut clauses hold for every K3
    configuration: 26,460 at-most-three clauses and 211,680 mixed clauses, block 05f31da4…e6dd.
- Files:
  - `L/review/AMENDMENT-4.r4.md` 75ac7aec…9a91 (frozen) and delta r5 75f8c382…b6e2;
  - generator r1 `code/k3_cuts_r1.py` 0ec92c86…1b0a, with receipt 9cfc0e81…babbf and pin record 4c23ec44…5dd3;
  - generator r6 `code/k3_cuts_r6.py` d0fc540e…b1aa, with receipt `cuts_r6_receipt.json` 9624d612…4a24. Its
    controls: C1 rejects exactly 450 of 2100 local assignments (90 of type (4,1,1), 360 of type (3,2,1)); the five
    classical AG(2,7) triples give 0 violations on the cut clauses; C4 checks lex compatibility; the Ψ(f)
    non-vacuity check gives (2940, 0);
  - appender controls r5 `cuts_cert_controls_r5.json` bb9445a2…b3e3;
  - supervisor controls r3 `supervise_controls_r3.json` 3c77be50…99de.
- Status: **CONDITIONALLY SOUND**.
  - AMENDMENT-4 disposition 3c9373c0…4e44, with the header erratum effec3db…b148.
  - The cuts are derived conditional clauses, not definition-level necessary conditions (decision 2, the
    README:91 ruling).
  - Condition: G1 and G2 ACCEPTED (Links 8–9), together with Links 3 and 7. The transport images satisfy the exact
    C321/C411 CNFs only through G4 on the image (Link 3) and the encoder instantiation (Link 7); AMENDMENT-4.r4 §3
    states this as "under H1–H5". [m3]
  - At the r5 writing time G1 (639fbf6b…b47f) and G2 (d41253f6…7aa7) are ACCEPTED and Link 7 is ACCEPTED at
    conditional scope (H3 verdict edba465a…abca7, which states that the cuts follow only under G1–G2). The remaining
    reconciliation (Link 3 applied to K3, and the transport itself) is part of the final composition verdict. [U3]

### Link 11 (lex representative, A route only)
- Statement:
  - Let H_311 = ⟨generators("C311")⟩ be the group generated by the seven C311 generators of AMENDMENT-3.r1 §1: row
    swaps (2,3), (3,4), (4,5), (5,6); column swaps (1,2), (2,3); and column swap 4/5 combined with the exchange of
    square labels 2/3. [F1]
  - The lex-minimal member of each H_311-orbit satisfies X ≤lex X∘σ for every generator (errata E2/E3). [F1]
  - The generator lists are cube-specific: 7 for C311, 7 for C321 and 8 for C411, 22 in all. Each cube's own listed
    generators preserve the g-projection of that cube's base ∧ cube conjunction. For example, C321's plain column
    swap 4/5 would violate C311's signed units. [F1]
  - The C311 generators also preserve the cuts. The cut family is indexed uniformly by frame, off-line point,
    square(s) and subsets, so every row/column permutation and square relabelling maps it onto itself; C4 checked this
    for all 22 generators and transposition. Independently, Link 10 gives the cuts for every K3 configuration,
    including every orbit member. [F1, m5]
  - Comparator lemma, any length. [m6] Fix a generator σ. Let v_1 < … < v_n be the indices with σ(v) ≠ v, let
    x_i = X_{v_i} and y_i = X_{σ(v_i)}, and let e_1 ≡ true. `k3_lex.lex_clauses` (`k3_lex.py` lines 55–69) emits
    C_i = ¬e_i ∨ ¬x_i ∨ y_i for i ≤ n, and D_i = ¬e_i ∨ ¬x_i ∨ ¬y_i ∨ e_{i+1} and D′_i = ¬e_i ∨ x_i ∨ y_i ∨ e_{i+1}
    for i < n. Some assignment to the e satisfies these clauses iff x ≤lex y.
    - (⇐) Set e_i := [x_k = y_k for all k < i]. Whenever e_i ∧ (x_i = y_i) holds, e_{i+1} is true, so D_i and D′_i
      hold. If e_i is true then i ≤ j, the first differing position (if any), so x_i ≤ y_i and C_i holds.
    - (⇒) If the first difference j has x_j = 1 and y_j = 0, then D/D′ force e_1, …, e_j true by induction, and C_j
      fails.
    - Positions fixed by σ are equal in X and X∘σ, so skipping them does not change the comparison. Each generator
      gets fresh prefix variables (`k3_lex.py` lines 118–121), so the comparators are independent.
- Files:
  - `L/review/AMENDMENT-3.r1.md` 374978c6…f3cc and bindings 0d842cf8…0316;
  - `L/code/k3_lex.py` 2b721e85…9b10;
  - `L/evidence/k3cubes/lex_controls_r1.json` 3bd546ad…4053: predicate bijections, 18 cube units preserved, and
    comparator truth tables up to length 4;
  - sidecar binding 1: A lex C311 059be616…8c4f, metadata 7bef0b78…190d, source cube 7fca33f1…2001 / 3b2ab04f…d9ed.
- Status:
  - Cover disposition Q3 **ACCEPTED** mathematically, with the text fixes E2 and E3.
  - The general-length comparator argument is written out above. Both static audits accept it (Codex 5a68a20d…47bf;
    Claude 786f3438…78e1), and the parent H3 verdict (edba465a…abca7) accepts, within its conditional scope, that the
    minimum of the finite H_311 orbit satisfies the lex comparisons after auxiliary reconstruction. Acceptance of the
    composition itself remains **PENDING**. The length-≤4 control (`lex_controls_r1.json`) is corroboration only. [S4]

### Link 12 (C311 + cuts on encoder A)
- Input: lex C311 059be616…8c4f plus the block, giving strengthened input 18583aab…2e5e (24,477,803 B, header
  107513/897308). Solver CaDiCaL 3.0.1 (601c9fa8…d1fa); checker drat-trim 111b0405…d5e4.
- Attempts:
  1. UNKNOWN: free-space floor at 04:09:50 (supervisor record f0311593…04d2). Non-contributing.
  2. UNKNOWN: free-space floor at 04:53:03 (driver receipt 06bd12b0…dab3, supervisor record 50a07ffd…fc87).
     Non-contributing.
  3. UNKNOWN: free-space floor at 07:04:14 (supervisor record 6cf3bd5d…0496). Non-contributing.
  4. UNKNOWN: free-space floor at 07:10:39 (supervisor record eea33007…aec6). Non-contributing.
  5. **VERIFIED_UNSAT_CASE**, 07:20:37–08:19:11, 3511.49 s, under delta r9 76f68d34…5487, driver r9 2f0ced45…77ed3 and
     supervisor r3 0ee8f394…ec4d:
     - driver receipt `L/evidence/k3cubes/C311cuts_A_r9/C311cuts_A.json` 88c154b75e9fa7acb3ec05867d0542b6be4b349c189931ad5217a4f16235f37f:
       rc 20/0, exactly ["s VERIFIED"] and ["s UNSATISFIABLE"]; both feeds 24,477,803 B with SHA 18583aab…2e5e;
     - supervisor record `C311cuts_A_r9.supervisor.json` 2fb5e03241f3d88416a04fe5c0671b15eb6b6c63329eec651f0d672458ff25b1:
       completed_cleanly true, no trip, no quarantine, leader rc 0;
     - checker log d9f86ef6…89f1: 517,255,126 proof bytes, streamed only.
- Status: exact-CNF **ACCEPTED UNSAT** by `R/moqls7-k3-A-C311cuts-parent-verdict-v1.md`
  (b18472b2aed47547f23e0c8288c9e9d7b6c25ebcbe9f9d4472626054464593a8, 11:06:26). [U4]
  - Parent replay A_C311cuts-p2 **PASS**: receipt `R/moqls7-k3-B-cube-parent-replay-v1/receipts/A_C311cuts-p2.json`
    59b27e91…69b4, RESULT `RESULT.A_C311cuts-p2.json` 51470bce…cd76, parent raw audit
    `R/moqls7-A-C311cuts-parent-audit-v1.json` 73660641…e306; formula 18583aab…2e5e, 24,477,803 B,
    `p cnf 107513 897308`; kissat 4.0.4 and the parent drat-trim (not the producer's CaDiCaL and lane checker);
    native self-exits 20/0 with singleton UNSATISFIABLE/VERIFIED lines; pipeline 09:39:16–10:58:29, 4,753.8 s;
    checker consumed 705,539,296 proof bytes; no stop, signal or quarantine.
  - The producer certificate (attempt 5 above) is evidence only. Desk A_C311cuts-p1 was disarmed before launch
    (NOT_STARTED; §10).
  - Scope (verdict §"Mathematical boundary"): formula-level evidence for Link 12; using the cuts for genuine C311
    triples additionally needs G1/G2 (accepted) and the scoped transport, normalisation and encoder-necessity
    lemmas, reconciled in the final composition verdict.

### Link 13 (C311 + cuts on encoder B)
- Input: original B_C311 b3ec0108…c077 plus the block, giving strengthened input ae3b8309…783a (38,353,647 B, header
  461370/1867942). Solver kissat 4.0.4 (05d6f3e9…a848).
- Result: **PRODUCER**.
  - Driver receipt `L/evidence/k3cubes/C311cuts_B_r6/C311cuts_B.json` 1f003634…c535: rc 20/0, exactly
    ["s VERIFIED"] and ["s UNSATISFIABLE"]; both feeds were 38,353,647 B with SHA ae3b8309…; 4237.757 s.
  - Supervisor record `C311cuts_B_r6.supervisor.json` 43d48141…e4cb: completed_cleanly true, no trip, no quarantine,
    leader rc 0.
  - Delta r6 899a0437…0681; driver r6 12b141fd…db91.
- Status: exact-CNF **ACCEPTED UNSAT** by `R/moqls7-k3-B-C311cuts-parent-verdict-v1.md`
  (10a65127d17bb8b8df0bccb42a7722eee86e3891b15189d5279ed616660cfbd3, 12:09:07). [U5] [U19]
  - Parent replay B_C311cuts-p2 **PASS** (§18): receipt `R/moqls7-k3-B-cube-parent-replay-v1/receipts/B_C311cuts-p2.json`
    edfbb2f1…241e, RESULT `RESULT.B_C311cuts-p2.json` 45eee709…c3f5, parent raw audit
    `R/moqls7-B-C311cuts-parent-audit-v1.json` 024e636d…cab9 (PARENT_AUDIT_PASS); formula ae3b8309…783a,
    38,353,647 B, `p cnf 461370 1867942`; kissat 4.0.4 and the parent drat-trim; native self-exits 20/0 with singleton
    UNSATISFIABLE/VERIFIED lines; pipeline 10:55:09–12:05:22, 4,212.783 s; checker consumed 842,063,946 proof bytes;
    no stop, signal, quarantine or remaining owned child.
  - Desk B_C311cuts-p2 ran in slot 2 under `scripts-v14/launch_B_v14.py`: gate `receipts/B_C311cuts-p2.gate.json`
    d09b4aad…fb21, pre `receipts/B_C311cuts-p2.pre.json` 4db347d1…7c41, launch `receipts/B_C311cuts-p2.launch.json`
    78a505e3…5455; input regenerated in memory, bound to `receipts/regen-B_C311cuts.json` 1df56436…3cc0.
  - The producer certificate (Result above) is evidence only. Desk B_C311cuts-p1 ended UNKNOWN (external SIGTERM
    after solver rc 20, no checker verdict): receipt `receipts/B_C311cuts-p1.json` ae0e4654…bf18, RESULT
    `RESULT.B_C311cuts-p1.json` a74b1256…207d. Non-contributing; no retrospective upgrade.
  - With Link 12, both C311+cuts formula obligations of the A+B standard are accepted (verdict).
  - Scope (verdict §"Composition boundary"): this discharges the exact formula replay of Link 13. The cut-transfer,
    normalisation and encoder-necessity premises must be reconciled in this r5 composition and the both-family final
    reviews before any K3 or M(7) conclusion.

### Link 14 (composition)
- Statement: assume all of the following:
  - Links 1–2;
  - Links 3, 7, 10 (transport and cut derivation) and 11 accepted in the composition review; [m2]
  - Links 4–6 as accepted;
  - G1 and G2 accepted, which with Links 3 and 7 discharges the condition of Link 10; [m3]
  - Links 12–13 certified and parent-replayed.

  Then every K3 triple, after `--sym`, lies in one of the three cubes up to residual symmetry:
  - in C321 it contradicts G1;
  - in C411 it contradicts G2;
  - in C311 it satisfies the cuts (Link 10). Its lex-minimal H_311-orbit member then satisfies the strengthened A input
    (Links 7, 10, 11). The configuration itself satisfies the strengthened B input (Links 7, 10). [m1] The certified UNSAT of
    either input excludes it, and the A+B standard (decision 1) requires both.

  Hence no K3 triple exists.
- Status: **PENDING**: the final parent composition verdict (decision 8), after both final composition reviews of
  this frozen r5. The encoder-B C311+cuts verdict (10a65127…fbd3) now exists. [U6] [U19]

## 3. What M(7) would then equal, and exactly why

**If** the composition (Link 14) is accepted:
1. No MOQLS(7) triple has exactly 1, 2 or 3 non-classical squares (Links 1, 2, 14). By (C0), no non-classical
   triple of MOQLS(7) exists.
2. For t ≥ 3, a non-classical set of t MOQLS(7) would contain an individually non-classical square (C0). That square
   together with any two other members is a set of 3 MOQLS(7), because orthogonality is pairwise, and it is
   non-classical by (C0). This contradicts step 1. Hence M(7) ≤ 2.
3. The published non-classical pair (Ball–Simoens Corollary 7, or Huang–Li Theorem 5.2), cited by the accepted
   baseline verdict a39911fd…3ff2, gives M(7) ≥ 2. The explicit construction at q = 7 is written out in §15. [U7]
4. **Therefore M(7) = 2.** The baseline bound M(7) ≤ 3 is consistent with this but is not used in step 2.

Until the composition is accepted, only the baseline 2 ≤ M(7) ≤ 3 holds, with K1 and K2 as accepted partial results.

Any such conclusion inherits this trust base:
- the proofs are computer-assisted;
- CaDiCaL and kissat are untrusted proof producers; drat-trim, CPython and the compiler are trusted;
- parent replays use the parent-built drat-trim;
- there is no formal (Lean) verification;
- imported results: the Ball–Simoens definitions, including set isotopy, on which (C0) rests (`LEMMAS.md` lines
  11–13); the Ball–Simoens Lemma 10 printed proof; the published non-classical pair used in step 3 (Ball–Simoens
  Corollary 7, or Huang–Li Theorem 5.2); and the Egan–Wanless MOLS(7) tables (through K1 and K2); [m9]
- the K2 verdict's 35-class provenance caveat still applies.

## 4. Open obligations at the writing time, in dependency order [U8]

1. Done: desk B_C311cuts-p2 PASS on the strengthened encoder-B input ae3b8309…783a, parent raw audit 024e636d…cab9
   (PARENT_AUDIT_PASS) and the parent's encoder-B C311+cuts verdict 10a65127…fbd3 (exact-CNF ACCEPTED UNSAT; §18).
   [U19]
2. Freeze of r5 (this file; done by exclusive create) and both final composition reviews (Codex and Claude; open).
3. The final parent composition verdict (decision 8), covering Link 3 applied to K3, Link 10 (transport, with G1–G2
   accepted), Link 11 and Link 14. Links 7 (conditional scope), 8 (G1), 9 (G2), 12 and 13 (exact CNF) are already
   accepted.

   Only then can any K3 or M(7) verdict follow. M(7) is not claimed here.

## 5. Errata noticed while composing (frozen files unchanged)

- `AMENDMENT-4.r4.md:390` says the text "becomes usable only as the frozen `review/AMENDMENT-4.r3.md`". It should
  name `review/AMENDMENT-4.r4.md`, as lines 3–5 of the same file do. The r4 freeze (byte-identical `cp -n`, together
  with delta r5) is recorded in the lane LOG at 03:35.
- `AMENDMENT-4.r4.md:224` names route directories `C311cuts_<route>_r5` and `:343` says "one attempt per route under
  this delta". Attempts after the external floor stops ran under path-only deltas, each with a parent PASS:
  - r6 (changeset cd3992b5…1f6d): directories `_r6`, A attempt 2 and the single B attempt;
  - r7 (changeset d03e0b8a…43f7a): directory `_r7`, A attempt 3.
- Minor deviation accepted by the parent: `k3_direct_B_r7.py` creates its output directory with `exist_ok=True`;
  every file in it is created exclusively.
- `AMENDMENT-4.r4.md:372` says "All 22 generators preserve base, cube and cuts". The lists are cube-specific: each
  cube's own listed generators preserve its base ∧ cube conjunction, and the A route uses H_311 (Link 11). [F1]
- `AMENDMENT-4.r4.md:364` says that, for encoder A, all other Gram-G1 … Gram-G5 clauses are direct clauses on g. The
  G2 clauses contain h; once h takes its defining conjunction, they hold by frame consistency (Link 7). [F3]
- `AMENDMENT-4.r4.md:358` ("Take a K3 triple normalised by `--sym`") together with `:371` ("hold by the choice of
  cube") needs the residual normalisation of Link 6 between `--sym` and the cube units (Link 7). [F2]
- `AMENDMENT-4.r4.md:148` says the maps "preserve the QLS axioms and mutual orthogonality, so the image is a K3
  triple". It should add that cell permutations, transposition included, leave each square's ray set unchanged, hence
  its individual non-classicality (`LEMMAS.md` lines 9–11; Link 10). [m4]
- `AMENDMENT-4.r4.md:362–363` says there is one G4 guard "per square, line and off-line point". (Square 1, row 0)
  has no guards: `--sym` replaces that line's G4 clause by three units (`gram_enc.py` lines 123–126; `gram_encB.py`
  lines 191–194). Wording only. [m8]
- Desk report template sentence (frozen reports unchanged). Every assembler of the parent B-replay desk (v1–v14)
  prints "Both logs are empty (0 bytes): no status line was printed before the stop." unconditionally. It is true
  only for the first B_C321 attempt (`REPORT.md` line 25; solver/checker logs 0 / 0 B). It is false in
  `REPORT.v2.md` line 26 (16 / 0 B), `REPORT.B_C321-a3.md` line 25 (16 / 478 B), `REPORT.B_C411-p1.md` line 26
  (16 / 0 B), `REPORT.B_C311cuts-p1.md` line 26 (16 / 0 B), `REPORT.B_C411-p3.md` line 25 (16 / 479 B; recorded in
  the G2 verdict) and `REPORT.A_C311cuts-p2.md` line 25 (16 / 475 B). The attempt receipts, the RESULT files and the
  log tables of the same reports give the correct sizes and SHA-256. `REPORT.B_C311cuts-p2.md` line 25 is false too
  (raw 16 / 478 B; recorded in the B-cut verdict and audit). [U18] [U19]
- `R/moqls7-A-C311cuts-parent-audit-v1.json` labels the checker's 466 CR-normalised bytes as `raw_log_bytes`; the
  actual raw A_C311cuts-p2 checker log is 475 B (SHA-256 4fb0b9a9…9348), as the A-side verdict states. Byte-count
  label only; statuses and outcomes are unchanged (recorded in the B-cut verdict). [U19]

## 6. File index (SHA-256 at the writing time)

Parent records (`R/`):
- `moqls7-parent-verdict.md` a39911fde4245526840157403cdcf535458011e55d0571a6d9ecbd78446a3ff2
- `moqls7-k1-parent-verdict.md` 1cd0603c5dc3e5d724725388de6f9130721c3b686bda3b6ebde765a53dd7dfb8
- `moqls7-k2-parent-verdict.md` 25ecb6bab8caad2a7e9c79faa8fbf8d2f34befab8c000338d8d14d63df811242
- `moqls7-k3-cover-parent-disposition-v1.md` fbfc0e1079cd94bcca65a9d1c68ef9f4ac545181d7f9f8bed02feb244aaff369
- `moqls7-k3-cover-review-v1/RESULT.md` 0f80460c1059a10fe6f3c614e55a5fdd7fd2af6606cc0b8b80781cc8d89eef84
- `moqls7-amendment4-parent-disposition-v1.md` 3c9373c0ca7a8a98d9af3b2288b04076cad421e65ce645638ab151b850694e44
- `moqls7-amendment4-review-v1/RESULT.md` 3792077335885fe78c8c632c347502314148592fec90177121b6a16384c55dac
- `moqls7-amendment4-header-erratum-v1.md` effec3dbc145dc366678bec31c2aa2b2cf8a13b3992bc4838e8f91f1058eb148
- `moqls7-k3-A-cubes-parent-verdict-v1.md` 0ba3fe4f0e14d17abbb21766523f1a18627cb1ca6178c5bf546d4eec2cb81f97
- `moqls7-k3-A-parent-receipt-audit-v1.json` 97c1e0e4dde7b188e447f40e76cb6935ebb9f8f7060a32ff9e96ebef8dbfc234
- `moqls7-k3-cube-parent-replay-v1/RESULT.json` 8b6f57b7cc9f14071849d916fcfa5001ed7dac43e6d0b5d2673adefb1431ca9b
- `moqls7-k3-cube-parent-replay-v1/REPORT.r2.md` d42882cd9f928890aaca6d6bcc008756468257ace5ec01b4fe3393fe9099c536
- parent A replay receipts (from the A-cubes verdict): A/C321
  cbd7f02f5b2850cae2814c641f283633abf5405b87035bac3043a1541502efa8; A/C411
  308e255ee1ec4c687f1b79db4157a44c3c3ae9fc1b8cffa24b976f8690707442
- `moqls7-k3-B-cube-parent-replay-v1/RESULT.json` e0cd7d87ba47c57a65db96d1723e3c18affc69dc1fae93db296d3f445f11f1b3
  (first B/C321 attempt, UNKNOWN; the desk is live and may supersede it)
- contract `screening/phys-2-moqls7-maximum-contract.json`
  21b1b38bf82e2923518ce8fd1a8885f38427d2a07ac968fbec53e0150744d372

Lane texts (`L/review/`):
- `K1-THEOREM.r3.md` 2d77c63719fafd1e7f7cfe2a3161931f2e90dff0976e3ee9c5083a88d076a096
- `K2-THEOREM.r2.md` a73a90078a3b9923935755d2663ecba645ba7f231d8f07384b8f34656ab532cd
- `LEMMAS.md` 4bddc9d422cf989bb9bfdf4f09de72742ea2d423b9a082f8fd76263ba1c850c9
- `GRAM-ENCODING.r2.md` c6c506a7d1ecba15b2e31393b0da4caa248db5c9227f512c0df9ea5bd07ad6c7
- `AMENDMENT-2.r1.md` 82ee394ef6b41c62991e3e8cce4077159a9a6432522abd0f7b1aa48ad0f714e0
- `AMENDMENT-2.bindings.r1.json` 1dc0636bedb0920c7304c7a60faef95b00d810942a4d9d9695256241b62d16ff
- `AMENDMENT-3.r1.md` 374978c66af3c3f3a82a518a0466d4bf80e79accad845741edc33d48404bf3cc
- `AMENDMENT-3.bindings.r1.json` 0d842cf890efe147662d7ca2500a3bea1e74c98b144931a0c914750df4fa0316
- `G6-G2-DERIVATION.r1.md` 8790e9e1af45d4b49e397a06fc4b8dbd70742278698c55561e03f0904f07e791
- `K3-ERRATA.r1.md` 85fa93fadaa636949c1c8c26672744833f8a42bc4ddd73d6328343eeeb47c662
- `K3-Q4-SIDECAR.r1.json` 34bb5251ce27e8c112c690fe2d6acec162f33d0e404251af5e54aff9cf3d16e5
- `K3-BMAP-ORACLE.r1.json` df28f4c558ac5d063d3a4057289ed4b3ac48252c00f48be370a1f8df7910f887
- `AMENDMENT-4.GENERATOR.r1.json` 4c23ec44b7189e9df9fd36b39ee2d0a1e62e71bc02bdfd73ff49ab194ac65dd3
- `AMENDMENT-4.r4.md` 75ac7aece0f050160bf147be91eec906ab99e68294bf9f70feb453b9bcbd9a91
- `K3-CUTS-CERT-DELTA.r5.json` 75f8c3823dfab4fc036e90f3fc2df50471b464d79d4e0045b406c73472acb6e2
- `K3-CUTS-CERT-DELTA.r6.json` 899a04375ca79ca39de9d315a6a3be2bc8157746fa278d6741f7432c72830681
- `K3-CUTS-CERT-DELTA.r7.json` 0084423249a671cc234d89077fc9628c037bb2aa01f21ddfda31a37229ad9563
- `K3-DIRECT-B-DELTA.r6.json` 5beb6009bf1f06b1c7fede07d8015ceaf53219fc5b480cbffd47b8fee3df1eb8
- `K3-DIRECT-B-DELTA.r7.json` 55b40519c6a67cee524cf002066eff220f6f621d8d04b5d2fcfef5e98bbeade4

Lane evidence (`L/evidence/`):
- `PARENT-K1-ACCEPTANCE-2356.json` 543677ad95ce34ca6a1260f93d982679ff66e2f2823476753b7703f7d406596a
- `PARENT-K2-K3COVER-0046.json` bc8ba66bdbbe88e79acfabf5cc0cf0d98e248ec08727777c969b6af9694ca399
- `gram/review_controls_r1/summary.json` 6ce1ddc241a88da9f0d2fdc0be3551b8a73f5659a979c5034ebcee5caaecd685
- `gram/transport_controls_r2/summary.json` 34a69ae60c1f09bc4029ae9bb589b581d45204e68146af6dc4f5d54be6fd95e6
- `k3cubes/coverage_r1.json` 14d00a2d3ceab288330198d97972809becf2d6190e77c68dd7959bb388f6f0f3
- `k3cubes/g6_controls_r1.json` edd313ebdf55714c4942919ff15e2f332c3f3485273bb9e78ea01df55c562615
- `k3cubes/lex_controls_r1.json` 3bd546ad71abc93e4616f3ff212ea78b7752c4e500dc0a3e7b003b6e3c584053
- `k3cubes/bmap_oracle_r1.json` 6e2bd95ee38c615ab2a1a6282531da730b2bf0cc45e104e95b850102e0b1952c
- `k3cubes/cert_r2/A_C321.json` c3a30df311eff2ed9b9b5a3706c2ca03a8d4337d8663ea529a9978126fde9314
- `k3cubes/cert_r2/A_C411.json` 5f117b60c6b7833978ea012b3c07921d2d19fa6d0a161c4b93d1d13cd6aa23cf
- `k3cubes/cert_B_r5/B_C321.json` b07100e3a06c3a80f34e62dbc09071fc1f1146cb2031bf48c209098390467614 (UNKNOWN)
- `k3cubes/cert_B_r5/B_C411.json` 1acc121b735e9f537b7e3403cff6d788188d1ef042c8eefd04a5d0815dd17dfc (UNKNOWN)
- `k3cubes/cert_B_r6/B_C321.json` 2ffc2fa87d1c1882a067125b0f6bc5520b1e215946b5285052c0355755d832ac
- `k3cubes/cert_B_r6/B_C411.json` 92354254f8a900688bfc7077a3563cfc556c5c732259412423496a6ee7fa0184 (UNKNOWN)
- `k3cubes/cert_B_r7/B_C411.json` 644b5b23d98a55c44df88f15531644b9e8f825b790a9391791d0f50d082a6f75
- `k3cubes/cuts_r1_receipt.json` 9cfc0e81bed2cbcbdcd2c205d697dc107b184609f722f0f799225e39092babbf
- `k3cubes/cuts_r6_receipt.json` 9624d6127890f90a279ab398888524ed0c5e89376b428e68130ad3bab6db4a24
- `k3cubes/cuts_cert_controls_r5.json` bb9445a2e62d7ed970bf031784934bfa85dc7c43f552554bf178720128beb3e3
- `k3cubes/supervise_controls_r3.json` 3c77be50cbbd9bc07cf44036ac40ab14d21f5805ea03a895bf68f3b11de799de
- `k3cubes/C311cuts_A_r5.supervisor.json` f031159323ded86681b5b16f73db4cd67fac180539f9180e8564fd0a841504d2 (UNKNOWN)
- `k3cubes/C311cuts_A_r6/C311cuts_A.json` 06bd12b0517c51a2d4be5f9b06997990e4ddc9e01811fa85d9b1140eaa3edab3 (UNKNOWN)
- `k3cubes/C311cuts_A_r6.supervisor.json` 50a07ffd0716cf3068dee2fd08fe8a0cea46ff73d669f65d6eacac3e0395fc87
- `k3cubes/C311cuts_B_r6/C311cuts_B.json` 1f00363467d3ed30787cd1b3e4c2e695b8b4d7249623fc6e3994130f4be6c535
- `k3cubes/C311cuts_B_r6.supervisor.json` 43d481410c4060a755dabaa0d028d16a5c5763348549fad837b778f74e96e4cb

Code and binaries (`L/`):
- `code/gram_enc.py` b2c206d8bf4896868fb4e45cd87c633a6cfbb0d62c8fdb62b146ac84a7d38833
- `code/gram_encB.py` c7583efe838816d39fe33456af09897cc2a1f5633d1e57e1ee63b3e5238e2b45
- `code/k3_cubes.py` 70c79c624dd4c4ad0929a41790b7674eaa7343f3fcb5802c5e0c1abdbfb30550
- `code/k3_lex.py` 2b721e85812cd7b3438771868f63da1e10f3fbeed6551f7888f74a399e159b10
- `code/k3_cuts_r1.py` 0ec92c861024a728aa38d238fda2d7f5f056fae12cb0f474a15db0335b6e1b0a
- `code/k3_cuts_r6.py` d0fc540e71c6de97027b59e74f35ed4d30a72c70cc57a830f67b5f0b58b2b1aa
- `code/k3_cuts_certify_r5.py` a12f9632f23cc76f66de7d619da6f2217480544625d047f0e21c27a3325ee0a5
- `code/k3_cuts_certify_r6.py` 12b141fd8e1e2997dec8966d66b2e5b1532069b3bd579f676201514cf271db91
- `code/k3_cuts_certify_r7.py` 6485a1eb5634266becd115195a82cf12750f759de47d8a95a750af8997691c98
- `code/supervise_r3.py` 0ee8f39496fa3d6051639e99f10d907b8adadcb5d3446f2bb6242c924a83ec4d
- `code/k3_direct_B_r6.py` 24fcfea8daeb275433480eaa4b223cab2d2d8bd85b856c29a0ed77b6ccc4c44d
- `code/k3_direct_B_r7.py` 386bff0cc014f3a46aee4c27b5057fb9230704c43dbb07ac74171ca8af894cfa
- `code/proof_stream_r2.py` 45163ed4442966779a818edf2e8a4cec9f7594fb78dcfb46ebda95fe1b7c5605
- `code/bmap_oracle_r1.py` 13f4a5e6c34b61478fcdbb5fddc1a934901c1b82480553cfee8b0f958f73cd8e
- `env/drat-trim/drat-trim` 111b0405566d55629f5d391b80b3220cc7a3ebc3cd406a35895ff65cc9acd5e4 (source
  d834b649f437e091597f5347f259b9f681087f89ca0844d0cee250a1a1a0c2ee)
- CaDiCaL 3.0.1 601c9fa8ba5d09fd81bb00c89b3e54832f138bccc3422bd8652e8cda4d74d1fa; kissat 4.0.4
  05d6f3e9c402a1fe8853b0746e384e1b3d1c4a550e255f11daa2461d279aa848
- sources: `sources/quantum-latin-2607.12933v2.pdf` 2d60d45fbc3e3d1d5f5d6cfec0f7040b6f362ba3d7c7b3e358d3fb02a6e21afe;
  `sources/2607.12933v2.layout.txt` df1d8b1467166d2e615461669401dfada86bb9033ffd4a7e0acb34b8e8584219

CNF and block pins:
- A_C321 d598507d84a8d7595b30a100d528dca08bc0ce1aa71978583f09aac188298388
- B_C321 8b7b8124dbaf7088626ae853f4e10fe9590459dde1676377326ceecfb6d812c6
- A_C411 2b92f5b15cd641e4a07ecec241b7957deac972aa3c7333056ff3e739e46addf2
- B_C411 01acf46491feef2fc26060266af8c2dead0cec9832c9e9ecbed83f886ecb8bf8
- A original C311 7fca33f1e6324cbe17bc44bbea7f8d9188bcac187252d766fb0fa5e39e1c2001
- A lex C311 059be6164176ee93c94d93bd47fa1d365477b6c94f3aa867df991f677e1a8c4f
- B_C311 b3ec010855ad4abd75ffd6eb57aaa3ff158bc8447625ee2097f5a6057594c077
- A base d0d884f9a0f9715b256da68be97408ae4a55c88d76183c02246a570f115a4388
- B base 42a5f30453bba3eb423e78b99b1a8fe6039e1c91c32b6ff1dd72f498fa8e0aac
- cut block 05f31da497315877347f7d780e0e6f4c9c4799c8becee3bdb192a8420ff6e6dd
- strengthened A 18583aabb486b2d7fdf2159ed2172c9dfc9b29bbd2e50c63a5d7d94d44ba2e5e
- strengthened B ae3b8309601d115e2258782ae3cb793f4dc4b5950064b9536b1eca61521f783a

r4 additions (SHA-256 at the r4 writing time): [S9]
- `R/moqls7-k3-h3-parent-verdict-v1.md` edba465af496963c0cac338d4d33fbc3edd1cbc7772908a92ac8115c66eabca7
- `R/m7-h3-instantiation-codex-v1.note.md` 2cdda1de5736dbf743b3f148de7b8d3a540f73440aaf8679eac8783a757d7190
- `R/moqls7-k3-composition-r1-codex-v1.note.md` 5a68a20d5d4a64cf1b4f3fecdd3761c552b09e6b562ae2bea306d3b2add447bf
- `R/moqls7-k3-composition-r2-claude-v1.note.md` 786f3438a5b817ff459d4fd1bef906d0ccc8d8fde9f56dfbdad7c526236c78e1
- `R/moqls7-k3-B-cube-parent-replay-v1/RESULT.v2.json` 49e61ef64ce7d14ccdd3569e207beaf7899247cc7e8082efe9f14c9c56fb373a
- `R/moqls7-k3-B-cube-parent-replay-v1/receipts/B_C321.json` 30017291a00e2da885b2d11f856f4c1a6a10d6026d4c74f0ee76e49a6985d117
- `R/moqls7-k3-B-cube-parent-replay-v1/receipts/B_C321-a2b.json` b558c3eed928101e8a86de80317f96f207b2bb6b63a36e1949fe22f308459874
- `R/moqls7-k3-B-cube-parent-replay-v1/receipts/B_C321-a3.launch.json` 57989320bec4c059ceb837cb5894ff85dbf1bbc6e048b1c43a0c0f728c4e0cde
- `L/review/K3-COMPOSITION.r3.md` b85daed48b15ebcc69ea2c8cdd54899911ce8565f9ceebe67a36cbdb01726aed
- `L/review/K3-H3-INSTANTIATION.r1.md` c3d8c05db226781de915d7a98ee84eae16cb7392e7aef2fc4a37b897dfd65cdc
- `L/review/K3-H3-INSTANTIATION.r1-ERRATUM-1.md` 9559a54bea22d62c5a61b8bb8a66cd3c35785881d32bf6425d0b6fc4677c17b5
- `L/review/K3-CUTS-CERT-DELTA.r8.json` 439e37ee13687877be412c9fccc255305c11e37896c3f58e63ee1f536024d3d4
- `L/review/K3-CUTS-CERT-DELTA.r9.json` 76f68d348e2265796696ae4dd9626a3855478748f8c236bfaa4ad57c90525487
- `L/code/k3_cuts_certify_r8.py` 1a50f09c0019107637a7c97cf3e997040aa09bf04d626b381ff279f31e087eb5
- `L/code/k3_cuts_certify_r9.py` 2f0ced454369242c47ee0f1446f433f92230aa58da4af3c3311aed7476077ed3
- `L/evidence/k3cubes/C311cuts_A_r9/C311cuts_A.json` 88c154b75e9fa7acb3ec05867d0542b6be4b349c189931ad5217a4f16235f37f
- `L/evidence/k3cubes/C311cuts_A_r9.supervisor.json` 2fb5e03241f3d88416a04fe5c0671b15eb6b6c63329eec651f0d672458ff25b1
- `L/evidence/k3cubes/C311cuts_A_r7.supervisor.json` 6cf3bd5db65862924eddde2ef283756dbeb9eceaa88a5f334267003298c60496 (UNKNOWN)
- `L/evidence/k3cubes/C311cuts_A_r8.supervisor.json` eea330071e6d06cd3a6e2eee7d37ac4bfabc77c095701e341f4c4b1aff90aec6 (UNKNOWN)
- `L/evidence/k3cubes/cert_B_r4/B_C321.json` 2692620cb7a2c663ef29e406d709a8de896577de9b12ea318f4d1ecf53130c37 (UNKNOWN)

r5 additions (SHA-256 at the r5 writing time): [U9]
- `R/moqls7-k3-G1-parent-verdict-v1.md` 639fbf6bfa1395ad575eef96ee2ea4715a6cba7283cdb4d79c5c4bb0e5cfb47f
- `R/moqls7-k3-G2-parent-verdict-v1.md` d41253f6473ef78df1fa9272363674e5c90c5a0f90616c3a0d0129470e067aa7
- `R/moqls7-k3-A-C311cuts-parent-verdict-v1.md` b18472b2aed47547f23e0c8288c9e9d7b6c25ebcbe9f9d4472626054464593a8
- `R/moqls7-k3-B-cube-parent-replay-v1/RESULT.B_C321-a3.json` 4c0845eedd0d37ca19e7c9731e4333d5fc7de1fb5716b034f157113b73dadb9f
- `R/moqls7-k3-B-cube-parent-replay-v1/receipts/B_C321-a3.json` 0ba462963e47936d171a9cfc81a569a995800efba3d1ab1eff756e9071cbb0c4
- `R/moqls7-k3-B-cube-parent-replay-v1/REPORT.B_C321-a3.md` 174255cfdad6fe1c732a31ccab4951885002ffbf156f950ddc01a7894e2e8887
- `R/moqls7-k3-B-cube-parent-replay-v1/deviations-B_C321-a3.json` 9bc2e569966e7ba19536774e6b8da60853487e0030de00ef6c89b035a918d707
- `R/moqls7-k3-B-cube-parent-replay-v1/RESULT.B_C411-p3.json` e1ef46d1249b9cc3dcb6a220cce0d744f75459d03cfe2b9b1cdd573925e189f0
- `R/moqls7-k3-B-cube-parent-replay-v1/receipts/B_C411-p3.json` c176b738bdafddf286896dd917a67edf9175bca6535fe0f174c743a867440ab1
- `R/moqls7-k3-B-cube-parent-replay-v1/REPORT.B_C411-p3.md` cc37da454799410bec0bd5b6c7facc6844a3c4dbcc730c421848a5c377deabd2
- `R/moqls7-k3-B-cube-parent-replay-v1/deviations-B_C411-p3.json` 0b207f3dddee0cc09b9afa39c790198e80fbaef9373b1ac33d18692775e2243f
- `R/moqls7-B-C411-parent-audit-v1.json` 9850fd8b1be897e4a55366513c9247fc3bb3aa4af66daf4f25a1c212e5020e12
- `R/moqls7-k3-B-cube-parent-replay-v1/receipts/A_C311cuts-p2.json` 59b27e911837fea015ca021c233b8ea6ad2a6e0f95d63d3615ad1b2996c569b4
- `R/moqls7-k3-B-cube-parent-replay-v1/RESULT.A_C311cuts-p2.json` 51470bce8e0a67ad7a3be71bcf89c101389cd15f8545a8346a74117df42fcd76
- `R/moqls7-k3-B-cube-parent-replay-v1/REPORT.A_C311cuts-p2.md` 8a9ff43bd107bfd8ab1f9f26e108c24d1b73c967dc2b7a4a5465cec60cdb7ad8
- `R/moqls7-k3-B-cube-parent-replay-v1/deviations-A_C311cuts-p2.json` ce0d81f7612ef8cdc651a07786104859ba1eb12300adf6898503fa154b3ee3e3
- `R/moqls7-A-C311cuts-parent-audit-v1.json` 73660641dbadab97e195b59beeffaf445261d57c88739564117f71eea2f3e306
- `R/moqls7-k3-B-cube-parent-replay-v1/RESULT.B_C311cuts-p1.json` a74b1256bd1c2fb5a74a6f9cb4bfe956b72965506b9e99300edeee0dc8b9207d (UNKNOWN)
- `R/moqls7-k3-B-cube-parent-replay-v1/receipts/B_C311cuts-p1.json` ae0e465492cb91fcef341bf6a50ba3405535c9bdb012dba25aef361770a1bf18 (UNKNOWN)
- `R/moqls7-k3-B-cube-parent-replay-v1/receipts/B_C311cuts-p2.gate.json` d09b4aadf1899b6274a1ac4fd5375946cb2cdb7ea3cfbd96ceb8c3855843fb21
- `R/moqls7-k3-B-cube-parent-replay-v1/receipts/B_C311cuts-p2.pre.json` 4db347d1f470ee09e1f8f02ab11bf7083dfaf17cc24619d9ad385e1343517c41
- `R/moqls7-k3-B-cube-parent-replay-v1/receipts/B_C311cuts-p2.launch.json` 78a505e3d2a0db7bcb69276774bae011228b272436c94f6df5842c651c5b3455
- `R/moqls7-k3-B-cube-parent-replay-v1/receipts/B_C311cuts-p2.json` edfbb2f134615fe3f6c09ab24ef52b5b4f13702ce357904625a71a1fc380241e [U19]
- `R/moqls7-k3-B-cube-parent-replay-v1/receipts/B_C311cuts-p2.driver.json` 8bb2ae362a8f602a6598a4ba938499f127d8f17ad45e621a5de9a302b7f6511c
- `R/moqls7-k3-B-cube-parent-replay-v1/receipts/B_C311cuts-p2.supervisor.json` 40f8f9ee36e24d159470b86b4c08efacb91e9a7966c9b8c9bce85fd485560dd8
- `R/moqls7-k3-B-cube-parent-replay-v1/receipts/B_C311cuts-p2.launch-outcome.json` 3a75b1217e3755b9f6841814f0656f73ab32c42594c1fe55454dd3f2ef236d91
- `R/moqls7-k3-B-cube-parent-replay-v1/logs/B_C311cuts-p2.solver.log` bde6e1eede96772c07c8ce29fd18088863815bd043aa59a06f11f5838cf8a162
- `R/moqls7-k3-B-cube-parent-replay-v1/logs/B_C311cuts-p2.checker.log` d55db210e80e07230ffe01610b0b3edd252f08d7ea583e4a2fc53711419130f2
- `R/moqls7-k3-B-cube-parent-replay-v1/RESULT.B_C311cuts-p2.json` 45eee709b8c4fe5a1438a8930da908379ef17ecf9351d1795a94fbd3468fc3f5
- `R/moqls7-k3-B-cube-parent-replay-v1/REPORT.B_C311cuts-p2.md` b34dcdec1aca389ec5de5f4efced5999d10c758a643e564c0acb30dc6f09c17c
- `R/moqls7-k3-B-cube-parent-replay-v1/deviations-B_C311cuts-p2.json` 948c4b3167a47b1b9f074e6c4705ed6436c7cce0e207b163024ec397123bcdfa
- `R/moqls7-k3-B-cube-parent-replay-v1/scripts-v14/launch_B_v14.py` a182058cf075110349d1c670eadf25823fe914091d72abea16929a9a0eb66589
- `R/moqls7-k3-B-cube-parent-replay-v1/logs/A_C311cuts-p2.checker.log` 4fb0b9a94ddd41d4222c7a04dc9fbbf014c811a6af19ab39ec94239db6de9348
- `R/moqls7-B-C311cuts-parent-audit-v1.json` 024e636da51941a0bdbf8ebb62c35ea6ca02ca9f77c1a4eb52bb4d90a349cab9
- `R/moqls7-B-C311cuts-parent-audit-attempt1-UNKNOWN.json` 1ccf778b450f421407e0fe6d7eea5add033178c59ef1c86543028b84a6f8aa21 (UNKNOWN audit attempt)
- `R/moqls7-k3-B-C311cuts-parent-verdict-v1.md` 10a65127d17bb8b8df0bccb42a7722eee86e3891b15189d5279ed616660cfbd3
- `R/moqls7-k3-B-cube-parent-replay-v1/RESULT.B_C411-p1.json` ae98762285033bd46d318ab9f3639ecab79a624cec6bce08b3a99581e5356fe1 (UNKNOWN)
- `R/moqls7-k3-B-cube-parent-replay-v1/receipts/B_C411-p1.json` 12ae7cd5afc868a16e466915fb7a403dde2295b762042090cefe97c342027b93 (UNKNOWN)
- `R/moqls7-k3-B-cube-parent-replay-v1/receipts/B_C411-p2.disarm.json` 0a5a5f327ce9055510ed7fbf942f49d1f386bbc53722ae4e90d7949a89297f9d (NOT_STARTED)
- `R/moqls7-k3-B-cube-parent-replay-v1/receipts/A_C311cuts-p1.disarm.json` 07ac6b5c16335a1d163baf09eafa92a8fa03e2849442a8532fea06b15936fe08 (NOT_STARTED)
- `R/moqls7-k3-B-cube-parent-replay-v1/receipts/regen-A_C311cuts.json` 95243e0816b71f2743678c10506c1b75e9d063e2a5991aa88576c44d7b1fa24b
- `R/moqls7-k3-B-cube-parent-replay-v1/receipts/regen-B_C311cuts.json` 1df56436d4a36bad8f0b1ebec09ad75ac02102dc6db1409f6f922089092a3cc0
- `R/moqls7-k3-cube-parent-replay-v1/receipts/v1-selfcheck-summary.json` 8b62446cdb2dbce7d5312f1055f7c3680413ea0479b3149ae91189c5e68e6171
- `R/moqls7-k3-B-cube-parent-replay-v1/receipts/selfcheck-summary.json` ec246769fa8f5ab2e289b949cfb7fbd8a1103264be9b6e667925d83092c8739b
- `R/moqls7-k3-B-cube-parent-replay-v1/receipts/test-v11-selftest-r2.selftest.json` ccb66053613e353dc3c9d95581cff5b876f1e656725a3bb0e59dfbf12b515d02
- `R/m7-launch-v6-r9-parent-addendum-v1.md` 595999fba42c7b89d4d9b1dc5a04b3a5d152fcc772b9107562ef2df115f57c1a
- `L/review/K3-COMPOSITION.r4.md` 152e13cbd6815ba54489bdf3d62857451f51514f0b34e52b2de1a7967d777b3e
- `L/review/drafts/K3-COMPOSITION.r5.md` 0dbaefe30cc595c04ae2e98762d0ff3363d5d89ee3809012fe7b9a1fbe252486 (lane draft this file derives from) [U17]
- `R/moqls7-k3-B-cube-parent-replay-v1/composition/K3-COMPOSITION.r5.final-draft-1.md` 55335a3ba897bb4e673f0f56404f92d9b7d63d4e9bd0df0100944a5fcfbf94e4 (pre-freeze draft) [U19]
- `L/evidence/k3cubes/no_duplicate_regen_controls_r1.json` 024cb624c27de100d48e96e7a64c5a103bb2801f37b7d29820d636270dfb0f6f
- `L/explore/k3cubes/A_C311.meta.json` 3b2ab04f2b42b799169bdccf3d868f544ba571ff1d72e18d0cf68187a0f4d9ed
- `L/explore/k3cubes/A_C321.meta.json` 030cc5b853fd4cd2a437da1bcde14743d3a66f6f3f7fb30202185d83adb4dbda
- `L/explore/k3cubes/A_C411.meta.json` c180a573fae37aab45cd9cdd2711786063695d3393cf4dfa58608acdc5769874
- `L/explore/k3cubes/B_C311.meta.json` bfa298eea4a6b102a16e15663d42c2cdf86ab7ab093f86bdecb7d8bf8d28a056
- `L/explore/k3cubes/B_C321.meta.json` 79c91883e72e8604f791747dd15ae54c693528563e5770a63012600bc1bf6120
- `L/explore/k3cubes/B_C411.meta.json` c0f769bb56342c2fe78df4051fa15900f8d2de67eff0f41a2471990b2fb58a12
- `L/explore/k3lex/A_C311.meta.json` 7bef0b78007151d94661181244fa8614c114705522b58fc16cf287014bde190d

## 7. r2 fix map (errata only; no other change)

All three findings are MINOR, from the Codex audit 5a68a20d…47bf. That audit gave Link 3 ACCEPT; Link 7
ACCEPT-WITH-FIXES; Link 10 ACCEPT, conditional on G1/G2; Link 11 ACCEPT-WITH-FIXES; Link 14 ACCEPT, conditional on
its premises.

| Fix | Finding | Where in r2 |
|---|---|---|
| F1 | The lex group is cube-specific: H_311 = ⟨generators("C311")⟩, not "all 22 generators" | Link 11 statement; Link 14 ("H_311-orbit"); §5 erratum for AMENDMENT-4.r4:372 |
| F2 | Separate `--sym` normalisation from the residual cube normalisation of Link 6 | Link 7 statement (first and third bullets); §5 erratum for AMENDMENT-4.r4:358/371 |
| F3 | A's G2 clauses contain h; they hold by frame consistency once h takes its defining conjunction | Link 7 statement (second bullet); §5 erratum for AMENDMENT-4.r4:364 |

Other changes are only the identification header (title, the r1 binding, the audit binding and the frozen-file
name) and this section. No status, hash, link, obligation or conclusion changed.

## 8. r3 fix map (errata only: wording and citations)

All nine findings are MINOR, from the Claude audit 786f3438…78e1 (ACCEPT-WITH-FIXES, 0 FATAL, 0 MAJOR, 9 MINOR).
That audit gave Link 3 ACCEPT; Link 7 ACCEPT-WITH-FIXES (m7, m8); Link 10 ACCEPT-WITH-FIXES (m3, m4), conditional
on G1–G2; Link 11 ACCEPT-WITH-FIXES (m5, m6); Link 14 and §3 ACCEPT-WITH-FIXES (m1, m2, m9), conditional.

| Fix | Finding | Where in r3 |
|---|---|---|
| m1 | Both strengthened inputs contain the cut block; cite Link 10 on both sides | Link 14, C311 bullet: "(Links 7, 10, 11)" and "(Links 7, 10)" |
| m2 | Link 14's composition-review premises omitted Link 10 | Link 14 premise list |
| m3 | Link 10's condition also needs Links 3 and 7 (G4 on the image, encoder instantiation) | Link 10 status; Link 14 premise list |
| m4 | The transport image stays individually non-classical (ray sets are invariant under cell permutations) | Link 10 statement; §5 erratum for AMENDMENT-4.r4:148 |
| m5 | Cut invariance under the C311 generators is structural; C4 is a check | Link 11, fourth statement bullet |
| m6 | The general-length comparator argument is written out | Link 11, comparator lemma bullet and status |
| m7 | No empty clause or `None` literal: list sizes in the 2-net domain; degenerate branches unreachable | Link 7, fourth statement bullet |
| m8 | (Square 1, row 0) has no G4 guards under `--sym` | §5 erratum for AMENDMENT-4.r4:362–363 |
| m9 | Trust base: add the set-isotopy definition behind (C0) and the source of the lower bound | §3 trust base, imported results |
| P | Pointer to later events (route A attempts 3 and 4 UNKNOWN on the external floor); not a status change | Header |

Other changes are only the identification header (title, the r2 binding, the audit binding and the frozen-file name)
and this section. No link status, hash, obligation or conclusion changed. Every edit carries its tag in the text.

## 10. Attempts that ended UNKNOWN (non-contributing) [S10]

None of these supports any link. Each stays UNKNOWN and is never relabelled.

| Item | Attempt | Record (SHA-256) | Outcome |
|---|---|---|---|
| A C311+cuts | 1 (delta r5) | `C311cuts_A_r5.supervisor.json` f0311593…04d2 | external free-space floor, 04:09:50 |
| A C311+cuts | 2 (delta r6) | receipt `C311cuts_A_r6/C311cuts_A.json` 06bd12b0…dab3; record 50a07ffd…fc87 | external floor, 04:53:03 |
| A C311+cuts | 3 (delta r7) | `C311cuts_A_r7.supervisor.json` 6cf3bd5d…0496 | external floor, 07:04:14 (solver rc 20, no checker verdict) |
| A C311+cuts | 4 (delta r8) | `C311cuts_A_r8.supervisor.json` eea33007…aec6 | external floor, 07:10:39 (after 99 s) |
| B_C321, producer | r4 | `cert_B_r4/B_C321.json` 2692620c…0c37 | global free-space floor after 77.704 s (before the B-map oracle) |
| B_C321, producer | r5 | `cert_B_r5/B_C321.json` b07100e3…7614 | checker clock (`s TIMEOUT` at 3600 s after solver rc 20) |
| B_C321, parent replay | first | `R/…/receipts/B_C321.json` 30017291…d117 | external floor, 04:53:03 |
| B_C321, parent replay | a2b | `R/…/receipts/B_C321-a2b.json` b558c3ee…9874 | external floor, 07:04:14 (solver rc 20, no checker verdict) |
| B_C411, producer | r5 | `cert_B_r5/B_C411.json` 1acc121b…7dfc | checker clock (`s TIMEOUT` after solver rc 20) |
| B_C411, producer | r6 | `cert_B_r6/B_C411.json` 92354254…0184 | global free-space floor, 04:09:50 |
| B_C411, parent replay | p1 | `R/…/receipts/B_C411-p1.json` 12ae7cd5…7b93 | external SIGTERM after solver rc 20, no checker verdict [U10] |
| B_C411, parent replay | p2 | `R/…/receipts/B_C411-p2.disarm.json` 0a5a5f32…7f9d | NOT_STARTED (disarmed, gate only) [U10] |
| A C311+cuts, parent replay | p1 | `R/…/receipts/A_C311cuts-p1.disarm.json` 07ac6b5c…fe08 | NOT_STARTED (disarmed) [U10] |
| B C311+cuts, parent replay | p1 | `R/…/receipts/B_C311cuts-p1.json` ae0e4654…bf18 | external SIGTERM after solver rc 20, no checker verdict [U10] |

The desk's B_C321 a2 has only a gate record (`receipts/B_C321-a2.gate.json`) and no pipeline receipt.

Desk B_C311cuts-p2 ended PASS (parent raw audit 024e636d…cab9; §18), so it has no row here. The parent's first raw
audit of it, `R/moqls7-B-C311cuts-parent-audit-attempt1-UNKNOWN.json` 1ccf778b…aa21, compared the gate's RSS-cap
object to a scalar and stopped before acceptance; it is retained as UNKNOWN. It is an audit record, not a replay
attempt, and no native work was repeated (B-cut verdict). [U17] [U19]

## 11. r4 fix map (status refresh only; no logic change)

| Tag | Change | Where in r4 |
|---|---|---|
| S0 | Identification header: r4, binding of r3, statuses as of 08:21:45 | Header |
| S1 | Link 7: ACCEPTED at conditional scope (parent H3 verdict edba465a…abca7, with erratum 1) | Link 7 status |
| S2 | Link 8: parent replay desk attempts (first and a2b UNKNOWN, a3 running); exactly which certificates discharge G1 | Link 8 |
| S3 | Link 9: B_C411 replay queued under launcher v11; exactly which certificates discharge G2 | Link 9 |
| S4 | Link 11: the H3 verdict's conditional scope covers the H_311 orbit-minimum lex step | Link 11 status |
| S5 | Link 12: attempts 3–4 UNKNOWN; attempt 5 producer certificate with receipt and supervisor SHAs; replay queued | Link 12 |
| S6 | Link 13: replay queued under launcher v11 | Link 13 |
| S7 | Link 14: final parent composition verdict pending | Link 14 status |
| S8 | §4 obligations refreshed | §4 |
| S9 | File-index additions | end of §6 |
| S10 | Non-contributing UNKNOWN attempts listed | §10 |

No link statement, premise, argument, erratum or conclusion changed. §3 (the conditional M(7) = 2 consequence) is
unchanged and still conditional on acceptance of Link 14.

## 12. Exact formulas, encoders A and B [U11]

Construction blocks (all variable maps are `k3_cubes.variable_map()`, equal to encoder A's map at run time and to
encoder B's map by the runtime oracle 6e2bd95e…952c):
- **A base**: `gram_enc.build(3, None, True, True, None)` (`code/gram_enc.py` b2c206d8…8833); base text SHA
  d0d884f9a0f9715b256da68be97408ae4a55c88d76183c02246a570f115a4388; header `p cnf 96978 627398` (derived: a cube
  header minus that cube block's clause count in its metadata; agrees with the Claude audit's hand count).
- **B base**: `gram_encB.py --squares 3 --heavy --sym` (`code/gram_encB.py` c7583efe…2b45); base text SHA
  42a5f30453bba3eb423e78b99b1a8fe6039e1c91c32b6ff1dd72f498fa8e0aac; header `p cnf 461370 1629644` (derived the
  same way).
- **Cube block** `k3_cubes.cube_clauses(vmap, C)` (`code/k3_cubes.py` 70c79c62…0550): 18 signed units plus 70 G6
  clauses per singleton support; +158 clauses for C311 and C411 (two singletons), +88 for C321 (one); no new
  variables. The cube CNF is the base text with the header's clause count increased and the block appended.
- **Lex block** (A route, C311 only; `code/k3_lex.py` 2b721e85…9b10): the seven H_311 generators, 4,156 clauses for
  each of the six simple swaps and 6,676 for the combined column-4/5 plus square-2/3 operation: +31,612 clauses and
  +10,535 prefix variables (lex metadata 7bef0b78…190d, finite controls PASS).
- **Cut block** (AMENDMENT-4.r4 §4): `k3_cuts_r1.emit` re-emitted by the appender, 238,140 clauses (26,460 + 211,680),
  6,974,640 bytes, SHA 05f31da497315877347f7d780e0e6f4c9c4799c8becee3bdb192a8420ff6e6dd; no new variables.

| Formula | = | SHA-256 | Bytes | Header | Status |
|---|---|---|---|---|---|
| A_C321 | A base ∧ C321 block | d598507d84a8d7595b30a100d528dca08bc0ce1aa71978583f09aac188298388 | 16,730,029 | `p cnf 96978 627486` | ACCEPTED UNSAT (A-cubes verdict; G1) |
| B_C321 | B base ∧ C321 block | 8b7b8124dbaf7088626ae853f4e10fe9590459dde1676377326ceecfb6d812c6 | 31,378,199 | `p cnf 461370 1629732` | ACCEPTED UNSAT (G1) |
| A_C411 | A base ∧ C411 block | 2b92f5b15cd641e4a07ecec241b7957deac972aa3c7333056ff3e739e46addf2 | 16,730,836 | `p cnf 96978 627556` | ACCEPTED UNSAT (A-cubes verdict; G2) |
| B_C411 | B base ∧ C411 block | 01acf46491feef2fc26060266af8c2dead0cec9832c9e9ecbed83f886ecb8bf8 | 31,379,006 | `p cnf 461370 1629802` | ACCEPTED UNSAT (G2) |
| A_C311 (original) | A base ∧ C311 block | 7fca33f1e6324cbe17bc44bbea7f8d9188bcac187252d766fb0fa5e39e1c2001 | 16,730,837 | `p cnf 96978 627556` | source of the lex input; screens UNKNOWN |
| A lex C311 | A_C311 ∧ lex block | 059be6164176ee93c94d93bd47fa1d365477b6c94f3aa867df991f677e1a8c4f | 17,503,163 | `p cnf 107513 659168` | input of the A strengthening; screens UNKNOWN |
| **A strengthened** | A lex C311 ∧ cut block | 18583aabb486b2d7fdf2159ed2172c9dfc9b29bbd2e50c63a5d7d94d44ba2e5e | 24,477,803 | `p cnf 107513 897308` | ACCEPTED UNSAT (A-cut verdict b18472b2…) |
| B_C311 (original) | B base ∧ C311 block | b3ec010855ad4abd75ffd6eb57aaa3ff158bc8447625ee2097f5a6057594c077 | 31,379,007 | `p cnf 461370 1629802` | input of the B strengthening |
| **B strengthened** | B_C311 ∧ cut block | ae3b8309601d115e2258782ae3cb793f4dc4b5950064b9536b1eca61521f783a | 38,353,647 | `p cnf 461370 1867942` | ACCEPTED UNSAT (B-cut verdict 10a65127…) |

Sizes and headers of the seven on-disk formulas were measured from the pinned files at 11:07 (SHA equal to the pins).
The two strengthened formulas are never written to disk; their sizes, headers and SHAs come from the producer and
parent receipts, which measure the bytes fed to solver and checker. Arithmetic: 627,398 + 88 = 627,486;
627,398 + 158 = 627,556; 1,629,644 + 88 = 1,629,732; 1,629,644 + 158 = 1,629,802; 659,168 + 238,140 = 897,308;
1,629,802 + 238,140 = 1,867,942; 17,503,163 + 6,974,640 = 24,477,803; 31,379,007 + 6,974,640 = 38,353,647.

## 13. Proof-stream boundary (no proof digest) [U12]

**How every K3 certificate cited here was produced and checked.** In every producer run and every parent replay in
this note, the solver writes a binary DRAT proof into a FIFO and drat-trim consumes that stream as it is produced
(lane producer runs: binary proof on drat-trim's standard input, `-i`). No proof file is written or retained and no
digest of the proof stream is recorded. drat-trim reports only how many proof bytes it
consumed, for example 705,539,296 (A_C311cuts-p2), 1,072,845,839 (B_C411-p3), 842,063,946 (B_C311cuts-p2) and, for
producer runs, 517,255,126 (A C311+cuts attempt 5), 842,063,946 (B C311+cuts r6), 1,072,845,839 (B_C411 r7) and
1,065,624,962 (B_C321 r6). [U19]

**What acceptance rests on**, for each accepted formula:
1. Formula identity: the CNF is regenerated in memory from pinned sources and its SHA equals the pin. In the parent
   replays B_C321-a3, B_C411-p3, A_C311cuts-p2 and B_C311cuts-p2 (and in the producer C311+cuts drivers) the bytes
   written to the solver and to the checker are each measured complete with SHA equal to the pin. In the parent
   A-cube replays (A_C321, A_C411) the feeds were pre-hashed immutable buffers with successful complete writes, not
   separately hashed write streams (A-cubes verdict 0ba3fe4f…). [U19]
2. Native exits: solver rc 20, drat-trim rc 0.
3. Exact status lines read from bytes, removing only CR: the singletons ['s UNSATISFIABLE'] and ['s VERIFIED'], with
   no NOT VERIFIED or TIMEOUT line.
4. Pinned binaries (solver and checker) at spawn and after the run; clean supervisor completion with no stop, signal
   or quarantine.

Complete measured CNF delivery matters because the checker's verdict refers only to the bytes it actually read.

**Residual boundary, explicitly not claimed:**
- No proof is retained, so no third party can re-check the same proof; re-verification means re-solving.
- No proof-byte identity between a producer run and its parent replay is claimed. The parent replays produced fresh
  proofs: kissat 4.0.4 for B_C321, B_C411, B C311+cuts and A C311+cuts (whose producer used CaDiCaL 3.0.1 and the
  lane checker), and the producer's own CaDiCaL binary for A_C321 and A_C411. Equal byte counts (B_C411 and
  B C311+cuts) are not identity. [U19]
- No retrospective proof digest exists for any run.
- drat-trim (lane build 111b0405…d5e4 for producer runs; parent build a46c0c71…8e37 for parent replays; source
  d834b649…c2ee) is trusted together with its compiler, the operating system and the hardware.
- This is the M7 exact-CNF replay standard named in the G2 and A-cut verdicts. It is **not** the separate, stricter
  n8 provenance protocol, and nothing here claims n8-level proof provenance.

## 14. Reused controls and chronology [U13]

No control below was rerun for the accepted replays; each is hash-bound and reused. Times are host-clock PDT.

| Control | Receipt (SHA-256) | Recorded | Relation to the production it supports |
|---|---|---|---|
| Three-cube coverage (18 assignments, 3 disjoint orbits) | `L/evidence/k3cubes/coverage_r1.json` 14d00a2d…f0f3 | before the AMENDMENT-2 freeze at 19:32:24 (10-17) | before every K3 cube CNF search |
| Exact G6 controls | `L/evidence/k3cubes/g6_controls_r1.json` edd313eb…2615 | 20:15:24 (10-17) | after the exploratory A screen began (about 20:14), before every certificate; G6 is redundant by `G6-G2-DERIVATION.r1.md` |
| Lex comparator controls (lengths 1–4, 22 generators) | `L/evidence/k3cubes/lex_controls_r1.json` 3bd546ad…4053 | 21:20:47 (10-17); re-run in process by `k3_lex make`, which wrote the lex input at 21:20:58 | before the lex input existed; corroboration only for the general-length argument |
| Matched component controls, both encoders (26/26) | `L/evidence/gram/review_controls_r1/summary.json` 6ce1ddc2…d685 | 21:24:52–21:25:09 (10-17) | after K2 production (the K2 verdict's README:91 deviation), before the first K3 certificate (A/C321 producer, 21:39:49) |
| Transport controls r2 (UNSAT accept; SAT, invalid-proof and early-writer reject) | `L/evidence/gram/transport_controls_r2/summary.json` 34a69ae6…95e6 | 21:38:40–21:38:43 (10-17) | before the first K3 certificate |
| No-duplicate in-memory regeneration controls | `L/evidence/k3cubes/no_duplicate_regen_controls_r1.json` 024cb624…0f6f | 23:04:46 (10-17) | before every direct-B producer run (from 23:58) and every C311+cuts run |
| Runtime B-map oracle (0 of 2646 differ) | `L/evidence/k3cubes/bmap_oracle_r1.json` 6e2bd95e…952c | 00:49:18–00:49:40 (10-18) | before every relied-on B certificate (B/C321 r5 onwards); the B cube CNFs were written earlier, at 20:14:50–53 (10-17) |
| Cut block generator r1 (C1: 450 of 2100 rejected; classical 0; Ψ(f) (2940, 0); mutations; invariance) | `L/evidence/k3cubes/cuts_r1_receipt.json` 9cfc0e81…babbf | 01:00:59–01:02:16 (10-18) | before AMENDMENT-4 drafting |
| Supervisor controls r3 (P1–P12, S1–S15) | `L/evidence/k3cubes/supervise_controls_r3.json` 3c77be50…99de | 03:32:18–03:32:53 (10-18) | before every C311+cuts run (first 03:36:50) |
| Generator r6 controls C1–C4 (re-bound to AMENDMENT-4.r4) | `L/evidence/k3cubes/cuts_r6_receipt.json` 9624d612…4a24 | 03:33:35–03:34:36 (10-18) | same |
| Appender, parser and transport controls r5 (C5–C8) | `L/evidence/k3cubes/cuts_cert_controls_r5.json` bb9445a2…b3e3 | 03:34:47–03:34:54 (10-18) | same; the strengthened SHAs 18583aab… and ae3b8309… are first recorded here |
| Parent A-cube desk self-checks X1–X3 (UNSAT accept, SAT reject, wrong-CNF proof reject) plus parser and verdict logic | `R/moqls7-k3-cube-parent-replay-v1/receipts/v1-selfcheck-summary.json` 8b62446c…6171 | 00:58:59–00:59:00 (10-18) | before the parent replays A_C321 (start 00:59:06) and A_C411 (start 01:34:51) |
| Parent B desk self-checks X1–X3 (UNSAT accept, SAT reject, wrong-CNF proof reject) | `R/moqls7-k3-B-cube-parent-replay-v1/receipts/selfcheck-summary.json` ec246769…739b | 04:22:09 (10-18) | before every replay by that desk (B_C321, B_C411, A C311+cuts, B C311+cuts); reused, not rerun (G2 verdict) |

Parent rulings that bound these controls: README:91 is applied at component level (AMENDMENT-4 disposition decision
2: no genuine K3 positive can exist; the cut clauses are checked against the five classical AG(2,7) triples; C1 is
re-bound to the frozen text). The K2 verdict records that the 26 matched controls ran after K2 production.

## 15. Lower bound M(7) ≥ 2: the published construction [U14]

Source: Ball–Simoens arXiv:2607.12933v2 (pinned PDF 2d60d45f…21afe; layout text df1d8b14…4219), Theorem 6 with
Lemmas 12–14, Example 15 and Corollary 7 (layout lines 57–62, 240–262, 296–336, 352–389). Alternative citation in
the accepted baseline verdict a39911fd…3ff2: Huang–Li Theorem 5.2.

Construction at q = 7 (R = F_7, generating character χ(x) = ω^x with ω = e^{2πi/7}):
- Corollary 7 with d = 3, the largest proper divisor of q − 1 = 6: H = {1, 2, 4} is the multiplicative subgroup of
  order 3. Example 15: f0(x) = x for x ∈ H and f0(x) = 0 otherwise. f0 determines q + 1 − |H| = 5 directions, so
  M0 = {2, 6} is the set of undetermined directions (x ↦ f0(x) − mx is a permutation exactly for m ∈ M0).
- As in the proof of Theorem 6, shift by m0 = 2: f(x) = f0(x) − 2x, that is (f(0), …, f(6)) = (0, 6, 5, 1, 3, 4, 2),
  a permutation, and M = M0 − 2 = {0, 4}.
- Ψ(f) has entries ψ_ij = (1/√7) Σ_{x∈F_7} ω^{i f(x) + j x} |x⟩ (i, j ∈ F_7). It is a QLS (Lemma 12, since f is a
  permutation) and non-classical (Lemma 13, since f is not additive plus a constant: f(0) = 0 and f(1) = 6 would
  force f(3) = 18 = 4, but f(3) = 1).
- Φ(4) has entries φ_ij = |4i + j⟩. It is a classical QLS, and Ψ(f) ⊥ Φ(4) by Lemma 14, because 4 ∈ F_7^* and
  x ↦ f(x) − 4x, that is (0, 2, 4, 3, 1, 5, 6), is a permutation.
- So {Ψ(f), Φ(4)} is a non-classical set of 2 MOQLS(7), and M(7) ≥ 2.

The lane used exactly this pair as a genuine control: its Gram support is exact (g(p,q) = 1 iff x ↦ (k−i) f(x) +
(l−j) x is not a permutation, since a sum of seven seventh roots of unity vanishes iff each occurs once), and both
encoders accept it (`GRAM-ENCODING.r2.md` §4; `code/gram_controls.py`, `code/gram_controlsB.py`,
`code/g6_controls.py`). The lower bound itself is the imported published result; the lane check is corroboration.

## 16. Imports and trust base (complete list) [U15]

Mathematical imports:
- Ball–Simoens arXiv:2607.12933v2 §2.2–2.3: the definitions of QLS(n), orthogonality, set isotopy (entry phases,
  simultaneous row/column permutations, a separate unitary per square), classical sets and M(n); (C0) rests on them
  (`LEMMAS.md` §C0).
- Ball–Simoens Lemma 10 ([2, Lemma 13]), through its printed proof, in the basis-free form of `LEMMAS.md` lines 54–67.
- Ball–Simoens Theorem 6, Lemmas 12–14, Example 15 and Corollary 7 (the lower bound, §15); alternatively Huang–Li
  Theorem 5.2.
- Egan–Wanless arXiv:1406.3681v2 (pinned PDF f01b494f…27e0): the classification tables (Tables 5 and 6) and
  Theorem 3.2, through K1 (4-net classes) and K2 (147 main classes, with the parent LS147 check).
- Parent verdicts used as premises: baseline a39911fd…3ff2 (not needed for M(7) ≤ 2), K1 1cd0603c…dfb8, K2
  25ecb6ba…1242 (with its 35-class provenance caveat), K3 cover disposition fbfc0e10…f369, AMENDMENT-4 disposition
  3c9373c0…4e44 with the header erratum effec3db…b148, A-cubes 0ba3fe4f…1f97, H3 edba465a…abca7 (read with erratum 1
  9559a54b…17b5), G1 639fbf6b…b47f, G2 d41253f6…7aa7, A C311+cuts b18472b2…93a8, B C311+cuts
  10a65127…fbd3. [U19]
- Runtime evidence for encoder B's variable map: the B-map oracle 6e2bd95e…952c.

Computational trust base:
- Untrusted proof producers: CaDiCaL 3.0.1 (601c9fa8…d1fa) and kissat 4.0.4 (05d6f3e9…a848).
- Trusted checker: drat-trim, upstream source d834b649…c2ee; lane build 111b0405…d5e4, parent build a46c0c71…8e37.
- Trusted: CPython (/usr/bin/python3 3.9.6 for the lane drivers and encoders; parent tools as recorded in their
  receipts), the C compiler, macOS and the hardware.
- Proof streams are not retained or hashed (§13). There is no formal (Lean) verification.

## 17. r5 fix map (status update and reference sections; no logic change) [U16]

| Tag | Change | Where in r5 |
|---|---|---|
| U0 | Header: unfrozen r5 draft, binding of r4, freeze condition, kept section numbers | Header |
| U1 | Link 8: B_C321-a3 PASS; G1 ACCEPTED (639fbf6b…) | Link 8 |
| U2 | Link 9: B_C411-p3 PASS; G2 ACCEPTED (d41253f6…) | Link 9 |
| U3 | Link 10: G1/G2 accepted and Link 7 accepted at conditional scope; final reconciliation remains | Link 10 status |
| U4 | Link 12: exact-CNF ACCEPTED UNSAT (b18472b2…) with the A_C311cuts-p2 replay records | Link 12 status |
| U5 | Link 13: desk p1 UNKNOWN; p2 running; replay pending (superseded by U19) | Link 13 |
| U6 | Link 14: final verdict after the B-cut verdict and both final reviews (B-cut verdict now exists, U19) | Link 14 status |
| U7 | §3: pointer to §15 | §3 step 3 |
| U8 | §4 obligations refreshed | §4 |
| U9 | File-index additions | end of §6 |
| U10 | New non-contributing attempts (desk B_C411-p1, p2; A_C311cuts-p1; B_C311cuts-p1) | §10 |
| U11 | Exact A/B formulas | §12 |
| U12 | Proof-stream boundary (no digest; not the n8 protocol) | §13 |
| U13 | Reused controls and chronology | §14 |
| U14 | Lower-bound construction at q = 7 | §15 |
| U15 | Complete imports and trust base | §16 |
| U16 | This fix map | §17 |
| U17 | Pre-freeze changes (final-draft-1 55335a3b…94e4): header (derivation from the lane draft 0dbaefe3…2486, freeze rule); Link 13 p2 start records; §4 item 1; §6 additions; §10 pointer; §12 status cell; new §18 result section (placeholders, filled under U19) | Header, Link 13, §4, §6, §10, §12, §18 |
| U18 | Desk report template erratum ("Both logs are empty (0 bytes)") | §5 |
| U19 | Freeze: placeholders filled only from the parent raw audit 024e636d…cab9 and the B-cut verdict 10a65127…fbd3; Link 13 exact-CNF ACCEPTED UNSAT; Link 14 status; §4; §5 (B report line 25, A-audit byte-count label); §6; §10 (UNKNOWN audit attempt); §12; §13 (B_C311cuts-p2 proof bytes, no identity); §16; §18; header frozen | Header, Links 13–14, §4, §5, §6, §10, §12, §13, §16, §18 |

No link statement, premise, argument or conclusion changed; the errata added in §5 concern only desk report wording
and an audit byte-count label (U18, U19). §3 (the conditional M(7) = 2 consequence) is unchanged and still
conditional on acceptance of Link 14; M(7) is not claimed.

## 18. Encoder-B C311+cuts parent replay result [U17] [U19]

Every value below is copied from the parent's raw audit `R/moqls7-B-C311cuts-parent-audit-v1.json`
(024e636da51941a0bdbf8ebb62c35ea6ca02ca9f77c1a4eb52bb4d90a349cab9, recorded 12:08:22) and the parent verdict
`R/moqls7-k3-B-C311cuts-parent-verdict-v1.md` (10a65127d17bb8b8df0bccb42a7722eee86e3891b15189d5279ed616660cfbd3,
recorded 12:09:07). The fields mirror the A-side record in Link 12. A stop of any kind would have left the attempt
UNKNOWN; none occurred.

- Desk attempt: B_C311cuts-p2 (slot 2; launcher `scripts-v14/launch_B_v14.py` a182058c…6589; supervisor wall
  10,200 s).
- Attempt receipt `R/moqls7-k3-B-cube-parent-replay-v1/receipts/B_C311cuts-p2.json` edfbb2f1…241e; driver receipt
  `receipts/B_C311cuts-p2.driver.json` 8bb2ae36…511c.
- RESULT `RESULT.B_C311cuts-p2.json` 45eee709…c3f5; deviations `deviations-B_C311cuts-p2.json` 948c4b31…cdfa; REPORT
  `REPORT.B_C311cuts-p2.md` (its line 25 is false, §5 U18; the raw byte counts govern).
- Status: desk **PASS**; parent raw audit **PARENT_AUDIT_PASS**, with all 43 assembled conditions true and all 39
  grouped parent predicates true (no failed parent predicate).
- Solver kissat 4.0.4 (05d6f3e9…a848), `-q -f --time=5400`: self-exit 20 with exactly `s UNSATISFIABLE`; wall time
  2,245.714 s; raw log 16 B, bde6e1ee…a162.
- Checker, the parent drat-trim (a46c0c71…8e37), `-i -t 9000`: self-exit 0 with exactly `s VERIFIED` after removing CR
  only; neither log contains `NOT VERIFIED` or `TIMEOUT`; raw log 478 B, d55db210…30f2. The checker reports consuming
  842,063,946 proof bytes.
- Feeds: both measured feeds wrote all 38,353,647 B with SHA-256 ae3b8309…783a; header `p cnf 461370 1867942`.
- Pipeline: 2026-10-18 10:55:09–12:05:22 PDT, 4,212.783 s.
- Supervision and settlement: no stop, signal, quarantine or remaining owned child is recorded; the audit predicates
  `pipeline_no_stop`, `supervisor_clean`, `supervisor_rss_cap`, `release_and_quiescence`, `binaries_bound_each_stage`,
  `parent_checker_build` and `source_and_native_pins` are true. Supervisor record 40f8f9ee…0dd8; launch outcome
  3a75b121…6d91.
- Proof provenance boundary: the proof stream has no recorded digest and is not retained. No proof-byte identity with
  the producer is claimed or reconstructed; the equal byte count with producer r6 is not identity (§13). This is the
  existing M7 exact-CNF protocol, not n8's stricter stream-digest protocol.
- Parent raw audit: `R/moqls7-B-C311cuts-parent-audit-v1.json` 024e636d…cab9. Its first attempt,
  `R/moqls7-B-C311cuts-parent-audit-attempt1-UNKNOWN.json` 1ccf778b…aa21, is retained as UNKNOWN (§10).
- Parent verdict: `R/moqls7-k3-B-C311cuts-parent-verdict-v1.md` 10a65127…fbd3, **ACCEPTED UNSAT for the exact
  encoder-B C311+cuts CNF**.
- Effect: Link 13 is exact-CNF ACCEPTED UNSAT, and with Link 12 both C311+cuts formula obligations are accepted. The
  verdict's composition boundary applies: the cut-transfer, normalisation and encoder-necessity premises are
  reconciled only in the final composition verdict. Link 14 stays PENDING until the final parent composition verdict
  (decision 8), after both final composition reviews of this r5. M(7) is not claimed.
