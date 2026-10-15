# A plant-derived Grassmannian section and complete unstabilized synthesis for m=p=2

Date: 2026-10-14 (America/Los_Angeles). This continuation preserves the earlier evidence. It addresses the exact plant and controller in the book, with D11=0 and arbitrary other feedthrough matrices. All statements are over the reals unless a complex comparison is explicitly stated. Exact computation claims use rational plant data.

**Verdict:** exact general reformulation plus a closed **m=p=2** unstabilized corollary, not a full solution of the book. The general Grassmannian mechanism is classical, and the corollary is elementary and **likely routine; publication novelty is unestablished**. The substantive addition to this local package is explicit synthesis for **two control inputs and two measurements, arbitrary state/disturbance/controlled-output dimensions, without internal stability**. The stable subset is characterized using the full state characteristic polynomial, but general stable selection is not solved. No polynomial-time requirement is attributed to the book.

## 1. Baseline and exact scope match

The original book images `../sources/book/pdfpage-0652.png` and `pdfpage-0653.png` were reread. The book asks to find one finite real static gain for arbitrary plants, with a separate strict internal-stability variant, and discusses all-gain descriptions for its resolved invertible-channel classes. This continuation additionally seeks all-gain parameterizations. Printed p.631 explicitly adopts **D11=0** immediately below equation (1); equation (3) is precisely the transfer expression used here. We do not extend the result to nonzero-D11 algebraic loops. The Sigma_Q definition has the apparent B/E typo already disclosed in the README.

Chen, Mareels, Zheng and Zhang (2000), *Automatica* 36, 1717-1724, [DOI](https://doi.org/10.1016/S0005-1098(00)00090-X), local `../sources/papers/chen-2000.pdf`, was reread, especially printed **1722**: the residual noninvertible case is a finite-step QEPCAD problem, and Groebner bases plus QEPCAD can find all solutions to both variants. The source itself warns that the conditions can be hard to interpret. Its Appendix A (A.7) uses finite Markov parameters. Thus generic polynomial decision remains **SOLVED-BY-PRIOR-WORK**, not new.

Grassmannian/Plucker linearization is classical. Gorla and Rosenthal, *Pole Placement with Fields of Positive Characteristic*, [arXiv:0912.2932v1, Section 2, equations (14)-(15)](https://arxiv.org/html/0912.2932v1), explicitly expand the characteristic polynomial linearly in controller Plucker coordinates. Eremenko and Gabrielov, *Pole Placement by Static Output Feedback for Generic Linear Systems*, [author PDF, Section 2, (2.2)-(2.5)](https://www.math.purdue.edu/~eremenko/dvi/polep72.pdf), construct the controller graph big cell and discuss failures of real solutions. Those primary sections were read. Their generic pole-placement theorems do not assert full feedthrough DDP or a solution for every exceptional real plant.

The referee-directed comparison also retrieved Karcanias and Leventides, *Solution of the determinantal assignment problem using the Grassmann matrices*, *International Journal of Control* 89(2), 352-367 (2016), [DOI](https://doi.org/10.1080/00207179.2015.1077525), [accepted manuscript](https://openaccess.city.ac.uk/id/eprint/12469/). Its Sections 1-3, equations (2)-(4), explicitly split the determinant problem into a linear coefficient system and decomposability, with real Grassmannian intersections. Section 7, (26)-(29), replaces the remaining selection by a nonlinear optimization and an iterative stopping criterion; this is not a proof that local numerical iteration certifies every real infeasible instance. **Theorem A is an instance of that classical framework; Theorem B is its elementary affine-Klein-quadric corollary specialized to all feedthrough DDP numerators.** No new general method or priority is claimed. The exact DDP corollary was not located verbatim, which does not establish novelty.

## 2. Plant-only linear maps on graph coordinates

Use the existing dimensions: x in R^n, u in R^m, y in R^p, w in R^q, z in R^r, and

    xdot = A x + B u + E w,
    y = C1 x + D1 w,
    z = C2 x + D2 u + D22 w,       u = K y.

Write M=A+BKC1, G=E+BKD1, F=C2+D2KC1, J=D22+D2KD1. For every increasing p-subset I of {1,...,p+m}, let delta_I be a coordinate. There are N=binomial(p+m,p) coordinates. Put I0={1,...,p}. Define

    X(s) = [sI-A; -C1],
    Z    = [[0_(n by p), -B], [I_p, 0_(p by m)]],
    a_I(s) = det [X(s), Z[:,I]].                         (1)

For controlled-output index alpha and disturbance index beta, append their row/column:

    X_alpha(s) = [sI-A; -C1; C2[alpha,:]],
    Z_alpha   = [[0,-B], [I_p,0], [0,D2[alpha,:]]],
    v_alphabeta = [-E[:,beta]; -D1[:,beta]; D22[alpha,beta]],
    b_I^(alphabeta)(s) = det [X_alpha(s), Z_alpha[:,I], v_alphabeta].  (2)

All these polynomials have degree at most n, because only the n state columns contain s. Their coefficients depend on the plant alone, not K or any candidate state subspace. Define L with columns indexed by I and rows indexed by (alpha,beta,j), 0<=j<=n, by L[(alpha,beta,j),I]=the coefficient of s^j in b_I^(alphabeta)(s). Then L delta=0 means every sum_I b_I^(alphabeta)(s) delta_I is identically zero. Let P map delta to the coefficients of sum_I a_I(s) delta_I.

Let G_big be the set of Plucker coordinates of p-planes whose projection onto the first p coordinates is an isomorphism, normalized by delta_I0=1. Concretely these are precisely the maximal minors of

    Q(K) = [I_p; K].                                     (3)

**Theorem A (general linear-section representation).** The map K -> minors(Q(K)) is a bijection from all finite real m-by-p matrices onto G_big. It restricts to a bijection

    {all DDP gains} <-> {delta in G_big : L delta=0}.       (4)

The full characteristic polynomial is exactly

    det(sI-M) = sum_I a_I(s) delta_I,                      (5)

not the denominator of a minimal transfer realization. For every alpha,beta,

    det(sI-M) T_alphabeta(s)
      = sum_I b_I^(alphabeta)(s) delta_I.                  (6)

**Proof.** Every finite K gives the full-column-rank matrix Q(K), with top minor 1. Conversely a p-plane with nonzero top minor has a basis Q=[Q_top;Q_bottom] with Q_top invertible. Right multiplication by Q_top^-1 gives the unique [I;K], K=Q_bottom Q_top^-1. Normalizing the common determinant scale makes its maximal minors exactly delta. Hence the chart covers every allowed controller and contains no implicit or singular controller relations. In 1-based indices its inverse is

    K[i,j] = (-1)^(p-j) delta_(I0 without j, with p+i).     (7)

This sign follows by moving the bottom selected row to row j. No other Grassmannian charts are needed for a finite gain u=Ky; admitting delta_I0=0 would introduce different controller relations and is forbidden.

Cauchy-Binet applied to [X,Z] diag(I_n,Q) gives (5), since that product is

    W_K(s) = [[sI-A, -BK], [-C1,I_p]].

Its Schur complement in I_p is sI-A-BKC1. In particular the polynomial is monic of degree n, independently of controllability, observability, or cancellations. Applied to the bordered product in (2), Cauchy-Binet gives the determinant of

    [[sI-A, -BK, -E[:,beta]],
     [-C1,   I_p, -D1[:,beta]],
     [C2[alpha,:], D2[alpha,:]K, D22[alpha,beta]]].

Over the rational-function field W_K is invertible, because its determinant is monic. Its Schur complement gives det(W_K) times the alpha,beta entry of J+F(sI-M)^-1G. This proves (6), including the sign of the bordered input column. A rational function is identically zero iff its product with this nonzero polynomial is zero. Taking all coefficients proves (4). The construction retains the entire state block, all D terms, and the exact algebraic equation y=C1x+D1w. There is no control-to-measurement feedthrough or algebraic loop under D11=0. QED.

This is not the previous HKR=-Q test for an unknown V. All plant dependence is in explicit linear maps L and P; the nonlinear constraint is the fixed, plant-independent decomposability variety. For arbitrary port counts, however, selecting a real decomposable point of ker L is still a genuine nonlinear obligation. Calling that selection a completed general synthesis algorithm would overstate the result.

**Corollary A1 (one control input or one measurement).** If min(m,p)=1, the complete unstabilized DDP gain set is an affine subspace, possibly empty, determined by the plant-derived linear equations L delta=0 and delta_I0=1. For rational plants every gain and an infeasibility certificate are obtained by rational linear algebra, for arbitrary state order and all remaining feedthrough/channel dimensions.

**Proof.** If p=1, the maximal minors of [1;K] are 1 and the entries of K. If m=1, a maximal p-by-p minor of [I_p;K] either uses all identity rows and equals 1, or replaces exactly one identity row and equals the corresponding entry of K with the sign in (7). These are all the minors. Consequently every normalized coordinate vector is the graph-minor vector of a unique gain, with no residual Plucker relation. Theorem A then leaves only affine linear equations; solve them and apply (7). QED.

This is an elementary corollary of the classical framework, with publication novelty unclear and no novelty claim. Stability is not covered by this affine synthesis: strict Hurwitz selection remains on the resulting gain family. In particular, with one measurement and E=C2=D1=D2=D22=0, every K decouples and the stable variant is exactly single-measurement static-output-feedback stabilization, to which the source-relative strong NP-hardness statement in the existing README applies.

## 3. Complete unstabilized synthesis for two inputs and two measurements

Set m=p=2, with no restriction on n,q,r or plant ranks. In the coordinate order (12,13,14,23,24,34), write

    delta = (1,b,d,-a,-c,t),       K=[[a,b],[c,d]].

The normalized Grassmannian has exactly one condition:

    delta12 delta34 - delta13 delta24 + delta14 delta23=0,
    equivalently t=ad-bc.                                  (8)

This can be proved without invoking general Plucker theory: the four single-replacement minors reconstruct a,b,c,d, and the only remaining minor is det K. Thus (8) is both necessary and sufficient, including all singular K.

**Theorem B (all-order synthesis for m=p=2).** Construct L by (2). Solve the plant-derived linear equations

    L delta=0,       delta12=1.                            (9)

If they are inconsistent, DDP is infeasible. Otherwise ordinary linear algebra gives every solution uniquely as delta=delta_*+N tvec, with N any basis of the homogeneous solution space and tvec in R^d, d<=5. Substitute this expression in the single relation (8), obtaining

    f(tvec)=tvec^T H tvec + 2 g^T tvec + gamma=0.          (10)

All DDP gains, with no missing exceptional cases, are the linear extraction (7) of the following explicit parameter families. For rational plant data this is an exact-arithmetic algorithm over Q with exact sign tests and algebraic square roots; for arbitrary real data it is a structural classification, not a finite-input algorithm claim. It requires neither search over state subspaces nor general polynomial/QE feasibility.

To enumerate the zero set of (10), choose a nonsingular real (rational for rational H) congruence U with U^T H U=diag(d_i). Put h=U^T g and tvec=U z. For d_i nonzero put z_i=x_i-h_i/d_i; for d_i=0 put z_i=x_i. Define

    rho = sum_(d_i nonzero) h_i^2/d_i - gamma.

The remaining equation is

    sum_(d_i nonzero) d_i x_i^2
      + 2 sum_(d_i=0) h_i x_i = rho.                     (11)

There are three exhaustive cases.

1. **A null direction has h_j nonzero.** All x_i for i!=j are free, and

       x_j = [rho - sum_(d_i nonzero)d_i x_i^2
                    -2 sum_(d_i=0,i!=j)h_i x_i]/(2h_j).

   This polynomial graph is nonempty and covers every solution.
2. **All d_i=0 and all h_i=0.** All x are free if rho=0; there are no solutions otherwise. This includes d=0 (a single candidate point).
3. **Some d_j is nonzero and all null h_i vanish.** If positive and negative d_i both occur, every rho is feasible. If all nonzero d_i are positive, feasibility is rho>=0; if all are negative, it is rho<=0. For a feasible case choose any nonzero d_j. Let all other x_i be free subject only to

       R(x_others)=[rho-sum_(i!=j)d_i x_i^2]/d_j >= 0,

   and set x_j=+sqrt(R) or -sqrt(R). These two radical charts cover the entire real zero set, including R=0 and all null directions. A witness is immediate: for rho!=0 choose a d_j with its sign, set other coordinates zero and take sqrt(rho/d_j); for rho=0 use zero.

**Proof.** The linear solution of (9) is complete. Equation (8) is the full graph condition, so Theorem A reduces synthesis exactly to (10). Symmetric congruence diagonalization and completing squares give (11). A nonzero null-linear coefficient can always be solved for. Otherwise a diagonal quadratic form has range R if indefinite, [0,infinity) if positive semidefinite nonzero, (-infinity,0] if negative semidefinite nonzero, and {0} if zero. This proves the feasibility classification. Solving for one squared coordinate yields both signs and all solutions. Reversing the invertible coordinate changes and (7) gives all gains. QED.

For rational input, every displayed congruence, affine solution, certificate of inconsistent linear equations, and inertia sign can be obtained exactly over Q; the witnesses may need a real square root. This is a constructive class result, not a promise that a symbolic closed form or a rational controller exists for every real solution set.

## 4. Stability: exact restriction, not a solved selection problem

For any delta in (4), write the monic degree-n polynomial (5) as

    s^n + ell1 s^(n-1) + ... + ell_n.

Its coefficients are linear in delta. Set ell0=1 and ell_j=0 outside 0<=j<=n. Let H_n[i,j]=ell_(2j-i), with 1-based indices, and let Delta_k be its k-th leading principal determinant. The real Routh-Hurwitz criterion gives

    M is strictly Hurwitz iff Delta_k>0 for k=1,...,n.     (12)

Thus (4) plus these strict inequalities is an exact description of every stable gain. In the m=p=2 class one may substitute the complete families of Theorem B. **This does not itself decide whether their strict Hurwitz region is nonempty without another nonlinear selection step.** In particular E=C2=D1=D2=D22=0 leaves arbitrary static output-feedback stabilization. No claim is made that this is settled by the quadric classification.

Hidden modes are retained by (5). For the explicit append operation A_new=diag(A,h), B_new=[B;0], E_new=[E;0], C1_new=[C1,0], C2_new=[C2,0], with all D matrices unchanged, (5) is multiplied by (s-h) and the transfer is unchanged. The zero E row and C2 column, as well as the absence of state coupling, matter: merely being unactuated/unmeasured would not suffice. At h=0 or h>0 there are no internally stable gains even if every transfer numerator vanishes. Equality in (12) is never accepted. No factor cancellation or minimal realization is used.

## 5. An irreducible curved family and the finite-fixed-subspace obstruction

Take n=m=p=2, q=r=1,

    A=-I_2, B=C1=I_2, E=[0;1], D1=[1;0],
    C2=[1,0], D2=[0,1], D22=0.                         (13)

Both channels are noninvertible in the directions required by Chen: Sigma_P has one output and two inputs; Sigma_Q has two outputs and one input. In the usual output-nulling/strongly-reachable definitions, V*(Sigma_P)=R^2 and S*(Sigma_Q)=0. The output-nulling input u2=-x1 leaves free input u1 and the controllable pair A_cc=[[-1,0],[-1,-1]], B_c=[1;0]; its controllability determinant is -1. Thus the output-nulling controllable component has dimension 2.

Here is the explicit match to **Chen (7), (11), (15)-(21)**, rather than an inference from those subspace dimensions alone. In (7), X has zero rows, Y has zero columns, and D22=0, so N=0. Keep the state and measurement coordinates, and swap the inputs to v0=u2, v_c=u1. The special-coordinate decomposition (11) has only x_c=x: no x_a, x_b or x_d blocks. Its data are A_cc as above, B_c0=e2, C_0c=e1^T, B_c=e1; indeed A=A_cc+B_c0 C_0c=-I. Step 4 (15) has no x_a block to split. Step 5 (19)-(21) keeps all of x_c and gives A_R=-I, B_R=[e2,e1] Gamma_i^-1=I, E_R=e2, C1R=I, D1R=e1, C2R=e1^T and D2R=[1,0] Gamma_i^-1=e2^T, where Gamma_i is the swap matrix. Thus the reduced plant is **exactly (13)**, still of order 2.

Chen's dualization (29) now gives A=-I, B=C1=I, E=e1, D1=e2, C2=e2^T, D2=e1^T. Simultaneously swapping the two state, control and measurement coordinates returns (13). The next reduction is therefore again the identity up to these permutations. This verifies that the alternating state-order reduction stops at this noninvertible residual plant. The source-equation match was expanded after the referee requested it; the referee had verified the component subspace/controllability facts but had not audited these source maps.

For K=[[a,b],[c,d]], the complete numerator is

    c(s+1)^2 +(a+d)(s+1)+b-2(ad-bc).                    (14)

It vanishes exactly when c=0, d=-a, b=-2a^2. Therefore **all** gains are

    K(a)=[[a,-2a^2],[0,-a]],            a in R.           (15)

In lifted coordinates the linear equations are c=0, d=-a, b=2t, and the one remaining quadric is t=-a^2. This displays the nonlinear geometry rather than replacing it with a gain grid.

The full poles are -1+a and -1-a, so stable gains are precisely (15) with -1<a<1. At these gains

    G=[a;1], F=[1,-a], M G=(-1-a)G.

For clarity, a state subspace is admissible here when im G is contained in V, MV is contained in V, and V is contained in ker F; J=0 is imposed separately. The minimal reachable subspace is V(a)=span([a;1]); it is also ker F. Thus **V(a) is the only admissible subspace**, not just the minimal one. Distinct a give distinct V(a). A finite collection of fixed state subspaces therefore cannot cover all gains of this one plant, even if only internally stable gains are requested. A larger V cannot rescue the finite list, because ker F is already one-dimensional.

Also this gain set is not a finite union of affine gain subspaces: any positive-dimensional affine subspace would contain a line; a line in (15) would make a affine in its line parameter and b=-2a^2 affine, forcing a constant and then the whole line constant. Each affine subspace contained in (15) is a singleton, whereas (15) is infinite. These obstructions refute finite fixed-V and finite affine-family approaches, not finite nonlinear Grassmannian charts, and not a procedure that only seeks one witness.

The old three-state no-greatest example is independently retained: B=e3, C1=[1,1,0], Ae1=e3, Ae2=-e3, Ae3=0, with prescribed output kernel span(e1,e2). The lines span(e1), span(e2) have gains -1,+1, but their sum would require both. This direct argument already proves failure of closure under sums; computational checks are separate evidence.

## 6. Exact real infeasibility beyond the linear section

Take m=p=2, n=4, q=r=1,

    A=[[-1,0,0,1], [0,-1,-1,0], [1,0,-1,0], [0,1,0,-1]],
    B=[I_2;0_(2 by 2)], C1=[I_2,0_(2 by 2)], E=[0;1;0;0],
    D1=[1;0], C2=[1,0,0,0], D2=[0,1], D22=0.             (16)

The coefficients of the bordered numerator, using t=ad-bc, in descending s-order are

    c,
    a+d+4c,
    -2t+3a+b+6c+3d,
    -5t+3a+2b+6c+3d+1,
    -3t+a+b+4c+d+1.

Linear elimination forces c=0, d=-a, b=2, t=1. The Grassmannian relation then says **a^2+1=0**, an explicit real infeasibility certificate. The linear section alone is nonempty; discarding decomposability would be a false positive. Over C, a=i, d=-i, b=2, c=0 is an exact decoupling gain. This also detects silently substituting complex algebraic feasibility for the required real problem. No numerical tolerance or solver-only assertion is needed.

## 7. Evidence contract and remaining mechanism

`../evidence/continuation/protocol.json` freezes the bounded exact checks. `grassmannian.py` constructs L and P for general port counts and implements all cases of Theorem B; `verify_continuation.py` compares its symbolic identities against a separately constructed adjugate numerator, exercises every quadric branch, and checks the counterexamples and hidden modes. No old exhaustive or random plant sweep is rerun. The independent CLI review is retained separately, with its input snapshot, exact command, output, identity, and disposition.

For arbitrary port counts, the controller-graph linear section is an exact classical reformulation, not additional general decision power. For **min(m,p)=1**, Corollary A1 gives complete unstabilized affine synthesis; for **m=p=2**, the one-quadric corollary closes unstabilized selection and supplies every gain. These are elementary corollaries, not certified new research results. For m,p>=2 other than m=p=2, multiple decomposability relations remain, and no generally complete explicit real parametrization is supplied. Even in the affine or one-quadric classes, arbitrary-order Hurwitz selection remains unsolved here. A further small plant sweep cannot close either gap. The checked determinantal-assignment literature confirms that this representation is established, so repeating it is not a justified next research campaign. General progress requires a genuinely additional selection theorem for these real linear sections or their strict Hurwitz regions. The original book verdict remains **not resolved by this continuation**.
