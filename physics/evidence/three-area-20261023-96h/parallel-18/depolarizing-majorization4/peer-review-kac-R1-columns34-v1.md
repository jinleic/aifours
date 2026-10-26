# v35-B — written derivation of all six detector rows for S3 and S4

Reviewer PhysicsDepol4-2. Actual activation clock from the exposure ACK: **Sun Oct 25 04:58:52 PDT 2026**. This header uses the observed activation time, not an invented exact settlement clock. WRITTEN reconstruction only; HOLD/v7 binding. No scientific interpreter/eval/arithmetic program/symbolic program/enumeration/replay/solver/CLI/subagent was used.

## 1. Frozen sources, coverage, exposure and verdict

- `level5-written-R1-R2-reconstruction-v1.md`, complete LF1–306, SHA256 `ef814cb9d86583ed4d81811cc47ac83bbc054c642778447602a6288509c8b91d`.
- `level5-full-invariant-quotient-v1.md`, complete LF1–144, SHA256 `a539f8b96afa6314367db190ae38bbd9c2f33afc517c2e96f5eb7a7d731129aa`.

Both are in `mathematics/evidence/three-area-20261023-96h/parallel-18/kac-moody/`. Call them **R** and **Q**, respectively, in source-line references below.

Mandatory literal packet `peer-review-wave-v35-kac-R1-columns34-sources-v1.md`, SHA256 `fc1654b7b2a6ace56b145c6fa1d1d41d2c873f45d2b1a065715478273d86cf9c`, was read completely, all464 packet lines including306+144 author-source lines, in three ranged windows. No truncated source line remains unread. Metadata hashes of both authorsources and the packet match v35-B. The packet receipt was read completely; its literal-equality claim is parent metadata, not an independent regeneration performed here.

Manifest SHA256 `8bdc46291eb47f18245077588ad3811e2f5fad420e485f0710e7530cc5971b7a`; receipt SHA256 `bf7674a0c9cd1ea7dda58cc0e94d066e3a78f0aee03026665b315de96eddbacb`. Parent erratumv7 was reread in full before the source body. `peer-review-kac-R1-columns34-ack-v1.json` records exposure before reconstruction. v32-H was fully returned before this source was opened; no other detector-slice or determinant review was read or assumed.

**Verdict at the assigned column slice: 0 FATAL / 0 MAJOR / 0 MINOR.** All **18 scalar coefficients for S3 and18 for S4** are derived below, from the trace/right-normed definitions, not from an unadmitted arithmetic output. This is supplied-proof same-harness WRITTEN support only. No other column, determinant, full source basis, invariant injectivity or actual3-to5 quotient is certified by this return.

## 2. Dual normalization and original lowering

**Reconstructed: Q LF37–59,76–93; R LF232–245.**

Root-unit trace duality reverses Eij to Eji. The Cartan trace Gram is `[[2,-1],[-1,2]]`, whose inverse is `(1/3)[[2,1],[1,2]]`. Thus d6=(2H1+H2)/3=diag(2,−1,−1)/3 and d7=(H1+2H2)/3. Consequently every declared c_i equals3d^i, with no root/Cartan exception. The five source slots give243.

The raw source orders assigned here are sigma3=(0,2,1,3,4), sigma4=(0,2,3,1,4), with raw factors−27 and81. Therefore after contracting unscaled trace-duals, the final multipliers are

`S3:243/(-27)=-9`, `S4:243/81=3`.                    (N)

These are source multipliers, not a symmetrization over equal detector letters.

Move the level-zero result of `[w_x,u_y]` rightwards through the tensor word. Its commutator with EACH later letter gives precisely

`a[[x,b_p],b_q]+b[xb_p+b_p x,b_q]-c Tr(xb_p)b_q`, p<q.

The Jordan scalar trace subtraction commutes with b_q and disappears only inside that matrix commutator. The central term does not disappear: `[z0,u_y]=c u_y` contributes once for each later position. The rightmost level-zero remainders cancel on a Lie polynomial of degree>=2: for each level-zero basis coefficient, the resulting scalar-valued generator derivation annihilates a two-letter bracket and then every higher Lie bracket by induction. Thus the literal ordered-pair recurrence retains the actual central level action and the tensor order.

## 3. Cut/join identities checked before using them

**Reconstructed: R LF234–272.**

The trace-completeness identities are

`sum_p d^p M b_p=Tr(M)I-M/3`,

`sum_p d^p Tr(Mb_p)=M-Tr(M)I/3`.

For a source cycle rotated as `(P,A,Q,B)`, contract q first. The a term gives `[Z,[x,b_p]]` and the b term gives `[Z,xb_p+b_p x]`. Expanding and then contracting p gives

`K_a=Tr(AZx)TrB-Tr(AZ)Tr(xB)-Tr(Ax)Tr(ZB)+TrA Tr(xZB)`,

`K_b=Tr(AZx)TrB+Tr(AZ)Tr(xB)-Tr(Ax)Tr(ZB)-TrA Tr(xZB)`

`       +(2/3)[Tr(AxZB)-Tr(AZxB)]`,

`K_c=-Tr(xAZB)`.                                      (CJ)

For example the four b completeness corrections are−(1/3)Tr(AZxB),−(1/3)Tr(AZxB),+(1/3)Tr(AxZB),+(1/3)Tr(AxZB). They leave EXACTLY the displayed2/3 correction; the analogous a corrections cancel. This checks its sign and normalization independently.

For slots in different cycles, replacing A by A−Tr(A)I/3 gives `J_a=Tr(B[Z,[x,A]])`, `J_b=Tr(B[Z,xA+Ax])−(2/3)TrA Tr(B[Z,x])`, and `J_c=−Tr(xA)Tr(ZB)`. This checks the general reduction, but J is NOT used by assigned single-trace sources3/4 and does not certify any product-trace-source column.

## 4. First perform the sixteen right-normed permutations symbolically

This step removes the sixteen R terms BEFORE numerical trace paths. It is not a copy of the detector matrix.

Write `C_tau(M)=Tr(M0 M_tau1 M_tau2 M_tau3 M_tau4)` for a cyclic order canonically starting at physical slot0. For each source let h3(tau),h4(tau) be its resulting coefficient after expanding the right-normed bracket and collecting cyclically identical traces. The unscaled tensor coefficient is the sum of h_j C_tau, with the global243 left outside.

The eight permutations of slots1..4 in `[1,[2,[3,4]]]` are

`1234(+),1243(-),1342(-),1432(+),2341(-),2431(+),3421(+),4321(-)`.

Placing0 on the left gives the first eight degree-five terms; placing0 on the right gives their negatives. For a first-half trace cycle tau, that second cycle is obtained by subtracting1 from EVERY physical slot index modulo5 and rotating back to start at0. The resulting first-half cycles are:

|sign|source3 cycle|source4 cycle|
|---|---|---|
|+|02134|02314|
|−|02143|02413|
|−|04123|04213|
|+|04132|04312|
|−|01423|01243|
|+|01432|01342|
|+|03412|03142|
|−|03421|03241|

Thus the COMPLETE collected h table, including zeros, is

|tau after initial0|h3|h4|
|---|---:|---:|
|1234|0|0|
|1243|1|−1|
|1324|0|1|
|1342|0|1|
|1423|−2|0|
|1432|1|−1|
|2134|1|0|
|2143|−2|0|
|2314|0|0|
|2341|−1|0|
|2413|0|0|
|2431|0|1|
|3124|1|0|
|3142|0|0|
|3214|−1|0|
|3241|1|−1|
|3412|1|−1|
|3421|−1|0|
|4123|−1|0|
|4132|1|0|
|4213|0|0|
|4231|1|0|
|4312|0|1|
|4321|0|0|

For instance source4's first-half02314 cancels its01342 second-half image, while first-half02413 cancels its own shifted second-half image. This is why only eight nonzero source4 cycles remain. No cyclic factor5 is added: cyclic rotation is only a canonical representation of the SAME trace.

## 5. The only nonzero matrix-unit trace paths needed

Use these actual output dual matrices:

`A=E21=d0`, `B=E12=d1`, `C=E32=d2`,

`D=E23=d3`, `V=E31=d4`, `H=d6=diag(2,-1,-1)/3`, `x=E13`.

The six detector dual words are

`AABC, AACB, ABAC, ABVH, ABHV, ACCD`.

For rows1–3, the only closed length-five root path is cyclically `(x,C,A,B,A)`. The two named A slots give TWO labeled cycles, each of trace1; they are added, not divided by2!. The only nonzero2+3 trace partition is pair(A,B) and triangle(x,C,A), again with the two assignments of A counted.

For row6 the length-five path is `(x,C,D,C,A)` with the two assignments of C; its nonzero partition is pair(C,D) and triangle(x,C,A).

For rows4/5 the root path is `(x,V,B,A)`. Inserting H after x,V,B,A gives respectively trace weights

`−1/3, 2/3, −1/3, 2/3`.                             (H)

The only nonzero2+3 partitions are:

- pair(A,B), with triangle `x,V,H` of value2/3 or `x,H,V` of value−1/3;
- pair(x,V), with triple `A,B,H` of value−1/3 or `A,H,B` of value2/3, including cyclic rotations of each triple.

These statements follow by `Eij Ekl=delta_(j,k) Eil` and reading the diagonal H entry at the visited vertex. Every other path misses a matrix-unit join or a final diagonal return. They determine all the trace evaluations below; no summed basis index remains.

## 6. Ordered deletion, central coefficients and adjacent long traces

For each deleted physical slot i=0,1,2,3, insert x there in the five slots and fill the remaining slots by the detector dual word in order. Let F_i be the h-weighted sum of the surviving length-five paths. Every table pair below is ordered `(source3,source4)` BEFORE source multipliers(N).

The c coefficient of the unscaled contraction is

`C_total=−sum_(i=0)^3 (4−i) F_i`.                       (C)

Indeed each of the4−i choices of later acted-on slot has `K_c=−Tr(xAZB)`; after contraction the trace is the same x-inserted source coefficient. There is no later slot when i=4.

|row|F0|F1|F2|F3|C_total|
|---|---|---|---|---|---|
|1|(2,0)|(−3,0)|(1,0)|(2,−1)|(−3,1)|
|2|(1,−1)|(0,1)|(−1,0)|(0,0)|(−2,1)|
|3|(−1,0)|(1,−1)|(0,2)|(−1,0)|(2,−1)|
|4|(−5/3,1/3)|(1/3,2/3)|(0,−1/3)|(4/3,−2/3)|(13/3,−2)|
|5|(0,0)|(4/3,−1)|(1,0)|(−2,2/3)|(−4,7/3)|
|6|(−1,1)|(1,0)|(−3,0)|(1,−1)|(6,−3)|

For example row1,i1 has the two surviving cycles03214 and01423, of h weights(−1,0) and(−2,0), giving F1=(−3,0). Row4,i0 has nonzero weighted contributions `(−2/3,0)`, `(−1/3,1/3)`, `(−2/3,0)` from03421,03241,03214; their sum is the listed F0. This also displays the Cartan denominator rather than treating H as a root.

For each surviving path, let n_+ be1 if the slot AFTER x has physical index>i and n_- be1 if the slot BEFORE x has index>i. The adjacent-pair long-trace contributions in(CJ) are

`A_i=3 sum h(path)*(n_++n_-)`,

`B_i=3 sum h(path)*(n_-−n_+)`,                         (AB)

where trace weights(H) are included. The second expression is only the±3 base part of K_b; its essential2/3 correction is kept separately in §8. The grouped values are

|row|A0,A1,A2,A3|B0,B1,B2,B3|
|---|---|---|
|1|`(12,0),(-12,0),(3,0),(6,-3)`|`(0,0),(6,0),(-3,0),(-6,3)`|
|2|`(6,-6),(0,3),(-3,0),(0,0)`|`(0,0),(0,-3),(3,0),(0,0)`|
|3|`(-6,0),(3,-3),(0,9),(-3,0)`|`(0,0),(-3,3),(0,-3),(3,0)`|
|4|`(-10,2),(3,2),(2,-1),(1,0)`|`(0,0),(1,-2),(2,1),(-1,0)`|
|5|`(0,0),(4,-3),(5,-2),(-5,1)`|`(0,0),(-4,3),(-1,-2),(5,-1)`|
|6|`(-6,6),(3,0),(-3,0),(0,0)`|`(0,0),(-3,0),(3,0),(0,0)`|

This table is just the neighboring-slot count on the explicit paths and h table. For instance row1,i1 has n_+=1 for both paths, n_-=1 only for03214; thus A1=3[2(−1)+(−2)]=−12 and B1=3[0(−1)−(−2)]=6.

## 7. All product-trace terms, with signs and physical order

Here is an explicit counting rule covering the remaining product terms of(CJ), not an unexplained residual fitted to the advertised matrix.

For a partition with pair(p,q), triangle(x,t,s), write I_j=1 if physical slot j>i, and0 otherwise. Let h(P,t,s,p,q) mean the h value of that cyclic source order after rotating to physical0, P being deleted slot i. The four possible nonzero product configurations group as

`U_i=h(P,t,s,p,q)(I_s−I_p)`

`       +h(P,t,s,q,p)(I_s−I_q)`,

`V_i=h(P,p,q,t,s)(I_t−I_q)`

`       +h(P,q,p,t,s)(I_t−I_p)`.                        (UV)

Multiply by the trace value of the triangle and sum all permitted assignments. Their a contribution is U_i+V_i and their b contribution is U_i−V_i. To see the signs directly: cycles(P,t,s,p,q) arise from the first and third products of(CJ), with acted-on slots s and p; cycles(P,p,q,t,s) arise from the second and fourth products, with acted-on slots q and t. The second/fourth signs reverse for b, exactly giving(UV).

For pair(x,V) in rows4/5, the triple is a cyclic rotation(T1,T2,T3) of(A,B,H) or(A,H,B), with its actual trace weight. Add to U_i the term

`h(P,V,T1,T2,T3)(I_V−I_T1)`,

and to V_i the term

`h(P,T1,T2,T3,V)(I_V−I_T3)`.                           (XV)

This comes from the same four products with x now in the length-two trace. In particular neither orientation of the Cartan triple is silently discarded.

All U0,V0 vanish because every other physical index is>0. The complete remaining grouped product terms are

|row|U1|U2|U3|V1|V2|V3|
|---|---|---|---|---|---|---|
|1|(1,0)|(−1,0)|(0,0)|(0,0)|(−1,0)|(1,0)|
|2|(1,0)|(1,0)|(0,0)|(−1,0)|(1,0)|(0,0)|
|3|(−1,0)|(0,0)|(0,0)|(0,1)|(1,−1)|(−1,0)|
|4|(4/3,0)|(−1/3,0)|(0,1)|(1/3,−1)|(2/3,0)|(−1,0)|
|5|(−7/3,0)|(7/3,−1)|(−4/3,0)|(2/3,1)|(7/3,−1)|(−8/3,1)|
|6|(−1,0)|(2,0)|(−2,0)|(0,0)|(1,−1)|(−1,1)|

For additional traceability, in row4 the pair(A,B) part alone has total U=(1,0), V=(0,0). The pair(x,V) part has U=(0,1), V=(0,−1), using weights−1/3 and2/3 from(H). In row5 these totals are respectively `U=(-1,0),V=(0,0)` and `U=(-1/3,-1),V=(1/3,1)`.

As a root-word example, row2,i1 selects triangle s=A2,t=C3 and pair p=A0,q=B4. Its U term is h(1,3,2,0,4)=h04132=(1,0); its V term is h(1,4,0,3,2)=h03214=(−1,0). The other triangle assignment contributes zero. This yields the displayed U1,V1 directly from physical ordering, not from a target value.

## 8. Essential b single-trace correction, fully retained

The remaining correction is `(2/3) E_i`, where E_i is the sum of `Tr(AxZB)−Tr(AZxB)` with h weights. It can be evaluated without another160-term expansion by removing P from a source cycle. For a cyclic order w of the four fixed output slots, define

`H_i(w)=sum_(four cyclic rotations w') h(P,w')`.

That is, sum the four source cycles obtained by inserting P in the four gaps of w; it is an explicit sum of FOUR entries of the h table.

For root rows1–3, use both orders w=(C,A1,B,A2). The correction is

`E_i=sum_w H_i(w)(I_C−I_(A2))`.

For row6 use both w=(C1,D,C2,A), with factor I_(C1)−I_A. These factors express that x must be immediately before its outgoing C or immediately after its incoming A to close the trace path.

For Cartan rows put

`w0=(V,B,A,H)`, `w1=(V,H,B,A)`, `w2=(V,B,H,A)`.

The four H-placement trace weights(H) give

`E_i=H_i(w0)[(2I_V+I_A)/3−I_H]`

`       +(I_V−I_A)[2H_i(w1)−H_i(w2)]/3`.              (E)

The COMPLETE grouped sums are

|row|E1|E2|E3|sum E_i|
|---|---|---|---|---|
|1|(−2,0)|(0,0)|(−1,0)|(−3,0)|
|2|(1,0)|(0,0)|(0,0)|(1,0)|
|3|(2,0)|(1,2)|(2,0)|(5,2)|
|4|(−1,0)|(−1/3,−2)|(0,0)|(−4/3,−2)|
|5|(2,0)|(2/3,2)|(−1/3,0)|(7/3,2)|
|6|(−1,0)|(0,−2)|(0,0)|(−1,−2)|

E0 is zero in every row. As an explicit root correction, row1,i1 has only the closing-A0 cycle w=(4,2,3,0). Its four P insertions give h01423+h04123+h04213+h04231=`(-2,0)+(-1,0)+(0,0)+(1,0)=(-2,0)`.

For a Cartan check, row4,i2 has

`H_i(w0)=(1,2)`, `H_i(w1)=(0,-2)`, `H_i(w2)=(0,0)`.

Here I_V=I_H=1,I_A=0; formula(E) gives `[-(1,2)+2(0,-2)]/3=(-1/3,-2)`. This displays the normalization causing the ninths in the final b coefficient. Omitting the2/3 correction would change the assigned matrix entries.

## 9. Assemble all36 scalar coefficients; comparison is not a premise

Let A=sum A_i, B=sum B_i, U=sum U_i, V=sum V_i, E=sum E_i. The unscaled affine coefficients are

`(coefficient_a, coefficient_b, coefficient_c)`

` =(A+U+V, B+U−V+(2/3)E, C_total)`.                  (SUM)

All preceding groups were obtained from definitions and matrix-unit paths. Their totals are

|row|A|B|U|V|E|C_total|
|---|---|---|---|---|---|---|
|1|(9,−3)|(−3,3)|(0,0)|(0,0)|(−3,0)|(−3,1)|
|2|(3,−3)|(3,−3)|(2,0)|(0,0)|(1,0)|(−2,1)|
|3|(−6,6)|(0,0)|(−1,0)|(0,0)|(5,2)|(2,−1)|
|4|(−4,3)|(2,−1)|(1,1)|(0,−1)|(−4/3,−2)|(13/3,−2)|
|5|(4,−4)|(0,0)|(−4/3,−1)|(1/3,1)|(7/3,2)|(−4,7/3)|
|6|(−6,6)|(0,0)|(−1,0)|(0,0)|(−1,−2)|(6,−3)|

Equation(SUM) gives the following unscaled triples. APPLY the source multipliers−9 and3 from(N) only after this contraction:

|row|source3 unscaled(a,b,c)|source4 unscaled(a,b,c)|S3 final(a,b,c)|S4 final(a,b,c)|
|---|---|---|---|---|
|1|(9,−5,−3)|(−3,3,1)|(−81,45,27)|(−9,9,3)|
|2|(5,17/3,−2)|(−3,−3,1)|(−45,−51,18)|(−9,−9,3)|
|3|(−7,7/3,2)|(6,4/3,−1)|(63,−21,−18)|(18,4,−3)|
|4|(−3,19/9,13/3)|(3,−1/3,−2)|(27,−19,−39)|(9,−1,−6)|
|5|(3,−1/9,−4)|(−4,−2/3,7/3)|(−27,1,36)|(−12,−2,7)|
|6|(−7,−5/3,6)|(6,−4/3,−3)|(63,15,−54)|(18,−4,−9)|

For instance row5 source3 has `a:4−4/3+1/3=3`, `b:−4/3−1/3+(2/3)(7/3)=−1/9`, and c=−4. Multiplication by−9 gives(−27,1,36). Thus the small positive b entry is not a sign guessed from the printed matrix.

These final triples agree with columns3/4 of Q LF102–107, coefficient by coefficient. All18+18 scalar coefficients have now been accounted for; **no entry in the assigned two columns remains NOT_RECONSTRUCTED**.

## 10. Exact exclusions and remaining acceptance gates

This review reconstructs ONLY the two assigned columns and the definitions/contraction tools needed for them. The following remain **NOT_RECONSTRUCTED by this slice**:

- Columns1,2,5,6 and their numerical detector values; the J identity check does not certify product-trace columns.
- The six-by-six determinant, all27 nonconstant polynomial coefficients, its scale and its claimed positivity consequence. These belong to the distinct determinant gate.
- The free/actual source dimensions, complete source-basis assertion, actual T4/T5 isotypic facts and full invariant/3-to5 quotient injectivity. They are not consequences of two columns alone.
- R2's Clebsch vectors, Hermitian norms, projected witnesses and its determinant996; their source bodies were read for coverage, but this assignment gives no R2 verdict.
- Any seven nontrivial primitive lowering-map rank, H13 authentication, general F5 or general Serre theorem.
- Historical unadmitted arithmetic and execution attestations, executable/finite-certificate, formal/kernel, human, cross-vendor or novelty acceptance.

**Scoped disposition:** complete WRITTEN reconstruction of R1 columnsS3/S4 at the pinned bytes, with literal affine coefficients in a,b,c. No mathematical correction identified in those columns. Full R1 acceptance still requires the other ACTUAL column returns, the determinant gate and parent composition; a title or copied arithmetic boolean supplies none of them.
