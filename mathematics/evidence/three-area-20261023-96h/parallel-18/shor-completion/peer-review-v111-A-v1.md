# Peer review v111-A — entire current PPT C1–C19/C21–C27 union (eight parts) with ADDENDUM-2

Reviewer MathShor (runtime MathShor-2), serial same-harness reviewer. Author PhysicsPPT44-2. Actual `/bin/date` immediately before composing this file: `Sun Oct 25 22:06:32 PDT 2026` (an earlier-observation bound, not an exact creation instant).

## 0. Verdicts at the exact reconstructed scope

**V1 — mathematics: 0 FATAL / 0 MAJOR / 1 NEW MINOR** (M1, the C27 optimality remark, §10.4). I reconstructed in writing every new proof (C19, C21–C27), the mandatory ADDENDUM-2 equivalence, and every old C1–C18 premise those proofs actually consume (§§3–12). The two old MINORs are retained: the C12 AT_MOST allocation and the old rectangle parent being 26LF, not 27. The cp071 row correction is also retained, and I verified the corrected identity row3 = 2·row1 + row2.

**V2 — dependency/application: SUPPORTED at named ordinary imports** for:
- C19 and C21–C26;
- C27's sign equivalence, strict margin and AA9 exclusion.

The following are **CONDITIONAL**:
- C27's finite-level completeness (AA8);
- C27's rational certifiability (end of AA8, and AA10).

They depend on the named classical import QD (infinite Bose-extendibility ⟺ separability), which is **NOT_RECONSTRUCTED** here, and on ordinary SDP strong duality. C26 does not consume QD.

No C19–C27 claim supplies a P44 pair or an unrestricted all-4×4 theorem, and the author says the same. ADDENDUM-2's provenance correction is right on the mathematics:
- at k = 2 the C27 cone is the old trace-corrected N4 cone, so ZERO new-method credit is due;
- C26 does not retire that cone.

**What "entire" covers here.** I read C1–C18 through every LF and ending. Outside the premises in §12 and the spot checks listed there, I did not freshly whole-reconstruct them in this gate. Their binding support stays the parent disposition `ppt-entire-C1-C18-PV-all-input-decomposition-parent-v1.md` (SHA256 0ce7d3a2…81a5) with its two MINORs. That is a stated boundary, not a transferred verdict. C20 (the conditional-generator material in X8) is CONTEXT ONLY and not reconstructed.

## 1. Process and exposure (conspicuous)

- **Permanent own reviewer PROCESS MAJOR (v109-A exactness).** Records: `peer-review-v109-A-written-exactness-finding-v1.json` (SHA256 f32c51d3…8584) and parent `v109-A-reviewer-exactness-parent-finding-v14.json`. It is retained and is not cured by this review. This review used exact symbols, fractions and integer products only, including in private working. It used no decimal magnitudes and no numerical scouts.
- **Opaque sequence:**
  - whole-primary checkpoint22 at 21:15:50 (SHA 6ae61e18…6c17);
  - opaque ACK at 21:16:33 (SHA 7e2952f6…c5a6);
  - parent release file `peer-review-v111-A-explicit-body-release-v1.json` (observed_clock 21:20:11, SHA 3a5e68f8…f402), read before the manifest entry or any part;
  - full reading;
  - substantive checkpoints in this root: `peer-review-v111-A-checkpoint-01-v1.json` (21:33:27) and `-02-v1.json` (22:02:24).
- **Serial exposure, NOT blind.** I am the same-harness reviewer of two earlier items. Neither verdict is transferred, and S33 was re-read in full here.
  - the old C1–C8 package (v94-B, 337LF review);
  - the old normalized N4 proposal (`peer-review-PPT-normalized-N4-soundness-v1.md`, v6).
- My exposure to unrelated privacy, NL, Rminus, Sun, preview and PH packets was disclosed in the ACK.
- **Primary paused.** The Shor primary has been paused since checkpoint22. It stays paused until this review is actually returned to Main and a separate resumption ACK is written.
- **Execution: none.** No scientific interpreter, calculator, eval, program, CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO was used. The only operations were metadata: `/bin/date`, `shasum`, `wc`.

## 2. Packet, coverage and bindings

| object | SHA256 | LF | read |
|---|---|---:|---|
| `peer-review-wave-eighteen-v111.json` | e2a86838…d47c | 3051 | own v111-A entry 1–690, including the full `post_ack_entire_scope` |
| `peer-review-wave-eighteen-v111-packet-receipt-v1.json` | — | — | whole; all four v111-A parts roundtrip/persisted equal |
| part1 | 5456a9ba…fe20 | 685 | 1–685 |
| part2 | edf7845b…ad28 | 1130 | 1–1130 |
| part3 | ad998469…58eb | 1167 | 1–1167 |
| part4 | e65bd034…83ac | 866 | 1–866 |

Live `shasum` of all four parts matched the release. Every LF of every part was read, including the endings.

| sections | content | LF |
|---|---|---:|
| S1–S19 | process records and parents (v9, v10 and v11 in that order) | — |
| S20 | ADDENDUM-2 | 52 |
| S21 | v3, C1–C10 | 723 |
| S22 | v4, C11–C14 | 394 |
| S23 | v5, C15–C17 | 290 |
| S24 | v6, C18 | 186 |
| S25 | v7, C19/C21/C22 | 306 |
| S26 | v8, C23/C24 | 225 |
| S27 | v9, C25 | 132 |
| S28 | v10, C26/C27 | 254 |
| S29 | ADDENDUM-1 | 42 |
| S30 | C12 overlay | 17 |
| S31 | cp071 addendum | 10 |
| S32 | cp080 author inventory only | 34 |
| S33 | old N4 proposal | 193 |
| S34 | 2505.22100v1, selected range only | LF 649–855 |
| S35 | parent C1–C18 | 66 |

## 3. C19 — interior point of the twisted-pair support cone

**Support pattern.**
- X_j = E_{j,j} + κ_j E_{j+1,j−1} and Y_j = E_{j+1,j} + γ_j E_{j,j+1} (indices mod 4).
- Each of the 16 positions of M(x,y) is used exactly once.
- The shift (r,c) → (r+1,c+1) maps the pattern of X_j/Y_j to that of X_{j+1}/Y_{j+1}, with κ_j → κ_{j+1}, γ_j → γ_{j+1}. It leaves prod κ and prod γ invariant. So cyclic transfer of every symbolic chart computation is valid.

**Lines (X2.3).** There are 16 distinct unordered pairs whose spans have rank ≤ 2 for all coefficients:

| pair | reason |
|---|---|
| X_j–X_{j+1} | two rows supported on one column |
| X_j–X_{j−1} | two rows supported on one column |
| X_j–Y_j | only two nonzero rows |
| X_j–Y_{j−1} (= Y_{j−1}–X_j) | only two nonzero columns |
| Y_j–Y_{j±1} | two rows supported on one column |

The remaining 12 pairs are: the two opposite-X pairs, the two opposite-Y pairs, and the eight pairs X_jY_{j+1}, X_jY_{j+2}. This matches X4.

**X0 chart.** The pivot is rows {0,1} × columns {0,3} = [[1, y3],[y0, κ0]], with determinant κ0 − y0y3.
- The Schur entries S21, S22, S32 have coefficient 1 in y1, x2, y2 respectively. All other dependence is multiplied by small variables, so the Jacobian is the identity at the base point.
- Leading terms: y1 = κ1γ0·ap, x2 = κ1κ3·ab, y2 = γ3κ3·bq.
- S31 gives κ2x2 = γ0γ3·pq + ab/κ0 + O(3). Hence (prod κ − 1)·ab − κ0γ0γ3·pq = O(3), which is (X3.2).

**Y0 chart.** The pivot is [[x0, γ0],[1, x1]], with determinant x0x1 − γ0.
- S22 gives x2 = κ1γ1·bp; S32 gives y2 = γ1γ3·pq; S33 gives x3 = γ3κ0·aq.
- S23 gives γ2y2 = pq/γ0 + κ0κ1·ab + O(3). Hence γ0κ0κ1·ab + (1 − prod γ)·pq = O(3), which is (X3.4).

Under (X2.1) both quadrics are nondegenerate, with nonzero gradient at every nonzero point.

**Curves.** F(εz)/ε² extends holomorphically to ε = 0, where it equals the quadric (up to a nonzero constant). The complex implicit-function theorem at a nonzero quadric point v gives z(ε) with z(0) = v. This avoids appealing to the oversized linear Zariski tangent space.

**Dual step.**
1. The eight strictly positive terms of σ0 force all eight diagonal H entries to be 0.
2. Each line forces its off-diagonal entry to be 0, because 2Re(z·H_UV) ≥ 0 for all complex z.
3. Along an actual curve the linear term vanishes, because X0 meets each of its four tangent directions in a line. The holomorphic ε² term averages to zero under the phase average. This gives <v,Hv> ≥ 0 on the whole quadric.
4. The planes (a,q) and (b,p), and then completion of an arbitrary (a,b), kill H_{X1X3}, H_{X1Y3} and H_{X3Y0}. Cyclically this kills both opposite-X entries and all eight cross entries; the Y charts kill both opposite-Y entries. Hence H = 0 on vecS.

**Closedness and conclusion.** K2(S) is closed: its trace-one base is compact and convex and does not contain 0. The supporting-functional argument also excludes an empty interior. So σ0 is interior, as claimed. No radius is asserted.

## 4. C21 — retirement of ρ64

**The map F.**
- F is unimodular: expanding along column 3 leaves a 3×3 determinant equal to 1.
- F|0> = |0>−|2>, F|1> = −|0>+|3>, F|2> = −|0>+|1>−|2>, F|3> = |3>.
- All nine transformed generators a′…h′ agree with (X5.1). Their squared norms are 7, 5, 4, 5, 3, 2, 3, 1, 2, so the trace is 7 + 5 + 4 + 3·16 = 64.
- The diagonal coefficients of each transformed generator sum to 0, so ρ64Ω4 = 0.

**PPT.** I re-derived the old C7B identity (10.2).
- R3^Γ consists of P(01+10), P(12+21), P00, P22, and the (02,11,20) block [[3,1,1],[1,1,−1],[1,−1,3]] = P(02+11−20) + 2P(02+20).
- The auxiliary part gives 3P(32+|0>⊗x̄) + 3P(|3>⊗x̄) + 3P(30+23) + 3P33.
- F is real, so [(I⊗F)X(I⊗F)^*]^Γ = (I⊗F)X^Γ(I⊗F)^T.
- The ten displayed vectors v1…v10 are exactly the images of the ten preimages, with weights 1,2,1,1,1,1,3,3,3,3. Trace: 7 + 10 + 4 + 5 + 2 + 3 + 3(5+2+3+1) = 64.
- At x = e0+e1 the nine generators are independent because each has a position no other uses; the same holds for the ten PT preimages. Hence ranks 9 and 10.

**22-phase identity.**
- Rows: [1,k,k²,0], [k^{-1},1,k,0], [ηk^{-1}, −k^{-1}, 1, (η/τ)k^{-4}], [f+k², k², g, ηk^{-1}].
- row0 = k·row1 and row3 = k²(1+τ)·row1 + τk³·row2, checked entrywise using f + k² = (1+τ)k + τηk² and g = (1+2τ)k³.
- row2 has a nonzero last entry, so the rank is exactly 2.
- τη = 1 + iε√2, so 1+τ = iε/√2, τη−1 = iε√2, 1+2τ = −1+iε√2 and |τ|² = 3/2. The squared moduli are 1/2, 2, 3, 2 and 4/3.
- The characters are 0, ±1, 2, 3, −4; their largest difference is 7 < 11. The crosses b/f, d/f and c/e vanish because E(1+τ) = E(τη−1) = Eη = 0.
- Average: Pa + Pb + Pc + Pd + 2Pe + (5/2)Pf + 3Pg + (4/3)Pj.
- Residual: 2Pd + Pe + (1/2)Pf + (5/3)Pj + 3Ph. Here d and e have SR 2, and f, j, h are products.
- Traces: 125/6 + 97/6 = 37 = 25 + 6·2.

Applying I⊗F gives the 27-summand certificate. The nonuniform weights are stated correctly, and so is the trace-zero ensemble consequence.

## 5. C22 — the entire complex weighted domain

**Two-point law.** With p + q = −|v| and pq = −T:
- Eτ = e^{iφ}(p+q) = −v;
- E(1/τ) = e^{−iφ}[1/(p−q) − 1/(p−q)] = 0;
- E|τ|² = p² + pq + q² = |v|² + T;
- E|τ+v|² = T;
- E|1/τ|² = −1/(pq) = 1/T.

For v = 0 the uniform law on ±√T works.

**Rows.** The rows of (X7.2) satisfy row3 = k²(v+τ)·row1 + τk³·row2, with entries (v+τ)k, vk², (v+2τ)k³, zk². Rows 1 and 2 are independent by their first entries, for every z.

**Retained coherences.** These are retained, not dropped:
- d/f = −ū, d/g = −w̄, f/g = uw̄;
- the f-diagonal is |u|² + T;
- the g-diagonal is |w|² + |v|² + 4T, using E|v+2τ|² = |v|² − 4|v|² + 4(|v|²+T).

Together this is P((1,−u,−w)) + diag(0, T, |v|²+4T) on (d_x,f,g). The crosses b/f and c/j vanish.

**Residual.** The residual is S_T. N(S_T) = V·S_T·V^* with V = [d_x,f,g], which is PSD whenever S_T is, and is supported on Alice levels {0,3}.

**Example and scope.** The example gives 1/3 + 4/11 + 1/16 = 401/528 < 1 and 1/16 ≤ 3/4, with strict inequalities, so it is a genuine open neighbourhood. The condition is sufficient only.

## 6. C23 — closed ball and projective Bob-filter domain

**Ball, z ≠ 0, with T = Z/3.**
- D1 = 3 − Z/3 ≥ 7/3.
- D2 = 3 − V − 4Z/3 ≥ 1 − Z/3 ≥ 1/3, using V ≤ 2 − Z; also D2 ≤ D1.
- The whitening load is ≤ 1/3 + (U+W)/D2 ≤ 1/3 + (2−V−Z)/(3−V−4Z/3).
- The bound is ≤ 1 because 2(3−V−4Z/3) − 3(2−V−Z) = V + Z/3 ≥ 0.
- Z/T = 3 exactly.

**z = 0 branch.**
- Rows [1,k,k²,0], [k^{-1},1,k,0], [0,−k^{-1},1,0], [0,vk²,−vk³,0], with row3 = −vk³·row2.
- A0 = Pa + Pb + Pc + N[P((1,−u,−w)) + diag(0,0,V)].
- S0 = diag(3,3,3−V) − P((1,−u,−w)), and 1/3 + U/3 + W/(3−V) ≤ 1/3 + (2−V)/(3−V) ≤ 1 because 3(2−V) ≤ 2(3−V).

**Source involution.** U and V5 send a→a, b→−c, c→b, d→−e, e→−d, f→g, g→−f, j→h, h→−j; I checked each ray. This is valid because b and c share weight 1, and d through h all share weight 3.

**Bob-filter charts.**
- B_xV5 = [e2, e1, −e0, −x, −e3], and F_x·x′ = −e3 for x′ = (w/z, v/z, −u/z, 1/z).
- If k4 ≠ 0: x = −first4(k)/k4, with chart norm (Ck+|k3|²)/|k4|².
- The involution chart uses V5^{-1}k = (k2, k1, −k0, −k4, −k3), with chart norm (Ck+|k4|²)/|k3|². This gives (Y4.2).
- If k3 = k4 = 0: Be0, Be1, Be2 are dependent, so the image of a has SR ≤ 2.

The necessity statement for a hypothetical SN3 output (both kernel components nonzero, and strict violation of (Y4.2)) is the correct contrapositive.

## 7. C24 — range-certificate barrier

- N_x has rows [1,1,1,0], [1,1,1,0], [0,−1,1,z], [1+v, v, 2+v, z], with row3 = (1+v)·row1 + row2. Its rank is exactly 2 for every z.
- Its coefficient on a is 1, so a lies in the span of SR ≤ 2 vectors inside the range.
- Every Bob rank-4 map is covered by a chart, the involution, or the core-kernel case. Lower ranks follow from B = L·B0 with ker B0 ⊂ ker B, and further local maps are covered too.
- The barrier holds. If v has a nonzero projection on S, some spanning SR2 vector C has <v,C> ≠ 0, which gives expectation −ε|<v,C>|² < 0. For the operator μP_{S⊥} − K, nonnegativity on the spanning SR2 vectors forces KS = 0.
- Scope: this certificate form only.

## 8. C25 — two weaker extension cones

**Class A.**
- V_N is an isometry with Bose-symmetric image.
- The extended-Alice PT is (I⊗V_N)ρ^{T_A}(I⊗V_N^*) ≥ 0.
- The Bell contraction selects only j = 1, with factor 1/(kN).
- DEC is closed, because the traces of the PSD parts are bounded. Since DEC* = PPT, bipolarity gives PPT* = DEC.

**Class B.**
- τ̂_N is permutation invariant.
- Every transpose of elementary factors leaves each summand PSD: ρ, ρ^{T_A}, ρ^{T_B}, ρ^T, P(v̄), and the diagonal auxiliaries.
- K_N and K̄_N both give Tr(Wρ)/(kN).

Both distinctions (which control, which objective) hold exactly as stated.

## 9. C26 — buffered full-PPT Bose obstruction (high consequence)

I reconstructed it completely and found no defect.

1. **AA2 (Haar range).**
   - The range of H_N(L)^{Γ_S} is span{w̄^{⊗m}⊗w^{⊗n}}, because it is an integral of rank-one projectors over a measure of full support.
   - That span equals Sym^m(C^L)⊗Sym^n(C^L). Take a vector of that space orthogonal to every w̄^{⊗m}⊗w^{⊗n}:
     - it gives a bihomogeneous polynomial in (w̄,w) that vanishes on the sphere;
     - since p(rw) = r^{m+n}p(w) for r > 0, it vanishes for every w ≠ 0;
     - so it vanishes identically in real coordinates, and all its coefficients are 0;
     - those coefficients correspond bijectively to the symmetric-basis coefficients, up to positive multinomial factors, so the vector is 0.
   - H_N(L)^{Γ_S} is positive definite on that range, with least eigenvalue γ > 0. Its one-body marginal is I_L/L by unitary invariance.
2. **AA3 (the three states).**
   - τ_sig is PSD, trace 1, Bose-supported via V_N, and PPT on the extended-Alice cut.
   - τ_0 = |0><0| ⊗ I/d ⊗ ∫P(|1,w>)^{⊗N}dμ and τ_b = |0><0| ⊗ I/d ⊗ H_N(D) are Bose-supported and separable across the complete parties.
   - τ_b is entangled inside pairs, so no inside-pair claim is made.
3. **Cuts.** By total transpose, every complete-party cut reduces to transposing a subset S of complete Bob pairs. S = ∅ is trivial. S = all uses τ_sig^{T_{A0A}} ≥ 0 together with separability.
4. **Proper S** (m = |S|, n = N − m ≥ 1). Write τ_sig = (1/N)·Σ_{j,j′}.
   - Within S: [(I⊗V_S)ρ(I⊗V_S^*)]^{T_S} = (I⊗V̄_S)ρ^{T_B}(I⊗V̄_S^*) ≥ 0, tensored with P(|1,v>^{⊗n}).
   - Within T: unchanged inside T, with spectators P(|1,v̄>^{⊗m}).
   - Both are ≥ 0, so D_S ≥ 0.
   - Cross terms, j ∈ S and j′ ∈ T: the pair factors are |0,b><1,v| at j and |1,v><0,b′| at j′; after T_S the factor at j becomes |1,v̄><0,b|.
     - The ket leg is |0>_{A0}⊗|a>⊗(auxiliary 1 on every pair)⊗v̄^{⊗m}⊗v^{⊗n}, independent of j, j′, b, b′. It lies inside E0_S = range τ_0^{Γ_S} = |0>⊗C^d⊗(auxiliaries all 1)⊗Sym^m(C^d)⊗Sym^n(C^d) (AA2 with L = d).
     - The bra leg is (Σ_{j∈S}|0,b>_j⊗|1,v̄>_{S∖j}) ⊗ (Σ_{j′∈T}|0,b′>_{j′}⊗|1,v>_{T∖j′}). It is symmetric within S and within T, and it lies in the two-zero sector orthogonal to E0_S.
   - The (T,S) blocks are the adjoints.
   - Every piece lies in R_S = |0>⊗C^d⊗Sym^m(C^D)⊗Sym^n(C^D), on which τ_b^{Γ_S} ≥ γ_S·P_{R_S}.
5. **Schur buffer.** Take u = x + y with x ∈ E0_S and y ∈ R_S ⊖ E0_S.
   - <u,B_S u> ≥ b_S‖x‖².
   - |<u,(C_S+C_S^*)u>| ≤ 2‖C_S‖‖x‖‖y‖.
   - Mε²γ_S‖u‖² ≥ Mε²γ_S‖y‖².
   - The 2×2 form [[b_S, −ε‖C_S‖],[−ε‖C_S‖, Mε²γ_S]] is PSD iff Mγ_S·b_S ≥ ‖C_S‖², a condition independent of ε. (AA4.4) gives it strictly.
   - Adding εD_S ≥ 0 and Mε²(τ_b^{Γ_S} − γ_S·P_{R_S}) ≥ 0 finishes the bound; every operator is zero outside R_S.
   - One finite M therefore serves every ε > 0 and every proper S.
6. **Objective.**
   - Tr(K_N τ_0) = 0, because the Bell vector pairs auxiliary 0 with auxiliary 0 while τ_0 has auxiliary 1.
   - Tr(K_N τ_sig) = Tr(Wρ)/(kN).
   - Tr(K_N τ_b) = Tr(Φ_k(|0><0|⊗I/k))·TrW/d² = TrW/(k²d²).
   - If Tr(Wρ) = −δ < 0, the expectation is negative for 0 < ε < δkd²/(MN·TrW) when TrW > 0, and for every ε > 0 otherwise.
   - Bose support makes the Q_N and K_N values equal.
7. **Conclusion.**
   - A nonnegative finite-level bare Bose/all-complete-party-PPT minimum forces Tr(Wρ) ≥ 0 on every physical PPT ρ. Hence W ∈ PPT* = DEC. The contrapositive follows by separation.
   - The auxiliary twirl Ū⊗U⊗…⊗U preserves everything: it is local on complete parties, commutes with pair permutations, and fixes φ_k, since (Ū⊗U)φ_k = (ŪU^T⊗I)φ_k = φ_k.
   - N = 1 and d = 1 are included.
8. **Direction.** What is proved is the implication "certificate ⟹ physical DEC", i.e. a necessary condition. No converse (DEC ⟹ certificate) is claimed or reconstructed. If the frozen scope word "equivalence" was meant as an iff, that iff is neither claimed by the source nor established here. This is not a source defect.

## 10. C27 — overlap normalization

**10.1 Sign equivalence.** For a unit Schmidt vector ψ with ℓ ≤ k terms and orthonormal auxiliary labels |r>:
- α and β are unit vectors, and the contraction is ψ/(√k·S);
- the overlap is 1/(kS²) ≥ 1/k², since S ≤ √ℓ ≤ √k.

The converse holds because every extended product contracts to an SR ≤ k vector.

**10.2 Strict margin.** Tr(Hτ_i) = <χ|W|χ> ≥ μ‖χ‖² = μ·Tr(Pτ_i). Hence every constrained separable mixture gives ≥ μ/k².

**10.3 AA8–AA10, under the named QD.**
- *Limit.* E_N is compact: it is the partial-trace image of a compact set of Bose states, intersected with the closed overlap set. The sets are nested, and by QD their intersection is the constrained separable set. The minima increase to the separable minimum, by the convergent-subsequence argument.
- *Duality.* The dual (AA8.1) follows by weak duality. Slater holds:
  - the maximally mixed Bose state has one-body marginal (I_{kd}/kd)⊗(I_D/D) and overlap 1/k²;
  - the Bose extension of an auxiliary-00 product has overlap 1/k > 1/k²;
  - their mixture is full rank with overlap > c.
- *Rational certificate.* Lowering β by δ′ adds δ′P_N. A rational perturbation then preserves both strict conditions.
- *AA10 regularizations* hold: νI with 0 < ν < the gap; mixing ρ with I; and Gaussian-rational approximation of the density.
- *AA9.* p_ε ≥ 1/k² ⟺ ε(k/N − 1) ≥ 1, which is impossible for N ≥ k.

**10.4 M1 (NEW MINOR, non-load-bearing).** The AA7 sentence "The threshold c is the largest universally safe one" is stated for arbitrary d ≥ 1 and k ≥ 2 (AA1). It has two problems:

- **(i) It is false when d < k.** Every unit physical vector then has Schmidt rank ℓ ≤ d, so S² ≤ d. The canonical factorization therefore has overlap 1/(kS²) ≥ 1/(kd) > 1/k², so the larger cap 1/(kd) is also universally safe.
- **(ii) For d ≥ k the supplied proof is incomplete.** The nuclear-norm argument only shows that a single unit product whose contraction is proportional to ψ_max has overlap ≤ 1/k². It does not by itself exclude a larger cap that separable mixtures could rescue.

For d ≥ k the statement is nevertheless TRUE. Take W_λ = λI − (λ+δ)P(ψ_max) with δ > 0:
1. <ψ_max|W_λ|ψ_max> = −δ, so W_λ is not k-block-positive.
2. For every unit-product contraction χ, write p = ‖χ‖². Then |<ψ_max,χ>|² ≤ min(p, 1/k²), by Cauchy–Schwarz and by ‖χ‖_1 ≤ 1/√k with ‖ψ_max‖_op = 1/√k.
3. g(p) = λp − (λ+δ)·min(p, 1/k²) = max(−δp, λp − (λ+δ)/k²) is convex, and nondecreasing on [1/k², ∞).
4. By Jensen, every separable τ with overlap ≥ c′ > 1/k² has Tr(Hτ) ≥ λ(c′ − 1/k²) − δ/k².
5. That is > 0 once λ > δ/(k²c′ − 1), so the cap c′ fails the sign equivalence.

**Repair (additive reading):** restrict the optimality remark to d ≥ k and supply the mixture argument. For general d, the cap 1/(k·min(k,d)) is safe.

Nothing depends on this remark: not C26, not AA8–AA10, not ADDENDUM-2, and not the P44 application (d = 4, k = 2). In every case c = 1/k² ≤ 1/(k·min(k,d)) remains a valid safe cap.

## 11. ADDENDUM-2 and the old 193-LF N4 proposal

**The cone equivalence.**
- The old cone is C_old(Y,μ) = Q_S(Y) + μ[P_N − 2Q_S(I)], with the unnormalized singlet S and Tr P(S) = 2.
- J = [[0,1],[−1,0]] on Alice's auxiliary gives (J⊗I)Ω2 = S. J is local on the Alice party, commutes with P_N, and preserves every complete-party cut.
- P(S) ≅ 2Φ2, hence C_old/2 ≅ Q_H(Y) − 2μQ_P + (μ/2)P_N = Q_H(Y) − η[Q_P − (1/4)P_N] with η = 2μ. This is exactly AA8.1 at c = 1/4 and β = −η/4.
- A positive certified bound δ = β + η/4 > 0 implies the zero-bound inequality (add δP_N).
- Product test, with the auxiliary-00 extension at overlap 1/2: <ab|Y|ab>/2 ≥ η(1/2 − 1/4), so <ab|Y|ab> ≥ η/2. With TrY = 16 this gives η ≤ 2 ⟺ μ ≤ 1.
- I re-derived the old §1 implication: Tr(C_Nσ_N) = <ψ|Y|ψ> + μ(ℓ² − 2) with ℓ² ≤ 2. This is the same as C27 at k = 2, where p = 1/(2ℓ²) ≥ 1/4.

**Provenance and N4 status.**
- I agree with the withdrawal. At k = 2, C27's normalized mechanism is the old corrected cone, so ZERO new-method credit is due.
- C26 concerns the bare objective. AA9 shows its buffered controls violate p ≥ 1/4 at every N ≥ 2, so C26 does not retire the corrected N4 assay.
- N4 status stays UNKNOWN / incomplete / overrun / historical-exit-unestablished.

**Old §2–§3: displayed arithmetic only.** I checked the following in writing:
- the q± values (5/4, 1/4) and (1, 1/2), and r + s = 11/4;
- the second-moment identities 23/8 and 5/2;
- the sector values 70/131 + 6/13 = 1696/1703 and 2/3 + 8/31 = 86/93;
- D ≥ μ = 1/2, which gives (1 − 1696/1703)/2 = 7/3406, and the scaling (8/29)(7/3406) = 28/49387;
- TrYctrl = 16 and the control value −1/29;
- 6·140 + 4·320 + 2·260 = 2640 = 8·binom(11,4).

The spin-sector formulas (3)–(5), the boson commutator identity and the highest-weight bases are NOT_RECONSTRUCTED here. They establish non-PSD headroom only, and they are not premises of C26, C27 or ADDENDUM-2.

**Checkpoint081 observation (my reading only).** cp081's general-k "normalized N ≤ k PSD-only" observation is not in this packet. For the PSD-only normalized Bose cone it follows elementarily from AA3's signal alone: for any physical ρ the overlap is 1/(kN), which is ≥ 1/k² iff N ≤ k. At k = N = 2 it specializes to the old corrected-N2 vacuity. This is not a gate on cp081.

## 12. Old C1–C18 premises actually used by C19–C27

| premise | status | used by |
|---|---|---|
| C7B (10.1)–(10.2): the R_x generators and the full PT Gram identity | re-derived in §4 | C21 (PPT of ρ64), the C22/C23 domains, the C24 ranges |
| R45's PPT | follows from the same computation with \|3>⊗x replaced by \|34> (x = e4) | C23, C24 |
| U2.1–U2.4 weighted PPT certificate: block [[r,1,1],[1,1,−1],[1,−1,s]] with Schur residual [[r−1,2],[2,s−1]], plus the 2×2 blocks [[G,r],[r,H]] and [[F,s],[s,J]] | re-derived | C22's application remark only |
| DEC closedness and PPT* = DEC (also C10 §13.6) | re-derived in §8 | C25, C26 |
| Ordinary imports: local Schmidt-rank upper-bound transfer, finite characters, PSD/Schur/Gram, rank-one whitening | model-specific instances checked | throughout |

**Not consumed by any C19–C27 proof:** C1, C3–C6 and C8–C18. C9, C10 and C18 appear only in scope and caller statements.

**Spot checks made while reading:**
- C2: the trace N, and the integer/332 density (traces of K0…K3 are 96, 96, 80, 60);
- C3: the row identities (4.2);
- C18: the block form and the Schur peel.

I found no new issue. No fresh whole-union certification is claimed.

## 13. Dependency/application verdict (V2)

**Dependency graph.** There is no circularity. C26 and C27 do not use each other, except that AA9 consumes the AA3 controls.

| item | depends on |
|---|---|
| C19 | rank-2 line algebra, complex IFT, cone separation |
| C21 | (10.2), the F congruence, finite characters |
| C22 | the two-point law, characters, the U-generators |
| C23 | the C22 identities (restated inline), the source involution, kernel factorization |
| C24 | the N_x algebra, the C23 charts |
| C25 | V_N, Bell contraction, DEC duality |
| C26 | AA2 Haar range, V_N, τ_0/τ_b, the Schur buffer, DEC duality (no QD) |
| C27 sign/margin | AA7 algebra |
| C27 AA8/AA10 | QD, compactness, SDP duality, Slater |
| C27 AA9 | the AA3/AA5 controls |
| ADDENDUM-2 | the old §1 definitions, AA8.1 |

**Applications are correctly scoped.**
- **C19:** an infinitesimal interior statement only.
- **C21:** an actual retirement of ρ64 against ANY sound SR2 witness, and also against trace-zero generators.
- **C22/C23:** sufficient domains only; failing them does not imply SN3.
- **C24:** one certificate mechanism, for all Bob rank ≤ 4 local images.
- **C25:** two weak cones.
- **C26:** every finite bare Bose/all-complete-party-PPT certificate forces physical DEC, so this cone cannot deliver P44 at any finite level. Inside-pair cuts, other objectives and the normalized cone stay outside it.
- **C27:** a correct nonvacuous replacement, conditional on QD. It fixes no N and gives no rational values.

**Original P44 remains UNMET.** There is no explicit rational or Gaussian-rational 4×4 PPT density with a strictly negative separator that is nonnegative on every complex SR≤2 vector, and no unrestricted all-4×4 theorem "PPT ⟹ SN ≤ 2".

## 14. Named imports and NOT_RECONSTRUCTED items

**NOT_RECONSTRUCTED:**
- **QD** (infinite Bose-extendibility ⟺ separability). S34 LF 800–805 states it with a citation and does not prove it in the selected range.
- **SDP strong duality and dual attainment under Slater** (ordinary).
- **The complex analytic implicit-function theorem and finite-dimensional cone separation** (ordinary); their elementary instances were checked.
- **Old N4 §2–§3:** the spin-sector derivations and the highest-weight bases.
- **C20/X8** conditional-generator material.
- **Literature context:**
  - Park 2602.09860;
  - Johnston–Lovitz 2609.11849;
  - Krebs–Gachechiladze 2509.07086;
  - 2508.21348;
  - 2010.15554;
  - 2010.07898 and 2010.11891.
- **The contents of cp081.**
- **Old C1–C18 beyond §12.**

**S34, LF 649–855, read literally as a selected range.** It covers Lemma 4 (sign equivalence of the k-extension), Remark 5, the infinite-exchangeability statement, Definition 6 and Proposition 1. This is not a whole-paper reading. It is not a claim that the source proves finite sign-completeness, and not a claim that the source is wrong.

## 15. Findings

| id | severity | location | finding |
|---|---|---|---|
| M1 | MINOR (new, precision) | S28 AA7, optimality sentence | "Largest universally safe" is false for d < k. The given proof covers only single products proportional to ψ_max. The claim is true for d ≥ k by the Jensen argument in §10.4. Non-load-bearing. |
| R1 | MINOR (retained) | C12, U5.2 | AT_MOST allocation overlay (S30) |
| R2 | MINOR (retained) | metadata | the old rectangle parent is 26LF/5003B, not 27 (S29) |
| R3 | correction (retained) | cp071 | row3 = 2·row1 + row2, verified (S31) |

There is no FATAL and no MAJOR finding.

All of the following remain in force:
- the author's process findings: cp049, cp063 and cp081 exactness, ACK order, cp013 cadence/admission, N4 UNKNOWN, old21;
- all parent and reviewer histories in S1–S19.

Mathematical zero counts are not process-clean counts.

## 16. Nonclaims

This is a same-harness, serial, written review. It is not any of the following:
- formal or kernel verification;
- executable or triple verification;
- configured-family or cross-vendor review;
- human review;
- novelty, SOTA or publication acceptance;
- scientific permission or parent adoption.

No source, author, shared or parent file was edited; all outputs are only in `shor-completion/`. The original cutoff (2026-10-27T11:05:38-07:00) and deadline (12:35:38) are unchanged. This is not a round closeout.

**END — entire v111-A union: all four packet parts and all 35 sources read through their endings; two verdicts given; one new precision MINOR.**
