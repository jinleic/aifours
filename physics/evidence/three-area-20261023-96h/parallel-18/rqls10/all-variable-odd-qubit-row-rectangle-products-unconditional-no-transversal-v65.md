# RQLS10 v65 — For ODDm the ENTIRE qubit/row-rectangle product model has NOquantumtransversal, even nonmaximal

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW complete manuscript: **Mon Oct 26 15:04:28 PDT 2026**. AUTHOR-WRITTEN CANDIDATE; exact partial-trace/eigenspace/overlap-graph/integerparity proof only, NOT machine/kernel checked. No scientific Eval/interpreter/arithmetic/CAS/program/enumeration/solver/replay/newGO/private approximate scout/backconversion. Prior metadataassembly has exactseparatecharacterizations; no cleanexecution/cognition census.

## 1. ENTIRE variable scope; no localdistinctness hypothesis

Use the FULLPRODUCTmodel and ALLindependentLatinplacements inv64, with ODDm>=3. Thus U_0,U_1 are ANYtwo ONBs ofC^m, V_j are ANYm ONBs ofC^2, lambda_i are ANYindependentLatin squares oforderm andmu_j ANYindependentLatin squares oforder2, with

    q_((i,k),(j,l))
       =u_(i,lambda_i(j,k)) tensor v_(j,mu_j(i,l)).

Here i,l arebinary, j,k rangeoverm labels. NEITHERlocalrayfamily is assumed distinct. Entire coincident/partiallyoverlapping/orthogonallydecomposablebasis cases are INCLUDED. No complexphase, MUB, realness or chosencontrol is imposed.

The theorem is STRONGERthanv64 on oddm: there is NOSINGLEquantumtransversal evenwhen the array is nonmaximal. The earlierv64scope remainsimmutable; this is a prospectivestrengthening, not a backdated blanketclaim. Gaussian/A5/common-sector/classifier/NR inputs are absent.

## 2. A hypotheticaltransversal forces integer first-factor multiplicities0,1,2

Suppose an actualquantumtransversal T existed. Its2m unitproductvectors are anONB ofC^m tensor C^2. Partialtrace overC^2 thereforegives

    sum_(cells inT) |firstfactor><firstfactor|=2I_m.

Let n_(i,a) count selectedcells having first-factor LABEL(i,a); repetitions are permitted. Set

    A_i=sum_a n_(i,a)|u_(i,a)><u_(i,a)|.

Then A_0+A_1=2I_m. EachA_i is positive and diagonal inits ownbasis, so EVERYintegern_(i,a) is0,1or2. Since T meets eachoriginalrow(i,k) once,

    sum_a n_(0,a)=sum_a n_(1,a)=m.                (ROWS)

This does NOT assume everyfirst-factorlabel occurs exactlyonce; those multiplicities willbe derived componentbycomponent.

## 3. COMPLETEoverlap-component decomposition of the TWO arbitrarybases

Form the bipartitegraph with U_0labels on one side, U_1labels on theother, joining a,b iff<u_(0,a),u_(1,b)>!=0. Eachvertex has aneighbor because bothfamilies are bases.

For eachconnectedcomponent, the span ofits U_0vectors equals the span ofits U_1vectors. Indeed allits U_0vectors are orthogonal to all U_1vectors outside thecomponent, giving oneinclusion; the reverseargument gives equality. The componenttherefore has d vertices on EACHside and a d-dimensionalspan. Differentcomponents are orthogonal and theirdimensions sum m. This covers allzeros, allsharedrays and everyproperblockdecomposition, including d=1components.

From A_1=2I-A_0, a U_1basisvector is an eigenvector ofA_0 with eigenvalue2-n_(1,b). Nonorthogonal eigenvectors of a Hermitianoperator have the sameeigenvalue. Consequently an overlapedge forces

    n_(0,a)=2-n_(1,b).

Connectivity makes n_0 a constant r in{0,1,2} onthecomponent and n_1=2-r throughoutits otherbasis. Let D_r be the TOTALdimension ofalllevel-r components. Then

    D_0+D_1+D_2=m,
    D_1+2D_2=m by(ROWS),
    D_0=D_2,        D_1=m-2D_0.                 (ROWPAR)

Thus D_1 has the SAMEPARITYas the oddnumberm.

## 4. Exhaustivequbitbasis classes and exact columncolors

Partition the jlabels by their unorderedPAIRof projectivequbitrays V_j. Distinctclasses share no ray and no orthogonalpair, because inC^2 the orthogonalcomplement of aray is UNIQUE. Within eachclass s choose an arbitraryorientation f_(s,0),f_(s,1). EveryV_j inclasss agrees withthispair up to phases and a possiblelabelswitch.

EverybinaryLatin square has the form mu_j(i,l)=i XOR l XOR epsilon_j: its firstentry determines the otherthree by row/columnLatinity. Absorb the labelswitch ofV_j intoepsilon_j. The ACTUALqubitray ofcell(i,k),(j,l) then has orientedindex

    b=i XOR l XOR epsilon_j.

Define its ORIGINALCOLUMNcolor withinclasss as

    c=l XOR epsilon_j=i XOR b.

If classs contains k_s labelsj, the2k_s originalcolumns in thatclass have EXACTLYk_s ofeachcolorc=0,1. A transversal uses eachsuchcolumn once. Arbitraryqubitphases/orientations have notbeen restricted; this is only a proof-labeling.

## 5. ALLcomponentlevels and the columnparity contradiction

For a levelr=0or2component, exactlyONEof the twofirst-factorbases is used, and eachof its d rays appears TWICE. Those two productvectors have the SAMEfirstfactor, so theirqubitrays must be orthogonal. They belong to onequbitbasisclass and have b=0,1. Theiroriginali label isfixed, so theirtwocolumncolors c=i XOR b are DIFFERENT. Eachsuch raypair thereforecontributesonecolumnofeachcolor tooneclasss. No assumption about whichjlabels realize the pair is made.

For a levelr=1component, EACHbasislabel on BOTHsides occursONCE. Across anoverlapedge the firstfactors are nonorthogonal, so the assignedqubitrays must be orthogonal. Connectedness and the uniqueness of a qubitorthogonalpartner propagate the SAMEqubitray throughout the U_0side and its partner throughout the U_1side. Hence the WHOLEcomponent uses ONEqubitbasisclasss. If the U_0side has qubitlabelb=t, the U_1side haslabel1-t; inBOTHcases

    columncolor c=i XOR b=t.

Thus this component contributes ALL2d cells toONEcolor inONEclass, not a balancedpair.

Fix a classs. Let L_s count the level0/2 raypairs assignedthere. Let E_(s,0),E_(s,1) be the sums ofdimensions of level1components assigned to colors0,1 there. The exact2-color columncounts give

    k_s=L_s+2E_(s,0)=L_s+2E_(s,1).

Therefore E_(s,0)=E_(s,1), so the TOTALdimension oflevel1components assigned toclasss is EVEN. Sum overALLclasses: D_1 is EVEN.

But(ROWPAR) says D_1=m-2D_0 is ODD. Contradiction. QED.

This covers EVERYlevel0/1/2 component, everysharedray/zerooverlap, everyduplicatequbitbasisclass and everyindependentLatinplacement. No division, approximateangle, selectedqubitbasis or genericconnectedness assumption is used.

## 6. Complete order10 consequence and exact original gap

For m=5, EVERYarray in the entirearbitrary-complexPRODUCTconstruction has NOSINGLEquantumtransversal, regardlessof itscardinality. In particular no100ray1-RQLS10 arises. The conclusion extends to the fullwholearray row/columnpermutation/transposition/cellphase/commonphysicalunitaryequivalenceclass and reversedtensorfactororder exactlyasinv64; it is NOTa WLOG claim for arbitraryproductarrays or arbitraryoriginalQLSs.

The integerparityargument concerns the two LABELFAMILIES and their partial-trace multiplicities, NOT physicalcommonreducingsectors of the100projectors. C^2tensorfactor does not implyrank2intrinsicsector. It does not solve/exclude any entireunrestrictedintrinsic10/4+6/5+5branch; allthree remainOPEN. No original100rayresolvedwitness/unrestrictedno-go, configured-family/formal/kernel/human/finitechecker/control/vendor/priority/current-openness/noveltypromotion.

An ENTIREreview must reconstruct partialtrace/ALLmultiplicitybounds; the exactequal-dimensionoverlapcomponents and allrlevels; arbitraryqubitbasiscoincidence/orientation classes; the XORcolumncolor identity for EVERYbinaryLatinmu_j; balancedlevel0/2pairs versus samecolor2d level1components; and the finalROWPAR/COLPARparitycontradiction. A maximal-onlydistinct-basis proof or a chosenphaseexample is NOTthis newcomplete scope.

Livev151A/B remains immutableENTIREv2/asofS55/96claims/9branches. This furtherUNREVIEWEDsource belongs only in a NEWCOMPLETEfutureunion retaining ALLolderbranches/independentlyunrestrictedS50/S33/the distinctNRconditionalBH5applications/BOTHactualflatfactorizations. No livegateexpansion or inheritedparentreading/adoption. Allhistoricalfindings/withdrawals/source/clock/cadencehistories andZERO-creditquarantinespersist. SameHOLD/noGO/18/exclusive-root/30minactualsubstantivecadence/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark.
