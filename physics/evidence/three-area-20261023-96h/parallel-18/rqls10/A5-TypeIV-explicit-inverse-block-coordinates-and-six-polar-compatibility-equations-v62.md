# RQLS10 v62 — COMPLETE inverse19-coordinate formulas and EXACTsix scalar equations for polar flip-compatibility

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW complete manuscript: **Mon Oct 26 14:27:26 PDT 2026**. AUTHOR-WRITTEN CANDIDATE; exact linearinverse/polar-application proof only, NOT machine/kernel checked. No scientific Eval/interpreter/arithmetic/CAS/program/enumeration/solver/replay/newGO/private approximate scout/backconversion. Metadataassembly is separately characterized, not a cleanexecution/cognition census.

## 1. Full variables and unambiguous block indices

Import ENTIREv58/v60coordinate/block proofs and ENTIREv61exhaustivepolarparametrization, with their TypeIVv31/v34ancestors. No root alphabet, specialphase, singularvaluecontrol, genericinvertibility or chosenansatz is used. No Gaussian/phase5/NOT_RECONSTRUCTEDclassifier is an input.

For ANY matrix A in the full19-complex-dimensionalcommutant write its threeblocks as

    t=(t_ij),   i,j in{0,D,I},      trivial3space;
    eta,                          signscalar;
    s=(s_ij),   i,j in{D,p,m},      standardmultiplicity3space.

Here p is the symmetricIstandardcopy and m is the twistedcopy m0J fromv60. These p,m labels are NOT the+/-eigenspaces ofF. Allblocks refer to the SAMEA; they are not independentlychosencontrols for the polarproblem.

## 2. COMPLETEinverse map from9+1+9blocks toALL19 orbitcoefficients

The inverse of the fullv60linearblockformulas is asfollows:

    h=t_00;
    X_D=t_D0/sqrt3,       X_I=t_I0/sqrt6;
    Y_D=t_0D/sqrt3,       Y_I=t_0I/sqrt6;

    E_a=(t_DD-s_DD)/3;
    Z_D=(t_DD+2s_DD)/3;

    E_c=(t_DI+2s_Dp)/(3sqrt2);
    B_s=sqrt2*(t_DI-s_Dp)/3;
    E_b=(t_ID+2s_pD)/(3sqrt2);
    C_s=sqrt2*(t_ID-s_pD)/3;

    B_d=-sqrt(2/3)*s_Dm;
    C_d=-sqrt(2/3)*s_mD.

For the remainingdiagonalvariables set the FOURscalarintermediates

    p0=(t_II+2s_pp)/3,      q0=2*(t_II-s_pp)/3,
    r0=(eta+2s_mm)/3,       s0=2*(eta-s_mm)/3.

Then

    Z_I=(p0+r0)/2,          T=(p0-r0)/2,
    S_s=(q0+s0)/2,          A_s=(q0-s0)/2,
    S_d=(s_mp-s_pm)/sqrt3,
    A_d=-(s_pm+s_mp)/sqrt3.

Recover the individualorientedcoefficients by

    S_+=(S_s+S_d)/2,        S_-=(S_s-S_d)/2;
    P_a^+=(A_s+A_d)/2,      P_a^-=(A_s-A_d)/2;
    P_b^+=(B_s+B_d)/2,      P_b^-=(B_s-B_d)/2;
    P_c^+=(C_s+C_d)/2,      P_c^-=(C_s-C_d)/2.

Together with h,X/Y/Z,E_a/E_b/E_c andT these formulas recover EVERYone of the19complexcoordinates. All denominators are FIXEDnonzeroconstants, so ZERO/degeneratecoefficientcases are INCLUDED. No variabledivision or selectedbranch occurs.

For a direct proof, t_DD=Z_D+2E_a ands_DD=Z_D-E_a give the firsttwo-variableinverse. The DIpair is t_DI/sqrt2=B_s+E_c andsqrt2*s_Dp=2E_c-B_s, and similarlytheIDpair. For theI-diagonals, p0=Z_I+T,q0=S_s+A_s,r0=Z_I-T,s0=S_s-A_s follow from the two2-by-2systems inv60. Finally s_pm=-(sqrt3/2)(S_d+A_d),s_mp=(sqrt3/2)(S_d-A_d) give the lasttwoformulas. This proves the inverse by exactwrittenidentities, not a matrixrankprogram.

## 3. EXACTsix scalar conditions for F(A)=A

The COMPLETEfliptable inv58 shows that F(A)=A IFF exactlythe following sixindependentcomplexequalities hold in orbitcoordinates:

    Y_D=Z_D,   Y_I=Z_I,   E_a=E_b,
    S_d=0,     A_s=B_s,   A_d=B_d.              (TAGPLUS)

There are no additionalconstraints on the sevenfixedtags or on the commonvalues of the sixexchangedpairs. Equivalently thepositiveeigenspace has complexdimension13, consistentlywithv58.

Substitute the COMPLETEinverse fromsection2. The result is the following sixEXPLICITlinearequations in the sameblockentries:

    t_0D/sqrt3 = (t_DD+2s_DD)/3;                 (L1)

    t_0I/sqrt6 = (p0+r0)/2;                      (L2)

    (t_DD-s_DD)/3 = (t_ID+2s_pD)/(3sqrt2);        (L3)

    s_mp = s_pm;                                (L4)

    (q0-s0)/2 = sqrt2*(t_DI-s_Dp)/3;             (L5)

    s_pm+s_mp = sqrt2*s_Dm.                     (L6)

The intermediates p0,q0,r0,s0 are the FIXEDlinearforms alreadydefinedabove. Thus(L1)-(L6) are genuinelylinear in t,eta,s, not unprintednonlinearblackboxes. Conversely, reversing the inverse formulas gives ALLof(TAGPLUS), proving sufficiency, not just necessity. In particular(L4) and(L6) are distinctconstraints; the star andpathorientationfreedoms have not been conflated.

## 4. Complete polar application, with every singularbranch retained

Use the ENTIREv61data: ARBITRARYsix-complexcoordinate T inA_- with||T||<=1;D=(T*T)^(1/2);S=(I-D^2)^(1/2);ANYH-equivariantunitarypolarextensionW withT=WD; andANYunitaryK commutingwithD, skew-Hermitianon0<d<1, arbitraryond=0andd=1, with ALLrepeated-eigenvalueprojectionfreedomretained. Put

    P=W K S.

Compute the ACTUALthreeblocks t(P),eta(P),s(P) in the explicitv60orthonormalbasis. Then the wholeTypeIVbiunitaritycondition is equivalent to(L1)-(L6) on THESEblocks, togetherwithv61's completepolarconditions. Indeed(L1)-(L6) IFFF(P)=P, and the exhaustivev61necessity/sufficiency proves V=P+T andF(V)=P-T bothunitary exactlyat thatremainingcompatibility.

This is a COMPLETEsix-scalar version of the residualflip-eigenspaceconstraint; it is not a claim that t,eta,s can be pickedindependently of T/W/K. Their dependence on thepolardata is nonlinear. No multiplication ofF throughW,K,S is used. All d=0,d=1 and repeatedsingularvaluecases remainallowed byv61; these inverseformulas add NO genericityassumption.

The result does NOT solve those sixnonlinearbacksubstitutionconditions or assert they have an admissiblepoint. It states them explicitly for the FULLspace, without a groupconjugationtable or hiddencoordinateinverse.

## 5. Original gap, exact source boundaries and no promotion

For a MAXIMALresolvedarray, v59's diagonal-raycriterion/complexquadratic/rankbudget and v58'sswapped-cellnoncollisionbounds remain necessary. In addition one must produce an ACTUALallowed necessarilyA5-symmetry-breakingLatinresolution and EVERYremaining100-raycomparison fromv31. None is supplied or excludedhere. The originalall-variableTypeIVproblem and all unrestrictedintrinsic10/4+6/5+5remainOPEN.

An ENTIREreview must cover EVERYinversecoordinate, the radical/orientationnormalizations importedfromv60, BOTHdirections of(TAGPLUS)<=>sixblockequations, and the COMPLETEv61polarnecessity/sufficiency with everyendpoint/degeneratebranch. A selectedscalarcondition or chosenunitarycontrol is not thisfullapplication.

Livev151A/B remains immutableENTIREv2/asofS55/96claimnodes/9branches. This source is a furtherUNREVIEWEDsuccessor, onlyfor a NEWCOMPLETEfutureunion retaining ALLoldbranches, independentlyunrestrictedS50/S33, the distinctNRconditionalBH5applications and BOTHactualflatfactorizationhypotheses. No livegateexpansion, inheritedparentreading/adoption, A5/originalWLOG, witness/unrestrictedno-go, finitechecker/control/vendor/formal/kernel/family/human/current-openness/noveltypromotion.

All historicalfindings/withdrawals/source/clock/cadencehistories andZERO-creditquarantinespersist. SameHOLD/noGO/18/exclusive-root/actual30minsubstantivecadence/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark.
