# RQLS10 v72 — COMPLETEbalancedbinaryrank4placementclassification: pairedfamilies OR oneconstantimbalance, with a newWHOLEclass excluded

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW complete manuscript: **Mon Oct 26 16:25:30 PDT 2026**. AUTHOR-WRITTEN CANDIDATE; exact F2feature/Walsh/integerpartition/converse/capacity proof only, NOT machine/kernel checked. No scientific Eval/interpreter/arithmetic/CAS/program/enumeration/solver/replay/newGO/private approximate scout/backconversion or chosenphysicalparameter/state/control/probe.

## 1. Fullactualscope and featurelabels, not a physicalansatz

Let M be ANYbinary10-by-10matrix with5onesperrow/column and rank_F2(M)=4. In the originalapplication it is theactualindicator ofa TRUEcommonrank5projection commutingwithALL100rayprojectors; the complexrays remainarbitrary. Import ENTIREv71normalform/capacity and its literalv15count/primarydefinitioninterface. The auxiliarynormalform is

    M_(a,b)=i_a+j_b+x_a dot y_b,
    (i_a,1,x_a),(1,j_b,y_b) inF2^4,
    x_a,y_b inF2^2.

Let r_(i,x),c_(j,y) be the fullfeaturemultiplicities, U_x=r_(0,x)+r_(1,x),V_y=c_(0,y)+c_(1,y), and D_x=r_(0,x)-r_(1,x),C_y=c_(0,y)-c_(1,y), using INTEGERdifferences. Allzero/missing/fullfeaturecases are allowed initially.

The actualbalanceconditions are

    sum_y C_y*(-1)^(x dot y)=0 forEVERYoccurringx,
    sum_x D_x*(-1)^(x dot y)=0 forEVERYoccurringy.  (BAL)

The i/jsigns multiply theseequalities harmlessly and do not changezero. Fullfactor-rank4 requires x andy supports eachAFFINELYspanF2^2: otherwise the factorrows/columns(onesincluded)wouldlie in aspaceofdimension<=3. Thus EACHsupport has at leastTHREEpoints. No fullsupport or genericity isassumed.

## 2. AtleastONEside is fullyCOMPLEMENT-PAIRED, not merelyeven

If the x-support has allFOURpoints, the first(BAL)andcompletefour-pointWalshinversion give C_y=0 forEVERYy. Thus the columnside is complement-paired:

    c_(0,y)=c_(1,y) forALLY.

If insteadbothx andy supports have exactlyTHREEpoints, Fourierinversion appliedto thefirst(BAL) says C_y is a scalar multiple of the characterassociatedto the ONE missingxpoint: it has the form q*(-1)^(x_missing dot y). But C_y=0 at the missingypoint, since BOTHcolumnmultiplicities therevanish. Thereforeq=0 andthecolumnside ispaired. SymmetricallyD=0.

The remainingcase yfull4 similarlymakesD=0. Hence everybalancedrank4matrix has at leastONEFULLcomplement-pairedside. By wholearraytranspose, orient it as thecolumnside. This is strongerthanv71's at-leastoneall-evenaggregatefamily, and its proof covers everymissingpointcase.

Write

    c_(0,y)=c_(1,y)=v_y,       sum_y v_y=5.

Eachnonzero v_y is a positiveinteger. Its support has size3or4.

## 3. CaseP: BOTHsides complement-paired, COMPLETE multiplicitytypes

If alsoD=0, write r_(0,x)=r_(1,x)=u_x withsumu=5. Since eachfeature support affinelyspansF2^2, it has3or4points. The unorderednonzerointegerpartitions of5 with thatmanypositiveparts are EXACTLY

    (3,1,1) onTHREEpoints;
    (2,2,1) onTHREEpoints;
    (2,1,1,1) onFOURpoints.                     (PAIREDTYPES)

These are the COMPLETEpossibletypes for BOTHu andv. Everyrelativeplacement/dualpairing ofthe supports remains a variable; this classification does NOTidentify allsuchrelativeplacements or assume oneaffinepairingWLOG. No computerlist ofmatrices wasgenerated.

The partitionassertion is immediatewithoutenumerationmachinery: forthreepositiveparts summing5 subtract1each, leaving2 distributed as2or1+1; forfourparts subtract1each, leaving1.

## 4. CaseB: ONEconstantimbalance, including ALLzero andendpointmultiplicities

Suppose D isNONZERO. The y-support CANNOTbeall4points, by the second(BAL)/Walshinversion. Thus it hasexactlyTHREEpoints, withmissingpointy0. Fourierinversion gives

    D_x=d*(-1)^(x dot y0).

A legalfeaturetranslation y->y+y0, absorbedinto rowlabeli in(NORMAL), makes the missingpoint0 and

    D_x=d forALLfourx.                          (BIAS)

Here d is an INTEGER, since everyD_x isinteger and the character'svalues are+/-1. Nonzerod forces ALLfourx tooccur because U_x>=|D_x|. EachU_x has thesameparityasd, andsum_xU_x=10. Hence4|d|<=10, so

    d in{+/-1,+/-2}.

If |d|=1, allfourU_x are positiveODDintegers summing10. Subtract1each, divideby2, andpartitionthe remaining3. The COMPLETEunorderedtypes are

    (7,1,1,1),   (5,3,1,1),   (3,3,3,1).       (ODDTYPES)

If |d|=2, eachU_x isevenandatleast2; subtract2each, leaving2. The ONLYtype is

    (4,2,2,2).                                 (EVENTYPE)

The actualrowmultiplicities are recoveredEXACTLYby

    r_(0,x)=(U_x+d)/2,
    r_(1,x)=(U_x-d)/2.

Zeros at |d|=U_x are INCLUDED, not dropped bygenericinvertibility or localdistinctness. The pairedcolumnv-support is threeNONZEROpoints afterthenormalization, withweights either(3,1,1)or(2,2,1). Eachsignofd and everyrelativeassignment ofweights tofeatures isretained. Swappingthebinaryilabel changesd'ssign and complementsM; for a true5+5sector thissimplyexchangesE/Eperp, but no suchswap is needed tocoverbothsigns.

## 5. COMPLETEbinaryconverse, not a quantumexistencecomposition

Everydata choice ofCaseP gives balancedrow/columnweights5 because eachcomplementlabelpair contributes exactlyitsweight to everyoppositecontext. Affinelyspanningx/ysupports plus theactualcomplementpairs make BOTHfactorfamilies fullrank4, sorankM=4.

ForCaseB, columnsremainpaired, making everyrowweight5. The y-support is thethreeNONZEROpoints andD_x=d constant, so for everyactualy!=0,

    sum_x D_x*(-1)^(x dot y)=d*0=0,

giving everycolumnweight5. The sidewithsign(d)available occurs atALLfourx; affineindependence gives3dimensions initsfactorrowspan. Because10>4|d|, at leastONEfeature has U_x>|d|, so BOTHilabels occurthere andsupplythefourthdimension. The pairedcolumns onthreeaffinelyindependenty givefullrank4too. Thus allstatedcases and allendpointzeros yield actualbalancedbinaryrank4matrices.

This is ONLYthe binaryplacementconverse. It proves NOactualcomplexsectorrays, ordinaryMAXQLS or originalTEN-classresolutionexistence. No selectedphysicalviabilityprobe or positive100QLS-as-originalwitnesspromotion occurs.

## 6. A NEWWHOLEbiased-heavy class fails ANYfulloriginalresolution

Take the ENTIRECaseBsubfamily Utype(7,1,1,1), eitherd=+1or-1, andpairedcolumnvtype(3,1,1) onits threepoints. ALLfeatureassignments and relativepairings areallowed.

For thev71capacityparityforms, choose the AUXILIARYoffsets h,k totranslate theuniqueheavyrowfeature anduniqueheavycolumnfeature to0. Theseare EXISTENTIALproofchoices ofaform, not a physicalstate/controlprobe. The rowaggregateweights thenare7at0 and1atALLthreeotherpoints. The columnaggregateweights are6at0 and2atTWOindependentnonzeropoints.

EachofthoseTWOactivecolumndirections selects exactlyTWOofthethreeunitweightnonzerorowfeatures. Therefore the entireinteractioncapacity is

    W_(h,k)=2*2+2*2=8.

This violates the NECESSARYfullresolutioncapacity>=12 ofv71. Hence NOactualoriginal5+5-sectorarray with ANYplacementinthiswholebiased-heavyclass can have thequalifyingTEN-classresolution, regardlessof itscomplexrays/cardinality. Thisclass is distinctfromv71's BOTHpaired3+1+1footprintclass; it has oneNONZEROrowbias andALLfourrowfeatures.

No claim that itsordinaryQLS or aSINGLEquantumtransversal is impossible ismade. The obstruction uses the actualFULLTEN-classcovering, not merelyordinarymaximality.

## 7. Exactfullfrontier and assurance

EVERYbalancedbinaryrank4indicator is now represented byCaseP's pairedtypes with ALLrelativefeatureplacements, orCaseB's COMPLETEbias/aggregateweighttypes with allsigns/zeros/assignments. This is an analyticALL-inputclassification/converse, not anotherinconsequentialsampleenumeration. The wholebiased-heavyclass is excluded prospectively, but manyrank4types remainOPEN, alongsidev68-v70's rank3canonical22NONprojectivefusiongeometry andEVERYhigherrankplacement.

Allactualcomplexvector/Latinresolutionconstraints on the survivingplacements are stillunsolved. Entireoriginal5+5/irreducible10/4+6branches remainOPEN. FeatureF2rank4 isnotphysicalrank4sector, nor a phasecode/qubitstateansatz. No A5/Gaussian/PRODUCT/classifier/NRpremise, originalWLOG, witness/unrestrictedno-go ornovelty/statusclaim.

The primaryinterfaceaudit remainsbinding: ONEFULLTEN-transversalresolution/CLASSICALmate isrequired. Live151v2/asofS55freeze staysimmutable; this furtherUNREVIEWEDsource is onlyfor a NEWWHOLEcurrentfutureunion retainingALLolderbranches/audit/independentS50/S33/NRconditionalBH5/BOTHflatfactorizations. No inheritedparentreading/adoption/formal/kernel/family/vendor/human/finitechecker/control/priority/current-openness/noveltypromotion.

Parentv138TWOadditionalMaincadencePROCESSMAJORSFULL30m02/FULL31m10PRECREATIONobservationsNOTexactwrite/runtime persistwithALLolderfindings. Actual106/107noticesprocess-only, notnewmathscope/permission/STOP/GO/reviewrestart/continuous18wayclaim. SameHOLD/noGO/18/exclusive-root/actual30minsubstantivecadence/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; allwithdrawals/source/clock/cadencehistories/ZERO-creditquarantinespersist. Metadataassembly hasseparateexactcharacterizations, not a globalcleanhistorycensus.
