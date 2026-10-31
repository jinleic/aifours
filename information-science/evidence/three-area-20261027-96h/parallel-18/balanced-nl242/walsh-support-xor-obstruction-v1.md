# info-6: a source-separated support-XOR obstruction for the original balanced target

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Actual `/bin/date` observed before this write: **2026-10-27T15:02:45-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** This excludes one broadly quantified branch of a putative original object, not the unrestricted target. No scientific program, chosen numeric state/direction, rank selection, formal/kernel or novelty claim.

## Claim

For a balanced Boolean f:F₂⁹→{0,1}, define the **original truth-support XOR** T=Σ_{x:f(x)=1}x. If |W_f|≤28 at every frequency, then

1. T≠0;
2. at least 86 frequencies have |W_f|=28.

Thus every putative witness remains in the T≠0 branch; this does not establish that any exists or exclude that remaining branch. Equivalently, a balanced f with T=0 has Walsh peak at least 32, hence nonlinearity at most 240. That is a conditional branch statement, **not** an unrestricted upper exclusion.

T is defined directly from all 512 original truth bits; it is not a selected historical rank, weight, state or held parameter. All nonzero values of T, all original rank/weight alternatives and `(24,24,2)` remain included.

## 1. Elementary nonzero-polynomial weight fact

If P:F₂ⁿ→F₂ is a nonzero multilinear Boolean polynomial of degree at most d≤n, then it is 1 at at least 2^{n−d} inputs. Proof by induction on n: write P=P₀+x_nP₁. If P₁=0, double the count for P₀. If P₁≠0, at each input where P₁=1 exactly one of the two x_n values makes P=1, so the count is at least the count for nonzero P₁ of degree at most d−1. Constants and zero derivatives are included. This is proved here from Boolean arithmetic, not imported as a rank-classification theorem. ∎

## 2. The even-residue quadratic on any subspace of T^⊥

Put k=W_f/4. The definition-first coupling gives, for all a,b,

    k(a) mod 2 = a·T,
    k(a+b)−k(a)−k(b) ≡ 2B(a,b) (mod 4),                         (1)

with B a symmetric F₂-bilinear form on the full frequency space. Let K≤T^⊥ be any linear subspace. On K all k(a) are even, so Q(a):=k(a)/2 mod 2 is well-defined and Q(0)=0. In a basis of K, iterating (1) expresses Q as a Boolean polynomial of degree at most 2; no polar rank is selected or classified. Therefore P=1+Q is nonzero, P(0)=1, and the weight fact shows

    #{a∈K:Q(a)=0} ≥ |K|/4.                                     (2)

## 3. Excluding T=0 and forcing the |W|=28 multiplicity

Suppose |k|≤7 at every frequency. If T=0, all 512 values of k are even, so |k|≤6. Take K=V. By (2), at most 384 frequencies have Q=1; the remaining at most 127 **nonzero** frequencies have Q=0 because k(0)=0. On Q=1, |k|≤6; on Q=0, |k|≤4. The total energy would satisfy

    2¹⁴=Σ_a k(a)² ≤ 36·384+16·127 < 2¹⁴,

a contradiction. Therefore T≠0. The last inequality is an all-frequency estimate, not a numerical input test.

Now K=T^⊥ has 256 points and (2) gives at most 192 points with Q=1. Its other nonzero points number at most 63; on K the respective square bounds are 36 and 16. On the opposite affine half all 256 coefficients are odd; if n₇ of them have |k|=7, the others have square at most 25. Hence

    2¹⁴≤49n₇+25(256−n₇)+36·192+16·63,

which forces n₇≥86. Every counted coefficient is at magnitude 28 in the original W scale. ∎

## Exact import and status boundary

The proof uses only the supplied S1 original definitions, the exact all-variable Walsh/parity caller derived in `prerequisite-derivation-v1.md` SHA-256 `075f61ffe1b5cfb000bb3bbda9ddd7fefea04e27806f19bedd9c5a2318fa3df9`, 87 LF, and the elementary polynomial induction proved above. It does not read or invoke an old Gate-I result, candidate, rank classification, held source or selection/method guide. Prior same-author exposure remains disclosed; there is no blind-review or clean-cognition claim.

This author candidate is a universal structural obstruction to the T=0 branch and a necessary frequency multiplicity in the surviving branch. It does **not** rule out T≠0, construct a Boolean inverse or solve NL242. Main-authored definition-to-book equivalence, independent complete written review, human, formal/kernel, executable and novelty gates remain NOT PERFORMED. All S1 STOP/HOLD/ZERO/NONINPUT, N4 UNKNOWN and aux214 STOP remain binding.
