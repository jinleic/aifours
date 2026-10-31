# Shor code: no anchored border tiling at n=165·2^t for any t≥1

**Disposition: same-harness written support, conditional on the explicitly named classical tiling imports.** For every integer t≥1, no direct factorization P⊕Q=Z_(165·2^t) contains A={0,3,8,11} in P and Y={0,1,7,13,14} in Q. There is no restriction on either factor's cardinality or parity.

For the literal code S=b{1,a,a^7,a^13,a^14} ∪ {a^3,a^8}b{1,a^2,a^4,a^6} ∪ a^11b{1,a,a^2}, it follows that no finite uniquely decipherable, factor-complete extension has actual pure-a atom a^(165·2^t). This is an infinite order-family exclusion, **not** unrestricted noncompletion, a new order floor, a novelty claim, or a statement at t=0.

Native clock before composing: **2026-10-29T09:22:22-0700 PDT**.

## Proof and exact import boundary

The same-code border argument is reconstructed from finiteness, unique decipherability, factor-completeness and b∈S: a pure-a atom exists and is unique; actual a^i b^k and b^l a^j atoms define P,Q; guarded words b^H a^G b^K prove directness by the positions of the last left b and first right b, and factor-completeness proves coverage. The sets are not borrowed from different codes.

Sands' divisor exclusion gives the opposite-parity rules: P differences must be divisible by one of 3,5,11, while Q differences cannot be divisible by exactly one. For odd differences gcd(u,165·2^t)=gcd(u,165), making the finite mod330 reductions exact for every t≥1.

**Load-bearing imported result:** Łaba–Londner arXiv:2106.14042v3, Corollary6.2, giving Coven–Meyerowitz T2 when at most two modulus primes divide both factor cardinalities. Here 3,5,11 occur to the first power and only2 can divide both. The reviewer checked the exact source statement and its hypotheses; the underlying Coven–Meyerowitz two-prime theorem, Tijdeman dilation theorem and subgroup reduction remain classical imports, not newly proved results.

T2 forces uniformity modulo the odd parts d,e of the factor cardinalities, with de=165. Three forbidden P classes reduce d to1,3,5,11. The first three cases give short residue contradictions. For d=11, the six-step Q structure gives Q mod55=Y with fixed parity by mod3; its mask is nonzero at orders11,22,55,110. Hence the P mask is divisible by their cyclotomic product (X^110−1)/(X^10−1), forcing10-periodicity after folding mod110. The anchor11 then forces an x≡1 mod110; comparison with heads0 and8 requires x≡0 and2 mod3 simultaneously. All divisions, parity boundaries, empty classes and uniformity hypotheses are covered in the source and the two reviews.

At n=330 the anchors already collide under Sands because gcd(8,330)=gcd(14,330)=2; the longer proof is redundant there. Without the T2 import the all-cardinality argument is not established by these reviews.

## Sources, corrections and reviews

- [Candidate](/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261029-165-family-all-q-anchored-border-no-go-v1.md), SHA `20169ac9e398d9d1ef37d263f9b51d0f9168c095c3e3eb21ade47572822d39c6`, 312 LF; parent read it completely, together with both complete reviews.
- [Additive erratum](/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261029-165-family-all-q-anchored-border-no-go-erratum-1-v1.md), SHA `54329f3e5d40ff6382c3de01ac029f638f88d0e52e246b159346d337491c1585`, 58 LF, read completely. It postdates both review inputs; no before-source reviewer claim is made. The d=5 comparison is −11, not11; the n330 shortcut is stated; author-checker records versus assertions and stale section labels are distinguished. Its historical “f176 pending” status is not a current queue statement.
- [f176 proof review](../review-waves/f176-shor-165-all-tail-written-proof/review-v1.md), SHA `28f7899153b343ccd0d52b4ba15152fe170274d323d480b242f7622f6b763a46`: **0 FATAL / 0 MAJOR / 4 MINOR**. Border reconstruction, all uniform cases and import hypotheses checked;50/50 own controls, including exhaustive n660 complements under the derived Q structure. Numerical duration161.902s and earlier capped prototypes are disclosed; no cap is an exclusion. The import's truth, author-run receipt, subsumption claims and owner provenance are not certified by that review. [Receipt](../review-waves/f176-shor-165-all-tail-written-proof/reviewer-f176-review-v1-receipt.json).
- [f177 finite review](../review-waves/f177-shor-165-all-tail-finite-audit/review-v1.md), SHA `fed47b9dd99a155617985f0c6ffe7fbef11feca18632ebce01f67319798ce26c`: **0 FATAL / 0 MAJOR / 3 MINOR**,71/71 exact checks, independently authored CRT/valuation/AC/backtracking/cyclotomic methods. This slice alone does not verify the imports or code-to-tiling bridge; the f176 slice supplies those interfaces conditionally. [Receipt](../review-waves/f177-shor-165-all-tail-finite-audit/reviewer-f177-arith-receipt-v1.json). Its unintended bytecode directory is retained.

The two reviews share a harness and saw the author checker before writing their own code; neither is blind or independent-model-family verification. All frozen source bytes remain unchanged.

## Parent checks and limitations

Parent reconstructed the guarded-word border argument, the squarefree-prime allocation, the all-t odd-difference reduction and the final cyclotomic-to-periodicity contradiction. An independent integer control checked the three forbidden mod330 head classes, d=1, the final types {1,111,221}, and the intended anchor-removal cases ([receipt](../review-waves/f176-shor-165-all-tail-written-proof/parent-residue-contradiction-control-v1.json), SHA `1bcf298a9f6690e954caa355ec50b2d404e8a6a9f4116f506c5b8866bbd76e23`). Each final constraint alone permits a type, while the pair excludes all; removing tail14 restores the d=1 type167.

No Q55, fibre packet, held output or earlier branch verdict is used as a mathematical premise. The new2310·2^k Tijdeman-only candidate is a separate f189 review, not adopted here. All conclusions remain same-harness and conditional on the named tiling inputs, not formal/kernel, human, novelty or original-problem closure.
