# f65 — all-fields PSU(3,q) actual-coset theorem

Reviewer **PhysicsPPT44-2**. Actual native clock observed immediately before creation: **Wed Oct 28 18:02:18 PDT 2026**.

**Verdict: NO_SUBSTANTIVE_DEFECT AT EXACT STATED IMPORTS AND SCOPES — 0 FATAL / 0 MAJOR / 0 MINOR.** The argument proves Sun8 for every `PSU(3,q)`, q≥3 a prime power, **conditional on the cited exact order/simplicity, unique-Sylow-maximal-overgroup and primitive-prime statements**. It imports no Sun7. The original proofs and transitive ancestry of those group-theory/number-theory inputs are not independently reconstructed here. This is same-harness written/source review plus bounded exact checks, not formal/kernel, human, configured-family, novelty, priority or unrestricted Sun8 acceptance.

## 1. Bound candidate and actual source reads

- Complete assignment `f65-psu3-all-fields/assignment-v1.json`: SHA256 `e8c09e419fcd8ef5965f2d395d3ca3eb5edfe7f0b79eb554d18d8eec4eb4d44b`.
- Complete 145-LF candidate `frontier-20261028-psu3-all-fields-v1.md`: SHA256 `c32a27c4e2c71cf76e3b129d37513dba9680da34cf4186a35d1d70126b7b8e7b`.
- [Baumeister–Burness–Guralnick–Tong-Viet, arXiv:2307.13976v2](https://arxiv.org/html/2307.13976v2): Theorem 2, §2.1 primitive-prime statement, Proposition 6.3, Table B and Remarks 9.2(a)–(c).
- [Korchmáros et al., arXiv:1902.10201v1](https://arxiv.org/html/1902.10201v1), §3 at its actual PSU(3,q) order/simplicity statement.

I have prior Sun-coset familiarity and reviewed other transfer/family candidates; this is not blind, clean-cognition or independent-model-family review. No author contact, held mathematical payload, nested agent, author checker or historical output is used as a theorem premise. The source statements are imports at the exact sites below; I did not verify the maximal-subgroup classification proof, the source's Magma small-group computations, Zsigmondy's original proof, unitary simplicity/order proofs or their complete citation ancestry.

## 2. Exact source interface and its small exceptions

The order/simplicity source states that for q≥3, `G=PSU(3,q)` is simple and

`|G|=q³(q³+1)(q²−1)/gcd(3,q+1)`.

For the maximal-overgroup source, Theorem 2 concerns an almost simple G with socle T and a Sylow r-subgroup, **r odd**, under the assumption G/T is an r-group. Here the candidate takes G=T, so the quotient is trivial and satisfies that assumption. Table B's `U₃(q)` rows include:

1. defining-characteristic **odd** r=p with maximal overgroup P₁;
2. the primitive r₆ case with overgroup `GU₁(q³)`, under `β(3,−1)` and either f>1 or, when f=1, `|R|>r` or `r>7`;
3. the special `(q,r)=(3,7)` row with `L₂(7)`.

The candidate uses only the first and second rows and keeps r>7 for its coset criterion. It handles q=3 separately and does **not** apply the r>7 criterion to the exceptional `(3,7)` row.

Remark 9.2(a) excludes the **alternative presentation** `G₂(2)'` because it is isomorphic to U₃(3); it does not say U₃(3) is excluded from its retained unitary notation. Remark 9.2(b) defines `β(3,−1)` by `(q^(1/k))³≠−1 (mod r)` for every **odd prime** k dividing f other than r. Remark 9.2(c) identifies P₁ as a totally singular one-space stabilizer. These are the source's conditions, not a stronger unqualified unique-overgroup assertion.

The source's Proposition 6.3 explicitly says q∈{3,4,5} are handled using Magma before its displayed q≥7 argument. In particular, applying Table B to q=4 is an application of the **source theorem/table including its small-case treatment**, not an independent reconstruction of that computation. For q=4=p², the exact control r=13 has `ord₁₃(2)=12` and `ord₁₃(4)=6`; f>1 and β is vacuous because f has no odd prime divisor. No excluded `L₃(4)` exceptional-presentation row is substituted for `U₃(4)`.

## 3. Unique-Sylow-overgroup actual-coset lemma

Let r>7 divide |G|, and suppose a fixed Sylow r-subgroup R has one maximal proper overgroup M, of index d≥8. Suppose eight actual disjoint left cosets have all pairwise original-index gcds≤7. At most one index is divisible by r, so at least seven subgroup indices are r-free. Each such proper subgroup H has the full r-part of |G| and hence contains a Sylow r-subgroup of G. Sylow conjugacy moves it to R; a maximal proper overgroup of the conjugated H contains R and must be M. Therefore d divides the original `[G:H]`, even though different H may lie in different conjugates of M. At least two r-free indices share d≥8, contradiction.

A subgroup equal to G cannot occur among eight nonempty disjoint cosets. This pays the proper-overgroup condition. No covering, normality, common-conjugate assumption, P7 reduction or Sun7 is used.

## 4. Uniform proper-index bound

A proper subgroup H of a finite nonabelian simple G has trivial core. The action on its actual left-coset space is therefore faithful, giving `|G|≤d!` for `d=[G:H]`.

At q=3 the imported formula gives `|G|=6048>7!=5040`. For q≥4, `gcd(3,q+1)≤3`, so monotonicity of the positive factors gives

`|G|≥4³(4³+1)(4²−1)/3=20800>5040`.

Thus every proper subgroup, and in particular every cited unique maximal overgroup, has d≥8. At q=4 the exact order is 62400; 20800 is only the uniform lower bound. The simplicity and order statements are the named external inputs, not consequences of a bounded calculation.

## 5. All extension degrees f≥2 and the q=7 prime field

Write q=p^f with p prime and f≥2. Apply the source-stated Zsigmondy theorem to p and d=6f≥12. Neither the `(2,6)` exception nor the d=2 Mersenne exception applies. A primitive divisor r has `ord_r(p)=6f`; Fermat gives `r≡1 (mod 6f)`, hence r≥13>7 and r is odd. Since

`ord_r(p^f)=6f/gcd(6f,f)=6`,

q³ has order 2 modulo r and is −1. Thus r divides q³+1 and survives the denominator `gcd(3,q+1)≤3`, so r divides |G|.

For every odd prime k|f, if `p^(3f/k)≡−1 (mod r)` then squaring gives `p^(6f/k)≡1 (mod r)` at a positive exponent strictly below 6f, contradicting primitivity. This verifies **all** odd-prime tests, including any test the source would omit, and hence β(3,−1). The Table B alternative f>1 holds; the source supplies the unique maximal overgroup and §4 pays d≥8. The actual-coset lemma in §3 proves Sun8(G), uniformly for all f≥2 and all characteristics, including q=4.

For prime fields p≥11, r=p is odd and >7; the defining-characteristic P₁ row applies with G=T, and §§3–4 finish. For p=7, r=43 is prime, `7³≡−1 (mod 43)`, and 7,7² are not 1 modulo 43, so the order is 6. The β condition is vacuous for f=1 and Table B's r>7 alternative holds. This is distinct from and does not use the `(q,r)=(3,7)` exceptional row. Thus only q=3,5 need the elementary support argument.

## 6. Written small-field support proof, all cases

The imported order formula gives

`|PSU(3,3)|=6048=2⁵·3³·7`,
`|PSU(3,5)|=126000=2⁴·3²·5³·7`.

Both have no proper subgroup of index 2,…,7 by §4. More generally, suppose a finite group has prime divisors contained in {2,3,5,7}, 7-adic order at most 1, and no proper subgroup of index 2,…,7. If eight actual disjoint cosets formed a counterconfiguration, all their indices would divide |G|, be at least 8, and have pair gcd in [2,7]. The lower bound is the elementary coprime-index actual-coset fact: the diagonal injection into the two coset spaces has domain index divisible by and at most the product of coprime indices, hence is onto.

For every seven-divisible index write n_i=7r_i. Pair gcd≤7 makes the r_i pairwise coprime. An index 7 is absent, so every r_i>1; the group order has only one factor of 7, so each r_i is seven-free and contains a prime from {2,3,5}. Distinct r_i cannot share one, giving at most **three** seven-divisible indices.

For seven-free indices, each is a divisor composed only of 2,3,5, is ≥8, and has pair gcd in [2,7]. If its support is exactly {2,3}, it is divisible by 12 or 18: otherwise the exponents would both be one, giving 6. At most two such indices are possible, since two divisible by 12 or two divisible by 18 would have gcd≥8.

The remaining cases are exhaustive:

- With a pure 2-power present, every index is even. At most one is a pure 2-power, at most two have support exactly {2,3}, and at most one contains both 2 and 5; total≤4.
- With a pure 3-power present, every index is divisible by 3. At most one is pure 3-power, at most two have support exactly {2,3}, and at most one contains both 3 and 5; total≤4.
- With a pure 5-power present, every index is divisible by 5. At most one is pure 5-power, at most one is even and at most one is divisible by 3; total≤3, even if categories overlap.
- With no singleton support, the possible supports are {2,3}, {2,5}, {3,5}, {2,3,5}. The first contributes at most two. Each of {2,5} and {3,5} contributes at most one; a triple-support index cannot coexist with either and at most one triple-support index exists. Thus all 5-containing supports contribute at most two, for total≤4.

In the first two bullets, two pure powers would share at least 8 or 9; in the third they share at least 25. Shared 2·5 or 3·5 already exceeds 7. These pigeonhole statements allow all exponents, including an index divisible by both 12 and 18, and do not assume distinct support labels. At most three seven-divisible plus four seven-free labels gives at most seven, contradicting eight. This pays q=3,5 without Sun7 or any executable search.

## 7. Independent exact checks and fault controls

I wrote `frontier-20261028-review-f65-psu3-arithmetic.py`, SHA256 `a9c6da506ed223f0deec0977711bf91b304ddeecd5449cdc3297e024c3ead214`, and ran

`PYTHONDONTWRITEBYTECODE=1 /usr/bin/env python3 frontier-20261028-review-f65-psu3-arithmetic.py`.

The program independently enumerates divisors of the stated q=3,5 orders and searches the exact integer compatibility graph, with an edge iff gcd∈[2,7]. Repeated index values need not be separately represented because any repeated index is ≥8 and would itself give gcd≥8. Actual output:

```text
q=3: order 6048, 42 divisor vertices, maximum clique 4,
     one clique [8,12,14,18], search_nodes=246.
q=5: order 126000, 113 divisor vertices, maximum clique 5,
     one clique [8,10,12,14,18], search_nodes=3959.
```

This graph allows many numbers that need not occur as actual subgroup indices and does not construct cosets. A no-eight-clique result is a finite overapproximation check; the written all-support proof above establishes the more general lemma.

The same independently written script trial-divides candidate primes and computes multiplicative orders and β directly for p∈{2,3,5,7}, f∈{2,3,4}; all 12 bounded controls returned a primitive r with the asserted orders, β and group-order divisibility. In particular q=4 returned r=13. The q=7/r=43 control has order 6. A separate direct integer calculation in the same script gave `Φ₃₆(7)=7¹²−7⁶+1=13841169553`, trial-division primality true, order 36 and β true. These are bounded checks, not Zsigmondy or classification proofs.

Two deliberate arithmetic fault controls show why the small-spectrum hypotheses matter: `[7,14,21,35]` has four seven-divisible indices with all pair gcds 7 if index 7 is allowed; `[49,14,21,35]` has the same property when a second factor of 7 is permitted. Neither tuple is asserted to be a realizable disjoint-coset family or an eight-label counterexample.

My first checker execution failed with `NameError: prod is not defined`; I added the missing standard-library import and reran. I also changed the first version's displayed order fields to compute the orders directly rather than print values inferred from its tests. The final hash and only the final observed results are given above; neither earlier execution is represented as a pass.

## 8. Exact disposition and limits

| Claim | Disposition |
| --- | --- |
| Unique-Sylow r>7 actual-coset caller | NO_SUBSTANTIVE_DEFECT; unique maximal overgroup, r|G and d≥8 are explicit |
| Proper-index bound and q≥3 simplicity/order interface | NO_SUBSTANTIVE_DEFECT conditional on the cited unitary order/simplicity statements |
| f≥2 primitive r and β, q=4 included | NO_SUBSTANTIVE_DEFECT conditional on Zsigmondy and the exact Table B theorem; q=4 source small-case computation remains imported |
| Prime fields p≥7, including p=7/r=43 | NO_SUBSTANTIVE_DEFECT at the cited defining-characteristic and r₆ rows |
| q=3 and q=5 all-support cases | NO_SUBSTANTIVE_DEFECT with the stated finite-order/index facts; no Sun7 import |

No exact-group counterexample or gap in these conditional implications was found. The f=1/q=3,r=7 exception, source's q=3/4/5 Magma handling, G=T condition, β quantifier and Zsigmondy exceptions have not been dropped. No arbitrary-group Sun8, all-simple classification, source-priority or novelty claim follows. Parent must read the operative source and review bodies before adopting; historical quarantine findings remain historical and are not retrospectively certified.
