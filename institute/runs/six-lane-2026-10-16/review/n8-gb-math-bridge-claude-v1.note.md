# Hostile audit: GB necessity and the genuine P1 normal form

I had no tools, so the source hashes are taken as given and were not recomputed.

- **Audited** means I re-derived it from the inlined text.
- **Imported** means the argument relies on it but these sources cannot check it.

No solver fact is used. No GB UNSAT is supplied, so nothing is excluded yet.

## Verdicts

| Item | Verdict | FATAL | MAJOR | MINOR |
|---|---|---|---|---|
| (i) GB NECESSITY | **ACCEPT-WITH-FIXES** | 0 | 0 | 6 |
| (ii) GENUINE NF | **ACCEPT-WITH-FIXES** | 0 | 0 | 6 |

Both verdicts are conditional on the imports listed in §4.

The combined statement holds as worded:
- Every normalized genuine configuration in a T16 template has a canonical GB assignment.
- In B1/B2/B3/B5, genuine moves reach M_s for some s in {2} / {2,4} / {2} / {2,3}, without leaving template C.
- So refutations of all six GB strengthened inputs would exclude every such configuration.

The argument makes no claim about arbitrary GB models and uses no GA auxiliary step.

## 1. GB NECESSITY — audited

**Canonical assignment.** T is true. Each nonconstant g_s(p,q) is set to [⟨Q_s(p),Q_s(q)⟩≠0]. Each auxiliary is set to its defining function. Every GB auxiliary is a full equivalence, so the extension is unique and needs nothing from GA's one-way w3 handling.

**Flags and call.**
- The CLI path (SOURCE02:244–247) matches SOURCE00:14,18.
- `classical=[]` (SOURCE02:39), so lines 53–85, 143–145 and 218–219 emit nothing.
- `fixg=None` skips 153–159.
- `allrows`/`allcols` are False, so line 210 runs r0=0 only and 212–214 is skipped.
- Lines 138–140 still allocate every nonconstant g, in (s, combinations) order. Keys are sorted, so all 245 column-0 primaries exist as `('g',s,(0,c),(i,0))`.

**Constants (89–97).** p=q gives T, and a shared row or column gives −T. These are the true Gram values: unit norm, and rows and columns are ONBs (SOURCE06:195–196).

**G2 (146–152).** For p≠q, ⟨ψ_p⊗φ_p, ψ_q⊗φ_q⟩ = ⟨ψ_p,ψ_q⟩⟨φ_p,φ_q⟩ = 0 (SOURCE06:209–216). Constancy depends only on (p,q), so a clause is skipped only when both literals are −T, i.e. when it would contain literal T.

**conj / counter2 / atleast3 (99–135).**
- conj: v ↔ a∧b.
- counter2: n1 ↔ ge1∨l, and n2 ↔ ge2∨(ge1∧l).
- atleast3: v_k ↔ ge_k∨(carry∧l). Here carry is T for k=0 and otherwise the OLD ge_{k−1}, because `nxt` is only committed at line 134.
- Canonical prefix-threshold values satisfy every clause.

**±T and degenerate cases.**
- counter2 inputs are always fresh conj outputs.
- conj inputs can be T with −T (G3 row/column pairs at the shared cell) or −T with −T, never T with T.
- atleast3 inputs contain exactly one −T (at k=p[1]) and never T.
- First iterations emit degenerate clauses: [1,n]; [−n2,−1,−1] (117); [−v,−1,1] and [−v,−1,−1] (131); and [−carry,1,v] when l=−T (130). SB2 at k=0 emits [1].
- All of these are tautologies or forcings consistent with the canonical values, given the unit clause at line 37. No empty clause is possible.
- This is harmless for necessity. The solver/checker path must accept duplicate and complementary literals unchanged; SOURCE00:86 says no deduplication is done.

**G3 (161–173).** It covers all 120 line pairs, in both directions.
- ALO: a unit vector has some nonzero coefficient in ONB B.
- Not-exactly-one: distinct entries of one line are orthogonal. A single common coordinate would leave exactly one nonzero term in the sum, contradicting that.

**G4 (174–183).** This is Parseval in every line frame. When gpq is the constant −T, the clause only forbids exactly-one, which is correct.

**G5 (184–207).** `single` is true exactly when the support is {a} (198–201). Then Q(q) = e^{iθ}Q(a), so g(p,q) = g(p,a) for every p ∉ {q,a}, including constant p.

**P4 (208–214).** There is exactly ONE ALO clause, for square 1 in the row-0 frame, over the 56 off-row-0 points. At (1,0), k=0 is −T and k=1,2,3 are true, so atleast3 is true.

**SB2 (215–227).**
- The allocation is {1:[1,2,3], 2:[4], 3:[5], 4:[6], 5:[7]} (220–223).
- This gives 35 nonconstant units plus five [1] units.
- These are exactly the normalized (1,0) supports (SOURCE01:13; SOURCE05:16–17).

**Appended clauses.**
- The 42 units are the template bits.
- Each of the 126 M_s binaries holds whenever every Q_s(i,0), i=2..7, has a single row-0 coordinate, which is the case when X_s is a permutation.

**No ROWLEX.** GB only drops constraints relative to the normalized problem. The T16 representative is sorted, and its rows 2–7 equal the full 42-bit list. GB uses only that list and never needs sortedness, so a sorted representative remains valid.

**Independent decode prediction** (from SOURCE02:36,138–140 alone):
- id(g_s((0,c),(i,0))) = 1568(s−1) + 49c + 7i − 5, and TRUE = 1.
- Example: Q2, row 1, coordinate 4 gives id 1766.

**Classical control (SOURCE00:101–111).**
- The GF(8) slopes give Q1(1,0)=|1⟩ and Q2..Q5(1,0)=|4⟩..|7⟩.
- So the only false clauses are the P4-ALO and the Q1-SB2 units at k=2 and k=3.
- Every other base family holds for classical MOLS.
- This is a sound control, but it is not evidence about the unrelaxed base.

### Findings (i)

**MINOR G1 — SOURCE00:30–31.**
- *Problem:* "…or normal-form leaf" reads as if the accepted NF covers GB. SOURCE04:9 is a GA Boolean-model lemma and yields no genuine configuration satisfying M_s.
- *Repair:* "…in template C, and for (C,s) with X_s a permutation. Coverage of all of C needs the separately reviewed genuine NF (SOURCE01)."

**MINOR G2 — SOURCE00:38–40.**
- *Problem:* "(89–97)" cites only `glit`. The no-classical claim actually depends on SOURCE02:39, 53–85, 143–145 and 218–219.
- *Repair:* cite those lines, and note that lines 138–140 allocate the g ids.

**MINOR G3 — SOURCE00:84–85.**
- *Problem:* `encode` is a module function that instantiates the global `F` (SOURCE02:35). It is not "inherited", so a sink subclass is used only if `gram_b_r2.F` is rebound. Separately, `' 0\\n'` should be `" 0\n"` (SOURCE02:251). The adapter itself is not supplied.
- *Repair:* document the binding, and make the n3 control assert that the sink was actually exercised (object type, bytes, header).

**MINOR G4 — SOURCE00:96,113–116.**
- *Problem:* the decode and component controls are "not yet run". Byte-level correctness of the 22 appended tails therefore rests on the imported hash comparison.
- *Repair:* a parent receipt that decodes every appended literal through GB's own table, cross-checked against the id formula above.

**MINOR G5 — SOURCE00:60–61.**
- *Problem:* the claim that the Boolean NF relabelling "applies" to GB's rules is unproved. It would need its own invariance argument for GB's P4/atleast3 and G5. It is not load-bearing.
- *Repair:* delete it, or mark it unused.

**MINOR G6 — SOURCE00:9,25.**
- *Problem:* "SAME semantic leaf statements" overclaims. GB relaxes GA: no ROWLEX, and different auxiliaries. The sameness holds only for the appended primary facts.
- *Repair:* say the GB formulas are "implied by the same genuine leaf".

## 2. GENUINE NF — audited

**Lemma 1 (SOURCE01:23–33).**
- (A), rows: Q_s(i,0) ⊥ |0⟩.
- (A), columns: |c⟩ ⊥ |0⟩, so it expands in {Q_s(i,0)}, i≥1.
- (B), rows: coordinate 0 vanishes, so the inner product sums over the common support in coordinates 1..7.
- (B), columns: U_s[c,i] = ⟨c|Q_s(i,0)⟩ is unitary, with U_s[c,0] = 0 for c≥1.
- (C) is rule #3 applied at cells (0,c) and (i,0) (SOURCE06:300–302).
- The orientation of X_s matches SOURCE03:35.

**NF §1, re-derived (SOURCE03:47–78).**
- All degrees are at most 3.
- X_1's rows 1, 7 and columns 2, 3 have degree 3. So each other square has four isolated edges:
  - rows {1, 7, r2, r3}, with r2, r3 ∈ {2..5};
  - columns {b1, b7, 2, 3}, with b1 ≠ b7 in B.
- The removed rows and columns carry no other entries. So row 6 and column 1 keep their X_s degrees (at most 2) in the 3×3 residual.
- The classification of the residual is complete: permutation, K22 plus an edge, or K33 minus (6,1). Also |A1| ≤ 1 and |A6| ≤ 1.
- Outside A1 ∪ A6, a non-permutation must be K22 plus the edge (6,1). By (C) at most one square can have that edge, so k ≤ 3.
- The ≥9-ones lemma holds. With m + 28 + 2k ≤ 49 it gives k ≤ 2 for B5 (m=17), i.e. at least two permutation squares.

**Lemma 2 (SOURCE01:39–56).**
- The move is Q'_{τ(s)}(ρ(i),σ(j)) = P_σ Q_s(i,j). It preserves the line-ONB property and pairwise orthogonality directly, since it is a reindexing and P_σ⊗P_σ is unitary.
- ρ(0)=0, so Q'(0,c) = |c⟩ exactly.
- τ is a bijection of {2..5}, and supp Q'_{τ(s)}(1,0) = σ(supp Q_s(1,0)), so SB2 is kept.
- X'_{τ(s)}(ρ(i),σ(c)) = X_s(i,c), so permutation status travels with the label.
- The template is preserved if and only if σ(T_i) = T_{ρ(i)} for i=2..7. This is exactly the Boolean condition at SOURCE03:137.
- Composites are (σ2σ1, ρ2ρ1), with τ_{σ2σ1} = τ_{σ2}∘τ_{σ1}.

**Representative coverage (SOURCE01:64–68).** The case split is exhaustive.
- B1: the action is all of Sym(B).
- B3: ⟨(45), (67), (46)(57)⟩, which is transitive on B.
- B2: the orbits are {4,5} and {6,7}. A label is sent to 4 or 6, giving M2 or M4.
- B5: there are two distinct labels, and at most one of them is 7.
  - Label 4 gives M2.
  - Label 5 gives M3.
  - Label 6 goes to 5 under (56), with τ(4)=3, giving M3.

**Consistency check on B1.** m=12 forces rows 2–5 of B1 to be distinct singletons. Ascending keys (weights 8, 4, 2, 1 for c=4..7) then force rows {7}, {6}, {5}, {4}. This matches r(b) = 9−b (SOURCE03:130).

**Sorted representative.** The masks are identical row by row, so the moved configuration has the same ROWLEX keys. It is again a T16-normal representative of C. That is valid for GA and unnecessary for GB.

### Findings (ii)

**MINOR N1 — SOURCE01:17.**
- *Problem:* U and T16 are called "accepted" on the strength of N8_ASSEMBLY, which is not supplied. SOURCE05:105–107 still lists parent acceptance of T16 as a gate.
- *Repair:* pin the parent disposition hash, or state the conditionality.

**MINOR N2 — SOURCE01:35.**
- *Problem:* row 1 = {1,2,3} comes from SB2 (SOURCE01:13), not the template. The row 6/7 masks, the B-lists and the m-values are imported table facts. "≥1 for B3" also understates NF's ≥2, though harmlessly.
- *Repair:* attribute each fact to its source, and cite WMAN and the parent RESULT.

**MINOR N3 — SOURCE01:52.**
- *Problem:* template preservation is imported (SOURCE03:137–139; SOURCE04:20).
- *Repair:* state the condition σ(T_i) = T_{ρ(i)} explicitly and cite the receipt.

**MINOR N4 — SOURCE01:62.**
- *Problem:* M_s means "at most one"; "exactly one" also needs (A)/G3. Only the implication permutation ⇒ M_s is used.
- *Repair:* fix the wording.

**MINOR N5 — SOURCE01:64.**
- *Repair:* change to "By Lemma 1 **and NF §1** (SOURCE03:47–78)."

**MINOR N6 — SOURCE01:73–75.**
- *Problem:* "GB(B_C)" conflates GA's B_C with GB.
- *Repair:* define GB_C as the GB base plus the 42 GB units, and GB_{C,s} as GB_C plus M_s^GB.
- Remark 3 imports GA's canonical extension and must stay outside the GB chain.
- The GA and GB P1 routes share NF §1/§4 and the template table. So the two-encoding independence holds only at the CNF level.

## 3. Missing hypotheses and silent restrictions

None of these breaks the argument, but each must be stated explicitly:

1. Normalization presupposes non-classicality. Non-classicality gives a weight-3 entry (A8/Lemma 10), which gives the U/T16 SB2-sorted representative. GB necessity only starts after that point.
2. The strengthened inputs exclude only the MOVED configurations. So all six must be refuted, including both B2 inputs and both B5 inputs. The full GB counterpart also needs the twelve direct GB inputs refuted.
3. The setting is fixed at n=8, five squares and ngen=0 (the assert at SOURCE02:217).

## 4. Imported, not audited

- U, A8/Lemma 10 and T16 (SOURCE05:15–31,92–107; SOURCE01:17).
- The content of WMAN 355b3380…fc74: the P1 rows, B-lists, m-values and sortedness.
- NF §4 stabilizer and orbit validity, and the parent RESULT e075aff8… (SOURCE04:20). I re-derived NF §1 here; I did not re-derive §4.
- The adapter `gb_one_p4_r2.py`, the conventions note, and all controls; none is reported as run.
- The 22 matched hashes (SOURCE01:74) and every SHA256 pin.
