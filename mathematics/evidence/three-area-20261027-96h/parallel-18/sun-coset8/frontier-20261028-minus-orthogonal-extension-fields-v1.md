# Minus-type orthogonal simple groups over nonprime extension fields

**Status: WRITTEN candidate, conditional on the named public theorem; not independently reviewed or accepted.** Let q=p^f for any prime p and f≥2. For each dimension

- n=2a with a≥5 prime, or
- n=2^a with a≥3,

the finite simple group PΩ_n^−(q) has no three proper subgroup indices with every pairwise gcd at most 7. In particular it has no direct P7 or Sun8 configuration. This is not a claim for other dimensions or f=1; it uses neither Sun7 nor a normal-section theorem. No priority or novelty claim is made.

## 1. Source inputs

The PΩ_n^−(q), r_n rows of Theorem 2/Table B and Proposition 6.11 of https://arxiv.org/html/2307.13976v2 give the following. If r is a primitive divisor of q^n−1, β(n/2,−1) holds, and r>n+1, then a Sylow r-subgroup R has exactly one maximal overgroup when either n=2a, a≥5 prime (unitary-type row), or n=2^a≥8 (extension-field orthogonal-type row). We use these exact sufficient branches only, with G=T the simple group. The classification proof and its cited dependencies are not independently reproduced here.

We also import the standard simplicity/order formula for these dimensions,
\[|P\Omega_{2m}^-(q)|=\frac{q^{m(m-1)}(q^m+1)\prod_{i=1}^{m-1}(q^{2i}-1)}{\gcd(4,q^m+1)},\]
and Zsigmondy's primitive-prime-divisor theorem at exponent nf≥16, outside its exceptions. The source theorem, order formula and simplicity are external inputs, not kernel verification.

## 2. Selection and proof

Choose r with ord_r(p)=nf. Then ord_r(q)=n and r≡1 mod nf, so r≥nf+1≥2n+1>n+1>7. In particular q^(n/2)≡−1 mod r: the order n is even, so the n/2 power is the unique element of order two in F_r^×. The factor q^(n/2)+1 therefore places r in |G|, and the denominator in the order formula is at most 4 and cannot cancel r.

For each prime k|f, p^(nf/(2k))≠−1 mod r, because squaring that congruence would imply p^(nf/k)=1, contrary to ord_r(p)=nf. This is stronger than β(n/2,−1), which requires the congruence only for the source's relevant **odd** primes k|f. The source applies to the chosen dimension family and gives one maximal overgroup M of R.

Because G is nonabelian simple and r>7, every proper subgroup index is at least 8: otherwise the core-free coset action injects G into S7, whose order is not divisible by r. Among three indices with pairwise gcd≤7 at most one is r-divisible. The other two subgroup representatives, after conjugation, contain R and lie in M. Their original indices both are divisible by [G:M]≥8, a contradiction. This uses actual group subgroups, not merely allowed integers.

## 3. Finite controls and review boundary

`frontier-20261028-minus-orthogonal-check.py`, SHA-256 `670dbd9e1e3e01815624284e8c2ddebedea584d95d13883499d5bc68d73ddb5f`, 39 LF / 1065 bytes, ran at 18:35:28 PDT on 2026-10-28. Exact integer arithmetic checked primality, orders and the stated congruences for six named examples with n=8,10,14,16 and f=2 or 3. The bounded control does not prove Zsigmondy, any maximal-subgroup classification, or the universal conclusion.

**Review-critical:** verify both exact Table B rows and Proposition 6.11, including the simple-group/field-characteristic scope, the β restriction to odd k, the projective order denominator, the n=8 and n=10 source exceptions, and the elementary common-index argument. No earlier historical holds are modified.
