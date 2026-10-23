# K1 is impossible: no set of 3 MOQLS(7) has exactly one non-classical square (lane moqls7-maximum)

Status: lane result, awaiting parent verification. It is a partial result for the frozen target. It excludes K1 only;
K2 and K3 stay open. Host-clock times are PDT 2026-10-17. Definitions are those of Ball–Simoens arXiv:2607.12933v2
§2.2–2.4 (pinned copy in `sources/`). Points are cells; vectors are taken up to phase.

## 1. Reformulation
**(C1)** Let L be a classical Latin square and Ψ a QLS of order n. Then Ψ ⊥ L iff, for every symbol a, the n
entries of Ψ on the cells with L(i,j) = a form an ONB.

*Proof.* The product vectors are ψ_ij ⊗ |L(i,j)⟩. The inner product of two of them is ⟨ψ_ij, ψ_kl⟩ when
L(i,j) = L(k,l), and 0 otherwise. So orthogonality says exactly that entries on a common symbol line are pairwise
orthogonal. There are n unit vectors per line in Cⁿ, so the line is an ONB. ∎

**K1 ⟺ net form.** In a K1 set {Ψ, L1, L2}, L1 and L2 are orthogonal Latin squares. So rows, columns, L1 and L2 form
a 4-net N of order 7 (Egan–Wanless notation, k = 2). By (C1) together with the QLS axioms, Ψ is an
*ONB-assignment* on N: a unit vector at each of the 49 points such that each of the 28 lines carries an ONB. Ψ is
non-classical iff the assignment uses more than 7 rays. The condition is symmetric in the 4 parallel classes and
invariant under net isomorphism and global unitaries, so it suffices to treat one representative per isomorphism
class.

## 2. Frame and the pattern families
Fix a line ℓ0 (in the encoders: the class-0 line with label 0). Rotate globally so that the point of ℓ0 on the
class-1 line with label j carries e_j.

**Frame lemma.** Let p ∉ ℓ0. The 3 lines through p of the other classes meet ℓ0 in 3 distinct points r. Each such r
is collinear with p, so ⟨e_label(r), ψ_p⟩ = 0. Hence supp ψ_p ⊆ A(p), the complement of these 3 coordinates, and
|A(p)| = 4.

**Families** (each is necessary for any ONB-assignment, in the frame):
- **F1** supports are nonempty, since the vectors are unit.
- **F2** two points on a common line never share exactly one support coordinate. Otherwise the inner product is a
  single nonzero product.
- **F3** on each line every coordinate lies in some support. A unitary has no zero column.
- **F4** if coordinate k lies in exactly one support on a line, that point has weight 1. Column k of the line's
  unitary then has a single entry of modulus 1, so the rest of that row vanishes.

A pattern with all supports of size 1 in the frame means every vector is a phase times a standard basis vector. Such
an assignment is classical.

## 3. The 7 net classes
`evidence/nets7_classes.json` (sha256 78d1728f9096afff9d23650f88808f9d7888b4cc380141f68b31578a26ec0d67) holds one
explicit 4-net for each of 7 isomorphism classes. Each class has an exact |par|, computed by `code/net_canon.c`
(cf1cae5a…4ab5) as a minimum over all 846720 normalisations:

| idx | origin | \|par\| | reduced lists 846720/\|par\| | maximal |
|---|---|---|---|---|
| 0 | cyclic orthomorphism (0,2,5,1,6,4,3) | 126 | 6720 | yes |
| 1 | random square | 6 | 141120 | yes |
| 2 | random square | 6 | 141120 | yes |
| 3 | random square | 24 | 35280 | yes |
| 4 | random square | 48 | 17640 | yes |
| 5 | Desarguesian harmonic {∞,0,1,2} | 2352 | 360 | no |
| 6 | Desarguesian equianharmonic {∞,0,1,3} | 3528 | 240 | no |

The canonical keys are pairwise distinct. The counts sum to 342480 overall and 341880 for the maximal classes. These
are the Egan–Wanless totals of reduced 2-MOLS(7) **sets** (arXiv:1406.3681v2, Theorem 3.2 and Tables 5–6).
Reduced **lists** are counted in Tables 7–8; for k = 2 these counts agree with those for sets by Theorem 3.1.
The equality of the sums proves that the representatives cover every class. **Lane trust base:** the published
Egan–Wanless counts, plus our exact |par| computation. The lane's attempted `mols7_classify` full enumeration was
interrupted and is void; this does not describe the parent's separate full-enumeration verification.

## 4. SAT results (two independent encoders, every UNSAT DRAT-checked)
- **Encoder A:** `code/k1_sat.py` (fce83465…1226), F1–F4 only, bitwise support variables. The driver is
  `code/k1_certify.py` (sha256 e61ab8126463c12fd177e96e7123fd2462747584548949a44dff3f5c33c7e113)
  with CaDiCaL 3.0.1. Output: `evidence/k1A/summary.json` (3f5843c9…af2a).
- **Encoder B:** `code/k1_encB.py` (3650f603…cb6a33), stdlib only, one-hot support choice, kissat 4.0.4 proofs.
  Output: `evidence/k1B/summaryB.json` (c9ac0158…387f).

For each class, all models projected on the supports were enumerated with blocking clauses. The final CNF (base plus
one blocking clause per model) was proved UNSAT, and every proof gave `s VERIFIED` under the lane drat-trim
(`env/drat-trim`, source sha d834b649…c2ee, identical to the parent-used copy). drat-trim controls: an UNSAT CNF
with the empty proof gave `s VERIFIED`; a SAT CNF with an empty-clause proof gave `s NOT VERIFIED`.

| class | models (A) | models (B) | identical sets | model weights |
|---|---|---|---|---|
| 0–4 (maximal) | 0 | 0 | yes | — |
| 5 harmonic | 4 | 4 | yes | all 1 (the 4 remaining directions) |
| 6 equianharmonic | 5 | 5 | yes | 4 × all-1, plus one pattern with every off-frame weight 4 |

So the following holds, under the frame lemma and F1–F4:
- **No ONB-assignment exists on a maximal 4-net of order 7.**
- Every ONB-assignment on the harmonic net is classical.
- On the equianharmonic net, every non-classical assignment has the weight-4 pattern: supp ψ_p = A(p) for every
  p ∉ ℓ0, with all 4 coefficients nonzero.

## 5. Refuting the weight-4 pattern (exact, hand-checkable)
Take two points on a common line whose supports share exactly the coordinates {k, k'}. Orthogonality reads
conj(c_pk) c_qk + conj(c_pk') c_qk' = 0 with all four coefficients nonzero. Taking arguments:
(arg c_qk' − arg c_pk') − (arg c_qk − arg c_pk) ≡ π (mod 2π).
The moduli play no role. In the class-6 net, points are indexed 7x+y and carry the labels (x, y, y−x, y−3x). Under
the weight-4 pattern A(x,y) = y − x·{2,4,5,6}:

| sign | p | q | common line class | shared coordinates |
|---|---|---|---|---|
| + | 29 = (4,1) | 28 = (4,0) | 0 (x) | {5,6} |
| − | 33 = (4,5) | 28 | 0 | {4,6} |
| + | 34 = (4,6) | 28 | 0 | {4,5} |
| − | 34 | 29 | 0 | {0,5} |
| + | 33 | 26 = (3,5) | 1 (y) | {4,6} |
| + | 34 | 26 | 2 (y−x) | {0,4} |
| − | 29 | 26 | 3 (y−3x) | {0,6} |

The signed sum of the seven relations cancels every phase variable. The right-hand side becomes an odd multiple of π,
so 0 ≡ π: a contradiction. The same argument in words: write Δ_p(k,k') = arg c_pk' − arg c_pk. Rows 1–3 give
Δ_28(4,6) ≡ Δ_34(4,5) + Δ_29(5,6). Rows 5–7 give Δ_26(4,6) ≡ Δ_29(0,6) − Δ_34(0,4). Rows 2 and 5 force these two to
be equal, so Δ_34(0,5) ≡ Δ_29(0,5). That contradicts row 4.

Checker: `code/k1_phase_cert.py` (stdlib, 70eb072c…19d1). It recomputes A(p), confirms that the enumerated
non-classical model equals the weight-4 pattern, verifies collinearity and the 2-element overlaps, and checks the
exact cancellation and odd parity. Output: `evidence/k1A/phase_cycle_certificate.json` (efd6a51b…1e7c).
Only this explicit seven-relation certificate is needed. No minimality claim, independent-count claim, or
acceptance of the exploratory elimination/MILP output is made.

## 6. Theorem K1
**No set of 3 MOQLS(7) has exactly one non-classical square.** In addition:
- a maximal 4-net of order 7 carries no ONB-assignment;
- every ONB-assignment on either Desarguesian 4-net of order 7 is classical.

## 7. Controls (`code/pattern_check.py` 16e9bea8…0ce0, output `evidence/k1A/pattern_controls.json` abfd2a94…38fa)
- **C1 (genuine non-classical).** Ψ(f) of Ball–Simoens Thm 6 / Example 15 at q = 7 with H = {1,2,4}, shifted by an
  undetermined direction m0 as in the proof of Thm 6, on its 3-net (rows, columns, Φ(m)). Supports are exact: a
  coordinate is absent iff x ↦ i f(x) + (j−y)x is a permutation. Both shifts, (m0, m) = (2, 4) and (6, 3), pass
  F1–F4 and the frame lemma; the weights are {1, 5}. F1–F4 reject 84 of the 294 single-coordinate mutations; they
  are only necessary conditions.
- **C2 (genuine non-classical).** The 4 × 4 QLS printed in Ball–Simoens §2.4 passes; all 48 single mutations are
  rejected.
- **C3.** All 18 enumerated models (9 per encoder) pass the independent F1–F4 evaluation.
- **C4.** All 294 single mutations of the weight-4 pattern are rejected.
- **Void output.** A first C1 run used Ψ(f) without the shift. This f is not a permutation, so Ψ(f) is not a QLS,
  and the run reported violations. It is retired to
  `archive/void-2026-10-17/pattern_controls.v0-wrong-psi-f-convention.json` and is void.

## 8. Consequence for the remaining cases (reduction; proof here, no transfer from the 4-square paper)
Let S = {Ψ1, Ψ2, Ψ3} be a non-classical set in standard form, and let Q be the set of squares having an entry of
weight ≥ 3.

Lemma 10 (Ball–Simoens, printed proof, LF178–192) replaces a square whose weights are all ≤ 2 by a classical one.
The replacement keeps all orthogonalities and keeps row 0 unchanged: only entries of a fixed weight-2 pattern are
rotated.

A square with an entry of weight ≥ 2 in standard form is non-classical. Indeed, its rays include e_0…e_6 and one
more.
- If |Q| ≤ 1: some square Ψ is non-classical, either because it lies in Q or because the set is non-classical.
  Classicalizing the other two squares, all of whose weights are ≤ 2, yields a K1 set. Theorem K1 forbids this.
- Hence |Q| ∈ {2, 3}. After classicalizing the square outside Q, if there is one, the result is a K2 set or a K3
  set in which **every non-classical square has an entry of weight ≥ 3** in the standard frame.
