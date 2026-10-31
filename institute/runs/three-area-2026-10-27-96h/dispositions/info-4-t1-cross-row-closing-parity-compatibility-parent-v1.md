# Actual T1 rows: joint closing-permutation parity

**Disposition: same-harness written support for a universal necessary compatibility identity.** Native clock before composition: 2026-10-30T08:12:48-0700 PDT. f329 reports0F/0M/0m. No T2(11) profile, boundary branch or realization is excluded.

## Theorem and exact hypotheses

For any actual T1(n), n>=2—n separately indexed directed permutation rows on n symbols with distinct directed adjacency events—index rows by their first symbolc, let E(c) be the last symbol and pi_c the closing adjacency-row permutation on S minus{c,E(c)}. Then

product_c sign(pi_c)=(-1)^[n(n+1)/2] sign(E).

For n11 this reduces to product sign(pi_c)=sign(E). Distance2 injectivity, boundary-column permutation assumptions and symmetry are not required.

## Written reconstruction

The n(n−1) adjacency events exhaust all ordered distinct pairs. Incoming/outgoing counts force each first and last column to be a permutation; E(c)!=c. Adjoin infinity to each EXISTING row as one directed n+1 cycle. Define H(x,y) as its unique augmented-row label whenx!=y and infinity on the diagonal. It is an actual Latin incidence square: every row/column map is a bijection; sigma_infinity=id and tau_infinity=E^−1 extended to fix infinity. A symbol class corresponding to each original row is one Hamilton cycle, not an arbitrary degree-compatible cycle cover.

For a=E(c), Phi_c=tau_c^−1 sigma_a fixes infinity, swaps a/c and restricts to pi_c on the complement. Its sign is therefore minus sign(pi_c). For a general Latin square of orderN, let A(x,y)=(x,H(x,y)), B(x,y)=(H(x,y),y), D(x,z)=(h_z(x),z) and T swap coordinates. The exact identity D A=T B gives the product of row/column/symbol permutation signs equal to(-1)^[N(N−1)/2]. In our augmentation the symbol-sign product is(-1)^[n²]; multiplying the closing-transposition signs and including tau_infinity cancels the extra(-1)^n and gives the displayed theorem. Parent checked this map equality and all exponent/orientation factors in universally quantified algebra; no specific Latin square/permutation was selected.

At n2 the closing permutation is the empty-set identity and the same structural sign equation holds. A local fixed point of pi_c corresponds to a two-adjacency occurrence of the closing pair already under T1. T2 additionally supplies distance2 uniqueness andcardM=n, so its prior equivalence M=closing-pair set iff every pi_c is a derangement remains at the original T2 scope. All mixed/full-source/full-target cases remain live. Neither axiomatic independence from all prior invariants nor exclusion by parity alone is established.

## Evidence and assurance

Parent displayed complete199 logical-line f327 candidate, complete363 logical-line f329 review (362LF) and all three adopted input dispositions; live hashes/bytes/LF match. Reviewer independently reconstructed all Latin/closing bijections, the universal sign proof and all n>=2 cases from the full270LF packet with no scientific executable or selected mathematical instance.

[Review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f329-tuscan-cross-row-closing-parity-review/review-v1.md) · [Manifest](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f329-tuscan-cross-row-closing-parity-review/manifest-v1.json) · [Original closing interface](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-4-tuscan-adjacency-row-closing-derangements-parent-v1.md). Same-harness only: no actual T2(11) witness/no-go, sufficiency, branch exclusion, source-wide status, human, independent-family, formal/kernel or novelty acceptance.
