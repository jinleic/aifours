# RQLS10 v77 — COMPLETEALLlocal4-dimensionalframe classification and the sparsebranch's actualprojectioncircuits

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW complete manuscript: **Mon Oct 26 17:10:48 PDT 2026**. AUTHOR-WRITTEN CANDIDATE; exact unitaryzero/phasegauge/modulus/graph-circuit/commonprojection proof only, NOT machine/kernel checked. No scientific Eval/interpreter/arithmetic/CAS/program/enumeration/solver/replay/newGO/private approximate scout/backconversion or chosenphysicalparameter/state/control/probe.

**SEPARATEFUTUREONLY:** Main'swholecandidatev17ASOFS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, itsindex/proofs and151v2/S55freeze remainUNCHANGED. This NEWsourceisOUTSIDEtheirgateandmayenteronlyaNEWfuturemanifest. No automaticreviewadmission/read/adoption.

## 1. ExactWHOLElocalframeproblem, not a realstate/control assumption

TakeANYtwo ONBs {e_1,...,e_4} and{f_1,...,f_4} ofC4 suchthat

    <e_i,f_i>=0 forEVERYi,
    NOe_i ray equals ANYf_j ray.

TheirunitarytransitionW hasdiagonalZERO and NOentryofmodulus1. This is exactlytheactualTWOrowframecondition atEVERYvertexofthev76graph: incidentedgei hasrank2planeP_i=span(e_i,f_i); the twoactualrowONBsarethe e_i andf_i.

Weclassify ALLsuchW, includingALLadditionalzero patterns. Allowedlocalgauge is independentphasechangesofbasisvectors and simultaneouspermutationofmatchedindices; it preservesdiagonalzerosandallprojectiverays. It is NOTonecommonphysicalgaugeforALLvertices, nor a globalrealness/phasealphabetansatz for theoriginalarray.

## 2. COMPLETEzeropatternsplit: fullTWELVE or twofull2-by-2blocks

No row/columnofW canhavetwoorthreeofitsOFF-diagonalentriesZERO: togetherwiththediagonalzero itwouldhave atmostONEunitentryofmodulus1, prohibited. Hence everyrow/columnhas2or3nonzeros.

IfthereisANYadditionalzero, simultaneouslypermute itsmatchedindices to W_12=0. Thenrow1hasBOTHW_13,W_14nonzero. Orthogonalityofrow1 withrow3has ONLYthecolumn4termleft, soW_34=0; similarlyW_43=0. Rows3/4mustnowhave BOTHcolumns1/2nonzero, andform anONB ofthat2-space. Column1norm thenforcesW_21=0. Row2hasBOTHcolumns3/4nonzero.

Thus the ENTIREadditional-zero branch is exactly

    W=[0_2  U]
      [ V  0_2],                               (SPARSE)

whereU,V areARBITRARY2-by-2unitaries withALLfourentriesnonzero. ALLphases/anglesofBOTHblocks areindependent. Conversely every(SPARSE)hasalltherequiredlocalproperties. Thereisnothirdzero-patterncase, andnogenericnonzeroassumption isused.

## 3. ENTIREfullsupportbranch: exactprojectivecanonicalform with ALLthreepositiveweights

NowallTWELVEoff-diagonalentriesarenonzero. Firstconsider theirpositiveMODULI. Put

    |W_12|=a, |W_13|=b, |W_14|=c,    a,b,c>0,
    a^2+b^2+c^2=1,
    d=|W_21|.

Eachpair ofdifferentrows overlapsinEXACTLYTWOcoordinates, so equalityofthetwotermmoduli gives

    b|W_23|=c|W_24|,
    a|W_32|=c|W_34|,
    a|W_42|=b|W_43|,
    d|W_31|=|W_24||W_34|,
    d|W_41|=|W_23||W_43|,
    |W_31||W_41|=|W_32||W_42|.

Allfactorsarepositive inTHISbranch, so substitutionsgive|W_24|/d=b/a and|W_23|/d=c/a. Row2normalizationthenforcesd=a. Substitutingbackandnormalizingtheremainingrows gives the FULLmodulustable

    [0 a b c]
    [a 0 c b]
    [b c 0 a]
    [c b a 0].                                  (MOD)

For completeness, afterd=a/write|W_34|=t, the displayedrelations give|W_31|=b*t/a,|W_32|=c*t/a; row3normgives t=a. Theotherrowthenfollowslikewise. No endpointwithzero wasdividedout; ALLsuchendpointsbelongto the SEPARATEcomplete(SPARSE)branch.

Dephasefirstrowandfirstcolumnpositive. Write thephaseofW_23as tau,|tau|=1. TheSIXtwo-termroworthogonalityequalitiesgiveexactly

    W_24=-b*tau, W_32=-c*tau, W_34=a*tau,
    W_42=b*tau,  W_43=-a*tau.

ThereisNOremainingindependentphase: row1withrow2/3/4firstfixesthreeoppositesigns; row2withrow3/4fixes thetworelativephases; row3withrow4isthenconsistent. Aremaininglocalrow/colphasegauge preserves thepositivefirstrow/column andsends tau to1: takeallrows2-4withphase1, column1phase1, row1phase tau, andcolumns2-4phase tau^-1.

Consequently EVERYfullsupportW is locallyprojectivelyequivalent to

    [0  a  b  c]
    [a  0  c -b]
    [b -c  0  a]
    [c  b -a  0].                               (DENSE)

Conversely(DENSE)isREALorthogonalforallpositivea,b,cwithsquaredsum1, bytheSAMEprintedtwo-termcancellationsandrownorms. This is anALL-variablecanonicalform, not a chosenrealstateor a particularconferencecontrol. Thelocalgauge cannotbe silentlyappliedsimultaneouslytoALLvertexframes/physicalrays.

## 4. Exactprojectionmeaning: sparsecasehas ONEuniquecomplementpairing

For distincti,j,

    tr(P_i P_j)=|W_ij|^2+|W_ji|^2.

In(DENSE) this gives

    tr(P1P2)=tr(P3P4)=2a^2,
    tr(P1P3)=tr(P2P4)=2b^2,
    tr(P1P4)=tr(P2P3)=2c^2.

ALLarestrictlybetween0and2. Thus NOtwoincidentedgeplanesareorthogonal/complementary, andNOtwoareequal.

In(SPARSE), P1 isorthogonaltoP2andP3orthogonaltoP4; sinceeachisrank2inC4,

    P2=I-P1,       P4=I-P3.

AllOTHERpairtracesarestrictlypositiveandstrictlybelow2 becauseBOTHU,VhaveALLentriesnonzeroandnoneofmodulus1. Hence theseare the ONLYcomplementarypairs: theedgepairingis UNIQUEandDERIVEDfromtheactualframes, not an arbitraryEulerianpairingimposedWLOG.

## 5. IfEVERYvertexissparse, its uniqueedgepairingsdefine ACTUALprojectioncircuits

NowuseENTIREv76graphG: connectedloopless4-regularmultigraphonfivevertices, ALLactualsectorraysdistinct. Suppose EVERYlocalvertextransitionliesin(SPARSE). At eachvertexitsUNIQUEcomplementpairingpairsitsFOURincidentedgesintotwopairs. Followinganedgeandthenitsactualpartner atthenextvertexdecomposestheTENedgecolumnsintocircuits; parallel-edge2-circuitsareallowed. Initiallythisis a combinatorialcircuitdecomposition, WITHOUTassumingvertex-simplicity.

Acrossanactualedge e={u,v}, v76givesP_(v,e)=I-P_(u,e). Passingfrome toitslocalpartnerf atv givesP_(v,f)=I-P_(v,e)=P_(u,e). Thus TWOsuccessivecomplementscancel. TheendpointplanesalongtheWHOLEcircuitareoneFIXEDrank2projectionP_Coritscomplement, withsignsgivenbythetraversal. This is anactualalgebraicpropagation, not a computedgraphwalk or a chosencircuitorientation.

Theactualoperatorpropagation nowFORCESvertex-simplicity. IfONEcircuit visitedBOTHlocalpairs atthesamevertex, allFOURlocaledgeplanes wouldbeP_CorI-P_C. Somecross-pairplanes wouldthenbeequalorcomplementary, contrarytosection4'sstrictcross-pairtracesbetween0and2. Hence everyactualcircuit isvertex-simple, oflength2,3,4or5; this is DERIVED, not assumed.

Therearetenedges, so at leastTWOcircuits. IfthereareEXACTLYTWO, bothhavelength5andvisitALLfivevertices: theactualgraph is theirunionastwoedge-disjointHamiltoncycles, withALLpossibleparallel-edgeplacementsretained. Eachvertexusesonepairfromeachcycle. No freelychosenHamiltondecomposition isbeingimposedontheoriginalarray.

If thereisONLYONEcircuit, ALLfortyE4sectorrays lieentirelyinrangeP_CoritsorthogonalcomplementinsideH4. ExtendP_CbyZEROonthephysicalE6complement. ItthencommuteswithALL100originalrayprojectors: the40E4raysareitseigenvectorsandtheother60raysareannihilated. It is a TRUErank2commonprojection, preciselytheliteralhypothesisofv15'sunrestricted<=86rayceiling.

Therefore NOoriginalmaximal1-RQLS10 inthisENTIREall-sparse/single-circuitfamilyexists. This uses theFULLactualderivedpairing, not a freelychosenEulerianone. MoregenerallytheSAMEobstructionholdsifALLcircuitprojectionscoincideup tocomplement, evenwhentherearemultiplecircuits.

AnactualoriginalMAXsolution in theALL-sparsebranch MUSTtherefore have ATLEASTTWOvertex-simplecircuitswithgenuinelydifferentprojectionpairs; theexactlyTWOcase is thederivedtwo-Hamiltoncyclegeometryabove. Such dataareNOTprovedfeasibleorimpossiblehere. Denseverticesarefullyallowed bythegeneralclassification anddoNOTdefineanartificialpairing, so thisdoesNOTexclude theentirev76graphfamily orwhole4+6branch.

## 6. Exactscope, unpaidoriginalconditions and assurance

This pays the previouslyimplicitESSENTIALlocalframeproblem explicitly: ALLzero-diagonal/no-shared-ray4-unitaries are either(SPARSE)withTWOindependentU2blocks or(DENSE)withALLthreepositiveweights andlocalphasegauge; no endpoint/pattern/phasecase isomitted. It thenconverts theENTIREall-sparsebranch into actualuniqueprojectioncircuits andcloses thewholeone-circuit/common-plane mechanism by a TRUEglobalcommonprojection, not byinferringa sectorfromoneisolatedlocalplane.

Stillunpaidarethefullgraphcompatibilityoflocalframes/edgecomplements,40distinctsectorrays/60complementraysand theSAMEallowedTEN-transversalresolution/CLASSICALmate. Densevertexfamilies, multi-circuitdifferent-plane families, otherplacementtypes/minimalrank3complexfamily/higherrankandALLoriginalintrinsic10/4+6/5+5remainOPEN. LocalrealitydoesNOTmakeALLoriginalraysgloballyreal; no real-onlyno-go or v15ceiling iscopiedoutsideitsactualhypotheses.

This SEPARATEFUTUREsource isOUTSIDEMain'simmutablev17/S72candidate/index/proofsand151v2/S55. OnlyaNEWcompletefuturemanifestmayincludeitwithALLolderbranches/audit/S50/S33/E5/product/NR+BOTHflatfactorizations/processcellhistoryretained. No automaticreviewadmission/read/adoption, originalWLOG, A5/Pauli/Gaussian/classifier/NRpremise, formal/kernel/family/vendor/human/finitechecker/control/priority/current-openness/noveltypromotion.

Parentv138TWOfull30m02/full31m10PRECREATIONcadencemajorsNOTexactwrite/runtime+Main156preopaque-pinreleaseMAJORper109NOTICEONLY+ALLolderfindingspersist.No109/newscopes/proof/coauditorreports/159/140access/readclaim/noextraGO/STOP/restart/continuous18wayinference.SameHOLD/noGO/18/OWN/actual30minsubstantivecadence/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark;allwithdrawals/source/clock/cadencehistories/ZERO-creditquarantinespersist.Metadataassemblyhasseparateexactcharacterizations,notglobalcleanhistorycensus.
