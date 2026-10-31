# v164-B review — PhysicsPPT44-2's entire current PPT 4x4 (P44) union

Reviewer: InfoGuessingRminus-2 (slot info-5). Author: PhysicsPPT44-2. Assignment: `v164-B` of `institute/runs/three-area-2026-10-23-96h/peer-review-wave-eighteen-v164.json`.

Actual clocks (verbatim `/bin/date` outputs):
- opaque stage-1 ACK: `Mon Oct 26 18:03:27 PDT 2026`;
- Main's explicit full-body release: received 2026-10-27T04:44:13-07:00;
- body checkpoints: 112 (05:01:01), 113 (05:18:12), 114 (05:39:32), 115 (05:53:09), 116 (06:14:38), 117 (06:25:48);
- this file was drafted after `Tue Oct 27 06:27:08 PDT 2026`. The pin clock is recorded in the RETURN message and in the post-return checkpoint, not here.

Status of this document: an exact WRITTEN review only. It is not formal or kernel verification, an executable or triple check, human, configured-family or cross-vendor review, novelty clearance, parent adoption or a round closeout. **P44 remains UNMET.**

---

## 0. Exposure, reciprocity and independence (stated before any verdict)

1. **Reciprocity.** The author is currently the LIVE v162-B reviewer of my own R-minus union. This review is therefore reciprocal and not blind. I have not read or looked up any v162 material, coauditor output or proof, and none of it is a premise here.
2. **Prior contact with this author's PPT bodies.** I have no recorded earlier PPT body-review assignment. I have seen PPT-related process findings only as they appeared in round briefings and in the v164 packet's own process sources (S1–S188). My other recent specific body exposures (v155-A Sun, v138-B Shor, v136-A RQLS, v130-B AME, v120-D) are disclosed in my ACK `peer-review-v164-B-opaque-ack-v1.json` (sha256 `416d48a0…`). None concerns PPT.
3. **Read-only material consulted beyond the 20 literal packet parts, after release:**
   - (a) For Parts 24–40, I re-read the author's 17 source files directly under `physics/evidence/three-area-20261023-96h/parallel-18/ppt-schmidt44/`. A `shasum -a 256` check shows all 17 are byte-identical to the packet pins (S229–S245). This is metadata only.
   - (b) `ppt-coherent-rectangle-SN2-parent-v1.md` and `ppt-entire-current-C1-C8-parent-v1.md`, checked by `shasum` and `wc` only, to test ADDENDUM-1. Results: 26 LF/5003 B, sha `992874f1…6682`; and 48 LF, sha `cdc08c42…9185`.
   - (c) For finding F-X1111, the parent records `ame-twoF-ppt-small-phase-parent-v1.md` and `ppt-entire-Parts9-23-rank-floor-and-chart-union-parent-v1.md`, plus the round README. I consulted the Parts 9–23 disposition only AFTER my own reconstruction of Parts 9–23 was complete. I then saw its precision items, including items #1, #2 and #8–#11. MINOR-1 below (Part12 L4.1, matching parent item #2) was already in my working notes from my Part12 reconstruction, before I read that disposition. MINOR-2 (Part12 L4.2, matching parent item #1) I checked freshly only AFTER seeing parent item #1; it is a concurrence, not an independent discovery. No verdict is transferred from any parent, earlier review or earlier gate.
4. **Context compaction.** My in-context copies of earlier reads were compacted twice. Every verdict below rests on my persisted working notes, `peer-review-v164-B-working-notes-v1.md`, and on disclosed targeted re-reads. The re-reads were of literal packet bytes or of the byte-identical author files. No unread byte is presented as read.
5. **Quarantined material.** No post-40, post-143, post-43 or post-57 unpublished continuation, no held 163/164 unliteral method and no withdrawn guide or control was used. Historical chosen states and limits were read only at their literal old scope.
6. **No clean-history claim.** I make no claim of clean private cognition, runtime, cadence or blind status.

## 1. Coverage

- **Envelope and metadata, read complete:** packets 178, PPT204 finding and 180; the release file; manifest `peer-review-wave-eighteen-v164.json` (own entry, including `post_ack_entire_scope`, and the 258-entry source-pin index); receipt `peer-review-wave-eighteen-v164-packet-receipt-v1.json`.
- **All 20 literal parts, every LF through the ending:**

| Packet part | Lines | Contents |
|---|---|---|
| part1 | 1–916 | S1–S26 |
| part2 | 1–1002 | S27–S65 |
| part3 | 1–827 | S66–S89 |
| part4 | 1–883 | S90–S117 |
| part5 | 1–733 | S118–S145 |
| part6 | 1–808 | S146–S169 |
| part7 | 1–810 | S170–S190 |
| part8 | 1–1288 | S191–S199 |
| part9 | 1–750 | S200–S205 |
| part10 | 1–1130 | S206 Dv3, S207 start |
| part11 | 1–1167 | S207–S212 |
| part12 | 1–757 | S213–S228 |
| part13 | 1–845 | S229–S234 |
| part14 | 1–808 | S235–S240 |
| part15 | 1–831 | S241–S245 |
| part16 | 1–1367 | S246/S247, legacy v2/v1 |
| part17 | 1–362 | S248–S255 |
| part18–part20 | entire | S256–S258 preflight index, 1–3484 |

- **Targeted re-reads after compaction**, with fresh reconstruction: S206 C1–C8; S209–S215; S195 Q5–Q8 and Remark 2; S194 B4; S197 G4; S198 closing; and Parts 24–40 from the identical source bytes.

**Method.** All algebra is done by hand in exact rationals, radicals and symbols. No interpreter, calculator, CAS, enumeration, table checker or solver was used. The only tool calls are `/bin/date`, `shasum`, `wc` and file reads. One stray metadata parse is disclosed in §9.

**Labels:**
- RECONSTRUCTED: I re-derived the statement and its proof, or every load-bearing identity in it.
- FRAME: read and consistent, but not re-derived entrywise.
- NOT_RECONSTRUCTED (NR): I could not complete or verify the step from the written text. For each NR item, the callers are named.

**Rubric:**
- FATAL: invalidates a main claim.
- MAJOR: a substantive false claim or a missing required proof.
- MINOR: local precision or exposition.

## 2. The original quantified problem

P44 asks for either of two things:
- an actual 4x4 PPT state with SN>=3 together with a separator that is nonnegative on EVERY complex Schmidt-rank-<=2 vector and strictly negative on that state (a negative PPT pair); or
- an unrestricted theorem that every 4x4 PPT state has SN<=2.

**No part of the union supplies either.**

The union does contain:
- **Family-restricted SN<=2 domains:** C2–C5, C9, C10, C13–C17, C19, C21–C23, C28–C47.
- **Witness-class decomposability closures:** C10, C18, C25, C26.
- **Method barriers:** C7, C24, Part15 Q7, Part16, Part17.
- **Existence representations of the original problem:** Parts 31–33 and 35–40. Each is an exact iff, and its existence side remains open.

Throughout, the author consistently refuses to promote any of these to an answer. I found no place where a normal-form iff is used as existence, a family restriction is promoted to the original problem, or an SN conclusion is drawn from a failed sufficient test. **Original-problem verdict: UNMET, correctly stated by the author in every part.**

## 3. Per-part verdicts (all 40 primary parts)

Counts are FATAL/MAJOR/MINOR of fresh findings for each part.

| Part | Source | Statements | Mathematics | Dependency, application and trust | F/M/m |
|---|---|---|---|---|---|
| 1 (Dv3 base) | S206 | C1–C10 | RECONSTRUCTED: all ten | C9 skew normal form re-proved inline. C10 rests on twirl and DEC closedness. LF449/LF711 carry the x1111 "accepted 37-term proof" anchor (§5, F-X1111). | 0/0/0 |
| 2 | S207 | C11–C14 | RECONSTRUCTED | C12 AT_MOST overlay concurred (pre-existing record). C13 exposition minor. | 0/0/1 |
| 3 | S208 | C15–C17 | RECONSTRUCTED | self-contained | 0/0/0 |
| 4 | S209 | C18 | RECONSTRUCTED | self-contained; quantifier distinct from C9 | 0/0/0 |
| 5 | S210 | C19, C21, C22 | RECONSTRUCTED, including the X5.2 PT Gram checked blockwise and the 22-phase X6.2 | implicit-function theorem and closed-cone separation (ordinary) | 0/0/0 |
| 6 | S211 | C23, C24 | RECONSTRUCTED, including involution Y4.1 | uses Part5 X7; the involution is a premise of Parts 10, 14, 19–22 (satisfied) | 0/0/0 |
| 7 | S212 | C25 | RECONSTRUCTED | DEC=PPT* duality | 0/0/0 |
| 8 | S213 | C26, C27 | RECONSTRUCTED; AA8 finite completeness only at the named import QD | QD (quantum de Finetti, standard) is NR by the reviewer; callers are AA8, AA10 and ADDENDUM-2 §4 | 0/0/0 |
| 9 | S189 | Pauli/Bell two-positive SN2 | RECONSTRUCTED | elementary; the Müller-Hermes screen is not a premise | 0/0/0 |
| 10 | S190 | C29 (H1–H6) | RECONSTRUCTED | H5 uses Part6 Y4.1 (verified). H6 LF127 status sentence: see F-X1111. | 0/1*/0 |
| 11 | S191 | Theorems D, D′; V3 map | RECONSTRUCTED | V3 open-core listing includes literal x1111: see F-X1111 | 0/*/0 |
| 12 | S192 | C31 (rank floor) | RECONSTRUCTED at imports I1–I5 | I1–I4 NR by reviewer (named literature imports; papers not re-read); I5 re-derived | 0/0/2 |
| 13 | S193 | C32 (x1111 SN=2) | RECONSTRUCTED | self-contained. X0 status/novelty wording: see F-X1111. | 0/*/0 |
| 14 | S194 | C33.1–C33.4 | RECONSTRUCTED, including the s=2,3,5 tables | uses the Part6 involution | 0/0/0 |
| 15 | S195 | C34.1–C34.4 | Lemma L, Q3–Q6, Q7(a)–(d) and the Q7(e) block: RECONSTRUCTED. Q7(e) forced-sum premise and Q7(f): NR. Remark 2 general frame: NR. | Q8 inherits the Q7(e)/(f) gaps | 0/0/1 |
| 15-ADD | S196 | interpolation | RECONSTRUCTED: A1 Vandermonde; A2 source-typo correction | minor g_i identities vs source (11): NR (nonpremise) | 0/0/0 |
| 16 | S197 | C35 | RECONSTRUCTED; G4 nine-vector independence verified by the reviewer | author omitted the G4 independence proof (expository) | 0/0/0 |
| 17 | S198 | range-criterion designs | RECONSTRUCTED at KCKL Lemma 5 (re-derived) | the closing "direct check" is redundant (NR) | 0/0/0 |
| 18 | S199 | C36 | RECONSTRUCTED. E3.1 entries: NR. | E3.1 is a within-family sharpness remark, nonpremise | 0/0/0 |
| 19 | S200 | C37, C37′, C38 | RECONSTRUCTED | Part15 Lemma L/Q6; Part10 H5; Part6 involution; Horodecki 2x2 | 0/0/0 |
| 20 | S201 | C39–C41 | RECONSTRUCTED | Part10 H1, Part15 Q6, involution | 0/0/0 |
| 21 | S202 | C42, C43 | RECONSTRUCTED | Part20, Part15 Q6, involution | 0/0/0 |
| 22 | S203 | C44–C46 | RECONSTRUCTED | Part20/21, involution | 0/0/0 |
| 20–22-ADD | S204 | entrywise table | 7 entries re-derived, all match. Remaining rows: NR (consistency table, nonpremise). | — | 0/0/0 |
| 23 | S205 | C47 | RECONSTRUCTED | Part10 H1, Part15 Q6, SN2 closedness | 0/0/0 |
| 24 | S245 | Z1–Z4 | RECONSTRUCTED | elementary | 0/0/0 |
| 25 | S244 | S1–S6 | RECONSTRUCTED | Part24; KG/MOM positive PRIOR | 0/0/0 |
| 26 | S243 | T1–T5 | RECONSTRUCTED | Part25; KG Thm 2 PRIOR | 0/0/0 |
| 27 | S242 | U1–U7 | RECONSTRUCTED | Part24 | 0/0/0 |
| 28 | S241 | V1–V7 | RECONSTRUCTED | Part24/27 | 0/0/0 |
| 29 | S240 | W1–W5 | RECONSTRUCTED | Part24 | 0/0/0 |
| 30 | S239 | X1–X6 | RECONSTRUCTED | Part29 hypothesis | 0/0/0 |
| 31 | S238 | Y1–Y5 | RECONSTRUCTED | Parts 24, 27, 29, 30 (all reconstructed here) | 0/0/0 |
| 32 | S237 | R1–R6 | RECONSTRUCTED | Part31 | 0/0/0 |
| 33 | S236 | S1–S5 | RECONSTRUCTED at I-RP and I-RCF | the I-RP/I-RCF background theorems are NR (standard) | 0/0/0 |
| 34 | S235 | T1–T9 | RECONSTRUCTED | unconditional elementary | 0/0/0 |
| 35 | S234 | U1–U7 | RECONSTRUCTED at I-RP and I-RCF | Parts 33, 34 | 0/0/0 |
| 36 | S233 | V1–V6 | RECONSTRUCTED at I-RP and I-RCF | independent of Parts 24–32 (correctly claimed) | 0/0/0 |
| 37 | S232 | W1–W6 | RECONSTRUCTED at I-POW5 | Powers Thm 5 is NR by the reviewer (positive PRIOR) | 0/0/0 |
| 38 | S231 | B1–B8 | RECONSTRUCTED; B8 at I-POW5 | Part36 V1–V3, Part37 | 0/0/0 |
| 39 | S230 | Z1–Z7 | RECONSTRUCTED; Z7 is optional at statement level with an RCF/QE trust cut | elementary | 0/0/0 |
| 40 | S229 | E1–E6 | RECONSTRUCTED | Part39 | 0/0/0 |

\* The single MAJOR, F-X1111, is one documentary/provenance finding whose text is spread over Dv3 LF449/LF711, Part10 H6, Part11 V3 and Part13 X0. It is counted once.

**Whole-branch verdicts.** Each of the 40 primary parts is supported as ordinary WRITTEN mathematics at its stated scope, conditional where noted on the named imports in §6. None is an original P44 answer.

## 4. Statement-level reconstruction record

Each item lists the load-bearing checks the reviewer performed.

### Base Dv3 (S206; 723 LF)

- **C1.**
  - Q0 = E0BE0* and Q1 = E1BE1*, with B_rk = (1+i^{r−k})/4.
  - Product tests: d >= 1/2 for differences 0 and 1; d >= 0 for differences 2 and 3.
  - Inverse-Gram iff by whitening. Conversely, z_j = A_j^{-1}V_j v gives g−g² < 0.
  - The (Z ⊗ conj Z) twirl is lossless; S_τ(r,k) = R_{r+k−τ}(r,k).
  - (2.6): the diagonal of A_k is 0 at k, z at j and 1±i at r/l, and the r/l determinant is 0, so rank <= 2.
  - Overlaps have modulus |z+2|/2, giving (2.7). The q=1 orientation (f1,g1) = (β_{1,j+2}, β_{1j}) is correct. Taking infima gives (2.8).
- **C2.**
  - PT is block diagonal in τ = Alice+Bob mod 4, with block_τ(r,k) = (R_{r+k−τ})_{rk}.
  - τ0 Schur residual is (s/2)[[1,i],[−i,1]], rank 1.
  - τ2 residual is 0.
  - In τ1 and τ3 the 2x2 determinants are (1±s)²/8 − (1±s)²/8 = 0.
  - PT rank is 9; N agrees with (3.1). At s=1/2, t=1: N = 83/12, and all entries of K0–K3 check, with traces 96+96+80+60 = 332.
- **C3.**
  - All four row identities (4.2) hold.
  - Rank is exactly 2 (minor 2(1+i)A_h²).
  - Seventh-root residues are 0,1,2,3,6,5.
  - Group sums: q0 gives R0 (A_+²+A_−² = 1/4, difference s/4); q1 gives tB.
  - |b_h|², |c_h|² (using 2(1−1/√2)² = 3−2√2 = κ), |e_h|² and |f_h|² all check, as does the placement of the shifted M_− entries.
  - (4.5) r1 and r3 algebra checks.
  - Rectangle bounds: 25/192 < 5/32, 1/144 and 47/288 give r1 > 97/288; 125/288 + 135/288 = 65/72 gives r3 > 7/72; κ < 1/5 since 8 > 196/25.
- **C4.**
  - At s=t=2/3: y1 = 2/5 and y3 = 2/3, so 4y1y3 = 16/15.
  - (5.1): rank via parity blocks.
  - (5.2): h_k(k) = 0, and Σ_k h_k(j)conj h_k(l) = tB.
  - n3_j = (t/4)√(z_j/z_{j+2}), and √(z_j z_{j+2}) = (1−s²)/(4t). Rays total 8+16 = 24.
  - The region is disjoint from the rectangle because 81/100 > 3/4.
- **C5.**
  - Both (6.2) identities hold.
  - Mixture parameter p = r(L−1)/(L−r).
  - Fifth-root characters; load bounds.
- **C6.**
  - kI−2T whitening: q/(k+2) + (k−q)/k <= 1.
  - Compression formulas are re-derived: (A*⊗B*)Ω6 = vec(A* conj B), and (A*⊗B*J)F6(A⊗J*B) = (N*⊗N)F4.
- **C7A.**
  - x = Tr PQ; y = Tr PΘQ; z = −Tr[QPΘ(QP)].
  - C^T = −ΘPΘQJ; ‖C+C^T‖² = 2x+2z.
  - The split identity holds; ‖Q−ΘP‖² = 8−2y; the triangle inequality gives z+x <= 4(4−y); hence a(4−a) + 2b(2−b).
  - Matched control:
    - I+T_N has kernel Ω_01; T_N^Γ = P(vec N*); PT rank is 10+1.
    - W_N = (W_{N+}+W_{N−})/2 + 2T_{N2}, and both W_{N±} are PSD.
- **C7B.**
  - Full R3^Γ and R_x^Γ Gram decompositions are re-derived term by term. The {02,11,20} block [[3,1,1],[1,1,−1],[1,−1,3]] equals P(1,1,−1) + 2P(1,0,1).
  - ⟨f,Wf⟩ + ⟨g,Wg⟩ >= 1 by contraction bounds.
- **C8.** (11.1) is re-derived term by term. The OPEN-gate statement is honest.
- **C9.**
  - T_A flip identity; skew K; the 36-Pauli average; the symmetric-projector remainder.
  - The inline Youla-type skew normal form proof is correct.
- **C10.**
  - B↔C PT exchange; phase law Ew = 0, Ew² = m.
  - One-zero peel.
  - Three-matching identity 4|1+tw|² − (1+t)²|1+w|² = 2(t−1)²(1−Re w).
  - Extremal dimension count r² >= 9 > 7; capacities; twirl with DEC closedness.

### Parts 2–8

- **Part2 (C11–C14).**
  - U2 PT certificate (Schur [[r−1,2],[2,s−1]]); U3.2.
  - C11: characters mod 3, 4 and 11.
  - C12: 277-trial loads and remainders exact (5/2, 5/2, 0, 199/24, 12, 2/5).
  - C13: whitening, contribution 4(1−t)E/(3(2−t)).
  - C14: AM-GM y + 1/(2y) >= √2.
- **Part3 (C16, C17).** Inverse series; wedge-2 minors; e2 superadditivity; (V2.9). C17 endpoint completion and ray split.
- **Part4 (C18).**
  - (A*⊗J)F(A⊗J*) restricted to C4⊗V is SWAP.
  - K_ij = ⟨v_j, conj a_i⟩ is skew (index check).
  - Antilinear pairing gives z with Schmidt squares u, u, v, v.
  - P0 Schur complement is exactly zero. R^Γ >= 0 via the P(z)^Γ spectrum and the max(u,v) bound. The q=4 branch is PSD. The F = AL factorization gives Q′ = (L*⊗G^T)Q0(L⊗conj G).
- **Part5.**
  - C19:
    - All eight line families hold.
    - X0 and Y0 chart pivots and leading terms check, and both alternative Schur expressions give (X3.2) and (X3.4).
    - Twelve undetermined pairs; phase averaging; plane/completion elimination; closed-cone interior.
  - C21:
    - All nine F-images (det F = 1).
    - Norms total 64; all coefficient matrices are trace-zero.
    - (X5.2) holds blockwise. For all four diagonal and six off-diagonal Alice blocks, Σ w m_k m_i^T equals Σ w n_i n_k^T.
    - Ranks 9 and 10 by unique supports.
    - (X6.1): row identities with τη = 1 + iε√2; the ε-means vanish; |1+τ|² = 1/2, |τη−1|² = 2, |1+2τ|² = 3, |η/τ|² = 4/3; residual 2Pd + Pe + Pf/2 + 5Pj/3 + 3Ph; traces 125/6 + 97/6 = 37.
  - C22:
    - Two-point law moments.
    - Retained d/f, d/g and f/g coherences.
    - Alice support {0,3}.
    - The example gives 401/528.
- **Part6.**
  - C23: ball with T = Z/3 (2(3−V−4Z/3) − 3(2−V−Z) = V+Z/3); z=0 family; chart cases.
  - V5^T k = (k2, k1, −k0, −k4, −k3).
  - C24: N_x has rank 2; lower-rank factorization; the barrier holds.
- **Part7 (C25).** V_N isometry; Alice-side PT; Bell contraction 1/(kN); classical mixture PPT on all cuts; i≠j terms vanish.
- **Part8.**
  - C26:
    - Haar buffer range Sym^m ⊗ Sym^n, from a polynomial identity.
    - Within-side and cross legs after Γ_S.
    - P_m is real, so Γ_S keeps the support.
    - The square completes, since ‖C‖² <= bMγ.
    - Expectations 0, Tr(Wρ)/(kN) and TrW/(k²d²).
  - C27:
    - p = 1/(kS²) >= 1/k².
    - Threshold optimality via the nuclear-norm bound.
    - Dual (AA8.1) with Slater; AA9: p >= 1/k² iff ε(k/N−1) >= 1.

### Parts 9–23

Fully reconstructed; all identities, tables, minors and Schur values were recomputed exactly.
- Part9: BB1–BB6.
- Part10: H1–H6, including Theorem C constants and the restricted-form exclusion.
- Part11: Theorems D and D′.
- Part12: Lemma P and Steps 1–3.
- Part13:
  - γ² = −5i/12; both determinant branches.
  - M3 and M−M3 entries; Schur 5/3 − 16/39 = 49/39.
  - Lower bound via Alice {0,1,2}.
- Part14: the s = 2, 3, 5 tables (all γ², diagonals and Schur values); B3; B4.
- Part15:
  - Lemma L; Q3.
  - Q4: kernel (1,1,−1,0); minors 11, 109, 1071 and 252.
  - Q5: polynomial minors.
  - Q6.
  - Q7(a): |z| >= 1/(6√(1+|w|²)), for both Alice-1 and Bob-1.
  - Q7(b)–(d): the reviewer derived every forced family by hand:
    - Alice-2: η = 0, Row1 = χ(1,σ,σ²,0), Alice amplitudes (σ,1,σ²v), and (12,30) = conj(v)Σw|χ|²|σ|⁴.
    - Bob-2: κ = η = 0, Alice (−1/r, 1, r, (v/z)r²), Bob (−r, 1). The residual (20,31) entry becomes zero-diagonal row (21,30) after Γ.
    - Alice-0: z=0 forces Bob |2⟩; for z≠0 the family (|1⟩ + r|2⟩ + (r²v/z)|3⟩) ⊗ (−r², r, 1, 0) gives (10,32) = −conj(v/z)Σw|r|⁴.
    - Bob-3: the same −S versus +S contradiction on Bob {0,1,2}.
  - Q7(e): block [[2+3W, 0, 3w̄], [0, 2V, 3v̄w], [3w, 3vw̄, 3+3W−V]] with det V(12−6W−4V−9W²−6VW), which is −13 at V=W=1.
- Part16: G2–G4, including the identity 1−κ = (tκ−εe′)(e′−κ).
- Part17: K1–K3, F1, F2.
- Part18: C36 and Res^Γ; s = 5/3 − v² − 2w².
- Part19: C37, C37′ and C38, including E|r|⁴ >= 1.
- Part20: B1–B6, including 7275 < 7384 and 880800 < 892255.
- Part21: C42 (711/1672 < 1/2), C43.
- Part22: T1, C44–C46, including 632016 > 452160.
- Part23: C47, Laurent series.

### Parts 24–40

The 17 source files are identical to the packet pins.
- Part24: product-zero kernel; regular-zero reduction with genericity; DEC transport (A⊗B)*Q^Γ(A⊗B) = [(A⊗conj B)*Q(A⊗conj B)]^Γ; doubled Hessian LMI.
- Part25: CP peel W = U + χ̃; Lemma S2; (COMPLETE); C_F rank <= 2; negative index <= 2; ZERO/NORMAL.
- Part26: FACTOR; CHARGE TρT* = H + Cσ⁺C*; GRAPH-SCHUR; BORDER; T5 trace-zero commutator.
- Part27: Takagi trace lemma; R_Δ has each singular value four times; MOMENT (I+|Ω⟩⟨Ω|)/6; AM-GM gives √6; global K2 positivity of EXT via α[L² − (τ−m)²]; P + Q^Γ; SVD transport.
- Part28: equality chain; doubled-matrix kernel vectors give S = √(R*R); D_N = 0; Δ-perp spanned by products; v = Ω/2; H_AA = α(I − |Ω⟩⟨Ω|/2); w = 0; not DEC-interior.
- Part29: pencil zeros; unbounded affine argument; CNB spans M2.
- Part30: O = K conj(U)Σ^{−1/2}; elementary Skolem–Noether; LOCAL action; similarity invariants.
- Part31: E_D perturbation; det polynomial; bottom filter; top filter.
- Part32: Πx0 = 0; ROBUST; rational slice; dual separation; strict LMI.
- Part33: X = UV*; h = 1 + t²f; real Nullstellensatz over Q (at I-RP and I-RCF); integer form.
- Part34: leading forms; bounded-polynomial invariance; complete mixed-quadratic classification (c = 0 via the imaginary unipotent); polarization; u-only/t-only multiplier exclusions.
- Part35: 16 minors as 32 real cubics; multi-generator Nullstellensatz; Cauchy–Binet pullback; aggregate rank term nonzero.
- Part36: C2 closed; εI gap; τI regularization; density; Tr(Zρ) < 0.
- Part37: compact K with 66 signed generators; preordering-to-ideal reduction; charge projection T(A²) = A_0² + 2Σ|A_k|²; degree-six bound; B(0) > 0.
- Part38: coercivity (TrA >= 4; eigenvalue floor T^{−3}); first variation gives balanced marginals; filter transport; Ψ(H²) − Ψ(H)² = V*D(I−VV*)DV >= 0 gives ‖W‖_F <= 1; δ <= 1/16.
- Part39: Haar mean; I in the interior of C2; t*; Carathéodory; converse.
- Part40: product-zero kernel; local normal form; graph chart; complex Hessian; ker H_top = C·I2.

## 5. Findings

### F-X1111 — MAJOR (documentary/provenance status claim; no theorem invalidated)

**What the union's own base records.** Dv3 S206 LF449 states: "Old x1111 retirement remains only at its accepted 37-term proof, not old21 repair." LF711 states: "Old x1111 is retired only at its accepted 37-term proof, not a repaired old21 claim." The legacy bases agree: v1 at LF579 and LF631, v2 at LF505 and LF693.

**What the parent records.** `ame-twoF-ppt-small-phase-parent-v1.md` (observed 2026-10-25T04:59:16; disposition sha `228b2b87…`) records WRITTEN_SUPPORTED SN(ρ) = 2 for the literal x = (1,1,1,1) state R/49. It does so through the 207-LF small-phase ADDENDUM-1 37-term identity, with old21 no longer a premise. So a written proof was accepted before Dv3 (pre-write 16:51 Oct 25) and before Part10 (22:04 Oct 25).

**What the later parts say instead:**
- Part10 H6 (S190 LF127): "Its Schmidt number therefore remains UNKNOWN."
- Part11 V3 places the literal input in the open core.
- Part13 X0 (S193 LF7) labels C32 a "NEW claim". LF10–12 name only the old 04:13 packet and old21. LF14 asserts: "That was accurate at their writing: no admissible complete proof existed."

These status, novelty and provenance statements contradict both the union's own base and the parent-supported record. The mathematics of C32 is correct; I reconstructed it independently. It is a valid alternative M-decomposition proof of an already-supported result, not a first proof.

**Propagation.** The parent's own Parts 9–23 disposition (observed 2026-10-26T07:44:31) repeats the "later state proof supersedes UNKNOWN" framing at LF53 and LF95, as does the round README at LF83. This is disclosed as context; it is the parent's record, not the author's.

**Repair.** An additive erratum, with no edit to any pinned file:
- withdraw "remains UNKNOWN" (Part10 H6) and "no admissible complete proof existed" (Part13 X0 LF14);
- relabel C32 as an independent alternative proof of the already-supported x1111 SN=2 result;
- carry zero new-result credit for the status change.

Part11's open-core description then excludes x1111 at the earlier date, as Part13 already concedes going forward.

### MINOR-1 — Part12 L4.1 statement overreach (coincides with parent item #2)

The text "Each of its extreme PPT components either has (4,4) rank>=6 or 3x4 rank>=6" is false as written. Take ρ = (1−ε)σ + εP00 with σ SN3. It has an extreme product component, and for small ε it is still SN3 by closedness.

The correct statement: in any extreme decomposition, at least one component has SN3, and every SN3 extreme component has those rank properties. C31 itself is unaffected.

### MINOR-2 — Part12 L4.2 "Every R_x has rank nine" false on a slice (concurrence with parent item #1; fresh-checked after reading it)

At u = v = z = 0, d_x = 02 + w·32 = (1/w)h_x + w·g, so rank R_x = 8. The same holds at x = 0, where h_x = 0. Restrict the sentence to the generic case.

### MINOR-3 — Part2 C13 exposition

The Bob filter is stated as mapping into V⊥. A general filter reduces to this case because the remainder after P_peel is supported on C3 ⊗ V⊥, but that one-line reduction is not written.

### MINOR-4 — Part15 Q7(e) premise and Q7(f) proof completeness (method barriers only)

Q7(e) asserts, off the z=0 slice and without derivation, that every Alice-1-carrying product "must have zero h-coefficient and |r|=1, and the moments m1..m4 must vanish". The PT block and determinant that follow are correct, and I reconstructed them.

Q7(f), the adapted Bob peel, is a sketch. It uses symbols (ρ, s, p, q, c2) that are undefined at that point and depends on the Remark 2 general frame. I could not reconstruct it, so it is NR.

Consequence: Q8's "not the adapted peel" and the off-slice Bob-0 part of "no coordinate peel certifies the far ray" (involution frame) inherit these gaps. No SN statement or later premise depends on them. In the original frame, Part16 G2–G4 (reconstructed) prove the Bob-0, Bob-1 and Alice-1 failures at (s,s,s,s) directly. Together with Q7(b)–(d) (reconstructed), the eight-coordinate-peel failure for s > 6(1+√2) stands without Q7(e)/(f).

### Expository notes (not findings)

- Exact-decimal glosses of rationals: 9.5/15.5/17.5 (Part15); "about 14.49" (Part16); "3.5Z" (Part20); "~0.894" (Part21); "~1/(1+p_z)" (Part22). None is used as proof.
- Part16 G4 omits the nine-vector independence proof. The reviewer verified it by unique-coordinate elimination.
- Powers' rational SOS weights are positive rationals. Every positive rational is a sum of four rational squares, so Part37's "SOS of Q[x] polynomials" is correct as stated.

### Concurrences with pre-existing recorded items (not new counts)

These remain mandatory, unchanged and still standing:
- C12 AT_MOST zero-mixture allocation overlay `0c33a599…`;
- the historical 26-not-27 metadata item, cured additively by ADDENDUM-1 and confirmed by my `wc`/`shasum`;
- C27 novelty withdrawal and zero new-method credit (ADDENDUM-2);
- the three historical pin-label corrections (178/PPT204);
- the ELEVEN Parts 9–23 precision qualifiers;
- the C19–C27 FOUR minors;
- old21 NOT_RECONSTRUCTED;
- N4 UNKNOWN, with the historical child exit unestablished;
- aux214 STOP;
- A10/A11 with three GB and no global native-free certificate.

The author's earlier process findings also all remain, unchanged:
- 8797d022 and 3c1edecd, and the v140 reciprocity finding;
- continuation after STOP;
- the 149 and older cadences;
- the v144 opaque guess;
- the THREE v156 current majors;
- the 164 unsupplied item;
- the 197/69/162 guides ZERO;
- the 473-versus-465 return record;
- the one-time 132 idle.

So does the parent's history: the 138 cadences, the 156 pre-ACK release and the 174 individual gates.

## 6. Named imports and NOT_RECONSTRUCTED items, with callers

- **Part12 I1–I4** (literature imports as quoted by the author, for the C31 rank-floor steps). NR by the reviewer; the papers were not re-read. Caller: Part12 C31. **I5:** re-derived by the reviewer.
- **Peres–Horodecki** (PPT iff separable on 2x2 and 2x3 systems). A classical import, used as standard and NR. Callers: Part12 Step 2; Part15 Q4/Q5/Q7 residual separability; the 2x2/2x3 residual steps of Parts 18–23.
- **I-RP and I-RCF** (real-prime/ordering theorem; Tarski transfer). NR (standard). Callers: Part33 S2/S3, Part35 U2/U3, Part36 V4/V5.
- **I-POW5** (Powers 2011, published Theorem 5 = preprint Theorem 4). NR by the reviewer; positive PRIOR with zero new-method credit. Callers: Part37 W2/W3, Part38 B8, Part39 Z7 (optional).
- **QD** (quantum de Finetti for Bose extensions). NR (standard). Callers: Part8 AA8, AA10; ADDENDUM-2 §4 bullet 3.
- **KG 2509.07086 Thm 2, Supp. A Thm 6, Supp. E; MOM 2104.14058v5 Prop. 3.1.** Positive PRIOR attributions for Part26 BORDER, the Part25 CP peel and all-plane criterion. The internal proofs in Parts 25/26 are complete without them; I reconstructed those proofs. The external papers are NR.
- **Part15 Remark 2** general-frame entries, and the open-neighbourhood sentence that rests on them. NR. Diagonal reductions were verified.
- **Part18 E3.1** F = f r² family entries. NR.
- **Part15 Q7(e)** forced-sum premise and **Q7(f)**. NR (MINOR-4); caller: Q8.
- **Part15 ADDENDUM-1 A2** source-(11) g_i identities; **S204** remaining table rows; **Part17** closing "direct check". NR (nonpremise consistency material).
- **Dossiers S248–S250.** Attribution and coverage records only. External sources are NR; they are premises only through I-POW5 (Part37) and through C31's I1–I5.

## 7. Watch-list checks required by the scope

| Check | Result |
|---|---|
| Projector-coordinate-only surrogate | Absent. Parts 33/35/37 quantify over all 32 real coordinates of an arbitrary complex X, explicitly not a density matrix. |
| CP nor coCP ⟹ indecomposable | Never inferred. Part26 T2 and Part27 U7 explicitly disclaim it. |
| Rational empty ⟹ physical empty | Only the valid direction is used: a physical counterexample gives a rational one through proved open conditions and density (Parts 32 R4/R5, 36 V3, 38 B5). |
| Strict versus weak gap | Kept apart. Part37 W2 requires strict slack δ < γ; Part33 handles the weak inequality through h = 1 + t²f; Part38 B1/B5 choose δ strictly below the gap. |
| Pointwise ⟹ uniform | Never claimed. Part28 V6/V7 and Part38 BOX state "no uniform lower bound". |
| Noncompact ⟹ Powers | Not done. Powers is applied only to the compact norm-1 rank<=2 set K (Part37 W1). |
| Quotient radical or SOS multiplier assumption | Absent. No primality or real-radical assumption (Part35 U2); no sign on b (Part33); Part34 uses only real squares. |
| Norm-1, all Re/Im rank minors, strict margin, equality ideal, preorder-to-Q-SOS, converse, closed dual cone, actual physical filter and triplet basis transform | Each is paid explicitly: Part37 W1/W2; Part36 V1 (C2 closed); Part38 B4 (filter); Part30 X3 (common SL2 realization of SO3(C)). |
| Normal-form iff used as existence | Never. Parts 31–40 state conditional existence equivalences only. |

## 8. Legacy bases and dossiers

- **Legacy v2 (S246, 708 LF) and v1 (S247, 646 LF):** read complete. Both are historical NONPREMISE, superseded by Dv3. No current part imports them. Spot checks of v2 C9 (12.6)–(12.10) agree with my Dv3 C9 reconstruction. Their x1111 sentences (v1 LF579/631; v2 LF505/693) are part of the F-X1111 evidence.
- **Dossiers S248 KG, S249 MOM, S250 Powers:** correct as positive-PRIOR attribution records at statement level, with zero new-method credit. The coverage claims are the author's (605/475/356 logical-reader extents); I did not re-read them.

## 9. Overall verdict and counts

**Fresh findings: FATAL 0; MAJOR 1 (F-X1111, documentary/provenance); MINOR 4.** Two of the MINORs (1 and 2) coincide with pre-existing parent items. Expository notes are not counted.

Every primary part is WRITTEN-supported at its stated scope, subject to the named imports and NR items in §6. The C32 mathematics stands; its status and novelty wording does not. The union contains no FATAL defect and no false theorem.

**P44 is UNMET.** The union proves many exact SN2 domains, decomposability closures, method barriers and existence representations. It supplies neither an actual PPT/SN>=3 negative pair nor an unrestricted all-state theorem, and it never claims to.

Disclosed deviation: once in this session I ran `python3 -c` (the interpreter path was not observed) for a one-line JSON key listing of the v164 manifest, a metadata read. No scientific content, computation or decision depended on it, and I then switched to the read tool's JSON query. It is disclosed as an administrative tool-choice deviation, with zero science involved.

## 10. Nonclaims and next step

There is no formal, kernel, executable, triple, human, configured-family, cross-vendor, novelty, SOTA, parent-adoption or publication acceptance. No pinned or shared file was edited. No external model, network publication, git operation, deletion, solver, interpreter calculation or new GO was used.

Next steps:
1. Pin this file and RETURN it to Main.
2. Write a NEW whole-primary checkpoint and a qualified post-return ACK.
3. Wait for Main's explicit future-only direction.

The original primary stays STOPPED until then. The same original eighteen owners, science cutoff 2026-10-27T11:05:38-07:00 and deadline 2026-10-27T12:35:38-07:00 remain in force.

**END OF v164-B REVIEW.**
