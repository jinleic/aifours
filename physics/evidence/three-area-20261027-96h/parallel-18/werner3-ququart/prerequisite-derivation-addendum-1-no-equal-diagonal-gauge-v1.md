# S1 addendum1 — NO equal or Loewner-ordered diagonal range gauge; inverse-free coupling

Owner **PhysicsResearch96h-2**, SAMEphysics-1. Actual `/bin/date` before writing: **Tue Oct 27 14:48:48 PDT2026**. **WRITTEN AUTHOR CANDIDATE**, not reviewed/adopted/formal/kernel/human/family/executable/novelty-cleared. Same exact definition-onlyS1 inputs and all controls; no new source, selected state/parameter/boundary/control, scientific execution, old proof/held-guide consumer or external model. This is additive to immutable `prerequisite-derivation-v1.md`, SHA256 `09b902fa35d379b21c21c5bb83145e0ae336fec986a9ef12eb719f3408e3cbe6` (219LF/16834B); no old bytes changed.

## 1. Exact actual-object setting

Use the already derived operator `P=⊗_(i=1)^3(I−F_i/2)` onH⊗H, withHi=C^4 andFi the local swaps; `mI<=P<=MI`, m=1/8,M=27/8. For EVERY isometryU:C^2→H, columnsu1,u2, define

`X_ab=(<u_a|⊗I)P(|u_b>⊗I)`,

`D1=X11`, `D2=X22`, `A=X12`.

Then `X_U=[[D1,A],[A†,D2]]>=mI`, whereas the originalq3 onALLoperatorsC=UV† with arbitrarycomplexV is represented by

`K_U=[[D1,A†],[A,D2]]`.

The faithful original criterion is `K_U>=0` for EVERYactualrangeplaneU; no first-site product ray or special co-range is required. Previousv1 proved both coverage/reconstruction, the exact Schur `S_U=D2−A D1^−1 A†`, and the weighted-adjoint mismatch with automatic `S0_U=D2−A†D1^−1A>=0`.

The new theorem below rules out, for ALLadmittedU and ALLtheir orthonormal bases, an equal-diagonal or one-sided-Loewner-order repair of that mismatch. It does NOT sayS_U is negative, and no candidateplane is chosen or tested.

## 2. Explicit conditional-operator map, derived from the SAME swaps

Define an elementary linear map on operatorsT onH by

`Lambda(T)=Σ_(S⊂{1,2,3})(−1/2)^|S|
             (Tr_(S^c)T)_S ⊗ I_(S^c)`,                    (Lambda)

with the tensor factors reinserted in their original site order. S=empty means `(TrT)I_H`; S=all means`−T/8`. Allpartialtraces are UNNORMALIZED. This is a formula for arbitrarycomplexT, not a new candidate state or selected input.

ExpandingP into partialswaps shows exactly

**`X_ab=Lambda(|u_b><u_a|)`.**                               (X-Lambda)

Proof at a subsetS: the matrix element ofF_S betweenu_a,u_b on the firstcopy, acting on thesecondcopy, is the reducedoperator `Tr_(S^c)(|u_b><u_a|)` onS, tensoridentity onitscomplement. This follows bythematrix units ofthe swaps: exchangedindicesremainasrow/columnindices onS andunexchangedfirst-copyindicescontractonS^c. Its sign/coefficient inP is precisely(−1/2)^|S|. SummingALLsubsets proves(X-Lambda), including the empty/full endpoints; no mixed contraction is discarded.

EquivalentlyLambda is the tensor product of THREEidentical elementarylocalmaps

`L(T)=Tr(T) I_4−T/2`                                        (localL)

on the full complexoperator spaces. This equivalence follows byexpanding the tensorproduct linear maps, not by assuming anoldraw-reduction theorem or anexternalpositive-map classification. No oldp12/q6 identity is input.

## 3. Injectivity and trace identities — no order of the inverse assumed

For any complexoperatorT onC^4, decompose uniquely

`T=alpha I_4+T0`, `alpha=Tr(T)/4`, `TrT0=0`.

Then

`L(T)=(7/2)alpha I_4−T0/2`.

The scalar andtraceless coefficients are nonzero. ThusL is invertible on the ENTIREcomplexoperator space; an explicitinverseis

`L^−1(S)=−2S+(4/7)Tr(S)I_4`.

Substitution, or the scalar/traceless decomposition, provesboth compositionidentities forALLS. No numericalmatrix is evaluated. The tensorproductLambda=L⊗L⊗L is therefore invertible with inverseL^−1⊗L^−1⊗L^−1. This usesonly the spanning elementarytensor matrixunits oftheoperator space.

**The inverse is used for injectivity ONLY; no positivity/order-preserving property of L^−1 or Lambda^−1 is asserted or applied.**

Also `TrL(T)=(7/2)TrT`. Tensoring andlinearity give

`TrLambda(T)=(7/2)^3 TrT`.                                  (Trace)

Sinceu1,u2 are orthonormal, theirtwo distinct rank-oneorthogonalprojectionsrho_a=|u_a><u_a| bothhavetrace1. Consequently

`TrD1=TrD2=(7/2)^3`, `TrA=0`.                               (DiagTrace)

These are exactstructural identities forEVERYU, not a finiteparametercount, sample or spectralprobe. Lambda preservesadjoints becauseeachpartialtrace/reinsertionhasrealcoefficients; D1−D2 is Hermitian.

## 4. Universal obstruction theorem: EVERY range basis has crossing diagonals

**Theorem G.** For EVERYisometryU:C^2→H, the actualconditionaloperatorsD1,D2 satisfy:

1. `D1 != D2`;
2. `D1−D2` has bothpositive andnegative spectraldirections;
3. neither `D1<=D2` nor `D2<=D1` inLoewnerorder;
4. allthreefacts remaintrue afterEVERYunitarychangeoftheorthonormalbasis ofthe SAMErangeplane.

**Proof.** EqualityD1=D2 and(X-Lambda) would implyLambda(rho1−rho2)=0. Injectivitywould giverho1=rho2, impossiblefororthogonalunitvectors: applyingthetwoprojections tou1 yieldsrespectivelyu1 and0. Hence the Hermitiandifference is nonzero. Its traceiszero by(DiagTrace). The finite-dimensionalspectraltheorem thereforeforces BOTHpositive andnegative eigenvalues: ifitwereone-sidedsemidefinite, tracezero wouldforceit tobezero. This proves1–3. Aunitarybasischangeagainproducesanorthonormalpair, so thesameargumentapplies universally, proving4. QED.

No particularplane/state orboundaryvalueis selected inthisproof. ThetheoremdoesNOT claimtheoriginalK_U isindefinite: positivityof aTWO-by-TWO blockmatrix doesnotrequireitsdiagonalblocksbeLoewner-comparable. Thetheorem is anexact failure ofONEsimplifyingcompletionpremise, notanoriginalW4counterexample orall-methodno-go.

Inparticular a proposed repair “choose a rangebasis withD1=D2 so adjointcontractionhasthesameweights” is impossible for EVERYactualrangeplane. Anattempt toswaporcompare thetwo weights by aone-sidedLoewnerorder is likewise unavailable in EVERYorthonormalbasis. This is a genuine all-variable obstruction at the ORIGINAL rank interface, strongerthan merely failingtofind aconvenient basis. It doesnot proveanynewnegativeq3 or universalSchur domination.

## 5. Gauge covariance and a basis-independent inverse-free criterion

LetG∈U(2), U'=UG and V'=VG; C=U'V'†=UV†. StackingtheVcolumns, `w=[v1;v2]`, gives `w'=(G^T⊗I)w`. Theactualcompressionchangesas

`X_(UG)=(G†⊗I)X_U(G⊗I)`.

TransposingONLYtheauxiliaryblocklabels gives

`K_(UG)=(G^T⊗I)K_U(bar(G)⊗I)`.                             (Gauge)

Bothouter factorsaremutualunitaryadjoints. Combinedwithw' and`bar(G)G^T=I`, theoriginalquadraticform isunchanged. ThuswholeK positivitydepends ontheactualrangeplane, notitsorthonormalbasis. This paysgaugecovariancewithoutclaimingthatindividualSchurentries/S/weightednormalityarebasis-invariant.

Put `D_U=D1+D2=Tr_aux X_U>=2mI`. Define the fixedauxiliaryunitary

`J=[[0,−1],[1,0]]`.

PureTWO-by-TWOblockmultiplication yields

**`K_U=(J†⊗I)[I_2⊗D_U−X_U](J⊗I)`.**                       (Reduction)

Indeed the middlematrixhasblocks `[[D2,−A],[−A†,D1]]`; multiplyinggives `[[D1,A†],[A,D2]]` withALLcrosscouplingsretained. No inverseofSchmidt/columncoefficientsandnoboundarylimitappears.

Hence the originalq3 problem is equivalently the universalactualrange-plane inequality

**`X_U <= I_2⊗Tr_aux(X_U)` for EVERYisometricU.**             (R)

Inbasis-independentphysicalnotation, Pi is the rank-twoorthogonalprojection onto rangeU,

`D_Pi=Tr_first[(Pi⊗I)P(Pi⊗I)]`,

and(R) says, onrangePi⊗H,

`(Pi⊗I)P(Pi⊗I) <= Pi⊗D_Pi`.                               (R-Pi)

Thetwoplanequantifier isunrestricted; noactualoperator ofrank<=2hasbeen lost by§2ofthepredecessor. Anynegativequadraticdirectionof thisdeficitmapsbyJ/gaugeandthepredecessor'sfactorconstructionto anactuallegalC. ExistenceofsuchadirectionisNOTclaimed.

BecauseD_U>=2mI, onecanoptionally normalize

`Y_U=(I_2⊗D_U^−1/2) X_U (I_2⊗D_U^−1/2) >=0`,

`Tr_aux Y_U=I_H`.

Then(R) isexactly `Y_U<=I`. ThisnormalizationisuniformlylegalforallUandrank0/1factorcoefficients; no singularreferenceinverseisintroduced. It is anexactinterface, notanewpositivitytheorem.

## 6. What genericpositivity does and does NOT pay

Thegenericpositiveblockoperator estimate givesonly

`X_U <= 2 I_2⊗D_U`.                                        (generic2)

To proveit, splitanarbitrarystackw intotwocomponentsw1,w2 supportedonitsauxiliarylabels. Positivitygives

`<w,X_Uw>=||X_U^1/2w1+X_U^1/2w2||^2
 <=2(||X_U^1/2w1||^2+||X_U^1/2w2||^2)
 =2(<v1,D1v1>+<v2,D2v2>)
 <=2(<v1,D_Uv1>+<v2,D_Uv2>)`.

Thisis a universalALL-variableHilbertspace inequality, not aselectedcontrol. Itsfactor2 isNOT thefactor1 requiredin(R), and no equality/sharpnesswitness ischosen. Reportinggeneric2 as(R) woulddropanunpaidfactor/coupling. Nooriginalsignadvanceisclaimedfromthisweakerbound.

Thepredecessor'sstrongeractualresidualCS estimateandDelta-selfcommutatoridentityremainseparatevalidcouplingfacts. TheoremG rulesout equal/ordereddiagonal-weightrepairs **universally**, notjustatselectedstates. None ofthese automaticallyproves(R) or theuniversalS0+Delta domination. Thefirstunpaidinput isnow exact andinversefree: prove(R-Pi) forEVERYphysicalrank-twoprojectorPi, or oneexactnegativeactualdirectionwiththegivenlegalC reconstruction.

## 7. Honest status, inputs and continued work boundary

**Interface reproduction:** (X-Lambda), gaugecovariance, Reduction andnormalization are exactreformulations, not alone scientifictargetprogress. **New written structuralobstruction at the supplied interface:** TheoremG proves the equal/Loewner-ordereddiagonal range-gauge simplifications are impossible forALLactualplanes. ItsproofusesONLY theliteralq3-derivedswaps, elementarylocaltrace/traceless decomposition/tensorinjectivity/tracecyclicity/spectraltheorem. Classicalmethodancestryisordinary; independentnovelty orstrictdifferencefromallpriorproviders isnotcertified.

Nooriginalq3 negativeoperator, universalW4positivity, all-copy result or source/bookequivalence isestablished. NR-UNIVERSAL-COUPLED-DOMINATION nowequivalently includes(R-Pi); NR-SOURCE-EQUIVALENCE andallreview/adoption/strongergatespersist. No co-Choi/rank-onlycertificate, product-rayWLOG, oldraw/signreduction, v4–v25 orprotectedguidancewasimported.

This completes thenextgenuinelyadmittedS1ALL-variablestepafterthefirstpacket, withouteditingit. Any furtherclaimmustaddress theactualfactor1jointcoupling, notrepeatencoding/generic2/equalgauge attempts ormanufactureparametertrials. Ifnoindependentnewcoupledinputisavailable, reportthatexactmathematicalprerequisite forparentallocation; itisnotall-routeexhaustion ororiginalcompletion. S0/HOLD/STOPoutsideS1/allZERO/priorauthorship-nonblind/N4UNKNOWN historicalchildexitUNESTABLISHED/aux214STOP/new96hdeadline remain.

**END COMPLETE S1 ADDENDUM1 — AUTHOR-WRITTEN UNIVERSAL GAUGE OBSTRUCTION; ORIGINAL W4 OPEN.**
