# v50-A — new PH7 coupling: broken old budget and complete quotient-cone closure

**Reviewer:** PhysicsRQLS10-2, physics-5. **Author:** MathResearch96h. Actual pre-write `/bin/date`: **Sun Oct 25 07:10:49 PDT 2026**.

**Verdict: 0 FATAL / 0 MAJOR / 0 MINOR at the ENTIRE stated selected principal/input-family scope**, for every p>3, C>=0, c>0 and all actual entrywise nonnegative r,f,Dback. The old one-quarter budget is genuinely invalid on the new generators. The new quotient-cone bounds and strictly negative original residual coefficient are reconstructed with their rational coefficients, not inherited from either closed family. No load-bearing identity in this chosen-family proof remains NOT_RECONSTRUCTED.

No scientific program, interpreter, eval, symbolic program, enumeration, sampling, certificate replay, solver, nested agent or external CLI was used. Metadata hashes/clocks and literal source reads only. This is same-harness genuinely cross-domain written reconstruction (physics reviewer, mathematics author), not parent/formal/human/cross-vendor acceptance or novelty clearance.

## 1. Exposure, pins and complete reading

Parent erratum v8 was read FIRST, ALL LF1–37. No premature parent acceptance or scientific-permission exception is used. The pre-body ACK `peer-review-ph7-new-coupling-cone-ack-v1.json` was written at **Sun Oct 25 07:07:12 PDT 2026**, BEFORE opening this proof body.

- Manifest `peer-review-wave-eighteen-v49-v50.json`, exact v50-A entry LF42–62: SHA256 `517acd36a632e251e8c11c38065ad3e3e40ba59e024ec37790540a4fa128a487`. The unrelated v49 entry is not part of this review.
- Packet receipt `peer-review-wave-eighteen-v49-v50-packet-receipt-v1.json`, ALL LF1–20 read: SHA256 `cc714690df12347f1aff968c16be6fef1c1263587298c505de469a6393c6d3f5`; its v50-A entry records all-source-line/literal-roundtrip equality.
- Literal packet `peer-review-wave-v50-a-ph7-new-coupling-cone-sources-v1.md`, ALL LF1–230: SHA256 `3a1b2d7e8b3983d4976b210c70669631703db7088987ecdbecf281f602f4cf92`.
- **S**, original complete source `mathematics/evidence/three-area-20261023-96h/parallel-18/phase-type/PH7-eight-ninths-new-coupling-quotient-cone-obstruction-v1.md`, ALL LF1–223: SHA256 `b9747a2eca32e476db1804c105511b0979efd4606b2217d1144b02c428e678ac`.
- **P**, the explicitly named premise record `checkpoint-010-new-coupling-premise-before-construction-v1.json` in that same author root, ALL LF1–28 read: fresh SHA256 `26b7d80b6d5450ffbdefd2415dce9cd66b6818f7c48e49b6ec4e8a54aa7529e4`.

All fresh source/packet metadata hashes match their frozen pins. Long/load-bearing packet lines were explicitly recovered with `:raw`: LF10,12,16–20,38,50–58,81–91,97–120,124–160,164–190,202–230. Source S line citations below use its original LF labels, not packet prefixes; packet line number is S LF+7.

P records the changed actual matrices/input and old-functional failure before the consolidated successor, with its quoted returned clock06:59:43; S quotes07:02:13. I reconstruct P's mathematical premise here. I do not independently attest original creation times merely from those fields or claim preregistration of the idea. P itself discloses preliminary written cofactor comparison and explicitly declines that preregistration claim.

## 2. Literal new principal/input data and actual adjugates

This reconstructs S:23–51,63–84 and P:11–24.

The chosen upstream block is

    A=[-1,1,0;9/10,-1,1;0,0,-2], b=e3,

and downstream

    F=[-1,1,0;0,-1,1;0,0,-1], t=e1.

A's internal two-cycle has product9/10 and its diagonal rates are1,1,2; its roots are−2 and−1±sqrt(9/10), all strictly negative. This is not the previous rate pattern or internal-loop product and is not an Erlang/WLOG principal block. F is Hurwitz Metzler.

Put X=y+1, a0=9/10 and J=X²−a0. Then

    J=y²+2y+1/10,
    a_R=det(yI−A)=(y+2)J
       =y³+4y²+(4+1/10)y+1/5
       =y³+4y²+(41/10)y+1/5.

The column v=(1,X,J)^T is the ACTUAL adjugate column: the first two residuals of `(yI−A)v` are X−X and −9/10+X²−J, while the third is(y+2)J. Therefore `(yI−A)v=a_R b`. For F,

    a_S=X³, w_S=t^T adj(yI−F)=(X²,X,1).

These are derived from the supplied matrices, not selected independently as polynomial generators.

For the actual beta_R=(C,p−2,1),

    beta_R v=C+(p−2)(y+1)+(y²+2y+1/10)
            =y²+p y+p−19/10+C=:Q(y).

Thus q=p−19/10+C>11/10 for p>3,C>=0. The quadratic is Hurwitz by p>0,q>0; no discriminant restriction is imposed or needed. Its roots may be real or nonreal.

**Boundary verdict:** 0F/0M/0m.

## 3. The frozen old-cone premise really breaks

This is the assigned checkpoint010 audit, S:17–49 and P:19–24. Evaluate the SAME linear functional

    ell_old(g)=[y⁰]g−(1/4)[y⁵]g

on the NEW generators. Both relevant generators are monic degree five:

    g_r3=a_S v3=X³ J,
    g_f1=a_R(w_S)_1=(y+2)J X².

At y=0, X=1 and J=1−9/10=1/10. Thus

    g_r3(0)=1/10,
    g_f1(0)=2*(1/10)=1/5,
    ell_old(g_r3)=1/10−1/4=−3/20,
    ell_old(g_f1)=1/5−1/4=−1/20.

These are exact coefficients in the ORIGINAL y basis, not a mistaken evaluation of the quotient coordinate X or J(0) in X. Since either generator by itself is allowed by a nonnegative actual feedback entry, the old functional is genuinely NOT nonnegative on the new whole generator cone. The old necessary budget R0>=R5/4 therefore cannot be reused.

The old input and trace formulas also do not survive: beta_R here forces q=p−19/10+C, with C a genuine extra initial coefficient; the six principal diagonal rates sum to7, not15/2. This validates the precise changed premise frozen in P. It is not evidence of a successful PH7 construction and does not by itself imply any replacement obstruction.

**Boundary verdict:** 0F/0M/0m.

## 4. Full common-matrix determinant, numerator, trace and PH ties

### 4.1 Every feedback retained — S:55–97

For the supplied full matrix

    G=[A b 0; r^T -w t^T; Dback f F],
    beta=(C,p−2,1,0,0,0,0), gamma=K e7,

take generic y and solve its resolvent equation using upstream vector U, center scalar u and downstream vector V. The three block equations give

    U=(v/a_R)u,
    V=(yI−F)^(-1)[(Dback v/a_R+f)u+K e3],
    (y+w)u=r^T U+t^T V.

The scalar Schur denominator is

    Psi=(y+w)−r^T v/a_R−w_S f/a_S
                −w_S Dback v/(a_R a_S).

Consequently the ENTIRE characteristic polynomial is

    chi=a_R a_S Psi
       =(y+w)a_R a_S−a_S r^T v−a_R w_S f−w_S Dback v.

The center forcing is K/a_S, so u=K a_R/chi and U=K v/chi. The scalar transfer is therefore EXACTLY `KQ/chi`. This derivation retains every r,f,Dback entry; no independent path-weight or zero-feedback substitution is made. The identity holds as a polynomial identity after the generic block elimination, not only where a principal block is nonsingular.

The target polynomial is independently expanded from `D=y(y²+2y+17/9)²`:

    D=y⁵+4y⁴+(70/9)y³+(68/9)y²+(289/81)y.

K=D(c)>0. Equality of the full transfer with K/D forces chi=DQ by cross-multiplication. Thus the same actual entries must satisfy

    R:=(y+w)a_R a_S−DQ
      =a_S r^T v+a_R w_S f+w_S Dback v.             (C)

The y⁶ characteristic coefficient is7+w, whereas DQ has coefficient p+4. Hence w=p−3 is FORCED by trace, not freely selected to fix another coefficient. In particular R has degree at most five.

### 4.2 Conditional PH normalization — S:99–113

For every allowed p,C, beta is nonnegative, including C=0, and gamma is nonnegative. The matrix is Metzler because all its off-diagonal entries, including all feedback, are nonnegative. If chi=DQ held, G's visible roots would be0 and−1±i sqrt(8/9) with the stated multiplicity, and Q's roots have negative real part. Thus M=G−cI is Hurwitz for every c>0.

Every state has a fixed positive forward path to state7. Therefore h=(-M)^(-1)gamma is strictly positive: the stable Metzler resolvent is the integral of its nonnegative semigroup, and each forward path supplies a positive matrix-power contribution. This uses an actual reachability-to-exit property of this common matrix, not arbitrary free PH boundaries.

With H=diag(h), `Tph=H^(-1)MH`, `alpha=beta H` and `omega=H^(-1)gamma` have the exact ties

    Tph1=−omega,
    alpha1=beta h=KQ(c)/[D(c)Q(c)]=1.

Here Q(c)>0. The initial probabilities are C h1,(p−2)h2,h3, allowing the first to be zero; the sole exit is K/h7 at state7. Positive diagonal similarity preserves the transfer. These statements are conditional on coefficient matching, not an existing PH7 witness. The contradiction below prevents that matching.

**Boundary verdict:** 0F/0M/0m.

## 5. Reconstructing ALL15 generator remainders

This reconstructs S:117–137 without evaluating at roots or running a polynomial program. Work in the REAL quotient algebra `R[X]/(X²−a0)`, with unique coefficient basis(1,X). The defining substitutions are

    J=0, X²=a0, X³=a0 X, X⁴=a0²,
    a0=9/10, a0²=81/100.

The baseline `(y+w)a_R a_S` vanishes because a_R=(X+1)J. All three f generators vanish for the same reason.

For r, the actual factors a_S v_j are `(X³,X⁴,X³J)`. Their remainders are respectively

    (9/10)X, 81/100, 0.

The NINE Dback generators are the outer-product entries `(w_S)_i v_j`, so BEFORE reduction their matrix is

    [X², X³, X²J;
     X,  X², XJ;
     1,  X,  J].

Applying only the displayed quotient relations gives

    [9/10, (9/10)X, 0;
     X,     9/10,   0;
     1,     X,      0].

This derives each table entry from its actual row/column factor and retains every actual coefficient. In particular, writing the remainder of the right side of(C) as U+VX,

    U=(81/100)r2+(9/10)(Dback_11+Dback_22)+Dback_31>=0,
    V=(9/10)r1+(9/10)Dback_12+Dback_21+Dback_32>=0.

r3, all f entries and the third Dback column have zero remainders; they have not been suppressed in the original determinant identity. As a quotient cone ALONE, its image is exactly the nonnegative quadrant, since Dback_31 and Dback_21 independently provide1 and X. This does not imply the original polynomial matching is feasible.

The cone order used here is componentwise in the basis(1,X). It is NOT an unsupported claim of pointwise positivity at both roots of J, nor a finite numerical evaluation.

**Boundary verdict:** 0F/0M/0m.

## 6. Deriving BOTH new input bounds, not assuming the constructive window

This reconstructs S:139–153. In X coordinates,

    D=(X−1)(X²+8/9)²,
    Q=J+B X+C, B=p−2>1.

Set

    L=a0+8/9=(81+80)/90=161/90,
    L²=25921/8100>0.

Modulo J, D becomes L²(X−1), Q becomes BX+C, and the baseline vanishes. Therefore

    R=-L²(X−1)(BX+C) modulo J.

The product before its final reduction is `BX²+(C−B)X−C`, so

    R mod J=L²[(C−a0 B)+(B−C)X].

Both actual generator coordinates in Section5 are nonnegative. Dividing by the POSITIVE L² therefore yields the two necessary inequalities

    (9/10)(p−2)<=C<=p−2.                           (I)

The upper bound is newly DERIVED, not borrowed from P's chosen constructive window0<=C<=p−2. The proof consequently covers the full originally stated p>3,C>=0 family. Boundaries with one remainder coordinate zero are included; no coefficient or feedback entry is divided out.

**Boundary verdict:** 0F/0M/0m.

## 7. Original-coefficient contradiction and every rational constant

This reconstructs S:157–183. In the ORIGINAL y coordinate,

    a_R=y³+4y²+(41/10)y+1/5,
    a_S=(y+1)³,
    v=(1,y+1,y²+2y+1/10),
    w_S=((y+1)²,y+1,1).

Every polynomial here has nonnegative coefficients. Thus the SAME actual nonnegative feedback requires every coefficient of R, in particular[y]R, nonnegative. This original-basis statement is separately justified; it does not follow merely by declaring the quotient remainder positive.

For E=a_R a_S,

    E(0)=1/5,
    [y]E=41/10+3/5=47/10.

Since D has zero constant and[y]D=289/81,

    [y]R=1/5+(47/10)(p−3)−(289/81)q
         =(47p−139)/10−(289/81)q,
    q=p−19/10+C.

The lower bound in(I) gives

    q >= p−19/10+(9/10)(p−2)=(19p−37)/10.

Multiplication by the NEGATIVE coefficient −289/81 reverses the inequality in the needed direction:

    [y]R <= [81(47p−139)−289(19p−37)]/810.

The numerator groups are

    81*47=3807, 289*19=5491, 3807−5491=−1684,
    −81*139+289*37=−11259+10693=−566.

Therefore

    [y]R <= −(1684p+566)/810 < 0

for EVERY p>3, contradicting the original generator coefficient requirement. This is the complete new selected-family closure. Zero r/f/Dback entries and C at either boundary of(I) do not remove the strict contradiction.

**Boundary verdict:** 0F/0M/0m. No rational coefficient or sign-direction step in the main contradiction is left unreconstructed.

## 8. Literal p10 control and the weaker valid budget

This reconstructs S:189–215 as written identities, not as sampled evidence for the preceding uniform proof.

For reference, the complete principal product is obtained from its coefficient groups:

    E=y⁶+(3+4)y⁵+(3+12+41/10)y⁴
      +(1+12+123/10+1/5)y³
      +(4+123/10+3/5)y²+(41/10+3/5)y+1/5
     =y⁶+7y⁵+(191/10)y⁴+(51/2)y³
        +(169/10)y²+(47/10)y+1/5.

Thus the degree-five residual is

    [y⁵]R=191/10+7(p−3)−[q+4p+70/9]
          =2p−C−70/9,

and its constant is(p−3)/5.

At p10,C=1/10,

    B=8, q=10−19/10+1/10=41/5, w=7,
    beta_R=(1/10,8,1), -tr G=7+7=14.

The target trace-square from its first two characteristic coefficients is `p²−2q+4/9`, giving

    100−82/5+4/9=(4500−738+20)/45=3782/45.

The actual fixed diagonal-square contribution is1+1+4+3+49=58; the fixed upstream two-cycle contributes2*(9/10)=9/5. Only r3 and f1 can contribute additional two-cycles through their unit forward partners. The leading coefficient is

    20−1/10−70/9=(1791−700)/90=1091/90,

and hence

    58+9/5+2*(1091/90)=(2610+81+1091)/45=3782/45.

Trace and trace-square are compatible with nonnegative leading feedback, but do not establish full coefficient matching.

The ordinary linear coefficient is also positive:

    [y]R=331/10−(289/81)(41/5)
         =(26811−23698)/810=3113/810.

There is a WEAKER valid constant/leading budget of1/10: the only degree-five generators have constants1/10 and1/5, while all other generators have lower degree and nonnegative constants. Thus R0>=R5/10. At this control,

    R0−R5/10=7/5−1091/900=(1260−1091)/900=169/900>0.

The invalid old1/4 budget cannot be used as a necessary rejection test. Its failure on generators, not a favorable test of it at this point, is what permits a genuinely different attempt.

The NEW quotient constant coordinate instead is

    C−a0 B=1/10−(9/10)*8=−71/10<0.

Repairing that coordinate demands C>=36/5. Then the uniform inequality of Section7 makes[y]R strictly negative. No redistribution among the full feedback entries, or adjustment of C, repairs this selected coupling.

**Boundary verdict:** 0F/0M/0m.

## 9. No hidden inheritance and precise final scope

The fixed-pair PH8 quotient obstruction is not used anywhere above. No forbidden-spectrum assertion, real-eigenvalue deletion or similarity repair is a premise. The earlier asymmetric-loop family's coefficients and one-quarter budget likewise are NOT correctness premises: that budget is explicitly false here, the upstream adjugate constants and trace have changed, and the input constant C is a genuine additional initial coefficient. The new proof derives a distinct two-coordinate cone and combines it with an original-y coefficient.

A coincidence of an isolated hidden quadratic with some earlier family would not constitute a reused proof; no claim that all sets of quadratic polynomials are disjoint is needed. The actual chosen common matrix and its feedback generator cone, not a quadratic label alone, determine this argument. The p10,C1/10 quadratic differs from the cited closed examples.

**NOT_RECONSTRUCTED / outside this review:** infeasibility of arbitrary3+3 principal blocks, different forward boundaries or initial polynomials, all five time-reversal representatives, arbitrary PH7 hidden quadratics, or the complete prior B6/upper8 proofs. None is an omitted load-bearing premise of this chosen-family contradiction. Historical acceptance/creation chronology beyond the actual read records is not independently certified.

The theorem closes precisely this selected A/F/b/t/beta(p,C) family with p>3,C>=0 and ALL nonnegative actual feedback. It is not a PH7 witness or an unrestricted8/9 no-go. The minimum set{7,8} remains at its named prior import boundary, and unrestricted8/9 remains NOT_PROVED.

Parent integration remains separate. No former premature acceptance is backdated, no historical unadmitted computation gains credit, and no new scientific GO is implied. All frozen author sources remain unchanged.
