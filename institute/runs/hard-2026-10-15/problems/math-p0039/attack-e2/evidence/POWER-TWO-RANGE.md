# Restricted exclusion for power-of-two orders

This is a sub-question only. No claim of novelty or of an all-orders solution
is made.

For every integer a with 3<a<59049, the special-prime difference-set
criterion cannot hold for n=2^a. Therefore, assuming the Kantor plus
Thas–Zagier geometric reduction, no non-Desarguesian flag-transitive projective
plane has order 2^a for such a. No conclusion about other orders follows.

The proof of POWER-TWO-LEMMA.md shows that prime p forces a=3^t. For a>3
the first such exponent is a=9. At a=9, p=262657 is prime but D is not planar:
the distinct ordered pairs (1,89785) and (4,89788) both have difference
172873 modulo p, and every displayed element satisfies x^513=1 modulo p.
See controls.json and the separate exact checker.

Every subsequent power of three below 59049 is covered by this proper-factor
table. The last column is r=2^a mod q, so r^2+r+1=0 mod q verifies divisibility
using small integers. Primality of q is unnecessary: 1<q<p is enough.

| a | proper factor q of 2^(2a)+2^a+1 | r=2^a mod q |
|---:|---:|---:|
| 27 | 2593 | 1455 |
| 81 | 487 | 254 |
| 243 | 80191 | 9101 |
| 729 | 39367 | 22066 |
| 2187 | 209953 | 12303 |
| 6561 | 141560137 | 52564303 |
| 19683 | 472393 | 266279 |


The exponent chain is gap-free: a=27,81,243,729,2187,6561,19683 are exactly
3^t for 3<=t<=9. All other exponents in 3<a<59049 were already excluded
algebraically by the proper-factor identity in POWER-TWO-LEMMA.md.

The first unhandled exceptional exponent here is a=59049 (t=10).
The bounded trial-progression search found no proper factor <=10^11 for its
p, but that is NOT primality and NOT infeasibility. No claim excluding this
case is made. For a hypothetical prime p at this or a later exceptional
exponent, all base-two/divisor-multiplier tests automatically pass. A different
argument or a difference collision would then be needed.

Reproduction: python3 code/check_family.py.
The independent check uses manual small-modulus exponentiation, does not import
the search code, and verifies the n=512 collision. A second direct full-integer
factor check is provided in claims.json. The corrupted-factor negative control
must fail.
