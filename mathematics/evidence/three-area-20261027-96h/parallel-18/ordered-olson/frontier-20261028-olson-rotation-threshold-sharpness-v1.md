# Separate sharpness control for R=p+1 (not an L_RES counterexample)

MathOlson-2-2. Native `/bin/date` before writing: **Wed Oct 28 22:37:28 PDT 2026**. WRITTEN separate control candidate, not a disjoint review or novelty claim. It does not enlarge any already frozen review of `frontier-20261028-olson-L-RES-universal-band-proof-v1.md` (SHA256 `32c5a485006c3d86cd7d49b7b9bd29922fa67ded560a20cb16af9f5794e5d40c`). The fatal history `frontier-20261028-olson-actual-block-fatal-correction-v1.json` (SHA256 `e11fd87345f8a54012f3a9245d87491c6ceb3a4a113558be07ca4ab62728f90e`) remains unchanged. No old verdict transfer.

## 1. Exact control family

For any odd prime p and a!=0 let b=−a/2. The actual word

`V=σ_0^(2p−1) ρ_b σ_aρ_b σ_(2a)ρ_b ... σ_((p−1)a)ρ_b`

has F=3p−2 reflections but only **R=p** rotations and length4p−2. It has NO original-order identity subsequence of length2p. Thus the rotation-count requirement p+1 in the new band theorem cannot be replaced by p. This is a boundary control, NOT a counterexample to that theorem, L_RES (whose R is p+1), or the length4p−1 Olson statement.

## 2. Complete direct proof

Normalize a=1. Consider an actual length2p selection. Let k be its selected rotation count; if k is odd, its reflection count2p−k is odd, so its product is a reflection, not1. Assume k is even; then k<=p−1.

Let t be the number of selected nonzero reflection labels and z the selected zero count. Then z+t=2p−k is even. If t=0, z<=2p−1 forces k>=1, hence even k>=2; the product is `ρ_(bk)`, nonidentity since 2<=k<=p−1 and b!=0.

If t>0, write selected tail labels as `1<=j_1<...<j_t<=p−1`. With all rotations skipped, the reflection product exponent is −L, where

`L=(j_2−j_1)+(j_4−j_3)+...` if t is even,

`L=j_1+(j_3−j_2)+(j_5−j_4)+...` if t is odd.

The disjoint positive integer intervals give `1<=L<=p−1`. Among ALL p actual rotation gaps, the prefix sign of selected reflections is negative in exactly L gaps: for even t, those gaps are `[j_1,j_2−1]`, `[j_3,j_4−1]`, etc.; for odd t they are `[0,j_1−1]`, `[j_2,j_3−1]`, etc. Select q_- rotations in negative gaps and q_+ in positive gaps. Thus `0<=q_-<=L`, `0<=q_+<=p−L`, and `q_-+q_+=k` is even. Exact actual-order multiplication (or conjugating rotations through the selected reflection prefixes) gives exponent

`−L−(q_+−q_-)/2 = −C/2`,  `C=2L+q_+−q_-`.

C is EVEN, while `1<=L<=C<=p+L<=2p−1`. The only possible multiple of the odd prime p in that strict interval is the ODD number p, so C is not divisible by p. Hence the selected product is never1. QED.

## 3. Finite diagnostics, no scope promotion

`frontier-20261028-olson-rotation-threshold-sharpness-check-v1.py` SHA256 `e3f91a8872b684ddff2e51a5c1854f70224c598de7c5fcb615bfb7dd8ecf1314` generated full words and computed their complete length2p group-product support at p=3,5,7,11,13,17. Data `frontier-20261028-olson-rotation-threshold-sharpness-results-v1.json` SHA256 `a2c4e5d98a5cf13a92658a73c543a388432833389741ad535ad74b921e291580` contains no identity in those supports.

Independent `frontier-20261028-olson-rotation-threshold-sharpness-audit-v1.py` SHA256 `1aa8a8f8a95d082a7006b1dac8179b84d4303569e65b717907f4ce82e475560d` imports no producer and reconstructs the negative-gap count and integer parity obstruction for all 3/15/63/1023/4095/65535 nonempty tail subsets respectively; it also checks all admissible (L,q_-,q_+) integer triples with even k at these primes. Its receipt `frontier-20261028-olson-rotation-threshold-sharpness-audit-results-v1.json`, SHA256 `587a7d2688ac93423dc3c19c39f311dec273a03f65c5a3370212b40f46b4bf31`, records PASS and a positive control (one extra zero reflection yields an explicit first2p zero-reflection identity). These are bounded same-model checks, not external-family/formal verification, an independent scientific review, or novelty clearance.

**END — R=p boundary control only.**
