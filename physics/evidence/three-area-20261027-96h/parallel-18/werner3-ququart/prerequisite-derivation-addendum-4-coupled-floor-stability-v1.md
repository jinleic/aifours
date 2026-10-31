# S1 addendum4 — all-variable rank-one floor stability and SAME-operator mixed coupling

Owner PhysicsResearch96h-2, SAMEphysics-1. Actual `/bin/date` before writing **Tue Oct 27 15:02:33 PDT 2026**. **WRITTEN AUTHOR CANDIDATE UNREVIEWED**. Inputs ONLY releasedS1 definitions and namedordinaryfinite-dimensionalfacts, with displayeddefinition-onlyv1/addendum3 identities. No scientific interpreter/calculator/CAS/program/instanceprobe/enumeration, selected state/control/singularvalue/phase/overlap/boundarytrial or oldZEROconsumer. No prior-boundaryfalseblind/noninfluenceclaim. This extends the universal ORIGINALq3 work; it doesnot authorize oldSTOPpedsource/route work.

Immutable fulladdendum3 **173LF/10897B SHA256 `86b90668fc1fdd1319c14aed5b83e27082cf363e8137cbf6de4091b91ee71d53`** proved a globalactualrank<=2 lowerbound/strictgap but didnotprovide quantitative same-inputfloorstability. Thisaddendum proves thatmissing stability estimate and an ALL-variablemixedcorrelationinequality. It doesNOTprove the ultimatepositiveendpoint orchoose a parameterregion/threshold.

## 1. Exact scope and statement

Retain `m=1/8`, `W=⊗(I−E_j/2)`, `P=⊗(I−F_j/2)` and the literal originalq3 onH=(C^4)^tensor3. `B(C,D)=<vecC,WvecD>` is itsFULLsesquilinearform, conjugatelinearfirst, includingALLcomplexmixedpartialtraces. The normalized rank-one operators below are arbitrarycomplexoperators, not assumedprojectors/product operators.

For EVERYunit-HSrank-oneT=|x><y| withunitx,y, put its ACTUALnonnegativeexcess

`delta(T)=q3(T)−m`.

There exists a unit-HSfloor-attainer

`T0=zeta |h1⊗h2⊗h3><h1⊗h2⊗h3|`, `|zeta|=1`,

constructed FROMtheactualmarginals ofx andtheactualphaseofT, suchthat

**`||T−T0||_HS² <= 48 delta(T)`.**                          (Stab)

This is an ALL-inputexistence/constructionlemma, not a chosenoperator/statecontrol/test. No lower/uppercutoffondeltaisassumed, and no state/region is selected.

Consequently for EVERYtwo unit-HSrank-oneT1,T2,

**`|B(T1,T2)| <= m + sqrt(48 delta(T1))
                        + sqrt(48 delta(T2))`.**            (Mix)

NeitherTnoritsfloorapproximationis optimizedindependentlyintheoriginalq3: these are theACTUALTterms, withtheirACTUALexcesses. Theproofusesafloorapproximationonlytoestimate theirfullmixedpairing, andneverreplacestheoriginalC orrankrequirement.

For anyACTUALrank-twooriginalC and ANYcomplexSVD

`C=s1T1+s2T2`, `s1,s2>0`, `Ti=|xi><yi|`,

withorthonormalleft/rightsingularvectors, define theACTUALdelta_i=q3(Ti)−m. Then

**`q3(C) >= m(s1−s2)² + s1² delta1+s2² delta2
             −2s1s2[ sqrt(48 delta1)+sqrt(48 delta2) ]`.**    (Coupled-Stab)

This is a global ALL-variable inequality withno sampled/chosen/independentlyassigned delta, phase, state, singularratioor overlap. Rankone has thealreadyprovedm||C||² floor, andrankzeroiszero. (Coupled-Stab) is **NOTclaimednonnegative**; the ORIGINALuniversalq3>=0/actualnegativeoperatoralternative staysOPEN.

## 2. Actual diagonal excess controls all three local mismatches

Let `A_j=(I−F_j)/2` be thelocalantisymmetricorthogonalprojection. Theyactondifferentpairedsitesandcommute. Theexactproductexpansion is

`P=(1/8)I +(1/4)Σ_j A_j +(1/2)Σ_(j<k) A_j A_k
                 +A1A2A3`.

EveryproductofthesecommutingprojectionsisPSD. Forunitx,ytheactualrank-oneidentityq3(T)=<x⊗y,P(x⊗y)> thereforegives

`delta(T) >= (1/4)Σ_j <x⊗y,A_j(x⊗y)>`.

Write rho_j=Tr_(other two sites)|x><x| andsigma_j similarlyfory; theyarePSDunittraceoperators. The matrixunitlocalswapidentitygives

`<x⊗y,F_j(x⊗y)>=Tr(rho_j sigma_j)`.

Define actualnumbers `d_j=1−Tr(rho_j sigma_j)` and `D=Σ_j d_j`. TheyarenonnegativebyPSD/unittrace andlargest-eigenvaluebound (orHS Cauchy–Schwarz). Thus

**`D <= 8 delta(T)`.**                                     (Mismatch)

This retainsALLthreelocalmarginals oftheSAMEoriginalx,y andmakesno spectrum/nondegeneracyassumption.

## 3. One product ray approximates BOTH original vectors

ForEACHactualrho_j letlambda_j beitslargest eigenvalue andh_j ANYunitvector inthatmaximaleigenspace; setpi_j=|h_j><h_j|. This isordinaryspectralexistence forEVERYinput, not anevaluatedspecialstateorinstanceprobe. DegeneracyisallowedandthefollowingboundholdsforANYsuchchoice.

Since `Tr(rho_j sigma_j)<=lambda_j`,

`1−lambda_j<=d_j`.                                         (x-loss)

Thepositiveoperator `R_j=rho_j−lambda_j pi_j` hastrace1−lambda_j, annihilatesh_j, and obeys

`0<=R_j<=(1−lambda_j)(I−pi_j)`.

Puttingt_j=Tr(pi_j sigma_j) gives

`1−d_j=Tr(rho_j sigma_j)
       =lambda_j t_j+Tr(R_j sigma_j)
       <= t_j+(1−lambda_j)`.

Consequently

`1−t_j<=d_j+(1−lambda_j)<=2d_j`.                            (y-loss)

No divisionbylambda_j orany spectralgapoccurs. Inparticular thisdoesnotfailonmultiplicity/degeneratewalls.

Let h=h1⊗h2⊗h3. Commutinglocalprojectionsobey

`I−⊗_j pi_j <= Σ_j (I−pi_j)`

withtheusualsiteinsertions, eitherbytelescopingtheproductorinthejoint0/1eigenbasis. Takingexpectationsinxandyandusing(x-loss),(y-loss) gives

`1−|<h,x>|²<=D`, `1−|<h,y>|²<=2D`.                         (Both)

Theseinequalitiesaregloballyvalid: ifarighthandsideexceeds1theboundismerelyweak, not anassumedlocalregime.

ForANYa,b in[0,1], `1−ab<=(1−a²)+(1−b²)`: indeed1−ab=(1−a)+a(1−b)<=(1−a)+(1−b), and1−a<=1−a²likewiseforb. Set a=|<h,x>|,b=|<h,y>|. Thereis aunitphasezetaaligningtheHSinnerproductofTwithzeta|h><h| (ifthatinnerproductiszeroanyphaseworks). Hence

`||T−zeta|h><h|||_HS²=2(1−ab)
                         <=2[(1−a²)+(1−b²)]
                         <=6D <=48delta(T)`.

TheapproximantT0isunitHSandhasq3(T0)=m bythealreadyprovedwholefloor-equalityclassification/directlocalproducttraceidentity. Thisproves(Stab) forEVERYcomplexrank-oneTincludingdelta0, andwithnospectral/phase/overlapinstanceevaluated.

## 4. Complete mixed pairing, not only diagonal norm control

Given ANYT1,T2, constructT10,T20individually asaboveFROMthoseactualterms. Theirnormsare1. Thewholefloor-classpairingidentity inaddendum3 says

`B(T10,T20)=bar(zeta1)zeta2
             product_j[Tr(pi_(1,j)pi_(2,j))−1/2]`,

andtherefore `|B(T10,T20)|<=1/8=m` forALLsuchpairs. Norelation/orthogonalitybetweenT10andT20isassumedorneeded.

TheuniversalexactreflectionidentityW†W=I gives

`|B(C,D)|<=||C||_HS||D||_HS` forALLcomplexC,D.

Byfullsesquilinearity,

`B(T1,T2)−B(T10,T20)
       =B(T1−T10,T2)+B(T10,T2−T20)`.

Thus

`|B(T1,T2)|<=m+||T1−T10||_HS+||T2−T20||_HS`,

and(Stab) proves(Mix). This is a boundon the ENTIREactualcomplexoff-diagonalpartialtracecontraction, not just individualsummands, a real restriction, phasechoicefortheoriginaloperatoror a separatelypositivecompressedform.

Fororiginalrank-twoC's ACTUALSVD, sesquilinearitygives

`q3(C)=s1²(m+delta1)+s2²(m+delta2)
                        +2s1s2 Re B(T1,T2)`.

Use ReB>=−|B| and(Mix); collectingthemterms gives(Coupled-Stab). Alltwo-sidedrank/source-mixeddataarefromoneandthesameactualC. No assertionthatthe displayedinequality'sindividualerrorboundsarejointlysharp, nor independentmaximization/parameterselection.

## 5. Imports, precise gain and residual

Newprovedinput: the **global stability/mixed-correlation bridge** (Stab),(Mix),(Coupled-Stab), withallsitesandactualcomplexmixedterms. Theexactrational48 is adirectinequalitycoefficient6times8intheall-variableproof, not avaluefoundby parametersearch, chosenboundary/magnitudeprobeor a numericaloptimization. This suppliesagenuinecouplingestimateratherthanjustanencoding/equalitydescription. It alsoquantifiestheearlierstrict-equalityobstructionwithoutclaimingapositiveendpoint.

Ordinaryimportsonly: finite-dimensionalspectraltheorem/maximaleigenspaceexistence, positiveunittraceeigenvaluebounds, thedisplayedmatrixunitlocalswapidentity, commutingprojectionproductinequality, unitphasepolarizationinHSspace, triangle/Cauchy–Schwarz, andexactcomplexSVD. NoCAS/program/kernelverification/solver/replay, oldrawproof/signlemma oradoptedheadlineusedasapremise.

Unpaid: (Coupled-Stab)'s rightside isnotshownnonnegative forALLactualSVDterms. Thisproofdoesnotestablishthattheactualdelta- andmixedcorrelationtuplescanor cannotreacheveryformallyallowedvalue. No state/tupleissampled; noregion/thresholdinferred. FullR-Pifactor1domination/originalq3>=0oractualnegativeC/source-bookequivalence/peerparentadoption/strongerformal-human-family-executable-noveltygatesremainOPEN. No all-routeexhaustionornewGO.

SAME18/OWN/S0S1/newdeadline2026-10-31T21:23:27Z/HOLDv2/oldroundCLOSED-FROZEN/STOP116142161outsideS1/ALLZEROHELD/N4UNKNOWN historicalchildexitUNESTABLISHED/aux214STOP/permanentpriorfindings/nonblindhistoryremain. Oldpinnedfilesunchanged.

**END COMPLETE S1 ADDENDUM4 — ALL-VARIABLESTABILITYAND FULLMIXEDBRIDGE; ORIGINAL W4 STILL OPEN.**
