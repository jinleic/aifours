# PH7 at z=8/9: exact path coupling and a necessary holding-rate gap

Clock actually observed before creation: **2026-10-23T15:52:16-07:00**. MathResearch96h, math-1. Parent ACK froze this bounded lower-order attack before the derivation below. The general cofactor-path idea had earlier written exploration, as disclosed in that ACK. No mathematical program, enumeration, solver, CAS, model CLI, nested agent or proof assistant was used.

## 1. Literal target and result reached

Retain c>0, d=a-c>0, z=b^2/d^2 and

    K=c(a^2+b^2)^2,
    H(s)=K/[(s+c)((s+a)^2+b^2)^2].

The bounded target is **topology-unrestricted PH7 impossibility at z=8/9**. Supported C8 supplies a PH8 there, so such an impossibility proof would give exact minimum8 at this point. **That impossibility is not proved here.**

Two actual necessary facts are proved below, for arbitrary holding rates and real or complex hidden quadratic:

1. An exact nonnegative simple-path/principal-minor coupling for the hidden quadratic, with all weights bound to one actual PH pair.
2. At z=8/9, every PH7 representation would necessarily have

       max_i(-T_ii) -(1/7)sum_i(-T_ii) > d/25.     (G7-gap)

Thus all uniform-rate topologies and an explicit neighborhood of them are excluded. This is an unrestricted **necessary heterogeneity conclusion**, not an assumption of uniform holding rates or a failed-companion test. It does not exclude the remaining large-heterogeneity region or prove minimum8.

Status: **AUTHOR-WRITTEN CANDIDATE LOWER-ORDER CHECKPOINT**, pending actual separate reconstruction and parent disposition. Novelty unclear; the cofactor identity and Perron tools are classical in character. There is no new upper construction.

## 2. Degree, reachability, Perron binding and relative degree

Suppose a seven-state PH pair (alpha,T) has this H; let omega=-T1>=0. Since the reduced denominator has degree5,

    det(sI-T)=(s+c)((s+a)^2+b^2)^2 Q2(s),

where Q2 is real monic of degree2, including full algebraic multiplicities. Neither its roots nor its diagonalization are restricted in advance.

At z=8/9>1/2, the supported B6 theorem excludes any representation of order<=6. Hence no state of T is unreachable from alpha: trimming it would preserve H and leave at most6 states. Every state also reaches a positive exit, since otherwise a finite closed no-exit final class would force eigenvalue0, contrary to Hurwitz stability.

These positive reachability/co-reachability facts imply that the spectral abscissa is exactly -c. Indeed the inverse transform has leading term

    K/[(d^2+b^2)^2] * exp(-ct),

with all other terms degree-at-most-one polynomials times exp(-at). A dominant irreducible diagonal block of larger abscissa would yield a positive exponential lower contribution to the density: for fixed positive t0, the restricted row alpha exp(Tt0) and column exp(Tt0)omega dominate positive multiples of that block's Perron left/right vectors. Paths remaining in the block then give a positive constant times its Perron exponential, contradicting the displayed asymptotic. Since -c is an actual pole, the abscissa cannot be smaller either.

This is the same exact Perron/positive-asymptotic interface used in supported B6, not the false assertion that canceled modes must be observable. Irreducibility of the entire T is not needed below.

Write

    Q2(y-c)=y^2+p y+q.

The hidden eigenvalues after shifting T by c have nonpositive real parts; thus p,q>=0. Put x_i=-T_ii-c>=0 and t_ij=T_ij>=0 for i!=j. Every two-state principal minor obeys

    x_i x_j-t_ij t_ji>=0.                         (1)

One elementary justification: add a large scalar to L=T+cI to make it nonnegative. Its Perron root is that scalar; each principal nonnegative submatrix has no larger spectral radius. Thus each principal block of L has spectral abscissa<=0. A two-state Metzler block has real eigenvalues, so its determinant (1) is nonnegative. No claim of strictness or hidden real poles is used.

The large-s asymptotic H(s)=K/s^5+O(s^-6) gives alpha T^j omega=0 for j<4 and alpha T^4 omega=K. Choose Lambda>=max(-T_ii) and B=T+Lambda I>=0. The binomial expansion gives the same first four zeros for alpha B^j omega. Consequently every positive initial-to-exit path has at least4 edges and some has exactly4. A shortest such path has5 distinct vertices.

Let I=supp(alpha), E=supp(omega). They are disjoint. The three internal vertices of a shortest4-edge path lie in neither I nor E, since either membership would shorten the path. Therefore

    |I|+|E|<=4.                                  (2)

This bounds the actual boundary supports, not just a companion initial row.

## 3. Exact seven-state cofactor path identity

For a simple oriented path P=(i0,...,i_l) of distinct vertices, set

    a(P)=alpha_(i0) omega_(i_l) product_(k<l) t_(i_k,i_(k+1))>=0.

For any finite matrix T, the numerator has the identity

    alpha adj(sI-T) omega
      =sum_(simple paths P) a(P) det(sI-T_(V\P)).             (3)

Here a length0 path is allowed in the general identity, and the empty determinant is1. For completeness, expand the coefficient of u in det(sI-T+u omega alpha). Rank-one multilinearity makes this coefficient alpha adj(sI-T)omega. In a determinant permutation, the marked omega-alpha link closes a unique cycle; removing it leaves the oriented initial-to-exit simple path. The permutation sign of that cycle cancels the signs on its off-diagonal -t edges. All other cycles contribute exactly the complementary principal determinant. This proves (3), with positive path signs and no independence assumption on its weights.

There are no positive paths shorter than4. On7 vertices only lengths4,5,6 remain. Define

- W_ij: total a(P) over length4 paths omitting exactly the pair {i,j};
- V_i: total a(P) over length5 paths omitting exactly i;
- U: total a(P) over length6 Hamiltonian initial-to-exit paths.

All are nonnegative polynomials in the **same** T,alpha,omega. Replace s by y-c in (3) and compare its numerator K(y^2+p y+q). The complete coefficient identities are

    K=sum_(i<j) W_ij,
    Kp=sum_(i<j) W_ij(x_i+x_j)+sum_i V_i,
    Kq=sum_(i<j) W_ij(x_i x_j-t_ij t_ji)
         +sum_i V_i x_i+U.                       (4)

There are no omitted principal determinants: a length4 path leaves2 states, a length5 path leaves1, a length6 path leaves none. Equations (1),(4) make all displayed right-hand summands nonnegative. They also bind hidden cancellation to actual initial/exit couplings, which generic spectrum and centered moments do not do.

Crucially, replacing the W,V,U by independently chosen nonnegative scalars would be a relaxation, not a realizability theorem. This checkpoint does not make that replacement.

## 4. An additional unrestricted gap at z=8/9

Let lambda_i=-T_ii, mu=(sum lambda_i)/7, and define dimensionless quantities

    h=(mu-a)/d,
    v=(max lambda_i-mu)/d>=0,
    X=(T+mu I)/d,
    C=X+vI=(T+max lambda_i I)/d>=0,
    rho=1+h.

Since T has abscissa-c, the nonnegative C has Perron root rho+v. Its visible eigenvalues are rho+v and h+v+/-i sqrt(z), the latter pair each twice. The two centered hidden eigenvalues xi1,xi2 have real sum

    xi1+xi2=-A, A=1+5h,

and real product theta=xi1 xi2. This follows simply from trace X=0, not from a real-hidden-pole assumption. Put

    L=2+12h+30h^2-4z,
    R=1+6h+10h^2+z.

Exact spectral power sums give

    tau2=tr X^2=L-2theta>=0,
    tau3=tr X^3=-12hR+3A theta.                  (5)

The first inequality follows for every real Metzler X from the squared diagonals and nonnegative reverse-edge products. It is not an assertion that X is entrywise nonnegative.

Three further necessary inequalities come from the actual nonnegative C:

    h+v >= (z-1)/2,                             (6)
    theta <= rho^2+(A+2rho)v,                   (7)
    0<=tr C^3=3(A-2v)theta-12hR+3vL+7v^3.      (8)

For (6), apply |h+v+i sqrt(z)|<=rho+v and square. For (7), each hidden eigenvalue xi_j+v has modulus<=rho+v. Their real product theta-A v+v^2 is therefore at most(rho+v)^2, regardless of whether the roots are real or conjugate. Equation (8) is the exact binomial trace expansion; C^3 has nonnegative diagonal.

We now prove that v<=1/25 is impossible at z=8/9. Set epsilon=1/25. Equation (6) would give

    h>=-1/18-epsilon=-43/450.

Thus A-2v>=199/450>0. Using theta<=L/2 from (5) in (8) yields the necessary condition

    F(h)+(7/3)v^3>=0,
    F(h)=-(7/9)(1+7h)+21h^2+35h^3.              (9)

The vL terms cancel exactly in this substitution.

### Case 1: -43/450<=h<=1/4

F''(h)=42+210h>=329/15>0, so the maximum on this closed interval is at an endpoint. Directly,

    F(1/4)=-161/576<-1/20.

At h=-43/450, dropping the negative cubic term gives the conservative upper bound

    F(-43/450)
       <=-1043/4050+38829/202500
        =-13321/202500<-1/20.

Therefore F(h)<-1/20 throughout. But (7/3)v^3<=7/46875<1/20, contradicting (9).

### Case 2: h>=1/4

Use (7) in (8), which is legitimate since A-2v>0. Dividing by3 gives the necessary inequality

    0<=G(h)+v H(h)-2(3+7h)v^2+(7/3)v^3,
    G(h)=1-(5/9)h-13h^2-35h^3,
    H(h)=-5/9+30h+63h^2.                        (10)

Here H(h)>0 and 3+7h>0. Since v<=epsilon, the right side of (10) is at most

    J(h)=G(h)+epsilon H(h)+(7/3)epsilon^3.

Its derivative is

    J'(h)=29/45-(524/25)h-105h^2<0  for h>=1/4.

The endpoint is already negative:

    J(1/4)=-907/14400+7/46875<0.

Thus J(h)<0, contradicting (10).

Both cases are impossible, proving v>1/25 and hence G7-gap after restoring dimensions. No diagonal/topology restriction was assumed on T. The additional information beyond the previously failed generic centered trace2/trace3 route is the Perron **modulus** control of the genuine nonnegative shift by the largest holding rate, retaining its actual diagonal slack v.

## 5. Mandatory falsifiers and exact remaining obstruction

The supported C7 anchor at z=31/49 has uniform holding rates, h=1/7, v=0, A=12/7, theta=44/49, rho=8/7. In the unspecialized inequalities, L=88/49 and R=132/49, so tau2=tau3=0, A L/2-4hR=0, and

    A rho^2-4hR=240/343>0.

It therefore satisfies (5)–(8). The present argument does **not** falsely exclude that accepted PH7. Its contradiction uses z=8/9 essentially.

The supported PH8 representation at z=8/9 also has uniform holding rates. It is not excluded: n=8 has a hidden cubic, not this seven-state hidden quadratic, and the trace identities and7v^3 term are dimension-specific. Thus the new conclusion is not a disguised exclusion of all PH representations at the target.

The full lower-order target remains unresolved. Every hypothetical PH7 at z=8/9 has now been reduced to the **large holding-rate-slack region v>1/25**, still subject to the actual common-matrix path identities (4). No argument here shows that region impossible, and there is no PH7 counterexample or min8 claim. The first unproved step is literal: determine whether a single nonnegative-coupling PH7 matrix with v>1/25 can satisfy (4), the repeated-pole characteristic binding, and the exact transfer. Freely solving scalar relaxations would not answer it.

## 6. Dependencies and verification gate

The B6 source is `proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`, at the parent's actual written-check disposition. It is used to trim unreachable seven-state states at z=8/9, not as a theorem already excluding PH7.

The standard Perron facts used above have precise finite-dimensional hypotheses: an entrywise nonnegative real matrix has a nonnegative real spectral radius in its spectrum, all eigenvalue moduli are no greater, and principal submatrix spectral radii are monotone; shifting gives the corresponding real spectral abscissa for a Metzler matrix. This is the same classical import boundary as B6. The determinant coefficient identity is proved inline. No general PH-existence characterization, new classification or unreviewed computational certificate is imported.

Read operative `institute/runs/three-area-2026-10-23-96h/PH8-PH9-upper-parent-v1.md`: C8 upper8[13/20,8/9] and C9 upper9[3/4,1] are supported at their actual written boundaries; neither supplies a lower exclusion. The accepted C7 endpoint remains5935/9126 and novelty remains unclear. Generic three-moment failure remains an explicit valid control.

Requested separate reconstruction, if the parent admits it: verify the rank-one determinant/path signs and common-matrix binding; relative-degree/boundary support count; Perron density interface without hidden observability assumptions; all centered spectral and modulus identities for both real and complex hidden roots; the two exact polynomial cases at v<=1/25; both falsifiers; and the explicit absence of a completed unrestricted PH7 exclusion. No execution is requested or authorized by this packet.
