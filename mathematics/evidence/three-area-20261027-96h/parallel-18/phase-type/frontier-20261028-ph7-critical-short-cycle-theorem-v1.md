# Any PH7 realization at 8/9 must contain a directed cycle of length at most four

**NEW ALL-TOPOLOGY CRITICAL-RATIO THEOREM CANDIDATE, exact symbolic/integer Bernstein certificate and separately written stdlib replay. Independent peer review, parent adoption, formal proof and novelty clearance pending.** MathResearch96h-2, original math-1. This is a substantial necessary graph restriction, NOT a proof that a PH7 realization exists or does not exist at 8/9.

## 1. The theorem

Normalize `d=a-c>0`, `z=b²/d²`, and suppose the original H has an actual PH realization with at most seven states at `z=8/9`. Then its seven-state directed transition graph contains a **directed cycle of length 2, 3 or 4**.

More generally, there is NO irreducible real seven-by-seven Metzler matrix with spectral bound0 whose characteristic polynomial contains

    D(y)=y[(y+1)^2+8/9]^2

and whose off-diagonal directed graph has no directed cycle of length at most4. This excludes every directed graph of girth>=5, regardless of its number of edges, all holding rates, all hidden quadratic roots and all input/exit supports. In particular it excludes the FULL 5-/7-cycle theta graph at8/9, without any equality or restriction among its seven diagonal rates. Five of the fourteen eight-edge theta/figure-eight shapes have girth>=5 and are therefore excluded; the remaining nine and all short-cycle graphs with more edges remain open.

For the PH application, the separately independently supported SCC theorem `frontier-20261028-ph7-global-irreducibility-v1.md` SHA256 `729926c5fa9779ec4b1ca27156f80c4ca80c49c973ca4c7cbf352da614a94b49` gives exactly seven reachable states, irreducibility and spectral bound0 after the standard shift/scale. The proof below is spectral-only and does not need the PH input/output numerator.

## 2. No short cycle fixes four characteristic coefficients

Let `G` be an irreducible seven-by-seven Metzler matrix with spectral bound0. Its positive Perron vector shows every diagonal entry is strictly negative; write `G_ii=-u_i`, `u_i>0`.

Suppose the directed graph has no 2-, 3- or 4-cycle. In the permutation expansion of `det(yI-G)`, any nonidentity permutation with a nonzero term consists of one or more directed cycles, each of length at least5. Thus its non-fixed support has size at least5 and its contribution has degree at most2 in y. This remains true with any number of cycles/edges, overlapping cycles, or nonnormality. Therefore the coefficients of `y^6,y^5,y^4,y^3` are EXACTLY those of the diagonal product `product_(i=1)^7(y+u_i)`.

Choose ANY five diagonal rates and denote their elementary symmetric functions by `s1,s2,s3,s4`; write the remaining two real positive rates as `v1,v2`, and set

    t=v1+v2,     r=v1 v2,     t²-4r=(v1-v2)² >=0.

If D divides the actual characteristic polynomial, its monic quadratic quotient `Q=y²+p y+q` has

    p=s1+t-4,
    q=s2+t s1+r-4p-70/9.                             (PQ)

Matching the unaffected y4 and y3 coefficients gives two LINEAR equations in t,r:

    E4=s3+t s2+r s1 -[4q+(70/9)p+68/9]=0,
    E3=s4+t s3+r s2 -[(70/9)q+(68/9)p+289/81]=0.   (E)

All five common rates are arbitrary. No presumption that Q has real roots or that its roots differ from the visible pair is used.

## 3. Exact global discriminant contradiction

Write `E4=a00 t+a01 r+b0`, `E3=a10 t+a11 r+b1`, where each coefficient is a rational polynomial in `s1,...,s4`. Set

    den=a00 a11-a01 a10,
    tn=-b0 a11+a01 b1,
    rn=-a00 b1+b0 a10,
    Dpol=81 den,
    Npol=-19683 (tn²-4 rn den).                       (DN)

The checker proves the following GLOBAL strict inequalities for EVERY choice of five positive real rates:

    Dpol>0,          Npol>0.                           (POS)

Thus(E) has the unique real solution `t=tn/den`, `r=rn/den`, but that solution satisfies

    t²-4r = -Npol/(3 Dpol²) < 0,

contradicting the actual real diagonal rates `v1,v2`. Hence no such G exists. The coefficient matching only uses the two displayed equations; all lower characteristic coefficients, feedback weights and PH numerator data may be arbitrary. □

## 4. How (POS) is certified on the ENTIRE positive orthant

After substituting the elementary symmetric functions of five positive variables, Dpol has individual degree2 in each variable and 96 nonzero integer coefficients; Npol has individual degree4 and 1753 nonzero integer coefficients. The certificate pins the exact reconstructed coefficient arrays by SHA256.

For each variable use the compactification `u_i=x_i/(1-x_i)`, `0<x_i<1`. For a polynomial P of individual degrees d_i define

    Ptilde(x)=P(x_i/(1-x_i)) product_i (1-x_i)^d_i.

Its tensor Bernstein coefficients on the unit cube are exactly the monomial coefficients of P divided by the five corresponding binomial factors. The checker uses a common positive integer scale and INTEGER de Casteljau subdivision; it never uses floats. It provides a complete binary dyadic cover of the 5-cube, splitting coordinate `depth mod 5`:

    Dpol: 513 certified leaves;   Npol: 657 certified leaves.

Every leaf has all Bernstein coefficients nonnegative. Each coordinate has been split at least once, and every leaf corner lying in the global open cube has strictly positive coefficient. Thus every finite positive-rate point lies in a leaf and has at least one strictly positive Bernstein basis contribution; both compactified polynomials, hence Dpol,Npol, are strictly positive there. The boundary where a rate is0 or infinite need not be used for the theorem. This is an exhaustive exact five-variable cover, not a sampled grid or floating optimization.

## 5. Two actually executed checks

Primary `frontier-20261028-ph7-girth5-critical-bernstein-check.py`, **72LF/4080B**, SHA256 `43e8d8f1290734227a29528052b2ec9257c9d50b974d0640237dde41323b23a0`, actually printed

    SymPy 1.14.0 integer 5D Bernstein PASS: all girth>=5 spectral graphs excluded at z=8/9
    coefficient counts D,N: 96 1753; leaf counts: 513 657

NumPy object arrays in that program hold Python integers only. Certificate `frontier-20261028-ph7-girth5-critical-bernstein-certificate.json`, **1199LF/21546B**, SHA256 `7d3b69a2eee8917e0fcd43adc0b9f973b16b5060c40b3dbbfaab12b51ab85151`, records both complete binary cover trees and canonical polynomial-coefficient SHA256s.

A separately written STANDARD-LIBRARY-ONLY replay `frontier-20261028-ph7-girth5-critical-integer-replay.py`, **100LF/4180B**, SHA256 `10315824e34e23f94822d402dc194bb079ca571740de11e639a92f3b9b8586d0`, actually printed

    Independent stdlib integer PASS: all 96/1753 polynomial coefficients and 513/657 exact Bernstein leaves

It independently builds the five-variable elementary symmetric sums and the actual(E)/(DN) expressions using sparse rational dictionaries, compares every canonical coefficient digest, reconstructs BOTH full subdivision trees without NumPy/SymPy, checks coverage and every integer coefficient/corner sign. It consumes the certificate's two leaf-path lists; this is independent implementation evidence, not a human or cross-vendor proof. A reviewer should independently reconstruct the coefficient system, digest binding, tree coverage and open-boundary positivity, not merely trust either script.

## 6. Original-question boundary

At8/9 this strengthens the already accepted irreducibility and >=8-transition conditions: any actual PH7 graph must be strongly connected, have at least8 positive transitions, **and have a short directed cycle of length2,3 or4**. It does NOT rule out such graphs and does not determine whether the original seven-state representation exists. The earlier PH6 lower is old, the earlier PH8 upper is a separately scoped input, and neither is newly proved here. No 8/9 exclusion/minimum8, global threshold, formal/Lean/kernel proof, independent reviewer acceptance or novelty clearance is claimed. Earlier held outputs remain nonpremises and historic findings remain.

END — every actual seven-state PH candidate at the critical ratio must contain a directed 2-, 3- or 4-cycle.
