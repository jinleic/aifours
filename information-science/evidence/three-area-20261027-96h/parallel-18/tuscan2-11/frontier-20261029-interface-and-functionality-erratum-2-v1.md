# Erratum 2: checksum and label corrections; the six profiles are universal; multiplicity of omitted targets

Owner **InfoRecursiveMDS18-2**, info-4. Actual `/bin/date` before writing: **Thu Oct 29 21:05:11 PDT 2026**. Additive; corrects two of my own files in this thread at the f282 reviewer's and Main's findings. Both target files are preserved byte-for-byte.

## A. Corrections to `frontier-20261029-distance-incidence-interface-14-types-v1.md` (SHA `27931aa7…797fa`, parked)

1. **§4, T2(6) row:** the printed check "30 ✓" is wrong. The correct checksum is k₁+2k₂ = 0+2·12 = **24** = n(n−2) = 6·4. The identity held; my transcription of it did not.
2. **§4, closing sentence:** "the t = C(n,2) extreme (M all 2-cycles)" is a wrong label. An all-2-cycle permutation has **t = n/2** (t = 2 at n = 4, t = 3 at n = 6), which is the maximum t for a permutation at even n, not C(n,2).

## B. Corrections to `frontier-20261029-one-column-forces-other-functionality-sharpening-v1.md` (SHA `c55e56ad…9d65`, parked)

3. **§2, Theorem 2's claim of sharpening is overdrawn.** The **six numerical profiles** (k₀, 11−2k₀, 44+k₀) for k₀ = 0,…,5 already follow from the universal identities 2k₀+k₁ = 11 and k₁+2k₂ = 99 together with k₁ ≥ 0 — **no boundary-column hypothesis is needed**. The one-column hypothesis makes k₀ the number of 2-cycles of a function m (a genuine structural refinement) and constrains which k₀ are admissible (both-columns-permutation forces t ≤ 4); it does not enlarge the count set. Theorem 2 should be read as structure-attribution, not a new count result.
4. **§3, item 3 is wrong as stated.** From α₉ ≡ 1 and *some* α₁(z) = 0 one cannot conclude image(m) = S∖{z}: **several** symbols may have α₁ = 0. The correct statement is image(m) = S∖Z with Z = {z : α₁(z) = 0}, and the balance Σ_{α₁≥2}(α₁(w)−1) = |Z| holds. Items 1–2 of §3 apply to **each** zero-indegree (full-target) symbol and each α₁ ≥ 2 symbol respectively. The multiplicity of omitted targets is a residual; "exactly one omitted target" is not established and must not be used.

## C. Status

The α₉ ≡ 1 ⇒ α₁ ≡ 1 question remains NOT PROVED. No further interface packet is being produced; any genuine next result must constrain actual-array realizability beyond these degree/count identities. Unrestricted T2(11) remains OPEN.
