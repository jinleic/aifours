# Exact route obstruction: Newton spectral inequalities leave a large-hidden-pole tail

Before-creation clock observed: **2026-10-23T14:04:19-07:00**. Slotmath-1, same PH residual problem. Status: **CANDIDATE written route assessment / NOVELTY_UNCLEAR**. No scientific program or parameter evaluation was performed.

## Source and precise question

The primary source actually read is Olga Holtz, [*M-matrices satisfy Newton's inequalities*, arXiv:math/0512610v1](https://arxiv.org/abs/math/0512610), especially the M-matrix definitions and Theorem4. It states that the normalized characteristic coefficients c_j=e_j/binomial(n,j) of a matrix similar to an M-matrix satisfy c_j^2>=c_(j-1)c_(j+1). Singular M-matrices are included. This is a named classical result, not a new theorem established by our search; the source proof was read but not independently authenticated here.

For a reachable six-state PH candidate, T has spectral abscissa-c by the already reconstructed trimming/Perron argument. Thus -(T+cI) is a singular M-matrix. After dividing rates by d=a-c and putting

    z=beta^2, v=(u-c)/d>0,

its characteristic polynomial is

    x(x+v)(x^2+2x+1+z)^2.

One might hope Newton's inequalities constrain the large hidden pole strongly enough to close the six-state residual. The following exact calculation shows why those spectral inequalities alone do not do that on the current band.

## All six normalized coefficients

Writing the characteristic elementary coefficients with positive signs,

    c0=1,
    c1=(v+4)/6,
    c2=(4v+6+2z)/15,
    c3=((6+2z)v+4+4z)/20,
    c4=((4+4z)v+(1+z)^2)/15,
    c5=(1+z)^2 v/6,
    c6=0.

These follow by ordinary multiplication. For fixed z, each Newton difference is a polynomial in v. Its leading term is:

    j1: v^2/36;
    j2: [(19-15z)/900]v^2;
    j3: [(9z^2-10z+17)/900]v^2;
    j4: [(1+z)^2(19-15z)/900]v^2;
    j5: [(1+z)^4/36]v^2.

For j3 the numerator has negative discriminant100-4·9·17<0 and positive leading coefficient, hence is positive for all real z. Every other displayed leading coefficient is strictly positive whenever0<=z<19/15. In particular this holds throughout the compact target band[1/2,53/96].

Consequently, for every fixed z in that band, all five Newton inequalities hold strictly for all sufficiently large v. The same conclusion is uniform on the whole closed band: the leading coefficients have a positive compact minimum and the finitely many lower coefficients have finite compact maxima, so one sufficiently large cutoff works simultaneously.

This is an exact large-v statement, not a claim that any such spectrum is M-matrix- or PH-realizable. It proves only that this complete family of Newton necessary conditions cannot supply an upper bound on the hidden pole or eliminate its whole tail.

## Consequence for the active attack

The new heterogeneity-gap candidate pushes any residual PH6 toward a separated hidden pole/nonuniform rate regime. Newton's spectral conditions do not close that regime: passing them is not a transfer-function realization, and their large-v feasibility is not a counterexample to a six-state lower bound. The next consequential constraint must use additional M-matrix structure, the five-vertex shortest path/one-extra-state geometry, or the actual input-output cancellation identity. Merely adding more Newton coefficient tests of this same characteristic polynomial has no headroom for excluding the entire large-v tail.

No all-topology six-state existence or impossibility is inferred. This assessment is a route obstruction within the same primary problem, not a new scientific slot or a solved book question.
