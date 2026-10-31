# RQLS10 v60 — Explicit COMPLETE3+1+3 isotypic formulas for ALL19 TypeIV variables

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW complete manuscript: **Mon Oct 26 14:15:43 PDT 2026**. AUTHOR-WRITTEN CANDIDATE; exact orbit/basis/intertwiner proof only, NOT machine/kernel checked. No scientific Eval/interpreter/arithmetic/CAS/program/enumeration/solver/replay/newGO/private approximate scout/backconversion. Past metadataassembly has its own exact characterization, not a global execution/cognition census.

## 1. Complete variable scope and shorthand

Import ENTIREv31/v34 ordinaryTypeIVmaster and ENTIREv58's19complexorbitcoordinates/parity/flip table. Every coefficient h,X_D,X_I,Y_D,Y_I,Z_D,Z_I,T,S_+,S_-,P_a^+,P_a^-,P_b^+,P_b^-,P_c^+,P_c^-,E_a,E_b,E_c is unrestrictedcomplex. No chosencontrol, root alphabet, phase/realness restriction or seedansatz is imposed. The following linear change ofcoordinates is an EXACTbijection for the ENTIREcommutant, not selectednecessaryentries.

Put

    A_s=P_a^++P_a^-,      A_d=P_a^+-P_a^-,
    B_s=P_b^++P_b^-,      B_d=P_b^+-P_b^-,
    C_s=P_c^++P_c^-,      C_d=P_c^+-P_c^-,
    S_s=S_++S_-,          S_d=S_+-S_-.

The scalarT below is the trianglecoefficient, not a matrixtranspose. The A5TypeIVcovariance assumption is NOT originalWLOG. The Gaussian/phase5/tenthrootpair branch and its NOT_RECONSTRUCTEDclassifier are NOT inputs.

## 2. Literal orthonormal isotypic decomposition, including its orientation

Fix a0=12. Index the remainingpoints byv=3,4,5 and set D_v={3,4,5}minus{v}. For f in W={f inC^3:sum f_v=0}, define the isometric embeddings

    d(f)=sum_v f_v e_(D_v),
    p(f)=sum_v f_v (e_(1v)+e_(2v))/sqrt2,
    m0(f)=sum_v f_v (e_(1v)-e_(2v))/sqrt2.

On the indexspace(3,4,5) set

    J=(1/sqrt3) [ 0 -1  1 ]
                [ 1  0 -1 ]
                [-1  1  0 ].

Then J*= -J, J^2=-(I-11^T/3), so J is unitary onW. If P_sigma permutes(3,4,5), then P_sigma J=sgn(sigma)J P_sigma; this follows directly from the alternatingcrossproduct matrix, or the three entries above. Every element ofH=S3 acts on{1,2} by the SAMEparity as its permutation sigma of{3,4,5}. Hence d(f),p(f),m(Jf)defined as m0(Jf) give THREEcopies of the SAMEstandardrepresentationW: the sign twist ofm0 is exactlycancelled byJ.

The trivialspace has orthonormalbasis

    e0=e_(12), eD=(sum_v e_(D_v))/sqrt3,
    eI=(sum_v(e_(1v)+e_(2v)))/sqrt6.

The signspace has unitbasis

    s=(sum_v(e_(1v)-e_(2v)))/sqrt6.

These spaces have dimensions3+1+3*2=10 and are mutuallyorthogonal. They explicitly realize the COMPLETEdecomposition inv31. To avoid a notationambiguity, the thirdstandardcopy is ALWAYS the map f->m0(Jf), not m0(f).

## 3. The full three blocks as explicit functions of ALL19 variables

In the trivialbasis the3-by-3 block is

    M_triv =
    [ h           sqrt3*Y_D          sqrt6*Y_I               ]
    [ sqrt3*X_D   Z_D+2E_a           sqrt2*(B_s+E_c)         ]  (T0)
    [ sqrt6*X_I   sqrt2*(C_s+E_b)     Z_I+T+S_s+A_s           ].

The scalar signblock is

    eta=Z_I+S_s-T-A_s.                           (SIGN)

On the THREEstandardcopies ordered(d,p,m0J), the multiplicity3-by-3 block is

    M_std =
    [ Z_D-E_a               (2E_c-B_s)/sqrt2         -sqrt(3/2)*B_d        ]
    [ (2E_b-C_s)/sqrt2      Z_I+T-(S_s+A_s)/2        -(sqrt3/2)*(S_d+A_d)  ] (STD)
    [ -sqrt(3/2)*C_d        (sqrt3/2)*(S_d-A_d)       Z_I-T-(S_s-A_s)/2     ].

Thus V is unitarilyequivalent to M_triv directsum eta directsum(M_std tensor I_W), up to the harmlesstensorfactorordering. In particular

    ||V||_HS^2=||M_triv||_HS^2+|eta|^2+2||M_std||_HS^2.

These are the fullblocks, not just theirdiagonals or principalminors. The map from the19orbitcoefficients to the9+1+9blockentries is bijective because this is an explicitlyconstructed orthonormalbasis change on the ENTIREcommutant and allthree copies are irreducible/equivalent; no numericalinvertibility test or hiddenclassification is used.

## 4. Complete derivation of the coefficients and signs

On the threeDcoordinates, the block has diagonalZ_D and offdiagonalE_a. Its trivial/standardvalues are Z_D+2E_a andZ_D-E_a. For maps betweenD and the symmetricIcopy, the fullthree-index-coordinate maps have diagonal sqrt2*E_c and offdiagonalB_s/sqrt2 for D<-p, and diagonal sqrt2*E_b/offdiagonalC_s/sqrt2 for p<-D. Taking the uniformvector or its orthogonalplane gives respectively the offdiagonalentries in(T0) or(STD).

WithinI, when the vlabels agree, the two-by-two u=1,2 block is[[Z_I,T],[T,Z_I]]. For differentvlabels its symmetric/antisymmetricprojections have sums(S_s+A_s)/2 and(S_s-A_s)/2. Their uniform/plane eigenvalues give the Itrivial entry, (SIGN), and the two diagonalentries of(STD). The firstrow/column of(T0) are exactlythe orbit-sumsY_D/Y_I andX_D/X_I.

For the remainingFOURcrossmaps first use the untwisted m0coordinates, so that an intertwiner between an ordinary and sign-twisted standardplane is a scalar multiple ofJ. The exactv58parity labels give

    D <- m0:       sqrt(3/2)*B_d *J,
    m0 <- D:      -sqrt(3/2)*C_d *J,
    p <- m0:       (sqrt3/2)*(S_d+A_d)*J,
    m0 <- p:       (sqrt3/2)*(S_d-A_d)*J.         (CROSS)

For an explicit signanchor, physicalc=34 and columnb=13/23 have middle-b paths with parity-/+, giving the D_v=5 to m0_w=3 entry -B_d/sqrt2, while J_(5,3)=-1/sqrt3. Physicalc=13/23 and columnb=34 give middle-c paths-/+, so the m0_v=3 fromD_w=5 entry is -C_d/sqrt2, while J_(3,5)=+1/sqrt3.

For v=3,w=4 withinI, the u-coordinate two-by-two block is

    [ S_-      P_a^+ ]
    [ P_a^-    S_+   ].

Its p<-m0 entry is-(S_d+A_d)/2 and m0<-p entry is(-S_d+A_d)/2. Since J_(3,4)=-1/sqrt3 these are exactlythe lastTWO(CROSS)coefficients. H-equivariance and the one-dimensional intertwiner space propagate eachanchor to the fullstandardplane; no other sign/orientation case is leftunassigned.

Finally replace the domainm0 bym0J and project the rangem0 onto m0J. OnW, J^2=-I andJ*J=I. Thus the first andthird(CROSS)coefficients acquire a minus sign in(STD), while the second andfourth are unchanged. This proves ALLfour offdiagonal radicalcoefficients asprinted, completing the fullblock derivation.

## 5. Exact full biunitarity equations, with NO weakened acceptance criterion

AseedV is unitary IFF

    M_triv* M_triv=I3,   |eta|=1,   M_std* M_std=I3.

The ENTIRETypeIVrow/columnQLS condition is this set AND the SAMEset evaluated at the completeflipcoefficients z^tau fromv58. In otherwords allSIXblockunitarities/scalarmodulusconditions are required; substituting only normbudgets or the shared-kernelquadratic does not solve them. The secondset is not independentlychosenblockdata: it is the exactlinearflip of the SAME19variables.

Afterward one STILLneeds an actualallowedLatinresolution and everystrict100-raycomparison fromv31. No suchsolution is claimed. This is an all-variable analyticform of the fullresidual, not a proposednumericalcontrol or newexecutionrequest.

## 6. Full six-complex-variable antisymmetric blocks

Let the six ucoordinates be exactly those inv58, and put

    U_P=u_++u_-,     V_P=u_+-u_-.

Because everyprintedblock is linear in z, substituting theF-antisymmetriccoefficients gives its ENTIREsign andstandardblocks:

    eta_-=-u_I-U_P,

    M_std,- =
    [ -u_D-u_E     U_P/sqrt2          sqrt(3/2)*V_P          ]
    [ sqrt2*u_E    -u_I-U_P/2        -(sqrt3/2)*(2u_S+V_P)  ] (ANTI)
    [ 0            (sqrt3/2)*(2u_S-V_P)   -u_I+U_P/2         ].

The trivialblock is exactly(TRIV)inv59, also obtained directly bysubstituting(T0). These formulas include everynegativecoordinate, includingthe star-difference and the path-difference invisible in the trivialblock; they are not a truncation to its fourvisiblecombinations.

Thus the completev59quadratic u_D*(u_I-U_P)=2u_I*u_E constrains ONLYthe forcedtrivialblock rank, not the generallynonzerostandard/signblocks. It must NOT be confused with a rankonefullseed or used todiscard the restof(ANTI). The coupled energybound and diagonal-raydichotomy inv59 retain their exacthypotheses and are not silentlyupgraded by these formulas.

## 7. Remaining original gap and immutable review boundaries

New delivered items are the explicit orthonormal3+1+3*2decomposition, EVERYlinearentry of BOTH3-by-3blocks and thesignscalar, their fulltwo-sidedunitaritytranslation, and the ENTIREsix-variableantisymmetricblock formulas. Completeproof uses onlyv31/v34/v58, standardfinite-dimensionalS3intertwiners and the printedorbit/paritycalculations; v59 is usedonlywhen its separatequadratic/rankcorollaries are mentioned. No externalfiniteclassifier/sourceNR input is operative.

No actualbiunitarypoint, allowedLatinresolution, full100raywitness or model/originalno-go is established. The fullALL19-variable system and unrestrictedoriginalintrinsic10/4+6/5+5remainOPEN. Livev151A/B stays immutableENTIREv2/asofS55/96claims/9branches; this furtherUNREVIEWEDsourcebelongs only in a NEWCOMPLETEfutureunion with ALLoldbranches, independentunrestrictedS50/S33, distinctNRconditionalBH5applications and BOTHactualflatfactorizationsretained. No livegateexpansion or inheritedparentreading/adoption.

No A5-WLOG, scientific/executablechecker/control/vendor/formal/kernel/family/human/current-openness/noveltypromotion. All oldfindings/withdrawals/source/clock/cadencehistories andZERO-creditquarantinespersist. SameHOLD/noGO/18/exclusive-root/actual30minsubstantivecadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark.
