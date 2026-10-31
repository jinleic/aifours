# PH7 feasibility above 1/2 has finitely many algebraic bands; any rational-z witness can be algebraic

**WRITTEN CANDIDATE, independent review/novelty clearance pending.** MathResearch96h-2. The exact PH/generator equivalence is from `frontier-20261028-ph7-compact-feasibility-and-endpoint-dichotomy-v1.md` SHA256 `0e83c669c46820de884c298e533ca0389b8c15f63efc7979b538bf9f60c9108b`; its spectral compactness dependency is unreviewed and explicitly remains conditional. This file imports the public Tarski–Seidenberg quantifier-elimination theorem, e.g. Theorem 4.8 in Heng Yang's [semialgebraic geometry notes](https://hankyang.seas.harvard.edu/Semidefinite/SOS.html#basic-algebraic-geometry) and ordered-ring quantifier elimination in Passmore–de Moura, [§2](https://leodemoura.github.io/files/addct-09.pdf). Neither is represented as newly proved here.

## 1. Main result

Let `Z7` be the set of all real `z>1/2` for which the original H admits a PH realization using at most seven states (for one, equivalently every c,d>0 with the prescribed ratio). Conditional on the named exact PH equivalence and compactness:

1. `Z7` is semialgebraic over the rationals. Consequently it is a FINITE union of intervals and isolated points; every finite boundary point is a real algebraic number.
2. `Z7` is relatively closed in `(1/2,infinity)`. Thus every finite boundary point above1/2 that belongs to the closure actually has a PH7 realization. In particular 8/9 is either realizable or separated from Z7 by a strictly positive gap, as in the preceding endpoint dichotomy.
3. If an algebraic z>1/2 is realizable, there is a realization for the normalized parameters `c=d=1` in which EVERY entry of T, alpha and omega is a real algebraic number. In particular, any 'yes' at the rational critical z=8/9 has a finite algebraic witness in principle; an arbitrary transcendental limiting matrix is unnecessary.
4. The exact 8/9 existence problem has the finite rational-coefficient real-algebraic feasibility formulation below and is decidable by general real-closed-field quantifier elimination IN PRINCIPLE. No such elimination or computational verdict was performed, and no practical runtime or small certificate is claimed.

These statements describe the global shape and exact evidence types, not which band contains8/9, the number of bands, an endpoint polynomial, monotonicity, or a new PH6 result.

## 2. A complete rational polynomial system at 8/9

For tau=c/d=1 set `z0=8/9` and

    D(y)=y[(y+1)^2+8/9]^2,
    K=D(1)=(4+8/9)^2=1936/81,
    Q(y)=y^2+p y+q.

The following is a finite existential sentence over the rationals. Its real variables are 42 off-diagonal rates `g_ij` (i!=j), 7 input entries beta_i, 7 exit entries gamma_i, and p,q; diagonal entries are defined by `G_ii=-sum_(j!=i)g_ij`:

    g_ij>=0,       beta_i>=0,       gamma_i>=0,
    sum_i beta_i=1,
    det(yI-G)=D(y) Q(y),
    beta adj(yI-G) gamma=K Q(y),                   (PH8/9)

where polynomial identities mean equality of ALL coefficients. The two equations each involve the same actual G. All constraints have rational coefficients; no inverse, trigonometric, analytic or matrix-exponential condition appears in the formula.

This sentence is TRUE iff an actual PH realization with <=7 states exists at 8/9. The forward direction is the positive-Perron gauge of the named predecessor. In the converse direction, the characteristic identity and the z>1/2 SCC lemma make G irreducible. `h=(I-G)^(-1)gamma` is strictly positive, `beta h=1` follows by evaluating the numerator identity at y=1, and

    T=diag(h)^(-1)(G-I)diag(h),
    alpha=beta diag(h),    omega=diag(h)^(-1)gamma

are actual PH data with all required row ties, nonnegative input/exit, Hurwitz T and exact transfer. Gamma cannot be zero because the constant K is positive and Q(1)>0 for a row generator. This verifies the full application; merely satisfying the characteristic factor without the second SAME-matrix identity would be insufficient.

## 3. Why the algebraicity and finite-band conclusions hold

For symbolic z>1/2, replace 8/9 and K by `z` and `(4+z)^2` in(PH8/9). All constraints remain polynomial with rational coefficients. Projecting this real semialgebraic set to z gives Z7. Tarski–Seidenberg gives a quantifier-free description by finitely many univariate rational polynomials and Boolean sign conditions. On each interval between their finitely many real roots, all signs are constant; each finite endpoint is consequently a real root of a nonzero rational polynomial. This proves the finite-band/algebraic-boundary statement, without computing that description.

For a fixed real algebraic z, the quantified system has coefficients in the real algebraic field. The latter is real closed; real-closed-field quantifier elimination implies an existential polynomial system over that field has a solution there whenever it has one over R. Therefore G,beta,gamma,p,q can all be chosen real algebraic. Since `I-G` is invertible, h is also real algebraic, and the displayed PH normalization preserves algebraicity. This is a mathematical witness-existence result, not an assertion that a particular algebraic sample or a rational sample has been found.

The relative-closedness statement uses the separate compactness theorem on each closed rational subinterval `[L,U]` with L>1/2. It is not a general property of projections (which need not be closed); the compact normalization and uniform resolvent bounds are essential. The criterion is therefore conditional on that proof and its algebraic applications.

## 4. What would settle 8/9

A positive answer requires actual algebraic data satisfying all coefficients of(PH8/9), independently verified and converted to a PH matrix. A negative answer can be obtained by an exact verified unsatisfiability proof of that SAME full system, or another sound universal obstruction. The existence of a decision algorithm does not constitute such a proof or a feasible computational plan. There is currently no endpoint witness and no all-topology exclusion in this file.

No held output, retrospective finding repair, actual QE run, kernel/Lean/cross-vendor verification, novelty clearance or stronger admission is claimed. All historic qualifications remain.

END — the post-PH6 PH7 parameter set is a finite algebraic band/point union, and 8/9 has a precise finite rational-algebraic witness-or-refutation problem.
