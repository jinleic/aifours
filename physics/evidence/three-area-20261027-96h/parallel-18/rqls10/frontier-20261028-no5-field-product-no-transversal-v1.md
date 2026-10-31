# A three-cell field obstruction for Fourier-product QLS10

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 20:56:53 PDT 2026**. This gives a simple independent exclusion for the formerly open entire q18 family and for every other q not divisible by5. It strengthens the alphabet frontier, but does NOT address arbitrary nonproduct QLS10.

## 1. Theorem

Let F be a conjugation-stable subfield of C over which `Phi5(x)=1+x+x²+x³+x⁴` is irreducible. Let K be ANY 10×10 complex Hadamard with entries in F. In the actual Fourier-product QLS

`psi_(r,c)(t)=zeta10^(r t) K_(t,c)/sqrt(10)`,

no three pairwise orthogonal cells can occupy three distinct physical rows of the SAME parity and three distinct columns. In particular there is NO orthogonal transversal, even if rays repeat.

For every positive q with **5∤q**, the cyclotomic fields Q(zeta_q) and Q(zeta5) are linearly disjoint because their conductors are coprime; so Phi5 is irreducible over Q(zeta_q). Therefore the theorem excludes the FULL BH(10,q) Fourier-product family for all such q, including q=6,12,18,24,36,42, etc. This corollary uses the standard cyclotomic disjointness theorem; no root-sum classification, Butson catalog or finite computation is a premise.

## 2. Proof

Take distinct columns c,d assigned to physical rows r,s of the same parity. Put `Delta=s-r mod10`; Delta is a nonzero even residue, and `k=Delta/2 mod5` is nonzero. For each coordinate t define the unit complex number

`z_t = conj(K_(t,c)) K_(t,d) ∈ F`.

K column orthogonality gives `sum_(t=0)^9 z_t=0`. Pairing coordinate positions u and u+5, u=0,...,4, define `w_u=z_u+z_(u+5)∈F`. Thus `sum_u w_u=0`. Orthogonality of the two physical cells gives

`sum_(u=0)^4 zeta5^(k u) w_u = 0`.

Because Phi5 is irreducible over F and k≠0 mod5, the five powers zeta5^(k u) have only the scalar relation with all coefficients equal. Consequently all five w_u are equal; their sum is zero, so **every w_u=0**:

`z_(u+5)=-z_u` for each u.                                               (1)

Write `h_c(u)=K_(u+5,c)/K_(u,c)`, which is well-defined and nonzero. Equation (1) is equivalent to

`h_d(u) = -h_c(u)` for each u.                                            (2)

Now select any THREE pairwise orthogonal cells in three distinct same-parity physical rows and distinct columns c1,c2,c3. Applying (2) to c1,c2 and to c1,c3 gives `h_c2(u)=h_c3(u)`. Applying it to c2,c3 gives `h_c3(u)=-h_c2(u)`, a contradiction because h_c2(u) is nonzero. Any transversal contains five cells in same-parity rows, so no transversal exists.

## 3. Independent finite corroboration and limits

A separate full, dephased q18 Z3 encoding `frontier-20261028-bh18-transversal-smt-v1.py` SHA **748c1184070a59c62af60eaf2cebaf33cd13a81a0c134983669481320daf6a7e** includes all BH10,18 column equations and all identity-normalized transversal equations in exact Phi18/Phi5 integer bases; 1479 assertions, Z3 4.15.4, bounded 120 s. Its actual result `frontier-20261028-bh18-transversal-smt-v1.json` SHA **9e1bbf221e861dd16dc0ead4cc12f43d9347f7936fa2e0e7f3be2810c14d781f** reports UNSAT in 17.825897 solver seconds on 2026-10-28 20:55 PDT. This is solver-scoped corroboration, not an independently checked proof certificate; the theorem's written proof does not depend on it.

Combining this field theorem with the all-odd and all-no3 Fourier-product results, any root order not yet excluded must be divisible by **30**. The first remaining order is30. Those other source/certificate imports still need their own review. The field theorem does not apply when Phi5 is reducible over F, including Q(zeta_q) when 5|q; nor does it settle continuous/general Hadamards, non-Fourier products, or arbitrary 1-RQLS10. Independent written review of the field argument and physical caller is required.
