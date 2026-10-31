# RQLS10 v67 — UNRESTRICTED5+5-sector placements of binaryrank<=3: no rank2transversal, complete rank3form and TWOmaximal residualpatterns

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW complete manuscript: **Mon Oct 26 15:36:17 PDT 2026**. AUTHOR-WRITTEN CANDIDATE; exact common-projection/binarylinearalgebra/graph/ONB-completion proof only, NOT machine/kernel checked. No scientific Eval/interpreter/arithmetic/CAS/program/enumeration/solver/replay/newGO/private approximate scout/backconversion or chosenparameter/state/control/probe.

## 1. Trulyunrestricted sectorhypothesis, not a product/A5/phase ansatz

Let an ACTUALQLS10 have a rankFIVEorthogonalprojection E commuting with EVERYone of its100rayprojectors. Its vectors are therefore ENTIRELYinrangeE or itsorthogonalcomplement. Let the binary10-by-10matrix M have entry1 exactlyonrangeE cells. The completev15sectorcount argument gives EXACTLYFIVE1s in EVERYrow/column, and thosefivevectors form anONB ofH=rangeE. Anyhypotheticalquantumtransversal likewise has EXACTLYFIVEsectorcells bytraceE.

AllHvectors are ARBITRARYcomplexrays; NOtensorfactor, rootofunity, Hadamard, A5, fieldcoordinate or specifiedresolution is assumed. This applies to the actualremainingintrinsic5+5branch, subject only to the explicitbinaryranksubcases below. The rankin thismanuscript means rank_F2(M), NOTphysicalrank3of a commonprojection and NOTv16'squtritsector.

The registeredoriginalresolutioncondition is the actualDefinition1.1/fullLemma2.2 bound bythe90LFprimaryinterfaceaudit: TENdisjointquantumtransversals/CLASSICALmate. No model or selectedLatinpattern is WLOG.

## 2. EVERYbinaryrank<=2placement forbids evenONEquantumtransversal

Everyrow ofM has oddweight5. Thus the parityfunctional on itsbinaryrowspace is nonzero and allactualrows lie in its oddcoset. Binaryrank1 wouldgive onlyONEoddrowtype, making everycolumncount0or10, impossible.

Atbinaryrank2 there are exactlyTWOpossibleoddrowtypesp,q. Bothoccur. In eachcolumn theirtwo bits cannotagree: agreeing0or1 would make thatcolumncount0or10. Therefore q=1+p. Columnbalanceforces eachrowtype to occurFIVEtimes, andp itself hasweight5. Hence

    M_(a,b)=r_a XOR c_b,
    sum_a r_a=sum_b c_b=5.

For ANYrow/columnpermutationmatching pi, the parity ofitssectorcount is

    sum_a M_(a,pi(a)) =sum_a r_a+sum_b c_b=0 mod2.

But a quantumtransversal is anONB and musthave5sectorcells, anODDnumber. Contradiction. This covers EVERYbalancedbinaryrank2placement, not onecheckerboardcontrol. Consequently anoriginalmaximal1-RQLS10withsuch a sector MUSThave binaryrankATLEAST3.

## 3. COMPLETEbinaryrank3classification, including potentiallymissingrowtypes

Now suppose rank_F2(M)=3. The oddcoset ofits3-dimensionalrowspace has FOURvectors p1,p2,p3,p4, summingto0. These include allactualrowtypes, but initiallysome may be missing. Let n_v>=0 be theirrowmultiplicities, with sum_v n_v=10.

In anycolumn, thefour p_vbits have evenweight. Weight0or4 is impossible because the actualcolumncountwould be0or10. Thus EVERYcolumn has exactlyTWO1bits amongthesefourtypes. Regard it as anedge of a looplessmultigraph G onfourvertices; its binaryincidencematrix has rows p_v and rank3. A rowdependency assigns vertexcoefficientsconstant on everyconnectedcomponent, sinceeachcolumn says z_u+z_v=0. Therefore itsrank is4-minus-numberofcomponents, and G is CONNECTED.

Everyedge{u,v} also satisfies

    n_u+n_v=5.                                  (EDGE)

Anoddcycle wouldforce aninteger n_v=5/2, impossible. Thus G isbipartite. Connectivitymakesn_v constant=a ononepart and5-a ontheother. Ifpartsizes are1and3, thetotalrowcount10 wouldforcea=5/2, againimpossible. Hence theparts have size2and2.

Ifa=0or5, onlyTWOactualrowtypes remain, contradicting rank3. Thus1<=a<=4: ALLFOURrowtypes actuallyoccur. Their Hammingweights aretherefore5, so everyvertex ofG has totalcolumnmultiplicity5. Write thetwo parts asA0,A1 andB0,B1, andcolumnedges as C_(alpha,beta)={A_alpha,B_beta}. The fouredge multiplicities necessarilyare

    [ t     5-t ]
    [ 5-t   t   ],     1<=t<=4.                 (COUNTS)

Indeed allrow/columnsums are5; ift=0or5 thegraphdisconnects. Theactualrowmultiplicities are

    |A0|=|A1|=a,      |B0|=|B1|=5-a.           (ROWS)

Acell ofM is1 IFFitsrowtype is anendpointof itscolumnedge. Equations(ROWS)/(COUNTS)andthisincidencerule are the COMPLETEcanonicalform for EVERYbalancedbinaryrank3matrix. Conversely EACHa,t in{1,2,3,4} yields a balancedbinaryrank3matrix: allfourtypes/edgesoccur andK2,2 isconnected. This converse is ONLYa binaryplacement assertion, not existence of quantumvectors or a Latinresolution.

## 4. PhysicalONBs exclude ALLcornercases a,t in{1,4}

Firsttakea=1, retaining ALLcomplexsectorrays. The A0 andA1rowgroups eachcontainONEactualrow, with sectorONBs U0 andU1. The B0rowgroup has FOURactualrows; itssectorcells occupy exactlythe FIVEcolumns in C00 unionC10. Eachofthosecolumns has itsfourB0sectorvectors plusoneadditionalvector: fromA0 onC00 andfromA1 onC10.

Sum thefivecolumnsectorONBprojectoridentities toobtain5I_H. The fourB0rowsectorONBs contribute4I_H. Therefore the remainingFIVEvectors

    A0-vectors onC00 (t ofthem),
    A1-vectors onC10 (5-t ofthem)

have projectorssummingtoI_H. They areunitvectors; putting them ascolumns of a square5-by-5matrix shows theyform anONB. This is an exactONB-completion identity, not a phase or rankapproximation.

If t=1, thefourA1vectors onC10 span the orthogonalcomplement of the ONEA0vector onC00. The remaining A1basisvector onC11 lies on that SAMEline as the A0vector: an ACTUALduplicateprojectiveray in twodifferentoriginalcells. If t=4, the ONEA1vector onC10 insteadduplicates the remainingONEA0vector onC01. Either contradicts100-raymaximality.

Swapping the two graphparts A/B replacesa by5-a andis only a relabeling/permutation ofrow/columnblocks. Thus the sameproof excludesa=4 witht=1or4. No state/control is selected; theproof covers ENTIREcomplexfamilies ofallfourcorners.

## 5. EXACTLYTWOcanonical placementclasses remain atbinaryrank3

The following are genuineequivalences ofthebinaryplacement/physicalarray, not newgeometrichypotheses:

- exchange thetwo graphparts: a->5-a;
- interchange onepart's vertexlabels: t->5-t;
- transpose thewholearray: (a,t)->(t,a), afterrelabelingtypes.

For the laststatement, thetransposedrowtypes are the fouroriginalcolumnedges. Theircomplementarypairs(C00,C11)and(C01,C10)occur t,t and5-t,5-t times. Theoriginalrowtypes then give the newedge multiplicities a,5-a,5-a,a. This pays the parameterexchange explicitly.

Hence normalizebotha,t into{1,2}. Thecorner(1,1) isphysicallyimpossible bysection4, and(1,2)/(2,1) are equivalentbytranspose. Consequently ANYmaximalarraywitha rank5commonsector and binaryrank3placement is equivalent to ONEof

    (a,t)=(1,2),       (a,t)=(2,2).             (TWO)

NOcomplexvectorassignment or actualLatinresolution in eitherremainingpattern is asserted. Everyrow/column/transversalONB andall50distinctsectorrays remainrequired. If the actualbinaryrank is>=4, thisclassification imposes nocanonical(TWO)restriction.

## 6. Exact originalscope and assurance

This is an UNRESTRICTEDcommon-sector theorem WITH anexplicitlow-binary-rankcase split: rank<=2 hasNOquantumT; rank3 has a completecanonicalclassification and fourphysicalduplicatecorners excluded, leavingexactlyTWOplacementclasses; higherrankplacements remainOPEN. It does NOTexclude the entireoriginal5+5branch, infercommonsectorsfromlocalplanes/tensorfactors, or touch arbitraryirreducible10/4+6arrays. Allthreeunrestrictedoriginalbranches remainOPEN.

Namedimports are the ACTUALcommonprojection/count premise inv15, elementaryF2linearalgebra/graphconnectedness and the printedprojectorONB-completion identities. No v14withdrawnmodel, A5/Gaussian/qubitPRODUCT/paritytheorem, phasecode/classifier orNRcomputationalinput is used. ThepriorparentWRITTENsupport ofv15doesNOTautomaticallyadopt thisnewclassification or itsphysicalapplication.

The requiredprimarydefinitionaudit was completedfirst and remainsbinding. Live151v2/asofS55freeze isunchanged; this furtherUNREVIEWEDsource is onlyfor a NEWWHOLEcurrentfutureunion retaining ALLolderbranches/audit/independentS50/S33/NRconditionalBH5/BOTHflatfactorizations. No inheritedparentreading/adoption, originalwitness/unrestrictedno-go, finitechecker/control/vendor/formal/kernel/family/human/current-openness/noveltypromotion.

Laterparentv138TWOadditionalMaincadencePROCESSMAJORSFULL30m02/FULL31m10atPRECREATIONobservationsNOTexactwrite/runtimeclocks persistwithALLolderfindings; no mathscope/newSTOP/GO/reviewrestart/continuous18wayclaim. SameHOLD/noGO/18/exclusive-root/actual30minsubstantivecadence/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; allwithdrawals/source/clock/cadencehistories/ZERO-creditquarantinespersist. Metadataassembly has itsownexactsource/outputcharacterizations, not a globalcleanhistorycensus.
