# Plateaued support XOR and the two redundant coupling conditions

**Disposition: scoped same-harness written support, with the advertised N2-additionality claim rejected.** Native clock before composition: 2026-10-29T20:43:14-0700 PDT. The f277 reviewer reports **0 FATAL / 1 MAJOR / 2 MINOR**. Parent has now read the complete 82-LF manuscript, 18-LF checkpoint, 266-LF returned review, and the three 151/24/31-LF named imports. Source and import bindings match the frozen manifest.

## Adopted statements

1. For every perfect signed array μ:F₂ⁿ→{0,±1} satisfying μ*μ=wδ₀ with **4 dividing w**, the XOR of its support is zero. This includes the weight-16 theorem on F₂⁶ and the normalized dual of a plateaued Boolean function whose Walsh support size is divisible by four.
2. At the expressly adopted rank-two, eight-zero, m=116, (0,4,8), (G₃,H)=(1,0) residual, **both (N1) and (N2) already follow from the frozen system**. They remain valid derived necessary conditions but do not shrink its feasible set. The weight-16 theorem independently explains N1. The original u-side realizability problem and odd-half capped sign problem (V) remain unpaid; no witness or exclusion follows.

## Parent reconstruction

In the integral group ring put uᵢ=gᵢ−1, so uᵢ²=−2uᵢ and u_Su_T=(−2)^|S∩T|u_(S∪T). The basis change from g^c to the square-free u_S is integral triangular with diagonal one. For x=Σμ(c)g^c=Σa_Su_S, x²=w gives a_∅²=w and the degree-one coefficient 2aᵢ(a_∅−aᵢ)=0. Thus aᵢ is zero or a_∅; since 4|w, a_∅ is even. But aᵢ=Σμ(c)cᵢ is congruent modulo two to the support's ith coordinate count. Every coordinate XOR vanishes. No finite instance or executable calculation is needed for this proof.

For N2, the imported common ternary inverse u is balanced and its Walsh transform is 2k, divisible by four on the relevant characters. Hence the half-character sum [û(0)−û(0,s)]/2 is even for each s∈P, forcing the P*-projection Z of XOR(supp u) to vanish. A three-entry block contributes its missing point z₀(c); a full/empty block contributes zero. Each two-entry type contributes a fixed nonzero difference, with even type counts 4,6,18 at H=0. Their contributions cancel, leaving Z=⊕_(c∈D)z₀(c)=0, precisely N2. This uses the full displayed residual system, not an independence assumption about gap positions.

## Rejected or corrected assertions

- **M1:** manuscript C2/C3 and the checkpoint repeat that N2 is genuinely additional or that the prior non-implication claim survives for N2. Rejected by the derivation above. Parent messages that instructed the owner to keep treating N2 as new were also wrong and have been withdrawn; the owner has acknowledged the correction.
- **m1:** C4 must restrict perfect-array weight to 4|w. The relevant even flat amplitude is the normalized dual's √w=2^((n−t)/2), not the Boolean Walsh amplitude 2^((n+t)/2). Augmentation makes w an integer square, so the purported perfect-array case w≡2 mod4 cannot occur. Singleton support supplies the stated counterexample when the weight restriction is removed.
- **m2:** the opening provenance pin is only 60 hexadecimal characters. Use the full base identifier printed in the source's final pin table; the base itself was not reopened for this disposition. This is a pin-transcription correction, not evidence of source mutation.
- The assertion that no mod-two argument of any kind could prove the theorem remains unestablished. Only the vacuity of the particular reduced square identity is shown.

## Evidence and limits

The source, returned review, manifest and named imports are bound in the companion parent receipt in the [f277 wave directory](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f277-nl242-plateaued-support-xor/). The reviewer used written reconstruction and metadata-only tools, with compulsory procedural reads disclosed; no reviewer scientific program or author code was run. Parent verification here is the all-variable written argument above, not an executable replay. Same-harness only: no human, independent-model-family, formal/kernel, source-equivalence or novelty certification.
