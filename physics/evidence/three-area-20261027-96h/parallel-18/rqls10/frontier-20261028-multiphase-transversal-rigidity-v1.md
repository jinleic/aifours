# Multi-parameter rigidity and a genuine two-phase maximal QLS(10)

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED; the explicit sample is independently exact-checked.** Native `/bin/date` at sample check: **Wed Oct 28 19:57:07 PDT 2026**. This generalizes the one-parameter argument `frontier-20261028-binary-lift-transversal-rigidity-v1.md` SHA **ba643286afd36efb48a57aceac82c7762860bf3058bc3b25198e329717a0aaef**. Neither its generic conclusion nor the sample settles general 1-RQLS10.

## 1. Generic multi-parameter theorem

Let H be an n×n unit-phase matrix over a field F containing zeta_n, and assume its Fourier-product array at parameter one has NO transversal. For any finite set of integer masks `R^(1),...,R^(m)`, define

`K_(t,c)(z)=H_(t,c)*product_j z_j^R^(j)_(t,c)`,  `|z_j|=1`.

For each fixed candidate transversal T, some pairwise inner product is nonzero at `(1,...,1)`, hence is a nonzero Laurent polynomial over F in z. Its zero set on the m-torus has Haar measure zero: induct on m, using that a nonzero one-variable polynomial has finitely many roots except on the lower-dimensional coefficient-zero set. Taking the finite union over at most n! transversals proves that **almost every parameter tuple has no transversal**. In particular, a tuple algebraically independent over F cannot give a transversal.

This statement needs no hypothesis that every K(z) is Hadamard. For an actual multi-parameter Hadamard family it excludes a full-measure subset of its physical QLSs; it says NOTHING about the remaining exceptional algebraic locus. It is not a no-T result at every parameter.

## 2. An exact two-cyclotomic-parameter no-go

Let n=10, H∈BH(10,6), F=Q(zeta30), and let BOTH masks be arbitrary {0,1}-valued. Set

`z1=zeta18`, `z2=zeta42`.

These two numbers are algebraic, NOT algebraically independent. Nevertheless their compositum degrees are

`[F(z1):F]=phi(90)/phi(30)=3`,
`[F(z2):F]=phi(210)/phi(30)=6`,
`[F(z1,z2):F]=phi(630)/phi(30)=18`.

Thus the monomials `z1^a z2^b`, `0<=a<3`, `0<=b<6`, are an F-basis. Every physical inner product becomes a polynomial of bidegree at most(2,2) after multiplying by z1 z2; such a polynomial vanishing at this pair is identically zero. Therefore ANY transversal at `(zeta18,zeta42)` would be the SAME transversal at `(1,1)`. The catalog-conditional all-BH(10,6) no-transversal result `frontier-20261028-all-bh10-6-product-no-transversal-v1.md` SHA **ae707c663690643c541edea9c54927672d48b9d561b4477a484e2d8bbb85b3de** excludes it. This applies to ALL pairs of binary masks, not only the compatible rectangle pairs counted below; if the resulting K is not Hadamard, it simply is not a QLS.

## 3. Explicit bivariate Hadamard and 100 actual rays

`frontier-20261028-bh6-two-parameter-lift-v1.py` SHA **2c668a19e6bd70806497e919cbb1c40d6f987ff578417e75545764dcc3c2389d** finds **176** pairs of normalized valid rectangle directions over21 literal source classes with linearly independent cross-ratio signatures and identically vanishing Laurent coefficients for every K row pair. This is an exact finite scan of that particular normalized rectangle list, NOT an exhaustive classification of all two-parameter Hadamards.

One candidate uses the SECOND Aalto BH(10,6) representative and masks

```text
R1={0,2,3,5,7},       C1={0,5}
R2={0,3,5,6,9},       C2={0,2,3,4,5,6,7,9}
```

The explicit K exponents modulo126 are in `frontier-20261028-bh6-two-parameter-lift-result-v1.json`, SHA **a85d2d8477f0655a6feed52973644b7c28cb8a667405990501126161c05e2898**. Independent verifier `frontier-20261028-q126-lift-vector-check-v1.py`, SHA **36ce3551914e23b305fdc07c0195803c061313637b5095eb500c82bbe768a77e**, reconstructs the source masks, verifies the bivariate Laurent coefficients vanish for ALL unit parameters, and checks that their cross-ratio signature vectors have rank2 modulo row/column gauges. It then computes the actual q630 physical vectors exactly using Phi630 (degree144):

```text
PASS exact all-phase bivariate Hadamard, 2 independent mask directions
PASS q630 exact 100 norms,20 original ONBs,4950 distinct ray pairs
transversal_found False complete_nodes 11
PASS no transversal for this explicit q126 sample only
```

This is an actual maximal-cardinality QLS10 with NO transversal, not a 1-RQLS. The independent full sample search does not rely on the catalog no-T theorem; §2's family-wide conclusion does.

## 4. Limits

The generic theorem leaves an exceptional measure-zero locus, and the concrete cyclotomic theorem covers a special two-parameter evaluation, not arbitrary multi-parameter values or general K. The explicit sample has no transversal. Other 1-RQLS constructions, arbitrary phases and nonproduct arrays remain open. All written/number-field arguments and source imports require independent review; no formal proof or novelty clearance is claimed.
