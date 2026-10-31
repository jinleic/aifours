# Exact privacy-optimum asymptotics at both ends of epsilon

**AUTHOR CANDIDATE — WRITTEN with selected exact rational/polynomial checks; NOT yet independently reviewed or parent-adopted.** Native pre-write clock: `Wed Oct 28 17:18:43 PDT 2026`.

## 1. Exact target and named import boundary

For finite epsilon>0, let F_epsilon be ALL Borel noise laws on R^2 satisfying the epsilon event inequality for EVERY Borel event and EVERY shift in the FULL CLOSED unit l1 diamond. Define

    W(epsilon)=inf_(mu in F_epsilon) E_mu ||X||_1^2,
    V(epsilon)=inf_(mu in F_epsilon) E_mu ||X||_2^2,
    V_rad(epsilon)=inf_(mu in F_epsilon, centered diamond-radial) E_mu ||X||_2^2.

These are squared l1, squared Euclidean, and centered diamond-radial squared Euclidean respectively; none is the PMLR source's FIRST-power l1 objective.

Named same-harness WRITTEN_SUPPORTED inputs:

1. Matching-norm per-cost existence/attainment by a centered staircase for W, at `institute/runs/three-area-2026-10-23-96h/privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA-256 `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`.
2. For every epsilon, `V_rad=(2/3)W` and `W/2<=V<=V_rad`, at `institute/runs/three-area-2026-10-27-96h/dispositions/info-1-angular-cost-and-radial-infimum-parent-v1.md`, SHA-256 `5e8fd8ec0cbd42af73a891acff0d8c0073d38e5e3795f558d401f6e5350374b4`.
3. For `0<epsilon<=epsilon_t`, `V=(2/3)W`, where epsilon_t is the positive threshold, and above it V is strictly smaller, at `institute/runs/three-area-2026-10-23-96h/privacy-v253-MDA-mixed-cost-composition-entire-parent-v1.md`, SHA-256 `a32085f921269874b24821146d7af820451ac48b844288887805c75042e7e71d`, lines 5–18. That result itself imports LAW642, MDA per-cost, NORM148 and separated v241; these assumptions are not new external-source attribution.

The scalar staircase and root calculation are also in my earlier unreviewed `frontier-20261028-squared-l1-unique-angular-rigidity-v1.md`, SHA-256 `2cd41fe9b1503c73b0b9c86d6cb82f64cf2e4bc04123332c6cdb5ba9b72806e5`. This note independently displays the scalar formulas and sign proof needed for VALUE asymptotics; it does NOT require accepting that candidate's all-law uniqueness or angular-preimage claims.

## 2. Main asymptotic conclusions

Let `b=exp(-epsilon)`, `m=b/(1-b)`, and let gamma_*(epsilon) be the unique minimizing centered-staircase offset in (0,1) selected below.

As **epsilon decreases to zero** (high-privacy endpoint, used as a limit, not a finite-epsilon extension):

    gamma_* = (3+sqrt(3))/6 - epsilon/12 + O(epsilon^2),                  (1)
    W(epsilon) = 6/epsilon^2 - (sqrt(3)/36) epsilon + O(epsilon^2),       (2)
    V(epsilon) = 4/epsilon^2 - (sqrt(3)/54) epsilon + O(epsilon^2).       (3)

Equation (3) is for the ORIGINAL full all-law squared-Euclidean optimum, conditional on the named positive-threshold/v253 union. It is not inferred merely from a centered-radial trial law.

As **epsilon tends to infinity**, put `s=m^(1/4)`:

    gamma_* = s + (1/2)s^2 - (5/8)s^3 - (3/2)s^4 + O(s^5),              (4)
    W(epsilon) = s^2 + 2s^3 + (3/2)s^4 - (3/4)s^5 + O(s^6),             (5)
    V_rad(epsilon) = (2/3)s^2 + (4/3)s^3 + s^4 - (1/2)s^5 + O(s^6).     (6)

Equivalently, `W=e^(-epsilon/2)+2e^(-3epsilon/4)+(3/2)e^(-epsilon)-(3/4)e^(-5epsilon/4)+O(e^(-3epsilon/2))`. In this LOW-privacy limit the original Euclidean optimum is NOT asserted equal to V_rad: only

    W/2 <= V < (2/3)W                 once epsilon>epsilon_t.               (7)

Consequently `liminf e^(epsilon/2)V>=1/2` and `limsup e^(epsilon/2)V<=2/3`; no limiting coefficient or rounded-core asymptotic is claimed.

All big-O statements are ordinary real one-sided asymptotics with constants in a sufficiently small endpoint neighborhood, not claims uniform across all epsilon.

## 3. Explicit scalar value and globally correct root

For `0<=gamma<=1`, the normalized centered diamond staircase Q_gamma has radii gamma+i. Set

    A=m+2m^2,
    B=m+6m^2+6m^3,
    C=m+14m^2+36m^3+24m^4,
    D(gamma)=gamma^2+2m gamma+A,
    N(gamma)=gamma^4+4m gamma^3+6A gamma^2+4B gamma+C.

The ball layer formulas `|rD|=2r^2` and `integral_(rD)||x||_1^2 dx=r^4`, and geometric moments, give

    W(Q_gamma)=N(gamma)/(2D(gamma)),      D>0.                            (8)

The matching-norm per-cost input identifies W(epsilon) with the MINIMUM of this actual scalar family. Differentiating gives `W'(gamma)=P_m(gamma)/D(gamma)^2`, where

    P_m(gamma) = gamma^5 + 5m gamma^4 + (2m+12m^2) gamma^3
               + (12m^3-2m) gamma^2
               - m(1+2m)(1+6m) gamma + m^2(1+2m).                     (9)

The descending coefficient signs have exactly two changes after zeros are omitted. `P_m(0)=m^2(1+2m)>0` and `P_m(1)=(1+m)^2(1+2m)>0`. For `gamma_0=2m/(1+4m)`, exact expansion shows

    (1+4m)^5 P_m(gamma_0)
      = -m^2[1+34m+352m^2+1472m^3+2944m^4+2816m^5+1024m^6] < 0.      (10)

Intermediate value plus Descartes gives exactly two distinct simple positive roots, one on either side of gamma_0 and both <1. The cost rises, then falls, then rises. Since Q_0=Q_1 as laws and the cost is strictly lower at the second root than at 1, the second root is the unique global minimizer gamma_* on [0,1]. Thus both endpoint expansions below use the ACTUAL minimizing branch, not an arbitrarily selected stationary point.

## 4. Small-epsilon proof for the original Euclidean value

Set `t=1/m`. Divide (9) by m^3:

    P_m(gamma)/m^3 = F0(gamma) + t F1(gamma)
                     + t^2 F2(gamma) + t^3 gamma^5,
    F0=12gamma^2-12gamma+2,
    F1=12gamma^3-8gamma+1,
    F2=5gamma^4+2gamma^3-2gamma^2-gamma.

The larger root lies above gamma_0, which tends to 1/2. The larger root of F0 is `g=(3+sqrt(3))/6`; the other lies below 1/2. Its derivative `F0'(g)=4sqrt(3)` is nonzero. The implicit function theorem and `g^2=g-1/6` give `F1(g)=2g-1`, hence

    gamma_*=g - 1/(12m) + O(m^(-2)).                                     (11)

The following exact rational decomposition, valid for every m>0 and gamma in [0,1], follows from (8):

    W(Q_gamma)=6m(m+1)+1/2
       + [2m gamma(1-gamma)(1-2gamma) - gamma^2(1-gamma^2)]/[2D(gamma)]. (12)

At gamma=g, `g(1-g)=1/6` and `1-2g=-sqrt(3)/3`. Substitution of (11) into (12) gives

    W=6m(m+1)+1/2 - sqrt(3)/(36m) + O(m^(-2)).                         (13)

The correction caused by replacing g with gamma_* contributes only O(m^-2), as does the constant numerator in (12). Since

    m(m+1) = 1/[4 sinh^2(epsilon/2)],   1/m=e^epsilon-1,
    6m(m+1)+1/2 = 6/epsilon^2 + O(epsilon^2),

(13) proves (2), and (11) proves (1). The separated v241 threshold is strictly positive; hence for all sufficiently small positive epsilon the v253 equality `V=(2/3)W` applies, proving (3). This last transfer is explicitly conditional on the full adopted mixed-cost union, not a consequence of the PMLR mean-norm theorem.

## 5. Large-epsilon proof for W and the radial comparison only

Put `m=s^4` and `gamma=s z`. The root equation (9), divided by s^5, is analytic near (s,z)=(0,1) and starts

    z^5-z - 2s z^2 + 2s^2 z^3 + s^3(5z^4+1) + O(s^4)=0.              (14)

For any fixed `0<a<1<c`, P_m(as)<0 and P_m(cs)>0 for sufficiently small s. Also gamma_0=O(s^4)<as, so the globally minimizing SECOND root lies in (as,cs). Therefore gamma_*/s ->1. Since the derivative of z^5-z at z=1 is 4, the implicit function theorem gives a unique analytic nearby branch. Coefficient matching in (14) yields

    z=1+(1/2)s-(5/8)s^2-(3/2)s^3+O(s^4),

which is (4). Substitute into (8) and divide by the positive denominator to get (5); the exact polynomial checks below independently verify the required finite coefficients. The all-epsilon radial identity then proves (6). Because epsilon is above the positive threshold eventually, (7) follows from the separately adopted mixed-cost union. It is intentionally only a TWO-SIDED BOUND for the original V, not the false inference that its rounded optimum is the radial staircase.

## 6. Actual exact arithmetic and one falsified tempting bound

The previous root candidate's integer-polynomial cell independently checked `N' D-N D'=2P`, P's endpoint coefficient lists and all-negative coefficients in (10). In this work a second bivariate integer/rational-polynomial cell checked the exact high-privacy identity (12): actual output was

```text
exact high-privacy rational decomposition verified: True
R(m,g) terms (m_degree,gamma_degree)->coefficient: [((0, 2), -1), ((0, 4), 1), ((1, 1), 2), ((1, 2), -6), ((1, 3), 4)]
```

A separate univariate `fractions.Fraction` polynomial substitution checked the low-privacy coefficients without numerical fitting. With `m=s^4` and `gamma_4=s+s^2/2-5s^3/8-3s^4/2`, actual output was

```text
P(s4, four-term gamma) coefficients s0..s8 all zero: True
N−2D*(s²+2s³+3s⁴/2−3s⁵/4) coefficients s0..s7 all zero: True
```

The implicit-function/branch selection is the written argument in §5, not a consequence of these finite coefficient checks.

Finally, this is the actual bounded rational ROOT-BRACKETING cell. It brackets the second positive root because the endpoint P signs, uniqueness argument in §3 and bisection all apply. It uses no floats and makes no claim about a named source or formal proof.

```python
from fractions import Fraction as F

def Pq(m,g):
 return g**5+5*m*g**4+(2*m+12*m*m)*g**3+(12*m**3-2*m)*g**2-m*(1+2*m)*(1+6*m)*g+m*m*(1+2*m)
def Wq(m,g):
 A=m+2*m*m; B=m+6*m*m+6*m**3; C=m+14*m*m+36*m**3+24*m**4
 return (g**4+4*m*g**3+6*A*g*g+4*B*g+C)/(2*(g*g+2*m*g+A))
def root_bracket(m,lo,hi,steps=30):
 assert Pq(m,lo)<0<Pq(m,hi)
 for _ in range(steps):
  mid=(lo+hi)/2
  if Pq(m,mid)<0: lo=mid
  else: hi=mid
 return lo,hi
m=F(1000); lo,hi=root_bracket(m,F(1,2),F(1)); mid=(lo+hi)/2
scaled=m*(Wq(m,mid)-(6*m*(m+1)+F(1,2)))
print('high-m=1000: exact gamma bracket=',lo,hi)
print('scaled correction in (-1/20,-1/25):',-F(1,20)<scaled<-F(1,25))
m=F(1,100_000_000); s=F(1,100); lo,hi=root_bracket(m,s/2,2*s); mid=(lo+hi)/2
pred=s+s*s/F(2)-F(5,8)*s**3
print('low-m=1/100000000: exact gamma bracket=',lo,hi)
print('gamma midpoint within s^4 of 3-term asymptotic:',abs(mid-pred)<s**4)
W=Wq(m,mid); approximation=s*s+2*s**3+F(3,2)*s**4
print('squared-l1 midpoint-cost within s^5 of 3-term asymptotic:',abs(W-approximation)<s**5)
print('low-branch endpoint bracket proves |gamma*-approx|>s^4:',max(lo,hi)<pred-s**4)
print('and proves |gamma*-approx|<10*s^4:',pred-10*s**4<lo and hi<pred+10*s**4)
print('signs P(low)<0<P(high):',Pq(m,lo)<0<Pq(m,hi))
```

Actual observed output (the last three lines were executed in the immediately subsequent cell using the retained low-branch variables):

```text
high-m=1000: exact gamma bracket= 846744035/1073741824 1693488071/2147483648
scaled correction in (-1/20,-1/25): True
low-m=1/100000000: exact gamma bracket= 215808367/21474836480 2158083673/214748364800
gamma midpoint within s^4 of 3-term asymptotic: False
squared-l1 midpoint-cost within s^5 of 3-term asymptotic: True
low-branch endpoint bracket proves |gamma*-approx|>s^4: True
and proves |gamma*-approx|<10*s^4: True
signs P(low)<0<P(high): True True
```

The tempting sharper inequality `|gamma_*-(s+s^2/2-5s^3/8)|<s^4` is therefore **false at this exact selected m**, not merely unverified. The actual fourth coefficient −3/2 also explains why coefficient 1 cannot work uniformly near s=0. The valid asymptotic claim is (4) with its explicit fourth term and an O(s^5) remainder. The midpoint value checks do not independently certify optimum W to a precision beyond the root bracket; they are diagnostics, not the proof.

## 7. Assurance and exact residual

This is a conditional, unreviewed asymptotic candidate at the cited prior source/theorem boundaries. The LOW-privacy original Euclidean rounded-core coefficient remains unpaid; inequalities (7) are not promoted to an equality or limit. The work does not solve nonadditive privacy, prove the complete LAW642 foundations anew, determine publication priority/novelty, or repair any historically held input. No independent model/human/formal/kernel/full-proof executable gate has been performed. Request disjoint review of scalar branch, implicit-function orders, exact cancellations and especially the v253 transfer before adoption.
