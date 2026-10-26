# Sixteen exceptional negative parallel-leaf paw cores: exact written closure v1

Observed before creation: **2026-10-23T17:02:24-07:00**. PhysicsRQLS10. **Complete author-written candidate for the16-core residual**, not independently reconstructed. No program, arithmetic runtime, solver, enumeration, compilation or scientific execution. This is an additive successor to the residual status in `axial-negative-paw-fourth-order-v1.md` and carries its count erratum; earlier immutable snapshots are not rewritten.

## 1. The exact16, four representatives and only safe symmetries

Keep first C, rho_ax=(0,2,1,6,7,8,3,4,5), H={1,2}, b={3,6}, d={4,7}, e={5,8}. In the second negative parallel-leaf paw, H is pendant, k is hub, i is the vertical leaf in the horizontal H's nonzero column, and j is the other vertical leaf. Its geometric orientation data from the fourth-order paper satisfy

    heavy A1_ij=-2, light A1_ki=A1_kj=a0,
    pendant A1_Hk=p0,
    a0=h*d0, p0=-e0*d0.

The only previously unresolved cases are(b=i,a0=+1) or(b=j,a0=-1), hub k one of the two first diagonals, and p0,d0 independently±1. These are exactly16 literal second cores.

Normalize the **source grid only**, using its actual order8 point stabilizer, to r=1,a=1,b=2 in the old geometric display. This is legitimate: the eight parallel-leaf raw matchings are transitive under independent coordinate signs and coordinate interchange. It does not change rho_ax or assume a symmetry of an unknown delta.

A tuple p below means Q1_xy=-Q0_(p(x),p(y)). Let source H endpoints be3,4; source hub endpoints6,5; source i endpoints1,7; source j endpoints2,8. For positive orientation e0,d0,h use those orders; reverse the relevant order for negative orientation. Set e0=-p0*d0 and h=a0*d0. This gives all16 without enumerating.

The first literal y-reflection acts as

    (hub,p0,d0)→(same hub,-p0,-d0),

and the first x-reflection as

    (d,p0,d0)→(e,-p0,d0), and conversely.

Both preserve the actual first C and rho_ax. Neither changes whether b=i or b=j, or the corresponding fixed a0. Thus each branch splits into two four-element orbits, represented by k=d,d0=+1,p0=±1. The four literal tuples are

    A+ (b=i,a0=+1,p0=+1): (0,4,3,1,6,2,7,5,8),
    A- (b=i,a0=+1,p0=-1): (0,3,4,1,6,2,7,5,8),
    B+ (b=j,a0=-1,p0=+1): (0,4,3,8,6,7,2,5,1),
    B- (b=j,a0=-1,p0=-1): (0,3,4,8,6,7,2,5,1).

Each is a genuine core from the same literal Paley class, not a fabricated Q block. If a positive-Q permutation form is desired, multiplication of the source field by1+alpha is a nonsquare and has tuple R=(0,4,8,5,6,1,7,2,3). Hence Q0_(R p(x),R p(y))=-Q0_(p(x),p(y)), so the negative notation is still a literal PC P^T input.

## 2. The exact raw entries and phase convention

Set u=w²=(-3+s)/4, v=w^-²=(-3-s)/4, s=i sqrt7. Thus uv=1, u+v=-3/2 and u-v=s/2. For any of the four p,

    M_it=conjugate(C_ti)*conjugate(C_(p(t),p(rho i))).

It is0 at t=i or t=rho i, and otherwise1,u or v. Write z in ker M. The row equations used below are displayed explicitly so that the exclusions are reconstructible on the source tuples. The unknown z remains completely arbitrary complex until a unit norm is explicitly invoked. Write t=z0; a phase vector necessarily has |t|=1.

## 3. A+: all kernel vectors have z0=0

The following six raw rows are necessary:

    R1: v*t+u(z3+z5+z6+z8)+v(z4+z7)=0,
    R2: t+z3+u*z4+z5+z6+z7+z8=0,
    R3: t+z1+u*z2+v*z4+z5+u*z7+z8=0,
    R6: v*t+z1+u*z2+u*z4+z5+z7+z8=0,
    R5: u*t+u*z1+z2+z3+v*z4+z6+z7=0,
    R8: t+u*z1+z2+z3+u*z4+z6+v*z7=0.

R3-R6 and R5-R8 give, respectively,

    (1-v)t+(v-u)z4+(u-1)z7=0,
    (u-1)t+(v-u)z4+(1-v)z7=0.

Their difference forces z7=t because2-u-v=7/2≠0. Substitution then forces z4=t because u-v≠0. Let S=z3+z5+z6+z8. R1,R2 now read3v*t+u*S=0 and(u+2)t+S=0. Eliminating S gives

    -(7/2)(1+u)t=0.

Thus t=0. In particular no all-unit vector is possible. No rank, field or phase-symmetry hypothesis was required.

## 4. A-: a saturated unit triangle forces projective K phases

For A-, R3,R6 have u*z1+z2 in place of z1+u*z2, and R5,R8 are unchanged. Their same differences still force z4=z7=t. The two H rows are

    R1: t+z3+z4+u*z5+z6+v*z7+u*z8=0,
    R2: v*t+u*z3+z4+z5+u*z6+z7+z8=0.

With X=z3+z6 and Y=z5+z8, these give X=Y and

    X=Y=[(u-1/2)/(1+u)]t=[(1+3s)/4]t.

Assume an all-unit vector. The coefficient has squared modulus4. Equality in |z3+z6|≤2 and |z5+z8|≤2 therefore forces

    z3=z6=z5=z8=q*t,   q=(1+3s)/8, |q|=1.

This is the exact equality case of the triangle inequality, not a tiny-residual approximation. It used arbitrary complex phases.

Two remaining raw rows are

    R3: t+u*z1+z2+v*z4+z5+u*z7+z8=0,
    R0: v*z1+z2+v*z3+z4+z5+z6+u*z7+u*z8=0.

They reduce to

    u*z1+z2=(1/2-2q)t,
    v*z1+z2=-(1+u+q/2)t.

Since u-v≠0, both z1/t,z2/t lie in K=Q(s). All other normalized coordinates already lie in K. An all-unit kernel vector would therefore be projectively K-valued, which is impossible by the fixed-coordinate mod7 descent recalled in section8. This excludes A- with unrestricted complex phases.

## 5. B+: a forced hub norm37/16

The necessary raw rows are

    R1: v*t+u(z3+z5+z6+z8)+v(z4+z7)=0,
    R2: t+u*z3+u*z4+v*z5+u*z6+z7+v*z8=0,
    R3: v*t+u*z1+u*z2+z4+z5+z7+z8=0,
    R6: t+u*z1+u*z2+z4+z5+v*z7+z8=0,
    R5: t+z1+z2+z3+z4+z6+u*z7=0,
    R8: u*t+z1+z2+z3+z4+z6+z7=0.

R3-R6 gives z7=t. Write A=z1+z2, X=z3+z6, Y=z5+z8, B=z4. Rows3,5 then give

    Y=-B-(1+v)t-u*A,
    X=-B-(1+u)t-A.

Substituting into R2 yields(u+1)A=(13/4)t-vB. Substituting this into R1 gives

    (12+23u)t+2(1+6u)B=0,
    B=[(-45+7s)/32]t.

Its squared ratio is

    |B/t|²=(45²+7*7²)/32²=37/16,

not1. Since |t|=1 for every phase vector, the necessary hub entry cannot be a phase. This is a linear forced norm discrepancy, with no field restriction on the original z.

## 6. B-: a forced horizontal norm487/784

The raw rows needed here are

    R1: t+u*z3+z4+z5+u*z6+v*z7+z8=0,
    R2: v*t+u*z3+z4+z5+u*z6+z7+z8=0,
    R3: v*t+u*z1+u*z2+z4+z5+z7+z8=0,
    R5: t+u*z1+v*z2+z3+z4+z6+u*z7=0,
    R7: t+v*z1+u*z2+z3+z5+z6+z8=0,
    R0: v*z1+z2+z3+z4+u*z5+v*z6+u*z7+z8=0,
    R4: u*t+v*z1+z2+v*z3+z5+z6+u*z8=0.

R1-R2 immediately gives z7=t. Put A=z1+z2, X=z3+z6, Y=z5+z8, B=z4. Comparing R1 with R3 gives X=A. Rows3,5,7 then yield

    Y=-B-u*A-(1+v)t,
    A=-[(1+u-v)/(2+v)]t=-(6+7u)t/4,
    B=(v-u)z1+A-v*t.

The sum R0+R4, after substituting these identities, yields

    (4u+1)t-7(2+u)z1+(5-3u)A=0.

Therefore

    z1/t=-(94+65u)/[56(2+u)].

For real a,b, |a+b*u|²=a²+b²-(3/2)ab. Here the numerator norm is3896 and the denominator norm is6272, hence

    |z1/t|²=487/784≠1.

Again an arbitrary all-unit complex z is impossible. No assumption about its algebraic field or a prescribed phase alphabet was made.

## 7. Coverage of the residual, and no new execution

The four prototype cases cover two disjoint first-reflection orbits in each of the b=i and b=j branches. Each orbit has four members: g_y changes(p0,d0) to(-p0,-d0), while g_x changes the hub and p0 but not d0. Thus the four literal proofs close all16 residual cores. Their source-grid normalization was explicitly justified in section1 and used no first-orientation replacement.

There is consequently no remaining negative P core in the axial first-order residual split:32 closed by the nonzero fourth-order scalar;16 closed here. No new exact assay is needed or prepared for this residual. The old permanently superseded scientific source remains untouched and UNRUN. This result is author-written CANDIDATE until its own actual pinned reconstruction, not an asserted independent verification.

## 8. The projective K-phase lemma used only after genuine phase constraints

For completeness, the A- field step uses the following exact lemma, also needed by the axis S prototype. No all-unit vector in ker M is projectively K-valued for any rho of this fixed-point type1+2^4. Clear rational denominators to Z[s] and let the nine common positive integer norms be c. If7 divides c, each constant coefficient is divisible by7, and division of every entry a+b*s by s gives b-(a/7)s, still integral, with common norm c/7. Continue until7 does not divide c. Reduction of M modulo(s) is N. Its kernel is rho-odd: the fixed coordinate0 is zero. Hence the fixed entry's norm is divisible by7, contradiction. The process terminates because c is a positive integer decreasing by factors7.

The lemma alone is not an all-complex-phase obstruction. In A-, actual complex unit conditions first forced two saturated pair sums and then the remaining phases into K. In B± the contradiction was a forced exact norm instead. Confusing these logically different steps would overstate the result.

Combined with the complete T0/T1 and positive-P closures, this supplies the **new fixed-axial-orientation** local exclusion for every second PC P^T and every independent D/E. It does not establish that axial rho is WLOG, exclude other first orientations or conference classes, close all complex H0 lifts, or prove unrestricted maximal1-RQLS10 impossibility. Full target remains UNKNOWN.
