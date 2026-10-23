Labels: **20** = 20-proof-B0S-r2.md, **00** = 00-proof-K0star-r2.md, **01** = 01-proof-RED-r2.md (excerpt), **08** = 08-notes-GRX-v1.md, **12** = olson-rotation-lowodd-parent-verdict-v2.md. This audit uses only the inlined text. No files were opened and nothing was computed.

## DISPOSITION: ACCEPT-WITH-FIXES

- 0 FATAL, 0 MAJOR, 9 MINOR.
- I re-derived every inequality and every case in 20:19-88. None needs a change of formula, step or case.
- The fixes are statement precision, one unstated step that is true, and provenance hygiene.
- This is a recommendation only; I have no gate or acceptance authority.

### Per-theorem verdict
- **Theorem B0S (20:10-13): correct**, provided the common rotation letter is read as ρ_x with x ≠ 0 (see MINOR-1).
- **Corollary (20:14): correct and immediate.** A RES_<(p) word (01:132-133) with B = 0 has all rotations ρ_1, all blocks odd, F, R ≥ 1 and κ > B = 0. If k ≤ p, B0S applies.
- **20:14-15 (the claim that B0S re-proves S1′/A1′ when g = 0): not audited**, because that source is not in the packet.

## Findings

**FATAL:** none. **MAJOR:** none.

**MINOR**

1. **20:10-12: the statement is wider than the proof.**
   - "Rotation letters EQUAL (after normalisation ρ_1)" literally includes ρ_0.
   - The normalisation, and H0's G-word frame (00:19-20), both need x ≠ 0.
   - The x = 0 case is true but not proved here. It follows from the H in-block pairs plus 2κ+2 ≤ R identity rotations.
   - Repair: write "equal to ρ_x, x ≠ 0" (as in 00:156-157), or add that one line.

2. **20:30-31: Step 0's case split has a gap in wording.**
   - "Otherwise both terms are floors" skips the case g_1(E) = ⌊E/2⌋ < E−κ with g_1(R−E) = R−E−κ.
   - That case is covered only by the symmetry E ↔ R−E, which is never stated.
   - Repair: "if either term is the truncation term (WLOG the first, by E ↔ R−E)". The bound itself is right.

3. **20:82: P = Z ∪ W is never shown to be proper.**
   - H0 applies only to proper P (00:55-59).
   - It is true: Z is nonempty and proper (20:57-58), so some run outside Z is adjacent to Z. That run lies in Y∖U, so it is not in W.
   - Repair: add one sentence.

4. **20:16 (also 20:5): the import's status is overstated.**
   - "GR0 = the parent-accepted GRX" conflates two things. GR0 is GRX's {±1} specialisation (08:44-45).
   - H0 lives in K0star-r2, which says "r2 itself not re-reviewed" (00:6-7). Its proof also routes through proof-GR.md Sec. 2 (00:53), which is not in the packet.
   - **This is not a gap for B0S.** The single H0 instance it uses follows from GRX (08:18) directly:
     - Put z = +1 exactly on P (m intervals, R_P = E), with all blocks odd. Then Φ_z = 2m and C_max = 2H+2m.
     - So n = 2p−C is even and lies in [2κ+2−2m, 2p−2m].
     - Choose a rotations in P and b in P^c. Then σ = a−b and T(z) = Σ_Pθ = 2u_P, so the condition is x := (a−b)/2 ≡ u_P.
     - For an integer x, a valid integer b exists iff max(0, −2x, κ+1−m−x) ≤ min(R−E, E−2x, p−m−x).
     - The nine pairwise inequalities are exactly x ≤ ⌊E/2⌋, x ≤ p−m, x ≤ E+m−κ−1, their three mirror images, and three tautologies (E ≥ 0, R ≥ E, κ ≤ p−1).
     - Hence every integer in [−g_m(R−E), g_m(E)] is realised, for every m ≥ 1.
   - Repair: state H0's review status precisely, and include this derivation.

5. **20:16: typo in the GRX hash pin.**
   - It is cited as `afc6c31a…0a30`, but the header of 08 and 12:13 both give `…620b1a30`.
   - The pins at 20:5 match 00 and 01. This is a text comparison only.

6. **20:14-15: unaudited cross-claim.** The hypotheses of S1′/A1′ are not visible. Repair: label it as an unaudited remark, or drop it.

7. **20:6: misleading scope line.** "All rotations in one {ρ_x, ρ_−x}" describes the notation universe, but the theorem covers only the B = 0 slice. Repair: "Theorem scope: B = 0 only."

8. **20:110: wrong count in the fix map.** It says "two displayed bounds", but three changes are listed. The r2 values themselves are correct.

9. **Cosmetic issues, with no effect on correctness:**
   - 20:57: (U3) is exact from the integrality of x(P) alone. Parity is needed only to reconcile the two forms of (L3), which is equivalent to δ_P ≤ R.
   - 20:58: Φ(P) = 2(ρ_P−x(P))+2m is even for every P, not only for P ⊆ Z.
   - 20:81: parity sharpens the bound to Σ_W(r_y+1) ≤ 2d−4.

## Audited vs imported
- **Fully audited:**
  - 20:19-88;
  - the Corollary against 01:132-133;
  - (0.1) at 00:30;
  - the H0 instance used (B = 0, β = 0, every m, solvable direction), re-derived from 08:18;
  - sign and group-law consistency (00:14, 00:60, 08:30-34, 12:7, 12:30);
  - 20:108-113 checked against the r2 text.
- **Imported, not re-audited:**
  - GRX (08:18-42, parent-accepted at 12:7). I spot-checked only 08:29-34.
  - Rotation invariance (08:41-42).
  - The normalising automorphisms (00:15-17).
- **Not audited:**
  - the general form of H0 (β > 0, B > 0, I(∅)), which B0S does not use;
  - 20:14-15;
  - 20:92-106 (remarks, and the finite aids E8/E8b, which are not premises);
  - RED beyond its definition of RES_<.

## Per-question summary

**Q1 (set-up): correct.**
- If R ≥ 2p, the subword ρ_1^{2p} is an identity.
- Otherwise k ≥ 2κ+1, hence p ≥ 2κ+1, R−2κ = 2p−k ≥ p, and R−κ ≥ p+κ.
- The window g_m follows from H0 with D_P = R_P (B = 0) and β = 0 (all blocks odd), since the complement has the same m. The p−1 cap in g_1 is redundant because E ≤ 2p−1.
- The kill test is H0's solvable direction, which is the only direction the proof uses.
- For empty runs, genuineness is equivalent to u_t ≢ 0 because 2 is invertible. E = 0 windows have the form [−g_1(R), −κ] and are handled.

**Q2 (main argument): every step holds.**
- **Step 0.** The window sum is ≥ 1; uniqueness of V_j needs only ≥ −1. The congruence x_t ≡ u_t holds for t = 1 and t = k as well, since u_[k] = 0. Also Σx = p and Σbh = k−2κ.
- **Step 1.** The exact values of the eight cases are:

  | Case | Exact value |
  |---|---|
  | FFF | R−3/2 |
  | TFF | R−κ−1+ρ_t/2 |
  | FTF | (3R−α)/2−κ−1 |
  | FFT | (3R−r_t)/2−κ−1 |
  | TTF | 2p−k+(R+r_t−1)/2 |
  | TFT | 2p−k+(R+α−1)/2 |
  | FTT | 2R−2κ−(ρ_t+1)/2 |
  | TTT | 2R−3κ |

  These use only 0 ≤ α, r_t, ρ_t ≤ R, which holds with empty runs. Each value is ≥ p−2.
- **Defects.**
  - x_t lies in [−L^t, p−L^t−1], a complete residue system.
  - Therefore x_t ≥ U^t+1, which forces U^t = r_t−κ and gives (2.1).
  - Empty defects lie in [1−κ, −1], and r_t+δ_t = 2(r_t−x_t) ≥ 2.
- **Kill conditions.** (U1)-(L3) are exact equivalents of x(P) ∈ I(P).
- **Case I.**
  - Each addition changes Φ by r_t+δ_t+2Δm with Δm ∈ {1, 0, −1}, and P never reaches [k].
  - So Φ(P) ≤ 4κ ≤ 2p−2.
  - (L2) holds with room to spare (2R−2κ−2 ≥ 6κ), and (L3) holds since 4κ−2 ≤ R−1.
- **Case II.**
  - I re-derived all of the following:
    - δ_Z = 2κ−|Z|+s;
    - |Z| ≤ κ−m_Z;
    - s ≤ g_Z−2m_Z;
    - δ_Z−ρ_Z ≥ 4m_Z;
    - d is even and lies in [2, κ−1];
    - κ+1 ≤ δ_Z ≤ 2κ−2.
  - Arcs of U have length < k, so the alternate-run selection never wraps around.
  - |F| ≥ d/2 is equivalent to k ≥ 2+2|Z|−ρ_Z, which holds.
  - m(P) = m_Z+|W|, and both choices of W pass all six conditions.
- **Boundary cases.**
  - k = 2κ+1 (so R = 2p−1): the Step 0 term is p−κ−1 ≥ κ.
  - k = p (so R = p+2κ, the tight case): 2R−2κ−2 = 2p+2κ−2, which is ≥ 6κ and ≥ 2p+2κ−8.
  - κ = 1: (2.1) together with r_t+δ_t ≥ 2 gives 2 ≤ 0, so no defect can exist. Line 20:57 is then already the contradiction. This is valid but only implicit; the text should say it.
  - p = 5: Case II needs κ ≥ |Z|+m_Z ≥ 3m_Z ≥ 3, so p = 5 (κ ≤ 2) is Case I only.
  - The smallest configuration that reaches Case II is p = 7, κ = 3, k = 7, with Z two adjacent empty runs at x = −1 and |W| = 1.
- **Wrap-around.** V_j can fall outside [0, p], since g_1(0) = −κ. All the work is in ℤ, and congruence is used only at the final kill, so this causes no problem.

**Q3 (use of H0).**
- H0 is used only as "x ≡ u_P and x ∈ I(P) implies solvable", together with its contrapositive under avoidance:
  - m = 1 in Steps 0-1 and for singletons;
  - arbitrary m in Case I;
  - m ≥ 2 in Case II, where the p−m cap enters only through (U1)/(L1).
- That instance is re-derived from GRX in MINOR-4.
- No RGR-only fact is used; every step is valid when r_t = 0:
  - E ∈ {0, R} is allowed in Step 0;
  - U^t = −κ for empty runs;
  - ρ_Z ≥ |Z|−g_Z;
  - runs in W have bh = 1, so they are odd and nonempty.
- Nothing else from 00 is used: no Theorem P, Davenport-α, EGZ, (Z0)-(P0) or moves.

**Q4 (assumptions, circularity, scope).**
- No circularity: 01 supplies only the definition of RES_<.
- No finite premise.
- Hidden assumptions: MINOR-1, MINOR-3, and the implicit handling of κ = 1.
- 20:97-98 is accurate. It should also say that κ = 0 lies outside B0S (it is covered by K0*). It should also say that the Corollary bears on REFL only through Theorem RED, which assumes (I1)-(I4) (01:134). Those hypotheses are not in the packet.

## Unresolved core (untouched by B0S; not endorsed)
- RES_<(p) avoiders with B = 0 and k ≥ p+1.
- RES_<(p) avoiders with 1 ≤ B ≤ κ−1 (the MIX classes).
- REFL(p), which needs both of the above plus RED's hypotheses (I1)-(I4).
- INV*(p), which also needs rotation rigidity beyond ROT-o2 (12:39-41).
- Ordered Olson for D_{2p}.

B0S removes exactly the class {B = 0, k ≤ p} from RES_<(p), and nothing more.
