# PH7 at 8/9: every graph with one 3-cycle and no 2- or 4-cycle is impossible

**NEW FULL RANGE EXACT THEOREM CANDIDATE, two independent integer implementations; peer review, parent adoption, formal proof and novelty clearance pending.** MathResearch96h-2, original math-1. This prospectively strengthens the earlier `theta<=31/32` source `frontier-20261028-ph7-one-triangle-31over32-critical-exclusion-v1.md` SHA256 `e7fbda7fab458e918f4a71a35146bcd4229bb5f7217995637d1b68ffff4e63fd`; that earlier immutable source remains true and is NOT rewritten.

## 1. Claim and scope

At the original critical ratio `z=b²/(a-c)²=8/9`, no actual seven-state PH realization can have a directed graph with

* NO directed 2-cycle;
* EXACTLY ONE directed 3-cycle; and
* NO directed 4-cycle.

The graph may otherwise contain arbitrary long cycles and arbitrarily many directed edges; all seven positive diagonal rates and all input/exit supports are unrestricted. The spectral theorem is stronger: no irreducible seven-by-seven Metzler matrix of spectral bound0 with this graph can have characteristic factor

    D(y)=y[(y+1)^2+8/9]^2.                            (D)

For PH, the separately supported SCC/Perron theorem gives exactly seven states, irreducibility, positive diagonal escape rates and spectral bound0 after shift/scale. This source does NOT prove the original PH7 8/9 question: graphs with a 2-cycle, multiple 3-cycles, or a 4-cycle are outside this claim.

Together with the separately frozen `frontier-20261028-ph7-critical-two-or-three-cycle-theorem-v1.md`, the following conditional structural consequence holds: among the 14 possible strongly connected 8-edge theta/figure-eight shapes, 12 are excluded at8/9. The only two remaining 8-edge shapes have a 2-cycle. This uses the separate exact graph classification and both theorem candidates; higher-edge short-cycle graphs remain open.

## 2. Actual characteristic coefficients

Positive Perron diagonal similarity makes G a row generator, preserving diagonal entries and cycle-edge products. Let the triangle's three diagonal escape rates be u1,u2,u3 and its edge-product w>0. Each triangle edge is at most its row escape rate, so

    w=theta u1 u2 u3,       0<theta<=1.               (THETA)

Choose ANY two of the four outside vertices, call their rates u4,u5, and put `O=u4+u5`. Let the two remaining outside rates be v1,v2 with `t=v1+v2` and `r=v1v2`. Let s1,...,s4 be the elementary symmetric functions of u1,...,u5.

Since there are no 2-cycles, the y6 and y5 coefficients of the actual characteristic are the first two diagonal elementary sums. Its unique 3-cycle contributes `-w` to y4. Since there is no 4-cycle, that same 3-cycle contributes `-w(O+t)` to y3; all cycles of length>=5 contribute degree<=2. If D divides the characteristic, the hidden quadratic `Q=y²+p y+q` therefore obeys

    p=s1+t-4,     q=s2+t s1+r-4p-70/9,
    E4=s3+t s2+r s1-w-[4q+(70/9)p+68/9]=0,
    E3=s4+t s3+r s2-w(O+t)
       -[(70/9)q+(68/9)p+289/81]=0.                 (EQ)

All identities are coefficients of the SAME actual matrix. No q sign, numerator identity, or assumption on hidden roots is needed.

## 3. A cubic positive for ALL theta

The equations(EQ) are linear in the real outer-rate sum t and product r. Write

    E4=a00 t+a01 r+c0,     E3=a10 t+a11 r+c1,
    den=a00 a11-a01 a10,
    tn=-c0 a11+a01 c1,     rn=-a00 c1+c0 a10,
    N=-19683(tn²-4 rn den), with w=theta u1u2u3.     (N)

For fixed positive u1,...,u5, N is a cubic polynomial in theta. Let its four cubic Bernstein coefficients on `[0,1]` be b0,b1,b2,b3:

    N(theta)=b0(1-theta)^3+3b1 theta(1-theta)^2
             +3b2 theta²(1-theta)+b3 theta³.         (BERN)

The exact five-rate certificate proves the following **strict** inequalities for ALL positive u1,...,u5:

    b0>0,      b1>0,      b3>0,
    4 b1 b3 - 3 b2² > 0.                            (POS)

Indeed, the symmetric matrix

    [ 3b1       3b2/2
      3b2/2     b3   ]

is positive definite: its leading entry is positive and its determinant is `(3/4)(4 b1 b3-3 b2²)>0`. Thus the bracket

    3b1(1-theta)²+3b2 theta(1-theta)+b3 theta²

is strictly positive for every theta in[0,1]. Equation(BERN) gives N>0 everywhere on that interval, including endpoints.

If den!=0, the coefficient equations force `t=tn/den`, `r=rn/den` and

    t²-4r=-N/(19683 den²)<0,

impossible because t,r are the sum/product of real v1,v2. If den=0, N>0 would require `tn²<0`, also impossible. Thus(EQ) has no actual solution for any positive rates or theta in[0,1], proving the theorem. □

## 4. Exact global positivity certificate

After substituting the five elementary-sum expressions, b0,b1,b3 each have individual degree4 in the rates; `4 b1 b3-3 b2²` has individual degree8. Their exact coefficient counts are respectively `1753,1753,1717,31422`.

Compactify `ui=xi/(1-xi)` for `0<xi<1` and multiply by `product_i(1-xi)^degree_i`. Exact INTEGER tensor Bernstein subdivision certifies strict positivity of the four resulting polynomials on the entire open five-cube. The binary dyadic leaf counts, in the order above, are

    657, 567, 522, 565.                              (LEAVES)

Every leaf has all Bernstein coefficients nonnegative and all vertices lying in the global open cube strictly positive; each coordinate was subdivided at least once. Hence every finite positive-rate point gets a strictly positive Bernstein contribution. No floating arithmetic, rate box cutoff or numerical extrapolation is involved.

## 5. Two actually executed verifications

Primary `frontier-20261028-ph7-one-triangle-full-critical-check.py`, **77LF/4147B**, SHA256 `dd323a51986972808cdcc209bbc2df58b81214072c2ec760480546c04996a6d3`, actually printed

    SymPy 1.14.0 integer 5D Bernstein PASS: every one-triangle/no-2/4 spectral graph excluded at 8/9

Certificate `frontier-20261028-ph7-one-triangle-full-critical-certificate.json`, **2377LF/51575B**, SHA256 `d1195a6f0099d105eb34e5a6acbeb1fec3d81c333658af7a3c8b2ea5ac79f2c9`, pins all four complete binary cover trees and canonical coefficient digests. NumPy object arrays contain only Python integers.

Separately written STANDARD-LIBRARY-ONLY replay `frontier-20261028-ph7-one-triangle-full-critical-integer-replay.py`, **128LF/5483B**, SHA256 `7c20fce389e2b87f4e4df3d9ac31f33bb62b40e8fcd19cb3e53f982fc13b7536`, independently reconstructs the actual characteristic equations and full cubic in theta with sparse rational dictionaries, computes all four Bernstein coefficient polynomials and their product/square, verifies all coefficient digests, and reconstructs every integer subdivision tree. It actually printed

    Independent stdlib integer PASS: all four full-theta polynomials and 2311 Bernstein leaves

The replay consumes the certificate's four leaf lists; it is independent implementation evidence, not a human/cross-vendor/Lean audit. A disjoint review must verify the one-triangle/no-four-cycle coefficient accounting, zero-denominator case, cubic positive-definite argument, 5D integer tree coverage and positive open-boundary inference, and actual PH caller.

## 6. Remaining original gap

The whole high-theta slice left open by the earlier 31/32 theorem is now excluded within this graph class. The result still permits a 2-cycle, multiple triangles, a 4-cycle, and all other higher-edge graphs. It does not determine PH7 existence at8/9 or prove minimum8. Earlier held outputs remain nonpremises and historic process findings remain.

END — a unique directed triangle without a 2- or 4-cycle cannot occur in any critical seven-state spectral realization.
