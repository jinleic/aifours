# Problem 16 at n = 8 — written arguments (model-authored), status PARTIAL (2026-10-17 PDT)

Conventions as README §0 (indices 0..7, row 0 reference, standard form). Lemma 2 (single shared coordinate ⇒ nonzero
inner product) and Lemma 3 (an ONB whose vectors have weight ≤ 2 splits into 1×1 and 2×2 blocks: a weight-2 vector
with support {a,b} has exactly one partner with support {a,b} and no other vector meets {a,b}) are as in the n = 7
lane (moqls7-problem16/review/PROOF_PARTIAL.md §1; their proofs do not depend on n). Prop 1 (orthogonality ⇔
disjoint non-orthogonality graphs) likewise.

## W8 (weights)
At an off-row-0 cell c = (i, j) the supports of five MOQLS(8) in standard form are pairwise disjoint (rule #3) and
avoid j (rule #2), so Σ_s w_s(c) ≤ 7 with w_s ≥ 1. Hence w_s ≤ 3; w_s = 3 forces the other four weights to be 1 and
the five supports to partition [8]∖{j}; and at most two entries of weight 2 occur at a cell.

## Theorem A8. If every entry of a set S = {Ψ1, …, Ψ5} of 5 MOQLS(8) in row-0 standard form has weight ≤ 2, S is
classical. (No MOLS classification is used.)
Proof. Fix s; we show Ψs has only weight-1 entries. Apply Lemma 10 (source; properties: supports never grow,
weight-1 entries unchanged, orthogonality to every square orthogonal to the original is preserved) to the four
squares Ψr, r ≠ s, one after the other. The results Ψ′r are classical with symbol arrays L′r (Latin, first row
identity), pairwise orthogonal and orthogonal to Ψs. Hence Ψs is an ONB on every line of the 6 classes
𝒞 = {rows, columns, L′r-lines (r ≠ s)} (Prop 1, as P2 in the n = 7 lane). Now apply Lemma 10 to Ψs itself: Ψ′s is
classical with symbol array L′s, and supp Ψ′s(c) ⊆ supp Ψs(c); L′s is orthogonal to every L′r, so on every line of 𝒞
it takes each symbol exactly once.
Suppose Ψs has an entry with support {a,b}; put E = {c : supp Ψs(c) = {a,b}} and V = {c : L′s(c) ∈ {a,b}}
(16 cells: 8 a-cells, 8 b-cells). Then E ⊆ V. For a line M ∈ 𝒞, Ψs|M is an ONB with weights ≤ 2, so by Lemma 3 M meets
E in 0 or 2 cells; V ∩ M consists of exactly one a-cell and one b-cell; hence if M meets E it meets it exactly in
V ∩ M. So E is a union of connected components of the bipartite graph H on V whose edges join the a-cell and the
b-cell of each line of 𝒞. 𝒞 is a net: two lines of different classes of 𝒞 meet in exactly one cell (row/column:
trivially; row or column with an L′r-line: L′r is Latin; L′r-line with L′r′-line: L′r ⊥ L′r′). Through an a-cell u
pass 6 lines of 𝒞 (one per class), pairwise meeting only at u; each contains one b-cell, so u has 6 distinct
neighbours among the 8 b-cells, and symmetrically each b-cell has 6 a-neighbours (H is 6-regular bipartite on 8 + 8
vertices). Two a-cells share ≥ 6 + 6 − 8 = 4 neighbours and every b-cell has a neighbour, so H is connected
(equivalently: a component would need ≥ 6 vertices on each side of every one of ≥ 2 components, i.e. ≥ 12 > 8 per
side). Since (0, a) ∈ V has weight 1 in Ψs (row 0), E ≠ V,
so E = ∅ — a contradiction. Thus every Ψs has only weight-1 entries, i.e. S is classical. ∎
Remark (general form). The same argument shows: a set of n − 3 MOQLS(n) (n ≥ 5) whose entries all have weight ≤ 2 in
some row-standard form is classical, because each a-cell has n − 2 neighbours among n b-cells and 2(n − 2) > n.
(For n = 7 this replaces Fact C and every plane-classification import in Theorem A of the n = 7 proof.)
Control (source Theorem 5 at n = 8): for 6 MOQLS(8), Σ_s w_s ≤ 7 with six terms forces weights ≤ 2, and the argument
with 7 classes (each a-cell has 7 of 8 b-neighbours) shows every set of 6 MOQLS(8) is classical.

## Reduction to classes K1..K5
Let S be non-classical. By A8 some square has a weight-3 entry. Let S′ arise by applying Lemma 10 (row-0 basis) to
every square of S without a weight-3 entry. As in the n = 7 proof (PROOF_CANDIDATE_r2 §2, R3), S′ is a set of
5 MOQLS(8) in row-0 standard form (not necessarily isotopic to S) whose non-classical squares are exactly the
m ≥ 1 untouched squares, each with a weight-3 entry; the other 5 − m squares are classical, with symbol arrays forming
5 − m MOLS(8) with first row identity. Class K_m: m quantum + (5 − m) classical squares. The support patterns satisfy
(P1)–(P4) of the n = 7 lane (README §2 there) with 8 in place of 7 (same proofs), and after the lossless (SB2_8)
normalization (README §0 here; same proof as PROOF_CANDIDATE_r2 §2 (R5) with 7 = 3 + (m − 1) + (5 − m)
coordinates at (1,0)) also the (SB2_8) unit conditions.

## K1 (Theorem B8 status)
In K1 the four classical squares form 4 MOLS(8). Import: Egan–Wanless Table 6 (layout.txt:763, n = 8, k = 4:
Equality 4800, Isotopism 3, Trisotopism 2, Paratopism 1): all 4-MOLS(8) are paratopic (net-isomorphic). The linear
set L_s(r, c) = c + s·r over GF(8), s ∈ {1, x, x+1, x²} (four distinct nonzero elements), is a 4-MOLS(8); hence the
6-net {rows, columns, L′2..L′5} of S′ is isomorphic to the net of six direction classes D of AG(2,8). E–W's single
PARATOPY class is not a single isotopy class (Table 6 lists 3 isotopism classes), and exchanging the roles of
row/column classes with symbol classes is NOT a set isotopy of MOQLS in the source's sense. The reduction therefore
goes through the following explicit lemma (not an isotopy statement).

Lemma R (regridding). Let 𝒩 be a 6-net of order 8 on a point set P (six parallel classes of 8 lines; lines of different
classes meet in exactly one point) and Ψ : P → unit vectors of C⁸ an ONB on every line of 𝒩. Choose two classes as
"rows" R and "columns" C, number their lines, and for each remaining class D number its lines. Put
A[i][j] = Ψ(R_i ∩ C_j) and L_D[i][j] = number of the D-line through R_i ∩ C_j. Then (i) A is a QLS(8); (ii) each
L_D is a Latin square, the four L_D are mutually orthogonal, so Φ_D = |L_D⟩ are four mutually orthogonal classical
QLS; (iii) A ⊥ Φ_D for each D (Prop 1: Φ_D's non-orthogonal pairs are the pairs on a common D-line, on which A is an
ONB); (iv) A has the same vectors as Ψ, merely re-indexed, so its number of distinct rays and, for any line ℓ of 𝒩,
the ℓ-frame supports {p ∈ ℓ : ⟨Ψ(p),Ψ(q)⟩ ≠ 0} are unchanged. Conversely every K1 configuration (S′ with its frame
row 0) is of this form with 𝒩 = {rows, columns, the four classical symbol classes} and ℓ = row 0. Proofs: immediate
from the net axioms and Prop 1.

Reduction of K1 to one FIXED instance. Given a K1 configuration, take (𝒩, Ψ = the quantum square, ℓ = row 0); the
weight-3 condition (P4) is the ℓ-frame statement "some q ∉ ℓ has exactly 3 points p ∈ ℓ with ⟨Ψ(p),Ψ(q)⟩ ≠ 0" and
depends only on (𝒩, Ψ, ℓ). By E–W, 𝒩 ≅ (AG(2,8), six directions D) as incidence structures; transport Ψ and ℓ along
the isomorphism. PGL(2,8) is sharply 3-transitive on the 9 directions; the setwise stabilizer of the 3 free
directions has order 6 and acts freely on D (an involution of PGL(2,8) is an elation with exactly one fixed direction,
which lies among the 3 free directions it permutes; an element of order 3 divides q + 1 = 9 and fixes no direction),
hence regularly; together with translations, the automorphisms of the AG 6-net are transitive on its lines. So ℓ can
be moved to the line x = 0 of direction ∞, with D = {∞, 0, 1, x, x+1, x²}. Regridding (Lemma R) with rows = direction
∞ and columns = direction 0, then the per-square standard-form unitary on ℓ (a permutation relabelling of the
coordinates indexed by ℓ's points), yields an assignment satisfying (P1)–(P4) for the FIXED K1 CNF. Hence FIXED-K1
UNSAT ⇒ K1 = ∅.
Computation (exploratory, 05:41 PDT): FIXED K1 instance UNSAT for encoder A8 (CaDiCaL) and B8 (kissat) in < 1 s;
without (P4) SAT (classical configurations accepted). Certificate run (DRAT) pending; until then K1 is
"solver-UNSAT, not yet proof-checked".
