# Proofs behind `code/cert.py` (rigorous I_c enclosures for symmetric inputs)

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
representation error of `π_{s+1}` as a DD (computed in Arb, ≤ 1e−40 in practice, added explicitly).
Since all terms are nonnegative, relative errors of summands combine by max and of factors by addition, so
after a chain of length L every computed entry `ẑ` satisfies `|ẑ − z| ≤ ((1+ε)^L − 1 + max δπ) z`; cert.py uses
`L = 10 · ((M − smin) + (N − smin)) + 20` (≥ 1.6× the derived count) and inflates by 1.01.
Underflow control: nonzero amplitudes must be ≥ 1e−100 (so all inputs ≥ 1e−200); after every step entries
below `2^{−900}` are set to 0. Intermediates (low words, TwoProd error words, `π·Y` products with `π` as small as
1e−40) CAN be subnormal; no normality is assumed. Absolute contributions: (i) a flushed perturbation R_t
(entries ≤ 2^{−900}, ≤ d² of them, d ≤ 10⁴) and (ii) the `A_op` terms of all primitives (≤ 12 primitives per
entry per step) both reach the output through trace-non-increasing CP maps (the remaining add steps, or
`Σ_{s'} π_{s'} C L` with `Σ π ≤ 1`), hence change any output entry by at most their trace norm:
(i) ≤ 10⁶ steps · d² · 2^{−900} < 2·10⁻²⁶²; (ii) ≤ 10⁶ · 10⁸ · 12 · 2^{−1000} < 2·10⁻²⁸⁶. Their sum is far
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

## Additions in v2 (PROOFS.md = v1 is pinned by the parent at SHA-256 f5804604…; v1 text above is unchanged)

**A1. Normalization and weights (exposition gap in v1; code unchanged).** The certified state is
`φ_i = a_i/‖a_i‖` for the dyadic witness vectors `a_i` exactly as stored; unit norm is not assumed. The DD
recursion acts on the unnormalized exact outer products `a_i a_j^T` (TwoProd); `‖a_i‖²` is enclosed in Arb and divided
out in ball arithmetic in every B/RB entry (`q_i/‖a_i‖²`, `√(q_i q_j)/(‖a_i‖‖a_j‖)`, times `1/Σ_{s≥smin} π_s`) and in the
flag weights `w_i = 1 − tr P_D Φ'(a_i a_i^T)/(‖a_i‖² Σπ)`. The weights `q_i` are exact rationals (`Σ q_i = 1`).
`S(ρ) = H(q)` is used only when the `a_i` have disjoint supports (then the `φ_i` are exactly orthonormal and
`ρ` has spectrum `q`); otherwise `S(ρ) ≤ log₂ r`.

**A2. C kernel (`code/ddkern.c`, optional fast path).** Same DD algorithms as `dd.py` except TwoProd uses one
explicit `fma` (exact for normal results; the subnormal case is covered by the `A_op` term of §3). Compiled with
`-ffp-contract=off -fno-fast-math` so that no other contraction or reassociation occurs. The error constants of §3
apply verbatim because they only use exactness of TwoSum/TwoProd and correct rounding of the remaining ops.
Any certificate produced with the C path must be cross-checked against the numpy path on at least one sector
(bitwise equality is not expected: Dekker vs FMA TwoProd give identical exact products but the code paths differ
only there, so outputs should agree exactly; any difference is a bug).

**A3. Corrections after the Codex hostile review (verdict accept-with-fixes, no fatal issue;
`codex-review-M2000-p1_5.json`, receipt `codex-review-M2000-p1_5.receipt.json`).**
- §3 flush budget (v1 line 94) is numerically wrong: `10⁶ · 10⁸ · 2^{−900} ≈ 1.18e−257` (not `< 2e−262`). With up
  to 16 phase parts per operator the total is `< 1.9e−256`, still far below `ABS_ENTRY = 1e−250`. The primitive
  term (ii) `≤ 10⁶·10⁸·12·2^{−1000} ≈ 1.1e−286` is unchanged. Conclusion unchanged.
- §3/v1 line 84 "π representation error ≤ 1e−40 in practice" is wrong: a DD has ~106 significand bits, so the
  relative representation error of `π_s` is up to ~1e−32 (Codex measured 2.07e−33 at N = 1344, s = 943). The code
  adds the actual per-sector `max(pis_rel)` to `relE` (logged relE ≈ 1.2e−26 includes it); the bound is unaffected.
- Provenance: the p = 1/5 result used `--ptail 1e-13 --pitail 1e-40` (defaults in combine.py are 1e−30;
  the invocation is in `evidence/LOG.md` and `review/RESULT_T1.md`). From code v3 on, every sector record carries
  the witness and cert.py SHA-256 and combine.py rejects mismatches and records ptail/pitail.
