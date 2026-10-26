# A sharp unrestricted six-state barrier for H_{1,2}

Before-creation clock observed: **2026-10-23T14:23:02-07:00**. Owner: `MathResearch96h`, slotmath-1. Status: **CANDIDATE / NOVELTY_UNCLEAR**, requiring a separate complete reconstruction. This proof makes NO constant-diagonal, companion, graph-layer or irreducibility assumption on the proposed PH6. No scientific program, sample matrix, symbolic-algebra execution or numerical root calculation was used.

The new lever is geometric-mean symmetrization of a real Metzler matrix: it preserves the first two traces and can only lower the third trace. This upgrades the earlier uniform-rate and heterogeneity arguments to an unrestricted moment obstruction. It is not asserted as a new general matrix inequality or a priority-cleared discovery.

## 1. Exact theorem and consequential bridge

Let a>c>0,b>0,d=a-c,beta=b/d and

    H(s)=K/D5(s),
    K=c(a^2+b^2)^2,
    D5(s)=(s+c)((s+a)^2+b^2)^2.

**Candidate theorem B6.** H has a PH representation with at most six transient states if and only if

    beta^2<=1/2.

The upper direction is the already written-checked explicit order5/6 construction in the operative baseline. The new lower direction below excludes **every** six-state PH topology above1/2.

**Endpoint rigidity.** At beta^2=1/2, every six-state PH representation has all holding rates lambda_i=-T_ii equal to a, its canceled real mode is-u=-(c+2d), and its off-diagonal graph contains no directed2cycle or3cycle.

**Candidate exact-order7 corollary.** Combining B6 with the separately written-checked G7 upper construction gives

    minimum unrestricted PH order=7
    whenever 1/2<beta^2<=53/96.

This is a genuinely unrestricted minimum7 conclusion IF the present proof survives review. It is NOT yet promoted. It does not determine minimum order above sqrt(53/96), the later PH/non-PH boundary or the general book problem.

## 2. A self-contained centered-Metzler third-moment inequality

**Lemma M.** Let X be any real n-by-n Metzler matrix with tr X=0, n>=2. Put tau2=tr(X^2). Then tau2>=0 and

    tr(X^3)>=-[(n-2)/sqrt(n(n-1))] tau2^(3/2).              (M)

For n6 the constant is4/sqrt30.

### 2.1 Geometric-mean symmetrization

Define the real symmetric matrix S by

    S_ii=X_ii,
    S_ij=S_ji=sqrt(X_ij X_ji) for i!=j.

The square roots are real because both off-diagonal entries are nonnegative. Direct expansion gives

    tr S=tr X=0,
    tr(S^2)=sum_i X_ii^2+sum_(i!=j)X_ij X_ji=tr(X^2).

In the cubic trace, the diagonal terms and all terms with exactly two distinct indices agree for X and S. For each unordered triple{i,j,k}, write

    A=X_ij X_jk X_ki>=0,
    B=X_ik X_kj X_ji>=0.

The X contribution is3(A+B), while the S contribution is6sqrt(AB). The arithmetic-geometric mean inequality gives3(A+B)>=6sqrt(AB). Hence

    tr(X^3)>=tr(S^3).                                    (2)

This is valid with zero entries, arbitrary real diagonals, reducibility and all feedback cycles. It is NOT a claim that X itself is nonnegative after centering.

### 2.2 Real zero-mean eigenvalue cubic bound

Let r_1,...,r_n be the real eigenvalues of symmetric S. Their sum is0 and sum r_i^2=tau2. If tau2=0 then S0 and(2) gives tr(X^3)>=0, so(M) holds.

For tau2>0 rescale to sum r_i^2=1. Minimize sum r_i^3 on the compact intersection of the unit sphere with sum r_i0. The constraint gradients are independent there. Lagrange multipliers give

    3r_i^2=lambda+2mu r_i,

so an extremum has at most two distinct values. One value alone would contradict sum0/norm1. If the negative value has multiplicity k and the positive value multiplicity n-k, the constraints give

    negative=-sqrt((n-k)/(nk)),
    positive= sqrt(k/(n(n-k))).

Their cubic sum is

    (2k-n)/sqrt(nk(n-k)).

The most negative value occurs at k1: for1<=k<=n/2 its squared magnitude is

    (1/n)[n^2/(k(n-k))-4],

maximized when k(n-k) is minimal, at k1. Thus the minimum is-(n-2)/sqrt(n(n-1)). Restoring tau2 gives tr(S^3) bounded below by the right side of(M). Combining with(2) proves the lemma completely, without an external theorem import or finite parameter check.

## 3. Characteristic binding and the accessible hidden real pole

A PH transform of N states has reduced denominator dividing det(sI-T). Therefore N>=5. At N5 its spectrum is-c once and-a±ib each twice. Shift by c and apply diagonal Cauchy plus nonnegative off-diagonal products:

    4(d^2-b^2)>=16d^2/5,

so beta^2<=1/5. In particular no order<=5 can occur when beta^2>=1/2.

Suppose now a six-state PH representation exists in that region. The characteristic polynomial is

    det(sI-T)=D5(s)(s+u)

for a real u>0. Any unreachable state could be deleted while preserving H, yielding at most5 states, impossible. Every state is therefore reachable from the positive initial support. Every transient state can reach a positive exit; otherwise a final nonabsorbing communicating class would force eigenvalue0.

Consequently the spectral abscissa of T is-c and u>=c. Here is the required positivity reasoning rather than an observability assumption: for a dominant irreducible diagonal block, the initial and exit factors in alpha exp(Tt0) and exp(Tt0)w are nonzero on that block for fixed t0>0. The semigroup paths remaining in the block and its positive Perron vectors give f(t+2t0)>=C exp(rho t) for large t. But the exact target density is asymptotic to

    [K/(d^2+b^2)^2]exp(-ct),

with the rest polynomial times exp(-at). Hence rho cannot exceed-c. Since-c is a pole/eigenvalue, rho=-c, and the extra real eigenvalue-u cannot lie to its right. This argument handles reducible generators and canceled noncritical modes without assuming every eigenvalue appears as a pole.

## 4. Mean-centered spectrum and forced sign of h

Let lambda_i=-T_ii and let mu=(sum_i lambda_i)/6. The characteristic trace gives

    6mu=c+4a+u.

Set

    h=mu-a, Delta=b^2-d^2/2>=0,
    X=T+mu I.

Then tr X=0 and

    u-c=2d+6h, h>=-d/3.

The six eigenvalues of X, including algebraic multiplicity, are

    d+h, -d-5h, h+ib twice, h-ib twice.

Thus

    tau2=tr(X^2)=12dh+30h^2-4Delta,                        (3)

    tau3=tr(X^3)=-12h R,
    R=d^2+6dh+10h^2+b^2.                                 (4)

These are exact trace expansions and require no diagonalizability. Because X is Metzler, tau2 is the squared-diagonal sum plus nonnegative reverse-edge products, hence tau2>=0.

If -d/3<=h<0, then12dh+30h^2=6h(2d+5h)<0, impossible. Hence h>=0. If Delta>0, h0 would also make tau2 negative, so

    Delta>0 implies h>0.                                 (5)

At Delta0 the possibilities are h0 or h>0; the latter is ruled out below as well.

## 5. The two cubic traces are incompatible when h>0

Assume h>0 and Delta>=0. Then R>0, tau3<0. Lemma M at n6 implies tau2>0 and

    12hR <= (4/sqrt30)tau2^(3/2).

Both sides are nonnegative, so squaring and rearranging gives the necessary inequality

    tau2^3>=270h^2 R^2.                                  (6)

Define

    tau20=12dh+30h^2=6h(2d+5h),
    R0=(3/2)d^2+6dh+10h^2.

Since Delta>=0, equations(3)/(4) give tau2<=tau20 and R>=R0. Direct written multiplication gives

    270h^2 R0^2-tau20^3
      =54h^2[(45/4)d^4+58d^3h+90d^2h^2] >0.             (7)

For transparency, after dividing by54h^2 the difference is

    5[(3/2)d^2+6dh+10h^2]^2-4h(2d+5h)^3
      =(45/4)d^4+58d^3h+90d^2h^2.

All coefficients are strictly positive for d,h>0. Therefore

    tau2^3<=tau20^3<270h^2 R0^2<=270h^2 R^2,

contradicting(6). This is a full symbolic identity/sign contradiction, not an inference from polynomial point evaluations.

It follows that h>0 is impossible whenever Delta>=0. For Delta>0 this contradicts(5), so no six-state PH representation exists. The already checked upper construction through Delta0 proves B6.

## 6. Endpoint rigidity without a diagonal ansatz

At Delta0, the preceding argument forces h0. Thus mu=a and u=c+2d. Equation(3) gives tau2=0. But

    tau2=sum_i X_ii^2+sum_(i!=j)X_ij X_ji,

a sum of nonnegative terms. Therefore every X_ii0, so every holding rate lambda_i equals a, and no directed2cycle has both positive edges. The now entrywise-nonnegative X has cubic trace0 by(4); its closed-walk expansion therefore forbids every positive directed3cycle. This proves the endpoint rigidity for arbitrary six-state topology, not only the old equal-rate companion.

The explicit six-state anchor at beta^2=1/2 indeed has lambda_i=a,u=c+2d and feedback cycles of lengths4and6, consistent with these conclusions.

## 7. Exact minimum7 in the previously constructed new band

G7 is the explicit PH7 construction on beta^2 in[1/2,53/96], immutable source SHA256 `59618311924521e8eceaa5179f837589aa2f1cd15955006aace5f39ee559fe4d`, with actual separate written review and parent support. Its positive coefficients, initial law, stable shifts and both canceled real modes are part of that baseline, not proved by the present lower bound.

For1/2<beta^2<=53/96, G7 gives upper7 and B6 excludes every representation of order<=6. Thus the unrestricted minimum is7, conditional only on correctness of this newly proposed barrier and the already checked explicit construction. The lower proof uses no Ellard–Smigoc or O'Cinneide existence theorem: its trimming asymptotic is the exact elementary inverse transform of H.

This closes the immediate residual six-versus-seven obligation if accepted, but not the full H_(1,2) minimum above sqrt(53/96), and not the full minimal-PH book question.

## 8. Relation to earlier packets, provenance and verification request

The earlier L6 layers, U6 uniform-rate exclusion and new-slot nonuniform-gap/HP6 packets were necessary partial restrictions on a hypothetical residual PH6. The present moment argument would show that class is empty. Those files and their review histories must remain intact; this is not retroactive acceptance or an erasure of the L6 minor qualification. In particular, a valid necessary heterogeneity condition can become vacuous once a stronger impossibility is proved.

The generic moment comparison in §2 is classical in mechanism and may have a known named equivalent. No novelty, first-result or major-contribution claim is made. The exact repeated-pole consequence needs a matched primary comparison in addition to correctness checking.

Independent check requested: reconstruct the geometric-mean symmetrization including all triangle terms; prove the symmetric zero-mean cubic bound with its n6constant; verify the hidden-mode trimming argument; rederive the mean-centered spectrum/traces; expand(7) coefficient by coefficient; check the strict/non-strict endpoint split and the G7 lower/upper bridge. No executable check is needed for this written packet; none is authorized or claimed. The parent verification/timestamp errata remain mandatory, and all formal/kernel/human/priority gates stay separate.
