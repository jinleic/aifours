# Repeated nonreal poles: algebraic-degree realizability and an exact five/six-state band

Status: **CANDIDATE / NOVELTY_UNCLEAR**. Written derivation by the mathematics lane; no parent acceptance, independent proof check, Lean/kernel verification, scientific program or numerical experiment is claimed. This is a scoped result related to the minimal-representation book question, not its general solution. The general upper bound in Theorem A imports the precise classical theorem in §3; Theorem B is self-contained apart from elementary matrix/Markov-chain facts.

## 1. Statements and notation

Let r,q be positive integers and a,c,b real with a>c>0 and b>0. Set

    d = a-c, beta = b/d,
    D_{r,q}(s) = (s+c)^r ((s+a)^2+b^2)^q,
    K_{r,q} = D_{r,q}(0) = c^r(a^2+b^2)^q,
    H_{r,q}(s) = K_{r,q}/D_{r,q}(s),
    N_0 = r+2q, L = ceil(q/r).

H is a normalized rational function. We do NOT assume it is a probability transform outside the regions where a PH construction is supplied.

A PH representation (alpha,T) has alpha>=0, alpha1=1, T real Metzler and Hurwitz, T1<=0, and transform alpha(sI-T)^(-1)(-T1). Its order is the dimension of T, excluding the absorbing state.

**Theorem A (algebraic-degree criterion).** H_{r,q} has a PH representation of order N_0 if and only if

    beta^2 <= 1/(2L+1).

At every parameter satisfying this inequality its minimum PH order is exactly N_0. The necessity is proved directly below. The all-q sufficiency uses the named classical companion-realization theorem in §3 with every hypothesis checked; it is not asserted as a new spectral theorem.

**Theorem B (explicit order5/6 classification).** For r=1,q=2, put H=H_{1,2}. On the entire parameter range 0<beta<=1/sqrt(2), H is PH and its minimum PH order is

    5, if 0<beta<=1/sqrt(5);
    6, if 1/sqrt(5)<beta<=1/sqrt(2).

The upper bounds are explicit formulas for all a>c>0, with endpoints included; they do not require the §3 import. For beta>1/sqrt(2), this manuscript supplies neither an exact minimum nor a non-PH claim.

Theorem A includes r=q=1, which is the classical order3 threshold and is NOT a new result. The earlier internal simple-pole all-n theorem is not used. Repeated-pole cases and Theorem B are not represented as established novel contributions.

## 2. Universal algebraic-degree lower bound, including all topologies

Every entry of (sI-T)^(-1) is a polynomial divided by det(sI-T). Thus the reduced denominator of the scalar PH transform divides det(sI-T). Because K_{r,q} is nonzero, H has no cancellation, and its reduced denominator has degree N_0. Any PH representation therefore has order at least N_0.

Suppose now that an order-N_0 representation exists. Both D_{r,q} and det(sI-T) are monic of the same degree, and the former divides the latter. Consequently

    det(sI-T) = D_{r,q}(s).

In particular, there are no unobserved extra eigenvalues in this exact-degree argument. The spectrum of T consists precisely of -c with multiplicity r and -a+ib,-a-ib each with multiplicity q. No diagonalizability is assumed.

Permute T into Frobenius block triangular form, using its directed off-diagonal graph. Every diagonal block T_j is an irreducible Metzler matrix (a one-by-one block is allowed). The spectral abscissa of an irreducible Metzler matrix is a real, algebraically simple eigenvalue: shift by a sufficiently large positive multiple of I and apply Perron–Frobenius. Since the only real eigenvalue available in the complete spectrum is -c, every block has exactly one occurrence of -c. Hence there are exactly r diagonal blocks. Each has some q_j>=0 conjugate pairs, and

    sum_j q_j = q, dim T_j = 2q_j+1.

A real irreducible block cannot contain a nonreal eigenvalue without its conjugate, and it cannot have a different real Perron eigenvalue hidden outside the listed spectrum. These are the reasons the block count is valid.

Choose a block with ell=q_j>=L; such a block exists by the pigeonhole principle. Put M=T_j+cI, a Metzler matrix of size n=2ell+1. Its spectrum is 0 once and -d+ib,-d-ib each ell times. Trace is invariant under similarity and is the sum of eigenvalues with algebraic multiplicity, even for nontrivial Jordan blocks. Therefore

    tr M = -2ell d,
    tr M^2 = 2ell(d^2-b^2).

Writing m_ij for the entries, the off-diagonal products m_ij m_ji are nonnegative, so

    tr M^2 = sum_i m_ii^2 + sum_{i!=j} m_ij m_ji
            >= sum_i m_ii^2
            >= (sum_i m_ii)^2/n.

The last step is the real Cauchy–Schwarz inequality; the diagonal entries need not be nonnegative. Thus

    2ell(d^2-b^2) >= 4ell^2 d^2/(2ell+1),
    b^2 <= d^2/(2ell+1) <= d^2/(2L+1).

This proves Theorem A's necessity for arbitrary PH topologies, not just cycles or companion matrices.

For Theorem B specifically, any five-state representation has spectrum {-c, -a+ib twice, -a-ib twice}. Shifting by c and applying the same trace inequality gives directly

    4(d^2-b^2) >= 16d^2/5,
    beta^2 <= 1/5.

The degree lower bound excludes order<5. Hence an explicit six-state construction above beta^2=1/5 will be minimal.

## 3. Exact classical import used only for general Theorem A sufficiency

**Imported theorem:** Ellard–Smigoc, *Diagonal elements in the Nonnegative Inverse Eigenvalue Problem*, arXiv:1702.02650v1 (8 Feb2017), Theorem1.2, stating the Laffey–Smigoc2006 theorem. [Official primary HTML](https://arxiv.org/html/1702.02650v1#S1.Thmtheorem2).

Let sigma=(rho,lambda_2,...,lambda_n) be self-conjugate, rho>=0, and Re lambda_i<=0 for i>=2. Define s_k=sum sigma_i^k. The list is the spectrum of a nonnegative matrix iff s_1>=0 and s_1^2<=n s_2. Furthermore, it can be realized by C+eta I with C a nonnegative companion matrix of trace zero and eta>=0. Theorem2.1 gives the displayed superdiagonal-one orientation used below.

Trust boundary: the primary statement and displayed construction have been read; this manuscript does not authenticate the entire2006 proof or claim a formal verification of that result. Repeated entries are allowed by the statement: it concerns a list, not a set of distinct roots. Its companion conclusion is stronger than merely prescribing a spectrum and will be essential for the transfer function.

Fix ell>=1 and suppose beta^2<=1/(2ell+1). Set n=2ell+1 and

    gamma = 2ell d/n,
    sigma = (gamma, (-d/n+ib) repeated ell times,
                    (-d/n-ib) repeated ell times).

It is self-conjugate; gamma>0; every other entry has strictly negative real part. Also

    s_1 = gamma - 2ell d/n = 0,
    s_2 = gamma^2 + 2ell(d^2/n^2-b^2)
        = 2ell(d^2/n-b^2) >= 0.

All imported hypotheses hold. The conclusion gives C+eta I nonnegative with this spectrum and C nonnegative companion, tr C=0. Since s_1=n eta=0, eta=0. Thus C itself is a nonnegative companion matrix of trace zero with the prescribed spectrum.

Write

    P(x) = (x-gamma)((x+d/n)^2+b^2)^ell.

For the standard upper-shift companion, C has ones on the superdiagonal and the last row contains the negatives of the nonleading coefficients of P in reverse order. Its trace-zero last diagonal entry is zero. The imported conclusion certifies all these last-row entries are nonnegative. The constant term of P is strictly negative, so the bottom-left entry is strictly positive. Thus C is irreducible, although the PH conversion below only needs stability and the explicit resolvent.

Put lambda=c+gamma and A=C-lambda I. Its spectrum is -c once and -a+ib,-a-ib each ell times, hence A is Hurwitz and Metzler. Moreover

    det(sI-A) = P(s+lambda)
              = (s+c)((s+a)^2+b^2)^ell =: D_ell(s).

Let k=D_ell(0)>0 and w=k e_n. Solving the first n-1 rows of (sI-A)y=e_n gives

    y_i=(s+lambda)^(i-1)y_1,
    y_1=1/D_ell(s).

The last equality follows by substituting into the final companion row. In particular

    e_1^T(sI-A)^(-1)w = k/D_ell(s).

This step checks the actual transfer function and the full nonreal pole multiplicity, not just the spectrum.

For an explicit diagonal normalization set h_i=lambda^(i-1) (i=1,...,n), S=diag(h_i). Evaluation of the resolvent formula at s=0 gives -A h=w: equivalently the first n-1 rows cancel, and the last row is P(lambda)=D_ell(0)=k. Now take

    T_ell = S^(-1) A S, alpha_ell=e_1^T.

T_ell is Metzler and Hurwitz; -T_ell 1=S^(-1)w>=0; alpha_ell1=1. The similarity identity proves

    alpha_ell(sI-T_ell)^(-1)(-T_ell1) = k/D_ell(s).

Therefore a one-real-pole block with ell repeated conjugate pairs has a PH representation of exactly 2ell+1 states under the asserted inequality. For ell=0 use the one-state exponential transform c/(s+c).

## 4. Assembling all r,q without assuming a single global Perron pole

Choose r integers ell_j>=0 whose sum is q and whose maximum is L=ceil(q/r), for example by distributing q objects as evenly as possible among r boxes. Under beta^2<=1/(2L+1), every positive ell_j satisfies beta^2<=1/(2ell_j+1), so §3 gives a PH block (alpha_j,T_j) for

    h_j(s)=c(a^2+b^2)^(ell_j) /
           [(s+c)((s+a)^2+b^2)^(ell_j)].

For ell_j=0 this is c/(s+c), as required. Let w_j=-T_j1. Form the block upper-bidiagonal matrix T with diagonal blocks T_j and blocks w_j alpha_{j+1} directly above them. Start with alpha=(alpha_1,0,...,0), and allow absorption only from the last block.

Every off-diagonal entry is nonnegative. Each nonfinal block row sum is T_j1+w_j(alpha_{j+1}1)=0; the final block row sum is nonpositive. The spectrum is the union of the stable diagonal-block spectra, so T is Hurwitz. The block inverse gives transform h_1(s)...h_r(s)=H_{r,q}(s). Its dimension is

    sum_j (2ell_j+1) = 2q+r=N_0.

Together with §2, this proves Theorem A at the stated classical-import boundary.

## 5. Self-contained five-state construction for H_{1,2}

Here no §3 import is needed. Let

    t=d/5, lambda=a-t=c+4t, v=t^2+b^2,
    U=12t^2-2v=2(d^2/5-b^2),
    V=16t^3+4tv,
    W=v(16t^2-v),
    Z=4t v^2,
    K=c(a^2+b^2)^2.

Assume b^2<=d^2/5=5t^2. Then U>=0, V>0, Z>0; also v<=6t^2, so W>=10t^2 v>0. Direct polynomial multiplication gives

    P_5(x)=(x-4t)(x^2+2tx+v)^2
          =x^5-Ux^3-Vx^2-Wx-Z.

Let C_5 have ones on the superdiagonal and final row (Z,W,V,U,0). Set A_5=C_5-lambda I. Then

    det(sI-A_5)=P_5(s+lambda)
              =(s+c)((s+a)^2+b^2)^2,
    P_5(lambda)=K.

Its eigenvalues are -c, -a+ib twice and -a-ib twice, all strictly stable. Take S_5=diag(1,lambda,lambda^2,lambda^3,lambda^4), T_5=S_5^(-1)A_5 S_5 and alpha_5=e_1^T. Explicitly, T_5 has diagonal -lambda, superdiagonal lambda, and final-row off-diagonal entries

    (Z/lambda^4, W/lambda^3, V/lambda^2, U/lambda).

All first four row sums are zero. The final row sum is

    -lambda + U/lambda + V/lambda^2 + W/lambda^3 + Z/lambda^4
    = -P_5(lambda)/lambda^4 = -K/lambda^4 < 0.

The same companion resolvent calculation as §3, or a direct first-row cofactor, gives transform K/P_5(s+lambda)=H_{1,2}(s). Thus this is an actual five-state PH representation including b^2=d^2/5. Degree5 makes it minimal.

## 6. Self-contained six-state construction and cancellation

Assume b^2<=d^2/2. Define

    A=d^2-2b^2 >= 0,
    B=b^2(2d^2-b^2) > 0,
    C=d^2 b^4 > 0,
    K=c(a^2+b^2)^2.

(The letters A,B,C in this section are scalar coefficients, not the generator in §3.) Let C_6 have ones on the superdiagonal and final row (C,0,B,0,A,0). Its characteristic polynomial is

    P_6(x)=x^6-Ax^4-Bx^2-C
          =(x^2-d^2)(x^2+b^2)^2.

Set G=C_6-aI. Then

    det(sI-G)=(s+c)(s+c+2d)((s+a)^2+b^2)^2,

and its eigenvalues are -c, -(c+2d), -a+ib twice and -a-ib twice. In particular G is Hurwitz.

This realization has one extra real eigenvalue. It must be canceled by a nonnegative numerator, not ignored. With w=K e_6 and z=s+a, the companion equations give

    e_1^T(sI-G)^(-1)w=K/P_6(z),
    e_2^T(sI-G)^(-1)w=Kz/P_6(z).

For the nonnegative row u=d e_1^T+e_2^T, therefore,

    u(sI-G)^(-1)w
      =K(z+d)/P_6(z)
      =K(s+c+2d)/[(s+c)(s+c+2d)((s+a)^2+b^2)^2]
      =H_{1,2}(s).

The canceled factor has a positive constant offset d in this row realization. No negative initial weight or signed exit is used.

For explicit PH parameters use h_i=a^(i-1)/(c+2d), S_6=diag(h_i). Since

    P_6(a)=c(c+2d)(a^2+b^2)^2=K(c+2d),

we have -G h=w, by either direct substitution or the preceding resolvent at s=0. Set T_6=S_6^(-1)G S_6 and alpha_6=uS_6. Thus

    alpha_6=(d/(c+2d), a/(c+2d), 0,0,0,0),

whose entries are nonnegative and sum to1 because a+d=c+2d. T_6 has diagonal -a, superdiagonal a, and final row

    (C/a^5, 0, B/a^3, 0, A/a, -a).

Its first five row sums are zero; its last exit rate is

    a-A/a-B/a^3-C/a^5=P_6(a)/a^5=K(c+2d)/a^5>0.

The off-diagonal entries are nonnegative, and its stable spectrum is unchanged by similarity. Hence (alpha_6,T_6) is PH, and the similarity identity preserves the exact desired transform. This proves an order6 upper bound throughout beta^2<=1/2, including equality. For beta^2>1/5, §2 excludes every order5 or lower representation, completing Theorem B.

## 7. Actual new mathematical delta and boundaries

Relative to the previously completed simple-pole H_{1,1} case, the candidate now addresses repeated nonreal poles, proves an all-(r,q) exact-degree obstruction/criterion with an explicit classical import, and supplies a genuinely super-algebraic-degree interval where the exact minimum is6 rather than the denominator degree5. It does not merely rederive the old n* formula.

A useful nontrivial witness family is a=c+d, b=d/2, c,d>0. Here beta^2=1/4 lies strictly between1/5 and1/2, so the formula supplies a six-state PH distribution and a universal five-state impossibility. This is an infinite exact family, not sampled numerical evidence.

Novelty remains unclear and may be limited to an explicit corollary/assembly: trace/JLL, nonnegative companions, Frobenius/Perron blocks, positive-to-PH rescaling, cascades and cancellation are all classical. No claim of first, best-known, publication readiness or full-book solution is made. Theorem A does not say H outside its criterion is non-PH; Theorem B leaves beta>1/sqrt(2) unresolved. No inference to Sun8, full Olson, Shor or Kac–Moody is present.

## 8. Next exact obstruction, not a solver result

To continue the broad H_{1,2} target above beta=1/sqrt(2), the displayed C_6 fails because A=d^2-2b^2 becomes negative. This refutes only this fixed companion construction, NOT all six-state PH realizations. A general order6 candidate has characteristic polynomial D_{1,2}(s)(s+u) for some additional real eigenvalue -u; reachable/co-reachable trimming and positive residues must determine the admissible u, and a different realization may use a nonuniform diagonal. Neither the sign failure nor a classical theorem with unmet hypotheses supplies a universal six-state lower bound.

An irreducible single directed cycle cannot carry a repeated nonreal eigenvalue. Indeed its characteristic polynomial is prod_i(s+lambda_i)-kappa with positive lambda_i and kappa>0. At a nonreal zero z with Im z>0, a repeated root would require

    sum_i 1/(z+lambda_i)=0.

Every summand has strictly negative imaginary part, a contradiction. Thus a naive single-monocycle extension of the old simple-pole construction is structurally unavailable; the multiple feedbacks above are a material representation change. This elementary topology obstruction is not asserted novel and does not constrain arbitrary PH graphs.

## 9. Verification requested from the parent

No commands are needed for the written candidate. Independently check: (1) exact-degree denominator/characteristic binding; (2) exactly r Frobenius blocks and their algebraic Perron multiplicities; (3) all scalar coefficients/signs and the endpoints; (4) row sums, initial mass and the correct orientation of the resolvent; (5) the actual linear-factor cancellation in §6; (6) the imported theorem's precise hypotheses and companion conclusion; (7) primary prior art for these formulas.

A future formalization would need real matrices, positive-state normalization, determinant/resolvent identities and Frobenius/Perron theory or a standalone proof for the concrete order5/6 matrices. This manuscript is not a Lean theorem and has no kernel replay. Any scientific executable check remains separately admission-gated.
