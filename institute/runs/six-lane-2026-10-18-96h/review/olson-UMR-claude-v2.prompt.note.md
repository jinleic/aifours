## UMR v1: independent written review (parent erratum v1 applied)

**Counts after the erratum: 0 FATAL / 0 MAJOR / 1 MINOR (wording only).**

I re-derived erratum items m1 and m2 independently. Both are correct and sufficient. I found no other mathematical defect.

### Claim-wise verdicts (proof LF unless marked)

| Claim | LF | Verdict |
|---|---|---|
| Lemmas 0–2 | 44–68 | Correct. (SR) follows from Φ=2m, δ_GRX=N−2m, C_max=2H+2m and 2p−2H=2κ+2. At central levels ℓ_m+M_m=δ+2≤2κ−2. |
| Lemma 3, normalisation, light side | 70–112 | Correct. SC0 applies to Y′z (length ≥p+2), giving ord g0=2p. (S′) at (p−1,κ−1) is met literally: R=2p+2κ′−k′, (S1) at κ′ by (b), t≤κ′, L≥p+1, g0 odd, W≤2p−1. FB-E is not used. The light-side swap keeps the labels. |
| Lemma 4(iv), reservoir | 90–98 | Correct in all three label cases. The −s_j case uses n_−≥1, which holds because t≥1. |
| Lemmas 5–6 | 113–129 | Correct. |
| Lemma 7 (all central m) | 133–160 | Correct. Case U: the minimal J holds at least bmax+3 units, by (C1). Case L: each move gains at most bmax+1 ≤ R−M−ℓ, by (C2). x+y≤δ+2. |
| Lemma 8 (λ=y−1, μ=x−1) | 161–173 | Correct. B*≤2p−4+x+y, and the representative window has length ≤2κ−2. |
| Lemmas 9–10 | 177–209 | Correct. All 36 sums are ≤2δ+8, so \|d_π−d_ρ\|≤4κ<2p. ρ_m exists for every m≤(p−1)/2. Chaining covers all of [g/2,κ+1] with no span limit. Empty runs get a nonzero even θ. |
| Lemma 11 | 212–216 | Correct. |
| Lemma 12 (m_T triple) | 217–237 | Correct. m_T is central and 3m_T≤N. The 27 lower sums are ≤M0+5 using Lemma 6(i)–(iii) and 2a′≥3κ+g. The upper sums are ≤2δ+5<B*+ν0+6. Hence Δ=2p. |
| Lemma 13 | 238–247 | Correct **with m1**: the run-addition step applies only for g/2≤m≤κ. Level κ+1 has G=g−1≥3 and is reached from level κ. |
| **Theorem UMR-F** | 24–28 | **Correct**, relative to the accepted imports, with m1. |
| Lemmas 14–19 | 252–305 | Correct. Lemma 14 is an identity in every frame. The n_S=κ case of Lemma 17(a) is impossible. Lemma 18's jumps need ≥p+5, ≥p+4 or ≥p+6 letters in runs of S, all excluded by the no-giant-pair hypothesis. |
| **Theorem UMR-P** | 29–31, 306–307 | **Correct at its exact hypothesis**: SOME frame of the NF satisfies UB(S_ev) ∧ UB(S_od). UB is a hypothesis and is never assumed. There is no circularity, because the frame fixes θ, N_S and P_S through UMR-F. |
| **Lemma 20** | 314–327 | **Correct only as a one-way necessary classification.** Boundary cases check out: n_S≤g/2 forces UB2; at n_S=κ the first alternative is impossible; the \|P_S′\|=κ alternative needs L(P_S′)=A^c and no empty run in S′∖P_S′. The "Moreover" clause holds (q′≤δ−ν0 at level κ+1). No converse is shown, and RES is not shown to exist. |
| LF328–330 | — | Withdrawn per m2. The replacement is verified: x_j(Q)=κ+2−j in Lemma 15(U) gives −e(S∖Q). |
| **Lemma FC** | 32–34, 311–313 | **OPEN.** It is not promoted anywhere. |
| Cells (7,17), (7,19), (8,19) | 335–356 | All instantiated constants re-derived. **OPEN at FC.** |

### Finding

**MINOR-1 (wording; no mathematical change).**
- **Step:** erratum m2 cites only LF328–330, but the same gloss survives elsewhere:
  - proof LF30–31: RES is "described by Lemma 20";
  - proof LF371: "The obstruction is the residual class RES";
  - package LF26–27: N_S is called "'A^c-saturated'".
- **Consequence for a reader:** they may take Lemma 20 as a characterisation of RES, or treat RES as a necessary obstruction. They may also assume saturation holds at every central level.
- **Minimal repair:** extend m2's reading to these loci:
  - Lemma 20 gives one-way necessary conditions only.
  - "A^c-saturated" means only the level-κ condition: q′(Q)≤δ−2 for every κ-superset Q of N_S, and q(Q)≤δ−2 for the P_S′ analogue.
  - "First failing" (LF8, LF309) is relative to this method.

### Reading of FC (not a finding)

Lemma 14 gives Ξ(S_ev)+Ξ(S_od)=e*≥0 in every frame, and a frame always exists. So FC is equivalent to the target itself. Restricted to RES, FC says exactly that no target-scope NF has all its frames in RES.

"First failing lemma" therefore means the first unproved step of this method. Nothing is shown false, necessary, or realised.

### Scope, quantifiers and separation

- **Premises:** all used at their literal scope:
  - NF LF28–43;
  - GRX LF18–19, if-direction only (its convention source, GRX LF9, is outside the packet; only the literal criterion is used);
  - SC0;
  - ZSTRUCT and FB in (S′);
  - the (S1) definition;
  - the LOWER erratum conventions.
- **Excluded premises:** none of FQW, TCW, P7L, FCW, SCW, USK, PL, S1(a) or FB-E appears as a premise.
- **Frame quantifiers (preserved):**
  - A surviving avoider needs EVERY frame of EVERY target-scope NF to lie in RES; the failing alternating set may differ between frames.
  - UMR-P needs only SOME frame meeting both UB conditions.
  - No UB hypothesis is universal.
- **Correctness:** UMR-F, the conditional UMR-P and the one-way Lemma 20 are correct.
- **Completeness:** the target is not proved. FC is open on RES, and all three cells are open.
- **Process (erratum item 4):** the following are disclosed and have no mathematical effect. Preregistration is not assessed.
  - Pre-freeze unwritten arithmetic.
  - "Before any derivation" means before the written proof.
  - Six text replacements before file creation.
  - Inherited byte estimates.
  - By-eye manifest checking.
- **Priority:** none claimed or assessed.
- **Computation:** none, in either the proof or this review.
- **Not approved:** the whole target, any cell, full ordered Olson, runtime. These verdicts are written-review only, pending the parent verdict.

**Editorial (not counted):** several symbols are reused.
- q1: LF106 and LF222–223.
- x1, y1: LF188–189 and LF226–236.
- X: run sum (LF109), exterior (LF143, LF149) and offsets (LF184); "X_e" at LF208 is the run sum.
