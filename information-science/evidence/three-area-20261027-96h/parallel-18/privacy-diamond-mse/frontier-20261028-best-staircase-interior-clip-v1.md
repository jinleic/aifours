# The best diamond staircase never prefers a boundary-square clip

**AUTHOR CANDIDATE — WRITTEN plus exact all-variable Fraction coefficient checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 21:15:29 PDT 2026`.

## 1. Exact finite-epsilon claim

Fix ANY epsilon>0 and b=e^(-epsilon). The original all-law model imposes pure epsilon privacy for ALL Borel events and the FULL CLOSED unit l1 diamond D; J=E|X|_2^2. Let g be the unique minimizing offset over ACTUAL centered diamond staircases, and consider the entire ACTUAL full-D-private clipped-core family

    K_eta=gD intersect {||x||_infinity<=g-eta},  0<=eta<=g/2.

With `M_j=E(g+N)^j`, N geometric `(1-b)b^k`, define

    B=M2-M4/(3M2),
    R(eta)=4eta^4-4M1 eta^3-4M2 eta^2+6M1 M2 eta-3M2 B.               (1)

The source-independent written conclusion is that R is strictly increasing on [0,g/2] AND

    R(g/2)>0   for the actual staircase-family minimizer g,                (2)

for EVERY epsilon>0. Consequently the UNIQUE minimum of J within this clipped family is:

* eta*=0 when B<=0;
* the UNIQUE root `R(eta*)=0` in the STRICT INTERIOR `(0,g/2)` when B>0.

In the second case P_(g,eta*) is an explicitly characterized ACTUAL original-class law that improves every centered diamond staircase. This is an exact finite-epsilon family optimum, not a claim that the original all-law optimizer lies in the family.

The named parent v241 `privacy-v241-separated-threshold-and-norm-gap-entire-parent-v1.md`, SHA `48274df7a84b16cd8ead4a0b9069b8359110e1b216bc72e6baea1de03e626138`, already records the cubic threshold for the actual original diamond/rounded phase. No new threshold or priority is asserted here. If its recorded criterion is used to decide the sign of B, that is a separate parent-scoped input; the solver (1)–(2) itself does not import it.

## 2. Exact costs and monotone quartic

Put m=b/(1-b),

    M1=g+m, M2=g^2+2mg+m+2m^2,
    M4=g^4+4mg^3+6(m+2m^2)g^2
       +4(m+6m^2+6m^3)g+m+14m^2+36m^3+24m^4.

Exact l1-layer and cap integration gives, with `Z_eta=2M2-4eta^2`,

    J(P_eta)-J(P_0)= [4eta^2/Z_eta][-B+(4/3)M1 eta-(2/3)eta^2],
    dJ(P_eta)/deta=16eta R(eta)/(3Z_eta^2),
    R'(eta)=2(3M1-4eta)(M2-2eta^2).                                     (3)

The all-k clipped dilation is exact: `(gD intersect {||x||_infinity<=g-eta})+kD` equals `(g+k)D intersect {||x||_infinity<=g+k-eta}`. Clip positive-quadrant coordinates to g-eta, then lower their sum if needed; `2eta<=g` ensures total l1 reduction <=k. Its geometric shell changes index by at most 1 under any h in D, establishing actual all-event/full-D feasibility. On eta in [0,g/2], both factors in R' are strictly positive; this proves monotonicity.

## 3. A direct positive endpoint bound at the scalar optimizer

The uncut staircase derivative has the sign of

    P_m(g)=g^5+5mg^4+(2m+12m^2)g^3+(12m^3-2m)g^2
              -m(1+2m)(1+6m)g+m^2(1+2m).                                (4)

It has exactly two simple positive roots in (0,1); its larger root is the unique family minimum because P_0=P_1 as laws. Specifically, with v=m(m+1) and `g0=sqrt(v)-m` in (0,1), direct substitution gives `P_m(g0)=-v sqrt(v)<0`. Positivity of P_m(0),P_m(1), and Descartes' sign rule then prove the root classification independently of an unreviewed selector candidate.

At any such positive root g, rearranging P_m(g)=0 and discarding nonnegative terms gives

    g^4 <= m(1+8m+12m^2)+2mg.                                           (5)

Expanding R(g/2), and using 0<g<1, gives the uniform strict lower bound

    R(g/2) >= 3m/4+9m^2+21m^3+12m^4
                 +(2m+13m^2+6m^3)g >0.                                  (6)

One transparent way to check (6) is to subtract its right side from R(g/2). The difference is exactly

    [m(1+8m+12m^2)+2mg-g^4]/4
       +(3m/2)(g-g^3)+2mg^2+2m^2(g-g^2),                                (7)

all nonnegative by (5) and 0<g<1. Thus whenever B>0 the monotone quartic root exists BEFORE eta reaches the square-core boundary; no boundary case or numerical sign check is needed.

## 4. Claim boundaries and actual checks

A Python eval-kernel `fractions.Fraction` sparse-polynomial calculation checked the FULL bivariate coefficient identity (7), and a separate exact four-variable calculation checked both derivative identities in (3). These checks certify only algebraic identities, not the privacy, variational or all-law conclusions. One exploratory helper call previously failed with an `AttributeError` after a Fraction shadowed a function; only that failed step was retried and disclosed in the companion quartic candidate.

The proof is WRITTEN from actual shell geometry, all-event privacy, scalar calculus and Descartes' rule; no LAW642, MDA, v241, v253 or previous unreviewed author theorem is a premise. It does not establish an all-law exact optimum, source equivalence, novelty, formal proof, independent/cross-model review or parent acceptance. Suggested review: bound (5), exact identity (7), eta=g/2 inclusion and the scope distinction between family and global optimization.
