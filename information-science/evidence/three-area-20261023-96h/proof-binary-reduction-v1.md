# Exact symbolic recovery of the seven-piece binary bounds

**Status: CANDIDATE / written derivation only.** Companion to `proof-bounded-outcome-sharp-bounds-v1.md`. No solver, enumeration or numerical check was used. This is a self-contained algebraic reduction of that manuscript's formulas to the existing Yin–Liu–Geng–Luo binary theorem, not a new binary result and not dependent on importing the source's sharpness assertion.

## 1. Binary data and the scalar formula

Let

    a=P(S_0=0,Y_0=1),  b=P(S_0=1,Y_1=1),
    c=P(S_0=0,Y_0=0),  d=P(S_0=1,Y_1=0),

with a,b,c,d>=0 and a+b+c+d=1. Let q=P(S_1=1), h=q-b-d and eta=gamma+a+d. Compatibility is 0<=eta<=1.

The main theorem gives

    I=[l,u]=[max(0,h), min(a+c,q)],
    t=r-h,
    L=min_(r in I) F(r),

where

    F(r)=(r-h-eta)_+ +(r+eta-1)_+
         -min(r,a)-min(r-h,b).

Since -min(x,k)=-x+(x-k)_+, this is

    F(r)=sum_(j=1)^4 (r-beta_j)_+ -2r+h,                   (1)

with

    beta_1=h+eta,
    beta_2=1-eta,
    beta_3=a,
    beta_4=h+b=q-d.                                       (2)

All identities are valid at zero cells, q=0, q=1 and compatibility endpoints.

## 2. Unconstrained minimum of the four hinges

Order the four numbers as beta_(1)<=beta_(2)<=beta_(3)<=beta_(4), with repetitions allowed. The slopes of (1), away from breakpoints, are -2,-1,0,1,2. Therefore the full unconstrained minimizer set is

    M=[beta_(2),beta_(3)],

and its minimum is

    M_0=h-beta_(1)-beta_(2)
       =max_(i<j) [h-beta_i-beta_j].                      (3)

Evaluating the six pairs in their original indices gives

    pair 12: -1,
    pair 13: -gamma-2a-d,
    pair 14: -gamma-q-a,
    pair 23: gamma+q-b-1,
    pair 24: gamma-2b-c,
    pair 34: -a-b.                                        (4)

The term -1 is redundant because -a-b>=-1. Thus (3) is the maximum of five of the seven published lower-bound expressions.

## 3. The lower endpoint of I never cuts off all unconstrained minimizers

Compatibility gives beta_1=h+eta>=h and beta_4=h+b>=h. Hence at least two beta values are >=h, so beta_(3)>=h.

Likewise beta_2=1-eta>=0 and beta_3=a>=0 give beta_(3)>=0. Thus

    beta_(3)>=max(0,h)=l.                                 (5)

Consequently M can fail to intersect I only by lying **above** u, that is beta_(2)>u. There is no omitted lower-end clipping case.

## 4. The only possible clipping values

If M intersects I, the constrained minimum equals M_0.

Suppose instead beta_(2)>u. Then exactly one beta is <=u, because at least one of the following anchors is <=u in the applicable case.

- If u=a+c<=q, then beta_3=a<=u. Every other beta must be >u, so (1) gives

      F(u)=h-2u+(u-a)=h-u-a=q-1-a.                       (6)

- If u=q<=a+c, then beta_4=q-d<=u. Every other beta must be >u, giving

      F(u)=h-2u+(u-beta_4)=-b-q.                        (7)

If a+c=q, both anchors are <=u, so beta_(2)>u is impossible. Therefore the apparent equality overlap in the two cases creates no missing case.

Since (1) is nonincreasing below beta_(2), u is the constrained minimizer in the clipped case. Equations (6)–(7) enumerate every possible extra minimum value.

To obtain one global maximum formula, also observe that both clipping expressions are lower bounds for every feasible r. Indeed,

    F(r)>=-min(r,a)-min(t,b)>=-a-t>=-a-(1-q),

because r<=a+c implies t=r-q+b+d<=1-q. Similarly

    F(r)>=-r-b>=-q-b.

Also F(r)>=M_0 by definition. If M intersects I, all these lower bounds are <=M_0. If it does not, one of the two clipping expressions equals the actual minimum. Hence, in all cases,

    L=max {
      -a-(1-q),
      -a-b,
      -b-q,
      -gamma-q-a,
      -gamma-d-2a,
       gamma-2b-c,
       gamma-(1-q)-b
    }.                                                    (8)

This proves the lower expression exactly, including every boundary.

## 5. Upper bound by outcome complementation

Transform each potential outcome by Y_s'=1-Y_s. The factual binary cells become

    (a',b',c',d')=(c,d,a,b),

while q is unchanged, gamma'=-gamma and delta'=-delta. This is an invertible transformation of the entire compatible-law set, not just an inequality. Therefore

    U(a,b,c,d,q,gamma)=-L(c,d,a,b,q,-gamma).

Applying (8) gives

    U=min {
      c+(1-q),
      c+d,
      d+q,
      gamma+a+2d,
      gamma+d+(1-q),
      -gamma+2c+b,
      -gamma+c+q
    }.                                                    (9)

The order of the expressions is arranged to match the primary source's displayed order.

## 6. Matched primary-source comparison

The actual retained source is `sources/yin-1607.05454v1.txt`, lines 589–632. Its Theorem 1 uses exactly the control joint binary cell probabilities, the treated surrogate marginal q and gamma=ACE(S->Y), under randomized treatment and strong surrogacy. Equations (8) and (9) are its seven lower and seven upper terms after substituting the above a,b,c,d notation.

The main manuscript independently proves that the scalar formulas identify and attain the whole compatible interval. This companion independently proves that those formulas reduce **algebraically** to the prior binary endpoints. No appeal to uniqueness of a source-imported sharp interval is now necessary for the reduction, and no finite LP check is being represented as performed.

**Claim boundary:** all-binary sharp bounds are prior art. The new candidate's proposed delta lies in the arbitrary bounded-real factual outcome laws and the constructive quantile criterion, not in (8)–(9).
