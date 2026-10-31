# RQLS10 v61 — Exhaustive six-complex-difference/polar parametrization of the ENTIRE TypeIV biunitary problem

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW complete manuscript: **Mon Oct 26 14:24:48 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact finite-dimensionalC*-algebra/polar/spectral proof only, NOT machine/kernel checked. No scientific Eval/interpreter/arithmetic/CAS/program/enumeration/solver/replay/newGO/private approximate scout/backconversion. Earlier metadataassembly has separateexactsource/outputcharacterization; no cleanexecution/cognition census.

## 1. Full scope and the remaining nonlinear compatibility, not a chosen control

Use ENTIREv31/v34/v58/v60TypeIValgebra/flip/coordinate/block proofs. A=Comm(U(S3)) is the FULL19-complex-dimensional C*-algebra, and F:A->A is its complexlinear Hilbert-Schmidtunitary involution. Write A_+ andA_- for its linear+/-eigenspaces, ofcomplexdimensions13and6. The ENTIRErow/columnQLScondition is V inA withV andF(V)BOTHunitary.

No coefficient, phase, singularvalue, orientation or seedcontrol is chosen here. We parametrize ALLsuchpairs, including everyzero/one/repeated singularvaluecase. No Gaussian/phase5/tenthrootpair or NOT_RECONSTRUCTEDclassifier is used. A5covariance remains explicit, NOT originalWLOG.

The residualcondition F(P)=P below is LINEAR INP, but P itself is a nonlinearpolar/spectralfunction of the parameters. It is NOT sixlinear equations in sixfreecomplexnumbers, not a solvedsystem, and not an implicitGO. The fullLatinresolution and100raymaximality remain separate.

## 2. Exact parametrization: every branch and every degree of freedom

Take the following data:

(A) An ARBITRARY T inA_- with operatornorm<=1. Its SIXcomplexcoordinates are the u_D,u_I,u_E,u_S,u_+,u_- ofv58; its ACTUALtrivial/sign/standardblocks are the FULLformulas inv59/v60. Let

    D=(T*T)^(1/2),       S=(I-D^2)^(1/2).

These are positiveoperators inA. Their definitions use exactpositivefunctionalcalculus, not a numericalsquare-root or executedranktest.

(B) Aunitary W inA extending the polarpart ofT, so

    T=W D.

ALLunitaryextensions onkerD are allowed. Such an extension ALWAYSexists insideA: in eachsquare3-by-3/scalar/3-by-3multiplicityblock, extend the polarpartialisometry between its equal-dimensionkernelcomplements, and match the remainingleft/rightkernels unitarily. The standardrepresentation factor remainsidentity. No externallychosenextension is silentlyWLOG.

(C) Aunitary K inA commuting withD, with the COMPLETEspectralconditions:

    on0<d<1:    K*=-K on the wholeD-eigenspace;
    on d=0:     arbitraryunitary on that kernel;
    on d=1:     arbitraryunitary, irrelevantto KS there.

On an interioreigenspace, K may be ANYskew-Hermitianunitary, equivalently i(P_+-P_-) for complementaryorthogonalprojections there, compatible with the H-action. Repeatedsingularvalues therefore retain ALLallowedcontinuousprojectionfreedom; they are NOT reduced to oneglobal sign or a genericdistinct-spectrumassumption. K commuteswithD, hencewithS. The0and1branches are not obtained by illegallydividing byD orS.

(D) Form the ACTUALmatrix

    P=W K S,

and impose the EXACTremaininglinear-eigenspacecondition

    F(P)=P.                                     (PLUS)

Here F is applied to the WHOLEproductP using the fullv58/v60coordinateformulas. F is NOT a product- or adjoint-homomorphism; no identity F(WKS)=F(W)F(K)F(S) is used or valid in general.

Then set

    V=P+T,       B=P-T.                          (PAIR)

The claim is: these data with(PLUS) yield precisely ALLTypeIVbiunitaryseeds, up to harmlessredundancy amongpolarextensions/spectralchoices. No one-to-oneparametrization or actualsolution of(PLUS) is claimed.

## 3. Complete sufficiency proof

Because K commuteswithD,S, both

    (D+KS)*(D+KS)=I,
    (D+KS)(D+KS)*=I

follow from D^2+S^2=I and

    DS(K+K*)=0.

The lastidentity holds on EVERYspectralbranch: D=0 orS=0 kills the product, and the interiorbranch hasK+K*=0. The samecalculation with MINUSinplaceofPLUS proves D-KS unitarytoo. Multiplying bytheunitaryW gives V=W(D+KS) and B=W(KS-D), bothunitary. The harmlessoverallminus inB relativetoW(D-KS) preservesunitarity.

T lies inA_- andP inA_+, so byLINEARITY

    F(V)=F(P)+F(T)=P-T=B.

Thus the wholemasterrow/columnQLScondition holds, not merely onecolumn/normtest. No resolution/maximality has been supplied by this argument.

## 4. Complete necessity proof, including all singular/degenerate branches

Conversely let V andB=F(V) be ANYtwo unitaryseeds in the fullmaster. Put

    P=(V+B)/2 inA_+,
    T=(V-B)/2 inA_-.

The unitarytriangleinequality gives ||T||<=1. TakeD and ANYunitarypolarextensionW as insection2, and put C=W*P. Expanding BOTHV/Bunitarities on bothsides gives

    C*C=CC*=I-D^2=S^2,
    D C+C*D=0.                                 (CS)

In particular C is NORMAL and commuteswithC*C=S^2. Since D=(I-S^2)^(1/2), exactfunctionalcalculus gives[C,D]=0. The crossidentity in(CS) is therefore

    D(C+C*)=0.

On a D-eigenspace with0<d<1, S is an invertiblepositiveSCALAR, so K=C/S is a unitary commutingwithD and hasK*=-K. On d=0, C is alreadyunitary and setK=C. On d=1, C=0; choose ANYunitaryK on that eigenspace, which cannot changeKS=0. This constructs K inA on ALLspectralbranches, including repeatedeigenvalues and everykernel. Hence C=KS, P=WKS andF(P)=P. Thus all data/conditions ofsection2 are NECESSARY.

This completes the two-sidedparametrization. No scientificprogram, numericalSVD, positive-eigenvalueapproximation or genericinvertibility assumption appears in eitherdirection.

## 5. Full maximal-resolution application and exact limitations

For a candidateMAXIMAL1-RQLS10 insideTypeIV, use the SAMEfullparametrization, not a selectedT. The v59noncollapseddiagonalcriterion and its quadratic/rankbudget remain necessary:

    |h+3X_D+6X_I|^2<10,
    u_D*(u_I-u_+-u_-)=2*u_I*u_E,
    0<beta_D<1, 0<beta_I<1,
    3beta_D+6beta_I<=8.

They are additionalnecessaryfilters on the resultingV, NOT assumptions built into the exhaustivebiunitaryparametrization: the latter deliberately retains the nonmaximalcollapseddiagonalbranch too.

Even after satisfying allthese, one must stilldeliver an ACTUALallowed necessarilyA5-symmetry-breakingLatinresolutionL and EVERYstrict100raycomparison ofv31. Neitherexistence nor impossibility of suchdata has been established. T=0/pureF-eigenvectors and singularboundarycases are not silentlyused as stand-ins for the fullproblem.

The newrepresentation replaces searching all19complexseedentries directly by the explicit6complexantisymmetricoperator, its FULLcommutantpolarextensions and ALLspectralphase/projectionfreedom, with exact(PLUS)compatibility. It does NOT pretend those freedoms are independent, drop degeneratebranches, or reduce the originalproblem toA5WLOG.

## 6. Immutable review/assurance boundary

An ENTIREreview must cover BOTHdirections, unitarypolarextension inside thecommutant, Cnormal=>commutationwithD, EVERYd=0/interior/d=1/repeatedspectralcase, the nonscalarH-compatibleinteriorprojections, and the crucial nonmultiplicativity ofF. A diagonalpolarcontrol or onegenericinvertibleexample is NOT this fulltheorem.

Livev151A/B remains immutableENTIREv2/asofS55/96claimnodes/9branches; this furtherUNREVIEWEDsource belongs only in a NEWCOMPLETEfutureunion with ALLoldbranches, independentunrestrictedS50/S33, the distinctNRconditionalBH5applications and BOTHactualflatfactorizations retained. No livegateexpansion, parentreading or adoption is inferred from metadata.

All unrestricted originalintrinsic10/4+6/5+5remainOPEN. No actualoriginal100rayresolvedarray/unrestrictedno-go, A5-WLOG, finitechecker/control/vendor/formal/kernel/family/human/current-openness/noveltypromotion. All historicalfindings/withdrawals/source/clock/cadencehistories andZERO-creditquarantinespersist. SameHOLD/noGO/18/exclusive-root/30minactualsubstantivecadence/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark.
