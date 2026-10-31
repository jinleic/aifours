# P44 definition-first prerequisite: universal alternating-contraction coupling and an exact positive-reconstruction obstruction

Owner **PhysicsPPT44-2**, physics-3. Actual `/bin/date` immediately BEFORE this new immutable write: **Tue Oct 27 14:58:09 PDT 2026**. **WRITTEN, UNREVIEWED.** No mathematical identity was machine-checked. This is the first substantive result/obstruction under the narrow S1 release; it does NOT solve P44 or lift another STOP.

## 0. Actual authority, pre-body ACK and allowed premises

I read the complete S1 controls BEFORE the release metadata, then wrote the actual pre-body ACK `prerequisite-prebody-exposure-ack-v1.json`, SHA `ada308f5829bf015b81470e1896a67cff9384364daa55dd4831b9a090ca60566` (15 LF/3886 B; preceding clock14:47:13). Only afterward did I read EVERY LF of the 35-LF exact packet and its equality receipt. Packet SHA: `4715d2190da98abb8781bb5713e9c45af51c73dd43e85fd3cc54e5e92351279a`.

Inputs are ONLY the supplied parent definitions S2, S1/S0/current contract/own safe intake, and the explicitly named elementary facts below. The parent definitions are not a verbatim-book/source-equivalence certification. No old proof/review/park/checkpoint, Parts24–40, post40 guidance, old N4/solver cone, QD, held normal/zero-ensemble/marginal-scaling lead or private control is a proof premise. No historical scientific-progress/novelty claim is made for these elementary identities. Prior exposure survives; this is not blind or a counterfactual untouched-cognition certificate.

The map used below is the classical trace-complement/reduction map, defined and proved here on ALL operators. Its use is not an evaluation, repair or universalization of any old fixed reduction-witness/control instance. That earlier exposure/finding is retained, not erased by a new file or a classical name. No old instance, guide, special vector, normalization or result enters a proof edge below; the entire input graph is the present S2 definitions plus elementary matrix identities. A stronger historical noninfluence or novelty assurance is NOT asserted.

## 1. FIRST: verbatim primary-claim screen and its exact limit

Primary admitted by S2 ONLY for this screen: Nathaniel Johnston and Benjamin Lovitz, [arXiv:2609.11849v1](https://arxiv.org/abs/2609.11849v1), *PPT states of almost maximal Schmidt number*.

I read the public abstract through the arXiv reader and ONLY the introductory result statements [Theorem1](https://arxiv.org/html/2609.11849v1#Thmtheorem1), [Corollary2](https://arxiv.org/html/2609.11849v1#Thmtheorem2) and [Corollary3](https://arxiv.org/html/2609.11849v1#Thmtheorem3). Static whole-paper reading would expose forbidden constructions, so a browser DOM extraction returned only these statement containers, removed any proof containers, and rendered their supplied math alt-text. Only labels—not bodies—of the other theorem/lemma containers were displayed. No proof or construction was read. The browser tab was closed afterward.

Theorem1, verbatim wording with the displayed formula rendered from the primary's math alt-text:

> Let $m,n\geq 2$ be integers. There exists a PPT state $\rho\in\operatorname{Density}(\mathbb C^m\otimes\mathbb C^n)$ with
> $\operatorname{SN}(\rho)\geq\left\lceil\frac{m+n-\sqrt{(m-n)^2+4(m+n-1)}}{2}\right\rceil.$

Corollary2:

> Let $n\geq 2$ be an integer. There exists a PPT state $\rho\in\operatorname{Density}(\mathbb C^n\otimes\mathbb C^n)$ with
> $\operatorname{SN}(\rho)\geq n-\left\lfloor\sqrt{2n-1}\right\rfloor.$
> In particular, $\displaystyle\lim_{n\rightarrow\infty}\frac{M_{\mathrm{PPT}}(n,n)}{n}=1$.

Corollary3:

> Let $n\geq 2$ and $m\geq 3n-4$ be integers. There exists a PPT state $\rho\in\operatorname{Density}(\mathbb C^m\otimes\mathbb C^n)$ with $\operatorname{SN}(\rho)\geq n-1$.

These read result statements contain **no explicit 4x4 PPT SN>=3 assertion**. I did NOT evaluate or specialize their bounds, reconstruct a construction, authenticate their proofs, inspect a further theorem body or infer worldwide absence. The PRIOR-CLAIM stop trigger was not found at this EXACT screened scope. The source is identity-pinned by the release, not a locally whole-paper-SHA-authenticated proof input; NONE of its mathematics is used below. This report was sent to Main before drafting the derivation.

## 2. Exact original objects and elementary foundations

The original application remains A=B=C^4. For a stronger universal statement let A=C^a, B=C^b with arbitrary integers a,b>=2. We use the UNNORMALIZED cone C2 of positive operators having a finite decomposition into rank-one operators on complex Schmidt-rank<=2 vectors. For trace-one states this is precisely SN<=2 in S2. The zero operator is included.

Let rho be an arbitrary positive operator; write rho_A=Tr_B rho, rho_B=Tr_A rho and s=Tr rho. PPT means Gamma_B(rho)>=0; full transpose shows Gamma_A(rho)>=0 as well. Define

    D_A(X)=I_A tensor Tr_A X,       D_B(X)=Tr_B X tensor I_B,
    D_0(X)=Tr(X) I_AB,
    R_A=D_A-id,                    R_B=D_B-id.

R_A/R_B act on the specified local factors and commute. These are actual linear maps on the SAME bipartite operator space, not independently chosen copies.

W is an arbitrary Hermitian operator with `<v|W|v>>=0` for EVERY complex v of Schmidt rank<=2, exactly S2. Therefore Tr(W Z)>=0 for every Z in C2 by summing its actual rank-one decomposition. No real-only test is substituted.

Named elementary foundations: finite-dimensional spectral decomposition of positive operators; matrix-unit multiplication/transpose; the tensor-rank definition of Schmidt rank; trace cyclicity/partial trace; and a finite-dimensional operator-space direct sum into identity and traceless factors. Each used implication is proved below. No source-specific theorem, Haar average, solver, norm estimate, rank-floor result or QD is imported.

## 3. Universal two-row contraction identity — ALL complex inputs

For an ARBITRARY orthonormal basis of C^d, let

    A_ij=|i><j|-|j><i|      (i<j),
    Psi_d(X)=sum_(i<j) A_ij X A_ij^*,
    R_d(X)=Tr(X) I_d-X.

Each A_ij has rank two. For EVERY complex matrix X, the contribution of one pair to `A_ij X^T A_ij^*` is

    X_jj E_ii + X_ii E_jj - X_ij E_ij - X_ji E_ji.

Summing the symbolic indices gives diagonal entry `Tr X-X_ii` and every off-diagonal entry `-X_ij`. Thus the ENTIRE identity is

    R_d = Psi_d composed with transpose,
    Psi_d(X)=Tr(X) I_d-X^T.                                  (3.1)

This is a universal symbolic matrix identity, not a selected matrix/control, enumeration or execution. The arbitrary basis disappears from its right-hand side. Psi_d is explicitly a completely positive map with rank-two Kraus operators, by the displayed sum; no assertion of complete positivity for R_d is made.

If Z>=0 on a bipartite space and L has local rank<=2, spectral decomposition writes `(L tensor I)Z(L^* tensor I)` as a sum of rank-one terms whose local support is contained in im L. Every vector in them has Schmidt rank<=2. Hence that whole positive congruence is in C2. The same statement holds when BOTH local maps have rank<=2. It is valid for all ranks, singular inputs and zero terms.

## 4. Primal coupling theorem: actual PPT complements are C2, without cancellation

**Theorem1.** For EVERY PPT rho>=0, the following THREE operators are in C2 and are themselves PPT:

    X_A = I_A tensor rho_B-rho = R_A(rho),
    X_B = rho_A tensor I_B-rho = R_B(rho),
    X_AB = s I_AB-I_A tensor rho_B-rho_A tensor I_B+rho
         = R_A R_B(rho).                                   (4.1)

Moreover X_AB is in C2 for EVERY rho>=0, even without PPT.

**Proof for X_A.** Since rho is PPT, rho^(Gamma_A)=(rho^(Gamma_B))^T is positive. Equation(3.1) gives the ACTUAL decomposition

    X_A=sum_(i<j) (A_ij tensor I) rho^(Gamma_A) (A_ij^* tensor I).

Every term is positive with Alice support at most two, hence C2 by §3. The proof for X_B uses the actual Bob-side matrices and rho^(Gamma_B), with no exchanged-sign convention.

For the PPT property, partial transpose on B commutes with R_A. Apply the same argument to rho^(Gamma_B): it is positive and its Alice partial transpose is rho^T>=0. Thus `X_A^(Gamma_B)=R_A(rho^(Gamma_B))>=0`. The Bob-side argument is the same with the two commuting partial transposes. No partial transpose of a general C2 decomposition is assumed positive.

**Proof for X_AB.** The two local transposes together are FULL transpose, so

    X_AB=(Psi_a tensor Psi_b)(rho^T)
        =sum_(i<j,k<l) (A_ij tensor B_kl) rho^T
                                  (A_ij^* tensor B_kl^*).

For every positive rho, rho^T is positive; all summands have local support at most two on each factor. Hence X_AB is C2 without using PPT. If rho is PPT, apply that SAME all-positive-input assertion to rho^(Gamma_B); R_A R_B commutes with Gamma_B, proving the additional PPT property. Expanding the two commuting R maps gives exactly(4.1). No normalization or inverse marginal was used. QED.

For a nonzero density input, these are generally unnormalized C2 operators; they may be normalized only if their actual trace is nonzero. Zero outputs are retained as zero cone elements. The proof does not divide by rho's trace, rank, marginal eigenvalues or any witness expectation.

The exact identity

    X_A+X_B+X_AB = s I_AB-rho                             (4.2)

also gives `s I-rho in C2` for PPT rho. This is a trace-COMPLEMENT statement, not rho in C2. The full identity is retained; no negative term is discarded.

## 5. Dual coupling theorem: explicit decomposable trace-complement of W

Use Gamma_B as S2's fixed partial transpose. Put

    K_A=(Psi_a tensor id)(W),
    K_B=(id tensor Psi_b)(W).

Every summand of K_A is positive: for arbitrary phi, `(A_ij^* tensor I)phi` has Alice support<=2, so its W expectation is nonnegative. The same proves K_B>=0. Equation(3.1) gives

    (R_A W)^(Gamma_A)=K_A,
    (R_B W)^(Gamma_B)=K_B.

Therefore `(R_A W)^(Gamma_B)=K_A^T>=0`, using FULL transpose, not an illegal claim that partial transpose preserves arbitrary positivity. Both R_A W and R_B W are completely copositive with respect to the specified Gamma_B.

Also

    Z_W=R_A R_B(W)

is positive. One direct proof is the same displayed rank-two congruence formula applied to W^T: full transpose preserves two-block-positivity, and every vector pulled back by `A_ij^* tensor B_kl^*` has Schmidt rank<=2. Thus each summand is positive even though W itself need not be positive.

As an identity of SUPEROPERATORS,

    R_A+R_B+R_A R_B=D_0-id.

Consequently the ACTUAL operator

    Tr(W) I_AB-W = Z_W + (K_A^T+K_B)^(Gamma_B)             (5.1)

has an explicit decomposable representation with BOTH displayed positive operators. This is a genuine universal map from every complex two-block-positive W into a decomposable TRACE-COMPLEMENT; it is NOT a decomposition of W. No original all-W decomposability theorem is claimed.

## 6. Joint actual-state/witness budget and its one-way caller

For the SAME actual rho,W define

    a0=Tr(W rho),
    b_A=Tr(W(I_A tensor rho_B)),
    b_B=Tr(W(rho_A tensor I_B)),
    t=Tr(rho) Tr(W).

The marginals are positive, so the two marginal-noise operators and `s I` are separable; hence b_A,b_B,t>=0. Theorem1 and the actual dual pairing give, for EVERY PPT rho and EVERY two-block-positive W,

    b_A+b_B-t <= a0 <= min(b_A,b_B).                      (6.1)

The lower bound already holds for every positive rho by the unconditional X_AB statement. The two upper bounds use PPT through X_A/X_B. Equation(5.1) also gives a0<=t directly. All constraints concern the SAME state, marginals, witness and partial-transpose convention.

Thus an eligible negative pair MUST satisfy

    a0<0  and  b_A+b_B<t.                                 (6.2)

Conversely, if an actual eligible pair has `b_A+b_B>=t`,(6.1) rules out its strict negative separation. This is a universal coupling obstruction, not a coordinate encoding or a selected numerical test. It is not restricted to an old chart, a rank floor, a chosen state or a proper witness ansatz.

**Non-converses are explicit:** the strict budget inequality alone does not prove a0<0, positivity/PPT, two-block-positivity or existence of an eligible pair. Neither (6.1) nor decomposition(5.1) proves W decomposable or rho C2. Actual negativity plus the other ORIGINAL conditions is still required to invoke S2's stated SN>=3 equivalence. That equivalence is the parent-supplied definition-side premise, not a newly authenticated printed-book theorem.

All degeneracies are covered without cancellation/division. rho=0 gives a0=b_A=b_B=t=0. W=0 does likewise. Singular rho/marginals and zero complement terms remain valid. No positive scalar threshold, artificial full-rank regularization or source-selected example is introduced.

## 7. Exact obstruction to reconstructing rho by positive complement iterations

The next tempting step is to recover the original rho as a positive combination of the universally C2 outputs in §4. This step has a precise obstruction at the fixed-linear-map level.

**Theorem2.** Suppose a,b>=3. Let Phi be ANY finite combination with nonnegative real coefficients of nonempty monomials `R_A^p R_B^q`, p,q>=0 and p+q>=1. One may additionally add nonnegative multiples of D_A,D_B,D_0. Then Phi cannot equal a positive scalar multiple of the identity superoperator. The same exclusion holds for limits of such maps in a finite-dimensional superoperator norm.

**Proof on the ENTIRE operator space, not a selected state.** On each local Hermitian space use the complete direct sum `R I direct-sum Herm_0`. Their tensor product gives all FOUR sectors. The monomial eigenvalues are

| Sector | R_A^p R_B^q |
|---|---|
| I tensor I | (a-1)^p(b-1)^q |
| traceless-A tensor I | (-1)^p(b-1)^q |
| I tensor traceless-B | (a-1)^p(-1)^q |
| traceless-A tensor traceless-B | (-1)^(p+q) |

This is a whole-space identity following from the definition of partial trace. No particular matrix, density operator or parameter boundary is substituted as a viability probe.

Put `mu=min(a-1,b-1)>1`. Every NONEMPTY monomial has its first-sector eigenvalue at least mu and its last-sector eigenvalue of absolute value one. For the nonnegative sum, with eigenvalues lambda_00 and lambda_11,

    lambda_00 >= mu * sum(coefficients)
              >= mu * abs(lambda_11).                    (7.1)

D_A,D_B,D_0 have nonnegative first-sector eigenvalues and zero last-sector eigenvalue, so their optional positive additions preserve the inequality. A positive multiple c*id has lambda_00=lambda_11=c>0, contradicting(7.1). Both eigenvalues are continuous linear functionals on this finite-dimensional diagonal-map space, so its norm limits still satisfy(7.1) and cannot be c*id. QED.

For the ORIGINAL4x4 space the dimension hypothesis holds without changing the problem. Every nonempty complement iteration sends PPT inputs to C2: Theorem1 gives the first step, preserves PPT, and therefore may be iterated. Nevertheless their positive linear-map cone cannot reconstruct the identity on ALL original inputs. This proves the exact failed **fixed positive-reconstruction mechanism**, not a no-go for states, for arbitrary maps, for state-dependent coefficients or for other representations.

## 8. Precisely what is gained and what remains unpaid

Gained in this NEW definition-side packet, without executable or novelty credit:

1. a full rank-two Kraus/congruence proof that the actual one-sided complements of EVERY PPT input are PPT and C2;
2. the unconditional double-complement C2 statement and the explicit decomposable trace-complement(5.1) for EVERY two-block-positive W;
3. the actual joint budget obstruction(6.1)–(6.2), with full complex inputs and no omitted singular cases;
4. an exact whole-superoperator-cone obstruction to turning those complement results into an all-state proof by fixed nonnegative iteration/noise combinations.

The missing implication is now explicit: **membership of the actual complements in C2 does not license subtraction/cancellation to put rho itself in C2.** That desired PPT-specific cancellation theorem is not supplied by the definition of a convex cone, and Theorem2 excludes one natural fixed-positive-map way of obtaining it. Conversely, no actual violating rho,W pair has been obtained. A cone is closed under positive addition, not arbitrary subtraction; I do not assert an unproved original-PPT counterexample to any stronger cancellation statement.

No claim that these classical identities are novel, historically absent from old files or already parent-adopted is made. Their useful present scope is the universal coupling and exact limited-mechanism obstruction, NOT unrestricted all-state closure. Proper-class rank-floor and PV/D-type adoptions were not needed as proof inputs and are not promoted. Old QD, N4, published-source imports and the source/book authentication gaps remain at their existing cuts.

## 9. Continuation and assurance

The next admitted definition-only question is whether the fixed positive-reconstruction obstruction survives the OTHER four PPT-preserving input transposes; no old formula or guide will be used to answer it. This is a new all-variable map question within the SAME actual object space, not a selected boundary test. A successor/addendum will state its exact scope and will not edit these frozen bytes. No route beyond this narrow release is self-authorized.

Current claim-screen/browser operations were SOURCE EXTRACTION only: primary abstract reader, theorem-label metadata and exact statement-container text extraction. They evaluated no scientific expression or identity. All mathematics above is WRITTEN. No interpreter/calculator/CAS/arithmetic Eval, scientific program/enumeration/solver/replay/build/test/typechecker, nested agent/modelCLI/paidAPI, selected state/control/decimal/boundary sample, Git, deletion, contact/publication or infrastructure mutation was used. No old body was reopened.

Every prior owner/reviewer/parent finding and ZERO quarantine persists; N4 UNKNOWN/historical child-exit unestablished, old21 NR and auxiliary214 STOP remain. No clean-history/private-cognition/noninfluence census, original P44 outcome, source-construction verification, formal/kernel/executable/human/configured-family or novelty acceptance follows. This is same-harness **WRITTEN UNREVIEWED** prerequisite work under S1, not an original-primary blanket restart or96-hour closeout. Successor science deadline remains2026-10-31T21:23:27.000Z.
