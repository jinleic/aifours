# Review v1 — f289-block-pairs-disjoint-after-f285-stop

- reviewer: ReviewF289Blocks (same-harness written review; no human, independent-model, formal/kernel, novelty or worldwide-status claim)
- clock opened: 2026-10-30T03:40:41-0700 PDT; derivation checkpoint 03:48:38 PDT; review write begun 03:48:48 PDT (all `/bin/date`)
- inputs actually read: manifest-v1.json (sha256 3b675946…57573e1, matches assignment), freeze-receipt-v1.json (f130805a…392dbbe, matches), literal-packet-v1.md (3d8bb4c4…581da3, 10650 B, 134 LF, read complete raw in seven ≤20-LF windows, no elision), four status-only controls (hashes verified before read)
- NOT read (contract): f285 review body/disposition/outcome, any sibling reviewer output, author code, quarantined payloads, f198 lemma content, f274 eta conclusions. Controls consumed as STATUS ONLY; no excluded link followed.
- review mode: WRITTEN_ONLY. All reconstruction below is symbolic and all-variable. No selected concrete state, matrix, array, operator, vector or parameter value was chosen by me or required by the packet; no code/CAS/interpreter/solver/enumeration/replay used; no auxiliary vectors chosen (the lemma's proof quantifies over arbitrary unit vectors; Schmidt reduction is a WLOG existence move on an arbitrary vector).

## Verdict

**Main theorem (S1|7–S1|11): SUPPORTED — proved at written level.** For traceless `A,B ∈ M4(C)`, each separately unitarily similar to a 2+2 direct sum, with `X = A⊗I4 + I4⊗B`, `L = ||A||_F²+||B||_F²`, `S2(X)=σ1(X)²+σ2(X)²`, the inequality `S2(X) ≤ 2L` follows by a complete written chain (Sections R1–R4 below).

All twelve packet claims C1–C12: SUPPORTED. Findings: 0 FATAL, 0 MAJOR, 4 MINOR (presentational; each closed by a routine written step recorded below), 1 scope observation. No defect found in any inequality, identity, case, or structural assertion.

## R1. Reduction, block form, budget identity (packet §1, §3 setup; S1|7–S1|11, S1|51–S1|59)

Local conjugation `(U_A⊗U_B) X (U_A⊗U_B)* = (U_A A U_A*)⊗I4 + I4⊗(U_B B U_B*)`, and Frobenius norms and singular values are unitarily invariant, so the proof may work in the two (independent) 2+2 reducing bases — the two unitaries act on different tensor factors, so no compatibility condition is needed. Verified.

Global trace zero gives `Tr A1 + Tr A2 = 0`, so with `α = Tr A1/2` one has `A = (α I2 + C1) ⊕ (−α I2 + C2)`, `Tr Ci = 0`, and likewise `B = (β I2 + D1) ⊕ (−β I2 + D2)`. This uses the global (not blockwise) hypothesis exactly as S1|57 states. Verified.

Cross terms vanish against traceless parts (`2Re(ᾱ Tr C1)=0` etc.), so (3.1) `L = 4(|α|²+|β|²)+Σr||Cr||_F²+Σs||Ds||_F²`. Verified (using `||P⊗Q||_F = ||P||_F ||Q||_F` and `||±α I2||_F² = 2|α|²`).

## R2. Lemma (2.1)/(2.2) — the load-bearing step (S1|15–S1|47)

**Statement (2.1):** for arbitrary `t ∈ C`, traceless `C,D ∈ M2(C)`: `||tI4 + C⊗I2 + I2⊗D||_op² ≤ 4|t|² + ||C||_F² + 2||D||_F²`. **Reconstructed proof (complete):**

1. Variational formula `||Y||_op = sup{|⟨u,Yv⟩| : ||u||=||v||=1}`; write coefficient matrices `U,V ∈ M2(C)` of `u,v` (`||U||_F=||V||_F=1`).
2. Coefficient extraction (column-stacking vectorization): `⟨u,(C⊗I2)v⟩ = Tr(U†CV) = Tr(CM)`, `M := VU†`; `⟨u,(I2⊗D)v⟩ = Tr(DᵀU†V) = Tr(DN)`, `N := (U†V)ᵀ = Vᵀ conj(U)`; `⟨u,tI4v⟩ = t·s`, `s := ⟨u,v⟩ = Tr(U†V)`. Both `Tr M = Tr N = s` (transpose/conjugate preserve trace). Verified by direct index expansion.
3. `M = (s/2)I2 + M0`, `N = (s/2)I2 + N0` with `M0,N0` traceless; `Tr(CM)=Tr(CM0)`, `Tr(DN)=Tr(DN0)` since `Tr C = Tr D = 0`. Frobenius expansion with `⟨M,(s/2)I2⟩_F = |s|²/2`, `||(s/2)I2||_F² = |s|²/2` gives `||M0||_F² = ||M||_F² − |s|²/2` and same for `N0`. Verified.
4. Weighted Cauchy–Schwarz on `ts + Tr(CM0) + Tr(DN0) = (2t)(s/2) + Tr(C·M0) + Tr((√2D)(N0/√2))`, i.e. Cauchy–Schwarz on the direct sum `C ⊕ M2 ⊕ M2` with component weights (4,1,2) (degenerate weights handled by the direct-sum inner-product formulation): inequality (2.3) with second factor `|s|²/4 + ||M0||_F² + ||N0||_F²/2 = ||M||_F² + ||N||_F²/2 − |s|²/2`, i.e. (2.4) `x + y/2 − |s|²/2` with `x = ||M||_F²`, `y = ||N||_F² = ||U†V||_F²` (transpose preserves Frobenius norm). Verified. (Packet's "harmless transpose" remark, S1|29, covers the `N=(U†V)ᵀ` identity — see finding F2.)
5. Invariance under simultaneous local rotation (implicit in S1|39; see finding F1): for local unitaries `W1,W2`, replace `U → W1 U W2ᵀ`, `V → W1 V W2ᵀ`; then `s → ⟨u,v⟩` unchanged, `M → W1 M W1†`, `N → W2 N W2*`, so `|s|, x, y` and hence (2.4) are invariant, and joint rotation is a bijection on unit pairs. Hence the supremum of (2.4) over unit pairs may be computed with `U = diag(a,b)`, `a,b ≥ 0`, `a²+b² = 1` (Schmidt WLOG). Sound.
6. With `V = [[p,q],[r,w]]`, `|p|²+|q|²+|r|²+|w|² = 1`, `s = ap+bw` (a,b real): `M = V diag(a,b)` gives `x = a²(|p|²+|r|²)+b²(|q|²+|w|²)`; `N = (U†V)ᵀ` gives `y = a²(|p|²+|q|²)+b²(|r|²+|w|²)`. Verified. Cross terms `2ab Re(p w̄)` cancel in the difference `|s|² − |bp+aw|² = (a²−b²)(|p|²−|w|²)`, and expanding `1 = (a²+b²)(Σ|V_ij|²)` confirms (2.5): `x+y = 1+|s|²−|bp+aw|²`. Verified by full expansion (both directions).
7. Therefore (2.4) `= (1+x−|bp+aw|²)/2 ≤ 1`, since `x` is a convex combination `a²·(||(p,r)||²) + b²·(||(q,w)||²)` of the squared column norms of `V`, whose sum is 1; so `x ≤ max(a²,b²) ≤ 1` and `|bp+aw|² ≥ 0`. Verified.
8. Supremum over unit `u,v` yields (2.1). Swapping tensor factors (conjugation by the swap unitary, norm-preserving, exchanges the roles of C and D) yields (2.2). Verified.

Special-case consistency (symbolic): `C=D=0` gives equality `||tI4||² = 4|t|²`; `D=0` gives the stronger `2|t|²+2||C||²` by eigenvalue shift — no contradiction with (2.1). The lemma is 4×4 with explicit scalar charge `4|t|²` and is dimensionally and logically independent of the excluded f198 arbitrary-T 4×2 claim (whose content I have not imported; S1|25, S1|130). Confirmed no f198 reuse anywhere in the packet.

## R3. Sector decomposition and the four placement cases (S1|61–S1|99)

In the product of the two reducing bases, `X` is block diagonal with four 4×4 sectors `Xrs = (εrα+εsβ)I4 + Cr⊗I2 + I2⊗Ds` (3.2) — since `A⊗I4` preserves the A-sector index and `I4⊗B` the B-sector index. Every singular value of `X` is a singular value of some `Xrs`. Verified.

(3.3) `||Xrs||_op ≤ ar+bs` with `ar = ||εrα I2+Cr||_op`, `bs = ||εsβ I2+Ds||_op`: triangle inequality plus `||P⊗Q||_op = ||P||_op||Q||_op`. Verified.

The two largest singular values of `X` (as multiset elements) originate from sectors; the possible origin patterns are exactly: both in one sector; two sectors in the same row (r=r′); two sectors in the same column (s=s′); two sectors in different rows and columns. This is exhaustive for unordered pairs of distinct sectors `{(1,1),(1,2)},{(1,1),(2,1)},{(1,1),(2,2)},{(1,2),(2,1)},{(1,2),(2,2)},{(2,1),(2,2)}` — each falls in exactly one case. Ties/degeneracies: when equal singular values admit several origin assignments, every assignment is covered, and each case bound holds for whichever sectors the representatives come from; the argument never needs the sector operator-norm bounds to be attained simultaneously (S1|99). Verified.

**Case 3.1 (both from one sector (r,s)):** `σ1²+σ2² ≤ ||Xrs||_F²`. The three summands of `Xrs` are pairwise Frobenius-orthogonal: `⟨I4, Cr⊗I2⟩_F = Tr(Cr)Tr(I2) = 0`, `⟨I4, I2⊗Ds⟩_F = Tr(I2)Tr(Ds) = 0`, `⟨Cr⊗I2, I2⊗Ds⟩_F = Tr(Cr†)Tr(Ds) = 0`. Hence `||Xrs||_F² = 4|εrα+εsβ|²+2||Cr||²+2||Ds||² ≤ 8(|α|²+|β|²)+2Σi||Ci||²+2Σj||Dj||² = 2L` by `|z+w|² ≤ 2(|z|²+|w|²)`. Verified.

**Case 3.2 (different rows and columns, (r,s),(r′,s′), {r,r′}={1,2}, {s,s′}={1,2}):** `(ar+bs)²+(ar′+bs′)² ≤ 2(ar²+ar′²+bs²+bs′²)` by `(x+y)² ≤ 2x²+2y²` applied per term; then `ar²+ar′² = a1²+a2² ≤ ||A1||_F²+||A2||_F² = 4|α|²+Σi||Ci||²` by `||·||_op ≤ ||·||_F` and traceless cross-term cancellation (similarly for B), so the total is `≤ 2L`. Verified ("the two rows and columns exhaust the blocks", S1|85).

**Case 3.3 (same row r):** apply (2.1) to `Xr1` (t = εrα+β) and `Xr2` (t = εrα−β), C = Cr, D = Ds; sum: `4(|εrα+β|²+|εrα−β|²) = 8(|α|²+|β|²)` by the complex parallelogram identity, plus `2||Cr||²+2Σs||Ds||²`, total `≤ 2L`. Same column via (2.2) with roles interchanged, giving `8(|α|²+|β|²)+2Σr||Cr||²+2||Ds||² ≤ 2L`. Both chains verified line by line.

Combining the four cases: `S2(X) ≤ 2L`. **Theorem proved.** All degenerate inputs (α=0, β=0, vanishing Cr or Ds) are covered by non-strict inequalities.

## R4. Slack, equality and zero inventory (packet §4, S1|101–S1|107) — verified as exact identities of the displayed chains

- Same row r: `2L − [8(|α|²+|β|²)+2||Cr||²+2Σs||Ds||²] = 2||C_{3−r}||_F²` exactly; vanishes iff `C_{3−r} = 0`.
- Same column s: slack `= 2||D_{3−s}||_F²` exactly; vanishes iff `D_{3−s} = 0`.
- Same sector (r,s): parallelogram identity gives `8(|α|²+|β|²)−4|εrα+εsβ|² = 4|εrα−εsβ|²` exactly, so chain slack `= 4|εrα−εsβ|² + 2||C_{3−r}||² + 2||D_{3−s}||²`; vanishes iff `εrα = εsβ`, `C_{3−r}=0`, `D_{3−s}=0`.
- Opposite sectors: expanding `2L − [(ar+bs)²+(ar′+bs′)²]` with `2L = 2Σi||Ai||_F²+2Σj||Bj||_F²` (Ai = εiα I2+Ci, Bj = εjβ I2+Dj) gives exactly `2Σi(||Ai||_F²−||Ai||_op²) + 2Σj(||Bj||_F²−||Bj||_op²) + (ar−bs)² + (ar′−bs′)²`, matching S1|105; the squared-difference terms come from `2arbs ≤ 2arbs` … i.e. `2Σa²+2Σb² − [(ar+bs)²+(ar′+bs′)²] = (ar−bs)²+(ar′−bs′)²`. Vanishing conditions: rank(Ai) ≤ 1 (equivalently σ2(Ai)=0, i.e. `||Ai||_F = ||Ai||_op`) for each i, likewise for each Bj, and `ar = bs`, `ar′ = bs′` pairwise.
- These are slacks of the intermediate bounds, not of `2L − S2(X)` itself; the packet says so (S1|107) and claims no global equality classification. Correct.

**Strict corollary (S1|107):** on the class {C1,C2,D1,D2 all nonzero AND every 2×2 block Ai,Bj of rank two}: same-sector/same-row cases have slack ≥ 2||C_{3−r}||² > 0; same-column ≥ 2||D_{3−s}||² > 0; opposite case has `2(||A1||_F²−||A1||_op²) > 0` already (rank two 2×2 ⇒ σ1 ≥ σ2 > 0 ⇒ Frobenius strictly exceeds operator norm). Every case strict ⇒ `S2(X) < 2L` throughout the class. Verified; correctly labeled optional corollary, no neighborhood/certificate-necessity claim.

## R5. Section 5 family (S1|111–S1|125) — all-variable, verified symbolically

With symbolic parameters `α,c,β,d` constrained only by `αcβd ≠ 0`:

- Traceless: `Tr A = 2α + 0 + (−2α) = 0`, likewise B; both separately 2+2 reducing by construction. Verified.
- Invertible: `det(αI2+cE12)·det(−αI2) = α⁴ ≠ 0` (E12 nilpotent), so rank 4, in particular not rank one. Verified.
- `A² = (α²I2+2αcE12) ⊕ α²I2` (since `E12² = 0`), and for `αc ≠ 0` the block `T = α²I2+2αcE12` satisfies `TT† − T†T = |2αc|²(E11−E22) ≠ 0`, i.e. T is a nonnormal Jordan-type block at eigenvalue α² ≠ 0; a direct sum is normal iff all summands are, so `A²` is nonnormal; likewise `B²`. Also A, B themselves nonnormal (first block `αI2+cE12` has the same nonnormality computation with αc ≠ 0). Verified.
- Nontrivial Jordan block at nonzero eigenvalue: `αI2+cE12 ~ J2(α)`, `α ≠ 0`. Verified.
- Not unitarily similar to any weighted partial permutation or cyclic weighted shift: an invertible weighted partial permutation has exactly one nonzero entry per row and column, hence is a weighted permutation; its cycles have characteristic polynomials `z^k − w` with `w ≠ 0`, which have k distinct roots (k-th roots of a nonzero number are distinct), so every cycle — and hence the direct sum — is diagonalizable over C. A is invertible but not diagonalizable (J2(α) with α ≠ 0), so A is not similar, a fortiori not unitarily similar, to any invertible weighted partial permutation; non-invertible ones are excluded since similarity preserves invertibility; an invertible cyclic weighted shift is a single-cycle weighted permutation, covered by the same argument. Verified.
- No numerical parameter instance is selected anywhere: the family is stated with symbolic parameters under a symbolic nonvanishing constraint. Compliant.

Scope observation (O1, not a defect): the mathematical content of the exclusions (nonnormality of A, B, A², B²; rank four; Jordan structure; non-similarity to weighted partial permutations/shifts) is fully verified above. The identification of these properties with the *names* "f215 rank-one / square-normal / weighted-permutation(-shift) / f281 normal-factor classes" is the packet's own framing; per this wave's contract I did not import those dispositions' content, so the label mapping is accepted only as the packet's self-description, with the underlying mathematics verified.

## R6. Boundary and non-claims (S1|3, S1|11, S1|13, S1|109, S1|127–S1|132)

- Scope is exactly the separately-2+2-reducing traceless family; no claim for all traceless pairs, T3, Z2, q3. Consistent with the proof (which uses the reducing bases essentially).
- No claim that the family meets or escapes f274's η > 2L region; the packet explicitly leaves the all-local-bases η comparison unpaid (S1|13, S1|109). Consistent with my instructions: f274 eta-region status remains UNKNOWN after this review; no conclusion drawn here.
- f198 false arbitrary-T lemma excluded and not reused (S1|3, S1|25, S1|130); (2.1) is independently proved above, so nothing rests on f198.
- No solver/code/finite search/selected instance/Lean/kernel/cross-family/novelty claim (S1|132). Verified against the packet text read in full.

## Claim-by-claim disposition

| # | Packet claim (lines) | Verdict |
|---|---|---|
| C1 | Main theorem S2(X) ≤ 2L on separately 2+2 reducing traceless pairs (S1|7–S1|11) | SUPPORTED (proof complete, R1–R3) |
| C2 | Lemma (2.1) and (2.2) with scalar charge 4\|t\|² (S1|17–S1|47) | SUPPORTED (R2, steps 1–8) |
| C3 | Block form from global trace zero, budget identity (3.1), sector split (3.2), triangle bound (3.3) (S1|51–S1|67) | SUPPORTED (R1, R3) |
| C4 | Case both singular values from one sector (S1|69–S1|77) | SUPPORTED (R3) |
| C5 | Case different rows and columns (S1|79–S1|85) | SUPPORTED (R3) |
| C6 | Case same row via (2.1) / same column via (2.2) (S1|87–S1|97) | SUPPORTED (R3) |
| C7 | Exhaustiveness incl. degeneracies/ties; no simultaneous attainment needed (S1|99) | SUPPORTED (R3) |
| C8 | Slack formulas for all four cases (S1|103–S1|105) | SUPPORTED — verified as exact identities of the chains (R4) |
| C9 | Strict corollary S2(X) < 2L on the stated class (S1|107) | SUPPORTED (R4) |
| C10 | Residual quantifier and honest non-claims incl. f274 openness (S1|109) | SUPPORTED |
| C11 | Section 5 both-squares-nonnormal family and structural exclusions, all-variable (S1|111–S1|125) | SUPPORTED (R5; label mapping = packet framing, O1) |
| C12 | Inputs/history/non-claims: no f198 reuse, no eta conclusion (S1|127–S1|132) | SUPPORTED |

## Findings (line findings, severity)

- **F1 (MINOR, LF S1|39):** the Schmidt WLOG ("By independent local unitaries, Schmidt-diagonalize u") does not state that the same local unitaries rotate v together with u, nor prove invariance of the quantity (2.4). Closed in R2 step 5: `s → s`, `M → W1MW1†`, `N → W2NW2*` under `(W1⊗W2)` applied to both; joint rotation bijects unit pairs, so the reduction is valid. Presentational only; no mathematical defect.
- **F2 (MINOR, LF S1|29, S1|35):** `y = ||U†V||_F² = ||N||_F²` rests on `N = Vᵀ conj(U) = (U†V)ᵀ` and Frobenius-norm invariance under transpose; the identity is implicit in the "harmless transpose" sentence. Closed in R2 step 2. Presentational only.
- **F3 (MINOR, LF S1|31–S1|33):** the weighted Cauchy–Schwarz (2.3) is stated without treating vanishing weights (t=0 or C=0 or D=0); the direct-sum inner-product formulation (or a limiting argument) covers the degenerate cases without change. Presentational only.
- **F4 (MINOR, LF S1|107):** the strict corollary uses, without display, that a rank-two 2×2 block satisfies `||·||_F > ||·||_op` (σ2 > 0). One-line inference; closed in R4. Presentational only.
- **O1 (observation, LF S1|125):** see R5 — verified mathematics; historical class-label identification is the packet's own framing, not independently imported.

No FATAL or MAJOR findings. No step of the proof chain failed reconstruction; no case is missing; no selected instance appears in the packet or in this review.

## Same-harness assurance

- This is a same-harness written review by ReviewF289Blocks; not human review, not an independent-model-family review, not a formal/kernel proof, not a novelty or worldwide-status determination, and not acceptance of any target theorem beyond the packet's own stated scope.
- Imports used, exact scope only: the packet's own text (complete, hash-verified) and the standard identities it lists (S1|129): unitary invariance of spectra and Frobenius norm, Schmidt decomposition, Frobenius duality `||P⊗Q||_F = ||P||_F||Q||_F`, `||P⊗Q||_op = ||P||_op||Q||_op`, the operator-norm variational formula, block singular spectra of direct sums, Cauchy–Schwarz (plain and weighted), the complex parallelogram identity, and `|z+w|² ≤ 2|z|²+2|w|²`. Nothing from f198, f274 conclusions, f215/f274/f281 dispositions, or any held material was used mathematically.
- Process compliance: manifest/receipt verified against assignment SHAs; four status-only controls hash-checked then read as status only; pre-body ACK recorded (reviewer-prebody-ack-v1.md) before any packet read; packet read complete in raw ≤20-LF windows incl. endings; checkpoints reviewer-checkpoint-v1.md (03:48:38 PDT) and this file; cadence gaps 03:40:41 → 03:48:38 → 03:48:48, all < 30 min; writes confined to this wave directory; no builds/lints/tests/formatters run; no network, no sibling/author/quarantined input consulted.
- Conclusion for the parent: the packet's theorem, lemma, case analysis, slack inventory, strict corollary, and structural family are SUPPORTED at the written level with 0 FATAL / 0 MAJOR / 4 MINOR presentational findings, each closed above. The f274 η-region membership of this family remains UNKNOWN, exactly as the packet states.
