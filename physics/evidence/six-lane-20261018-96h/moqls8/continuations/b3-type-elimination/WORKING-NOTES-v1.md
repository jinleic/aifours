# B3 type elimination — WORKING NOTES v1 (NOT a package; no family eliminated)

Written at 2026-10-19T17:32:18-0700 under `SCOPE-FREEZE-v1.json` (SHA256 `875e31d56902d6829535fe9395747ef77ae6029944c81d0d8f63199f1aba1555`). Status: working notes only.

The packaging rule of the transition [TR] forbids packaging before at least one whole family is eliminated. **No whole family is eliminated here.** These notes record the proved reductions and laws so that the work is reusable, together with the exact blocker. Everything is written by hand; no script, assertion or machine enumeration was used. Notation, hypotheses H1-H4 and the type definitions are those of the joint-completion candidate [JC], which is not a premise. The items used below are re-proved or are elementary.

## 1. Symmetry reduction (proved)

Each move below is a genuine move Q'_{τ(s)}(ρ(i),σ(j)) = P_σ Q_s(i,j): a common row permutation ρ, a common column permutation σ, the same coordinate unitary P_σ on every square, and a relabelling τ of squares. Such a move preserves the QLS and pairwise-orthogonality axioms [PRIM]. It preserves standard row 0 when σ fixes 0 and ρ fixes 0, because Q'(0,σ(c)) = P_σ e_c = e_{σ(c)}. It preserves SB2 when ρ fixes row 1, σ maps {1,2,3} to itself, and τ(s) = σ(s+2) − 2. It preserves the exact template iff σ(T_i) = T_{ρ(i)} for i = 2..7, where T_i is the template support. ROWLEX then holds because the template keys are reproduced row by row.

- **ρ23 := (ρ = (2 3), σ = id, τ = id).** It preserves the template because T_2 = T_3. Effect: J_2 ↔ J_3, q_1^2 ↔ q_1^3, t ↦ 1−t. All I-sets and C data are unchanged, since I_6, I_7 ⊆ R' avoid rows 2 and 3.
- **ρ45 := (ρ = (4 5), σ = id).** The C analogue: J_4 ↔ J_5.
- **b := (σ = (6 7), ρ = id, τ = (4 5)).** It preserves the template because T_2 = T_3 = {6,7}. Effect: I_6 ↔ I_7, since column 6's B-content ∝ e_7 is sent to column 7 as ∝ e_6. J_2 and J_3 are unchanged, because σ fixes the columns {1..5}. t ↦ 1−t.
- **a := (σ = (4 5), ρ = id, τ = (2 3)).** The C analogue: I_4 ↔ I_5.
- **c := (σ = (4 6)(5 7), ρ = (2 4)(3 5), τ = (2 4)(3 5)).** It preserves the template: σ{6,7} = {4,5} = T_4, T_5 and σ{4,5} = {6,7} = T_2, T_3, while rows 1, 6, 7 are fixed. Effect, the B↔C twin:
  - (J_2,J_3) ↦ (J'_4,J'_5) = (σJ_2, σJ_3), with σ mapping {1..5} onto {1,2,3,6,7}. Row 2's content ∝ q_1^3 becomes row 4's content ∝ P_σ q_1^3 = q'^5.
  - (I_6,I_7) ↦ (I'_4,I'_5) = (ρI_6, ρI_7), with ρ mapping R' onto R'_C. Column 6's content ∝ e_7 becomes column 4's content ∝ P_σ e_7 = e_5.
  - Symmetrically, (J_4,J_5) ↦ (J'_2,J'_3) and (I_4,I_5) ↦ (I'_6,I'_7).

**Orbit count.** A swap of the two sets acts on the 9 types T1-T9 with the orbits {T1}, {T2}, {T3,T5}, {T4,T6}, {T7}, {T8}, {T9}. For example T3 (J_2 = {a}, J_3 = {a,b}) ↔ T5 (J_2 = {a,b}, J_3 = {a}).
- Each block/frame pair therefore has **7 representatives**, giving 7 × 7 = 49 for the B pair (common, own).
- The twin c exchanges the B pair with the C pair. So the 9^4 = 6561 combinations reduce to **(49^2 + 49)/2 = 1225 orbit representatives**: unordered pairs {B-pair representative, C-pair representative} with repetition.
- Column relabellings such as σ = (2 3) preserve the abstract types and give no further reduction.

## 2. Global laws proved here (beyond [JC])

**(Λ1) Overlap parity laws in the B-region R' × {1..5}.** Let w := <e_6,q_1^2> conj(<e_7,q_1^2>) and u := conj(<e_7,q_1^2>) <e_7,q_1^3>. Both are nonzero.
- Since |q_1^2><q_1^2| + |q_1^3><q_1^3| = P_B, the (6,7) entry of D(a) is (x_a − y_a)w.
- The (q^2,q^3) entry of E(r) is (y'_r − x'_r)u.
- Therefore, in column a, the cells whose B-part has both coordinates 6 and 7 must number at least one if x_a != y_a, and must not number exactly one if x_a = y_a. In every row r ∈ R', such cells number 0 or at least 2, because E(r) is e-diagonal.
- Dually, in row r the cells whose B-part has both own indices 2 and 3 must number at least one if x'_r != y'_r and must not number exactly one otherwise. In every column they number 0 or at least 2.
- *Proof.* Expand the vanishing or prescribed off-diagonal entries as sums over the cells. A single nonzero term cannot vanish.

**(Λ2) Tightness forcing pure vectors in squares 2..5.** Suppose |R_d(a)| + [a ∈ J_2] + [a ∈ J_3] = 3 for a column a ∈ {1..5} and d ∈ {6,7}. Then each square s >= 2 carries coordinate d in column a at exactly one of the 4 free rows, and Q_s(i,a) = ω e_d there. The four squares fill the four free rows bijectively.
- *Proof.* The coordinate-d mass of each square in column a is 1. By (F2) the four squares occupy pairwise disjoint nonempty subsets of the 4 free rows, so each occupies exactly one row and carries its full mass there. A unit vector with |<e_d,v>| = 1 equals ω e_d.
- The own-frame dual: if row i ∈ R' has |C_k(i)| + [i ∈ I_6] + [i ∈ I_7] = 3, then Q_s(i,c) = ω q_s^k at one free column for each s >= 2, bijectively.

**(Λ3) Exclusivity.** A square has at most one cell proportional to a fixed vector in each row and in each column (orthonormality). Combined with (Λ2) and with the row saturation of [JC] Theorem K2 (re-proved there by the same counting), this pins down the pure vectors of squares 2..5 in rows 2, 3 and in the tight columns.

## 3. The exact blocker

These laws were applied by hand to:
- the extremal B-families T7 × T7' (two L4 columns and two L4' rows);
- T9 with saturated rows 2 and 3 and an arbitrary own type;
- the cross-block configuration B-T1 × C-T1 sharing a column a ∈ {1,2,3}.

They were applied together with:
- the P4 capacities, the local tables LC/LR, the compatibility law X and the A couplings;
- the row saturations, the column tightness forcing (Λ2), exclusivity (Λ3), and the own-index and coordinate disjointness of the forced pure vectors.

**No contradiction was derived in any of these families.** In each case the forced pure placements, the mass identities (including the totals 4 and the B-region operator identity sum = 4 P_B) and the parity laws could be accommodated at this level by the flexible lines L9 and L9'. This is reported as "no contradiction derived". It is NOT a proof that any family is consistent.

Consequently **no whole family is eliminated**, and by the transition's rule no package is produced. A family elimination appears to need what this note does not have:
- coupling with the A- and Z-content in rows {1,6,7} × columns {1,2,3};
- or the interior line frames, which are unknown vectors.

For calibration only (not a premise): the qualified computer-assisted GA certificate for the related Boolean input P1-B3.M2 needed a 671,174,069-byte checked proof.

## 4. Sources

- [TR] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-slot-transition-moq-20261019-1726-v1.json`, SHA256 `436f3a38c4483258cc186b8b48051eddfc55d78821123b187314fd07d2b327a3`.
- [SC] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-type-elimination/SCOPE-FREEZE-v1.json`, SHA256 `875e31d56902d6829535fe9395747ef77ae6029944c81d0d8f63199f1aba1555`.
- [JC] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-joint-completion/B3-JOINT-COMPLETION-CANDIDATE-v1.md`, SHA256 `b19cfabb4a8fb863aa4e4e118bbe2f97d403cde0d0583b2e0e0250ca76eec3d9`.
- [PRIM] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16/sources/2607.12933v2.raw.txt`, SHA256 `265851e451cc30706b0a4ea1860c5f04568d99be85896c7b049f95c995108df9`.
- [J] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-gb-parent-binding-v1/GBBINDING.json`, SHA256 `d917203deb29a13e212c290e227a001a695765d080a897141d6dc154d79fc673`.
