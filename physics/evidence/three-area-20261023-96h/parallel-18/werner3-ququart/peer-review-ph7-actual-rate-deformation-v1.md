# v34-B — full written reconstruction of the actual-rate PH7 deformation

Observed `/bin/date` before this report: **Sun Oct 25 05:00:24 PDT 2026**. Reviewer PhysicsResearch96h-2; author MathResearch96h. Serial prerequisites v30-A and v32-D were fully returned before this assignment; no v33 review is pending for this owner.

**Verdict: 0 FATAL / 0 MAJOR / 0 MINOR at the stated written/import scope.** The complete two-parameter actual-matrix identity, derivative and strict feasible direction, ordered algebraic root construction, closed-interval simultaneous positivity, and PH normalization are reconstructed below. They do establish a strictly larger ACTUAL positive family beyond zeta, with an unevaluated algebraic endpoint z_new<8/9. They do NOT decide unrestricted PH7 at8/9.

## 1. Frozen sources, complete coverage and method

Read exact assignment v34-B in RUN/`peer-review-wave-eighteen-v34.json`, SHA256 `e18f755217a6aae669ae886f201a89a676e75dc2782b687a672458b0e42e0a0c`, complete parent erratum v7, and the packet receipt SHA256 `0e4bf0f0363704e98d3da089559c1e4179f071b84293ee422ddf1265803a9821`.

Read the ENTIRE literal packet RUN/`peer-review-wave-v34-ph7-actual-rate-deformation-sources-v1.md`, LF1-210, SHA256 `20c1cce8f505d69ddb8d8ab7796f7dfb1bb30458ff799fc12c5d5102be1e9cb6`. This includes ALL original source LF1-201. Explicit RAW rereads were made at packet LF28,104,145,161,168,181,185,199,207,209. No truncated load-bearing line is assumed read without recovery.

The actual source `mathematics/evidence/three-area-20261023-96h/parallel-18/phase-type/PH7-u-deformation-actual-family-v1.md` hashes to `9f9b048bd4113b5008bdebf56f1e5d903e06e0b6ffe1f8eed78dbcd7ebb1a01e`, matching the manifest. References below use ORIGINAL source LFs. RUN is `institute/runs/three-area-2026-10-23-96h/`.

Exposure was frozen in `peer-review-ph7-actual-rate-deformation-ack-v1.json` before the packet body. The review is not blind: this reviewer already reconstructed the predecessor charts, endpoint and normalization in v30-A and the time-reversal reduction in v32-D. The latter is not needed for this construction.

**STRICTLY WRITTEN METHOD:** no scientific interpreter/eval/arithmetic program/symbolic program/enumeration/certificate replay/solver, no model CLI or extra agent, no GO. All calculations below are written coefficient/derivative reasoning, not copied historical booleans or owner program output. Only metadata clocks/hashes and source extraction were used. No author/shared or pinned files were changed. No executable-verification, formal/human/cross-vendor or novelty credit follows.

## 2. Entire actual two-parameter characteristic identity — LF33-104

The literal six-rate polynomial is

```
E(y)=(y+u)^3(y+1)^3
    =y^6+a y^5+b y^4+c3 y^3+e4 y^2+e5 y+e6.
```

Multiplying the two cubics gives exactly the displayed a,b,c3,e4,e5,e6. In particular there is no independently chosen coefficient list detached from the actual principal blocks.

Write v_z=1+z. The visible degree-five polynomial expands to

```
D_z(y)=y^5+4y^4+(6+2z)y^3+(4+4z)y^2+(1+z)^2 y.
```

Therefore the coefficients of `D_z(y)(y^2+p y+q)`, from degree7 down to degree0, are

```
1,
p+4,
q+4p+6+2z,
4q+(6+2z)p+4+4z,
(6+2z)q+(4+4z)p+(1+z)^2,
(4+4z)q+(1+z)^2p,
(1+z)^2q,
0.                                                        (R1)
```

The corresponding coefficients of `(y+w)E(y)` are `1,a+w,b+aw,c3+bw,e4+c3w,e5+e4w,e6+e5w,e6w`.

Degree6 equality gives `w=p+4-a`. Degree5 equality then gives the source q. Substituting both into the degree4 difference yields EXACTLY `Lp-N`; hence its cancellation is the displayed p=N/L, without a hidden extra equation. Degrees3,2,1,0 give exactly phi,R2,R1,R0.

The actual feedback polynomial is

```
phi(y+u)^3+D1(y+1)^2+D2(y+1)+D3.
```

Its coefficients at degrees3,2,1,0 are

```
phi,
3u phi+D1,
3u^2 phi+2D1+D2,
u^3 phi+D1+D2+D3.
```

The literal definitions LF63-65 set these equal to phi,R2,R1,R0. Thus ALL eight polynomial coefficients in identity(A) match for every u,z with L!=0. This reconstructs the entire two-variable identity, not selected samples or a tangent approximation.

Every displayed p,q,w,B,C,phi,D1,D2,D3 is affine in p and q,w (and those in p), with polynomial u,z multipliers. Consequently multiplying by L really does give the stated polynomial numerator; no L^2 or other unmentioned denominator is introduced in H.

The actual common-matrix determinant is obtained by eliminating J_u and J_1; it is `(y+w)(y+u)^3(y+1)^3-phi(y+u)^3-D1(y+1)^2-D2(y+1)-D3`. The same elimination gives the numerator `K[(y+u)^2+B(y+u)+C]=KQ(y)`. Clearing the temporary triangular inverses establishes polynomial identities everywhere. All backward first-column D entries and the last-to-center phi feedback are retained. r=0 and the other zero entries are explicitly CHOSEN members of this family, not alleged restrictions on every PH7.

## 3. Exact specialization and derivative identity(B) — LF108-135

It is useful to simplify the source's actual definitions BEFORE differentiating:

```
h0=-6u^2+3u,
L=3u^2-3u+1-2z,
N=8u^3-9u^2+3u-4z.                                       (R2)
```

At u*=3/2, put M=13-8z. Then

```
L=M/4, N=(45-16z)/4,
L_u=6, N_u=30, h0_u=-15,
a-4=7/2.
```

Thus the displayed old-chart p,q,w follow. The factor-of-four difference between the general L and the old Chart II denominator M is harmless but MUST be retained: general L is M/4, not M. Substitution into the general phi gives the old F3/M. Since identity(A) specializes to the previously reconstructed identity with the SAME p,q,w,phi, the unique residual-degree2,1,0 recurrences give precisely the predecessor D1,D2,D3 as well. Likewise B,C specialize to their actual old boundary values. The strict imported signs therefore apply to all nine quantities at (u*,zeta), with phi=0.

Differentiate `Lp=N` at fixed z:

```
p_u=(30-6p)/L
    =24(5-p)/M
    =96(5-6z)/M^2.
```

Differentiating q yields `q_u=3p+(7/2)p_u-15`, while `w_u=p_u-3`. At u*, the actual coefficient values/derivatives are

```
c3=305/8, (c3)_u=171/4, (e4)_u=201/4.
```

Therefore direct differentiation of the actual phi, with NO independently varied feedback, gives

```
phi_u=(99/4-6z)p+(105/8-11z)p_u-495/4+30z.
```

For an explicit check of the full rational simplification, after multiplication by M^2 the three displayed terms have coefficient vectors in increasing powers of z:

```
(57915/4, -17568, 6576, -768),
(6300, -12840, 6336, 0),
(-83655/4, 30810, -14160, 1920).
```

Their sum is exactly `(-135,402,-1248,1152)`, proving identity(B) for all z with M!=0. These are written expansions of the displayed derivatives, not a program-produced coefficient array.

## 4. Strict feasible direction at the cubic endpoint — LF133-141

The endpoint equation gives

```
1152 zeta^3=-432 zeta^2+1128 zeta-81.
```

Hence the numerator in(B) reduces exactly to

```
-1680 zeta^2+1530 zeta-216
 =-6(280 zeta^2-255 zeta+36).
```

The bracket's derivative is560z-255>0 for z>=77/100, and at77/100 its value is

```
(83006-98175+18000)/500=2831/500>0.
```

Because zeta>77/100 and M^2>0, phi_u(u*,zeta)<0 strictly. Since phi(u*,zeta)=0, the definition of derivative makes phi(u,zeta)>0 for u<u* sufficiently close to u*. All nine other required quantities were strictly positive and remain so by continuity. This is a simultaneous ACTUAL feasible direction; it does not vary a numerator separately from the principal rates, drop D, or assume a new exit vector.

## 5. Ordered algebraic u0 and z_new, including every nonzero-polynomial issue — LF145-177

H is the product of L and the nine polynomial numerators Lp,Lq,Lw,LB,LC,Lphi,LD1,LD2,LD3. At z=zeta, the nine factors other than Lphi are strictly positive at u*. Also

```
partial_u(Lphi)(u*,zeta)=L(u*,zeta) phi_u(u*,zeta)!=0,
```

because phi itself vanishes there. Thus none of the ten factors is identically zero in u. Their product is a NONZERO polynomial over the algebraic field Q(zeta), so it has finitely many real roots. This step is essential: without it the maximum/root-gap definition would not be justified.

The set defining u_left includes1 and only roots strictly below3/2. It is nonempty and finite; therefore `1<=u_left<3/2`, and its midpoint u0 satisfies `1<u0<3/2`. There is no H root in `(u_left,3/2)`. The nine initially positive factors remain positive there by continuity and absence of zeros. The remaining Lphi is positive immediately on the left of3/2 by Section4 and L>0, hence remains positive on the SAME entire interval. This is an individual-factor sign argument, not the invalid assertion that a positive PRODUCT implies every factor positive. In particular all actual rational quantities at(u0,zeta) have the required signs.

All roots used in u_left are algebraic: a root over Q(zeta) is algebraic over Q. Finite ordering, taking a maximum and forming the midpoint therefore define a definite algebraic u0; no unevaluated positivity assumption is hidden in its definition.

Now H(u0,zeta)>0. Thus H(u0,z), with algebraic coefficients, is also a nonzero polynomial, with finitely many real roots. The set defining z_right includes8/9 and all roots in `(zeta,8/9]`, so it is finite/nonempty and has a minimum strictly greater than zeta. Therefore

```
zeta<z_new=(zeta+z_right)/2<z_right<=8/9.
```

These numbers are algebraic for the same field argument. No factor vanishes on the CLOSED interval `[zeta,z_new]`, since H was positive at zeta and z_new lies strictly before the first allowed root. Each factor therefore preserves its individually established positive sign throughout this entire closed interval. Division by the positive L gives all ten literal inequalities claimed at LF175. The fallback bound8/9 causes no failure when there is no intervening root; the midpoint is still strictly below8/9.

Accordingly u0 and z_new are fully specified exact parameters, not a promise to choose a small epsilon later. This conclusion does not numerically locate them, give a rational lower increment, prove maximality, or supply a finite interpreter/root-isolation certificate. None is needed for this written existence construction.

## 6. Actual PH pair and exact-order composition — LF181-201

For the fixed algebraic u0 and EVERY z in the closed extension interval, the actual G is Metzler and beta,gamma are nonnegative. The reconstructed determinant is D_z Q. Since p,q>0, Q's roots have negative real parts; the visible roots after subtracting cI are -c and the double pair `-(c+1)+/-i sqrt(z)`. All seven eigenvalues of G-cI are strictly stable for every c>0, including possible pole coincidences. The raw transfer is the exact rational identity KQ/(D_z Q)=K/D_z, not finitely many evaluated frequencies.

Every phase reaches state7 through the actual positive forward chain. The nonnegative semigroup integral therefore gives h=(-M)^(-1)gamma>0, and the exact diagonal similarity supplies

```
T1=-diag(h)^(-1)gamma,
alpha1=beta h=K/D_z(c)=1.
```

The PH exit is the sole actual `K/h7` exit, not a freely selected boundary. Every positive/backward/central feedback is merely rescaled by positive h ratios, so no literal nonzero feedback of the chosen family is lost during normalization. For a completely explicit normalization interface,

```
h_R=(1,c+u0,(c+u0)^2)^T/Q(c),
h_o=(c+u0)^3/Q(c),
h7=(K+D3 h1+phi h_o)/(c+1),
h6=(h7+D2 h1)/(c+1),
h5=(h6+D1 h1)/(c+1).
```

The middle equation follows from the same reconstructed scalar determinant elimination. These are positive actual rational/algebraic expressions, and verify the claimed old-normalization interface with u replaced by u0.

Time scaling by d after construction at c/d gives the stated target for every c,d>0. The old band and new interval meet at their ACTUAL zeta point; hence they cover continuously through z_new. Conditional on the named topology-unrestricted B6 and old upper7 imports, the minimum is exactly7 on `1/2<z<=z_new`. This is a strict extension of an actual positive family beyond the old fixed-u cubic endpoint, not merely a necessary relaxation. Nevertheless z_new<8/9, so the requested unrestricted8/9 verdict remains NOT_PROVED/minimum{7,8}.

## 7. Reconstruction boundary and exact non-claims

**New load-bearing obligations NOT_RECONSTRUCTED: NONE.** Identity(A), rational denominator control, identity(B), its endpoint reduction and strict sign, both nonzero-polynomial/root-order arguments, all closed-interval signs, literal actual feedback, stability/transfer and PH normalization have complete written derivations above.

**Named imports:** the previous band source SHA256 `4e490052336693f7f65b1978820aafa600636c421f91a217015d05aeb4928a05`; the actual v30-A written review SHA256 `589654952d0268e5b43e356acae34c492dda14945543ab5bbe23f464a425bf18`; and B6 SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`. The old full-band exact-order imports keep their earlier assurance. The author's separate rational-fiber wording correction mentioned at LF20 is NOT reviewed here and is not a premise of this actual family. No time-reversal theorem is needed.

**Not claimed or exercised:** numerical evaluation of u0/z_new, a rational endpoint increment, interpreter/CAS verification, historical arithmetic replay, executable finite-certificate acceptance,8/9 PH7 witness, unrestricted separator, whole-orbit infeasibility, principal-block WLOG, formal/kernel/human/cross-vendor/novelty acceptance, new GO or96-hour closeout. Frozen predecessor computations and all source bytes remain unchanged; parent erratum v7 is binding.

No mathematical finding requires repair of this frozen packet at the stated scope. The0F/0M/0m verdict concerns this supplied written construction and its explicit imports only, not the full PH minimum-order target or process/novelty acceptance.
