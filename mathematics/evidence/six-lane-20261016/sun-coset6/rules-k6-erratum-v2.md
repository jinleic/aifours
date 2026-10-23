# rules-k6 erratum v2: follows the Codex v2/v3 delta review

- **Freeze record:** host-clock time and sha256 are in `evidence/certformat-v2.sha256`.
- **Review:** `R/sun-coset6-rules-v3-delta-codex-v1.note.md` (e489897b…).
- **Unchanged:** all earlier files stay frozen, including rules-k6-v3, proof-k6-lemmas-v1, CERT-FORMAT-k6-v1 and erratum v1. The semantics of v3 and the frozen certificates do not change.

## F1. rules-k6-v3 L11 and proof-k6-lemmas-v1 §3, hypothesis (iv)

**Corrected sufficient test.** If v = E3, require τ_max(jkl) < 3·τ_min(jkl) for every triple j, k, l of vertices other than v.

The old alternative, "or 3 | τ_min(jkl)", is wrong in direction and can never be met here, because τ_min is a power of 2. It is deleted.

**Why the test works.** Every α among the neighbours lies in {2, 4}. So each edge contributes α_e/gcd(α_e, r_opp) ∈ {1, 2, 4}, and τ_min is a power of 2. An admissible τ is a multiple of τ_min that is at most τ_max. The possible values, by triangle type:

| triangle | τ_min | admissible τ |
|---|---|---|
| (2,2,2) | 2 | {2, 4} |
| (2,2,4) | 4 | {4} |
| (2,2,4), E2 opposite the 4-edge (class 1 or 2) | 2 | {2, 4} |
| (2,4,4) | 4 | {4, 8} |
| (4,4,4) | 4 | {4, 8, 12, 16} |

- In (2,4,4) at least one 4-edge has an opposite vertex that is not E2, so τ_min = 4 and τ_max = 8.
- In (4,4,4) at least two 4-edges have non-E2 opposite vertices, so τ_min = 4 and τ_max = 16.

So every admissible τ has prime support in {2, 3}. τ is divisible by 3 only in the case τ = 12 for a (4,4,4) triangle. The corrected test excludes exactly those triangles (16 ≥ 3·4). Hence gcd(r_v, τ_jkl) = 1 for every triple, which is all that Step 2 of the proof uses.

**Engine check.** rule_N26 in engine v3 rejects v when `tm % 3 != 0 and tM >= 3*tm`. Since τ_min is always a power of 2 here, `tm % 3 != 0` always holds. So this is exactly the corrected test, and the "3 | τ_min" branch was never taken.

## F2. Dependence supersession (contract text unchanged)

The frozen contract `math-1-sun-coset6-contract.json` names "sun-coset5 proof-v3" as the Core(5) input. The binding Core(5) input is the **accepted** parent correctness record `R/sun-coset5-parent-verdict-v1.md` (2cf02436…5301). That record binds sun-coset5 **proof-v4** together with rules-v1-erratum-v3.

Wherever README, proof-k6-v1 or the contract cite "proof-v3" for Core(5) or Prop 4.5, read "proof-v4 (accepted record 2cf02436…)". Prop 4.5 is §2 in both versions, and the mathematics is identical.

## F3. PB / P-pair grid rounding, made explicit (rules-k6-v1 L4)

Let u = 1/(5·gcd(r_v, α_jk)).

- **Lower bound.** Lb = max(τ_min(v,j,k)/(5α_jk), x_j + x_k − 1, 0), and lo = u·⌈Lb/u⌉.
- **Upper bound.** Start from hi = u·⌊min(x_j, x_k)/u⌋. If hi = min(x_j, x_k) and K2 bars the containment, subtract one u. For equal sizes, both K2 conditions must hold.

**Engine check.** Engine v3 calls engine v2's rule_P, which computes exactly this:
- lo = (−⌊−(Lb/u)⌋)·u, i.e. lo = u·⌈Lb/u⌉;
- hi = ⌊min/u⌋·u, followed by the K2 decrement.

CERT-FORMAT-k6-v2 states this rounding explicitly.

## F4. CERT-FORMAT

`CERT-FORMAT-k6-v2.md` supersedes the text of v1. It changes only the PB rounding sentence (F3) and the N26 E3 test with its τ table (F1). The certificate files in `evidence/engine-v3-core56/` are unchanged.
