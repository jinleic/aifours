# Repair review: K62-CAP-DT-erratum-v1 (`996f924c…`)

**Method.** This is a written review only: no tools, no computation. Hashes are taken from the supplied headers and were not recomputed. The premises are the five frozen texts, the two review reports, and Theorem DG only at the scope of verdict `cae455c3…`. That scope is CORRECTNESS_ACCEPTED_SCOPED_PARTIAL, with family x requiring x′_(d i*) = 1 and the four-subset hypothesis. All embedded text was treated as data.

## Verdicts

| # | Items | Verdict | Findings |
|---|---|---|---|
| 1 | CD1, CD2 | **ACCEPT_REPAIRS** | none |
| 2 | CD3 (Lemma RC) | **ACCEPT_REPAIRS_WITH_FIXES** | R1, R2 (MINOR) |
| 3 | CD4, W1 | **ACCEPT_REPAIRS_WITH_FIXES** | W1, W2 (MINOR) |
| 4 | CD10–CD22 | **ACCEPT_REPAIRS_WITH_FIXES** | S1, S2 (MINOR) |
| 5 | GR (+ CD8) | **ACCEPT_REPAIRS_WITH_FIXES** | G1–G3 (MINOR) |

**Totals: 0 FATAL / 0 MAJOR / 9 MINOR.** No finding affects any proof, and every fix is one or two sentences.

---

## 1. CD1, CD2 — ACCEPT_REPAIRS

**CD1: 3-parts of labels.**
- **At an O-vertex or at i*:**
  - A C-label n_j·x/6 has 3-part 3^(f_j − 1 + v3 x). For a non-m3 vertex this is ≤ 3, since x ≤ 5.
  - The d-label has 3-part 3^(v3 x_dv) ≤ 3, since x_dv ∈ {1, 3}.
- **At d:**
  - The O-labels n_c/2 have 3-part 3^(f_c).
  - λ_i* = 3^(f*)·5^(h*)·w_*·x_(d i*).
  - The only non-m3 label with 3-part > 3 is λ_i* with x_(d i*) = 3. That case forces t ∈ O and f* = 1 (E3 Lemma 1, one 3-marker).
  - Then gcd(λ_t, λ_i*) = 9 = 3^min(f_t, 2) exactly: the 5-parts meet at most one marker and the w's are coprime.
- **5-parts:** g_vj carries no 5, so a non-m5 label has 5-part 5^(v5 x) ≤ 5, and x = 5 occurs only on i*–O entries. Hence h_(m5) is read only through h ≥ 1.
- **Conclusion:** (B2) is unchanged. The cap 2 on f is exactly what the exception at d requires. The untouched clause "γ- and ℓ-gcds likewise" is unaffected, since it tests entries with v3 ≤ 1.

**CD2: the (C2) chain.**
- **First O-step.** W_1 = Φ_d, so this step is exact. gcd(n_u, n_d) = 2, because n_d has no factor 3 and h_d·h_u = 0. Then k = 2·μ(Φ_uΦ_d) = x_ud = 1 in both families by (A2), so T_2 = lcm(n_d, n_u) contains a factor 3.
- **Later O-steps.** Each later step has gcd 6:
  - 2-part 2;
  - 3-part 3, because t, if present, is u, so f_e = 1;
  - 5-part 1: if e = p, then h_d = h* = 0, no earlier O-vertex is 5-marked, and every k ∈ {1, 2, 3};
  - w-part 1.
  
  Hence k ≤ 6·(1/2) = 3.
- **Final gcd.** gcd(n_i*, T) = 4·3·1·1 = 12:
  - v2 T ≥ e_d;
  - f* = 1;
  - if h* ≥ 1 then T is 5-free;
  - w_* is excluded.
- **Coverage and statement.** The chain covers t absent with p ∈ O, p absent, t = p, and markers on i*. The statement is unchanged, and (C2) now holds with equality.

## 2. CD3 Lemma RC — ACCEPT_REPAIRS_WITH_FIXES

**What I checked.**
- **Translation.** Setting g_v = 1 conjugates every U*_j by one common element. So T_α* is unchanged and U*_v = U_v.
- **Exact double count.** L_j = g_jU_jU_v is the union of exactly t_j = n_v·x_vj/g_vj fibres. With S_F = {j : F ⊆ L_j}, we get Σ_j y_j t_j = Σ_F y(S_F) (LFC (a)–(b)).
- **Light fibres are unoccupied.** Suppose wu ∈ L_j with w = g_j a g_j⁻¹. Then g_j⁻¹ ∈ U_jU_v, so g_j ∈ U_vU_j and g_jU_j meets U_v. That contradicts disjointness. So every fibre in W′U_v has S_F = ∅. U_v is among these fibres, so (RC) contains LFC (d)'s bound 1 − 1/n_v.
- **Count of light fibres.** M = [W′ : W′∩U_v] = [G : W′∩U_v]/T ≥ lcm(n_v, T)/T = n_v/gcd(n_v, T). Equality holds iff [G : W′∩U_v] = lcm(n_v, T). No equality case is claimed or needed.
- **Occupied fibres.** S_F is λ^α-allowed (LFC (c)), so y(S_F) ≤ 1. Hence n_v·Σ ≤ n_v − M. The bound is nonstrict, with no slack depending on n_v.
- **Granularity.** The x-row uses T_x′, the opposite family.
  - The α* case goes through the inverted configuration: it has the same indices, α-matrix α* (INV (b)), and conjugated family (U_j). This gives T_α.
  - The VFC form bounds the x′-row by the x-granularity: Φ_vW misses every D′_j by (V1), and μ(Φ_vW) ≥ 1/gcd(n_v, T_x). This is the same rule seen from the other side, and it is exactly CI's use of (C1) for its own family x with x_(d i*) = 1.
- **Instances.**
  - (RC-O) needs v ∈ O unmarked and x′_(d i*) = 1. Then (C1) for x′ gives gcd | 6, so the bound is 5/6.
  - (RC-i*) needs only f* = 1, because i* is not in the (C2) chain. It holds in every orientation, with bound 11/12.
  - These are exactly the frozen Consequences in their frozen orientations. No proper-subset grid is introduced.

**R1 (MINOR, scope).**
- **Problem.**
  - (RC) is stated "for a vertex v", which includes d, marked O-vertices and i* with f* ≥ 2. The proof is valid there, so there is no gap.
  - However, this is a new statement beyond the frozen paragraph, which contradicts the Rules line "No statement changes".
  - (D2) also admits "Lemma RC" wholesale. Outside (RC-O)/(RC-i*), the quantity gcd(n_v, T_x′(V∖v)) is not a function of π, and an index T is not in (D3)'s list of non-π slacks.
- **Fix.** Add to CD3: "Rules import Lemma RC only through (RC-O) and (RC-i*). Elsewhere the slack is not a pattern quantity, and (D3) yields only Σ < 1, i.e. LFC (d)." Alternatively, restrict the statement to the two cases, as Claude m3 did.

**R2 (MINOR, provenance).**
- **Problem.** The Provenance line says "Lemma RC is LFC (a)-(d) plus index arithmetic". In fact the proof uses LFC (a)–(c) and supersedes (d). It also uses L0.1 with Lagrange and, for x = α*, INV (a)–(b) with E6.
- **Fix.** Correct that line.

## 3. CD4, W1 — ACCEPT_REPAIRS_WITH_FIXES

**What I checked.**
- **(D1) is decidable from π.** Markers, orientation, f* = 1 (equivalent to m3 ≠ i*), and the four-subset hypothesis via r_Q = min(ê_d, δ_x(Q)) from (π4).
- **(D4).**
  - r_R = min(ê_d, 1 + v2 τ_x(R)) ≤ 5 is a function of π, so S_x is one as well.
  - 32·S_x ∈ ℤ, so S_x < 38/32 gives S_x ≤ 37/32.
  - When ê_d = 4, 16·S_x ∈ ℤ, so S_x ≤ 18/16.
  - DG-1 fixes the grid but not the value.
- **Counterexamples.**
  - **n_d = 16** (e_d = 4, h_d = 0, w_d = 1): DG gives S ≤ 17/16. But 18/16 = 8·(1/8) + 2·(1/16) passes S < 19/16 and the 1/16 grid.
  - **n_d = 32:** DG gives S ≤ 36/32. But 37/32 (for example 9·(1/8) + 1/32) passes.
  - These are arithmetic counterexamples, which is enough to refute equivalence; realizability is not needed.
  - In this class n_d ∈ {16, 32} or n_d ≥ 64, so "absorbs only when n_d ≥ 64" is accurate for the 1/32 grid.
- **Transfer.** The quantifiers are right:
  - ∀Γ, π(Γ) ∈ U62;
  - surjectivity is not needed;
  - full coverage is required;
  - no element-wise check exists.
- **Equivalence uses removed.**
  - (3c) now says "implies" (CD11).
  - B4 uses only the implication.
  - CD22 confines the DG weights to the (D) forms.
  

  - One consumer is still loose: the CD18 residual description (finding S2).

**W1 (MINOR, false statement).**
- **Problem.** W1 says "Both claims are false", but the N(O) claim is true.
  - N(O) is the integer fibre count of DG-1; (D) itself lists it among the absolute counts.
  - 8 | n_d, since e_d ≥ 4.
  - Hence N(O) ≤ n_d/8 − 1/2 ⇔ N(O) ≤ n_d/8 − 1 ⇔ N(O)/n_d < 1/8.
  - Equivalently, DG-1's grid step 2^(−r_O) ≥ 1/n_d > 1/(2n_d) absorbs the slack.
  - Only an argument that rounds N(O)/n_d onto the 1/32 grid would be invalid, since r_O can exceed 5.
- **Fix.** Replace with: "The first claim is false (counterexamples below). The second holds by integrality, but it is withdrawn as unneeded, and no rule relies on it."

**W2 (MINOR).**
- **Problem.** The bold (D) sentence "Strict weakenings are lossy; they are not equivalent to their sources" is false as a universal. The DG-2 example in (D3) itself is lossless.
- **Fix.** Replace with: "Strict weakenings are labelled LOSSY. No rule or consumer may use one as an equivalence, and some are strictly weaker than their source (Theorem DG (a) at n_d ∈ {16, 32})."

## 4. CD10–CD22 — ACCEPT_REPAIRS_WITH_FIXES

**What I checked.** No item changes a quantifier or a proof dependency.
- **CD10.**
  - A triple's raw depth is 1 + v2 τ ≤ 5, and its capped depth is r = min(e_d, raw).
  - r ≥ 4 ⇔ raw ≥ 4, because e_d ≥ 4.
  - T1 and T2 have depth 4. T3 has raw depth 5 and capped depth min(e_d, 5).
- **CD11.**
  - Using Σθ_r = 10 and r ≥ 1: 32·S = 16θ1 + 8θ2 + 4θ3 + 2θ4 + θ5 = 40 + 12θ1 + 4θ2 − 2θ4 − 3θ5.
  - So 32·S ≤ 37 is equivalent to the displayed inequality.
  - "Implies" is correct, and the case e_d = 4 is handled.
- **CD12.**
  - The labels are λ_u = w_u·x_vu, λ_i* = 2·3^(f*−1)·5^(h*)·w_*·z and λ_d = 2^(e_d−1)·5^(h_d)·w_d.
  - gcd(λ_d, λ_i*) = 2^(1+v2 z), times 5 exactly when h_d ≥ 1 and z = 5.
  - The withdrawn sentence is used nowhere else: CI steps 2 and 4 involve neither λ_i* nor entries equal to 5.
- **CD13.**
  - The positive non-1 labels {2w_u, λ_d} have pairwise gcd 2. So, by Sun(3) and heredity, an allowed set holds at most two half-weights.
  - The value is 11/2.
  - The counterexample {two, i*, d}, with gcds 2, 2, 10, is genuine.
- **CD14.**
  - The positive labels {2w_u, the single 4w_u′, λ_i* with z odd} have pairwise gcd exactly 2.
  - The values are 5 + z/2 ≥ 11/2.
  - The zero-weight d-label is irrelevant.
- **CD15, CD17.**
  - The renames are correct.
  - The complement {ab, ea, eb, ec, eq} of the diamond contains one triangle.
  - By B1, c and q have H_x-degree exactly 3, so B2 applies with fourth neighbour e.
  - The parity statement now concerns only x′_(c i*) and x′_(q i*).
- **CD16.**
  - CI′ removes (1,4,4) cherries, τ = 8 on (2,4,4) and τ = 16 on (4,4,4), so θ5 = 0.
  - In branch 2: raw depth ≥ 5, v2 T(Q∖e) ≤ 4 and v2 m_e ≤ 2 give exactly the two stated alternatives.
  - DG-4 for x = α via INV is within scope in G, since α*_(d i*) = 1. This makes an existing dependency explicit rather than adding one.
- **CD18.**
  - The case division (exactly one diamond family, or none; never both) is exhaustive.
  - No connectivity is assumed.
  - The (1,3)/(3,1) split is correct: DG for x needs x′_(d i*) = 1, while CI′ for x needs x_(d i*) = 1.
- **CD19–CD21.**
  - n_4(α) = N41 + N42 and n_1(α) = N14 + N11 + N12; symmetrically for α*.
  - Put s = N41 + N14 and L = N12 + N21.
  - s = 1: N11 = 0, L ≤ 1, N22 ≤ 4 − 3L, and N42 + N24 = 9 − L − N22 ≥ 5, with equality only at L = 0, N22 = 4.
  - s = 2: N42 + N24 ≥ 6. s = 3: N42 + N24 = 7.
  - Entries 1 occur on s + N11 + L ≤ 3 pairs.
  - CD21 correctly supersedes the old DT-C erratum.
- **CD22.**
  - H_x-degree 1 means the x-row has three O-entries in {1, 2} and one 4, so (R3) applies under (RC-O).
  - H_x-degree 3 gives H_x′-degree exactly 1 and x′_(v i*) even, and says nothing about x_(v i*).
  - If both i*-entries are even, the pair is (2,2), (2,4) or (4,2).

**S1 (MINOR).**
- **Problem.** CD18 says the patterns not excluded by Parts A–B "are" those satisfying (R3), (R4), B1–B5 and the imports.
  - This omits Corollary CI′, which is a Part A exclusion not implied by that list.
  - Example: a (1,4,4) cherry with both edges tight, in a family x with u(x) ≥ 1 elsewhere, satisfies the whole list, because B4 is vacuous there. CI′ excludes it.
  - So, read as an identity, the sentence is false.
- **Fix.** Add "CI′ (both families, every O-vertex)" to the list, or replace "are" with "lie among".

**S2 (MINOR; the remaining W1/CD4 consumer).**
- **Problem.** "Satisfy … K62-SH/DG constraints" has to mean the pattern-level forms:
  - S_x ≤ 37/32, or ≤ 9/8 when ê_d = 4;
  - the DG-1 grids;
  - DG-4 in raw depths.
  
  The n_d-dependent forms are not predicates on U62.
- **Fix.** Insert "(in their CAP (D3)–(D4) forms)".

**Editorial (not counted).** CD19 keeps the frozen pairing "C2 for α* (…) and for α (…): n_4(α) ≥ … and n_4(α*) ≥ …", which is in reverse order. By (3b) and B5, C2 for y yields n_4(y) ≥ 2n_1(y) + 2 and needs y′_(d i*) = 1. This is harmless in G, but reordering it would avoid a misreading in (1,3)/(3,1).

## 5. GR (+ CD8) — ACCEPT_REPAIRS_WITH_FIXES

**What I checked.**
- **Every CONDITIONAL ON DG label is covered:**
  - DT-A status line (via CD8) and the DT-A §3 heading;
  - DT-B Labels and the §3 and §4 headings;
  - DT-C Labels and the C3 heading.
- **Every consumer lies in orientation (1,1).** For DT-A §3 this follows from its first sentence; DT-B and DT-C sit inside G. So DG applies to both families at the accepted scope.
- **The four-subset hypothesis is explicit.** It is stated in (3c) (CD11) and is B4's case split (CD16). The other branch of B4 uses DG-4, not Theorem DG.
- **Row-bound citations are correctly oriented.**
  - "Lemma RC with (C1) for the opposite family" has the right orientation.
  - "(RC-i*), needs f* = 1" is correct.
  - CI's use of (C1) for its own family x is a VFC union bound on the x′-row, consistent with Lemma RC, and is correctly left untouched.

**G1 (MINOR, coverage).**
- **Problem.** GR's quoted strings occur verbatim only in DT-A. These two citations are not covered literally:
  - DT-B Labels: "the 5/6 row bounds of `K62-CAP-v1.md` (C)";
  - DT-C Labels: "5/6 bound of `K62-CAP-v1.md`".
  
  Both still resolve correctly through the overlaid CAP, and (RC-O) holds in G, so there is no gap.
- **Fix.** Quote these two strings in GR.

**G2 (MINOR, stale label).**
- **Problem.** After GR, DT-B Labels still carries "(`K62-DG-v1.md` a4bfc41e… + erratum e435430c…, under dual review)".
  - "Under dual review" is now stale.
  - The list omits `K62-SH-DG-erratum-v1` 755edc21…, and the verdict requires DG to be read through it.
- **Fix.** Supersede that parenthetical, as CD8 does for DT-A.

**G3 (MINOR, label completeness).**
- **(a) Problem.** B4 also depends on Lemma DG-4 (verdict item 3; e unmarked; family swap via INV in G), but the GR reading names only Theorem DG.
- **(a) Fix.** Add DG-4 to the GR reading.
- **(b) Problem.** CD9 makes DT-A §1 cite DG-3 in its G3 form and claims it "applies verbatim to either family". That goes beyond the verdict's statement, which as written is phrased for τ*. It is also outside DT-A's import list, while CD8 still calls §1 "unconditional (given the imports below and (C1))". The claim itself is harmless, because the same constraints follow from the accepted rules-k7 L1 (with INV for α*), as both reviews checked.
- **(b) Fix.** Either cite L1 + INV in §1, or name G3 (verdict cae455c3…) in the §1 label.

---

## Conclusions now supported

These hold after the MINOR fixes. All files remain candidates until the parent's verdict on this round. They are partial necessary conditions only, and none of them excludes a sub-case of the residue.

**CAP-62**
- **(A)** π(Γ) ∈ U62 for every configuration of the residue. This covers every marker placement and all three d–i* orientations.
- **(B)** The listed quantities are functions of π. The absolute counts t_j, M and N(Q), the indices n_v and n_d, and the slacks are not.
- **(C1)** If v ∈ O is unmarked and x_(d i*) = 1, then gcd(n_v, T_x(V∖v)) divides 6.
- **(C2)** If f* = 1, then gcd(n_i*, T_x(V∖i*)) = 12, for both families and all orientations.
- **Lemma RC**
  - (RC-O): the x-row bound is 5/6 when v ∈ O is unmarked and x′_(d i*) = 1.
  - (RC-i*): the bound is 11/12 when f* = 1.
  - It also holds in VFC form. It gives no grid of proper subsets.
- **(D)** Only the transfer implication is established. No coverage of U62 is supplied.

**DT-A**
- **§1:** the apex table holds in both families. "Admissible" makes no realizability claim.
- **§2:** CI and CI′ hold for v unmarked and x_(d i*) = 1.
- **§3,** in orientation (1,1) at DG's accepted scope:
  - (3a): the deep-triple types T1–T3, with raw and capped depths distinguished;
  - (3b): n_4(x′) ≥ 2u(x) + 2 and n_4(α) + n_4(α*) ≤ 10;
  - (3c): under the four-subset hypothesis, 2θ4 + 3θ5 ≥ 3 + 4θ2 + 12θ1. DG (a) implies this but is not equivalent to it.

**DT-B (G only)**
- (R4) and (R3), with the positive-support certificates.
- B1–B3.
- B4 and B5, including the oriented parity at c and q.
- §4 as a description of what remains, not a characterization.

**DT-C (G only)**
- **C1:** 2N41 + 2N14 + 5N11 + 3N12 + 3N21 + N22 ≤ 6.
- **C2:** 3 ≤ |H_α| ≤ 7 and 3 ≤ |H_α*| ≤ 7.
- **C3:**
  - N41 + N14 ∈ {1, 2, 3};
  - N42 + N24 ≥ 5, ≥ 6, = 7 respectively;
  - at most 3 O-pairs carry an entry 1;
  - N11 = 0.
- **C4:** the parity facts, in their stated orientations.

## OPEN

- **Marked sub-cases.** Every sub-case with t and/or p in O, in every orientation, remains open. This includes (1,3) and (3,1), where:
  - Theorem DG holds for one family only;
  - CI′ and (RC-O) hold for the other family only;
  - (R3) and (R4) do not transfer.
- **Remaining G-patterns.** These are the patterns satisfying (R3), (R4), CI′, B1–B5, C1–C3 and the pattern-level E3/SH/DG/L1 constraints. They include:
  - the branch with the 3-marker on i* (f* ≥ 2, where (RC-i*) is unavailable);
  - the branch with the 5-marker on d;
  - the weight details when ê_d = 4.
- **Coverage of U62.** Nothing has been enumerated, so (D) proves nothing about the residue yet.
- **Full K6.2*** with e_d ≥ 4, e* = 2.
- **K7 and full Sun(7).**
- Sun(5) and Sun(6) remain computer-assisted imports in every closure.

No claim is made of full K6.2*, Sun(7), novelty, Lean verification or human review.
