VERDICT: ACCEPT-WITH-FIXES

**Scope of the verdict.** The implication "every set of 4 MOQLS(7) is classical, hence 2 ≤ M(7) ≤ 3" is sound under two conditions:
- the supplied parent receipt holds; the logic needs one verified UNSAT per class K2/K3/K4, and six are claimed;
- the imports listed in §7 are trusted.

I found no blocking defect in the mathematics, the reduction, the symmetry breaking, or the six code translations. Every required fix is about packaging and readiness. I ran nothing, so I take the receipt as supplied evidence, not as something I reproduced. This is a model review, not human peer review, and I did not assess novelty.

## 1. The implication chain

1. **Standard form.**
   - A per-square unitary is an allowed set isotopy.
   - It preserves orthogonality, because U_s⊗U_t is unitary.
   - It preserves classicality, because classical means at most n rays up to phase.
   - Rules #2 and #3, and Lemma 4 (weight ≤ 3; a weight-3 entry forces the other three entries to weight 1), are correct.

2. **R2 and survival of a non-classical square.**
   - Off row 0 every weight is ≤ 3.
   - If no square had a weight-3 entry, Theorem A applied to S itself would make S classical. So m ≥ 1 squares have a weight-3 entry.
   - Lemma 10 is never applied to those squares (its hypothesis would fail), so they pass into S′ unchanged, entry for entry.
   - A weight-3 entry in standard form means the square is non-classical.
   - S′ need not be isotopic to S. The argument only uses three facts about S′: it exists, it is a 4-MOQLS(7) set in row-0 standard form, and its non-classical squares are exactly the m untouched ones, each with a weight-3 entry. ✓

3. **Lemma 10's properties (import I1), checked against the pinned proof.**
   - The proof has one unstated step, the claim that another entry is "same support or disjoint". It holds for *any* orthogonal pair in the square, not only pairs in the same row or column:
     - Suppose supp ψ(c) = {a,b}, ψ(c′) ⊥ ψ(c), and |supp ψ(c′)| ≤ 2.
     - Lemma 2 rules out |supp ψ(c′) ∩ {a,b}| = 1.
     - So supp ψ(c′) is either {a,b} or disjoint from it.
   - Consequences:
     - Each row or column is either untouched or mapped entirely by U, so the result is still a QLS.
     - N(Ψ′) ⊆ N(Ψ), so orthogonality to every other square (already modified or untouched) persists, in any order of application.
     - Supports only shrink.
     - Weight-1 entries, including all of row 0, are literally untouched, not just "up to phase".
   - I1 is therefore a verified lemma, not an external trust item.

4. **R4 (Theorem B).** If m = 1, three squares are classical, so the fourth is classical, which contradicts its weight-3 standard-form entry. ✓

5. **Lemma P.** All four conditions are necessary:
   - **P1:** nonempty support; the column coordinate is excluded; L_t(c) is excluded (rule #3 with Ψ_t(c) ∝ |L_t(c)⟩); quantum supports are disjoint.
   - **P2:** each quantum square forms an ONB on every row, column and L_t-line, including that line's row-0 cell (via Prop 1). From the unitary rows and columns:
     - every coordinate is covered;
     - no two cells share exactly one coordinate;
     - no pair of coordinates co-occurs in exactly one cell.
   - **P3:** follows from Prop 1 plus Lemma 2, over all 1176 cell pairs including row 0.
   - **P4:** holds by construction of S′.

6. **SB2.**
   - The two moves:
     - (α) permutes rows 1–6.
     - (β) applies one column permutation σ to every square and P_σ to every square; on a classical square, P_σ is exactly the symbol relabelling.
   - Both are isotopies of S′. They preserve row-0 standard form, weights, the quantum/classical split and P4. So the normalized set is again a K_m set, and Lemma P applies to it directly.
   - The normalization steps, in order:
     1. Move a weight-3 entry of Ψ1 to cell (1,0).
     2. Apply σ with σ(0)=0 to send the distinct nonzero values L_t(1,0) to 1,…,4−m.
     3. Apply σ fixing 0,…,4−m to arrange the forced 3+1+…+1 split of {5−m,…,6}.
     4. Encoder A only: permute rows 2–6 to sort column 0 of the first classical square.
   - Each later step fixes everything the earlier steps normalized, so SB2 is lossless.

7. **UNSAT gives the contradiction.** By §3, the canonical extension satisfies every clause of all six CNFs, so UNSAT means no normalized K_m set exists.

8. **The bound on M(7).**
   - A non-classical t-set with t ≥ 4 contains a non-classical 4-subset, so M(7) ≤ 3.
   - M(7) ≥ 2 follows from Corollary 7 in the pinned source (q=7, d=3, H={1,2,4}).
   - This settles only n=7 of Problem 16. Whether M(7) is 2 or 3 stays open.

## 2. Theorems A and B, and the parent's Fact C / Fact L

**Lemma 3.**
- The unitary is block-structured, which forces k = k′ in each component.
- A component with ≥ 2 vectors contains no weight-1 vector (Lemma 2).
- It has no degree-1 coordinate, because each column is a unit vector.
- So the component is a 2k-cycle. If k ≥ 3, consecutive vectors share exactly one coordinate, which is impossible. ✓

**Theorem A, step 4.** ✓
- E ⊆ V(G_ab) by property (i).
- Each row or column meets E in 0 or 2 cells (Lemma 3 applied to the *original* Ψ1).
- A row or column that meets E contains both of its a/b cells, so E is closed under G_ab-adjacency.
- G_ab is connected, and the cell (0,a) is in V(G_ab) but not in E.

**Fact C (parent's proof).** ✓
- Choose coordinates with rows {x=i} and columns {y=j}; the third class is ax+by=const with a,b ≠ 0.
- The alternating walk s→t→s shifts the row by (s−t)/a ≠ 0, and that step generates Z/7.
- So the graph is a single 14-cycle, and the property is isotopy-invariant.
- This replaces the 336-triple enumeration.

**Fact L (parent's proof).**
- GL(2,7) induces all of PGL(2,7) on the 8 directions, and PGL(2,7) is sharply 3-transitive. So we may take F = {∞,0,1}.
- f_c(x) = 1/(x−c), with matrix [[0,1],[1,−c]], sends c to ∞ and F to T_c = {0, −1/c, 1/(1−c)}.
- With L0: x=0 and L1: x=1, we get A((1,y)) = y − T_c, and |A(q)∩A(q′)| = #{f ∈ T_c : f + (y′−y) ∈ T_c}.

Recomputed:

| c | T_c | ordered differences | linear |
|---|---|---|---|
| 2 | {0,3,6} | 3,6,3,4,1,4 | no |
| 3 | {0,2,3} | 2,3,1,5,4,6 | **yes** |
| 4 | {0,2,5} | 2,5,3,5,2,4 | no |
| 5 | {0,4,5} | 4,5,1,3,2,6 | **yes** |
| 6 | {0,1,4} | 1,4,3,6,3,4 | no |

- The non-linear classes {2,4,6} are exactly the harmonic conjugates H(0;1,∞), H(∞;0,1) and H(1;0,∞). This matches the description in PROOF_PARTIAL.
- The result does not depend on the chart:
  - any other map sending c to ∞ differs by x ↦ αx+β;
  - a different pair of c-lines rescales T_c by (b−a);
  - neither change affects the distinct-differences property.
- Theorem B needs a linear class in 𝒩. That holds because both linear classes lie outside F.

**Complex phases.** Every inference in Theorems A and B, Lemma P and both encoders uses only three facts:
- a single-term inner product is nonzero (Lemma 2);
- a unitary row or column cannot have exactly one nonzero product term;
- a unit column is nonzero.

No step assumes that a sum of two or more complex terms fails to cancel. ✓

## 3. The six code translations

The pinned encoder hashes (b935bb11…, 097c62f8…) equal the `encoders` entries in the receipt. The effective parameters from the recorded argv are:

| case | quantum | classical | P4 | SB2 constants at (1,0) | extra normalization |
|---|---|---|---|---|---|
| K2A | 1,2 | L3,L4 | 1,2 | L3=1, L4=2; S1={3,4,5}, S2={6} | L3(i,0)=i |
| K2B | 1,2 | L3,L4 | 1,2 | same | none |
| K3A | 1,2,3 | L4 | 1,2,3 | L4=1; S1={2,3,4}, S2={5}, S3={6} | L4(i,0)=i |
| K3B | 1,2,3 | "L3" (label only) | 1,2,3 | L3=1; same S values | none |
| K4A/B | 1–4 | – | 1–4 | S1={1,2,3}, S2={4}, S3={5}, S4={6} | – |

All constants match the §4 prescription. In both encoders, every clause family is a consequence of P1–P4 plus SB2:
- **Classical squares:** Latin squares with first row = identity, and orthogonality (each off-row pair (x,y) with x≠y at most once in A, exactly once in B; L_a(c) ≠ L_b(c)).
- **P1, P2 (coverage, exactly-one-shared, exactly-one co-occurrence) and P3** on all lines, including row-0 cells.
- **P4** is encoded as weight ≥ 3. That is weaker than "= 3", which is fine.

**Auxiliary variables.**
- Full equivalences:
  - encoder A: the AND variables b/v/u/t, and X;
  - encoder B: AND2, the counter outputs, z, and e.
- One-sided definitions: A's `w3` and B's coverage `y`. The canonical extension still satisfies them.

**Other checks.**
- A's constant folding (identity tests on True/False) is correct; the row-0 clauses reduce to the right unit clauses.
- In B's K3 run, `one_hot[(3,…)]` and `sup[(3,…)]` are separate dicts, so no variable aliasing occurs.

## 4. Imported tables

- **E-W Table 5, n=7 rows:** only k=1, k=2 (341880; 17/11/5 classes) and k=6 (120; 1/1/1, PP 1).
  - The text says the table covers all 1 ≤ k < n ≤ 9, so a missing row means zero maximal sets.
  - So there are no maximal 3-, 4- or 5-MOLS(7), and every set of 3 MOLS(7) extends step by step to 6.
  - Maximality is invariant under isotopy and paratopy, so the "reduced" normalization loses nothing.
- **E-W Table 6, n=7:** IMPORTS I5 quotes the figures correctly (k=2: 342480 sets, 7 paratopism classes; k=3: 1200 sets, 1 class).
- **E-W Table 7:** its n=7 rows are not in the excerpt, which stops at n=5.

## 5. Do the known issues invalidate the theorem?

No, given the six UNSAT facts.
- **ERR counted as UNSAT:** this only affects negative controls, which test whether an encoding is strong enough. An UNSAT claim is sound if there is no over-constraint, and §3 establishes that by auditing every clause. Readiness issue only.
- **B's metadata omits p3/fixpat:** the CNF is pinned by its argv plus a byte-identical hash. With no `--no-p3` and no `--fixpat`, p3=True and fixpat=None.
- **Not every auxiliary is a full equivalence:** harmless (see §3). It only makes encoder A's docstring false.
- **K3 label mismatch:** cosmetic; no aliasing.

## 6. Findings

**BLOCKING:** none.

**READINESS-MAJOR (fix before any external claim)**
- **F1** — PROOF_CANDIDATE.md, Status and §5 table: the "PENDING" and "NOT independently reviewed" entries are stale, hashes are 8-hex prefixes, and proof hashes are missing. Replace them with the receipt data: full CNF and proof SHA256, drat-trim source/binary hashes, argv. State that the logic uses one verified UNSAT per class.
- **F2** — PROOF_PARTIAL.md, status line ("NOT solved") and §5 ("no exclusion claimed"): these contradict the candidate. Mark them superseded by the K2–K4 certificates.
- **F3** — PROOF_CANDIDATE.md §5.3, `k2_controls.py`, `controls_{a,b}.json`: the "agrees" claim is unsupported wherever the status was ERR. Withdraw it, or rerun treating ERR as distinct from UNSAT. Not load-bearing.
- **F4** — PROOF_CANDIDATE.md Status (a): replace "human proofs" with "model-authored written arguments".

**MINOR**
- **F5** — PROOF_CANDIDATE.md §2 (R3, R5, R6) and §4:
  - state that S′ need not be isotopic to S;
  - state that the normalization is applied to the vectors of S′ (P_σ on every square) before Lemma P;
  - list encoder A's row sort in R6.
- **F6** — IMPORTS.md I1: add the same-or-disjoint justification from §1.3; change "unchanged up to phase" to "unchanged".
- **F7** — `k2_encode_a.py` docstring: "full equivalences" is false for `w3`; "(P1)-(P5) of README §2" does not match P1–P4 plus SB2.
- **F8** — `k2_encode_b.py`:
  - `T = tuple(range(3, 3 + ngeneric))` ignores Q;
  - the docstring still says "SB default OFF… does not rely on the row-permutation argument", but the certified runs use `--sb2`;
  - the meta output lacks p3 and fixpat.
- **F9** — `k2_encode_b.py` `counter()`: constant ±TRUE inputs produce tautologies such as (¬v∨¬TRUE∨TRUE) and duplicate-literal clauses such as (¬v∨¬TRUE∨¬TRUE). Both are legal and preserve semantics; normalize them before using a verified checker.
- **F10** — PROOF_PARTIAL.md §0 cites E-W Table 7, but IMPORTS I5 uses Table 5. Cite Table 5 throughout.
- **F11** — `parent-proofcheck.json`: the drat-trim command line is not recorded. The wall clock (≈719 s) is less than the sum of check times (≈1569 s), so the checks ran concurrently; record that, along with the host and the solver that produced each proof.
- **F12** — Index conventions differ: PROOF_PARTIAL uses 1..7, PROOF_CANDIDATE and the encoders use 0..6. Harmonize them.

**NOTES (optional hardening)**
- **N1** — Export LRAT (`drat-trim -L`) for at least one proof per class and check it with cake_lpr. This removes drat-trim from the trusted base.
- **N2** — Encoders A and B are independent only at the implementation level: same lane, same spec. They protect against coding slips, not spec errors; spec soundness rests on Lemma P and SB2, which I checked above.
- **N3** — No SAT control exercises the `--sb2` code path. A relaxed SAT run (for example `--no-p3 --sb2`) would test it. I checked the constants by hand.
- **N4** — Theorem C is correct, but its every-frame claims are unused.

## 7. Exact trusted-import boundary

**Trusted, not verified by me**
1. **Egan–Wanless 2016, Table 5, n=7 rows:** maximal sets exist only for k ∈ {1,2,6}. Used in Theorem B for the 3→6 extension.
2. **Shrikhande 1961** (Ball–Simoens Theorem 9): 4 MOLS(7) extend to 6. Used in Theorem A. Redundant given item 1.
3. **Uniqueness of the order-7 projective plane** (Hall 1953 and its 1954 correction; bodies not consulted): every affine plane of order 7 is AG(2,7). Used in both theorems.
   - It is redundant given E-W's n=7, k=6 row (one isotopism class).
   - Both theorems only need "every complete set of MOLS(7) is isotopic to the Desarguesian one".
4. **Bose 1938:** a complete set of MOLS plus rows and columns forms an affine plane. Elementary.
5. **Machine facts (supplied receipt):**
   - six CNFs regenerated byte-identically from the pinned encoders;
   - each verified UNSAT by upstream drat-trim 2e3b2dc0 (source d834b649…, binary a46c0c71…), with exit code 0 and "s VERIFIED".
   - The trusted base here is the drat-trim C code, the compiler, CPython and the parent's harness.
6. **The pinned Ball–Simoens v2 text:** definitions, rules #1–#3, and Corollary 7 for the lower bound.

**Verified by reading:**
- Prop 1; Lemmas 2–4; Lemma 10 properties (i)–(iii) and its QLS/orthogonality preservation;
- Theorem A; Theorem B, given imports 1, 3 and 4;
- Facts C and L, including all five cases;
- Lemma P; SB2 losslessness and its per-class constants;
- clause-level soundness of all six translations;
- the M(7) bounds.

**Not relied on:** any controls, the FIXED-net runs, solver names or timings, model reviews, and Theorem C beyond steps R1–R4.
