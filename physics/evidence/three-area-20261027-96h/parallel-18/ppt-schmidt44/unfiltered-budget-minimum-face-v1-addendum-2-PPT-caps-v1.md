# Unfiltered minimum-face addendum2 — actual PPT dual caps, priced cap upper bounds, and the exact missing improvement

Owner **PhysicsPPT44-2**, physics-3. Actual native `/bin/date` immediately BEFORE this NEW immutable write: **Tue Oct 27 17:26:02 PDT 2026**. **WRITTEN UNREVIEWED**. This is a substantive exact failed-PPT-coupling result, NOT favorable sign or an eligible negative-pair certificate.

## 1. Same narrow boundary and newly adopted input

Main's17:20 continuation asks for use of the ACTUAL PPT condition to reach the residual threshold, or an exact failing coupling. The earlier actual pre-derivation ACK `b49ec7b0...` and release `e7064ab24f10a1228c22b9d9c7c2e9a6868b4aee3d2818eaf2c422ec9ec300ff` remain binding for this SAME original-operator scope.

I read the COMPLETE parent disposition `physics-3-minimum-face-sign-cases-and-negative-margin-parent-v1.md` through its ending. Its exact adopted statements are inputs: product-zero/kernel and small-support signs, original minimum-face equivalence, Z positivity/identity and the quantitative margin. I did not open its linked reviewer or any old proof. The supplied current source bodies were already completely read/reconstructed under that ACK; adoption is not backdated in their immutable headers.

No projector/congruence/compression/filter/regauging/marginal normalization or lower-dimensional substitute is used. W stays the ORIGINAL input W. The only state transpose below is rho's actual partial transpose already required by PPT; it remains on C^4 tensor C^4 and BOTH positivity conditions are retained. No selected operator/state/basis/parameter or sanity probe, even privately, supplies proof or confidence.

## 2. Exact original objects

Let W be EVERY nonzero Hermitian operator nonnegative on EVERY complex SR<=2 vector, with

    A=Tr_B W, B=Tr_A W, tau=Tr W,
    alpha=lambda_min(A), beta=lambda_min(B),
    E_A=Emin(A), E_B=Emin(B).

The residual case is alpha,beta>0 and both minimum spaces of dimension>=3. Let rho be EVERY PPT density operator with original range in E_A tensor E_B. Set

    sigma=rho^(Gamma_B),       Y=W^(Gamma_B),
    a0=Tr(W rho)=Tr(Y sigma).

Define the following ORIGINAL-space auxiliary operators:

    C_A=I_A tensor B^T-Y,
    C_B=A tensor I_B-Y.                                   (2.1)

These are exact trace/transpose expressions of the SAME W, not a replacement witness, tested ansatz or new input. Section3 proves their positivity directly from the original vector condition, without physical transformations.

## 3. Intrinsic positive-cap lemma — full original-vector identity

**Lemma1.** C_A>=0 and C_B>=0 for EVERY W as above.

Use the ORIGINAL defining reference family e_j of the Bob transpose, not a basis selected for a test. For ANY original vector psi, write the exact full expansion `psi=sum_j x_j tensor e_j`, with all x_j arbitrary original Alice vectors. Elementary partial-trace/transpose index algebra gives

    <psi|C_B|psi>
      =sum_(j<k) <x_j tensor e_k-x_k tensor e_j | W |
                         x_j tensor e_k-x_k tensor e_j>.  (3.1)

To verify the ENTIRE identity, the A tensor I pairing is `sum_(j,k) q_W(x_j tensor e_k)`, while the Y pairing is `sum_(j,k)<x_j tensor e_k|W|x_k tensor e_j>`. The diagonal j=k terms cancel; the two cross terms for each unordered pair form exactly the displayed quadratic expression. No coefficient values or particular vector are substituted.

Each vector on the right is a sum of TWO original product vectors and has SR<=2. Therefore the right side is nonnegative for EVERY psi, proving positivity of the ORIGINAL C_B. No local map/congruence or compressed operator is introduced by this scalar identity.

The Alice-side version proves `I tensor B-W^(Gamma_A)>=0`. Full transpose, which preserves positivity, gives C_A as defined in(2.1). This is a full-transpose identity, NOT an assertion that partial transpose preserves arbitrary positivity. The proof includes all complex x_j and all zero/degenerate terms. QED.

The lemma reproduces the relevant positive caps intrinsically; it does not inherit a Kraus/filter operation from another proof or turn Y into a positive operator.

## 4. The ACTUAL PPT state stays a coupled original object

Since rho is PPT, sigma>=0, Tr sigma=1, and `sigma^(Gamma_B)=rho>=0`. Thus sigma is itself PPT. The exact support transport is

    range sigma subset E_A tensor conjugate(E_B).          (4.1)

To prove it without a projector, expand each original spectral vector of rho in products x tensor y with x in E_A,y in E_B. The definition of partial transpose gives for every pair of terms

    (|x tensor y><x' tensor y'|)^(Gamma_B)
       =|x tensor conjugate(y')><x' tensor conjugate(y)|.

Every image ket stays in the indicated ORIGINAL subspace. Summing proves(4.1); individual transposed terms are not assumed positive. Their actual sum is positive ONLY because of the given PPT condition.

Conversely any ORIGINAL PPT density sigma with(4.1) gives rho=sigma^(Gamma_B)>=0 with range in E_A tensor E_B by the SAME full tensor identity and conjugation twice. Its partial transpose is sigma>=0. This is an exact forward/converse bijection retaining BOTH positivity predicates, not permission to choose sigma as an arbitrary positive state or a transformed smaller-dimensional problem.

Because B is Hermitian, B^T acts on conjugate(E_B) by beta; A acts on E_A by alpha. Consequently the ACTUAL cap expectations are

    u=Tr(C_A sigma)=beta-a0,
    v=Tr(C_B sigma)=alpha-a0,
    v-u=alpha-beta.                                      (4.2)

Lemma1 and the ACTUAL sigma>=0 imply u,v>=0, hence `a0<=min(alpha,beta)`. This uses PPT but is an UPPER bound on a0, not the favorable lower sign.

## 5. Pricing BOTH ordinary PPT reduction inequalities

The adopted original complement theorem applies to sigma, because BOTH sigma and sigma^(Gamma_B) are positive:

    I_A tensor sigma_B-sigma>=0,
    sigma_A tensor I_B-sigma>=0.                          (5.1)

These are operator inequalities on the SAME original partial transpose. They are not normalized into a replacement state or used to transform the problem.

The original cap partial traces, from(2.1), are exactly

    Tr_A C_A=(d_A-1)B^T,       Tr_B C_A=tau I_A-A,
    Tr_A C_B=tau I_B-B^T,      Tr_B C_B=(d_B-1)A,          (5.2)

where d_A,d_B are the dimensions of the ORIGINAL factors, not minimum-space dimensions. They remain the original dimensions throughout.

Pair BOTH inequalities(5.1) with the positive ORIGINAL C_B. Using(5.2) and the actual range condition of sigma gives

    v<=tau-beta,
    v<=(d_B-1)alpha.

For C_A the two pairings similarly give

    u<=(d_A-1)beta,
    u<=tau-alpha.                                        (5.3)

Every use of positivity and partial trace has been paid on actual original operators. No missing target-copy/commuting-form assumption or restricted trace has been substituted.

Equivalently this explicit use of the ACTUAL PPT condition yields

    a0>=max{alpha+beta-tau,
             -(d_B-2)alpha, -(d_A-2)beta}.                (5.4)

It is a valid bound, but does not reach zero in the residual positive-minimum case. It does not improve the already adopted `a0>=-kappa*c`: with c=min(alpha,beta) and kappa=max(min(dim E_A,dim E_B)-2,0), the intrinsic dimension bounds give `kappa*c<=(d_B-2)alpha` and the analogous Bob-side inequality. No parameter or spectral multiplicity was evaluated to make this comparison.

Thus simply applying the standard positive complements to the actual PPT transpose does NOT raise the previously priced floor. This is a proved limitation of this SPECIFIC inference chain, not a claim that full PPT plus full SR2 positivity can never supply the missing relation.

## 6. Exact missing cap upper, with all directions retained

On the actual face the adopted original residual is

    Z=tau I-I tensor B-A tensor I+W>=0.

Its transpose identity is

    Z^(Gamma_B)=tau I-I tensor B^T-C_B
               =tau I-A tensor I-C_A.

There is NO assertion Z^(Gamma_B)>=0. The actual trace equality gives

    Tr(Z rho)=tau-beta-v=tau-alpha-u.                     (6.1)

The favorable threshold is therefore EXACTLY

    Tr(Z rho)>=tau-alpha-beta
      IFF v<=alpha
      IFF u<=beta
      IFF a0>=0.                                         (6.2)

Lemma1 gives lower bounds on u,v, and(5.3) gives weaker upper bounds. Neither supplies(6.2) at the residual case. The missing original PPT coupling is precisely

    NR-PPT-CAP-UPPER:
    Tr(C_B sigma)<=alpha
    for EVERY ACTUAL sigma=rho^(Gamma_B) in(4.1),
    sigma>=0 AND sigma^(Gamma_B)>=0,
    with C_B constructed from the SAME full-complex-SR2 W.

The equivalent C_A form must be kept if sides are exchanged. A positive operator C_B and a positive state sigma have nonnegative expectation; that is NOT an upper bound alpha. Dropping the backward positivity sigma^(Gamma_B)>=0 would instead enlarge the state set and change the caller. Likewise partial transpose cannot be moved from the positive state into a supposed positivity of Y or Z^(Gamma_B).

The common cap excess is the exact symbolic quantity `u-beta=v-alpha=-a0`. The already adopted margin only bounds this excess above by kappa*c; the desired sign requires it nonpositive. This statement describes the FULL algebraic gap. No particular scalar tuple is selected or asserted realizable by an original rho,W; no numerical counterexample or actual negative pair is inferred from a loose interval.

## 7. Exact result, stopped prospective branch and remaining work

Newly completed here are the full original-vector positive-cap identity(3.1), the two-way actual PPT-face transport, BOTH reduction pairings and their full-trace constants, and the exact cap upper that those priced PPT steps still fail to establish. The result uses the ACTUAL PPT condition rather than ignoring it, and isolates its wrong-direction/insufficient-threshold use precisely.

The equivalence(6.2) is a caller identity, not counted as a solution. No positive-minima/high-dimensional sign or complete negative certificate is obtained. The existing zero-minimum and <=2-support sign cases stay adopted; the residual original case is not exhausted. Excluding every minimum-face negative pair, if achieved later, would still exclude only that route, not all PPT states.

While seeking a stronger bound I identified a changed-witness reformulation as a prospective branch. It is NOT pursued as a proof method: it would alter the original input boundary. No altered witness is used as a source/input, no favorable assertion about it is retained or backconverted, and no actual operator/state case was evaluated. That branch and any consuming confidence are NONINPUT; the complete proof above uses only the original W, its actual trace/transpose expressions and rho's mandated PPT transpose. This is a boundary disclosure, not an attempt to rename a forbidden transformation.

There is also no replacement of the full constants d_A,d_B in(5.2) by dimensions of E_A,E_B. Doing so would require a different trace/operator identification, not the original full partial traces; no compressed trace or projector operation is introduced to claim it.

A genuine next success needs a new original-operator coupling proving NR-PPT-CAP-UPPER, or a full eligible original pair violating it. Neither positive-cap existence, ordinary reduction inequalities, nor the merely formal possibility of a positive excess is that success. A further proof cannot silently import the stopped filter/scaling/normalization branch, an old guide, JL construction or L1 consumer to supply it.

## 8. Assurance

Sole inputs are the current original definitions and adopted statements at exact scope, plus elementary full tensor/trace/positive-form algebra reconstructed above. No peer-return lookup, outside source, old proof/held body or author contact. No projector/congruence/compression/filter/regauging/normalization or lower-dimensional replacement is a proof step. The original fixed transpose reference is used for the FULL arbitrary-vector identity, never as a basis sanity probe.

No scientific interpreter/calculator/Eval arithmetic/CAS/program/enumeration/solver/replay/build/test/typechecker, selected operator/state/basis/parameter/control example even privately, nested agent/modelCLI/paidAPI, Git/delete/contact/publication/infrastructure action. All history/STOP/HOLD/ZERO—including w30, JL and L1 consumers—N4 UNKNOWN historical exit unestablished, old21 NR and auxiliary214 STOP persist. No mathematical identity machine-checked, clean-cognition/noninfluence, formal/kernel/human/configured-family/executable/novelty/P44 acceptance. Successor science end2026-10-31T21:23:27.000Z unchanged.

## 9. Additive comparison proof BEFORE the first pin/return

Actual native observation before this pure append: **Tue Oct 27 17:28:28 PDT 2026**. No prior bytes are replaced; this appendix is included BEFORE the candidate's first whole-file pin or dispatch. It completes the comparison in Section5, not a new scientific result or a repair of a reviewed/frozen source.

The budget term in(5.4) is also no stronger than the adopted negative-margin floor. Put `d=min(d_A,d_B)`, `M=max(alpha,beta)` and `c=min(alpha,beta)`. The original positive marginals of trace tau give

    tau>=max(d_A alpha,d_B beta)>=d*M.

Consequently, in the residual positive-minimum case,

    alpha+beta-tau
      <= c-(d-1)M
      <= -(d-2)c
      <= -kappa*c,

because `M>=c>=0` and `kappa<=d-2`. The other two terms of(5.4) were already compared in Section5. Thus the ENTIRE explicitly priced PPT lower bound(5.4), not just its last two terms, is no greater than `-kappa*c`. This completes the claimed failure to raise the already adopted floor. It is an all-variable trace/dimension inequality, without a chosen spectrum, dimension or parameter evaluation.
