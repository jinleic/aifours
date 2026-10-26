# CURRENT P44 CONSOLIDATION v11 — PART9/9: entire two-qubit-Pauli Bell class and a full-space decomposable neighborhood

PhysicsPPT44-2. Actual pre-write `/bin/date`: **Sun Oct 25 21:14:11 PDT 2026**. Exact WRITTEN finite-dimensional proof only, no scientific arithmetic interpreter/calculator/eval/program/CAS/enumeration/solver/replay/build/test/CLI/nested agents/new GO. All old source/process findings and the same original cutoff/deadline remain.

## BB0. Scope, old/new separation and complete-current rule

This is additional C28, a WHOLE but PROPER Pauli-diagonal witness/state classification, not a P44 solution. It rejects a proposed multi-quaternion/Pauli negative-half route rather than claiming a genuinely new viable two-positive indecomposable half. It is NOT the fixed cyclic-four-Weyl scalar claim, NOT an arbitrary<=3-ME scalar claim, and NOT a hypothesis that all ququart witnesses are Pauli-diagonal. The collapse below to PSD plus a single-Bell completely copositive witness is the actual reason this attempted replacement fails. No old scalar closure is relabeled as a winning construction.

An entire-current v11 gate requires ALL NINE original parts/endings, BOTH mandatory current-consolidation addenda and the already mandated C12/process overlays. Parts1–8 retain immutable historical headers/counts. Nothing new is retroactively inserted into v10 or inherited from old reviews. This Part9 alone is not a full-current gate.

In particular mandatory `current-consolidation-ADDENDUM-2-C27-old-normalized-N4-cone-equivalence-v1.md`, SHA256 `afe008cfb7a7c2471f2f901198b10d9aa1814d8b53b6e0a92722ac37122d4df1`, WITHDRAWS any NEW-mechanism credit for C27 at k2: it is EXACTLY the owner's old trace-corrected N4 cone, eta=2mu. C26 concerns the BARE cone and does NOT retire that corrected assay. C27's additional general finite-completeness/rational-certifiability argument remains at the explicit QD import, unaccepted, no actual certificate/N. Original N4 remains UNKNOWN/incomplete/overrun/oldexit-unestablished.

Checkpoint081's later approximate scout/inferences remain ZERO credit under actual parent v16; its exact code-plane/low-level text stays CONTEXT ONLY, not used as a premise below. The following argument is independent Pauli spectral algebra, not a rerun/backconversion of that scout. No general clean-thought census is claimed. Parent C1–C18 adoption/two retained MINORs does not adopt C19–C28.

## BB1. Actual complex Pauli Bell basis and pair-rank identity

Fix physical C4=C2 tensorC2 on each side. Let sigma0=I2,sigma1=X,sigma2=Y,sigma3=Z, with the actual imaginary Y matrix. The sixteen unitary matrices

`U_(a,b)=sigma_a tensorsigma_b`

are orthogonal in Hilbert-Schmidt inner product. Put `Phi_U=vec(U)/2`, so these form an orthonormal maximally entangled ququart basis. Define `Pi_U=P(Phi_U)` and use Bob partial transpose Gamma.

For ANY DISTINCT U,V, their relative unitary U*V is a phase times a nonidentity two-qubit Pauli. Hence there is an EXACT phase t in{1,-1,i,-i} such that

`H=t U*V` is Hermitian unitary, `TrH=0`.

It has eigenvalues+1,-1 EACH multiplicity2: H^2=I,trace0,dimension4. Therefore

`rank(U+tV)=rank(U-tV)=2`.                              (BB1.1)

The actual unit vectors

`psi_plus=(Phi_U+tPhi_V)/sqrt2`,
`psi_minus=(Phi_U-tPhi_V)/sqrt2`

have Schmidt rank exactly2. Orthogonality of Phi_U,Phi_V fixes their norms. Their FULL operator average is

`(Pi_U+Pi_V)/2=[P(psi_plus)+P(psi_minus)]/2`.             (BB1.2)

All complex phases and cross-term cancellation are literal, not finite sampled products or a real-vector restriction. This identity is special to this Pauli basis. It is NOT asserted for arbitrary pairs in the cyclic Weyl basis or arbitrary maximally entangled vectors.

## BB2. EVERY Pauli-Bell-diagonal state with largest coefficient<=1/2 has SN<=2

Let

`rho=sum_U p_U Pi_U`, p_U>=0,sum_U p_U=1,max_U p_U<=1/2.

The polytope defined by those inequalities has only the equal-pair vertices `(e_U+e_V)/2`. Indeed if two coordinates are strictly between0 and1/2 one can transfer a small signed amount between them and remain feasible, so the point is not extreme. If exactly one coordinate is fractional, the sum1 with all others0 or1/2 forces it also to be0 or1/2. Thus a vertex has exactly two1/2 coordinates. Compact finite-dimensional convexity gives a finite convex combination of equal pairs. Applying (BB1.2) gives an actual finite SR2 ensemble of rho, including all zero/closed boundaries.

For rational p the pair weights can also be specified without an existence-only LP: partition the unit circle into consecutive half-open intervals I_U of lengths p_U and let

`m_UV=length[I_U intersect(I_V-1/2)]`, `w_UV=2m_UV` forU<V.

Translation by1/2 shows m_UV=m_VU. Since each interval has length<=1/2, m_UU=0 apart from measure-zero endpoints. Row sums are p_U, hence `sum_(U<V)w_UV=1` and `p=sum_(U<V)w_UV(e_U+e_V)/2`. Intersections are finite unions of intervals with rational endpoints when p is rational, so all weights are rational. Together with the explicit phases t this is a finite exact symbolic ensemble prescription; no enumeration/program generated a table.

## BB3. ALL PPT states in this proper Bell-diagonal class are covered

For ANY physical PPT density rho and ANY normalized ququart maximally entangled Phi_U,

```
Tr(Pi_U rho)=Tr(Pi_U^Gamma rho^Gamma)
 <=(1/4)Tr(rho^Gamma)=1/4,                              (BB3.1)
```

because `Pi_U^Gamma=F_U/4`, where F_U is a Hermitian unitary conjugate of the flip. Thus a PPT Pauli-Bell-diagonal density has p_U<=1/4, strictly within the cap1/2 from BB2. It therefore has SN<=2 by the full displayed operator ensemble, not by a restriction on tested witnesses.

This covers arbitrary real probabilities, not just uniform lattice subsets; no finite vertex census or computer-assisted252-ray classification is imported. It does NOT say that twirling preserves an arbitrary state's Schmidt number: it need not. Only objectives of witnesses with the actual corresponding symmetry can be reduced without loss.

## BB4. ENTIRE Pauli-Bell-diagonal universal complex two-positivity iff

Let the Hermitian physical witness be

`W=sum_U lambda_U Pi_U`, ALL lambda_U real with no positivity/normalization assumption.

If W is universally complex-SR<=2-nonnegative, testing either actual rank2 vector in (BB1.2) gives

`lambda_U+lambda_V>=0 for EVERY distinct U,V`.           (BB4.1)

Conversely suppose (BB4.1). If every lambda is nonnegative, W is PSD. Otherwise there is exactly ONE negative eigenvalue lambda_U0=-a<0 and all the others are>=a. The exact decomposition is

```
W=a[I16-2Pi_U0]+P,
P=sum_(U!=U0)(lambda_U-a)Pi_U>=0.                       (BB4.2)
```

For any unit SR<=2 vector psi, its maximally entangled fidelity obeys `|<Phi_U0,psi>|^2<=2/4=1/2` by the Schmidt/SVD Cauchy bound. Thus I-2Pi_U0 is universally complex-SR<=2-nonnegative, and so is W. This proves (BB4.1) is NECESSARY AND SUFFICIENT, all real/complex and zero/tied boundaries included.

The proof does not assert that all two-positive ququart witnesses can be put in this diagonal form. The simultaneous Pauli eigenbasis is a material restriction.

## BB5. Explicit decomposability, not merely failure on an attractive control

The non-PSD branch of (BB4.2) has

`Q=a[I16-(1/2)F_U0]>=aI16/2>0`,                         (BB5.1)

and `a[I16-2Pi_U0]=Q^Gamma`. Hence

`W=P+Q^Gamma`, P,Q>=0.

Therefore EVERY universally two-positive witness in this ENTIRE proper Pauli-diagonal class is physically decomposable and misses EVERY actual PPT input of ANY geometry. No selected state/old rectangle/source support or new input can rescue it. The PSD branch is decomposable trivially.

This rejects, in particular, any proposed multi-skew/quaternion expression only AFTER verifying it truly lies in this same Pauli-Bell diagonal algebra. For Pauli monomial J, `(I tensorJ)F(I tensorJ*)` is diagonal in this Bell basis (the flip's transpose parities are diagonal and local Paulis permute the basis), so a combination of I,Pi_I and such terms is covered. Arbitrarily rotated different J need not be simultaneously in that algebra; no unrestricted multi-J or all-map transfer is made.

## BB6. An actual full-space neighborhood outside the exact symmetry class

For a non-PSD W as above and ANY Hermitian perturbation E, not assumed diagonal/Pauli-covariant/two-positive, if

`norm(E^Gamma)_operator<=a/2`,                           (BB6.1)

then

`W+E=P+[Q+E^Gamma]^Gamma`, `Q+E^Gamma>=0`.

Thus the entire closed PT-operator-norm neighborhood in the FULL Hermitian16x16 space is decomposable. The boundary is valid since Q>=aI/2; strict inequality gives strict positivity of the CCP positive part. This is a real off-symmetry method barrier, not a claim that the symmetry closure extends to arbitrary perturbations. Any nondecomposable deformation of such a witness must violate this actual norm bound. No norm was numerically evaluated or inferred from samples.

A unitary local congruence transports the displayed positive decomposition and its natural transformed neighborhood. Arbitrary singular filters preserve decomposability of the image, but no unchanged a/2 norm radius is claimed after a nonunitary filter. This distinction avoids a hidden all-filter norm assumption.

## BB7. Source screen, imports, original gap and exact residual

A bounded public source screen read the actual initial LF1–300 of Müller-Hermes, `https://arxiv.org/html/2006.14543v1` (tool artifact33389, total2450LF), including abstract/introduction/main tensor-square theorem, complete Pauli definitions and the beginning of spectral/duality theory. NOT a whole-paper/AppendixA/252-extremal-ray reconstruction, and no novelty conclusion. The source discusses a much larger positive/decomposable Pauli cone and known classifications; none of its computer or long combinatorial proofs is a correctness premise for BB1–BB6. The proof above is self-contained at elementary Pauli/SVD/convex/PSD/PT facts. Literature search/miss is not priority or P44-openness proof.

This does not reset the old cyclic four-Weyl scalar controls or claim that Pauli re-expression supplied the missing positive half. Rather it exhausts this attempted alternative and proves why it collapses to a PSD plus single-Bell-CCP form. No new rational PPT/SN3 state is put forward without a separator. No hypothetical Pauli-negative P44 pair survives the exact universal rank2 tests.

**Original P44 remains UNMET.** No explicit rational/Gaussian-rational4x4 PPT state with a universally complex-SR2-nonnegative strictly negative witness, and no unrestricted all4x4 PPT SN2 theorem. The source-compression/fullD residuals outside their actual closures remain open; all C19–C28 await exact fresh adoption at their own scopes. The current full v11 is not a completed assignment, park or round closeout.

All older findings and mandatory C12/normalization-provenance/metadata/process overlays remain. The later private approximate code-plane scout is ZERO credit, not reused here. WRITTEN proof is not formal/kernel/executable/triple/configured-family/human/cross-vendor assurance, novelty clearance or a scientific GO. Same original18/cutoff/deadline.

**END OF COMPLETE CURRENT v11 PART9/9.**
