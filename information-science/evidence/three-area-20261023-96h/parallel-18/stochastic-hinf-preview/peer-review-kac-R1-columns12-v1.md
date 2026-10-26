# v35-A — complete written derivation of R1 columns S1 and S2

Reviewer **InfoHinfPreview-2**, retaining info-3. Author **MathKacMoody**. Actual ACK clock: **Sun Oct 25 04:59:49 PDT 2026**; actual clock after the handwritten derivation and before this return: **Sun Oct 25 05:12:11 PDT 2026**, both returned `/bin/date` outputs.

## 1. Verdict and exact delivered coefficient count

**0 FATAL / 0 MAJOR / 0 MINOR findings in the assigned two-column detector slice.** All **18 scalar a,b,c coefficients in column S1 and all18 in column S2** are derived below from trace duality and the right-normed source definitions. There are **no NOT_RECONSTRUCTED coefficients among these36**.

The derivation is grouped paper algebra, not a copied matrix or interpreter boolean. Its main intermediate objects are universal trace formulas H1/H2, an eight-term right-normed four-letter coefficient functional, and explicitly evaluated matrix-unit/Cartan trace groups. These independently produce the two columns at the end.

**No verdict on the other four columns, the six-by-six determinant, full source independence, actual3-to5 quotient, general F5 or the full Serre problem is supplied.** This is one of four disjoint v35 gates. The domain is a same-harness different-domain supplied-proof written reconstruction, not blind/cross-vendor/configured-dual-family/human/formal/executable/novelty acceptance.

## 2. Pins, complete literal coverage, exposure and execution boundary

Fresh metadata hashes matched the assignment:

| Record | SHA-256 |
|---|---|
| v35 manifest | `8bdc46291eb47f18245077588ad3811e2f5fad420e485f0710e7530cc5971b7a` |
| v35 packet receipt | `bf7674a0c9cd1ea7dda58cc0e94d066e3a78f0aee03026665b315de96eddbacb` |
| mandatory literal packet `peer-review-wave-v35-kac-R1-columns12-sources-v1.md` | `df194c61feadb5e6697b69775e30835622c84addf8bffec532218b725f92e996` |
| `level5-written-R1-R2-reconstruction-v1.md` (W) | `ef814cb9d86583ed4d81811cc47ac83bbc054c642778447602a6288509c8b91d` |
| `level5-full-invariant-quotient-v1.md` (F) | `a539f8b96afa6314367db190ae38bbd9c2f33afc517c2e96f5eb7a7d731129aa` |

The first three records are under `institute/runs/three-area-2026-10-23-96h/`; W/F are under `mathematics/evidence/three-area-20261023-96h/parallel-18/kac-moody/`. The complete464-line literal packet was read in ranges covering LF1–178,179–323,324–464, including **all306 W lines and all144 F lines**. The complete31-line packet receipt, exact v35-A entry/common rules and complete39-line parentv7 were read before author body. No displayed long-line truncation was accepted as complete. Source citations below refer to the author LF numbers reproduced literally in the packet.

The ACK/exposure record was written first in `peer-review-kac-R1-columns12-ack-v1.json`. Prior v31-A/v32-C reviews were fully returned before this work; the v32-C actual path/hash/verdict was sent to Main before starting this ACK. Prior exposure was round-level summaries of earlier Kac row-one/three-plane claims and the existence of historical Kac reviews in this owner's root. Those historical reviews were not reread or inherited. I read the present claimed matrix while reading the complete source, so this is not blind reconstruction; the derivation below does not use its entries as equations or fitting constraints.

**No scientific eval/interpreter, arithmetic or symbolic program, finite enumeration, replay, solver, simulation, external CLI, nested agent, git operation, deletion or author/shared write was used.** All calculations below are written manipulation. Old unadmitted coefficient/determinant outputs receive zero credit. Parentv7/HOLD remain binding; no scientific GO exists.

## 3. Duals, normalization and cut/join signs — F LF35–59, W LF230–272

Write d^i for the unscaled trace-dual of b_i. Root-unit duals are transposes. The Cartan trace Gram is

$$\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\qquad
G^{-1}={1\over3}\begin{pmatrix}2&1\\1&2\end{pmatrix}.$$

Thus `d6=(2H1+H2)/3`, `d7=(H1+2H2)/3`, as in F; every source coefficient matrix c_i equals **3d^i**. All five source slots therefore give the common factor `3^5=243`, with no factor attached to the output coefficient dual.

Full matrix-unit completeness, after subtracting the scalar line with dual I/3, gives exactly

$$\sum_p d^p M b_p=\operatorname{Tr}(M)I-M/3,$$

$$\sum_p d^p\operatorname{Tr}(M b_p)=M-\operatorname{Tr}(M)I/3.$$

For one trace cycle `Tr(d^p A d^q B)` and traceless output dual Z, contract q first. The a part becomes

$$\sum_p\operatorname{Tr}(d^p A[Z,[x,b_p]]B).$$

Expanding the double commutator gives four terms. Their product traces are, respectively,

$$\operatorname{Tr}(AZx)\operatorname{Tr}B,
-\operatorname{Tr}(AZ)\operatorname{Tr}(xB),
-\operatorname{Tr}(Ax)\operatorname{Tr}(ZB),
\operatorname{Tr}A\operatorname{Tr}(xZB).$$

Their scalar-line corrections are

$$-\tfrac13\operatorname{Tr}(AZxB),\quad
+\tfrac13\operatorname{Tr}(AZxB),\quad
+\tfrac13\operatorname{Tr}(AxZB),\quad
-\tfrac13\operatorname{Tr}(AxZB),$$

and cancel. This derives K_a in W(8.3).

For b, expand `[Z,xb_p+b_p x]`. The product-trace signs are `+,+,-,-`; the correction sum is

$$\tfrac23\operatorname{Tr}(AxZB-AZxB)
 =\tfrac23\operatorname{Tr}(A[x,Z]B).$$

For c, direct duality gives `-Tr(xAZB)` because x,Z are traceless. Thus the used same-cycle formulas, including the essential sign and normalization of the b correction, are

$$
\begin{aligned}
K_a&=\operatorname{Tr}(AZx)\operatorname{Tr}B
-\operatorname{Tr}(AZ)\operatorname{Tr}(xB)
-\operatorname{Tr}(Ax)\operatorname{Tr}(ZB)
+\operatorname{Tr}A\operatorname{Tr}(xZB),\\
K_b&=\operatorname{Tr}(AZx)\operatorname{Tr}B
+\operatorname{Tr}(AZ)\operatorname{Tr}(xB)
-\operatorname{Tr}(Ax)\operatorname{Tr}(ZB)
-\operatorname{Tr}A\operatorname{Tr}(xZB)
+\tfrac23\operatorname{Tr}(A[x,Z]B),\\
K_c&=-\operatorname{Tr}(xAZB).
\end{aligned}                                                     \tag{1}
$$

For completeness, W(8.4) has also been checked algebraically, though columns1/2 have only single source cycles. Separate cycles project A to `A0=A-Tr(A)I/3`. The a commutators remove the scalar part, whereas `xA0+A0x=xA+Ax-(2/3)Tr(A)x`. Projecting B against the remaining traceless commutator gives precisely

$$J_a=\operatorname{Tr}(B[Z,[x,A]]),$$

$$J_b=\operatorname{Tr}(B[Z,xA+Ax])
       -\tfrac23\operatorname{Tr}A\operatorname{Tr}(B[Z,x]),$$

$$J_c=-\operatorname{Tr}(xA)\operatorname{Tr}(ZB).$$

No mixed-cycle term is needed or silently inserted into either assigned column.

## 4. A smaller exact right-normed grouping instead of160 separate tensor terms

Use the literal local action from F LF76–93:

$$L_x(p,q)=a[[x,b_p],b_q]+b[xb_p+b_p x,b_q]
                       -c\operatorname{Tr}(xb_p)b_q,$$

where x=E13. It is the action of the actual level-zero bracket on a later generator, including the central level action. It acts as a derivation on every later Lie bracket.

Apply lowering directly to the original **right-normed five-letter** bracket. If it hits slot i=0,1,2,3, its level-zero action distributes over each later slot j>i. If it hits the last slot4, the innermost bracket is `[u3,K4]=-K4.u3`; after this the three outer generators remain unchanged. Therefore the exact result is a sum of:

- the ten forward pairs `0<=i<j<=4`, each a right-normed FOUR-letter bracket after deleting i and replacing j by L_x(i,j);
- **one backward terminal term**, with slot4 deleted and slot3 replaced by `-L_x(4,3)`.

This eleven-group formula is derived from the nested brackets themselves. It is equivalent to the source's ten-pair recurrence applied to the sixteen tensor terms, but reduces the bookkeeping to eleven contractions followed by the eight tensor terms of a four-letter bracket. It does not discard the rightmost action. In particular the terminal term matters for the Cartan b coefficient in row5.

For a target's four trace duals D0,D1,D2,D3, define the coefficient functional

$$
\begin{aligned}
\mathcal R H(D)=&\ H(D_0,D_1,D_2,D_3)-H(D_3,D_0,D_1,D_2)\\
&-H(D_0,D_3,D_1,D_2)-H(D_0,D_1,D_3,D_2)\\
&+H(D_3,D_2,D_0,D_1)+H(D_3,D_0,D_2,D_1)\\
&+H(D_0,D_3,D_2,D_1)-H(D_3,D_2,D_1,D_0).
\end{aligned}                                                     \tag{2}
$$

These are the inverse permutations of the exact right-normed four-letter expansion, with its signs. There is no Dynkin normalization division: the source is defined by the literal bracket, not a normalized Lie projection.

## 5. Universal trace groups used in both columns

For an arbitrary ordered quadruple D define

$$T_i=\operatorname{Tr}(x D_iD_{i+1}D_{i+2}D_{i+3})$$

with cyclic subscripts modulo4. Also put

$$U_0=\operatorname{Tr}(xD_0D_2D_1D_3),\quad
U_1=\operatorname{Tr}(xD_2D_1D_3D_0),$$

$$V_0=\operatorname{Tr}(xD_0D_1D_3D_2),\quad
V_1=\operatorname{Tr}(xD_3D_2D_0D_1),\quad
V_2=\operatorname{Tr}(xD_2D_0D_1D_3).$$

The product-trace groups are

$$
\begin{array}{ll}
E_0=\operatorname{Tr}(xD_0)\operatorname{Tr}(D_1D_2D_3),&
E'_0=\operatorname{Tr}(xD_0)\operatorname{Tr}(D_2D_1D_3),\\
E_3=\operatorname{Tr}(xD_3)\operatorname{Tr}(D_0D_1D_2),&
E_2=\operatorname{Tr}(xD_2)\operatorname{Tr}(D_3D_0D_1),\\
F=\operatorname{Tr}(D_0D_1)\operatorname{Tr}(xD_2D_3),&
F'=\operatorname{Tr}(D_0D_1)\operatorname{Tr}(xD_3D_2),\\
G=\operatorname{Tr}(D_2D_3)\operatorname{Tr}(xD_0D_1).&
\end{array}                                                       \tag{3}
$$

All these are unscaled-dual traces. In the following tables the same symbol after applying R means its signed value under (2), not an unevaluated basis sum.

## 6. Deriving the S1 universal coefficients by telescoping

The raw source1 cycle is01234. For a forward pair with deleted i and acted target slot k=j-1, rotate that cycle after the deleted variable. In (1),

$$A=D_i\cdots D_{k-1},\qquad
Z=D_k,\qquad
B=D_{k+1}\cdots D_3D_0\cdots D_{i-1}.$$

For a prefix S of this cycle define

$$\Phi(S)=\operatorname{Tr}(xS)\operatorname{Tr}(S^c)
          -\operatorname{Tr}S\operatorname{Tr}(xS^c),$$

and define Psi with a plus between the two terms. Then `K_a=Phi(prefix through Z)-Phi(prefix before Z)`; the analogous K_b difference uses Psi plus its `2/3` commutator correction. This telescopes for each fixed deleted i.

Here are the complete eleven groups, already summed over all later j for each fixed i; the last row is the negative terminal contraction. Each cell follows directly from (1) and cyclic trace, so no hidden sum remains:

| deleted i / group | a | b | c |
|---|---|---|---|
|0|`6T0`|`0`|`-4T0`|
|1|`3T1-E0`|`-(7/3)T1-(2/3)T0+E0`|`-3T1`|
|2|`3T2+F-G`|`-(7/3)T2-(2/3)T0+F+G`|`-2T2`|
|3|`3T3+E3`|`-(7/3)T3-(2/3)T0+E3`|`-T3`|
|terminal4, acted3|`-3T0-E3`|`-(7/3)T0-(2/3)T3+E3`|`+T0`|

For the b correction at a forward pair, `Tr(A[x,Z]B)=T_k-T_(k+1)`. Summing k and subtracting the terminal correction produces `(2/3)(-2T0+T1+T2)`. This verifies the fractional coefficients and signs in the table.

Summing its rows gives the three pre-four-bracket tensors

$$H_{1a}=3(T_0+T_1+T_2+T_3)-E_0+F-G,$$

$$H_{1b}=-\tfrac{13}3T_0-\tfrac73T_1-\tfrac73T_2-3T_3
                       +E_0+F+G+2E_3,$$

$$H_{1c}=-3T_0-3T_1-2T_2-T_3.                              \tag{4}
$$

The term **+2E3 in H1b must remain**: the forward and negative-terminal product-trace contributions add, rather than cancel. It contributes to the row5 b coefficient. This is one point at which treating the rightmost action casually would give a wrong column.

## 7. Deriving the S2 universal coefficients from its actual source order

The raw source2 cycle is01324, not01234. For deleted slots0,1,2,3, the source cycles after the deleted slot are, respectively,

```
D0 D2 D1 D3,
D2 D1 D3 D0,
D3 D0 D1 D2,
D2 D3 D0 D1.
```

The allowed acted slots are all4, the three except D0, then D3/D2, then D3. The terminal negative pair has `A=D0 D1`, `Z=D3`, `B=D2`. Applying (1) yields the COMPLETE grouped table:

| deleted i / group | a | b | c |
|---|---|---|---|
|0|`6U0`|`0`|`-4U0`|
|1|`3U1-E0'`|`-(7/3)U1-(2/3)U0+E0'`|`-3U1`|
|2|`6T3+E3+E2`|`E3-E2+(2/3)(T2-T0)`|`-2T3`|
|3|`F-G-E2`|`F+G-E2+(2/3)(T3-T0)`|`-T2`|
|terminal4, acted3|`E2+G-F'`|`-E2+G+F'-(2/3)(V1-V2)`|`+V0`|

For example i2 consists of the first and last Q positions in cycle `D3 D0 D1 D2`; their a terms each give3T3 and their b T3 terms cancel. The terminal b correction is exactly `-(2/3)(V1-V2)`, including the terminal minus sign. Thus the changed source order is retained throughout.

Summing gives

$$H_{2a}=6U_0+3U_1+6T_3-E'_0+E_3+E_2+F-F',$$

$$
\begin{aligned}
H_{2b}={}&-\tfrac23U_0-\tfrac73U_1+\tfrac23T_2+\tfrac23T_3
          -\tfrac43T_0-\tfrac23V_1+\tfrac23V_2\\
 &+E'_0+E_3-3E_2+F+F'+2G,
\end{aligned}
$$

$$H_{2c}=-4U_0-3U_1-2T_3-T_2+V_0.                         \tag{5}$$

Equations(4),(5), not the advertised matrix entries, are the formulas evaluated next.

## 8. Matrix-unit trace paths and all six target group evaluations

Use abbreviations

$$A=E_{21},\quad B=E_{12},\quad C=E_{32},\quad D=E_{23},
\quad E=E_{31},\quad H=\operatorname{diag}(2,-1,-1)/3.$$

The target dual quadruples in F's row order are

```
A A B C;   A A C B;   A B A C;
A B E H;   A B H E;   A C C D.
```

All evaluations use `Eij Ekl=delta_(j,k) Eil`, cyclic trace, and the displayed diagonal entries of H. The only root-only closed five-factor trace paths, starting immediately after x=E13, are

```
C A B A     for the AABC multiset,
C D C A     for the ACCD multiset.
```

Each has trace1; every other ordering of those root multisets has trace0. For the Cartan multiset the only nonzero orders after x and their traces are

```
H E B A : -1/3;   E H B A : 2/3;
E B H A : -1/3;   E B A H : 2/3.
```

These path rules collapse all zero single traces without summing a Lie basis.

### 8.1 The complete signed word groups for R

For ANY trace function of the ordered four D's, (2) reduces in the six rows to the following signed word lists. Repeated terms already canceled or combined are shown explicitly:

```
row1: AABC - CAAB - ACAB - AACB + CABA + ACBA
row2: AACB - BAAC - ABAC - AABC + BACA + ABCA
row3: ABAC - 2CABA - ACBA - ABCA + 2CAAB + ACAB
row4: ABEH - HABE - AHBE - ABHE + HEAB + HAEB + AHEB - HEBA
row5: ABHE - EABH - AEBH - ABEH + EHAB + EAHB + AEHB - EHBA
row6: ACCD - ACDC + DCAC - DCCA.
```

For example the two CBAA terms cancel in row1; BCAA cancels in row2; DACC and ADCC each cancel in row6. No actual program or word enumeration was run: these are the eight substitutions of (2), grouped on paper.

For rows1–3, the single-trace functions `T0,T1,T2,T3,U0,U1,V0,V1,V2` are respectively nonzero precisely on the following ordered D words (each with value1):

```
CABA, ACAB, BACA, ABAC, CBAA, AACB, CAAB, BAAC, ABCA.
```

For row6 the analogous words are

```
CDCA, ACDC, CACD, DCAC, CCDA, ADCC, CDAC, CADC, DCCA.
```

Thus their signed coefficients can be read directly from the COMPLETE signed lists, rather than guessed from the final detector matrix.

### 8.2 Complete single-trace group table

Substitute those path rules, and for rows4/5 use the four Cartan paths above. The resulting R values are:

|row|T0|T1|T2|T3|U0|U1|V0|V1|V2|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|1|1|-1|0|0|0|-1|-1|0|0|
|2|0|0|1|-1|0|1|0|-1|1|
|3|-2|1|0|1|0|0|2|0|-1|
|4|1/3|-1|1/3|0|0|1/3|-1/3|-1/3|0|
|5|-2/3|1|0|0|-1/3|0|2/3|0|0|
|6|0|-1|0|1|0|0|0|0|-1|

To make the Cartan grouping explicit, row4 has its T contributions only from HAEB, AHEB and -HEBA: respectively `T2=-1/3`, `(T1,T2)=(-1/3,2/3)`, and `(T0,T1)=(1/3,-2/3)`. Hence `(T0,T1,T2,T3)=(1/3,-1,1/3,0)`. Its U1 is `-1/3+2/3=1/3`, V0 is `-1/3`, and V1 is `1/3-2/3=-1/3`; all other U/V terms vanish by the same four path patterns.

For row5, -AEBH, AEHB and -EHBA give T1 contributions `1/3,2/3,0` and T0 contribution `-2/3`. Its U0 is `-2/3+1/3=-1/3`; its U1 is `1/3-1/3=0`; V0 is `2/3`; V1,V2 vanish. This explains every Cartan single-trace entry rather than treating the fractions as an unexplained table.

### 8.3 Complete product-trace group table

In rows1–3 and6, all E groups vanish because no D_i is E31, the only letter that can make `Tr(xD_i)` nonzero. For rows1–3:

- F detects exactly `ABCA` or `BACA`;
- F' detects exactly `ABAC` or `BAAC`;
- G detects exactly `CAAB` or `CABA`.

For row6 the corresponding pairs are `(CDCA,DCCA)`, `(CDAC,DCAC)`, `(CACD,CADC)`. Apply the signed lists above.

For Cartan rows only `Tr(ABH)=-1/3`, `Tr(BAH)=2/3` and their cyclic rotations are needed. Also `Tr(xEH)=2/3` and `Tr(xHE)=-1/3`. The COMPLETE product group values are:

|row|E0|E0'|E3|E2|F|F'|G|
|---:|---:|---:|---:|---:|---:|---:|---:|
|1|0|0|0|0|0|0|0|
|2|0|0|0|0|2|-2|0|
|3|0|0|0|0|-1|1|0|
|4|0|0|0|0|1|-1|0|
|5|0|0|-1/3|1/3|-1|1|0|
|6|0|0|0|0|-1|1|0|

Here are the possible nontrivial cancellations behind the zero cells. In row4, E3 gives `1/3-2/3+1/3=0`, E2 gives `-1/3-1/3+2/3=0`, and G gives `-1/3+1/3=0`; E0/E0' have no E31 in the initial slot. Its F gives `2/3+1/3=1`, and F' gives `-1/3-2/3=-1`.

In row5, E0 gives `1/3-1/3+2/3-2/3=0`, E0' gives `-2/3+2/3-1/3+1/3=0`, E3 receives only `-1/3`, E2 receives only `1/3`, and G gives `2/3-2/3=0`. Its F is `-1/3-2/3=-1` and F' is `2/3+1/3=1`. In root rows, G is zero by `-1+1` in row1, `2-2` in row3, and absence of either allowed word in rows2/6.

These two intermediate tables, their closed-path rules, and the complete signed word lists account for all nonzero and zero traces used for BOTH columns.

## 9. All36 scalar coefficients, derived from the groups

Substitute the two trace-group tables into (4) and (5). Before applying either source scale, the resulting triples `(a,b,c)` are:

|row|`R(H1a),R(H1b),R(H1c)`|`R(H2a),R(H2b),R(H2c)`|
|---:|---|---|
|1|`(0,-2,0)`|`(-3,1,2)`|
|2|`(2,8/3,-1)`|`(1,-1,-2)`|
|3|`(-1,7/3,2)`|`(4,8/3,0)`|
|4|`(0,10/9,4/3)`|`(3,-7/9,-5/3)`|
|5|`(0,-10/9,-1)`|`(-4,-2/9,2)`|
|6|`(-1,-5/3,2)`|`(4,0,-2)`|

For illustration of the nonzero Cartan arithmetic, row5 in H1b gives

$$\tfrac{26}{9}-\tfrac73-1-\tfrac23=-\tfrac{10}{9},$$

where the last term is **2E3**. Row4 in H2b gives

$$-\tfrac79+\tfrac29-\tfrac49+\tfrac29=-\tfrac79.$$

These are consequences of the full tables, not isolated checks offered in place of the rest.

Finally the raw traces all carry243. The source definitions are `F1=-27 S1`, `F2=27 S2`; hence multiply the first raw triple column by **-9** and the second by **+9**. There is no additional projection or tensor-normalization factor. This yields the exact independently derived assigned columns:

|detector word|S1 coefficients `(a,b,c)`|S2 coefficients `(a,b,c)`|
|---|---|---|
|`(0,0,1,2)`|`(0,18,0)`|`(-27,9,18)`|
|`(0,0,2,1)`|`(-18,-24,9)`|`(9,-9,-18)`|
|`(0,1,0,2)`|`(9,-21,-18)`|`(36,24,0)`|
|`(0,1,4,6)`|`(0,-10,-12)`|`(27,-7,-15)`|
|`(0,1,6,4)`|`(0,10,9)`|`(-36,-2,18)`|
|`(0,2,2,3)`|`(9,15,-18)`|`(36,0,-18)`|

They agree with the corresponding entries of F LF102–107. **All18+18 scalar coefficients, including every zero coefficient, have the displayed grouped derivation.** No specialization in r,s, determinant interpolation, copied positive coefficient list or previous executable output was used.

## 10. Precise unreviewed scope and recommended disposition

1. **Reconstructed:** trace-dual scales for these sources; cut/join signs and scalar corrections; actual central action in the nested lowering recurrence; the full right-normed coefficient functional; every trace group and all36 scalar coefficients of S1/S2.
2. **NOT_RECONSTRUCTED:** the24 entries in source columns S3–S6. No verdict is inherited from this two-column calculation.
3. **NOT_RECONSTRUCTED:** the full six-by-six determinant identity, its27 nonconstant coefficients, scale or positivity on the parameter quadrant. That is the separate v35-D gate.
4. **NOT_RECONSTRUCTED as a target acceptance:** full source independence/basis status, full invariant injectivity, actual3-to5 quotient, the R2 image-witness theorem, the other primitive maps or general Serre equality. The complete W/F bodies were read as required, but this assignment is only the R1 two-column contraction slice.
5. **Named interface, not re-proved presentation theorem:** the local bracket and actual-isotypic/PBW/structural identifications in F LF25–33 and76–93. The calculation above derives the detectors from those displayed definitions and verifies the central level action's use. It does not authenticate every earlier representation-theoretic import.
6. **NOT_PERFORMED:** scientific execution/replay, formal/kernel verification, human/cross-vendor/configured-dual-family review, novelty or parent composition/acceptance.

**Recommendation:** accept this actual v35-A return as a completed no-defect WRITTEN reconstruction of the two named R1 columns, and nothing more. Require all remaining disjoint detector and determinant returns plus parent full read before composing any full R1 or quotient claim. Parentv7 and the global scientific-launch HOLD remain binding; this written result supplies no execution GO.
