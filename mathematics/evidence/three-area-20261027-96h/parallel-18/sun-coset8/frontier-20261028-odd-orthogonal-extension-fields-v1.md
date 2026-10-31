# Odd-dimensional orthogonal simple groups over degree-at-least-three extensions

**Status: WRITTEN candidate, conditional on the public theorem stated below; not independently reviewed or accepted.** Let n≥9 be odd, p an odd prime, f≥3, q=p^f, and G=Ω_n(q) the finite nonabelian simple odd-dimensional orthogonal group. Then no three proper subgroups of G have indices with every pairwise gcd at most 7. Hence this family excludes both direct P7 and Sun8 configurations. No Sun7, normal-section theorem, priority or novelty claim is involved. This does not claim f=1 or f=2, even dimension, or characteristic 2.

## 1. Source and mathematical inputs

- The Ω_n(q), r_(n−1) row of Theorem 2/Table B, Remark 9.2 and Proposition 6.9 in https://arxiv.org/html/2307.13976v2: for odd q, odd n≥9, a primitive prime divisor r of q^(n−1)−1 with α(n−1,1) and r>2n−1 has a unique maximal overgroup of a Sylow r-subgroup. This is a stated external classification import; neither the classification nor its underlying computations are independently reconstructed here.
- The standard simplicity and order of Ω_(2m+1)(q) for m≥4, q odd:
  \[|G|=\frac12 q^{m^2}\prod_{i=1}^m(q^{2i}-1).\]
- Zsigmondy's theorem for p^((n−1)f)−1, exponent at least 24, outside its exceptions.

The parent directed continuation after the separately recorded incidental cross-topic search; no content from those snippets is used here, and no clean-cognition or historical-hold rehabilitation claim is made. No broad search for earlier family coverage is asserted.

## 2. Prime selection and written proof

Choose r with ord_r(p)=(n−1)f. Since q=p^f, ord_r(q)=n−1; thus r is a primitive divisor of q^(n−1)−1 and divides |G|. Further,
\[r\equiv1\pmod{(n-1)f},\qquad r\ge (n-1)f+1\ge3n-2>2n-1>7.\]
For each relevant prime k|f, p^((n−1)f/k)≠1 mod r by the exact order. This is precisely α(n−1,1). The public source therefore supplies exactly one maximal overgroup M of the fixed Sylow r-subgroup R.

The index [G:M]≥8: a proper subgroup of smaller index would produce an injective coset action into S7 because G is simple, but r>7 divides |G|. In any three subgroup indices with pairwise gcd≤7, at most one is divisible by r. Each of the other two subgroups contains a Sylow r-subgroup and, after conjugation, contains R. Both lie in M, so both original indices are multiples of [G:M]≥8, contradiction. This is a statement about actual finite simple groups and their actual subgroups; it is not merely a numerical divisor relaxation.

## 3. Finite checks and review scope

`frontier-20261028-odd-orthogonal-check.py`, SHA-256 `17477e04d26e78cebe49efc978ac9aa0a80db204dfba423503c1775ef165ba22`, 39 LF / 1039 bytes, ran at 18:34:25 PDT on 2026-10-28. It verified primality and exact modular orders for four named (n,p,f,r) examples, including the source α tests and r>2n−1. These checks do not establish the infinite prime-existence theorem or classify any subgroup.

**Review-critical:** verify the exact Table B row/Proposition 6.9 scope for the simple group Ω_n(q), the inequality for all n≥9 and f≥3, the primitive-prime/subfield condition, and the Sylow/index proof. The external classification, Zsigmondy, order and simplicity statements remain unreproduced imports.
