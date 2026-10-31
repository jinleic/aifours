# PH7 at z=8/9: the direct centered trace-two/three bound cannot by itself exclude even real hidden roots

MathResearch96h-2, original math-1. **Exact algebraic obstruction to a proposed exclusion method, not a PH7 existence or exclusion theorem.** Actual observation before writing: Wed Oct28 17:44:30 PDT2026. Independent review/novelty clearance pending. The derivation below uses no candidate graph or held result.

## Claim

For a hypothetical seven-state realization of the target, after scaling d=1 and shifting by c, write the characteristic polynomial

    det(yI-G)=y[(y+1)^2+z]^2 (y^2+p y+q).

If G is real Metzler, the familiar topology-independent centered trace-two/three inequalities below are necessary. **At z=8/9 they are STRICTLY compatible with p=8,q=15**, whose hidden roots are both real and strictly negative (-3,-5). Thus the universal trace-two/three comparison alone does not refute PH7 at the critical ratio, even if one adds real, negative hidden roots; one needs additional structure, a stronger invariant, or a genuinely new obstruction.

This is an exact feasible point in the stated NECESSARY INEQUALITIES only. It is NOT asserted to be the spectrum of any Metzler matrix with an actual PH input/exit, and it is not an all-topology feasibility point.

## Derivation of the universal necessary inequalities

Let `a=p+4`, `h=a/7`, and `X=G+hI`, so `tr X=0`. From the complete characteristic polynomial, including all multiplicities and arbitrary hidden-root coincidence, Newton sums give

    S2=tr G^2=4(1-z)+p^2-2q,
    S3=tr G^3=-4+12z-p^3+3pq,
    tau2=tr X^2=S2-a^2/7,
    tau3=tr X^3=S3+3h S2-2a^3/49.              (T)

No diagonalizability assumption is needed: traces of powers are spectral Newton sums with algebraic multiplicity.

Define real symmetric `S` by `S_ii=X_ii` and `S_ij=sqrt(X_ij X_ji)` for i!=j. Metzler off-diagonal entries make the square roots real. Then `tr S=0`, `tr S^2=tr X^2=tau2>=0`. For each unordered triple of distinct indices, AM-GM on the two oriented 3-cycle products proves `tr X^3>=tr S^3`; the diagonal and two-state cycle terms agree exactly.

For a real symmetric traceless seven-by-seven matrix with square trace tau2, the elementary compact eigenvalue extremum is

    tr S^3 >= -(5/sqrt(42)) tau2^(3/2).              (C)

For completeness: at a constrained extremum, eigenvalues solve the same quadratic Lagrange equation, hence there are at most two distinct values; zero variance is trivial. With one negative value -6t and six positive values t, the ratio is -5/sqrt42, and checking the remaining multiplicities gives no smaller ratio. Consequently a necessary condition on (p,q,z) is

    tau2>=0,    tau3 >= -(5/sqrt(42)) tau2^(3/2).  (NEC23)

This comparison has no chosen topology, positivity-of-entrywise-inverse assertion, hidden-mode localization, or assumption that its necessary inequalities are sufficient.

## Exact failure to exclude at the target

Take `z=8/9`, `p=8`, `q=15`. Then `y^2+8y+15=(y+3)(y+5)` and exactly

    h=12/7,
    tau2=874/63 >0,
    tau3=-5692/147 <0,
    (25/42) tau2^3 - tau3^2 = 9641252/107163 >0.

Because tau3 is negative, the final strict rational inequality is precisely `tau3 > -(5/sqrt42) tau2^(3/2)`. This point therefore survives(NEC23) STRICTLY. Its seven spectral values have nonpositive real part (one0, two copies each of `-1 +/- i sqrt(8/9)`, plus -3,-5), and its hidden roots are positive-coefficient real factors. These facts do NOT show that a Metzler matrix or PH transfer exists at this spectrum.

The standard-library `Fraction` checker `frontier-20261028-ph7-trace23-limit-check.py`, SHA256 `055741fed792875fe6ba2f51c11d0750ffa900ad709954128a72597a1e88efc5`, was actually run:

    Fraction exact 7-state centered trace2/trace3 non-exclusion point PASS
    z,p,q,h,tau2,tau3,comparison_slack: 8/9 8 15 12/7 874/63 -5692/147 9641252/107163
    hidden roots -3,-5; not a PH realization or existence proof

No floats, sampled eigenvalue optimization, external theorem-characterization import or scientific hidden-result assumptions are used here.

## Remaining exact gap

The actual problem additionally binds determinant AND numerator of the SAME matrix, shortest-path-distance FOUR, positive normalization/row ties, and (where used) admissible upstream and downstream principals. Any one of these or higher/cross-moment information might exclude this spectral point or all PH7 matrices. No such additional exclusion is proved here; no 8/9 solution, minimum8, or all-matrix search conclusion follows. Old PH6 lower/upper8 are not premises of this method-limit argument. Prior held outputs remain historical and nonpremises; no process finding is cured.

END — exact strict counterexample to sufficiency of the simplest universal 7-state trace-two/three exclusion test.
