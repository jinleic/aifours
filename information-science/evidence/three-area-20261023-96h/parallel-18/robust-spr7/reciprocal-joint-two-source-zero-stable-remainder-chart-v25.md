# SPR7 — complete stable-positive-real-remainder chart for the joint TWO source-imaginary-pair boundary

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 07:15:03 PDT 2026**. InfoSPR7/info-2. **NEW COMPLETE WRITTEN BOUNDARY-REPRESENTATION THEOREM CANDIDATE.** This supplies the next representation named by v24 rather than assuming a common cubic factor exhausts the boundary. It is NOT an admitted strict-Hurwitz box, an actual closure point of W_III, a feasibility/emptiness statement or a universal result.

All-variable exact conventional proof only, including privately. No numerical/control trial, decimal gloss, calculator, scientific interpreter/eval/program/CAS, enumeration, solver, replay, CLI, nested agent or GO. All FIVE owner exactness findings, the fifth instance/consuming guidance ZERO-credit withdrawal and every prior history remain permanent. The qualified future-only ACK SHA256 `80ea3c102fea58d9549d470039bdca85b4066eace6afb5163b51bc88b838cdad` preceded these proofs. Frozen source/gates unchanged.

## 0. Exact boundary being represented, with no scope substitution

Consider the following precise JOINT source-zero face of the original reciprocal representation:

- B is a real monic palindromic STRICTLY HURWITZ septic with B(0)=1.
- A real monic source corner a2 has constant1, EXACTLY TWO distinct simple imaginary pairs at s=+/-i sqrt(p),+/-i sqrt(q), with0<p<q.
- Its remaining real monic cubic H is STRICTLY HURWITZ. Thus

`a2(s)=N(s)H(s)`, `N(s)=(s^2+p)(s^2+q)`.

- The ENTIRE boundary pairing is nonnegative:

`Re[a2(iomega)/B(iomega)]>=0 for EVERY real omega`.

The theorem parameterizes ALL such pairs(B,a2). It does NOT cover a face with only one source-zero pair, a third source imaginary pair, a nonstrict remaining cubic H, a nonpalindromic target B or loss of target strictness. Nor does every represented pair automatically satisfy the OTHER pal-corner/global width/contact requirements of the full physical W systems.

The original actual corner/width relations and target root map are those in the qualified supported v11 packet, SHA256 `6ce35ce58f8636a95aeddb3b3bbdcbda33a29facb18cdeb28d9b98f236c405b8`. The nonnegative cubic positive-factor lemma used below is proved in the COMPLETE v14 packet, SHA256 `8726e13bcebb5f2d0c3ae718ec9b5a6483e83f55f88bb4e93256c52931d0f433`; it remains a later written candidate, not inherited acceptance. The COMPLETE v24 common-factor route barrier, SHA256 `5f01d6fce2a4f021dac90877522edfdd88f34121da23d1825c9ba239444f508c`, is a separate PROPER subfamily exclusion, not a premise that this whole face is empty.

## 1. Exact positive residue extraction — proof, not an imported network theorem

Put G=B/a2. Since a2/B is analytic in the right half-plane, has nonnegative boundary real part and tends to1, the minimum principle gives STRICT positive real part inside. Therefore it has no interior zero and its reciprocal G is analytic with positive real part there as well.

The source zeros are simple and B has no imaginary zero, so G has simple poles at +/-i sqrt(p),+/-i sqrt(q). At ANY such pole s0, write the leading term R/(s-s0). For approaches s-s0=r exp(i theta), -pi/2<theta<pi/2, the real part of the leading term is r^-1 Re(R exp(-i theta)). Positivity for EVERY such theta forces R to be a NONNEGATIVE REAL number: the limits theta→+/-pi/2 force its imaginary part0, and theta=0 forces the real sign. The pole is genuine, so R>0.

Real coefficients give equal residues at the conjugate pole. Thus there are UNIQUE positive c_p,c_q for which

`G(s)=F0(s)+c_p s/(s^2+p)+c_q s/(s^2+q)`,

where F0 has no imaginary poles. Since H is strictly Hurwitz, F0 has poles only among its roots and tends to1. The two extracted pole terms have purely imaginary boundary values away from their poles, so Re F0(iomega)=Re G(iomega)>=0 there. By continuity after cancellation this remains true at the removed poles too. The minimum principle then gives nonnegative real part for the stable remainder F0 throughout the right half-plane.

Hence

`F0(s)=W(s)/H(s)`,

where W is a REAL monic cubic. Put S=p+q,P=pq,c=1/P. Constant terms of B=N W+... give W(0)=c, and a2(0)=1 gives H(0)=c. Write

`H=s^3+h2 s^2+h1 s+c`,

`W=s^3+w2 s^2+w1 s+c`.

Here h2,h1,c>0 and h2h1>c, with no corresponding source-stability hypothesis silently imposed on W. Its weak-positive property is exactly the finite cubic condition supplied below.

The stable remainder has infinity limit1. Its strictly proper difference W/H-1 NEED NOT be positive real, and is not required to be. This avoids replacing the complete remainder by an unjustified smaller cone.

## 2. Exact polynomial reconstruction of the entire boundary pair

Put

`U=c_p+c_q>0`, `V=c_p q+c_q p`.

Since0<p<q, positive residues are EQUIVALENT to

`pU<V<qU`,

with c_p=(V-pU)/(q-p)>0 and c_q=(qU-V)/(q-p)>0.

Clearing the exact decomposition gives

`B(s)=N(s)W(s)+sH(s)(U s^2+V)`. (BFORM)

Conversely choose0<p<q, c=1/(pq), a strict H as above, a monic W with constant c for which W/H is globally weak positive real, and U,V in the strict residue cone. If BFORM is palindromic strictly Hurwitz, then

`B/(NH)=W/H+c_p s/(s^2+p)+c_q s/(s^2+q)`

has positive real part inside. Each pole term has positive real part there (its expression is half the sum of 1/(s-i sqrt(p)) and 1/(s+i sqrt(p)), scaled by c_p), and W/H is weak positive real. Its reciprocal a2/B is therefore weak positive real. It is monic/constant1 and has EXACTLY the two stated imaginary source pairs because H is strict and p,q distinct.

This proves BOTH directions of the boundary representation, with actual residue signs, denominators and target stability retained. It does NOT assert every such algebraic pair is a limit of admitted W_II/W_III points.

## 3. Palindromic target conditions are THREE explicit AFFINE equations

Expand(BFORM), using c=1/P:

`B1=w2+U`,

`B2=w1+S+U h2`,

`B3=c+S w2+U h1+V`,

`B4=S w1+P+U c+V h2`,

`B5=S c+P w2+V h1`,

`B6=P w1+V c`.

The original septic is monic with constant Pc=1. It is palindromic EXACTLY when

`w2+U=P w1+cV`,

`w1+S+U h2=S c+P w2+V h1`,

`c+S w2+U h1+V=S w1+P+Uc+Vh2`. (PAL)

For fixed H,p,q these are THREE affine equations in w2,w1,U,V. No generic full-rank or uniqueness assumption is made; all rank-degenerate solutions are retained.

Its target cubic coordinates are EXACTLY

`d=B1-1`, `e=B2-B1-2`, `f=B3-B1-B2+1`.

B is strictly Hurwitz IFF d,e,f>0 and de>f, by the exact palindromic target root map. Those inequalities are MANDATORY. Pole extraction alone does not prove target strictness or permit a degenerate target.

## 4. The stable positive-real remainder has an exact finite two-parameter chart

At t=omega^2,

`Re[W(iomega) conjugate H(iomega)]`

`=t^3+alpha t^2+beta t+c^2`,

`alpha=w2h2-w1-h1`,

`beta=w1h1-c(w2+h2)`.

Since H is strict, W/H is globally weak positive real IFF this monic cubic is nonnegative for EVERY t>=0. The complete v14 cubic factor lemma makes this equivalent to

`t^3+alpha t^2+beta t+c^2=(t+z^2)[(t-h)^2+lambda t]`,

`z>0`, `h=c/z>0`, `lambda>=0`.

Thus

`alpha=z^2+lambda-2c/z`,

`beta=c^2/z^2+z^2(lambda-2c/z)`.

With D_H=h2h1-c>0, the numerator coefficients invert UNIQUELY:

`w2=[h1^2+c h2+h1 alpha+beta]/D_H`,

`w1=h2 w2-h1-alpha`. (WINV)

This is an exact two-real-parameter representation of EVERY stable remainder at fixed H, not a positivity sample or a selected real-root branch.

Both coefficients are actually positive, with no numerical root check. For w2 the numerator is

`(h1-c/z)^2+h1(z-c/h1)^2+c(h2-c/h1)+lambda(h1+z^2)>0`.

For w1, its numerator after multiplication by D_H is

`c(h2-z)^2+c[h1-2c/z+h2c/z^2]+lambda(c+h2z^2)>0`,

because the bracket is (h2/c)(c/z-c/h2)^2+h1-c/h2>0. These use only D_H>0. Nevertheless W can have an imaginary pair on the exact weak boundary lambda=0 with vanishing remainder amplitude; strict W is not an unmentioned assumption.

Together(WINV), (PAL), the residue cone and strict target-cubic inequalities are a complete finite boundary system. They preserve a general nonconstant stable positive-real remainder rather than just W=H.

## 5. ACTUAL original source widths and the conditions STILL missing

The actual C2 source is a2=N H, whose six original coefficients are

`A1=h2`, `A2=h1+S`, `A3=c+S h2`,

`A4=S h1+P`, `A5=S c+P h2`, `A6=P h1`.

Thus actual positive paired widths require

`P h1-h2>0`,

`h1+S-S/P-P h2>0`,

`c+S h2-S h1-P>0`.

These are NECESSARY original width conditions, not automatic from the positive-real remainder cone. The actual palindromic corners determined by this list and its reversal must ALSO have their complete nonnegative pairings, correct pal-contact shapes/cells and strict pal source amplitudes if one is studying the W_III joint-face closure. None is inferred from BFORM or the successful single-corner ratio.

V24's common-cubic-factor construction is ONE proper subfamily where the stable remainder is the constant1 (W=H) and the target/source factors have its specific reciprocal alignment. That subfamily has positive-width members but a strictly negative C1 Hurwitz determinant, so cannot produce an admitted box. This does NOT prove ALL algebraic W=H solutions of(PAL) have that specific alignment or remove rank-degenerate PAL solutions. The complete chart here explicitly retains them unless a new proof excludes them.

One-source-zero faces, three-imaginary-pair faces and loss of strict H are separate. No covering or closure theorem for those faces is claimed by the present exact two-pair/strict-H parametrization.

## 6. Exact next physical problem and assurance

The next problem is the real intersection of this COMPLETE stable-remainder boundary chart with ALL actual positive widths, pal-corner global/contact/amplitude constraints and target strictness, followed by a justified perturbation into a strict-source physical point or a uniform boundary exclusion. Neither a boundary solution nor a perturbation preserving the full contact system is supplied. A formal dimension count or an affine PAL system is not a physical feasibility proof.

This is a genuinely broader next representation than the failed common-factor ansatz, not a new solved problem, an original nonembedding theorem or a numerical witness. All claims are WRITTEN candidates requiring complete source/application reconstruction at their stated ordinary analytic/real-algebraic interfaces. No formal/kernel/human/configured-family/cross-vendor/executable/triple-finite/novelty or parent acceptance, scientific GO, source cutover, nineteenth owner, deadline reset or round closeout. Same original18/HOLD/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 and actual-clock substantive cadence; work remains active.
