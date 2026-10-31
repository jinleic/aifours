# RQLS10 v78 — ENTIREtwo-sparse-circuit mechanism is excluded: ALLtwo-projection spectra, no chosenframe/control

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW complete manuscript: **Mon Oct 26 17:18:51 PDT 2026**. AUTHOR-WRITTEN CANDIDATE; exact two-projection/spectral/commutant/product-ONB/incidence proof only, NOT machine/kernel checked. No scientific Eval/interpreter/arithmetic/CAS/program/enumeration/solver/replay/newGO/private approximate scout/backconversion or chosenphysicalparameter/state/control/probe.

**SEPARATEFUTUREONLY:** Main'sfrozencandidatev17ASOFS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, itsindex/proofs and151v2/S55remainUNCHANGED. S78isOUTSIDEthosegatesandmayenteronlyaNEWcompletefuturemanifest. No automaticreviewadmission/read/adoption.

## 1. ENTIREactualmechanism and exactscope

Use ENTIREv76/v77truecommonE4graph/frameclassification. Assume EVERYvertex's actualzero-diagonaltransitionisSPARSEand its UNIQUEactualcomplementpairings give EXACTLYTWOprojectioncircuits. Wequantify overALLgraphs, ALLcomplexframes andALLprojectionangles inthismechanism; NOmatrix/state/cycledecompositionis chosenas acontrol.

Byv77'sderivedvertex-simplicity andtenedges, bothcircuits areHamilton5cycles throughALLfivevertices. CalltheirFIXEDrank2projectionpairs {P,I-P} and{Q,I-Q} inH=rangeE, dimension4. AtEVERYvertextheFOURincidentedgeplanes are P,I-P,Q,I-Q. Theircross-pairtracesarestrictlybetween0and2, so QisNEITHERPnorI-P. Bothactualoriginalrows at eachvertexareONBs inH.

The theorem is: NOoriginal100-raymaximal1-RQLS10 can have thisENTIREtwo-circuitmechanism. This is NOTall-sparse/allgraph/whole4+6classicality, anddoesnotassumethattwo arbitrarycircuits areWLOG for threeormore.

## 2. ALLlocalrayframes admit an actualrank2projection commutingwithBOTH P,Q

At anyvertexlabelthematchededgeplanes P1=P,P2=I-P,P3=Q,P4=I-Q, allowingharmlesswithin-pairlabelswaps. Let e_i be itsfirstoriginalrowONB andf_i itssecondrowONB. TheSPARSEtransitionfromv77has

    f1,f2 inspan(e3,e4),
    f3,f4 inspan(e1,e2).

Therefore theactualrank2projection

    R_v onto span(e1,e2)

commuteswithBOTH P,Q: eachP_i=|e_i><e_i|+|f_i><f_i| isblockdiagonal inR_v/R_v-perp. Moreover

    rank(P restrictedR_v)=rank(Q restrictedR_v)=1,
    rank(P restrictedR_v-perp)=rank(Q restrictedR_v-perp)=1.

ALL EIGHTactualcellrays atthatvertex lieENTIRELYinR_v orR_v-perp. This is a DERIVEDlocalcommonprojection for thetwo circuitoperators, not automaticallyforALLoriginalrays. We prove theglobalconsequenceonlywith the fulltwo-projectioncase analysisbelow.

## 3. Complete two-projection normalform, with allendpoint cases

Diagonalize thepositivecompressionPQP onrangeP, with twoeigenvalueslambda1,lambda2 in[0,1]. For eachinteriorlambda_i chooseunitp_i inrangeP andput

    r_i=(Q p_i-lambda_i p_i)/sqrt(lambda_i(1-lambda_i)).

The r_i areorthonormalinrangeP-perp. On theorthogonal2-spacesH_i=span(p_i,r_i),

    P_i=[1 0;0 0],
    Q_i=[lambda_i, sqrt(lambda_i(1-lambda_i));
         sqrt(lambda_i(1-lambda_i)), 1-lambda_i].  (CS)

For lambda_i=0, pair p_i with ar_i inrangeQ intersectkerP, soQ_i=diag(0,1). For lambda_i=1, pair p_i with ar_i inkerQ intersectkerP, soQ_i=diag(1,0). RankP=rankQ=2anddimension4giveexactlythematchingendpointdimensions. Theseendpointplanes arecommon-eigenlinepairs, not omittedinvertibilitycases.

Thus ALLspectra are covered bytwo2-by-2blocks(CS). Thecentraloperator

    Z=(P-Q)^2

commuteswithP,Q andactsas(1-lambda_i)I onH_i. No numericalCS/SVD/eigenvaluecalculationisrun; theinteriorformulaandendpointcommon-eigenspacesarethewrittenconstruction.

## 4. ALLunequal-angle cases force a TRUEglobalcommon2sector

Suppose lambda1!=lambda2. ZhasTWOdistincteigenvalues with thefixedrank2spacesH1,H2. EveryR_vcommutingwithP,QcommuteswithZ, so itisblockdiagonalacrossH1/H2.

On anyinterior(CS)block, acommutingorthogonalprojection is0orI: commutingwithdiag(1,0) makesitdiagonal, and theNONZEROoffdiagonalentryofQforcesitsequaldiagonalentries. Hence itcannotgiverank1there.

If oneblock isinteriorandtheotheranendpoint, rankR_v=2thereforeforcesR_v tobeexactlyONEwholeblock, since anendpointcontributionofrank1wouldleaveanoddtotal1or3. Ifbothblocksareinterior,theSAMEconclusionfollowsimmediately.

The onlyremainingUNEQUALcase is thetwoendpoints0and1. EachR_v isdiagonalontheFOURcommonlines(P,Q)=(1,0),(0,1),(1,1),(0,0). A rank1choicefromEACHendpointblock wouldeitherhaveP-rank0or2, ORQ-rank0or2; itCANNOTgivebothrank1conditionsfromsection2. Thus R_v againisexactlyH1orH2. This checksALLendpointcombinationswithouta generic-angleassumption.

ConsequentlyALLfortyE4sectorrays, acrossALLfivevertices, liein the SAMEglobaldecompositionH1 directsumH2. Extend theprojectionontoH1 byZEROontheE6complement. ItcommuteswithALL100rayprojectors andhasrank2. Theliteralv15unrestrictedcommon-sectorboundgivescardinality<=86foranyoriginal1-RQLS10, contradicting100-raymaximality.

This excludes ALLunequal-anglecases oftheTWO-circuitmechanism at theiroriginalFULLresolutionhypothesis. It doesNOTclaim theylackeverySINGLEtransversalwithoutthatfullhypothesis.

## 5. Equalendpointangles are impossiblealreadybythelocalpairing

If lambda1=lambda2=1, thenQ=P. Ifbothare0, thenQ=I-P. Bothcontradictv77'sstrictcross-pairtracebetween0and2foractualSPARSEframes. No ordinarymaximalarray in the statedmechanism can havetheseequalendpointcases.

## 6. ENTIREequalINTERIOR-angle case becomes an exact productrepresentation

Let lambda1=lambda2=lambda in(0,1). Thetwo(CS)blocksareequivalent. Identifyingtheir p_i/r_i coordinatesgivesONEcommonphysicalunitary underwhich

    H=C2_first tensor C2_second,
    P=|p+><p+| tensor I2,
    Q=|q+><q+| tensor I2,

where {p+,p-}and{q+,q-}areTWOqubitONBs, withALLFOURraysdistinct andALLcross-basisoverlapsNONZERO. Thelastfactfollowsdirectlyfrom0<lambda<1, not anassumedunbiasedangle.

P,QgenerateALLM2 onthefirstfactor: P isdiagonalrank1 andQhasnonzerooffdiagonalentry. Theircommutant isI2 tensorM2. Hence eachlocalR_v fromsection2hasformI2 tensor|u_v><u_v| for someunitrayu_v. Itscomplement usesu_v-perp.

TheactualEIGHTlocalcellrays atvertexv are EXACTLYthecartesianfamily

    {p+,p-,q+,q-} tensor {u_v,u_v-perp}.

Indeed eachofP/I-P/Q/I-Qedgeplaneshas oneactualcellineachoriginalrow. Thefirstrow'sP-pairbothlieinR_vanditsQ-pairbothlieinR_v-perp; thesecondrowreversestheassignmentbytheSPARSEtransition. No first-factor orsecond-factorstateis chosen; this is a DERIVEDrepresentation ofEVERYisoclinicframefamily.

Global100-raydistinctnessforcesALLTENsecond-factor rays u_v,u_v-perp fromthefivevertices tobedistinct: acoincidencebetweenverticesduplicatesanACTUALproductraybyfixingthesamep+factor. Consequently anytwoqubitraysfromDIFFERENTvertexbases are NONORTHOGONAL, byuniquenessofaqubit'sorthogonalpartner.

## 7. Such anisoclinicMAXsectorcannotcontribute theFOURrays of ANYquantumtransversal

AnactualglobalquantumtransversalwouldcontainexactlyFOURE4-sectorrays forminganONB ofH, in distinctoriginalrows/columns. Groupthosefourproductrays bytheirvertexv. For distinctvertexgroups, the SECOND-factoroverlapsareNONZERO, sotheir FIRST-factor spans mustbemutuallyorthogonalinC2.

AtmostTWOvertices canthereforebeused. ONEvertexcannotprovideFOURcells, sinceit hasonlyTWOactualoriginalrows. Thus exactlyTWOvertices mustbeused, withTWOcellsfromEACH. Theirfirst-factor spans musteachbeONE-dimensional. Thetwo selectedcells atagivenvertex must consequentlyhavethe SAMEfirst-factor ray.

But atthatvertex eachofp+,p-,q+,q-belongs to EXACTLYONEactualincidentedgecolumn: thetwoP-cycleedgescarrytheoppositePplanes, andthetwoQ-cycleedgescarrytheoppositeQplanes. Bothoriginalrowcells withtheSAMEfirst-factor rayliein that SAMEedgecolumn. SelectingTWOsuchcellsviolatesthetransversal'sdistinct-columncondition. Contradiction.

This excludes EVERYquantumtransversal in the ENTIREequalinterior-angleMAXcase, notjusta chosenresolution or MUB/productcontrol. It uses theactualcolumnincidenceandglobaldistinctness, withallqubitangles/second-factorbasesfree.

## 8. Entiretwo-circuit conclusion and exactremainingoriginalgap

Thefourpossibilities—unequallambdasincludingALLendpoints, equallambda0, equallambda1, andequalinteriorlambda—areexhaustive. Sections4-7exclude EVERYoriginal100-raymaximal1-RQLS10 withtheENTIREall-SPARSE/exactly-TWOactualcircuitsmechanism. No scalaranglewaschosen, no densevertex discardedWLOG, andno two-circuitassumption imposedonotheractualcircuitcounts.

Thus anactualMAXoriginalarray inthev76graphfamily mustEITHERhave atleastONEdensevertex OR, ifALLverticesaresparse, haveATLEASTTHREEactualvertex-simpleprojectioncircuits. Theirdifferentprojectionpairs/fullframecompatibility, otherplacementtypes/minimalrank3complexfamily/higherrank, complement60raysand theSAMEallowedTEN-classresolutionremainOPEN. Theentireunrestricted4+6/5+5/irreducible10branchesremainOPEN; no originalwitness/unrestrictedno-go isdelivered.

The proofusesonlyENTIREv15actualcommon-sectorceiling,v76/v77graph/framefacts, elementarytwo-projection spectral/commutantargumentsprintedabove, andtheactualprimaryTEN-transversalresolution/CLASSICALmateinterface. No A5/Gaussian/Pauli/phasecode/classifier/NRpremise or actualcommon2sectorinferencebeforeitsfullALL100proof.

This SEPARATEFUTUREsource isOUTSIDE Main'sfrozencandidatev17/S72/index/proofsand151v2/S55. OnlyaNEWcompletefuturemanifestmayincludeitwithALLolderbranches/audit/S50/S33/E5/product/NR+BOTHflatfactorizations/processcellhistoryretained. No automaticreviewadmission/read/adoption/formal/kernel/family/vendor/human/finitechecker/control/priority/current-openness/noveltypromotion.

Parentv138TWOfull30m02/full31m10PRECREATIONcadencemajorsNOTexactwrite/runtime+Main156preopaque/preACK-pinreleaseMAJORper109/110NOTICESONLY+ALLolderfindingspersist.No109/110/newscopes/proof/coauditorreports/159/140access/readclaim/noextraGO/STOP/restart/continuous18wayinference.SameHOLD/noGO/18/OWN/actual30minsubstantivecadence/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark;allwithdrawals/source/clock/cadencehistories/ZERO-creditquarantinespersist.Metadataassemblyhasseparateexactcharacterizations,notglobalcleanhistorycensus.
