# Hostile written review: K7(a2) Unit 1

**Basis.** I used only the embedded snapshot: no tools, files, computation or delegation. I did not recompute any hash or the byte totals at `review-package-A2-unit1-v1.md:35`.

**Abbreviation.** U1 = `K7-A2-UNIT-1-v1.md` (79d948bf…9d51).

**Status.** Every Unit 1 claim stays CANDIDATE_UNVERIFIED. "PASS" below means only that this reviewer found no mathematical defect at the displayed hypotheses.

## 1. Verdict per claim

| # | Claim (U1 lines) | Verdict | Decisive check |
|---|---|---|---|
| 1 | §0 setting (9–22) | PASS + m1 | LFC labels r_j·x_uj and fibre counts n_u·x_uj/6 match LFC(a)(b). μ(D_j)=x′_aj/6 matches INV(b)/E7. d_j=r_j·x′_aj matches V2. (Γ*)*=Γ holds. |
| 2 | §2 G_z, G_t as explicit hypotheses (35–41) | PASS + m2 | The definitions are exactly what later proofs consume. The remark at 39–40 is true but unproved. |
| 3 | TC (42–45) | PASS + m6 | Both inclusions are correct. Disjointness comes from V1 in the same family. Needs three distinct vertices, as stated. |
| 4 | K3 (46–48) | PASS | Uses only TC, V4 and integrality. The restriction j,a≠z is unused but harmless. |
| 5 | B (58–61) | PASS + m7 | All W-parts with at most one four are covered: none, 1114, 1124, 1224, 2224. Each is crossed with e∈{1,2,4} and with E=1 versus E≥2. The z–two gcd is 2 for every E; the z–four gcd is 2 exactly when E=1, which is what makes the E=1 vector feasible. |
| 6 | R1 (63–64) | PASS | Each support contains one four, so no allowed triple exists. Values are 5 with y_z=0, so E plays no role (E=1 is fine). Subtracting y_A−y_B gives [f1]=[f2] on every fibre that is not z-only. |
| 7 | R1minus (65–66) | PASS | {f1,f2,s} sums to 1. The four-set and {f,s,s} are not allowed. t is coprime to every W-label. |
| 8 | R3/R3′ (67–69) | PASS + m8 | Both values are 5 with t-weight ½. Only the z-free equality clause is used. |
| 9 | R4/R5 (70–72) | PASS + m8 | L_z puts o or f in every fibre ⊄{z}; L_t excludes z-only fibres. o is coprime to everything (c=3, e∈{2,4}, 5^B never matched). |
| 10 | R6, impossible rows, "≥1 four, ≤1 one" (73–77) | PASS | Every value-6 vector is feasible. |
| 11 | Twins (79–81) | PASS | On W∪{t}, ℓ is odd, so τ_min is the largest entry. τ_max (γ=6) is the product of the two smaller entries. Hence (1,a,b) forces a=b. |
| 12 | §4 preamble (84–90) | PASS + m9 | The types are exactly 12, 13, 21, 31, 22. The complement criterion is correct. |
| 13 | K2 (92–94) | PASS + m10 | If x_as=1, twins give s F-degree 1, i.e. type 11. Otherwise K3 in Γ^{x′} at apex a gives x_at+x_as=6. |
| 14 | Type list (96–101) | PASS | W={v,g}∪N_F(v), so every vertex is covered. Parity arguments hold. Types 31 and 13 cannot coexist. Normalisation is by the actual Γ*. |
| 15 | Four-degree-1 kill (102–104) | PASS | Degree sequence 11112 has max degree 2, so no spanning K1,4/K2,3, so the complement is connected. CL then gives \|P_{x′}\|≥2, against ≤1. This kills the no-3 cases (4,0,1)/(0,4,1) and the degree-3 cases (4,0,1) and (2,2,1). |
| 16 | Case (a) (106–110) | PASS | F′=C5 and F=P5; the F′ edge list is correct. No W-ones. Triangle (t,u1,a) gives α_ta≠1. Both 4+2 K3 kills (at u1 and at b) check. |
| 17 | Case (b) (111–118) | PASS | F′ is forced uniquely in each of the three shapes. The K2 orientation in each bullet is correct. |
| 18 | Case (c) (119–123) | PASS | F∪F′=K5. The path is killed by K3 at w, then at y. This leaves F=K2,3. |
| 19 | all22 (125–131) | PASS | u and w1′ are at F-distance 2, so α*_{uw1′}=4. One 4/6+2/6 disjoint pair contradicts V4. |
| 20 | §6 reduction to M_A (133–142) | PASS | R2 is forced at x, y, w. If α_v1v2=1: R4 z-containment (needs L_z and L_t at v_i), then TC at x, then the V_t union containing D_z, D_v1, D_v2, D_y, then Sun(3) on 4ρ_y, 2ρ_v1, 2ρ_v2. The t-row 44411 has value 6. |
| 21 | EQ (144–149) | PASS | At most one small set inside B and at most two outside. Then 1 ≤ 2μ(Q)−b ≤ 10/6−b, so b=4/6. Only non-z labels are used. |
| 22 | SUB (150–152) | PASS | X_j is right ⟨Φ_j,Φ_k⟩-invariant and contains 1. The measure squeeze 1/3=μ(Φ_jΦ_k) yields an actual subgroup. L0.2 gives the coset separations. |
| 23 | IN (153–156) | PASS | The action of h_iΦ_ih_i⁻¹ is transitive. Counting fibres and excluding j's own gives x_ji ≤ 2m − 6m/n_j < 2m. |
| 24 | CELL (157–164) | PASS + m11 | KL=(LK)⁻¹=G, so all nine cells are nonempty. Piece index is n_v·m_v^L/9; in general N_j=n_j·ab/9. |
| 25 | M_A (166–178) | PASS + m12 | Order of steps: choose i′ with α_{tv_{i′}}=2. EQ at v_i (V_z, Γ^α) and SUB give K⊇Φ_v1,Φ_v2,Φ_t with the v-columns distinct. LFC at t in Γ^{α*} leaves at least two a with α*_ta=2. EQ and SUB at x give L. IN gives m_a^K=3 (pigeonhole over the v-columns) and m_j^L=3. Then LK⊇Φ_xK=G. CELL puts t and z outside the v-columns, so Φ_z⊆K, against α_zv1/6=1/2>1/3. |
| 26 | M_B (180–191) | PASS + m13 | Same chain in Γ^{α*}. Then v₃(n_z)=1 forces m_z^H=3 and N_z=2^{E+1}w_z. In t's column the t, a, z pieces have pairwise gcd 2, so Sun(3) fails. |
| 27 | H_A Case-A theorem (export 194–197) | PASS, conditional | §§4–6 exhaust the degree types, and the terminal K2,3 case is M_A at V_z(Γ^α). The inverse orientation is the actual Γ*. |

## 2. Focused checks requested

- **Marker placement and unbounded exponents.**
  - p may be any W-vertex; every gcd used only pairwise coprimality of the ρ's (prime to 6, w_z, w_t).
  - All entries lie in {1,2,3,4}, so no label multiplier is 5 and 5^B is never matched.
  - E, A and B are never bounded. E≥2 is derived exactly where it is used.
  - No LFC vector gives positive weight to both z and t, so the shared 3 never enters.
  - The cell indices 2·3^A·w_t and 2^{E+1}·w_z have gcd 2 for all E and A.
- **Actual inversion.** It is used for the type normalisation, for (2,0,3)↔(0,2,3), for the K2,3 orientation and for the \|P\|≥3 branch of all22. H_A is symmetric across the two families, so these transfers are valid.
- **Sun instances and equality saturation.** Checked in four places: the L_z equality clause, EQ (b=4/6), the SUB measure squeeze, and §6 (D_v1=D_v2). The Sun(3) triples are at U1:140, 161, 176, 188 and 190.
- **Cell reasoning.** The CELL lemma uses LK=G, not K≠L. Pieces and the index n_v/3 are established before t is placed. The crossing pigeonhole uses the two distinct v-columns.
- **Conditional joins.** Unit 1 has no Unit 2/3 premise. The only cross-unit bridge it gestures at is m2.

## 3. Findings

FATAL: none. MAJOR: none. All findings below are MINOR.

**Setting and interface (5)**

- **m1** `U1:11-12`. "At most one ρ_u has a 5-part" admits configurations with no p, so line 12's "exactly the (a2) index arithmetic" is false as written (the scope, `K7-A2-SCOPE-v1.md:15-16`, requires p∈W with B≥1). No proof depends on this.
  - *Repair:* say the setting "contains" the (a2) arithmetic and note that the existence of p is never used.
- **m2** `U1:39-40`. The remark "subset gcd 6 supplies L_z/L_t and V_z/V_t" is true but unproved here and absent from the export list (194–197). Yet line 40 implies Unit 2 gcds reach Unit 1 through it.
  - *Repair, a proof to add here:* for Q⊆V∖{u}, ⋃_{j∈Q} L_j^(u) is right Φ_u-invariant and left ⋂_{j∈Q}Φ′_j-invariant, since h_jΦ_jh_j⁻¹=Φ′_j. Its measure therefore lies in (1/gcd(n_u, T_{x′}(Q)))ℤ. It misses h_uΦ_u by LFC(b). The y-count over its fibres then gives val≤5 and the equality clause. The same argument for D_j (left Φ_u-, right Φ_j-invariant) gives V. Then add the statement to the exports.
- **m3** `U1:25-29` and the manifest. Sun(3) is applied directly (U1:140, 161–162, 176, 188, 190), but its statement is not in the excerpts: `README.md:15` only names it, and `rules-k7-v1.md:13` grants it inside subgroups.
  - *Repair:* add one line, "Sun(k): among k pairwise disjoint cosets some pair of indices has gcd ≥ k", with its accepted source.
- **m4** `K7-A2-SCOPE-v1.md:24` against `U1:25-29, 194-197`. There is no per-lemma dependency table.
  - *Repair:* add one. Suggested content:
    - B: L_t only.
    - R1, R1−, R3, R3′, R6: L_z.
    - R4/R5: L_z, plus L_t for the z-containment.
    - §6: V_t at x; L_z and L_t at v_i.
    - M_A: V_z at v_i and x in Γ^α.
    - M_B: V_z at a1 and v_i in Γ^{α*}.
    - CL: the U1:102–104 kill (and §5).
- **m5** `U1:198`. "K23 through all29 repairs" is a provenance typo, presumably for E1–E29.
  - *Repair:* correct the label.

**TC/K3 (1)**

- **m6** `U1:43`. "consequently D_j^(a)∩D_u^(a)=∅" is conditional on the containment, and the family is not named.
  - *Repair:* "…; consequently, if L_j^(u)⊆L_a^(u) (same family x), then D_j^(a)∩D_u^(a)=∅."

**B/rows (2)**

- **m7** `U1:59-61, 75`. Import over-citation. Only the no-W-four vector (value 11/2) needs L_t. The E=1 vectors (13/2), the e=1 and e=2 vectors (6), and the rows at line 75 (6) already contradict LFC's val<6.
  - *Repair:* cite LFC(d) for those cases.
- **m8** `U1:68, 72`. Two wording gaps. At line 68, the feasibility note omits R3's three-twos triple (it is covered by U1:54; cite it). At line 72, "all four L_f" is ambiguous.
  - *Repair:* line 72 should read "the L_f of every W-four (three in R4, two in R5) coincide."

**H_A classification, all22, refinement (2)**

- **m9** `U1:87-90`. F∩F′=∅, P∩P′=∅ and d+d′≤4 come from α+α*≤6 (INV(b)/E7), not from "B/row list". Separately, the sentence "A four-vertex graph cut complement…" is garbled.
  - *Repair:* "By INV, F∩F′=P∩P′=∅ and d+d′≤4; by B, d,d′≥1. Under H_A, Γ_x is the complement of F_x, and a five-vertex graph has a disconnected complement iff it contains a spanning K1,4 or K2,3."
- **m10** `U1:92`. The K2 statement is ungrammatical.
  - *Repair:* "There are no a,s∈W with deg_{F_x}(a)=1, deg_{F_{x′}}(s)=1 and N_{F_{x′}}(s)={a}."

**EQ/SUB/IN/CELL (1)**

- **m11** `U1:158-159`. "in an H-coset of Phi_v cap L" is garbled.
  - *Repair:* "in a left coset of the subgroup Φ_v∩L≤H".

**M_A/M_B (2)**

- **m12** `U1:175`. "If t shared v1's column" should cover both v's.
  - *Repair:* "v_i's column; v_{i′}'s is excluded by SUB, and v1, v2 are symmetric."
- **m13** `U1:183-191`. In M_B, H names the index-3 subgroup, which clashes with CELL's H=K∩L at U1:157.
  - *Repair:* rename it L, with cells as (K∩L)-cosets and N_z=[K∩L:Φ_z∩L].

## 4. Non-findings (optional; not counted)

- **o1. L_z follows from V_z in the other family.** L_z(u,x) is implied by V_z(u,x′), because ⋃L_j^(u)[x] is a right translate of (⋃D_j^(u)[x′])⁻¹. Unit 3 could therefore verify only V_z and V_t in both families.
- **o2. all22 does not need CL.** Since P∩P′=∅, every vertex lies outside P or outside P′. That vertex's row in the corresponding family is 2244|e≤2, and the same 4/6+2/6 kill applies.
- **o3. Redundancies.**
  - R1minus's y_B is redundant; y_A alone suffices.
  - K3's restriction j,a≠z is never used.
  - M_B uses α_{a1t}=2 only at the chosen a1, and never uses za=3.
  - No widening is needed or made, consistent with `review-package-A2-unit1-v1.md:26`.
- **o4. Open join obligations.** Unit 1 is finite-G only. These remain for Unit 3, consistent with U1:5 and U1:200:
  - the R0 lift;
  - the Lemma F no5/zt5 split;
  - the zt5 normalisation;
  - verification of c=3, entries in {1,2,4}, G_z/G_t, CL, and the M_B data.
- **o5. Unchecked overlays.** Erratum items E4/E5 (`K7-LFC-INV-erratum-v1.md:33-46`) are not embedded. The snapshot cannot confirm that they leave LFC(a)–(d) and INV(a)–(b) unchanged; the parent should confirm.

## 5. Counts

| Group | FATAL | MAJOR | MINOR |
|---|---|---|---|
| Setting/interface | 0 | 0 | 5 (m1–m5) |
| TC/K3 | 0 | 0 | 1 (m6) |
| B/rows | 0 | 0 | 2 (m7, m8) |
| H_A classification/all22/refinement | 0 | 0 | 2 (m9, m10) |
| EQ/SUB/IN/CELL | 0 | 0 | 1 (m11) |
| M_A/M_B | 0 | 0 | 2 (m12, m13) |
| **Total** | **0** | **0** | **13** |

**Conclusion.** On this reading, Unit 1's exports hold at their displayed hypotheses, and the 13 MINOR repairs are textual or accounting fixes. This is not a verdict on Theorem A2X: no (a2), K7 or Sun(7) closure follows from this packet. Sun(5)/Sun(6) remain disclosed computer-assisted transitive imports (U1:28–29). No novelty, Lean or human-review claim is made.
