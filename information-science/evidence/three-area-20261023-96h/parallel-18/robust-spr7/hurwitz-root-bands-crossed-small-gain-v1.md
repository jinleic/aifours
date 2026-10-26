# SPR7 direct Hurwitz front — six actual root bands and a sharp crossed-span exclusion region

Actual `/bin/date` observation before creation: **Sun Oct 25 05:12:23 PDT 2026**. InfoSPR7 / info-2. **WRITTEN CANDIDATE ONLY.** No scientific eval, arithmetic interpreter, symbolic program, numerical calculation, enumeration or replay was used. Metadata/source reads only. HOLD/v7 and the owner execution erratum remain binding. This is one consolidated direct-Hurwitz continuation, not another abstract separation equivalence.

## 0. Delivered scope and exact limit

For **every** robustly Hurwitz independent monic degree-seven coefficient box, the actual even and odd zero-attainability sets are six compact, strictly alternating root bands. This permits a sharp, quantitative **two-band small-gain theorem** for the entire real crossed-midpoint numerator span. Its condition excludes the full four-component projected moment obstruction whenever it holds, because its numerator lies in that hybrid cone.

The theorem is necessary and sufficient for that crossed span, not for all four hybrid coefficients or unrestricted numerators. If its condition fails, it gives actual corner/frequency obstruction atoms for the crossed span only. The remaining two Euler moment coordinates are explicitly not annihilated by that construction.

This packet also proves an unconditional localization: **any genuine four-component projected zero balance must contain both an even-sign-reversal atom and an odd-sign-reversal atom, in two disjoint actual root bands**. It cannot consist only of anchor roots, one parity's uncertainty bands, zero or infinity.

No claim that whole-box Hurwitzness automatically forces the small-gain condition is made. The first remaining geometric question is the cross-band gain bound or a repair by the two Euler directions in its complementary region. This is the exact stated residual, not a universal SPR7 verdict.

## 1. Imports and full original quantifiers

Use the literal box and pairing from `hybrid-cone-full-space-written-alternative-v1.md`, SHA256 `a4dac632d2b30ae7c133ec2cc2d87a38d8bea4dc279598947950bd3a70aca455`, read with `hybrid-cone-full-space-wording-addendum-1.md`. The actual v32-H reconstruction supports its compactified alternatives at its stated classical imports, with the original wording-MINOR preserved and corrected additively. Its source LF103 now means O_v has degree three and leading coefficient -1; it is not monic.

No explicit union-box coefficient, numerical margin, integer certificate or historical owner/parent arithmetic is imported. All such unadmitted new computations retain no verification credit. The earlier pinned even/odd profile definitions are used only as definitions.

Let

`K={s^7+a_1 s^6+...+a_7 : l_j<=a_j<=u_j}`

be compact and robustly Hurwitz, allowing degenerate intervals. Write midpoint/half-width coefficients m_j,w_j and

`E_0(t)=E_mid(t)=m_1 F(t)`, `Q(t)=O_mid(t)`.

Define the exact nonnegative width polynomials on t>=0:

`R(t)=w_1 t^3+w_3 t^2+w_5 t+w_7`,

`S(t)=w_2 t^2+w_4 t+w_6`.

At each fixed t the ACTUAL sets of component values are the independent intervals

`E_a(t) in [E_0(t)-R(t),E_0(t)+R(t)]`,

`O_a(t) in [Q(t)-S(t),Q(t)+S(t)]`.

Every value in either interval is attained because a linear image of a coefficient box is the whole interval between its extrema. The two component choices can be attained simultaneously, since they use disjoint even/odd coefficient blocks. This independence is essential to all statements below.

Named classical written imports: degree-seven Hermite–Biehler, continuous dependence of ordered simple real roots, the intermediate-value theorem, compactness/extreme values, and monic root continuity. The root-band geometry is a classical stability ingredient, not itself claimed novel.

## 2. A load-bearing consequence of actual whole-box Hurwitzness

Put

`I_E={t>=0: |E_0(t)|<=R(t)}`,

`I_O={t>=0: |Q(t)|<=S(t)}`.

These are precisely the frequencies where zero is attainable by an actual even or odd component, respectively.

### Rectangle lemma

The sets I_E and I_O are disjoint, and neither contains zero. For I_E at zero this follows from the strictly positive lower constant coefficient l_7. The odd set need not be excluded from zero merely by imaginary-axis stability, but here every odd constant coefficient a_6 is positive for a real monic Hurwitz box, so `Q(0)-S(0)=l_6>0` as well.

For t>0, a point in both sets would allow independent coefficient choices with E_a(t)=O_a(t)=0. The ACTUAL resulting member of K would vanish at `s=i sqrt(t)`, impossible. This is not just a pointwise surrogate avoiding a selected family member.

Conversely, for any original independent monic box with l_7>0 and a Hurwitz midpoint, disjointness of these two zero-attainability sets for all t>0 implies every member is Hurwitz: interpolate linearly from the midpoint to any member. No point of that path can have an imaginary-axis zero, by the same independent rectangle argument. Fixed monic degree and bounded coefficients prevent root escape through infinity. Root continuity proves stability. No numerator or cancellation is involved.

### Six actual root bands, not merely two arbitrary disjoint sets

Fix the midpoint odd component Q. It combines independently with every actual even component to give a Hurwitz member. Hermite–Biehler therefore gives each even cubic three simple positive roots, one in each of the three gaps before/between the three midpoint odd roots. Ordered root maps are continuous on the compact connected even coefficient box. Their three images are compact intervals

`I_Ej=[e_j^-,e_j^+]`, j=1,2,3.

Their union is exactly I_E: zero attainability is the same as being a root of some actual even component. Analogously, fixing the midpoint even component gives three compact odd-root ranges

`I_Oj=[o_j^-,o_j^+]`, j=1,2,3,

whose union is exactly I_O. Uniform positive lower bounds on the actual even leading coefficient and bounded coefficients keep all these roots finite; the odd leading coefficient is the fixed -1. All band endpoints are attained, not asymptotic cutoffs.

Because EVERY actual even component can be combined with EVERY actual odd component, Hermite–Biehler applies to every pair of root choices. Taking the attained extrema yields the strict ordering

`0<e_1^-<=e_1^+<o_1^-<=o_1^+<e_2^-<=e_2^+`

` <o_2^-<=o_2^+<e_3^-<=e_3^+<o_3^-<=o_3^+<infinity`.     (BANDS)

Thus there are six alternating compact bands, with strictly positive gaps. No claim that the endpoints are rational or already computed is made.

## 3. Exact worst pairing for the crossed-midpoint span

Consider the one common normalized polynomial

`b_k(s)=k E_0(-s^2)+s Q(-s^2)`.

Its degree-seven leading coefficient is one. For the ENTIRE real two-component crossed span `u E_0(-s^2)+v sQ(-s^2)`, strict exact-degree-seven positivity forces v>0 by the finite tail and u>0 by zero frequency. Dividing by v gives precisely k=u/v>0. Thus no relevant real normalization is omitted.

Define

`A(t)=E_0(t)^2-|E_0(t)|R(t)`,

`B(t)=t[Q(t)^2-|Q(t)|S(t)]`.

Since k>0 and the even/odd blocks are independent, the exact minimum over the ORIGINAL box is

`min_(a in K) P_(a,b_k)(t)=k A(t)+B(t)`.                 (MIN)

Both component minima are attained simultaneously at an actual coefficient corner; its identity may vary with t, which is legitimate for a necessary worst-case condition. The numerator itself never varies with t or corner.

The six-band geometry now supplies the sign controls missing from a generic separation formulation:

- On I_E, all actual odd values have the same strict sign as Q, so **B(t)>0** throughout I_E.
- On I_O, all actual even values have the same strict sign as E_0, so **A(t)>0** throughout I_O.
- A can be negative only inside I_E, away from an E_0 root. B can be negative only inside I_O, away from a Q root.
- Outside both bands, A and B are positive for t>0. At zero A(0)>0 while B(0)=0.

In particular the two possible negative contributions occur on separated actual Hurwitz root bands; they never occur at the same frequency.

## 4. Sharp cross-band small-gain theorem

Let `(x)_+=max(x,0)` and define the finite exact real numbers

`Gamma_E=max_(t in I_E) (-A(t))_+/B(t)`,

`Gamma_O=max_(t in I_O) (-B(t))_+/A(t)`.

These maxima are well-defined: the bands are compact, and the indicated denominators are strictly positive there. They are zero if their corresponding negative contribution is absent. No maximization program or finite sampling is used or proposed by this definition.

### Theorem

There is a strict common degree-seven numerator in the ENTIRE crossed-midpoint span if and only if

`Gamma_E Gamma_O < 1`.                                  (SG)

More precisely, b_k works exactly when

`k>Gamma_O` and `k Gamma_E<1`, with k>0.                  (K)

If Gamma_E>0 and SG holds, the explicit real choice

`k=(Gamma_O+1/Gamma_E)/2`

works. If Gamma_E=0, `k=Gamma_O+1` works. These are mathematical formulas, not executed arithmetic or a rational-coefficient claim.

### Written proof: sufficiency on the WHOLE half-line

On I_E, `A>=-Gamma_E B`, so

`kA+B >= (1-k Gamma_E)B >0`.

On I_O, `B>=-Gamma_O A`, so

`kA+B >= (k-Gamma_O)A >0`.

Outside the six bands both terms are nonnegative and at least one is strictly positive; zero is covered by kA(0)>0. This proves every finite t>=0, including all band endpoints and anchor roots. MIN then proves the same fixed b_k works against every original denominator.

Its normalized pairing tends to one at infinity, because the leading term of tQO_a is t^7, whereas the even product has degree at most six. Continuity and compactness over the corners therefore give an actual positive uniform weighted margin. No numeric margin is invented. Denominators were already proved stable before any cancellation.

### Necessity, including strict endpoints

If Gamma_E>0, its maximum is attained where A<0. At that point MIN is positive only if `k Gamma_E<1`; equality gives an actual corner pairing zero. If Gamma_O>0, the analogous attained maximum where B<0 forces `k>Gamma_O`, again strictly. If Gamma_O=0, strict zero-frequency positivity already forces k>0. Gamma_E=0 imposes no upper bound. Hence K is necessary, and a positive k satisfying it exists exactly when SG holds.

This is not a conservative sufficient budget: SG is sharp for the named entire crossed span. It is only a sufficient condition for the larger four-component hybrid cone and the unrestricted numerator space.

## 5. Direct exclusion and localization of a genuine hybrid moment balance

Use the four hybrid columns F,D,H,Q of the earlier reviewed packet, with the same actual midpoint anchors. A positive corner/frequency balance annihilating those four columns in particular annihilates the F and Q columns. Multiplying the F moment by positive m_1, its two crossed moments are

`sum_i lambda_i rho_i E_0(t_i) E_(v_i)(t_i)=0`,

`sum_i lambda_i rho_i t_i Q(t_i) O_(v_i)(t_i)=0`,

with the compactified endpoint values from the earlier packet. This is only use of that packet's moment representation; no new separation equivalence is being substituted for the geometry.

### Unconditional sign-reversal localization

Such a balance MUST include a finite atom with

`E_0(t_i) E_(v_i)(t_i)<0`,

and another finite atom with

`t_j Q(t_j) O_(v_j)(t_j)<0`.

For the first claim, suppose every even product in its support were nonnegative. A zero even moment then restricts all atoms to even-product zeros or infinity. Every finite even-product zero lies in I_E, where the odd product is strictly positive; at infinity the odd compactified value is one. The odd moment could not vanish. The second claim is symmetric with the only extra odd zero at t=0: at zero the even product is strictly positive, and at every odd-product zero in I_O the even product is strictly positive. Infinity is not an odd-product zero. Thus neither negative type can be absent.

The two atoms necessarily lie in the disjoint interiors of an even and an odd root band from BANDS. This is a Hurwitz-specific restriction on any putative H0 certificate. It excludes balances confined to one parity's bands, to only midpoint/denominator root zeros, or to zero/infinity atoms alone.

### A uniform region where the FULL hybrid obstruction is impossible

Whenever SG holds, b_k is in the hybrid cone, with parameters

`(alpha,beta,gamma,zeta)=(k m_1,0,0,1)`.

Its strict common pairing contradicts every positive four-moment zero balance. Thus SG excludes the full projected balance, not merely a failed scalar choice at isolated frequencies. The proof is the direct actual-box sign argument above and covers all seven independent widths.

## 6. What an SG failure really supplies — and what it does not

If `Gamma_E Gamma_O>=1`, both gains are positive. Choose attained maximizing frequencies t_E in I_E and t_O in I_O. Set

`U=1/Gamma_E`, `L=Gamma_O`, so L>=U.

At their simultaneous minimizing ACTUAL corners, the two uncompactified crossed evaluation vectors have forms

`(-a, U a)` and `(d,-L d)`, with a,d>0.

After compensating their positive compactification factors, positive weights proportional to 1/a and 1/d cancel the first coordinate and leave second coordinate U-L. If L=U these two actual atoms are a crossed-span zero balance. If L>U, add the genuine infinity evaluation vector `(0,1)` with positive weight L-U and normalize all weights to sum one. This is an exact conditional construction of at most three crossed obstruction atoms; it requires no enumeration.

But their remaining two Euler moments need not vanish. Therefore this construction proves **no four-component hybrid obstruction**, and certainly no unrestricted eight-coordinate obstruction. It only proves the impossibility of the crossed span when SG fails. No literal box with SG failure is supplied here.

This is now the exact load-bearing residual rather than a generic projection warning: in the SG-complementary region the actual even/odd uncertainty bands impose incompatible crossed gains, but the additional D and H directions may repair them. Their moment signs must be controlled on those specific bands.

## 7. Where Hurwitz/Rolle control of the companions stops

Write the three midpoint odd roots as q_1<q_2<q_3. Since tQ has simple roots 0,q_1,q_2,q_3, Rolle and degree give exactly one D=(tQ)' root in each interval

`(0,q_1)`, `(q_1,q_2)`, `(q_2,q_3)`.

These are the broad gaps containing the corresponding even root bands. They do NOT by themselves put the D roots outside those actual bands.

Similarly, at the three midpoint F roots r_1<r_2<r_3, H=4F-tF' has signs +,-,+ and negative leading coefficient. Its three roots therefore lie respectively in

`(r_1,r_2)`, `(r_2,r_3)`, `(r_3,infinity)`.

Those are the broad gaps containing the odd root bands. Again this is not a placement relative to their endpoints. Thus ordinary interlacing does not already fix the signs of `E_v D` on the forced even-reversal atoms or `t O_v H` on the forced odd-reversal atoms.

**Exact first missing step after this packet:** either prove that actual whole-box Hurwitzness forces SG, or, when SG fails, obtain a uniform sign/size relation for these two remaining Euler moments on the six ordered bands that excludes all four-moment balances. A genuine alternative negative result would need a literal stable box and an actual balance of ALL FOUR moments; the at-most-three crossed balance in §6 is insufficient. An unrestricted negative result still requires all eight moments.

No conclusion is drawn from an abstract support pattern lacking actual coefficient-box realizability. No claim that a failed sufficient profile condition is necessary for unrestricted synthesis is made.

## 8. Parkable scientific state

Delivered in one packet: actual rectangle/root-band geometry, a sharp entire-crossed-span gain theorem, a full hybrid exclusion region, mandatory two-band localization of every putative hybrid obstruction, and the exact remaining companion-root/moment problem. The fixed-even/fixed-odd limits are classical controls, not counted as discoveries. No new numeric example, certificate, root approximation or machine check was used.

The root-band and gain theorems are WRITTEN CANDIDATES requiring separate reconstruction. Prior v32-H support of the abstract alternative does not accept these new Hurwitz-specific claims in advance. The original wording finding remains in its immutable addendum chain. Universal hybrid feasibility and unrestricted universal SPR7 remain unproved; novelty remains UNCLEAR.
