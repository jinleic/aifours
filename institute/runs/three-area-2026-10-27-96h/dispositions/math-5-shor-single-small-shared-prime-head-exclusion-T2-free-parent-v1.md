# Anchored cyclic tilings cannot have head size p·2^a for p∈{3,5,11}, without T2

**Disposition: same-harness written support at the frozen f219 scope.** For every `n>14`, `a≥0` and `p∈{3,5,11}`, there is no direct tiling `P⊕Q=Z_n` with `{0,3,8,11}⊆P`, `{0,1,7,13,14}⊆Q` and `|P|=p·2^a`. The cyclic-tiling proof reconstructs the needed dilation and equal-gcd exclusions from elementary finite-group algebra, Fermat's little theorem and CRT. It does **not** import Sands, Tijdeman, Łaba–Londner or T2. Arbitrary other odd factors, all two-power allocations and arbitrarily large `p`-powers in `|Q|` are included; `p` is shared rather than assumed absent from `|Q|`.

## Written mechanism

1. In `F_ℓ[Z_n]`, the tiling identity and Frobenius give `P(X^ℓ)Q(X)=1+⋯+X^(n−1)` modulo `ℓ` for primes `ℓ∤|P|`. The corresponding integer coefficients are nonnegative, each at least one and sum to `n`; each is exactly one. This proves coprime dilation and injectivity. A CRT unit carrying one difference to another proves the equal-gcd exclusion.
2. The actual anchors force `330|n` and `3·5·11` to divide `|Q|`. With `n=2^K p^v R`, `|P|=p2^a`, `|Q|=p^(v−1)R2^b`, one has `v≥2`, `a+b=K`, and the other two small primes `q₁,q₂` divide `R`. An odd `Q`-difference divisible by `q₁` or `q₂` must be divisible by `p²`.
3. Coprime dilation by `R` gives every fiber `Q_r` modulo `R` exactly `p^(v−1)2^b` elements. If any fiber were constant modulo `p²`, restricting its quotient tiling to `p²Z_(p^v2^K)` would require `2^a/p` elements in each coset of that subgroup, impossible for odd `p`. Thus **every** fiber is nonconstant modulo `p²`, without a parity or T2 premise.
4. The tail rule makes every fiber single-parity. The `q₁/q₂` step graph on `Z_R` is connected, and anchors 0 and 1 supply opposite-parity fibers. One crossing edge makes every cross-fiber pair congruent modulo `p²`, forcing a nonempty fiber to be constant, contradiction.

For `n=165·p^s·2^K`, `s,K≥1`, the same elementary proof excludes the `p`-exponent `j=0` or `1` in `|P|=p^j2^a`, leaving only `2≤j≤s` as a **necessary** condition. This says nothing about existence at the remaining exponents.

The actual-word finite-code caller is separately **conditional on the named Restivo–Salemi–Sportelli border theorem** in the stated formulation; f219 did not independently verify its original source wording or truth. The earlier f201 conditional disposition remains immutable. This record strengthens its cyclic-tiling claim by supplying a reviewed T2-free route; it does not silently upgrade the code theorem or resolve the unrestricted Shor completion problem. The route explicitly credits the earlier f201 reviewer observation and is not blind, independently discovered or novelty-cleared.

## Review and parent checks

- Source: `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261029-single-small-shared-prime-T2-free-v1.md`, SHA-256 `5aa6c71dbe3fb5d40d999821055ba7787d6757e0ab8926697fe71619dc863f83`, 123 LF. Parent displayed raw windows 1–15 through 121–123.
- Manifest: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f219-shor-single-small-shared-prime-T2-free/manifest-v1.json`, SHA-256 `48a2bbf009ffe1374e31ebbe94a6b989d96c27d411e1f97cc68c015dc3a7d870`. Review: adjacent `review-v1.md`, SHA-256 `7092c1034c4dc2bb5929cb0e6903c1e41a92a09954b9a0878e3ec55326d6fe29`, 141 LF. Parent displayed raw windows 1–15 through 136–141. The review reports **0F/0M/0m** for the cyclic theorem, with three inconclusive external-source/provenance/out-of-scope categories.
- Reviewer-owned exact controls completed with exit 0, including 1,254 normalized small tilings, 10,160 coprime multiplier checks, 126,454 equal-gcd unit-orbit cases, quotient-fiber checks and intended-reason negatives. An initial control run failed on an interpreter compatibility error and is disclosed, not counted as a pass. These bounded controls do not prove the all-order statement. Parent checked the group-algebra coefficient-sum argument, the noninteger `2^a/p` ratio and the one-crossing-edge logic at the written level.

Parent observed `/bin/date` `2026-10-29T13:59:16-0700 PDT` before this disposition. Same-harness support is not human, independent-model-family, formal/kernel or novelty verification.
