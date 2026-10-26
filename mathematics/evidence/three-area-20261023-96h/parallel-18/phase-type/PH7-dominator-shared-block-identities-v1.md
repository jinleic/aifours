# PH7 at z=8/9: exact shared-block identities after the dominator freeze

Clock actually observed before creation: **2026-10-24T03:51:49-07:00**. MathResearch96h, math-1. Written algebra only; no scientific program, arithmetic code, import, compile, test, solver, enumeration, native launch, model CLI or nested agent.

This is a separate packet written **after** the dominator proof/block form was frozen at `PH7-dominator-normal-form-v1.md`, SHA256 `5e259982c3fe8f762acc0546080aa87afec405e0cbc34b00afc460f01b39f846`. Preliminary hand factorization exploration before that freeze was disclosed there and to the parent. Neither packet has an actual separate reconstruction at this freeze; both remain AUTHOR-WRITTEN CANDIDATES, not formal or novelty acceptance.

## 1. Actual target and new logical input

Fix c,d>0, a=c+d, b^2=8d^2/9 and

    D5(s)=(s+c)((s+a)^2+b^2)^2,
    K=D5(0)=c(a^2+b^2)^2.

The target is an actual seven-state PH pair with H(s)=K/D5(s), or a topology-unrestricted proof that none exists. The supported B6 and C8 boundaries leave the minimum at this point in{7,8}. **This packet does not settle which.** It supplies exact common-matrix equations, not another rate-gap increment, a new allowed upper order, or free path weights.

The new topology-unrestricted input is the preceding internal-dominator theorem. It puts every actual PH7 of relative degree5, after permutation, into

    T=[ A     b       0
        r^T  -lambda  t^T
        D     f       F ],
    alpha=(alpha_R,0,0), omega=(0,0,omega_S),     (1)

with m=dim A>=1,n=dim F>=1,m+n=6. A,F are Hurwitz Metzler principal blocks. The actual off-diagonal blocks b,r,t,D,f are nonnegative. The literal PH constraints include

    alpha_R>=0, alpha_R1=1,
    b=-A1>=0,
    lambda=r^T1+t^T1>0,
    omega_S=-D1-f-F1>=0.                        (2)

In particular omega_S is tied to D,f,F and cannot be selected independently. Neither D nor f is discarded.

## 2. The two boundary polynomials are defined from that same matrix

Put

    a_R(s)=det(sI_m-A), a_S(s)=det(sI_n-F),
    A#(s)=adj(sI_m-A), F#(s)=adj(sI_n-F),
    N_R(s)=alpha_R A#(s)b,
    N_S(s)=t^T F#(s)omega_S.                    (3)

These are literal polynomials in the entries of(1)-(2), not unknown positive-coefficient factors to be chosen separately.

For generic s where the principal resolvents exist, solve (sI-T)y=omega. Its first block gives

    y_R=(sI-A)^(-1)b y_o.

Its last block gives

    y_S=(sI-F)^(-1)omega_S
        +(sI-F)^(-1)[f+D(sI-A)^(-1)b]y_o.

The middle equation is therefore

    W(s)y_o=t^T(sI-F)^(-1)omega_S,

where the exact scalar feedback expression is

    W(s)=s+lambda-r^T(sI-A)^(-1)b
         -t^T(sI-F)^(-1)f
         -t^T(sI-F)^(-1)D(sI-A)^(-1)b.          (4)

The original scalar transfer is consequently

    alpha(sI-T)^(-1)omega
      =N_R(s)N_S(s)/[a_R(s)a_S(s)W(s)].         (5)

Ordinary block determinant elimination gives the complete characteristic polynomial

    P7(s)=(s+lambda)a_R(s)a_S(s)
          -a_S(s) r^T A#(s)b
          -a_R(s) t^T F#(s)f
          -t^T F#(s)D A#(s)b.                 (6)

Thus a_R a_S W=P7=det(sI-T). Equations(5)-(6), initially derived on an open resolvent domain, are rational/polynomial identities. They do not assume principal poles are distinct or avoid roots of the hidden quadratic. In particular the full adjugate numerator is exactly

    alpha adj(sI-T)omega=N_R(s)N_S(s).          (7)

The feedback term involving D is generally nonzero. Omitting it, or imposing a rank-one alignment not present in(1), would change the feasibility problem.

## 3. Positive numerator coefficients and exact normalization ties

Both N_R,N_S are nonzero polynomials with nonnegative coefficients and positive constant terms. Here is a direct reason, without treating them as independent data.

The positive simple-path/principal-minor identity applies to alpha_R adj(sI-A)b and to t^T adj(sI-F)omega_S. Each path coefficient is a nonnegative product of actual entries. Every complementary principal matrix of a Hurwitz Metzler principal block is Hurwitz; its real characteristic polynomial has positive coefficients, by factoring its real negative roots and conjugate left-half-plane pairs. Consequently each path contribution has nonnegative coefficients.

There is a positive pre-o and post-o segment on an original simple initial-to-exit path. The preceding normal-form proof showed that the pre segment lies in R and the post segment in S. Thus both polynomials are nonzero and their values at0 are positive.

More strongly, the actual pre-block row tie gives

    (-A)^(-1)b=1,
    N_R(0)=a_R(0).                             (8)

It is the first-hitting transform to o, normalized at0, not a freely scaled positive polynomial. For the other side,

    N_S(0)=a_S(0)t^T(-F)^(-1)omega_S>0.         (9)

Using all row ties in(2) also yields

    W(0)=t^T(-F)^(-1)omega_S,
    P7(0)=N_R(0)N_S(0).                        (10)

For example, substitute (-A)^(-1)b=1 into(4). Since lambda-r^T1=t^T1 and

    (-F)^(-1)omega_S=1-(-F)^(-1)(D1+f),

equation(10) follows exactly. This verifies that the global normalization is retained by the common-block equations, including the backwards returns.

## 4. Complete degree allocations of the hidden quadratic

Let delta_R be the shortest positive path length from I to o, and delta_S the shortest positive path length from o to E. The two segments stay respectively in R then S; conversely their shortest choices concatenate without sharing a vertex outside o. Therefore

    delta_R+delta_S=4,
    1<=delta_R<=m, 1<=delta_S<=n.               (11)

The first positive high-s coefficient of the two principal resolvents gives

    deg N_R=m-delta_R,
    deg N_S=n-delta_S,
    deg N_R+deg N_S=2.                          (12)

This can also be seen directly from the longest-degree path term: minimum edge length gives the highest polynomial degree, and its positive leading terms cannot cancel.

For an actual seven-state representation, write the real monic hidden factor Q2(s) so that

    P7(s)=D5(s)Q2(s).

Combining the actual transfer with(7) gives

    N_R(s)N_S(s)=K Q2(s).                       (13)

Equations(11)-(12) give the following complete integer allocation table. It is derived by these inequalities, not an automated topology enumeration:

| m | n | delta_R | delta_S | deg N_R | deg N_S |
|---:|---:|---:|---:|---:|---:|
|1|5|1|3|0|2|
|2|4|1|3|1|1|
|2|4|2|2|0|2|
|3|3|1|3|2|0|
|3|3|2|2|1|1|
|3|3|3|1|0|2|
|4|2|2|2|2|0|
|4|2|3|1|1|1|
|5|1|3|1|2|0|

If both degrees are1, each factor has positive leading and constant coefficients, so **both hidden roots are real and negative**. A genuinely nonreal hidden conjugate pair therefore has to occur wholly as the degree2 numerator on one side, with the other numerator constant. This covers the complex-hidden cases without silently deleting the real-hidden cases.

This is a statement about **numerator zeros**, not localization of hidden eigenvectors. In particular it does NOT say that Q2 divides a_R or a_S. The accepted C7 control below explicitly refutes that shortcut.

## 5. An exact topology-unrestricted common-matrix feasibility statement

For each fixed c,d>0 at z=8/9, an actual PH7 pair exists **if and only if** there are m,n and real blocks as in(1), with m+n=6, satisfying:

1. A,F Hurwitz Metzler; b,r,t,D,f nonnegative; lambda>0; alpha_R nonnegative with alpha_R1=1; the row ties(2) with omega_S nonnegative.
2. A real monic Hurwitz quadratic Q2(s)=s^2+p s+q, equivalently p>0,q>0. Its discriminant is unrestricted.
3. The entire coefficient identity(6) equals D5(s)Q2(s).
4. The entire product of the actual polynomials(3) equals K Q2(s).

Necessity is the normal form plus(3)-(13). For sufficiency, assemble the literal seven-by-seven T from those blocks. It is Metzler, its actual exit is (0,0,omega_S) by the row ties, and alpha is a probability row. The characteristic identity makes T Hurwitz because every root of D5Q2 is in the open left half-plane. Equations(5)-(7) give exactly K/D5, including the repeated nonreal poles and cancellation of the full Q2. Thus this is an actual PH pair, not a spectrum-only or scalar-weight certificate.

The monic D5/Q2 identities themselves enforce the required relative degree; no independent simple-path weights need to be assigned. All products, inverses used in derivation and final polynomials belong to that one matrix. The finite allocation table can be used to distinguish cases, but its rows are not asserted feasible.

The existence or inconsistency of this structured coefficient system at z=8/9 is **not resolved here**. This equivalence is an author-written exact reduction at the current candidate normal-form dependency, not a declaration that the matrix feasibility problem has been solved or that scalar polynomial factors suffice.

## 6. Actual C7 control checks both identities and forbids false localization

Use the supported z=31/49 C7 anchor and its exact blocks printed in the preceding normal-form packet. There m=n=3, o=4, A=F=J3 with diagonal-lambda and superdiagonal lambda. Thus

    a_R(s)=a_S(s)=(s+lambda)^3,
    Q2(s)=R(s+lambda),
    R(x)=x^2+12eta x+44eta^2,
    D0=R(lambda), eta=d/7.

Direct triangular resolution with b=(0,0,lambda)^T gives

    A#(s)b=(lambda^3,lambda^2(s+lambda),
                    lambda(s+lambda)^2)^T.

With the actual positive initial row this yields

    N_R(s)=(lambda^3/D0)Q2(s).

The actual t=(lambda,0,0)^T and omega_S=(0,0,K D0/lambda^6)^T give

    N_S(s)=K D0/lambda^3.

Their product is exactly K Q2, not a freely selected factorization. The row ties and actual nonzero D,f are those of the accepted PH matrix.

The characteristic formula(6) gives its actual polynomial with feedback terms of degrees3,2,1,0. In particular the term `a_R t^T F# f=f4(s+lambda)^3` is nonzero. Thus a purported universal reduction replacing all feedback by a constant would fail this actual control.

Also Q2 is a nonreal quadratic while a_R,a_S have only the real root-lambda. Hence **Q2 does not divide either principal characteristic polynomial**, despite occurring entirely in N_R. This supplies an explicit accepted one-matrix falsifier of the tempting inference from numerator cancellation to principal-eigenvalue localization.

For the supported PH8 anchor at z=8/9, the actual dominator is5, with m=4,n=3 and a hidden cubic. Its actual initial polynomial is degree3 upstream and constant downstream, not one of the seven-state degree2 allocations. The same general block elimination is consistent with that eight-state pair, but m+n=7 and the total numerator degree is3. It is not excluded by any seven-state quadratic statement here.

## 7. Additional actual same-matrix feedback control

There is another exact constraint that does not choose independent W,V,U. For any actual PH pair of this relative degree, alpha_i omega_i=0 at every coordinate. Therefore

    T_theta=T+theta omega alpha, theta>=0,

is Metzler and has **the same diagonal holding rates**. At theta=1 it has row sums0; for0<=theta<1 its exit is(1-theta)omega. The rank-one determinant identity gives

    det(sI-T_theta)=[D5(s)-theta K]Q2(s).        (14)

The hidden factor is the same actual Q2 for the entire feedback family. This is not a claim that arbitrary characteristic polynomials of that form are realizable.

At the target, all seven states of an actual pair are initial-reachable and exit-co-reachable by the named B6 trimming argument. For theta>0 the added edges from every exit phase to every positive initial phase make T_theta irreducible: go from any state to an exit, use the new edge to the required initial phase, then its original path to the destination. Consequently T_1 is an irreducible conservative seven-state generator. These are actual linked constraints, not a construction of T from its eigenvalues.

For theta<1 the same graph and a remaining positive killing probability make the subgenerator transient. Its transform is the exact geometric-regeneration expression

    H_theta(s)=(1-theta)H(s)/(1-theta H(s)).

No standalone feedback-spectrum test is claimed sufficient for the original realization. These identities retain alpha,T,omega as shared data throughout.

## 8. Point-specific real-root diagnostic and the first unproved step

At z=8/9, write y=s+a. Direct differentiation gives

    D5'(s)=(y^2+b^2)[5y^2-4dy+b^2]
           =(y^2+b^2)[5(y-2d/5)^2+4d^2/45]>0

for every real s. Thus D5 plus any real constant has exactly one real root. This is an exact scalar fact about the target, not a new PH lower bound.

It would be invalid to combine that fact with an unproved assertion that the full block equations force D5 plus a constant to have several real roots. Equations(6) and the accepted C7 control retain nonconstant feedback terms and backwards D coupling. Neither the dominator nor numerator factorization removes them. Likewise, locating Q2 in N_R or N_S does not locate its eigenvectors in a principal block.

The first unproved constraint is now explicit: **can any one of the common-block degree allocations satisfy both full polynomial identities with the row-sum and nonnegativity ties, in the necessary large-rate-slack region?** A successful actual block solution would give a PH7 pair and, with B6, exact minimum7 at this point. A contradiction must cover all these complete block cases, not just a companion family, a root-count shortcut or independently chosen positive factors.

There is no PH7 witness or topology-unrestricted PH7 exclusion here. The unresolved step is mathematical feasibility, not a missing file, quota/access gate or claimed exhaustion result. No new scientific execution is proposed. The parent may independently reconstruct the preceding normal form and these exact identities before using the new interface; novelty, formal verification and full minimum-order resolution remain separate.
