# An exact finite-epsilon solver for the feasible clipped-diamond family

**AUTHOR CANDIDATE — WRITTEN plus exact Fraction polynomial/interval checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 21:13:52 PDT 2026`.

## 1. Actual class and exact finite solver

Fix ANY epsilon>0, b=e^(-epsilon), and ANY offset g in (0,1]. For every eta in [0,g/2], define the compact core and ACTUAL full-D-private shell law

    K_eta=gD intersect {||x||_infinity<=g-eta},
    P_eta(dx) proportional to b^(min{k:x in K_eta+kD}) dx.

Here D is the FULL CLOSED unit l1 diamond, and privacy is for ALL Borel events. The source-independent written result below determines the UNIQUE minimizer of the actual original squared-Euclidean J=E|X|^2 inside this ENTIRE one-parameter clipped family, with a monotone quartic. It does NOT assert that this family contains the global all-law optimum.

Let N be geometric with `P(N=k)=(1-b)b^k`, `M_j=E(g+N)^j`, and

    B=M2-M4/(3M2),
    R(eta)=4eta^4-4M1 eta^3-4M2 eta^2+6M1 M2 eta-3M2 B.               (1)

Then R is STRICTLY increasing on `[0,g/2]`. The unique cost-minimizing clip is

* eta*=0 if B<=0;
* the unique root R(eta*)=0 in (0,g/2] if B>0 and R(g/2)>=0;
* eta*=g/2 if B>0 and R(g/2)<0.

All three are actual full-D-private laws, including the boundary square core eta=g/2. For B>0 the minimum is strictly below the uncut staircase cost. This is a finite exact characterization within the stated family; it uses no unreviewed author result or global radiality assumption.

## 2. Exact layer geometry and derivative

For 0<=eta<=g/2 and every integer k>=0,

    K_eta+kD=(g+k)D intersect {||x||_infinity<=g+k-eta}.                 (2)

The reverse inclusion follows by reducing each positive-quadrant coordinate to at most g-eta at total l1 cost <=k, then lowering their sum to g if needed; the inequalities and `2eta<=g` bound the total. At the endpoint 2eta=g the four removed caps only touch on null boundaries.

At radius R0=g+k each removed cap has area eta^2 and squared-Euclidean moment `R0^2 eta^2-(4/3)R0 eta^3+(2/3)eta^4`. Exact geometric summation gives

    Z_eta=2M2-4eta^2>0,
    J(P_eta)-J(P_0)
      =[4eta^2/Z_eta][-B+(4/3)M1 eta-(2/3)eta^2].                       (3)

Differentiation yields the exact identities

    dJ(P_eta)/deta=16 eta R(eta)/(3Z_eta^2),
    R'(eta)=2(3M1-4eta)(M2-2eta^2).                                     (4)

For 0<=eta<=g/2, `3M1-4eta>=g>0` and `M2-2eta^2>=g^2/2>0`. Thus R is strictly increasing, and the cases in §1 follow with all endpoint/equality cases handled. At eta=0 continuity supplies the uncut law; there is no numerical search, radiality premise or unexamined local stationary root.

## 3. Exact original-objective obstruction at ln 64

At epsilon=ln 64, let m=1/63 and let g be the larger positive root of the actual uncut staircase quintic

    P_m(x)=x^5+5mx^4+(2m+12m^2)x^3+(12m^3-2m)x^2
           -m(1+2m)(1+6m)x+m^2(1+2m).

Exact signs at `a=3761763123/10^10` and `z=3761763124/10^10`, positive endpoint signs, and Descartes' two-change bound put this unique global staircase-family minimizing root in (a,z). Fraction interval arithmetic gives B>0 and the exact monotone-quartic signs

    R(883/100000)<0<R(884/100000),
    0.00883<eta*<0.00884<g/2.                                            (5)

For a FULLY RATIONAL competing mechanism, instead use core offset a and eta=8835/10^6. Its exact cost is given by (3), with the geometric moments at (a,m). The following inequality was checked by exact fractions:

    [M4(a)/(3M2(z))] - J(P_(a,8835/10^6)) >1/500000.                    (6)

Because M4 and M2 have positive coefficients and g in (a,z), the first term in (6) is a rigorous lower bound on the ENTIRE staircase-family minimum. Hence the stated rational, ACTUAL full-D private law improves EVERY centered diamond staircase by >1/500000. This is an original all-law obstruction, not a claim that the rational law is globally optimal.

**Separate conditional all-radial bridge:** parent MDA26 `privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA-256 `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`, gives the same-model matching-l1-norm square minimum as a centered staircase. Since each l1-radial density has `J=(2/3)E||X||_1^2`, (6) THEN excludes every l1-radial law as a J optimizer. That additional conclusion depends on the named parent alternative, not on a mean-only source or on assuming original radiality.

## 4. Owner checks and disclosure

The Python eval kernel checked the full formal identities `(N'Z-NZ')=(16/3)eta R` for (3) and `R'=2(3M1-4eta)(M2-2eta^2)` coefficient-by-coefficient using exact `fractions.Fraction`. It also checked the exact rational root/eta interval signs and (6). A helper name had been shadowed by an existing Fraction, causing one `AttributeError`; only that failed symbolic step was rerun with the intact named polynomial and succeeded. Decimal renderings were diagnostic, not evidence.

No LAW642, v241, v253, MDA, previous unreviewed theorem or external source is imported into the exact solver or unconditional counterexample. The ALL-radial bridge is explicitly conditional on the named MDA26 parent. This does not repair the separately frozen f145 source or its mandatory numeric correction. No exact global all-law optimum, source-equivalence, novelty, formal/independent review or parent acceptance is claimed. Priority review should check (2), the derivative identity, endpoint eta=g/2, unique-root cases, and (6)'s outward rational comparisons.
