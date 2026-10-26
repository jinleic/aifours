# Addendum 1 — even a four-point B/D2 switch is impossible at every order

Owner MathShor / MathShor-2. Actual preceding `/bin/date`: `Sun Oct 25 14:23:18 PDT 2026`. WRITTEN CANDIDATE, unreviewed. This strengthens the first inequality of `proof-three-complement-small-trade-obstruction-v1.md` from4 to5. It does not change its two other inequalities or establish full noncompletion. No scientific computation.

## 1. Exact statement

Under the SAME common-complement hypotheses A,B,D2,D3, with all unknown elements and all admissible moduli retained,

    |D2 minus B| = |B minus D2| >= 5.

The prior literal collisions already force

    {1,7,13,14} subset B minus D2,
    {2,4,6} subset D2 minus B.

If the trade size were4, it would therefore have the EXACT form

    B minus D2 = {1,7,13,14},
    D2 minus B = {2,4,6,u},

for one arbitrary unknown residue u. No restriction on u or n beyond the common-complement hypotheses is imposed.

We will prove that such a trade would force A to be periodic modulo20, hence produce an impossible FACT pair at20.

## 2. Reduction to one unknown power of a root of unity

Both B and D2 complement A, so their signed difference is annihilated by convolution with1_A. At an nth root zeta where A(zeta) is nonzero, it gives

    zeta^u = Q(zeta),
    Q(z)=z+z^7+z^13+z^14-z^2-z^4-z^6.             (Q)

**Root lemma.** If zeta is a primitive dth root and Q(zeta)=zeta^u for ANY integer u, then

    d in {1,4,5}.                                  (RL)

The proof below is exact and uniform in u. It uses classical cyclotomic field degree/irreducibility and finite sums, not evaluated roots or a sampled conductor cutoff.

## 3. A residue-class fact for prime divisors of d

Let ell be prime dividing d, and group the terms of Q(zeta)-zeta^u by exponent modulo ell.

- If ell^2 divides d, the powers1,zeta,...,zeta^(ell-1) are linearly independent over Q(zeta^ell), since the field-extension degree is ell. Thus EACH grouped coefficient must vanish.
- If ell divides d only once, write zeta as a product of an ellth root and a root of order d/ell, adjusting their primitive generators. The only relation among the ell powers of the ellth root over Q(zeta^ell) is the all-ones relation. Therefore, if EVEN ONE exponent residue class is empty, all grouped coefficients must vanish (the nonzero scaling factors from the coprime component do not change this conclusion).

In either case, a group containing one sole term with coefficient+1 or-1 cannot vanish. An unknown exponent u can remove at most one such singleton obstruction.

These statements are standard consequences of phi(d)/phi(d/ell) and the irreducible cyclotomic polynomial for an ellth root over the coprime cyclotomic field. They are the named classical algebra inputs to RL.

## 4. No prime ell>=7 can divide d

The SEVEN known exponents of Q are1,2,4,6,7,13,14; signs are irrelevant for singleton counts.

- ell=7: the occupied known classes are0,1,2,4,6. Classes1,2,4 are singletons; classes3,5 are empty. Adding u leaves an empty class and at least two singletons.
- ell=11: classes are0..10, with known occupied classes1,2,3,4,6,7. Five of them are singletons. Adding u still leaves an empty class and multiple singletons.
- ell=13: six known occupied classes0,1,2,4,6,7; five singleton classes and multiple empty classes remain after adding u.
- ell>=17: the seven known exponents are distinct modulo ell. Even after adding u there is an empty class and at least six singleton classes.

The residue-class fact therefore rules out ell in EVERY case, including higher powers of these primes. All prime divisors of d lie in{2,3,5}.

## 5. High powers of5 or3 are impossible

### If25 divides d

Grouping modulo5 must give zero in every class. Known class3 contains only zeta^13, so u must be3 modulo5. Then class1 still contains exactly zeta-zeta^6, forcing zeta^5=1, contrary to25|d. Hence25 does not divide d.

### If9 divides d

Known class0 modulo3 contains only -zeta^6, so u must be0 modulo3. Class2 then remains zeta^14-zeta^2, forcing zeta^12=1. This contradicts9|d. Hence9 does not divide d.

## 6. If4 divides d, then d=4 exactly

Grouping by parity is linearly independent over Q(zeta^2).

If u is even, the odd group gives

    zeta+zeta^7+zeta^13=0,
    1+zeta^6+zeta^12=0.

Thus zeta^18=1, incompatible with4|d. So u is odd, and the even group must give

    zeta^14-zeta^2-zeta^4-zeta^6=0.

Put w=zeta^2. Then

    w^6=1+w+w^2.

Since |w|=1, the right side has modulus |1+2 Re(w)|. Its modulus must be1. Hence Re(w)=0 or Re(w)=-1, so w=i,-i or-1. The values i and-i fail the ORIGINAL equation (left side-1, right side respectively i or-i). The only possibility is w=-1. Therefore zeta has order4, as claimed.

Together, §§4–6 leave only

    d in {1,2,3,4,5,6,10,15,30}.

## 7. The remaining small conductors, by exact algebra

At d=1, Q(1)=1. At d=4, Q(i)=i. At d=5, reduction modulo z^5-1 gives Q(zeta)=zeta^3. These are compatible with RL.

The other orders are excluded:

- d=2: Q(-1)=-5, not a unit complex number.
- d=3: Q(zeta)=2zeta-1, whose squared modulus is7.
- d=6: Q(zeta)=4zeta-1, whose squared modulus is13.
- d=10: Q(zeta)=2zeta-2zeta^2+zeta^3. The ten possible powers are plus/minus1,zeta,zeta^2,zeta^3,zeta^4, and zeta^4=zeta^3-zeta^2+zeta-1. None has the coefficient vector(0,2,-2,1) in the linearly independent basis1,zeta,zeta^2,zeta^3.

### Exact conjugate-norm control for15 and30

For any integer polynomial R, set c_r^(m) to the sum of its coefficients at exponents congruent to r modulo m. Using

    c_15(k) = (3*1_(3|k)-1)(5*1_(5|k)-1),

where c_15 is the Ramanujan sum over the eight primitive15th roots, direct expansion gives

    sum_(t unit mod15) |R(zeta_15^t)|^2
      =15 sum_r (c_r^(15))^2
       -3 sum_r (c_r^(3))^2
       -5 sum_r (c_r^(5))^2 + R(1)^2.             (CN)

This identity is proved by expanding the squared modulus and summing each character; no arithmetic script or finite root evaluation is used.

For R=Q:
- Seven distinct exponent coefficients modulo15, so the first square-sum is7.
- Modulo3 the coefficient vector is(-1,2,0), square-sum5.
- Modulo5 it is(0,0,0,1,0), square-sum1.
- Q(1)=1.

Thus CN equals15*7-3*5-5*1+1=86, not8. If Q(zeta_15)=zeta_15^u, the integer polynomial identity at one primitive root would hold at every Galois conjugate, and the sum would be8. So d=15 is impossible.

For d=30 put w=-zeta, a primitive15th root, and use R(z)=Q(-z):
- Its first square-sum modulo15 is7.
- Modulo3 the vector is(-1,-4,0), square-sum17.
- Modulo5 it is(0,-2,-2,-1,0), square-sum9.
- R(1)=-5.

CN is15*7-3*17-5*9+25=34, not8. Again an equality R(w)=(-1)^u w^u would force all eight conjugate norms to be1. Hence d=30 is impossible.

This completes RL without any unbounded-conductor assumption or finite sampling of u.

## 8. Conclude the trade obstruction

By RL, every Fourier character where1_A has nonzero transform has order1,4 or5. Therefore

    1_A(x+20)=1_A(x) for every x in Z_n.

Here20|660|n, so this is an exact group period. Quotienting by its generated subgroup gives a direct cyclic factorization at20 containing all endpoint seeds, as in the periodic-descent proof. But the multiplier seed-bootstrap would require its start-factor cardinality to be at least330, a contradiction.

Thus a four-point B/D2 trade cannot exist, proving the bound>=5 at ALL orders.

## 9. Remaining gap and assurance

This eliminates the entire minimal-trade case with one arbitrary unknown positive location. A larger trade can have more unknown negative as well as positive locations; then the seven fixed exponents used in RL no longer exhaust its polynomial, and none of the conductor elimination above may be reused without a new proof.

The full common-complement existence question, actual PR saturation, and eventual finite raw STAB/GP completion remain open. No C-specific all-order contradiction for ALL trade sizes has been proved.

All identities and conductor cases above were checked in WRITING only. Classical cyclotomic extension/irreducibility, elementary complex geometry and finite Fourier inversion are explicit imports. No interpreter arithmetic, symbolic algebra program, enumeration, replay, solver, formal checker, external model or new GO occurred. No novelty or stronger acceptance is claimed.
