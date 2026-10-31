# SPR7 reciprocal system — an exact 3x3 Bezoutian replaces ALL nonpalindromic amplitude-admission tests

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 06:44:44 PDT 2026**. Owner InfoSPR7/info-2. **NEW COMPLETE WRITTEN THEOREM CANDIDATE**, LATER than the comprehensive v11-v20 intake manifest. It is NOT automatically part of that frozen/pending union or a proof that any physical system is feasible.

## 0. Process order, exact scope and imports

The held symbolic matrix lead and its missing converse were disclosed BEFORE this proof. The later private numeric instance check in `owner-written-exact-arithmetic-erratum-v5.json`, SHA256 `d321055bf2392664787130f48b2ab14f22b668626a0c73e1262f3b840b36f6e7`, is entirely WITHDRAWN/ZERO credit. It is NOT reproduced, recomputed or used as guidance/evidence here. All FOUR earlier findings/v18 and every older history remain permanent.

After Main explicitly reported COMPLETE actual finding/checkpoint reading and future-only direction, the WHOLE-state qualified ACK `primary-after-fifth-scope-finding-future-only-ack-v1.json`, SHA256 `80ea3c102fea58d9549d470039bdca85b4066eace6afb5163b51bc88b838cdad`, observed06:41:25, was WRITTEN and SENT BEFORE any new source/proof. This proof then supplies the previously missing converse with ALL-variable algebra and a finite-dimensional self-adjoint companion argument. No numerical/control instance, decimal gloss, calculator, scientific interpreter/eval/program/CAS, enumeration, solver, replay, CLI, nested agent or GO.

The only named ordinary inputs of the generic theorem are the real symmetric spectral theorem/positive-definite quadratic forms, polynomial division, Vandermonde algebra and the EXACT degree-seven Hermite–Biehler criterion. The specialized matrix identities and its converse-to-positive-interlacing proof are supplied below, not imported from a headline.

The reciprocal application uses the complete v11 actual corner/zero/admission representation (`reciprocal-WII-WIII-pal-contact-height-wall-and-two-gap-v11.md`, SHA256 `6ce35ce58f8636a95aeddb3b3bbdcbda33a29facb18cdeb28d9b98f236c405b8`), and the pal-corner strict-stability certificate of v17 (`reciprocal-pal-contact-Hurwitz-square-and-amplitude-chart-v17.md`, SHA256 `28ad2d2d80ad25b693b581bc61f5433e12564c1ea8a0e580e5437fcd0c9a5990`). Their original v5/v9/v10+erratum interfaces remain. N12/N14 frequency factor templates can be used exactly as already stated; no positive-zero or source-Hurwitz condition is dropped.

## 1. Generic degree-seven theorem — exact matrix

Let

`a(s)=s^7+A1 s^6+A2 s^5+A3 s^4+A4 s^3+A5 s^2+A6 s+1`,

with ALL six Ai>0. Define

`P(t)=t^3-p t^2+q t-r`, `p=A2,q=A4,r=A6`,

`Q(t)=alpha t^3-beta t^2+gamma t-1`, `alpha=A1,beta=A3,gamma=A5`.

Thus P=-O_a and Q=-E_a in a(iomega)=E_a(t)+iomega O_a(t), t=omega^2. Put z(t)=(1,t,t^2)^T and define the symmetric matrix B by

`[P(t)Q(w)-Q(t)P(w)]/(t-w)=z(t)^T B z(w)`.

Its entries, obtained by pairing the polynomial monomials, are EXACTLY

`B00=gamma*r-q`, `B01=p-beta*r`, `B02=alpha*r-1`,

`B11=alpha*r-1+beta*q-p*gamma`,

`B12=gamma-alpha*q`, `B22=alpha*p-beta`. (BEZ)

**Theorem.** Under the displayed Ai>0 hypotheses, a is STRICTLY HURWITZ IFF B is POSITIVE DEFINITE. Equivalently, by Sylvester's criterion with reversed basis order:

`B22>0`,

`B22*B11-B12^2>0`,

`det B>0`. (PD)

These are THREE explicit strict rational polynomial inequalities. No numerical eigenvalue, root search, sample or formal-kernel claim is involved.

## 2. Proof that positive definiteness forces three DISTINCT REAL roots

The companion matrix for multiplication by t modulo P is

`M=[[0,0,r],[1,0,-q],[0,1,p]]`.

Its characteristic polynomial is P, and the vector e0=(1,0,0)^T is cyclic because e0,Me0,M^2e0 are the three coordinate basis vectors. Hence the minimal polynomial of M has degree3 and equals P.

The defining Bezout identity implies

`M B=B M^T`. (INT)

Here is the coefficient-level argument. Modulo P(t), the column t z(t) is M^T z(t); the last entry reduces by t^3=p t^2-q t+r. Multiplying the kernel by t-w gives P(t)Q(w)-Q(t)P(w), which is zero modulo P(t),P(w). Reducing each variable gives

`z(t)^T(MB-BM^T)z(w)=0`.

Each variable degree is at most2 after reduction, so EVERY coefficient is0, proving(INT). This is an exact polynomial identity, not an unverified companion convention.

If B is positive definite, equip R^3 with inner product <x,y>=x^T B^-1 y. From(INT), B^-1 M=M^T B^-1, so M is self-adjoint in this positive inner product. The real finite-dimensional spectral theorem gives real eigenvalues and diagonalizability. Because M is cyclic, its minimal polynomial equals its characteristic polynomial P. A diagonalizable real operator has square-free minimal polynomial. Therefore P has THREE DISTINCT REAL roots, not merely real eigenvalues with an unexamined multiplicity.

This supplies the missing converse bridge from matrix definiteness. It does not assume the sought real-root/interlacing conclusion.

## 3. Positive roots, residues and EXACT Hermite–Biehler orientation

Let the three real simple P roots be o1<o2<o3. For x>=0,

`P(-x)=-x^3-px^2-qx-r<0`,

because p,q,r>0. Thus no root is nonpositive: 0<o1<o2<o3.

At a root oi, the diagonal Bezout limit is

`z(oi)^T B z(oi)=P'(oi)Q(oi)>0`.

Thus Q(oi)!=0 and the exact partial-fraction residues

`c_i=Q(oi)/P'(oi)>0`.

Polynomial division gives

`Q(t)/P(t)=alpha+sum_(i=1)^3 c_i/(t-oi)`,

whose derivative is `-sum c_i/(t-oi)^2<0` between poles. Since alpha>0 and Q(0)/P(0)=1/r>0:

- On(0,o1), the ratio decreases from a positive value to minus infinity, so it has EXACTLY one zero e1 there.
- On(o1,o2) and(o2,o3), it decreases from plus infinity to minus infinity, giving EXACTLY one zero e2,e3 respectively.
- On(o3,infinity), it decreases from plus infinity to alpha>0, so no additional zero occurs.

Q is cubic, so these exhaust its roots. Therefore

`0<e1<o1<e2<o2<e3<o3`.

This is the PRECISE degree-seven Hermite–Biehler arrangement for E_a=-Q and O_a=-P, with positive constant and monic leading coefficient in the original s-polynomial. By that ordinary criterion, a is strictly Hurwitz. No reversal of the root order or modulo-four phase rule is used.

Conversely, if a is strictly Hurwitz, degree-seven Hermite–Biehler gives exactly that interlacing. The signs of P'(oi) and Q(oi) match at every oi, so P'(oi)Q(oi)>0. For distinct roots oi,oj, the off-diagonal Bezout value is0. Thus, with V having columns z(oi),

`V^T B V=diag(P'(o1)Q(o1),P'(o2)Q(o2),P'(o3)Q(o3))`.

V is invertible by the Vandermonde determinant, hence B is positive definite. This proves BOTH directions of the generic theorem.

## 4. Reversal gives the SAME matrix test for C4

For the reciprocal reversal Ra(s)=s^7a(1/s), the actual coefficients are reversed. Its P_R,Q_R satisfy

`P_R(t)=-t^3 Q(1/t)`, `Q_R(t)=-t^3 P(1/t)`.

Consequently its Bezout kernel is

`t^2 w^2 z(1/t)^T B z(1/w)`.

Let J be the 3x3 coordinate-reversal permutation matrix. Since t^2 z(1/t)=J z(t),

`B_R=J B J`.

Thus B_R is positive definite IFF B is. This is a direct congruence, not a second unverified set of source stability inequalities. It also agrees with the ordinary fact that reversal preserves strict Hurwitz stability when both leading/constant coefficients are positive.

## 5. Actual reciprocal C2 coefficients and full whole-box application

Let the two ACTUAL pal-corner cubics, reconstructed by v11, be

`U1=z^3+u2 z^2+u1 z+u0`,

`U3=z^3+v2 z^2+v1 z+v0`.

They are strictly Hurwitz when the exact pal amplitudes are nonzero, by v17's determinant square. Their coefficients u_i,v_i are all strictly positive. Direct expansion of (s+1)s^3U(s+1/s) gives coefficient list

`(A1,A2,A3,A4,A5,A6)=(1+U2,3+U2+U1,3+2U2+U1+U0,3+2U2+U1+U0,3+U2+U1,1+U2)`.

The ACTUAL C2 corner combines the EVEN component from C1 with the ODD component from C3, so its coefficients are exactly

`A1=1+u2`, `A2=3+v2+v1`,

`A3=3+2u2+u1+u0`, `A4=3+2v2+v1+v0`,

`A5=3+u2+u1`, `A6=1+v2`. (C2DATA)

All six are positive automatically; the generic theorem's coefficient hypotheses are ACTUALLY verified, not omitted. C4 is its reversal and uses the congruent matrix from Section4.

Now retain ALL original positive paired-width inequalities and global weak corner-pairing positivity from v11, or its EXACT finite factor alternatives v12/v14. Under these hypotheses:

`ALL nonpalindromic positive-zero amplitudes are nonzero`

`IFF the matrix(BEZ), with(C2DATA), is positive definite`.

**Proof.** If the matrix is positive definite, C2 and C4 are strictly Hurwitz by Sections1–4, so their actual values are nonzero at EVERY finite positive frequency, not just at selected or listed determinant roots. Conversely v11's ALL-zero amplitude admission, together with global corner-pairing positivity and target/end guards, proves strict Hurwitz stability of the whole box and hence of its C2 corner; the generic theorem then gives positive definiteness.

The WHOLE original independent box remains strictly Hurwitz under the new matrix condition by the SAME direct admission argument: for every member a, a/B is analytic in the right half-plane, has nonnegative boundary real part and positive infinity limit. The minimum principle excludes right-half-plane zeros. Any imaginary zero forces a pairing minimum0. At target-component zeros the margin is strict; elsewhere the minimizing actual corner is UNIQUE. It would therefore force a zero of C1,C3,C2 or C4, all now strictly Hurwitz, contradiction. Actual constant1 excludes0. No use of an unprovided Kharitonov theorem, finite root grid or scientific Routh computation is needed.

Thus THREE finite strict polynomial inequalities replace the ENTIRE nonpalindromic ALL-zero admission family, including every unselected/higher-multiplicity/extra-cubic zero. They do NOT replace global pairing positivity, the physical width cone, correct selected contact-orientation signs, or pal nonzero-amplitude walls. Those remain EXACTLY as before.

## 6. Two-height geometry and exact remaining problem

At FIXED T,a,b, every u_i is affine in the C1 height l and every v_i affine in the C3 height m. Hence EVERY entry of(BEZ) is bi-affine in l,m: constant + l term + m term + lm term. For either height held fixed, the whole matrix is affine in the other height. Its positive-definite preimage on that line is an interval (possibly empty), since the positive-definite matrix cone is convex.

Combining it with the actual width/height-wall linear inequalities and v11's whole-frequency affine pairing half-planes preserves this separate-line convexity. It is NOT a claim of joint convexity in(l,m), feasibility, global target compactness or matrix positivity by its diagonal entries alone. The full determinant/minor inequalities are mandatory.

A complete physical W_II/W_III point may now be specified by: strict target/cells, exact pal-contact inverse/height wall, actual positive widths, complete nonnegative septic factorization, these THREE strict Bezout minors, and selected actual alternating amplitude signs. This is equivalent to the earlier full source-admission formulation; it provides a cleaner exact finite source-Hurwitz barrier for the remaining physical system, not a solved instance.

The original unrestricted/general-box SPR7 target and reciprocal alternatives remain OPEN. This later proof needs its OWN complete gate/claim-DAG update before promotion, not insertion into the already requested v11-v20 union. Conventional observable proof and source metadata only; no hidden-reasoning/global-cognition census, stronger formal/kernel/human/configured-family/cross-vendor/executable/triple-finite/novelty acceptance, new GO, source cutover, nineteenth owner, deadline reset or round closeout. Same original cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 and actual-clock substantive cadence remain binding; work remains active.
