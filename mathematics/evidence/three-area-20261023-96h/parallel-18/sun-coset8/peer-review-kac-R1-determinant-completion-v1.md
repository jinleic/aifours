# v39-B — serial determinant completion: seven further coefficients derived; eighteen remain unclosed

Reviewer **MathSun8-2 / math-6**. Actual pre-write clock: **Sun Oct 25 05:41:18 PDT 2026** (`/bin/date`). Serial AFTER the completed v38-A review. **WRITTEN rational elimination/cofactor algebra only**; no scientific interpreter/eval, arithmetic or symbolic program, enumeration, replay, solver, CLI or nested agent was used. Metadata clocks/hashes/source reads only. Parentv7 and HOLD remain binding.

## 1. Exact current verdict

**The full determinant identity remains NOT_RECONSTRUCTED: a MAJOR load-bearing acceptance gate is still open.** This return is substantive progress beyond v35-D, not a relabelled PASS:

- v35-D derived the zero constant and both degree-one coefficients.
- Here ALL THREE degree-two and ALL FOUR degree-three coefficients are independently evaluated in writing through a five-by-five rational inverse, normalized cofactor perturbation, explicit trace products and displayed vector contractions.
- Thus **nine of27 nonconstant coefficients** now have actual written derivations. **Eighteen degree4–6 coefficients remain individually NOT_RECONSTRUCTED**, listed in §8. No full all-quadrant sign certificate is supplied.

No wrong author coefficient is established. The MAJOR is the remaining reconstruction gap, not a mathematical counterexample. No actual D3/source-column or quotient verdict is made; those are outside this determinant-only assignment. The old v35-D snapshot remains unchanged and was correct about its then25 unresolved coefficients.

### Binding and exposure

The complete144LF `level5-full-invariant-quotient-v1.md` (**F**) and64LF `level5-full-invariant-arithmetic-v1.json` (**J**) were re-read through the complete222-line mandatory v39 packet. No truncated source line remained. Exact v39-B entry, complete packet receipt and parentv7 were read before the exposure ACK.

Fresh hashes:

- F: `a539f8b96afa6314367db190ae38bbd9c2f33afc517c2e96f5eb7a7d731129aa`.
- J: `6a22a92ae52d82b6dd86488ed713170efa747ad6858722750da9788ed9a4c85b`.
- v39 packet: `7ee329f23763bb3d586c44e5e98005db14c22de110a8084e78184e5b4260e085`.
- Own prior review: `3f6ad962f2954b5df5c6f9593a7f140c5b875d8e1e7a7c1d2906d85cbd98948c`.

Source references below mean ORIGINAL F/J lines. This is explicitly SAME-reviewer/SAME-domain supplied-proof continuation, not blind, independent-family or cross-vendor review. The full claimed triangle was already exposed. The source's kernel booleans and historical computed outputs are not premises.

## 2. Normalize the GIVEN pencil and reuse the exact column reduction

This review concerns the GIVEN matrix F102–107/J28–33. Let

    N=M/3=a A+b B+c C,

where A is the integer constant matrix displayed as A0 in v35-D §3, and B=M_b/3,C=M_c/3 are read directly from the three scalar coefficient arrays. The formal determinant D=det N satisfies det M=729D. The target normalization would be D=-60P; this is a TARGET identity, not an assumption.

Replace column2 by2column1+column2-3column4. The distinguished column becomes

    b k_b+c k_c,
    k_b=(6,-10,-10,-8,8,14)^T,
    k_c=(3,-3,-9,-7,5,-9)^T.

Other columns retain their original values. At(a,b,c)=(1,0,0), its cofactor vector is z0 ell with

    z0=-1215,
    ell=(6,2,-1,48,36,5)^T,
    ell^T k_b=0, ell^T k_c=-180.

The cofactor proof in v35-D gave rank A=5 and the exact minor determinant -1215; it was not a sampled full determinant. Therefore D's first term is218700a^5 c, reproducing the old degree-one result after substitution.

For the NEW calculation set a=1 formally and retain b,c as independent variables. Homogeneity restores the powers a^(6-d) at each resulting total degree d. Formal expansions are legitimate near b=c=0 because the selected five-minor has nonzero constant; no analytic assumption about the physical quadrant is needed.

## 3. Explicit five-minor inverse and normalized left-cofactor derivatives

Let O=(1,3,4,5,6). Delete row3 and the distinguished column2 of N. Its constant five-minor is

    E=
    [ 0 -27 -3 -3 -27;
     -6 -15 -3 -7  12;
      0   9  3  2   3;
      0  -9 -4 -2  -3;
      3  21  6  3  27],
    det E=-1215.

The exact rational inverse is

    E^-1=
    [-1/3 -2/9 -31/9 -7/3 -1/9;
     -1/3 -1/9 -20/9 -5/3 -2/9;
      0     0     -1    -1    0;
     19/15 2/5  51/5  38/5  4/5;
      7/45 1/15 6/5 14/15 2/15].

A written derivation, not a quoted inverse: for EX=d, with variables ordered by O, row4+row3 gives X4=-(d3+d4). Put e1=-d1/3+d3+d4, e3=4d3+3d4 and e2=d2+2d5+9d3+9d4. The last source variable is X6=(e2-7e1+4e3)/15; then X5=e3-e1+6X6, X3=(2e1-e3)/9-(5/3)X6, and X1=d5/3-7X3-2X4-X5-9X6. Expanding these equations gives exactly the displayed inverse.

Let the actual distinguished-column cofactor vector be

    g(b,c)=z(b,c) ell(b,c),
    ell_3(b,c)=-1,
    z(b,c)=det(E+b E_b+c E_c).

The sign follows because the row3/column2 cofactor is minus this minor. The vector ell(b,c) annihilates the other FIVE columns, not the full generally invertible matrix. Write ell=ell0+b ell_b+c ell_c+... with ell0=ell above.

Direct multiplication from the GIVEN coefficients gives

    ell0^T B=12(1,-11,-17,-3,-2,2),
    ell0^T C=-6(17,5,35,3,4,6).

Consequently ell_b^T A_j=-ell0^T B_j and ell_c^T A_j=-ell0^T C_j for j∈O, with third component zero. Solving through the same five-minor inverse gives

    ell_b=(-112/3,-12,0,-232,-188,-28)^T,
    ell_c=(-68,-34,0,-548,-390,-34)^T.

For traceability, their five right-hand-side equations, ordered by O, are respectively

    (-12,204,36,24,-24),
    (102,210,18,24,36).

These determine the displayed derivative vectors uniquely with component3 fixed to zero. Useful actual dot products are

    ell_b k_b=-144, ell_c k_b=720,
    ell_b k_c=860, ell_c k_c=2090.

## 4. Evaluate the minor determinant through degree two

The derivative minor matrices are the corresponding row/column restrictions of B,C. Multiplying by the displayed E^-1 gives

    T_b=E^-1 E_b=
    [79/27 520/27 68/27 52/27 -2/3;
     -10/27 251/27 40/27 26/27 -2;
      0       6      1     4/3     2;
     -4/15 -688/15 -104/15 -73/15 36/5;
      8/45 -244/45 -14/15 -34/45 1/5],

    T_c=E^-1 E_c=
    [61/9 130/9 11/9 14/9 8/3;
     44/9 83/9 7/9 10/9 4/3;
      1    1   -1/3  0     2;
     -108/5 -42 -17/5 -26/5 -34/5;
     -13/5 -5 -2/5 -8/15 -22/15].

These are explicit rational row reductions of the displayed minor coefficients. Their traces are77/9 and9. The following grouped products show the required second traces without a program:

| Quantity | diagonal contribution | sum over i<j of the paired off-diagonal products | total trace |
|---|---|---|---|
|T_b²|2181653/18225|-888484/18225, counted twice|8993/405|
|T_c²|324587/2025|-37306/2025, counted twice|1111/9|
|T_b T_c|791231/6075|-224006/6075, counted once as both orders|2521/27|

For example the T_b pair sum consists of

    -5200/729, 0, -208/405, -16/135,
    80/9, -17888/405, 488/45,
    -416/45, -28/15, -136/25.

The T_c pair sum is

    5720/81,11/9,-168/5,-104/15,
    7/9,-140/3,-20/3,0,-4/5,272/75.

The mixed paired sum is

    21580/243,68/27,-5672/135,298/135,
    166/27,-2468/27,374/135,-68/15,-8/3,292/225.

Each entry is simply the indicated product(s) from the two displayed five-matrices. With det(I+T)=1+trT+((trT)^2-trT²)/2+..., the actual minor coefficients become

    z0=-1215,
    z_b=-10395, z_c=-10935,
    z_bb=-30978, z_bc=19890, z_cc=25785.

For example z_bb=-1215*(3442/135), z_bc=-1215*(-442/27), z_cc=-1215*(-191/9). Here the subscripts bb,bc,cc denote COEFFICIENTS, not unnormalized second derivatives. All numbers follow from written products above, not the author's determinant table.

## 5. ALL three quadratic determinant coefficients

Since D=g^T(bk_b+ck_c), its total-degree-two coefficients at a=1 are

    [b²]D=z0*(ell_b k_b)=174960,
    [bc]D=-180z_b+z0*(ell_b k_c+ell_c k_b)=-48600,
    [c²]D=-180z_c+z0*(ell_c k_c)=-571050.

Thus the homogeneous quadratic term in a,b,c is

    a^4(174960b²-48600bc-571050c²).

This is an actual evaluation of all three quadratic terms, not just a sign comparison or a specialization.

For u,v use T=u+v,d=u-v, a=1+T/2,b=d/2,c=-T. Including the degree-two contribution from218700a^5 c, the resulting degree-two part of -D/60 is

    18630T²-405Td-729d²
      =17496u²+38718uv+18306v².

Therefore all THREE degree-two coefficients agree with F126/J41 at the required global scale det M=729D=-43740*(-D/60).

## 6. ALL four cubic determinant coefficients

This computation avoids unexplained second left-null-vector solves. Define the two explicit source-coordinate vectors (column2 coordinate zero)

    h_b=(68/9,0,4/9,0,-6,0)^T,
    h_c=(118/9,0,77/9,2,-38,-14/3)^T.

Multiplication gives

    A h_b=k_b,
    A h_c=k_c-180e3.

Their needed B/C images are

    B h_b=(22,-38,-50,-32,112/3,46)^T,
    C h_b=(4,4/3,-36,-24,16,-124/3)^T,
    B h_c=(-75,27,-347/3,-1241/9,1301/9,167)^T,
    C h_c=(-5,-10/3,0,-275/3,80,-320/3)^T.

For instance these follow from the first/third/fifth columns for h_b and the first/third/fourth/fifth/sixth for h_c. All are direct small rational products of the GIVEN coefficient matrices. No tensor-source identity is assumed.

Because higher coefficients of ell have third component zero and annihilate the other-five-column pencil, they obey

    ell_bb k_b=-ell_b B h_b,
    ell_bc k_b=-ell_b C h_b-ell_c B h_b,
    ell_cc k_b=-ell_c C h_b,

and the corresponding k_c identities with h_c. Put w=C h_b+B h_c. The four exact contractions needed after grouping are

    ell_b B h_b=-1248,
    ell_b w+ell_c B h_b=66364/9,
    ell_c w+ell_b C h_c=316174/9,
    ell_c C h_c=69340/3.

For additional traceability,

    w=(-71,85/3,-455/3,-1457/9,1445/9,377/3)^T,
    ell_b w=55492/9, ell_c B h_b=1208,
    ell_c w=231214/9, ell_b C h_c=9440.

Substitute the already derived z coefficients and first ell coefficients. The FOUR cubic coefficients are

    [b³]D=z_b*(-144)+z0*(1248)=-19440,

    [b²c]D=-180z_bb+1580z_b-144z_c
                    +z0*(-66364/9)=-314280,

    [bc²]D=-180z_bc+2090z_b+1580z_c
                    +z0*(-316174/9)=100440,

    [c³]D=-180z_cc+2090z_c
                    +z0*(-69340/3)=587250.

Hence the homogeneous cubic term is

    a³(-19440b³-314280b²c+100440bc²+587250c³).

After restoring the lower-degree a-expansions and dividing by-60, the total-degree-three term in u,v is

    37935T³-1647T²d-(5535/2)Td²+(81/2)d³
      =33561u³+114804u²v+118341uv²+36774v³.

The conversion includes the a^5 c and a^4 quadratic contributions; it does not mistake the homogeneous a,b,c term for the shifted u,v coefficient. Thus all FOUR degree-three coefficients agree with F127/J42 at the required scale.

## 7. Current coefficient ledger and global-scale qualification

Together with v35-D's written derivation, the established coefficients of the target-normalized -D/60 are exactly

| Degree | Actually derived coefficient row |
|---|---|
|0|0|
|1|3645,3645|
|2|17496,38718,18306|
|3|33561,114804,118341,36774|

All nine nonconstant terms have a written derivation. Their common relation to M is exact: M=3N gives detM=729D, and729*60=43740. Scaling2M multiplies its determinant by64. These scalar relations are proved; they do not establish the unknown higher coefficients.

This does NOT prove the ENTIRE identity detM=-43740P. In particular no positive-quadrant conclusion may be inferred from the nine known terms while the remaining terms are unspecified. No coefficient positivity is inherited merely because the author copied its table or printed a boolean.

## 8. Eighteen exact NOT_RECONSTRUCTED obligations

The remaining literal obligations are the following individual coefficient equalities in the u,v expansion of detM, each expected to be-43740 times the listed source-normalized number:

| Degree | Monomials | UNRECONSTRUCTED source claims |
|---|---|---|
|4|u⁴,u³v,u²v²,uv³,v⁴|32184;148365;239004;158895;36972|
|5|u⁵,u⁴v,u³v²,u²v³,uv⁴,v⁵|15438;89052;195747;202992;99540;18621|
|6|u⁶,u⁵v,u⁴v²,u³v³,u²v⁴,uv⁵,v⁶|2964;20414;56828;80639;61380;23913;3762|

These are F128–130/J43–45. The original exact grouping formula in v35-D §5 continues to identify each finite cofactor sum, but those EIGHTEEN evaluations have not been completed in writing here. No alternative all-u,v≥0-not-both-zero factorization/sign certificate has been established.

## 9. FATAL/MAJOR/MINOR and composition boundary

- **New degree2/3 algebra:**0F/0M/0 substantive MINOR at the explicit written partial scope above.
- **Full determinant identity/all27 coefficients:** **NOT_RECONSTRUCTED; MAJOR load-bearing acceptance gate remains**, now eighteen rather than twenty-five coefficients.
- **All-quadrant sign/nonzero determinant:** NOT established by this return.
- **Pencil equals actual D3 images / columns S1–S6:** OUT OF SCOPE; no verdict. v35-A/B/C own those gates.
- **Actual invariant3→5/full-source injection:** not accepted here; determinant completion and parent composition remain required.

No FATAL contradiction or incorrect author coefficient is demonstrated. The old partial verdict is preserved, not retroactively rewritten. Historical scientific computations under the withdrawn exception remain unadmitted and supply zero executable verification. This serial SAME-domain supplied-proof derivation is not blind, independent-family, cross-vendor, human, formal/kernel, novelty or worldwide-priority acceptance. All author/shared/pinned files remain unchanged.
