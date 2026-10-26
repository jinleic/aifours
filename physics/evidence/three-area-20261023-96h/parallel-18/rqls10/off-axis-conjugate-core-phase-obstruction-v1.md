# Off-axis first matching, conjugate second core: an exact rank5 torus obstruction v1

PhysicsRQLS10, same physics-5 primary. **Complete author-written candidate for this literal second-core subcase**, not the whole new all-P orientation. No scientific execution, arithmetic interpreter, solver, enumeration, compilation, control or CLI was used. All arithmetic below is printed written algebra; it is not a formal/kernel or exercised-program certificate. Stage clock observed before derivation:2026-10-24T04:01:18-07:00.

## 1. Actual input, full complex phase freedom and actual low rank

Keep C=(J-I+sQ0)/sqrt8 on the original F9 labels, s=i sqrt7, and

    rho=(0,7,8,6,5,4,3,1,2),
    H={4,5}, J={3,6}, U={1,7}, V={2,8}.

The companion first-block freeze gives the actual rank3 mixed Q0 block and proves this first matching is outside the supported central/axial/conjugate-axial orbit. Select the **genuine literal** second core C'=conjugate(C). It is C_R for the nonsquare multiplication R, not another unclassified conference matrix.

The necessary equation is

    M*delta=0,
    M_(i,t)=conjugate(C_(t,i))*conjugate(C_(t,rho(i))),
    EVERY |delta_t|=1.

Rows i and rho(i) coincide. Hence rank M≤5. Its reduction N has rank5 over F7, so actual rank M=5 and dim_C ker M=4. The usual rank8 obstruction does NOT apply; no projectively K-valued, real, symmetric or finite-alphabet phase assumption will be made.

## 2. Exact full-kernel equations under a literal common reflection

The first x-reflection g(x,y)=(-x,y) preserves both literal cores and commutes with rho, so M commutes with g. Normalize only the harmless global phase delta0=1. Write its g-even part as

    delta3=a, delta6=b,
    c=(delta4+delta5)/2,
    d=(delta1+delta2)/2,
    e=(delta7+delta8)/2.

The fixed physical coordinates a,b retain modulus1. The means c,d,e are NOT assumed unit, nor is the whole delta assumed invariant. Its g-odd part is

    alpha=(delta4-delta5)/2,
    beta=(delta1-delta2)/2,
    gamma=(delta7-delta8)/2.

The five raw-row representative equations split into four even equations and one odd equation. Put

    u=(-3+s)/4, v=(-3-s)/4,
    uv=1, u+v=-3/2, u-v=s/2.

The even equations, from rows0,H,J,U, are

    v(a+b)+2u*c+2v*d+2u*e=0,
    u+v*a+u*b+2d+2e=0,
    v+2c+2u*d+2e=0,
    1+u*a+b+(u+v)c+d+e=0.                        (1)

The odd row U gives exactly

    beta+gamma=-(s/2)*alpha.                      (2)

For example in that row the H coordinates have coefficients v,u and the opposite-column U/V coordinates have coefficient1, giving(v-u)alpha-beta-gamma=0. All equations are from the literal character-neighbour rule, not an auxiliary coefficient ansatz.

The physical pair-unit conditions imply

    |c|²+|alpha|²=1, Re(conjugate(c)*alpha)=0,
    |d|²+|beta|²=1,  Re(conjugate(d)*beta)=0,
    |e|²+|gamma|²=1, Re(conjugate(e)*gamma)=0.      (3)

Equations(2),(3) retain the g-odd freedom; averaging alone is not an exclusion.

## 3. What the two fixed unit coordinates force

Let L=26+2u. Eliminating(1) gives

    (11-16u)+(33+30u)*a+(26+2u)*b=0.               (4)

The three means are the following exact affine expressions in a:

    c=[16(1+u)-21a]/L,
    d=[(29+62u)-7(29+6u)a]/(14L),
    e=[(97+22u)+14(18+10u)a]/(14L).               (5)

These can be checked without a large inverse: first use

    d+e=-[u+v*a+u*b]/2,
    c=(2/3)[1+u*a+b+d+e],

then the other two even rows. In particular(4),(5) do not constrain a to K.

For verification of the actual unit reduction, write r0=11-16u,r1=33+30u,r2=L. Their norms are641,504,602, respectively, and

    conjugate(r0)*r1=675+858u=(63+429s)/2.

Since |a|=|b|=1, equation(4) implies

    Re[(675+858u)a]=-543/2.

Write a=x+(z/7)s, with x=Re a and z=sqrt7*Im a real. Thus

    63x-429z=-543,
    z=(181+21x)/143,
    x²+z²/7=1.

Consequently x is a root of

    P(x)=71792x²+3801x-55191.                     (6)

This quadratic is irreducible over Q. Its discriminant is143²*775761, and

    880²=774400 <775761<776161=881².

Thus neither physical root x is rational. This is an exact irrationality statement, not a search miss or a prescribed phase field.

## 4. A necessary paired-unit invariant not visible to the linear kernel rank

Define the real quantities

    D=|d|², E=|e|²,
    A=Re(conjugate(c)*d), B=Re(conjugate(c)*e).

Any full physical phase vector satisfying(2),(3) must obey

    F=A²*E*(1-D)-B²*D*(1-E)=0.                    (7)

Proof: if d or e is zero, (7) holds identically since respectively(A,D) or(B,E) is zero. Otherwise perpendicularity in(3) gives beta=i*k*d and gamma=i*l*e for real k,l, with k²=(1-D)/D and l²=(1-E)/E. Also conjugate(c)*alpha is purely imaginary; since s is purely imaginary, conjugate(c)*[-s*alpha/2] is real. Taking imaginary parts of conjugate(c) times(2) therefore gives

    k*A+l*B=0.

Squaring and inserting the two norm conditions proves(7). No choice of the odd-part signs or a reality condition on the original phases was imposed. If c=0 the same formula remains trivially necessary.

After substituting(5) and a=x+[(181+21x)/(7*143)]s, the expression F is a rational polynomial in x, up to constant denominators. Conjugation fixes x and sends s to-s, so every norm and real part has rational coefficients. All these constant denominators are units at5: they arise from2,7,14,143 and the fixed nonzero norm |L|²=602. No denominator depending on x is introduced.

If a physical phase vector existed, its real x would satisfy both P(x)=0 and F(x)=0. Since P is irreducible over Q, this would force P to divide F over Q (after clearing the constant denominators).

## 5. Small exact residue certificate that P does NOT divide F

This last divisibility is false, witnessed by a single written residue computation. Work in

    F5[s]/(s²-3),   conjugation s→-s.

The quadratic s²-3 is irreducible over F5. All preceding constant denominators remain invertible. The leading coefficient of P is2 modulo5, so polynomial division by P also preserves coefficients localized at5. Therefore divisibility over Q would imply divisibility after this reduction.

The reduction of P is2x²+x+4. At x=3 it is25=0. At this same residue point,

    z/7=4,  a=3+4s,
    u=3+4s, v=3+s,
    L=2+3s, L^-1=1+s.

In particular a=u and u²=u-1. Direct substitution into(5) now gives

    c=1+s, d=4, e=3.

For transparency: modulo5 the c numerator is1+u-a=1; the d numerator becomes L while its denominator is4L, so d=1/4=4; the e numerator becomes2L with the same denominator4L, so e=1/2=3. Hence the residue values in(7) are

    D=1, E=4, A=4, B=3,
    F=4²*4*(1-1)-3²*1*(1-4)=27=2 (mod5),

which is nonzero. Thus P cannot divide F over Q. Irreducibility of P was essential: a common modular root alone would not settle the characteristic-zero question, but a root of the reduced P where F is nonzero disproves divisibility, and every characteristic-zero common root would force that divisibility.

This contradicts the necessary consequence of a physical phase vector. Therefore the ENTIRE four-dimensional complex kernel of this actual rank5 matrix contains **no** all-coordinate-unit vector.

## 6. Scope and exact remaining obligation

This closes C'=conjugate(C) for the genuinely uncovered rho_off, with all arbitrary complex phases and all independent compatibility D/E. It uses the actual rank3 first mixed block and a new paired-unit invariant; neither rank8 nor a hidden K-phase restriction could close this case by itself.

It is one literal second core (with many duplicate permutation representations), NOT all5040 second cores. No multiplicity of those representations is counted as new closures or separate scientific problems. Other second cores remain part of the all-P orientation-level target and require actual further analysis. An exact surviving kernel, if found elsewhere, would still need all other conference magnitudes and global QLS compatibility; zeros are only necessary.

The calculation is a complete written candidate, pending its own actual reconstruction. No program or finite assay was executed to confirm it, no formal/kernel verification is claimed, and no novelty/publication/full-H0 or unrestricted maximal1-RQLS10 verdict follows. Existing central, corrected axial and monomial-bridge supports retain their exact scopes and all prior errata/history.
