# RQLS10 v71 — ENTIREsector-placement bilinearnormalform; ALLbinaryrank4resolutions need at leastTWELVEinteractioncells in EVERYshift

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW complete manuscript: **Mon Oct 26 16:18:30 PDT 2026**. AUTHOR-WRITTEN CANDIDATE; exact F2rank-factor/parity/Walsh/integercapacity proof only, NOT machine/kernel checked. No scientific Eval/interpreter/arithmetic/CAS/program/enumeration/solver/replay/newGO/private approximate scout/backconversion or chosenphysicalparameter/state/control/probe.

## 1. Actualunrestrictedcommon5sector and the FULLoriginalresolution

Let an actualQLS10 have a TRUErank5projection E commutingwith ALL100rayprojectors. Its binarysectorindicator M has FIVE1s perrow/column, and ANYquantumtransversal has FIVE1s bytraceE, exactlyasinv15. Allcomplexvectors are otherwiseunrestricted. The registeredoriginalcondition requires ONESETTENdisjointquantumtransversals covering100cells, equivalentlyaCLASSICALmate; ordinary100-rayQLS alone isnotenough, aspaid bytheprimarydefinitionaudit.

Put r=rank_F2(M). Everythingbelow concerns this AUXILIARYbinaryplacementrank, NOTphysicalsectorrankr, NOTroot-of-unityraycoordinates or a tensorfactorization. This gives a newrepresentation for the higher-placement-rank residual, not a chosenmatrixexample. NoA5/Gaussian/qubitPRODUCT/classifier/NR input is used.

## 2. EXACTnormalform for EVERYbinaryrank r

Choose ANYfull-rank factorization overF2

    M=A B,        A:10-by-r, B:r-by-10.

Let u=sumofALLrowvectors ofA andv=sumofALLcolumnvectors ofB. Column/rowweights5ODD give

    u B=1^T,       A v=1.

Hence u,v areNONZERO, and

    u v=sum ofALLentriesM=50=0 inF2.

In particularr>=2. Choose a basischangeT whose secondcolumn isv, whose firstcolumn hasu-pairing1, and whose remainingcolumns completev to abasis ofkeru. Then uT=e1^T andT^(-1)v=e2. ReplacingA,B byAT,T^(-1)B, EVERYactualrow andcolumn have forms

    row a:       (i_a,1,x_a),
    column b:    (1,j_b,y_b),       x_a,y_b inF2^(r-2).

Therefore the ENTIREactualmatrix has theexactbitformula

    M_(a,b)=i_a+j_b+x_a dot y_b.                 (NORMAL)

Moreover the vectorSUMS are exactly

    sum_a i_a=1,       sum_a x_a=0,
    sum_b j_b=1,       sum_b y_b=0.              (SUMS)

These follow from sumrows(AT)=uT=e1^T andsumcols(T^(-1)B)=e2; the tenconstantcoordinates sum0. This is an existence/basisproof for ALLactualM, not an executedrow-reduction or a restriction on physicalrays. ANYsuchnormalization may beused; no onefeaturelabeling is scientificWLOG beyond its exactmatrixidentity.

## 3. ALLshiftedinteractioncounts have ODDintersection with EVERYquantumtransversal

For ANYrow/columnmatching pi, summing(NORMAL)alongitscells andusing(SUMS) shows

    sectorcount mod2=sum_a x_a dot y_(pi(a)).

If the matching is a QUANTUMtransversal, itssectorcount is5ODD. Now take ANYauxiliaryoffsets h,k inF2^(r-2). The shiftedinteractionbit

    (x_a+h) dot (y_b+k)

differs fromx_a doty_b by x_a dotk+h doty_b+h dotk. Summing along ANYmatching kills those terms by(SUMS) and theevenorder10. Hence EVERYquantumtransversal contains an ODDnumber, at leastONE, ofcells in

    I_(h,k)={(a,b):(x_a+h) dot (y_b+k)=1}.

If a FULLTEN-classresolution exists, it partitions ALLcells, so for EVERYoffsetpair

    W_(h,k)=|I_(h,k)|>=10.                      (CAP)

No matching/control was selected. The offsets are auxiliaryparityforms, not physicalparameterprobes. This capacitycondition is valid for EVERYbinaryrankr; at r2 it recovers the no-transversalobstruction because there are nointeractioncoordinates. It does notreplace the strongerfullrank3classification/v68proof.

## 4. Atbinaryrank4, allpairmultiplicities on EITHERside have a COMMONparity

Nowr=4, sox,y lie inF2^2. Let U_x countactualrows withfeaturex andV_y countactualcolumns withfeaturey, ignoringi,j. The total10 and the twocoordinatesumidentities in(SUMS) imply

    U_00=U_01=U_10=U_11 mod2,
    V_00=V_01=V_10=V_11 mod2.                  (UNIFORMPAR)

For example U_10+U_11=U_01+U_11=0, andsum_xU_x=0, force allfourparitiesequal. ZEROmultiplicities are allowed; no fullsupport is assumed.

AtleastONEof thesetwofamilies is ALL-EVEN. To proveit, iftheUfamily isnotall-even, (UNIFORMPAR)makes allfourU_x ODD, so ALLfourfeaturex values occur. Let c_(j,y) countactualcolumns withfullfeature(j,y), andC_y=c_(0,y)-c_(1,y). Integerrowweight5 gives, for eachactual(i,x),

    sum_y C_y*(-1)^(x dot y)=0.

BecauseALLfourx occur, elementaryfour-pointWalshinversion givesC_y=0 forEVERYy. Explicitly multiplyby(-1)^(x dot y0),sumALLx anduse sum_x(-1)^(x dot(y+y0))=4delta_(y,y0). Hence c_(0,y)=c_(1,y), andV_y isEVENforEVERYy. This proves the assertion with allmissing/zero casesincluded.

## 5. COMPLETEdivisibilityproof: EVERYshiftedcapacity is a MULTIPLEofFOUR

Suppose firstallU_x areeven. For fixedx setz=x+h. Ifz=0 it contributesnothing toW_(h,k). Ifz!=0, the conditionz dot(y+k)=1 selects EXACTLYTWOof thefour yvalues. TheirV_y counts sum to anEVENnumber by(UNIFORMPAR). Thus

    U_x * sum_(y:z dot(y+k)=1) V_y

is divisiblebyFOUR. SumoverALLx: W_(h,k) is divisibleby4.

IfinsteadallV_y areeven, use thesymmetricargument and theuniformparityofU_x. The precedingsection guarantees atleastONEcase, including theirintersection. Therefore for ALLbinaryrank4matrices and EVERYoffsetpair,

    4 divides W_(h,k).

Combinewith(CAP): ANYoriginalfullresolution requires

    W_(h,k)>=12 for EVERYh,k inF2^2.             (RANK4CAP)

This is an ALL-variableplacementobstruction: if ANYnormalizedauxiliaryshift hascapacity0,4or8, NOqualifyingTEN-classquantumresolution exists, regardlessof thecomplexsectorvectors. It is NOTa no-single-transversalclaim and does NOTassert12forhigherbinaryranks where thisdivisibilityargument wasnotproved.

## 6. A wholeexcluded3+1+1paired-footprint class, not a physicalcontrolprobe

For clarity the obstruction closes an entireNONEMPTYbinaryplacementclass. In(NORMAL), suppose rowfeatures occupy0,p,q withp,q independent, withBOTHcomplementlabels i at0 repeated3times andbothlabels atp,q repeatedONCE. Do thesameon thecolumnside with0,p',q', andsuppose the2-by-2pairingtable ofp,q againstp',q' is a permutationmatrix overF2. This describes a fullaffine/dual-label-equivalenceclass ofplacements, not a selectedraystate or viabilityprobe.

Such actualbinarymatrices have row/columnweights5: eachcomplementlabelpair contributes exactlyitsmultiplicity to everyoppositeweight. Bothfactorfamilies spanall4coordinates, sorankM=4. At offsets h=k=0, theheavyzero groups contribute0, and the interactiontablehas exactlyTWOactive2-by-2singletonpairblocks. Hence

    W_(0,0)=4+4=8,

violating(RANK4CAP). Thus EVERYcomplexarray withtruecommonE5andANYplacementinthisentireclass fails theFULLoriginalresolution. The binaryplacementconverse asserts NOquantumvectorassignment or ordinaryMAXQLS existence; it is not a positiveoriginalcomposition.

## 7. Exactremainingoriginalscope and assurance

New delivered results are the fullbilinearfeature normalform for ANYrankr, ALLshiftcapacity>=10, COMPLETErank4uniform-parity/all-even-side/divisibilityargument and>=12bound, plus the wholepaired3+1+1footprint exclusion. The firstfeaturesi,j,x,y are AUXILIARYF2labels oftheactualsectorindicator, not qubitstates or a physicalcoordinateansatz. The TRUEcommonE5premise and allcomplexrays remainliteral.

The survivingrank3canonical22NONprojectivefusionbranch fromv68-v70 remainsOPEN. Manyrank4placements satisfyingallcapacities, allhigherbinaryranks and theiractualcomplexvector/fullLatinresolutionconditions remainOPEN. The entireoriginal5+5/irreducible10/4+6branches remainOPEN; no originalwitness/unrestrictedno-go, A5/product/phaseWLOG or novelty/statusclaim.

The actualprimaryinterfaceaudit remainsbinding: FULLTEN-classresolution/CLASSICALmate isrequired, ordinary100QLS alone notenough. Live151v2/asofS55freeze staysimmutable; this furtherUNREVIEWEDsource is onlyfor a NEWWHOLEcurrentfutureunion retainingALLolderbranches/audit/independentS50/S33/NRconditionalBH5/BOTHflatfactorizations. No inheritedparentreading/adoption, formal/kernel/family/vendor/human/finitechecker/control/priority/current-openness/noveltypromotion.

Parentv138TWOadditionalMaincadencePROCESSMAJORSFULL30m02/FULL31m10PRECREATIONobservationsNOTexactwrite/runtime persistwithALLolderfindings. Actualcheckpoint106/107notices areprocess-only, notnewmathscope/permission/STOP/GO/reviewrestart/continuous18wayclaims. SameHOLD/noGO/18/exclusive-root/actual30minsubstantivecadence/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; allwithdrawals/source/clock/cadencehistories/ZERO-creditquarantinespersist. Metadataassembly hasseparateexactcharacterizations, not a globalcleanhistorycensus.
