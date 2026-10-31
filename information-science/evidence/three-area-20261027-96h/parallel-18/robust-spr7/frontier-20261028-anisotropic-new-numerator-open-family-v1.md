# An explicit open family of Hurwitz septic boxes needs a different common numerator

Owner **InfoSPR7-2**, slot info-2. Actual preceding `/bin/date`: **Wed Oct 28 18:40:56 PDT 2026**. **WRITTEN-checked-in-kernel candidate with an independently structured exact in-kernel replay; same author/harness, not parent-reviewed or formally verified.** This produces a genuine open family of actual boxes and a new explicit common numerator. It is NOT an unrestricted SPR7 counterexample or a universal synthesis theorem.

## 1. Exact assertion and base box

Let K be the monic degree-seven box `a(s)=s^7+sum_(j=0..6)a_j s^j` with independent closed intervals:

| j | lower | upper |
|---:|---:|---:|
|0|886849/200000|917351/200000|
|1|2148651/200000|2299949/200000|
|2|2366653/100000|2436747/100000|
|3|4096899/100000|4319301/100000|
|4|425163/40000|448797/40000|
|5|653239/50000|716061/50000|
|6|2207/2000|453/400|

All seven widths are strictly positive; the least is `29/1000`. Define

`b_new(s)=s^7+(58911/100)s^6+(17402/25)s^5+(92178/25)s^4`
`             +(291423/100)s^3+(112341/100)s^2+(30987/50)s+1/25`.

Let `b_old` be the earlier pinned base-box numerator

`b_old(s)=s^7+(3413/100)s^6+(3851/100)s^5+(23757/100)s^4`
`             +(16691/100)s^3+(7183/100)s^2+(883/25)s+1/1000`.

Put `rho=1/100000000`. For EVERY closed monic independent coefficient box K' whose fourteen endpoints differ from K's corresponding endpoints by at most rho:

1. All seven widths of K' are positive, and EVERY member is strictly Hurwitz.
2. The SAME b_new is an exact-degree-seven common SPR numerator for EVERY member of K' at EVERY finite real frequency, with the explicit uniform ratio bound

   `Re[b_new(iw)/a'(iw)] >= 48125357341543196609375/58214235678253038721514340352 >0`.

3. The old b_old is NOT a common numerator for K': the corresponding actual `(E_+,O_+)` corner has negative pairing at the exact squared frequency `t=7/25`.

Thus this is a fourteen-endpoint open neighborhood of actual original boxes on which a previously successful fixed numerator fails, yet an independently certified DIFFERENT unrestricted numerator succeeds. The fact that K itself is not a symmetric enlargement of the earlier box matters: its six other widths are 101/100 of the old widths while the s^6 width is halved. No conclusion follows for every original box, nor does failure of b_old imply failure of any other numerator.

## 2. Independent exact base stability

Write `a(i sqrt(t))=E_a(t)+i sqrt(t) O_a(t)`. The exact extrema of each parity interval are

`E_-=l_0-u_2 t+l_4 t^2-u_6 t^3`, `E_+=u_0-l_2 t+u_4 t^2-l_6 t^3`,
`O_-=l_1-u_3 t+l_5 t^2-t^3`, `O_+=u_1-l_3 t+u_5 t^2-t^3`.

The frozen certificate supplies three disjoint rational sign-change brackets for EACH of these four cubics. Their corresponding roots lie in these six strictly ordered common bands:

| root bands of both extrema | exact enclosing interval |
|---|---|
| E1 | `[2669023231/13421772800, 1156003953/5368709120]` |
| O1 | `[362900403/1342177280, 4221316401/13421772800]` |
| E2 | `[70863980953/26843545600, 45719303009/13421772800]` |
| O2 | `[46576076907/13421772800, 142434266679/26843545600]` |
| E3 | `[155163355863/26843545600, 196289908087/26843545600]` |
| O3 | `[40202548589/5368709120, 141418767751/13421772800]` |

Each cubic has degree three, positive constant and negative leading coefficient. Three disjoint sign changes prove three distinct positive simple roots and no other roots. Outside its three bands, the lower and upper E extrema have the same nonzero sign; likewise for O. Because the E and O bands are mutually disjoint, at any positive t at least one entire actual value interval excludes zero. At t=0 every a_0>0. Thus NO member of K has an imaginary-axis root.

The `(E_-,O_-)` actual corner has an exact strictly positive Routh first column; all eight rational entries are saved in the frozen certificate. A separate rational Gaussian-determinant implementation found all 28 leading Hurwitz determinants of the four corners strictly positive as an additional check. Starting from the reference corner, every straight coefficient segment to a member stays in K and monic. Root continuity and the absence of imaginary-axis roots keep the Hurwitz root count fixed, so EVERY K member is strictly Hurwitz. This proof uses the actual root bands and one reference Routh check; it does not rely only on checking vertices or import an unproved Kharitonov theorem.

## 3. Exact base numerator and explicit old failure

For each of the four actual parity corners a_i, define `P_i(t)=Re[b_new(i sqrt(t)) a_i(-i sqrt(t))]`. The source search constructed the coefficient polynomials by signed monomial expansion and independently compared `E_a E_b+t O_a O_b`. It then checked strict positivity of `Q_i(x)=(1-x)^7 P_i(x/(1-x))` on `[0,1]` by exact degree-seven Bernstein subdivision. The four subdivisions have `6,6,7,9` leaves.

The independent replay did NOT reuse the subdivision algorithm. For each reported dyadic interval it recomputed the power polynomial Q, substituted `x=left+(right-left)u`, converted those power coefficients directly to degree-seven Bernstein coefficients, compared EVERY recorded leaf coefficient, checked all coefficients positive, and checked the intervals partition `[0,1]`. The smallest coefficient is exactly

`d=1050465553521003/96207267430400000 >0`.

Hence for every corner and t>=0, `P_i(t)/(1+t)^7 >= d`. For fixed t, the independent even/odd coefficient intervals fill the rectangle spanned by the four actual corners. The SAME b_new pairing is affine on this rectangle, so the same inequality holds for EVERY a in K. The upper coefficient L1 sum is `S=178113/1600`, implying the base-box ratio is at least

`d/S^2 = 116718394835667/132469727243471421440 >0`.

For b_old, the independently reconstructed actual `(E_+,O_+)` corner a_++ gives

`Re[b_old(i sqrt(7/25)) a_++(-i sqrt(7/25))]`
`= -553009337053/39062500000000 <0`.

Since that corner is Hurwitz, its denominator squared modulus is positive, so b_old fails strict SPR for the BASE box. This is an exact rational pairing at the finite real frequency `sqrt(7)/5`, not a rounded numerical comparison.

## 4. The entire endpoint neighborhood

For any actual a' in K', choose the same interval-interpolation parameter in the corresponding K interval for each coefficient. This gives a in K with `|a'_j-a_j|<=rho` for j<=6 and identical leading coefficient. The same holds for each corresponding parity corner. Set

`B_new=sum_j |b_new,j|=963073/100`,
`B_old=sum_j |b_old,j|=585271/1000`.

For j<=7, `|w|^j <= (1+w^2)^(7/2)`. Consequently, uniformly in all real w and all mapped members,

`|(a'-a)(iw)|/(1+w^2)^(7/2) <= 7rho`,
`|b_new(iw)|/(1+w^2)^(7/2) <= B_new`.

The base pairing bound implies `|a(iw)|/(1+w^2)^(7/2)>=d/B_new`. On every straight segment from a to a', the triangle inequality gives a positive lower bound `d/B_new-7rho`, since

`d-7rho B_new = 3080022869858764583/300647710720000000000 >0`.

Each segment stays monic and has NO imaginary-axis zero; its starting a is Hurwitz, so root continuity proves a' Hurwitz. Separately, the same difference estimate yields `P_(a',b_new)/(1+t)^7 >= d-7rho B_new`. Since `|a'(iw)|/(1+t)^(7/2)<=S+7rho`, division gives exactly the uniform positive ratio in §1. The width lower bound is

`29/1000-2rho = 1449999/50000000 >0`.

For the corresponding actual perturbed `(E_+,O_+)` corner, the coefficient perturbation estimate at `t=7/25` bounds the old pairing change by `7rho B_old (32/25)^7`. Its remaining strict negative absolute margin is

`553009337053/39062500000000 - 7rho B_old (32/25)^7`
`= 1062500322801560113/76293945312500000000 >0`.

Thus b_old fails throughout the WHOLE stated neighborhood while b_new works for all members of every box there.

## 5. Evidence, controls and remaining gap

- Immutable complete rational box, numerator, four pairing polynomials, 28 Bernstein leaves and 12 root brackets: `frontier-20261028-anisotropic-common-numerator-frozen-v1.json`, SHA256 `41411d5d0f25108a14e1dad8f8ac770ee580867d573206ce4ea22b6cf71005a4`.
- Independently structured exact base replay: `frontier-20261028-anisotropic-independent-replay-kernel-v1.py`, SHA `41872fc88f47cd3110c48c9221cc5f2f03e7cf86aa81439d0790436fc6060af1`; result `frontier-20261028-anisotropic-independent-replay-result-v1.json`, SHA `aa6ec5a8487861998a8acfc6bbea2ff4ff66c9bc1160da9b2a96774320ff6311`. It rederived the actual corners, 12 root signs/six disjoint bands, reference Routh column, 28 rational determinants, all recorded leaf coefficients by the different power-basis method, the complete interval cover and b_old failure. Corrupting one leaf yielded `LEAF_MISMATCH`; reversing a root bracket yielded `ROOT_BRACKET`.
- Independent exact neighborhood arithmetic source `frontier-20261028-anisotropic-open-family-replay-kernel-v1.py`, SHA `0fbc352741274e836477feec20196b8bd41b0ec9958bbbc0886f41f28434fa9d`; result `frontier-20261028-anisotropic-open-family-replay-result-v1.json`, SHA `48c053fdc6151e6bc8314e347f23a3229474328f367dc38d6db575c8fce95242`. Oversized radius1 and radius1/1000 were rejected for intended `WIDTH` and `NEW_MARGIN` reasons.
- The search's anisotropic candidate receipt is `frontier-20261028-anisotropic-exact-search-result-v1.json`, SHA `af830d936a56ca8b446d09b4082ff2bcfa0b4c036e969c0cb98dfc5a9fa60d66`. Floating-point data were not used; rational simplex and finite-grid leads were NOT treated as whole-frequency proof.

The replay source uses the top-level loop variable `os`, which temporarily shadows Eval's prelude `os` module after the successful mathematical run. The subsequent receipt-write bridge failed for that reason; `import os` restored the host helper and the receipt write was retried successfully. The scientific replay was NOT rerun or retroactively changed; this tooling detail should be corrected if the source is reused.

All exact checks ran in the owner's Python Eval kernel using integers and `fractions.Fraction`; the two independent mathematical implementations share the same harness, source bytes and owner. No native scientific subprocess, external model CLI, nested agent, Git or publication was used in these checks. Independent human/configured-family/formal verification and novelty screening remain unperformed. The original full septic-box synthesis/obstruction question remains OPEN.

**END.**
