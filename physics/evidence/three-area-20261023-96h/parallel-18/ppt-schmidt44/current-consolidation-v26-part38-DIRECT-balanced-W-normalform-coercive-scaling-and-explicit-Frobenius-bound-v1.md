# P44 v26 — PART38: DIRECT full-original balanced-W normal form, coercive scaling, exact Frobenius bound and finite certificate

PhysicsPPT44-2. Actual preceding `/bin/date`: **Mon Oct 26 10:23:50 PDT 2026**. **AUTHOR-WRITTEN / LATER UNREVIEWED.** ALL-variable matrix/variational proof only. No chosen state/control/code/parameter/numeric/magnitude/boundary/limit/trig probe, decimal, scientific interpreter/program or machine check. No actual W,rho,delta, filters or polynomial certificate. **Original P44 remains UNMET.**

## B0. Actual authority, source lineage and assurance cut

Main's EXPLICIT future-only v57 **c6d6ea7eea5c2734fb96caa9cd29fde4a551150e2e3ce7c1d6ff2b441aba5dc7** was read ACTUALLY ENTIRE before resumed work, including full raw direction21/ending22–23, after complete wholeACK/finding149/addendum read. No new GO/self-release/redundant ACK loop.

The COMPLETE new balanced-W/coercivity/Kadison lead was saved UNWRITTEN in checkpoint161 **799d55eb72ebee5817db865f1b5c4ec4e41d047c59d07ff101794074c4eabe09** BEFORE this body. Its prospective source is the DIRECT full-norm gap/duality of LITERAL Part36, the compact-certificate interface of LITERAL Part37, and elementary finite matrix/positive-map algebra. It is not a chosen map family or a recovered trial. ENTIRE post143 UNWRITTEN and every consuming representation/source-guidance remain ZERO/no salvage/retest/repair/replay/backconversion/search direction. No verified counterfactual private-independence/unaffected-provenance certificate; recognized separation failure requires immediate STOP/report/WAIT.

Ordinary inputs: finite-dimensional compactness/AM–GM/spectral decomposition, positive square roots/invertible local congruence, differentiable matrix exponential/determinant and partial-trace algebra, exact rational linear-system density. The positive-map Hermitian-square inequality is PROVED below, not a hidden CP assumption or a cited non-Hermitian Schwarz claim. Original counterexample equivalence uses Part36V1–V3's supplied cone-closure/separation/full-I/rationalization argument, not UNREVIEWED Part24–32 zero normalization. The optional finite SOS certificate uses positive-PRIOR Powers I-POW5 through Part37, not a new algorithm/admission.

## B1. ENTIRE original-existence theorem and explicit bounds

**Theorem B1 — WRITTEN at the supplied ordinary facts/proofs.** An original4x4 PPT state with SN>2 exists IFF there are Hermitian Gaussian-rational W,rho, a positive rational delta and the full Part37 rank+sphere identity, such that

- `Tr_A W=Tr_B W=I4/4`, hence TrW=1;
- `q_W(X)>=delta||X||_F² for EVERY COMPLEX rank<=2 X`, certified by that SAME exact identity;
- rho has trace1, rho>0,rho^Gamma>0 and Tr(Wrho)<0.

The data can be taken in the explicit outer bounds

`||W||_F<=1`, `||rho||_F<=1`, `0<delta<=1/16`.            (BOX)

Only W is marginal-balanced. **rho is NOT required balanced.** No regular-zero/normal-I/diagonal-triplet constraint is imposed on W: those cannot simply be conjoined with a strict FULL-norm gap. This is an alternative ENTIRE existence reduction, not a selected topology/family or classification of individual old degenerate states.

The normal-form/filter and Frobenius proofs are provided in B2–B7; the rational/exact-certificate bridges in B5/B8. BOX is a proved compact OUTER domain after including delta=0 in its closure, NOT a known finite grid, positive uniform lower margin, coefficient-height/degree/resource bound or native solver GO. No actual data is supplied.

## B2. A full-gap block-positive W gives a COERCIVE determinant-one trace functional

Start with ANY actual strict-global-gap separator W supplied by Part36V1–V3: for SOME gamma>0, q_W(psi)>=gamma||psi||² for EVERY SR<=2 vector, and an actual PD/PTPD negative PPT pair exists. In particular the inequality holds for ALL product vectors.

For ARBITRARY positive-definite4x4 A,B with detA=detB=1, put

`F(A,B)=Tr[W(A tensor B)]`.

Spectral decompositions of A and B express their product as a positive sum of product projectors; the ENTIRE product inequality gives

`F(A,B)>=gamma TrA TrB>0`.

AM–GM gives TrA,TrB>=4. Thus on ANY nonempty finite sublevel F<=L,

`TrA,TrB<=L/(4gamma)`.

All eigenvalues are bounded above by this common trace bound. Since their product is1, each eigenvalue is bounded below by the inverse cube of that bound. The sublevel therefore lies in a compact set of Hermitian matrices UNIFORMLY separated from the PSD boundary; determinant-one and the F-sublevel are closed there.

A minimizing sequence has an eventual finite nonempty sublevel, so compactness gives an ACTUAL global minimizer (A*,B*). No convexity of F, numerical optimization, actual filter/value or selected test point is required. This proves the relevant scaling existence directly instead of invoking an unexamined operator-Sinkhorn theorem.

## B3. ALL traceless-Hermitian variations yield BOTH exact marginals

At the minimizer, for ANY traceless Hermitian H use

`A_t=A*^(1/2) exp(tH) A*^(1/2)`.

detA_t=1 for EVERY real t, so it is an admissible ALL-variable variation. Let

`C=A*^(1/2) tensor B*^(1/2)`, `W'=C W C`, `F*=TrW'>0`.

The derivative of F(A_t,B*) at0 is

`Tr[(Tr_B W')H]=0` for EVERY traceless Hermitian H.

Therefore Tr_BW' is a scalar identity. Its trace is F*, so it is(F*/4)I. The corresponding arbitrary B-variation gives Tr_AW'=(F*/4)I. Normalize

`W_b=W'/F*`.

Then BOTH marginals are EXACTLY I4/4 and TrW_b=1. This is first-variation algebra at an existing minimizer, not a chosen perturbation/control sample or private numerical boundary calculation.

## B4. ALL global positivity and the ACTUAL PPT negative pair survive the local filter

C is an invertible LOCAL operator, so it preserves Schmidt rank. For EVERY SR<=2 psi,

`q_W'(psi)=q_W(C psi)>=gamma||C psi||²`
`          >=gamma lambda_min(A*)lambda_min(B*)||psi||²`.

After division by F*, W_b still has a strictly positive FULL uniform gap. No singular filter or unproved finite-subset positivity is used.

Let rho be the original PD/PTPD negative pair. Set `rho'=C^(-1)rho C^(-1)`. It is PD, and

`(rho')^Gamma=(A*^(-1/2) tensor bar(B*)^(-1/2)) rho^Gamma`
`             (A*^(-1/2) tensor bar(B*)^(-1/2))`

is PD by LOCAL invertible congruence. Its positive trace s normalizes rho_b=rho'/s. Cyclic trace gives

`Tr(W_b rho_b)=Tr(Wrho)/(F* s)<0`.

No Schmidt-number invariance under PARTIAL TRANSPOSE is asserted; only local-filter covariance and PPT positivity are used. No rho-marginal balancing is added. The filters themselves may be irrational; no rational-filter theorem is claimed.

## B5. Rational data can retain the EXACT balance equations and full gap

The affine space of Hermitian W with Tr_AW=Tr_BW=I4/4 is defined by REAL-linear equations with rational coefficients in its real/imaginary entries. It contains W_b. A consistent rational linear system has a rational particular solution and rational basis for its homogeneous nullspace. Gaussian-rational points are therefore dense EXACTLY inside this affine space, not merely approximately balanced.

A sufficiently close Gaussian-rational W_Q retains the uniform GLOBAL gap, because |q_E(psi)|<=||E||op||psi||², and retains strict negativity against the fixed rho_b. It has the two EXACT marginals and trace1. Gaussian-rational Hermitian approximation of rho_b preserves PD/PTPD and strict pair negativity; normalize by its positive rational trace. This produces eligible rational rho_Q, but not necessarily rational local filters.

A positive rational delta may be chosen existentially BELOW the remaining gap, without selecting/evaluating any value. Thus every original counterexample admits the asserted rational balanced-W/full-rank-PPT data. The converse from any such actual global-gap/negative pair is the original witness duality. No old regular-zero/Pauli normalization theorem is a premise.

## B6. An elementary positive-map Hermitian-square inequality — NOT full Schwarz/CP

Now let W be ANY marginal-balanced BLOCK-POSITIVE Hermitian matrix with Tr_AW=Tr_BW=I4/4. Strict gap/2-positivity/negative pair are NOT needed for the bound below.

Use the Choi convention Phi(Eij)=the ij Alice block of W. Block positivity makes Phi POSITIVE: its expectation on a PSD input's rank-one spectral summands is the corresponding product expectation of W with conjugated Alice vector. The marginals give

`Phi(I)=I/4`, `Tr Phi(H)=TrH/4`.

Thus Psi=4Phi is positive, UNITAL and TRACE-PRESERVING, not necessarily completely positive.

For ANY Hermitian H=sum_l h_l P_l, let E_l=Psi(P_l)>=0, sum_lE_l=I. Define the isometry V by `(Vx)_l=E_l^(1/2)x`, and D=diag_l(h_l I). Then

`Psi(H)=V^dagger D V`, `Psi(H²)=V^dagger D² V`,
`Psi(H²)-Psi(H)²=V^dagger D(I-VV^dagger)DV>=0`.

Taking traces and using trace preservation gives

`||Psi(H)||_F²<=||H||_F²` for EVERY HERMITIAN H.

This proves precisely the inequality needed. It does NOT invoke the generally false non-Hermitian Kadison–Schwarz assertion for arbitrary merely positive maps. No CP property was inferred from block positivity and no spectral example was computed.

## B7. Basis-independent Choi norm gives the EXPLICIT full-domain outer bound

Take ANY Hilbert–Schmidt orthonormal Hermitian basis H_alpha, alpha1,...,16. Summing the proved Hermitian contraction yields

`sum_alpha||Psi(H_alpha)||_F²<=16`.

The Hilbert–Schmidt superoperator norm is basis-independent, and the Choi identity is

`||C_Psi||_F²=sum_ij||Psi(Eij)||_F²=sum_alpha||Psi(H_alpha)||_F²`.

Since C_Psi=4W, it follows that16||W||_F²<=16, hence

`||W||_F<=1`.

No selected product/Schmidt-rank controls were used: the basis equality is universal linear algebra, not a finite positivity test. Each complex entry of W, and therefore each real/imaginary coordinate, is bounded in modulus by1. Any PSD trace-one rho has ||rho||_F<=1 by its nonnegative eigenvalue sum, giving the corresponding state-entry bound.

For a balanced full-gap W, the ALL-product Haar average is

`E_(unit a,b) q_W(a tensor b)=TrW/16=1/16`.

The inequality q_W>=delta on EVERY unit product vector therefore implies delta<=1/16. This is the exact isotropic-mean identity over the WHOLE product sphere, not numerical quadrature, a chosen root-of-unity set or a boundary-value test. Constants1 and1/16 are structural consequences of the original dimension4 and trace normalization, not evaluated probe parameters.

BOX follows. The margins may approach0 across candidate sequences: there is NO uniform positive lower bound, rational denominator bound, certificate-degree upper bound, finite-grid completeness or admission inferred from this outer compact box.

## B8. Complete finite certificate and the remaining original gap

For rational balanced W with a strict full gap, Part37's POSITIVE-PRIOR Powers rational compact preordering theorem and exact rank+sphere reduction give, for ANY positive rational delta STRICTLY BELOW that gap,

`q_W(X)-delta=sum A_j(x)^2+B(x)(||X||²-1)`
`             +sum_(I,J)[C_IJ Re det(X_IJ)+D_IJ Im det(X_IJ)]`,

in ALL32 real coordinates of an ARBITRARY complex coefficient matrix X and ALL16 complex3x3 minors. The converse identity supplies the ENTIRE global norm gap by homogeneity. Its optional ALL-phase-balanced form and degree-six lower obstruction remain as proved in Part37. No auxiliary t or old normal-I zero is imposed.

Powers source dossier **ce876de2b07252aa0949bc5081e55fb7a9fb53ea08fa87403b3eed997568174e** pins complete published/preprint reading and ordinary transitive trust cut. This is standard positive PRIOR, not new method/priority credit. The scaling/norm theorem itself B2–B7 needs no Powers/real-Nullstellensatz theorem; only this finite-certificate application uses the separate positive-PRIOR input.

All forward and reverse bridges for B1 are now supplied. This is an ENTIRE original-existence equivalence and explicit OUTER norm bound at ordinary/provided proofs, NOT an original counterexample or all-state SN<=2 proof. No actual W,rho,delta/filter/certificate, successful degree6 ansatz, coefficient list, degree/height/runtime/resource upper bound or executable assay exists in this packet.

The remaining task is STILL an ACTUAL balanced full-global witness/PPT negative pair/exact certificate, OR an ALL-data exclusion. The finite box does not decide that intersection; neither a finite sample nor a chosen certificate degree suffices. No native solver/interpreter/replay/new GO, parent/formal/kernel/human/configured-family/executable/triple/novelty acceptance or world-novelty/SOTA/source-absence claim follows. Classical scaling/Kadison arguments may be prior; no priority claim is made.

## B9. Whole state, replacement of the held trace route and permanent findings

The earlier unbalanced trace-normalized compactness thought is NOT a correctness premise or a claim of ||W||F<=1 for arbitrary unbalanced W. The delivered replacement proves a full-original existence reduction to BALANCED W and a bound on THAT entire domain, with all local-filter/rational/PPT ties retained. This is not another instance restriction or an unproved WLOG.

Prior37parts+TWOaddenda/ALLdeclared leads/THREEcurrent positive-PRIOR intake dossiers (KG,MOM,NEWPowers with full reader transport pin) remain; JL362logical reader remains EXPOSURE metadata ONLY, not a third intake/proof/adoption/guidance. Parts24–38 remain LATER UNREVIEWED where not individually adopted, not verified unaffected. No pinned/reviewed file is changed and no old verdict transfers.

Own8797d022/new3c1edecd continued-source/unwritten/scope-concern/delayed-recognition findings persist, ENTIRE post143 UNWRITTEN/guidance ZERO/no salvage/retest/repair/replay/backconversion, no invented immediate-at-probe clean stop/separate knowingly-recognized interval/precise private clock. Cadence149 FULL33m12s/even31m45s plus parent delayed handling persist, not cured by v57 or later proof. All cp049/063/081/083/085/089/oldcp013/admission/ACK/cadence/falsequotation/source/parentv9–v57/other-owner/previewv48 histories remain; N4 UNKNOWN/incomplete/overrun/historicalexit-unestablished, old21 NOT_RECONSTRUCTED, auxiliary214 STOP, oldFOUR minors/ELEVEN later proper-domain qualifiers/C27 normalizedN4 ZERO new-method credit/QD-NR. D-N2 false quotation rejected/source already>=0/no author patch. No blind-family/private-cognition/runtime/cadence/clean-history/global-owner census.

Exact source-fixed/ALL-variable conventional WRITTEN/fractions/integer products only, including privately. NO scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/build/test/CLI/nestedagent/newGO; no chosen state/code/control/parameter/boundary/limit/numeric/magnitude/trig probe EVEN rational/decimal/withdrawn-guide/source-fraction decimal restatement. No machine check. Exclusive own root/frozen shared immutable/no Git/deletion/publication. Same original eighteen/full original primary, science cutoff **2026-10-27T11:05:38-07:00**, deadline **2026-10-27T12:35:38-07:00**, substantive actual-clock checkpoints<=30minutes. Active writing, NOT early final park/round closeout.

**END OF COMPLETE v26 PART38. P44 remains UNMET.**
