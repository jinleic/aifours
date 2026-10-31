# V-saturation: the capped complementary signing is forced to be majority-extremal

**SAME-SLOT WRITTEN MANUSCRIPT (future-only duty after parent ruling 8294c02f47b190a595f96642c3a555464631ee701a3a77da22759a097fa0964b; PARTIAL, necessary-condition interface).** Native clock observed before writing: **2026-10-30T04:02:10-0700 PDT**. Owner InfoBalancedNL242-3, slot info-6. This packet attacks the ORIGINAL (V) capped complementary signing problem using only the clean adopted interfaces of the f272 and f277 parent dispositions and the frozen composite they govern. The held fibre-sign-gate packet (`daadae98…`) and all its consumers are NONINPUT here: nothing below uses, references or restates it. No selected assignment or operator, no private sanity check, no numerical instantiation, no code/solver/paid run; all derivation is symbolic on universally quantified count variables. No witness, no exclusion; (U), (V), rank two and the global target remain open.

## 1. Clean imported interface (named, not restated beyond statement)

| Import | Pin | Statements used |
|---|---|---|
| f272 parent disposition `info-6-nl242-uv-caller-interface-and-unconditional-congruences-parent-v1.md` | `b1834337…2fede` (as quoted by Main; not opened) | caller split `W_f = 2Û` on K, `W_f = 2V̂` off K; unconditional congruence `V̂ ≡ 2 (mod 4)` on all 256 characters; adoption of the interface theorems |
| f272 frozen composite (base `a1b7036f…` + erratum `a3826398…`) | as frozen | value set `V̂ ∈ {±2,±6,±10,±14}` (cap 14 with residue 2 mod 4); Parseval `ΣV̂² = 35840` over the 256 characters; per-fibre energies `Σ_{r}V̂(r,s)² = 64E_s`, `Σ_s E_s = 560`, `E_s ≡ 0 (mod 4)` |
| f277 parent disposition `info-6-plateaued-support-xor-and-both-coupling-redundancies-parent-v1.md` | `6a668529a4d42a260d0346325c9c83d8f818937356d8614141c5b160139123a6` (as quoted by Main; not opened) | scope delimitation: this packet treats only (V) |

Notation: `n_j := #{λ : |V̂(λ)| = j}` for `j ∈ {2,6,10,14}` (global counts), `n_j(s)` per fibre `s ∈ P`. The frozen scope (balanced, `max|W_f| ≤ 28`, m=116, (0,4,8), `G₃=1`, local H=0) is preserved verbatim.

## 2. The saturation theorem

**Theorem (V-saturation; necessary at the frozen residual).** Any complementary signing v meeting the cap satisfies

`108 ≤ n₁₄ ≤ 181`.

Equivalently: at least 108 and at most 181 of the 256 characters λ have `|V̂(λ)| = 14`, i.e. `|W_f| = 28` and `|k| = 7`; for each such λ the character χ_λ agrees with v on exactly 77 of the 140 points of Ω (if `V̂ = +14`) or exactly 63 (if `V̂ = −14`), since `#agree = (140 + V̂(λ))/2`. **The off-K half of the Walsh spectrum of any solution is therefore majority-extremal: the cap 14 is not merely respected, it is attained on a strict majority of characters.**

*Proof.* The value set and Parseval give the two exact count equations (frozen composite, §6 ledger):

`n₂ + n₆ + n₁₀ + n₁₄ = 256`,  `n₂ + 9n₆ + 25n₁₀ + 49n₁₄ = 8960`,

equivalently, eliminating `n₂ = 256 − n₆ − n₁₀ − n₁₄`,

`n₆ + 3n₁₀ + 6n₁₄ = 1088`,  with `n₂ = 2n₁₀ + 5n₁₄ − 832`, `n₆ = 1088 − 3n₁₀ − 6n₁₄`.

*Lower bound.* Since each unit of `n₆ + n₁₀` contributes at most 3 to `n₆ + 3n₁₀`, and `n₆ + n₁₀ ≤ 256 − n₁₄`:

`1088 = (n₆ + 3n₁₀) + 6n₁₄ ≤ 3(256 − n₁₄) + 6n₁₄ = 768 + 3n₁₄`,

so `n₁₄ ≥ (1088 − 768)/3 = 320/3`, hence `n₁₄ ≥ 107`. Suppose `n₁₄ = 107` for contradiction. Then `n₆ + 3n₁₀ = 446` and `n₆ + n₁₀ = 149 − n₂`, so `2n₁₀ = 297 + n₂` forces `n₂` odd, and `n₆ = 149 − n₂ − (297+n₂)/2 = (1 − 3n₂)/2 ≥ 0` forces `n₂ ≤ 0`; odd and non-positive gives `n₂ = −1 < 0`, a contradiction. Hence `n₁₄ ≥ 108`.

*Upper bound.* Nonnegativity of `n₂` and `n₆` gives `2n₁₀ + 5n₁₄ ≥ 832` and `3n₁₀ + 6n₁₄ ≤ 1088`; the latter with `n₁₀ ≥ 0` gives `n₁₄ ≤ ⌊1088/6⌋ = 181`.

*Sharpness within the ledger (algebraic corner solutions).* At `n₁₄ = 108` the binding constraints force `n₂ = 0`, and solving `2n₁₀ + 5·108 = 832` with `n₆ = 1088 − 3n₁₀ − 648` yields the unique corner `(n₂,n₆,n₁₀,n₁₄) = (0,2,146,108)`; at `n₁₄ = 181` the corner is `(73,2,0,181)` (from `n₂ = 5·181 − 832` and `n₆ = 1088 − 6·181`). Both satisfy the two equations identically, so the window `[108,181]` is the exact ledger range; these are solutions of the count system, not spectra, signings, or claims of realizability. ∎

## 3. Per-fibre refinement

Per fibre s, the same elimination on the per-fibre ledger (`n₂(s)+n₆(s)+n₁₀(s)+n₁₄(s) = 64`, `Σ_{r}V̂(r,s)² = 64E_s`) gives

`n₆(s) + 3n₁₀(s) + 6n₁₄(s) = 2E_s − 8`, and since each unit of `n₆(s) + n₁₀(s)` contributes at most 3 while `n₆(s) + n₁₀(s) ≤ 64 − n₁₄(s)`,

`2E_s − 8 ≤ 3(64 − n₁₄(s)) + 6n₁₄(s) = 192 + 3n₁₄(s)`, i.e. `n₁₄(s) ≥ ⌈(2E_s − 200)/3⌉` whenever `2E_s > 200`.

Since `Σ_s E_s = 560` with each `E_s ≡ 0 (mod 4)`, the largest fibre energy is at least `140`, forcing that fibre alone to carry `n₁₄(s) ≥ ⌈(280 − 200)/3⌉ = ⌈80/3⌉ = 27` saturated characters — a full 27 of its 64 characters at the extreme — and the global window of §2 bounds the sum.

## 4. Twist invariance of (V)

**Proposition.** If v signs Ω feasibly (cap and congruence), then so does `v_μ := v·χ_μ` for every character `χ_μ` of V (`μ ∈ V*`): `V̂_μ(λ) = V̂(λ+μ)` merely permutes the 256 values, preserving the multiset, the cap, and the residue class `2 (mod 4)` (residues move with their values). Feasibility, min-max value, and the saturation window are therefore invariants of the 256-element twist group; `Σ_μ`-averages and any obstruction criterion may be sought among twist-invariant data of Ω alone. (The imbalance `Σv = V̂(0)` is not itself invariant, but its only constraint, `|Σv| ≤ 14` with `Σv ≡ 2 (mod 4)`, is the λ = 0 instance of the cap and is preserved.)

## 5. Interface corollary (the whole target is boundary-pinned)

On K the frozen k-values give `|W_f| ≤ 24`; off K `|W_f| = 2|V̂| ≤ 28` with equality on at least 108 characters. Therefore, for ANY Boolean function realizing the frozen residual:

`max_a |W_f(a)| = 28` exactly, `NL(f) = 2⁸ − 28/2 = 242` exactly,

and the maximum Walsh modulus is attained off K at least 108 times. A witness, if one exists, is exactly at the boundary with a forced strict-majority multiplicity of extremal off-K values; no slack in nonlinearity is available on the complementary half.

## 6. Exact unpaid premise (restatement of (V) after this packet)

(V) is equivalent to: **sign the u-determined 140-set Ω with {±1} so that all 256 character sums lie in `{±2,±6,±10,±14}`, with at least 108 (and at most 181) of them at exactly ±14, where a ±14 value means agreement of the character with the signing on exactly 77 (resp. 63) points of Ω.** This is the construction interface this packet contributes: (V) is not a generic bounded-signing problem but a majority-extremal spectral rigidity problem. Its solvability remains open; nothing here is sufficient for existence, and no exclusion is proved.

## 7. Status and provenance

Necessary only; (U) common ternary u realization, (V), rank two, and the global balanced NL242 target remain open. No N1/N2 statements, no 4|w material, no held-packet content. Native clocks: ruling received; this file at 2026-10-30T04:02:10-0700 PDT. Frozen bytes everywhere preserved; same-harness; not human, independent-model-family, formal/kernel or novelty verification.
