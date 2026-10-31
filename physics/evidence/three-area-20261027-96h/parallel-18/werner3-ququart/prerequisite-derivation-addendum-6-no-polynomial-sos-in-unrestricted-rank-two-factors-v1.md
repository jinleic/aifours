# S1 addendum6 — no polynomial sum-of-squares identity in unrestricted actual rank-two factors

OwnerPhysicsResearch96h-2, SAMEphysics-1. Actual `/bin/date` before writing **Tue Oct 27 15:18:20 PDT 2026**. **WRITTEN AUTHOR CANDIDATE UNREVIEWED**, ordinaryproofonly/notformal-kernel-human-family-executable-noveltycleared. Inputs ONLYreleasedS1literaldefinitions, exactoriginalfactorcaller andexplicitpolynomial/linear-algebrafactsbelow. No selectedoperator/state/control/parameter/phase/singularratio/overlap/boundary/magnitudeprobe, no scientificinterpreter/CAS/program/calculator/enumeration/solver/replay, no excludedoldproof/guideconsumer. The gaugeparametersbelow are UNIVERSE-QUANTIFIEDvariables inpolynomialidentities, never assigned/probedinstances.

This is a NEWmethod-class obstruction in the ORIGINALfaithfulfactorization, independentof whetherW4eventuallyispositiveorfalse. It is NOTanoriginalnegativeC or a proofallpossiblecertificatesfail. It is NOTcountedasnewversusliterature/SOTA: thataudit isunperformed. Initialauthorpacket/addenda1–5stayimmutable andUNREVIEWED. ThislaterpaperisNOTretroinsertedintothe853LFfrozenreviewrequestalreadySENTtoMain.

## 1. Exact no-go theorem

LetU,V beARBITRARYcomplex64-by-2matrices and `C=UV†`. There are **NO FINITELYMANY polynomials**p_k in thereal/imaginaryentriesofU,V, withfixedcomplexcoefficients, suchthat

**`q3(UV†)=Σ_k |p_k(U,V,barU,barV)|²` for ALL U,V.**          (SOS)

Thepolynomials mayhaveANYfiniteaprioridegree andmayinvolvebothvariablesandconjugates. Realpolynomialsumsofsquaresareincludedasspecialcases. No orthonormality, columnnondegeneracyorotherconstraintonfactorsispermittedin(SOS); thecaller coversALLactualrank<=2operators, includingrank0/1.

This rulesout an entire unrestrictedpolynomialSOSidentityapproach, **not** rational certificates/positivepolynomialmultipliers, certificatesonorthonormalizedfactorsmoduloU†U=I, validinequalityproofsusingrank, nonpolynomial/operator-valuedinput-dependentcoefficients, higher constraints, or futurecoupledcoercivityarguments. It provesNOTHINGbyitselfaboutthesignofq3onactualrank<=2.

## 2. Elementary quadratic rigidity of the actual rank-two domain

**Lemma Q.** A realhomogeneousquadraticformR onthe REALvectorspaceofcomplex64-by-64matrices, vanishingforEVERYactualrank<=2C, vanishesforEVERYC.

**Proof.** Take theFULLrealmatrixunitbasis consistingofALL E_ab andiE_ab. Everybasisvectorhascomplexrankone; EVERYrealcombination `s e_beta+t e_gamma` oftwoofthesehascomplexrank<=2. Thus

`R(s e_beta+t e_gamma)=0` forALLreal s,tandALLbasisindexpairsbeta,gamma.

Comparingcoefficientsofthispolynomialidentity (no chosenparameterinstance) killseverydiagonal/mixedcoefficientofR. HenceRidenticallyzero. QED.

Inparticular thereisno nonzeroquadraticrank-nullcorrection whichcouldchangeanindefiniteoriginalquadraticformintoaglobalPSDformwhileagreeingwithit onALLrank<=2operators. Thefullunrestrictedcomplexdomainisessential; noHermitian/real/productrestrictionissilentlyinserted.

## 3. If(SOS)existed, every square would have homogeneous degree exactly two

TheleftsideishomogeneousofdegreeFOURunderSIMULTANEOUSREALscaling(U,V)→(rU,rV): C→r²Candq3→r^4q3. Decomposeeachp_kintoreal-homogeneousdegreepieces.

At thelowestnonzerodegreeeacrossALLp_k, thecoefficientofr^(2e) in thesquaredsumis `Σ_k |p_(k,e)|²`. Ife<2, itmustvanishidentically, forcingeachsuchpiecezero, contradiction. Similarlythehighestdegreeh>2wouldhaveleadingcoefficient `Σ_k |p_(k,h)|²` atdegree2h>4, againimpossible. ThusEVERYnonzerop_kisreal-homogeneousdegree2. This argumentusespolynomialcoefficientidentityforallr, not a sampledscaling/magnitude.

WritingthesepolynomialsinU,barU,V,barVislegitimate: theseareaninvertiblecomplexlinearchangeoftheformalreal/imaginarycoordinates, soformalcoefficientcomparisonremainsvalid.

## 4. Noncompact actual-factor gauge forces each square to be individually balanced

TheactualoperatorUV†isinvariantunderEVERYinvertiblecomplex2-by-2G:

`(U,V) → (UG, V G^(−†))`.

Indeed `(UG)(V G^(−†))†=U G G^(−1)V†=UV†`. Hencehypothetical(SOS)wouldsaythesquarednormofthepolynomialvector(p_k) isCONSTANTonEACHsuchgaugeorbit.

FirstuseALLpositiverealdiagonalgauges `G=diag(t1,t2)`, witht1,t2ARBITRARYpositivevariables. Letu_alpha,v_alpha bethefactorcolumns. Theytransformas

`u_alpha→t_alpha u_alpha`, `v_alpha→t_alpha^(−1)v_alpha`,

andlikewiseforconjugates. ForfixedarbitraryU,Veachp_kbecomesaLaurentpolynomialint1,t2, boundedon(0,infinity)²bytheconstantnonnegativeSOSsum. A LaurentpolynomialboundedforALLpositivevaluesofeachvariablecanhaveonlyexponentzero: thehighestpositivepowerisunboundedatinfinity, thelowestnegativepowerisunboundedat0. Applyingthistoallvariablesforcesconstancy. This is a universal bounded-polynomial argument, NOT a choice/measurementoflargeorsmallt oraboundarytrial.

ThusEVERYp_kisindividuallyinvariantunderALLthesepositivediagonalrescalings. Homogeneousdegree2andweightzeroineachcolumnforceitsform

`p=Σ_(alpha=1)^2 [ u_alpha^T A_alpha v_alpha
                   +u_alpha^T B_alpha bar(v_alpha)
                   +bar(u_alpha)^T D_alpha v_alpha
                   +bar(u_alpha)^T F_alpha bar(v_alpha) ]`,  (Balanced)

withfixedcomplex64-by-64coefficientmatrices. TherearenoU-U/V-Vtermsor unequal-columnU-Vterms: theircolumnweightsarenonzero. Transposehereisplainalgebraictranspose, andnoHermitian/realcoefficientrestrictionisassumed.

Theboundednessargumentisconditionalon(SOS); ifanyorbit'sq3wererathernegative,SOSwouldalreadybeimpossible. Wehavenotassertedthatnegativeoriginaloperatorsactuallyexist.

## 5. ALL-complex shears force every square to factor through C itself

Use thewholeunipotentgaugefamily `G(t)=I+tE_12`, withARBITRARYcomplex t. SinceE_12²=0 itsinverseisI−tE_12. Thecolumntransformationsare

`u1'=u1`, `u2'=u2+t u1`,

`v1'=v1−bar(t)v2`, `v2'=v2`.

ForfixedarbitraryU,Veachp_kontheorbitisapolynomialinRe(t),Im(t), whoseabsolutevalueisboundedbecauseΣ|p_k|²isconstant. A polynomialonALLrealEuclideanspacewhichisgloballyboundedmustbeconstant: anynonzerohighesthomogeneouspiecewouldgrowalongadirectiononwhichitisnonzero. HenceEACHp_kisindividuallyinvariantunderALLtheseshears.

Substituting(Balanced), thefourindependenttypesofmonomialschangeby

`u1^T [t A2−bar(t) A1]v2`,

`t u1^T(B2−B1)bar(v2)`,

`bar(t)bar(u1)^T(D2−D1)v2`,

`bar(u1)^T[bar(t)F2−t F1]bar(v2)`.

TheircoefficientidentitiesforALLcomplex t,ALLcomplexu1,v2give

`A1=A2=F1=F2=0`, `B1=B2`, `D1=D2`.

Here t,bar(t)areindependentlinearcoordinatesoverCintherealvariablesRe(t),Im(t); thefourU/barU,V/barVmonomialtypesarealsoindependentformalcoordinates. No numericalphase/shearinstanceistested.

ConsequentlyEVERYsquarepolynomialhastheform

`p_k=Σ_alpha[u_alpha^T B_k bar(v_alpha)
                  +bar(u_alpha)^T D_k v_alpha]
    =Σ_(i,j)[(B_k)_(i,j) C_(i,j)
                  +(D_k)_(i,j) bar(C_(i,j))]
    =:L_k(C)`.

ThusL_kisafixedREAL-LINEARcomplex-valuedfunctionalof theACTUALoriginaloperatorC. Thisindividualfactor-throughpropertywasNOTassumed: itwasforcedbythepositiveSOSsum'sboundednessalongnoncompactactual-objectgauges.

## 6. Contradiction with the actual original quadratic operator

Everyrank<=2CisUV†, asprovedbothdirectionsintheinitialpacket, includingdegeneratecases. Hypothetical(SOS)thereforegives

`q3(C)=Σ_k |L_k(C)|²` forEVERYactualrank<=2C.

Bothsidesarerealhomogeneousquadraticforms inC'sreal/imaginaryentries. LemmaQforces thisidentityforEVERYC, regardlessofrank. Thustheoriginalq3wouldbegloballyPSD.

Buttheliteraldefinitiondirectlyprovesit isNOTgloballyPSD. Set `e_j=E_j/4`, theCANONICALlocalmaximallyentangledrank-oneprojection suppliedbythedefinitions, and `Q_j=I−e_j`. EachQ_jisnonzero(localpairedspacehasdimension16). Theliteralquadraticoperatoris

`W=⊗_(j=1)^3(I−2e_j)`.

Thecanonicalprojection

`Pi=e1⊗Q2⊗Q3`

isnonzeroandobeys `W Pi=−Pi`. ThereforeWhasanegativespectralspace, anditsquadraticformcannotbegloballyPSD. This is aspectralidentity/existenceargument, NOT an evaluatednewstate/Ccontrol/probeor anactualrank-twoexample. Indeedthealreadyprovedglobalrank-two lowerbound inaddendum3excludesrank<=2forEVERYnonzerooperatorwhosevectorizationliesintheminus-oneeigenspace. No route-negativevectorismislabeledW4.

Thiscontradictionprovesthefullno-go(SOS).

## 7. Scope, imports and the live residual

ProvedALL-variableobstruction: **arbitraryfinite-degreepolynomialSOSinUNRESTRICTEDactualrank-twofactorvariablesisIMPOSSIBLE**, becausehomogeneity/noncompactgaugeforcesallsquarestobequadraticandlinearintheactualC, andrank-twoquadraticrigiditywouldincorrectlymakeq3globallyPSD. Thisisnotjustanencodingoranotherselectedinconsequentialenumeration. It eliminatesaconcretewholecertificateclasswithoutanyscientificexecution.

ImportsareONLYthefaithfulUV†caller, real/complexpolynomialcoefficientcomparison, elementarybounded(Laurent)polynomialfactsprovedabove, realquadraticpolarization, andtheliteralmatrixunits/projectionidentities. No invarianttheorytheorem, externalpaper, CAS or source-count/rankheuristicisimported. Priorliterature/noveltyofthisordinarygaugeargumentisUNVERIFIED; writtenparent/peeradoptionnotconferred.

WhatitdoesNOTeliminate: polynomialSOSmoduloISOMETRIC-Uconstraints (noncompactgaugeisthenNOTadomainpreservingaction), rational or multipliercertificateswithfullyjustifieddenominators/boundaries, actualrank-dependentoperatorinequalities, or anewcoupledMS/R-Picoercivitylemma. No assertionthosealternativesexist/succeed. OriginalW4q3>=0vsactualnegativeCremainsOPEN; no all-routeexhaustion/earlypark/newGO.

NextvaluableadmittedstepmustrespectthisobstructionratherthansearchingunrestrictedpolynomialSOSunderanothername. Anyconstrained/rationalcandidatewouldneedALLoriginalcomplexcouplings,degeneraciesandexactdomainjustification; nobarefactorization/co-Choireferencecanreplaceit. AllS0/S1/OWN/HOLD/STOPoutsideS1/ZERO/nonblindhistory/SAME18/deadline2026-10-31T21:23:27Z/N4UNKNOWNhistoricalchildexitUNESTABLISHED/aux214STOPremain.

**END COMPLETE S1 ADDENDUM6 — UNRESTRICTEDPOLYNOMIALSOSNO-GO; ORIGINAL W4 STILL OPEN.**
