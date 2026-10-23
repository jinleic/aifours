# Sun k7: K62-A and corrected triple-granularity clique exclusion

Recorded at 2026-10-19T02:39:50-0700.

**CORRECTNESS-ACCEPTED SCOPED PARTIALS**, with the mandatory source errata and parent wording overlays below. No computation is a premise.

## Accepted statements

1. **K62-A:** no class-K6.2* configuration has e_d=2 and f_c=1 for every ordinary c∈C∖{i*} (the3-marker is absent or sits on i*). The5-marker may be anywhere; e*, f* and5exponents are arbitrary within the class.
2. **TG:** for finiteG and finite-indexsubgroups, or in their common finite-core quotient with induced density, putX_j=U_vU_j andT=[G:U_a∩U_b∩U_c]. Then mu(X_a∩X_b∩X_c)≥1/gcd(n_v,T). Disjointcosets are not needed for this lemma.
3. **K63-CLIQUE:** no class-K6.3 configuration has alpha_ab=alpha*_ab=3 for ALL distincta,b∈C. This is the corrected full-clique theorem, NOT the withdrawn single-star theorem. Arbitrarygroups follow byR0.

## Evidence

**K62-A mandatorytext**
- [K62-A-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K62-A-v1.md) `d3cde0bf343cd0c42a51a7e9673fbe10d86dc5ded7ccd5ccf45a2933e07da6b5`
- [K62-A-erratum-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K62-A-erratum-v1.md) `7fbea76c238788a12a9ee8c244ce437aca584ec0985f27ec95680d5445f30bb4`

**TG/CLIQUE mandatorytext**
- [K63-TG-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K63-TG-v1.md) `3e6a7cf604027a60f5e0b055c5d203cc0c167e08ca59ac81c36fc3a943ebc071`
- [K63-TG-erratum-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K63-TG-erratum-v1.md) `1dbcac91c17af170c752efd569a5bdbc37047cab852819a832029aa574fe0bdf`
- [K63-TG-erratum-v2.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K63-TG-erratum-v2.md) `22ccda2faff32b04b8aaa72646fc84038dc0a3942dc39fd59641e49beced8ec3`
- [K63-TG-erratum-v3.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K63-TG-erratum-v3.md) `4cb34dda31eb2a251ee10fd5b3fc198984612a4a6583bc448fb74f9ba191724f`

- [Codex](sun7-K62A-TG-codex-v1.prompt.stdout.txt) `70800db389a9ea3f9fd5aee2b9fd0dd5176f81262cf3d069ce936c5864c7d30d`: ACCEPT allthree,0FATAL/0MAJOR/0MINOR. Actual CLIgpt-6.1-sol.
- [Claude](sun7-K62A-TG-claude-v1.prompt.note.md) `81733b6d2e721734eafff09e34f097e5694e6a8d1786f37a7b267ee3517da033`: allcorrect,0FATAL/0MAJOR;4MINOR forK62-A,2MINOR forTG,7MINOR forCLIQUE, plusoptionalsharpenings. Actual CLIclaude-opus-5-5.

Parentreadallcandidate/erratatextsandbothreports. ParentidentifiedtheoriginalCLIQUEstarhypothesisgapbeforeCLIreview; erratumv2suppliesallinneredges3, andv3suppliestheno-i*branch. Thosearemandatory, noteditorialoptionalnotes.

## Parent mathematical checks

Atd inK62-A, allsixlocalindexgcds equal3. Uniform1/3weightsforcealpha_di*=1bystrictLFC; inversionforcesalpha*_di*=1. Ati*, weightsincludingtheisolateddcontribution3/2andexplicitfive-neighbourclassweightsleaveonly(2,2,4,4,4). Bothorientationsneedthree4positionsamongfivepositions, disjointbyINV, impossible.

TGfollowsbecauseU_v(U_a∩U_b∩U_c)liesinsideallthreeXsetsandhasmeasureQ/(n_vT), withlcm(n_v,T)|Q. ForCLIQUEchoosev∈Cwith e_v=f_v=1; atleastfourchoicesexist. EverytripleofotherCverticeshasT=Ltau,3|tau,tau≤9, sotau∈{3,6,9}andgcd(n_v,T)=6. TGboundsall10tripleunionsofYsetsby5/6. TightnessgivesD_c=Y_c,eachmeasure1/2; VFC/Sun4permitsatmostthreeCpiecesperfibre. Summingthe10tripleboundsandthetotalmeasure5/2gives(8/3)m1+(7/3)m2≤0; hencem1=m2=0andtheCunionhasmeasure5/6. Thedsetadds≥1/3unlessq_d=2andaneveni*exists; inthelattercaseoverlapcanonlylieinsideD_i*ofmeasure1/2, soD_dadds≥1/6. Thetotalis≥1againststrictV4≤1−1/n_v.

## Mandatory parent wording overlays (no theorem changes)

**K62-A (A-m1..4):** state theactualtransferprinciple: allowednessdependsonlyonthepairwiselabel-gcdmatrix, sothesubsetclassweightsapplyatthefive-neighbourrow. InStep2(a) chooseoneoutsidefive-classneighbourwithweight1andsety_d=0; theoutside-markedcasehask5=4,h_d=0andalpha*≥1. ThegcdreductioninStep2(b)isafterk5=0. The(2,2,4,4,4)weightedvalue4isboundedbyaddingthetwoallowedfour-setconstraints; the9/2boundarydiesbystrictness. ExplicitSuninstancesusedare2,3,4,5; Sun6unused. TheoptionalSun5-freeproofvariantisNOTpromotedhere.

**TG (B-m1..2):** thelemmaexplicitlyusesfiniteGoritscommonfinite-corequotient. ThePpairparentheticalisnavigation, notanimport. Optionalassertionthattheintersectionmeasureitselfisamultipleof1/gcd isNOTneeded/promoted.

**CLIQUE (C-m1..7):** choosevwith e_v=f_v=1explicitly. Replacegarbledoldgcdclausebycoprime(r_v,6)=1, tauhasprimes2/3,andpairwisecoprimecofactors. Combinethelabelgcdcasesas gcd(3r_c,q_dr_d)=3^[f_d≥2]2^[c=i*,q_d=2]; Sun4istheonlyload-bearingfibrerestriction, withSun2anoptionalvalidrefinementwhenf_d1. CiteVFCV1–V4andINVdirectly. EachrightU_vcosethaspositivemeasure1/n_v, som1=m2=0excludesallone/two-Cfibres. R0suppliesthearbitrarygrouplift. Probe-v14referencesarenavigationonly, notproofpremises; no e*=2restrictionandnostarformremaininthestatement.

## Remaining Sun7 frontier

- K7: both2-and3-markers, sameordifferentvertices (5anywhere).
- K6.3:3-markerondand2-markeri*inC; thefullall-3cliqueisnowexcluded,butotherpatternsarenot.
- K6.2*: e_d≥3, ore_d=2witha3-markeronanordinaryCvertex.

No fullSun(7), Lean,humanreview,noveltyorsignificanceclaim. Exploratoryempty/cappedcensusesareunchangedandremainnon-premises.
