# Review f285-werner-arbitrary-2plus2 — review-v1

Reviewer: ReviewF285Blocks (same-harness written review; not human, not independent-family, not formal/kernel, not novelty verification, no original-target closure).

## 0. Process and read receipt

- Manifest `manifest-v1.json` SHA256 `7f0263a7eb764d8a2d1e8f9cccd80bce9b943e48029cba0f9c79b5df93ea9c81` (4103 B, 53 LF) — read; matches task SHA.
- Freeze receipt `freeze-receipt-v1.json` SHA256 `8434a8dd0a552dc18216e03a3fc3150a8bd4d65c5473adbe9a7612a8f1f81e3f` — read; matches task SHA.
- Packet `literal-packet-v1.md` independently re-hashed this session: SHA256 `067ec4f77642896e3e361f7371c4fe0d6cff67a9bb204f740123b31aa6dd89a8`, 10653 B, 134 LF — matches freeze receipt exactly.
- Input S1 `frontier-20261029-d4-t2-arbitrary-2plus2-blocks-v1.md` independently re-hashed: SHA256 `bb09c6bf442b9d497241297c57f9da678b559b5d13ee56cc871de4a6fc7f1473`, 9802 B, 132 LF — matches manifest and freeze receipt.
- Pre-body administrative ACK sent to Main before any mathematical body read.
- Status-only controls read as authority/status only (no mathematical payloads followed): `contract-addendum-2-frontier-first-owner-direction-v1.json` (5e18c2d4…), `parent-physics-selected-vector-authority-and-cadence-reconciliation-20261030-v1.json` (2a15d523…), `parent-L1-selected-diagnostic-release-quarantine-v1.json` (ba6b4bb9…).
- Packet read coverage: COMPLETE. Raw windows `:raw:1-20`, `:raw:21-40`, `:raw:41-60`, `:raw:61-80`, `:raw:81-100`, `:raw:101-120`, `:raw:121-134`, i.e. packet lines 1–134 = source lines S1|1–S1|132 (packet line = source line + 2 header lines). Windows are contiguous with no gap and no elision marker was encountered; the final window ends on the last source line S1|132. No truncated or unread line is certified.
- Scientific mode: WRITTEN_ONLY. No computation, code, CAS, enumeration, selected instance, author script, sibling review, network, or model output was used. All reconstructions below are hand derivations from the packet text. f198's arbitrary-T assertion was NOT imported (it is false and withdrawn per S1|25/S1|130); the two-qubit lemma (2.1) was re-proven from scratch below. f215/f274/f281 are treated as historical scope labels only.
- Checkpoint clock: `/bin/date` = Fri Oct 30 03:17:29 PDT 2026 (metadata verification, within cadence).

## 1. Verdict summary

**Theorem (S1|11: for traceless A,B ∈ M4(C), each separately unitarily similar to a 2+2 direct sum of arbitrary complex 2×2 blocks, S2(A⊗I4+I4⊗B) ≤ 2(||A||_F²+||B||_F²)): SUPPORTED.**

Counts: **FATAL 0, MAJOR 0, MINOR 3** (M1 wording "uniformly", S1|107; M2 understated slack, S1|103; M3 label-mapping unavoidably accepted as scope label, S1|13/S1|125). No proof repair was needed for correctness of the theorem; the two strictness wording items are non-load-bearing.

Per-claim table (LF = source line in packet `S1|n|`):

| # | Claim | LF | Verdict |
|---|---|---|---|
| C1 | Local-unitary invariance allows using the separate 2+2 reducing bases | 11 | SUPPORTED |
| C2 | Block parametrization A=(αI+C1)⊕(−αI+C2), B=(βI+D1)⊕(−βI+D2), C_r,D_s traceless, from GLOBAL trace zero | 53–57 | SUPPORTED |
| C3 | L = 4(|α|²+|β|²)+Σ‖C_r‖²+Σ‖D_s‖² (3.1) | 59 | SUPPORTED |
| C4 | Four orthogonal 4-dim sectors X_rs=(ε_rα+ε_sβ)I4+C_r⊗I2+I2⊗D_s; every singular value of X in a sector | 61–65 | SUPPORTED |
| C5 | Operator triangle ‖X_rs‖_op ≤ a_r+b_s (3.3) | 65–67 | SUPPORTED |
| C6 | Lemma (2.1) ‖tI4+C⊗I2+I2⊗D‖²_op ≤ 4|t|²+‖C‖²+2‖D‖² (C,D traceless 2×2) | 19 | SUPPORTED |
| C7 | Lemma (2.2) leg-swapped variant ≤ 4|t|²+2‖C‖²+‖D‖² | 21–23 | SUPPORTED |
| C8 | Matrix-element linear forms Tr(CM), Tr(DN); Tr M=Tr N=s | 29 | SUPPORTED |
| C9 | Weighted Cauchy–Schwarz split (2.3) | 31–33 | SUPPORTED |
| C10 | Second factor identity (2.4) x+y/2−|s|²/2 | 35–37 | SUPPORTED |
| C11 | Schmidt gauge U=diag(a,b), expansions x,y, identity (2.5) | 39–45 | SUPPORTED |
| C12 | x ≤ 1; second factor ≤ 1; supremum ⇒ (2.1) | 47 | SUPPORTED |
| C13 | Same-sector case: ‖X_rs‖_F² identity and ≤ 2L | 69–77 | SUPPORTED |
| C14 | Opposite-row-and-column case ≤ 2L | 79–85 | SUPPORTED |
| C15 | Same-row case via (2.1), parallelogram, ≤ 2L; same-column via (2.2) | 87–97 | SUPPORTED |
| C16 | Three cases exhaust all sector locations incl. ties/degeneracies; simultaneous attainment not needed | 99 | SUPPORTED |
| C17 | Strictness/slack expressions (same-row, same-column, same-sector, opposite) | 103–105 | SUPPORTED (M2) |
| C18 | Strict corollary S2(X)<2L on the all-C,D-nonzero, all-blocks-rank-2 class | 107 | SUPPORTED (M1) |
| C19 | Residual-scope statement (remaining T2 quantifier; no f274-region claim) | 109 | SUPPORTED (scope bookkeeping only) |
| C20 | Section-5 family: traceless, invertible, A²/B² explicit, both squares nonnormal, not normal, not rank one, nontrivial Jordan blocks at nonzero eigenvalues | 113–125 | SUPPORTED |
| C21 | Weighted-partial-permutation diagonalizability; A,B not unitarily similar to invertible weighted partial permutation/cyclic weighted shift | 125 | SUPPORTED |
| C22 | "Outside f215 rank-one/square-normal/weighted-permutation classes, outside f281 normal-factor class" | 13, 125 | INCONCLUSIVE as class-membership (historical scope labels; not imported, not independently verifiable here — per manifest this is permitted labeling, and the internally provable sub-claims are all SUPPORTED) |
| C23 | Non-claims: not f274-region enlargement, no η>2L member, no T3/Z2/q3, no equality classification | 13, 107, 109, 125 | SUPPORTED (correctly disclaimed; reviewer confirms nothing in the reconstruction supports such claims) |

## 2. Written reconstruction (all steps hand-derived; no computation used)

### 2.1 Reduction to reducing bases (C1, S1|11)

If A = U_A(⊕_r A_r)U_A*, B = U_B(⊕_s B_s)U_B* with 2×2 blocks, then (U_A⊗U_B)* X (U_A⊗U_B) = (⊕_r A_r)⊗I4 + I4⊗(⊕_s B_s), and S2, ‖·‖_F, traces are unitarily invariant. The two unitaries act on different tensor factors, so nothing requires them equal. WLOG A,B are literally block diagonal.

### 2.2 Sector decomposition and L (C2–C4)

C4⊗C4 = ⊕_{r,s∈{1,2}} (C2_r⊗C2_s), four mutually orthogonal 4-dimensional subspaces. A⊗I4 preserves the first-factor split (acts as A_r⊗I2 on sector (r,s)); I4⊗B preserves the second (acts as I2⊗B_s). Hence X = ⊕_{r,s} X_rs with X_rs = A_r⊗I2 + I2⊗B_s, and the singular values of a finite direct sum are exactly the multiset union of the blocks' singular values, so each of the 16 singular values of X lies in a unique sector (C4).

Writing A_r = ε_rα I2 + C_r, B_s = ε_sβ I2 + D_s with ε_1=1, ε_2=−1 is possible with C_r, D_s traceless iff Tr A_1 + Tr A_2 = 0 and Tr B_1 + Tr B_2 = 0, i.e. exactly the GLOBAL trace-zero hypothesis (blockwise tracelessness would force α=β=0): take α = (Tr A_1)/2 = −(Tr A_2)/2, then Tr C_r = 0, and similarly β, D_s. Conversely every such tuple is realized. (C2.) Neither block is required normal or traceless — arbitrary opposite block traces are the point of this packet.

‖±αI2+C‖_F² = Tr((|α|²I+ᾱ(±C)+(±α)C*+C*C)) = 2|α|²+‖C‖_F² because the cross traces vanish (Tr C=0) — same for B. Summing the two blocks of each: L = 4(|α|²+|β|²)+Σ_r‖C_r‖²+Σ_s‖D_s‖², i.e. (3.1). (C3.)

X_rs = (ε_rα I2+C_r)⊗I2 ⊕-decomposed as [(ε_rα I2+C_r)⊗I2] + [I2⊗(ε_sβ I2+D_s)] since ε_rα(I2⊗I2)+ε_sβ(I2⊗I2) recombine to (ε_rα+ε_sβ)I4. Operator triangle inequality plus ‖P⊗I2‖_op = ‖I2⊗Q‖_op = ‖P‖_op (‖·‖_op is multiplicative on Kronecker products; I2 has norm 1) give (3.3): ‖X_rs‖_op ≤ a_r + b_s with a_r=‖ε_rα I2+C_r‖_op, b_s=‖ε_sβ I2+D_s‖_op. (C5.)

### 2.3 The two-qubit lemma (2.1) (C6–C12, S1|17–47) — load-bearing, fully re-proved

Convention: u ↔ U means u = Σ_{ij} U_{ij} e_i⊗e_j (any other convention transposes/conjugates coefficient matrices, which preserves traces, Frobenius norms and the argument — the packet's "harmless transpose" caveat at S1|29 is correct).

Matrix elements (hand derivation):
- ⟨u,v⟩ = Σ Ū_{ij}V_{ij} = Tr(U*V) =: s.
- (C⊗I2)v ↔ CV, so ⟨u,(C⊗I2)v⟩ = ⟨U,CV⟩_F = Tr(U*CV) = Tr(CVU*) = Tr(CM) with M = VU*.
- (I2⊗D)v has coefficient matrix (Σ_k D_{jk}V_{ik})_{ij}, so ⟨u,(I2⊗D)v⟩ = Σ_{ijk} Ū_{ij}D_{jk}V_{ik} = Σ_{jk} D_{jk}(VᵀŪ)_{kj} = Tr(DN) with N = VᵀŪ.
- Tr M = Tr(VU*) = Tr(U*V) = s; Tr N = Σ_{jk}V_{kj}conj(U_{kj}) = s. (C8.)

Decompose M = M0 + (s/2)I2, N = N0 + (s/2)I2 with Tr M0 = Tr N0 = 0. Since Tr C = Tr D = 0, ⟨u,(tI4+C⊗I2+I2⊗D)v⟩ = t·s + Tr(CM0) + Tr(DN0).

Weighted Cauchy–Schwarz on (C ⊕ M2 ⊕ M2) with the bilinear pairing b(P,Q)=Σ P_{ij}Q_{ij} (|b(P,Q)| = |⟨P̄,Q⟩_F| ≤ ‖P‖_F‖Q‖_F):
ts + Tr(CM0) + Tr(DN0) = b((2t, C, √2D), (s/2, M0ᵀ, N0ᵀ/√2)), and transposition is a Frobenius isometry, so
|⟨u, X v⟩|² ≤ (4|t|²+‖C‖²+2‖D‖²)·(|s|²/4+‖M0‖²+‖N0‖²/2), which is (2.3) with exactly the displayed weights — the weight pairing is consistent (2t·s/2 = ts; √2·(1/√2)=1 on the D-pairing). (C9.)

‖M0‖² = ‖M‖² − 2Re((s̄/2)Tr M) + |s|²/2 = ‖M‖² − |s|²/2 (Tr M = s), and identically ‖N0‖² = ‖N‖² − |s|²/2. With x = ‖VU*‖_F² and y = ‖U*V‖_F² = ‖N‖_F² (N = (U*V)ᵀ, so the equality at S1|35 is exact), the second factor is |s|²/4 + x − |s|²/2 + (y−|s|²/2)/2 = x + y/2 − |s|²/2. (C10, identity (2.4).)

Schmidt step: under (W1⊗W2), U → W1UW2ᵀ, V → W1VW2ᵀ; then VU* → W1(VU*)W1*, N → W2NW2*, s → s (cyclicity). So x, y, s are invariant under independent local unitaries, and one may Schmidt-diagonalize u: U = diag(a,b), a,b ≥ 0, a²+b² = 1, V = [[p,q],[r,w]], |p|²+|q|²+|r|²+|w|² = 1, s = ap + bw. Direct expansion (hand):
- VU* = V·diag(a,b): column 1 scaled by a, column 2 by b ⇒ x = a²(|p|²+|r|²) + b²(|q|²+|w|²) (S1|41 exact).
- U*V = diag(a,b)·V: row 1 scaled by a, row 2 by b ⇒ y = a²(|p|²+|q|²) + b²(|r|²+|w|²) (S1|43 exact).
- |s|² − |bp+aw|² = (a²−b²)(|p|²−|w|²) (the cross terms 2ab Re(pw̄) cancel). Hence x+y = 2a²|p|² + 2b²|w|² + |q|²+|r|² (from x+y using a²+b²=1) = 1 + (a²−b²)(|p|²−|w|²) = 1 + |s|² − |bp+aw|², i.e. (2.5). (C11.)
- x = a²·‖col1(V)‖² + b²·‖col2(V)‖² ≤ a²+b² = 1, a convex combination of squared column norms. Then (2.4) = x + (y−|s|²)/2 = x + (1−|bp+aw|²−x)/2 = (1+x−|bp+aw|²)/2 ≤ 1. (C12.)

Taking the supremum over unit u,v (variational formula for the operator norm, a permitted elementary import per S1|129) proves (2.1). Leg swap: the commutor S(e_i⊗e_j)=e_j⊗e_i conjugates tI4+C⊗I2+I2⊗D to tI4+I2⊗C+D⊗I2 = tI4+D⊗I2+I2⊗C, and applying (2.1) with (C,D)→(D,C) gives (2.2). (C7.)

Remark (why the weights are essential — confirms the lemma is not a disguised import): with unit weights the second factor would be x+y = 1+|s|²−|bp+aw|², which exceeds 1 whenever |s|²>|bp+aw|² (e.g. a=1,b=0,w≠0,p≠0: 1+|p|²−|w|² can be >1). The 4|t|² / ‖·‖²-1 / ‖·‖²-2 charging is exactly matched to make the second factor x+y/2−|s|²/2 ≤ 1. This matches the packet's disclaimer (S1|25) that (2.1) is a genuinely two-qubit statement, distinct from the withdrawn arbitrary-T f198 claim, which is nowhere used.

### 2.4 Case analysis (C13–C16, S1|69–99)

Same sector (r,s): σ1²+σ2² ≤ Σ_k σ_k(X_rs)² = ‖X_rs‖_F². Expand: ‖tI4‖²=4|t|²; ‖C⊗I2‖²_F=2‖C‖²; ‖I2⊗D‖²_F=2‖D‖²; the three cross terms are 2Re(t̄·2TrC)=0, 2Re(t̄·2TrD)=0, 2Re Tr(C*⊗D)=2Re(TrC*·TrD)=0 (all vanish because C,D are traceless — S1|77's stated reason is correct). With t=ε_rα+ε_sβ: ‖X_rs‖_F² = 4|ε_rα+ε_sβ|²+2‖C_r‖²+2‖D_s‖² ≤ 8(|α|²+|β|²)+2Σ_i‖C_i‖²+2Σ_j‖D_j‖² = 2L, using |z+w|² ≤ (|z|+|w|)² ≤ 2(|z|²+|w|²) and block domination. (C13.)

Opposite sectors (r,s),(r′,s′), r≠r′, s≠s′: each chosen singular value ≤ its sector's operator norm ≤ a_r+b_s, a_{r′}+b_{s′}; then (a+b)² ≤ 2a²+2b² (2xy≤x²+y²) applied to both, a_i² ≤ ‖A_i‖_F², b_j² ≤ ‖B_j‖_F², and {r,r′}={1,2}, {s,s′}={1,2} exhaust both direct sums, so the total is ≤ 2(‖A‖_F²+‖B‖_F²) = 2L. (C14.)

Same row r (sectors (r,1),(r,2)): apply (2.1) to each sector with t = ε_rα±β, C = C_r (coefficient 1, charged twice ⇒ 2‖C_r‖²), D = D_s (coefficient 2):
‖X_{r1}‖²op+‖X_{r2}‖²op ≤ 4|ε_rα+β|²+‖C_r‖²+2‖D_1‖² + 4|ε_rα−β|²+‖C_r‖²+2‖D_2‖² = 4(|ε_rα+β|²+|ε_rα−β|²)+2‖C_r‖²+2Σ_s‖D_s‖² = 8(|α|²+|β|²)+2‖C_r‖²+2Σ_s‖D_s‖² ≤ 2L, by the complex parallelogram identity |z+w|²+|z−w|² = 2|z|²+2|w|² (|ε_rα|=|α|) and ‖C_r‖² ≤ Σ_i‖C_i‖². Same column: symmetric via (2.2), coefficient 1 on the repeated D_s, slack 2‖D_{3−s}‖². (C15.)

Exhaustiveness: two sector labels (r,s)≠(r′,s′) satisfy either (r=r′, s≠s′) — same row; (r≠r′, s=s′) — same column; or (r≠r′, s≠s′) — opposite; equal labels is the same-sector case. Multiplicity and ties are harmless: the singular values of X as a multiset are distributed among sectors, each is bounded by its own sector's quantity, and only upper bounds per sector are combined; no simultaneous attainment of the per-sector bounds is assumed (S1|99's two parenthetical statements are both correct). This completes S2(X) ≤ 2L. **Theorem SUPPORTED.**

### 2.5 Slack expressions and strict corollary (C17–C18, S1|103–107)

- Same row: 2L − Σ_s‖X_{rs}‖²op ≥ 2Σ_i‖C_i‖² − 2‖C_r‖² = 2‖C_{3−r}‖². Exact for the displayed bound. SUPPORTED.
- Same column: symmetric, ≥ 2‖D_{3−s}‖². SUPPORTED.
- Same sector: using parallelogram, 4|ε_rα+ε_sβ|² = 8(|α|²+|β|²) − 4|ε_rα−ε_sβ|², so 2L − ‖X_rs‖_F² = 2‖C_{3−r}‖²+2‖D_{3−s}‖²+4|ε_rα−ε_sβ|² — this is an IDENTITY for the displayed Frobenius quantity, so "at least" (S1|103) is true and in fact understated (MINOR M2, not an error).
- Opposite: 2L − [(a_r+b_s)²+(a_{r′}+b_{s′})²] = 2Σ_i(‖A_i‖²−a_i²) + 2Σ_j(‖B_j‖²−b_j²) + (a_r−b_s)²+(a_{r′}−b_{s′})², using 2a²+2b²−(a+b)²=(a−b)² and the two rows/columns exhausting the blocks. Exact identity for the chain. Matches S1|105 with A_i=ε_iα I2+C_i, B_j=ε_jβ I2+D_j. SUPPORTED.
- Strict corollary (S1|107): if all of C1,C2,D1,D2 ≠ 0, then same-row slack ≥ 2‖C_{3−r}‖² > 0, same-column > 0, same-sector ≥ 2‖C_{3−r}‖² > 0; if additionally every 2×2 block A_i, B_j has rank two, then ‖A_i‖²−a_i² = σ_2(A_i)² > 0 for each i (and similarly B), so the opposite-case slack is > 0. Every case therefore gives S2(X) < 2L at every member of the stated class. SUPPORTED as a pointwise statement. MINOR M1: "uniformly throughout" should be read pointwise (for every member, by the same argument); no uniform quantitative margin over the class is established or needed (‖C_{3−r}‖ can be arbitrarily small). Not load-bearing.

### 2.6 Section 5 family (C20–C21, S1|113–125)

A = (αI2+cE12)⊕(−αI2), B = (βI2+dE12)⊕(−βI2), αcβd ≠ 0.
- Traceless: 2α−2α = 0, 2β−2β = 0. Invertible: triangular blocks with diagonals α,α,−α (det α²·α² ≠ 0) — rank 4, so certainly not rank one.
- (αI+cE12)² = α²I+2αcE12 (E12²=0) ⇒ A² = (α²I+2αcE12)⊕α²I2 (S1|121 exact); likewise B² (S1|123).
- Nonnormality of T = α²I+λE12, λ=2αc≠0: TT* − T*T = |λ|²(E11−E22) ≠ 0 (cross terms cancel; only the E12E21 vs E21E12 terms survive). Hence both squares are nonnormal (a direct sum is normal iff every reducing block is), and the same computation with base α shows A, B themselves nonnormal (λ=c≠0).
- αI+cE12 (αc≠0) is a nontrivial (size-2) Jordan block at the nonzero eigenvalue α: exactly J with one eigenvector.
- Weighted partial permutation (≤ one nonzero per row/column) that is unitarily similar to invertible A must itself be invertible, hence a weighted permutation (exactly one nonzero per row and column = monomial). Its underlying permutation splits into disjoint cycles; a k-cycle with weights w_1..w_k has det(zI−C) = z^k − Πw_i with Πw_i ≠ 0, whose roots (k distinct solutions of z^k = nonzero) are k distinct eigenvalues ⇒ diagonalizable; a direct sum of diagonalizable cycles is diagonalizable. A is not diagonalizable (nontrivial Jordan block), so A is not similar — a fortiori not unitarily similar — to any invertible weighted partial permutation or cyclic weighted shift (a cyclic weighted shift is a single weighted cycle, covered). Same for B. All internal mathematical sub-claims SUPPORTED.
- The family lies in the theorem's hypothesis (it is literally 2+2 block diagonal with opposite block traces ±2α, ±2β — the arbitrary-block-trace regime) and exhibits both-squares-nonnormal, so S1|11's inclusion statement holds.
- C22: the statements "outside the f215 rank-one/square-normal/weighted-permutation classes" and "outside f281's normal-factor class" are mappings to historical scopes whose definitions are not imported here; per manifest they are labels, and the packet itself already withholds any f274-region or certificate-region claim (S1|13, S1|109, S1|125). Verdict INCONCLUSIVE as external classification, which is the correct, permitted status — no enlargement of any earlier result is claimed by the source or by this review.

## 3. Edge cases and degenerate/equality boundaries

- Arbitrary block traces: parametrization (3.2) requires exactly global trace zero (opposite block traces 2α,−2α), including α,β = 0 (then all block traces vanish) as a special case; the proof nowhere divides by α, β or block norms.
- Ties/degenerate singular multiplicities, and σ1=σ2 split across or within sectors: handled by multiset attribution (§2.4); only per-sector upper bounds are used.
- Zero blocks (C_r=0, D_s=0, α=0, β=0, X=0): all inequalities hold trivially; the strict corollary's hypotheses simply fail there.
- Strictness failure points, matching the source's hypotheses: same-row slack dies iff C_{3−r}=0; same-column iff D_{3−s}=0; same-sector needs C_{3−r}=D_{3−s}=0 AND ε_rα=ε_sβ to die; opposite-case dies when every A_i,B_j has σ_2=0 (all blocks rank ≤1) and a_r=b_s, a_{r′}=b_{s′}. The corollary's hypotheses (all C,D ≠ 0, all blocks rank two) exclude exactly these.
- Second-factor equality x=1 with bp+aw=0 is attainable (e.g. a=1,b=0, q=w=0), so the constant 1 in lemma (2.1)'s proof is sharp as a bound of that factor; no global equality classification of S2(X)=2L is attempted by the source, and none is offered here (per acceptance: no global equality classification beyond the source).
- The lemma's scalar charge 4|t|² is loose at t-only operators (‖tI4‖²=|t|²); this slack is by design of the weighted split and costs nothing in the theorem.

## 4. Findings

- FATAL: 0.
- MAJOR: 0.
- MINOR: 3.
  - M1 (S1|107): "S2(X)<2L uniformly throughout that stated class" — correct pointwise throughout the class; the word "uniformly" could be misread as a uniform quantitative margin, which is neither established nor needed. Wording only.
  - M2 (S1|103): same-sector slack "at least 2‖C_{3−r}‖²+2‖D_{3−s}‖²+4|ε_rα−ε_sβ|²" is in fact an exact identity for the displayed Frobenius bound; understatement, not an error.
  - M3 (S1|13/S1|125): f215/f274/f281 class-membership labels are historical scope labels, not independently verified here (and per manifest not to be imported); the internally provable sub-claims are all SUPPORTED and the source withholds the f274-complement/enlargement claim itself.
- Proof repair: none required for correctness of any load-bearing claim; M1–M3 need no repair for the theorem. Per policy, no retroactive correctness is conferred on any historical scope label.

## 5. Scope of this review

Same-harness written review only. No human review, independent-family review, formal/kernel verification, novelty determination, or closure of the original T2/T3/Z2/q3 targets. The false f198 arbitrary-T lemma was neither used nor rehabilitated. No sibling review, author code, later overlap/strictness packet, network source, or held payload was consulted. No global equality classification beyond the source is asserted. Frozen inputs, controls, manifest, packet, README, ledger and other waves were not modified; this wave directory contains only this file and the reviewer process record.

(End of review-v1.)
