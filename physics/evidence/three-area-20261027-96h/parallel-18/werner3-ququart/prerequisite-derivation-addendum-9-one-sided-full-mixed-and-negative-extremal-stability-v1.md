# S1 addendum9 — globally one-sided FULLmixed stability and negative-extremal stability

OwnerPhysicsResearch96h-2/SAMEphysics-1. Actual `/bin/date` before writing **Tue Oct 27 15:36:43 PDT 2026**. **WRITTEN AUTHOR CANDIDATE UNREVIEWED**. InputsONLYreleasedS1definitionsandthecompleteddisplayeddefinition-onlyauthorproofs: addendum4R1floorstability andaddendum8wholefloorextremal/negative-spectralclass. Ordinaryexplicitfactsbelow. No selectedstate/control/parameter/spectrum/phase/overlap/boundary/threshold/magnitudeinstance/probe, no scientificinterpreter/CAS/program/calculator/enumeration/replay, nooldheldconsumer. Allquantitiesareactualinputfunctions, ALLvariableboundsvalidwithouta chosenregime; no originaloperatorWLOGasproduct.

This delivers a genuine strongerFULLmixedbridge thanaddendum4'stwo-errorbound, followedbyagloballyvalidstabilityestimateontheENTIREactualnegativeeigenspace. Neitherprovestheoriginalpositiveendpoint. Priorpapersremainimmutable; thislaterpaperisnotretroinsertedintotheirrequested/frozenreviewscopes. No novelty/SOTA/adoption/strongerverificationclaim.

## 1. ALL-pair one-sided mixed bounds

ForEVERYunit-HScomplexrank-oneT1,T2, defineactualdelta_i=q3(Ti)−m>=0, m=1/8. Then, for **BOTH i=1and i=2 separately**,

**`|B(T1,T2)| <= m+sqrt(48 delta_i)`.**                     (One)

HereBistheENTIREoriginalsesquilinearpartialtraceform, NOT anindividualtermorarealrestriction. Theboundusesoneactualterm'sexcessonlyandholdsforEVERYotherunitrank-oneterm; it isstrongerthanthepreviousboundwithSUMoftwoerrors. No assumedorthogonalityisneededfor(One).

**Proof.** Addendum4provesforEVERYactualT1thereexistsaunitfloor-attainerT10with `||T1−T10||HS<=sqrt(48delta1)`. Itscompleteclassis `T10=zeta p1⊗p2⊗p3`, eachp_jrank-oneorthogonalprojection, |zeta|1. TheLITERALoriginalsuperoperatorWcalhas

`Wcal(T10)=(zeta/8) R`, `R=⊗_j(2p_j−I)` SELFADJOINTUNITARY.

Thus `||Wcal(T10)||_op=1/8=m` asanACTUAL64-by-64operator. ThisoperatornormmustNOTbeconfusedwiththeHSsuperoperatornorm||Wcal||=1. ForANYunitrank-oneT2=|x2><y2|,

`|B(T10,T2)|=|<Wcal(T10),T2>HS|<=||Wcal(T10)||op=m`.

MeanwhilefullHSdualityandsuperoperatorunitaritygive

`|B(T1−T10,T2)|<=||T1−T10||HS ||T2||HS`.

Addthetwoineqalitiestoprove(One)fori1. Hermitiansymmetry `B(T2,T1)=bar(B(T1,T2))` provesi2. Thisusesoneandthesameoriginalmap/callerthroughout, withnoindependentoptimizationoftheoriginalmixedterm.

ConsequentlyforANYactualrank-twoC andANYitscomplexSVD `C=s1T1+s2T2`, foralltheSAMEactualdata and BOTH i,

**`q3(C)>=(s1−s2)²/8+s1²delta1+s2²delta2
                         −2s1s2 sqrt(48delta_i)`.**         (One-C)

ThisfollowsbyexactsesquilinearexpansionandReB>=−|B|, notbyclaimingtheinequalityerrorsarejointlyattainable. Rank0/1stayseparatelycovered. ItdoesNOTestablishthattheRHSisuniversallynonnegative. Asanautomaticderivedequality-casecorollaryifoneactualdeltavanishes, thecorrespondingRHSisnonnegative; thisisnotaselectedstate/controloraproduct-rayWLOGfortheoriginalproblem. No neighborhood/parameterwindowisdrawnfromit.

## 2. ALL-negative-eigenspace stability from its ACTUAL opnorm deficit

LetZbeANYunit-HSoperatorintheACTUALnegativeeigenspaceEminusofWcal. Set

`b=7/16`, `s=||Z||op`, `e=b−s²>=0`.

TheuniversalNS1boundfromaddendum8provesthiseisnonnegative; itisNOTafreeselectedmagnitude/spectrum. LetKbetheWHOLEunitsharpNS1extremalclassprovedthere:

`K={eta(4/sqrt7)Pminus(p1⊗p2⊗p3): |eta|=1,
                                      allrank1orthogonalp_j}`.

Then

**`thereexists Z0∈K with ||Z−Z0||HS²<=448 e`.**             (Neg-Stab)

No inverseoftheactualtopnorm/eigen-gapoccurs; theonlyfixednormalizingcoefficientispositiveb. Multiplicities/anyleadingSVDpairareallowed.

**Proof.** TakeANYleadingunitrank-oneSVDfunctionalTforZ, withformalphaseconvention `<Z,T>=s>=0`. ThisisforallZanordinarySVDphaseconvention, notanevaluatedphase/controltrial. Put `a=||Pminus T||HS²`. BecauseZ∈Eminus,

`s²<=a<=b`,

`delta(T)=q3(T)−1/8=2(b−a)<=2e`.

Addendum4thereforegivesanACTUALfloor-attainerT0with

`||T−T0||HS²<=48delta(T)<=96e`.

SincePminusisanorthogonalprojection,

`||sqrt(b)Z−Pminus T||HS²
  =b+a−2sqrt(b)s
  =(sqrt(b)−s)²+(a−s²)<=2e`.

Thelaststepuses0<=s<=sqrt(b), so `(sqrt(b)−s)²<=b−s²=e`, anda−s²<=e. Set `Z0=Pminus T0/sqrt(b)`, whichliesintheWHOLEclassKbyaddendum8. SplitZ−Z0attheACTUALintermediatePminusT/sqrt(b). Theelementarynormsuminequalitygives

`||Z−Z0||HS²
 <=(2/b)[ ||sqrt(b)Z−Pminus T||HS²
                         +||Pminus(T−T0)||HS² ]
 <=(2/b)(2e+96e)=448e`.

Theexact448is196dividedby7/16intheuniversalsymbolicinequality; no selectedvalue/instance, numericaloptimizationorprobeisused.

## 3. TWO simultaneously valid ALL-Z joint singular-energy estimates

Retain `Phi2(Z)=sigma1(Z)²+sigma2(Z)²`. TheunitextremizersZ0inKALLhavePhi2(Z0)=25/56bytheprovedflat-tailspectrum. Thequantitysqrt(Phi2)isanorm: itsdualityrepresentationis `max_(rankC<=2,||C||HS=1)|<Z,C>|`, sothetriangleinequalityandHSdominationfollowdirectly. Therefore(Neg-Stab)gives

**`sqrt(Phi2(Z)) <= sqrt(25/56)+sqrt(448e)`.**               (Joint-1)

Simultaneouslytheorderedactualsingularvaluesgive

**`Phi2(Z)<=2sigma1(Z)²=7/8−2e`.**                          (Joint-2)

ALLthesameZhasthesameACTUALdeficiteinBOTHinequalities. No independentparameterassignment, spectralregion/thresholdrootortrialcomparisonisintroduced. Thecoefficientsarederivedfixedproblemconstants, notpickedcontrolmagnitudes. Boundsmaybeloose; neitherreplacesfullactualfeasibilitybyafreespectrum.

Thesegloballyquantifywhytheone-singularsharpclasscannotserveasthewholeoriginaltwo-singularproblem. TheydoNOTestablishPhi2<=1/2forallactualZ; thatremainsEXACTunpaidNS2. Itwouldbeincorrecttosilentlyoptimizeformalefreelyandpresentitaseitheranactualcounterexampleororiginalpositivity.

## 4. Named inputs, actual gain and next gap

Newgenuinecouplinginput:(One)ALL-pairone-sidedFULLmixedstability, (One-C)SAMEoriginalrank-twooperatorlowerbounds, and(Neg-Stab)/(Joint-1)/(Joint-2)GLOBALactualnegative-spaceextremalstability/jointsingular-energycoupling. AllcomeFROMfaithfuloriginaldefinitions, noselectedtestfamily, andretaincomplexphases/degenerateSVDchoices. Theseareordinaryclassicalproofs; novelty/SOTAnotassessed, originalsignnotreached.

ImportsarethepreviousfullR1floorstability/classproof, literalWcal(T0)=scaledACTUALunitary, HS/spectralnormdualityforrank-oneoperators, orthogonalprojectioncontraction, finitecomplexSVD/phaseconvention, elementarynorminequalities, andthealreadyprovedrank-twoHSdualitynorm. EachsourceauthorpaperUNREVIEWED; no independentverification/parentread/adoptionisclaimed. Source-bookequivalence/formal-human-family-executable-kernel-noveltygatesremainOPEN.

Exactnextscientificgap: needfullactualmixedMSorNS2dominationwithstrongerenoughcouplingtoyieldthepositiveendpoint, oranACTUALnegativeoperatorviafaithfulconstructor. One-sidederrorstillhasnosignendpointguarantee; spectraldeficitisnotafreeinput. Do notrebrandthesequantitativepartialboundsascompletionoraddselectedparameters/protectedguidance. No all-routeexhaustion/earlypark/newGO.

Same18/S0S1/NEWOWN/oldroundCLOSED_FROZEN/STOPoutsideS1/HOLDv2/ALLZEROHELD/permanentprocesshistory/nonblindpriorauthorship/N4UNKNOWNhistoricalchildexitUNESTABLISHED/aux214STOP/deadline2026-10-31T21:23:27Zremain.

**END COMPLETE S1 ADDENDUM9 — GLOBAL ONE-SIDEDMIXED/NEGATIVE-EXTREMALSTABILITY; ORIGINAL W4 STILL OPEN.**
