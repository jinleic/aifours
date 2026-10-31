# Null erosion alone does not suffice without regular-closed core

**AUTHOR CANDIDATE — WRITTEN, with a bounded exact rational geometric check; NOT independently reviewed or parent-adopted.** Native pre-write clock `Wed Oct 28 18:32:31 PDT 2026`.

## 1. What is falsified

My preceding UNREVIEWED `frontier-20261028-nonconvex-erosion-tv-criterion-v1.md`, SHA `6aecba0e2d05a565d6ae753498df55e80db0a949ce7f2eff618a11ad984dfea6`, explicitly assumes `S=closure(int S)` and null boundary. The following actual FULL-private construction shows that its regular-closedness hypothesis cannot simply be dropped, even if S is compact, has nonempty interior, has null boundary and its core erosion `S minus-D={x:x+D subset S}` is EMPTY.

At exact epsilon=log2, there is such an S and a sequence of exact-epsilon laws mu_n satisfying EVERY Borel-event inequality for EVERY h in the FULL CLOSED unit l1 diamond D, such that

    mu_n => Q_S weakly,        TV(mu_n,Q_S) -> 1/(96pi Z_S) > 0.         (1)

Here `Q_S` is the canonical geometric-shell law `q_S=Z_S^(-1)2^(-n_S)`, `n_S=min{k:x in S+kD}` and `0<Z_S<infinity`. This is NOT a counterexample to the earlier theorem, which retains its regular-closedness assumption, or to the original Euclidean optimizer stability. It is a precise falsification of the overgeneralized *null-erosion-only* proposition.

## 2. Explicit core, empty erosion and the hidden first-shell region

Take

    c1=(1/2,0), c2=(-1/2,0), c3=(0,1/2), c4=(0,-1/2),
    C={c1,c2,c3,c4},
    S=C union B_2((10,0),1/4),
    D={x:||x||_1<=1},       A=(1/4)D.

Here B_2((10,0),1/4) is the CLOSED Euclidean disk. S is compact, has nonempty interior, and its boundary is the circle of that disk plus four isolated points, hence has area 0. It is NOT the closure of its interior: the four isolated points are missing from that closure.

The erosion is empty. Any translate of the connected diamond D contained in S must lie inside a single separated connected component; each component is either one point or a disk of Euclidean diameter 1/2, whereas D has diameter 2. Therefore no x+D is contained in S.

Nevertheless the first dilation K1=S+D has a positive-volume shield at the origin. For EVERY y in D, choose a center c in C along a coordinate of maximal absolute value and with the same sign. If that maximum is at least 1/2 then `||y-c||_1=||y||_1-1/2<=1/2`; otherwise `||y-c||_1=1/2+||y||_1-2 max_i|y_i|<=1/2`. Thus

    D subset C+(1/2)D,      (3/2)D subset C+D subset K1.                 (2)

Consequently `A+D=(5/4)D` is contained in int K1. A is disjoint from S, but A+D can meet the four isolated points of S. Their zero area is the decisive nonregularity: they generate positive-area shell geometry while contributing no positive-area top-core neighbor.

## 3. A pointwise-private representative at the isolated points

Set b=1/2 and `q_S(x)=Z_S^(-1)b^(n_S(x))`. The compact-core argument gives a finite positive normalizer and full-D privacy. On the FOUR isolated points c_i its canonical value is 1/Z_S, but changing values at these four points leaves the probability law unchanged. Define a representative

    q_tilde(c_i)=b/Z_S,       q_tilde(x)=q_S(x) otherwise.

This modified representative STILL satisfies the privacy inequality pointwise for every h in D. If neither member of a pair (x,y), ||x-y||_1<=1, is one of the c_i, this is the original q_S inequality. If one point is c_i, both lie in `(3/2)D subset K1`, far from the remote disk. Every point there has density b/Z_S under q_tilde: outside C it is in K1 but not S, and the four C-values were changed to b/Z_S. Thus the ratio is 1. This pays the delicate h-dependent null-set issue explicitly, not merely almost-everywhere for a selected shift.

## 4. Perturb only the protected first-level region

Let `psi=1_A` and a=1/6. For every integer n>=1 set

    p_n(x)=q_tilde(x)[1+a psi(x) sin(2pi n x1)].                         (3)

On A+D=(5/4)D, q_tilde is identically b/Z_S. If either x or y at l1 distance<=1 belongs to A, both lie in this first-level region, and their perturbed density ratio is at most

    (1+a)/(1-a)=7/5 <2=e^epsilon.

If neither belongs to A, the q_tilde pointwise privacy inequality is unchanged. Therefore p_n is pointwise private for ALL closed-D shifts, and every Borel event satisfies epsilon=log2 privacy. It is strictly positive.

The integral is exactly 1: the perturbation is supported on the centrally symmetric A, q_tilde is constant there and sin(2pi n x1) is odd. The far positive-quadrant e1-shift event is unaffected and attains ratio 2, so the ACTUAL privacy parameter is exactly log2.

Riemann–Lebesgue gives p_n dx=>Q_S weakly, while periodic averaging gives

    TV(p_n dx,Q_S)
      =(a b/(2Z_S)) integral_A |sin(2pi n x1)|dx
      -> a b |A|/(pi Z_S)=1/(96pi Z_S)>0,

because `|A|=2(1/4)^2=1/8`. Thus (1) holds. The perturbation lives in a positive-area plateau with no positive-area top-level neighbor, not in the null isolated points themselves.

## 5. Exact bounded geometric control

The proof of the nearest-center bound in §2 is universal. A supplementary Fraction enumeration of the 841 rational grid points of D at spacing 1/20 gave:

```text
rational-grid D points= 841 maximum nearest-center l1 distance= 1/2
A_area= 1/8 privacy_ratio= 7/5 TV_limit_coefficient_times_Z_pi= 1/96
```

This selected finite grid is a diagnostic, not the all-point covering proof. Z_S is left as the actual positive normalization integral; no guessed numeric value or executable optimization is claimed.

## 6. Exact boundary and review request

The mechanism has an ACTUAL regularity failure: isolated zero-area core points create a thick K1 shield, so examining only the erosion of S misses a positive-area interior of a later plateau's erosion. The prior nonconvex iff remains claimed only for regular-closed, null-boundary S; this example does not contradict it. Neither this note nor its proof imports LAW642, f68, MDA or a named-publication proof, and it does not identify the original optimal law.

Request disjoint review of the set covering, four-point density-version modification, all-pairs privacy, exact budget event and TV limit before any adoption. No formal/kernel/human/configured-family, priority or novelty acceptance is claimed. Historical held results are not premises.
