# physics-2 — complete mixed-state two-erasure equality rigidity and quantitative SAME-projector gap

Actual returned `/bin/date` before this NEW additive write: **Tue Oct 27 15:22:50 PDT 2026**. Owner PhysicsDepol4-2, SAME S1 release/current new root. NEW **WRITTEN ordinary-input candidate**, not peer-reviewed/adopted/formal/kernel/executable/novelty-cleared. v1/v2/v3 are immutable. No scientific calculation program, selected state/noise/control/boundary/decimal probe or new source read.

This continues the universal operator route established in v3, not the trace-only route already shown insufficient in v2. The new results are (i) COMPLETE equality characterization for the two-erasure Ky-Fan3 cap for EVERY mixed or pure input, not merely joint equality with a different bound, and (ii) a quantitative actual-rho/P inequality connecting the exact two-erasure slack, input overlap and input marginal-purity gap. Neither is an original-channel result or a uniform positive GME margin.

## 1. Exact inputs and already derived positive interface

The PRIMARY-confirmed convention is `D_p(X)=(1-p)X+(p/2)Tr(X)I`, physical0<=p<=4/3, with arbitrary four-qubit output majorized BY product-reference output; only [arXiv:2609.37240v1](https://arxiv.org/html/2609.37240v1) abstract/Introduction Eqs.(1)–(2) were read, not its proofs. Current S1/definition packet/S0/contract/own SAFE intake and ordinary explicitly named finite-dimensional facts are the only inputs. Prior exposure is NOT denied or called independently unaffected cognition.

Let rho be ANY four-qubit density, P ANY actual complex rank3 orthogonal projector, `r=Tr(P rho)`. Define

`E_S(A)=I_S/2^|S| tensor Tr_S(A)`,
`F2(A)=sum_(|S|=2) E_S(A)`.

The exact current-run v3 interface, SHA256 `81fd1d7a0b6a31fd0ecda36d8d61acf84de95a3dfa44385fd076fe4c06e20471`, was PROVED from elementary swap algebra, not imported from an old proof. For completeness its full load-bearing identity is restated with its proof: if S_i are the four commuting local copy swaps and Q2 projects onto EXACTLY TWO negative local swap signs, then

`3(I+product_i S_i)-sum_(i<j)S_iS_j=8Q2>=0`.         (R1)

On m negative signs the pair sum is[((4-2m)^2-4)/2]; m0/4 gives6 with even global sign, m1/3 gives0 with odd global sign, and m2 gives-2 with even global sign. Thus the difference is8 exactly on m2 and0 on all other sectors. Swap trace identities on arbitrary rho tensor sigma give the two-party marginal overlaps and global Tr(rho sigma). Testing all unit-vector sigma yields

`K_rho := (3/4)(I+rho)-F2(rho) >=0`,                 (R2)
`delta :=Tr(P K_rho)=9/4+3r/4-Tr(P F2(rho))`
`       =2 ||Q2(rho^(1/2) tensor P)||_HS²>=0`.        (R3)

All mixed/complex/degenerate cases and normalization factors are included. In particular Tr(P F2(rho))<=3, since r<=1. Ordinary facts newly used below are positivity of trace products, support projections and spectral minimum on a finite support, Schmidt factorization of pure marginals, linear tensor-product subspaces, Hilbert–Schmidt triangle/Cauchy–Schwarz, and the finite Ky-Fan variational principle. No old candidate, protected guide, paper proof or selected tuple is used.

## 2. The COMPLETE equality theorem, including arbitrary mixed input

**Theorem7.** The following are equivalent:

1. `Tr[P F2(rho)]=3` for the actual rho and rank3 P.
2. rho is a pure PRODUCT four-qubit density with product vector Omega, and

`Range(P)=span{Omega} direct-sum W`,

where W is ANY complex two-dimensional subspace of the four-dimensional one-site-orthogonal-excitation space relative to Omega.

Consequently `K3(F2(rho))=3` IFF rho is pure product; for EVERY other density the Ky-Fan sum is STRICTLY less than3. This is an exact equality/strictness theorem, NOT an evaluated uniform separation or an original noisy-channel regional theorem.

### 2.1 Support and equality propagate to EVERY pure vector in the support

If f2=3, (R3) and r<=1 force r1 and delta0. Positivity gives support(rho)<=Range(P). Also Tr(P K_rho)=0 implies `K_rho^(1/2)P=0` and hence K_rho P=0.

If rho has rank at least2, let alpha be its smallest positive eigenvalue on its support;0<alpha<1. For ANY unit u in that support, rho>=alpha|u><u|. Thus

`rho=alpha|u><u|+(1-alpha)sigma_u`

with sigma_u an actual density. This is a universally quantified decomposition, not a selected input evaluation. Linearity and the universal cap3 on each component force `Tr[P F2(|u><u|)]=3` for EVERY such u. For rank1 the same assertion is immediate for its one support line. Zero eigenvalues outside the support cause no inverse or undefined division.

### 2.2 Every such u must be fully product

Since u belongs to Range(P), Pu=u. The positive operator `K_u=(3/4)(I+|u><u|)-F2(|u><u|)` has zero trace against P, so it annihilates u. Evaluating its expectation on u gives

`0=3/2-(1/4)sum_(i<j)Tr[(rho_u)_(ij)^2]`,

where rho_u=|u><u|. Every pair marginal is a density of purity at most1. All SIX purities therefore equal1. In particular purity of the12 marginal factors u across12|34 as v12 tensor w34. Purity of its13 marginal then makes both one-party marginals of v12 and w34 pure, because the13 marginal is their tensor product and each purity is at most1. Schmidt decomposition factors both v12 and w34. Thus u is fully product. The argument covers EVERY complex u in the support, not a special representative or basis.

### 2.3 A mixed support would require a rank3 space inside an actual dimension2 intersection

Suppose support(rho) has dimension at least2. Choose two orthonormal support vectors u0,u1; both are product, and EVERY nonzero linear combination is also product by §2.2. Two nonparallel product vectors can have a product sum only if their local factors differ at at most ONE site: if two local factors differ, separating one of them from the rest gives two independent local factors and two independent residual factors, so the sum has Schmidt rank2. Therefore u0,u1 differ on one site j and share the other three factors. Orthogonality makes their two local j factors orthogonal.

For any arbitrary product vector u, F2(|u><u|) is diagonal in its local product/orthogonal basis. A basis vector with excitation set T appears in an erased pair S exactly when T<=S, and then with coefficient1/4. Thus its eigenvalue is `C(4-|T|,2-|T|)/4` for |T|<=2, and0 otherwise:6/4 on u,3/4 on the four one-excitation directions,1/4 on the six two-excitation directions,0 on the remaining directions. This is the complete combinatorial proof for the ENTIRE product class, not a scientific enumeration or evaluation of a chosen state.

By Ky-Fan equality at f2=3, P must contain u and be contained in `T_u=span{u}+V1(u)`, with the other two dimensions in V1(u). There is a strict spectral gap below the one-excitation level, while its fourfold internal degeneracy is fully retained.

Apply this to BOTH forced support vectors u0,u1. In the common local product basis, T_(u0) has the zero-excitation vector and all single excitations. T_(u1), whose reference differs by the j flip, has that j vector, the zero vector, and the double excitations involving j. Their intersection is EXACTLY span{u0,u1}, dimension2. Yet Range(P) would have dimension3 and lie in both. Contradiction. Thus rho cannot be mixed: it has rank1 and is product.

This is an all-support dimensional argument; no particular site, product factor, rank3 test or noise value was chosen for a viability check. Choosing an orthonormal pair EXISTING under the contradicted rank hypothesis is a universal proof step, not a selected numerical/control input.

### 2.4 Sufficiency and all threshold degeneracies

For ANY product rho=|Omega><Omega| and ANY complex rank2 W<=V1(Omega), P onto Omega plus W is a GENUINE complex rank3 orthogonal projector. The diagonal eigenvalues just derived give `Tr(P F2(rho))=6/4+2*(3/4)=3`. Conversely those are all maximizing rank3 projections because the highest eigenvalue6/4 is simple and the next four are3/4, separated from the lower1/4 level. Arbitrary complex mixing INSIDE the next-four eigenspace is permitted, not replaced by two chosen basis states.

The Ky-Fan maximum is attained on the compact finite-dimensional projector set (or directly by the spectral theorem). The pairwise equality characterization therefore proves the final density-only equality/strictness assertion. There is no claim that a sequence of GME states has a uniform evaluated gap from3, or that strictness in this auxiliary coefficient already proves the full original channel inequality.

## 3. Quantitative SAME-rho/P slack, valid for ALL densities and off-containment

The exact remainder(R3) supplies more than an equality label. Define the actual input functional

`kappa(rho)=Tr(rho K_rho)`
` =(3/4)(1+Tr(rho²))-(1/4)sum_(i<j)Tr(rho_(ij)^2)>=0`, (R4)

and let `M(rho)=(3/4)(1+||rho||op)`. Since F2(rho)>=0,

`0<=K_rho<=(3/4)(I+rho)<=M(rho)I`.                  (R5)

**Theorem8.** For EVERY actual rho,P above,

`[ sqrt(kappa(rho))-sqrt(M(rho)(1-r)) ]_+² <= r delta`, (R6)

where delta is the exact SAME-pair quantity(R3), and x_+=max(x,0). No free scalar tuple is asserted physical. This inequality remains meaningful at r0/r1 and at kappa0; no division by r or other vanishing quantity occurs.

**Full proof.** Put Q=I-P. The Hilbert–Schmidt triangle inequality gives

`sqrt(kappa)=||K_rho^(1/2)rho^(1/2)||_HS`
` <=||K_rho^(1/2)P rho^(1/2)||_HS`
`   +||K_rho^(1/2)Q rho^(1/2)||_HS`.

P rho P is positive, supported on P and has trace r, hence `P rho P<=r P`. Therefore the FIRST squared norm is

`Tr(K_rho P rho P)<=r Tr(K_rho P)=r delta`.

By(R5), the SECOND squared norm is at most `M(rho)Tr(Q rho Q)=M(rho)(1-r)`. Subtract this nonnegative root, take its positive part and square to prove(R6). All order comparisons are between ACTUAL positive operators constructed from the SAME rho and P. Noncommutativity does not invalidate the trace inequalities: if0<=A<=B and K>=0, then Tr(KA)<=Tr(KB).

For pure rho, the input functional becomes the complete pair-marginal linear-entropy sum

`kappa(rho)=(1/4)sum_(i<j)[1-Tr(rho_(ij)^2)]`.

For r1, (R6) gives delta>=kappa. For general rho, the displayed mixed formula(R4), not that pure-state specialization, must be used. No quantitative product-neighbourhood theorem, chosen Schmidt restriction, parameter limit, numerical margin or old product-tube guidance is invoked.

## 4. Original-object application and precise missing implication

The original four-qubit channel, all physical p, and its SAME rank3 testing projector remain as in v3's exact erasure expansion. The new theorems mean that the two-erasure coefficient is controlled by the ACTUAL input overlap and a positive SAME-pair remainder, with COMPLETE actual equality rigidity and an additional input-marginal constraint. No independently chosen copies or scalar extrema are treated as realizable original data.

Forward: EVERY original rho,P,p supplies(R2)–(R6), including off-containment, mixed input and all complex phases. Converse: the product/W equality form produces GENUINE rank3 projectors and densities for ALL its symbolic arguments; no arbitrary feasible values of r,delta,kappa are asserted realizable. A strict original trace violation for a genuine rho,P,p would imply Ky-Fan3 violation, and any original k3 violation gives such a maximizing P by the finite variational principle; nothing here constructs one.

The exact still-unpaid step is the one-erasure/state-conditioned interaction in the full original comparison, including its coupling to these nonnegative slacks. Neither f2<3 for every nonproduct density nor the quantitative(R6) controls the sign or size of the missing one-erasure term. Strictness without a sufficiently strong joint bound does not settle GME global k3. The product-reference bound, all-index majorization, a physical witness and every p>1 sign/composition boundary remain unproved by this packet. No original regional increment or new registered success is reported.

## 5. Outside-input request and continued scope

At the actual15:22:50 observation, a narrow new-input request was sent to Main: the envelope cites adopted GLOBALCLIP but does not supply its operative definition/inequality or exact mapping to the current erasure interface. To use that adoption without guessing, request a NEW screened literal GLOBALCLIP statement/carrier/normalization/named TC–scalar–Pauli/NR application cut. This is a request for input OUTSIDE the present packet under Main's standing direction(a), not a per-step permission loop. NO old parent/proof/status/checkpoint/search was opened to obtain it and it is NOT assumed as a premise of this derivation. The current proof continues entirely from the new positive two-erasure identity and elementary finite-dimensional facts.

All old actual-common-projector/odd-part/output-purity/route/method-selection ZERO consumers remain NONINPUT. No special tested state, private confidence guide, old review verdict or scientific code is used. Prior exposure survives; the displayed correctness-input cut is not a clean-cognition or provenance-unaffected certificate. New candidate sources must be read fully and actually reviewed at complete scope before Main adoption.

Next substantive work stays inside the current S1 actual-object scope while that source request is pending; any unprovided GLOBALCLIP identification is NAMED_NOT_RECONSTRUCTED, not inferred from its title. Same18/OWN append-only/old roots read-only/HOLDv2/N4UNKNOWN historical exit unestablished/aux214STOP/all permanent findings and ENTIREZERO histories. No scientific interpreter/calculator/CAS/program/enumeration/solver/replay/build/test/typechecker, chosen numeric/control/state/noise/boundary/decimal probe, nested agent/modelCLI/paidAPI/newGO, Git/delete/contact/publication/infrastructure or stronger formal/kernel/human/family/executable/novelty claim. Deadline2026-10-31T21:23:27.000Z; continued real results/obstructions, not timer/heartbeat/fake progress.
