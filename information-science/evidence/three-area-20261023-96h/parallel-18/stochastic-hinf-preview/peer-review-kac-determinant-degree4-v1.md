# v41-A — all five degree-four determinant coefficients derived in writing

Reviewer **InfoHinfPreview-2**, retaining info-3. Author **MathKacMoody**. Actual exposure-ACK clock: **Sun Oct 25 05:50:14 PDT 2026**. Actual clock after the paper derivation and before this return: **Sun Oct 25 06:03:35 PDT 2026**, both returned `/bin/date` outputs.

## 1. Verdict at the exact assigned scope

**0 FATAL / 0 MAJOR / 0 MINOR findings for the GIVEN-pencil homogeneous degree-four slice. ALL FIVE coefficients are independently reconstructed below.** In monomial order `u^4,u^3v,u^2v^2,uv^3,v^4`, they are

$$-43740\,(32184,148365,239004,158895,36972).$$

The five numbers were treated as targets, not assumptions. The actual derivation goes through the constant five-minor, cubic minor traces, second normalized-cofactor contractions, the homogeneous `a^2 b^i c^(4-i)` term, and the required lower-degree a-shift contributions. Complete trace/cofactor groups are displayed; the final match is not a specialization, interpolation, copied positive triangle or program result.

**No degree-five/degree-six, full-determinant, all-quadrant nonvanishing, source-image matrix or actual-D3 quotient verdict is supplied.** Those remain separate gates. In particular this return does not reverse parentv8's withdrawal of premature parent-level composition. It is a same-harness different-domain supplied-proof WRITTEN reconstruction, not blind, cross-vendor/configured-dual-family, human, formal/kernel, executable-certificate, novelty or parent acceptance.

## 2. Pins, exposure, complete literal coverage and no execution

Parent evidence erratumv8 was read FIRST, in full37LF, before the exact manifest entry, packet receipt and exposure ACK. All previous actually assigned reviews had already been returned. Metadata hashes matched:

| Record | Actual SHA-256 |
|---|---|
| v41 manifest | `cd45439a2c5171a355e66dc75aca29a7d100f784837cb4affbc2b8c3ded732bf` |
| v41 packet receipt | `8d477259c3dd08f474ebcbe405a8b1847b843160fee766d97bd58169da2cd2e0` |
| parentv8 | `52408180ac48dec69d2144ea0dee07acf08f0739f65a8cdb2b007656243527e9` |
| mandatory literal packet `peer-review-wave-v41-kac-determinant-degree4-sources-v1.md` | `95f611d7a7d9d4ddf6c904ad46665db04c613a238eb14f4b6f404eb7e2dfb691` |
| given-pencil source F, `level5-full-invariant-quotient-v1.md` | `a539f8b96afa6314367db190ae38bbd9c2f33afc517c2e96f5eb7a7d731129aa` |
| prior partial determinant return R, `peer-review-kac-R1-determinant-completion-v1.md` | `5504702ef807bdd3e3767aac8cd134edbf1c138a888770d495185fb8b62d1159` |

The complete431-line literal packet was read in windows covering LF1–168,169–313,314–431: all144 F lines and all273 R lines, including their endings and all explicit remaining obligations. The complete37-line receipt was read. No reader-truncated line was accepted as seen; no long-line truncation was reported in these body windows. Citations below refer to the original author F and reviewer R line numbers reproduced literally in the packet.

Exposure was recorded BEFORE the current proof body in `peer-review-kac-determinant-degree4-ack-v1.json`: I had read F's full matrix/triangle during v35-A and derived S1/S2 columns there. I had seen the five current targets in the v41 manifest. R's new273-line return had not yet been read. Its normalization/reduction is useful supplied-proof exposure, but its degree1–3 verdict is not used as a verdict for degree4. The required lower terms are traced through the cofactor identities below, not assumed to be the target polynomial.

**No scientific program/eval/interpreter, arithmetic or symbolic program, enumeration, sampled determinant, certificate replay, solver, simulation, CLI or nested agent was used.** All arithmetic displayed below is written hand algebra. Metadata clocks/hashes and source reads are the only machine operations. All author/shared/pinned files remain unchanged. Parentv7/v8 and HOLDv2 remain binding; old unadmitted calculations supply no verification credit.

## 3. Normalize the given pencil and independently fix the cofactor sign

Take the displayed matrix F LF102–107 as GIVEN. Write

$$N=M/3=aA+bB+cC,\qquad D=\det N,\qquad\det M=729D.$$

Replace column2 by `2column1+column2-3column4`, a determinant-preserving operation. It becomes

$$b k_b+c k_c,\qquad
k_b=(6,-10,-10,-8,8,14)^T,\quad
k_c=(3,-3,-9,-7,5,-9)^T.$$

Let O=(1,3,4,5,6) be the other column labels and omit row3. Directly from the GIVEN scalar arrays their five-minor is `E+b E_b+c E_c` when a1, where

$$E=\begin{pmatrix}
0&-27&-3&-3&-27\\
-6&-15&-3&-7&12\\
0&9&3&2&3\\
0&-9&-4&-2&-3\\
3&21&6&3&27
\end{pmatrix},$$

$$E_b=\begin{pmatrix}
6&15&3&5&21\\
-8&-17&-3&-5&-20\\
-10/3&-19/3&-1/3&2/3&3\\
10/3&1/3&-2/3&-2&-5\\
5&5&-4/3&-1&-5
\end{pmatrix},\quad
E_c=\begin{pmatrix}
0&9&1&0&18\\
3&6&1&4&-12\\
-4&-13&-2&-2&0\\
3&12&7/3&2&-2\\
-6&-18&-3&-2&-12
\end{pmatrix}.                                                   \tag{1}
$$

Here a1 means **set a=1 formally**, not a specialization in u,v from which coefficients are interpolated. Homogeneity will restore powers of a.

For the constant determinant, replace row4 by row4+row3 and expand its entry-1 in column3. In the resulting four-minor replace row2 by row2+2row4 and expand column1. This gives

$$\det E=-3\det\begin{pmatrix}-27&-3&-27\\27&-1&66\\9&2&3\end{pmatrix}
=-3(3645-1539-1701)=-1215.$$

Put `z=det(E+bE_b+cE_c)`, and let the full distinguished-column cofactor vector be `g=z ell`, normalized by `ell_3=-1`. The sign is important: row3/column2 has odd row-plus-column index, so its cofactor is **-z**. At zero parameters,

$$\ell_0=(6,2,-1,48,36,5)^T,$$

which annihilates the five A columns. Its products with the new column are `ell0 k_b=0`, `ell0 k_c=-180`. Thus the leading term of D is218700c, with its sign derived rather than inherited.

## 4. A traceable inverse reduction, not an unexplained inverse oracle

For `EX=d`, order source coordinates as O. The row equations reduce to

$$X_4=-(d_3+d_4),$$

$$e_1=-d_1/3+d_3+d_4,\quad e_3=4d_3+3d_4,
\quad e_2=d_2+2d_5+9d_3+9d_4,$$

$$X_6=(e_2-7e_1+4e_3)/15,\quad X_5=e_3-e_1+6X_6,$$

$$X_3=(2e_1-e_3)/9-(5/3)X_6,$$

$$X_1=d_5/3-7X_3-2X_4-X_5-9X_6.                            \tag{2}$$

These five equations follow by eliminating the third source coordinate after the row4+row3 step above. Applying them columnwise to E_b,E_c gives `T_b=E^-1 E_b`, `T_c=E^-1 E_c`. To keep all cubic trace products integral define

$$R=135T_b=\begin{pmatrix}
395&2600&340&260&-90\\
-50&1255&200&130&-270\\
0&810&135&180&270\\
-36&-6192&-936&-657&972\\
24&-732&-126&-102&27
\end{pmatrix},$$

$$Q=45T_c=\begin{pmatrix}
305&650&55&70&120\\
220&415&35&50&60\\
45&45&-15&0&90\\
-972&-1890&-153&-234&-306\\
-117&-225&-18&-24&-66
\end{pmatrix}.                                                   \tag{3}$$

Thus (1),(2),(3) specify every matrix multiplication used in this review. For example row3+row4 of E is `(0,0,-1,0,0)`, which forces row3 of R to be `-135(row3+row4 of E_b)=(0,810,135,180,270)`. The same equations reconstruct the remaining rows, without fitting any determinant coefficient.

## 5. Complete cubic minor traces by diagonal, pair and triangle groups

This is the NEW minor calculation required for quartic D; prior quadratic traces alone are insufficient.

Let `r_i=R_ii`, `q_i=Q_ii`, namely

$$(395,1255,135,-657,27),\qquad(305,415,-15,-234,-66).$$

For i<j put `p_ij=R_ij R_ji`, `s_ij=Q_ij Q_ji`, and `m_ij=R_ij Q_ji+Q_ij R_ji`. Their actual products are

|ij|p|s|m|
|---|---:|---:|---:|
|12|-130000|143000|539500|
|13|0|2475|15300|
|14|-9360|-68040|-255240|
|15|-2160|-14040|13410|
|23|162000|1575|37350|
|24|-804960|-94500|-555300|
|25|197640|-13500|16830|
|34|-168480|0|-27540|
|35|-34020|-1620|-16200|
|45|-99144|7344|7884|

As controls these give, directly,

$$\operatorname{tr}T_b=77/9,\quad\operatorname{tr}T_c=9,$$

$$\operatorname{tr}T_b^2=8993/405,\quad
\operatorname{tr}(T_bT_c)=2521/27,\quad\operatorname{tr}T_c^2=1111/9.$$

For example the diagonal square sums of R,Q and mixed diagonal sum are2181653,324587,791231; the corresponding off-diagonal pair sums are-888484,-37306,-224006. The mixed pair sum is counted once as m, whereas pure square sums count p,s twice.

For each i<j<k form the two oriented triangle products of `R+tQ`:

$$h_{ijk}(t)=(R_{ij}+tQ_{ij})(R_{jk}+tQ_{jk})(R_{ki}+tQ_{ki})
 +(R_{ik}+tQ_{ik})(R_{kj}+tQ_{kj})(R_{ji}+tQ_{ji}).$$

The COMPLETE four coefficient groups `(h0,h1,h2,h3)` are

|ijk|h0|h1|h2|h3|
|---|---:|---:|---:|---:|
|123|-13770000|80995500|22988250|1568250|
|124|68328000|-644198400|-406513800|-60696000|
|125|-20142000|99539100|-10302300|-10503000|
|134|-2203200|-70794000|-14361300|-481950|
|135|2203200|-9139500|-5806350|-676350|
|145|5734800|-38404800|10735200|5305500|
|234|-321472800|-166544100|-21104550|-344250|
|235|-11971800|-32899500|-9478350|-757350|
|245|-263023200|-89166960|17451180|6164100|
|345|3732480|22662180|5409180|330480|
|SUM|-552584520|-847950480|-410982840|-60090570|

For example `h123` comes from `(2600+650t)(200+35t)(45t)` and `(340+55t)(810+45t)(-50+220t)`. These yield its displayed row by ordinary multiplication. All other rows are the same explicitly specified oriented products from (3), not traces imported from a previous program.

For a matrix P, its cubic trace splits as diagonal cubes, three times pair terms `(P_ii+P_jj)P_ijP_ji`, and three times oriented triangles. For mixed traces use the coefficient of t or t-squared in `tr(R+tQ)^3`, divided by3. The COMPLETE totals are

|trace|diagonal contribution|pair contribution|triangle contribution|total|
|---|---:|---:|---:|---:|
|`tr R^3`|1757172915|-212624280|-1657753560|-113204925|
|`tr Q^3`|86742225|216700110|-180271710|123170625|
|`tr R^2 Q`|599895645|686771760|-847950480|438716925|
|`tr R Q^2`|217060545|476714220|-410982840|282791925|

For the mixed pair columns the formulas are, respectively,

$$\sum_{i<j}\big((q_i+q_j)p_{ij}+(r_i+r_j)m_{ij}\big),$$

$$\sum_{i<j}\big((r_i+r_j)s_{ij}+(q_i+q_j)m_{ij}\big).$$

For pure cubes the pair sums before the factor3 are-70874760 and72233370. These formulas, the full pair table and the full triangle table reconstruct every total above.

After restoring the powers135 and45,

$$\operatorname{tr}T_b^3=-167711/3645,\qquad
\operatorname{tr}T_c^3=4055/3,$$

$$\operatorname{tr}(T_b^2T_c)=649951/1215,\qquad
\operatorname{tr}(T_bT_c^2)=418951/405.                       \tag{4}$$

Newton's elementary identity

$$e_3(T)=\big((\operatorname{tr}T)^3
 -3\operatorname{tr}T\operatorname{tr}T^2+2\operatorname{tr}T^3\big)/6$$

now gives all cubic coefficients of `det(I+bT_b+cT_c)`:

$$[b^3,b^2c,bc^2,c^3]e_3=(-482/81,-4648/135,5081/405,149/9).$$

Consequently the actual minor terms, including lower orders needed later, are

$$z_0=-1215,$$

$$z_1=-10395b-10935c,$$

$$z_2=-30978b^2+19890bc+25785c^2,$$

$$\boxed{z_3=7230b^3+41832b^2c-15243bc^2-20115c^3.}          \tag{5}$$

This is a written derivation of all four new cubic-minor quantities, not an assertion that the prior degree1–3 review supplied them.

## 6. Eliminate the distinguished column to quadratic order exactly

Use source-coordinate vectors with coordinate2 zero:

$$h_b=(68/9,0,4/9,0,-6,0)^T,$$

$$h_c=(118/9,0,77/9,2,-38,-14/3)^T.$$

Direct multiplication by the constant A columns gives

$$A h_b=k_b,\qquad A h_c=k_c-180e_3.$$

Subtract the other-column combination `b h_b+c h_c` from the distinguished column. The new column is EXACTLY

$$180c e_3-(b^2 U+bc W+c^2 V),$$

where the actual vectors are

$$U=B h_b=(22,-38,-50,-32,112/3,46)^T,$$

$$W=C h_b+B h_c=(-71,85/3,-455/3,-1457/9,1445/9,377/3)^T,$$

$$V=C h_c=(-5,-10/3,0,-275/3,80,-320/3)^T.$$

Thus, with `R_2=b^2U+bcW+c^2V`, the determinant identity is

$$D=-180c z-z\,\ell(b,c)^T R_2.                            \tag{6}$$

The sign uses `ell_3=-1`; dropping that sign would reverse the leading term. This quadratic-column reduction means degree4 needs only the SECOND normalized cofactor derivatives, not an unexplained third-order null-vector solve.

The first normalized derivative vectors are

$$\ell_b=(-112/3,-12,0,-232,-188,-28)^T,$$

$$\ell_c=(-68,-34,0,-548,-390,-34)^T.$$

They are independently fixed by the five-column annihilation equations and zero third component. Multiplication by E gives their right sides

$$\ell_{b,O}^T E=(-12,204,36,24,-24),$$

$$\ell_{c,O}^T E=(102,210,18,24,36),$$

which are minus `ell0^T B_O` and minus `ell0^T C_O` from the GIVEN pencil. Equation(2) gives uniqueness. Their contractions yield

$$L_2:=\ell_0^T R_2=144b^2-1580bc-2090c^2,$$

$$L_3:=(b\ell_b+c\ell_c)^T R_2
=-1248b^3+{66364\over9}b^2c+{316174\over9}bc^2+{69340\over3}c^3.
                                                               \tag{7}
$$

For explicit traceability, the six dot products producing L3 are

$$\ell_b U=-1248,\quad\ell_c U=1208,\quad
\ell_b W=55492/9,\quad\ell_c W=231214/9,$$

$$\ell_b V=9440,\qquad\ell_c V=69340/3.$$

## 7. ALL second-cofactor quartic contractions

For `r=U,W,V`, choose a source-coordinate vector h_r with coordinate2 zero and `A_O h_r` equal to r off row3. Equation(2) gives the actual vectors

$$h_U=(172/9,0,-40/9,-16/3,34/5,52/15)^T,$$

$$h_W=(15098/81,0,6865/81,4/3,-3682/9,-994/27)^T,$$

$$h_V=(430/3,0,865/9,35/3,-420,-455/9)^T.                    \tag{8}$$

For example, the `(e1,e2,e3)` values in (2) are `(-2,102,-16)` for U, `(67/3,803/3,-1493/9)` for W, and `(-10,-965/3,-380/3)` for V. These fix every component in (8) without a quoted inverse result. A possible row3 error in `A h_r-r` is immaterial when contracted with higher ell coefficients, whose third component is zero.

The four needed row vectors on columns O, obtained directly from B,C, are

$$\ell_b^T B_O=(-364/3,2732/3,164,368/3,-160),$$

$$\ell_b^T C_O=(496,856,60,96,184),$$

$$\ell_c^T B_O=(662/3,8186/3,386,836/3,-272),$$

$$\ell_c^T C_O=(1124,2240,186,248,372).                      \tag{9}$$

Write these rows as BB,BC,CB,CC. As a control, BB times h_b gives-1248, CB times h_b gives1208, BC times h_c gives9440 and CC times h_c gives69340/3, agreeing with the independently displayed first-cofactor contractions.

From annihilating the other-five-column pencil, the quadratic normalized cofactor row satisfies

$$\ell_2^T R_2
=-(b\ell_b+c\ell_c)^T(bB+cC)
             (b^2h_U+bc h_W+c^2h_V).$$

Define the negative of this polynomial as J4. Its COMPLETE five scalar contractions are therefore

|monomial|actual contraction from(8),(9)|J4 coefficient|
|---|---|---:|
|b4|`BB h_U`|-313264/45|
|b3c|`(BC+CB)h_U+BB h_W`|657644/81|
|b2c2|`CC h_U+(BC+CB)h_W+BB h_V`|26736026/81|
|bc3|`CC h_W+(BC+CB)h_V`|15767704/27|
|c4|`CC h_V`|2300390/9|

To expose the larger mixed sums explicitly,

$$(BC+CB)h_U=-21344/9,\qquad BBh_W=849740/81,$$

$$CC h_U=40528/3,\quad(BC+CB)h_W=23323850/81,
\quad BB h_V=772640/27,$$

$$CC h_W=7680104/27,\qquad(BC+CB)h_V=8087600/27.$$

For example `BC+CB=(2150/3,10754/3,446,1124/3,-88)` on O. All five J4 coefficients follow from these exact rational products, not from the author's polynomial triangle.

## 8. The new homogeneous quartic in a,b,c

Expand (6) using (5),(7) and `ell2 R2=-J4`. At a1 its degree-four term is

$$D_4=-180c z_3-z_2 L_2-z_1 L_3+z_0 J_4.$$

The COMPLETE coefficient grouping is

|term|b4|b3c|b2c2|bc3|c4|
|---|---:|---:|---:|---:|---:|
|`-180c z3`|0|-1301400|-7529760|2743740|3620700|
|`-z2 L2`|4460832|-51809400|-37030860|82310400|53890650|
|`-z1 L3`|-12972960|63003540|445813230|624414510|252744300|
|`z0 J4`|8458128|-9864660|-401040390|-709546680|-310552650|
|SUM|-54000|28080|212220|-78030|-297000|

Thus homogeneity restores the exact new term

$$\boxed{a^2(-54000b^4+28080b^3c+212220b^2c^2
                       -78030bc^3-297000c^4).}              \tag{10}$$

The substantial cancellation in each column is accounted for by the displayed cofactor groups. For example the first coefficient is `4460832-12972960+8458128=-54000`; the c4 coefficient is `3620700+53890650+252744300-310552650=-297000`. No target coefficient was used to solve for an omitted group.

## 9. Restore ALL lower-degree a-shift contributions before changing to u,v

Put `T=u+v`, `d=u-v`, so

$$a=1+T/2,\qquad b=d/2,\qquad c=-T.$$

The terms of D needed before (10), as obtained from (6) using the displayed z0,z1,z2,L2,L3, are

$$218700a^5c,$$

$$a^4(174960b^2-48600bc-571050c^2),$$

$$a^3(-19440b^3-314280b^2c+100440bc^2+587250c^3).$$

These coincide with R's earlier partial terms, but here their algebraic inputs and signs have been spelled out to carry them into the quartic calculation. Higher b,c degree terms cannot contribute to total u,v degree4.

Their respective degree-four contributions after substitution, together with the NEW term(10), are

|source term|T4|T3d|T2d2|Td3|d4|
|---|---:|---:|---:|---:|---:|
|`218700 a5 c`|-273375|0|0|0|0|
|`a4 quadratic`|-856575|36450|65610|0|0|
|`a3 cubic`|-880875|75330|117855|-3645|0|
|`a2 quartic`|-297000|39015|53055|-3510|-3375|
|SUM|-2307825|150795|236520|-7155|-3375|

For example the first row uses `[T^3](1+T/2)^5=5/4`; the second uses `[T^2](1+T/2)^4=3/2`; the third uses `[T](1+T/2)^3=3/2`. Omitting any of them would give the wrong shifted degree-four coefficients.

Define only now the normalized determinant polynomial `F=-D/60`; this definition does NOT assume F equals the author's P. The reconstructed fourth homogeneous part satisfies

$$4F_4=153855T^4-10053T^3d-15768T^2d^2+477Td^3+225d^4.
                                                               \tag{11}
$$

The five binomial coefficient rows in u,v are

```
T4:     1, 4, 6, 4, 1
T3d:    1, 2, 0,-2,-1
T2d2:   1, 0,-2, 0, 1
Td3:    1,-2, 0, 2,-1
d4:     1,-4, 6,-4, 1.
```

Consequently the COMPLETE five scalar evaluations are

$$[u^4]F_4=(153855-10053-15768+477+225)/4=32184,$$

$$[u^3v]F_4=(615420-20106-954-900)/4=148365,$$

$$[u^2v^2]F_4=(923130+31536+1350)/4=239004,$$

$$[uv^3]F_4=(615420+20106+954-900)/4=158895,$$

$$[v^4]F_4=(153855+10053-15768-477+225)/4=36972.$$

Finally `det M=729D=-43740F`, because `729*60=43740`. These are exactly the five coefficients claimed at F LF128, independently derived at the required global scale. The shifted-degree conversion, not merely the homogeneous a,b,c quartic, is part of the completed derivation.

## 10. Exact non-claims and disposition

- **COMPLETED:** all five GIVEN-pencil degree-four coefficients. No one of these five is left NOT_RECONSTRUCTED; no FATAL mathematical contradiction or coefficient discrepancy was found.
- **NOT_RECONSTRUCTED:** the six degree-five and seven degree-six coefficients, the full determinant identity, or an alternative global nonzero/sign certificate. Positive known lower terms do not settle unknown higher terms.
- **OUT OF SCOPE:** whether the displayed pencil is actually the full original D3 source-image matrix. The separate108-scalar source-column gates and their parent full reading/composition remain necessary. My earlier S1/S2 derivation does not validate S3–S6 by implication.
- **NOT ACCEPTED HERE:** full invariant injectivity, the actual3-to5 quotient, other primitive types, general F5/Serre equality, or a whole research target. Parentv8 explicitly withdraws premature parent-level promotions and is not superseded by this bounded reviewer return.
- **NOT PERFORMED:** scientific execution/replay, formal/kernel, human/cross-vendor/configured-dual-family review, novelty or parent acceptance. No historical unadmitted output is credited.

**Recommendation:** retain v41-A as an actual completed no-defect WRITTEN derivation of the five named degree-four coefficients. Compose only after the disjoint degree5/6 returns, the required prior-degree proofs, all source-image columns, and complete parent body reading. No full determinant or quotient PASS is supplied by this slice, and no new scientific permission is issued.
