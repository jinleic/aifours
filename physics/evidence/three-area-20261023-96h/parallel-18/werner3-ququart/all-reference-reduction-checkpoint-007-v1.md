# All-reference obligation — every three-dimensional principal minor of the four-block is PSD

Before-creation clock observed: **2026-10-23T17:12:32-07:00**. PhysicsResearch96h. New unreviewed written proof, no scientific program/CAS/root search/sampling. This closes the generic four-block's third leading-minor obligation by hand, but **NOT its full determinant** and therefore not the full four-block upper sign or all-reference target.

The proposed coefficient program remains unexecuted by this owner and has no received fresh GO. Its preregistered source is unchanged. A negative coefficient, even for the now-hand-proved lower minors, would remain only failure of that coefficient ansatz, not a route failure.

## 1. The representative three-dimensional form

Use the generic four-block matrix M=C4-S4 from checkpoint001. One principal triple has the form

`M3=[[1,alpha,-u],[alpha,1,-v],[-u,-v,1]]`,

where, in normalized probabilities A+B+C+D=1,

`u=1/2+A/[2(2-A-B)]`,

`v=1/2+D/[2(2-C-D)]`,

`alpha=1/4+E_AC`.

Every other principal triple is obtained by relabeling the probabilities and its coordinate vectors. Its determinant is

`F(u,v,alpha)=1-u^2-v^2-alpha^2+2alpha u v`.

The two-dimensional principal minors are already nonnegative, since all off-diagonal magnitudes are at most1. We prove F>=0 on the entire physical parameter domain, strict in the all-positive interior.

## 2. Actual coupled edge domain

Put p=2u-1 and q=2v-1. Then p,q>=0, and with T=A+B,

`A=p(2-T)`, `D=q(1+T)`.

The remaining probabilities are nonnegative only if

`T>=2p/(1+p)`, `T<=(1-q)/(1+q)`.

Consequently

**`p+q+3pq<=1`.**

In particular1/2<=u,v<=1 and u+v<=3/2. If w=max(u,v), the other variable lies between1/2 and

`min(w,w/(3w-1))`.

This coupled domain, not an independent square in u,v, is used below.

Checkpoint006 gave alpha>=1/3; checkpoint001 gave alpha<=1/2. We next prove an additional universal lower bound that becomes relevant near a concentrated reference.

## 3. Universal lower correlation bound

The sharper bound is

**`alpha>=max(1/3,3u/2-1,3v/2-1)`.**

To prove the u part, work homogeneously with nonnegative formal probabilities A,B,C,D and S=A+B+C+D. Define

`W3=S^3+2S e2-e3`, `Dab=2S-A-B`,

`H=S[2S^2+(A+C)(B+D)]`.

Then alpha=H/(4W3), while `3u/2-1=(4A+B-2S)/(4Dab)`. Both denominators are positive for S>0. It suffices to prove the quartic

`P=Dab H-W3(4A+B-2S)>=0`.

Here is an explicit nonnegative expansion. Put

`t=B+C+D`, `q=B+2C+2D`, `h=B+D`,

`m=BC+BD+CD`, `n=BCD`.

Then

`P=A^3(2C+3D)+A^2 R2+A R1+q[3t^3+t C h+2t m-n]`,

where

`R2=9B^2+18C^2+21D^2+27BC+28BD+38CD`,

`R1=t C h+2n+q[(t+C)h+m]`

`   +t[11B^2+22C^2+22D^2+29BC+29BD+40CD]`.

Every coefficient is nonnegative. In the last bracket, `3t^3-n` still has nonnegative coefficients: its BCD coefficient is18-1=17, and all other monomials are unchanged positive terms. The expansion follows by multiplying the displayed homogeneous polynomials; it is not an interpolation or sign assumption.

This proves alpha>=3u/2-1. Relabeling(A,B,C,D) to(D,C,B,A) preserves the complementary partition defining alpha and swaps u with v, so the v bound follows as well. No Schmidt coefficient equality is imposed.

## 4. Reduction to endpoints of a concave correlation interval

At fixed u,v, F is concave in alpha. It therefore suffices to check

`alpha=1/2` and `alpha=ell(w)=max(1/3,3w/2-1)`.

For alpha=1/2,

`F=3/4-u^2-v^2+uv>=0`.

Indeed write u=1/2+r, v=1/2+s, r,s>=0, r+s<=1/2. Then

`u^2+v^2-uv=1/4+(r+s)/2+(r+s)^2-3rs<=3/4`.

The remaining endpoint has two branches. For either branch, F is also concave in the smaller edge variable v, with w fixed. Thus only v=1/2 and the physical maximum from Section2 need be checked. This endpoint reduction uses the actual domain and does not assume that every value between the original probabilities is physically attained; checking the larger enclosing interval is sufficient.

## 5. Branch w<=8/9: ell=1/3

At v=1/2,

`F=23/36+w/3-w^2>=47/324>0`,

because this expression decreases for w>=1/2 and the endpoint is w=8/9.

If w<=2/3, the other endpoint is v=w, giving

`F=8/9-(4/3)w^2>=8/27>0`.

If2/3<=w<=8/9, the other endpoint is v=w/(3w-1). After multiplying by the positive denominator,

`9(3w-1)^2 F=N(w)`,

`N(w)=-81w^4+72w^3+48w^2-48w+8`.

Put `w=2/3+2s/9`, 0<=s<=1. Exact expansion gives

`N=8/3+(32/9)s-(32/27)s^2-(128/81)s^3-(16/81)s^4`.

Since s^k<=s for k>=2 and all those coefficients are negative,

`N>=8/3+(16/27)s>0`.

This proves the whole first branch with no numerical root or matrix check.

## 6. Branch w>=8/9: ell=3w/2-1

At v=1/2, exact factorization gives

`F=(1-w)(7w-1)/4>=0`.

At v=w/(3w-1), it gives

`F=3w(1-w)(27w^2-23w+4)/[4(3w-1)^2]>=0`.

The last quadratic is increasing on[8/9,1] and at8/9 is44/9>0. Thus both endpoints are nonnegative, and they are strictly positive if w<1. Concavity in v and then in alpha proves F>=0 throughout this branch.

## 7. Consequence and exact remaining four-block burden

Every principal3x3 submatrix of the generic four-dimensional upper form is PSD. Its third leading determinant is strictly positive when all reference probabilities are positive, because w<1 there and the endpoint bounds above are strict. Boundary nonnegativity follows directly from the same inequalities or physical continuity.

Together with checkpoint006, the first THREE leading principal minors of M are now universally controlled in written algebra. **The full fourth determinant is still unproved.** PSD of all principal triples does not imply PSD of a4x4 matrix, so this result is not promoted to a full four-block result.

The complete all-reference frontier is now:

- full determinant of the generic4x4 upper form (its lower sign is conditional on that upper proof);
- both seven-dimensional residuals from the nonzero12-weight forms;
- both zero-charge12-dimensional residuals.

No exact failure of the sufficient route has been found. The full all-reference target and unrestricted W4 remain NOT PROVED. All zero/repeated Schmidt coefficients remain part of the target; no small-region substitute or numerical evidence is used as a universal premise.
