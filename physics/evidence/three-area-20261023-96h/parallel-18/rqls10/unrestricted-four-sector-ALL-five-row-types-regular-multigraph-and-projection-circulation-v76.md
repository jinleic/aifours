# RQLS10 v76 — ALLfive-row-typecommon4-sector placements are4-regularmultigraphs onFIVEvertices; exactmatrixcirculation and framegluing interface

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW complete manuscript: **Mon Oct 26 17:04:45 PDT 2026**. AUTHOR-WRITTEN CANDIDATE; exact weightedsubset/graph-rank/projector-circulation/frame proof only, NOT machine/kernel checked. No scientific Eval/interpreter/arithmetic/CAS/program/enumeration/solver/replay/newGO/private approximate scout/backconversion or chosenphysicalparameter/state/control/probe.

**SEPARATEFUTUREONLY:** Main'scandidatev17ASOFS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, itsindex/proofs and151v2/S55freeze remainUNCHANGED. This NEWsource is OUTSIDEtheirgate andmayenteronlyaNEWfuturemanifest; no reviewadmission/read/adoption.

## 1. Exactall-inputstatement and truecommon-sectorpremise

Let M be ANYbinary10-by-10matrix withFOUR1sineveryrow/column and EXACTLYFIVEdistinctrowtypes. In anactualoriginalapplication it is theindicatorofa TRUErank4commonprojectionE commutingwithALL100rayprojectors, with arbitrarycomplexsectorrays. WeclassifyALLsuchM, NOTjusta symmetricA5duad, simplegraph, tensor orphasecase.

The conclusion is that EVERYrowtype occursEXACTLYTWICE andEVERYcolumn is theincidencevectorof anEDGEbetweenTWOfivevertices. Thetenedgecolumns form a CONNECTEDloopless4-regularmultigraphG onfivevertices. ItsF2rank is4. ConverselyEVERYsuchG gives oneoftheseindicators. Allparallel-edgepositions remainallowed. Noactualquantumrays/resolutionexistence isassertedbythisbinaryconverse.

## 2. COMPLETEpositiveintegerclassification, with allnonuniformcases excluded

Asinv74, eachpositiverowtypemultiplicityn_i isatmost4 andtheirsum is10. TheCOMPLETEpartitions intoFIVEpositiveparts are

    (4,3,1,1,1), (4,2,2,1,1), (3,3,2,1,1),
    (3,2,2,2,1), (2,2,2,2,2).

Acolumn'ssetof1-types musthave totalmultiplicity4.

For(4,3,1,1,1), the4-typesingletonrequiresFOURcolumns; each1-type canappearonlypairedwiththe3-type, so eachrequiresFOURadditionalcolumns, at leastTWELVEsuchcolumns—impossible.

For(4,2,2,1,1), aftertheFOUR4-onlycolumns, thepossiblecolumnsubsets are thepair of2-types, orone2-type togetherwithBOTH1-types. Thetwo1-types thereforehave IDENTICALbits inEVERYcolumn, so theyareNOTdistinctrowtypes, contradiction.

For(3,3,2,1,1), the2-type canoccuronlywithBOTH1-types, requiringFOURsuchcolumns. Thenboth1-types havealreadyusedalltheirFOUR1s andcannotoccurinany3+1column. The3-types consequentlyhaveNO1-column, contradiction.

For(3,2,2,2,1), the3-type and1-type canoccuronlyTOGETHER, soagainareIDENTICALrowtypes, contradiction.

Thus ONLY(2,2,2,2,2)remains. This is a writtenALL-integercaseproof, not anenumeratedmatrixlist or a restrictedconstant-statecheck.

## 3. COMPLETEgraphclassification and binaryconverse

Takeonevertex foreachrowtype, withTWOactualrows pervertex. Aweight4column mustchooseexactlyTWOtypes, henceoneedgeofalooplessmultigraphG. Eachtype'srowweight4 saysitsvertexdegreeis4; therearetenedgecolumns.

G cannotbedisconnected. Withfivevertices, noisolatedvertex(degree4), anydisconnectedpartitioncontainsaTWO-vertexcomponent. Bothvertices ofsuchacomponent haveexactlythesameincidentedgecolumns, contradictingDISTINCTrowtypes. HenceG isconnected.

For anedge{u,v}, aF2linearrowdependencyhascoefficientz_u+z_v=0. ConnectivityforcesallcoefficientsEQUAL, so theFIVEvertexincidencerows haveEXACTLYONEdependency andrank4. DuplicatingeachrowtypeTWICE doesnotchangethatrank.

Converselya connectedloopless4-regularmultigraphonfivevertices hasdistinctvertexincidencerows: twoequaloneswouldhaveonlyedgesjoiningthosevertices, makinganisolated2-component. DuplicateeachrowTWICE; eachcolumnthenhas4ones andeachrow4ones. Thus itgivesALLtheassertedbinarydataandF2rank4. Parallelcolumns are genuine distinctoriginalcolumns; theyarenotdiscarded.

G isnecessarilyNONbipartite: a4-regularbipartitegraphhas equalnumbersofverticesinitsTWOparts bydegreecount, impossiblewithFIVEvertices. Edge-multiplicity4wouldisolateatwo-vertexcomponent, soactualmultiplicitiesareatmost3. Noonegraph(e.g.,K5ordoubled5-cycle) isselectedorassumedWLOG; theENTIREmultigraphfamily isretained.

## 4. ALLactualcomplexsectorgeometry gives a conservedrank2projectionflow

WorkinH=rangeE, dimension4. For edgecolumn e={u,v}, theTWOsectorvectors initsTWOu-rows span arank2projectionP_(u,e). TheotherTWOsectorvectors fromv are itsorthogonalcomplement:

    P_(v,e)=I_H-P_(u,e).                        (EDGE)

Atvertexu, eachofitsTWOactualrows hasFOURsectorvectorsforming anONB. Summingtheirprojectorsgives

    sum_(e incidentu) P_(u,e)=2I_H.             (VERTEX)

These are FULLoperatoridentities for EVERYactualedge/vertex, not averagedtraceconditions. Define thetracelessHermitianreflections

    A_(u,e)=2P_(u,e)-I_H.

They satisfy EXACTLY

    A_(u,e)*=A_(u,e),  A_(u,e)^2=I_H,
    tr A_(u,e)=0,
    A_(v,e)=-A_(u,e),
    sum_(e incidentu) A_(u,e)=0.                (FLOW)

Thus theactualsupport carries an operator-valuedCIRCULATION byrank2reflections on theWHOLEconnected4-regularodd-vertexmultigraph. Choosinganorientationmerelychoosesoneof thetwoendpointsignsperedge; it isnot a physicalcontrol, unitarygauge or numericalflowprobe.

## 5. Exacttwo-sidedframegluing interface, including the missingcondition

Converselysuppose anallowedG andrank2projectionsP_(u,e) satisfy(EDGE)/(VERTEX). OneSTILLmustsupply, forEVERYvertexu andEVERYincidentedgee, anACTUALONB

    p_(u,e,0), p_(u,e,1) ofrangeP_(u,e),

suchthat for EACHfixedrowindexa=0or1, theFOURvectors

    {p_(u,e,a): e incidentu}

form anONB ofH. This is the ESSENTIALtwo-rowframefactorization, not automaticfromtheoperatorSUM(VERTEX). Allframechoices remaincomplex/free; noneis providedorselected.

Givenactualsuchdata, puttingthesevectorsintheTWOu-rows andedgecolumns makesEVERYsectorrowanONB bythiscondition, andEVERYsectorcolumnanONB by(EDGE). ConverselyANYactualsectorrow/columnassignmentproducesexactlytheseprojectionsandframefactorizations. This proves theCOMPLETEiffinterface for the40-sectorrayROW/COLUMNproblem inthisWHOLEplacementclass.

Global40-raydistinctness, the60complementraysand theSAMEallowedTEN-classquantumresolution/CLASSICALmate remainADDITIONALrequirements. Theprojectionflowbyitself isnot a witness, a quantumLatincompletion, or a commonrank2projectorsectorofALL40rays. IndividualP_(u,e) varywithedges andneednotcommutewithothercellprojectors.

## 6. Exactoriginalfrontier and immutableassurance

Newdeliveredfacts are theCOMPLETEfive-row-typeclassification/converse, itsminimalnextF2rank4andNONbipartitegraphstructure, andtheFULLoperatorcirculation/two-framegluingnecessity-and-sufficiencyinterface. These are ALL-variablegeometry, not anotherchosengraph/Pauli/A5control or genericexistenceclaim.

S75'sENTIREminimalbinaryrank3canonicalblockremainsitsownstill-unsolvedphysicalfamily; thisv76class entersrank4withEXACTfive actualrowtypes. Rank4withmoretypes, higherranks, bothphysicalcanonicalcomplexfamiliesandtheentireoriginal4+6/5+5/irreducible10branchesremainOPEN. Noactual40+60rays/qualifyingresolution or unrestrictedno-go isdelivered. S50/S33remainindependent; nofinitegraphclassifier, representation/WLOG, NRphasecode/Gaussian/productpremise ornovelty/statusclaim.

Theactualprimarydefinitionauditremainsbinding: ordinary100QLSwithoutONEFULLTEN-transversalresolution/CLASSICALmate isnotregistered. ThisfurtherSEPARATEFUTUREsource mayenteronlyaNEWcompletefuturemanifestretainingALLolderbranches/audit/S50/S33/E5/product/NR+BOTHflatfactorizations/processcellhistory; Main'sfrozencandidatev17/S72and151v2/S55/index/proofsremainimmutable. Noautomaticreviewadmission/read/adoption/formal/kernel/family/vendor/human/finitechecker/control/priority/current-openness/noveltypromotion.

Parentv138TWOfull30m02/full31m10PRECREATIONcadencemajorsNOTexactwrite/runtime+Main156preopaque-pinreleaseMAJORper109NOTICEONLY+ALLolderfindingspersist. No109/newscopes/proof/coauditorreports/159/140access/readclaim/noextraGO/STOP/restart/continuous18wayinference.SameHOLD/noGO/18/OWN/actual30minsubstantivecadence/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark;allwithdrawals/source/clock/cadencehistories/ZERO-creditquarantinespersist.Metadataassemblyhasseparateexactcharacterizations,notglobalcleanhistorycensus.
