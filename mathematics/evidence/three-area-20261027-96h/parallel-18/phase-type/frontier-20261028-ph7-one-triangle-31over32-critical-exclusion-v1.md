# PH7 at 8/9: a sole triangle without a 4-cycle must carry more than 31/32 of each triangle row

**NEW RATE-INDEPENDENT EXACT SUBCASE, with two independently implemented integer checks. Independent peer review, parent adoption, formal proof and novelty clearance pending.** MathResearch96h-2, original math-1. This attacks a remaining 3-cycle class, not the unrestricted 8/9 problem.

## 1. Exact claim

Let G be an irreducible seven-state Metzler matrix of spectral bound0 whose characteristic polynomial contains

    D(y)=y[(y+1)^2+8/9]^2.

Assume its off-diagonal graph has NO directed 2-cycle, EXACTLY ONE directed 3-cycle C, and NO directed 4-cycle. It may have arbitrarily many longer cycles and edges. Let the three positive diagonal escape rates on C be `u1,u2,u3`, and let w be the product of its three positive directed edge weights. Then

    w/(u1 u2 u3) > 31/32.                            (MAIN)

Under positive Perron diagonal similarity G is a row generator, its diagonal rates and cycle-edge product do not change, and each row escape rate is the sum of outgoing rates. Therefore each of the three triangle transitions separately uses **more than 31/32** of its row's total escape rate. Irreducibility and four outside vertices imply at least one triangle vertex has an outgoing edge leaving the triangle; hence the product fraction is strictly less than1.

Thus any PH7 candidate in this graph class at8/9 must have a nearly closed triangle with

    31/32 < theta=w/(u1 u2 u3) < 1.

This covers, in particular, the three eight-edge theta/figure-eight shapes whose short cycle has length3 and long cycle length>=5, but it does not exclude their remaining high-theta regime. Graphs with two or more 3-cycles, any 4-cycle, or any 2-cycle are outside the claim. No full 8/9 decision follows.

## 2. Two actual coefficient equations

Select the three triangle vertices plus ANY two outside vertices, and let their five positive diagonal rates be `u1,...,u5`, with elementary symmetric functions `s1,...,s4`. Let the remaining two outer diagonal rates be `v1,v2`; write

    t=v1+v2,   r=v1 v2,   O=u4+u5,
    theta=w/(u1 u2 u3),   0<theta<=1.

With no 2-cycles the characteristic coefficients y6,y5 are the corresponding elementary diagonal sums. The unique 3-cycle contributes `-w` to y4; with no 4-cycle it contributes `-w(O+t)` to y3. Every cycle of length>=5 contributes only degree<=2. Consequently, if D divides the actual characteristic polynomial, the hidden quadratic `Q=y²+p y+q` has

    p=s1+t-4,      q=s2+t s1+r-4p-70/9,

and the two ACTUAL coefficient conditions are

    E4=s3+t s2+r s1-w-[4q+(70/9)p+68/9]=0,
    E3=s4+t s3+r s2-w(O+t)
        -[(70/9)q+(68/9)p+289/81]=0.                 (EQ)

No q sign, PH numerator assumption, feedback topology, or root simplicity is needed for these necessary equations.

## 3. Discriminant and rate-independent positive certificate

The equations(EQ) are linear in t and r. Write them as

    E4=a00 t+a01 r+b0,     E3=a10 t+a11 r+b1,
    den=a00 a11-a01 a10,
    tn=-b0 a11+a01 b1,     rn=-a00 b1+b0 a10.

Define

    N=-19683 (tn²-4 rn den),    with w=theta u1u2u3. (N)

N is a polynomial in the five positive rates and theta, cubic in theta. The exact certificate proves

    N>0 for EVERY ui>0 and EVERY theta in [0,31/32].  (POS)

If den!=0, the equations force `t=tn/den`, `r=rn/den` and `t²-4r=-N/(19683 den²)<0`, impossible for the two real diagonal rates v1,v2. If den=0, (POS) would give `tn²<0`, also impossible. Hence(EQ) cannot hold in that theta interval. This proves(MAIN) without dividing by a potentially zero coefficient.

For(POS), the checker converts the cubic in theta to Bernstein form and divides `[0,31/32]` into the five exact dyadic intervals

    [0,1/2], [1/2,3/4], [3/4,7/8], [7/8,15/16], [15/16,31/32].

The four cubic Bernstein coefficients on each interval are polynomials in the five rates; adjacent endpoints are shared, leaving exactly 16 distinct polynomials. Each has individual degree4 in every rate. For each polynomial, compactify `ui=xi/(1-xi)` and prove positivity on `(0,1)^5` by an EXACT tensor Bernstein cover. The 16 covers have 12,754 binary dyadic leaves in total. Every leaf has nonnegative integer Bernstein coefficients and strictly positive interior-domain vertex coefficients; every dimension is subdivided at least once. This certifies strict positivity at every finite positive rate, not a sampled or floating inequality.

## 4. Exact executed evidence

Primary `frontier-20261028-ph7-one-triangle-31over32-critical-check.py`, **83LF/4323B**, SHA256 `3ee48d12eba7b231708c948bdb6af7ef112d90ce822b9106e112938e39816192`, actually finished

    SymPy 1.14.0 integer 5D Bernstein PASS: all one-triangle theta<=31/32 excluded at 8/9

The full certificate `frontier-20261028-ph7-one-triangle-31over32-critical-certificate.json`, **12907LF/327221B**, SHA256 `07c5cc114d071fae0582e90413472ef5764abc4985e14a92755317fc47fa0bc4`, pins all 16 coefficient digests and all 12,754 cover paths. NumPy object arrays in the primary checker contain Python integers only.

A separately written STANDARD-LIBRARY-ONLY replay `frontier-20261028-ph7-one-triangle-31over32-critical-integer-replay.py`, **116LF/4892B**, SHA256 `4812ee5f6066704ac5fb11cd7a1595414663bd523f21ec4a5d58b39baf0f2a7a`, independently reconstructs the actual characteristic coefficient equations, N, the cubic theta subdivisions, and every one of the 16 five-rate polynomial coefficient arrays, then verifies the FULL 12,754 binary cover leaves with integer arithmetic. It actually printed

    Independent stdlib integer PASS: all 16 triangle-rate polynomials and 12754 exact Bernstein leaves

The replay consumes the primary certificate's path lists and scales; it is independent implementation evidence, not an independent human or cross-vendor review. A disjoint reviewer should check the unique-triangle/no-4-cycle coefficient formula, linear-system determinant and zero-denominator case, all theta/rate cover boundaries, and the actual row-fraction application.

## 5. Original-question boundary

The result applies to ALL positive rates without numerical bounds and to arbitrary extra long-cycle edges, but only the stated graph/weight class. It leaves `31/32<theta<1`, multiple triangles, four-cycles, all two-cycle graphs, and the full PH7 8/9 existence question open. It does not establish a global threshold, minimum8, formal/Lean/kernel proof, independent-review acceptance or novelty. Historic process findings remain unchanged and held outputs are not premises.

END — a sole 3-cycle without 2/4-cycles must be more than 31/32 closed at the original critical ratio.
