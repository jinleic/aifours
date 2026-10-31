# SPR7 W_III — bounded entire height plane, no outer-frequency escape, and uniform target-wall guards at every fixed target/contact slice

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 05:30:07 PDT 2026**. InfoSPR7/info-2. **NEW COMPLETE WRITTEN CONDITIONAL THEOREM CANDIDATE.** This is an all-height W_III result at fixed T,a,b, not a tiny-r W_I bound and not an assertion of global target-parameter compactness or existence.

Only SYMBOLIC variables/exact fractions/integer-product identities are used, privately too. No numerical instance, decimal gloss, calculator, scientific interpreter/eval/program/CAS, enumeration, solver, replay, CLI, nested agent or GO. All FOUR owner exactness/v18 findings and all earlier histories remain permanent/ZERO probe credit; all frozen sources/gates unchanged.

## 0. Exact inputs and quantified scope

Use the complete new v11 packet `reciprocal-WII-WIII-pal-contact-height-wall-and-two-gap-v11.md`, SHA256 `6ce35ce58f8636a95aeddb3b3bbdcbda33a29facb18cdeb28d9b98f236c405b8`, for target phase roots, height wall, original interval inverse, determinant and admission. Sections4–5 also use the exact finite factor template of `reciprocal-WII-WIII-positive-factor-and-amplitude-template-v14.md`, SHA256 `8726e13bcebb5f2d0c3ae718ec9b5a6483e83f55f88bb4e93256c52931d0f433`. Their full named reciprocal v5/v9/v10+erratum and assurance boundaries remain.

FIX ANY strictly Hurwitz T=z^3+d z^2+e z+f with d,e,f>0,D=de-f>0. Let its phase roots satisfy0<rho1<f/d<rho2<e<rho3. FIX the palindromic contact positions

`rho2<a<e`, `0<b<rho1`.

The theorem quantifies over EVERY pair of heights l,m and EVERY W_III point with THESE fixed T,a,b. No smallness of a,b,d,e,f is assumed. There may be no such point.

**Conclusion.** All heights, widths, all positive determinant roots, and all positive-factor parameters have explicit finite upper bounds. ALL nonpal contact roots are uniformly separated from the three target component walls. Thus neither an outer v→infinity/physical-frequency→0 escape nor a target-wall collision can occur while only the heights vary in this fixed slice.

This leaves height/width/amplitude degenerations and variation of T,a,b as genuine separate issues; it does not prove an arbitrary global bad infimum is attained.

## 1. The whole W_III height domain is bounded

Define the fixed positive height-wall value

`l_*=f(e-a)/(da-f)>0`.

W_III's C1 lag side gives0<l<l_*. Width positivity implies

`L=w1+w2+w3=(a^2l-b^2m)/(2f)>0`.

Therefore

`0<l<l_*`, `0<m<m_*:=(a^2/b^2)l_*`,

`0<L<L_*:=a^2l_*/(2f)`, and every `0<w_i<L_*`. (HEIGHT)

These inequalities hold for the ENTIRE height domain, including arbitrarily large m allowed in an uncoupled parameterization: that apparent large-height escape is excluded by the actual shared width sum at fixed b>0. This uses original interval correlations, not an independent height cutoff.

## 2. A uniform coefficient bound for the actual septic determinant

Write Phi=v^3+p2v^2+p1v+p0. The exact v11 coefficients give the fixed bounds

`|p2|<=P2_*:=(l_*+m_*)/2+a+b`,

`|p1|<=P1_*:=(a^2+b^2)/2+a l_*+b m_*`,

`0<p0<=P0_*:=a^2 l_*`.

Put

`P_*=1+P2_*+P1_*+P0_*`.

For a real polynomial F let ||F||_1 be the SUM of the absolute values of its coefficients. The displayed inequalities imply ||Phi||_1<=P_*.

For K=k2v^2+k1v+k0, direct width formulas are

`k2=(d+1)w1+w2`,

`k1=(d+2)L+(2d-f-e)w1-(2d+e)w2`,

`k0=-(f+2e)L+2f(w2-w1)`.

Using positive widths and(HEIGHT),

`|k2|<=(d+2)L_*`,

`|k1|<=(5d+f+2e+2)L_*`,

`|k0|<=(3f+2e)L_*`.

Hence, with

`K_*=(6d+4f+4e+4)L_*`,

we have ||K||_1<=K_*. The polynomial norm is submultiplicative by the triangle inequality for convolution; multiplying by v preserves it, and ||v+4||_1=5. Therefore the actual monic septic

`R=(v+4)Phi^2-vK^2`

satisfies

`||R||_1<=M:=5P_*^2+K_*^2`. (COEFF)

No coefficient has been evaluated, sampled or computed by a program. M is an explicit symbolic finite bound determined ONLY by fixed T,a,b.

## 3. No positive root escapes; exact uniform target-wall guards

Put `F_*=1+M`. EVERY positive real root v0 of R satisfies

`v0<F_*`. (ROOT)

**Proof.** Each nonleading coefficient has magnitude at most M. If v0>=1+M>1 and R(v0)=0, then

`v0^7<=M sum_(i=0)^6 v0^i=M(v0^7-1)/(v0-1)<=v0^7-1`,

a contradiction. This is the elementary monic root bound, not a numerical root finder.

In particular the outer selected W_III contact s obeys rho3<s<F_*, uniformly over ALL admissible heights. Under t(v)=(v+2-sqrt(v(v+4)))/2, this gives t(s)>t(F_*)>0. The reciprocal partner is also bounded away from infinity. If F_*<=rho3, the fixed slice is EMPTY immediately; no existence is inferred when the interval is nonempty.

Now define, for i=1,2,3, the fixed positive quantities

`D_i=(rho_i+4)(rho_i-a)^2(rho_i-b)^2 rho_i^2`.

At a target component wall A(rho_i)=0, the exact determinant identity gives

`R(rho_i)=(rho_i+4)phi1(rho_i)phi3(rho_i)>=D_i>0`,

because rho_i+l>=rho_i and rho_i+m>=rho_i. This lower bound is independent of BOTH heights.

Put `V_*=F_*+rho3>1` and `G_*=7M V_*^6`. On the entire interval[0,V_*],

`|R'(v)|<=7V_*^6 ||R||_1<=G_*`.

Both every positive R root and every rho_i lie in this interval. The real mean-value theorem therefore gives the uniform guard

`|v0-rho_i|>=delta_i:=D_i/G_*>0` (GUARD)

for EVERY positive root v0, including unselected/extra/higher-multiplicity contacts. Thus W_III's selected roots must satisfy

`rho1+delta1<=r<=rho2-delta2`,

`rho3+delta3<=s<F_*`.

These are genuine all-height frequency guards from the actual target-component margins, not guessed band separations. If the indicated closed inner interval is empty or the outer upper bound does not exceed its guarded lower bound, the slice is EMPTY.

## 4. The three positive-factor parameters are uniformly bounded as well

Use the exact factorization R=(v-r)^2(v-s)^2 Q from v12/v14. All selected roots are below F_*. Its quotient coefficients satisfy

`|c2|<=B2:=M+4F_*`,

`|c1|<=B1:=M+4F_* B2+6F_*^2`,

`0<c0<=B0:=M+4F_* B1+6F_*^2 B2+4F_*^3`.

These follow from v12's explicit top-coefficient equations with S=r+s<=2F_* and P=rs<=F_*^2. They do not divide by a potentially small selected root.

Set `B_*=max(1,B2,B1,B0)` and `A_*=1+B_*`. In ANY representation

`Q=(v+alpha)[(v-h)^2+lambda v]`, alpha,h>0,lambda>=0,

-alpha is a real root of the monic cubic. The same monic root argument applied to Q(-v) gives alpha<A_*.

Its coefficient equations yield

`h^2=c1-alpha c2+alpha^2<=H2_*:=B1+A_* B2+A_*^2`.

Thus, for example, `h< H_*:=1+H2_*`, and

`0<=lambda=c2-alpha+2h<B2+2H_*`.

The positive amplitude parameter z=sqrt(alpha) from v14 is bounded too, for example z<1+A_*. These bounds apply to EVERY possible negative-root choice in the positive-factor representation, not just a preferred factorization. On lambda=0, h is an actual extra R root and also satisfies(ROOT)/(GUARD).

## 5. What compactness is and is NOT established

At FIXED T,a,b, all W_III solutions to the complete finite system lie in an explicit bounded coordinate box, and their nonpal contact frequencies have the uniform target-wall guards above. This proves no upper-coordinate/frequency escape within that fixed slice. It also shows the selected contact orbits stay distinct: r lies below rho2, s above rho3, and the pal contacts a,b are fixed strictly in their separate cells.

The closure of this bounded parameter set is compact in the ordinary finite-dimensional sense. It need NOT consist of admissible W_III points: l or m can approach0, some width can approach0, C1 can approach its zero-amplitude wall, or a nonpal denominator amplitude can vanish. Those are NOT waived. Varying T,a,b can also destroy the fixed constants or let them diverge. No global all-parameter attainment or unrestricted SPR verdict follows.

The exact next task is to exploit the bounded finite coefficient system with all strict source/admission boundaries retained, or to control those actual boundaries by a new written argument. No rational subdivision/SOS generation, finite search, solver or certificate replay is admitted or performed. All claims remain WRITTEN candidates at their named imports, not formal/kernel, family/human/cross-vendor, executable/triple-finite, novelty or parent acceptance. Original full SPR7, reciprocal alternatives, same18, cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 remain unchanged; work is active.
