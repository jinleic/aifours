# S1 addendum8 — exact negative-spectral caller and whole sharp one-singular-value extremal class

OwnerPhysicsResearch96h-2/SAMEphysics-1. Actual `/bin/date` before writing **Tue Oct 27 15:30:41 PDT 2026**. **WRITTEN AUTHOR CANDIDATE UNREVIEWED**. InputsONLYreleasedS1literaldefinitions, displayeddefinition-onlyreflection/R1floorproofsandnamedordinaryfinite-dimensionalfacts. No oldsource/guideconsumer, selectedstate/control/spectrum/parameter/overlap/boundary/magnitude/decimalprobe, scientificcalculator/interpreter/CAS/program/enumeration/replay. ALLvariablesbelowareuniversallyquantified; equalityclassesarederivedWHOLEclasses, not sampled/chosenstates orproduct-rayWLOGfororiginalranktwo. No earlypark/newGO/adoption/noveltyclaim.

This changes the blockedcouplingrepresentation to the ACTUALnegativeeigenspaceof the ORIGINALquadraticoperator, not a separate referencecompression/co-Choirankproxy. The exactcallerbyitselfis interface reproduction, NOTscientificcompletion. Theadditionalprovedglobaloperator-normboundandcompleteextremal-tailclassificationgive a concrete saturation obstruction for the new caller; the neededtwo-singular-valuedominationremainsOPEN.

## 1. Exact fixed negative linear space from the original partial traces

OnB(H), H=(C^4)^tensor3, retain

`Wcal(C)=Σ_(S⊂{1,2,3})(−1/2)^|S| I_S⊗Tr_S C`,

`q3(C)=<C,Wcal(C)>_HS`, `Wcal†=Wcal`, `Wcal²=id`.

ThelocalHSorthogonaltraceprojectionsare

`T_j(C)=(1/4)I_j⊗Tr_j C`,

so `Wcal=product_j(id−2T_j)`. ThisfaithfullykeepsALLoriginalpartialtraces, complexentriesandsiteinsertions. Define

`Pminus=(id−Wcal)/2`,

`Eminus={Z:Wcal(Z)=−Z}=range(Pminus)`.

PminusistheACTUALHSorthogonalprojection, NOT anindependentpositiveblockchosenforconvenience. Itslinearspaceisnonzero (theliteralproductofonecanonicalOmega-projectionandtwoorthogonalcomplementsinvecspaceisnonzeroandhaseigenvalue−1). Noactualrank-twoexampleisbeingofferedfromthatfullspectralspace.

ForEVERYactualC,

**`q3(C)=||C||_HS²−2||Pminus(C)||_HS²`.**                   (Projection)

## 2. FULL original rank-two problem iff two singular values of EVERY actual negative eigenoperator

ForZ let itscomplexmatrixsingularvaluesbe `sigma1(Z)>=sigma2(Z)>=...>=0`, INCLUDINGZEROS. Define

`Phi2(Z)=sigma1(Z)²+sigma2(Z)²` forunit-HSZ,

`beta2=max_(Z∈Eminus,||Z||HS=1) Phi2(Z)`.

NoZorbetavalueisselected/evaluated. Allmaximaexistbyfinite-dimensionalcompactness/continuity. Then

**`min_(rankC<=2,||C||HS=1) q3(C)=1−2 beta2`.**              (Exact)

Consequentlyoriginaluniversalq3>=0foractualrank<=2iff

**`sigma1(Z)²+sigma2(Z)² <= (1/2)||Z||HS²
                         for EVERY Z∈Eminus`.**            (NS2)

ThesearetheFULLactualcallerquantifiers; source/originalrank/complexnormalizationisnotdropped. Inparticular mereabsenceofrank-twoeigenoperatorsinEminus isNOT(NS2).

**Proof.** ForEVERYfixedZ,theordinaryrank-twoHSdualityidentityis

`max_(rankC<=2,||C||HS=1) |<Z,C>|²
                            =sigma1(Z)²+sigma2(Z)²`.

IndeedifrangeCiscontainedinaplaneU, `|<Z,C>|<=||P_U Z||HS`; diagonalizingZZ†gives `Tr(P_U ZZ†)<=sigma1²+sigma2²` becauseitsdiagonalprojectionweightsliein[0,1]andhavesum<=2. Normalizinga two-termSVDtruncationofZattainstheboundwhenZnonzero. Allsingularvalue-tiechoicesareallowed; no chosenstateinstanceisneeded.

Orthogonalprojectiondualitygives `||Pminus C||=max_(Z∈Eminus,||Z||=1)|<Z,C>|`. SwappingthetwoMAXIMA overtheSAMEjointcompactdomainthereforegivesmax_rank2||Pminus C||²=beta2. Insert(Projection). No separateincompatibleoptimizationsordifferentoperatorsexchangedasthoughjointlyattainable.

**Explicitbothdirectionsforactualcounterobjects.** IfanACTUALunitZ∈EminuswithPhi2(Z)>1/2wereprovided, letZ_2beANYtwo-leading-termcomplexSVDtruncationandsetC=Z_2/||Z_2||HS. ThisisACTUALrank<=2, and `<Z,C>=sqrt(Phi2(Z))` up toharmlessglobalphase. Then||PminusC||²>=Phi2(Z)>1/2, soq3(C)<0. ItwouldnecessarilyberankEXACT2bytheR1positivefloor. ThisisconditionalconstructorONLY—nosuchZisdelivered.

ConverselyfromanACTUALunitrank<=2Cwithq3(C)<0,setZ=PminusC/||PminusC||. ItisACTUALunitnegativeeigenoperatorandPhi2(Z)>=|<Z,C>|²=||PminusC||²>1/2. Thedenominatorisnonzeroasprovedbyq3(C)<0, notassumedacrossaboundary. No route-onlynegativedirectionissubstitutedforC.

## 3. A SHARP universal single-singular-value bound on the WHOLE Eminus

ForEVERYZ∈Eminus,

**`sigma1(Z)² <= (7/16)||Z||HS²`.**                         (NS1)

ThecoefficientisSHARP, andtheWHOLEnonzeroequalityclasswillbedeterminedbelow. ThiscoefficientisderivedfromtheoriginalR1minimum, not a chosenbound/parameterprobe.

**Proof.** NormalizeZonlybyhomogeneity. ForEVERYunitrank-oneT,

`|<Z,T>|=|<Z,Pminus T>|<=||Pminus T||`,

andby(Projection)plusR1floorq3(T)>=1/8,

`||Pminus T||²=(1−q3(T))/2<=7/16`.

MaximizingoverALLunitrank-oneTgives(NS1), theordinaryoperatornormduality. R1floorattainersalreadyexistandwerecompletelyclassifiedinaddendum3: EVERYsuchunitTisaphasemultipleofaproductrank-oneorthogonalprojection. ForANYoneofthem, normalizationofPminusTattainstheupperboundbyHSduality/Cauchy–Schwarz. Thisisanentirederivedclass, notanevaluatedspecialteststate.

## 4. WHOLE equality class and exact flat singular tail — no selected pair

ForANYunit-HSnonzeroZ∈Eminus,saturationof(NS1)holdsexactlywhen

**`Z=eta (4/sqrt(7)) Pminus(p)`, `|eta|=1`,
  `p=p1⊗p2⊗p3`, eachp_j ANYrank-oneorthogonalprojection.**   (Class)

**Necessity.** Choosealeadingrank-oneSVDfunctionalTforZ (universalSVDexistence, nosampledinput). EqualityinthechainaboveforcesBOTHq3(T)=1/8andHS-CauchyequalityZproportionaltoPminusT. TheCOMPLETEderivedR1floorclassmakesTphase timespoftheshape(Class). Itsprojectionnorm²is7/16; normalizinggivesexactly(Class). Sufficiencyfollowsfromthesameoverlapequality; theexplicitwhole-tailcalculationbelowalsochecksit.

ForALLsuchp, put

`R=⊗_(j=1)^3(2p_j−I)`.

Ris aSELFADJOINTUNITARY, andRp=pR=p. TheLITERALoriginalsuperoperatorgives

`Wcal(p)=⊗_j(p_j−I/2)=R/8`,

`Pminus(p)=(1/2)p−(1/16)R`.

Thusontheone-dimensionalrangep,thisoperatorhaseigenvalue7/16; ontheENTIREorthogonalcomplementit is−R/16, ascaledunitary. ThereforeitsWHOLEsingularspectrumis

`7/16 once; 1/16 on ALL remaining dimH−1=63 dimensions`.

Thisisafulloperatoridentity/classification, not a basis-stateenumerationorachosenparameterexample. ItsHSnorm²is `(49+63)/256=7/16`, consistentwithprojectionduality. Normalizingas(Class)gives

`sigma1(Z)²=7/16`,

`ALL remaining sigma_j(Z)²=1/112`.

Inparticular for EVERYsharp(NS1)extremizer,

**`Phi2(Z)=7/16+1/112=25/56 < 1/2`.**                       (Tail)

Hencewholeone-singular-extremizerssatisfytherequiredtwo-singularsigncriterion, but **NOproduct-rayWLOG**isdrawnforarbitraryZ∈EminusororiginalC. ThisdoesNOTshowthatPhi2'smaximizerliesin(Class), nor thatallotherZobey(NS2), nor thattheirPhi2valuesaredeterminedbytheirfirstsingularvalue. Thereisnoclaimaboutaneighborhood/parameterregion/thresholdorselectedprobecomparison.

Thecrudeuseof(NS1)twiceonlygivesPhi2<=7/8, not1/2. Theflat-tailclassificationrigorouslypreventsattaining7/8; compactnessgivesastrictuniformimprovement, consistentwiththeearlieractualrank-twobound>−3/4. ThisisanalternativegeometricviewoftheSAMEprovedgap, **not independentverificationor anewsignresult**.

## 5. Exact gain and next unpaid coupled premise

Delivered: FULLexactoriginalnegative-spectralcaller/bothactualcounterobjectdirections; theSHARPglobalNS1bound; WHOLEequalityclassandflat-tailidentity(Tail). Thecalleritselfisinterface reproduction; thecompleteextremalgeometryisasaturationobstruction, nottargetcompletion. The ALL-Ztwo-singularbound(NS2)remainsUNPROVED. Itwouldbeincorrecttoreplacerank-twoq3byajust-rank/just-operatornormbound, aco-Choiform, independentlyassignedsingularvalues, anabstractspaceinsteadofEminus, ortheproductextremalclassalone.

Nextvaluableadmittedstepis agenuinejointsingular-valuecoercivity/majorizationestimateonTHISFULLfixedEminus; no selectedZ,spectrumorcontrolprobe, nooldheldsource. Classicalprojectionduality/KyFanvariationalreasoningareprior, notnewmethod; novelty/SOTA/strictliteratureincrementnotaudited. Scopehonesty: noactualnegativeC, noW4positivity, noexhaustionorretrospectiveadoption.

Ordinaryimportsproved/usedabove: exactmatrixpartialtraceadjoint/HSreflection, orthogonalprojectionduality, finitecomplexSVDandtwosingular-energyvariationalboundwithprojectionweightproof, compactness/continuity, Cauchy–Schwarzequality, andthepreviousWHOLE R1floorclassificationfromtheliteralPswapproof. AuthorpapersareUNREVIEWED; fullsource/body/applicationtrustreviewstillrequired. Noformal/human/cross-family/executable/kernel/noveltygateorsource-bookequivalencecertificateisconferred.

AllS0/S1/SAME18/NEWOWN/oldroundCLOSED_FROZEN/STOPoutsideS1/HOLDv2/ALLZEROHELD/permanentprocesshistory/nonblindpriorauthorship/N4UNKNOWNhistoricalchildexitUNESTABLISHED/aux214STOP/deadline2026-10-31T21:23:27Z/noearlyparkremain.

**END COMPLETE S1 ADDENDUM8 — EXACT FULLSPECTRALCALLER AND SHARP EXTREMAL GEOMETRY; ORIGINAL W4 STILL OPEN.**
