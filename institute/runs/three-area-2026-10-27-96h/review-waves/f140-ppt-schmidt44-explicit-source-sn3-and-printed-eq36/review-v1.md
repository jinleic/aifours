# review-v1.md — f140-ppt-schmidt44-explicit-source-sn3-and-printed-eq36

- Reviewer: same-harness scientific reviewer (slot physics-3 assignment; NOT human, NOT independent-family, NOT formal/kernel, NOT novelty clearance).
- Manifest: `manifest-v1.json` SHA256 `8466a142441327f5ba475a7a986b2b62182267036f3a3e31c497569df000da95`, 3860 bytes (recomputed 2026-10-29T03:35:09Z, match).
- Authority: `contract-addendum-2-frontier-first-owner-direction-v1.json` (frontier-first addendum 2), as named in the manifest.
- Inputs re-verified in declared order at 2026-10-29T03:35:29Z (SHA256 / bytes / LF all match the manifest):
  1. `frontier-20261028-hor-crosshatch-source-sn3-and-erratum-v1.json` `011197ff…9827` 5926 B, 18 LF — candidate 1 packet (read in full, raw).
  2. `frontier-20261028-hor-crosshatch-source-sn3-check.py` `0165c650…ba11` 3207 B, 71 LF — author checker 1 (read only; NOT executed, NOT imported).
  3. `frontier-20261028-hor-crosshatch-printed-eq36-npt-v1.json` `93dd7451…95b2` 3021 B, 17 LF — candidate 2 packet (read in full, raw).
  4. `frontier-20261028-hor-crosshatch-printed-list-npt-check.py` `0eb07db8…8f3a` 1513 B, 28 LF — author checker 2 (read only; NOT executed, NOT imported).
- Permitted external read: `https://arxiv.org/html/2402.12966v1` (HTML rendering via the harness read tool, between 2026-10-29T03:36:16Z and 03:40:08Z) for Eq.34/Eq.36/Fig.5 transcription only. No web_search, no external model, no Git, no deletion, no author contact, no repository build/test suites.
- Parent-relayed author status note (not an input): the HTML "Eq.36" list is Eq.(E3) and HTML "Eq.34" is Eq.(E1) in the arXiv v1 PDF. I transcribed from the **HTML rendering** and keep all findings scoped to that v1 printed list; no PDF was read, no PRL-version or intent claim is made.

## Reviewer artifacts (all in this directory, `reviewer-` prefixed)

| file | SHA256 | role |
|---|---|---|
| `reviewer-independent-exact-check-v1.py` | `cdd572f0653e46d2844e1b13adc3a3fbed593276b5c92b9b5e4ca504165d51c1` (21280 B) | reviewer-written exact Q(√2) checker; rebuilds the source from the packet prose and the printed list from my own transcription; mutation controls |
| `reviewer-independent-exact-check-output-v1.json` | see `reviewer-receipts-v1.txt` | its output (run 2026-10-29T03:45:21Z, exit 0, `author_code_executed_or_imported: false`) |
| `reviewer-arxiv-appendixE-reader-excerpt-v1.txt` | `6ed98b2134124160cfa021f6721c9f5cbe300506e317f686eb713c1bf1183ad9` (15038 B) | verbatim lines 351–419 of the reader text I read (Appendix E); full reader text SHA256 `93e2c654b6c1f7de1cec5e9e7498817b3ee7faa3111be1edea1e4134b48f5fe9` |
| `reviewer-receipts-v1.txt` | — | clock/hash receipts for inputs, script, outputs and this review |

Arithmetic everywhere is exact: elements of Q(√2) stored as pairs of `fractions.Fraction`; positivity decided by exact symmetric Gaussian elimination (a matrix is PSD iff every pivot is ≥ 0, every zero pivot has a zero row, and each Schur complement is PSD; signs of p+q√2 decided by comparing p² with 2q²). No floating point is used anywhere. The PSD routine was controlled on a Bell-state partial transpose (correctly NOT PSD), a separable 2×2 state (PSD) and the known-PPT H^Γ, Q^Γ, R^Γ (PSD).

---

## Candidate 1 — explicit additive H⊗Q/Π_A source: PPT and Schmidt number exactly 3

### 1.1 Reconstruction of the source (from the packet's `explicit_source` prose only)

- H = [|00⟩] + [|01⟩+|10⟩] + [|03⟩+|12⟩] + [|02⟩+|11⟩] + [√2|13⟩+|10⟩] on C²⊗C⁴ ( [v] := |v⟩⟨v| ). tr H = 10.
- Q = [|10⟩+|02⟩] + [|20⟩+|12⟩] + [|00⟩+|21⟩] + [|01⟩+|22⟩] on C³⊗C³ (the crosshatch edges of the paper's Fig.1). tr Q = 8.
- H⊗Q regrouped as Alice = (A_H, A_Q), Bob = (B_H, B_Q); Alice restricted to the rows (0,0),(0,1),(0,2),(1,1) in that order (rows 0,1,2,3); Bob index 3·b_H + b_Q. This is exactly the compression by Π_A = 1 − |1⟩⟨1|_{A_H}⊗(|0⟩⟨0|+|2⟩⟨2|)_{A_Q} of the paper's Eq.(8)/(35). R := (Π_A⊗1)(H⊗Q)(Π_A⊗1) = Σ_{k,l} (Π_A⊗1)|h_k q_l⟩⟨h_k q_l|(Π_A⊗1), 20 formal generators.
- Exact results: **tr R = 44**; **rank R = 18**; R ≥ 0 (sum of projectors; also LDL-verified).
- Documentary (not an error): two of the 20 formal generators, h₄⊗q₂ and h₄⊗q₃ (h₄ = √2|13⟩+|10⟩ has Alice support {1}; q₂,q₃ have A_Q support {0,2}), are annihilated by Π_A. R therefore has **18 nonzero generators**, matching its rank 18 (the generators are linearly independent). The packet's "20 source kets" is literally true; the zero kets satisfy every stated identity vacuously.

### 1.2 H is PPT of rank 5 and entangled (full product-range / partial-conjugate argument)

Exact facts verified (`checks.H_*`): H ≥ 0, rank H = 5; H^Γ (Bob transpose) ≥ 0, rank H^Γ = 5; the five h_k are linearly independent; the three stated vectors k₁ = −|00⟩+|11⟩, k₂ = −|01⟩+|12⟩, k₃ = −|02⟩ − (1/√2)|10⟩ + |13⟩ are annihilated by H^Γ and are linearly independent, hence span ker H^Γ (dimension 8−5 = 3). Since H^Γ is Hermitian, ran H^Γ = (ker H^Γ)^⊥.

Range parametrization (verified entrywise from the five basis kets): ran H = { X(a,b,c,d,e) } with 2×4 coefficient matrix
X = [[a, b, d, c], [b+e, d, c, √2·e]], a,b,c,d,e ∈ ℂ.

Range criterion (Horodecki): if H were separable, H = Σ_i p_i |e_i f_i⟩⟨e_i f_i| with p_i > 0, then every |e_i f_i⟩ ∈ ran H and, because H^Γ = Σ_i p_i |e_i f̄_i⟩⟨e_i f̄_i| (f̄ = componentwise complex conjugate), every |e_i f̄_i⟩ ∈ ran H^Γ. I classify all nonzero product vectors in ran H (rank-1 coefficient matrix X):

- (A) Row 0 of X is zero ⇒ a=b=c=d=0 ⇒ X = e·[[0,0,0,0],[1,0,0,√2]] = e·|1⟩⊗(|0⟩+√2|3⟩) = e·h₄ (a genuine product vector in ran H, SR = 1 verified). It is real, so its partial conjugate is itself; ⟨k₃|h₄⟩ = −1/√2 + √2 = **1/√2 ≠ 0** (exact value `1/2*sqrt2`), so h₄ ∉ ran H^Γ.
- (B) Row 0 ≠ 0 and rank 1 ⇒ row 1 = t·row 0 for a unique t ∈ ℂ: b+e = ta, d = tb, c = td, √2·e = tc.
  - (B1) t = 0 ⇒ b+e = d = c = e = 0 ⇒ b = 0 ⇒ X = a|00⟩ with a ≠ 0. ⟨k₁|00⟩ = **−1 ≠ 0**, so |00⟩ ∉ ran H^Γ.
  - (B2) t ≠ 0 ⇒ d = tb, c = t²b, e = t³b/√2, a = (b+e)/t. If b = 0 then d=c=e=0 and a = 0, contradicting row 0 ≠ 0; so b ≠ 0 and we scale b = 1: X = (|0⟩+t|1⟩) ⊗ (a|0⟩+|1⟩+t|2⟩+t²|3⟩) with a = 1/t + t²/√2 (this identity was additionally confirmed exactly at 12 rational sample points; it is a Laurent-polynomial identity of degree ≤ 6, so 12 points suffice, and the derivation above is the proof anyway). Its Bob-partial conjugate is v = (|0⟩+t|1⟩) ⊗ (ā|0⟩+|1⟩+t̄|2⟩+t̄²|3⟩), coefficient matrix [[ā, 1, t̄, t̄²],[tā, t, |t|², t·t̄²]]. Membership in ran H^Γ requires ⟨k₂|v⟩ = −1 + |t|² = 0 ⇒ |t| = 1, and ⟨k₁|v⟩ = −ā + t = 0 ⇒ ā = t ⇒ a = t̄ = 1/t. Comparing with a = 1/t + t²/√2 gives t²/√2 = 0 ⇒ t = 0, contradiction. (The packet instead uses k₃: with ā = t and t̄ = 1/t, ⟨k₃|v⟩ = −t̄ − tā/√2 + t·t̄² = −t²/√2 ≠ 0 — also a valid contradiction; I confirm the reduction.)

Conclusion: **no nonzero product vector |e f⟩ ∈ ran H has |e f̄⟩ ∈ ran H^Γ.** Hence H ≠ 0 cannot be separable: H is PPT entangled. (The packet's formulation — "every compatible product vector lies in the single product line e·h₄, and one line cannot span rank 5" — is also correct; the stronger statement is that even that line is incompatible, via k₃.) As a 2×4 state SN(H) = 2 (entangled ⇒ ≥ 2; ≤ min dim = 2).

### 1.3 R is PPT

Structural: Bob of the regrouped system is (B_H,B_Q), so (H⊗Q)^{T_B} = H^{T_{B_H}} ⊗ Q^{T_{B_Q}} ≥ 0 (both factors verified PSD; Q^Γ verified exactly to equal the sum of the four flipped-edge projectors [|12⟩+|00⟩]+[|22⟩+|10⟩]+[|01⟩+|20⟩]+[|02⟩+|21⟩], i.e. the paper's Fig.1-right grid state, rank 4). Π_A is a real projector acting on Alice only, so conjugation by Π_A⊗1 commutes with T_B and R^Γ = (Π_A⊗1)(H^Γ⊗Q^Γ)(Π_A⊗1) ≥ 0.
Direct: the full 48×48 R^Γ was tested by exact elimination: **PSD, rank 18** (`checks.R_PT_psd_direct_48x48_exact = true`). The same holds after the paper's relabeling (a permutation; `R_paper_PT_psd = true`).

### 1.4 Core and range identities

- Core: Alice rows {1,3} = (0,1),(1,1) and Bob columns J = (0,3,6,9) (b_Q = 0). The 8×8 compression of R onto these coordinates (row 1 ↔ a_H=0, row 3 ↔ a_H=1) **equals H in all 64 entries** (`core_R_equals_H_64_entries = true`). Reason: among the four Q edges only q₀ = |10⟩+|02⟩ has an (a_Q,b_Q) = (1,0) component (coefficient 1), so P R P = Σ_k |h_k⟩⟨h_k|·1 = H. In paper coordinates this is exactly Eq.(37)'s compression (Alice {1,2}, Bob {0..3}) and it equals H exactly (`documentary_compression_R_paper_equals_H = true`).
- Range identities, verified on every one of the 20 generators (which span ran R because R = Σ|v⟩⟨v|): for every X ∈ ran R written as a 4×12 coefficient matrix,
  (I1) rows 1 and 3 vanish on columns J+1 = (1,4,7,10);
  (I2) row 2 on J+1 equals row 0 on J (componentwise, same b_H);
  (I3) row 1 on J equals row 0 on J+2 = (2,5,8,11).
  (Structural reason: a_Q = 1 never pairs with b_Q = 1 in Q; (I2) comes from the edge |00⟩+|21⟩ and (I3) from |10⟩+|02⟩, both multiplied by the same H factor with a_H = 0.)

### 1.5 Lemma: every X ∈ ran R with rank(X) ≤ 2 has core rank ≤ 1

Suppose rank X ≤ 2 and the core rows (row 1|_J, row 3|_J) are linearly independent. Then rows 1 and 3 of X (full 12-vectors) are independent, so they form a basis of the row space of X; write row 0 = α·row1 + β·row3 and row 2 = γ·row1 + δ·row3. By (I1) rows 1,3 vanish on J+1, hence row 2 vanishes on J+1; by (I2) row 0 vanishes on J; restricting row 0 = α·row1 + β·row3 to J and using independence of the core rows gives α = β = 0, so row 0 = 0 everywhere; by (I3) row 1 vanishes on J, contradicting independence of the core rows. Hence the core has rank ≤ 1. ∎ (Consistency check on the generators themselves: all generators with SR ≤ 2 have core rank ≤ 1, `lemma_consistency_on_source_kets = true`.)

### 1.6 SN(R) = 3

- SN(R) ≥ 3: if R = Σ_i p_i|ψ_i⟩⟨ψ_i| with p_i > 0 and SR(ψ_i) ≤ 2, then each ψ_i ∈ ran R (the range of a PSD sum of projectors is the span of the vectors), so by §1.5 each P|ψ_i⟩ (P = projector onto Alice {1,3} ⊗ Bob J) has coefficient matrix of rank ≤ 1, i.e. is a product vector or zero. Then H = P R P = Σ_i p_i P|ψ_i⟩⟨ψ_i|P would be separable, contradicting §1.2. 
- SN(R) ≤ 3: each nonzero generator occupies at most 3 Alice rows (exact counts over the 20 generators: [2,2,2,2,3,3,2,2,3,3,2,2,3,3,2,2,1,1,0,0]; Schmidt ranks identical), so each has SR ≤ 3 and R is an SR≤3 decomposition of itself.
- Therefore **SN(R) = 3 exactly, and R is PPT.** Both properties are scale-invariant, so they hold for the density operator R/44.

### 1.7 Relation of the 495 coordinate SN2 cut certificates to this source (description read in the packet only)

495 = C(12,4) is the number of 4-element subsets of the 12 Bob coordinates; the "coordinate 4×4 Bob cuts" are the compressions (1⊗P_B) R (1⊗P_B) with P_B a 4-coordinate diagonal projector. The packet states that R as defined above "is the sole source used in our 495-cut certificates" (`frontier-20261028-hor-crosshatch-coordinate-sn2-v1.json`, SHA 5a98e552…, not an input here) and that each cut is PPT with SN ≤ 2. Within this review: (i) PPT of every such cut follows from R PPT (a diagonal Bob compression commutes with T_B); (ii) the SN ≤ 2 content of the certificates was **not** independently verified here (outside the inputs; author code not executed) — status INCONCLUSIVE at this review's level; (iii) the read-only author checker 1 obtains its source kets from the same object (`h['source']`) exposed by the hash-pinned 495-cut verifier script, which is structurally consistent with the identity claim but is not evidence I generated. Consequence as stated by the packet and agreed here: the cut certificates pertain only to R as explicitly defined, and SN ≤ 2 of those particular 4×4 compressions says nothing positive about the existence of a 4×4 PPT SN-3 state.

### 1.8 Mutation controls (candidate 1)

- M1 (altered H ket √2|13⟩+|00⟩ in place of √2|13⟩+|10⟩): H'^Γ NOT PSD (negative pivot −1 at index 4), stated kernel vectors k₁,k₃ no longer annihilated, core(R') ≠ H, R'^Γ NOT PSD. 
- M2 (swap Bob columns 0↔1 in generator h₁⊗q₀ only): identity (I1) fails, core ≠ H, mutated R^Γ NOT PSD.
- Positive controls: R^Γ, Q^Γ, H^Γ PSD; negative control: Bell PT not PSD. Sign-routine self-tests pass.

### Verdict — candidate 1

**VERIFIED at same-harness level, no FATAL or MAJOR finding.** The explicitly defined R (tr 44, rank 18) is PPT (structural argument and direct exact 48×48 check) and has Schmidt number exactly 3 (SN ≥ 3 from the entangled core H via the range identities and lemma; SN ≤ 3 from the ≤3-Alice-row generators). MINOR documentary notes: (a) two of the 20 formal generators are zero after Π_A, so R has 18 nonzero generators (packet wording "20 source kets" is literal, not wrong); (b) the packet's "single compatible product line" is weaker than the truth (no compatible product vector exists), which only strengthens the conclusion; (c) applicability of the 495-cut SN≤2 certificates to this R is asserted in the packet and structurally consistent with the read-only checker, but INCONCLUSIVE here (not independently verified; outside inputs). Scope: this is a statement about R only — a 4×12 operator; it says nothing about any 4×4 state.

---

## Candidate 2 — the printed 18-ket list of arXiv:2402.12966v1 (HTML Eq.36 / Fig.5 caption) is NPT; exact 90-entry mismatch with R

### 2.1 My transcription (HTML rendering, read 2026-10-29T03:36Z; verbatim excerpt preserved in `reviewer-arxiv-appendixE-reader-excerpt-v1.txt`)

Stated relabeling (HTML text after Eq.35): Alice {|00⟩,|01⟩,|11⟩,|02⟩}_{A₁A₂} ↦ {|0⟩,|1⟩,|2⟩,|3⟩}; Bob |ij⟩_{B₁B₂} ↦ |i+4j⟩. Eq.36 ("equal mixture of the subsequent (unnormalized) states"):
|s̃⟩ = √2|2,0⟩+|2,3⟩; |s̃'⟩ = √2|2,8⟩+|2,11⟩; |h_i⟩ = |0,9+i⟩+|1,i⟩+|2,1+i⟩ (i=0,1,2); |h₃⟩ = |0,1⟩+|3,8⟩; |r_i⟩ = |1,9+i⟩+|2,8+i⟩+|3,1+i⟩ (i=0,1,2); |r₃⟩ = |0,3⟩+|1,8⟩; |q_i⟩ = |0,4+i⟩+|3,i⟩ (i=0..7). Total 18 kets. The Fig.5 caption lists the identical 18 components. This agrees ket-for-ket with the `literal_list` field of the candidate-2 packet.

P := Σ (18 projectors), unnormalized; **tr P = 44** (exact).

### 2.2 NPT proof (elementary, confirmed exactly)

Bob partial transpose: ⟨a,b|P^Γ|a',b'⟩ = ⟨a,b'|P|a',b⟩.
- No listed ket has a |0,0⟩ component (exact check: empty list) ⇒ ⟨0,0|P^Γ|0,0⟩ = ⟨0,0|P|0,0⟩ = 0.
- ⟨0,0|P^Γ|1,9⟩ = ⟨0,9|P|1,0⟩ = Σ_kets ⟨0,9|k⟩⟨k|1,0⟩; the only ket containing both |0,9⟩ and |1,0⟩ is h₀ (exact check) ⇒ 1.
- ⟨1,9|P^Γ|1,9⟩ = ⟨1,9|P|1,9⟩; the only ket containing |1,9⟩ is r₀ ⇒ 1.
Principal 2×2 block of P^Γ on (|0,0⟩,|1,9⟩) = **[[0,1],[1,1]]** (exact), determinant −1 < 0 ⇒ P^Γ is not PSD. Test vector |0,0⟩−|1,9⟩: ⟨v|P^Γ|v⟩ = 0 − 1 − 1 + 1 = **−1** (exact; −1/44 for P/44). Independently, the exact 48×48 elimination on P^Γ reports NOT PSD with witness "zero pivot at index 0 (|0,0⟩) with nonzero entry 1 in column 21 (|1,9⟩)" — the same block. (P itself is PSD, rank 18.) In the paper's own graphical language: (0,0) is an isolated vertex of the printed hypergraph, yet the flipped edge of {(0,9),(1,0)} ⊂ h₀ lands on it, so the degree-vs-diagonal condition of the paper's PPT criterion fails. NPT does not depend on which party is transposed.

### 2.3 Eq.34 documentary observation

The HTML LaTeX of Eq.34 reads `…(|03⟩+|12⟩)(⟨03|+⟨12|)\\ (|02⟩+|11⟩)(⟨02|+⟨11|)+…` — a `\\` line break with **no `+`** between the third and fourth projector terms, inside a 1/10 prefactor. Documentary only: the additive five-term reading has trace 1+2+2+2+3 = 10, matching the printed 1/10. The candidate-1 packet explicitly adopts the additive operator by definition rather than deciding editorial intent; I make no intent claim either.

### 2.4 Exact mismatch between R (under the paper's stated relabeling) and P — my own code

R was rebuilt in paper coordinates (Alice (0,0)→0, (0,1)→1, (1,1)→2, (0,2)→3; Bob b_H+4b_Q) and compared entrywise with P (both 48×48 over Q(√2)):
- **unequal entries: 90** (14 on the diagonal, 76 off-diagonal); **tr R = tr P = 44**; **⟨0,9|R|0,9⟩ = 1 vs ⟨0,9|P|0,9⟩ = 2** — all three numbers agree with the packet.
- Diagonal differences (a,b): R, P → (0,0):1,0 (0,2):1,0 (0,9):1,2 (0,10):1,2 (0,11):1,2 (1,3):1,0 (2,8):2,3 (2,11):2,1 (3,1):1,2 (3,2):1,2 (3,3):1,2 (3,9):1,0 (3,10):1,0 (3,11):1,0.
- For the record (fact about R, no inference about cause): R's 18 nonzero generators in paper coordinates are |0,8⟩+|1,0⟩; |1,8⟩+|3,0⟩; |0,0⟩+|3,4⟩; |0,4⟩+|3,8⟩; |0,9⟩+|1,1⟩+|2,0⟩; |1,9⟩+|2,8⟩+|3,1⟩; |0,1⟩+|3,5⟩; |0,5⟩+|3,9⟩; |0,11⟩+|1,3⟩+|2,2⟩; |1,11⟩+|2,10⟩+|3,3⟩; |0,3⟩+|3,7⟩; |0,7⟩+|3,11⟩; |0,10⟩+|1,2⟩+|2,1⟩; |1,10⟩+|2,9⟩+|3,2⟩; |0,2⟩+|3,6⟩; |0,6⟩+|3,10⟩; |2,0⟩+√2|2,3⟩; |2,8⟩+√2|2,11⟩. Only r₀,r₁,r₂ of the printed list coincide with generators of R; in particular (0,0) is not isolated in R, consistent with R being PPT and P not.
- Documentary, outside both verdicts: the Eq.(37)-type compression of P onto Alice {1,2} ⊗ Bob {0..3} has trace 9 and is not proportional to H (whereas the same compression of R equals H exactly). This is an exact statement about the printed list, not an inference about the authors' intended construction.

### 2.5 Mutation controls (candidate 2)

- M3 (delete |0,9⟩ from h₀): the block becomes [[0,0],[0,1]] and the test value flips to +1 — the specific certificate disappears as it should; the mutated list is still NPT via another isolated-vertex block (zero pivot at |0,0⟩ with entry 1 at |3,4⟩, from q₀ and q₄), and its mismatch count with R changes from 90 to 85. 
- The relabeled R passes the same PT routine (PSD), so the NPT verdict on P is not an artifact of the code path.

### Verdict — candidate 2

**VERIFIED (exact), no finding.** The equal-weight projector sum of the 18 kets printed in the HTML rendering of arXiv:2402.12966v1 Eq.36 / Fig.5 caption, under the paper's stated coordinates, is NPT: Bob-PT principal block [[0,1],[1,1]] on (|0,0⟩,|1,9⟩), test value −1 (−1/44 normalized), confirmed by an independent exact 48×48 positivity test. The explicit source R and this printed list differ in exactly 90 of 2304 entries under the stated relabeling (traces both 44; |0,9⟩ diagonal 1 vs 2). Scope: a source-text consistency finding about one displayed list in the v1 HTML rendering only.

---

## Explicit scope statement (both candidates)

Nothing here establishes, suggests or refutes what the authors intended by Eq.36/(E3), whether some other relabeling or local transformation reconciles the printed list with Eq.(8)/(35), the Schmidt number of the printed list, the content of any later (PRL) version, or any other result of the paper. The only operator proved PPT/SN3 here is the explicitly defined 4×12 operator R; the 495 coordinate 4×4 cuts are compressions of R whose SN≤2 certificates were not re-verified here. **No claim about the 4×4 original target follows; it stays OPEN.** This review is same-harness and is not human, independent-family, formal/kernel, or novelty clearance.

## Overall

- Candidate 1 (PPT/SN3 of the explicit source): VERIFIED, MINOR documentary notes only; 495-cut applicability INCONCLUSIVE within these inputs.
- Candidate 2 (printed list NPT; 90-entry mismatch): VERIFIED exactly.
- No FATAL, no MAJOR.
