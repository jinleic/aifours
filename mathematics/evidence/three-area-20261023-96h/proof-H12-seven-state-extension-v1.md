# H_{1,2}: an explicit seven-state extension beyond the verified six-state band

Before-creation clock observed: **2026-10-23T13:24:38-07:00**. Status: **CANDIDATE / NOVELTY_UNCLEAR**, not yet parent/peer accepted. This selects the parent's next-phase option(a): an actual higher-order construction on a new subrange of the SAME frozen H_{1,2} target. No program, symbolic algebra engine, solver, enumeration or scientific replay was executed. The polynomial search/derivation below was written reasoning, not a blind preregistration.

## 1. Exact statement and remaining lower-bound gap

Let a>c>0,b>0,d=a-c and beta=b/d. Put

    H(s)=K/D_5(s),
    K=c(a^2+b^2)^2,
    D_5(s)=(s+c)((s+a)^2+b^2)^2.

**Candidate theorem G7.** Whenever

    1/2 <= beta^2 <= 53/96,

H has the explicit seven-state PH representation in §4. In particular, it extends the previously written-checked order6 upper bound from beta<=1/sqrt2 to beta<=sqrt(53/96), an interval with strictly larger endpoint.

For

    1/sqrt2 < beta <= sqrt(53/96),

the current full-topology lower bound only excludes order5 or lower. Thus the minimum is **6 or7**, not proved to be7. No universal six-state impossibility is inferred from the old six-state companion's sign failure. The exact minimum-order band remains a live obligation.

The construction introduces two canceled real poles and positive weights on the first three chain states. This is not a numerical optimization or the earlier single-extra-pole construction with its negative coefficient ignored.

## 2. Fixed shifted spectrum and exact polynomial

Set

    z=b^2/d^2,
    w=z+1/144,
    lambda=a+d/12=c+13d/12,
    u_1=c+11d/6=lambda+3d/4,
    u_2=c+7d/4=lambda+2d/3.

Consider the monic degree7 polynomial

    P_7(x)=(x-13d/12)(x+3d/4)(x+2d/3)
            ·[(x-d/12)^2+b^2]^2.

Under x=dX this is d^7 p_w(X), where

    p_w(X)=(X^3+X^2/3-149X/144-13/24)
            ·(X^4-X^3/3+(1/36+2w)X^2-wX/3+w^2).

The two factors follow by ordinary multiplication of the displayed cubic and squared quadratic. Multiplying them gives exactly

    p_w(X)=X^7
       +(2w-161/144)X^5
       +(w/3-3/16)X^4
       +(w^2-157w/72+787/5184)X^3
       +(w^2/3-319w/432-13/864)X^2
       +[w(26-149w)/144]X
       -(13/24)w^2.

The X^6 coefficient is zero. Every rational coefficient is explicit and can be checked by hand independently; no sampled coefficient values are proof premises.

## 3. All feedback coefficients are nonnegative on the full stated interval

For z in[1/2,53/96],

    73/144 <= w <= 161/288,

which is a subset of[1/2,3/5]. The nonleading coefficients of p_w are nonpositive:

* X^5: 2w-161/144<=0, with equality at the upper z endpoint.
* X^4: w/3-3/16<=161/864-162/864=-1/864<0.
* X^3, using w in[1/2,3/5]:

      w^2-157w/72+787/5184
        <=9/25-157/144+787/5184
        =-74969/129600<0.

* X^2: w^2/3<=w/5, so its coefficient is at most

      (1/5-319/432)w-13/864<0.

* X: 26-149w<=26-149/2=-97/2<0.
* Constant: -(13/24)w^2<0.

Write therefore

    P_7(x)=x^7-f_2 x^5-f_3 x^4-f_4 x^3-f_5 x^2-f_6 x-f_7,

with

    f_2=d^2(161/144-2w),
    f_3=d^3(3/16-w/3),
    f_4=d^4(-w^2+157w/72-787/5184),
    f_5=d^5(-w^2/3+319w/432+13/864),
    f_6=d^6 w(149w-26)/144,
    f_7=d^7(13/24)w^2.

All f_j>=0, and f_3,...,f_7 are strictly positive. In particular the endpoint zero f_2=0 is harmless; the generator is still a valid irreducible chain-with-feedback matrix.

Let C_7 be the upper-shift companion matrix with ones on the superdiagonal and final row

    (f_7,f_6,f_5,f_4,f_3,f_2,0).

It is entrywise nonnegative and has characteristic polynomial P_7. Set G=C_7-lambda I. Its eigenvalues are

    -c,
    -a+ib twice, -a-ib twice,
    -u_1, -u_2.

All have negative real part. Thus G is Metzler and Hurwitz. Its determinant is exactly

    det(sI-G)=P_7(s+lambda)=D_5(s)(s+u_1)(s+u_2).

This treats the repeated nonreal eigenvalues and both hidden real eigenvalues explicitly.

## 4. Actual PH parameters, positive normalization and both cancellations

For the companion equations,

    e_i^T(sI-G)^(-1)e_7=(s+lambda)^(i-1)/P_7(s+lambda),
    i=1,...,7.

Use the nonnegative row

    v=(d^2/2)e_1^T+(17d/12)e_2^T+e_3^T,

and output column K e_7. Since

    (s+u_1)(s+u_2)
      =(s+lambda)^2+(17d/12)(s+lambda)+d^2/2,

we get the exact transfer identity

    v(sI-G)^(-1)K e_7
      =K(s+u_1)(s+u_2)/[D_5(s)(s+u_1)(s+u_2)]
      =H(s).

Both canceled factors have positive coefficients in the chosen input-state row; no signed initial probability is used.

Define

    h_i=lambda^(i-1)/(u_1u_2), i=1,...,7,
    S=diag(h_i), T_7=S^(-1)G S,
    alpha_7=vS.

Every h_i is strictly positive. Because P_7(lambda)=K u_1u_2, direct substitution gives -G h=K e_7. The PH initial probabilities are explicitly

    alpha_7=(d^2/(2u_1u_2),
             17d lambda/(12u_1u_2),
             lambda^2/(u_1u_2),0,0,0,0).

They sum to1 because their numerator is(lambda+3d/4)(lambda+2d/3)=u_1u_2.

The actual generator T_7 has diagonal-lambda, superdiagonal lambda, and final row

    (f_7/lambda^6, f_6/lambda^5, f_5/lambda^4,
     f_4/lambda^3, f_3/lambda^2, f_2/lambda, -lambda).

All first six row sums are zero. The final exit rate is

    lambda-f_2/lambda-f_3/lambda^2-f_4/lambda^3
            -f_5/lambda^4-f_6/lambda^5-f_7/lambda^6
      =P_7(lambda)/lambda^6=K u_1u_2/lambda^6>0.

The off-diagonal entries are nonnegative; similarity retains the stable spectrum. Consequently T_7 is a PH subgenerator and alpha_7 is a probability row. Its transform is H by the exact similarity identity. This completes the candidate theorem.

## 5. Baseline, novelty and next obligation

The written-checked five-state impossibility above beta^2=1/5 remains the full-topology lower bound. The old six-state construction reaches beta^2=1/2; G7 reaches beta^2=53/96. The inequality53/96>1/2 is exact, so the newly covered parameter band is not empty. This is an actual all-parameter seven-state upper bound in that band, not an assertion of minimum7 or a finite range assay.

All mechanisms—nonnegative companions, hidden stable modes, nonnegative polynomial numerators, positive diagonal normalization—are classical. Priority of this particular family/subrange remains unestablished; the result may be a modest explicit corollary. The new candidate is NOT included in the parent's already-completed WRITTEN_CHECKED verdicts for P1/P2/E/O.

Next consequential alternatives within the same primary target are: exclude arbitrary six-state realizations somewhere in this new band, or obtain a materially larger explicit higher-state construction. An ansatz coefficient sign alone does not close the lower bound. No scientific execution is necessary for reviewing the present candidate; an actual executable check would require a separate named GO.
