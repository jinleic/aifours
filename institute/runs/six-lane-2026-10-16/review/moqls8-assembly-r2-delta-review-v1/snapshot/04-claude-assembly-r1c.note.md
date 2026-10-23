**DISPOSITION: ACCEPT-WITH-FIXES** (conditional proof skeleton only). 0 FATAL, 0 MAJOR, 11 MINOR.

**Does the chain prove n=8?** Yes, under two conditions:
- the six S_j are refuted exactly as SOURCE00 §6 specifies, under the full predicate; and
- r1 is re-frozen against SOURCE10.

Under those conditions the chain proves that every set of 5 MOQLS(8) is classical in the sense of SOURCE09:223–225. That is Problem 16 at n=8, relative to the imported trust base.

**Is every accepted link used within scope?** Yes. Only one step is scope-sensitive: replacing four exact-B_C certificates with NF plus S6. SOURCE10:36 is the only authority for that step. It postdates r1, and r1 correctly marks it pending.

## Findings

### FATAL
None.

### MAJOR
None. I probed specifically for five failure modes and found none:
- a Boolean-cover claim on bare F_one;
- P4 or weight conditions leaking onto squares 2–5;
- name-map drift between the 42 units and the M_s tails;
- a missing S_j;
- a non-classical five-set that escapes row-0 standardisation or the witness step.

### MINOR

**m1. r1's link states are superseded** (SOURCE00:22, :88, :98–105, :113)
- SOURCE10 is timed 06:11:00, after r1's 06:00:41 freeze (SOURCE00:5). It records three things r1 still calls pending:
  - the Claude NF review (SOURCE10:14);
  - parent CORRECTNESS-ACCEPTED (SOURCE10:3);
  - parent binding of all six S_j (SOURCE10:26).
- r1 still reads "PENDING Claude + parent coverage/contract acceptance" and "binding: pending".
- The error is conservative. But under SOURCE00:5, r1 cannot be the object of the final composition verdict.
- *Repair:* freeze an r2 that pins:
  - SOURCE10 (`4748f023…7826`);
  - the Claude NF note (`a1a8eb7d…3805`);
  - BINDING.json (`5e1116e8…f98c`).
- Print the six bound hashes next to SOURCE00:100–105. SOURCE10:26 only says they "equal the worker r2 hashes".
- Then set: binding = bound, UNSAT = pending, composition verdict = pending.

**m2. The amendment's reach is not reconciled with U's accepted text** (SOURCE10:36; used at SOURCE00:90, :111)
- SOURCE10:36 amends only "item 3" (SOURCE01:14).
- Other accepted U text, read together (SOURCE00:28; SOURCE01:5–8), still says 16/16:
  - SOURCE01:37: "All16 cases required".
  - SOURCE01:41: "After16/16 qualifying refutations … intended negative controls".
  - SOURCE03:105–110: "The ONLY permitted final implication is conditional on ALL of: … 16/16 strict refutations … fail-closed controls".
  - SOURCE02:93: "verified UNSAT of ALL16".
- The amendment is logically sound. NF plus UNSAT of all six gives literal Boolean UNSAT of the four exact B_C. That is all U's contradiction consumes (SOURCE02:93–95; SOURCE05:30–31).
- Read literally, though, the final step is still unlicensed.
- *Repair:* r2 §7 should list the amendment as an explicit antecedent, superseding SOURCE01:37/:41 and SOURCE03:108–110 (items 3–5) for P1-B1/B2/B3/B5 only. The twelve direct leaves stay under the original contract. A one-line parent erratum to SOURCE10 would also help.

**m3. The S6 predicate is restated incompletely** (SOURCE10:37–40 vs SOURCE01:40–41)
- The "unchanged F4" bullets omit five elements:
  - solver/checker self-exit, with no guard/relay/feed error;
  - recorded proof-stream SHA and byte count;
  - raw-log hash binding (the inherited parser strips whitespace, SOURCE01:40);
  - exclusion of LRAT-only and proof-free outcomes;
  - the negative-control clause (SOURCE01:41; SOURCE03:110).
- These are incorporated by reference, but the list invites a weaker reading.
- *Repair:* r2 §6 should state the full predicate verbatim, using SOURCE01:40 plus the controls clause of :41, or the SOURCE00:69 form.
  - Bind the feeds to the BINDING.json hashes.
  - Say whether the six replays get their own controls or inherit those of SOURCE07:23.
  - Unit flips that fail by unit propagation alone count only as binding controls (SOURCE00:71).

**m4. Wording of the final implication** (SOURCE00:19–20, :84, :111)
- (a) SOURCE00:111 says "then NF refutes the remaining four B_C". NF refutes nothing. NF plus the six certificates imply Boolean UNSAT of the four.
- (b) Step 3 at SOURCE00:19 is stated across templates ("one of those four → one of six"). The accepted lemma is per-C, with the same 42 units (SOURCE05:20–26; SOURCE10:9). That per-C form is what makes both of B2's and both of B5's S_j necessary.
- (c) SOURCE00:84 says "iff", but the accepted lemma runs one way only. The converse is trivial, because S_j's clauses contain B_C's (SOURCE00:96), and it carries no load.
- (d) The antecedents at :111 omit the m2 amendment and the mandatory final verdict (SOURCE10:42). The verdict appears only at :22.
- *Repair:* rewrite as: "for each C ∈ {P1-B1,B2,B3,B5}, by the accepted NF lemma, UNSAT of every S_j with source C implies Boolean UNSAT of B_C". Add both missing antecedents.

**m5. The trust boundary omits the shift for the four P1 leaves** (SOURCE00:113, :115)
- The twelve direct leaves rest on DRAT certificates of the exact B_C.
- The four P1 leaves would rest on two different things:
  - a written lemma reviewed by two models, plus a finite/format check (SOURCE10:13–20); SOURCE05:161 says it is "not compiled into DRAT, Lean or an independently checked clause audit";
  - certificates of *different* formulas (the S_j).
- *Repair:* state this split explicitly in r2 §7.

**m6. W8 scope is overbroad** (SOURCE00:32)
- r1 says "W8 bounds every frame support by3".
- The accepted W8 is only the row-0 standard-form bound (SOURCE06:13: "In row-0 standard form the five supports at a cell are disjoint and avoid the column coordinate, so weights are ≤ 3").
- The column-0-frame bound is proved inside T16 (SOURCE04:9–18).
- *Repair:* say "off-row-0 entries in row-0 standard form". Attribute the any-line form to T16 §1.

**m7. T16's authority and import range are not stated** (SOURCE00:44)
- r1 says "ACCEPTED by U". The actual acceptance is item 1 of the parent disposition (SOURCE01:12).
- The admissible text is the F3 range in SOURCE01:29:
  - TPL LF9–19, with LF20's justification replaced;
  - LF22–55;
  - LF60–64, minus the reduced-K5/P4 sentence;
  - LF66–109.
- Excluded: LF1, LF4–5, LF59 and LF111–131. These lines still assert the 13-case/c112/reduced-K5 interface (SOURCE04:1, :62, :111–113).
- *Repair:* cite SOURCE01:12 and the SOURCE01:29 ranges explicitly.

**m8. Undefined "G1", and NF's dependency wording** (SOURCE00:86; SOURCE10:9)
- r1 says "primary G1–G5". No G1 family is defined in any inlined source. SOURCE05:88–96 treats constants plus G2–G5.
- If r2 quotes SOURCE10:9's "uses only G2/G3 support facts", it must qualify the claim:
  - Only the local permutation-count lemma (SOURCE05:33–78) uses G2/G3 alone.
  - The model transformation also needs invariance or re-extension of G4, G5, the constants, SB2, the kept Q1 P4, ROWLEX/lexeq, and the AND/u5 definitions.
  - It also needs the absence of classical-L and fixg (SOURCE05:82–123; SOURCE10:25).
- *Repair:* write "constants and G2–G5", and quote the qualified dependency.

**m9. The M-tail fingerprints are not pinned** (SOURCE00:96)
- r1 says "matches the independent parent M-tail fingerprints" but pins no artifact or SHA.
- The confirming check came later, in SOURCE10:22–24:
  - the ID formula 1568(s−1)+49c+7i−6 on map `7b4dd597…b197`;
  - the SB2 decode, 1765;
  - tails rebuilt for s=2..5.
- *Repair:* pin the fingerprint artifact and SOURCE10:22–24. State that the 42 units (s=1) and the three tails used (s=2,3,4) decode against the same map as the WMAN units (SOURCE01:28; SOURCE00:34).

**m10. Hygiene in the target statement** (SOURCE00:11, :17, :26)
- (a) The reduction relabels squares (SOURCE02:59; SOURCE03:37). Relabelling is not an isotopy (SOURCE09:220–222).
  - This is harmless, because a t-MOQLS is a *set* (SOURCE09:215–217).
  - Phases and permutations never change membership in {|1⟩,…,|n⟩}. So set-classicality (SOURCE09:223–225) equals every square being classical, which is how A8's "wholly classical" must be read.
  - r1 should say this.
- (b) "Genuine(ly) non-classical" collides with the paper's "not genuinely quantum", which means classical (SOURCE09:201, :223). Define "genuine" as "realised by vectors in C⁸, not a Boolean model".
- (c) SOURCE09:209–215 is garbled by extraction (stray "n" lines, "C ⊗ C"). Note that SOURCE00:11 reads it as an orthonormal basis of Cⁿ⊗Cⁿ.

**m11. The accepted NF text is r2 as qualified by SOURCE10** (SOURCE00:86)
- Five Claude MINORs were dispositioned as wording-only and were not applied (SOURCE10:30).
- The r2 text still labels itself "UNREVIEWED" and "PENDING" (SOURCE05:1, :7, :161).
- *Repair:* cite "NF r2 read with SOURCE10:28–32", with SOURCE10:9 as the operative claim.

## Audit answers

### 1. Target fidelity: PASS
The definitions in SOURCE09:
- **Quantum Latin square** (SOURCE09:195–196): "an n × n matrix over Cn such that each row and each column forms an orthonormal basis".
- **Orthogonality** (SOURCE09:209–215): "{ψij ⊗ ϕij …} … is an orthonormal basis of C ⊗ C", i.e. of Cⁿ⊗Cⁿ.
- **Isotopy of sets** (SOURCE09:220–222): "(i) multiplying each entry by a phase factor, (ii) permuting rows and columns, simultaneously among all squares, and (iii) applying, separately to each square, a unitary transformation".
- **Classical** (SOURCE09:223–224): "classical … if, up to isotopy, all entries are contained in {|1⟩,…,|n⟩}".
- **Problem 16** (SOURCE09:642): "Is a set of n − 3 MOQLS(n), n ≠ 4, necessarily classical?"

How SOURCE00 matches:
- At n=8, n−3=5 and n≠4 holds.
- SOURCE00:11 matches the definitions term for term, with scope restricted to n=8.
- Every move in U and T16 is either an isotopy or a harmless relabelling (m10a):
  - row-0 standardisation is (iii) (SOURCE09:287–289);
  - common row/column moves are (ii);
  - P_σ applied to every square is (iii) (SOURCE03:34–35).

### 2. Interfaces: PASS

**U → T16.**
- U's output normal form (SOURCE02:55–69) is T16's hypothesis verbatim (SOURCE03:15–17): row-0 aligned, with (1,0) supports {1,2,3},{4},{5},{6},{7}.
- T16 assumes nothing about squares 2–5 beyond the QLS/MOQLS axioms (SOURCE03:26–28).

**T16 → D12/NF.**
- T16 outputs a model of an exact B_C (SOURCE01:13; SOURCE03:45–57).
- This covers genuine images only (SOURCE00:46; SOURCE04:122–123). No step needs more than that:
  - D12 is exact-formula UNSAT.
  - NF's hypothesis is "every Boolean model of B_C" (SOURCE10:9), which is weaker than "genuine image".
- The D12 formula and receipt hashes (SOURCE00:56–67) match SOURCE07:7–16 and SOURCE08:7–8 row for row.

**P4 and weight conditions.**
- Only Q1 carries P4: the kept ALO (SOURCE00:35) and the witness flag at (1,0).
- Squares 2–5 carry none, in F_one, T16, NF (SOURCE05:113–116) or S6 (SOURCE00:96).
- A8 supplies one weight-3 entry somewhere in the set, not P4 on each square (SOURCE00:32).
- M_s only requires singleton column-0 supports in rows 2–7 (SOURCE05:17–18, :153–157). It is not a classicality condition.

**Units and tails.**
- The units are g₁((0,c),(i,0)) for i=2..7, c=1..7 (SOURCE03:71). The tails are ¬g_s(c) ∨ ¬g_s(d) (SOURCE10:9).
- Both decode against the same map. The ID formula is injective on c,i ∈ 1..7, and 1568+196+7−6 = 1765 confirms the SB2 decode.
- S_j = new header + unchanged B_C body + 126 tail clauses (SOURCE00:96; SOURCE10:26).
- Clause counts check out: 5740230 − 4 = 5740226; + 42 = 5740268; + 126 = 5740394, where 126 = 6 rows × C(7,2).

**Is "SAT(B_C) ⇒ SAT(B_C ∧ M_s) for some s ∈ Rep(C)" what the contradiction needs?**
- Yes. The contradiction needs ¬SAT(B_C) for each of the four templates. Given NF, that holds exactly when every S_j with that source is UNSAT.
- The representatives {2}, {2,4}, {2}, {2,3} give exactly the six rows at SOURCE00:100–105.

**Is SOURCE10's amendment sound and sufficient?**
- It is sound.
- It requires all six refutations, including both of B2's and both of B5's (SOURCE10:36).
- It keeps the twelve direct refutations and keeps the final verdict mandatory (SOURCE10:42).
- It is sufficient once m2 and m3 are fixed.

### 3. Completeness of the case split: PASS
**Template count.**
- 16 = 6 (P0) + 6 (P1) + 4 (P2) (SOURCE04:84–104). The independent parent check also found 16 orbits (SOURCE01:23).
- D12 = 6 P0 + P1-B4 + P1-B6 + 4 P2 = 12.
- The remainder is exactly NF's domain: P1-B1, B2, B3, B5.

**No gap at the front end.**
- Row-0 standard form always exists (SOURCE09:287–289).
- A8's premise covers all five squares and all entries. So its contrapositive fires for every set that is not wholly classical, whatever the number of non-classical squares (SOURCE02:38–39, :55–57).
- W8 caps the weight at 3.
- The witness avoids its own column coordinate (SOURCE03:43; SOURCE09:297–299).
- The budget at (1,0) is 3+1+1+1+1 = 7, which forces the SB2 pattern (SOURCE02:64–67).

**NF's label coverage** (SOURCE05:141–145).
- B2 has orbits {4,5} and {6,7}, giving M2 or M4.
- B5 has at least 2 permutation squares, at most one with label 7. Label 4 gives M2; labels 5 or 6 give M3.
- No seventh S_j is needed.

### 4. Scope and wording: PASS with m1–m11
- No claim for all n (SOURCE00:11, :111, :113).
- No K4/K5 claim from old inputs (SOURCE00:113, :33, :38).
- No novelty claim (SOURCE00:3, :113).
- A8 is used without Egan–Wanless, K1 or K2 (SOURCE00:32 vs SOURCE06:13–15).
- Overstatements: m4, m6, m8.
- Hidden assumptions: m5, m10a.
- Unsupported citation: m9.
- Circularity: none. U and T16 use no refutation, NF is independent of S6, and A8 rests only on the primary Lemma 10 plus its own net argument.

## Audited versus imported

**Audited here, from the inlined text only:**
- the target statement against SOURCE09;
- every interface, and the case-split completeness, including the mapping from NF representatives to S_j;
- hash cross-references from SOURCE00 to SOURCE01–08 and SOURCE10;
- the deletion-index spacing of 1569, consistent with 56×28 one-way clauses plus 1 ALO per square;
- clause and variable arithmetic: the 509,915 auxiliary sum, 672 = 16×42, and the permutation-count bounds [1,1,2,3,2,4] from m = [12,14,16,18,17,20];
- scope labels.

**Imported, not re-derived:**
- SOURCE09's definitions and Lemma 10, and the fidelity of the raw text to the arXiv paper;
- A8/W8 and their independence from Egan–Wanless (only the outline in SOURCE06:13 is inlined);
- encoder necessity and canonical extension (K4K5 r3 and binding v2 are not inlined);
- the T16 component proof, sanity-checked only;
- NF's internal proof;
- all registry and byte identities;
- the D12 solver and checker facts.

The S6 refutations do not exist yet, so there was nothing to audit.

This audit has no gate authority and makes no novelty judgment.
