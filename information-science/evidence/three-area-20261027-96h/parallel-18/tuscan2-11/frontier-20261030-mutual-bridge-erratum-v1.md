# Erratum 1 to the mutual-bridge packet: the "exact equivalence" is withdrawn

Owner **InfoRecursiveMDS18-2**, info-4. `/bin/date` before writing: **Fri Oct 30 04:03:41 PDT 2026**. Additive to `frontier-20261030-mutual-m-endpoint-bridge-v1.md` (SHA `f83c8f6e…9d43`), preserved unchanged. One correction per Main's finding; no computation used or needed.

1. **The §3 equivalence is false as pure count logic and is withdrawn.** With T = #E-2-cycles, k_on = mutual M-pairs that are E-2-cycles, k_off = mutual M-pairs that are not, we have k₀ = k_on + k_off with k_on ≤ T, so **k₀ ≤ T ⟺ k_off ≤ T − k_on**, not ⟺ k_off = 0. The statement "every mutual M-pair is an E-2-cycle" is only a **sufficient** condition (k_off = 0 forces k₀ = k_on ≤ T); unused E-2-cycles could in principle compensate off-cycle mutual pairs. No actual-array realizability is inferred from this arithmetic in either direction.
2. **"Correspondence theory permits every configuration" is corrected** to: the displayed identities and correspondences have **not ruled out** off-cycle mutual pairs. No existence claim is made.
3. Theorems 1 and 2 (the E-2-cycle two-derangement dictionary and the cross-witness rectangles) are unaffected. The conjecture k₀ ≤ T remains unproved, now with the correct decomposition: it fails exactly when k_off > T − k_on.
