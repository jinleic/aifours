# K4/K5 at n = 8: soundness of the all-frames Gram-pattern encodings and their symmetry breaking — revision r1
# (model-authored; for review; no result is claimed here beyond "every genuine configuration satisfies the CNF")

Scope: the CNFs of README §2/§5/§7/§8 — unconditional K5 (code/gram_a.py `--quantum 12345 --ngeneric 0 --p4 12345
--sb2 --g5 --rowlex`, base of the certified split, SHA-256 6ecb77a7…469b) and K4-minimal with a weight-1 classical fifth
square (code/gram_a_r3.py `--quantum 12345 --ngeneric 0 --p4 1234 --p4-all-rows --p4-all-cols --sb2 --g5 --weight1 5`).
Soundness = for every set of 5 MOQLS(8) of the class in question (after the stated lossless normalisations) the
canonical assignment satisfies every clause; UNSAT then excludes the class. Conventions and Prop 1, Lemma 2, Lemma 10,
W8, A8, Lemma R, K1–K3 = ∅: review/PROOF_K1_K2.r2.md and review/PROOF_K3.r2.md.

## 1. Variables and canonical assignment
For squares s = 1..5 of a set S in row-0 standard form and unordered pairs of distinct cells {p,q}:
g_s(p,q) := [⟨Ψ_s(p), Ψ_s(q)⟩ ≠ 0]. Pairs in a common row or column are the constant 0 (ONBs). The row-0-frame support of
a cell p is {k : g_s((0,k),p) = 1} since Ψ_s(0,k) = |k⟩. Auxiliary variables (AND gates "b3", "c4"; one-way flags
"w3", "u5"; lex-prefix variables) are given their defining values; for the AND gates the clauses are full equivalences,
the flags are only required in the direction used.

## 2. Clause families and why each holds (any QLS, any frame line)
- G1 (zero on common lines): rows and columns are ONBs. [gram_a.py g(): same row/column → constant False]
- G2 (Prop 1): for s ≠ u, not g_s(p,q) ∧ g_u(p,q): ⟨Ψ_s(p)⊗Ψ_u(p), Ψ_s(q)⊗Ψ_u(q)⟩ = ⟨Ψ_s(p),Ψ_s(q)⟩⟨Ψ_u(p),Ψ_u(q)⟩ = 0.
- G3 (transition patterns): for two distinct lines l1, l2 ∈ {rows, columns}, U[a][b] = ⟨Ψ(a),Ψ(b)⟩ (a ∈ l1, b ∈ l2) is
  the unitary change of basis between the two ONBs (diagonal entry 1 at a common point). Its support has nonempty
  rows/columns, and two rows (columns) cannot share exactly one nonzero position: Σ_b U[a][b] U[a′][b]* = δ_{aa′}
  (Parseval in l2's ONB) and a single nonzero term cannot vanish.
- G4 (Parseval in a frame): for a row/column l and p, q ∉ l, ⟨Ψ(p),Ψ(q)⟩ = Σ_{a∈l} ⟨Ψ(p),Ψ(a)⟩⟨Ψ(a),Ψ(q)⟩; exactly one
  a with both factors nonzero ⇒ g(p,q) = 1; none ⇒ g(p,q) = 0.
- G5 (same ray): if in the frame of a row/column l the support of q is {a}, then Ψ(q) = λΨ(a) with |λ| = 1, so
  g(p,q) = g(p,a) for every p ∉ {q, a}.
- P4: K5 (unconditional): in the reduced set S′ of PROOF_K1_K2.r2 §5 with m = 5, every square has a weight-3 entry in
  the row-0 frame (it is untouched by Lemma 10 exactly because it has one); the clause asks for weight ≥ 3 (one-way
  flag w3 ⇒ at least 3 of the 8 row-0 overlaps; W8 makes ≥ 3 equivalent to = 3). K4-minimal: P4 for Q1..Q4 in every
  row and every column frame — minimal-counterexample argument, README §5 (column frames by transposition).
- Weight-1 square (K4 only): the classical square L in standard form has exactly one nonzero row-0 overlap at every
  off-row-0 cell (at-most-one clauses; at-least-one is G3). Its Gram pattern is the symbol-class equivalence, and G2
  between it and Q_s is exactly "Q_s is an ONB on the L-lines" at the pattern level (Prop 1).

## 3. Symmetry breaking (lossless normalisations, applied to the vectors before encoding)
Moves: (α) a permutation of rows 1..7 applied to all squares; (β) a permutation σ of the columns applied to all squares
together with P_σ|k⟩ = |σ(k)⟩ on every square (keeps row-0 standard form; supports are relabelled by σ). Both preserve
QLS-ness, mutual orthogonality, classicality, weights and every frame-weight statement used in P4.
- SB2, K5: Ψ1 has a weight-3 entry; by (α), (β) move it to (1,0). At (1,0) the coordinates 1..7 are available (0 is the
  column coordinate); Ψ1 takes 3 and Ψ2..Ψ5 at least one each, pairwise disjoint (W8), so exactly one each and the
  five supports partition {1,…,7}; σ fixing 0 makes S1(1,0) = {1,2,3}, S_s(1,0) = {s+2} (s = 2..5). Clauses:
  g_s((0,k),(1,0)) fixed accordingly (gram_a.py SB2 block).
- ROWLEX, K5 (after SB2): rows 2..7 are permuted by (α) only, which fixes rows 0, 1 and hence the SB2 values; choose the
  order in which the 8-bit vectors v_i = (g_1((0,k),(i,0)))_{k=0..7} are lexicographically non-decreasing (ties
  allowed). Encoding: for i = 2..6 a prefix-equality chain e_k (e_k ⇔ e_{k−1} ∧ (v_i[k] ↔ v_{i+1}[k])) with clauses
  e_{k−1} ⇒ (v_i[k] ⇒ v_{i+1}[k]); the canonical assignment of a sorted configuration satisfies them.
- SB2 + row sort, K4 (README §7): Q1's weight-3 entry to (1,0); L(1,0) ↦ 1; S1(1,0) = {2,3,4}, S2..S4 = {5},{6},{7};
  rows 2..7 sorted by L's column 0, i.e. g_5((0,i),(i,0)) = 1 (i = 2..7).
Order of application: SB2 first, then the row normalisation; each later step fixes what earlier ones set.

## 4. From UNSAT to exclusion
K5: any S′ with m = 5, after SB2 and ROWLEX, yields a canonical assignment satisfying all clauses (§2–§3); hence UNSAT of
the base CNF (or of every cube of a covering split, §5) means no set of 5 MOQLS(8) has five non-classical squares (by
the reduction, m(S) = 5 for the reduced set of any S whose row-0 form has five squares with weight-3 entries).
K4-minimal: UNSAT excludes a minimal counterexample with m* = 4 (README §5).
Combining with K1–K3 = ∅: if a non-classical set existed, the minimal m* would be 4 or 5; K4-minimal and K5 exclusions
would then give a contradiction. (Status: K5 certified split in progress; K4 open.)

## 5. Certified split (README §8)
Cubes = all 2^7 complete assignments of the declared literals g_1((0,k),(2,0)), k = 1..7 (DIMACS 57, 106, 155, 204,
253, 302, 351): their disjunction is a tautology, so F is UNSAT iff every F ∧ cube is UNSAT. Each cube CNF = base +
7 units, bytes hashed; DRAT verified by drat-trim (strict); ledger code/k5_ledger.py re-derives the cube list and the
cube-CNF hashes from the base CNF.

## 6. Points for reviewers
(a) G3/G4/G5 are imposed only for rows/columns (fixed lines), never for variable classical lines — this weakens but
cannot invalidate. (b) The P4 flag w3 is one-way. (c) SB2 uses W8's partition property at a weight-3 cell. (d) The
row lex-leader is compatible with SB2 because it permutes rows 2..7 only. (e) The K5 instance uses P4 in the row-0 frame
only (no minimality); the K4 instance uses all-frame P4 (minimality). (f) The weight-1 encoding of the classical
square relies on standard form (row 0 = identity) of that square.
