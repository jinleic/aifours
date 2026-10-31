# The c=0 fibre-sign gate: a two-integer skeleton for (U) with (V) linkage at the origin block

**SAME-SLOT WRITTEN MANUSCRIPT (bounded future-only step; PARTIAL, necessary-condition interface).** Native clock observed before writing: **2026-10-30T03:51:18-0700 PDT**. Owner InfoBalancedNL242-3, slot info-6. Per the governing directive this packet derives ONE substantive all-variable bridge at the actual joint interface — necessary conditions on (U) common ternary u realization with the (V) capped complementary signing linked at the distinguished block c=0 — and then stops. Scope preserved exactly: balanced f on F₂⁹, `max|W_f|≤28`, rank-two polar, exactly eight Walsh zeros, **m=116**, `(e₁,e₂,e₃)=(0,4,8)`, `T≠0`, `q⁻¹(0)=R`, residual `G₃=1` with H the explicit local U₀-peak count 0. No N1/N2 statements, no 4|w exception variants, no held episode or selected diagnostic, no code/solver/paid run, no selected character assignment or operator; no witness or exclusion is claimed; (U),(V), rank two and the global target remain open.

## 1. Named imports (cited, not restated)

| Import | SHA-256 | Use |
|---|---|---|
| f255 correction (block normalization) `successor-20261029-f255-boolean-local-normalization-correction-v1.md` | `e0c3f4807732d6cd70d47485f1692366c0f77abfd1c5169e7a5782114bfddcf4` | `16U_s(c) = 3·Walsh_R(σ_s)(c) − 2t_s(c)`; `t₁ = 0`; `U₁ ∈ {0,±3}` with 16 nonzero; block value ranges |
| f263 residual parent (f270/f272-corrected composite) `info-6-nl242-rank2-eightzero-116-fibre-048-residual-10-cross-fibre-parent-v1.md` | `e09be9069bf8027bdb53e60a73c804f525b1c5c1953d517e417b5749b555ba09` | residual scope, class counts `A₁=16,C₂=4,C₃=6,D₁=18,G₂=2,G₃=1,H=0,O=17`, energies, k-fibre values |
| f263 base §8 control `successor-20261029-f244-residual-cross-fibre-placement-v1.md` | `686dd9177d6ff8788b6463d8d4e444e8bda4231ce7060a76ad0cfdea5f39144c` | the quoted formal placement sign fields (detection check, §3) |
| f272 parent disposition `dispositions/info-6-nl242-uv-caller-interface-and-unconditional-congruences-parent-v1.md` | `b1834337…2fede` (as quoted by Main; not opened here) | unconditional caller split and congruence adoption governing the interface |
| f277 parent disposition `dispositions/info-6-plateaued-support-xor-and-both-coupling-redundancies-parent-v1.md` | `6a668529a4d42a260d0346325c9c83d8f818937356d8614141c5b160139123a6` (as quoted by Main; not opened here) | redundancy closures delimiting this packet's scope |

## 2. The gate

Throughout, `σ_s = sign k(·,s)` on R (well-defined on fibres s=1,2,3 where `|k|∈{2,6}`), `n₋⁽ˢ⁾ := #{r∈R : σ_s(r)=−1}`, `E_s := Σ_{a∈A_s} σ_s(a)`, and on the s=0 fibre (where `k∈{0,±4}` with exactly 56 nonzero) `n₊⁽⁰⁾ := #{r : k(r,0)=+4}`. `D` is the set of 16 blocks with `|U₁|=3`; the block class of `c=0` is u-data.

**Theorem (c=0 fibre-sign gate; necessary at the frozen residual).** Any realization satisfies, per fibre:

- **s=1:** `U₁(0) = (192 − 6n₋⁽¹⁾)/16`, so `3n₋⁽¹⁾ ≡ 0 (mod 8)` and, since `U₁(0) ∈ {0,±3}` with `U₁(0)=±3 ⟺ 0 ∈ D`: **`n₋⁽¹⁾ ∈ {24,32,40}`, and `0 ∈ D ⟺ n₋⁽¹⁾ ∈ {24,40}`**.
- **s=2:** `U₂(0) = 12 − (3n₋⁽²⁾ + E₂)/8` with `E₂ ∈ {−4,−2,0,2,4}`, so **`3n₋⁽²⁾ + E₂ ≡ 0 (mod 8)` and `64 ≤ 3n₋⁽²⁾ + E₂ ≤ 128`**, forcing `n₋⁽²⁾ ∈ [20,44]`.
- **s=3:** `U₃(0) = 12 − (3n₋⁽³⁾ + E₃)/8` with `E₃` an even integer in `[−8,8]`, so **`3n₋⁽³⁾ + E₃ ≡ 0 (mod 8)` and `64 ≤ 3n₋⁽³⁾ + E₃ ≤ 128`**, forcing `n₋⁽³⁾ ∈ [19,45]`.
- **s=0:** `U₀(0) = (n₊⁽⁰⁾ − 28)/4`, so **`n₊⁽⁰⁾ ≡ 0 (mod 4)`** with the class coupling `0∈O ⟹ n₊⁽⁰⁾=28`; `0∈C₂∪C₃∪D₁∪G₂∪G₃ ⟹ n₊⁽⁰⁾ ∈ {20,28,36}`; `0∈D ⟹ n₊⁽⁰⁾ ∈ {24,32}` (these use `|U₀|=4` peaks being the H class, of count 0 here, and the A₁-block value `|U₀|=1`).
- **Joint, all four fibres at once:** the four displayed integers `(n₋⁽¹⁾, 3n₋⁽²⁾+E₂, 3n₋⁽³⁾+E₃, n₊⁽⁰⁾)` must satisfy all listed congruences and ranges **simultaneously**, with the class of c=0 consistent across the s=0 and s=1 instances (`0∈D ⟺ n₋⁽¹⁾∈{24,40} ⟺ n₊⁽⁰⁾∈{24,32}` and, by the same block, `U₀(0)=±1`).

*Proof.* All are the single character c=0 of the imported identity `16U_s = 3·Walsh_R(σ_s) − 2t_s`, using `Walsh_R(σ_s)(0) = Σ_r σ_s = 64 − 2n₋⁽ˢ⁾`, `t_s(0) = Σ_{A_s}σ_s = E_s` (s=1: `t₁=0`, `A₁=∅`), integrality of `U_s(0)` and the block value ranges (`|U_s| ≤ 4`; `U₁ ∈ {0,±3}`; the import's class taxonomy for `U₀` at H=0); on s=0 invert `2k(r,0) = Σ_c U₀(c)(−1)^{r·c}` at c=0 to get `U₀(0) = Σ_r k(r,0)/32 = (4(n₊⁽⁰⁾−(56−n₊⁽⁰⁾)))/32 = (n₊⁽⁰⁾−28)/4`. ∎

## 3. Detection check (diagnoses the known non-realization exactly)

The frozen f263 §8 formal control (import 3) takes `σ₃ ≡ +1` and `σ₂ = −1` at exactly four points, with `E₂ = 0`. Instantiating: s=2 gives `3·4+0 = 12 ≢ 0 (mod 8)` — the **integrality** gate fails, `U₂(0) = 12 − 12/8 = 21/2`, matching the quoted `U₂(0)=168/16`; s=3 gives `3·0+8 = 8 ≡ 0 (mod 8)` — integrality **passes**, but `8 < 64` violates the **range** gate, `U₃(0) = 11 > 4`, matching the quoted value. Both published failures of that control are thus exactly the two instances of this gate family, in closed two-integer form. (This is arithmetic on the imported, fully displayed §8 sign fields — no new finite object is constructed or consulted.)

## 4. Linkage to (V) at the same block

The class of `c=0` simultaneously pins the v-column of the origin block: `0∈D ⟹ W_s(0) = δ·χ_s(z₀(0))` (all four magnitudes 1); `0∈` a pair class `⟹ W_s(0) ∈ {0,±2}` with the two-nonzero pattern on the class's forced fibre pair (criterion `η₃η₄ = η₁η₂` as adopted in the f272 disposition); `0∈G₂∪G₃ ⟹ W_s(0)=0`; `0∈O ⟹ (W_s(0))` is a single ±4 spike or a ±2 quartet. Since `V̂(0,s) = Σ_c W_s(c)` and, by the f272-adopted unconditional congruence, `V̂(0,s) ∈ {±2,±6,±10,±14}` for all s, the origin column contributes to four capped forms whose admissible totals are pinned modulo the u-class of c=0 — the two sides of the joint problem read off one shared block. This is the bridge's construction-interface reading: **(U) and (V) meet first at c=0, where both gates are two-integer checks on the same block class.**

## 5. Status and exact remaining gap

The gate is necessary, not sufficient: passing all four instances plus the class couplings does not realize u (the full system requires the congruence `16 | 3·Walsh_R(σ_s)(c) − 2t_s(c)` with class-consistent values at **all** 64 c per fibre — the c=0 instances above are its only two-integer reductions — together with the adopted geometry, energies, zero sets and cross-fibre conditions), nor does it sign v. (U) common ternary u realization, (V) capped complementary signing over Ω, rank two, and the global balanced NL242 target remain open. No witness, no exclusion, no N1/N2 or 4|w statement is made or used.

Native clocks: directive received; this file at 2026-10-30T03:51:18-0700 PDT. Frozen bytes everywhere preserved; same-harness; not human, independent-model-family, formal/kernel or novelty verification.
