# Every seven-state PH representation at 8/9 must contain a directed triangle

**NEW ALL-TOPOLOGY CRITICAL-RATIO THEOREM CANDIDATE. Exact six-rate integer Bernstein certificate independently replayed INCLUDING all finite zero-rate faces. Separate peer review, parent adoption, formal proof and novelty clearance pending.** MathResearch96h-2, original math-1. This strengthens `frontier-20261028-ph7-critical-two-or-three-cycle-theorem-v1.md`; the earlier immutable candidate remains valid and is not revised.

## 1. The theorem

At `z=b²/(a-c)²=8/9`, if the original H has an actual PH representation using at most seven transient states, its directed off-diagonal transition graph contains a **directed 3-cycle**.

The spectral statement is stronger: an irreducible real seven-by-seven Metzler matrix of spectral bound0 whose actual characteristic polynomial contains

    D(y)=y[(y+1)^2+8/9]^2

cannot have a graph with NO directed 3-cycle. This allows arbitrarily many directed 2-cycles, 4-cycles and longer cycles, arbitrary edge counts and all hidden-root types. It therefore strictly strengthens the no-2/no-3 theorem; no hypothesis excluding any 2- or 4-cycle is used.

For the PH caller, the previously independently supported SCC/Perron source `frontier-20261028-ph7-global-irreducibility-v1.md`, SHA256 `729926c5fa9779ec4b1ca27156f80c4ca80c49c973ca4c7cbf352da614a94b49`, provides exactly seven states, irreducibility, spectral bound0 and the actual repeated-pole multiplicities after shift/scale. No input/exit or scalar numerator is needed below.

## 2. Symmetric geometric-mean comparison is negative semidefinite

Suppose toward contradiction G has no directed 3-cycle. Define the real symmetric Metzler matrix

    S_ii=G_ii,          S_ij=sqrt(G_ij G_ji)  (i!=j).

Choose k so `A=G+kI>=0`. Since G is irreducible and has spectral bound0, A has Perron root k and strictly positive right/left Perron vectors v,w. Let `h_i=sqrt(v_i w_i)`. Cauchy–Schwarz in each row gives

    sum_j sqrt(A_ij A_ji) h_j
       <= sqrt[(sum_j A_ij v_j)(sum_j A_ji w_j)]
       = k h_i.

The symmetric nonnegative matrix on the left is `S+kI`; comparison against the positive vector h yields its spectral radius <=k. Therefore every eigenvalue of S is <=0. Write the seven real eigenvalues of `-S` as

    lambda_1,...,lambda_7 >=0.                       (REAL)

The matrix S may be reducible or singular; neither strict negativity nor a positive spectral gap is assumed.

## 3. Matching the high coefficients and comparing all 4-cycles

The bidirectional graph of S has no triangle: a triangle of positive S edges would mean all six orientations are positive in G and would create directed 3-cycles there. In determinant permutation expansions, each 2-cycle product is the same in G and S, and all disjoint pairs of 2-cycle products are also the same. Hence, in the absence of directed 3-cycles,

    [y^6]det(yI-G)=[y^6]det(yI-S),
    [y^5]det(yI-G)=[y^5]det(yI-S),
    [y^4]det(yI-G)=[y^4]det(yI-S).                  (SAME)

At y3 the only additional supports of size4 are directed 4-cycles. For each unoriented four-vertex cyclic order, let A_C,B_C be the products in the two opposite orientations in G, with missing edges interpreted as0. The two S-orientation products sum to `2 sqrt(A_C B_C)`, at most `A_C+B_C` by AM–GM. Extra one-way G cycles are also included. Their determinant signs are negative, so

    [y^3]det(yI-G) <= [y^3]det(yI-S).              (ORDER)

This accounts for ALL directed 4-cycles, overlapping cycles and disjoint 2+2 terms; it does not assert entrywise inverse positivity or symmetric similarity.

## 4. The real-rate coefficient contradiction

The characteristic factor D has a real monic quadratic quotient `Q=y²+p y+q`; irreducibility and spectral bound0 force Q Hurwitz and hence `q>0`. Let `e_j` be the elementary symmetric functions of the seven NONNEGATIVE rates lambda_i in(REAL). By(SAME), the target leading coefficients and y4 equation give

    p=e1-4,
    q=e2-4p-70/9,
    E4=e3-4e2+(74/9)e1-28/3=0.

By(ORDER), the target y3 coefficient is at most that of S, so

    E3=e4-(70/9)e2+(212/9)e1-1007/27 >=0.          (REQ)

Choose any six lambda_i and let f1,...,f4 be their elementary symmetric functions; let x>=0 be the seventh. Define

    A=f2-4f1+74/9,
    B=f3-4f2+(74/9)f1-28/3,
    h0=f4-(70/9)f2+(212/9)f1-1007/27,
    h1=f3-(70/9)f1+212/9,
    Qpol=81[A²-(f1-4)B],
    Hpol=-243[h0 A-h1 B].                            (QH)

The exact checked inequality below says BOTH `Qpol>0` and `Hpol>0` on ALL `[0,infinity)^6`, including zeros. E4=0 is `A x+B=0`. If A=0, then B=0 and Qpol=0, impossible. Thus A!=0 and x=-B/A. The actual hidden constant and comparison residual are

    q=Qpol/(81 A),          E3=-Hpol/(243 A).

Since q>0 and Qpol>0, A>0, which forces E3<0, contradicting(REQ). This proves the theorem. □

## 5. Exact certificate includes all zero-rate boundaries

The separate girth>=4 candidate `frontier-20261028-ph7-critical-two-or-three-cycle-theorem-v1.md`, SHA256 `76ff376815423d69546c10e2608f7c373a80f3e7752d306c911751e8eb50f33b`, prints the explicit symmetric Qpol/Hpol expansions and proves their positivity on positive rates. Its exact certificate `frontier-20261028-ph7-girth4-critical-bernstein-certificate.json`, **10697LF/254486B**, SHA256 `b2674b8221205230df969c205c0975486c2079202c896f6d4e37f4c6269e87d8`, contains 5332 and 5334 six-dimensional integer Bernstein leaves. Parent reports its f129 review independently reconstructed all 10,666 leaves; that review's broader conclusion does not itself check the new symmetrization application here.

The new condition needed here is positivity at **zero** eigenrates too. The separately written standard-library wrapper `frontier-20261028-ph7-girth4-nonnegative-boundary-check.py`, **33LF/1655B**, SHA256 `03d2853e583ddb5284eb2d5a35a0bae063ab1b104df40350a5283128359ee204`, reuses the independent stdlib six-dimensional replay to reconstruct all coefficients and trees, and additionally verifies strict positivity at EVERY finite boundary vertex of every leaf, including coordinates0. It actually returned

    Independent stdlib integer PASS: all 168/435 coefficients and 5332/5334 exact six-dimensional Bernstein leaves
    Exact stdlib integer PASS: Q and H strictly positive also on ALL finite zero-rate boundary faces; 10666 leaves

Every leaf has nonnegative Bernstein coefficients. Because all six coordinate directions are split at least once and every corner with all coordinates <1 is strictly positive, every compactified point with coordinates in `[0,1)` receives a positive Bernstein contribution. Thus the conclusion covers all finite nonnegative rates, not just strictly positive ones; coordinates1, corresponding to infinite rates, are outside the domain. No float, numerical grid or extrapolation is involved.

## 6. Consequences and limits

An 8/9 PH7 candidate must contain a directed 3-cycle. Combined conditionally with `frontier-20261028-ph7-one-triangle-full-critical-exclusion-v1.md` SHA256 `2e30b352597880b78bfc59baa3adead91e4d4f0f1717a8cf7f684cee0a92decc`, it must also have at least one of: a directed 2-cycle, a directed 4-cycle, or a SECOND directed 3-cycle. Neither candidate is automatically adopted from this message.

A separate graph-theoretic corollary can then rule out all eight-edge strongly connected 7-vertex graphs: their two cycles cover all vertices; if one has length3 the other has length>=5, so they have exactly one triangle and no 2/4-cycle. That forces at least nine transitions but still does not exclude seven states. The full proof of the edge corollary and its dependencies should be reviewed separately if used.

This theorem does not prove an 8/9 realization or exclusion, minimum8, global frequency threshold, novelty, Lean/kernel or cross-vendor review. The new symmetrization, 4-cycle AM–GM comparison, q>0, all-zero boundary and PH caller require a disjoint full audit. Earlier held outputs remain nonpremises; historic process findings remain.

END — every critical seven-state PH representation must have a directed 3-cycle, even if other short cycles are present.
