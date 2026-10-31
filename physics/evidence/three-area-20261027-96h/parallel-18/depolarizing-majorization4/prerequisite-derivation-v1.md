# physics-2 — universal conditional-variance coupling and joint rank-three marginal rigidity

Owner **PhysicsDepol4-2**. Actual returned `/bin/date` immediately before this write: **Tue Oct 27 14:57:14 PDT 2026**.

**NEW WRITTEN candidate under the narrow S1 definition-first release**, not a parent adoption, formal/kernel check, executable certificate, independent-family review or novelty claim. The original all-index majorization problem remains OPEN. No original physical violation is asserted. No scientific interpreter/calculator/Eval arithmetic/CAS/program/enumeration/solver/replay/build/test, selected state/noise/boundary/decimal probe, nested agent or modelCLI was used.

The non-encoding mathematical content is: an exact positive sum-of-squares coupling for the SAME projector throughout the physical channel; a sharp universal one-qubit marginal-purity gap for every complex rank-three projector, including its COMPLETE equality classification; and a joint compatibility theorem showing that THREE such local equalities cannot occur and classifying ALL two-equality cases. The latter yields a stronger joint constraint than treating the four local minima as independent. These are ordinary-input candidate lemmas, NOT a new claim of original-channel closure or priority. The precise still-unpaid state-conditioned inequality is stated in §7.

## 1. Required PRIMARY convention confirmation, before derivation

Admitted primary: Zhiwei Song, Xin Wang, Marco Tomamichel, Kun Fang, *Approximate majorization and high-order capacity of quantum depolarizing channels*, [arXiv:2609.37240v1 abstract](https://arxiv.org/abs/2609.37240v1), [HTML Introduction, Eqs.(1)–(2)](https://arxiv.org/html/2609.37240v1).

Actual admitted reads: abstract via the abs page; rendered HTML prefix through the Eq.(1) definition and the Eq.(2) convention section, returned by native text ranges1–45 and49–64 with the reader's surrounding-line additions. These displayed the definition and Eq.(2), not any proof. Earlier raw HTML1–60/61–145 and49–68 displayed header/UI boilerplate only; raw and rendered line numberings differ. An exact-ID grep returned no matches, not proof coverage. No proof section, full paper, PDF or source archive was opened. The introductory abstract/adjacent contextual prose is not a correctness input for the lemmas below. No full-publication/algorithm/book-equivalence or reader-hash-to-original-PDF certificate is claimed.

PRIMARY Eq.(1) states:

> `D_(p,d)(X) := (1-p)X + (p/d) Tr(X) I_d`, with `0<=p<=d^2/(d^2-1)` and `d>=2`.

PRIMARY Eq.(2) states:

> `lambda^downarrow(D_(p,d)^tensor n(rho^n)) prec lambda^downarrow(D_(p,d)^tensor n(|0^n><0^n|))`.

Its text says that the output of a pure product input **majorizes** the output of an arbitrary, possibly entangled input; eigenvalues are nonincreasing, and `x prec y` means x is majorized by y. Specializing d2/n4 gives precisely `D_p(X)=(1-p)X+(p/2)Tr(X)I_2`, physical `0<=p<=4/3`, and the SAME direction as S2. **No transcription discrepancy was found.** This convention decision and exact quotes were sent to Main at the actual14:49:22 metadata observation BEFORE deriving these lemmas. Main's transcription is not independently called a verbatim-book certification.

Original target retained: EVERY mixed or pure four-qubit density rho, EVERY physical p, EVERY nontrivial Ky-Fan index1–15; or an ACTUAL physical strict violation. The priority is original global k3, including genuinely multipartite-entangled inputs, with the SAME actual complex rank-three projector, input and channel. No epsilon cutoff, chosen state, independent-copy relaxation, regional substitute or numerical margin is introduced.

## 2. Actual inputs, carrier and ordinary facts

The actual pre-body ACK `prerequisite-prebody-exposure-ack-v1.json` was written at14:47:18 BEFORE the supplied definitions/packet or any derivation;18LF5495B, SHA256 `41bc8bb64edcf3c6c88e094847e56ca02ab4781c905159f15076b7b9545a8574`.

Complete controls19LF FIRST, complete release JSON, then that ACK, complete35LF packet and complete equality receipt were read in that order. Packet SHA256 `6d06f83f90a26848071ddd95a5ba509f3517d21c89e55a2ce64375a5765c20ec`; receipt `657f26e32db9eba439cfe9798e2a9f3c9f90552f5cc3e273fcd9139ff0262fb9`. Controls pin `efa80f475013904c44b84b60beff5db3dfd0596696c3d22255f1d41516d6ccf3`; release pin `bab72fbd84dbef5659032049e5db858d97ac9579f3792d98869fb614ee567b40`. Current S0/contract/own safe intake and envelope-adopted statements may be used only at their exact cuts. NONE of the old proposed source bodies, candidates, reviews, parks, checkpoints, metadata-map expansions, held/withdrawn content or private method/selection/confidence guides is a correctness premise here.

All proofs below use only the confirmed channel definition and ordinary finite-dimensional facts: partial trace, orthogonal projections, Hermitian spectral theorem, trace cyclicity, conditional expectation bimodule/self-adjointness, the elementary Pauli basis multiplication, positive-functional Cauchy–Schwarz, tensor-product subspaces, and the Ky-Fan variational principle (whose relevant finite-dimensional argument is given below). No special research lemma, old TC-operator theorem, old common-projector energy/covariance route, tested state or source-paper proof is imported.

Let H=(C2)^tensor4. For each site i define the normalized conditional expectation

`E_i(A)=(I_i/2) tensor Tr_i(A)`,

with the remaining tensor factors in their original order. It is trace preserving, unital, positive, Hilbert–Schmidt self-adjoint and idempotent. If B belongs to its range, `E_i(BA)=B E_i(A)` and `E_i(AB)=E_i(A) B`. These follow directly from partial trace on simple tensors and linearity. In particular its range and kernel are Hilbert–Schmidt orthogonal.

Put `Phi_i=(1-p)Id+p E_i`. The four-qubit channel is `Lambda_p=Phi_4 Phi_3 Phi_2 Phi_1`; the local maps commute, so any site ordering is available. Throughout p is an ARBITRARY symbol in the ENTIRE physical interval, not a parameter selected for a check.

For completeness, on a qubit the Pauli identity is `sum_a sigma_a X sigma_a=2 Tr(X)I-X`, obtained by expanding X in I,sigma_x,sigma_y,sigma_z. Hence

`D_p(X)=(1-3p/4)X+(p/4)sum_a sigma_a X sigma_a`.

All four weights are nonnegative exactly on the confirmed physical interval. Thus every Phi_i is completely positive, unital, trace preserving and self-adjoint; no scientific Kraus enumeration is used. Endpoint zero weights cause no division or omitted case below.

## 3. Universal single-site sum-of-squares coupling — ANY Hermitian input

**Lemma1.** For ANY Hermitian A on H, set B=E_i(A) and C=A-B. Expand the traceless-on-i Hermitian part as

`C=sum_(a=x,y,z) X_a`, with `X_a=sigma_a^(i) tensor C_a`,

where each C_a is Hermitian on the other three sites. Define

`S_i(A)=sum_(a<b)(X_a-X_b)^2`.

Then for EVERY physical p,

`Delta_i(A):=Phi_i(A^2)-Phi_i(A)^2`
` = p E_i(C^2)+p(1-p) C^2`
` = p(4/3-p) C^2+(p/3)S_i(A) >=0`.                 (V1)

**Complete proof.** E_i(C)=0 and the bimodule rule give E_i(A²)=B²+E_i(C²), while Phi_i(A)=B+(1-p)C. Expand both squares; the B² and B–C cross terms cancel, leaving the first displayed identity. Pauli trace orthogonality gives

`E_i(C^2)=I_i tensor sum_a C_a^2=sum_a X_a^2`.

For arbitrary Hermitian X_a, expansion of the THREE pair-difference squares gives

`S_i(A)=3 sum_a X_a^2-(sum_a X_a)^2=3 E_i(C^2)-C^2`.

Substitution proves the second identity. Both coefficients p(4/3-p) and p/3 are nonnegative on the ENTIRE physical interval. Each square is positive; this proves positivity without dropping the p>1 range or assuming A commutes with its conditional expectation. The Pauli basis is fixed operator algebra, not a state-dependent axis or selected state. All complex entries and all repeated/zero eigenvalues are covered.

Tracing (V1) also gives the exact identity

`Tr Delta_i(A)=p(2-p) Tr C^2`.                        (V2)

Indeed trace preservation gives Tr E_i(C²)=Tr C². This is an all-variable equality, not a noise-boundary evaluation. For an arbitrary density tau, positive-functional Cauchy–Schwarz gives

`Tr[tau Delta_i(A)] >= p(4/3-p) (Tr[tau(A-E_iA)])^2`. (V3)

No state-independent strictly positive right side is asserted. At p0 all terms vanish. At p4/3 the first square coefficient vanishes but the remaining sum is retained; no equality classification is incorrectly transferred across that endpoint.

**Scope/verdict.** NEW WRITTEN universal operator identity and state-conditioned coupling at the named ordinary facts. It is a fresh explicit correctness-input candidate, not a claim that the classical conditional-variance principle or Pauli algebra is novel. It imposes a relation among operators generated from the SAME A; their entries are not free variables.

## 4. Full four-channel telescoping — SAME original projector and input

Let P be ANY complex rank-three orthogonal projector, rho ANY four-qubit density. No containment or relation between rho and P is assumed. Put A0=P and A_j=Phi_j(A_(j-1)) for j1–4, and write `Psi_(>j)=Phi_4 ... Phi_(j+1)` (identity at j4). The telescoping identity is

`Lambda_p(P)-Lambda_p(P)^2`
` =sum_(j=1)^4 Psi_(>j)(Delta_j(A_(j-1)))`.           (V4)

**Proof.** Add and subtract Psi_(>j)(A_j²) successively in `Lambda_p(P²)-A4²`. Consecutive terms cancel exactly; P²=P gives (V4). Each remainder is positive by (V1) and complete positivity of the remaining maps. Later A_j need NOT be projections and need NOT have rank3. Applying a rank3 projection-only inequality to all later stages would be invalid.

For every j let `rho_j=Psi_(>j)^*(rho)=Psi_(>j)(rho)`, an ACTUAL density, and let C_j=A_(j-1)-E_j(A_(j-1)). With `G=Tr[rho Lambda_p(P)]`, take the SAME input rho against (V4). This gives

`Tr[rho(Lambda_p(P)-Lambda_p(P)^2)]`
` >=p(4/3-p) sum_j (Tr[rho_j C_j])^2`.               (V5)

Moreover, with `Var_rho(A4)=Tr(rho A4²)-G²>=0`,

`G(1-G)=Var_rho(A4)+sum_j Tr[rho_j Delta_j(A_(j-1))]` (V6)

and hence the sum of Var_rho(A4) and the right side of (V5) is at most G(1-G). For each j the overlaps are coupled by

`G=Tr(rho_j A_j)`
` =(1-p)Tr(rho_j A_(j-1))+p Tr(rho_j E_j A_(j-1))`.  (V7)

These rho_j and A_j are generated by the SAME original rho,P and parameter p; no independently chosen copies or scalar overlap assignments are supplied. All p endpoints and mixed rho are included. This is more than a coordinate encoding: it supplies explicit nonnegative square remainders and quadratic restrictions on every such actual pair. It is nevertheless NOT sufficient by itself for the original product-reference ceiling.

## 5. Sharp universal rank-three marginal gap — COMPLETE equality set

For ANY site i and ANY rank3 P, write `E_i(P)=I_i tensor T`, where `T=(Tr_i P)/2`. Positivity and P<=I give0<=T<=I; Tr T=3/2. Thus the eigenvalues t_l of T belong to[0,1] and sum to3/2.

**Lemma2.** For EVERY such P,

`Tr(E_i(P)^2)<=5/2`,
`L_i(P):=Tr(P-E_iP)^2=3-Tr(E_iP)^2>=1/2`.           (M1)

Equality holds IFF there are arbitrary unit u in C2 and arbitrary orthonormal v,w in the other-site C8 such that

`P=I_i tensor |v><v|+|u><u|_i tensor |w><w|`.         (M2)

No member of this entire equality class, no site-specific state and no noise value is chosen or evaluated as a viability test.

**Proof of the bound and all spectral equalities.** To maximize sum_l t_l² with t_l in[0,1] and sum3/2, two strictly fractional coordinates cannot remain at a maximum. If a>=b are both fractional, transfer a positive amount h=min(1-a,b) from b to a; the increase is2h(a-b)+2h²>0. Thus at most one fractional coordinate remains. The trace forces precisely the spectrum1,1/2,0,...,0. Conversely that spectrum attains sum t_l²=5/4. Since the identity factor has trace2, Tr(E_iP)²<=5/2. Hilbert–Schmidt orthogonality of E_i gives the second equality and bound in(M1). This is the complete forced extremal proof, not a tested tuple or numerical optimization.

**Necessity of(M2), with no arbitrary marginal realization.** In the equality case, let v,w be unit eigenvectors of T for1,1/2. For z perpendicular to their span, the sum over a qubit basis of <a,z|P|a,z> is0. Each term is nonnegative, so P annihilates C2 tensor z. On C2 tensor v, the two expectations sum to2 and each is at most1; P is identity on that whole2-dimensional subspace. Self-adjointness removes cross terms from it. The remaining projector has rank1 and is supported on C2 tensor w, so it is exactly |u><u| tensor |w><w| for a unit u. This proves(M2), not only the eigenvalue necessary condition.

**Sufficiency of(M2).** Orthogonality of v,w makes the two displayed summands mutually orthogonal projections of ranks2 and1. Thus their sum is a GENUINE complex rank3 projector. Its partial trace gives T=|v><v|+(1/2)|w><w|, so equality holds. v,w may be arbitrarily entangled among the remaining three physical sites; no real-amplitude or globally product-code assumption is made.

For a single local physical channel, (V2) and P²=P give

`Tr[Phi_i(P)-Phi_i(P)^2]=p(2-p)L_i(P)>=p(2-p)/2`.   (M3)

For p>0 throughout the physical interval, p(2-p)>0 and equality is EXACTLY(M2). For p0, both sides are0 for EVERY P, so the noisy equality statement does not force(M2). The bound(M1) itself remains unchanged. Formula(M3) is sharp for the whole universally classified set; no state or p is selected for checking it.

From (V4), trace preservation and positivity, the full-channel trace variance is at least any FIRST-stage value(M3); arbitrary order puts any chosen site first. No sum of four independent first-stage bounds is claimed: the later A_j are not projections. This global trace lower bound is not claimed sharp or sufficient for majorization.

## 6. A joint compatibility theorem, not four independent local minima

**Lemma3.** For EVERY complex rank3 projector P on four qubits:

1. At most TWO sites can satisfy L_i(P)=1/2.
2. For two distinct sites i,j, BOTH equalities hold IFF there are unit vectors a in C2_i, b in C2_j and c in the remaining two-qubit space such that

`Range(P)=(C2_i tensor b + a tensor C2_j) tensor c`, (J1)

or equivalently, writing unit perpendicular vectors a_perp,b_perp,

`P=[I_(ij)-|a_perp,b_perp><a_perp,b_perp|] tensor |c><c|`. (J2)

3. If those two equalities hold, then for EACH remaining site k one has L_k(P)>=3/2. Consequently `sum_(k=1)^4 L_k(P)>=4` in this ENTIRE two-equality class. Equality in that sum holds exactly when c is product across the remaining two sites. **No assertion of that sum bound for ALL rank3 P is made here.**

**Complete proof.** If site i saturates(M1), (M2) supplies a2-dimensional subspace `U_i=C2_i tensor v_i` inside the3-dimensional Range(P). If site j also saturates, its analogous U_j has dimension2, so their intersection is nonzero. Any vector in U_i is a product across i versus the rest; any vector in U_j is a product across j versus the rest. A nonzero common vector is therefore `a tensor b tensor c`: factoring the fixed pure i and j factors leaves one common residual c. Hence

`U_i=C2_i tensor b tensor c`,
`U_j=a tensor C2_j tensor c`.

Their intersection is precisely the common line, so their sum has dimension3 and equals Range(P). This proves(J1) and(J2). Conversely the right side of(J2) is a genuine rank3 projection; taking either of its i or j partial traces gives exactly the spectrum required in(M1), so both equalities hold. This is a full actual-subspace converse, not an independent choice of marginal eigenvalues.

Let Q be the rank3 bracket in(J2). For a remaining site k, let l be the other remaining site and rho_l=Tr_k |c><c|. Direct conditional expectation gives

`E_k(P)=Q tensor [(I_k/2) tensor rho_l]`,
`Tr(E_k(P)^2)=(3/2)Tr(rho_l^2)<=3/2`.

Thus L_k(P)=3-(3/2)Tr(rho_l²)>=3/2, strictly larger than1/2. No third site can saturate. The same holds for l, and the two original sites contribute1/2 each, giving the stated sum bound4. A pure two-party vector has pure one-party marginal IFF it factors (ordinary Schmidt decomposition); this supplies the complete equality condition for the sum. Every a,b,c is arbitrary complex data throughout, not a selected control. The theorem exhausts ALL two-local-equality possibilities and ALL attempted three-local-equality cases.

**Interpretation.** A relaxation assigning all four L_i their separate minimum1/2 cannot correspond to any actual common rank3 projector. This is a genuine universal actual-object coupling obstruction, not a nonphysical block presented as an original counterexample. It does not imply a quantitative global sum bound merely from absence of three equalities; a separate argument would be needed for every nonsaturating projector. Compactness or a headline equality classification is not such an argument.

## 7. Exact original-object caller, failed implication and remaining gap

For an arbitrary Hermitian output Y, the maximum of Tr(PY) over complex rank3 projections is its three-largest-eigenvalue sum: diagonalize Y; each diagonal occupation of P lies in[0,1], sums to3, and placing weight on the largest eigenvalues gives the maximum, attained by their eigenspace projector. Boundary degeneracy allows any appropriate3-dimensional selection and changes neither value nor argument.

Self-adjointness of the confirmed channel gives `Tr(P Lambda_p(rho))=Tr(rho Lambda_p(P))=G`. Therefore:

- EVERY actual original rho,p,rank3 P supplies all identities/inequalities(V1)–(V7), (M1) and the joint compatibility theorem when its equality hypotheses hold.
- If ANY such actual pair has G greater than the ORIGINAL product-reference top3 sum, its trace is a lower bound for the output Ky-Fan3 sum, hence it is a strict physical violation. Conversely any original k3 violation supplies an actual maximizing rank3 projector and such a pair. For mixed input a strict trace violation also has a pure component with the SAME P,p that violates, by linearity; this is not a claim that arbitrary convex-hull extensions may change projector or parameter.
- The actual-subspace converses(M2)/(J2) produce genuine rank3 projectors for ALL their symbolic arguments. They do NOT assert that an arbitrary collection of scalar marginal numbers satisfying the displayed bounds is realizable, or that any of these projectors/input pairs violates original majorization.

**Exact failed implication, paid with actual objects.** The positive TRACE gap(M3) cannot be upgraded to a strictly positive lower bound on `Tr[rho(Phi_i(P)-Phi_i(P)^2)]` uniform over EVERY rho,P. In the COMPLETE equality set(M2), Phi_i(P) is identity on `C2_i tensor v` for EVERY physical p, so its variance operator is ZERO on that whole subspace. ANY density supported there has zero expectation, even though its total trace variance is p(2-p)/2 for p>0. No particular u,v,w,rho or p has been instantiated, no margin evaluated, and no original-channel comparison performed. This proves failure of that uniform TRACE-to-SAME-STATE implication on actual legitimate objects, not on an enlarged nonphysical copy space. Later noisy channels can change the variance; no partial-channel zero is transferred to the full original output.

(V5)–(V7) supply a valid state-conditioned replacement but do NOT provide the necessary product-reference ceiling on G. The exact unpaid next step is a sufficiently strong all-variable estimate on these SAME linked rho_j,A_j,C_j (or another independently admitted actual-object bound), with EVERY GME/boundary/p case, to establish the original top3 ceiling or yield a strict physical alternative. Neither total variance, the sharp one-site purity gap, nor the joint equality classification supplies that estimate. The global conjecture `sum_i L_i(P)>=4` for all P is also NOT established merely by the two-equality theorem and is not adopted as an input. No further original index is reported closed.

## 8. What changes, process ceiling and continuation

This packet supplies explicit newly written ordinary-input coupling candidates and an actual-object failure of a particular inference, not a coordinate encoding alone. No original global k3, all-index result, GME region, physical witness, numerical bound or source novelty is claimed. Whether these lemmas are already known or implied by older constraints is NOT checked or answered by mining old sources; this is not scientific priority clearance. The envelope-adopted k2/k4/central/biseparable/regional/parity scopes retain precisely their old imports/MINOR/NR cuts; they are not used to smuggle an unprovided rank3 bridge into these proofs.

All old STOP/HOLD/ZERO findings, N4 UNKNOWN/historical exit unestablished and aux214 STOP persist. Prior authorship/source/method exposure is disclosed in the pre-body ACK; there is NO clean-private-cognition or independently-unaffected-history claim. The stated correctness inputs of this proof are only the admitted definitions/PRIMARY convention and named ordinary facts; no old common-projector coupling line, legacy candidate or held guide is cited, quoted or reopened. If a material provenance/input concern is identified, the affected branch must stop for Main's explicit disposition, not be repaired through a paraphrase. No old root/shared/frozen file was changed.

**Next genuinely admitted step:** attempt an ALL-projector strengthening of the joint local-marginal compatibility constraints, without treating the two-equality classification as a global bound and without selecting a test projector/noise/state. Record the exact successful universal implication or exact obstruction within the next substantive cycle; do not end research merely because this first file exists. Only the present narrow S1 inputs remain allowed. Main must actually read complete author and full-scope review returns before any adoption; writing/hashing or a no-defect headline is not that gate.

Same existing physics-2 owner/new exclusive root. Science deadline **2026-10-31T21:23:27.000Z**; first substantive packet follows the actual14:47:18 pre-body ACK, target<=20min. No timer/heartbeat/ACK-only loop, selected arithmetic, scientific execution, nested/modelCLI/newGO/Git/delete/contact/publication/infrastructure action, stronger formal/kernel/human/family/executable acceptance or original-round deadline reset.
