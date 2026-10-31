# RQLS10 v66 — ODDcontrolled-qubit parity forbids a transversal for ARBITRARYfirst-factor states

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW complete manuscript: **Mon Oct 26 15:26:10 PDT 2026**. AUTHOR-WRITTEN CANDIDATE; exact completeproduct-basis/dimension/binarycount proof only, NOT machine/kernel checked. The REQUIREDprimary-definition/interfaceaudit was delivered FIRST: `S64-primary-definition-original-interface-audit-v1.md`,90LF,SHA256`8571d752b313e8f8f4fbe096fdbc5c3209af0258c28fb6c80180b6d54a74d4ba`. No chosenparameter/state/control/probe, scientificEval/interpreter/arithmetic/CAS/program/enumeration/solver/replay/nativeGO/private approximate scout/backconversion is used.

## 1. Entire newvariable scope, with NOrow-rectangle assumption

Let m>=3 beODD. Label rows(i,k) andcolumns(j,l), where i,l arebinary andj,k rangethroughm labels. For eachj choose ANYqubitONB V_j={v_(j,0),v_(j,1)} and ANYbinaryLatin squaremu_j. For EVERYcell choose an ARBITRARYunitvector

    x_(i,k,j,l) inC^m.

The wholearray consists ofunitproductvectors

    q_((i,k),(j,l))
       =x_(i,k,j,l) tensor v_(j,mu_j(i,l)).       (CONTROL)

The firstfactor may depend on ALLFOURindices, includingl. It need not come from twofixedbases, a rowrectangle, anyQLS(m), a phasealphabet or a commonset oflocalrays. Allqubitbasiscoincidences/orientations areallowed.

We do NOTclaim everychoice of thesefirstfactors makes rows/columnsONBs. The theorem is stronger: NOarrayofunitvectors ofform(CONTROL) can have an ACTUALquantumrow/columntransversal, whetherornot the restof itsrow/columnQLSconditions happen tohold. No positiveordinaryQLS/nonemptymaximalclass claim is beingcomposed.

## 2. Complete qubitbasis-class structure of ANYorthonormal productbasis

Suppose forcontradiction that a quantumtransversal T existed. Its2m orthonormalproductvectors form anONB ofC^m tensorC^2. Partition thejlabels into classes s by theirunorderedPAIRofprojectivequbitrays. Distinctclasses share neither a ray nor an orthogonalpair: inC^2 an orthogonalpartner isunique. Let k_s be the number ofjlabels inclasss.

Choose a proof-orientation f_(s,0),f_(s,1) ineachclass. Among the selectedproductvectors inclasss, let n_(s,b) be the number withqubitray f_(s,b), and let W_s be the span of ALLtheir firstfactors. Cross-classqubitrays have nonzerooverlap, so the firstfactors fromdifferentclasses are mutuallyorthogonal. Hence the W_s are pairwiseorthogonal. Putd_s=dimW_s; then sum_s d_s<=m.

Within a fixedclass and fixedqubitrayb, thefirstfactors are orthonormal, so n_(s,b)<=d_s. Since T is a2m-elementONB,

    2m=sum_s(n_(s,0)+n_(s,1))
       <=2 sum_s d_s<=2m.

ALLinequalities areequalities. Therefore for EVERYclass

    n_(s,0)=n_(s,1)=d_s.

T uses eachoriginalcolumnonce, so it has EXACTLY2k_s cells inclasss. Thus

    d_s=k_s,
    n_(s,0)=n_(s,1)=k_s.                        (QBAL)

This proves the needed COMPLETEproduct-basisdecomposition without a two-fixed-basis, connected-overlap or localdistinctness hypothesis. Bothqubitgroups inclasss are ONBs oftheSAMEW_s, and the W_s orthogonallypartitionC^m. Everyclass, zerooverlap and repeatedbasis case is retained.

## 3. Exactcolumncolors for ALLbinaryLatincontrols and orientations

EverybinaryLatin square has mu_j(i,l)=i XOR l XOR epsilon_j. Arbitrarylabelswitches betweenV_j and itsclassorientation are absorbed intoepsilon_j; phases do not affectqubitrays. The actualorientedqubitlabel inclasss isthen

    b=i XOR l XOR epsilon_j.

Define the originalcolumncolor

    c=l XOR epsilon_j=i XOR b.

The2k_s columns(j,l) belonging toclasss include EXACTLYk_s ofcolor0 andk_s ofcolor1. A transversal uses eachcolumnonce. This is a proof-labeling oftheFULLdata, not a chosenphysicalbasis/control.

## 4. The complete2-by-2 count table forces an EVENnumber ofrow-part cells

For eachclasss let N_(i,b) count itsselectedcells withoriginalrowparti andorientedqubitlabelb. By(QBAL), BOTHqubitcolumns ofthistable sumtok_s. By the exactcolumncolors, BOTHparity-diagonals sumtok_s:

    N_(0,0)+N_(1,0)=k_s,
    N_(0,1)+N_(1,1)=k_s,
    N_(0,0)+N_(1,1)=k_s,
    N_(0,1)+N_(1,0)=k_s.

Subtracting gives

    N_(0,0)=N_(0,1),
    N_(1,0)=N_(1,1).

Thus EVERYclass contains an EVENnumber ofselectedcells fromrowparti=0, andalso an EVENnumber fromrowparti=1. SummingoverALLclasses, the wholeT contains an EVENnumber from eachrowpart.

But T meets eachoriginalrowonce, and there are mrows ineachpart. Thatnumber isODD. Contradiction. QED.

The proof covers ARBITRARYcell-dependentfirstfactors, ALLqubitONBs/coincidences/phases, ALLbinaryLatinmu_j and EVERYpotentialtransversal. No rowrectangleconstruction, partial-traceintegermultiplicityassumption, selectedparameter or first-factoroverlappattern is needed.

## 5. Registeredoriginalinterface and exactscope

Atm=5, ANYordinaryQLS10 whoseentries admit(CONTROL) has NOSINGLEquantumtransversal, independentlyofcardinality. The exactregisteredoriginalcondition requires ONESETTENmutuallydisjointquantumtransversals covering100cells, equivalentlyaCLASSICALorthogonalQLS10mate by the actuallyreadDefinition1.1/ENTIRELemma2.2 paid intherequiredprimaryinterfaceaudit. Such a resolution would contain at leastONET, contradictingthis theorem. Therefore noneofthesecontrolled-qubitQLS10arrays can be anoriginalmaximal1-RQLS10witness.

This is a fullmodeltheorem, NOT a WLOG claim for arbitraryproduct-stateQLSs, arbitrarycommon5+5sectorplacements or arbitraryoriginalarrays. The two rowparts/columnpairs and the binaryLatinqubit-controlpattern are REALhypotheses. Commonphysicalunitaries, wholearrayrow/columnpermutations/transposition, cellphases andfactor-swapunitaries preserve the no-transversalconclusion andgive the fullequivalenceclass, but do NOTerase those hypotheses.

When everyV_j isthesamebasis, the model includes a particularbinarycontrolled5+5sectorpattern, not ALLpossible5-plexplacements. When basesvary, the qubitfactor still does NOTimply anintrinsicrank2commonreducingsector. Allunrestrictedintrinsic10/4+6/5+5branches remainOPEN. No original100rayresolvedwitness/unrestrictedno-go, genericmaxordinaryQLS-as-originalpromotion, A5/Gaussian/NRimport, finitechecker/control/vendor/formal/kernel/family/human/current-openness/noveltypromotion.

This proof is source-independent ofS64/S65mathematics: it generalizes their controlledqubitpattern but does NOTretroactivelyreview/adopt theirwrittenproofs or their even-m scopes. Its own ENTIREreview must cover the completeorthonormalproductbasisclass-dimensionequality, actualcolumncount2k_s, ALLbinaryLatin/orientationreductions, EVERYcount-tableequation and the registeredR=>Tapplication.

## 6. Laterprocessassurance and immutable reviewscopes

Livev151A/B remains immutableENTIREv2/asofS55/96claimnodes/9branches; this newUNREVIEWEDsource is onlyfor a NEWWHOLEcurrentfutureunion retaining ALLoldbranches/independentlyunrestrictedS50/S33/NRconditionalBH5applications/BOTHactualflatfactorizations. No livegateexpansion or inheritedparentreading/adoption.

The laterparentv138processrecord was ACTUALLYreadCOMPLETE39LF and isbound inwholeunionv10: TWOadditionaldistinctMainnumberedroundcheckpointCADENCEPROCESSMAJORS103to104FULL30m02 and104to105FULL31m10 atrecordedPRECREATIONobservations, NOTexactnativewrite/runtimeclocks. They persistwithALLolderfindings, notnewmathfalsity/STOP/GO/reviewrestart/continuous18wayclaim. SameHOLD/noGO/18/exclusive-root/actual30minsubstantivecadence/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; allwithdrawals/source/clock/cadencehistories andZERO-creditquarantinespersist. Metadataassembly has separateexactcharacterizations, not a globalcleanexecutioncensus.
