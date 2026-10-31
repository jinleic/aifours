# RQLS10 v64 — ENTIRE arbitrary-complex qubit/row-rectangle product model has NOsingle quantum transversal when maximal

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW complete manuscript: **Mon Oct 26 14:55:17 PDT 2026**. AUTHOR-WRITTEN CANDIDATE; exact tensor-ray/orthogonal-subspace proof only, NOT machine/kernel checked. No scientific Eval/interpreter/arithmetic/CAS/program/enumeration/solver/replay/newGO/private approximate scout/backconversion. Earlier metadataassembly has exactseparatecharacterizations; no cleanexecution/cognition census.

## 1. ENTIRE variable model, with every complex basis and independentLatin placement allowed

Let m>=2, with physicalspace C^m tensor C^2. Choose ARBITRARYorthonormalbases

    U_i={u_(i,a):a inA},      i in{0,1}, |A|=m,
    V_j={v_(j,b):b in{0,1}},  j inJ, |J|=m.

No phase alphabet, realness, unbiasedness, nonzero-cross-overlapcondition or specialmatrix is imposed. For EACH i independently, choose ANYLatin square

    lambda_i:J xK ->A,       |K|=m.

For EACH j independently, choose ANYLatin square oforder2

    mu_j:{0,1} x{0,1} ->{0,1}.

The actualarray has rows(i,k), columns(j,l), and entries

    q_((i,k),(j,l))
       =u_(i,lambda_i(j,k)) tensor v_(j,mu_j(i,l)). (PRODUCT)

This contains the standard row-quantum-Latin-rectangle product construction at2-by-m/m-by-2, but allows independentLatin placements rather than onlycyclicshifts. It is an ENTIREall-variable productmodel, not a chosencontrol or a WLOG representation of arbitraryQLSs.

The standardconstruction is publiclydescribed, e.g., Huang-Li arXiv:2606.27758v1section2.1/Lemma2.1. That source is attributionONLY: everyfact needed here is proved below; no existence/classification theorem or sourceNR import is used. The presentmodel is different from v14section6's phasedtensor-Fourier/companion construction, which is not an input and must not be revived by sharing the wordtensor.

## 2. Full ordinaryQLS proof, with no hidden placement restriction

Fix row(i,k). For differentj values, lambda_i(j,k) are distinct by columnLatinity, so the firstfactors are orthogonal. For the samej, the two l values give the twoV_jbasisvectors by rowLatinity ofmu_j. Hence all2m entries of thatrow are anONB.

Fix column(j,l). For differenti values, mu_j(i,l) are different by columnLatinity ofmu_j, so the qubitfactors are orthogonal. For the samei, distinctk give distinctlambda_i(j,k) by rowLatinity, so the firstfactors are orthogonal. Thus everycolumn is anONB too. Allentries areunitvectors. This proves that EVERYchoice of the fullstateddata produces an ordinaryQLS(2m).

## 3. EXACTmaximality criterion for the wholecartesian factorfamily

For eachlocalfactorlabelpair((i,a),(j,b)), the equations

    lambda_i(j,k)=a,        mu_j(i,l)=b

have UNIQUEsolutionsk,l. Therefore the(2m)^2 cells of(PRODUCT) enumerate the COMPLETEcartesianfamily

    {u_(i,a) tensor v_(j,b): all i,a,j,b},

eachlabelpair ONCE.

Two unitproductvectors x tensor y andx' tensor y' define the samecomplexprojectiveray IFF bothfactorpairs define the sameprojectiverays. Necessity follows by taking the two partialtraces of their equalrank-oneprojectors; sufficiency follows by multiplyingthe two scalarphases.

Consequently(PRODUCT)has maximal(2m)^2distinctrays IFF BOTHlocalfamilies

    all2m rays [u_(i,a)],
    all2m rays [v_(j,b)]

are distinct. Aduplicate in eitherfactorfamily repeats an actualglobalray by fixing ANYray of the otherfamily. This is an iffcondition, not an extra genericity assumption. If it fails, the array is alreadyNOTmaximal; no no-transversal claim is made for suchnonmaximalarrays.

## 4. Qubitorthogonality across differentj is impossible in the maximalcase

Assume the localfamilies are distinct. InC^2 aunitray has a UNIQUEorthogonalray, namely the othermember of anyONB containingit. Thus ifj!=j', NOv_(j,b) can be orthogonal to ANYv_(j',b'): otherwise v_(j',b') would be proportional to the othermember ofV_j, contradicting the distinctness of ALL2m localqubitrays.

This conclusion uses onlydimensionTWO and fullmaximality. It does NOT assume mutuallyunbiasedqubitbases, a phaseform or anycondition on overlaps between the twoU_ibases.

## 5. Complete no-single-transversal proof, ALL first-factor overlap patterns covered

Suppose an ACTUALquantumtransversal T existed. It chooses exactlyONEcell in eachoriginalcolumn(j,l). Thus for eachj it chooses EXACTLYTWOcells, one incolumn(j,0) andone incolumn(j,1). Denote theirfirstfactors by x_(j,0),x_(j,1) inC^m, and put

    W_j=span{x_(j,0),x_(j,1)}.

For j!=j', section4 says EVERYrelevantqubitinnerproduct is nonzero. Orthogonality of the selectedproductvectors thereforeforces

    <x_(j,l),x_(j',l')>=0 for ALL l,l'.

Hence the mNONZEROsubspacesW_j are pairwiseorthogonal in anm-dimensionalspace. Eachhas dimensionatleast1, and theirdimensions sumatmostm. Therefore EACHW_j has dimensionEXACTLYONE.

For a fixedj, its two selectedfirstfactors must consequentlybe proportional. By the distinctness of all2m U-familyrays, theirlabelsi andlambda_i(j,k) must be IDENTICAL. In particular theiri labelsagree, and rowLatinity oflambda_i at thatj forces theirk labels toagree too.

The two selectedcells atj therefore lie in the SAMEoriginalrow(i,k). This contradicts the row-and-columntransversalcondition. QED.

No assumption about zeros, blockdecompositions or affinepatterns of the first-factor transition was made. The proof covers allU(m)^2choices, allU(2)^mchoices, ALLindependentlambda_i andmu_j, and EVERYpotentialtransversal—not a selectedresolution or Latinmatching.

## 6. Full originalorder10application, invariances and exact remaininggap

For m=5, EVERYarray(PRODUCT) is an ordinaryQLS10. It EITHERfails100-raymaximality OR, ifmaximal, has NOSINGLEquantumtransversal. In particular NONEcan be a maximal1-RQLS10. This closes the entirearbitrary-complex row-rectangle/qubitproductconstruction route, not merely its root-of-unity or Fourier/phaseinstances.

The conclusion is unchanged under arbitrarywholearray row/columnpermutations, transposition, independentcellphases and ANYcommonphysicalunitary, even one notrespecting the tensorfactorization. It also covers the reversedfactororder by the commonfactor-swapunitary. These invariances preserve actualraydistinctness and alltransversalresolutions; they do NOT make arbitraryproductarrays or arbitraryQLSs equivalent to(PRODUCT).

The physicalC^2tensorfactor is NOT a rank2commonreducingsector of the100projectors. No unrestrictedsectorbound, A5covariance, phase5code/classifier or Gaussianproof is an input. This branch is independent of the TypeIV/S50/S33/Gaussianbranches, and excludes NOarbitraryintrinsic10/4+6/5+5array outside its explicitproductmodel. AllthreeunrestrictedoriginalbranchesremainOPEN, and no original100rayresolvedwitness/unrestrictedno-go is delivered.

An ENTIREreview must cover the generalizedindependentLatinplacements, ordinaryrow/columnONBs, cartesianfactorlabelbijection and bothdirections ofprojectivemaximality, qubitcross-basisnonorthogonalityfromlocaldistinctness, ALLmorthogonalsubspaces and the finalSAMEORIGINALROWcontradiction, plus everyinvariance/scopeboundary. A chosenpair ofMUBs or assumingallfirst-factoroverlapsnonzero is NOT thisfullresult.

Livev151A/B stays immutableENTIREv2/asofS55/96claims/9branches. This furtherUNREVIEWEDsource belongs only in a NEWCOMPLETEfutureunion retaining ALLoldbranches/independentlyunrestrictedS50/S33/the distinctNRconditionalBH5applications/BOTHactualflatfactorizations. No liveexpansion, inheritedparentreading/adoption, originalWLOG, finitechecker/control/vendor/formal/kernel/family/human/current-openness/noveltypromotion. Allhistoricalfindings/withdrawals/source/clock/cadencehistories andZERO-creditquarantinespersist. SameHOLD/noGO/18/exclusive-root/30minactualsubstantivecadence/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark.
