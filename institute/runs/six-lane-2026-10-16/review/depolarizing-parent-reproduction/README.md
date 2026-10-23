# Depolarizing witness, M = 2000: independent parent-side reproduction

> **Status.** This is an **independent numerical reproduction** in IEEE binary64 arithmetic, plus exact and brute-force validation at small M. It is **not a rigorous certificate**. No interval arithmetic or directed rounding is used. The error estimate in §6 is empirical and non-rigorous. Nothing here is promoted; it is reported only.

## 0. Result

| quantity | value |
|---|---|
| I_c(ρ, N_{1/5}^{⊗2000}), pinned witness, p = 1/5 (η = 11/15) | **1.14134071 × 10⁻⁸ bits** = 7.9111709 × 10⁻⁹ nats |
| worker's claimed enclosure (bits; `M2000_p1_5_TOTAL.json`) | [1.12885479 × 10⁻⁸, 1.14364441 × 10⁻⁸] → **our value is inside** (at 84.4 % of the width; 1.25 × 10⁻¹⁰ above the lower end, 2.30 × 10⁻¹¹ below the upper end) |
| run-to-run spread over 7 variants with D ≥ 300 (window, normalisation, perturbed inputs) | 7.7 × 10⁻¹⁶ nats (1.1 × 10⁻¹⁵ bits) |
| conservative numerical error estimate (§6) | \|δI_c\| ≲ 5 × 10⁻¹⁴ bits (about 4 × 10⁻⁶ relative); the nearer interval end is ≥ 460 × farther away |
| sign control, p = 201/1000 (η = 183/250) | **−7.6690931 × 10⁻⁹ bits**, negative |
| sign control, p = 1/4 (η = 2/3) | **−9.9060228 × 10⁻⁷ bits**, negative |
| per-sector check against the worker's 220 sector enclosures (`*.sectors.jsonl`) | **220 of 220** of our I_c(ρ, Φ_N) values lie inside the worker's per-sector intervals |

The value is positive and lies inside the worker's interval in **bits**. The worker's logs are base 2 (PROOFS.md:4). In nats the same number is 7.91 × 10⁻⁹, which falls *below* the quoted interval. Any quotation of the interval must therefore carry its unit.

For capacity: Q(N_{1/5}) ≥ I_c/M ≈ 5.7 × 10⁻¹² bits per use.

## 1. Conventions

- The channel is D_η(X) = ηX + (1−η) tr(X) I/2 = (1−p)X + (p/3)(XσX + YσY + ZσZ), with η = 1 − 4p/3. We write f := (1−η)/2, so f = 2/15 at p = 1/5.
- The input is ρ = Σ_i q_i |φ_i⟩⟨φ_i|, with φ_i ∈ Sym^M written in the Dicke basis |M;x⟩, where x is the number of |1⟩s.
- The purification is |ψ⟩ = Σ_i √q_i |i⟩_R |φ_i⟩. This is valid for any φ_i, orthogonal or not.
- I_c = S(B) − S(RB) = S(D^{⊗M}(ρ)) − S((id_R ⊗ D^{⊗M})(ψ)). Entropies are computed in nats and converted to bits by dividing by ln 2.
- The witness (`witness_g3_M2000_p1_5.json`, file sha256 4ced4ed9…, verified against MANIFEST.json) has:
  - two real vectors: φ₁ on x ≡ 0 (mod 3) with x ≤ 300, and φ₂ on x ≡ 1 (mod 3) with x ≤ 298;
  - q = (1/2, 1/2);
  - an exact overlap of 0 (the supports are disjoint).

## 2. Derivation (own route; no worker material consulted)

### 2.1 Schur–Weyl blocks through a singlet embedding

The decomposition is (C²)^{⊗M} = ⊕_{r=0}^{⌊M/2⌋} V_{J_r} ⊗ W_r, with J_r = M/2 − r and multiplicity m_r := dim W_r = C(M,r) − C(M,r−1). Write N := M − 2r.

1. **Permutation invariance.** Y^{ij} := D^{⊗M}(|φ_i⟩⟨φ_j|) commutes with every qubit permutation, because D^{⊗M} commutes with permutation conjugation and the φ_i are symmetric. Hence Y^{ij} = ⊕_r Y_r^{ij} ⊗ 1_{W_r}. The same holds for Y^{RB} = Σ_{ij} √(q_i q_j) |i⟩⟨j| ⊗ Y^{ij}.
2. **The embedding is an intertwiner.** Define E_r : Sym^N → (C²)^{⊗M} by |u⟩ ↦ |ψ⁻⟩^{⊗r} ⊗ |u⟩, with singlets on the pairs (1,2), …, (2r−1, 2r). E_r is an isometry, and it is SU(2)-equivariant because U ⊗ U |ψ⁻⟩ = |ψ⁻⟩. Every singlet pair is annihilated by its own total spin, so J⃗ E_r = E_r J⃗_N. The image therefore lies in the spin-J_r isotypic component. By Schur's lemma, E_r = V_r ⊗ |w_r⟩ with V_r unitary and w_r a unit vector. Consequently E_r† Y E_r = V_r† Y_r V_r for every permutation-invariant Y, with the same intertwiner for every (i, j). The spectra of the B block and the RB block are therefore preserved.
3. **Reduction to the symmetric subspace.** D is self-adjoint under the Hilbert–Schmidt inner product, so ⟨a|E_r† D^{⊗M}(X) E_r|b⟩ = tr[X · (D⊗D)(ψ⁻)^{⊗r} ⊗ D^{⊗N}(|b⟩⟨a|)]. Here (D⊗D)(ψ⁻) = η²ψ⁻ + (1−η²) 1/4. Π_sym annihilates any ψ⁻ factor, so only the 1/4 part survives:

   **E_r† D^{⊗M}(X) E_r = c_r S_N(tr_{2r} X)**, with c_r = ((1−η²)/4)^r = (f(1−f))^r and S_N(Z) := Π_N D^{⊗N}(Z) Π_N.

   This identity was checked entrywise against brute force (§4 B).
4. **Weights do not depend on the input.** S_N is SU(2)-covariant and Sym^N is irreducible, so S_N(Π_N) = λ₀(N) Π_N. Hence tr S_N(Z) = λ₀(N) tr Z. Taking Z = |0^N⟩⟨0^N| gives S_N(Z) = diag((1−f)^{N−a} f^a), so λ₀(N) = ((1−f)^{N+1} − f^{N+1})/(1−2f). The block weight is

   p_r = m_r c_r λ₀(M−2r) tr ρ.

   With 60-digit mpmath, Σ_r p_r − 1 = 7 × 10⁻⁶⁰.
5. **Block formula for I_c.** S(B) = H(p) + Σ_r p_r [S(ρ_r^B) + log m_r], and S(RB) has the same form with ρ_r^RB. The terms H(p) and log m_r cancel, so

   **I_c = Σ_r p_r [S(ρ_r^B) − S(ρ_r^RB)]**,

   where ρ_r^B ∝ S_N(tr_{2r} ρ) and ρ_r^RB ∝ Σ_ij √(q_i q_j) |i⟩⟨j| ⊗ S_N(tr_{2r} |φ_i⟩⟨φ_j|).

### 2.2 The compressed channel S_N in the Dicke basis (four-letter expansion)

1. **Single-site action.** On computational-basis matrix units, D(|σ⟩⟨σ|) = (1−f)|σ⟩⟨σ| + f|σ̄⟩⟨σ̄| and D(|σ⟩⟨σ̄|) = η|σ⟩⟨σ̄|. Each site therefore carries one of six letters (st → uv):

   | letter | weight |
   |---|---|
   | 00→00 | 1−f |
   | 00→11 | f |
   | 11→00 | f |
   | 11→11 | 1−f |
   | 10→10 | η |
   | 01→01 | η |

2. **Generating function.** Summing over all strings gives ⟨N;a|D^{⊗N}(|N;x⟩⟨N;y|)|N;b⟩ = [α^x β^y γ^a δ^b] P^N / √(C(N,x) C(N,y) C(N,a) C(N,b)), with

   P = (1−f)(1 + αβγδ) + f(αβ + γδ) + η(αγ + βδ).

3. **Charge and letter counting.** The charge Q = x − y = a − b is conserved. Fix ℓ copies of βδ, which forces ℓ+Q copies of αγ. The remaining m = N−2ℓ−Q sites carry the diagonal letters with generating function ((1−f)(1+pq) + f(p+q))^m. The Dicke-normalised coefficient matrix of this function is B_m := Sym^m([[1−f, f], [f, 1−f]]), and all its entries are ≥ 0. Counting multinomials gives, for Q ≥ 0,

   **S_N(Z)[b+Q, b] = Σ_ℓ η^{2ℓ+Q} g_ℓ(b) Σ_y g_ℓ(y) B_{N−2ℓ−Q}(b−ℓ, y−ℓ) Z[y+Q, y]**, with g_ℓ(y)² = C(y+Q, ℓ+Q) C(N−y−Q, ℓ) / C(N, y), which is a hypergeometric probability mass function in ℓ.

   Entries with Q < 0 follow from S_N(Z)† = S_N(Z†).
4. **Computing B_m.** B_m comes from the all-positive recursion

   B_{m+1}(k′,k) = [(1−f) s(k′)s(k) B_m(k′,k) + f t(k′)s(k) B_m(k′−1,k) + f s(k′)t(k) B_m(k′,k−1) + (1−f) t(k′)t(k) B_m(k′−1,k−1)] / (m+1),

   where s(j) = √max(m+1−j, 0) and t(j) = √j. The closed form used for checking is

   B_m(k′,k) = (1−f)^m √(k!(m−k)! k′!(m−k′)!) Σ_j ρ^{k+k′−2j} / (j!(k−j)!(k′−j)!(m−k−k′+j)!), with ρ = f/(1−f).
5. **Partial trace.** tr_{2r}(|φ⟩⟨χ|) = A_φᵀ A_χ*, where A_φ[w, x′] = h_r(w; x′+w) φ[x′+w] and h_r(w; x)² = C(2r, w) C(N, x−w) / C(M, x).
6. **Design choice: positive sums only.** The kernel is a sum of nonnegative terms, which keeps relative accuracy even for entries near 10⁻²⁵⁰. Sym-compressed outputs are of order e^{−0.143N} ≈ e^{−210}. A spectral (Krawtchouk or Pauli-weight) truncation would therefore have needed relative precision far below its truncation error. We did not use one; this rationale is [INFERENCE] and was not tested.
7. **Exactness of the window.** Each block is computed exactly on the window a, b ≤ D_out. The input support is not truncated: all 301/299 amplitudes are used.

### 2.3 Normalisation of the witness vectors

The witness amplitudes are exact dyadic rationals. Their exact squared norms are

- ‖φ₁‖² − 1 = +3.24 × 10⁻¹⁶
- ‖φ₂‖² − 1 = −1.57 × 10⁻¹⁶

These were computed with `fractions.Fraction`; the overlap is exactly 0.

- **Default "exact" mode.** Each vector is multiplied by 1/‖φ_i‖, computed with 60-digit mpmath and then applied in float64. The state is therefore (1/2)(|φ̂₁⟩⟨φ̂₁| + |φ̂₂⟩⟨φ̂₂|).
- **"raw" mode.** The vectors are used as given, and each block is normalised by its own trace. This changes the mixture weights by about 10⁻¹⁶.
- **Comparison.** The two modes differ by 5.8 × 10⁻¹⁶ nats, which is at the noise level.

## 3. Implementation (`code/`)

- `sym_depol.py` is the evaluator: hi/lo log-factorial table, B_m sliding windows, partial trace, S_N, block assembly, entropies. It runs in float64 with eigenvalues from LAPACK `eigvalsh` (Accelerate).
- `run_witness.py` is the M = 2000 driver. It uses mpmath block weights from the exact rational p.
- `bruteforce.py` is an independent 2^M reference.
- `validate_small.py` and `precision_checks.py` are the checks.
- `compare_worker.py` performs the audit comparison (it was written and run only after §5).
- `summarize.py` writes `evidence/SUMMARY.json`.

Production settings:

- Blocks: r ∈ [121, 440], i.e. log p_r > −60, 320 blocks.
- Excluded weight: 2.45 × 10⁻²⁶. Its contribution is ≤ 1.7 × 10⁻²⁶ nats, by |S(ρ_r^B) − S(ρ_r^RB)| ≤ S(ρ_R) ≤ ln 2.
- D_out = 440.
- Runtime: about 7 minutes per evaluation, single thread, about 0.9 GB RSS.

## 4. Small-M validation (`evidence/validation_small.json`)

| check | scope | max deviation |
|---|---|---|
| A: S_N vs Π D^{⊗N}(Z) Π, entrywise | random complex Z; N ≤ 8; 6 values of η | 1.7 × 10⁻¹⁵ |
| B: E_r† D^{⊗M}(X) E_r vs c_r S_N(tr_{2r} X), entrywise | random complex PSD X on Sym^M; M ≤ 8; all r; 3 values of η | 2.2 × 10⁻¹⁶ |
| C: p_r formula vs m_r tr(brute-force block); Σ p_r = 1 | M ≤ 8 | relative 1.0 × 10⁻¹⁴; sum 5.6 × 10⁻¹⁶ |
| D: I_c vs brute-force S(B) − S(RB) on R ⊗ (C²)^{⊗M} | 216 cases, see below | 2.6 × 10⁻¹⁴ |

The 216 cases in check D cover:

- M = 2 to 10;
- η ∈ {0.15, 0.5, 2/3, 0.732, 11/15, 0.9};
- supports: full, mod-3 (residues 0 and 1), mod-3 complex, mod-2 complex;
- non-orthogonal pairs and random q;
- |I_c| up to 0.67.

## 5. M = 2000 results (`evidence/ic_*.json`, per-block records included)

| run | I_c (nats) | I_c (bits) |
|---|---|---|
| p = 1/5, D = 440, exact normalisation (baseline) | 7.9111709477 × 10⁻⁹ | 1.1413407094 × 10⁻⁸ |
| p = 1/5, D = 360 | 7.9111701772 × 10⁻⁹ | 1.1413405982 × 10⁻⁸ |
| p = 1/5, D = 300 | 7.9111703389 × 10⁻⁹ | 1.1413406216 × 10⁻⁸ |
| p = 1/5, D = 250 (window too small; shown to expose truncation) | 7.7965070894 × 10⁻⁹ | 1.1247982114 × 10⁻⁸ |
| p = 1/5, D = 440, raw vectors | 7.9111703665 × 10⁻⁹ | 1.1413406255 × 10⁻⁸ |
| p = 1/5, D = 440, amplitudes × (1 ± 2⁻⁵² noise), seed 1 / seed 2 | 7.9111709518 × 10⁻⁹ / 7.9111704055 × 10⁻⁹ | 1.1413407100 × 10⁻⁸ / 1.1413406312 × 10⁻⁸ |
| p = 1/5, D = 440, amplitudes × (1 ± 10⁻¹² noise) | 7.9111704428 × 10⁻⁹ | 1.1413406366 × 10⁻⁸ |
| p = 201/1000, D = 440 | −5.3158102853 × 10⁻⁹ | −7.6690931370 × 10⁻⁹ |
| p = 1/4, D = 440 | −6.8663317774 × 10⁻⁷ | −9.9060228043 × 10⁻⁷ |

Structure of the p = 1/5 result:

- **Per-block differences.** S(ρ_r^B) − S(ρ_r^RB) decreases smoothly from +6.6 × 10⁻⁷ at r = 140 to −9.3 × 10⁻⁷ at r = 440. It crosses zero near r ≈ 270, and the weights p_r peak at r = 266.
- **Cancellation.** The positive part sums to +3.23 × 10⁻⁸ nats and the negative part to −2.44 × 10⁻⁸ nats.
- **Truncation diagnostics, D = 440:**
  - The largest last-diagonal population in any block, relative to its trace, is 5.4 × 10⁻⁵⁸.
  - The relative mismatch between the window trace and c_r λ₀ is at most 2.0 × 10⁻¹⁴, which is pure rounding.
  - The smallest B eigenvalue is +2.5 × 10⁻¹⁰⁶. The most negative RB eigenvalue is −2.9 × 10⁻¹⁷; such values are dropped.

## 6. Numerical error estimate (non-rigorous)

**Building blocks** (`evidence/precision_checks.json`):

- B_m recursion vs the 40-digit closed form, 188 sampled entries with m ≤ 2000 and values down to 10⁻²⁶⁵: maximum relative error 8.6 × 10⁻¹⁴.
- Coefficients g and h vs mpmath: maximum relative error 2.8 × 10⁻¹⁶.

**Whole blocks at the true size, float64 vs mpmath.** M = 2000 and r ∈ {200, 267, 340}, on a reduced problem: the witness truncated to x ≤ 40 and renormalised, with D_out = 70. A separate straightforward 40-digit mpmath implementation uses the closed-form B_m, explicit loops and `mp.eigsy`. The |Δ(S_B − S_RB)| per block are 1.6 × 10⁻¹⁵, 8.1 × 10⁻¹⁶ and 3.7 × 10⁻¹⁵ nats.

**Eigensolver sensitivity, production blocks** (r = 200, 267, 340; D = 440): eigvalsh, SVD, and eigvalsh after a random orthogonal similarity were compared.

- The spread is ≤ 4.4 × 10⁻¹⁴ nats per block.
- eigvalsh vs SVD alone agree to ≤ 6.9 × 10⁻¹⁵.
- The rotated variant destroys the graded structure, so it is pessimistic.

**Global.**

- The seven p = 1/5 variants with D ≥ 300 span 7.7 × 10⁻¹⁶ nats.
- Window truncation is negligible for D ≥ 300; the D = 250 run shows it does matter (−1.1 × 10⁻¹⁰ nats).
- Excluded blocks contribute ≤ 1.7 × 10⁻²⁶.
- **Estimate:** |δI_c| ≲ 5 × 10⁻¹⁴ bits, taking the pessimistic per-block eigensolver bound and weighting by Σ p_r = 1. The observed spread is about 10⁻¹⁵.

**Conclusion.** The value lies inside [1.12885 × 10⁻⁸, 1.14364 × 10⁻⁸] bits with a margin of at least 460 times this estimate. This is not a proof: binary64 rounding was not enclosed.

## 7. Audit of the worker's PROOFS.md and cert.py

These files were read only after §5 was finished. Paths are relative to `../depolarizing-parent-inputs-v1/`, and line numbers refer to the pinned snapshot.

| item | finding |
|---|---|
| Channel parameterisation | PROOFS.md:3 and `cert.py:92` (η = 1 − 4p/3) are identical to ours. |
| Sector map | PROOFS.md:23-38 obtains Ψ_N = (ab)^λ P_N D^{⊗N}(L_{M→N}·) P_N by GL(2) polarisation, with a = 1−f and b = f. This is the same identity as our singlet-embedding result c_r S_N(tr_{2r}·), reached by a different route. |
| Loss and add formulas | PROOFS.md:54-55, `cert.py:163-196`: they agree with our hypergeometric partial-trace coefficients (re-derived). |
| Sector weights and multiplicities | PROOFS.md:27, `cert.py:117-125`: the formula is identical to ours. Their pN agrees with our p_r to 1.8 × 10⁻¹⁵ relative over all 220 sectors. |
| π_s weights | PROOFS.md:26, `cert.py:128-139`: re-derived as C(N+1,s+1) η^s b^{N−s}/q_N; consistent. |
| Purification and reference ordering | PROOFS.md:40-42 and `cert.py:382-383,427-441`: the RB blocks are √(q_i q_j) \|i⟩⟨j\| ⊗ Φ(\|φ_i⟩⟨φ_j\|), and blocks with i > j are conjugate transposes. Identical to ours. |
| Units | PROOFS.md:4 and `cert.py:62` use bits. Our per-sector nats/ln 2 values fall inside their per-sector intervals. |
| Normalisation | `cert.py:487-493` computes ‖φ_i‖² in Arb from the float amplitudes. `cert.py:381-383` and `cert.py:396` divide by it, which is per-vector exact normalisation and the same as our "exact" mode. S(ρ) = H(q) (`cert.py:494-496`, `combine.py:28-29`) is justified because the overlap is exactly 0. Our raw-vs-exact difference is 5.8 × 10⁻¹⁶ nats. **No discrepancy.** |
| Truncation, D = 440 | `cert.py:101` reads D from the witness. The add step is cut at Dmax (`cert.py:179-196`), which is exact on the kept block (PROOFS.md:57-58). The flag channel (`cert.py:385-398,446-455`, PROOFS.md:101-105) gives a valid DPI lower bound. Independently, the populations at a = 440 are ≤ 5.4 × 10⁻⁵⁸, and D = 300, 360 and 440 agree to 8 × 10⁻¹⁶. Their reported `max_w_tail` of 1.2 × 10⁻²⁶ is their error radius, not real leakage. **D = 440 is ample; no discrepancy.** |
| π-tail and sector tail | `cert.py:535-540` (pitail 1e-40), `cert.py:457-461`, `combine.py:46-54`. Their `rest_mass_hi` (3.6230631 × 10⁻¹³) equals our independently computed mass outside N ∈ [1236, 1674] (3.6230631 × 10⁻¹³). **Provenance gap:** the effective `--ptail` for `combine.py` lies in (7.6 × 10⁻¹⁴, 1.1 × 10⁻¹³], not the default 1e-30 (`combine.py:19`, `cert.py:574`), and `TOTAL.json` does not record it. The bound remains rigorous: ±3.6 × 10⁻¹³ bits, included. |
| Witness identity | `TOTAL.json` `witness_sha256` is 43117f99…, which is sha256(`json.dumps(w, sort_keys=True)`) (`cert.py:566-567`), not the file hash. We verified that the pinned file canonicalises to exactly 43117f99…: **same witness**. |
| Q ≥ I_c/M and p-monotonicity | PROOFS.md:6,10-14: D_{η₂} = D_{η₂/η₁} ∘ D_{η₁} together with data processing and LSD. Correct. |
| Snapshot vs PROOFS | PROOFS.md:126-127 says the lowest-cluster refinement postdates this run. The snapshot `cert.py:277-329` indeed lacks it; it affects only upper bounds. Consistent. |
| Per-sector enclosures | All 220 of our values fall inside, at relative position 0.81–0.88 of each interval. The intervals have width (1.1–2.0) × 10⁻¹⁰, so the total enclosure width is set by the per-sector Gershgorin/Ostrowski looseness, not by the tails. |
| Not audited here | The double-double rigorous error model (PROOFS.md §3, `dd.py`), the Arb entropy enclosure (PROOFS.md §5), and the claim that the earlier rigorous record is 0.194868. |

**No discrepancy affecting the claimed enclosure was found.** Remaining caveats are provenance only:

- the ptail used by `combine.py` is not recorded;
- the witness hash is a canonical-JSON hash;
- the worker's brute-force cross-checks cover M ≤ 7 only (PROOFS.md:43).

## 8. Commands

Python: `/Users/jinleic/.local/state/research-explorer/venv/bin/python` (Python 3.14, numpy 2.4.3 with Accelerate, mpmath 1.3.0). All commands are run from `code/` with `OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1`.

```
python validate_small.py                                   # §4 (≈45 s)
python run_witness.py --p 1/5 --Dout 440 --out ../evidence/ic_p1_5_D440.json        # ≈7 min
python run_witness.py --p 201/1000 --Dout 440 --out ../evidence/ic_p201_1000_D440.json
python run_witness.py --p 1/4 --Dout 440 --out ../evidence/ic_p1_4_D440.json
python run_witness.py --p 1/5 --Dout {250,300,360} --out ../evidence/ic_p1_5_D{...}.json
python run_witness.py --p 1/5 --Dout 440 --norm raw --out ../evidence/ic_p1_5_D440_raw.json
python run_witness.py --p 1/5 --Dout 440 --perturb 2.220446049250313e-16 --seed {1,2} --out ...
python run_witness.py --p 1/5 --Dout 440 --perturb 1e-12 --seed 3 --out ../evidence/ic_p1_5_D440_pert1e-12.json
python precision_checks.py                                 # §6 (≈75 s)
python compare_worker.py                                   # §7, run after §5
python summarize.py                                        # evidence/SUMMARY.json (incl. sha256 of evidence files)
```

**Independence record.** Before the evaluator and the three M = 2000 runs were finished, only MANIFEST.json (for hash checks) and the witness JSON were opened, together with the claim text in the assignment. PROOFS.md, cert.py, combine.py, TOTAL.json and the sector files were opened afterwards, for §7 only. dd.py and make_witness.py were never opened. No worker code was imported, copied or adapted.
