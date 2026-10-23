# Remaining seven residue types: new necessary conditions and precise stopping points

**Status.** No further residue type is excluded. This note proves several new necessary conditions, one sub-case exclusion for type (6,144), and coset lemmas for type (2,192). It also gives explicit relaxation witnesses that show where each lever stops. Everything is conditional on the same reviewed inputs as `../zero-geometry/PROOF.md`:

- the canonical-spectrum and quadratic-residue tools (`../PROOF.md`, `../SHARPER.md`);
- the Opus-reviewed candidate lemmas: the zero-count table, `hat p ∈ {0,±64}`, `hat(p²) ≡ 0 mod 32`, the next-bit lemma (E has degree ≤4 and its quartic part is the principal 4×4 Pfaffians of the polar matrix), and the exact slack identity.

This is a model-written proof with exact finite checks. It is not Lean-verified or peer reviewed, and novelty is unestablished: the residue, Pfaffian and canonical-sign tools are prior art. The book question remains open, because seven types remain.

## 0. Setting

Let `g,h` be odd-weight eight-variable halves with `|G|+|H| ≤ 28`. Write `K_g, K_h` for the canonical spectra (`hat K ∈ {±256}`), `J_g, J_h` for their quadratic residues, `D = J_g + J_h` (polar rank `2t`, weight `d`), and `S = K_g+K_h`, `R = K_g−K_h`, `p = R/8`, `T = (−1)^D S`. Let `z = #{p=0}`, `c = #{|p|=1}` and `a = #{|S| ∈ {4,12}}`. Put `E = (p−D)/2 mod 2`, `L = {|p|=1}` and `A = {|S| ∈ {4,12}}`. All eight-variable transforms are unnormalized: `hat f(x) = Σ_a f(a)(−1)^{a·x}`.

For a balanced target, `p(0)=0` and `D(0)=0`. In any linear coordinates `D` is a quadratic form, so Dickson's classification under `GL_8(F_2)` (polar rank, whether `D` vanishes on the radical, and weight) gives these WLOG normal forms. Coordinates are `a_0..a_7`, and the hypotheses are invariant under `a ↦ Ma` (`hat p ∘ M^{−T}`), as used in the reviewed note:

| Type | Normal form `D` | rad dim | `D` on radical | `K = rad ∩ D^{-1}(0)` dim τ |
|---|---|---:|---|---:|
| (2,192) | `a0+a1+a0a1` | 6 | zero | 6 |
| (4,160) | `a0a1+a0+a1+a2a3` | 4 | zero | 4 |
| (6,112) | `a0a1+a2a3+a4a5` | 2 | zero | 2 |
| (6,128) | `a0a1+a2a3+a4a5+a6` | 2 | nonzero linear | 1 |
| (6,144) | `a0a1+a0+a1+a2a3+a4a5` | 2 | zero | 2 |
| (8,120) | `a0a1+a2a3+a4a5+a6a7` | 0 | — | 0 |
| (8,136) | `a0a1+a0+a1+a2a3+a4a5+a6a7` | 0 | — | 0 |

## 1. Partition lemma and dual correlations (lever 1)

**Lemma 1.1 (partition).** For every `x`, exactly one of `hat S(x)`, `hat R(x)` is nonzero, and it is `±512`. Hence `A_S = supp hat S` and `A_R = supp hat R` partition `F_2^8`. Moreover `Σ S² = 1024|A_S|` and `Σ R² = 1024|A_R|`, so

`|A_R| = Σ p²/16 = 64 + (5d − 4z − 8c)/16`.

For the balanced target this also equals `128 + AC_f(s)/4`.

*Proof.* `hat S = hat K_g + hat K_h` and `hat R = hat K_g − hat K_h` with `hat K_g, hat K_h ∈ {±256}`. Plancherel gives the squared sums. The pointwise identity `p² = 4 + 5D − 4·1_Z − 8·1_L` is checked on all seven values of `p`. The autocorrelation form follows from `Σ_{a∈s⊥} W_f(a)² = 131072 + 256·AC_f(s)` and `R = ηW_f` on `s⊥`. ∎

**Lemma 1.2 (dual correlation).** Let `Q` be any quadratic with polar rank `2τ_Q`. Its Walsh support `supp W_Q` has `2^{2τ_Q}` points, each with `|W_Q| = 2^{8−τ_Q}`. Put `Γ_S(Q) = Σ(−1)^Q S` and `Γ_R(Q) = Σ(−1)^Q R`. Then

`Γ_S(Q) = 2^{9−τ_Q} Σ_{x∈A_S∩supp W_Q} ε_x`, `Γ_R(Q) = 2^{9−τ_Q} Σ_{x∈A_R∩supp W_Q} ε'_x`,

with signs `ε, ε' ∈ {±1}`. So with `N_S = |A_S ∩ supp W_Q|`, `N_R = |A_R ∩ supp W_Q|` and `N_S + N_R = 2^{2τ_Q}`:

`|Γ_S(Q)| ≤ 2^{9−τ_Q}N_S`, `|Γ_R(Q)| ≤ 2^{9−τ_Q}N_R`, `Γ_S(Q) ≡ 2^{9−τ_Q}N_S`, `Γ_R(Q) ≡ 2^{9−τ_Q}N_R (mod 2^{10−τ_Q})`.

*Proof.* Plancherel gives `Γ_S(Q) = 256^{-1}Σ_x hat S(x)W_Q(x)`. Insert Lemma 1.1 and the plateaued spectrum of a quadratic. ∎

`SHARPER.md`'s bound `|Σ(−1)^D S| ≤ 512·2^r` is the case `N_S ≤ 2^{2r}` for `Q=D`. The new content is that the S- and R-correlations share one budget of `2^{2τ_Q}` support points, and each satisfies its own congruence. The lemma applies to every quadratic, in particular to `D`, `J_g` and `J_h`.

**Proposition 1.3 (scalar stopping point).** For each of the seven types, `results/explore.json.gz` holds an explicit nonnegative integer count vector over the 28 canonical value pairs `(K_g,K_h)`. Each vector satisfies:

- 256 points with the correct number of `D=1` points;
- both Parseval identities;
- `ΣK_g = ±256` and `ΣK_h = ±256`;
- the rank-specific zero-count table, with `z ≥ 1`;
- `|A_R|` an even integer;
- Lemma 1.2 for `Q = D`, `J_g` and `J_h`, with polar ranks compatible with their weights.

`code/audit.py` replays these checks exactly, without z3. The vectors are **not** Boolean functions. They show only that these scalar levers, including the refined lever 1, cannot exclude any remaining type.

## 2. S-side coupling (lever 2)

**Lemma 2.1 (exact representations).** Let `J1 = [|S| ∈ {12,20}]` and `X = J1 + D`. On all 28 canonical pairs:

- on `D=1`: `p = (−1)^E (−3 + 4·1_L)`;
- everywhere: `S = 4(2D−1) + 8(−1)^X(−3 + 4·1_A)`.

*Proof.* Finite check (audited). ∎

**Lemma 2.2 (S–R residue coupling).** For every coordinate subset `T` with `|T| ≤ 4`, write `d_T = Σ_{a⊇T} D(a)`. Then

`Σ_{a⊇T} J1 ≡ Σ_{a⊇T} E ≡ d_T/2 (mod 2)`.

Hence `J1 + E ∈ RM(3,8)`, `J1` has degree ≤4 with the same Pfaffian quartic as `E`, and `X ≡ E` modulo `RM(3,8)`. For polar rank ≤2, `E` and `J1` are cubic. The statement holds for every odd pair with no cap: define `J1 := ((−1)^D S − 4)/16 mod 2`, which agrees with the displayed set under the cap.

*Proof.* `S ≡ 4+8D (mod 16)`, so `S = (1−2D)(4+16j)` with `j ∈ Z` and `J1 = j mod 2`. `hat S ≡ 0 mod 512` and mixed differences give `Σ_{a⊇T} S ≡ 0 mod 2^{9−|T|}`, that is `4n_T − 8d_T + 16Σj − 32ΣDj ≡ 0 mod 2^{9−|T|}` with `n_T = 2^{8−|T|}`. For `|T| ≤ 4`, reduce mod 32: `Σj ≡ d_T/2 mod 2`. (A quadratic restricted to ≥4 variables has even weight, so `d_T` is even.) The E half is the reviewed moment argument: `Σ_{a⊇T}p ≡ 0 mod 2^{6−|T|}` with `p = D + 2e`. Equal moments of order ≤4 put `J1+E` in `RM(4,8)^⊥ = RM(3,8)`. ∎

Like the reviewed next-bit lemma, this is a pruning identity, not a standalone obstruction. It does couple S magnitudes to the sign class of `p`.

## 3. Coset energy and projection thresholds (lever 3)

Let `K ⊆ rad(B) ∩ D^{-1}(0)`, `τ = dim K`, and fix a complement `W`. Translations by `K` preserve `D`. For `u ∈ W` and a character `κ` of `K`, put `hat p_u(κ) = Σ_{k∈K} p(u+k)(−1)^{κ(k)}`, and define `hat S_u` likewise.

**Lemma 3.1 (coset energy identity).** For every `κ`:

`Σ_u [hat S_u(κ)² + 64·hat p_u(κ)²] = 2^{18}`.

Also `hat p_u(κ) ∈ 2^{τ−2}Z` and `hat S_u(κ) ∈ 2^{τ+1}Z`. In particular `Σ_u hat p_u(κ)² ≤ 4096`, so `|hat p_u(κ)| ≤ 64`.

*Proof.* Each frequency `x` with `x|_K = κ` gives `hat p(x) = Σ_u (−1)^{x·u}hat p_u(κ)`, an `(8−τ)`-dimensional Hadamard transform in `u`. Parseval over that coset of `K^⊥`, together with Lemma 1.1, gives the identity. Integrality follows from inverting the Hadamard transform. ∎

**Lemma 3.2 (coset form).** On a `D=1` coset with `ℓ_u = |L ∩ (u+K)|`, let `E_u` be `E` restricted to the coset. Then

`hat p_u(κ) = −3W_{E_u}(κ) + 4Λ_u(κ)`, where `|Λ_u| ≤ ℓ_u` and `Λ_u ≡ ℓ_u (mod 2)`.

Hence `3|W_{E_u}(κ)| ≤ 64 + 4ℓ_u`. If `E_u` is affine with linear part `χ`, then `|hat p_u(χ)| = 3·2^τ − 4ℓ_u`. On every coset,

`hat(S_u/4)(κ) = (2D_u−1)2^τ δ_κ + 2(−3W_{X_u}(κ) + 4Λ^S_u(κ))`,

with `|Λ^S_u| ≤ |A ∩ (u+K)|`. ∎ (Lemma 2.1, transformed coset by coset.)

**Proposition 3.3 (single-character threshold).** Suppose `E` is K-equivariant on `D^{-1}(1)` with one character `χ`, that is, `E(a+k) = E(a) + χ(k)`. Then `9d − 24c ≤ 2^{12−τ}`.

*Proof.* Put `q = −3(−1)^E·1_{D=1}` and `ℓ = 4(−1)^E·1_L`, so `p·1_{D=1} = q + ℓ` and `P_χ q = q`. Then `‖P_χ p‖² ≥ ‖q + P_χℓ‖² ≥ ‖q‖² + 2⟨q,ℓ⟩ = 9d − 24c`. Here `P_χ` is the orthogonal projection onto χ-equivariant functions, which preserves `D^{-1}(1)`. On the other side, `hat(P_χ p)` is `hat p` restricted to one coset of `K^⊥`, so `‖P_χ p‖² ≤ 2^{8−τ}·64²/256 = 2^{12−τ}`. ∎

| Type | `9d` | slice bound `2^{12−τ}` | Lever needs | Available bound on `c` |
|---|---:|---:|---|---|
| (2,192) | 1728 | 64 | c ≥ 70 | c ≤ 28 (proved, §6) |
| (4,160) | 1440 | 256 | c ≥ 50 | c ≤ 24 (proved, §5) |
| (6,144) | 1296 | 1024 | c ≥ 12 | witnesses exist up to c = 48 (scalar model) |
| (6,112) | 1008 | 1024 | never violated | — |
| (6,128) | 1152 | 2048 | never violated | — |
| (8,120) | 1080 | 4096 | never violated | — |
| (8,136) | 1224 | 4096 | never violated | — |

**Consequence (precise obstruction).** For (6,112), (6,128), (8,120) and (8,136), even perfect single-character equivariance cannot contradict Proposition 3.3. The whole forced `D=1` energy fits inside one Fourier slice. The (4,128) projection mechanism therefore cannot extend to these four types. For (2,192) and (4,160) the threshold would be decisive, but its equivariance hypothesis is not forced (§5–6).

## 4. Type (6,144): an exclusion when the zero set is K-invariant

**Theorem 4.1.** For type (6,144), `K = rad(B) = span(e6,e7)`. If the zero set `Z` is K-invariant, then `c ≥ 12`.

*Proof.* The Pfaffian quartics use only coordinates `0..5`, so for `k ∈ K`, `Q_k := E + E(·+k)` is a quadratic. On `D^{-1}(0)`, `E = 1 + 1_Z`, so `Q_k = 1_Z + 1_Z(·+k) = 0` there. A finite check (audited) shows that the only quadratics vanishing on `D^{-1}(0)` are `0` and `D`. So `Q_k` is constant on `D=1`. Additivity in `k` gives a single character, and Proposition 3.3 yields `1296 − 24c ≤ 1024`, i.e. `c ≥ 12`. ∎

This does not exclude the type. The scalar model has witnesses with `c ≥ 12`, and nothing is proved about zero sets that are not K-invariant. For (6,112) the same equivariance holds, but the threshold row above makes it vacuous.

## 5. Type (4,160): where the lever stops

Here `K = rad(B) = span(e4..e7)`. The slack identity gives `Γ = −256 − 64(a+c) − 32z` with `|Γ| ≤ 128·16`, so `2(a+c) + z ≤ 56`. With `z ≥ 8` this gives **c ≤ 24**, below the threshold 50.

The obstruction is that the K-character of `E` on `D=1` is not forced to be single. Among the 29 basis words of the kernel of `RM(3,8)` restricted to `D^{-1}(0)`, 16 have non-constant K-derivatives on `D=1`. Even when `Z` is K-invariant, the quadratics vanishing on `D^{-1}(0)` form a space of dimension greater than one (audited). So `Q_k` can make the character `χ_u` depend on the `D=1` coset `u`. Lemma 3.1 then yields only the collision inequality `Σ_{u: χ_u=κ, D_u=1} (48 − 4ℓ_u)² ≤ 4096` for coset-affine `E`. Ten `D=1` cosets and sixteen characters permit injective characters, so no collision is forced. No exclusion is claimed.

## 6. Type (2,192): coset lemmas

`U = D^{-1}(0) = {a0=a1=0}` is a six-dimensional subspace and equals `K`. The three `D=1` sets are its other cosets, labeled `c ∈ F_2^2 \ {0}`. Write `x = (x', κ)` with `x' ∈ F_2^2`. Then for each `κ` the four coset transforms are a 2-variable fiber pattern:

`(hat p_c(κ))_c = 16·H v'`, `(hat S_c(κ))_c = 128·H σ'`, `v' + σ' = (−1)^{u(·,κ)}`, `v' − σ' = (−1)^{w(·,κ)}`.

Here `H` is the 4×4 Sylvester matrix and `v', σ' ∈ {0,±1}^4` have complementary supports. Put `h_c = hat p_c/16` and `s_c = hat S_c/128`.

**Lemma 6.1.** `1_Z|_U ∈ RM(3,6)`, `0 ∈ Z`, `z ≥ 8` and `z ≠ 10`. Also `2(a+c) + z ≤ 64`, `z + 2c ≡ 0 (mod 8)` and `a ≡ 0 (mod 4)`; hence `c ≤ 28`. *(E is cubic and `E|_U = 1 + 1_Z`. For the rest, `Γ = 1024 − 64(a+c) − 32z = 256·(an integer of absolute value ≤4)`.)*

**Lemma 6.2.** For each `D=1` coset, `3·max|W_{E_c}| ≤ 64 + 4ℓ_c ≤ 176`, so `E_c` is **never affine**. For every coset, `3|W_{X_c}(κ)| ≤ 64 + 32δ_κ + 4a_c`. Consequently at most one coset has affine `X_c`, and then `a_c ≥ 24` and `z + 2c ≤ 16`.

**Lemma 6.3 (shared parity).** All eight coset functions `h_c, s_c` have the same parity pattern `π(κ) = k(κ) mod 2`, where `k = |supp v'|`.

**Lemma 6.4 (parity weights).** These follow from Lemma 3.2, Parseval for `E_c` or `X_c`, the identities `Σ_κ h_c² = 144 − 2ℓ_c` and `Σ_κ s_c² = 140 − 2a_c + (2D_c−1)·4s_c(0)`, and exhaustive solution of the resulting integer systems (audited):

- R side, `D=1` coset: `ℓ_c = 0 ⇒ h_c ∈ {0,±3}` and `wt(π) = 16`; `ℓ_c = 1 ⇒ (#|h|=1, #|h|=2, #|h|=4) = (42,21,1)` and `wt(π) = 42`.
- S side, any coset: `a_c = 0 ⇒ wt(π) ∈ {12,16}`; `a_c = 1 ⇒ wt(π) ∈ {42,46}`.
- R side, `D=0` coset: `wt(π) ≤ 64 − z`.

**Lemma 6.5.** At most one `D=1` coset has `ℓ_c = 0`. *(At `κ` with `h_c = ±3`, the only patterns with an entry ±3 have `k = 3`, and their other three entries are ±1.)*

**Lemma 6.8 (parity classes).** Odd squares are `1 mod 8` and even squares are `0 mod 4`. So the energy identities give `wt(π) ≡ 144 − 2ℓ_c ≡ 2ℓ_c (mod 4)` on each `D=1` R-coset, `wt(π) ≡ 140 − 2a_c ≡ 2a_c (mod 4)` on each S-coset, and `wt(π) ≡ 64 − z ≡ z (mod 4)` on the `D=0` R-coset. Since `π` is shared (Lemma 6.3), **every `ℓ_c` and every `a_c` is congruent to `z/2` modulo 2.** The audited exact parity-weight tables agree: `ℓ=2: {12,16,20,24,28}` and `ℓ=3: {30,34,…,58}`, each in the predicted class mod 4.

**Corollary 6.6.** `c ≥ 3`. A coset function with parameter 0 cannot coexist with one of parameter 1. If all seven parametrized coset functions (`ℓ_1,ℓ_2,ℓ_3,a_0..a_3`) are ≤1, then `ℓ = (1,1,1)`, every `a_c = 1`, and `z = 18`. By Lemma 6.8: if `z ≡ 2 (mod 4)`, all `ℓ_c, a_c` are odd, so `c ≥ 3` and `a ≥ 4`; if `z ≡ 0 (mod 4)`, all are even, and Lemma 6.5 gives `c ≥ 4`.

**Proposition 6.7 (stopping point).** The **full** joint count relaxation of Lemmas 3.1–6.8 is satisfiable. It combines per-`κ` 2-variable fiber patterns for R and S; the `E_c`/`X_c` Walsh–Parseval identities; the mod-3 integrality of `W_{E_c}` and `W_{X_c}`; the ranges and parities of Λ; the per-coset S energy and S–Λ cross identities; κ=0 bookkeeping; and every scalar constraint of Lemma 6.1, including `a ≡ 0 mod 4`. Three explicit witnesses satisfying the whole family are verified independently: `results/rank2-probe-senergy-scross-aux.json` (`z = 8`, `ℓ = (4,4,4)`, `a = (0,4,8,4)`), `…-senergy-aux.json` (`ℓ = (4,4,4)`, `a = (4,0,8,4)`) and `…-scross-aux.json` (`ℓ = (0,4,4)`, `a = (8,4,4,4)`). These were found by solver runs that did not impose every family; the audit then checked each against the full family. Two solver runs that imposed `a ≡ 0 mod 4` were `UNKNOWN`: the producer's full run at 600 s and a 400 s probe. A 1500 s full probe was cancelled once full-family witnesses existed. **No UNKNOWN is promoted.** These count-level coset lemmas therefore do not exclude (2,192). Excluding it would require using that the `E_c` and `X_c` spectra come from genuine six-variable cubics, sharing the cubic part of `1_Z` and coupled across cosets by `E = A + a0B1 + a1B2 + a0a1C`. Parseval and pattern counts alone are not enough.

As a positive control, genuine odd halves of pinned cap-32 NL240 corpus functions realize the same residue geometry: their `D` has weight 192 and a six-dimensional `K`. They satisfy Lemmas 1.1, 2.2 and 3.1 exactly (audited). They are not targets, because their peak is 32.

## 7. Precise status by type

| Type | Proved here | Where the levers stop |
|---|---|---|
| (2,192) | Lemmas 6.1–6.8; all `ℓ_c, a_c ≡ z/2 (mod 2)`; `c ≥ 3`; no `E_c` affine | scalar witness; full joint coset count-relaxation witnesses; equivariance not forced (`E_c` non-affine, cubic part from `1_Z`) |
| (4,160) | `c ≤ 24`; coset collision inequality | scalar witness; characters `χ_u` not forced to collide |
| (6,112) | — | scalar witness; projection threshold never violated |
| (6,128) | — | scalar witness; τ = 1, threshold never violated |
| (6,144) | K-invariant `Z ⇒ c ≥ 12` | scalar witnesses with large `c`; non-K-invariant `Z` unconstrained |
| (8,120) | — | scalar witness; no radical (τ = 0) |
| (8,136) | — | scalar witness; no radical (τ = 0) |

Lemmas 1.1–1.2, 2.2 and 3.1 hold for every type and for every odd pair under the cap; Lemma 2.2 even without the cap. None resolves a type alone. The (4,128) exclusion in `../zero-geometry/` and the 1–3-zero corollary are unchanged.
