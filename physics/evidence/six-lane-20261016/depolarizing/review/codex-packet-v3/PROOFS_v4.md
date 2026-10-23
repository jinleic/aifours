# Proofs behind `code/cert.py` — v4 (= v3 text + exposition fixes F1–F6 of the parent bridge review; code unchanged: code_snapshot_v3)
# (historical heading of v3 follows)
# Proofs behind `code/cert.py` — v3 (frozen for the v3 reruns; supersedes PROOFS.md v1 and PROOFS_v2.md for
# code_snapshot_v3; v1/v2 are kept unchanged as historical records)

Conventions. `N_p(ρ) = (1−p)ρ + (p/3)(XρX+YρY+ZρZ) = D_η(ρ) := ηρ + (1−η)tr(ρ) I/2`, `η = 1 − 4p/3`,
`a = (1+η)/2`, `b = (1−η)/2` (so `a − b = η`, `a + b = 1`). Logs base 2. `h(x) = −x log x`.
Imported (classical) facts: Schur–Weyl duality for `(C²)^{⊗M}`; data processing for coherent information
(Schumacher–Nielsen 1996); LSD: `Q(N) ≥ I_c(ρ, N^{⊗M})/M`; concavity and almost-convexity of von Neumann
entropy; Alicki–Fannes–Winter continuity (Winter, CMP 347, 2016, Lemma 2); Ostrowski's theorem
(Horn–Johnson, Matrix Analysis, Thm 4.5.9); Gershgorin; IEEE-754 binary64 correct rounding.

## §0 Monotonicity in p and the capacity statement

`D_{η1} ∘ D_{η2} = D_{η1 η2}`. For `0 ≤ η2 ≤ η1 ≤ 1`, `D_{η2} = D_{η2/η1} ∘ D_{η1}` with `D_{η2/η1}` CPTP, so by data
processing `I_c(ρ, D_{η2}^{⊗M}) ≤ I_c(ρ, D_{η1}^{⊗M})`. A certified `I_c(ρ, N_{p0}^{⊗M}) > 0` therefore gives
`Q(N_p) ≥ I_c(ρ, N_{p0}^{⊗M})/M > 0` for every `0 ≤ p ≤ p0`.

## §1 Sector decomposition (independent re-derivation of 2609.39747 Thm II.3/II.9)

**Lemma 1 (two-row Schur–Weyl).** `(C²)^{⊗M} ≅ ⊕_N Q_N ⊗ P_N`, `N ∈ {M, M−2, …}`, `Q_N ≅ Sym^N(C²)`,
`m_N := dim P_N = C(M,λ) − C(M,λ−1)` with `λ = (M−N)/2`, and for every `A ∈ L(C²)`:
`A^{⊗M} ≅ ⊕_N (det A)^{λ} S_N(A) ⊗ I_{P_N}`, `S_N(A) := A^{⊗N}|_{Sym^N}`. (Standard; proved from first principles in
2608.15870 App. E, Lemma E1; extends from GL(2) to all A by continuity.)

**Lemma 2.** For `X ∈ L(Sym^M)`: `D_η^{⊗M}(X) ≅ ⊕_N p_N Φ_N(X) ⊗ I_{P_N}/m_N` with
`Φ_N = Σ_{s=0}^{N} π_s C_{s→N} ∘ L_{M→s}`, where `L_{M→s} = tr_{M−s}` (restricted to Sym), the cloner
`C_{s→N}(Z) = (s+1)/(N+1) · P_N (Z ⊗ I^{⊗(N−s)}) P_N`, and
`π_s = C(N+1,s+1)(2η)^{s+1}(1−η)^{N−s} / ((1+η)^{N+1} − (1−η)^{N+1})`,
`p_N = m_N (ab)^{λ} (a^{N+1} − b^{N+1})/η`.

*Proof.* Products `|u⟩⟨v|^{⊗M}` span `L(Sym^M)` (polarization). With `g = ⟨v|u⟩` and
`A_uv := D_η(|u⟩⟨v|) = b g I + η|u⟩⟨v|`, `det A_uv = b²g² + bηg² = ab g²`, and `D_η^{⊗M}(|u⟩⟨v|^{⊗M}) = A_uv^{⊗M}`.
By Lemma 1 the output is block diagonal with Q_N-part `Ψ_N(|u⟩⟨v|^{⊗M}) = (ab)^λ g^{2λ} S_N(A_uv)`, extended
linearly. Since `L_{M→N}(|u⟩⟨v|^{⊗M}) = g^{M−N} |u⟩⟨v|^{⊗N}` and `P_N A^{⊗N} P_N = S_N(A)`,
`Ψ_N = (ab)^λ · P_N D_η^{⊗N}( L_{M→N}(·) ) P_N`. Expanding `D_η = η·id + b·tr(·)I` over subsets S of the N qubits,
`P_N D_η^{⊗N}(Y) P_N = Σ_s C(N,s) η^s b^{N−s} P_N (L_{N→s}(Y) ⊗ I^{⊗(N−s)}) P_N
 = Σ_s C(N+1,s+1) η^s b^{N−s} C_{s→N}(L_{N→s}(Y))` (permutations are absorbed by P_N; `C(N,s)(N+1)/(s+1) = C(N+1,s+1)`).
With `L_{N→s} L_{M→N} = L_{M→s}` and tr-preservation of `C, L`, `tr Ψ_N(X) = (ab)^λ q_N tr X`,
`q_N = Σ_s C(N+1,s+1) η^s b^{N−s} = ((η+b)^{N+1} − b^{N+1})/η = (a^{N+1} − b^{N+1})/η`. Normalizing gives Φ_N, π_s
(multiply numerator/denominator by `2^{N+1}`) and `p_N = m_N tr Ψ_N(X)`. ∎

**Corollary.** For `|Ψ⟩ = Σ_i √q_i |i⟩_R |φ_i⟩` with `φ_i ∈ Sym^M`, linearity gives
`(id_R ⊗ D^{⊗M})(Ψ) ≅ ⊕_N p_N (id ⊗ Φ_N)(Ψ) ⊗ I/m_N`; the multiplicity entropies `H(p) + Σ p_N log m_N` cancel in
`S(B) − S(RB)`, so `I_c(ρ, D^{⊗M}) = Σ_N p_N I_c(ρ, Φ_N)`.
Checks: brute force on `2^M` dims for M ≤ 7 (evidence/test_cert_small.log, 15/15 inside enclosures); KG's
published 45-qubit state R reproduced inside both of KG's certified intervals (evidence/controls/).

## §2 Single-particle steps (Schwinger form)

Identify `Sym^n` with n bosons in two modes; Dicke `|n;x⟩ = |n−x, x⟩` (x = number of `|1⟩`s). For `ψ ∈ Sym^n`,
`P_{n+1}(|ψ⟩ ⊗ |i⟩) = (n+1)^{−1/2} a_i^† |ψ⟩` and `(⟨i| ⊗ I)|ψ⟩ = n^{−1/2} a_i|ψ⟩` (standard first↔second
quantization identities; checked on occupation basis states). Hence
`L_{n→n−1}(X) = tr_1 X = (1/n) Σ_i a_i X a_i^†`,
`C_{n→n+1}(Z) = (n+1)/(n+2) Σ_i P(Z⊗|i⟩⟨i|)P = (1/(n+2)) Σ_i a_i^† Z a_i`, and `C_{s→N} = C_{N−1→N} ∘ … ∘ C_{s→s+1}`
because `P_{n+2}(P_{n+1} ⊗ I) = P_{n+2}`. In the Dicke basis:
`[L(X)]_{xy} = (1/n)[√((n−x)(n−y)) X_{xy} + √((x+1)(y+1)) X_{x+1,y+1}]`,
`[C(Z)]_{xy} = (1/(n+2))[√((n+1−x)(n+1−y)) Z_{xy} + √(xy) Z_{x−1,y−1}]`.
Horner: with `Y_s = L_{M→s}(X)`, `Z_{smin} = π_{smin} Y_{smin}`, `Z_{s+1} = C_{s→s+1}(Z_s) + π_{s+1} Y_{s+1}` gives
`Z_N = Σ_{s≥smin} π_s C_{s→N}(Y_s)`. C never lowers x and L never raises it, so entries with `x, y ≤ D` (resp. the
input support) are computed exactly from entries in the same range: truncation is exact on the kept block.

## §3 Floating-point error model (double-double on nonnegative operands)

`u = 2^{−53}`; every binary64 op is correctly rounded. Standard model *with* gradual underflow:
`fl(x) = x(1+δ) + η`, `|δ| ≤ u`, `|η| ≤ 2^{−1075}`, `δη = 0` (IEEE 754; numpy float64 on arm64 does not flush
subnormals). Each DD primitive therefore has error `≤ ε·|exact| + A_op` with `A_op ≤ 2^{−1000}`: if every
intermediate of the primitive is ≥ 2^{−969} in magnitude, TwoSum/TwoProd/Sterbenz steps are exact and only the
`δ` parts remain; otherwise the failing sub-computation (e.g. a subnormal TwoProd error word, a Dekker split of a
subnormal `π·Y` product) only involves quantities below `2^{−1015}`, so its total absolute damage is `< 2^{−1000}`.
The relative statements below are for the `δ` parts (normal range).
Inputs: every complex amplitude vector is split exactly into ≤ 4 entrywise nonnegative real parts with phases
`1, −1, i, −i`; Φ_N is linear, so each operator `|c_i⟩⟨c_j|` is a phase-weighted sum of ≤ 16 nonnegative outer
products, each formed exactly by TwoProd (`dd.two_prod`). Every subsequent quantity in the recursion is a sum
and product of nonnegative numbers.
Primitive bounds (`δ` parts) for nonnegative DD operands `x = x_h + x_l`, `|x_l| ≤ u x_h` (normalized output of
quick_two_sum):
- `add`: `two_sum` exact; neglected/rounded terms: `fl(x_l + y_l)` (≤ u·u(x_h+y_h)), `fl(e + t)`
  (≤ u(|e|+|t|) ≤ 3u²(x_h+y_h)); final quick_two_sum exact (|e| ≪ s). Total ≤ 4.2 u² (x+y).
- `mul`: `two_prod` exact (Dekker split, no FMA); cross terms `fl(x_h y_l) + fl(x_l y_h)` rounded twice
  (≤ 4.1 u² x y), `fl(e + cross)` (≤ 3.1 u² x y), neglected `x_l y_l` (≤ u² x y). Total ≤ 8.3 u² x y.
- `sqrt_int(m)`, `recip_int(m)` (integers < 2^52): Newton correction from a correctly rounded seed with the
  residual computed exactly by TwoProd and Sterbenz: relative error ≤ 3.1 u².
We use the single constant `ε = 2^{−100} = 64 u²` for every primitive (a factor ≥ 7 slack).
Per loss step the longest chain is: coefficients (`√` twice, outer product: ≤ 2·3.1u² + ε), product with Y (ε),
add (ε), product with `1/n` (ε + 3.1u²): ≤ 5ε. Per add step (incl. `+ π_{s+1} Y_{s+1}`): ≤ 6ε plus the relative
representation error of `π_{s+1}` as a DD (≈ 1e−32 relative: a DD carries ~106 bits; the actual per-sector maximum
`max(pis_rel)` is computed in Arb and added to relE).
Since all terms are nonnegative, relative errors of summands combine by max and of factors by addition, so
after a chain of length L every computed entry `ẑ` satisfies `|ẑ − z| ≤ ((1+ε)^L − 1 + max δπ) z`; cert.py uses
`L = 10 · ((M − smin) + (N − smin)) + 20` (≥ 1.6× the derived count) and inflates by 1.01.
Underflow control: nonzero amplitudes must be ≥ 1e−100 (so all inputs ≥ 1e−200); after every step entries
below `2^{−900}` are set to 0. Intermediates (low words, TwoProd error words, `π·Y` products with `π` as small as
1e−40) CAN be subnormal; no normality is assumed. Absolute contributions: (i) a flushed perturbation R_t
(entries ≤ 2^{−900}, ≤ d² of them, d ≤ 10⁴) and (ii) the `A_op` terms of all primitives (≤ 12 primitives per
entry per step) both reach the output through trace-non-increasing CP maps (the remaining add steps, or
`Σ_{s'} π_{s'} C L` with `Σ π ≤ 1`), hence change any output entry by at most their trace norm:
(i) ≤ 10⁶ steps · d² · 2^{−900} ≈ 1.2·10⁻²⁵⁷, times ≤ 16 phase parts < 2·10⁻²⁵⁶; (ii) ≤ 10⁶ · 10⁸ · 12 · 2^{−1000}
< 2·10⁻²⁸⁶. Their sum is far
below `ABS_ENTRY = 1e−250` per entry, which cert.py adds to every entry radius. (Exact-arithmetic spot audit of
dd.py primitives by the parent: institute/runs/six-lane-2026-10-16/review/check_depolarizing_dd_exact.py —
finite controls, not a substitute for this argument.)

## §4 Truncation, tails, sector bounds

Lower bound. `T_D(Z) = P_D Z P_D + tr(Q_D Z)|⊥⟩⟨⊥|` (`Q_D` = projector onto `x > D`) is CPTP; data processing
gives `I_c(ρ, Φ̂) ≥ I_c(ρ, T_D∘Φ̂)`. For mod-k inputs (`φ_i` supported on `x ≡ r_i`, `r_i` distinct) every
`Φ(|φ_i⟩⟨φ_j|)` is supported on `x − y ≡ r_i − r_j` (U(1) covariance of D and of both steps), so the flag block of
`RB` is `diag(q_i w_i)`, `w_i = 1 − tr P_D Φ̂(φ_i)`, and B and RB split into k residue blocks. When D ≥ N no
truncation occurs and the flag weight is exactly 0.
`π`-tail: `Φ_N = (1−ε)Φ̂ + εΦ_R` with `Φ̂ = Σ_{s≥smin} π_s C L / (1−ε)`. For any channel mixture
`I_c(ρ, Σ p_k N_k) ≥ Σ p_k I_c(ρ, N_k) − H(p)` (concavity of S(B), `S(RB) ≤ Σ p_k S(RB_k) + H(p)`), and
`I_c ≥ −S(ρ)`, so `I_c(ρ, Φ_N) ≥ (1−ε) I_c(ρ, Φ̂) − ε S(ρ) − h₂(ε)`.
Uncomputed sectors (mass `p_rest`, computed rigorously as a sum of Arb balls) contribute `≥ −p_rest S(ρ)`.
Upper bound (used only for sign controls). `I_c(ρ, Σ p_k N_k) ≤ Σ p_k I_c(ρ,N_k) + H(p)` and `I_c ≤ S(ρ)` handle
tails/sectors. Truncation: pinching `Ω ↦ (I⊗P)Ω(I⊗P) + (I⊗Q)Ω(I⊗Q)` changes Ω by
`‖PΩQ + QΩP‖_1 ≤ 2√(w(1−w))`, so by AFW (`d_R = r`)
`I_c(Φ̂) ≤ (1−w) I_c^{P} + w log r + 2√w log r + (1+√w) h₂(√w/(1+√w))`, and
`(1−w) I_c^{P} = I_c(T_D∘Φ̂) − [h(Σq_iw_i) − Σ h(q_i w_i)] ≤ I_c(T_D∘Φ̂) + Σ_i h(q_i w_i)`.

## §5 Entropy enclosure of a Hermitian PSD block A (tr A ≤ 1)

V = binary64 eigenvectors of the midpoint (exact dyadic matrix). In Arb: `W = V*AV`, `G = V*V`,
`δ ≥ ‖G − I‖_F ≥ ‖G − I‖_2` (require δ < 1e−6). Ostrowski: `λ_k(W) = θ_k λ_k(A)`, `θ_k ∈ [1−δ, 1+δ]` (sorted).
Gershgorin for Hermitian W: every eigenvalue lies in `∪_i [W_ii − r_i, W_ii + r_i]`, `r_i ≥ Σ_{j≠i}|W_ij|`; a connected
component of k discs contains exactly k eigenvalues (continuity of eigenvalues along `diag W + t(W − diag W)`).
Dividing by θ (outward) gives intervals for A's eigenvalues, clipped to [0,1]; on each component the k
eigenvalues contribute to `S = Σ h(λ)` between `k·min h` and `k·max h` over the interval (h concave, increasing on
[0,1/e], decreasing on [1/e,1], max `log₂e/e`). Endpoint values of h are Arb enclosures; all conversions to
binary64 are rounded outward (`nextafter`).
Lowest-cluster refinement (code versions after the M=2000 p=1/5 run; the snapshot in
`evidence/cert/code_snapshot_M2000_p1_5/` predates it): the lowest Gershgorin component holds the k smallest
eigenvalues of W, which are ≥ 0 because `W = V*AV` with A PSD. Ky Fan's minimum principle gives
`Σ_{j≤k} λ_j(W) ≤ tr(P W P)` for the coordinate projector P onto the component's indices, i.e. `≤ Σ_{i∈c} W_ii`.
By Ostrowski `λ_j(A) ≤ λ_j(W)/(1−δ)`, so the k smallest eigenvalues of A have total mass
`m ≤ Σ_{i∈c} W_ii/(1−δ)`; since h is concave and increasing on [0,1/e], `Σ_{j≤k} h(λ_j(A)) ≤ k·h(m/k)` when
`m/k ≤ 1/e`. Only the upper entropy bound uses this; the lower bound for that cluster stays `k·min h ≥ 0`.

**Normalization and weights.** The certified state is `φ_i = a_i/‖a_i‖` for the dyadic witness vectors `a_i` exactly
as stored (unit norm not assumed). The recursion acts on the unnormalized exact outer products `a_i a_j^T`;
`‖a_i‖²` is enclosed in Arb and divided out in ball arithmetic in every B/RB entry (`q_i/‖a_i‖²`,
`√(q_i q_j)/(‖a_i‖‖a_j‖)`, times `1/Σ_{s≥smin} π_s`) and in the flag weights. `q_i` are exact rationals with
`Σ q_i = 1`. `S(ρ) = H(q)` is used only when the `a_i` have disjoint supports (then the `φ_i` are orthonormal).

## §6 What a certificate is (verification protocol, v3)

A run writes one JSON record per sector carrying `witness_sha256`, `cert_py_sha256`, `dd_py_sha256`, `M`, `p`,
`D_param`, `ptail`, `pitail` and the rigorous sector bounds. `combine.py` rejects (with a named reason) records from
another witness or code version, parameter mismatches, duplicates, non-finite or inverted intervals, sectors outside
the ptail-selected set, and missing selected sectors (unless `--allow-missing`, in which case each omitted sector is
bounded by `±S(ρ)·p_N` and its mass reported). Records are **replayable evidence, not proof**: a record whose numbers
were altered consistently passes combine.py; `replay.py` recomputes sectors with the same code and compares every
field bitwise. Acceptance requires replay of every sector (a full rerun) or an independent recomputation.
The optional C kernel (`code/ddkern.c`) is NOT part of v3 and was not used for any certificate.

## §7 Exposition fixes F1–F6 (parent bridge review, institute/runs/six-lane-2026-10-16/review/depolarizing-sector-bridge-review.note.md; no math error found)

**F1 (split and renormalization).** `ε_N := Σ_{s<s_min} π_s`, `Φ̂_N := (1−ε_N)^{−1} Σ_{s≥s_min} π_s C_{s→N} L_{M→s}`,
`Φ_R := ε_N^{−1} Σ_{s<s_min} π_s C_{s→N} L_{M→s}`; both CPTP and `Φ_N = (1−ε_N)Φ̂_N + ε_N Φ_R`. The Horner recursion
returns the UNNORMALIZED `Z_N = (1−ε_N) Φ̂_N(X)`; every kept block and every flag weight is divided by
`1−ε_N = Σ_{s≥s_min} π_s` (cert.py v3: `inv_mass`), i.e. `w_i = 1 − tr(P_D Z_N[a_i a_i^T])/(‖a_i‖²(1−ε_N))`. The flag never
absorbs `ε_N`; `ε_N` enters only through the almost-convexity step of §4.
**F2 (residues).** The flag argument needs pairwise distinct residues mod k (k ≥ 2), or more generally pairwise
disjoint Dicke supports: since `x − y` is conserved by both steps, the diagonal of `Φ(X)` depends only on the diagonal
of `X`, so `tr(Q_D Φ(|φ_i⟩⟨φ_j|)) = 0` whenever `φ_i, φ_j` have disjoint Dicke supports.
**F3 (kept off-diagonal reference blocks).** Only the FLAG reference block is diagonal (`diag(q_i w_i)`). The kept block
retains `√(q_i q_j) P_D Φ̂(|φ_i⟩⟨φ_j|) P_D` for `i ≠ j` (cert.py v3 builds RB from all `(i,j)` operators via `sc_RB`);
dropping them would keep the lower bound valid but break the upper bound of §4.
**F4 (flag identity, explicit signs).** With `Ω_P` the kept part (trace `1−w`, `w = Σ_i q_i w_i`) and `I_c^P` its
normalized coherent information: `I_c(ρ, T_D Φ̂) = (1−w) I_c^P + h(w) − Σ_i h(q_i w_i) = (1−w) I_c^P − w H({q_i w_i/w})`;
the flag term is ≤ 0. (Convention: `(1−w) I_c^P := 0` when `w = 1`.)
**F5 (§1 details).** The `(M−λ, λ)` isotypic block of `A^{⊗M}` is `V_N(π(A) ⊗ I_{m_N})V_N^*` with ONE fixed intertwiner
`V_N` (Schur's lemma on U(2)); holomorphic extension carries the identity to all of `M_2(C)`, covering singular
`A_uv` (g = 0). `P_N (Y_S ⊗ I) P_N` is independent of the subset S because `P_N P_σ = P_N` for permutations σ and
`Y ∈ L(Sym^N)`. The cloner is trace-preserving because `tr_{N−s} P_N = ((N+1)/(s+1)) P_s` (Schur's lemma).
**F6 (AFW hypotheses).** Winter (CMP 347, 2016), Lemma 2: for states with `½‖ρ−σ‖₁ ≤ ε ≤ 1` on `A⊗B`,
`|H(A|B)_ρ − H(A|B)_σ| ≤ 2ε log dim A + (1+ε) h₂(ε/(1+ε))`; here `A = R` with `dim R = rank ρ = r` (the pinching acts
on B only) and `ε = √w ≤ 1`.
Optional tightening noted by the reviewer (upper bound without `h₂(ε)`) is not used.
