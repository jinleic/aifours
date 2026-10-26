# Independent written reconstruction: explicit seven-state PH extension

Before-creation clock observed: **2026-10-23T13:35:44-07:00**. Reviewer: PhysicsResearch96h. No author edit, scientific execution, symbolic algebra engine, coefficient sampling, solver, model CLI or formal proof was performed.

## Snapshot and verdict

Reviewed all 170 lines of `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261023-96h/proof-H12-seven-state-extension-v1.md`, pinned SHA-256 **`59618311924521e8eceaa5179f837589aa2f1cd15955006aace5f39ee559fe4d`**.

**0 FATAL / 0 MAJOR / 0 MINOR. No substantive defect found at the stated parameter and order boundaries.** The explicit seven-state construction, both canceled poles, normalized nonnegative initial row and proper PH generator reconstruct directly. The new band has an upper bound seven, not a proof that the minimum is seven; the manuscript correctly retains the six-or-seven gap.

## 1. Both polynomial factors and the full hand product (lines 29–57)

For x=dX, the real-root cubic is

`(X-13/12)(X+3/4)(X+2/3)`

`=(X-13/12)(X^2+17X/12+1/2)`

`=X^3+X^2/3-149X/144-13/24`.

Since `w=z+1/144`, the repeated complex factor is

`[(X-1/12)^2+z]^2=(X^2-X/6+w)^2`

`=X^4-X^3/3+(1/36+2w)X^2-wX/3+w^2`.

I multiplied these factors coefficient by coefficient. The resulting coefficients from degrees six to zero are:

- X6: `-1/3+1/3=0`;
- X5: `1/36+2w-1/9-149/144=2w-161/144`;
- X4: `-w/3+1/108+2w/3+149/432-13/24=w/3-3/16`;
- X3: `w^2-w/9-149/5184-149w/72+13/72=w^2-157w/72+787/5184`;
- X2: `w^2/3+149w/432-13/864-13w/12=w^2/3-319w/432-13/864`;
- X1: `-149w^2/144+13w/72=w(26-149w)/144`;
- X0: `-13w^2/24`.

These exactly match the manuscript. Multiplication by d7 gives the displayed d powers in f2,...,f7, because the coefficient of x^(7-j) scales as d^j. No finite evaluation is used to establish this polynomial identity.

## 2. Every sign inequality, including its direction (lines 59–95)

The z endpoints translate exactly to `w in [73/144,161/288]`, a subset of [1/2,3/5]. Therefore:

- `2w-161/144<=0`, equality only at the upper endpoint;
- `w/3-3/16<=161/864-162/864=-1/864`;
- because w>=1/2 and the linear coefficient is negative, `-157w/72<=-157/144`; because w<=3/5, `w^2<=9/25`. Hence the cubic coefficient is at most `9/25-157/144+787/5184=-74969/129600<0`;
- `w^2/3<=w/5` follows from w<=3/5 and w>=0, so the quadratic coefficient is at most `(1/5-319/432)w-13/864<0`;
- `26-149w<=26-149/2=-97/2<0`, and w is positive;
- the constant coefficient is strictly negative.

Thus all f_j are nonnegative and f3,...,f7 strictly positive. No sign bound reverses an inequality or substitutes an invalid independent parameter range.

## 3. Companion orientation and complete stable spectrum (lines 97–111)

An upper-shift companion with superdiagonal ones and last row `(f7,f6,f5,f4,f3,f2,0)` has characteristic polynomial `x7-f2x5-f3x4-...-f7`, exactly P7. Subtracting lambda I moves its roots to

`-c`, `-a±ib` each twice, `-u1`, `-u2`.

Indeed `lambda=c+13d/12`, `lambda-d/12=a`, `u1=lambda+3d/4`, `u2=lambda+2d/3`. All real parts are negative. Direct factor substitution, not only a root comparison, gives

`P7(s+lambda)=D5(s)(s+u1)(s+u2)`.

The two hidden real poles are distinct because u1-u2=d/12>0, and both are stable.

## 4. Resolvent and both cancellations (lines 115–135)

Let `r=(sI-G)^(-1)e7` and x=s+lambda. The first six row equations give `r_(i+1)=x r_i`; hence `r_i=x^(i-1)r1`. The final row equation then gives `P7(x)r1=1`. Therefore

`e_i^T(sI-G)^(-1)e7=x^(i-1)/P7(x)`

with the exact orientation stated, not its transpose.

The nonnegative row `v=(d^2/2)e1^T+(17d/12)e2^T+e3^T` supplies numerator `x^2+17dx/12+d^2/2`, which factors as `(x+3d/4)(x+2d/3)`. It therefore cancels exactly `(s+u1)(s+u2)` in the denominator when the output is K e7. Both cancellations use positive row coefficients; no signed initial probability is hidden.

## 5. Positive diagonal normalization, initial probabilities and exits (lines 137–162)

With `h_i=lambda^(i-1)/(u1u2)`, the first six entries of Gh vanish. The last is

`[f7+f6lambda+f5lambda^2+f4lambda^3+f3lambda^4+f2lambda^5-lambda^7]/(u1u2)`

`=-P7(lambda)/(u1u2)=-K`,

because `P7(lambda)=D5(0)u1u2=K u1u2`. Hence `-Gh=K e7` exactly and all h_i are positive.

The diagonal similarity `T=S^-1 G S` has superdiagonal lambda and last-row entries `f7/lambda^6,...,f2/lambda,-lambda`, as displayed. Its first six row sums are zero; its final exit rate is

`lambda-f2/lambda-...-f7/lambda^6=P7(lambda)/lambda^6=K u1u2/lambda^6>0`.

Off-diagonal entries are nonnegative and similarity preserves the Hurwitz spectrum, so T is a proper PH subgenerator.

The row alpha=vS has its three displayed positive entries. Their sum is one because

`lambda^2+17d lambda/12+d^2/2=(lambda+3d/4)(lambda+2d/3)=u1u2`.

Finally the exit column is `S^-1 K e7`, so the exact similarity identity yields

`alpha(sI-T)^(-1)(-T1)=v(sI-G)^(-1)K e7=H(s)`.

Every scaling factor cancels in the correct direction.

## 6. The f2=0 endpoint and claim boundaries

At the upper endpoint, only f2 vanishes. The directed superdiagonal chain 1→2→...→7 remains intact, and f7>0 provides 7→1, so the generator remains irreducible. Its positive exit at state7 and stable spectrum remain valid. Removing the extra 7→6 feedback does not break the construction. No strict f2 positivity was used elsewhere.

The exact new endpoint satisfies53/96>1/2 and beta<1, hence it lies strictly inside the previously reconstructed PH-existence region beta<beta_* with beta_*>1. The explicit construction itself requires no O'Cinneide existence import. Its order-seven upper bound does not exclude an alternative six-state representation; the manuscript correctly reports minimum6 or7 in the new band, relying only on the previously declared full-topology order-five exclusion for the lower side.

This review is ordinary in-harness written checking. It does not establish prior-art priority, human acceptance, a proof-assistant kernel theorem, full minimum order in the residual band, or the broad book problem.
