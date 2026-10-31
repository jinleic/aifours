# f172 review v1 — corrected composite 121 (four-qubit depolarizing k3 regions and all-density |1−p| ≤ 1/200)

Reviewer: `ReviewF172DepolFresh`, a same-harness subagent. Wave: `f172-depolarizing-corrected-composite`. Manifest `manifest-v1.json`, SHA-256 `1fc2d5fc1c49575969daf20c06f3963eb32e637b620736d3190b7de43975acb9` (verified). Native clock observed before composing this file: **2026-10-29T08:03:48-0700 PDT**. This is not the creation time of any other file.

This is a fresh prospective review of the fully corrected composite. I did not open the earlier f155 review, and I know of it only through the parent note's one-sentence summary. I executed no author code. This review is **not** a human, independent-model-family, formal/kernel or novelty verification. It confers no acceptance, and the parent decides the disposition.

## 0. Verdict summary

- **FATAL: none. MAJOR: none.** I found five MINOR items: three wording or scope items, each already corrected by the errata or the parent note, and two presentation items that are new in this review. None is an error in a load-bearing calculation.
- **Regional branch.** The claim covers P, U, D_p and H; the finite convex hull at fixed p; and every p in [0,4/3] via (6). I reconstructed every load-bearing step, and it is written-supported at this same-harness level. Class H and class D_p are defined by hypotheses; (9) is **not** asserted for all pure states.
- **All-density branch (§§7–9).** The claim is that (2) holds for every four-qubit density whenever `t=|1−p|≤1/200`, i.e. exactly for `199/200 ≤ p ≤ 201/200`. I independently reconstructed the whole argument for all complex amplitudes and all `0<t≤1/200`, including:
  - the corrected weight-three conjugation;
  - the all-variable Hessian blocks;
  - stationarity;
  - the §7→§8 bridge identity, which the candidate uses but never writes out;
  - the remainder and block-separation constants;
  - the tube/far overlap;
  - the t=0 and η=0 endpoints;
  - the t-preserving reflection.

  This branch is written-supported at this same-harness level.
- **Not supported; no claim preserved:**
  - all-density (2) at p=4/3, or at any p with |1−p|>1/200. The §9 sentence "including p=4/3" is wrong for this branch, and the parent note is right;
  - original/global k3 outside the stated regions;
  - any other prefix;
  - full majorization;
  - novelty.

## 1. Actual source order and input verification

Before reading any input, I verified all eight inputs in one batch against the manifest's SHA-256, byte count and LF count. All matched.

| Order | Input (manifest role) | SHA-256 (verified) | bytes / LF | How read |
|---|---|---|---|---|
| 0 | `manifest-v1.json` | `1fc2d5fc…acb9` | 5081 / – | complete raw read; its hash was checked in the same parallel batch, clock 07:16:37 PDT |
| 1 | erratum 125 (source clock) | `1922f5bd…580c8c` | 2692 / 33 | complete raw |
| 2 | erratum 127 (fixed-Q equality) | `a19cf2ac…4de9c6` | 2699 / 21 | complete raw |
| 3 | erratum 128 (prior-prefix scope) | `873390c3…af285` | 2839 / 25 | complete raw |
| 4 | erratum 130 (exclusion bindings) | `e1b3c3a3…6b001` | 2342 / 28 | complete raw |
| 5 | erratum 133 (weight-3 conjugation) | `237a9e74…41c453` | 2403 / 14 | complete raw |
| 6 | parent reflection scope note | `c8795540…29f958` | 1392 / 11 | complete raw |
| 7 | f130 scope-only framework | `cdda493b…b38d` | 5579 / 37 | complete raw |
| 8 | candidate `frontier-20261028-121-consolidated-physical-k3.md` | `91643ea8…5c36b` | 25795 / 427 | complete raw reads of lines 1–140, then 141–290, then 291–427 |

Source-order facts:
- **Parallel fetches.** Inputs 4, 5 and 6 were fetched in one parallel tool batch, issued and returned in declared order. Candidate chunks 141–290 and 291–427 were also fetched in one parallel batch, in order. In every case the errata, the parent note and the framework were completely read before any candidate byte was opened.
- **Timing.** The only clock observed during the reading interval is 07:16:37 PDT (the manifest check). The next observed clock, 07:42:00 PDT, came from a tool-availability command issued after the reads. Reading therefore ended before 07:42:00. I started the mathematical reconstruction only after all 427 candidate lines had been read.
- **Files not opened.** I did not open any file referenced inside the inputs: the §10 dependencies and checkers, 105/106/109/110, the prior k2/k4 dispositions, the f130 sub-links, or f155.

## 2. Claim-by-claim verdicts and dependencies

"VERIFIED" means the load-bearing step was reconstructed independently by me, with no finding. Controls (§6) are instance checks only.

| ID | Claim (location) | Verdict | Explicit load-bearing dependencies |
|---|---|---|---|
| C1 | (1) `R3=a⁴+2a³b`, `16R3=3+8t+6t²−t⁴`; the reference spectrum depends only on t=\|1−p\| (§1) | VERIFIED | `Φ_p(\|0⟩⟨0\|)` has spectrum {a,b} on both sides of p=1 |
| C2 | (3) erasure expansion; product layer traces (1,3,3,5/4,3/16), whose weighted sum is R3; nonnegative coefficientwise comparison for 0≤p≤1; T3 top-three sum `(12+L)/16≤5/4`, also for mixed ρ (§2) | VERIFIED | `Φ_p=(1−p)id+pE` with p∈[0,1]; Q₀ is the top-three eigenprojector of the reference output |
| C3 | (4) `T1=ρ+F/4`, `4T2=H1+ρ+ρ̃+F/2−I`; (5) is sufficient for the same input and every Q (§2) | VERIFIED | full spin flip `=⊗(2E_i−id)=Σ(−1)^{4−m}2^mT_m`; `8T3=H1`; `16T4=I` |
| C4 | (6) reflection for 1≤p≤4/3: same input; actual complex `Q↦Y⊗⁴QᵀY⊗⁴`, a rank-3 projector; reference preserved (§2) | VERIFIED | `YXᵀY=Tr(X)I−X`; `Tr(Q·Y⊗⁴AᵀY⊗⁴)=Tr(Y⊗⁴QᵀY⊗⁴·A)`; (6) maps t↦t |
| C5 | §3: `M(σ)≥σ≥0`; (7); λ₁≤4; branch s≥1 | VERIFIED | Schmidt 2×2 PSD block; `σ_i=I−ρ_i`; rank-one interlacing |
| C6 | §3 branch s=0 ("equality by class P") | **MINOR (wording)**. Erratum 127's inequality reading is correct; only the inequality is needed | class P (Ky Fan) |
| C7 | §3 branch 0<s<1: marginal polygon; a_x≥0; `a_x=0⇒P_x=0`; two-way Schur equivalence (9), equality allowed | VERIFIED | union bound for commuting projectors and its equality case; Haynsworth inertia additivity; rank-one PSD criterion |
| C8 | (10): equal radii are a full subcase of (9) | VERIFIED | constraints `ΣP_h=1`, `ΣhP_h=s` on the actual amplitudes |
| C9 | §4: purity/flip moments, `A2=2+S+4C`, (11), Cauchy–Schwarz ⇒ `K3(F)≤8` under `4S+8C≤64/9`; class H | VERIFIED | F and the 12×12 Gram share nonzero spectrum; `f(x)=x²/3+(12−x)²/9` increases for x>3 |
| C10 | §5: class U and gap (12), with p'=min(p,2−p) | VERIFIED | Schmidt coefficients 1/√2 ⇒ spectrum of E_i(ρ) is (1/4)⁴; `T3=I/4`; spin-flip identity |
| C11 | §6: (13), (14), class D_p for nonnegative t, including p>1 via (6) | VERIFIED | Ky Fan for `Σr_i·σ_i` (=L); Parseval constants 39 and 15−S; `t^k≤t²` |
| C12 | (2) on the finite convex hull of P∪U∪D_p∪H at fixed p | VERIFIED | fixed-Q linearity in ρ; each component bound holds for every Q at that p |
| C13 | §7 gauge (15): maximizer exists, m>0, complex stationarity removes the weight-one amplitudes | VERIFIED | first variation in each local factor; `⟨π\|ψ⟩≠0` |
| C14 | §7: blocks (16), covariance decoupling, (17), (18), (20), (19), (21) for all complex v and 0<t≤1/200 | VERIFIED. **MINOR (explanatory)**: the sentence after (19) is wrong as written (erratum 133); (18) itself is right | matrix-unit rules; ‖v‖=1; K₂ sublinear and monotone |
| C15 | §8 (22)–(27): tube bound `R3−K3(Λ(ρ))≥tη²/32` for 0<η≤9/40 | VERIFIED. **MINOR (presentation)** M4, M5 | bridge identity `Q₀₀=(16/t)A`, `Q_{wt1}=(16/t)M` (§3.6; not written in the candidate); Taylor remainder; (26); Cauchy interlacing; Weyl |
| C16 | §9 far region η≥9/40 via (14) | VERIFIED | product of majority eigenvectors plus the union bound; `δ−Σ(1−r_i)=4−2r₃−2r₄≥0` |
| C17 | §9: η=0 (product); t=0 (output I/16); mixing at fixed Q | VERIFIED | no division by t anywhere at t=0 (§3.7) |
| C18 | §9: "(6) then covers the negative-shrink physical half, including p=4/3" (all-density branch) | **MINOR (scope wording); the sentence itself is incorrect.** Reflection covers only 1≤p≤201/200. The parent note is right | (6) preserves t |
| C19 | Combined all-density theorem, (2) for every density when t≤1/200 (§1 statement) | VERIFIED as written-supported for **199/200≤p≤201/200** | C2–C4, C11, C13–C17 |
| C20 | Erratum 127: counterexample, replacement interpretation, endpoint completion at p=0 and p=1 | VERIFIED | identity channel; Ky Fan equality characterization |
| C21 | Errata 125, 128, 130 (documentary clock, prior-prefix scope, nonpremise bindings) | NOT ASSESSED beyond reading. The referenced files are outside the manifest. No step of my reconstruction depends on them | – |

## 3. Reconstruction of the load-bearing steps

Throughout, `0≤p≤1`, `t=1−p`, `a=(1+t)/2`, `b=(1−t)/2`, `λ_h=a^{4−h}b^h`. The case p>1 is reached only through (6).

### 3.1 Reference, layers, reflection (§§1–2)

- **Reference.** `16R3=(1+t)³(3−t)=3+8t+6t²−t⁴`. For p≥1, `Φ_p(|0⟩⟨0|)=diag(1−p/2,p/2)=diag(b,a)`, so the same formula holds with t=p−1.
- **Layer traces.** For `Q₀=span{0000,1000,0100}` the layer traces are 1, 3, 3, (2+2+3+3)/8=5/4 and 3/16. Q₀ is the top-three eigenprojector of `Λ_p(|0000⟩⟨0000|)`, so `Σ(1−p)^{4−m}p^m·(1,3,3,5/4,3/16)_m=R3`.
- **T3.** `T3=(1/8)Σ_l I_{\bar l}⊗ρ_l` is diagonal in the product eigenbasis with entries `(4+Σε_l r_l)/16`. Its top three entries are: all signs +, then the smallest radius flipped, then the second smallest flipped. They sum to `(12+L)/16`.
- **(4).** Each `E_i` is the local Pauli twirl, giving the T1 identity. The full spin flip is `⊗(2E_i−id)`, which gives `ρ̃=ρ−2T1+4T2−8T3+16T4`.
- **(6).** `YΦ_{2−p}(X)ᵀY=(1−p)X+(p/2)Tr(X)I`. Moving the transpose onto Q gives `Tr(QΛ_pρ)=Tr(Y⊗⁴QᵀY⊗⁴·Λ_{2−p}ρ)`; the sign `(−1)⁸` from `Yᵀ=−Y` cancels. The map is a bijection of rank-three projectors for complex Q. Since |1−p|=|1−(2−p)|, **(6) never changes t**.

### 3.2 Spin-flip criterion (§3) and the equal-radii subcase

- **`M(σ)≥σ`.** Write `φ=√λ₀e₀f₀+√λ₁e₁f₁` across i|rest. On span{eₖf_l}, the operator `I⊗σ_i−σ/2` has the 2×2 block `[[λ₀/2,−√(λ₀λ₁)/2],[·,λ₁/2]]`, whose determinant is 0 and whose diagonal is nonnegative. Summing over the four sites gives `H1(σ)≥2σ`.
- **(7).** Since `σ_i=I−ρ_i`, we have `H1(σ)=4I−H1(ρ)`, which gives (7).
- **Branch s≥1.** `D=H1(σ)` is diagonal with `D_x=Σ_i(x_i?p_i:1−p_i)`, and its minimum is `D_{1111}=s`. So `D−I≥0`, and subtracting the rank-one σ leaves at most one negative eigenvalue.
- **Branch 0<s<1.**
  - *Polygon.* For pure σ, `λ_max(σ_{\bar i})=1−p_i`. With the union bound this gives `1−Σ_{j≠i}p_j≤⟨⊗_{j≠i}|0⟩⟨0|⟩≤1−p_i`, hence `2p_i≤s<1`, and the local axes are nondegenerate.
  - *Signs of a_x.* `a_x=D_x−1` is positive at weights 0, 1 and 2, and equals `s−2p_i` at the word missing i.
  - *Zero entries.* If `s=2p_i`, the union bound is tight. Then `⟨Σ_{k≥2}(k−1)Π_k⟩=0` for the commuting minority projectors of the other three sites, so the probability of three minorities among them is 0, i.e. `P_x=0` for that weight-three word.
  - *Schur step.* The pivot `N_{1111,1111}=s−1−q₄<0` is negative, so Haynsworth gives `In(N)=In(pivot)+In(S)`. The Schur complement is `S=diag(a)−[(1−s)/(1−s+q₄)]φ'φ'†`: the coupling `β=−\bar φ_{1111}φ'` contributes `q₄φ'φ'†/(1−s+q₄)`. On supp(a), `S≥0` iff `W≤1+q₄/(1−s)`; the zero-a rows of S vanish.
  - *Conclusion.* λ₂(M)≥1 ⟺ (9), in both directions, with equality allowed. Then `K3(H1+ρ̃)≤4+3+3`.
- **Equal radii.** The a_x by weight are `3−s`, `2−s/2`, `1`, `s/2`. Eliminate `P₀` and `P₃` with the two constraints. The constant term is `1/(3−s)−1+sK=0`, and the P₃ coefficient is `2/s−1/(3−s)=3K`. This yields exactly the displayed reduced form, with `a₁=Ks/(4−s)` and `a₂=sK`, so every coefficient is ≤0 for 0<s<1.

### 3.3 Frame moment, class H (§4)

- **Moments.** Equating the purities of the complementary 1|3 splits gives `4+3S+2A₂+A₃=16+4S`, i.e. `A₃=12+S−2A₂`. Total purity gives `A₄=3−2S+A₂`. Under the flip, `⟨P⟩_ρ̃=(−1)^{|P|}⟨P⟩_ρ`, so `16C=Σ(−1)^jA_j`, which yields `A₂=2+S+4C`.
- **Gram Frobenius sum.** The 12 diagonal entries give 12. Same-site pairs give `2r_i²` per site. Different-site pairs give `2A₂`. Together with the A₂ formula this is (11).
- **Cauchy–Schwarz.** `Tr F²≥x²/3+(12−x)²/9`, which equals 208/9 at x=8 and increases strictly beyond. So `4S+8C≤64/9` forces x≤8, including rank<12.
- **Class H.** Combining (5) and (3): `TrQT1≤3` and `TrQT2≤3` for the same Q, so class H holds.

### 3.4 Class U, class D_p, hull (§§5–6)

- **Class U.** The bounds are `TrQT1≤4·3/4` and `TrQT3=3/4`; the spin-flip identity gives `4TrQT2≤1+6+6−3`. The layer-2 and layer-3 gaps of 1/2 give `½p²(1−p)²+½p³(1−p)=½p²(1−p)`.
- **Class D_p.**
  - *Expansion.* `Λ_{1−t}(P)=t^{|P|}P`, so the weight-one term is at most `tL` by Ky Fan.
  - *Remainder.* Cauchy–Schwarz with `Σ_{P≠I}Tr(QP)²=48−9=39` and `Σ_{|P|≥2}c_P²=15−S` bounds the rest by `t²√(39(15−S))`.
  - *Conclusion.* `16R3≥3+8t+5t²` then gives (14).
- **Hull.** At fixed p the hull follows by fixed-Q linearity.

### 3.5 §7: gauge and the all-variable Hessian (special-attention items)

**Stationarity.** Varying a local factor `π_i→π_i+εξ` with ξ⊥π_i changes `|⟨π|ψ⟩|²` at first order by `2Re(\overline{⟨π|ψ⟩}·ε̄⟨ξπ'|ψ⟩)`. At a maximum this vanishes for all complex ε, and m>0, so `⟨e_i|ψ⟩=0` after rotating the maximizer to |0000⟩. Hence (15) holds.

**Matrix units** (valid for any complex v supported on weights 2–4):

- `V_{k0}=t^{|k|}a^{4−|k|}v_k`, so `V_{(\bar i),0}=at³g_i` and `V_{(ij),0}=a²t²c_ij`.
- `V_{(e_i),k}=t^{|x|}b a^{3−|x|}\bar v_x` for `k=x+e_i` (i∉x), and 0 otherwise. Hence **`V_{(e_i),1111}=bt³\bar g_i`** and `V_{1111,(e_i)}=bt³g_i`. This is exactly the orientation stated by erratum 133.
- `W_{00}=Σ|v_x|²λ_{|x|}−λ₀`.
- `W_{e_ie_j}` (i≠j) pairs only `x=y+e_i−e_j`, with coefficient `t²·Π(a or b)`.

**Covariance and decomposition.** Phase covariance under `⊗diag(1,e^{iθ})` forces `|x|−|x'|=|y|−|z|`. So in A (rows/columns at weight 0) and in M (weight 1), only same-weight amplitude pairs survive; for virtual terms, k has weight |x|+1 on both sides. Because ‖v‖=1, the terms −λ₀ and −λ₁ split by the weight shares `w_h=‖v_h‖²`, giving `A=Σw_hA_h` and `M=Σw_hM_h`.

**Weight 2.**
- Diagonal: `W_ii=n_ia³b+(1−n_i)ab³−a³b=−abt(1−n_i)`.
- Off-diagonal: `W_ij=abt²Σ_l c_il\bar c_jl=abt²Γ_ij`.
- Virtual (gap `λ₁−λ₃=abt`): `abt³(1−n_i)` on the diagonal and `abt³Γ_ij` off it.
- Sum: (17). Also `K=tΓ+(1−2t)diag(n)≥0` and `Tr K=2(1−t)`, so `K₂(M₂)≤0`. Finally `A₂=−a²t+a⁴t⁴/(a²t)`.

**Weight 3.**
- Diagonal: `W_ii=|g_i|²b⁴+(1−|g_i|²)a²b²−a³b=−a²bt−b²t|g_i|²`.
- Off-diagonal: `W_ij=t²b²\bar g_i g_j`.
- Virtual (gap `λ₁−λ₄=btD₃`): `bt⁵\bar g_ig_j/D₃`, with the **same** orientation.
- Sum: (18) with `\bar g\bar g†` (entries `\bar g_ig_j`).
- Weight-0 part: `A₃=−atD₃+at⁵/D₃`.

**Weight 4.** `M₄=−abtI` with no virtual term, since weight 5 does not exist, and `A₄=−tD₄+t⁷/D₄`.

**Bound (19).** Drop the negative diagonal and use `K₂(c\bar g\bar g†)=c` (since ‖g‖=1). This gives `A₃+K₂(M₃)≤−atD₃+at⁵/D₃−2a²bt+t²b²+t⁵b/D₃`. Multiplied by `32D₃`, this equals `−t(1−t)(15+24t+38t²+32t³+3t⁴)` as a polynomial identity (degree 6; I checked it at 11 points, and the mutation 38→37 is detected).

**Orientation-independence.** (19) uses only the trace of the rank-one term, so it would be unchanged under either orientation. The explanatory sentence therefore cannot affect (19) or (21).

**Bound (21).** The three margins are `a²(1−t²)>15/64`; `(15/32)(1−t)>15/64`, using poly ≥15 and `D₃≤1`; and `1−2t⁶>15/64`, using `D₄≥1/2`. K₂ is sublinear and Σw_h=1, which gives (21).

### 3.6 §8: normalized conjugation, including the bridge identity

- **Normalized operators.** `H_t(X)=Σ_{P≠I}Tr(XP)t^{|P|−1}P` is polynomial in t. D is diagonal with `d_h=((1+t)^{4−h}(1−t)^h−1)/t`. The gaps are `d₀−d₁=2(1+t)³≥2` and `d₁−d₂=2(1+t)²(1−t)≥2`, the latter because `t(1−t−t²)≥0`. Also `‖D‖=d₀<5`.
- **Rescaled perturbations.** `V_H=16V/t` and `W_H=16W/t`, since both arguments are traceless.
- **Frobenius bounds.** Parseval gives `‖V_H‖_F²=16Σ_{|P|≥2}Tr(XP)²t^{2|P|−2}≤512t²<(23/200)²`; there are no weight-one terms because v has no weight ≤1 support. The same bound holds for `W_H−W₀`, because the weight-one Pauli part of `W_H` is exactly `W₀` (and `‖|v⟩⟨v|−|0⟩⟨0|‖_F²=2`).
- **Generator S₁.** The divided gaps across the blocks are ≥2, so `‖S₁‖_F≤‖V_H‖_F/2<23/400`.
- **Bridge (used in §8 but not written in the candidate).** In row/column 0 and in the weight-one rows, V_H is entirely off-block. So:
  - `[V_H,S₁]₀₀=2Σ_k|(V_H)_{k0}|²/(d₀−d_k)`;
  - `½[[D,S₁],S₁]₀₀=−½[V_off,S₁]₀₀=−Σ_k|(V_H)_{k0}|²/(d₀−d_k)`;
  - hence `Q₀₀=(W_H)₀₀+Σ_k|(V_H)_{k0}|²/(d₀−d_k)=(16/t)A`, and identically `Q_{e_ie_j}=(16/t)M_ij`.

  This is what licenses "the rescaled leading blocks (16/t)A, (16/t)M".
- **Taylor step (25).** `f(τ)=e^{−τS}Xe^{τS}` satisfies `‖f^{(k)}‖=‖ad_S^kX‖≤(2‖S₁‖)^k‖X‖`. Three remainders are kept: order 3 for D, order 2 for hV_H, and order 1 for η²W_H. With h≤η and the conservative tail factor `e^{2hs₁}≤e^{2ηs₁}<1/(1−207/8000)<103/100`, this gives coefficient `580473701/600000000<1`. Writing `h²=η²−η⁴` produces the `−η⁴B` term.
- **Norm bounds (23) and (24).**
  - `‖B‖_F≤3‖V_H‖_F‖S₁‖_F<0.0199`; the cruder route `2‖V_H‖‖S₁‖_F+2‖D‖‖S₁‖_F²<0.0463` also works. Either way `‖B‖_F<47/1000`.
  - `‖Q‖<163/20+47/1000<41/5`.
  - off(W₀) is **exactly** the compression of the transverse `G=Σ(r_{ix}X_i+r_{iy}Y_i)` to weights ≤2. So `‖off Q‖<4+23/200+47/1000<21/5`.
- **Block bound (26).** It holds for **every** g>0, because the difference is the Gram matrix of `[B₀/√g;−√gI]`. The gap condition is needed only to place `D₀+gI` below `λ_min(A)I`.
- **Separations.** `‖H_*−D‖≤441/1000`, so Weyl applied to compressions gives both separations `>2−0.882>11/10`. This holds even if the weight-one block is degenerate.
- **Combining.** Cauchy interlacing gives `K3(H_*)≤λ₁(H_*)+K₂(C)`. Then `λ₁(H_*)≤d₀+η²Q₀₀+‖B₀‖²/g` and `K₂(C)≤2d₁+η²K₂(Q₁₁)+2‖B₁‖²/g'`, where `‖B_•‖≤η²‖off Q‖`. Hence `K3(H_*)≤K3(D)−(15/4)η²+3(21/5)²η⁴/(11/10)`, and with the error terms `K3(H)≤K3(D)−(15/4)η²+(54870831/17600000)η²<K3(D)−η²/2`. Since `R3−K3(Λρ)=t(K3(D)−K3(H))/16`, this is (27).

All constants are uniform over the complex normal sphere and over 0<t≤1/200.

### 3.7 §9: far region, endpoints, coefficient division, reflection scope

- **Far region.** The majority-eigenvector product state and the commuting union bound give `m≥1−Σp_i`, i.e. `η²≤½Σ(1−r_i)≤δ/2`. So η≥9/40 forces `δ≥81/800`. Since `√585−5<20`, we get `t(√(39(15−S))−5)<20t≤1/10<81/800`, and the bracket in (14) is positive. The tube (η≤9/40) and the far region (η≥9/40) overlap at the boundary.
- **Endpoints.** η=0 is class P.
- **Coefficient division at t=0.** The t=0 case is separate: the output is I/16, with equality for every Q. No formula divides by t there. The §7 denominators `λ₀−λ_h` are positive for t>0. In the normalized frame the divided gaps are ≥2, independent of t. `(16/t)A` and `(16/t)M` are finite. (12) and (14) multiply by p or t; they never divide.
- **Mixing.** Average over a finite spectral decomposition at fixed Q.
- **Reflection scope.** (6) carries each p'∈[199/200,1] to p=2−p'∈[1,201/200] at the same t. It cannot reach p=4/3, where t=1/3. The regional classes reach p=4/3 only under their own hypotheses, e.g. D_{4/3} with t=1/3.

## 4. Findings

| # | Severity | Location | Finding | Explanatory or load-bearing? |
|---|---|---|---|---|
| M1 | MINOR (scope; sentence incorrect) | §9, mixing paragraph | "Equation (6) then covers the negative-shrink physical half, including p=4/3" is false for the all-density branch. The correct coverage is 1≤p≤201/200, as the parent note says. | Not load-bearing for the §1 theorem statement, which is correctly restricted to t≤1/200. **No all-density p=4/3 claim is preserved.** |
| M2 | MINOR (explanatory) | §7, after (19) | "V_(i,1111)=bt³ times the corresponding g" must read `bt³\bar g_i` (erratum 133). | Explanatory only. (18) correctly displays `\bar g\bar g†`, and (19) is orientation-independent. |
| M3 | MINOR (wording) | §3, s=0 | "equality by class P" must read "inequality (2) holds for every Q" (erratum 127). | Not load-bearing; the branch needs only the inequality. |
| M4 | MINOR (presentation) | §8 | The identities `Q₀₀=(16/t)A` and `Q_{wt1}=(16/t)M`, which connect (21) to the K3 estimate, are used but not derived. The split `A=ΣA_h` silently needs ‖v‖=1. | Load-bearing step, but **correct**; reconstructed in §3.6 and exact-checked (T7.Qblocks). |
| M5 | MINOR (presentation) | §8 constants | The derivations of `‖B‖_F<47/1000`, (24) and the cubic coefficient are compressed: the three terms come from D at order 3, from hV_H at order 2 and from η²W_H at order 1, using `‖V_H‖≤‖V_H‖_F`. The displayed `exp(2η‖S₁‖)` is a valid upper bound for the tail factor `exp(2h‖S₁‖)` because h≤η. The integral form of the remainder would not need the factor at all. | Every displayed constant verified exactly, with room to spare. |

The errata record three documentary items: 125 (clock attribution), 128 (an over-broad "every unaddressed prefix" nonclaim) and 130 (missing 110/105/109 bindings). I read them but did not assess them; they are provenance/scope statements about files outside this manifest.

## 5. Dispositions of the mandatory errata and the parent note

- **125.** Read first. A documentary clock qualification with no mathematical content; I did not verify it.
- **127.**
  - The counterexample is exact: at p=0, `Tr=0<R3(0)=1`, while Q₀ attains equality.
  - The replacement interpretation is correct: equality holds iff Q is a top-three Ky Fan maximizer, with the cutoff-eigenspace description.
  - The endpoint completion is correct:
    - at p=0, `Tr(Qρ)≤1` for every density, with equality iff `supp ρ⊆range Q`;
    - at p=1, every Q gives 3/16.
- **128.** Read. A documentary scope correction. I did not open the prior k2/k4 dispositions and make no statement about them. The f130 framework itself states that it does not establish k3.
- **130.** Read. Nonpremise bindings only. No step of my reconstruction uses 105/106/109/110, and I opened none of them.
- **133.** Correct. I derived the orientation independently (§3.5) and reproduced the exact witness `V_(1,1111)=−199i/3200000000` at t=1/200 for v=i|\bar1⟩. The unconjugated sign is detected (T5.err133.witness and its mutation).
- **Parent note.** Correct (C18, and T4.interval).

## 6. Independent controls (reviewer-authored; bounded; no author code)

Both scripts were written by me, use the standard library (exact) or numpy (float) only, and read no author files. Receipt: `reviewer-controls-v1.receipt.json`.

**Exact controls.** Script `reviewer-exact-controls-v1.py` (SHA-256 `d10eaf63e4c53c02e26fda918b0ac2c5ba10791c00923eb0ba449e6ce6667934`), run `python3 -B` 07:59:00–07:59:06 PDT, exit 0. Result `reviewer-exact-controls-v1.result.json` (`fd68facea9055dea4dc2854afcda3cc2fca9df647c3ad7a2d5336a58d59790a6`): 70 exact checks, all with the expected outcome. Highlights:

- *Univariate polynomial identities* (checked at 11 points, more than each degree), positive: (1); the layer sum equals R3; the d_h gaps; (19); (20).
- *Weight-three complex phases.*
  - Positive: (18) holds with `\bar g\bar g†` for `g=(2+i,1+2i,−2+i,1+3i)/5` at t=1/200 and t=2/7; the entry identities of erratum 133 hold; the coupling goes only to weight 4.
  - Negative, each detected: the `gg†` orientation; the unconjugated `V_(i,1111)`; the wrong-sign erratum witness.
- *Weight two and weight four.* Positive: (17) with complex `c` and `Γ=TT†`; `K≥0` by exact inertia; `Tr K=2(1−t)`; (20) with phase `(3+4i)/5`. Negative, detected: `Γ→T†T`.
- *Mixed weights.* For a mixed complex normalized v on weights 2, 3 and 4: positive, cross-weight terms vanish exactly and `V` vanishes on the weight-0/1 blocks; negative, the mis-oriented sum is detected.
- *§8 for the mixed v at t=1/200.* Positive: S₁ is anti-Hermitian and satisfies `V_off+[D,S₁]=0`; `Q₀₀=(16/t)A` and `Q_{wt1}=(16/t)M` hold exactly; the instance Frobenius bounds hold; off(W₀) equals the compression of G to weights ≤2; (22) holds at η=9/41. Negative, detected: dropping `½[[D,S₁],S₁]`.
- *Reflection, complex density.* Using an exact complex Cayley-built rank-3 projector, at p∈{201/200,7/6,4/3}: positive, (6) holds and t is preserved, and Parseval gives 39; negative, detected: dropping the transpose on Q, and dropping it on the output. The interval check confirms that only 199/200≤p≤201/200 meets t≤1/200.
- *Spin flip and frame, complex pure state.* Positive: (4); the flip expansion; (7); `M−σ≥0`, positive definite with inertia (16,0,0); the moment identities; (11). Negative, detected: the flip without transpose.
- *Criterion (9).* Positive, with exact inertia of `M−I`:
  - an even-weight state with s=11/50: (9) holds and the inertia is (15,1,0);
  - equal radii: equality W=1 and inertia (14,1,1), so a zero eigenvalue is allowed;
  - unequal radii: W=79/90 and inertia (15,1,0).

  Negative, detected: an abstract violation, W=36/5 with inertia (14,2,0); and a support mutation where a_x=0 but P_x≠0, which passes the W-test yet gives two negative eigenvalues, showing that `P_x=0` is load-bearing.
- *Constants and interval edges.* Positive: all §7–§9 constants, including `580473701/600000000`, `441/1000` and `54870831/17600000<13/4`. Negative, detected: the 23/200 constant fails at t=1/196, and the far margin fails at t=1/190.
- *Erratum 127 and (10).* Positive: the p=0 witness and the equality case; the (10) reduction. Negative, detected: the wrong-K mutation.

**Float sanity.** Script `reviewer-float-sanity-v1.py` (`b9f5b17a7a5f2eaf04ae0da194f070d9e074c828d67f0beb1cdc68688525d431`), run 07:59:06–07:59:10 PDT, exit 0. Result `f7c615ce185993ab0e0ef6716ee0e0518c4dcb60276f8d36c6c256a09d60f794`. This is non-exact, non-proof sampling with seed 20261029:
- Tube (27): 450 samples, minimum of gap/(tη²/32) ≈ 10.5.
- Reflection: K3 difference between p and 2−p at most 2.8e-16.
- (21): 400 samples, maximum of (A+K₂M)/t ≈ −0.337, against the bound −0.2344.
- All-density at t=1/200 and p=1±t: 810 evaluations, minimum R3−K3 = 0.0, attained by the product state.

These checks only probe for gross contradictions; they prove nothing.

**Development runs.** Two stdout-only development runs preceded the receipted runs (details in the receipt). No result file was written by either.

## 7. Boundaries, imports, conditional premises and process facts

- **Imports.** Only standard facts: Ky Fan; Weyl and Cauchy interlacing; Haynsworth inertia additivity; the rank-one PSD criterion; Schmidt decomposition; Pauli Parseval; the union bound for commuting projectors; compactness. The controls additionally use Faddeev–LeVerrier, Descartes' rule for real-rooted characteristic polynomials, and the Cayley transform.
- **Conditional premises.** Class H requires (9) or s∈{0}∪[1,∞) as a hypothesis. D_p is defined by its inequality. The all-density statement holds only for t≤1/200.
- **Not reviewed:**
  - §10's dependency and helper tables, every checker, and the 74 audit;
  - packets 01–120;
  - the 105/106/109/110 obstructions;
  - the f130 sub-documents;
  - the prior-round dispositions;
  - f155;
  - the provenance and clocks of the source tables.
- **No inference.** Nothing here supports any formal, family, novelty, priority or operational conclusion.
- **Process facts.**
  - No author code was executed. No file outside this wave directory was written.
  - I used no Git, web search, external model or author contact. Nothing was deleted, published or changed in infrastructure.
  - The frozen candidate bytes are unchanged.
  - During the work, Main sent two status-only notices, about f162 and f161 holds. I never accessed any of those materials.
  - All clocks above are actual `/bin/date` observations.

## 8. Files created by this reviewer in this wave directory

- `reviewer-exact-controls-v1.py` — `d10eaf63e4c53c02e26fda918b0ac2c5ba10791c00923eb0ba449e6ce6667934`
- `reviewer-exact-controls-v1.result.json` — `fd68facea9055dea4dc2854afcda3cc2fca9df647c3ad7a2d5336a58d59790a6`
- `reviewer-float-sanity-v1.py` — `b9f5b17a7a5f2eaf04ae0da194f070d9e074c828d67f0beb1cdc68688525d431`
- `reviewer-float-sanity-v1.result.json` — `f7c615ce185993ab0e0ef6716ee0e0518c4dcb60276f8d36c6c256a09d60f794`
- `reviewer-controls-v1.receipt.json` — `0a0b38413e73c03af756c1d18ea4d27f6edd841364cd5b19268aad4df5aaf9dd`
- `review-v1.md` — this file. Its own SHA-256 is reported in the return message and cannot be self-contained.
