# Gram-support encoding for K2 and K3 (lane moqls7-maximum): soundness

Status: lane draft, awaiting parent verification. The definitions are those of Ball–Simoens arXiv:2607.12933v2
§2.2–2.4. Entries are unit vectors taken up to phase. Theorem K1 is `review/K1-THEOREM.r1.md` (still unverified by
the parent).

## 1. Objects
Let S be a set of mutually orthogonal QLS(7). For a quantum square Ψ_a ∈ S and cells p ≠ q, put
G_a(p,q) = ⟨ψ_a,p, ψ_a,q⟩. Its support g_a(p,q) = [G_a(p,q) ≠ 0] does not depend on phases or on any global
unitary. The ONB lines of Ψ_a are:
- its 7 rows and 7 columns (QLS axioms);
- in K2, the 7 symbol lines of the classical square L. By (C1), Ψ_a ⊥ L iff Ψ_a is an ONB on each symbol line of L.

## 2. Necessary conditions (each holds for every quantum square a)
- **G1.** If p ≠ q lie on a common ONB line, then g_a(p,q) = 0.
- **G2 (frame consistency).** Let ℓ be an ONB line and p, q ∉ ℓ. Then ψ_p = Σ_{r∈ℓ} G(r,p) ψ_r, so
  G(p,q) = Σ_{r∈ℓ} conj(G(r,p)) G(r,q). Hence #{r ∈ ℓ : g(p,r) ∧ g(q,r)} = 0 forces g(p,q) = 0, and = 1 forces
  g(p,q) = 1. When p and q are collinear, G1 then forbids the count 1.
- **G3 (unitary transitions).** For ONB lines ℓ1 ≠ ℓ2, the matrix U[r,q] = G(r,q) (r ∈ ℓ1, q ∈ ℓ2) is the product
  of two unitaries. If the lines meet in s, then U[s,s] = 1 and the 6 × 6 block on (ℓ1∖s) × (ℓ2∖s) is unitary.
  Hence:
  - every r ∈ ℓ1∖ℓ2 has a neighbour on ℓ2∖ℓ1;
  - if r has exactly one neighbour q there, then |U[r,q]| = 1, so q has no other neighbour on ℓ1∖ℓ2.
- **G5 (orthogonality, exact).**
  - For quantum squares a ≠ b: ⟨ψ_a,p ⊗ ψ_b,p, ψ_a,q ⊗ ψ_b,q⟩ = G_a(p,q)·G_b(p,q). So Ψ_a ⊥ Ψ_b iff
    g_a(p,q)·g_b(p,q) = 0 for all p ≠ q.
  - Orthogonality to a classical L is exactly G1 on L's symbol lines.
- **G4 (heavy).** In a non-classical 3-set S that minimises the number m of non-classical squares, every
  non-classical square Ψ is heavy in every ONB B: some entry has ≥ 3 nonzero coefficients in B.
  - *Proof.* Theorem K1 gives m ≥ 2. Suppose Ψ is light in B, i.e. every entry has ≤ 2 nonzero coefficients.
    Apply a global unitary V with V(B) = standard basis. Lemma 10 (Ball–Simoens LF178–192) then gives a classical
    Ψ'' that is orthogonal to every square orthogonal to VΨ. Orthogonality of Ψ to the other squares is invariant
    under ψ ↦ Vψ applied to all entries of Ψ alone. So V⁻¹Ψ'' is classical and orthogonal to the other two squares.
    The resulting 3-set has m − 1 ≥ 1 non-classical squares, which contradicts minimality. ∎
  - With B the ONB of an own line ℓ: the weight of p ∉ ℓ is #{r ∈ ℓ : g(p,r)}. So *every own ONB line ℓ has a
    point p ∉ ℓ with ≥ 3 neighbours on ℓ.*
  - When K1 is impossible, any K2 set already has minimal m = 2. When K1 and K2 are both impossible, any K3 set has
    minimal m = 3. G4 therefore applies to every K2 set and to every K3 set that survives.

## 3. Symmetry and the case split
- **K2.** All conditions are symmetric in the three classes (rows, columns, L lines) and invariant under relabelling
  of each class. A K2 configuration on L therefore transports to every L′ paratopic to L. One representative per
  main class suffices.
  - The 147 main classes are in `evidence/ls7_main_classes.txt` (sha256 898065c8…8158), produced by
    `code/ls_classes.c` (968ad4e5…8794).
  - Each class was found by canonical form, a minimum over the 211680 normalisations. |Par| is the multiplicity of
    the minimum.
  - Completeness: Σ 211680/|Par| = 16942080, the number of reduced Latin squares of order 7; observed MATCH. The
    count of 147 classes agrees with the literature (McKay–Meynert–Myrvold). That reference is cited, not re-derived.
- **K3.** Row and column permutations, transposition and relabelling of the squares preserve every condition.
  - WLOG (`--sym`) square 1 is heavy in the frame of row 0 at point (1,0), with neighbours (0,1), (0,2), (0,3).
  - Justification: permute rows so that the frame row is 0 and the heavy point's row is 1. Permute columns so that
    the heavy point's column is 0 and three of its neighbours lie in columns 1, 2, 3. A neighbour cannot be in
    column 0, because (0,0) and (1,0) are collinear.

## 4. Controls (genuine data, exact Gram supports)
For a prime p, a sum of p p-th roots of unity vanishes iff each root occurs once. So the Ψ(f) Gram support is exact:
g(p,q) = 1 iff x ↦ (k−i)f(x) + (l−j)x is not a permutation.

| control | encoder A (`explore/gram/gram_controls_v1.json`) | encoder B (`explore/gram/gram_controlsB_v1.json`) |
|---|---|---|
| classical triple aI + J, 3 squares, no heavy | SAT | SAT |
| genuine non-classical pair (Ψ(f), Φ(m)), Ex. 15, q = 7, H = {1,2,4}, f shifted | SAT | SAT |
| Ψ(f) alone on its 3-net (net-L = Φ(m)), heavy | SAT | SAT |
| classical K2-shaped data (net-L = L1, squares L2, L3), no heavy | — | SAT |
| single-bit mutations of Ψ(f)'s support (40) | 6 rejected (the conditions are necessary only) | — |

## 5. Results (exploration pass; certification separate)
- K2, encoder A with CaDiCaL (`explore/k2classes/screen_v1.jsonl`):
  - for all 147 classes, one heavy assignment on the 3-net is SAT;
  - two edge-disjoint heavy assignments are **UNSAT** for all 147 classes, each solve ≤ 23.5 s.
- K2, encoder B with kissat (`explore/k2classes/screenB_v1.jsonl`): see the certification record.
- K3: see the certification record.
