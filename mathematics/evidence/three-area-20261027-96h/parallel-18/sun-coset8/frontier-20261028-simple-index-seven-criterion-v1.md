# Index-seven simple groups and a prime-support exclusion criterion

**Status: WRITTEN-checked-in-kernel, source-conditional and UNREVIEWED.** Assuming Jones's versioned primitive-cycle classification at k=0, the only finite nonabelian simple groups admitting a subgroup of index 7 are A7 and GL3(2)≅PSL3(2). Both have seven distinct index-7 subgroups and seven pairwise disjoint corresponding left cosets which partition the group. Consequently a universal claim that seven subgroup indices cannot all have pairwise gcd 7 is false even with distinct subgroups and disjoint cosets. These examples have **seven**, not eight, cosets and do not refute Sun8 or settle a source-specific P7 definition with additional premises.

For every other finite nonabelian simple group S, if 7 divides its order and the integer |S|/7 has at most six distinct prime divisors, then seven proper-subgroup indices with pairwise gcd 7 are impossible. If 7 does not divide |S|, the conclusion is immediate. This is an actual-simple-group criterion with a stated order hypothesis, not a classification of every simple group, an all-group Sun8 result, an infinite-family or novelty claim.

## 1. Source boundary and correction order

Before any earlier affected candidate or successor, read the three complete additive overlays in order: `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`; `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` SHA `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`; and `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` SHA `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`. In particular, the previous at-most-one-unit claim is withdrawn. No historical hold or frozen source is edited.

The sole substantive classification import is Gareth A. Jones, [arXiv:1209.5169v1, Theorem 1.2, k=0](https://arxiv.org/html/1209.5169v1), precisely frozen in `frontier-20261028-jones-k0-source-v1.json` SHA `ce6d3b4a032bf9fe04446c87a538d09e012142ef4fbc1e29853a31c29769130a`, with pinned HTML SHA `5c85e920dd479c8f4834e33184c4c4b495f8e3a2e078a95ece3ab6b203c2848b`. The source says its proof uses classification of finite simple groups; that proof was not replayed. Elementary finite-group facts, Cauchy's theorem, coset actions and Sylow/order divisibility are also used. The author's incidental nonblind cross-topic display was disclosed separately; no such excerpt is used.

## 2. Classification of index-seven simple groups

If a finite nonabelian simple group S has a subgroup of index 7, the coset action is faithful: its core is normal and proper. Thus S is a transitive degree-seven subgroup of S7. It is primitive because a nontrivial block size would be a proper divisor of 7. By Cauchy's theorem S contains an element of order 7, necessarily a 7-cycle in this faithful action.

If S contains A7 then S=A7, since S embeds in S7 and simplicity prevents the sign map from being a surjection onto C2. Otherwise apply the imported Jones theorem at k=0. Its affine case contains a normal cyclic subgroup C7 and is not nonabelian simple; its sporadic cases have degree 11 or 23. In the projective case,

\[7=1+q+\cdots+q^{d-1},\qquad d\ge2.\]

For d=2 one gets q=6, not a prime power; for d=3 one gets q=2; and for d≥4 the sum is at least 15. Thus d=3,q=2. There is no field automorphism and the scalar center over F2 is trivial, giving S=GL3(2)=PGL3(2). The simple-group assertion for this specific group is independently reducible to the following finite arithmetic certificate, but has not received an independent review.

## 3. Seven actual cosets in both groups

For A7 take the seven point stabilizers H_i. They are distinct of index 7. Choosing g_i with g_i(i)=1 gives g_iH_i={g:g(i)=1}, and these seven sets partition A7. A separate parent exact check of this construction reports group order 2520, all seven stabilizer orders 360, all 21 gcds 7, partition verification and a rejected duplicate-coset mutation: `review-waves/f134-alternating-all-degrees-p7/parent-a7-cosets-exact-result-v1.json`, reported SHA `f76b3a00ee3e1a7b86692db8c0b700c17ad5de7ba9525672714a133b1be76339`. This is one independent parent check, not three independent checkers or formal verification.

For GL3(2), act on the seven nonzero vectors of F2^3. The action is transitive, since any nonzero vector extends to a basis. The group has order (8−1)(8−2)(8−4)=168, so each point stabilizer has order 24 and index 7. The seven point stabilizers are distinct: a transvection can fix one prescribed nonzero vector while moving any different one. The seven left cosets with a fixed target vector are its point-preimage fibers and partition the group.

Author checker `frontier-20261028-gl32-index7-check-v1.py` SHA `de3d309fa78f46c971604b9fd8d6c38a5b678f3cb61fc5a07552b2f4663d6d64`, 62 LF / 2474 bytes, was executed inside the author's eval kernel before 20:48:28 PDT on 2026-10-28. It enumerated all 168 invertible binary matrices, verified the seven distinct stabilizers of order 24 and equality of each point-preimage fiber to a left coset, and checked their disjoint union. It also checked element counts by (conjugacy-class size, element order) as `(1,1):1`, `(21,2):21`, `(24,7):48`, `(42,4):42`, `(56,3):56`. Thus the conjugacy-class sizes are 1,21,24,24,42,56. No sum of the identity size and a nonempty proper selection of the other five sizes divides 168, so Lagrange's theorem excludes a nontrivial proper normal subgroup. This is an author-only machine-assisted simplicity argument, not an independent checker, formal proof or source-proof replay.

## 4. Cofactor bound without the repeated-unit error

Suppose S is not A7 or GL3(2) and seven proper-subgroup indices satisfy gcd(m_i,m_j)=7 for i≠j. Their gcd condition makes each m_i=7a_i and the a_i pairwise coprime. Since the classification proves that S has no index-7 subgroup, **every a_i>1**, rather than merely assuming units cannot repeat. Lagrange gives a_i dividing |S|/7. Every a_i therefore needs a prime divisor of |S|/7, and the seven selected primes must be distinct. If |S|/7 has at most six distinct prime divisors, this is impossible. This proof remains valid if 7² divides the group order: 7 is then counted among the possible prime divisors of |S|/7.

## 5. Review boundary

A disjoint reviewer should independently check the exact Jones k=0 hypotheses and degree-7 case split, verify that no affine case can be nonabelian simple, and independently reconstruct the GL3(2) group, conjugacy classes and seven cosets without importing the author's checker. The prime-support implication uses subgroup indices only and does not prove that every abstract cofactor tuple is realizable. Neither the k=0 source proof, an external human/model review, a Lean proof nor a priority screen is claimed. No all-simple-group, source-specific P7, eight-coset counterexample, or arbitrary-group conclusion follows.
