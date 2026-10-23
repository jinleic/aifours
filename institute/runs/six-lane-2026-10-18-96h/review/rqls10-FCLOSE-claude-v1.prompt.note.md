# Hostile written review: `wh5-family-couple-closure` (00–05)

The review is frozen at 2026-10-19T21:14:06-0700, the stamp you supplied. I used only the pasted text of 00–05, with no tools, files, code or numerics. Package labels such as "proved" and "CLOSURE" were treated as untrusted, and every verdict below rests on my own re-derivation.

**File legend**
- 00 = `00-scope-freeze-v1.md`
- 01 = `01-column-reduction-v1.md`
- 02 = `02-pair-lemma-and-conditional-closure-v1.md`
- 03 = `03-family-base-identities-and-closure-v1.md`
- 04 = `04-import-interface-map-v1.json`
- 05 = `05-process-and-deviations-v1.md`

## Counts

**FATAL 0 · MAJOR 0 · MINOR 5.** None of the five is a correctness error:
- 1 interface item that leaves one reading conditional
- 1 exposition item
- 1 pair of omitted one-line justifications
- 1 incomplete premise list for a conditional claim
- 1 metadata item

There are also 3 process observations. They are not counted and have no mathematical consequence.

**I found no correctness flaw in C1–C12.**

## Claim-wise verdicts

| Claim | Source | Verdict |
|---|---|---|
| C1: three-basis flatness ⇔ φ₁ supported in {1,2,3} and φ₂ in {1,2,4}; tilde supports {0,±1} and {0,±2} | 01 LF13-29 | CORRECT |
| A prescribed column integrates to a diagonal E (moduli match, Π w_t = 1, q ≠ 0) | 01 LF30-33 | CORRECT |
| C2: modulus lemma, cases (A)/(B), global phase retained | 01 LF35-56 | CORRECT |
| Symmetry ⇒ u = w ⇒ q = k(z+z⁻¹)+b | 01 LF58-62; 03 LF97 | CORRECT (terse; see MINOR-3) |
| C3: pair lemma | 02 LF9-39 | CORRECT, given symmetric M, q ≠ 0 and F1 |
| C4: Theorem 4 (all of (B) eliminated; conjugate column eliminated; μ⁵ = 1) | 02 LF41-63 | CORRECT (see MINOR-2, MINOR-3) |
| C5: Lemma 5 identities and strict signs | 03 LF9-42 | CORRECT |
| C6: Lemma 6 (U-eigenvectors, rank-2 projector, U-invariance, flat in Z/X/T) | 03 LF44-87 | CORRECT |
| Expansions of q0, q1, q2, r0, r1; nonvanishing; symmetry for every τ | 03 LF89-97 | CORRECT |
| C7: F1, Im(T0·conj T1) > 0 | 03 LF99-107 | CORRECT |
| C8: F2 and k ≠ 0 | 03 LF109-116 | CORRECT |
| C9: dilation S, the four labels as one 4-cycle, support preservation both ways | 03 LF118-130 | CORRECT |
| C10: E P_τ E* flat ⇔ E = λZ^c, for every τ | 03 LF132-137 | CORRECT for the family displayed at 03 LF46-49 |
| 03 LF50: "these are exactly the frozen coordinates" | 03 LF50 vs 00 LF11-12 | UNVERIFIED. The frozen-F reading of C10–C12 is CONDITIONAL (MINOR-1) |
| C11: the Anti_Z maps with flat image are exactly the five circles λZ^cQK; image is Z^c P_(−τ) Z^(−c) | 03 LF144-152 | CORRECT |
| C12: all WH translates, bases Z/T/X, five circles each; images D_(w+l) P_(−τ) D*_(w+l), l ∈ L_b | 03 LF139-172 | CORRECT (MINOR-1 caveat) |
| C13: no W8 solution has even one F-plane | 03 LF174-182; 04 LF37 | CONDITIONAL on HW, HF and the MINOR-4 premises. Not accepted here |
| Scope answer | 04 LF13-16 | Consistent with C10/C12 |

## Findings

**MINOR-1 (interface; keeps the frozen-F reading conditional).**
- *Step.* 03 LF50 asserts that X_τ and Y_τ at 03 LF47-48 are the frozen coordinates of 00 LF11-12 (c29b8bf7…877a). That source is not pasted, so the equality cannot be checked here.
- *Consequence.* Theorems 10–12 are proved for the family displayed in 03, and that proof is self-contained. Applying them to the frozen F requires entrywise equality: the placement of a/b/g/d, the signs of iσ and iσ′, and the R = diag(ζ^{t²}) gauge. The order of the τ labels does not matter, because F is a union over all four τ and Lemma 9 cycles through them.
- *Repair.* The parent compares the coordinates literally, or 03 LF46-49 is declared the definition of F for this slice.

**MINOR-2 (exposition; no mathematical consequence).**
- *Step.* Π is never defined in 01–03 (it appears at 02 LF51-53 and 00 LF34). The three facts used all hold for Π e_t = e_(−t):
  - Π f_m = f_(−m) and Π g_m = g_(−m);
  - ΠR = RΠ;
  - ΠMΠ = conj M is equivalent to M_(−r,−s) = conj M_(r,s).
- Several symbols are overloaded:
  - A is a constant (03 LF12) and also the antiunitary (03 LF144-150);
  - c is a constant (03 LF13), an element of Z₅ (03 LF133 ff.), and T(4) (02 LF15);
  - d is a constant and also d_t (02 LF22);
  - e is 1/√5 and also e_t.
- *Repair.* Define Π explicitly and rename the clashing symbols.

**MINOR-3 (two one-line justifications missing at load-bearing steps; both statements are true).**
- (i) At 02 LF57, Lemma 3 needs H′ = conj(M) to be flat, and this is never stated. It holds because the supports {0,±1} and {0,±2} are symmetric under negation; equivalently, R·conj(M)·R* = Q·conj(P)·Q*.
- (ii) At 01 LF61-62 and 03 LF97, "u = w" needs two facts:
  - z_(−t−1) = η·ζ^(−t−1) = η⁻¹ζ^(−t) = z_t⁻¹;
  - the coefficients of a three-frequency expansion are unique.
- *Repair.* Insert both lines.

**MINOR-4 (incomplete premise list for the conditional C13).**
- *Step.* 03 LF177-180 goes from HW+HF to "one F-plane implies all four". It also uses three premises it does not state:
  - (a) Every representative W8 plane is flat in Z/X/T. Theorem 12 only classifies flat images.
  - (b) The F-plane has an Anti_b couple to each of the other three planes ("three incident couples"). At minimum, the couple graph on the four planes must be connected.
  - (c) Anti_b and K_b in HW are the objects defined at 03 LF142, with b ∈ {Z,T,X}.
- *Consequence.* If (b) fails, the one-plane deduction fails. C13 stays conditional in any case.
- *Repair.* Add (a)–(c) to HW at 03 §6 and 04 LF37.

**MINOR-5 (metadata and wording).**
- 04 LF27: C3 also depends on the symmetry M_(−r,−s) = conj M_(r,s), which forces T = (a,b,b,a,c).
- 04 LF32 and LF34: C8 and C10 also depend on 01 LF58-62.
- 04 LF28: the C4 hypotheses (symmetry, q ≠ 0, k ≠ 0, F2) are not listed.
- 03 LF185: "Lemmas1-4" should read "Lemmas 1–3, Theorem 4".
- 02 LF58: "a real nonzero scalar times q2/q0" is in fact an equality.
- 01 LF39: "exactly … suffice" describes a list of necessary forms (01 LF44 says this).
- *Repair.* Make these edits in a new versioned file. No mathematical statement changes.

## Re-derivation record (load-bearing steps)

**01: Fourier reduction and modulus lemma**
- From (t+a)² − t² = 2at + a²:
  - 5 f_m*Hf_m = Σ_a ζ^(−ma) S_a;
  - 5 g_m*Hg_m = Σ_a ζ^(−ma−2a²) Σ_t φ_a(t) ζ^(−4at).
- Hermiticity gives φ_(−a)(t) = conj φ_a(t−a). Hence S_(−a) = conj S_a, and the weighted sum for −a is ζ^(4a²) times the conjugate of the weighted sum for a.
- The forbidden frequencies are therefore {0,4} for a = 1 and {0,3} for a = 2.
- Gauge: q_a(t) = ζ^(−2at−a²) φ_a(t), giving tilde supports {0,±1} and {0,±2}.
- Lemma 2:
  - z²·(difference of moduli squared) has degree ≤ 4 and vanishes at five distinct points of |z| = 1, so it is zero;
  - the three coefficient identities follow;
  - after the phase normalisation, (w−u)·Im v = 0;
  - in case (A), Re v = Re(k·conj b)/K = Re(Kb/k) and |v| = |b|.

**02: pair lemma and Theorem 4**
- Triangle invariance gives the second columns T(t)d_t and λ²·conj T(t)·d_t.
- The frequency ±1 conditions say that both rows (a,b,c) and their conjugates annihilate v_±.
- Kernel:
  - the cross product of the two rows is 2i·n, and n₃ = Im(a·conj b) ≠ 0;
  - so the rows have rank 2 and the kernel is ℂ·n.
- Comparing third entries gives v₋ = ζ^(−8)·v₊ = ζ²·v₊. Hence:
  - (1−ζ²)(d0−d3) = 0;
  - (ζ⁴−ζ³)(d1−d2) = 0.
- The ratios (1+ζ³)/ζ⁴ = ζ+ζ⁴ and (ζ+ζ²)/ζ⁴ = ζ²+ζ³ are real and nonzero, so d0/d4 and d1/d4 are real.
- Then h1 = h3 and h0 = h4.
- Case (B):
  - (ΠHΠ)_(t+1,t) = conj h(−t−1) = conj(μ)²·h(t);
  - the pair lemma then gives (u−w)(z_t − z_t⁻¹) = 0, with z₀ = η ≠ ±1.
  - The frequency-±1 conditions for H′ follow from those for H. The elimination is therefore non-circular, and it covers **every** real unequal-coefficient candidate without solving any (B) equation.
- Conjugate column: h = μ·conj q gives d0/d1 = conj(h2/h0) = q2/q0, which must be real. This contradicts F2.
- Original column: w_t ≡ μ and Π w_t = μ⁵ = 1.

**03 Lemma 5: constants and signs** (every identity re-derived)
- αβ = 2cos(2π/3) + 2cos(2π/5).
- γδ = 2cos(6π/5) + 2cos(2π/3) = −φ².
- δ² = 2 + α, using cos(28π/15) = cos(2π/15).
- βδ = β + 1/φ, using cos(22π/15) = cos(8π/15).
- uv = −1 − 3φ, so AB = 9 − 3φ = κ².
- (2+β)A + (2+α)B = 6√5, and the difference is (3−√5)κ + 2(γ−δ).
- c²φ² = 1/20, so gd = −1/20.
- g² + d² = (11−3√5)/40 and a² + b² = (5+3√5)/40.

**03 Lemma 6: eigenvectors and flatness**
- Gauss sums: G₁ = √5 and G₂ = −√5.
- (F*g_m)_n = −ζ^(−2(m−n)²)/√5, so U g_m = −ζ^(3m²) f_(−m).
- U v_(μ,j) = −μ·v_(μ,j), using μ³ = 1.
- All seven ε-identities hold, for example:
  - ω²ζ² + ω = ε² + ε¹⁰ = γζ;
  - (ζ−ζ⁴)(ω²ζ² − ωζ³) = (2i)²·sin(6π/15)·sin(2π/15) = β − γ;
  - (ζ²−ζ³)(ω²−ω) = 4·sin(π/5)·sin(2π/3) = κ.
- Normalisation:
  - c² = p/N = (3−√5)/40;
  - c(1+√5) = e;
  - sκ/√B = a.
- With these, x_τ = R X_τ and y_τ = R Y_τ hold entry by entry.
- Flatness transfers to the other bases through g_m = U e_(−m) and f_j = ζ^(2j²)·U* e_j.

**03 LF89-116: expansions, F1, F2**
- X(−t) = conj X(t) and Y(−t) = conj Y(t) for all τ.
- I re-expanded q0 through q4, r0 and r1. All match, including q3 = q1, q4 = q0, r2 = r1 and r3 = r0.
- Lemma 7, using R0 + 2a² and 2d² − R0:
  - V = (G² + a² − b²) + 2iGb;
  - W = [d(g²+d²+a²−b²) − 2gab] + i[a(d²−g²+a²+b²) − 2dgb].
  - Every sign follows from Lemma 5 alone.
- Lemma 8:
  - Im(q0·conj q1) = 2de[ga + (2g+d)b];
  - the coefficient (φ+2)/√5 in 03 LF114 simplifies to φ.

**Independent exact cross-check (not in the package).** For a symmetric column pattern, first-column flatness is equivalent to q2 = (1−φ)q0 + φq1.
- Real part: (1−φ)(2−φ)/10 − φ/10 = 3(1−φ)/10 = R0.
- Imaginary part:
  - The condition reduces to (δ+1)·a = (γ−1+φδ)·b.
  - Over ℚ(√5) every constant is a polynomial in γ:
    - α = 1 + γ/φ, β = (1−γ)/φ, δ = −1/φ − γ;
    - γ² = φ² − γ/φ;
    - A = 3φ − 1 + φγ, B = 3φ − 2 − φγ.
  - Both (δ+1)²A and (γ−1+φδ)²B equal 11φ − 13 + (7−4φ)γ.
  - Both (δ+1)a and (γ−1+φδ)b are negative, so the condition holds.
- So the displayed expansions agree exactly with Lemma 6.

**03 Lemma 9: dilation**
- X_τ read at indices (0,2,4,1,3) equals Y_(−σ′,σ), and Y_τ read the same way equals X_(−σ′,σ).
- This gives the cycle (++) → (−+) → (−−) → (+−).
- Supports:
  - q2(2t) has support {0,±1};
  - q4(2t) = conj q1(2t−1) has support {0,±2}.
- S⁴ = I, and S*ES = diag(e_(3t)).
- Independent support: R S R* sends f_m ↦ g_(2m) and g_m ↦ f_(2m).

**03 Lemma 11 and §5: antiunitaries and transport**
- Q = R², and conj X_τ = X_(−τ).
- (DK)P(DK) = D·conj(P)·D*.
- The g basis is the eigenbasis of XZ⁻¹, with eigenvalue ζ^(3−m) on g_m.
- F*XF = Z⁻¹ and F*ZF = X. Hence:
  - U X U* = Z⁻¹;
  - U Z U* = Q X Q* = ζ²·XZ⁻¹;
  - U D_(a,c) U* is proportional to D_(c,−a−c).
- The lines cycle L_Z → L_T → L_X.
- U K U⁻¹ = K_T exactly, and U²KU⁻² lies in Anti_X.
- Anti_b does not depend on the phase choice for the basis, since K_(θb) = D_θ²·K_b.
- Necessity and sufficiency in Theorem 12 follow by conjugating Lemma 11 by D_w, U and U², using U P_(−τ) U* = P_(−τ).

## Correctness versus the other axes

- **Correctness.** C1–C12 are correct as stated; C10–C12 apply to the family displayed in 03. C13 is conditional.
- **Completeness.** Every obligation in 01 §3 and 02 §3 is discharged:
  - H0 by Lemma 6;
  - H1 by 03 LF96 and Lemma 8;
  - F1 by Lemma 7;
  - F2 by Lemma 8;
  - the product condition at 02 LF61;
  - the transports in 03 §5.

  The "direct expansions" at 03 LF92-95, LF102-105 and LF111 omit their intermediate lines. I redid them and they are correct.
- **Computation.** No numerical value appears in any proof step. The float exposure (00 LF27-28) is disclosed and never used. The identity at 03 LF21 is unused but harmless.
- **Process** (not mathematical; the parent owns this verdict):
  - Use of `wc` and the glob tool outside the 00 LF41 list is disclosed at 05 LF16-19.
  - Checkpoint055's early claim of a complete argument is disclosed at 05 LF8-13, superseded by 01 LF71-72, and not used as a premise.
  - The stamps show note03 (186 LF) was dated 18:37:04 (03 LF3). If the 18:38:46 byte count (05 LF16) included it, note03 was persisted within two minutes. That fits pre-composed working text. It has no effect on correctness, because every step was re-derived here.
- **Priority.** The package makes no novelty or priority claim (03 LF186, 04 LF66), and none is made here.

## Errata and limits

- **Errata.** The pasted text contains no mathematical errata. The only superseding statement is checkpoint055's non-evidence status (01 LF71-72, 05 LF8-13). I applied it: checkpoint055 was not used.
- **Not approved by this review:**
  - W8 nonexistence;
  - the internal-F HW/HF claims (c625b377);
  - the match to the frozen coordinates;
  - maximal 1-RQLS(10);
  - runtime, which stays on HOLD (00 LF6, 05 LF25).
- **No other claims.** This review makes no Lean, human, independent-verification or novelty claim.
- **Re-submission.** None is needed for correctness. The MINOR repairs are textual and belong in a new versioned note.
