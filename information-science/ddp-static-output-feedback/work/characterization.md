# Exact algebraic decision and the geometric obstruction

Date: 2026-10-14 (America/Los_Angeles). Domain: finite-dimensional continuous-time real LTI plants; rational input matrices for the algorithmic claims. This is a self-contained derivation, not a priority claim.

## 1. Claim, baseline, and missing ingredient

**Claim.** Both book variants have a finite, exact semialgebraic feasibility characterization and a terminating real-algebraic decision algorithm. For a fixed candidate disturbance-containing subspace, all feedthrough constraints can be checked jointly by two rank tests. Neither statement resolves the book's intended general structural-synthesis challenge. The book does not require polynomial time, so lack of a polynomial-time algorithm is not our definition of that gap.

**Baseline.** The fully fetched Chen et al. (2000), printed p. 1722, explicitly describes the non-invertible remainder as a finite-step QEPCAD problem and mentions Groebner bases plus QEPCAD for both DDPCM and DDPCMS. Its Appendix A, equation (A.7), already uses the finite Markov-parameter criterion. We must not relabel the reduction below as a new solution to the historical structural-design question. See `../sources/references.md`, item 2.

**Missing ingredient for structural progress.** Select the relevant subspace and parameterize all compatible gains for an arbitrary plant through a constructive, informative control-theoretic characterization, not merely by restating existential gain/subspace feasibility. With stability, determine which compatible gains are Hurwitz, including hidden modes. A greatest admissible subspace need not exist. This states the residual research deliverable, not a polynomial-time requirement absent from the book. A September 2026 preprint establishes strong NP-hardness of unrestricted static-output-feedback stabilization; our explicit embedding transfers its lower bound to the stable DDP variant, relative to that source theorem. Hardness is a barrier to one algorithmic objective, not a full solution to disturbance decoupling.

## 2. Notation and exact plant

Let x be n-dimensional, u m-dimensional, y p-dimensional, w q-dimensional, and z r-dimensional, with n,m,p,q,r positive integers. Let

- A: n by n, B: n by m, E: n by q;
- C1: p by n, D1: p by q;
- C2: r by n, D2: r by m, D22: r by q.

D11 is zero. For K in R^(m by p), put

M=A+BKC1, G=E+BKD1, F=C2+D2KC1, J=D22+D2KD1.

The question is whether T(s)=F(sI-M)^(-1)G+J is identically zero as a rational matrix. Initial state is zero in this transfer definition. Internal stability additionally means M is Hurwitz, including modes invisible in T. We do not replace internal stability by stability of a reduced transfer realization.

## 3. Finite Markov-parameter characterization

**Theorem 1.** For any fixed real K, T(s)=0 if and only if

J=0 and F M^j G=0 for j=0,...,n-1.                    (1)

**Proof.** The limit as real s tends to positive infinity gives J=0. For |s| greater than a matrix norm of M, the convergent Neumann expansion gives T(s)=J+sum_{j>=0}(F M^j G)s^(-j-1). Identical vanishing therefore implies every Markov parameter vanishes. Conversely, Cayley-Hamilton expresses M^n as a linear combination of I,...,M^(n-1), so (1) implies every higher parameter vanishes by induction. The Neumann series is zero on an open set; the rational matrix is identically zero. This argument neither requires controllability/observability nor tests a singular resolvent at a pole. QED.

Consequently, without stability, the solution set is the real zero set of at most (n+1)rq scalar polynomials in mp unknowns, of degree at most n+1. The bound includes direct feedthrough (degree at most one). Zero and repeated polynomials may be removed. A complex Groebner-basis solution is not a real-feasibility decision: real roots are required.

## 4. Stability and a polynomial-size lifted encoding

**Theorem 2.** The stable DDP holds if and only if there exist K and a symmetric P satisfying (1), P positive definite, and M^T P+PM=-I.

**Proof.** A Hurwitz M admits the convergent integral P=integral_0^infinity exp(M^T t) exp(Mt) dt, which is positive definite and solves the equation. Conversely, for any complex eigenpair Mv=lambda v, multiplication gives 2 Re(lambda) v*Pv=-v*v<0, hence Re(lambda)<0. QED.

A compact low-degree encoding, useful for complexity rather than necessarily fastest in practice, introduces X_j (n by q) for j=0,...,n-1:

X_0=G; X_(j+1)=M X_j for j=0,...,n-2; F X_j=0; J=0.    (2)

Every scalar polynomial in (2) has degree at most two. To encode stability using polynomially many low-degree constraints, introduce symmetric P and lower-triangular L, require

P=L L^T, L_ii>0 for every i, M^T P+PM=-I.               (3)

The Cholesky characterization of positive definiteness makes (3) equivalent to Theorem 2. All equations in (2)-(3) have degree at most two. Count the variables before removing redundant constraints:

v_0=mp+n^2 q (unstable-allowed variant),
v_1=mp+n^2 q+n(n+1) (stable variant).

A safe polynomial count is

s_0=n^2 q+(n+1)rq,
s_1=s_0+2n^2+n.

In (2), the X equations number n^2 q, the output equations nrq, and feedthrough rq. In (3), using full matrix equalities counts n^2+n^2 equations plus n strict inequalities; symmetry is already built into the variables. Rational coefficients and their bit lengths grow at most polynomially in the dense input size. These formulas establish membership in the existential theory of the reals (exists-R) for both variants. They do not establish exists-R-hardness, NP membership, or polynomial-size rational controllers.

A complete rational-input decision algorithm is: construct (2), optionally (3), clear rational denominators by positive common multiples, and apply exact real-algebraic feasibility (e.g. sign-invariant cylindrical algebraic decomposition). CAD terminates, handles strict inequalities and all degenerate strata, and can return real-algebraic sample points on satisfiable cells. Basu (2014), Theorem 2.4, gives the arithmetic-operation bound (s d)^(2^O(v)); here d=2. Arithmetic complexity is not bit complexity. Let ell denote the total bit length of the explicit dense rational plant input. Combining the polynomial-size encoding with standard CAD coefficient-growth and bit bounds gives the conservative coarse bit upper bound 2^(2^poly(ell)). No uniform sharp coefficient-bit prefactor is asserted. Stronger existential-only bounds are available; see Basu Section 2.2 and Theorem 2.16. This is a known mathematical decision method, not a claim that the included bounded Z3 runs implement worst-case CAD, scale well, or resolve the book's structural question.

## 5. Exact subspace formulation with all D terms

**Theorem 3.** DDP without stability holds if and only if there are K and a subspace V of R^n such that

im G subset V, M V subset V, V subset ker F, and J=0.    (4)

**Proof.** If (1) holds, use V=span{im G,im MG,...,im M^(n-1)G}. Cayley-Hamilton gives invariance and (1) gives output annihilation. Conversely (4) annihilates every F M^j G and implies (1). QED.

For a fixed d-dimensional V, choose a full-column-rank basis T (n by d) and a full-row-rank annihilator N ((n-d) by n) with ker N=V. Empty matrices for d=0 or d=n are interpreted in their usual zero-dimensional sense. Define

H = vertical_stack(NB,D2),
R = horizontal_stack(C1 T,D1),
Q = [[N A T, N E],[C2 T,D22]].

All four conditions (4), with this same K, are precisely

H K R = -Q.                                            (5)

**Theorem 4 (fixed-V test).** A K satisfying (5) exists if and only if

ker R subset ker Q and im Q subset im H,                (6)

or equivalently

rank(vertical_stack(R,Q))=rank(R),
rank(horizontal_stack(H,Q))=rank(H).                    (7)

**Proof.** Necessity follows by composition. For sufficiency, ker R subset ker Q defines a well-defined map U:im R -> im Q, U(Ra)=-Qa. Since im Q subset im H, choose a linear lift of U through the surjection H:R^m -> im H. Extend this lifted map from im R to all of R^p. Its matrix is K, satisfying (5). All choices are finite-dimensional linear algebra. QED.

The test is independent of the basis/annihilator choices. It is genuinely linear in K once V is fixed, but existential search over V remains. Imposing only separate disturbance, output, and invariance rank conditions can be wrong: they must use one shared K. Stable DDP further requires a Hurwitz member in the affine solution set of (5); ranks alone do not provide it.

## 6. The controlled/conditioned-invariance lemma: scope and proof

For one fixed V and no extra input/output annihilation constraints, the following are equivalent:

(a) there exists K with (A+BKC1)V subset V;
(b) AV subset V+im B and A(V intersect ker C1) subset V.

**Proof.** Necessity is immediate. For sufficiency, quotient R^n by V using N. The map -NAv on V factors through C1|_V precisely because it vanishes on V intersect ker C1. Its image lies in im(NB) precisely by controlled invariance. Lift through NB and extend to all measured-output space as in Theorem 4. QED.

This does not require B injective, C1 surjective, or V complemented by a prescribed space. It is NOT, by itself, a sufficient DDP or stable-DDP test. The complete feedthrough-sensitive constraints are (5).

## 7. Concrete lattice obstruction

Set n=3, B=e3, C1=[1,1,0], A e1=e3, A e2=-e3, A e3=0. Restrict candidate V to S=span(e1,e2). Then V1=span(e1) is invariant under A+B(-1)C1, and V2=span(e2) under A+B(1)C1. But V1+V2=S is not output-feedback invariant under any scalar K: the e3 coefficients on e1 and e2 are 1+K and -1+K, which cannot both vanish. Equivalently e1-e2 lies in S intersect ker C1 but A(e1-e2)=2e3 is outside S.

A greatest output-feedback-invariant subspace contained in S would have to contain both V1 and V2, and hence equal S. Therefore no greatest element exists. This refutes a naive supremal-subspace iteration, not all geometric algorithms. It also does not assert that *every* plant lacks a greatest element.

## 8. Lower bound from unrestricted output-feedback stabilization

Given any rational SOF stabilization instance (A,B,C), create a DDP instance with C1=C, q=r=1, E=0, C2=0, D1=0, D2=0, D22=0. Then T(s)=0 for every K, whereas stable DDP holds exactly when A+BKC is Hurwitz. The embedding is polynomial time and adds only zero data. It preserves integer coefficient magnitude bounds. Therefore Theorem 1 of Ahmadi, Chaudhry, Narang and Tang, arXiv:2609.20636v2, transfers strong NP-hardness to general stable DDP. This source is a recent preprint; the full source proof is not independently reproduced by this project. Our reduction is proved here and checked on small plants.

The 1997 Blondel-Tsitsiklis theorem alone does NOT justify unrestricted SOF hardness: it restricts gains to intervals. The 2026 theorem explicitly removes that restriction. The embedding supplies no hardness for DDP *without* stability: that embedded problem is then trivially feasible. NP-hardness rules out polynomial-time algorithms unless P=NP, but does not rule out concise characterizations or exact exponential-time algorithms.

## 9. Evidence boundaries

Theorems 1-4, the fixed-subspace invariance lemma, and the lattice counterexample are self-contained mathematical certification, independently examined in `../evidence/codex-referee-reply.md`. Finite algebra checks are recorded in `../evidence/verification.json`; the reviewer was not asked to audit those computations. No novelty is asserted. The hardness reduction is self-contained, but its inherited lower bound depends on the cited 2026 theorem: this is not an independent proof of that paper's full 3SAT reduction. Exact small-instance checks test implementation and boundary cases; they do not prove universal mathematical statements. No kernel-checked formal proof is claimed.
