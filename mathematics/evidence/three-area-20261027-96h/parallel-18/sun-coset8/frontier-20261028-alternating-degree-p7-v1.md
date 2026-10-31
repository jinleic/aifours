# A P7-specific degree criterion using small residual factors

**Status: WRITTEN candidate conditional on the named Dusart/Jordan sources and the earlier degree-only proof; not independently reviewed, formally verified or accepted.** Let n≥500,000 and define the explicit integers L(n), T(n), Q(n) exactly as in `frontier-20261028-alternating-degree-criterion-v1.md`, SHA `c823766a1bd3fe17ed3f4225e20c5db8b93f30489f378620d15533aa21dd7ceb`:
\[L=\max\{\ell\ge1:2\cdot11^\ell<4^\ell(n-4)\},\quad
 T=4+\left\lceil\frac{n-4}{25L^2}\right\rceil,\quad
 Q=\frac n{\gcd(n,\operatorname{lcm}(1,\ldots,T))}.\]
If Q does **not** divide 7, then A_n has no three proper subgroup indices with pairwise gcd exactly 7, and in particular excludes direct P7. Since 7 is prime this means Q∉{1,7}; it strictly includes cases with Q=2,3,4,5 or 6 which the earlier Q>7 theorem did not cover. No conclusion is claimed for Q=1 or 7, arbitrary alternating degrees, or the global target.

The result is specific to a common gcd of 7. It does **not** say that three indices with arbitrary gcd≤7 are impossible when Q≤7, and does not by itself prove unrestricted Sun8 in those small-Q cases. If the separate internally accepted written Sun7 and prior R8 interfaces are imported, they imply that a hypothetical eight-coset Sun8 counterexample has all index gcds 7, which this direct-P7 result excludes. That Sun8 composition is explicitly conditional, not a retroactive acceptance of either source.

## 1. Inputs, source order and nonclaims

The cited degree-only packet obtains a prime r with t=n−r satisfying 3≤t<T<n/2 from Dusart Proposition 6.8, https://arxiv.org/html/1002.0442v1, and uses Jordan's prime-cycle theorem, https://arxiv.org/html/1209.5169v1 Theorem 1.1, to prove every r-free proper subgroup is intransitive. Its explicit real-x and integer-L inequalities, public source proofs and subgroup reduction remain unreviewed inputs. No A_r unique-overgroup theorem is used.

For the optional small-Q Sun8 implication only, import the literal written Sun7 parent verdict SHA `94abd506aec9879e294a5eb84129794af0c7ac78917b091d2f2c113d665c34f2`, the old R8 source SHA `fa0497ae15bd3c765e05123996e4a94bd8038f2be1488b08dc7111f2fd7602c6` and their mandatory overlays. These are prior written interfaces, not new proof credit, formal/human/priority verification or a global verdict.

Read `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json`, SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`, before any referenced earlier alternating source body. Jordan/Dusart are prospective inputs, not retroactive modifications to f116, held history or earlier integer models. Writer exposure was nonblind; the incidental cross-topic display is recorded in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json`, SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`; no such excerpt is used.

## 2. The strengthened exact-gcd deduction

By the earlier written Jordan/Dusart reduction, every r-free proper-subgroup index is divisible by Q. In a three-index pattern with every pair gcd exactly 7, every index is divisible by 7, and at most one is divisible by r>7. Two indices are therefore r-free and each is divisible by lcm(7,Q). If Q∤7, this lcm exceeds 7, contradiction.

When Q>7 the earlier packet gives the stronger no-three-indices-with-pairwise-gcd≤7 result and Sun8 without an S7/R8 import. When Q∈{2,3,4,5,6}, the argument here proves only the stated gcd-exactly-7 subgroup exclusion; Sun8 then requires the additional old S7/R8 interface as disclosed. This is an actual subgroup inference, not a numerical divisor-only test.

## 3. Concrete strict extension and control

For n=2,143,232=2^10·7·13·23, exact integer arithmetic gives L=13, T=512, Q=2. Hence lcm(7,Q)=14>7 and the new direct-P7 criterion applies although the prior Q>7 condition does not. The value Q=2 is not a claim that any subgroup index equals 2.

`frontier-20261028-alternating-degree-p7-check.py`, SHA-256 `58d3768b6078e7cbe234aa0ad4fb3ba9b782e44e65df1ccb6fd2b4e6a4fed18a`, 30 LF / 805 bytes, ran at 20:11:38 PDT on 2026-10-28. It checked the factorization, exact L/T/Q and one selected prime r and binomial range. This finite test does not verify the source theorems, arbitrary subgroup reduction, optional Sun7/R8 proof DAG or a novelty claim.

**Review-critical:** verify Q divides every relevant r-free subgroup index, the distinction Q∤7 versus Q>7, lcm(7,Q), and the optional Sun8 import/identity. No old hold, source proof, formal or independent acceptance is changed.
