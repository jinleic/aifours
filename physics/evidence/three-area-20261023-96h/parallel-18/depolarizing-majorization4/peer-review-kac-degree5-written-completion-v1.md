# v42-B — six degree-five determinant coefficients completed by written arithmetic

Actual returned `/bin/date` before this freeze: **Sun Oct 25 06:36:18 PDT 2026**. Reviewer PhysicsDepol4-2. SAME degree-five continuation, with NEW DISCLOSED supplied inputs from v41-A. **WRITTEN only**: no scientific interpreter/eval/arithmetic or symbolic program, enumeration, sampling, interpolation, replay, solver, CLI, nested agent or GO.

## 1. Verdict, provenance and exact acceptance scope

**All SIX assigned degree-five coefficient identities are now derived.** In monomial order u5,u4v,u3v2,u2v3,uv4,v5, the degree-five part of det M is

`-43740*(15438,89052,195747,202992,99540,18621)`.

**0 FATAL /0 MAJOR /0 MINOR author findings at this GIVEN-pencil degree-five slice.** There is no remaining unevaluated scalar group for these six coefficients. The earlier honest v41-B partial remains immutable and historically NOT_RECONSTRUCTED; this successor supplies new arithmetic, not a retroactive PASS.

This is NOT independent rediscovery of v41-A's inverse, integer matrices, cubic traces or existing cofactor products. Those are explicit supplied written inputs. The NEW work here evaluates all five quartic-minor coefficients, all six third-normalized-cofactor contractions, the resulting homogeneous quintic, every lower-a-shift contribution and all six final binomial sums. No author target was used to determine an omitted group.

No degree-six, full determinant, all-quadrant sign, original-source-image matrix, actual3-to5 quotient, formal/kernel/human/cross-vendor/executable/novelty or parent acceptance follows from this slice alone.

### Complete literal coverage and exposure

The complete861-line v42-B literal packet was read, all source LF144+283+419, including endings. No reported reader truncation was left unread. The exact manifest entry was additionally recovered raw at LF82. ACK/exposure preceded opening the new proof body.

- S1, `kac-moody/level5-full-invariant-quotient-v1.md`, LF1–144, SHA256 `a539f8b96afa6314367db190ae38bbd9c2f33afc517c2e96f5eb7a7d731129aa`.
- S2, own `peer-review-kac-determinant-degree5-v1.md`, LF1–283, SHA256 `b8c57de3863e8c8de445c1b71ab5d9a77efef03a03e9a5208991b3737849fa21`.
- S3, `stochastic-hinf-preview/peer-review-kac-determinant-degree4-v1.md`, LF1–419, SHA256 `dc3faec7e7405710b9afd8f9ab5af5c4a9d030a217c849d567f892c11a3e24b4`.
- Literal packet SHA256 `09b9efaa1a2397585ab399a98dd087262822d8966922b5fe43659e5be8c01df9`.
- v42 manifest SHA256 `5a6c96653bdd223e31c7d1cd4ff9cf353856363eed43b9363e603d2da3d35159`; packet receipt SHA256 `2fe64dc5d5e566a50cbdc18f117c7a3ed8892ee92467faca49397700c4022744`.

Parentv8 was read FIRST, complete37LF. Receipt reports literal round-trip equality; this reviewer hashed the actual files but did not run a regeneration program. S1's target triangle and S2's partial were already exposed. This is supplied-proof reconstruction, not blinded discovery. Historical unadmitted arithmetic supplies zero verification credit.

## 2. Retained normalization and the supplied inputs actually used

Use S2's exact GIVEN-pencil reduction, with one-based other-column order O=(1,3,4,5,6):

`N=M/3=aA+bB+cC`, `D=det N`, `det M=729D`.

The distinguished-column operation gives bk_b+ck_c; the constant five-minor has det E=-1215. With normalized cofactor ell3=-1 and z=det(E+bEb+cEc), S3 LF233–249 gives the exact polynomial identity

`D=-180c z-z ell(b,c)^T R2`,

`R2=b² U+bc W+c² V`.                                  (1)

The positive/negative signs here are fixed by the row3/column2 cofactor, not chosen to fit the target triangle.

The supplied lower minor and normalized-cofactor products are (S3 LF211–217,265–277,313–317):

`z0=-1215`,

`z1=-10395b-10935c`,

`z2=-30978b²+19890bc+25785c²`,

`z3=7230b³+41832b²c-15243bc²-20115c³`,

`L2=ell0 R2=144b²-1580bc-2090c²`,

`L3=ell1 R2=-1248b³+(66364/9)b²c+(316174/9)bc²+(69340/3)c³`,

`ell2 R2=-J4`,

`J4=(-313264/45)b4+(657644/81)b3c+(26736026/81)b2c2`

`       +(15767704/27)bc3+(2300390/9)c4`.

These inputs are credited to the supplied v41-A written derivation. They are not claimed newly rediscovered here. What remains in(1) at degree five is exactly z4 and K5:=ell3 R2. Both are evaluated below.

## 3. NEW: all six third-normalized-cofactor contractions

Use S3's source-coordinate vectors restricted to O:

`hU=(860,-200,-240,306,156)^T/45`,

`hW=(15098,6865,108,-33138,-2982)^T/81`,

`hV=(1290,865,105,-3780,-455)^T/9`.

They satisfy A_O hR=r off row3 for r=U,W,V. Higher ell coefficients have third component zero, so the possible row3 error is irrelevant in these contractions.

From the other-five-column annihilation equations,

`ell_n^T A_O=-ell_(n-1)^T(bB+cC)_O`.

Applying this twice to ell3 R2 yields

`K5=(b² BB+bc F+c² CC)(bTb+cTc)(b²hU+bc hW+c²hV)`,       (2)

where the supplied rows are

`BB=(-364,2732,492,368,-480)/3`,

`F=BC+CB=(2150,10754,1338,1124,-264)/3`,

`CC=(1124,2240,186,248,372)`.

Tb=E^-1Eb and Tc=E^-1Ec. This derivation fixes the POSITIVE sign in(2): ell2 has the preceding minus, ell3 has the next minus. It does not confuse a derivative with an unnormalized polynomial coefficient.

### 3.1 Actual row-matrix products

Let R=135Tb,Q=45Tc be the INTEGER matrices supplied in S3 LF102–116. Write B0=3BB,F0=3F. The six NEW row products, evaluated by ordinary integer multiplication, are

|row product|five integer entries|
|---|---|
|B0 R|`-305148,953484,205092,156264,-227304`|
|B0 Q|`210624,331800,20556,36528,83592`|
|F0 R|`264750,13403490,2043630,1486320,-1650420`|
|F0 Q|`2020200,3855660,307350,431520,697140`|
|CC R|`331980,4076340,576270,416040,-404640`|
|CC Q|`559410,1116150,92790,123720,185580`|

For example the first entry of B0R is `-364*395+2732*(-50)+492*0+368*(-36)-480*24=-305148`. All entries use only the literal integer R,Q supplied by v41-A, not the target polynomial.

Consequently the four actual row groups

`G0=BB Tb`, `G1=BB Tc+F Tb`,

`G2=F Tc+CC Tb`, `G3=CC Tc`

are

`G0=(-101716,317828,68364,52088,-75768)/135`,

`G1=(298874,4799630,701766,531968,-466548)/135`,

`G2=(156812,528800,58908,56504,19500)/9`,

`G3=(37294,74410,6186,8248,12372)/3`.

### 3.2 ALL twelve scalar dot products, then six grouped coefficients

The NEW integer-numerator products against the three explicit h vectors are

|group|actual dot product|
|---|---:|
|G0 hU|`-163329600/6075`|
|G0 hW|`-846587604/10935`|
|G0 hV|`-11532400/1215`|
|G1 hU|`-781317480/6075`|
|G1 hW|`21300540882/10935`|
|G1 hV|`2812353140/1215`|
|G2 hU|`35292624/405`|
|G2 hW|`4073543088/729`|
|G2 hV|`443427200/81`|
|G3 hU|`20160120/135`|
|G3 hW|`764342022/243`|
|G3 hV|`76316740/27`|

For instance the G3hV numerator is

`37294*1290+74410*865+6186*105-8248*3780-12372*455`

`=48109260+64364650+649530-31177440-5629260=76316740`.

The six coefficient groups of(2), in b5,b4c,b3c2,b2c3,bc4,c5 order, are

`G0hU`,

`G0hW+G1hU`,

`G0hV+G1hW+G2hU`,

`G1hV+G2hW+G3hU`,

`G2hV+G3hW`,

`G3hV`.

Their EVALUATED values are

`K5=(-2177728/81, -750986356/3645, 1476643342/729,`

`        652202180/81, 232735958/27, 76316740/27)`.       (3)

For traceability, the mixed numerator additions before reduction are

`[-846587604*5-781317480*9]/54675=-750986356/3645`,

`[-11532400*9+21300540882+35292624*27]/10935=1476643342/729`,

`[2812353140*3+4073543088*5+20160120*27]/3645=652202180/81`,

`[443427200*3+764342022]/243=232735958/27`.

Thus no third-cofactor scalar is left as an unevaluated recurrence.

## 4. NEW: all five quartic minor coefficients by literal four-principal-minor products

This section evaluates z4 without an interpreter and without using determinant samples.

### 4.1 A small integer pencil and the exact weights

Factor rows(5,5,15,9,3) from R+tQ. The remaining matrix S(t) is

`[79+61t, 520+130t, 68+11t, 52+14t, -18+24t;`

` -10+44t,251+83t,40+7t,26+10t,-54+12t;`

` 3t,54+3t,9-t,12,18+6t;`

` -4-108t,-688-210t,-104-17t,-73-26t,108-34t;`

` 8-39t,-244-75t,-42-6t,-34-8t,9-22t]`.

Let D_i(t) be its four-principal-minor omitting index i. Products of the retained row factors give

`e4(R+tQ)=225 H(t)`,

`H=9D1+9D2+3D3+5D4+15D5`.                            (4)

Since `bTb+cTc=(b/135)R+(c/45)Q`, coefficient extraction gives

`[b^(4-j)c^j] z4 = -3^j [t^j]H(t)/1215`.              (5)

This is a polynomial coefficient identity, not interpolation in t and not an argument requiring b nonzero.

### 4.2 COMPLETE quadratic two-by-two minor data

Every triple in the following tables is the actual coefficient vector(constant,t,t²). Locally A,B,C,D,F,G name two-row minor families of S(t), not the original pencil's scalar matrices.

A uses rows12, B rows45:

|ij|A_ij|B_ij|
|---|---|---|
|12|`25029,288,-657`|`6480,1500,-90`|
|13|`3840,111,-57`|`1000,640,-15`|
|14|`2574,228,-6`|`720,1065,-150`|
|15|`-4446,-1314,-324`|`-900,3600,1050`|
|23|`3732,435,-3`|`3520,1000,-15`|
|24|`468,750,138`|`5580,825,-270`|
|25|`-23562,-5310,-432`|`20160,13050,2070`|
|34|`-312,42,12`|`470,-120,-20`|
|35|`-2952,-612,-36`|`3600,1355,170`|
|45|`-2340,-576,-72`|`3015,1080,300`|

C uses rows23 on columns2345, D rows13 on columns1345:

|ij|C_ij|ij|D_ij|
|---|---|---|---|
|23|`99,-2,-104`|13|`711,266,-94`|
|24|`1608,378,-30`|14|`948,576,-42`|
|25|`7434,2514,462`|15|`1422,1626,294`|
|34|`246,20,10`|34|`348,58,14`|
|35|`1206,204,54`|35|`1386,372,90`|
|45|`1116,192,60`|45|`1152,276,84`|

F uses rows35 on columns1235, G rows34 on columns1234:

|ij|F_ij|ij|G_ij|
|---|---|---|---|
|12|`-432,1350,-108`|12|`216,3780,-306`|
|13|`-72,233,-57`|13|`36,656,-159`|
|15|`-144,681,168`|14|`48,1077,-78`|
|23|`-72,-19,-93`|23|`576,-28,-261`|
|25|`4878,1653,384`|24|`4314,897,-78`|
|35|`837,153,58`|34|`591,43,26`|

These44 minors each use `(a0+a1t)(d0+d1t)-(b0+b1t)(c0+c1t)`. For example A12 has constant25029, linear `79*83+61*251-520*44-130*(-10)=288`, and quadratic `61*83-130*44=-657`.

### 4.3 Nineteen explicit product groups, rather than a hidden five-determinant assertion

Laplace expansion in the first two rows of each four-minor has signs(+,-,+,+,-,+). Collect the parts9D1+9D2+3D3 as `sum B_ij T_ij`, with the following ACTUAL T polynomials:

|ij|definition of T_ij|coefficient triple|
|---|---|---|
|45|`9(C23+D13)+3A12`|`82377,3240,-3753`|
|35|`-9(C24+D14)`|`-23004,-8586,648`|
|34|`9(C25+D15)`|`79704,37260,6804`|
|25|`9C34-3A14`|`-5508,-504,108`|
|24|`-9C35+3A15`|`-24192,-5778,-1458`|
|23|`9C45`|`10044,1728,540`|
|15|`9D34+3A24`|`4536,2772,540`|
|14|`-9D35-3A25`|`58212,12582,486`|
|13|`9D45`|`10368,2484,756`|
|12|`3A45`|`-7020,-1728,-216`|

Collect5D4+15D5 as `sum A_ij S_ij`, where

|ij|definition of S_ij|coefficient triple|
|---|---|---|
|12|`5F35+15G34`|`13050,1410,680`|
|13|`-5F25-15G24`|`-89100,-21720,-750`|
|15|`5F23`|`-360,-95,-465`|
|23|`5F15+15G14`|`0,19560,-330`|
|25|`-5F13`|`360,-1165,285`|
|35|`5F12`|`-2160,6750,-540`|
|14|`15G23`|`8640,-420,-3915`|
|24|`-15G13`|`-540,-9840,2385`|
|34|`15G12`|`3240,56700,-4590`|

The nineteen ordinary quadratic-product convolutions now have the following COMPLETE nonconstant coefficient groups:

|top product|t|t²|t³|t4|
|---|---:|---:|---:|---:|
|B45T45|98735760|16897005|-3081240|-1125900|
|B35T35|-62080020|-13211910|-581580|110160|
|B34T34|7947720|-2867400|-1561680|-136080|
|B25T25|-82040040|-15801480|366120|223560|
|B24T24|-52199640|-6370650|357210|393660|
|B23T23|16126560|3478140|514080|-8100|
|B15T15|13834800|14256000|4854600|567000|
|B14T14|71054820|5017950|-1369710|-72900|
|B13T13|9119520|2190240|446580|-11340|
|B12T12|-21727440|-3359880|-168480|19440|
|SUM|-1227960|228015|-224100|-40500|

|bottom product|t|t²|t³|t4|
|---|---:|---:|---:|---:|
|A12S12|39049290|8851950|-730530|-446760|
|A13S13|-93294900|-212220|1154790|42750|
|A15S15|895410|2308860|641790|150660|
|A23S23|72997920|7277040|-202230|990|
|A25S25|25538130|-684540|-1010070|-123120|
|A35S35|-18604080|-2459160|87480|19440|
|A14S14|888840|-10224810|-890100|23490|
|A24S24|-5010120|-6338340|430830|329130|
|A34S34|-17554320|3852360|487620|-55080|
|SUM|4906170|2371140|-30420|-58500|

For the constant, direct numeric two-row Laplace expansions give

`(D1(0),D2(0),D3(0),D4(0),D5(0))`

`=(161865,-759915,142155,1579257,-196101)`.

For example

`D3(0)=25029*3015-2574*20160-4446*5580`

`          -468*900+23562*720-2340*6480=142155`.

With the weights in(4), the constant is−1215. Adding all nineteen nonconstant product groups gives

`H(t)=-1215+3678210t+2599155t²-254520t³-99000t4`.

Equation(5) therefore EVALUATES the entire formerly missing quartic minor:

`z4=b4-9082b3c-19253b2c2+5656bc3+6600c4`.              (6)

No matrix samples or interpolation were used: each coefficient is accounted for by the displayed two-by-two products and nineteen convolutions.

### 4.4 Mandatory correction of an intermediate reviewer checkpoint

`resume-checkpoint-008-v1.json` is preserved unchanged but its reported z4b2c2,z4bc3,z4c4 and corresponding H2,H3,H4 are WITHDRAWN. It had used−3090 rather than−750 for the t² coefficient of S13. The direct minor arithmetic is `-5*384-15*(-78)=-1920+1170=-750`. The sign of the second term was the reviewer error.

Correcting that ONE product adds2340 to S13's quadratic coefficient. Its contributions to H2,H3,H4 are respectively `3840*2340=8985600`, `111*2340=259740`, `(-57)*2340=-133380`, producing the corrected tables above. A consistency comparison with the already exposed target led me back to this sign; the corrected values themselves are derived from the literal minors, not solved from the target. Checkpoint009 records the additive withdrawal. This is an intermediate WRITTEN reviewer arithmetic correction, not an author finding or an interpreter/program rerun. No earlier partial is retroactively accepted.

## 5. NEW: evaluate the complete homogeneous quintic determinant

Expanding(1) at a1, the degree-five term is

`D5hom=-180c z4-z3 L2-z2 L3+z1 J4-z0 K5`.              (7)

The five separate polynomial-product rows are ALL evaluated here; columns are b5,b4c,b3c2,b2c3,bc4,c5:

|term|b5|b4c|b3c2|b2c3|bc4|c5|
|---|---:|---:|---:|---:|---:|---:|
|-180c z4|0|-180|1634760|3465540|-1018080|-1188000|
|-z3 L2|-1041120|5399592|83400252|66241500|-63639570|-42040350|
|-z2 L3|-38660544|253247608|973786148|-172872560|-1365562710|-595977300|
|z1 J4|72363984|-24823484/3|-10559715830/3|-9679929550|-9042870570|-2794973850|
|-z0 K5|-32665920|-750986356/3|7383216710/3|9783032700|10473118110|3434253300|
|SUM|-3600|43740|-11880|-62370|27180|73800|

For example the b4c sum is

`-180+5399592+253247608-(24823484+750986356)/3=43740`.

The c5 sum is

`-1188000-42040350-595977300-2794973850+3434253300=73800`.

Thus homogeneity restores the NEW term

`a*(-3600b5+43740b4c-11880b3c2-62370b2c3+27180bc4+73800c5)`.  (8)

This is an evaluated six-coefficient polynomial, not the earlier unevaluated bordered formula.

## 6. Include EVERY lower a-shift contribution

Use T=u+v,d=u-v, so a=1+T/2,b=d/2,c=−T. From the supplied written lower terms S3 LF361–365 and348–349, together with(8), the relevant terms of D are

`218700a5c`,

`a4(174960b²-48600bc-571050c²)`,

`a3(-19440b³-314280b²c+100440bc²+587250c³)`,

`a²(-54000b4+28080b3c+212220b2c2-78030bc3-297000c4)`,

and(8). Terms homogeneous of degree6 in b,c cannot contribute to shifted degree5.

The coefficients required from the a-powers are respectively5/16,1/2,3/4,1,1. Their ACTUAL shifted degree-five contributions are

|source|T5|T4d|T3d²|T²d³|Td4|d5|
|---|---:|---:|---:|---:|---:|---:|
|a5c|-273375/4|0|0|0|0|0|
|a4 quadratic|-285525|12150|21870|0|0|0|
|a3 cubic|-880875/2|37665|117855/2|-3645/2|0|0|
|a² quartic|-297000|39015|53055|-3510|-3375|0|
|a quintic|-73800|13590|31185/2|-1485|-10935/4|-225/2|
|SUM|-4660425/4|102420|149445|-13635/2|-24435/4|-225/2|

For instance the first row uses `[T4](1+T/2)^5=5/16`, and the quintic row contains `-3600(d/2)^5=-225d5/2`. Thus the shifted quintic is not confused with the homogeneous a,b,c quintic.

Define F=−D/60, without assuming it equals the author's target P. The complete reconstructed degree-five part is

`16F5=310695T5-27312T4d-39852T3d²`

`          +1818T²d³+1629Td4+30d5`.                   (9)

## 7. ALL six final scalar sums and the exact scale

The six binomial rows, in u5,u4v,u3v2,u2v3,uv4,v5 order, are

`T5:   1, 5,10,10, 5, 1`,

`T4d:  1, 3, 2,-2,-3,-1`,

`T3d²: 1, 1,-2,-2, 1, 1`,

`T²d³: 1,-1,-2, 2, 1,-1`,

`Td4:  1,-3, 2, 2,-3, 1`,

`d5:   1,-5,10,-10,5,-1`.

Using(9), the EVALUATED scalar numerators are

`u5: 310695-27312-39852+1818+1629+30=247008`,

`u4v: 1553475-81936-39852-1818-4887-150=1424832`,

`u3v2: 3106950-54624+79704-3636+3258+300=3131952`,

`u2v3: 3106950+54624+79704+3636+3258-300=3247872`,

`uv4: 1553475+81936-39852+1818-4887+150=1592640`,

`v5: 310695+27312-39852-1818+1629-30=297936`.

Division by16 gives, respectively,

`15438,89052,195747,202992,99540,18621`.

Finally det M=729D=−43740F because729*60=43740. Thus all six assigned coefficients are exactly−43740 times these six numbers. No degree-five coefficient remains NOT_RECONSTRUCTED at the stated supplied-input boundary.

## 8. Scope, dependency disclosure and remaining nonclaims

The NEW evaluated groups are(3), the complete quartic-minor proof(6), the six-column product sum(7), all lower shifts and the six final sums. The dependency on S3/v41-A is explicit: its inverse elimination, R/Q integer matrices, z0..3, L2/L3/J4, hU/hW/hV and rowBB/BC/CB/CC data are supplied WRITTEN inputs. I do not claim an independent rediscovery of those earlier products or a blinded reconstruction. The source's claimed target row was exposed throughout; it was not a premise used to fill any absent group.

The following remain OUT OF SCOPE / NOT_RECONSTRUCTED by this return:

- degree-six coefficients or a complete all-quadrant determinant sign/nonzero theorem;
- the full determinant identity without composition with the actual prior-degree and degree-six returns;
- whether the GIVEN pencil is the actual original D3 source-image matrix, including every108-scalar source-column gate and actual quotient imports;
- full invariant injectivity, the actual3-to5 quotient, seven other primitive types, H13/generalF5/Serre equality;
- scientific/executable replay, formal/kernel, human/cross-vendor/configured-dual-family, novelty or parent acceptance.

Parentv8's withdrawn historical coverage/acceptance is not repaired retroactively. Fresh full parent reading and composition are still required. No scientific permission is inferred from this written completion.

**Disposition:** actual completed WRITTEN degree-five derivation at the GIVEN-pencil/supplied-v41-A input boundary, with all six target equalities proved and the intermediate reviewer sign correction permanently disclosed. Preserve the earlier partials and checkpoint008 unchanged; this successor, not an edit or a copied positive triangle, closes the previously named degree-five arithmetic gap.
