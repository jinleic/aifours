# Addendum 1: the downstream two-cycle family is excluded at 8/9 for EVERY u>0

Actual `/bin/date` observation before this write: **Sun Oct 25 23:48:29 PDT 2026**. MathResearch96h-2. AUTHOR-WRITTEN CANDIDATE; no machine/scientific check. Base manuscript SHA256 `10ef27dffb680402d830faa6fcbe3a36a9e1a815caa0269616407683dd21d124` is unchanged. All process findings and ZERO-credit quarantines remain.

## 1. New statement and retained actual matrix

The base manuscript excludes u>=1 in its actual 3+1+3 matrix with ALL fifteen through-middle feedback entries and the additional downstream two-cycle sigma>=0. This addendum covers the previously open 0<u<1 case, without extrapolating its six-ray cone to negative delta.

A stronger statement holds on this side: **if 0<u<1, the actual common-matrix system has no PH realization whenever z+sigma/2>=1/2**, provided the actual initial row is nonnegative. Consequently the entire stated topology is excluded at z=8/9 for ALL u>0.

This remains a restricted actual topology/holding theorem, not an unrestricted PH7 point decision.

## 2. Two necessary high functionals, valid for every sigma>=0

Use the SAME A,F,r,f,D, beta and gamma as in the base manuscript. Put

    x=y+u,       a=1−u in (0,1),
    B=p−2u>=0,  C=Q(−u)>=0,
    Z=z+sigma/2.

The inequalities B,C>=0 are the actual initial-row conditions in (NUM), not freely imposed polynomial signs. Trace gives w=B+a. The unchanged characteristic identity reads

    R=(y+w)x^3[(x+a)^3−sigma(x+a)]−D_z Q
      =a_S r^T(1,x,x^2)^T+x^3 U f+U D(1,x,x^2)^T,

where U=((x+a)^2−sigma,x+a,1), a_S=(x+a)^3−sigma(x+a), Q=x^2+Bx+C.

Define

    J5=[x^5]R,
    J4=[x^4]R−2a[x^5]R.

These are nonnegative on ALL actual generators for every sigma>=0, even when sigma>a^2 and some lower coefficients are negative. In fact their values follow directly from the five generators of degree at least four:

| actual generator | J5 | J4 |
|---|---:|---:|
| x^2 a_S (r3) | 1 | a |
| x^3((x+a)^2−sigma) (f1) | 1 | 0 |
| x a_S (r2) | 0 | 1 |
| x^3(x+a) (f2) | 0 | 1 |
| x^2((x+a)^2−sigma) (D13) | 0 | 1 |

Each of the other ten generators has degree at most three and gives zero in both columns. Therefore the SAME actual matrix has

    J5=r3+f1>=0,
    J4=a r3+r2+f2+D13>=0.                            (N)

No claim about the whole low-degree cone is needed.

## 3. Exact visible-parameter shift in these two constraints

Expanding the left side of R at x=y+u, with the actual trace tie w=B+a, gives

    J5=(1−2a)B−C+a−a^2−2Z,
    J4=(−3a^2+2a−2Z)B+(1−3a)C
                         +a^2−a^3+2Z(1−a).          (H)

One way to see the sigma terms without dropping cycle products is to subtract exactly

    sigma x^3(x+B+2a−1)(x+a)

from the no-sigma residual. It subtracts sigma from the degree-five coefficient and sigma(B+3a−1) from degree four. Thus it subtracts sigma(B+a−1) from J4, which is precisely the change z→z+sigma/2 in (H).

Equations (N),(H) are valid for the full feedback matrix; no lower feedback generator or disjoint-cycle term has been replaced by a free sign assumption.

## 4. A single positive polynomial closes all 0<a<1

Suppose Z>=1/2. Write h=a(1−a), so 0<h<=1/4.

If a>=1/2, B,C>=0 make J5<=h−2Z<=1/4−1<0, contradicting (N).

Now 0<a<1/2. Put D0=1−2a>0. J5>=0 and C>=0 force

    B >= (2Z−h)/D0.                                 (L)

### Case 1: 0<a<=1/3

Here E=1−3a>=0. From J4+E J5>=0 obtain

    H0 B <= U0,
    H0=2Z−1+3h>0,
    U0=h D0+4aZ.

Compatibility with (L) would require

    (2Z−h)H0−U0 D0 <=0.

But exact multiplication gives

    (2Z−h)H0−U0 D0
      =2Z(2Z−1)+4Za^2+a^2(1−a)^2 >0.               (P)

The strict sign includes Z=1/2 because a>0.

### Case 2: 1/3<a<1/2

Here the C coefficient in J4 is negative. Dropping that NONPOSITIVE term yields the necessary upper bound

    V0 B <= W0,
    V0=2Z+3a^2−2a>0,
    W0=(1−a)(a^2+2Z).

For V0>0, use 3a^2−2a=3(a−1/3)^2−1/3 and 2Z>=1. Compatibility with (L) requires

    (2Z−h)V0−W0 D0<=0.

The left side is EXACTLY the SAME polynomial (P), hence strictly positive. Contradiction.

All 0<a<1 are covered. Thus every 0<u<1 member of this actual topology must have z+sigma/2<1/2. In particular none can attain z=8/9.

## 5. Whole-topology conclusion and precise nonclaim

Combining this proof with the base manuscript's u>=1 proof excludes the ENTIRE family with holdings (u,u,u,w,1,1,1), arbitrary u,w>0, all fifteen through-middle backward entries, and the additional downstream two-cycle sigma>=0, at z=8/9. All actual numerator, characteristic and conditional PH normalization ties are retained.

This also strengthens the earlier no-sigma u<1 argument (`PH7-band-closure-through-mid-cycles-addendum-3.md`, SHA256 `343d99a03c17c103ff104c264efe2876f671aab353fa7169314abeef724a193b`): the exact obstruction there already follows at z>=1/2 from (P), without the earlier split-range numerical-looking margins. Its frozen source is not edited, and no older review is claimed to cover this stronger proof.

Arbitrary unequal block holdings, additional off-middle cycles, different principal/input/exit arrangements and both unrestricted dominator strata remain. No PH7 witness, full empty-intersection certificate or minimum-eight claim is supplied. The original unrestricted 8/9 verdict stays NOT_PROVED/minimum {7,8}; no formal/kernel/configured-family/human/executable/novelty gate, new GO, clean-process assertion or deadline change follows.
