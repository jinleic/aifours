# An intrinsic limitation of the chosen necessary-condition tests

This elementary lemma is included to identify the remaining logical gap.
No novelty is claimed, and it is not used to skip production candidates.

**Lemma.** Let a≥1, n=2^a, and suppose p=n²+n+1 is prime. Then a=3^t
for an integer t≥0, the multiplicative order of 2 modulo p is exactly
3^(t+1), and 2^(n+1)=1 (mod p). In fact every positive divisor d of n
satisfies d^(n+1)=1 (mod p).

**Proof.** If a has a prime divisor l other than 3, write a=lc and y=2^c.
In the polynomial quotient Z[X]/(X²+X+1), we have X³=1. Since l=1 or
2 (mod 3), X^(2l)+X^l+1=0 in that quotient. Consequently

    1 < y²+y+1 < y^(2l)+y^l+1 = p

and y²+y+1 divides p, a contradiction. Thus a=3^t.

The identity (n−1)p=n³−1 gives 2^(3a)=1 (mod p). On the other hand,
2^a=n lies strictly between 1 and p, so 2^a is not 1 modulo p. The order
of 2 divides 3a=3^(t+1) but does not divide a=3^t. These are consecutive
powers of 3, hence the order is exactly 3^(t+1).

Set A_t=2^(3^t)+1=n+1. We have 3|A_0. The factorization

    A_(t+1) = A_t · (2^(2·3^t) − 2^(3^t) + 1)

and 2^(3^t)=−1 (mod 3) show that the second factor is divisible by 3.
Induction gives 3^(t+1)|A_t. Therefore the order of 2 divides n+1,
so 2^(n+1)=1 (mod p). Every positive divisor of n is 2^j, and raising
that congruence to j gives the last assertion. QED.

Thus a base-two test, followed only by valid divisor-multiplier tests, cannot
exclude a hypothetical prime p of this form. We do NOT assert that such primes
exist for infinitely many t. A prime in this family is NOT automatically
special: n=512 gives p=262657, passes all these tests, and its D is NOT planar,
as verified by the explicit difference collision in controls.json. This is
also why Feit's invalid general exclusion of powers of two cannot be silently
used to fill the remaining gap.

## Stronger limitation: an infinite family of filter survivors

The second part of the proof does not require p prime. For ANY t>=0, set
a=3^t, n=2^a and p=n²+n+1. The number p is odd, so 2 is a unit modulo p.
Its order divides 3a but not a (because 1<2^a<p); hence its order modulo p
is exactly 3a. The same induction above gives 3a|(n+1). Thus all these
integer n pass the base-two and every divisor-multiplier congruence even
when their p is composite. The composite n=2^27 control is one example.

Every prime factor q of p satisfies q=1 (mod 6a). To prove this, first q is
odd and q!=3, since p=1 (mod 3). The order of 2 modulo q divides 3a. If it
divided a, then n=1 (mod q) and p=3 (mod q), forcing q=3, impossible.
Because 3a is a power of three, the order is therefore exactly 3a.
Lagrange's theorem gives 3a|(q-1), and the oddness of 3a together with even
q-1 gives 6a|(q-1). In particular q>=6a+1. Products of such prime factors
are also 1 modulo 6a, justifying the trial progression used for the factor
searches in power_two.py.

For ANY FIXED sieve bound B, all t large enough that 6·3^t+1>B therefore
give n=8 (mod 24), n>8, with no proper prime divisor of p at most B, while
all base-two/divisor congruences still pass. For B=1000000 this holds for
t>=11. The finite-sieve-plus-necessary-power-test strategy thus has infinitely
many integer survivors beyond its current range. There is NO assertion that
any of their p are prime, that D is planar, or that counterexample planes
exist. Exact factors above B or further mathematical conditions can still
eliminate them. The point is the limitation of the fixed filtering strategy.
