# Shor completion: common two-power fibre tilings in an even-tail family

Owner **MathShor-2**, math-5. Native clock of the exact synthetic controls: **Wed Oct 28 21:32:44 PDT 2026**.
**ALL-ORDER WRITTEN necessary structure with an explicitly named classical import. It is not a completion, an unrestricted noncompletion result, formal/peer/cross-family verification or a novelty claim.**

## 1. Exact scope and conclusion

Let `k>=2`, `1<=a<k`, `b=k-a`, and `n=165*2^k`. Suppose the SAME actual b-run border factors of a finite UD factor-complete extension of the literal Shor code form a direct tiling

    P+Q=Z_n,     |P|=3*2^a,     |Q|=55*2^b,
    {0,3,8,11} subset P,        Y={0,1,7,13,14} subset Q.   (1)

Here Q is EVEN. For `i=0,1,2` and `j=0,...,54`, define multisets of normalized exponents modulo `m=2^k` from the actual residue representatives `0,...,n-1`:

    P_i={ (p-i)/3 mod m : p in P, p==i mod3 },
    Q_j={ (q-j)/55 mod m : q in Q, q==j mod55 }.

Then EVERY one of the `3*55` pairs `P_i,Q_j` is a **direct set factorization of Z_m**, with cardinalities `2^a` and `2^b`; in particular neither projected multiset has repeated residues. Moreover, for each old tail `j in Y`, all residues in Q_j are even. Equivalently, every actual Q-tail residue in the same mod55 class as an old tail j is congruent to j modulo110.

These are necessary SAME-D conditions, not a construction or a proof that any original completion exists. They apply for every k and every split `1<=a<k` in this cardinality family. They do not use the pending odd-Q/55-tail theorem.

## 2. Explicit named import and prime allocation

We use the **Łaba–Londner common-prime T2 corollary**: in a cyclic tiling where at most two primes divide BOTH tile cardinalities, both tiles satisfy the Coven–Meyerowitz T2 condition. See [Łaba–Londner, Corollary6.2](https://arxiv.org/html/2106.14042v1) and its stated reduction. This is an explicitly imported prior theorem, not independently reproved or a novelty claim.

It applies because the only common prime of `3*2^a` and `55*2^b` is2. The direct-tiling identity puts `Phi_3` in P and `Phi_5,Phi_11` in Q. T2 puts `Phi_55` in Q. Their product is `1+X+...+X^54`, so P is uniform mod3 and Q is uniform mod55:

    |P_i|=2^a,    |Q_j|=2^b

as ACTUAL element counts, prior to folding modulo m.

For each s=1,...,k, the tiling identity puts `Phi_(2^s)` in exactly one of P,Q: the factors each evaluate to2, and the total valuations of the two cardinalities sum to k. Let I_P and I_Q be the complementary index sets.

## 3. The 165 separate fibre factorizations

For every `s in I_P`, T2 with Phi_3 gives

    Phi_(2^s)(X) Phi_(3*2^s)(X) = Phi_(2^s)(X^3) | P(X).

Write the P-mask as `sum_(i=0)^2 X^i P_i(X^3)` BEFORE folding. Uniqueness of this free-module decomposition over `Z[X^3]` implies each normalized P_i polynomial is divisible by `Phi_(2^s)`.

Likewise, for every `s in I_Q`, T2 with Phi_5 and Phi_11 gives the four factors at orders `2^s,5*2^s,11*2^s,55*2^s`. Their product is `Phi_(2^s)(X^55)`. Decomposing the Q-mask by mod55 therefore makes EACH normalized Q_j polynomial divisible by `Phi_(2^s)`.

At every nontrivial m-th root, one of P_i,Q_j vanishes because I_P and I_Q partition the two-power orders. At1, their values multiply to `2^a*2^b=m`. Fourier inversion on Z_m shows the convolution of their folded nonnegative integer masks is identically1. Since both are nonempty, no folded coefficient can exceed1: they are actual SETS and form a direct factorization of Z_m. This holds for every i,j on the same P,Q, not merely for separately chosen witnesses.

## 4. Old anchored fibres have a fixed parity

The normalized P_0 set contains0 and1, coming from the actual old heads0 and3. In each direct tiling `P_0+Q_j=Z_m`, the classical Sands gcd-difference criterion forbids Q_j from having an odd difference, because P_0 has difference1. Thus every Q_j lies in a single parity class.

For `j in Y`, the actual old word `b a^j` gives the tail j, whose normalized exponent is0. Hence that entire Q_j is even, and every actual Q residue congruent to j modulo55 is congruent to j modulo110. This condition does not say that any other fibre is even, nor does it prove a completion exists.

## 5. Controls and limits

`frontier-20261028-even-tail-fiber-check.py`, SHA256 `16c191aa6a8fa42ec62131deeb399407c8416ed5cff3eae69b52e8bc8cffd443` (17 LF, 924 bytes), directly checks all165 fibre-pair tilings and all55 single-parity fibres for the synthetic n2640 factorization `P={0,...,11}`, `Q={0,12,...,2628}`. That control contains old heads0,3 but NOT all Shor old tails, so it is emphatically not a completion. The all-order proof above imports Corollary6.2 and the classical Sands criterion and has not been independently reviewed or novelty screened.

Other even-Q cardinality families, the separate 2310-family branches and the original unrestricted finite UD factor-completion problem remain OPEN.

**END OF EVEN-TAIL TWO-POWER FIBRE STRUCTURE.**
