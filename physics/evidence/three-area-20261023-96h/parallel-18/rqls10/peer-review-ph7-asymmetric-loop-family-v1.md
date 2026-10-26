# v43-A — asymmetric-loop PH7 family: complete written reconstruction

**Reviewer:** PhysicsRQLS10-2 / physics-5. **Author:** MathResearch96h. Actual pre-write `/bin/date`: **Sun Oct 25 06:44:57 PDT 2026**.

**Verdict: 0 FATAL / 0 MAJOR / 0 MINOR for infeasibility of the ENTIRE CHOSEN literal p>7/2 family**, for every c>0 and arbitrary entrywise nonnegative r,f,Dback. Every load-bearing matrix, transfer, normalization and rational coefficient identity used in that family contradiction is derived below. No such identity remains NOT_RECONSTRUCTED.

This is NOT a theorem for all3+3 common matrices, all five representatives, arbitrary hidden quadratics or unrestricted PH7 at8/9. The prior fixed-pair compression obstruction is only prior exposure and is NOT a correctness premise here. No scientific program/interpreter/eval, symbolic program, enumeration, sampling, certificate replay, solver, nested agent or external CLI was used. Metadata hashes/clocks and literal source reading only.

## 1. Exact exposure and source coverage

Parent erratum v8 was read FIRST, ALL LF1–37. Its withdrawals of premature parent acceptance and complete-coverage claims are binding; it grants no new scientific permission.

The exposure ACK `peer-review-ph7-asymmetric-loop-family-ack-v1.json` was written BEFORE opening the proof body, at **Sun Oct 25 06:40:43 PDT 2026**.

- Manifest `peer-review-wave-eighteen-v43.json`, exact v43-A entry LF21–42: SHA256 `97cdf16df4713419ac41fa50741eab54667ae6033f68bd617f949bf3621787b6`.
- Packet receipt `peer-review-wave-eighteen-v43-packet-receipt-v1.json`, ALL LF1–39 read: SHA256 `3ec5b87eb2fb944c4b474bf17f5b2569781b42683e9908732ecc2eb08ece7638`; it records all-source-line/literal-roundtrip equality for v43-A.
- Full literal packet `peer-review-wave-v43-ph7-asymmetric-loop-family-sources-v1.md`, ALL LF1–220 read: SHA256 `81f33da704ee5140919254752e70c97909faab5517dbbf6f5e06dfac1cd1ab13`.
- **S**, the complete original source `mathematics/evidence/three-area-20261023-96h/parallel-18/phase-type/PH7-eight-ninths-asymmetric-loop-family-first-constraint-v1.md`, ALL LF1–213: SHA256 `51e91e72b24db78cb09b79ca95671ada2e90c65b2d871e754bb9fea07e455c4d`. Fresh metadata hashes match these pins.

Long/load-bearing packet lines additionally reread verbatim using `:raw`: LF18,43,63–69,87,95–101,105–117,136,143–149,153–182,192–220. Source S line numbers below are the original LF labels; packet line number is S LF+7. No omitted or truncated body is credited by inference.

The proof uses ordinary determinant/adjugate and Schur-complement identities, polynomial coefficient comparison, elementary real Hurwitz criteria for quadratics, positive semigroups/resolvents for Metzler matrices, and diagonal PH normalization. Relevant interfaces are reconstructed below. No prior finite table or unrelated review verdict is imported.

## 2. Literal blocks, input-derived hidden quadratic and target

### 2.1 Actual blocks, not WLOG principal matrices — S:17–62

The upstream block is

    A=[-3/2,1,0;2,-3/2,1;0,0,-3/2], b=e3,

and downstream

    F=[-1,1,0;0,-1,1;0,0,-1], t=e1.

All off-diagonal entries are nonnegative. The upstream two-cycle has product2, so A is not an Erlang block. Its eigenvalues are −3/2 and −3/2±sqrt(2), all negative since2<9/4; F has eigenvalue−1. This reconstructs the chosen-block assertions without claiming that every principal block has this form.

With p>7/2, w=p−7/2>0 and beta_R=(1/20,p−3,1), the full G and both boundaries are exactly

    G=[A b 0; r^T -w t^T; Dback f F],
    beta=(beta_R,0,0), gamma=K e7,

where EVERY entry of r,f,Dback is free nonnegative. Thus G is Metzler for all permitted feedback, and beta,gamma are nonnegative raw boundaries. They are not yet asserted normalized PH boundaries.

The target expansion follows from

    (y+1)²+8/9=y²+2y+17/9.

Squaring and multiplying by y gives

    D(y)=y⁵+4y⁴+(4+34/9)y³+(68/9)y²+(289/81)y
        =y⁵+4y⁴+(70/9)y³+(68/9)y²+(289/81)y.

K=D(c)>0 for c>0. These are polynomial identities for the whole parameter family, not point evaluations.

### 2.2 Deriving both adjugate boundaries — S:66–88

Write x=y+3/2. The upstream determinant is

    a_R=x(x²−2)
       =y³+(9/2)y²+(27/4−2)y+(27/8−3)
       =y³+(9/2)y²+(19/4)y+3/8.

The column v=(1,x,x²−2)^T satisfies `(yI−A)v=a_R b` componentwise: the first two residuals are x−x and −2+x²−(x²−2), while the last is x(x²−2). Therefore it is the ACTUAL adjugate column, with

    v=(1,y+3/2,y²+3y+1/4)^T.

For F, its upper-triangular inverse has first row `(1/(y+1),1/(y+1)²,1/(y+1)³)`, so

    a_S=(y+1)³, w_S=t^T adj(yI−F)=((y+1)²,y+1,1).

In particular w_S(K e3)=K. There are no independently chosen numerator weights in these formulas.

The initial polynomial is then forced by the SAME beta_R:

    beta_R v
      =y²+[(p−3)+3]y+[1/20+(3/2)(p−3)+1/4]
      =y²+p y+(3/2)p−21/5=:Q_p(y),

because 1/20+1/4=3/10 and 3/10−9/2=−21/5.

Put q=(3/2)p−21/5. For p>7/2, q>21/20>0. Also

    p²−4q=p²−6p+84/5=(p−3)²+39/5>0.

Thus both hidden roots are real and negative: their sum is −p<0 and product q>0. The family is different from the earlier fixed hidden quadratic: its constant at p=14/3 is 7−21/5=14/5, not6. This is a direct comparison only; no old quotient obstruction is used.

**Boundary verdict:** 0F/0M/0m.

## 3. Full feedback determinant and numerator from one matrix

This reconstructs S:88–94,121–129, including ALL r/f/Dback terms.

For generic y let R_y=yI−A and S_y=yI−F. Solve the resolvent equation for gamma using upstream vector X, bridge scalar U and downstream vector Z:

    R_y X=b U,
    S_y Z=Dback X+f U+K e3,
    (y+w)U=r^T X+t^T Z.

Hence X=(v/a_R)U and

    Z=S_y^(-1)[(Dback v/a_R+f)U+K e3].

The scalar Schur denominator is

    Psi=(y+w)−r^T v/a_R−w_S f/a_S−w_S Dback v/(a_R a_S).

Block elimination therefore gives the ENTIRE characteristic polynomial

    chi(y)=det(yI−G)=a_R a_S Psi
      =(y+w)a_R a_S−a_S r^T v−a_R w_S f−w_S Dback v.

There are no missing products of feedback parameters: the displayed block zero makes all three feedback contributions enter through this single bridge denominator. Generic invertibility of the monic principal polynomials is enough for the derivation; the resulting polynomial identity extends to all y and all permitted feedback.

The bridge right-hand side is K/a_S, so U=K a_R/chi and X=K v/chi. Thus the FULL scalar transfer is

    beta(yI−G)^(-1)gamma=K beta_R v/chi=K Q_p/chi.

Equality with the target K/D forces, by polynomial cross-multiplication with K nonzero,

    chi=D Q_p.

Conversely that identity yields the target transfer. No independent path-weight substitution, numerator assumption, or prior compression result is used.

Writing E=a_R a_S, the determinant requirement is exactly

    R_p:=(y+w)E−D Q_p
         =a_S r^T v+a_R w_S f+w_S Dback v.          (F)

**Boundary verdict:** 0F/0M/0m.

## 4. Conditional PH ties, including every initial and exit component — S:98–110

If chi=D Q_p held, G's visible roots would be0 and −1±i sqrt(8/9), with the specified multiplicities, together with the strictly negative hidden roots just derived. Therefore M=G−cI is Hurwitz for every c>0. It is Metzler by the literal off-diagonal signs.

The fixed forward path1->2->3->4->5->6->7 has positive rates. Hence every state reaches the gamma-supported final state. For a Metzler/Hurwitz M, `(-M)^(-1)=integral_0^infinity exp(Mt)dt` is nonnegative, and that path makes each component of h=(-M)^(-1)gamma strictly positive. The positive-semigroup fact can be seen by adding a sufficiently large scalar aI to make M+aI nonnegative and expanding its exponential series; each fixed path supplies a positive power entry.

With H=diag(h), set

    T=H^(-1)M H, alpha=beta H, omega=H^(-1)gamma.

Similarity preserves Hurwitzness, and positive diagonal similarity preserves off-diagonal nonnegativity. Also

    T1=−omega,
    alpha1=beta h=K Q_p(c)/[D(c)Q_p(c)]=K/D(c)=1.

Q_p(c)>0 because its coefficients are positive. Thus the initial probabilities are exactly `(h1/20,(p−3)h2,h3)` on states1,2,3 and zero elsewhere; the sole exit rate is K/h7 at state7. The normalized transfer is the same K/D(s+c).

These ties are valid CONDITIONAL on the common determinant identity, not an actual PH7 construction. The subsequent contradiction makes that identity impossible. No missing normalization can repair the contradiction, but arbitrary PH7 matrices outside this chosen family are not constrained by it.

**Boundary verdict:** 0F/0M/0m.

## 5. Full principal product and trace choice — S:114–129

The complete product E is derived by the following coefficient groups:

    [y⁶]E=1,
    [y⁵]E=3+9/2=15/2,
    [y⁴]E=3+27/2+19/4=85/4,
    [y³]E=1+27/2+57/4+3/8=233/8,
    [y²]E=9/2+57/4+9/8=159/8,
    [y]E=19/4+9/8=47/8,
    E(0)=3/8.

All are from multiplying the actual a_R by `(y+1)³`, not a copied target coefficient list.

The trace of G is `−(15/2+w)`; none of the free feedback entries is diagonal. Thus chi's degree-six coefficient is15/2+w. The degree-six coefficient of the monic target D Q_p is p+4. Their equality forces

    w=p+4−15/2=p−7/2.

Therefore R_p has degree at most five. Changing feedback cannot change this trace choice.

**Boundary verdict:** 0F/0M/0m.

## 6. Nonnegative generator cone and the coupled budget — S:129–142

Every coefficient of a_R,a_S,v and w_S is nonnegative as explicitly derived. Since r,f,Dback are arbitrary nonnegative ACTUAL matrix entries, every generator on the right of(F) has nonnegative coefficients in y.

Its degree structure is exact:

- The r_j generators a_S v_j have degrees3,4,5. Only r3 reaches degree five, with leading coefficient1 and constant `a_S(0)v3(0)=1/4`.
- The f_i generators a_R(w_S)_i have degrees5,4,3. Only f1 reaches degree five, with leading coefficient1 and constant `(3/8)*1=3/8`.
- A Dback_ij generator is `(w_S)_i v_j`, with degree at most2+2=4. Its constant is nonnegative; none contributes degree five.

Consequently(F) forces

    [y⁵]R_p=r3+f1,
    [y⁰]R_p >= r3/4+3f1/8 >= (r3+f1)/4,
    [y]R_p>=0.                                           (B)

This is one common-entry coupling. All zero-feedback boundaries are included: no division by r3,f1 or Dback occurs. Other feedback can only add nonnegative constants, and replacing leading mass r3 by f1 increases its constant cost. Thus adding any of the omitted-from-leading-degree entries cannot evade(B).

**Boundary verdict:** 0F/0M/0m.

## 7. Derivation of every rational coefficient in the contradiction

This reconstructs S:146–175 without programs or sampling. Write q=(3/2)p−21/5.

### 7.1 Leading degree five

    [y⁵](y+w)E=85/4+(15/2)(p−7/2)=−5+(15/2)p,
    [y⁵]D Q_p=q+4p+70/9=(11/2)p+161/45.

The constant161/45 is `−21/5+70/9=(-189+350)/45`. Therefore

    L:=[y⁵]R_p=2p−386/45,

since −5−161/45=−386/45.

### 7.2 Constant coefficient

D has zero constant, so

    C:=[y⁰]R_p=(3/8)w=3p/8−21/16.

### 7.3 Linear coefficient

    [y](y+w)E=3/8+(47/8)(p−7/2)=47p/8−323/16,
    [y]D Q_p=(289/81)q=(289/54)p−2023/135.

Here `289*21/(81*5)=2023/135`. The p coefficient difference is

    47/8−289/54=(1269−1156)/216=113/216,

and the constant difference is

    −323/16+2023/135=(-43605+32368)/2160=−11237/2160.

Hence

    [y]R_p=(1130p−11237)/2160.

Nonnegativity requires p>=11237/1130>9, since11237>9*1130.

### 7.4 Actual constant-versus-leading budget

Using the same C,L, not independent coefficient variables,

    C−L/4
      =3p/8−21/16−p/2+193/90
      =−p/8+(-945+1544)/720
      =(599−90p)/720.

Budget(B) requires p<=599/90<7, since599<7*90. The bounds p>9 and p<7 cannot both hold. This excludes EVERY p>7/2 with ANY permitted r,f,Dback and any c>0. It is not merely rejection of p10 or a subset of feedback supports.

**Boundary verdict for all rational coefficients and the entire-family contradiction:** 0F/0M/0m.

## 8. The p10 control: spectral screen passes, budget fails

This reconstructs S:179–207 exactly as a written substitution, not as sampled numerical evidence for the uniform proof.

At p10,

    q=15−21/5=54/5, w=13/2, beta_R=(1/20,7,1),
    -tr G=15/2+13/2=14=p+4.

Newton's identity applied to the target's first two coefficients gives

    tr G²=(p+4)²−2(q+4p+70/9)
          =p²−2q+4/9,

so at this point it is `100−108/5+4/9=(4500−972+20)/45=3548/45>0`.

The fixed diagonal-square contribution is

    3*(9/4)+3+(13/2)²=(27+12+169)/4=52.

The fixed upstream two-cycle contributes4. The only additional two-cycles pair b3 with r3 and t1 with f1; Dback has no opposite R-to-S block and all other b/t entries vanish. Thus the actual trace-square is `56+2(r3+f1)`. The leading equation asks for

    r3+f1=20−386/45=514/45,
    56+2*(514/45)=(2520+1028)/45=3548/45.

Hence the trace-square equation itself is consistent with nonnegative leading feedback. It does not assert that the full target characteristic is attainable.

The other displayed coefficients are

    [y]R=(11300−11237)/2160=63/2160=7/240>0,
    C=(3/8)*(13/2)=39/16>0,
    L/4=(514/45)/4=257/90.

Finally

    C−L/4=(1755−2056)/720=−301/720<0.

Thus all three displayed coefficient signs pass, but the actual coupled constant budget fails. This control genuinely distinguishes the new obstruction from a trace-square rejection or the previous fixed hidden pair.

**Boundary verdict:** 0F/0M/0m.

## 9. Scope, imports, explicit non-premises and disposition

The reconstructed theorem excludes exactly the source's chosen A,F,b,t,beta_R(p),w(p) with arbitrary nonnegative r,f,Dback. The nonnegative-generator proof is specific to these actual adjugates and cannot be transferred to arbitrary principal blocks. No assumption that Erlang blocks are WLOG was made; A in fact has a nontrivial asymmetric internal loop.

**NOT_RECONSTRUCTED here:** a universal infeasibility theorem for all3+3 common matrices, all five time-reversal representatives, different principal/input couplings or other hidden quadratics; the complete previous PH8/PH7 band manuscripts; and the full historical parent disposition cited at S:13. None is a correctness premise for the chosen-family proof. The earlier fixed-pair quotient result is likewise NOT imported into any step above. No load-bearing identity within the assigned new family is omitted.

The prior B6/upper8 imports retain minimum{7,8}; this review does not derive or improve that global boundary. Unrestricted PH7 at8/9 remains NOT_PROVED. No actual new PH7 witness, interval extension, all-orbit separator or broader no-go is supplied.

The whole chosen mechanism is infeasible at written level; merely redistributing its complete nonnegative feedback cone cannot repair it. Initial/exit/normalization ties were proved conditionally, not left as an implementation task. Parent integration remains separate, and no prior premature acceptance is backdated.

Same-harness cross-domain supplied-proof reconstruction only, not blind/human/cross-vendor, formal/kernel, executable-certificate or novelty acceptance. All author/frozen sources unchanged; no new GO or scientific permission.
