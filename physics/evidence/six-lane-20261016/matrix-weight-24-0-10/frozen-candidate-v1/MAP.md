# Frozen candidate v1 — integral matrix weights for AMH Open Problem 1 (`[[24,0,10]]_2`)

Frozen 2026-10-16 (America/Los_Angeles). Lane: `physics/evidence/six-lane-20261016/matrix-weight-24-0-10/`.

## Claim (exact scope)

There is an explicit table of nonnegative integers `λ^{t,p}_{i,j}` (file `lambda_24_0_10.json`: 1616 nonzero
entries `[i,j,t,p,λ]`, every other `(i,j,t,p) ∈ I(24)` has `λ = 0`, total `Σλ = 2^48`) such that with
`x^{t,p}_{i,j} = λ^{t,p}_{i,j}/γ^{t,p}_{i,j}` all constraints of Anglès Munné–Huber, arXiv:2603.19901v1, Eq. (31),
(32) pure, (33) self-dual, (34) additive and (35) Type II hold for `n=24, K=1, δ=10, k=0`, with
`λ^{0,0}_{i,0} = A_i` of Eq. (38). This is a positive answer to AMH **Open Problem 1** ("provide a putative integer
matrix weight enumerator λ for this code").

**Not claimed:** existence of a `[[24,0,10]]_2` code; any statement beyond the listed necessary conditions;
priority/novelty (dated searches only).

## Map from AMH equations to checker code (`verify_amh.py`, stdlib + Fractions only)

| AMH item (v1 text) | Statement checked | Function / key |
|---|---|---|
| Eq. (41) γ | `γ = 3^{i+j−t} 2^{t−p} n!/(p!(t−p)!(i−t)!(j−t)!(n−i−j+t)!)` | `gam` |
| Eq. (42) β | `β^{m,t}_{i,j,k} = Σ_u (−1)^{t−u} C(u,t) C(m−2k, m−k−u) C(m−k−u, i−u) C(m−k−u, j−u)` (= AMH `fun.jl` `beta` with `C(m−2k,u−k)`) | `bet` |
| Eq. (42) α | `β^{n−a,t−a}_{i−a,j−a,k−a} · 3^{(i+j)/2−t} · Σ_g (−1)^{a−g} C(a,g) C(t−a,p−g) 2^{t−a−p+g}`, exact in `Q(√3)` | `alp`, class `Q3` |
| (31) normalization | `x^{0,0}_{0,0} = 1` | `31_x0000_is_1` |
| (31) parity | `x = 0` if `t−p` odd | `31_odd_t_minus_p_zero` |
| (31) triple symmetry | `x` equal when `t−p = t'−p'` even and `(i,j,i+j−t−p)` permutes `(i',j',i'+j'−t'−p')` | `31_triple_symmetry` |
| (31) projector rows | `Σ_{k=i+j−t−p} γx = (2^n/K) γ^{0,0}_{k,0} x^{0,0}_{k,0}` for every `k` | `31_row_sums` |
| (31) KL | `K 2^{−n} Σ_i K_j(i,n) γ^{0,0}_{i,0}x^{0,0}_{i,0} = γ^{0,0}_{j,0}x^{0,0}_{j,0}`, `0<j<δ` | `31_KL` |
| (31) PSD | for all `0≤a≤k≤n+a−k`: `(Σ_{t,p} α x^{t,p}_{i,j})_{i,j=k..n+a−k} ⪰ 0`, exact LDL^T in `Q(√3)` | `31_blocks_psd` (169 blocks) |
| (32) pure | `x = 0` if `{i,j,i+j−t−p} ∩ {1..δ−1} ≠ ∅` | `32_pure` |
| (33) self-dual | `Σ_i (−1)^i K_j(i,n) λ^{i,i}_{i,i} = 0` for `n−j` odd; `(K/2^n) Σ_i K_j(i,n) λ^{i,i}_{i,i} = λ^{j,j}_{j,j}` ∀j | `33_shadow_odd`, `33_B_equals_A` |
| (34) additive | `x ≥ 0` and `λ ∈ Z` | `34_nonnegative`, `34_integral` |
| (35) Type II | `Σ_{j even} λ^{j,j}_{j,j} = 2^{n−k} = 2^{24}` | `35_typeII` |
| Eq. (38) | `λ^{0,0}_{i,0} = A_i` | `38_weights` |

`K_j(i,n) = Σ_α (−1)^α 3^{j−α} C(i,α) C(n−i,j−α)` (AMH Eq. (6)).

## One-command verification

```sh
cd frozen-candidate-v1 && ../../noncws-code/env/venv/bin/python verify_amh.py lambda_24_0_10.json && ../../noncws-code/env/venv/bin/python snapshot_controls.py
```

`verify_amh.py` needs only the Python standard library (tested with CPython 3.13.9); `snapshot_controls.py`
additionally needs numpy (2.5.4 in the lane venv). Observed runtimes: ~1–2 s and ~17 s on the Mac Studio.

## Receipts (`receipts/`)

- `amh_check.json`: full report of `verify_amh.py lambda_24_0_10.json` (ALL_PASS).
- `controls.json`: positive controls (hexacode, dodecacode brute-force pair counts pass; 3 random even additive
  groups at n=24 and 3 random groups with odd weights at n=7 give PSD blocks, exercising the `√3` branch) and
  mutations (+1, −1, swap, ×2, delete one entry, spurious odd-weight entry — each fails).
- `g2_rigorous_*.json`: SEPARATE extra property (below).

## Separate extra property (not part of AMH's question)

The table also satisfies the genus-2 (pair-enumerator) MacWilliams self-duality of an additive self-dual code:
`Σ_τ f(τ) K(τ→τ') = 2^{48} f(τ')` for the full symplectic transform `T` and `Σ_τ f(τ) K_1(τ→τ') = 2^{24} f(τ')`
for the partial transform `T_1` (Fourier transform of the first factor only), for **every** pair type `τ'`
(all 20475 coefficients). `verify_g2_rigorous.py` evaluates every coefficient modulo each prime with int64
arithmetic (all intermediates `< 2^36`, products `< 2^62`). Deterministic height bounds: `Σ_τ f(τ) = 2^{48}`,
`|K| ≤ 16^{24} = 2^{96}` (row absolute sums of `T` ≤ 16), `|K_1| ≤ 4^{24}`; hence every integer residual is
`< 2^{145}` in absolute value, and vanishing modulo six 31-bit primes (product `> 2^{185}`) proves it is exactly 0.
This relies on the correctness of `transform_row` (a direct modular product of linear forms) and of `T`, `T_1`
(derived by brute force from the symplectic character in `genus2.py`). It also satisfies divisibility
`λ ≡ 0 mod |Stab_{S3}(n_0x,n_x0,n_xx)|` for pair types with `u, v, u+v` all nonzero (2-dimensional subspace count).

## Verifier v1.1 and review dispositions (appended; candidate table unchanged)

- `verify_amh_v1_1.py` (v1 `verify_amh.py` preserved byte-for-byte): skips zero-binomial summands before forming
  powers (v1 could form `2**negative` floats inside zero summands), asserts exact intermediates, documents inputs.
  Receipts: `receipts/amh_check_v1_1.json` (ALL_PASS, exit 0), `receipts/controls_v1_1.json`
  (ALL_EXPECTATIONS_HOLD), `appendix-psd-control/amh_check_of_control_v1_1.json` (PSD fails, exit 1).
- Genus-2 receipts on this frozen table: `receipts/g2_rigorous_{a,b,c}.jsonl` — all 20475 coefficients of the full
  and partial identities vanish modulo six primes; the +1 mutation (`receipts/g2_mutation_input.json`) is rejected
  by the total-pair-count precondition (`2^48 + 1`), see `receipts/g2_rigorous_mutation.jsonl`.
- Codex `gpt-6.1-sol` (max, read-only, ephemeral) hostile review: **ACCEPT**, own inline verifier; all Eq. (31)–(35),
  (38) gates, 169 PSD blocks (rank histogram 0:44, 1:84, 2:37, 3:4), genus-2 full and partial identities checked
  coefficient-by-coefficient over the integers, divisibility, marginals; mutations rejected; hexacode control.
  Informational findings: Eq. (41) typeset with a duplicated multinomial (orbit-size γ intended, = `fun.jl`);
  HTML drops the KL range `0<j<δ` (PDF has it); no realizability claim. Files: `../review/codex-review-*`.
- Parent gates: full-table independent check PASSED and PSD-only control confirmed (parent reports in
  `institute/runs/six-lane-2026-10-16/review/`).
