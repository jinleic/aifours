# P44 v26 — PART27: a SHARP unrestricted trace bound at the rank-two zero, with explicit globally K2-positive DEC extremizers

PhysicsPPT44-2. Actual preceding `/bin/date`: **Mon Oct 26 06:44:08 PDT 2026**. AUTHOR-WRITTEN, LATER UNREVIEWED. Exact symbolic linear algebra/standard integration only; no machine-checked arithmetic, scientific interpreter, parameter trial or new GO. Same original P44/eighteen/HOLD/cutoff/deadline.

## U0. Scope and authority: a FULL-cone necessary bound, NOT an original P44 outcome

This continues the SAME unrestricted regular-zero representation of Part24, after ACTUAL v118-A RETURN and the separate whole-primary ACK **5315c8e48b34da02fd7240e576b90547ec6781ac876c183dc75758a8194d3057** was written and SENT before primary/source work. No review is live. The complete26part+2addenda union and both positive-PRIOR source intakes remain bound in checkpoint126, SHA256 **4e291a78c79570b5992863087451842fccd440b33406738ac02e5fa7e2c08024**. No predecessor is edited.

Parts25–26 give exact global-plane and all-PPT-charge interfaces, not a new scientific outcome. The complete KG2509.07086v1 and MOM2104.14058v5 intakes explicitly credit generic Schur peeling, local extensions, Schmidt-border and all-complex-plane positivity as PRIOR. The result below is a directly supplied full-cone extremal calculation, not a claim of world novelty or a method/source priority theorem.

**P44 remains UNMET:** neither an actual globally K2-positive indecomposable W/PPT-negative pair nor an unrestricted all-state SN<=2 theorem is supplied. The decomposable extremizers below prove sharpness of a NECESSARY bound; their decomposability is not a substitute family outcome.

## U1. Exact theorem and notation

Identify vectors with complex4x4 matrices X, in2x2 blocks `X=[[A,B],[C,N]]`. Put `X0=[[I2,0],[0,0]]`, write Omega=vec(I2) in the A-space, and let W be ANY Hermitian operator globally nonnegative on EVERY complex matrix of rank<=2, with q_W(X0)=0. Part24's exact first variation gives

    W vec(X0)=vec([[0,0],[0,Delta]]), Delta in M2(C).

Let `||Delta||_*` denote the sum of singular values and `||Delta||_F` its Frobenius norm. The full trace is the trace of W on the16-dimensional bipartite space, with ||Omega||^2=2.

**Theorem U1 — WRITTEN at the explicitly stated finite-dimensional facts below.** EVERY such global W satisfies

    Tr(W)>=4||Delta||_*+sqrt(6)||Delta||_F.             (SHARP)

For EVERY prescribed nonzero complex Delta, equality is ATTAINED by an explicitly given Hermitian W in K2 AND DEC, with the SAME exact zero X0 and W X0=Delta. For Delta=0, W=0 attains equality. Thus (SHARP) is a sharp full-cone bound; it is not a sufficient condition for K2 or DEC, and no assertion that every equality case is decomposable is made.

The standard imports are PSD kernel/Schur complements, SVD/Takagi factorization, ordinary unitary-invariant sphere integration with its elementary second/fourth moment, Cauchy–Schwarz/trace-singular-value inequality and continuity. The specialized inequalities, global positivity of the extremizer and explicit DEC decomposition are proved here. No unreviewed source theorem about the original4x4 problem is imported.

## U2. Hessian trace floor: EVERY normal coupling costs at least4 nuclear norms in the off-diagonal tangent directions

Write the tangent space as A⊕U with U=(B,C), and N-space as the lower-right block. Since all A and all N matrices have rank<=2, their W diagonal restrictions H_AA and W_NN are PSD. The full tangent restriction H is PSD by Part24's exact complex second variation; H_AA Omega=0. Let

    h=Tr(H_AA)>=0,
    S=H_UU-H_UA H_AA^+ H_AU>=0.

The PSD range condition is included even when H_AA is singular. Part24 gives the universally-COMPLEX inequality

    u^dagger S u>=|u^T R_Delta u|,
    R_Delta=[[0,K_Delta],[K_Delta^T,0]],
    b^T K_Delta c=Tr(Delta^dagger C B), u=(b,c).       (HESS)

For ANY complex symmetric R, this inequality implies `Tr S>=Tr sqrt(R^dagger R)`. Indeed take a Takagi factorization R=U D U^T, D diagonal nonnegative. With u=conjugate(U)z, the transformed Hermitian S'=U^T S conjugate(U) has the same trace, and testing z on each coordinate gives S'jj>=Djj. Summing proves the claim. This is only a necessary trace consequence of the FULL inequality; coordinate tests are NOT substituted as a global positivity certificate.

Here K_Delta has each singular value of Delta twice, because its index contraction has two identical Delta blocks up to row/column permutations. R_Delta then has each singular value of Delta FOUR times: R^dagger R has diagonal blocks conjugate(K)K^T and K^dagger K. Thus

    Tr(S)>=4||Delta||_*.

Since `H_UA H_AA^+ H_AU>=0`,

    Tr(H_UU)>=4||Delta||_*.

This controls the off-diagonal tangent contribution, but does not yet charge for the nonzero A/N coupling itself. The next step supplies that missing global cost.

## U3. A rank-one sphere average couples the A and normal traces without an ansatz

Let u be uniformly distributed on the complex unit sphere in C2, and put A_u=u u^dagger. This is a rank-one2x2 matrix, with trace1 and Frobenius norm1. Its coefficient vector is u tensor conjugate(u). The exact identities are

    E vec(A_u)=Omega/2,
    E |vec(A_u)><vec(A_u)|=(I4+|Omega><Omega|)/6.       (MOMENT)

For completeness, `E(|u><u| tensor |u><u|)=(I+Flip)/6`: the average is supported on the symmetric two-copy subspace, is scalar there by unitary invariance, and has trace1; that symmetric subspace has dimension3. Transposing the second factor gives the second MOMENT identity. The first follows from `E|u><u|=I2/2`. These are exact ordinary integrals over symbolic unit vectors, not sampled points, a numerical parameter scout or an executed enumeration.

Because H_AA Omega=0, MOMENT gives

    E q_W([[A_u,0],[0,0]])=h/6.

Fix ANY normal rank-one matrix Y in M2(C). For EVERY complex s, `[[s A_u,0],[0,Y]]` has rank<=2. Average its NONNEGATIVE W quadratic form over the SAME u. Using W X0=Delta and E A_u=I2/2 gives EXACTLY

    (h/6)|s|^2+q_W([[0,0],[0,Y]])
                  +Re(conjugate(s) Tr(Delta^dagger Y))>=0. (AVG)

If h=0, varying arbitrary complex s forces Tr(Delta^dagger Y)=0 for every rank-one Y, hence Delta=0. If Delta≠0, therefore h>0. Minimizing the scalar quadratic in s, without choosing any numerical value, yields

    q_W([[0,0],[0,Y]])
       >=(3/(2h))|Tr(Delta^dagger Y)|^2
       for EVERY complex rank-one Y.                 (NORMAL-ORDER)

Sum this inequality on an orthonormal product matrix basis of the normal2x2 space. Parseval gives

    Tr(W_NN)>=(3/(2h))||Delta||_F^2.                  (NORMAL-TRACE)

This is an unrestricted necessary condition derived from actual globally rank-two test matrices, not a local-Hessian converse or an assumed isotropic/symmetric W.

## U4. Combine the independent charges

The trace splits orthogonally across A,U,N, so for Delta≠0,

    Tr W=h+Tr H_UU+Tr W_NN
       >=4||Delta||_*+h+3||Delta||_F^2/(2h)
       >=4||Delta||_*+sqrt(6)||Delta||_F.

The last inequality is the exact AM–GM identity for positive h, with equality in that scalar step at `h=sqrt(3/2)||Delta||_F`. For Delta=0, TrW>=0 follows already by summing the nonnegative diagonal expectations on a product basis, so (SHARP) holds as well.

In particular a nonzero trace-normalized global witness has the compact normal-coupling bound `4||Delta||_*+sqrt(6)||Delta||_F<=1`. This does not make that norm bound sufficient for the remaining global/DEC/PPT-pair conditions.

## U5. Explicit equality candidate for diagonal normal coupling

First prescribe `Delta=D=diag(d1,d2)>=0`, not both zero, and choose ANY exact symbolic alpha>0. Define W_(alpha,D) by its Hermitian quadratic form on ALL complex blocks:

    q_(alpha,D)(X)
      =alpha(||A||_F^2-|Tr A|^2/2)
       +||B D^(1/2)||_F^2+||D^(1/2) C||_F^2
       +|Tr(D N)|^2/(2alpha)
       +Re(conjugate(Tr A) Tr(D N)).                 (EXT)

This is a fully specified Hermitian operator, not a restricted list of tested vectors. Its A/N cross block is `( |Omega><D|+|D><Omega| )/2`. Directly,

    q_(alpha,D)(X0)=0, W_(alpha,D) X0=Delta,
    Tr W_(alpha,D)=3alpha+4Tr D+||D||_F^2/(2alpha).    (EXT-TRACE)

The A term has trace3alpha because its4-dimensional operator is alpha(I4-|Omega><Omega|/2). Each off-diagonal tangent term has trace2Tr D. The N term has trace||D||_F^2/(2alpha). No normalization or hidden multiplicity is omitted.

## U6. GLOBAL complex rank-two positivity of the extremizer — not inferred from its local Hessian

Take any rank<=2 X with invertible A. Its exact Schur relation is `N=C A^(-1)B`. Let L>=m>0 be the singular values of A, set `tau=|Tr A|`, `a=||A||_F^2=L^2+m^2`, and `z=Tr(D N)`, r=|z|. Cauchy–Schwarz gives

    |z|=|Tr((D^(1/2)C) A^(-1) (B D^(1/2)))|
       <=m^(-1)||D^(1/2)C||_F ||B D^(1/2)||_F.

Thus the TWO tangent terms in EXT have sum at least2m r. The trace-singular-value bound gives tau<=L+m. Consequently

    q_(alpha,D)(X)
       >=alpha(a-tau^2/2)+(2m-tau)r+r^2/(2alpha).    (GLOBAL)

If tau<=2m, the last two terms are nonnegative and `a>=tau^2/2`, so GLOBAL is nonnegative. If tau>2m, minimize its last quadratic over r>=0 at the symbolic value alpha(tau-2m). The result is

    q_(alpha,D)(X)>=alpha[a-tau^2+2m tau-2m^2]
                  =alpha[L^2-(tau-m)^2]>=0,

since0<tau-m<=L. All A,B,C,N, singular values and phases remain arbitrary; this proves positivity on the ENTIRE invertible-A rank-two chart, not on a selected numerical tuple.

That chart is dense in ALL complex matrices of rank<=2: factor X=YZ with Y4x2 and Z2x4, then perturb the upper2x2 block of Y and left2x2 block of Z to invertible ones while keeping their product arbitrarily close. The resulting product has rank2 and invertible A. These invertible blocks form dense open sets; no trial, program or sampled perturbation is used. Continuity of the Hermitian quadratic form extends the inequality to EVERY singular-A/rank-one/rank-zero case. Therefore

    W_(alpha,D) belongs to K2 GLOBALLY.

This step is indispensable: PSD tangent/normal blocks or the trace norm inequality alone would NOT prove it.

## U7. Explicit decomposability and sharpness for EVERY complex Delta

Use computational indices i=0,1 for the top blocks, and k=2,3 for the bottom, with d_k denoting d1,d2. Define the PSD operator

    Q=sum_(i=0,1; k=2,3) (d_k/2)
           | i,k + k,i >< i,k + k,i |.

Bob partial transpose sends its cross term |i,k><k,i| to |i,i><k,k|. Hence Q^Gamma supplies EXACTLY the A/N cross term in EXT and HALF of each off-diagonal tangent diagonal weight. The remainder P=W_(alpha,D)-Q^Gamma is the direct sum of:

- alpha(I4-|Omega><Omega|/2) on A;
- HALF of each positive weighted B,C norm operator;
- `|D><D|/(2alpha)` on N.

Every summand is PSD. Thus `W_(alpha,D)=P+Q^Gamma` is explicitly DEC. No inference from mere failure of complete positivity/copositivity or from an undeclared solver is made.

Choose the SYMBOLIC positive parameter `alpha=||D||_F/sqrt(6)`. EXT-TRACE becomes

    Tr W=4Tr D+sqrt(6)||D||_F,

attaining (SHARP). This is exact analytic minimization over the displayed symbolic family, not a numeric parameter probe or a claimed P44 counterexample.

For arbitrary complex Delta, take its SVD Delta=U D V^dagger. A local block-diagonal unitary, identity on both top2-dimensional factors and U / conjugate(V) on the two bottom factors, fixes X0 and sends D to Delta. Conjugating the constructed W by that local unitary preserves trace, K2 and DEC, and sends W X0 to the prescribed Delta. Thus equality is attained for EVERY Delta, including rank-one and fully complex nonsymmetric cases. Delta=0 is handled separately by W=0.

## U8. Exact advance and the still-unsettled original step

This supplies an UNRESTRICTED necessary trace/coupling inequality and proves its SHARPNESS with actual globally positive, explicitly decomposable extremizers. It is stronger than the Hessian-only4nuclear-norm charge because it uses genuine rank-two matrices with both a rank-one A and rank-one normal component. The added sqrt(6) term is not obtained by relabeling a local Hessian as global positivity.

Nothing here proves that a witness exceeding the bound is DEC, that all equality cases are DEC, or that any non-DEC global member exists. The constructed DEC extremizers give no negative PPT pair and are NOT an original closed-family outcome. Part25 ALL-complex-plane constraints, Part26 genuine PPT-entangled compression and the actual CP-charge inequality remain unresolved jointly.

The next original mathematical gap is whether a globally admissible deviation from these sharp DEC extrema can leave DEC while retaining all-complex SR2 positivity, or whether an unrestricted DEC extraction exists. Any such deviation must be proved globally and paired with a strict eligible PPT target; no decimal tuple, finite phase sample, enumeration, solver/certificate request or old normalized-N4 mechanism substitutes for it.

All26parts/twoaddenda, TWOcomplete positive-PRIOR source intakes, held Alice-scalar-gauge lead and all cp120 earlier Delta/conditional-norm/CPtarget/Laurent/chart/range/Bell/code/PV/DOC leads remain saved. This theorem was derived AFTER checkpoint126; it is not absent, pre-v118, or backdated into an old ACK. All owncp049/063/081/083/085/089, oldcp013/admission and parent findings survive; N4 UNKNOWN/incomplete/exit-unestablished, old21 NOT_RECONSTRUCTED, C19–C27 FOUR minors and normalized N4 ZERO new-method credit. No clean cognition/runtime/cadence/blind-family or novelty assurance.

Only exact WRITTEN/source/metadata; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/build/test/nestedagent/newGO, approximate/numeric probes or withdrawn-output guidance. No old pin/body/parent edited. No formal/kernel/executable/human/configured-family/parent/novelty or publication acceptance. Original eighteen, science cutoff **2026-10-27T11:05:38-07:00**, deadline **2026-10-27T12:35:38-07:00** remain. Active increment, NOT early final park or round closeout. **P44 remains UNMET.**

**END OF COMPLETE v26 PART27.**
