# Shor completion: only Q55 can remain for odd tails over a 165 cofactor

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 22:16:12 PDT 2026**. **UNREVIEWED WRITTEN candidate with an explicit classical T2 import.** No finite search, formal proof, independent-family review, human acceptance or novelty claim is made.

## 1. Exact statement and scope

For every integer `t>=1`, put `n=165*2^t`. If

    P direct-sum Q = Z_n,
    {0,3,8,11} subset P,  {0,1,7,13,14} subset Q,
    |Q| odd,

then necessarily `|Q|=55` and `|P|=3*2^t`. No such tiling or code is claimed to exist. This is a direct cyclic-tiling statement and applies to SAME-code actual multi-b borders of a hypothetical finite UD factor-complete extension of the literal Shor code. It does not address even Q, other orders, or unrestricted completion.

The result **does not use** the separate universal Q55 exclusion, the odd-55 cofactor classification, their pending reviews, or the n2640 even-tail packet. If this candidate and the separately unreviewed Q55 exclusion both survive scientific review, their combination would exclude odd Q in this family. Until then Q55 remains explicitly OPEN and no adoption is asserted.

## 2. Classical inputs and transversals

The actual border factorization is Restivo–Salemi–Sportelli as stated in Cordero, [arXiv:2301.13566v1, p. 3, Theorem 1.1](https://arxiv.org/pdf/2301.13566v1); it concerns actual `a^i b^+` and `b^+ a^j` atoms. Sands divisor exclusion appears in Łaba–Londner, [arXiv:2106.14042v3, p. 10, Theorem 2.5](https://arxiv.org/pdf/2106.14042v3): P and Q cannot use the same nonzero difference gcd. Here Q uses gcds 1,2,6, via old tail pairs `(1,0)`, `(14,0)`, `(7,1)` respectively; P uses gcds 3 and11, via `(3,0)` and `(11,0)`.

We invoke Łaba–Londner, [arXiv:2106.14042v3, p. 26, Corollary 6.2](https://arxiv.org/pdf/2106.14042v3): in a cyclic tiling, if at most two primes divide both factor cardinalities, both masks satisfy the Coven–Meyerowitz T2 condition. Here `|Q|` is odd, n has odd prime factors 3,5,11 each to the first power, so the two cardinalities are actually coprime and the hypothesis applies.

The tiling root identity makes each prime-power cyclotomic divide the side whose cardinality contains that prime. T2 supplies the cyclotomic for every product of its owned pairwise distinct prime powers. Therefore each factor's mask, reduced modulo its own cardinality, is the all-ones polynomial: **P and Q are transversals modulo their respective sizes**. In particular, if P owns primes p and q then it is uniform modulo pq. These are necessary consequences of the stated theorem, not general properties of arbitrary tilings.

Since odd `|Q|` divides 165 and Q contains the five distinct old tails, the complete cardinality list is

    |Q| in {5,11,15,33,55,165}.                                (1)

We exclude all entries except55 by the written arguments below.

## 3. Q5 and Q11: missing joint-prime head classes

For `|Q|=5`, P owns 3 and11 and is uniform modulo33. It would have a head `x=1 mod33`. If x is odd, compare it with even old heads0 and8; if x is even, compare it with odd old heads3 and11. In either case both differences are odd and divisible by neither3 nor11. Because gcd1 is a Q-difference, each must be divisible by5, but the two compared old heads have different mod-5 residues: respectively `(0,3)` or `(3,1)`. Contradiction.

For `|Q|=11`, P owns 3 and5 and is uniform modulo15. It would have a head `x=4 mod15`. The same opposite-parity old-head comparison shows both odd differences divisible by neither3 nor5, so each must be divisible by11 to avoid gcd1. The corresponding old-head residues modulo11 are respectively `(0,8)` or `(3,0)`, different. Contradiction.

## 4. Q15 and Q33: missing actual head transversals

Let `m=2^t`. In both branches P is a transversal modulo its actual size. Select a head x in class 1 modulo that size. It is odd. For `t>=2`, x is 1 mod4; for `t=1`, the two-adic valuation of n is only1. In either case its even difference from old head3 or11 has gcd two-adic valuation exactly1.

**Q15.** P has size `11m`, so x is 1 modulo11 and modulo m. Against old even heads0 and8, neither odd difference is divisible by11. To avoid gcd1, each must be divisible by3 or5. As 0 and8 are distinct modulo both primes, exactly two `(x mod3,x mod5)` possibilities remain: `(0,3)` and `(2,0)`.

* For `(0,3)`, `x-11` is even and divisible by none of 3,5,11, so its gcd with n is2.
* For `(2,0)`, `x-3` is even and divisible by none of 3,5,11, so its gcd with n is2.

Both contradict old Q-difference gcd2.

**Q33.** P has size `5m`, so x is 1 modulo5 and modulo m. Against old even heads0 and8, neither odd difference is divisible by5. To avoid gcd1, the only `(x mod3,x mod11)` possibilities are `(0,8)` and `(2,0)`.

* For `(0,8)`, `x-3` has two-adic valuation1 in the gcd, is divisible by3, and is divisible by neither5 nor11. Its gcd is6.
* For `(2,0)`, `x-3` has two-adic valuation1 in the gcd and is divisible by none of 3,5,11. Its gcd is2.

Both contradict old Q-difference gcds 6 and2. The parity and modular arguments cover `t=1` as well as all larger t.

## 5. Q165: a missing tail-transversal class

For `|Q|=165`, Q is a transversal modulo165 and therefore contains a tail `x=2 mod165`. If x is even, `x-13` is odd, divisible by11 and by neither3 nor5, so `gcd(x-13,n)=11`. If x is odd, `x-14` is odd, divisible by3 and by neither5 nor11, so `gcd(x-14,n)=3`. Both conflict with the old P-difference gcds 11 and3. Thus the required tail class is absent and Q165 is impossible for every t.

Equations (1) and §§3–5 leave only Q55, as claimed. The proof does not use any computational result or assumption that a larger completion exists.

## 6. Review boundary

A disjoint reviewer should reconstruct the actual-word border premise, verify the coprime-cardinality hypothesis and exact Łaba–Londner Corollary 6.2, the transversal derivation, every specialization of the two head-class cases, and the pure-tail class2 argument. In particular, no pending Q55 result is a premise. The result remains an unreviewed conditional mathematical candidate; Q55, all even-Q branches, and the original finite UD factor-completion problem remain OPEN.

**END OF 165-FAMILY ODD-TAIL ONLY-55 CANDIDATE.**
