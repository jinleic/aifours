# Problem 16 at n = 8, classes K4 and K5: soundness of the Gram-pattern encodings, symmetry breaking, frames and
# splitting — revision r2 (complete; supersedes the r1 draft, which is unchanged; model-authored, for Codex/Claude audit)

Claim audited here (and nothing more): for every set S of 5 MOQLS(8) of class K5 (resp. K4), after the lossless
normalisations of §4, the canonical assignment of §2 satisfies every clause of the K5 base CNF (resp. the K4 weight-1
CNF) and of exactly one cube/leaf of the declared split. Hence verified UNSAT of all leaves excludes the class.
No exclusion of K4 or K5 is claimed in this document. Sources/conventions as in review/PROOF_K1_K2.r2.md (§0–§3:
Prop 1, Lemma 2, Lemma 10, W8, A8, Lemma R) and review/PROOF_K3.r2.md.

## 1. Classes and the reduction (PROOF_K1_K2.r2 §5)
Let S be a non-classical set of 5 MOQLS(8) in row-0 standard form (Ψ_s(0,j) = |j⟩) and S′ := S with Lemma 10 applied to
every square that has no entry of weight ≥ 3 (row-0 frame). S′ is a set of 5 MOQLS(8); its non-classical squares are
exactly the m untouched squares with a weight-3 entry (W8: weights ≤ 3); m ≥ 1 by A8. K_m := such S′ with this m.
Established (parent-accepted): K1 = K2 = K3 = ∅. Consequence (F3): no set T of 5 MOQLS(8) has exactly 1, 2 or 3
non-classical squares — reduce T in its own row-0 frame: A8 excludes m(T′) = 0 (T would be classical), and
m(T′) ∈ {1, 2, 3} is excluded by K1–K3 (Lemma 10 never turns a classical square non-classical, so m(T′) ≤ 3).

## 2. Variables, canonical assignment, constants
For squares s and distinct cells p, q: g_s(p,q) := [⟨Ψ_s(p),Ψ_s(q)⟩ ≠ 0], symmetric; constant False when p, q share a row
or a column (ONBs). Row-0-frame overlaps are g_s((0,k), p) because Ψ_s(0,k) = |k⟩. Auxiliary variables take their
defining values: AND gates b3 = g(a,b) ∧ g(a′,b) and c4 = g(a,p) ∧ g(a,q) (full equivalences; the memo key determines
the operands up to the symmetry of g, so a reused gate always has the same meaning), u5 ⇔ "frame-l support of q is
exactly {a}" (full equivalence), w3 = [frame weight ≥ 3] (one-way: w3 ⇒ weight ≥ 3), lexeq chain variables (full
equivalences). gram_a.py (bf1aada1…d05a, base of K5) lines 140–282; gram_a_r3.py (40622a6f…, K4) same families plus
weight1 (lines 276–300).

## 3. Clause families (valid for every QLS and every row/column line l; checked against the code)
- G2 (gram_a.py 150–153), Prop 1: for s ≠ u and p ≠ q, ¬g_s(p,q) ∨ ¬g_u(p,q).
- G3 (179–190): for distinct lines l1, l2, U = [⟨Ψ(a),Ψ(b)⟩]_{a∈l1,b∈l2} is unitary (change of ONB): every row and column
  of its support is nonempty; no two rows (columns) share exactly one nonzero column (row), since
  Σ_b U[a][b]·conj(U[a′][b]) = 0 for a ≠ a′ cannot have a single nonzero term (Lemma 2).
- G4 (191–206), Parseval in the ONB of l: for p, q ∉ l (any pair, also on a common line where g = False):
  ⟨Ψ(p),Ψ(q)⟩ = Σ_{a∈l}⟨Ψ(p),Ψ(a)⟩⟨Ψ(a),Ψ(q)⟩; exactly one a with c4 true ⇒ g(p,q); none ⇒ ¬g(p,q).
- G5 (207–232): u5(q,a) ⇒ Ψ(q) = λΨ(a), |λ| = 1 ⇒ g(p,q) ↔ g(p,a) for p ∉ {q,a}.
- P4 (233–247; r3 236–252 adds column frames): w3(s,frame,p) ⇒ every 6 of the 8 frame overlaps contain a nonzero one
  (⇔ weight ≥ 3); per (s, frame) at least one flag. Justification: §5.
- weight1 (r3 276–285): square L (label 5 in K4) has at most one nonzero row-0 overlap at every off-row-0 cell.
  A classical square in standard form is Ψ(p) = phase·|L(p)⟩, so its overlap with |k⟩ is nonzero iff k = L(p);
  its Gram pattern is [L(p) = L(q)]; G2–G5 hold for it as for any QLS.

## 4. Normalisations (lossless; applied to the vectors before reading off the canonical assignment)
Moves: (α) permute rows 1..7 of all squares; (β) permute columns by σ and apply P_σ|k⟩ = |σ(k)⟩ to every vector of
every square (row-0 standard form kept; supports relabelled by σ). Both preserve the QLS property, mutual orthogonality,
classicality, and the multiset of frame weights of every row/column frame (frames are mapped to frames).
- K5 SB2 (gram_a.py 271–281): every square has a weight-3 entry (row-0 frame); (α), (β) put one of Ψ1's at (1,0). At
  (1,0) coordinate 0 is excluded (common column with (0,0)); the five supports are pairwise disjoint (Prop 1 with
  q = (0,k)) and nonempty with |S1| = 3: 3 + 1+1+1+1 = 7 forces S1 = 3 coordinates and singletons for Ψ2..Ψ5, a
  partition of {1..7}; σ fixing 0 maps them to {1,2,3}, {4}, {5}, {6}, {7}.
- K5 ROWLEX (248–270): then (α) restricted to rows 2..7 (fixes rows 0, 1, hence SB2) sorts the rows so that the vectors
  v_i = (g_1((0,k),(i,0)))_{k=0..7} (k = 0 most significant) are lexicographically non-decreasing (ties allowed); the
  chain e_k ⇔ e_{k−1} ∧ (v_i[k] ↔ v_{i+1}[k]) with e_{k−1} ⇒ (v_i[k] ⇒ v_{i+1}[k]) is satisfied by a sorted order.
- K4 SB2 + row sort (r3 286–300): Q1 has a weight-3 entry (row-0 frame) moved to (1,0); at (1,0) the supports of
  Q1 (3), Q2, Q3, Q4 (≥ 1) and L (= {L(1,0)}, L(1,0) ≠ 0) partition {1..7}; σ fixing 0 makes L(1,0) = 1,
  S1 = {2,3,4}, S2 = {5}, S3 = {6}, S4 = {7}; then (α) on rows 2..7 makes L(i,0) = i (column 0 of L holds 2..7 there),
  i.e. g_5((0,i),(i,0)) = 1. Each step fixes what the earlier ones set.

## 5. Why P4 holds
- K5 base (row-0 frame only): in S′ with m = 5 every square is an untouched square with a weight-3 entry. No minimality.
- K4 (every row and column frame, squares Q1..Q4): let S′ ∈ K4 and ℓ a row (column) of the grid. If some Q_s had no
  weight-3 entry in the ℓ-frame, regrid by Lemma R with ℓ as row 0 (transpose first for a column), restandardise and
  apply Lemma 10 to Q_s in that frame: the result is a set of 5 MOQLS(8) with exactly 3 non-classical squares
  (Q_s becomes classical; the other three Q's and L are unchanged as squares), contradicting (F3). So all-frames P4
  holds for EVERY K4 set — it rests on the accepted K1–K3 exclusions, not on a minimality assumption.

## 6. Splitting (README §8, §8.1; same design intended for K4 §9)
The cubes of a level are all 2^7 complete assignments of a declared 7-variable list; their disjunction is a tautology,
so F is UNSAT iff F ∧ c is UNSAT for every cube c, and a refined leaf c is replaced by c ∧ a over all 2^7 assignments a
of the next declared list (disjunction = c). The canonical assignment of §2 lies in exactly one cube per level. Leaf CNF
bytes = base header with C + |lits|, base clause bytes, one unit per literal (hash-bound; regenerable).

## 7. Points for audit
(a) G3/G4/G5 are imposed for rows and columns only (never for the lines of unknown classical squares) — weaker, never
unsound. (b) w3 is one-way. (c) SB2 relies on disjointness of supports at a common cell (Prop 1) and on |S1| = 3.
(d) ROWLEX permutes rows 2..7 only, after SB2. (e) K5 uses row-0 P4 only; K4 uses all-frames P4 via §5 and (F3).
(f) weight1 encodes the classical square only through its Gram pattern (no symbol variables).
(g) Trust: Lemma 10 (re-checked from the printed source proof), A8, Lemma R, W8, K1–K3 = ∅ as accepted.
