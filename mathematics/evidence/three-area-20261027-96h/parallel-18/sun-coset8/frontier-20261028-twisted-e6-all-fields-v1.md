# Sun8 for all finite simple twisted E6 groups

**NEW FAMILY CANDIDATE at NAMED EXTERNAL INPUTS — WRITTEN plus bounded exact polynomial checks; not yet independently reviewed/adopted/formally verified or novelty-cleared.** Actual native prewrite clock **Wed Oct 28 18:10:53 PDT 2026**. This is an exact all-fields subgroup/coset theorem at the stated external classification and primitive-prime statements, not a solution of unrestricted Sun8.

## 1. Exact theorem and named sources

`Sun_8(X)` means that every eight pairwise-disjoint ACTUAL LEFT cosets of finite-index subgroups of X have a pair of indices with gcd>=8.

**Theorem.** For EVERY prime p and integer f>=1, with q=p^f, the finite nonabelian simple group `^2E6(q)` satisfies Sun8, assuming the named finite-group statements below.

1. [Baumeister–Burness–Guralnick–Tong-Viet, arXiv:2307.13976v2](https://arxiv.org/html/2307.13976v2), Proposition7.7, Theorem2 and Table C, give the group order

       |^2E6(q)| = q^36 (q²−1)(q⁵+1)(q⁶−1)(q⁸−1)(q⁹+1)(q¹²−1)
                    / gcd(3,q+1),

   and identify the following precise UPPER/LOWER SCOPE: for r a primitive prime divisor of `q^18−1`, if `beta(9,−1)` and at least one of `f>1`, `r>19`, `|R|>r`, or `f=1` with p a nonsquare modulo5, then a Sylow r-subgroup R has a UNIQUE maximal overgroup of the named type. The source has another f=1 quadratic condition not needed here. I read the exact order, row, beta definition and Proposition7.7's relevant source discussion, but have NOT rederived their classification proofs. **NR-TWISTED-E6-ORDER/SIMPLICITY AND NR-UNIQUE-OVERGROUP-PROOFS** remain.
2. The source's beta(9,−1) means `(q^(1/k))^9 != −1 (mod r)` for every ODD prime k|f with k!=r. This is checked explicitly, not assumed from the phrase primitive.
3. The source §2.1 states Zsigmondy's theorem with its `(2,6)` and exponent2/Mersenne exceptions. It is used only for `p^(18f)−1` with f>=2, where neither exception applies. **NR-ZSIGMONDY-PROOF** remains.

The source's unique-overgroup theorem is a strong external classification input, not a new group classification proved here. No Sun7, NC7, P7 or old held exceptional-family candidate is an input.

## 2. The actual-coset caller

For any finite nonabelian simple G and prime r>7 dividing |G|, if a Sylow r-subgroup R has a UNIQUE maximal proper overgroup M, then Sun8(G).

In a putative counterconfiguration, at most one original subgroup index is divisible by r; otherwise a pair's gcd is at least r>7. Every other actual subgroup H has r-free index, hence contains a Sylow r-subgroup. Sylow conjugacy and uniqueness put H in a conjugate of M, so `[G:M]` divides its original index. At least seven such indices exist. Simplicity makes the action on G/M faithful; an index<=7 would embed G into S7, impossible because r>7 divides |G|. Hence `[G:M]>=8` and any two such original indices contradict the gcd bound. No coset-cover, normal H or common conjugate M is assumed. □

## 3. Every nonprime field: f>=2

By Zsigmondy choose r with `ord_r(p)=18f`. There is no exceptional pair for 18f>=36. Since 18f divides r−1,

    r>=18f+1>=37>19>7.

For q=p^f, `ord_r(q)=18`, so q^9≡−1 mod r and r divides q^9+1. The displayed projective-center denominator is at most3 and therefore does not remove r from the order.

For EVERY odd prime k dividing f,

    (q^(1/k))^9 = p^(9f/k) != −1 (mod r),

because squaring a contrary congruence would give order dividing18f/k<18f. Thus ALL beta(9,−1) source conditions hold, including those the source would omit when k=r. The f>1 and r>19 alternatives both apply. The cited classification gives a unique maximal Sylow r-overgroup, and Section2 proves Sun8(G). This pays the complete arbitrary-p, arbitrary-f>=2 range.

## 4. An exact degree-18 primitive-factor lemma for prime fields

For x>=2 set

    F(x)=x^6−x^3+1,       (x^3+1)F(x)=x^9+1.                   (4.1)

F(x) is odd for every integer x. Its 3-adic valuation is at most1. In fact, if x≡0 or1 (mod3), F(x)≡1 (mod3); if x≡−1 (mod3), the binomial expansion gives x³≡−1 (mod9), so F(x)≡3 (mod9).

If a prime r!=3 divides F(x), then `ord_r(x)=18`. Indeed r is odd and x is nonzero modulo r. Equation(4.1) gives x^9≡−1, so the order is one of2,6,18. Because r!=3, the derivative of X^9+1, `9 X^8`, is nonzero at x modulo r; the factor X³+1 and F(X) cannot share that root. If the order were2 or6, x³ would be−1 and the first factor would also vanish. Hence the order is18, and r≡1 (mod18), so r>=19.

For x>=3,

    F(x)=x³(x³−1)+1 >= 3³(3³−1)+1=703 > 3*19=57.         (4.2)

Thus for any prime p>=3, F(p) has either a prime divisor r>19 or a prime divisor r=19 with exponent at least2. Otherwise, with the only possible nonprimitive factor3 of exponent<=1, F(p) would be at most3*19=57, contrary to (4.2). Every prime r!=3 in F(p) has the required order18.

## 5. All prime fields, including the exceptional p=2

Let f=1. For p>=3, select r from Section4. It has `ord_r(p)=18`, so r divides p^9+1 and survives division by gcd(3,p+1)<=3 in the displayed ^2E6 order. If r>19, the source's r>19 alternative holds. If r=19 occurs to exponent>=2, then r² divides the group order and the actual Sylow r-subgroup has |R|>r, another source alternative. Beta is vacuous because f=1. Section2 proves Sun8.

For p=2, `F(2)=57=3*19`. The sole non-3 factor r=19 has order18 by Section4 and occurs to exponent1, so neither `r>19` nor `|R|>r` is claimed. Instead, the SOURCE'S DISTINCT f=1 alternative applies: 2 is a nonsquare modulo5 because the nonzero squares are1 and4. Beta is vacuous; the source row gives the unique Sylow19 overgroup, and Section2 applies. This explicitly treats `^2E6(2)` and does not delete the exceptional hypothesis.

Together with Section3, all q=p^f are covered. □

## 6. Bounded exact polynomial controls

Executed `/opt/homebrew/bin/python3 frontier-20261028-2e6-cyclotomic-check.py` under a10-second deadline. Source SHA256 `cb502c70d1c45572221dc72cae1b362b2d199de2e0fc2bf6cadfcaeaacd70ab6`. It multiplies integer coefficient arrays for (4.1), checks the parity/3-adic assertions on x=2,...,100, and trial-factors F(p) for p=2,3,5,7,11, with exact modular-order/source-alternative checks. Actual output:

```text
x9_plus_1_factorization: PASS
v2_zero_and_v3_at_most_one_x2_to_100: PASS
p=2, Phi18=57, factors=[(3, 1), (19, 1)], result=source quadratic-residue exception
p=3, Phi18=703, factors=[(19, 1), (37, 1)], result=source threshold (37, 1)
p=5, Phi18=15501, factors=[(3, 1), (5167, 1)], result=source threshold (5167, 1)
p=7, Phi18=117307, factors=[(117307, 1)], result=source threshold (117307, 1)
p=11, Phi18=1770231, factors=[(3, 1), (590077, 1)], result=source threshold (590077, 1)
PASS: bounded twisted-E6 primitive-source alternatives
Wed Oct 28 18:10:48 PDT 2026
```

These finite tests do not prove the all-integer 3-adic lemma, the full source classification, Zsigmondy or any actual subgroup existence. The relevant all-variable arithmetic is written in Sections3–5.

## 7. Prior scope and honest ceiling

The old final summary did not adopt a full twisted-E6 family gate; its later exceptional/unitary/E8 leads had separate unreviewed/held statuses. This is a fresh source-based proof CANDIDATE at explicit published statement imports, not an assertion that old held bodies or their selection/confidence guidance have been validated or erased. The repository/publication priority search is not exhaustive; no discovery/firstness claim.

If reviewed it excludes only the finite simple twisted-E6 family. It does NOT prove arbitrary-group Sun8, all finite simple P7 exclusions, the untwisted E6/E7 families or the source classification proofs. Parent and a disjoint reviewer must check the EXACT Table C row, the p=2 nonsquare alternative, every projective-center exception, primitive-factor reasoning and actual Sylow-to-coset caller before adoption. Human/kernel/independent-family and publication/priority remain unpaid.
