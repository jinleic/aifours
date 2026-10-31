# A genuine clipped-core competitor for the full mixed-loss frontier

**AUTHOR CANDIDATE — WRITTEN with an exact rational construction check; NOT independently reviewed or parent-adopted.** Native pre-write clock `Wed Oct 28 18:41:34 PDT 2026`.

## 1. Original all-law objective and constructive advance

For finite epsilon>0 set b=e^(-epsilon), m=b/(1-b), and let F_epsilon be ALL Borel laws satisfying epsilon privacy for EVERY Borel event and EVERY shift in the FULL CLOSED l1 unit diamond D. Write

    J(mu)=E||X||_2^2,    W(mu)=E||X||_1^2,
    W_*=inf_F W,         H_lambda=inf_F [J+lambda W],    lambda>=0.

The named matching-norm theorem gives an ACTUAL centered staircase W-minimizer Q_q with some 0<q<1. This note constructs a fully private clipped-core law whose cost is STRICTLY BELOW the radial staircase value for a concrete nonempty interval of weights whenever an explicit scalar condition holds.

Let `M_j=E(q+N)^j`, where N is geometric with P(N=k)=(1-b)b^k. Put

    A=M4/(2M2)-M2,            B=M2-M4/(3M2).                            (1)

At EVERY such W-minimizing q, A>0. If B>0 define `Lambda=B/A`. Then for EVERY `0<=lambda<Lambda` there is an explicitly specified `eta>0` and an ACTUAL full-D-private clipped law Q_(q,eta) such that

    H_lambda <= J(Q_(q,eta))+lambda W(Q_(q,eta))
               < J(Q_q)+lambda W(Q_q) = (lambda+2/3)W_*.                (2)

Thus the centered squared-l1 optimum is NOT an optimizer of this original full-law mixed objective in that whole weight interval. No claim is made for lambda>=Lambda or when B<=0. No assumption about uniqueness of nonradial W optimizers is used.

Moreover, with `s=m^(1/4)`, as epsilon->infinity,

    Lambda = 1/(3s) - 5/6 + O(s).                                        (3)

In particular B>0 for all sufficiently large epsilon, Lambda diverges, and for EACH fixed finite lambda>=0 the strict actual-law improvement in (2) eventually holds. This is a rigorous low-privacy constructive window, NOT an exact global scalarized phase diagram or claim that a lambda-weighted PMLR theorem exists.

## 2. Sole research input and explicit geometry

Parent matching-norm per-cost alternative proof `institute/runs/three-area-2026-10-23-96h/privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`, supplies an attained centered staircase W-minimizer in the SAME full-Borel/full-closed-D class. The squared-l1 scalar cost has q in (0,1): Q_0=Q_1 as laws and its exact derivative at 1 is positive, so the endpoint is not a minimum. This is elementary scalar calculus, not an imported original Euclidean optimizer or threshold.

For `0<eta<q/2`, define the ACTUAL convex core

    S_(q,eta)=qD intersect {max(|x1|,|x2|)<=q-eta}.

Its normalized geometric shell density is `p_(q,eta)(x)=Z_eta^(-1)b^(min{k:x in S_(q,eta)+kD})`. Membership plus the full closed-D triangle inequality proves `|n(x+h)-n(x)|<=1` for EVERY x,h; hence Q_(q,eta) is actually private for EVERY Borel event and every h. It is not a formal profile, linearized deformation or unverified numeric array.

For every integer k>=0, with R=q+k,

    S_(q,eta)+kD = R D intersect {max(|x1|,|x2|)<=R-eta}.              (4)

A direct proof: by sign/permutation symmetry take x,y>=0 satisfying `x+y<=q+k` and `x,y<=q+k-eta`. Lower each coordinate to at most q-eta, at total l1 cost <=k: if both need lowering the cost is at most `k-q+2eta<k`; if only one does, its cap bound makes the cost <=k. If their remaining sum exceeds q, lower coordinates further to sum q; the TOTAL lowering is then x+y-q<=k. The result lies in S_(q,eta), and the removed vector lies in kD. The reverse inclusion follows from the two triangle inequalities. This is an exact SAME-core dilation, not an assumed rounded-circle ansatz.

## 3. Exact all-layer costs, including cubic and quartic terms

For the radius-R diamond, the four removed axis caps are disjoint because eta<q/2<=R/2. On one cap write x1=R-u, `0<=u<=eta`, `-u<=x2<=u`. Exact integration gives per cap

    area=eta^2,
    integral (x1^2+x2^2)=R^2 eta^2-(4/3)R eta^3+(2/3)eta^4,
    integral (|x1|+|x2|)^2=R^2 eta^2-(2/3)R eta^3+(1/6)eta^4.        (5)

Using the geometric layer identity and `(1-b)sum b^k=1`, the actual normalizer and the two actual unnormalized moments are

    Z_eta = 2M2 - 4eta^2,
    NJ_eta = (2/3)M4 -4M2 eta^2 +(16/3)M1 eta^3 -(8/3)eta^4,
    NW_eta = M4 -4M2 eta^2 +(8/3)M1 eta^3 -(2/3)eta^4.                 (6)

Here `(Z_eta,NJ_eta,NW_eta)` are for ONE actual law Q_(q,eta), and `J=NJ_eta/Z_eta`, `W=NW_eta/Z_eta`. No first-order boundary approximation or neglected infinite-tail term is used.

For the centered staircase Q_q, `Z0=2M2`, `W0=M4/(2M2)=W_*`, `J0=M4/(3M2)=(2/3)W_*`. Its interior scalar optimum satisfies

    2M3 M2=M4 M1,    hence W0=M3/M1.

The geometric N is nondegenerate, so

    A=W0-M2=[M3-M1 M2]/M1=Cov(q+N,(q+N)^2)/M1>0.                       (7)

The covariance is strictly positive because both functions are strictly increasing and N has at least two positive-probability values. This proves positivity without a root sign table.

## 4. Explicit competitor and guaranteed positive gap

Suppose B=M2-J0>0, let Lambda=B/A and take any `0<=lambda<Lambda`. Set

    Delta=B-lambda A>0,
    C_lambda=(4/3+2lambda/3)M1>0,
    eta=min{q/4, Delta/(2C_lambda)} >0.                                  (8)

This eta satisfies eta<q/2 and the actual normalizer Z_eta>0. Subtracting `(J0+lambda W0)Z_eta` from (6) yields EXACTLY

    (J(Q_(q,eta))+lambda W(Q_(q,eta)))-(J0+lambda W0)
      = [4eta^2/Z_eta][ -Delta + C_lambda eta
                         -(2/3+lambda/6)eta^2 ]
      <= - Delta eta^2/M2 <0.                                            (9)

The inequality uses `C_lambda eta<=Delta/2` and `Z_eta<=2M2`. Equation (2) follows with an explicit actual law and a positive numerical-formula gap. It is not an assertion that the clipped law is the globally optimal H law.

## 5. All-variable low-privacy window

Let s=m^(1/4). A trial q=s and the elementary bound

    W(Q_q)>=(q^4+m)/[2(q^2+4m)]

force q^2=Theta(s^2) for every global staircase minimizer. The leading scalar cost is `(s^2/2)(z^2+z^(-2))` with z=q/s, so global minimality gives z->1. The stationary polynomial divided by s^5 begins

    z^5-z-2s z^2+2s^2 z^3+O(s^3)=0.

The root near z=1 is simple, and implicit expansion gives

    q=s+(1/2)s^2-(5/8)s^3+O(s^4),
    M2=s^2+s^3+O(s^5),
    W0=s^2+2s^3+(3/2)s^4+O(s^5).

Therefore

    A=s^3+(3/2)s^4+O(s^5),
    B=(1/3)s^2-(1/3)s^3-s^4+O(s^5),
    Lambda=B/A=1/(3s)-5/6+O(s).

This proves (3), B>0 eventually and the strict competitor for every fixed finite lambda at all sufficiently large epsilon. It does not assert the sign of B in other regimes or claim Lambda is a NECESSARY/SHARP global boundary.

## 6. Exact selected construction and a failed trial disclosed

A Fraction cell first tried `m=1/10000`, rational q=1/10, lambda=1. Its actual condition was `A>0, B>0` but `Delta<0`; an unguarded calculation produced negative eta and was NOT a valid competitor. That failed selected trial is disclosed, not relabelled as progress.

I then chose a different rational TRIAL q=21/200, still m=1/10000, lambda=1, and required A,B,Delta>0 before constructing eta. Exact observed output:

```text
m= 1/10000 q= 21/200 lambda= 1 A>0= True B>0= True Delta>0= True
eta= 19004022149/3904822340000 clipped_H_less= True positive_gap= True guaranteed_bound= True
q is a rational trial, NOT asserted to be exact global W-minimizer
```

The second control verifies (6)–(9) arithmetically for two actual private shell laws. It is NOT used to infer the sign at the unknown optimal q; that all-variable large-epsilon sign is proved in §5.

## 7. Exact scope and review request

The centered W-minimizer existence is the sole named research import. No LAW642/v241/v253, Euclidean original-optimum uniqueness, source-equivalence, first-moment PMLR selector, or unreviewed earlier candidate is a premise. The clipped competitor makes no claim that the ALL-law W optimizer is unique, that H is attained at its proposed law, or that Lambda is a true transition. Request disjoint review of exact Minkowski dilation (4), both cap moments, the signed gap (9), scalar-root interior and asymptotic constants. No parent, human/configured-family/formal/kernel, independent-model or novelty acceptance is claimed.
