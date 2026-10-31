# Distance-two incidence counts and the conditional permutation table

**Disposition: partial same-harness written support from f282, with its exhaustive-branch claim rejected.** Native clock before composition: 2026-10-29T21:07:16-0700 PDT. Review verdict **0F/1M/2m** remains attached to the original 63-LF manuscript. Parent read that source, the complete 279-LF return, the 22-LF status handoff and all three 17/22/22-LF named imports. Bindings match. The later five-line erratum and 45-line functionality successor were read separately; neither was part of f282's frozen input or changes that review retrospectively.

## Adopted universal counts

For every linear T2(n), n≥2, define k_j as the number of unordered symbol pairs occurring at distance two in exactly j rows. Injectivity allows at most one event in each orientation, so j∈{0,1,2}. There are n(n−2) distinct directed events and n missing ordered pairs. Counting events and missing directions gives

- k₀+k₁+k₂=n(n−1)/2;
- k₁+2k₂=n(n−2);
- 2k₀+k₁=n.

Thus k₁=n−2k₀ and k₂=n(n−1)/2−n+k₀, with k₁≡n mod2. These hold without any boundary-column assumption. At n=11 all six nonnegative count possibilities are (t,11−2t,44+t), t=0,…,5. They are arithmetic possibilities, not realizations or exclusions. A one-permutation-column hypothesis does not reduce that count set.

## Conditional structural branch

The missing-pair digraph M has out-degrees equal to penultimate-column multiplicities and in-degrees equal to second-column multiplicities. It is a loopless permutation digraph **if and only if both columns are permutations**. In that branch its mutual missing pairs are exactly its two-cycles. At n=11, deleting t two-cycles leaves a partition of 11−2t into parts at least three, so t=0,…,4. The source's fourteen types split into groups of sizes 6,4,2,1,1 and its five-profile table is correct under that hypothesis. The complementary exhaustive branch is a full source **or** full target, possibly both; exactly one permutation boundary column has not been ruled out for actual arrays.

If M=E⁻¹ for the endpoint permutation E, k₀ equals the number of two-cycles of E. The explicit adjoining-∞ circular-completion interpretation is supported by counting the added last→first, penultimate→∞ and ∞→second events. No f204 automorphism classification is newly adopted: that unlisted body and its precise group action were not checked here. Conditional on the already adopted odd-order-21 group-table construction, M is right multiplication by the one missing nonidentity quotient; odd group order forbids a two-cycle and gives (0,21,189). This does not establish that M has three seven-cycles merely from E having that cycle type.

## Rejected assertions and later packets

- **M1:** penultimate-column permutation alone implies only out-degree one, not in-degree one. It cannot justify the fourteen-permutation-type branch. The reviewer gives a degree-theory countermodel with five mutual pairs and an extra incoming arc; this is not a T2(11) construction. The late erratum correctly narrows the permutation branch but does not make the old gate compliant or dispose of the omitted case.
- **m1:** the displayed order-six vector (3,0,12) has k₁+2k₂=24, not30.
- **m2:** a permutation entirely composed of two-cycles has t=n/2, not n(n−1)/2.
- Raw-row diagnostics and finer order-eight/profile censuses are not independently verified here. The universal equations do not force k₀=0 at n=8.

The later functionality packet's count formula is already a corollary of the universal equations above. Its stronger claim image(m)=S∖{z} is **not established** by the existence of some zero-indegree symbol: the correct general image omits the whole nonempty set {z:α₁(z)=0}, which may contain several symbols. No wholesale adoption of that successor, global absence-of-mixed-array status or one-column-forces-other theorem is made. Likewise “only the odd-k₁ law survives” is not a complete numerical interface: all three universal equations remain in force in every branch.

The first actual-array realizability gap remains open. Neither the fourteen conditional types nor the sixth numerical possibility nor any complementary boundary case is excluded; T2(11) has no witness/no-go from these packets. Parent verification is the all-variable event/missing-arc counting and partition argument above, not a selected-array computation. Source, review, late-packet pins and coverage are in the companion receipt in the [f282 wave directory](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f282-tuscan-distance-incidence-interface/). Same-harness only; no human, independent-family, formal/kernel, priority or novelty verification.
