# Explicit forty-ray complex C4 subsystem: verified, but not completable on this 4+6 support

**Disposition: explicit finite physical-subsystem witness, supported by two same-harness written reconstructions, an independently authored exact verifier run once by parent, and a separate earlier author-code parent smoke.** There are40 pairwise nonparallel UNIT vectors in C4 on H_S={(r,c):c−r∈{0,1,5,6} mod10}. All10 restricted rows,10 columns and10 ACTUAL cyclic symbol classes L(r,c)=r+c mod10 are ONBs. Cell relabeling gives allten two-antipodal-pair support masks, without anyunitarycovariance assumption.

**This is NOT a100-ray RQLS10 witness.** The independently adopted [whole60-ray complement obstruction](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-5-rqls10-sixty-ray-complement-and-ten-four-sector-orbit-exclusion-parent-v1.md) proves this physical C4 subsystem cannot be completed as a full orthogonal4+6 realization on that support orbit. The two statements are compatible: the positive result concerns40 C4 vectors; the negative result concerns the required60 distinct C6 vectors. This record doesnot claim a global100-ray no-go.

## Complete closed-form physical assignment

Write r=(a,u),c=(b,v) by residuesmod5/mod2, with crt(a,u)=a+5((u−a) mod2). The selected support consists of four-cellblocks A_a:(b=a) andB_a:(b=a+1), a∈Z5, u,v∈Z2. Everycellisassignedbelow; noequationsremainunsolved.

Use Pauli matrices X,Y,Z and N(theta)=cos(theta)Z+sin(theta)X, with theta1=0,theta2=pi/4,theta3=pi/8,theta4=3pi/8. Set U0=I, U1=−Z, U2=−exp(−iYpi/4), U3=N(−pi/8), U4=−iY. For epsilon=±1, w0^epsilon=(1,epsilon i)/sqrt2. Fori1..4 set wi^+=(cos(theta_i/2),sin(theta_i/2)), wi^−=(−sin(theta_i/2),cos(theta_i/2)). For eta=±1 define

Q_i^U(epsilon,eta)=2^−1/2 (wi^epsilon, eta Ui^dagger wi^epsilon),

Q_i^V(epsilon,eta)=2^−1/2 (wi^epsilon, −i(−1)^i eta Ui^dagger wi^epsilon).

| a | A_a index/branch | B_a index/branch |
|---|---|---|
|0|0/U|4/V|
|1|3/V|2/V|
|2|1/V|0/V|
|3|4/U|3/U|
|4|2/U|1/U|

AtA_a cell(u,v), use epsilon=(−1)^(u+v),eta=(−1)^v. AtB_a cell(u,v), use epsilon=−(−1)^(u+v),eta=−(−1)^u. ThetableplusCRTformulaassignsall40actualphysicalcells, not a multisetwithunroutedrays. [Full literal exact cyclotomic coordinates and all30contexts](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f534-rqls10-forty-ray-independent-exact-cyclotomic-verification/parent-independent-finite-run-v1.stdout.txt) are retained.

## Why every physical consumer holds

The exactrecurrenceUi=(−1)^i Ni U_(i−1) closesatU4=−iY. With T(U)=[[0,U],[Udagger,0]], ti=T(Ui),bi=(−1)^iT(iUi),g0=diag(Y,Y),gi=diag(Ni,U_(i−1)^dagger Ni U_(i−1)), allareHermitianinvolutionswithtwo-dimensional±eigenspaces. Thecorrectclosingidentities areb4=g0t0 andb0t4=−g0. TheQ branchesareexplicitjointONBsof(gi,ti)/(gi,bi).

Use sharedrowobservables R=(b4,b2,b0,t3,t1), columnobservables C=(t0,b3,b1,t4,t2), andsymbolobservables D=(g0,g3,g1,g4,g2). AtA_a, physicalsignsare((−1)^u,(−1)^v,(−1)^(u+v)); atB_a theyaretheirnegatives, withobservablesR_a,C_(a+1),D_(a−2). EachactualrowcombinesA_a/B_a complementary2planes; eachcolumncombinesA_b/B_(b−1); eachsymbol(s,w) combinesA_(3s)/B_(3s+2). TheseareALL30physicalONBs, not justthetenfour-cellblocks.

Allfirsttwo-componentrayscome fromthefiveaxesY,Z,N(pi/4),N(pi/8),N(3pi/8), pairwisedifferentuptosign. Differentaxes have disjointeigenrays. Forfixedaxis/eigenray,thefourrelative lower-blockmultipliers are±1,±i; bothblocksnonzero,so no two areparalleloverANYcomplexscalar. Thusall40raysaregloballydistinct, includingnonadjacentcells. Normalizationisexact.

Themap(r,c)→(hr,hc+t),h∈{1,3,7,9},t∈Z10, isaphysicalcellbijectionandmapsLtohL+t. Ittransportsallvectorsandcontexts, realizingexactlythetenmasksconsistingofanytwoantipodalpairs. Thisdoesnotassertvectorcovarianceor aunitaryaction.

## Verification and immutable chronology

[Completef496author](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f496-rqls10-rank28-5plus5-or-remaining-cyclic-4sector-frontier/review-v1.md) · [earlierAUTHOR-codeparentone-shot](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f496-rqls10-rank28-5plus5-or-remaining-cyclic-4sector-frontier/parent-author-exact-finite-run-v1-receipt.json) · [f532fullcontextwrittenreview](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f532-rqls10-explicit-forty-ray-four-sector-physical-review/review-v1.md) · [f533independentdistinctness/orbitreview](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f533-rqls10-forty-ray-distinctness-affine-orbit-and-complement-review/review-v1.md) · [f534independentreport/source](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f534-rqls10-forty-ray-independent-exact-cyclotomic-verification/review-v1.md) · [independentexactsource](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f534-rqls10-forty-ray-independent-exact-cyclotomic-verification/independent-forty-ray-exact-cyclotomic-v1.py) · [actualparentindependentone-shot](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f534-rqls10-forty-ray-independent-exact-cyclotomic-verification/parent-independent-finite-run-v1-receipt.json). Parentdisplayedall585author/code,501/626writtenreviewand978independentreport/sourcelogicallines. Bothwrittenreviewscopesreport0F/0M/0m; neitherreviewer norindependentcheckerreadtheauthorprogram. Thetwo reviews’ earlier “complementunproved” text remains frozenhistoricalscope; thelaterC6obstructionisaseparateadoption,notbackdatedinto them.

Independentcodeparentexecutionafterfullstaticread/GO:ONCE,exit0,emptystderr,0.1802s. EXACTinteger/dyadicQ(zeta32),zeta32^16=−1, nofloatingtolerance. Observed:40unitnorms,ALL30contexts,180prescribedorthogonalpairs,ALL780globalnonparallelpairs; exactly180pairs hadzeroinnerproduct. All40affinemaps/10masks/1,200transportedcontextschecked. Eightmutantsrejectedforintendedreasons:wrongsymbolr−c,wrongCRTbits,omittedimaginaryphase,duplicatecontext,duplicateray,wrongU4closure,badBsigns,39-rays. Fieldmultiplication/conjugation/trigonometricidentitieswereseparatelycheckedagainst32-poweralgebra; exactequalityusesirreducibilityofPhi32, notnumericnear-zero. Fullvector/contextoutputandlogsarepinned.

This verifies theENTIRE40-rayfiniteobject anditsstatedtransport; itisnotanexhaustivesearchoverallphysical100-rayarrays. Othercyclicfour-supportorbit,noncirculant4+6,otherresolutions,rank28 5+5andirreducibleC10remainopen. Sourceequivalence,novelty,worldwidepriority,independent-family,humanandformal/kernelassurancearenotclaimed. Held episodesANDconsumersremainNONINPUT.
