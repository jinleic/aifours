# Hostile review: B3 joint-completion candidate v1, erratum 1, and the parent wording erratum

This is a written review only. Nothing was executed. I took the SHA256 values and line ranges as given and did not recompute them. [BP], [CX] and the 17:35 [TR] are not in the packet. Nothing below depends on them, because no proof in the candidate depends on them (§6).

## 0. Verdict

**FATAL 0 · MAJOR 0 · MINOR 8.**

- **Both prior MAJOR claims are withdrawn in substance.**
  - E1 makes LC and LR necessary-only and turns F into a product of schemas.
  - E2 deletes the absorption claim.
  - Some wording that E1's literal edits miss is still present (m1–m4). No proof step depends on that wording.
- **Every inserted argument is correct.** This covers E1's η-identity and its dual, the T8 relation, E5's AX, the own-frame Lemma Z, the three-number step, and the direct O5 proof.
  - The parent's rereading of erratum LF45 is correct. It needs one stated hypothesis and a two-line proof (m7).
  - The E2 replacement sentence is true but has no witness (m8).
- **No lemma is only cited.** No elimination and no no-go is inferred anywhere once the erratum is applied.

## 1. Claim-by-claim

| Claim (lines) | Verdict | Re-derivation note |
|---|---|---|
| F1, F2, S (L25–28) | ✓ | (i,j) and (0,d) differ in row and column iff i≥1 and d≠j. (i,j) and (r,0) differ iff r≠i and j≥1. |
| AX (L27; E5 L57) | ✓ | Uses cells (r,0),(0,d) with r,d≥1. Coordinate 0 is excluded because q_s^r ⊥ q_s^0 in column 0. |
| Lemma R (L30–34) | ✓ | Interior sum = P_B − P_{q^i}, which is rank one. At the corners, q_1^i and e_c span V_B because supp q_1^i = {6,7}. |
| t (L36) | ✓ | 2×2 unitary change of basis. |
| Theorem K (L38–44) | ✓ | Row 2: coordinate 7 lives on columns {1..6} (6 columns), shared by 4 squares plus J_2. Column 6: own index 3 lives on rows ≠ 3 (6 rows). |
| Lemmas D, E (L48–58) | ✓ | |
| Lemma Sc (L60–62) | ✓ | Needs only one eigenvector with full support. |
| P4 common / own (L70–77) | ✓ | 7 lines. The ranges guarantee a≠d and k≠i. |
| P1 (L79) | ✓ | Uses δ_d(a) = Σ_{r∈R'} \|⟨e_d,b_{r,a}⟩\|², a one-line consequence of Lemma D that is not written. |
| LC, L1–L9 (L81–103) | ✓ as necessary conditions | Hand table in §2. |
| LR, L1'–L9' (L105–126) | ✓ as necessary conditions | Hand table in §2. |
| X1–X4 (L131–134, with E4) | ✓ | |
| X5 (L135–138) | ✓ | Redundant and incomplete (m5). |
| X proof (L140) | Conclusion ✓ | One sentence is overbroad (m2). |
| O1 (L144–150) | ✓ | Rows: P_X q_1^r (P_Y q_1^r)^* = 0 because q_1^r lies in one block. Columns: I − P_{e_c}. |
| O2 (L152, L167) | ✓ | No parity is claimed, correctly. The ≥4-cell count is in §2. |
| O3 (L154–156, L168) | ✓ | §2. |
| O4 (L158–161, E3, parent) | ✓ | §2 and m7. |
| O5 (L163; E5 L60) | ✓ | §2. |
| C-twins (L173–182) | ✓ | Induced by an explicit isotopy (§2). Presentation is m6. |
| A couplings (L184–188; E5 L58–59) | ✓ | |
| Theorem F (L190–214, with E1, E2) | ✓ | Lists are complete. Nothing is eliminated. Wording is m3 and m4. |
| E1 algebra (L15–28), T8 (L29) | ✓ | §2. |
| E2 (L33–37) | ✓ | True, but no witness given (m8). |
| E3 (L41–45) and parent L3 | ✓ | Literal LF45 was too strong. The parent's repair is right (m7). |
| E4 (L49–53) | ✓ | |

## 2. Hand checks

### LC, common frame

Define cap = 3 − [x>0] − [y>0] (from P4) and P_v = |v⟩⟨v|.

| case | (x,y) | D(a) | cap | forced structure, re-derived |
|---|---|---|---|---|
| L1 | (1,1) | 0 | 1 | All b_{r,a} = 0. Q_1(2,a) = ωq³ and Q_1(3,a) = ω'q², since they are unit vectors whose B-part has norm 1. |
| L2 | (1,m) | (1−y)P_{q²} | 1 | Rank one, so every b_{r,a} ∝ q². Hence R_6 = R_7 = the support. cap = 1 and D ≠ 0 give one row with b = ω(1−y)^{1/2}q². |
| L3 | (m,1) | (1−x)P_{q³} | 1 | Mirror of L2. |
| L4 | (m,m) | rank 2 | 1 | δ_6, δ_7 > 0, so R_6 = {r} and R_7 = {r'}. If r = r', D has rank ≤ 1, a contradiction. So b_r ∝ e_6 and b_{r'} ∝ e_7. Then D is e-diagonal, Sc gives D = μP_B, hence x = y = 1−μ and both masses equal μ. |
| L5 | (1,0) | P_{q²} | 2 | One or two rows, all ∝ q², masses summing to 1. With one row, Q_1(r,a) ∈ V_B. |
| L6 | (0,1) | P_{q³} | 2 | Mirror of L5. |
| L7 | (m,0) | (1−x)P_{q³} + P_{q²} | 2 | Rank 2, so at least two rows. If \|R_6\| = \|R_7\| = 1, either the two rows coincide (rank 1) or D is e-diagonal and hence scalar, but its eigenvalues are 1−x ≠ 1. |
| L8 | (0,m) | P_{q³} + (1−y)P_{q²} | 2 | Mirror of L7. |
| L9 | (0,0) | P_B | 3 | Rank 2, so at least two rows. |

- **Exhaustiveness of the bins.**
  - x=1 ⇔ J_2 = {a}; x ∈ (0,1) ⇒ |J_2| = 2 by Theorem K. The same holds for y and J_3, so the 3×3 bins are complete.
  - The boundary values |λ|² ∈ {0,1} are their own bins.
- **Dependence on t.** t enters only through t ∈ (0,1), in three places:
  - δ_7 = (1−x)t + (1−y)(1−t) vanishes iff x = y = 1, so R_6 and R_7 are nonempty outside L1;
  - Lemma Sc;
  - η ≠ 0.

### LR, own frame

Here E(i) = (1−y')P_{e6} + (1−x')P_{e7} and cap' = 3 − [x'>0] − [y'>0]. The dictionary from LC is q³ ↔ e_7 (coefficient 1−x, resp. 1−x') and q² ↔ e_6. So the printed labels line up.

| case | E(i) | cap' | forced structure |
|---|---|---|---|
| L1' | 0 | 1 | No B-content in columns 1..5. |
| L2' | (1−y')P_{e6} | 1 | One cell, pure e_6, mass 1−y'. |
| L3' | (1−x')P_{e7} | 1 | One cell, pure e_7, mass 1−x'. |
| L4' | rank 2 | 1 | ⟨q^k,Eq^k⟩ > 0, so C_2 = {c} and C_3 = {c'}. c = c' would give rank 1. So the cells are pure q² and pure q³, E is diagonal in both bases, and Sc gives x' = y' = 1−μ'. |
| L5' / L6' | P_{e6} / P_{e7} | 2 | One or two cells, pure e_6 / e_7, masses summing to 1. |
| L7' / L8' | not scalar | 2 | Same argument as L7 / L8. |
| L9' | P_B | 3 | At least two cells. |

### Theorem F

(|J_2|,|J_3|) ∈ {1,2}². The possible intersection patterns are:

| sizes | patterns | types |
|---|---|---|
| (1,1) | equal, disjoint | T1, T2 |
| (1,2) | contained, disjoint | T3, T4 |
| (2,1) | containing, disjoint | T5, T6 |
| (2,2) | equal, one common column, disjoint | T7, T8, T9 |

That is nine types and there are no others. I checked every column bin:

| type | column bins |
|---|---|
| T1 | a(1,1) |
| T2 | a(1,0), b(0,1) |
| T3 | a(1,m), b(0,m) |
| T4 | a(1,0); b, c(0,m) |
| T5 | a(m,1), b(m,0) |
| T6 | a, b(m,0); c(0,1) |
| T7 | a, b(m,m) |
| T8 | a(m,m), b(m,0), c(0,m) |
| T9 | a, b(m,0); c, d(0,m) |

- At most 4 of the 5 lines are special, so every type has at least one L9 line.
- I_6, I_7 ⊆ R' because κ_{2,c} = κ_{3,c} = 0. J_4, J_5 ⊆ {1,2,3,6,7}. The same nine-type combinatorics apply to all four 5-element ranges.
- Nothing derives an elimination. E1 L8 and L72 state that realizability and elimination are both unproved.

### O2 (counting and parity)

- **No line meets X in exactly one cell.** Every row and column sum vanishes, so one nonzero term cannot stand alone.
- **At least 4 cells.** Take (r,c) ∈ X. Row r contains a second cell (r,c'). Columns c and c' contain second cells (r'',c) and (r''',c'), with r'', r''' ≠ r. These four cells are distinct and occupy at least 2 rows and 2 columns.
- **No evenness is claimed, and none follows.** Three nonzero terms can sum to zero.

### O3

- **B-completion.** Σ_{r∈R'} Σ_{a≤5} |⟨e_7,Q_1(r,a)⟩|² = Σ_a δ_7(a) = 4. Each row contributes 1−x'_r ≤ 1, so at most one row of R' contributes nothing. Hence at least 2 rows of {1,6,7} carry B-completion mass.
- **C-completion.** The C-twin, over rows R'_C = {1,2,3,6,7}, also gives at least 2 rows of {1,6,7}.
- **Pigeonhole.** Two 2-subsets of a 3-set meet.
- The result is a joint row, not a joint cell, as E3 states.

### E1 algebra

- **Column identity.**
  - Since P_{q²} = P_B − P_{q³}, D(a) = (1−y)P_B + (y−x)P_{q³}.
  - Hence D_{67} = (y−x)q³_6 conj(q³_7), and |η|² = t(1−t) > 0.
  - D_{67} = Σ_r b_6 conj(b_7), whose terms are supported on R_6 ∩ R_7. ✓
- **Dual identity.**
  - ⟨p,q⟩ = 0 gives ⟨p,e_7⟩⟨e_7,q⟩ = −⟨p,e_6⟩⟨e_6,q⟩.
  - Hence ⟨p,Eq⟩ = (x'−y')⟨p,e_6⟩⟨e_6,q⟩, and the terms are supported on C_2 ∩ C_3. ✓
- **Consistency with the tables.**
  - In L2, L3, L5 and L6, R_6 = R_7 ≠ ∅.
  - In L4, x = y and R_6 ∩ R_7 = ∅.
  - The E1 consequence (R_6 ∩ R_7 ≠ ∅ in L7/L8) subsumes the old "distinct singletons" elimination.
- **T8.** x_a + x_b = 1 = y_a + y_c and x_a = y_a give x_b = y_c. ✓

### O5 (E5)

- **The direct proof is correct.**
  - In the row-2 orthonormal basis, the q-coefficients are 0 at column 0 (⟨q²,q³⟩ = 0) and at every j ∉ J_2.
  - So q³ = conj(λ_a)v_a + conj(λ_b)v_b. Taking non-B parts gives conj(λ_a)n_a + conj(λ_b)n_b = 0, and ‖n_a‖² = |λ_b|² > 0.
  - Consistency check: ⟨n_a,n_b⟩ = −conj(λ_a)λ_b holds.
- **The original L170 argument was a gap, not an error.**
  - O1's proof extends verbatim to Y = V_B^⊥, because P_{V_B^⊥}q_1^2 = 0.

### C-twins (symmetry claim)

The substitution in L176–180 is induced by an isotopy of the normal form:
- rows are permuted by π = (2 4)(3 5);
- columns and coordinates are both permuted by σ = (4 6)(5 7);
- squares are relabelled 2↔4, 3↔5;
- the new configuration is Q̃_s(i,c) := U_σ Q_{τ(s)}(π(i), σ(c)).

It preserves every hypothesis:
- **H2.** Q̃_s(0,c) = w e_c, because the column permutation equals the coordinate permutation.
- **H4.** New rows 2,3 come from old rows 4,5, and σ{4,5} = {6,7}. New rows 4,5 come from old rows 2,3, giving {4,5}. Rows 1, 6, 7 are fixed, and σ fixes {1,2,3}.
- **H3.** σ{τ(s)+2} = {s+2}.
- **H1.** The isotopy uses items (ii) and (iii) plus a reordering of squares, all of which preserve the MOQLS property.

It maps R' → R'_C, {1..5} → {1,2,3,6,7} and t → t_C. So every B-statement proved for all H1–H4 configurations yields its C-twin. That includes E1 and O5 for rows 4 and 5.

### A couplings

- **Rows.**
  - d = 1: rows {1,7}, since 1 ∉ supp q_1^6. Their fractional parts sum to 2−1 = 1.
  - d ∈ {2,3}: rows {1,6,7}, summing to 3−1 = 2.
- **Columns (E5).**
  - Row sums are 1−δ_{rk}, which are integers.
  - The fractional column sums sit at supp q_1^k: columns {1,2,3} (total 2) for k ∈ {1,7}, and columns {2,3} (total 1) for k = 6.
- **Subset step.** Singletons lie in (0,1) and pairs in (1,2), so neither is an integer. ✓

### Frames

| Statements | Frame | Why this frame is forced |
|---|---|---|
| K (row), P4-common, LC, O1–O3 | common (e_d) | Other squares have coordinate-d mass 1 in column a≠d. In a row this fails: square 4 has coordinate-6 mass 0 in row 1, because q_4^1 ∝ e_6. |
| K (column), P4-own, LR | own (q_s^k, each square in its own frame) | Other squares have own-index-k mass 1 in row i≠k. In a column the mass would be 1−\|⟨q_s^k,e_c⟩\|². |

Every statement uses the correct frame. Theorem X compares common-column data with own-row data for the same cell b_{r,a}.

## 3. Withdrawal audit

- **MAJOR-1 (exact classification).** E1 L7–14 is effective. No deduction still uses exactness. Residual wording remains at L1, L7, L8, L140, L190, L207 and L212 (m1–m3).
- **MAJOR-2 (absorption).** E2 is effective, and the replacement sentence is local and true. A residual dependency remains in the first sentences of L9 and L214 (m4).

## 4. MINOR findings and minimal repairs

**m1 — residual "exact" and "surviving list" wording (L1, L7, L8, L190, L207).**
- E1 L14 deletes only the literal phrase "the explicit finite list of surviving configurations".
- L1 and L7 still say "exact local case tables".
- L8, L190 and L207 use variant phrases: "…configuration types", "…surviving types" and "Surviving list".
- **Repair:**
  - In L1, L7, L81 and L105, read "necessary mass-case table(s)".
  - In L1, L8, L190 and L207, read "exhaustive product of support-shape schemas".

**m2 — L140 is overbroad.**
- It says LC and LR "prescribe the type … and the mass of every nonzero B-part".
- That is false for L7–L9 and L7'–L9', where the type is free.
- It is also false for two-row L5/L6, two-cell L5'/L6', L7–L9 and L7'–L9', where the mass is free.
- X1–X5 use only the forced cases, so the theorem stands.
- **Repair:** "In the cases used below, LC and LR force the type (L1–L6, L1'–L6') and the mass (L2–L4, L2'–L4', one-row L5/L6, one-cell L5'/L6') of each nonzero B-part."

**m3 — L212 is stale.**
- It says the eliminated sub-branches are "exactly those listed in the tables".
- That omits the exclusions in X1–X4 and E1's added ones:
  - R_6 ∩ R_7 = ∅ in L7/L8;
  - |R_6 ∩ R_7| = 1 in L9;
  - their duals.
- **Repair:** "…are those of the §§3–4 tables, X1–X5 and E1 L19–28, together with their C-twins."

**m4 — L9 and the first sentence of L214 lack support.**
- They say "No type … is eliminated by the results proved here."
- Their only support was the withdrawn absorption sentence.
- Read as a mathematical claim, it is unproved.
- **Repair:** "No schema is claimed eliminated. Whether the proved necessary conditions already exclude some schema is not examined."

**m5 — X5 (L138).**
- "L4/L3'" repeats what L137 already says.
- X5 also omits two exclusions that follow from its own principle (L140, "masses at a cell are a single number"):
  - A one-row L5/L6 cell has B-mass 1, so it cannot lie in an L4' row, whose cells have mass μ' ∈ (0,1).
  - A pure-e cell of an L4 column has mass μ ∈ (0,1), so it cannot be the cell of a one-cell L5'/L6' row, which has mass 1.
- **Repair:** Replace L138 with "Analogously for L3/L4'; X5 is not exhaustive." Optionally retain the two exclusions as eliminated sub-branches.

**m6 — presentation of the C transfer (L175, L182).**
- The transfer list omits Lemmas R and Sc.
- "The C block is dense" is undefined. What is needed is supp q_1^4 = supp q_1^5 = {4,5}, i.e. 0 < t_C < 1.
- The transfer itself is valid.
- **Repair:** Cite the isotopy from §2 as the justification.

**m7 — parent erratum L3: the claim needs its hypothesis and a proof.**
- **Claim:** "Witnesses remain in at least one completion region."
- **The claim is true when the initiating cell (r,a) has r ∈ {1,6,7} and a ∈ {1,2,3}:**
  - row witness (r,c'): if c' ≤ 5 it lies in R'×{1..5}; if c' ∈ {6,7} it lies in R'_C×{1,2,3,6,7};
  - column witness (i,a): if i ∈ R' it lies in the B region; if i ∈ {2,3} ⊂ R'_C it lies in the C region.
- **It fails without that hypothesis.** Starting from (r,4), the column witness may be (2,4) or (3,4), which lie in neither region.
- Erratum LF45, read literally, was false. The parent's repair is right.
- **Repair:** State the hypothesis and add this two-line proof.

**m8 — erratum L35: "admit both pure directions locally" has no witness.**
- **Witnesses:**
  - An L9 column with B-parts ωq², ω'q³ in two rows satisfies D = P_B, |R_d| ≤ 3 and |R_6 ∩

R_7| = 2 ≠ 1.
  - An L9 column with B-parts ωe_6, ω'e_7 in two rows also satisfies D = P_B. Here |R_d| = 1 and R_6 ∩ R_7 = ∅.
  - Dually, an L9' row works with cells ωe_6, ω'e_7: then C_2 = C_3, both of size 2, and |C_2 ∩ C_3| = 2. It also works with cells ωq², ω'q³: then C_2 ∩ C_3 = ∅.
- **Limit.** "Admit" does not mean "absorb". E1 already forbids an L9 column with exactly one cell carrying both coordinates.
- **Repair:** Add the two witnesses. Define "locally" as "consistent with D = P_B (resp. E = P_B), P4 and E1 only".

## 5. Observations (not counted)

- **O4(i) is weak as a statement of O_next.** O4(i) is the precise form chosen for O_next. It follows in one line from row completeness, so the cross-line content of the partial is in O2, O3 and X.
  - The packet does not contain [BP], so I cannot check that this form matches the informal O_next there.
  - If [BP] meant a cell-wise statement, that is not proved here. E3 itself says O3 gives a joint row, not a joint cell.
- **The tables use range inclusion only.** They do not use the stronger cell-wise domination b b^* ≤ D(a) and b b^* ≤ E(r). This fits E1's "necessary only" status.
- **L111, entry L1'.** "none" should be read as "no nonzero B-part in columns 1..5", which is the scope of that table's header. By contrast, the L1 entry goes beyond its own header by also recording rows 2 and 3.
- **Stale metadata.** The status string at REVIEW-REQUEST L6 still says "exact local case tables" and "explicit 9^4 type list".
- **"Genuine" is never used.** No proof uses the "genuine" condition in H1. Every result holds for all configurations satisfying H1–H4.

## 6. Imports and premises

**Nothing is only cited.** Every statement the candidate uses is proved in this file or in the erratum:

| Statement | Where proved |
|---|---|
| F1, F2, S | L25–28 |
| AX | E5 L57 |
| R | L34 |
| K | L40–44 |
| D, E, Sc, P4 | L52–77 |
| P1 | L79, plus the unwritten one-line identity |
| LC, LR, X | L97–140 |
| O1–O5 | L165–170; E5 L60 |
| Lemma Z and the A couplings | L185–187; E5 L58–59 |
| C-twins | L175–182; isotopy in §2 |
| E1 additions | E1 L15–28 |

- **[BP] is not a premise.** It is never invoked inside a proof.
- **Traceability gap.** The scope target names "P1–P6", but this file names only P1 and P4. P2, P3, P5 and P6 are not mapped to anything here. This is harmless, because no proof here relies on them.

**Premises.** H2–H4 are the declared normal form (SCOPE-FREEZE L21).
- **H4** matches the [J] snapshot `supports_row2to7` (L21–47) exactly.
- **H3's supp q_1^1 = {1,2,3} is an independent premise.** It does not follow from H4 plus orthonormality of column 0.
  - Counterexample: take q_1^1 = (α,0,γ) and q_1^6 = (0,β_2,β_3).
  - Then q_1^7 ∝ conj(q_1^1 × q_1^6) = conj(−γβ_2, −αβ_3, αβ_2), which has full support {1,2,3}, while q_1^1 does not.
  - The A couplings use H3: the row sets {1,7} and {1,6,7}, and the column set {1,2,3}. So they hold only under the declared normal form.
  - The s ≥ 2 part of H3 is used nowhere.
