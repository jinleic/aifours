# SPR7 reciprocal palindromic contacts — an exact Hurwitz-determinant SQUARE and a signed-amplitude coordinate chart

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 05:49:35 PDT 2026**. InfoSPR7/info-2. **NEW COMPLETE WRITTEN THEOREM CANDIDATE.** It gives a direct algebraic stability certificate for the two palindromic corners and distinguishes the actual remaining W_III admission walls. It supplies no box point, emptiness theorem, universal SPR7 result or novelty claim.

Use the COMPLETE v11 packet `reciprocal-WII-WIII-pal-contact-height-wall-and-two-gap-v11.md`, SHA256 `6ce35ce58f8636a95aeddb3b3bbdcbda33a29facb18cdeb28d9b98f236c405b8`, for the actual target/corner/box correspondence and contact-amplitude convention. Its original reciprocal v5/v9/v10+erratum interfaces remain named. V16's stronger fixed-target boundary results remain separate; no old file/gate is edited or its verdict inherited.

All reasoning is exact SYMBOLIC-variable polynomial algebra and the ordinary cubic Hurwitz criterion. Boundary coefficient comparisons below are identities, NOT numerical parameter trial scouts. No calculator/interpreter/eval/program/CAS, enumeration, solver, replay, CLI, nested agent or GO. All FOUR owner written-exactness/v18 findings and other histories remain permanent/ZERO probe credit.

## 1. The contact cubic in a symmetric form

Let T=z^3+d z^2+e z+f, with d,e,f>0 and D=de-f>0. For v=u^2 put X_T=f-dv,W_T=e-v.

For a>0,l>0, v11 constructs the UNIQUE monic cubic

`U(z)=z^3+A_U z^2+B_U z+C_U`

with real pairing `(v-a)^2(v+l)`. Define

`G=(a-e)^2`, `X=da-f`,

`C=e-2a+d a^2/f=(d/f)(a-f/d)^2+D/d>0`.

Then the v11 inverse can be written

`A_U=(G+lC)/D`,

`B_U=[fC+l X^2/f]/D`,

`C_U=a^2l/f`. (SYM)

The first and third are v11's formulas. For the middle, substitute A_U into B_U=d A_U-e-l+2a. The constant numerator is d(a-e)^2+(2a-e)D=fC; the l coefficient is dC-D=X^2/f. Thus all THREE cubic coefficients are STRICTLY positive for every a,l>0, independently of the sign of the contact amplitude.

The exact signed amplitude from v11 is

`kappa(a,l)=(a/D)[e-a-lX/f]`.

At contact U(iu)/T(iu)=i y and kappa=y u. On the physical half-frequency u<0, lead means kappa<0 and lag means kappa>0.

## 2. Exact Hurwitz determinant square, with full algebra

**Theorem.** The cubic Hurwitz determinant is EXACTLY

`A_U B_U-C_U=(fC/a^2) kappa(a,l)^2`. (SQ)

In particular U is strictly Hurwitz IFF kappa!=0. This gives an algebraic proof of v11's strict-corner criterion, not a sampled root calculation or an assumption that a nonnegative pairing automatically makes a corner strict.

**Proof.** The elementary identity

`(a-e)X-fC=-aD`

follows by substituting X=da-f,C=e-2a+d a^2/f. Squaring gives

`G X^2+f^2 C^2-2fC(a-e)X=a^2D^2`.

Now expand using(SYM):

`D^2(A_U B_U-C_U)`

`=(G+lC)(fC+lX^2/f)-a^2l D^2/f`

`=fCG+(l/f)[G X^2+f^2 C^2-a^2D^2]+l^2 C X^2/f`

`=fC[(a-e)+lX/f]^2`.

Since kappa=-(a/D)[(a-e)+lX/f], this is(SQ). All factors f,C,a,D have the stated positive signs. By(SYM) the cubic coefficients A_U,B_U,C_U are positive; the ordinary monic-cubic Hurwitz criterion is therefore exactly A_U B_U>C_U. It holds precisely when kappa!=0. ∎

No substantial import beyond that stated ordinary criterion is hidden in the stability assertion. The original degree-seven palindromic corner `(s+1)s^3 U(s+1/s)` is Hurwitz IFF U is, by the reciprocal root-map identity used in v11.

## 3. The contact-amplitude wall is a QUADRATIC tangency of stability

When f/d<a<e, the positive height wall is

`l_*(a)=f(e-a)/(da-f)`.

Then

`kappa(a,l)=a(da-f)(l_*-l)/(fD)`.

So the Hurwitz determinant is a strictly positive coefficient times `(l-l_*)^2`. It vanishes quadratically at the wall and is positive on BOTH sides. The side of the wall changes the contact lead/lag orientation, NOT the strict-Hurwitz status away from it. A statement that one whole side is unstable would be false.

At the wall kappa=0, U(iu)=0 for u^2=a, and the actual factorization is

`U(z)=(z^2+a)(z+k)`, `k=a l_*/f=a(e-a)/(da-f)>0`.

This is an actual imaginary pair in the cubic/reciprocal corner, not a target-component collision. It explains why the signed-amplitude wall remains an admission boundary even after v16's target-wall guards.

For the C3 corner use b in(0,rho1), hence b<f/d. Its amplitude

`kappa3=(b/D)[e-b+m(f-db)/f]`

is STRICTLY greater than

`kappa3,0=b(e-b)/D>0` for m>0.

Thus its SELECTED finite contact amplitude never vanishes in that fixed slice. The distinct boundary m→0 instead makes C_U=b^2m/f→0. At m=0 the remaining coefficients in(SYM) stay positive, and

`U3(z)=z(z^2+A_3 z+B_3)`

has its extra zero at z=0. In the original reciprocal septic this is a frequency1 imaginary pair. It is not the selected contact b and not a nonpalindromic R zero. Keeping these TWO different boundary mechanisms separate is essential.

## 4. Exact signed-amplitude coordinates for the W_III height plane

Fix T and pal contacts rho2<a<e,0<b<rho1. Put

`X_a=da-f>0`, `Y_b=f-db>0`.

W_III has C1 lag amplitude kappa1>0 and C3 lag amplitude kappa3>0. The height equations invert EXACTLY to

`l=f[a(e-a)-D kappa1]/(a X_a)`,

`m=f[D kappa3-b(e-b)]/(b Y_b)`. (AMPINV)

Consequently positive heights on the correct strict lag side are EQUIVALENT to

`0<kappa1<a(e-a)/D`,

`kappa3>b(e-b)/D`.

No quadratic solve, numerical branch or root-viability probe is needed. The two heights, centers and actual widths are affine in these signed amplitudes at fixed T,a,b. The whole physical positive-width cone remains the SAME three strict linear inequalities under this invertible affine change.

The actual total-width condition is also explicit:

`2L=a[a(e-a)-D kappa1]/X_a`

`    -b[D kappa3-b(e-b)]/Y_b`.

Thus kappa3 has a finite affine upper bound from L>0, and this is the same bounded height triangle expressed in the TWO actual corner amplitudes. It is NOT an independent choice of amplitudes or a discarded original coefficient correlation.

V16's l and L lower bounds cut away kappa1's upper endpoint and L=0. They do NOT cut away kappa1→0 or kappa3→kappa3,0. The square identity now identifies the precise distinct source-stability quantities lost on those faces:

- kappa1→0: A_1 B_1-C_1→0 quadratically, with the actual imaginary pair at v=a;
- kappa3→kappa3,0: C_3→0, with the actual frequency1 pair, while the selected amplitude at b stays positive.

The nonpalindromic amplitudes at all determinant roots still need their separate admission checks from v11/v12/v14. No palindromic formula here substitutes for them.

## 5. Scope and exact next step

This packet proves a whole-corner algebraic Hurwitz certificate and an exact signed-amplitude representation of W_III. It does NOT prove that the finite remainder/positive-factor equations cannot meet the strict amplitude/width cone, nor give a point where they do. The residual can now be stated with its actual source stability walls as two explicit amplitude faces, rather than confusing them with target-wall/frequency escape.

The next written task is to use(SQ)/(AMPINV) with the complete septic factor/amplitude balance and positive-width inequalities, keeping every nonpalindromic zero and source-admission face. No scientific program, evaluation, finite witness/certificate or new GO follows. Original universal SPR7 and reciprocal W_I/W_II/W_III remain OPEN; no formal/kernel/human/configured-family/cross-vendor/executable/triple-finite/novelty or parent acceptance, source cutover, nineteenth owner, deadline reset or round closeout. Same original science cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 and substantive actual-clock cadence remain binding; written work stays active.
