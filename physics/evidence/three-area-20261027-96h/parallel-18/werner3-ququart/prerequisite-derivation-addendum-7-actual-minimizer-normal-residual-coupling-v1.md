# S1 addendum7 — actual-rank minimizer normal residual and coupled coercivity constraints

OwnerPhysicsResearch96h-2/SAMEphysics-1. Actual `/bin/date` before writing **Tue Oct 27 15:24:16 PDT 2026**. **WRITTEN AUTHOR CANDIDATE UNREVIEWED**. InputsONLYreleasedS1literalq3/rank/trace andnamedordinaryfinite-dimensionalfacts. No newsource/oldguideconsumer/scientificinterpreter/CAS/program/calculator/probe/replay. ALLoperators/factorvariationsbelowareuniversallyquantifiedsymbols; no choseninput/state/control/threshold/parameter/boundary/magnitudeisassigned/evaluated. ThispaperisNOTretroinsertedintotheearlierfinishedcandidatefreezerequests.

The resultis a faithfulnecessarysupport/complementCOUPLINGforanACTUALnegativeglobalminimizer, ifoneexists. It is NOT a construction/existenceclaim, notanoriginalsignproof, andnotanassertionthatnecessaryconditionsaresufficient. Ordinaryvariational/polynomialmethodsareprior; novelty/SOTAnotcleared.

## 1. Exact original superoperator, DISTINCT from the earlier Lambda map

DefineonthefullcomplexoperatorspaceB(H), H=(C^4)^tensor3,

`Wcal(C)=Σ_(S⊂{1,2,3})(−1/2)^|S| I_S⊗Tr_S(C)`,

withoriginalsiteinsertionsandUNNORMALIZEDpartialtraces. Inparticular theemptytermisC andthefulltermis−Tr(C)I/8. **This is NOT Lambda** fromaddenda1–2: Lambdahasthecomplementarytrace conventionanddifferentlocaloperator. No interchangeofthetwomapsisused.

Partialtrace-adjointmatrixunitsgive

`q3(C)=<C,Wcal(C)>_HS`,

includingALLcomplexmixedterms. Thelocalsuperoperators `C→C−(1/2)I_j⊗Tr_j C` areHSselfadjointinvolutionsindimension4andcommuteondifferentsites; thecoefficient4comesfromTr_j I_j. Thus

`Wcal†=Wcal`, `Wcal²=id`, `||Wcal(C)||_HS=||C||_HS`,

and `q3(C)<=||C||_HS²` forEVERYC, regardlessofrank. ThesearetheoriginalvecWreflectionidentitieswithfaithfulactualmatrixcaller, notsourcepositivityofadifferentcompression.

## 2. If the original sign fails, an ACTUAL rank-two global minimizer exists

The setofunit-HSactualrank<=2operatorsiscompact (closedrankconditionbythree-by-threeminorsandfinite-dimensionalunitsphere). Thecontinuousoriginalq3hasaminimumlambdaonit. **lambdaisthisACTUALvariationalminimum, not a chosenparameterinstance.** Ifuniversalq3>=0fails, lambda<0andaminimizerC*exists.

Rankonehasq3>=||C||²/8; rankzeroisnotunitnorm. ConsequentlyEVERYsuchnegativeglobalminimizerhasACTUALrankEXACTLY2. ChooseANYitscomplexSVD

`C*=s1u1v1†+s2u2v2†=U Sigma V†`,

withs1,s2>0, orthonormalleft/rightcolumns, ands1²+s2²=1. Equalnonzerosingularvaluesareallowed. Theearlierglobalrank-two boundgiveslambda>−3/4, hence |lambda|<1inthepresentnegativecase. No particularC*,lambda,singularratioorstateisdelivered; theentirestatementisconditionalonfailureoftheoriginaluniversalproblem.

Byhomogeneityandthezerooperatorcase,

`F(D):=q3(D)−lambda||D||_HS²>=0`

forEVERYactualrank<=2D, whileF(C*)=0. ThisSAMEoriginaldomain—notarbitraryunrelatedmaps—controlsALLfollowingcoefficientidentities.

## 3. Exact normal residual on the actual support and co-support

Set `N=Wcal(C*)−lambda C*`. ForEVERYcomplex64-by-2Z,thepath `C*+t Z V†` hasrank<=2forALLrealt; expandingFalongit,theconstanttermis0andnonnegativityforalltsforcesitslinearcoefficientzero. Thus

`Re<Z V†,N>_HS=0` forALLcomplexZ,

andHSdualityforcesNV=0. LikewiseALLpaths `C*+t U Z†` forceU†N=0. Hence

**`N=(I−UU†)N(I−VV†)`, `NV=0`, `N†U=0`.**                (Normal)

Thiscoefficientargumentisordinaryexactpolynomialvariationalalgebra: nopathvalueormagnitudeisevaluatedandnochosenboundaryprobeisrun. AllcomplexZ/phasesarequantified, not a real-operatorrestriction. No inverseofSigmaisneeded, andthereisnoextensionacrossavanishedsingularvalue.

InparticularNisHSorthogonaltoC* anditsrange/co-rangelieintheTWOactual62-dimensionalcomplements. Involution/unitaritygive

**`||N||_HS²=1−lambda²`,**

**`Wcal(N)=(1−lambda²)C*−lambda N`,**

**`q3(N)=−lambda||N||_HS²`.**                               (Residual)

Because|lambda|<1, NisNONZERO; `1<=r:=rankN<=62`. ThisrankistheACTUALnormalresidual'srank, not aninvariant/sourcecounttransferredtothecriticalcaller. No claimNisranktwooranoriginalnegativewitness: itsq3ispositiveintheconditionalnegative-minimumcase.

## 4. ENTIRE quadratic factor-path coefficient constraints

FixEITHERsingularcolumn a=1or2. Letx beANYcomplexvectororthogonaltoBOTHu1,u2, andy ANYcomplexvectororthogonaltoBOTHv1,v2. Theexactfactorpath

`C_a(t)=Σ_(b≠a) s_b u_bv_b†
                +s_a(u_a+t x)(v_a+t y)†
       =C*+t H+t² K`,

`H=s_a(x v_a†+u_a y†)`, `K=s_a x y†`,

hasACTUALrank<=2forEVERYrealt, includinganydegeneration. Thevectorsx,yarearbitrarycomplexinputs, soallrelativephasesandalltangentnormalmixedcouplingsarepresent. Thepathisnotanumericalperturbation/probe.

ThefollowingareEXACT, includingallouter/innercrosses:

`F(C_a(t))=t²[A+2t B+t² D]`,

`A=q3(H)−lambda||H||²+2 Re<K,N>`,

`B=Re<H,(Wcal−lambda id)K>`,

`D=q3(K)−lambda||K||²`.

Thelinearcoefficientvanishesby(Normal); constantF(C*)=0. TheformulausesfullWcal—notdiscardedpartialtraces. Intheseactualsupportpositions<H,K>=0and<C*,K>=0, butthenorm-subtractionhasbeenleftintheformulaforBtoshowthewholecoefficient. No falseD²=0/co-Choireferenceisinserted.

NonnegativityforALLrealtisthereforeequivalenttotheordinaryrealquadraticconditions

**`A>=0`, `D>=0`, `B²<=A D`.**                              (Path)

IfD=0thismeansB=0andA>=0; nozero-denominatordivision. FornonzeroK itsactualrankoneboundgives `D>=(1/8−lambda)||K||²>0` intheconditionalnegativecase. Ifxoryiszero, K=0andthedegenerateconditionsstillhold. TheSVDsingularvaluemultiplicitydoesnotaffectanyidentity.

TheseareNECESSARYforanactualnegativeglobalminimizer. ThepaperdoesNOTassertthatanyfreelyspecifiedA,B,D,Nsatisfyingthemcomesfromtheoriginalmap/caller, or thattheyexcludeALLactualminimizers.

## 5. A concrete necessary normal-residual coercivity bound

Since `q3(H)<=||H||²` globallyand `||H||²=s_a²(||x||²+||y||²)`, conditionA>=0forcesforalltheSAMEcomplexx,y

`0<=s_a²(1−lambda)(||x||²+||y||²)
                       +2s_a Re<x y†,N>`.

Divideonlybys_a>0. Because `<x y†,N>=x†Ny`, thissaystheACTUALcomplementblockoperator

`[[ gamma_a I_(Uperp), N ],
  [ N†, gamma_a I_(Vperp) ]] >=0`,

`gamma_a=s_a(1−lambda)>0`.

Theordinaryscalar-diagonalSchurcompletion, validbecausegamma_a>0, gives

**`||N||_op <= s_a(1−lambda)` for BOTH a, hence
  `||N||_op <= s_min(1−lambda)`.**                          (Coerc)

Nophaseischosen/probed: blockPSDusesALLcomplexx,yatonce. Thisisnotanassumptionthatthefullcriticalsourceisthepositiveblockfromanothermap; itwasdeducedfromtheactualrank-preservingpaths ofC*.

Combine(Residual), theACTUALrankr andtheelementarysingularvalueinequality||N||HS²<=r||N||op². Since1−lambda>0,

**`r s_min² >= (1+lambda)/(1−lambda)`,
  `s_min² >= (1+lambda)/(62(1−lambda))`.**                   (Support)

Thusanyactualnegativeglobalminimizerhasthisquantitativejointnormal-residual/source-singularvalueconstraint. Itisnotanargumentthatno suchminimizerexists, notaparameterregion/thresholdselection, andnotanunprovedsparse-boundaryinverseextension. No numericalvalueoflambdaoranycandidateinputisassignedorchecked.

## 6. What was gained and what remains exactly unpaid

Genuineprovednecessarycoupling:(Normal),(Residual), FULLmixedpathconditions(Path), andinparticular thecoerciveupperbound(Coerc)/sourcebound(Support)ontheSAMEoriginalglobalminimizer'sactualnormalresidual. Thesearemorethanmerelynamingacoordinatematrix, but remain **auxiliarynecessaryconditions**, notpositivityoracounterexample. Classicalvariational/Schurmethodsandpossibleknownanaloguesareprior; noveltyandSOTAunverified. Itwouldbeincorrecttocounttheseconditionsasprogressontheoriginalsignbythemselveswithoutanactualexclusionargument.

Exactnextgap: no proofyetthatALLactualC*,lambda<0withtheliteralWcalareincompatiblewiththeseconstraints (orwithMS/R-Pifromearlierpapers). NoactualsuchC*isfound. Substitutinganarbitraryinvolution, independentlyassigningnormalblocks/spectra, or producingasatisfyingabstracttuplewouldNOTanswerthisoriginalmapquestion. AnyproposedexclusionmustretainALLtracecouplings/source-supportnormalidentitiesandthedegeneratecasesalreadyseparatedabove.

Ordinaryimports: finite-dimensionalcompactness/continuity, fullcomplexSVD, polynomialcoefficientnonnegativity/duality, originalHSselfadjointinvolution, ordinaryrealquadraticPSDcriterion/scalarSchurcompletionandactualmatrixsingularvaluebounds. No unprovidedpublishedlemma, calculator/CAS/program/probe or oldheldscientificguide.

AllproofsWRITTEN/notpeerorparentadopted; source-bookequivalence/formal-human-family-executable-noveltygatesremainOPEN. Same18/NEWOWN/S0S1/oldroundCLOSED_FROZEN/STOPoutsideS1/HOLDv2/ALLZEROHELD/permanentfindings/nonblindpriorhistory/N4UNKNOWNhistoricalchildexitUNESTABLISHED/aux214STOP/deadline2026-10-31T21:23:27Z/noearlyparkpersist.

**END COMPLETE S1 ADDENDUM7 — ACTUAL MINIMIZER COUPLING NECESSARY ONLY; ORIGINAL W4 STILL OPEN.**
