DISPOSITION: ACCEPT-WITH-FIXES

## FATAL

none.

I found no unsound clause, reduction, symmetry, missing class or circularity. The static checks behind this (items 1–6, all by reading and hand reasoning) follow.

- **Item 1 (G1–G3).**
  - **G1:** this is the ONB axiom on rows and columns, and follows from C1 on L's symbol lines.
  - **G2:**
    - Take ⟨·,·⟩ conjugate-linear in the first slot. Then ψ_p = Σ_{r∈ℓ} G(r,p)ψ_r, so G(p,q) = Σ_r conj(G(r,p))G(r,q).
    - Since |G(p,r)| = |G(r,p)|, g is symmetric. Count 0 forces G = 0, and count 1 leaves a single nonzero product.
    - If p,q are collinear through another line, G(p,q) = 0, so count 1 is impossible. Both encoders emit this (`code/gram_enc.py:95-99`, `code/gram_encB.py:150-151`).
    - Terms with r collinear to p or q are constant 0.
  - **G3:**
    - The transition matrix U = B₁*B₂ is unitary, and net lines meet in at most one point.
    - A shared point s gives U[s,s] = 1. Row and column s then vanish elsewhere, and the 6×6 block is unitary.
    - Unit-norm rows give "a neighbour on ℓ₂∖ℓ₁", which also encodes nonempty supports. |U[r,q]| = 1 empties column q.
    - Both directions are emitted because ordered pairs are iterated (`code/gram_enc.py:100`, `code/gram_encB.py:158-161`).
    - Skipping zeros forced by third lines only weakens clauses.

- **Item 2 (G5).**
  - The 49 product vectors are unit vectors in C⁴⁹. Pairwise orthogonality is therefore the same as being an ONB.
  - Their inner product is G_a·G_b, which vanishes iff one factor does. So G5 is exact.
  - A unitary plus phases applied to L alone (isotopy (i) and (iii)) puts L in the standard basis without touching Ψ₁ or Ψ₂. Then ⟨ψ_p⊗|L(p)⟩, ψ_q⊗|L(q)⟩⟩ = G(p,q)[L(p)=L(q)], which is G1 on L lines.

- **Item 3 (G4).**
  - **Lemma 10 is basis-free.** The printed proof (`sources/2607.12933v2.layout.txt:185-192`) never uses standard form; weight is relative to any fixed ONB.
  - **Rotation preserves zeros.**
    - Suppose all weights are ≤2, supp u = {1,2} and v ⊥ u. One shared coordinate k would give ⟨u,v⟩ = conj(u_k)v_k ≠ 0.
    - So weight ≤2 forces supp v = {1,2} or disjoint from {1,2}.
    - U preserves span{e₁,e₂} and fixes e₃…e₇, so every zero of G_Ψ survives: g_Ψ′ ≤ g_Ψ pointwise.
    - Hence rows and columns stay ONBs, and orthogonality to both other squares holds simultaneously (Ψ′ is built without reference to Φ).
    - The weight-2 count strictly decreases and ends at 7 rays, i.e. classical.
  - **Global unitary.** A global V gives G_{VΨ} = G_Ψ.
  - **Minimality.**
    - m ∈ {1,2,3} attains a minimum m*, and K1 (`review/K1-THEOREM.r1.md:113-116`) gives m* ≥ 2.
    - Replacing a light square leaves m−1 ≥ 1 non-classical squares, still a non-classical set by C0.
    - No QLS is orthogonal to itself (that would need 49 orthonormal vectors in C⁷), so the result is a genuine 3-set.
  - **Encoded frames.** Weight in an own-line ONB equals the neighbour count on that line, and points on the line have weight 1. Restricting to the 21 (K2) or 14 (K3) frames is therefore a weakening.
  - **K2.** Once K1 holds, any K2 set has m = 2 = m*. Both quantum squares are non-classical by definition, so both are heavy on all 21 lines.
  - **Ordering.**
    - `review/GRAM-ENCODING.r1.md:54-55` is correct: K2-heavy UNSAT plus K1 excludes K2, and only then is every K3 set minimal.
    - While K2 is open, K3-heavy UNSAT excludes only minimal K3 sets.
  - **K1 §8.** It is unused by :47-51, and it would be insufficient anyway: it yields weight ≥3 only in the standard row-0 frame (`review/K1-THEOREM.r1.md:144-145`).

- **Item 4 (mathematics of the class reduction).**
  - **Transport.**
    - Any paratopism (any of the 6 class orders, plus relabelling inside classes) maps the 49 points and 21 lines of L's 3-net onto those of L′.
    - Carrying the vectors along keeps every line an ONB: rows and columns give a QLS, and L′ lines give ⊥L′ by C1.
    - It also keeps the same 49 product vectors, the same ray multiset and the same heaviness.
    - With sym off, both encoders treat all 21 lines uniformly, so CNF(L′) ≅ CNF(rep).
  - **Normalisation.** `code/ls_classes.c:32-60` is a complete normalisation.
    - A choice of (class order, origin o, ordering of o's class-a line) corresponds bijectively to a paratopism θ with θ(L) reduced. Row 0 fixes the column and symbol labels, and column 0 fixes the row labels (:46-50).
    - The fibres are cosets θ·Par(L). So the minimum key is a complete main-class invariant, its multiplicity is |Par| (free action), and a class has 211680/|Par| reduced squares.
  - **Completeness.**
    - Distinct correct keys whose counts sum to the published 16942080 prove completeness.
    - The BFS closure (:101-122) alone does not.
    - The decoders (`code/k2_classes.py:22-33`, `code/ls_classes.c:62-67`) match the key layout at :52.

- **Item 5 (sym).**
  - Once K2 is excluded, square 1 of any K3 set is heavy in every row frame.
  - Simultaneous row and column permutations (isotopy (ii)) bring the frame to row 0, the heavy point to (1,0) and three of its neighbours to columns 1–3.
  - No neighbour can sit in column 0, because (0,j₁) shares a column with (i₁,j₁).
  - These permutations permute lines and re-index the product ONBs. Every other clause survives, including the other 41 heavy clauses.
  - The three unit clauses imply the omitted (square 1, row 0) heavy clause. Transposition and square relabelling are unnecessary.
  - `code/gram_enc.py:123-126` and `code/gram_encB.py:191-194` are identical, and K3 uses only the 14 row/column lines (L = None).

- **Item 6 (clause families).**
  - **Encoder A:**
    - variables exist only for non-collinear pairs (:66-71);
    - h is a full equivalence (:83-85);
    - G2 (:95-99), G3 (:105-114) and G5 (:115-118) match the text;
    - the guarded (n−2)-subsets (:45-52, :127-137) force ≥3.
  - **Encoder B:**
    - counter2 (:41-57) is a true equivalence s1⇔≥1, s2⇔≥2 in both branches;
    - in G2, 0 items forces ¬g (:146-149), and 1 item is exact for non-collinear pairs (:154-155);
    - G3 (:166-183) and G5 (:184-187) match.
  - **Heavy (B).** counter_ge3 (:60-89) and the heavy disjunction (:188-202) are one-directional. Every genuine heavy pattern extends via c[i][k] := [≥k among the first i] and t := [≥3].
  - **Strength.** No clause is stronger than G1–G5. Underconstraint cannot invalidate UNSAT, and Boolean SAT is not realisation.

## MAJOR

**MAJOR-1 (items 4, 7): class-list completeness is not bound to evidence.**
Locations: `review/GRAM-ENCODING.r1.md:61-66`, `code/ls_classes.c:9`, `code/ls_classes.c:94-99`, `explore/ls_classes.stderr:149`, `manifest.json:681-694`.

- **Defect:**
  - The list comes from an unpinned binary (fe5e0857…, build not recorded).
  - It was run on unpinned seeds (19a19309…, 32 seed classes per `explore/ls_classes.stderr:1`).
  - The only completeness evidence is that binary's self-reported MATCH: an observed log, not a source-bound validation.
  - The normalisation and multiplicity lemma appears only as a code comment (`code/ls_classes.c:2-6`).
  - 16942080 and the McKay–Meynert–Myrvold count of 147 have no pinned source.
- **Hand checks (no counterexample found):**
  - Line 1 decodes to r+c (Z₇), with 120·1764 = 211680 and |Par| = 6·49·6.
  - Line 136 is a reduced Latin square (all rows and columns checked), with 210·1008 = 211680.
  - Line 2 is Latin, with 17640·12 = 211680.
  - Column 2 tallies to 44×211680 + 57×105840 + 16×35280 + 11×52920 + 4×70560 + 3×8820 + 2×17640 + 2×13230, plus singletons {26460, 21168, 14112, 11760, 2940, 1470, 210, 120}. That is 147 rows summing to exactly 16,942,080, and every red·par = 211680.
- **Correction:**
  - Write the normalisation proof into GRAM.
  - Rebuild from the pinned source, recording compiler, flags and binary hash, and re-run with pinned seeds.
  - Byte-compare the output to 898065c8….
  - Independently check that every key is a reduced Latin square, re-canonicalises to itself and has the stated |Par|.
  - Pin sources for both published constants.

**MAJOR-2 (item 6 driver, item 7): `code/gram_certify.py` does not implement the frozen protocol.**
Locations: `code/gram_certify.py:46`, `:56`, `:69-78`; `review/AMENDMENT-1.r1.md:30`, `:33`, `:42-43`; `README.md:96`, `:107`.

The build parameters themselves are correct. `make_cnf` (:39-56) produces the stated A and B K2/K3 builds, and `:all` expands to indices 0–146. The defects:

- **(a) No time cap.** No native limit is set for cadical or kissat, unlike `code/k2_classes.py:38` and `code/k2_classesB.py:58`. drat-trim's own limit is left at its default. The ≤3 h cap is not enforced.
- **(b) SAT models are lost.** `sout` (:71) is discarded, so a SAT model is neither kept nor decoded (contrary to AMENDMENT:33).
- **(c) Missing provenance.**
  - The record (:76-78) lacks code SHAs, the class-list SHA, the key, solver versions and binary hashes.
  - The drat-trim binary (111b0405…) is not bound to its source (d834b649…; `manifest.json:702-714`).
  - The frozen-control rerun promised at AMENDMENT:42-43 is not implemented.
- **(d) No cross-check.** VERIFIED is not checked against rc = 20 or the checker's exit status.
- **(e) Liveness.**
  - If the solver exits before opening the FIFO, drat-trim blocks in open(), so :72 hangs. The converse case hangs :71.
  - The checker's stdout pipe is not drained during `sp.communicate()`, so heavy output deadlocks both processes.
  - Nothing guards against `README.md:103`.

None of this can produce a false "s VERIFIED".

- **Correction:**
  - Add native limits (`-t 10800`, `--time=10800`) and an explicit drat-trim `-t`.
  - Persist solver stdout and decode models via vmap.
  - Record all SHAs and the key.
  - Accept a result only when rc = 20, the exact "s VERIFIED" line appears and the checker exits cleanly.
  - Drain checker output concurrently.
  - Add a SIGTERM watchdog with a bounded wait.
  - Re-run the controls first.

**MAJOR-3 (item 6 controls, item 7): controls miss the production paths, and the mutation control is uninformative.**
Locations: `code/gram_controls.py:53-71`, `code/gram_controlsB.py:47-65`, `review/GRAM-ENCODING.r1.md:79-83`, `review/AMENDMENT-1.r1.md:36-43`, `README.md:89-91`.

- **The mathematics is right (hand-checked):**
  - A 7-term sum of 7th roots of unity vanishes iff each root occurs once, because 1+z+…+z⁶ is minimal.
  - m0 = 2, f = [0,6,5,1,3,4,2], M0 = {2,6}, so M = {0,4} and m = 4.
  - f is non-additive: f(3) = 1 ≠ 3f(1) = 4.
  - The nonzero count is 1176 − 294 − 147 = 735, matching both JSONs. Zeros fall exactly on rows, columns and Φ(4) lines.
- **What the controls exercise:** only components. These are 2 squares with no net and no heavy, 1 square with net and heavy, and classical data with no heavy.
- **What they miss:**
  - Nothing runs 2 squares + net + heavy, or 3 squares + heavy + sym.
  - The sym branch never executes.
  - Encoder B has no mutation control.
- **GC4's "6 rejected":**
  - By hand, exactly six of the 40 picks (indices 22, 330, 484, 528, 550, 594 of :63-64) are Φ(4)-collinear 0→1 flips, which G5 alone rejects.
  - If the recorded split is accurate, all 34 single deletions passed. GC4 is no evidence that G2–G4 bite.
- **Unbound and unreconciled:** the JSONs carry no code or CNF hashes. The 4×4 control in README:89 is inapplicable (P = 7 is hard-coded) and has not been dropped.
- **Add, on frozen code, under both encoders, with hashes recorded:**
  - **(i) Sym, positive and negative.** In native coordinates, Ψ(f) gives (1,0) row-0 neighbours in columns {1,2,3,5,6} (g = 1 iff c ∉ {0,4}). So `build(1,None,heavy,sym)` with g1 fixed must be SAT. With columns 1↔4 swapped it must be UNSAT.
  - **(ii) Production-shape negatives.** GB4 data with `--heavy`, and the classical triple with heavy and sym, must both be UNSAT, since classical squares have weight 1 in their own frames.
  - **(iii) Transport and decoder.** Carry Ψ(f) from the Φ(4) net to the line-1 representative via i ↦ 4i, and through one conjugate, using `square_from_key`. One square with heavy must be SAT.
  - **(iv) Designed mutants per family** must be UNSAT: G2 exactly-one, G3 empty row, G3 singleton column, G4 light line.
  - **(v) End-to-end through the FIFO.**
    - A small UNSAT instance must give "s VERIFIED" with rc 20 under both solvers.
    - A tampered proof must give NOT VERIFIED.
    - A SAT instance must keep its model.
    - This also tests drat-trim's binary-mode detection on a non-seekable FIFO.
- These controls establish only admissibility and non-vacuity. Soundness rests on the static proof above, and no K2/K3 witness is required.

## MINOR

**MINOR-1 (items 3, 7): G4 cites K1 §8.**
- `code/gram_enc.py:15-16` grounds G4 in K1 §8, which is unaccepted and insufficient.
- `review/AMENDMENT-1.r1.md:18` does not say §8 is unused.
- Correction: cite GRAM G4 plus K1 §6 only.

**MINOR-2 (item 7): stale references and status.**
- These point to a deleted, unversioned draft: `review/AMENDMENT-1.r1.md:11`, `code/gram_enc.py:6`, `code/gram_encB.py:4`.
- `review/GRAM-ENCODING.r1.md:3` still says "lane draft", and its first sentence is split between :3 and :21 (`manifest.json:662`).
- Correction: fix in r2. Any edit to code docstrings changes the pinned hashes and needs a delta review.

**MINOR-3 (item 6): latent malformed or vacuous output.**
- `code/gram_encB.py:151` writes "None" if a collinear pair has exactly one product.
- `code/gram_encB.py:169`, `code/gram_enc.py:48`, `:106` and `:137` can emit empty clauses. Combining sym with a net emits None (`code/gram_enc.py:125`, `code/gram_encB.py:193`).
- None of these is reachable in production. In a 3-net, an off-line point is collinear with exactly 2 points of any line. So G2 has ≥3 items, G3 has 5 candidates and heavy has 5; in the 2-net these are ≥5, 6 and 6.
- If reached, an empty clause would let drat-trim verify vacuously.
- Correction: assert that L is Latin, that no clause is empty or contains None, and that sym implies L = None.

**MINOR-4 (item 6): fix-json handling differs between A and B.**
- `code/gram_enc.py:146` rejects collinear pairs marked nonzero; `code/gram_encB.py:209-215` silently drops them.
- The current control data contain none. GB4 collinearity in L1 and L2 forces p = q.
- Correction: add the same assert to B.

**MINOR-5 (item 6): driver parsing and labels.**
- `code/gram_certify.py:73-74` strips all whitespace, whereas AMENDMENT:28 and docstring :11 say only CR.
- `:52-53` routes any unknown ID to K3-B.
- Correction: use `rstrip('\r')` and reject unknown IDs.

**MINOR-6 (item 7): exploration outcomes appear in claim documents.**
- Affected: `review/AMENDMENT-1.r1.md:7-8`, `:36-41`, `:46-47`, and `review/GRAM-ENCODING.r1.md:79-83`, `:86-88` (including the ≤23.5 s runtimes).
- These are unpinned and unaccepted. Label them as exploration, and never use them as exclusion evidence.

**MINOR-7 (wording).**
- `review/GRAM-ENCODING.r1.md:54`: write "attains the minimum m* = 2".
- `:67`: transposition is unneeded.
- `:36`: write B₁*B₂.
- `review/AMENDMENT-1.r1.md:29` should restate the K2-before-K3 dependence.

**MINOR-8 (item 7): hashes.**
- All printed target hashes match the headers and `manifest.json:655`. GRAM:10-11 are abbreviated and should be printed in full.
- Both context mismatches are as recorded (`manifest.json:631-653`). By hand, "3c7e" sits at 0-based offset 57 of e61ab812…e113, not at the end. "ff3a2" does not occur in a39911fd…a3ff2.
- I could not see `review/K1-THEOREM.r1.md:64` or `README.md:7` themselves.

## Scope

**Checked by reading and hand reasoning (no tools, no execution, all arithmetic by hand):**
- both target documents in full, all inlined code, the class list, the Lemma 10 proof and Ex. 15, and the K1, README, stderr and manifest excerpts;
- G1–G5 necessity and the exactness of G5;
- the G4 minimality argument and that it depends on K1 alone;
- the transport and normalisation theory, and the sym WLOG;
- clause correspondence and extensibility of auxiliary variables;
- production collinearity counts;
- the control data, the classification of GC4's picks, the class-list spot checks and full sum, and the digest offsets.

**Could not check:**
- canonical keys and |Par| for 144 of the rows;
- whether the binaries match their sources, and the seeds;
- FIFO behaviour of the solvers and drat-trim;
- Theorem K1 and the published constants;
- the lines `review/K1-THEOREM.r1.md:64` and `README.md:7`;
- any SAT, UNSAT or runtime claim (none is accepted).

**Still open:**
- K1 (pending);
- MAJOR-1 to MAJOR-3;
- production certification of 147 K2 classes, then K3;
- whether K3 finishes within the cap.

**Answer to the question:** given Theorem K1 and a validated complete class list, verified UNSAT of the specified instances would exclude K2 and then K3. Any later change to pinned code or documents needs a delta review.
