# Actual k3 continuation v25 — explicit pair-product margin and a uniform paired-Schmidt neighbourhood

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 07:01:06 PDT 2026**. Owner PhysicsDepol4-2. **NEW AUTHOR-WRITTEN CANDIDATE, NOT adopted/global closure.** Exact source-symbolic written proof including privately; no chosen physical-parameter/noise/control probe, decimal magnitude, scientific interpreter/calculator/eval/CAS/program/enumeration/solver/replay/CLI/nested agent/GO. Same post-v120 actualRETURN→wholeACKWRITTEN/SENT ordering as v24; original primary and ALL held leads remain. No old pinned edit, early park or round closeout.

Named substantive input: the **parent-adopted exact Theorem NP** at `depol-v12-v19-entire-families-and-F3-refutation-parent-v1.md`, SHA256 `05dd4952211ba4b4f223cba81483af65b5cf0716feb4b4ae16a998018424d036`: G>=124/125 implies K3(X3)<=6-(1-G)/40. The complete v15 source was read here, but its frozen decimal illustrations acquire NO proof/guidance credit; the named parent independently supplies the exact written Feshbach interface. No scalar trial from that source was replayed. Everything else needed below is derived directly; in particular the Lipschitz bound is rederived, not opaque reliance on unreviewed v20.

## 1. Exact whole spectrum reduction for an ACTUAL product of TWO physical pairs

Let phi=u_A tensor v_B, where u,v are arbitrary complex two-qubit pure states and A:B is ANY physical2|2 cut. Local U(2) rotations on EACH physical qubit put u and v in their individual TWO-QUBIT Schmidt forms. These are legitimate physical LUs, not the false arbitrary-U(4) covariance of the full pair-cut map. Define

    alpha=4det(Tr_(one qubit)|u><u|),
    beta=4det(Tr_(one qubit)|v><v|), s=alpha+beta,
    0<=alpha,beta<=1.

They are the squared two-qubit concurrences of the ACTUAL dominant pair vectors, not freely selected moment parameters. The local Bloch lengths are t_A=sqrt(1-alpha),t_B=sqrt(1-beta).

For any two-qubit pure u in its physical Schmidt basis, `Y_A=Tr_1(P_u) tensor I_1+Tr_2(P_u) tensor I_2` has diagonal entries2lambda,1,1,2(1-lambda). In the basis(u,u_perp) of span00/11 its compression is

    [[2-alpha,sqrt(alpha(1-alpha))],
     [sqrt(alpha(1-alpha)),alpha]],

up to an immaterial phase/sign in u_perp; the orthogonal01,10 directions have eigenvalue1. Similarly for v. The physical tensor-placement identity is

    X3(P_phi)=Y_A tensor P_v+P_u tensor Y_B.

Thus the complete nonzero spectrum consists of FOUR eigenvalues1 and the THREE eigenvalues of the actual arrow matrix

    C=[[4-s,sqrt(alpha(1-alpha)),sqrt(beta(1-beta))],
       [sqrt(alpha(1-alpha)),alpha,0],
       [sqrt(beta(1-beta)),0,beta]],                      (CORE)

plus NINE zeros (with additional zero/core coincidences allowed). The central basis is(phi,u_perp tensor v,u tensor v_perp). No vanished Schmidt coefficient is divided out; the displayed formula extends to alpha/beta0 or1 directly. TraceCORE=4, giving trace8 with the four unit modes.

Interlacing with the lower diagonal2x2 block gives lambda2(C)<=max(alpha,beta)<=1. Also lambda1(C)>=4-s>=2. Therefore

    K3(X3(phi))=lambda1(C)+2.

This is an exact full-output reduction for the actual pair-PRODUCT family, distinct from the refuted arbitrary pair-cut Schmidt-spectrum claim.

## 2. A direct division-safe strict pair-product margin

Set L=4-s/2, so L>=3>alpha,beta. The Schur condition L I-C>=0 reduces to

    s/2 >= alpha(1-alpha)/(L-alpha)
                          +beta(1-beta)/(L-beta).

Each denominator is>=2, so the right side is at most[alpha(1-alpha)+beta(1-beta)]/2<=s/2. The case s=0 gives the diagonal product matrix directly; no0/0 or positive spectral cutoff is hidden. Hence

    lambda1(C)<=4-s/2,
    K3(X3(phi))<=6-s/2.                                 (PAIR-MARGIN)

This gives an explicit positive margin for EVERY pair-product state that is not a four-qubit product (s>0), with arbitrary complex phases handled by actual physical LUs. It does not claim the numerical coefficient is sharp or optimize a global margin functional.

## 3. A genuinely arbitrary-direction Lipschitz estimate

X3 is completely positive and TrX3(Y)=8TrY, so X3/8 is positive trace-preserving. For Hermitian Delta, its positive/negative decomposition gives `||X3(Delta)||1<=8||Delta||1`. For Delta=rho-sigma with both inputs trace1, X3(Delta) has trace0, hence EVERY projector obeys

    |TrPi X3(Delta)|<=||X3(Delta)||1/2<=4||Delta||1.

The Ky Fan variational formula gives

    |K3(X3(rho))-K3(X3(sigma))|<=4||rho-sigma||1.          (L4)

This is trace-zero norm control, not a differentiability or positive-part Loewner assertion. For pure psi,phi with squared overlap p, the input trace norm is2sqrt(1-p). Thus an arbitrary pure psi with pair-cut largest squared Schmidt coefficient p and its corresponding actual pair-product phi satisfies

    K3(X3(psi))<=6-s/2+8sqrt(1-p).                       (PTUBE)

Here s belongs to the actual dominant pair vectors u,v; it is not inferred from the eigenvalues of an unrelated marginal. In particular `1-p<=s^2/256` suffices for original all-p k3 via the established SAME-projector coefficient interface. A positive excess kappa instead requires `kappa<=8sqrt(1-p)-s/2`.

## 4. Explicit UNIFORM neighbourhood of the ENTIRE pair-product set

The previous inequality loses margin near actual four-qubit products (s=0). NP supplies that boundary without a false first-order argument. Put the EXACT positive constant

    y_*=sqrt(2+1/sqrt125)-sqrt2,
    w_*=y_*^4.                                         (RADIUS)

It is the derived positive solution of `y_*^2+2sqrt2 y_*=1/sqrt125`; no selected parameter instance, magnitude trial or numerical evaluation defines it. It is strictly positive, and y_*^2<1/sqrt125<1 gives w_*<1.

**Theorem PP-TUBE.** EVERY pure four-qubit state psi whose largest pair-cut Schmidt probability p satisfies `1-p<=w_*` on ANY physical2|2 cut has K3(X3)<=6, hence ORIGINAL k3 at every physical noise/projector.

Proof. Let w=1-p and choose the actual Schmidt pair-product phi with |<psi|phi>|^2=p. If `s>=16sqrt w`, PTUBE directly gives K3<=6. This includes w=0, all pair-product states and all s endpoints.

Otherwise `s<16sqrt w`. Each pair's maximal physical qubit-PRODUCT overlap is

    g_A=(1+sqrt(1-alpha))/2>=1-alpha/2,
    g_B=(1+sqrt(1-beta))/2>=1-beta/2.

Their product g satisfies `g>=1-s/2`; if this lower bound is negative the ensuing inequality `1-g<=s/2` is still true. Choose the corresponding ACTUAL four-qubit product pi. Pure-state trace-distance triangle gives

    sqrt(1-|<psi|pi>|^2)
       <=sqrt w+sqrt(1-g)
       <=sqrt w+sqrt(s/2)
       <sqrt w+2sqrt2 w^(1/4).

For w<=w_*, monotonicity of y^2+2sqrt2 y at y=w^(1/4)>=0 makes the last expression<=1/sqrt125. Hence the ACTUAL maximal qubit-product overlap G(psi)>=124/125. The named parent NP theorem yields K3<=6. No independent choice of pair/concurrence/Bloch data, no parameter testing and no assumption that every near-pair-product state remains parity symmetric is used.

The radius is only a derived sufficient bound, not claimed sharp. The theorem is a GENUINE neighbourhood of the FULL compact pair-product family INCLUDING its product corners, with arbitrary complex perturbations. It bypasses the unsupported cutoff-degenerate first-order PAR aside by using exact finite spectrum/margins plus NP.

## 5. Combined exact structural residual, not a new scientific cutoff

Together with independent v24's PAIR bound, EVERY possible pure coefficient-U3 violator must have, on EACH of the THREE physical2|2 cuts,

    1/2 < lambda_max(rho_ij) < 1-w_*.

The lower bound is quantitative `>=1/2+kappa/4`; the upper exclusion is the proved PP-TUBE, not an imposed numerical cutoff or a narrowed assignment. Dominant pair entanglements additionally obey PTUBE's necessary margin inequality at each actual cut. These state/projector restrictions must still be coupled to the exact original channel quartic/critical system; they are not a proof that the middle region is empty or an eligible original failure. No full-B CLIP-prime or all-state theorem is inferred.

Original all-p extension uses the SAME fixed-projector rho/X3/X2/X1 bounds1/6/12/10, polynomial expansion and full spin flip at the named current parent interface, exactly as in v24. Fixed-Pi affine averaging gives the actual convex hull/LU/permutation images; a mixed state's own pair marginal eigenvalue condition is not asserted to guarantee that decomposition. No all-index certificate replay, numerical value, uniqueness or novelty gate follows.

All oldv8/v10-v19/v20-v24/park/heldleads remain at their qualified scopes; F3falsefinal/cp062 and ENTIREv22 remain WITHDRAWN, parentv35 and all SEC/W2/optimizer/firstorder/ROW limitations mandatory. Every earlier own/parent/peer cadence/exactness/privateapproxZERO/pause/inventory/orientation/readorder/freeze/clock/admission finding remains. Source-correct symbolic work does not cure history. Same18/HOLD/OWNroot/October27 cutoff11:05:38/deadline12:35:38 PDT; no scientificGO, frozen edit, newslot/model, early park or round closeout.
