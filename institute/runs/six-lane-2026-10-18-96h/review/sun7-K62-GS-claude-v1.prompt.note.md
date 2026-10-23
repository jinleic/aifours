# Hostile review: K62-GS-v1 (`020fdc7a…4627`, 213 lines)

**Bottom line.** Theorems FB and GE and Corollary OM are correct as written. I found no FATAL or MAJOR issue. There are six MINOR findings, all citation or wording, and none changes a proof step.

**Basis.** I reviewed the pasted text against the parent-accepted statements at their verdict scopes:
- CAP-DT `84061c6f` items 5–6, with CD3, CD9, CD13, CD17, V4 and V11.
- SH-DG `cae455c3` items 3–4, with G3, G4 and G6.
- E3 `576969dd`, with Z11.
- LFC/INV `8621e744`, with E1, E6 and E7.
- `73a25ba6` with rules-k7 L1 and VFC, plus README L0.1, L0.6 and R0.

I did not use as premises: the author's requested checks, the mutation controls, the scope disclosure, the IRC hint, historical headers, or the HD/GX files. I used no tools or computation and recomputed no SHA256.

## 1. Verdicts

| Claim | Verdict | Findings |
|---|---|---|
| **Theorem FB** | **ACCEPT** | none against the proof |
| **Theorem GE** (finite, plus R0 transfer) | **ACCEPT** | none |
| **Corollary OM** | **ACCEPT** | scope correct |
| P1 (O-values, edge-disjointness) | ACCEPT-WITH-FIXES | m1 |
| P2 / P4 (triangle table, apex identity and equality) | ACCEPT | m3, m5 |
| P3 (chain step with equality case) | ACCEPT | — |
| EQ | ACCEPT | m4 |
| BUD, DEG | ACCEPT | — |
| T16, ONE (new) | ACCEPT | — |
| TRI (new) | ACCEPT-WITH-FIXES | m2 |
| DEEP (new) | ACCEPT | m6 |

**File as a whole: ACCEPT-WITH-FIXES.** FATAL 0, MAJOR 0, MINOR 6.

## 2. Findings (all MINOR)

**m1. P1's {1,2,4} comes from a proof sub-claim, yet §2 says "each proved here"** (`K62-GS-v1.md:42`, `:54–55`)
- E3-a is C2 sub-claim (a) (Z11). The E3 verdict (`sun7-K62E3-parent-verdict-v1.md:29`) kept this Lemma-2 extension as a proof sub-claim and explicitly did not broaden an accepted statement.
- It is disclosed, so not a hidden promotion. It is true, and it is already a premise of accepted DG-3/G3. But P1 imports it as a standalone result and does not prove it.
- **Repair, in G:**
  - x ≤ g − 1 = 5 by E1.
  - Value 3 is excluded by accepted Lemma 2; value 5 is excluded by Lemma 2 when h_d ≥ 1.
  - If h_d = 0 and x_vu = 5, then λ_u = 5w_u and λ_d = 2^(e_d−1)w_d are coprime. So y_u = y_d = 1 is feasible, and val = 5 + 3 = 8 ≥ 6 contradicts LFC (d).
  - For α*, apply this to the inverse via INV (a)/E6.
- Also reword `:54` as "derived here from the §1 imports". P1, P6 and P7, and EQ's both-tight branch, are import assemblies.

**m2. TRI is literally false as worded** (`:134–135`)
- "…and two of its triangles share an edge" fails for every admissible graph with at most one triangle.
- Counterexample: {pq, qr, rp, sf}. It has maximum degree 2, no K4, no bowtie, and one triangle.
- The proof (`:136–140`) actually establishes "any two distinct triangles share an edge". That is all GE Step 1 uses (t = 2 ⇒ diamond), so nothing downstream breaks.
- **Repair:** "at most two triangles, and any two distinct triangles share an edge (hence two triangles form a diamond)".

**m3. Forward reference from P2 to P4** (`:67`)
- This is not circular: P4's proof (`:89–91`) uses only the definition of τ, lcm = 6w_aw_bw_c, and L0.1.
- **Repair:** state the apex identity before the table.

**m4. EQ does not state its setting** (`:96`)
- The both-tight branch needs v unmarked and x_(d i*) = 1, which is CI.
- The one-tight branch needs n_a = 6w_a and n_b = 6w_b, so that the local indices are coprime.
- Both hold in G but not in general.
- **Repair:** begin the statement with "In G, …".

**m5. DG-3/G3 cited for P2 in both families** (`:46`)
- DG-3 is accepted for the α*-family.
- CAP-DT erratum-v2 V11 (`K62-CAP-DT-erratum-v2.md:211–227`) replaced exactly this "either family" citation with L1 + INV.
- P2 is fully re-derived in the file for the actual x-configuration, so this citation is only a cross-reference and not a domain violation.
- **Repair:** cite L1 + INV (a)/E6, as V11 does.

**m6. Bookkeeping** (`:195`, `:31`)
- FB also uses P1 (m_e ∈ {1,2,4}) and P2 (deep types, and τ ≤ 8 for (2,4,4)).
- DEEP also uses P2.
- "EQ → BUD → DEG" is a listing order, not a dependency chain.
- At `:31`, note that raw-depth "deep" equals DG's capped notion because e_d ≥ 4.
- The dependency graph stays acyclic.

**Observation (no repair needed).** In FB (v), at `:158–159`, the set equality from P3's equality clause is not needed. μ(Φ_bW_(R_b)) = k_b/6 = 2/6 already follows from k = 6μ. The equality clause is correct but carries no load anywhere.

## 3. Verification record

All steps below run on actual subgroups and double cosets of the configuration, or of its actual inverse (INV (a)). None reasons over abstract matrices or the CAP-62 pattern map, and none bounds f*, h_d, h* or the w-parts.

**P3 (chain step).**
- Base case: T({j}) = 6w_j.
- Induction step: W_(S+e) ≤ Φ_e and W_(S+e) ≤ W_S, so lcm(n_e, T(S)) divides T(S+e).
- By L0.1, μ(Φ_eW_S) = T(S+e)/(n_eT(S)) = k/gcd(n_e, T(S)).
- Part (a) for S makes w_e coprime to T(S), so gcd(n_e, T(S)) = gcd(6, T(S)) = 6.
- W_S ≤ Φ_j gives the set inclusion Φ_eW_S ⊆ Φ_eΦ_j, which has measure x_ej/6. Neither product is assumed to be a subgroup. Equal cardinalities therefore mean equal sets.
- k ≤ 4 has prime factors only in {2,3}, so no new odd prime enters and the prime-to-30 part stays w_e∏w_j.
- v2 lcm(n_e, T(S)) = v2 T(S), because v2 n_e = 1 ≤ v2 T(S).
- If v2 k > v2 m then k ≥ 2m > m. No divisibility k | m is assumed. ✓

**P2 and P4 (triangles and apex measure).**
- lcm(n_a, n_b, n_c) = 6w_aw_bw_c, with v2 = 1.
- 6w_aw_bx_ab divides 6w_aw_bw_cτ, and w_c is odd, so x_ab divides τ.
- μ(Φ_b(Φ_a∩Φ_c)) = τ/(6x_ac). This set lies in X^b_a ∩ X^b_c, so τ ≤ x_ac·min(x_ba, x_bc). Minimising over apexes gives x1x2.
- I rechecked the table entry by entry. Deep ⇔ τ ∈ {8,16}, and δ = 5 occurs only for (4,4,4) with τ = 16.
- For x = α*, everything is computed in the actual U*_j, where the index identity holds by the definition of α*. ✓

**EQ.**
- q = x' holds by INV (b) applied to the x-configuration, whose α*-matrix is x' (double inversion is the identity).
- One-tight case:
  - D_b ⊆ Y and μ(D_b) = 2/6 = μ(Y), so D_b = Y.
  - D_a ⊆ Y = D_b. D_a is non-empty and left Φ_v-invariant, so it contains a genuine right coset Φ_v y lying in D_a ∩ D_b.
  - (V3) then needs gcd(d_a, d_b) ≥ 2, but d_a = w_a and d_b = 2w_b are coprime.
- Both-tight case: CI's full hypothesis list holds, including its own entry x_(d i*) = 1 for both families in G.
- I also re-traced CI steps 2–5 in G, including h_d ≥ 1; they are consistent. ✓

**BUD.**
- E3-C2 for x' requires x_(d i*) = 1 (orientation at `K62-E3-v1.md:105`). This holds for both x in G.
- n_1(x') ≥ u(x).
- n_4(x) + n_4(x') ≤ 10.
- Together these give n_4(x) ≤ 8 − 2u(x). ✓

**DEG.**
- Degree ≥ 1: R4 on the x-row, through RC-O with x'_(d i*) = 1.
- Degree ≤ 3: R4 on the x'-row, which needs x_(d i*) = 1.
- No K4 and no bowtie: B3.
- The CD13 certificate has y_(i*) = 0, so 5-on-d, 5-on-i* and f* ≥ 2 are all covered. RC-i*, C2 at i*, and f* = 1 are not used. ✓

**T16.**
- τ = 16 = 4·4 gives the apex equality at every apex.
- EQ at two apexes makes all three edges non-tight, so u ≥ 3 and n_4 ≤ 2 < 3. ✓

**ONE.**
- τ = 8 = 4·x_ab gives the equality at the apex opposite the 2-edge.
- Each triple R_i is the set of endpoints of its 4-edge pair E_i, so E_1 ≠ E_2 and |E_1 ∪ E_2| ≥ 3.
- Then n_4 ≤ 2 < 3. ✓

**TRI.**
- Since 3 + 3 > 5, two triangles meet; with no bowtie they share an edge pq.
- A third triangle either contains pq, giving p degree 4, or is forced to {q,r,s}, giving a K4. ✓

**FB.**
- (i) T16 gives δ(R_e) ≤ 4. So δ(Q) ≥ 5 forces v2 k_e ≥ 1 and m_e ≥ 2 for every e, hence no 1-pair.
- (ii) No K4, so N is non-empty.
- (iii) For v ∈ I, m_v = 2, so v2 k_v ≤ 1 and δ(R_v) ≥ 4. Then τ(R_v) = 8, and the 2-pairs of R_v are exactly the N-edges avoiding v.
- (iv) By ONE, at most one v ∈ I has an N-edge avoiding it. If |I| ≥ 3, two vertices lie on every N-edge, so |N| = 1 and |I| = 2, a contradiction. This covers every N-shape with |N| ≥ 2: adjacent, disjoint, path, star, triangle.
- (v) Then k_b = 2, so μ(Φ_bW_(R_b)) = 2/6. Since W_(R_b) ≤ Φ_a ∩ Φ_j, τ({a,b,j})/24 ≥ 2/6, so τ = 8 for j = c and j = q. That gives two (2,4,4) triples with τ = 8, contradicting ONE.
- All products are oriented Φ_b·(·), matching P4. ✓

**DEEP.**
- Both orientations of DG apply in G.
- DG's four-subset hypothesis comes from FB, and FB uses no DG input, so there is no circularity.
- G6's single-triple alternative has capped depth exactly 5, which means raw depth ≥ 5 and (4,4,4) with τ = 16. T16 excludes this, including when e_d = 4. ✓

**GE.**
- Let A be the number of deep (4,4,4) triples and B the number of deep (2,4,4) triples. Then A + B ≥ 2, A ≤ t(H_x) ≤ 2 by TRI, and B ≤ 1 by ONE.
- If t ≤ 1, then t = 1, B = 1 and n_4 ≤ 4. Minimum degree forces H_x = triangle + sf. Every adjacent pair of 4-edges then lies in the triangle, so B = 0, a contradiction.
- So t = 2 and H_x contains a diamond, for both families.
- The complement of a diamond in K₅ is {ab, ae, be, ce, qe}, whose only triangle is {a,b,e}. So H_α* cannot contain a diamond, which contradicts Step 1 for α*.
- Transfer to arbitrary groups: R0 preserves indices and disjointness, and G is defined by the index tuple. ✓

**OM.**
- E3 gives e_d ≥ 4 and e* = 2, and d has no 3-part.
- With no O-marker, the configuration lies in G, which GE has shown empty.
- The scope is exactly the E3 K6.2* class over arbitrary groups. Lines `:190–191` are labelled navigation and assert nothing. ✓

## 4. Original-domain audit (separate from proof gaps)

| Import | Accepted scope | Use in GS | Status |
|---|---|---|---|
| R0, L0.1, L0.6 | general | product formula; transfer to arbitrary groups | in scope |
| INV (a)(b), E1, E6, E7 | any finite disjoint family | x-configuration; x + x' ≤ 6; q = x' | in scope |
| VFC (V1)–(V4) | GEN | EQ | in scope |
| E3 Lemma 1; E3 C2 (Z11) | K6.2*; family y with y'_(d i*) = 1 | (1,1) in G; BUD | in scope |
| Z11 (a) | proof sub-claim of C2 | P1 | true; provenance issue m1 |
| CI | unmarked v, the family's own entry equal to 1 | EQ both-tight branch | in scope |
| R4 (CD13), B1, B3, DT-C C2 | G only; RC-O orientation | DEG | in scope |
| DG (b) with G6 | each orientation; four-subset hypothesis | DEEP | in scope; hypothesis supplied by FB |
| DG-3, DG-4, DT-A table, B5 | as accepted | cross-reference only; re-derived in file | non-load-bearing (m5) |

Not used anywhere: RC-i*, C2 at i*, f* = 1, CAP-62/CAP(D), CI', M13, K7 material, HD-v1/v2, the HD erratum, GX-v1, and the IRC hint. FB (v) resembles the hint's single-2-edge branch, but every step is derived in the file.

**New-proof gaps: none found. Domain violations: none.**

## 5. Trust and still-open boundaries

**Trust.**
- This is written mathematics resting on the imports above.
- The only new direct Sun instance is Sun(2), in EQ. Sun(3) and Sun(4) enter through CI, R3/R4, E3 and DG.
- The computer-assisted Sun(5) and Sun(6) remain transitive imports, through the LFC/VFC package and the K6.2* class reduction.
- This is a single model review. It is not a Lean check, not a human referee review, not a novelty or priority assessment, and not a hash verification.

**FB, T16, ONE, EQ and DEEP are internal to G.** Their proofs depend on n_c = 6w_c holding at every O-vertex:
- in P3, for gcd = 6 and the prime-to-30 control;
- in EQ, for the coprime local indices;
- through CI, R4, B1 and B3, which are accepted only in G.

Because GE shows G is empty, FB says nothing about any configuration that survives. DG's e_d ≥ 5 four-subset alternative therefore remains open outside G.

**What this would discharge, if the parent accepts.** From the CAP-DT "Remaining open" list (`sun7-K62-CAP-DT-parent-verdict-v1.md:43`), and only inside G:
- the remaining G-patterns: f* ≥ 2, the 5-marker on d or i*, all exponents;
- the e_d ≥ 5 higher-depth alternative.

**Still open.**
- Every O-marked K6.2* configuration:
  - 3-marker t ∈ O, in orientations (1,1), (1,3) and (3,1). The last two are the M13 candidates, which are unreviewed and not imported.
  - 5-marker p ∈ O.
- Complete U62 coverage (not claimed, and not needed for OM).
- Full K6.2*, marked K7, marked K6.3, and the other reduction classes.
- Sun(7).

Nothing here approves full K6.2*, K7 or Sun(7).
