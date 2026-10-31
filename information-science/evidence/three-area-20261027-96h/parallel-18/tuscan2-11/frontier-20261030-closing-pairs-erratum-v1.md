# Erratum 1 to the closing-pairs packet: §3 arithmetic slip and cancellation mechanism

Owner **InfoRecursiveMDS18-2**, info-4. `/bin/date` before writing: **Fri Oct 30 03:36:44 PDT 2026**. Additive to `frontier-20261030-closing-pairs-derangements-and-failed-inequality-v1.md` (SHA `77e61e00…65e9`), preserved unchanged. One bounded repair per Main's finding; Theorem D and §§1–2 are untouched.

1. **Arithmetic slip.** A k₂-pair has TWO rows at d = 1 and TWO rows at d = 2, so its distance-sum minimum is 2+4+3(n−4) = **3n−6**, not the displayed "4+3(n−4)" (= 3n−8). The correct class minima are 3n−4 (k₀), 3n−5 (k₁), 3n−6 (k₂), and the k₀ coefficient then cancels exactly: (3n−4) − 2(3n−5) + (3n−6) = 0. The displayed value would have given −2.
2. **Cancellation mechanism, corrected.** For additive f, each class minimum is affine in m = the pair's number of d = 2 rows (m = 0,1,2 across the three classes); since the identity k₁+2k₂ = n(n−2) fixes the total count of d = 2 rows, every affine-in-m aggregate is constant. The earlier "same multiset"/reallocation phrasing is replaced by this; the classes explicitly differ in their d = 2 counts.
3. No broad statement about nonlinear or mixed statistics is made here; the (II) mixed-moment attempt stands only as an unproved step at the stated overlap point, and Theorem D stands unreviewed.
