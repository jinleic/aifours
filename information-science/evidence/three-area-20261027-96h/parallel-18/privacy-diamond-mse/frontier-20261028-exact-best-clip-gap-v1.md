# Exact finite-epsilon gain from the best feasible axis clip

**AUTHOR CANDIDATE — WRITTEN plus exact Fraction coefficient and interval checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 21:17:49 PDT 2026`.

## 1. Original model, exact solver, and explicit gap

For ANY finite epsilon>0 let b=e^(-epsilon), m=b/(1-b), and consider ALL Borel additive-noise laws satisfying pure epsilon privacy for EVERY Borel event and EVERY shift in the FULL CLOSED unit l1 diamond D. J denotes E|X|_2^2.

Let g be the unique best centered diamond-staircase offset specified by the larger root in §2. Let N be geometric with `P(N=k)=(1-b)b^k`, write `M_j=E(g+N)^j`, and set `B=M2-M4/(3M2)`. For eta in [0,g/2], let P_eta be the ACTUAL original-class geometric shell law around

    K_eta=gD intersect {||x||_infinity<=g-eta}.

If B<=0, eta=0 is the UNIQUE J minimizer in this clip family. If B>0, define eta_* as the UNIQUE root in `(0,g/2)` of

    R(eta)=4eta^4-4M1 eta^3-4M2 eta^2+6M1 M2 eta-3M2 B=0.             (1)

Then eta_* is the UNIQUE family minimizer, the clipped law is truly full-D private, and the exact positive improvement is

    J(P_0)-J(P_eta*)= 4 eta_*^3 (M1-eta_*)/(3M2) >0.                    (2)

In particular, for the original ALL-law optimum V_J,

    V_J <= J(P_eta*) = min_(0<=gamma<=1)J(P_gamma)
                       -4 eta_*^3(M1-eta_*)/(3M2).                       (3)

This is an exact finite-epsilon upper bound on the ORIGINAL objective, not a claim that P_eta* attains V_J. Equations (1)–(3) are WRITTEN using no previous unreviewed theorem or parent source as a premise.

**Separate conditional radial consequence:** the parent MDA26 matching-norm alternative `privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`, gives the SAME full-D class's minimum of `W=E||X||_1^2` as a centered staircase. Since every l1-radial density has J=(2/3)W, that separately named input would identify the radial infimum with the scalar minimum in (3); consequently the actual radial-vs-all-law gap is AT LEAST the explicit positive term (2). No claim is made about every genuine norm, the exact original optimizer, source proof repair, novelty or priority.

## 2. Root g, actual privacy and monotone quartic

For the staircase P_gamma, exact layer moments give `J=M4/(3M2)`. Put m=b/(1-b). Its derivative has the sign of

    P_m(gamma)=gamma^5+5m gamma^4+(2m+12m^2)gamma^3
       +(12m^3-2m)gamma^2-m(1+2m)(1+6m)gamma+m^2(1+2m).                (4)

At `gamma0=sqrt[m(m+1)]-m` the value is `-m(m+1)sqrt[m(m+1)]<0`, while P_m(0),P_m(1)>0. Its two coefficient sign changes imply exactly two simple positive roots; the LARGER root g in (gamma0,1) is the global scalar minimum because P_0=P_1 as laws.

For every eta<=g/2, the exact clipped dilation is

    K_eta+kD=(g+k)D intersect {||x||_infinity<=g+k-eta},  k>=0.

Reduce coordinates to g-eta, then reduce their sum if needed; `2eta<=g` bounds the total l1 movement by k. The shell index changes by at most 1 under every h in D, so each P_eta obeys the original full-event privacy condition.

Exact cap integration gives Z=2M2-4eta^2>0 and

    J(P_eta)-J(P_0)=4eta^2[-B+(4/3)M1 eta-(2/3)eta^2]/Z,
    J'(eta)=16eta R(eta)/(3Z^2),
    R'(eta)=2(3M1-4eta)(M2-2eta^2)>0.                                  (5)

At the scalar root, P_m(g)=0 implies `g^4<=m(1+8m+12m^2)+2mg`. Substituting eta=g/2 and using 0<g<1 yields

    R(g/2)>=3m/4+9m^2+21m^3+12m^4
              +(2m+13m^2+6m^3)g>0.                                      (6)

The difference between the left side and the displayed lower bound is the sum of `[m(1+8m+12m^2)+2mg-g^4]/4`, `(3m/2)(g-g^3)`, `2mg^2`, and `2m^2(g-g^2)`, each nonnegative. Since R(0)=-3M2B, (5)–(6) prove the complete cases in §1 without a selected root or numerical sign table.

## 3. Derivation of the closed stationary gain

At the unique interior root R(eta_*)=0, the exact polynomial identity

    3M2[B-(4/3)M1 eta+(2/3)eta^2]
       -2eta(M1-eta)(M2-2eta^2) = -R(eta)                               (7)

makes the bracket in (5) equal to `2eta(M1-eta)(M2-2eta^2)/(3M2)`. Since `Z=2(M2-2eta^2)`, cancellation gives precisely (2). Positivity follows from eta_*<=g/2<M1. This does not depend on evaluating the quartic in radicals or on unknown 2D optimizer regularity.

## 4. Certified original-model instance at epsilon=ln 64

For b=1/64, m=1/63, exact Fraction comparisons give

    3761763123/10^10 < g < 3761763124/10^10,
    883/100000 < eta_* < 884/100000.                                    (8)

The bounds follow from P_m endpoint signs and outward interval evaluation of R; B>0 is separately checked. In (2), monotonic positive numerator factors and outward M2 bound give the rigorous certified lower

    4 eta_low^3(M1_low-eta_high)/(3M2_high)
      =3490422721931598324123/1685114800618782102083600000
      >1/500000.                                                         (9)

Thus the constructed ACTUAL P_eta* improves the best centered staircase, and hence every such staircase, by more than 1/500000 at this epsilon. The ratio in (9) is an interval LOWER BOUND on (2), not the exact algebraic gap; exact Fraction checks support the inequality, not the all-law optimum.

## 5. Source and verification limits

The Python eval kernel checked (7) coefficient-by-coefficient in exact `fractions.Fraction`, together with (8)–(9). The geometric, monotonicity, root and global model arguments are WRITTEN, not formally or independently reviewed. Parent v241 already records the relevant original threshold; this note does not reclassify it as a discovery. No MDA/LAW/v241/v253 or prior unreviewed author theorem is needed for (1)–(9); MDA26 is used ONLY in the explicitly conditional radial interpretation. This note does not rely on or alter the frozen f145 ln64 source or its required denominator correction. No source equivalence, novelty, priority or parent adoption is claimed. Review should check (6), cancellation (7), the original-model upper direction, and the exact input boundaries.
