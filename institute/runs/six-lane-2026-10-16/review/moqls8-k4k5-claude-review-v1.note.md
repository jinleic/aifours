VERDICT: ACCEPT-WITH-FIXES

**Per-bridge verdicts** (soundness bridge only; no exclusion is assessed or implied)
- **K5 bridge: ACCEPT-WITH-FIXES.** SB §1–§4 and §6 are mathematically correct. The K5 bridge uses only the class definition, Prop 1, Lemma 2, BS rules #2/#3 and vector-level moves. It does **not** use F3. It is conditional on M2 (the P4 frame set must be {row 0}), M3 (self-pairs) and gates C1–C7, C9–C12.
- **K4 bridge: ACCEPT-WITH-FIXES.** All-frames P4 is correctly derived from F3 for every set with exactly four non-classical squares. It is conditional on M1 (no inherited K5-SB2, ROWLEX or P4 on square 5), on M3, on gates C1–C6, C8–C12, and on the K4 split being declared in §6 form (SB LF 65 says only "intended").

Document keys: SB = K4K5_ENCODING_SOUNDNESS r2; KK = PROOF_K1_K2 r2; K3 = PROOF_K3 r2; BS = Ball–Simoens.

## Answers to (a)–(e)

**(a) F3 is implied, with the quantifier §5 needs.**
- KK LF 8 and K3 LF 9 are already invariant statements quantified over all sets ("no set of 5 MOQLS(8) has exactly one/two/three non-classical squares"). F3 (SB LF 14) is simply their conjunction.
- The route in SB LF 15–16 is also valid, provided T is first restandardised. Per-square unitaries preserve ray counts and Prop-1 orthogonality.
  - A square with a weight-3 entry in row-0 standard form has at least 9 rays (KK LF 14–17).
  - Every other square of T′ is a classical Lemma-10 output.
  - So 1 ≤ m(T′) ≤ #nc(T) ≤ 3, and T′ ∈ K_{m(T′)} = ∅.
- §5 applies F3 to a set that has been transposed, row-permuted, restandardised and modified by Lemma 10. That set is not a reduced set in any pre-fixed frame, so the universal form is required. That universal form is exactly what was proved.

**(b) Yes, for both K5 and K4. No counterexample exists.** At (1,0):
- Coordinate 0 is excluded (rule #2, since (0,0) = |0⟩).
- All 10 pairs of supports are disjoint. For pairs among the squares this is G2 with q = (0,k), i.e. rule #3. For L it holds because L(0,k) = |k⟩ and L(1,0) = phase·|L(1,0)⟩.
- Every support is nonempty, and |S1| = 3.
- Hence 3 + Σ_{s≥2}|S_s| ≤ 7 with each |S_s| ≥ 1. This forces every other support to be a singleton, and the five supports partition {1..7}.
- The target families have the same block sizes:
  - K5: {1,2,3},{4},{5},{6},{7}.
  - K4: {2,3,4},{5},{6},{7},{1}.
- So a σ fixing 0 exists. Applied to columns and coordinates simultaneously, it keeps (1,0) and row-0 standard form.

**(c) Yes, for every set with exactly four non-classical squares, however it arose.**
- For a row or column ℓ: transpose if needed, move ℓ to row 0 by a simultaneous row permutation, then restandardise. This turns ℓ-frame weights into computational weights and preserves ray counts and orthogonality.
- W8 in the new frame makes "no weight-3 entry" equivalent to "all weights ≤ 2". Lemma 10 then applies to that single Q_s.
- The result has exactly three non-classical squares: the other three Q's keep at least 9 rays, while L and Q_s′ are classical. This contradicts F3.
- The §4-normalised object is again such a set, so no minimality is used anywhere.
- The flags must range over Q1..Q4 only (M1(iii)).

**(d) Yes.**
- Per-square unitaries (BS LF 113 (iii)) preserve each square's Gram matrix. That fixes every g, the ray counts (= classicality, KK LF 14–17) and the frame weights.
- They also preserve ⟨ψ⊗φ, ψ′⊗φ′⟩ = ⟨ψ,ψ′⟩⟨φ,φ′⟩, hence set orthogonality. Phases are invisible to g.
- Transposition is **not** a BS isotopy (BS LF 107–113). It does, however, map a set of 5 MOQLS(8) to a set of 5 MOQLS(8) with the same per-square ray counts, which is all F3 needs.
- Lemma 10 changes only the treated square, keeps it orthogonal to all others (BS LF 189–192; KK LF 34–39), and outputs a classical square.
- No genuine Lemma-R regrid occurs in SB, so square identities are preserved throughout.

**(e) Yes.**
- For any 7-tuple of literals, ∨_{a∈{0,1}^7} ∧ x_i^{a_i} ≡ ⊤. This holds even if variables repeat or are already fixed by c.
- So replacing c by {c∧a} preserves the disjunction exactly. By induction the disjunction of all leaves is ⊤.
- Overlaps only create contradictory (x∧¬x) or duplicate leaves. They never lose a case.
- A total canonical assignment satisfies exactly one a per step, hence exactly one leaf.
- The residual risk is at the ledger level only (C9–C11).

## Clause families vs. real vectors

| SB LF | Family | Reason it holds for the canonical assignment | Status |
|---|---|---|---|
| 19–20 | g, line constants | ⟨Ψ(p),Ψ(q)⟩ = 0 on a common row/column (each line is an ONB); row-0 overlaps are the supports | ✓ (self-pairs: M3) |
| 28 | G2 | Prop 1 (factorised tensor inner product); with q=(0,k) it is rule #3 | ✓ necessary |
| 29–31 | G3, b3 | The Gram matrix between two ONBs is unitary. Rows and columns are nonempty. A single-term sum is ≠0 (Lemma 2), both for UU* and for U*U | ✓ (diagonal: M3) |
| 32–33 | G4, c4 | Parseval in the ONB of l. Only "1 term ⇒ ≠0" and "0 terms ⇒ 0" are used; nothing is inferred from ≥2 terms (cancellation) | ✓ |
| 34 | G5, u5 | Frame support {a} ⇒ Ψ(q)=λΨ(a) with \|λ\|=1 | ✓ |
| 35–36 | P4, w3 | "Each 6 of 8 has a nonzero" ⇔ ≤5 zeros ⇔ weight ≥3. Setting w3 := [weight ≥3] satisfies the one-way clause. The at-least-one clause holds by definition (K5) or by F3 (K4) | ✓ (M1, M2) |
| 37–39 | weight1 | Classical in row-0 standard form ⇒ phase·\|L(p)⟩, so exactly one ⇒ at most one | ✓ (weaker) |
| 45–55 | SB2 / ROWLEX / sort | The vectors are moved first; auxiliaries are then set to their defining values; no CNF symmetry is assumed | ✓ |

## Findings

**FATAL:** none in the supplied mathematics.

**MAJOR**

**M1. It is unspecified which families the K4 CNF inherits (SB LF 24–25; cf. LF 45–51, 52–55, 59).** "gram_a_r3.py … same families plus weight1" does not say which gram_a.py families are replaced. Three inherited families would each make the K4 base stronger than justified:

- **(i) K5-SB2.** gram_a.py 271–281 (LF 48) requires supp(square 5) = {7} at (1,0). LF 54 gives L the support {1}. Every true K4 object violates this.
- **(ii) ROWLEX.** The freedom to permute rows 2..7 is already consumed by L(i,0)=i. No lossless move remains to lex-sort Q1's column 0, and nothing in a K4 object relates Q1's column 0 to L's column 0.
  - Applied to square 5, ROWLEX is outright false. With k=0 most significant, e_2 = 00100000 >_lex e_3 = 00010000.
- **(iii) P4 on square 5.** L has frame weight 1 in every row and column frame. Any at-least-one-flag clause for square 5 is therefore violated by every true K4 object.
- **Signal (line-count inference only, not evidence of an error):** r3 253–275 is mapped to no family. It is 23 lines, exactly the size of ROWLEX (gram_a.py 248–270), and sits right after P4 (r3 236–252).

**Fix:** For each encoder, give a complete line→family map, with the square set and frame set of each family. The audit should then confirm in the emitted K4 CNF:
- no lexeq variables or clauses;
- no K5-SB2 units;
- P4 only for squares 1–4;
- symmetry-breaking units exactly as in LF 53–55.

**M2. The K5 P4 frame set is ambiguous (SB LF 35 vs LF 58, 59).**
- LF 35 ("r3 adds column frames") leaves open whether gram_a.py 233–247 already emits row frames 1..7. LF 58 asserts row 0 only.
- Any non-row-0 frame is not implied by K5 membership. Applying §5 to a K5 set in which some Ψ_s has all row-r weights ≤ 2 yields a set with four non-classical squares, i.e. an object in the open class K4.
- Such clauses would therefore make the K5 result conditional on K4 = ∅.

**Fix:** State explicitly "K5: frames {row 0}, squares 1–5", and state the exact K4 frame set (both row 0 ∪ columns and all rows ∪ columns are justified). The audit should count the at-least-one-flag clauses: exactly 5 for K5. Otherwise, regenerate the CNF or declare the dependency on K4 = ∅.

**M3. Self-pairs are undefined, and the literal LF 20 rule makes the base vacuous (SB LF 19–20, 29–33).**
- g is defined only for distinct cells. LF 20 sets g = False whenever two cells share a row, which a cell trivially does with itself.
- G3 on intersecting lines involves U[c₀][c₀] = 1 at the shared cell c₀. G4 "any pair" does not exclude p = q.
- **Counterexample 1.** Take l1 = row 0 and l2 = column 0. The U-row of (0,0) is all False, so "row nonempty" becomes the empty clause. Every instance is then UNSAT vacuously.
- **Counterexample 2.** In G4 with p = q, c4(a) = g(a,p). With g(p,p) = False, the clause forbids ℓ-frame weight 1. Squares 2–5 at (1,0) violate it after SB2.

**Fix:** State the index domains explicitly:
- G3 only for parallel pairs, or with U[c₀][c₀] := ⊤ (equivalently, use the 7×7 block);
- G4 only for p ≠ q with p, q ∉ l;
- G5 only for q ∉ l, a ∈ l, p ∉ {q,a};
- P4 flags only at p ∉ ℓ.

The audit should check that the base contains no empty clause and no self-pair literal, and run the C12 control.

**MINOR**

- **m1 (LF 14–16).** F3 is correct as stated. Cite KK LF 8 and K3 LF 9 directly. Add "after restandardising T". Replace the parenthetical with the bound 1 ≤ m(T′) ≤ #nc(T) from (a).
- **m2 (LF 60–62).** "Lemma R" is stated only for k ∈ {5,6} (KK LF 51) and k = 4 (K3 LF 15–20), whereas the K4 net has k = 3. It is also unnecessary here.
  - Use a simultaneous row permutation (BS (ii)), preceded by transposition when ℓ is a column.
  - Add a sentence justifying transposition as a non-isotopy symmetry.
  - Replace "unchanged as squares" with "isotopic/transposed images, same ray counts".
- **m3 (LF 25 vs 37, 52).** LF 25 says weight1 occupies r3 276–300; LF 37 and LF 52 split that range as 276–285 and 286–300. gram_a.py 154–178 and 282, r3 lines before 236, and r3 253–275 are mapped to no family.
- **m4 (LF 24).** The hashes are truncated. Give the full SHA-256s, the exact command lines, and the base-CNF hashes.
- **m5 (LF 35–36).** State the flag domain and the 8 overlaps g_s(a,p), a ∈ ℓ. Say whether "6 of 8" is encoded as the 28 explicit clauses or through counters; counters would need canonical values.
- **m6 (LF 49–51).** State the pairs as (i,i+1) for 2 ≤ i ≤ 6, with e_{−1} = ⊤ and one common bit order. Widening to the pair (1,2) would be unsound: v_1 = 01110000 forces supp Ψ1(2,0) = {1,2,3}.
- **m7 (LF 65).** The K4 split is only "intended". The leaf-level K4 bridge is conditional on the actual declaration.
- **m8 (LF 8, 76).** Extend the trust list with:
  - Prop 1, Lemma 2 and rules #2/#3;
  - KK LF 14–17 (used at LF 38 and 53);
  - the transposition symmetry.
  
  Also record that K5 is F3-independent, while K4 inherits all K1–K3 certificates and the E–W counts through F3.
- **m9 (LF 4, 13).** State that K5 is the *reduced* class. A set with five non-classical squares can reduce into K4, so only K4 = K5 = ∅ together with F3 covers all non-classical sets.
- **m10 (LF 21–22).** The gate memo key must include s and the unordered operand set. Reuse across squares would be unsound.

## Code / auxiliary / exhaustiveness obligations (Codex/parent)

- **C1.** Full encoder hashes and flags; regenerated base CNFs byte-equal to the recorded ones.
- **C2.** Exactly one variable per (s, unordered pair of distinct cells). Line constants are False. No self-pair literal appears except as ⊤.
- **C3.** Enumerate every auxiliary family.
  - b3, c4, u5 and lexeq (and any XNOR helper) must be fully defined.
  - w3 is one-way.
  - No unlisted counters.
  - Memo keys must be per-square.
- **C4.** G2 is emitted for all 10 square pairs.
- **C5.** The domains of G3, G4 and G5 are as in M3: rows and columns only, and no empty clause.
- **C6.** P4 squares and frames per M1/M2; flags only at p ∉ ℓ; the 6-of-8 family is exact.
- **C7.** K5 symmetry breaking is exactly:
  - the (1,0) support literals of LF 48;
  - ROWLEX on square 1, column 0, rows 2..7;
  
  and nothing else.
- **C8.** K4 symmetry breaking is exactly:
  - the units of LF 53–55;
  - g_5((0,i),(i,0)) for i = 2..7;
  - weight1 for square 5 at all 56 off-row-0 cells;
  
  with no K5-SB2, no lexeq, and no P4 for square 5.
- **C9.** Split lists for K5 come from README §8/§8.1. All cube variables must be ≤ V. The K4 lists must be checked once §9 is declared.
- **C10.** Ledger exhaustiveness:
  - every refined node has exactly 128 children of the form c∪a over its declared list;
  - no cube is pruned by symmetry or heuristics;
  - no leaf is closed on UNKNOWN or a timeout.
- **C11.** Each leaf is regenerated as the base CNF plus the path units, and its DRAT proof is VERIFIED against those exact bytes; the parent replays this.
- **C12.** Positive controls:
  - A pinned classical control: five MOLS(8) from AG(2,8), normalised as each mode requires (K5: rows sorted for ROWLEX; K4: L(1,0) = 1 and L(i,0) = i). Run it against the base with P4 and the Q-part of SB2 off; it must be propagation-consistent.
  - A unit test of the P4 gadget: a flag with 2 nonzero overlaps must conflict; a flag with 3 must not.

## Scope, imports, remaining gates

- **Established here (model review, conditional on imports and C1–C12):** Every K5 or K4 object normalises losslessly. Its canonical assignment satisfies every clause family described in SB §3–§4 and lies in exactly one leaf of any §6-form split.
- **Not established:** K4 = ∅, K5 = ∅, or Problem 16 at n = 8. The cubes are still running; K4 and K5 remain open.
- **Imports conditioned on:**
  - BS §2.2–2.4 definitions and rules #2/#3.
  - BS Lemma 10. I re-checked its printed proof, in particular the same-or-disjoint step.
  - KK: Prop 1, Lemma 2, W8, the reduction, and "8 rays ⇔ classical". A8 is imported by reference to r1 and was not re-audited here.
  - The invariant results K1 = K2 = K3 = ∅ (KK LF 8; K3 LF 9), with their DRAT certificates and E–W catalogue counts as parent-accepted.
- **Remaining gates:**
  - Resolve M1–M3 in the code audit.
  - Complete the K5 leaf ledger with every leaf DRAT-verified, plus a parent replay.
  - Declare the K4 split, complete it, and verify it.

Model review is not peer review.
