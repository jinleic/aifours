# S1 addendum3 — universal actual-rank-two lower bound and strict nonattainment

Owner **PhysicsResearch96h-2**, SAMEphysics-1. Actual `/bin/date` before writing: **Tue Oct 27 14:57:44 PDT2026**. **WRITTEN AUTHOR CANDIDATE ONLY**, not peer-reviewed/parent-adopted/formal/kernel/human/family/executable/novelty-cleared. No scientific interpreter/calculator/CAS/program, selected operator/state/parameter/boundary/decimal probe, enumeration/replay or external model. This is an ALL-variable theorem for the ORIGINAL literalq3 and ACTUALrank<=2C, not a rank-only co-Choi surrogate or a separately optimized compression.

Inputs: ONLY the releasedS1 literalq3/trace/rank conventions, ordinary explicitly used finite-dimensional facts, and this owner's displayed definition-only derivations. Immutable initialpacket SHA256 `09b902fa35d379b21c21c5bb83145e0ae336fec986a9ef12eb719f3408e3cbe6`; addendum1 `5f711787a2e4a8b2a9aa08a68c5183f7aae26f55273409fe0e766bc0dc3fcf92`. No oldv4–v25/raw/sign/metric/Jensen/Kirchhoff/selectedv18/heldL1–L6/S242/C889 or ZERO consumer supplies a proof or method. Prior exposure is not erased or certified noninfluential.

## 1. Exact theorem and original-problem boundary

Let ||C||_* denote the nuclear norm (sum of its singular values), not an extra original restriction. For EVERYcomplexC:H→H of rank<=2, withH=(C^4)^tensor3 and the UNNORMALIZEDpartialtraces inS2,

**`q3(C) >= ||C||_HS^2 − (7/8)||C||_*^2
              >= −(3/4)||C||_HS^2`.**                       (LB)

Moreover for EVERYnonzero suchC,

**`q3(C) > −(3/4)||C||_HS^2`.**                              (Strict)

There consequently exists a constant epsilon>0, independentofC, suchthat

`q3(C) >= (−3/4+epsilon)||C||_HS^2`                          (Gap)

for ALLrank<=2C. No explicitepsilon is provided, and neitheritsvalue nor nonnegativityof−3/4+epsilon is asserted. No parameter/state was sampled toobtaintheseexactrationalconstants or thepositiveuniformgap.

These are universal lower bounds/strict nonattainment, **NOTq3>=0** andNOTanactualnegativeoperator. OriginalW4remainsOPEN. Classicalmethodancestryandstrictdifferencefromexistingliterature/baselines areunverified; noSOTA/noveltyoradoptionclaim.

## 2. The original quadratic operator is a self-adjoint involution

For each localpair, `E_j=|Omega_j><Omega_j|` withUNNORMALIZEDOmega_j=Σ_(k=1)^4 |kk>. ThusE_j^2=4E_j, bytheinnerproductofOmega_j withitself. The source-defined localfactor satisfies

`(I−E_j/2)^2=I−E_j+E_j^2/4=I`.

Factors act ondisjointpairedsites andcommute. Therefore

`W=⊗_(j=1)^3(I−E_j/2)` satisfies `W†=W`, `W^2=I`.

Inparticular `−I<=W<=I` and

`M=I−W>=0`.

The faithful traceidentity fromtheinitialpacket is `q3(C)=<vecC,WvecC>` for ALLC, includingALLmixedcontractions. Consequently

`q3(C)=||C||_HS^2−||M^1/2 vecC||^2`.                        (M)

The square root is anordinaryPSD square root; no inverse orsingularboundaryformula isused. Thedirect boundW>=−I alonewouldgive−||C||_HS². The actualrank restriction plusrank-onegeometrystrengthensthatbound below.

## 3. FULLsame-operator singular-column coupling, not independent optimizations

Use theordinaryfinite-dimensionalcomplexsingularvaluedecomposition ONLYas an exactrepresentation ofthe GIVENoperatorC. For itsr<=2nonzerosingularvalues write

`C=Σ_(a=1)^r s_a T_a`,  `s_a>0`,

`T_a=|x_a><y_a|`, withorthonormal{x_a} and{y_a}.

Thenf_a=vec(T_a)=x_a⊗bar(y_a) areorthonormal,

`||C||_HS²=Σ s_a²`, `||C||_*=Σ s_a`.

Rank0 isC0andallinequalitiesgive0; rank1usesonesummand. No nonzero column isdivided by a vanishing singularvalue andnostate/instanceischosen. This is theuniversalSVDproof forEVERYoriginaloperator, not anavoider/feasibilitymodel.

The initialpacket proved for EVERYunitrank-oneT that

`a(T):=q3(T)=<x⊗y,P(x⊗y)> >= m=1/8`,

where `P=⊗(I−F_j/2)>=I/8`. Alsoa(T)<=1fromW<=I. Put

`g_a=M^1/2 f_a`, `e_a=||g_a||²=1−a(T_a)`,

so0<=e_a<=7/8. The exactSAMEoperatorcoupling in(M) is

`q3(C)=Σ s_a²−||Σ s_a g_a||²`.                              (Coupled)

No g_a can be chosenindependently ofitsactualT_a/W. ThetriangleinequalityfollowedbytheprovedR1margin gives

`||Σ s_a g_a|| <= Σ s_a sqrt(e_a)
                 <= sqrt(7/8) Σ s_a`.

Thus the moredata-retainingALL-variableestimateis

`q3(C) >= ||C||_HS²−(Σ s_a sqrt(1−q3(T_a)))²`,              (Data-LB)

and thefirstinequalityof(LB) follows. Forr<=2,

`(Σ s_a)²<=2Σ s_a²`,

by `(s1−s2)²>=0` (witha missingsecondvaluezero). This gives thesecondinequalityof(LB). It is a fullcoupledestimate, not separateincompatiblemaximizations: everyCauchy/triangletermbelongs tooneactualSVDofoneactualC.

No thresholdregionorchosen singularvalueratio isderived/tested. TheboundappliestoALLlegalC atonce. It doesnot asserttheseinequalitiesarejointlyattainable; theactualjointcoupling preventsattainmentofthelastbound, asprovednext.

## 4. Complete equality class of the rank-one floor

**Lemma R1-EQ.** Letx,y beunitvectors inH. Then

`q3(|x><y|)=1/8`

iff thereareunitlocalvectorsh1,h2,h3 andphaseswith

`x=h1⊗h2⊗h3` up tophase, and `y` is aphase multipleofx.

This is an ALL-variable equalityclassification ofthe givenliteralform, not a selectedproductstatecontrol or a product-rayWLOG forranktwo.

**Proof.** EachlocalswapF_j hasorthogonal±1eigenspaces; thefactorI−F_j/2 hascorrespondingeigenvalues1/2and3/2. Thejointorthogonalprojectorsfor thethreecommutingswapsresolveP intoeigenspaceswithcoefficients `(1/8)3^k`, wherek countslocalantisymmetricsites. ItsMINIMUMeigenspace at1/8 isexactlytheintersectionofALLthree localsymmetricspaces. EqualityoftheR1quadraticform withtheminimumthereforeforces

`F_j(x⊗y)=x⊗y` for EVERYsitej.                              (sym)

This uses thespectraldecompositionofafixedoperator, notaprogram/case-tableorselectedeigentrial.

Let rho_j^x andrho_j^y betheactualsingle-sitemarginaldensityoperators oftheunitvectors. Matrixunitsoftheswapgive

`<x⊗y,F_j(x⊗y)>=Tr(rho_j^x rho_j^y)`.

By(sym)thisis1. ForANYpositiveunittracerho,sigma,

`Tr(rho sigma)<=sqrt(Tr(rho²)Tr(sigma²))<=1`,

usingHS Cauchy–Schwarz andthe nonnegativeeigenvalues ofunittrace. Equality1 forcesBOTHpurities1, so bothrankone, andCS equalitywiththeirunittracesmakesthe SAMErankoneprojection. Thus forEVERYj thetwomarginalscoincideandarepure.

A pureglobalvectorwithapuresingle-sitemarginalfactorizesatthatsite: itsSchmidtdecompositionhasone nonzeroSchmidtcoefficient (or equivalentlyorthogonal-complementcomponentshavenormzero). Applyingthistoeachsitegivesfullyproductxandfullyproductywiththe SAMEthree localrays. Henceyisaglobalphase multipleofx. Converselythosesame-local-rayproductvectors satisfyALL(sym), givingtheminimum1/8. QED.

No rank-twooperator was assumedtohave this form; thislemma isusedONLYfor a necessaryequalitycase intheuniversalbound.

## 5. Actual mixed correlation of TWO floor-attaining rank-one terms

LetT1,T2 be ANYtwo unitrank-oneoperatorsattainingR1'sminimum. Bythelemmawrite

`T_a=e^(i theta_a) ⊗_(j=1)^3 pi_(a,j)`,

wherepi_(a,j)=|h_(a,j)><h_(a,j)| areunitrankoneprojections. Theordinarysesquilinearpolarizationofq3is

`B(C,D)=Σ_(S⊂{1,2,3})(−1/2)^|S|
          <Tr_S C,Tr_S D>_HS =<vecC,WvecD>`.

TensorfactorizationoftheseparticularEQUALITYterms—notarestrictiononoriginalC—givesEXACTLY

`B(T1,T2)=e^(i(theta2−theta1))
           product_(j=1)^3 [Tr(pi_(1,j)pi_(2,j))−1/2]`.      (Floor-mix)

Eachrealoverlapliesin[0,1] bytheunitvectorCauchy–Schwarz inequality; henceeachbrackethasabsolutevalue<=1/2. ThusforALLsuchterms

**`|B(T1,T2)| <= 1/8`.**                                    (Floor-bound)

This is derivedover the ENTIRErank-oneequalityclasswithoutselectinganypair, overlapsorphases. No controlvalueorexampleis evaluated. Inparticular it remainsvalidfortheorthonormalSVDterms considerednext.

## 6. Strict nonattainment of −3/4 on EVERY nonzero legal C

Assumeequalityinthelast(LB) for anonzeroC. Rank1cannotattainitbecauseitsq3>=1/8||C||². Thusr2andthelastsingularvalueinequalitymustbeequality, sos1=s2>0.

Everyprecedingupperboundon `||s1g1+s2g2||` mustalsoattainitsmaximum. Sincebothcoefficientsarepositive,thisforces

`e1=e2=7/8`, hence`q3(T1)=q3(T2)=1/8`,

andtriangleequalityforcesg1,g2parallelwiththe samephase. Therefore

`|<g1,g2>|=7/8`.

But thef1,f2areorthonormalSVDvectors, so

`<g1,g2>=<f1,(I−W)f2>=−<f1,Wf2>=−B(T1,T2)`.

The twoTtermsarenowinthe COMPLETEfloor-equalityclass; (Floor-bound) givesabsolutevalue<=1/8, contradicting7/8. This proves(Strict) for EVERYnonzerolegalC. No assumedindependenceofextremalconditionsornewchosenspectralinstanceisused: theargumentexcludesALLpotentialequalitycases.

The set `S={C:rankC<=2,||C||_HS=1}` is compact in the FINITE-dimensional Euclidean operator space: the unit HS sphere is compact and rank<=2 is closed (all three-by-three minors vanish). q3 is a continuous quadratic polynomial in real/imaginary matrix entries. It attains a minimum on S; by(Strict) that minimum exceeds−3/4. Denote its positive gap by epsilon. Homogeneity then proves(Gap), including C0. This is existence of a UNIFORM strict lower bound, not a computed epsilon, proof it crosses zero or a closed target value.

## 7. What changed and exact next unpaid step

Relativeonlytothepermittedliteraldefinitions, this delivers a genuine universalboundon ORIGINALrank<=2complexC, strictnonattainment, and anunevaluatedpositiveuniformgap. It is notmerelyrankfactorization/encoding, not asufficientco-Choiformcounterexample, andnot a positivityclaimfromseparatecompressions. It usesALLactualmixedSVDcorrelations; theincompatibleextremizersarerigorouslyexcluded.

It remains farfromtheoriginalnonnegativeendpoint: theboundmaystillbenegative, andepsilon isnotestimated. NoactualnegativeCisgiven. Novelty/SOTA/strictincrementoverhistoricalknownboundsareNOTaudited/adopted. MethodinputsareordinarySVD, thedisplayedmatrixunitidentities/spectralprojectionsofW/P, HS Cauchy–Schwarz/triangleinequality, elementaryrank-oneequalitycase, finite-dimensionalcompactness/continuity. Allareexplicitlyused; noextraoldprooforsourcebodyenters.

A furthergenuinelyadmittedstep would need aquantitative SAME-inputcouplingbetweenR1diagonalexcessesandtheoff-diagonalcorrelation, or adirectuniversalR-Pi factor1bound. Near-equalitymustnotbefilled by aselectedstate/boundarysampleorindependentlyassignedoverlaptuple. Thispacketonlyprovesthecompleteequalitycase/strictgap, notsuchquantitativedomination. TheuniversalW4sign/actualnegativealternative, NRsource-equivalenceandallpeer-parent/strongergatesremainOPEN.

S0/S1/newdeadline2026-10-31T21:23:27Z/scientificHOLDv2/N4UNKNOWN historicalchildexitUNESTABLISHED/aux214STOP/alloldSTOPoutsideS1/ZEROconsumerboundariesandnonblindpriorauthorshippersist. No oldfilechanged; no strongerverificationororiginalcompletion.

**END COMPLETE S1 ADDENDUM3 — UNIVERSALACTUAL-OPERATOR LOWER BOUND; ORIGINAL W4 STILL OPEN.**
