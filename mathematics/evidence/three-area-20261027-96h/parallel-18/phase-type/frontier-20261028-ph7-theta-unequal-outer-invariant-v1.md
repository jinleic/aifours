# An exact positive-cycle invariant for arbitrary unequal outer rates in the PH7 5/7-theta graph

**EXACT WRITTEN + SYMBOLIC/FRACTION IDENTITY CHECKED; independent peer review pending.** MathResearch96h-2. This is prospective work on the still-open unequal-outer-rate graph, not an 8/9 exclusion. The separately frozen equal-outer theorem remains unchanged.

## Claim

In the seven-state 5-/7-cycle theta graph, let the five common-vertex escape rates be arbitrary positive `u1,...,u5`, and the two outer escape rates be arbitrary positive `v1,v2` (they need not be equal). Define

    s=sum_i u_i,       t=v1+v2,       r=v1 v2,
    Delta=t²-4r=(v1-v2)² >=0.

If the actual characteristic polynomial contains the target factor `D_z(y)=y[(y+1)^2+z]^2`, the longer-cycle edge product is positive, and `z>4/5`, then NECESSARILY

    s>4.                                              (MAIN)

This holds in particular at 8/9 with fully unequal outer rates. It is one all-variable necessary inequality on ONE graph; it does not decide 8/9 or imply the outer rates must be equal.

## Derivation from the actual two-cycle determinant

Let `e_j` be the elementary symmetric functions of the five common rates, `e1=s`; write

    A(y)=y^5+s y^4+e2 y^3+e3 y^2+e4 y+e5,
    B_out(y)=y²+t y+r.

For the literal graph the only nontrivial determinant permutations are the two overlapping cycles, so

    P(y)=A(y) B_out(y)-D1 B_out(y)-D3,

with positive long-cycle product D3. If `D_z` divides P, the monic hidden quadratic Q has

    p=s+t-4,
    q=e2+t s+r-4p-(6+2z),      Q=y²+p y+q.

Writing `T_j=[y^j](D_z Q)`, y4/y3 coefficient matching gives

    e3=T4-t e2-r s,
    e4=T3-t e3-r e2.

After eliminating D1 with the y2 coefficient, the y1 equation is

    F=(r-t²)e4-t r e3-T1+t T2=0.                     (F)

The y0/y2 coefficients give

    D3/r = L=T2-t e4-r e3.                           (L)

The coefficient equation F is affine in e2; write `F=B-C e2` with B independent of e2. Thus if C!=0 it uniquely fixes `e2=B/C`. Define

    M=(r-t+1-z)²+z(t-2)².

Direct symbolic algebra establishes the exact all-variable identity

    L=(s-4) M²/C   after F=0.                         (ID)

No input/exit choice or numerical fit appears. The symbolic checker and independent rational interpolation replay below verify this identity for all variables.

## Why the denominator and M are strictly positive

Substitute `r=(t²-Delta)/4`. The exact identity for C is

    16 C = Delta²
         +2 Delta(5t²-16t+4z+12)
         +(t²-4t+4z+4)(5t²-12t+4z+4).               (SOS)

For z>4/5 all factors in(SOS) are strictly positive except the nonnegative powers of Delta:

    t²-4t+4z+4       =(t-2)²+4z >0,
    5t²-12t+4z+4     =5(t-6/5)²+4z-16/5 >0,
    5t²-16t+4z+12    =5(t-8/5)²+4z-4/5 >0.

Hence C>0 even for v1=v2. Further M>0: if M=0, z>0 forces t=2 and r=1+z, contradicting `Delta=t²-4r=-4z>=0`. Since r>0 and D3>0, L>0. (ID) then implies s>4, as claimed. □

## Exact scope for the next global attack on this graph

At the critical z=8/9, the entire still-open unequal-outer 5/7-theta graph reduces necessarily to three real aggregate variables `(s,t,r)` with

    s>4, t>0, 0<r<=t²/4, Delta>=0,
    e2=B/C>0, e3>0, e4>0, L=(s-4)M²/C>0.

All e2,e3,e4 are exact rational functions obtained from(F) and the preceding coefficient equations, with uniformly positive C. Five positive common rates additionally impose every ordinary Newton inequality and positivity of their 3-by3 moment Hankel Gram matrix. The short-cycle product is `D1=e5-L>0`, and the last Newton inequality gives the further strict necessary condition

    e4² > (5/2) e3 L.

These are all necessary, not claimed sufficient. Clearing positive C gives an explicit rational-polynomial feasibility problem in three variables. The equal-outer slice `Delta=0` has already been excluded separately by exact CAD plus degenerate resultants. No proof here resolves the full `Delta>0` slice, any other theta/figure-eight topology, or >=9-edge generators.

## Actual verification

Primary exact SymPy checker `frontier-20261028-ph7-theta-unequal-outer-invariant-check.py`, **29LF/1678B**, SHA256 `dedd31eb6482c00b15dc250d9f066016aadc2f6fcf7a0f65e3b259902409378f`, actually returned

    SymPy 1.14.0 exact all-variable unequal-outer theta identity and C sum-of-squares PASS

Certificate `frontier-20261028-ph7-theta-unequal-outer-invariant-certificate.json`, **14LF/504B**, SHA256 `95b523a3c3fa086b0fce9e8a979cfb82ef5bfb6274f79ce994fb71369b41adf7`.

A separately written standard-library-only replay `frontier-20261028-ph7-theta-unequal-outer-invariant-fraction-replay.py`, **33LF/1374B**, SHA256 `13b91b1cb92b196360d45e869dfaa72fb7791458b217fb5a25a1107e706842ea`, actually returned

    Independent stdlib Fraction PASS: 675 multivariate identity values and 45 SOS identity values, exact degree bounds

It reconstructs all target coefficients independently. The cleared(ID) polynomial has degrees at most `(2,8,4,4)` in `(s,t,r,z)`; equality at a full `3x9x5x5` exact rational grid establishes the identity, not an empirical check. The SOS identity has degrees at most `(4,2,2)` in `(t,Delta,z)`, covered by the exact `5x3x3` grid. This is an independent implementation, not peer/human/formal review.

No 8/9 witness, unrestricted exclusion, minimum8, new PH6 theorem, or historical process repair is asserted.

END — any 5/7-theta spectral candidate above4/5, with arbitrarily unequal positive outer rates, must have total common escape rate strictly above4.
