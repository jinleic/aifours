# A robustly Hurwitz septic box defeats an entire explicit affine numerator line

Owner **InfoSPR7-2**, slot info-2. Actual preceding `/bin/date`: **Wed Oct 28 18:51:58 PDT 2026**. **WRITTEN-checked-in-kernel candidate with an independently structured exact same-harness replay.** This is a genuine, exact barrier to a named numerator-construction route on one actual robustly Hurwitz box. It is NOT an unrestricted negative box, a universal SPR7 result or a claim that no other numerator exists.

## 1. Exact box and excluded whole line

Let K be the monic septic independent coefficient box with these exact endpoints:

| j | lower | upper |
|---:|---:|---:|
|0|5670911/1280000|5875969/1280000|
|1|13726949/1280000|14744091/1280000|
|2|15135267/640000|15606493/640000|
|3|26184261/640000|27679419/640000|
|4|2717229/256000|575223/51200|
|5|4170591/320000|4592929/320000|
|6|2207/2000|453/400|

It is the `r=679/640` box from the anisotropic boundary bracket: six widths use r around the pinned earlier base midpoint and the s^6 width is halved. All seven widths are strictly positive and §2 proves every actual member Hurwitz.

Define the two explicitly specified monic polynomials

`A(s)=s^7+(2028281/100)s^6+(1971569/100)s^5+(6620777/50)s^4`
`          +(4490113/50)s^3+(160147/4)s^2+(949689/50)s+3/10`,

`G(s)=s^7+(63/25)s^6+(247/20)s^5+(189/10)s^4`
`          +(707/20)s^3+(337/50)s^2+(747/100)s`.

A is the exact common numerator of the smaller nested K_H in `frontier-20261028-larger-nested-box-new-numerator-v1.md`, SHA256 `c1159723feb73d54e1e954998ea421a074c79cf5e1fe20c8a553715b92a14db5`. G is a rational rounding of a finite-grid dual lead and has constant coefficient zero; neither its grid origin nor its status is needed for the exact proof.

**Theorem.** No polynomial on the entire real affine line

`b_eta=(1-eta)A+eta G`, `eta in R`,

is a common strict-positive-real numerator for K. Multiplication by any positive real scalar also cannot help. The proof uses only two actual parity corners and two exact positive squared frequencies; it does not exclude any b outside this line.

## 2. Actual all-member Hurwitz stability

Write the actual parity extremum cubics E_-,E_+,O_-,O_+ as in the frozen JSON. The independently checked rational root brackets for these four cubics produce the six STRICTLY separated bands

| band | exact enclosing interval |
|---|---|
| E1 | `[5327535079/26843545600, 1447957831/6710886400]` |
| O1 | `[7231073823/26843545600, 52974307/167772160]` |
| E2 | `[8816787609/3355443200, 46094469509/13421772800]` |
| O2 | `[11555133659/3355443200, 9100127023/1677721600]` |
| E3 | `[154070379403/26843545600, 98485106183/13421772800]` |
| O3 | `[98510712041/13421772800, 555402053/52428800]` |

Each cubic has positive constant and negative nonzero leading coefficient. The frozen three disjoint sign changes for each cubic force exactly three simple positive roots. Outside an E band the lower/upper E values have the same nonzero sign; the same holds for O. As the six bands are mutually disjoint, at every t>0 at least one complete actual value interval excludes zero. At t=0 all actual a_0>0. No member of K has an imaginary-axis root.

The exact Routh first column of the `(E_-,O_-)` corner is strictly positive and is stored in the receipt. As K is convex and monic of fixed degree, the segment from that actual Hurwitz corner to any member remains in K and avoids the imaginary axis. Root continuity therefore proves EVERY member Hurwitz. This is not an unproved inference merely from stable corners.

## 3. Two exact constraints exclude every eta

Let `P_(a,b)(t)=Re[b(i sqrt(t))a(-i sqrt(t))]`. Take the actual corners

`a_1=(E_-,O_+)`, at `t_1=197/59`, and
`a_2=(E_+,O_+)`, at `t_2=53/203`.

Write `P_(a_i,b_eta)(t_i)=A_i+eta D_i`. Independent exact calculations by both direct monomial expansion and E/O convolution give

`A_1=-3111053405919714332717419/318547390056832000000`,
`D_1= 3295819818853828922267/337444269128000000 >0`,

`A_2= 2786864593859122445419389/72734796211931069440000`,
`D_2=-134089442642294550529/3499018444616450000 <0`.

At the simple rational threshold `eta0=7999/8000`, their exact values are

`A_1+eta0 D_1=-94201830162290955099253/159273695028416000000000 <0`,
`A_2+eta0 D_2=-81906391888185735590779/45459247632456918400000000 <0`.

If eta<=eta0, the first pairing is at most its negative value at eta0 because D_1>0. If eta>=eta0, the second is at most its negative value at eta0 because D_2<0. These alternatives cover ALL real eta, including eta0. Both denominators are actual Hurwitz members, so their imaginary-axis squared moduli are positive; the corresponding real-part ratio is negative. No positive rescaling can change that sign. This proves the entire-line obstruction.

The proof does not assert that A, G, or any member of the line is a counterexample to the original box problem: a line of failed candidate numerators is weaker than failure of ALL unrestricted degree-seven numerators. The exact bounded simplex exchange on a finite frequency set did not return a strict negative coefficient certificate; the first unpaid question is to construct a common numerator OUTSIDE this line or a full actual strict-cone certificate for K.

## 4. Replay and boundary

- Frozen endpoints, twelve root brackets, reference Routh column, both line polynomials and exact two-atom values: `frontier-20261028-boundary-affine-obstruction-frozen-v1.json`, SHA256 `bca55dad8e27f93371bc163093d5d49404eb2bdfd538827b11d7c4076cc131b0`.
- Independently structured exact replay: `frontier-20261028-boundary-affine-independent-kernel-v1.py`, SHA `6b73f99210313d1395b38fb5f78dd92d745ff7af2dde17cb395a5bbf60b70749`; receipt `frontier-20261028-boundary-affine-independent-result-v1.json`, SHA `10608f88bd7d5a32d748f2e35f0403e93482f097c3a383149f756ab801447394`. It recomputes the four corners, twelve cubic sign changes, six global bands, reference Routh column, both pairing formulas, slopes and threshold values. Reversed bracket/slope and nonnegative-threshold mutations were rejected as `ROOT_BRACKET`, `SLOPE` and `THRESHOLD`.

Exact checks used integers/Fraction inside the owner's Eval kernel; the two implementations share the same owner and harness. Independent human/configured-family/formal verification and novelty clearance have not occurred. No original negative-box or universal-synthesis claim, external-model CLI, native scientific subprocess, Git, deletion or publication is made.

**END.**
