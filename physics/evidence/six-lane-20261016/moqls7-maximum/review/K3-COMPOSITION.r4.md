# K3 composition note r4 (phys-2, lane moqls7-maximum)

**r4 is a status refresh of r3** (`review/K3-COMPOSITION.r3.md`
b85daed48b15ebcc69ea2c8cdd54899911ce8565f9ceebe67a36cbdb01726aed), written 2026-10-18 from 08:21:45 PDT (host clock)
at the parent's request. It changes no logic: every link statement, premise, argument and conclusion is r3's. Only
link statuses, the open obligations and the file index are refreshed to the writing time, and §10 lists the attempts
that ended UNKNOWN as non-contributing. The r4 fix map is §11 and the unified diff is
`review/K3-COMPOSITION.r3-to-r4.diff`. Earlier fix maps: r2 §7 (Codex F1–F3), r3 §8 (Claude m1–m9).

Statuses in r4 are those at its writing time. Later events are recorded in the lane README and LOG and, if needed,
in a new version of this note. [S0]

r1 was written at the parent's request: a static note giving the exact chain from the K1/K2 reduction to "no triple
with three non-classical squares", with each link's statement, files, SHA-256 and status. This version is frozen by
`cp -n` from `review/drafts/K3-COMPOSITION.r4.md` and never rewritten.

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
- **B_C321** (8b7b8124…12c6): **PRODUCER**.
  - Receipt `L/evidence/k3cubes/cert_B_r6/B_C321.json` 2ffc2fa8…32ac: rc 20/0, ["s VERIFIED"], 4035.475 s; driver
    `k3_direct_B_r6.py` 24fcfea8…c44d; delta r6 5beb6009…1eb8.
  - An earlier r5 attempt was UNKNOWN on the checker clock (b07100e3…7614).
  - Parent replay desk `R/moqls7-k3-B-cube-parent-replay-v1/`:
    - first attempt UNKNOWN, floor stop at 04:53:03 (receipt `receipts/B_C321.json` 30017291…d117);
    - attempt a2b UNKNOWN, floor stop at 07:04:14 after solver rc 20, no checker verdict (receipt
      `receipts/B_C321-a2b.json` b558c3ee…9874; RESULT.v2.json 49e61ef6…373a);
    - attempt a3 **RUNNING** at the writing time (launch receipt `receipts/B_C321-a3.launch.json` 57989320…0cde). [S2]
- **Gate G1**: **PENDING**. It is discharged by a parent verdict naming A_C321 d598507d…8388 (parent-accepted UNSAT,
  verdict 0ba3fe4f…1f97) and B_C321 8b7b8124…12c6 (producer certificate cert_B_r6 2ffc2fa8…32ac, needing a passing
  parent replay). [S2]

### Link 9 (gate G2: C411 excluded on A and B)
- **A_C411** (2b92f5b1…ddf2): **ACCEPTED UNSAT**.
  - Same verdict; parent replay receipt 308e255e…7442.
  - Producer receipt `cert_r2/A_C411.json` 5f117b60…a23cf.
- **B_C411** (01acf464…8bf8): **PRODUCER**.
  - Receipt `L/evidence/k3cubes/cert_B_r7/B_C411.json` 644b5b23…6f75: rc 20/0, ["s VERIFIED"], solver log
    "s UNSATISFIABLE", 4181.588 s; driver `k3_direct_B_r7.py` 386bff0c…4cfa; delta r7 55b40519…ade4.
  - Earlier attempts were UNKNOWN: r5 on the checker clock (1acc121b…7dfc), r6 at the free-space floor (92354254…0184).
  - Parent replay **PENDING**: queued under the parent launcher v11, after its Codex review. [S3]
- **Gate G2**: **PENDING**. It is discharged by a parent verdict naming A_C411 2b92f5b1…ddf2 (parent-accepted UNSAT,
  verdict 0ba3fe4f…1f97) and B_C411 01acf464…8bf8 (producer certificate cert_B_r7 644b5b23…6f75, needing a passing
  parent replay). [S3]

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
- Status: **PRODUCER**. Parent replay **PENDING**: queued under the parent launcher v11, after its Codex review. [S5]

### Link 13 (C311 + cuts on encoder B)
- Input: original B_C311 b3ec0108…c077 plus the block, giving strengthened input ae3b8309…783a (38,353,647 B, header
  461370/1867942). Solver kissat 4.0.4 (05d6f3e9…a848).
- Result: **PRODUCER**.
  - Driver receipt `L/evidence/k3cubes/C311cuts_B_r6/C311cuts_B.json` 1f003634…c535: rc 20/0, exactly
    ["s VERIFIED"] and ["s UNSATISFIABLE"]; both feeds were 38,353,647 B with SHA ae3b8309…; 4237.757 s.
  - Supervisor record `C311cuts_B_r6.supervisor.json` 43d48141…e4cb: completed_cleanly true, no trip, no quarantine,
    leader rc 0.
  - Delta r6 899a0437…0681; driver r6 12b141fd…db91.
- Parent replay: **PENDING**: queued under the parent launcher v11, after its Codex review. [S6]

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
- Status: **PENDING**: the final parent composition verdict (decision 8). [S7]

## 3. What M(7) would then equal, and exactly why

**If** the composition (Link 14) is accepted:
1. No MOQLS(7) triple has exactly 1, 2 or 3 non-classical squares (Links 1, 2, 14). By (C0), no non-classical
   triple of MOQLS(7) exists.
2. For t ≥ 3, a non-classical set of t MOQLS(7) would contain an individually non-classical square (C0). That square
   together with any two other members is a set of 3 MOQLS(7), because orthogonality is pairwise, and it is
   non-classical by (C0). This contradicts step 1. Hence M(7) ≤ 2.
3. The published non-classical pair (Ball–Simoens Corollary 7, or Huang–Li Theorem 5.2), cited by the accepted
   baseline verdict a39911fd…3ff2, gives M(7) ≥ 2.
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

## 4. Open obligations at the writing time, in dependency order [S8]

1. Parent replay of B/C321 (8b7b8124…12c6): attempt a3 is running.
2. Parent replays queued under the parent launcher v11, after its Codex review: B/C411 (01acf464…8bf8), B C311+cuts
   (ae3b8309…783a) and A C311+cuts (18583aab…2e5e).
3. The G1 verdict (A_C321 d598507d…8388 accepted; B_C321 8b7b8124…12c6 after its replay) and the G2 verdict (A_C411
   2b92f5b1…ddf2 accepted; B_C411 01acf464…8bf8 after its replay).
4. The final parent composition review (decision 8), covering Link 3 applied to K3, Link 10 with G1–G2, Link 11 and
   Link 14. Link 7 (H3) is already accepted at conditional scope.

   Only then can any K3 or M(7) verdict follow.

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

The desk's B_C321 a2 has only a gate record (`receipts/B_C321-a2.gate.json`) and no pipeline receipt.

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
