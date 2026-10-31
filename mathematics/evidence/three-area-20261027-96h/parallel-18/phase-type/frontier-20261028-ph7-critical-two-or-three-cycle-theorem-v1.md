# Any PH7 realization at 8/9 must contain a directed 2-cycle or 3-cycle

**NEW ALL-TOPOLOGY CRITICAL-RATIO THEOREM CANDIDATE; exact symbolic/integer certificate plus independently implemented stdlib replay. Independent peer review, parent adoption, formal proof and novelty clearance pending.** MathResearch96h-2, original math-1. This is a stronger graph restriction than the earlier girth>=5 candidate; it is NOT an unrestricted 8/9 existence/exclusion theorem.

## 1. The theorem

At `z=b²/(a-c)²=8/9`, if the original H has an actual PH representation with at most seven states, its directed off-diagonal transition graph must contain a **directed cycle of length2 or3**.

Equivalently, no irreducible seven-by-seven Metzler matrix G of spectral bound0, with characteristic factor

    D(y)=y[(y+1)^2+8/9]^2,

can have a graph without 2-cycles AND without 3-cycles. Four-cycles, longer cycles, arbitrary edge counts, arbitrary holding rates, hidden roots, and input/exit supports are allowed in the contradiction. This excludes all graphs of directed girth>=4, not just an eight-edge or theta family.

The PH caller uses the separately independently supported SCC theorem `frontier-20261028-ph7-global-irreducibility-v1.md` SHA256 `729926c5fa9779ec4b1ca27156f80c4ca80c49c973ca4c7cbf352da614a94b49`, which supplies exactly seven reachable states, irreducibility and spectral bound0 after shift/scale. The present argument itself is spectral-only. Among the 14 eight-edge theta/figure-eight shapes listed in the separate graph classification, nine have girth>=4 and are excluded; the other five, all with 2- or 3-cycles, and all higher-edge short-cycle graphs remain open.

## 2. Four-cycle contributions have the required sign

The positive Perron vector of irreducible G makes each diagonal entry strictly negative. Write its seven positive diagonal escape rates as `u1,...,u7`, and let `e_j` be their elementary symmetric functions.

With no 2- or 3-cycles, the permutation expansion gives characteristic coefficients

    [y^6]det(yI-G)=e1,
    [y^5]det(yI-G)=e2,
    [y^4]det(yI-G)=e3,
    [y^3]det(yI-G)=e4-C4,                           (CHAR)

where `C4>=0` is the sum of the products of weights around every directed 4-cycle. Indeed a nontrivial permutation supporting a term of degree >=3 moves at most4 vertices; with no 2/3-cycles it must be one 4-cycle, and the product of the permutation sign and the four off-diagonal signs is negative. No two disjoint 4-cycles fit into seven vertices. There may be no 4-cycles, in which case C4=0.

Let the real monic hidden quadratic be `Q=y²+p y+q`. Matching the two leading nontrivial coefficients of `D Q` gives

    p=e1-4,             q=e2-4p-70/9.

Irreducibility and simple Perron eigenvalue0 imply every other eigenvalue has strictly negative real part; thus the two roots of Q have negative real parts and **q>0**, even if Q's roots coincide or are complex. Matching y4 and y3 gives the necessary conditions

    E4=e3-4e2+(74/9)e1-28/3=0,
    E3=e4-(70/9)e2+(212/9)e1-1007/27=C4>=0.         (REQ)

No assumption on geometric multiplicities, PH numerator cancellation, or a particular graph is used.

## 3. Eliminate one diagonal rate and obtain opposite signs

Choose ANY six of the positive rates and let `f1,f2,f3,f4` be their elementary symmetric functions; call the seventh rate x>0. Then `e1=f1+x`, `e2=f2+f1 x`, `e3=f3+f2 x`, `e4=f4+f3 x`. Define

    A=f2-4f1+74/9,
    B=f3-4f2+(74/9)f1-28/3,
    h0=f4-(70/9)f2+(212/9)f1-1007/27,
    h1=f3-(70/9)f1+212/9.

The first equation in(REQ) is `A x+B=0`. Define two polynomial quantities in the six rates:

    Qpol=81[A²-(f1-4)B],
    Hpol=-243[h0 A-h1 B].                            (QH)

The exact six-dimensional certificate proves BOTH quantities strictly positive for EVERY six positive real rates. If A=0 then `A x+B=0` forces B=0, contradicting Qpol>0. Thus A!=0; substituting `x=-B/A` gives the exact identities

    q=Qpol/(81 A),          E3=-Hpol/(243 A).

Because q>0 and Qpol>0, A>0. Consequently E3<0, contradicting the second condition E3=C4>=0 in(REQ). This proves the theorem. □

For a literal coefficient reference, the two symmetric polynomials are

    Qpol=630 f1²-324 f1 f2-81 f1 f3-1908 f1
         +81 f2²+36 f2+324 f3+2452,

    Hpol=7356 f1²-5724 f1 f2+108 f1 f3+972 f1 f4-18612 f1
         +1890 f2²-972 f2 f3-243 f2 f4+1707 f2
         +243 f3²+3456 f3-1998 f4+21094.

They are evaluated at the first four elementary sums of SIX arbitrary positive rates. Their universal positivity is the only computer-assisted inequality; q's sign and the 4-cycle sign are written Perron/permutation consequences.

## 4. Exact global positivity on the entire positive six-orthant

After substituting elementary sums, Qpol and Hpol have individual degree2 in each of the six variables, with respectively168 and435 nonzero integer coefficients. The certificate pins their exact canonical coefficient arrays by SHA256.

Use `u_i=x_i/(1-x_i)`, `0<x_i<1`, and multiply by `product_i(1-x_i)^2`. In the six-dimensional tensor Bernstein basis, coefficients are the original monomial coefficients divided by the corresponding binomial factors. The primary checker uses a common positive integer scale and INTEGER de Casteljau subdivision; no floating arithmetic occurs. It supplies two complete binary dyadic covers of the six-cube, splitting coordinate `depth mod 6`:

    Qpol: 5332 certified leaves;    Hpol: 5334 certified leaves.

Every leaf has all Bernstein coefficients nonnegative. Each coordinate was split at least once, and every leaf vertex lying in the global open cube has strictly positive coefficient. Every finite positive-rate point belongs to a leaf and receives a positive Bernstein contribution at a suitable interior-domain vertex; hence both polynomials are strictly positive. The full 10,666 leaf paths are in the pinned certificate; no grid sample or numerical lower bound is used.

## 5. Actual checks and review boundary

Primary `frontier-20261028-ph7-girth4-critical-bernstein-check.py`, **69LF/3729B**, SHA256 `8f5fc02b87996bbda2ea8b7af1976b467ef3c9a46c3a9b9274e538eea941e1c4`, actually printed

    SymPy 1.14.0 integer 6D Bernstein PASS: all girth>=4 spectral graphs excluded at z=8/9
    coefficient counts Q,H: 168 435; leaf counts: 5332 5334

Its NumPy object arrays contain only Python integers. Full tree/digest certificate `frontier-20261028-ph7-girth4-critical-bernstein-certificate.json`, **10697LF/254486B**, SHA256 `b2674b8221205230df969c205c0975486c2079202c896f6d4e37f4c6269e87d8`.

Separately written STANDARD-LIBRARY-ONLY replay `frontier-20261028-ph7-girth4-critical-integer-replay.py`, **90LF/3631B**, SHA256 `ac5b069e3d4d5c108b9b9a6e3df12172f5bc360390f92c119a0af58e48116177`, actually printed

    Independent stdlib integer PASS: all 168/435 coefficients and 5332/5334 exact six-dimensional Bernstein leaves

It independently constructs the elementary sums and(QH) using sparse rational dictionaries, verifies all coefficient digests, reconstructs both complete binary subdivision trees without NumPy/SymPy, and checks every integer Bernstein coefficient and required interior-domain vertex. The replay consumes the exact leaf lists; it is independent implementation evidence, not human/cross-vendor/Lean verification. A disjoint reviewer should independently reconstruct (CHAR)/(REQ), q>0, all coefficients/tree coverage, and the six-cube open-boundary positivity.

## 6. Remaining gap

An actual PH7 witness at8/9, if one exists, must now have a 2-cycle or a 3-cycle. This proof does NOT exclude either possibility, any of the five remaining eight-edge short-cycle shapes, or higher-edge short-cycle graphs. It does not decide the original 8/9 existence question or establish minimum8; PH6 and PH8 statements remain separate scoped inputs. No historical holds are accepted as premises and no earlier process finding is cured.

END — a critical seven-state realization necessarily contains a directed 2-cycle or directed 3-cycle.
