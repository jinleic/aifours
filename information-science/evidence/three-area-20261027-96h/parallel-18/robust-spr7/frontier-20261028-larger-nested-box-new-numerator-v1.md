# A larger nested septic box and an open family: a third common numerator succeeds where two fail

Owner **InfoSPR7-2**, slot info-2. Actual preceding `/bin/date`: **Wed Oct 28 18:46:24 PDT 2026**. **WRITTEN-checked-in-kernel candidate with a separately structured exact same-harness replay; not parent-reviewed or formally verified.** This is a constructive original-box result, not a negative box or a proof for every septic box.

## 1. A larger actual box, strict numerator, and its endpoint neighborhood

Let `K_H` be the monic septic independent box `a(s)=s^7+sum_(j=0..6)a_j s^j` with endpoints:

| j | lower | upper |
|---:|---:|---:|
|0|177249/40000|183591/40000|
|1|429131/40000|460589/40000|
|2|473053/20000|487627/20000|
|3|818499/20000|864741/20000|
|4|84939/8000|89853/8000|
|5|130399/10000|143461/10000|
|6|2207/2000|453/400|

Let

`b_H(s)=s^7+(2028281/100)s^6+(1971569/100)s^5+(6620777/50)s^4`
`             +(4490113/50)s^3+(160147/4)s^2+(949689/50)s+3/10`.

For EVERY closed monic independent box K' whose fourteen endpoints are within `rho=1/100000000` of those of K_H:

1. Every K' width is positive and every member is strictly Hurwitz.
2. The SAME exact-degree-seven b_H is a common SPR numerator for all K' members and all finite real w, with the explicit literal ratio bound

   `Re[b_H(iw)/a'(iw)] >= 47884938654688953125/4068914417784016897605632 >0`.

3. Both previously pinned numerators `b_old` and `b_new` of `frontier-20261028-anisotropic-new-numerator-open-family-v1.md`, SHA256 `25db31d50117b74462a3fc25f22d46f48d2e44e79d28455c0b875eef93063d2f`, fail on K': the corresponding actual `(E_+,O_+)` corner has strictly negative pairing against BOTH at `t=w^2=7/25`.

The earlier 101/100-wide, s^6-half-width base box from that source is exactly contained in K_H; the independent replay checked all fourteen endpoint inclusions. Thus b_H also works for every denominator in that earlier base box. K_H is genuinely larger in the other six widths (21/20 versus 101/100); it is not a second unrelated finite-frequency sample. The open endpoint neighborhood here is new and is not asserted to contain every endpoint perturbation of the earlier box.

## 2. Exact all-member stability of K_H

For the actual endpoint even and odd cubics E_-,E_+,O_-,O_+ defined by the original alternating coefficient choices, the frozen certificate contains three disjoint rational sign-change brackets per cubic. The merged bands are strictly ordered:

| band | exact enclosing interval |
|---|---|
| E1 | `[213191589/1073741824, 5789292083/26843545600]` |
| O1 | `[7236846593/26843545600, 2117183011/6710886400]` |
| E2 | `[70604801551/26843545600, 46012809853/13421772800]` |
| O2 | `[92592846141/26843545600, 144881718683/26843545600]` |
| E3 | `[30861454973/5368709120, 1968244273/268435456]` |
| O3 | `[197918584993/26843545600, 71009652837/6710886400]` |

Each cubic has positive constant, nonzero negative leading coefficient and three distinct positive sign changes, hence exactly three simple positive roots and no others. Outside the three E bands both E extrema have the same nonzero sign; outside the O bands the O extrema do. The bands are mutually disjoint, so the actual E/O value rectangle cannot contain zero at any t>0. The entire K_H has positive a_0 at t=0. Hence no actual member has an imaginary-axis root.

An independent rational Gaussian-determinant implementation finds all 28 leading Hurwitz determinants for the four actual parity corners positive; independently, the saved `(E_-,O_-)` reference Routh first column is strictly positive. Convex monic coefficient homotopy from that reference to any actual member, combined with the no-imaginary-axis result, gives **all-member** Hurwitz stability. The 28 corner checks are not used alone as an unproved full-box stability inference.

## 3. Exact whole-frequency witness and two exact failures

For each actual parity corner, the exact raw pairing polynomial is in the frozen JSON. The search and replay agree on these polynomials by independent `E_a E_b+t O_a O_b` and signed monomial expansions. At `x=t/(1+t)`, the degree-seven Bernstein proof partitions `[0,1]` into `6,11,11,7` leaves for the four corners. Every recorded coefficient is positive; an independently structured replay converts the full power polynomial directly to the Bernstein basis of each reported interval and checks exact equality, positivity and interval-cover endpoints. The least exact coefficient is

`d=1131593723113/6710886400000 >0`.

It follows that `P_(a,b_H)(t)/(1+t)^7>=d` at every corner and hence for EVERY a in K_H by the actual fixed-t even/odd rectangle argument. The upper coefficient L1 sum is `S=178293/1600`, so the base-box literal SPR ratio is at least

`d/S^2 = 1131593723113/83331367171522560 >0`.

At the actual `(E_+,O_+)` corner and squared frequency 7/25, the two previous numerators fail exactly:

`P_(a,b_old)(7/25) = -19650719733069/195312500000000 <0`,
`P_(a,b_new)(7/25) = -157843475513483/195312500000000 <0`.

The corner is Hurwitz, so both associated real-part ratios are negative. These are exact pairings at the finite frequency `sqrt(7)/5`, not floating estimates. They prove the TWO specified polynomials fail; they do not exclude other unrestricted numerators, as b_H itself demonstrates.

## 4. All perturbed boxes and both failure margins

Map any a' in K' to a in K_H by using the same coefficientwise interval-interpolation parameters; then each of the seven lower coefficients changes by at most rho and the leading monic coefficient stays1. Put

`B_H=sum |b_H,j|=32124813/100`, `B_new=963073/100`, `B_old=585271/1000`.

The inequality `|w|^j <= (1+w^2)^(7/2)` gives the normalized polynomial bounds

`|a'(iw)-a(iw)|/(1+w^2)^(7/2)<=7rho`,
`|b_H(iw)|/(1+w^2)^(7/2)<=B_H`.

The base pairing lower bound d gives `|a(iw)|/(1+w^2)^(7/2)>=d/B_H`. Therefore every point of the straight segment from a to a' avoids the imaginary axis whenever `d-7rho B_H>0`. The exact value is

`d-7rho B_H = 3064636073900093/20971520000000000 >0`.

Monic root-count continuity carries the Hurwitz property to every a' in every K'. The same bound gives a strictly positive new pairing, and `|a'(iw)|/(1+w^2)^(7/2)<=S+7rho` gives the ratio claimed in §1. The width margin is `29/1000-2rho=1449999/50000000>0`.

For the two earlier numerators at t=7/25, the old pairing can change by at most `7rho B_old (32/25)^7` and `7rho B_new (32/25)^7`, respectively. Their remaining exact negative absolute margins are

`7658466357099997613/76293945312500000000 >0` for b_old,
`12273612385949610863/15258789062500000000 >0` for b_new.

Therefore BOTH fail on the corresponding actual corner of every K' in the stated neighborhood, while b_H succeeds on all members.

## 5. Evidence and limits

- Complete frozen actual box, b_H, all pairing polynomials, 35 Bernstein leaves, 12 root brackets and two old-pairing failures: `frontier-20261028-harder-box-common-numerator-frozen-v1.json`, SHA256 `74c3ccc312cb0e7b86b8c76f2e89ab2043d36288454720c583ca2bf8a5027eec`.
- Exact independent-method base replay `frontier-20261028-harder-box-independent-replay-kernel-v1.py`, SHA `baed94f127a001d4cc7db998fdd0a9155a3934f92a31cb7eaa09f717e3269ce7`; receipt `frontier-20261028-harder-box-independent-replay-result-v1.json`, SHA `9c34ed0ad1e57a4b8187d6394ae0f92bc74bc8b6c260f24b7fc25e24355c41fa`. It reconstructs corners, 12 cubic root signs, six disjoint bands, 28 determinants, reference Routh column, every leaf by the independent power-basis conversion and the previous numerator's exact failure. Corrupted leaf/reversed root-bracket controls rejected as `LEAF_MISMATCH`/`ROOT_BRACKET`.
- Exact nesting and neighborhood arithmetic `frontier-20261028-harder-open-family-replay-kernel-v1.py`, SHA `8d034b268f6ac507acf34e96b51ea5f258c7b51cf506311f00663bf1c35dd728`; receipt `frontier-20261028-harder-open-family-replay-result-v1.json`, SHA `14d0517f954e8121b29dfa358e24ce0c7c2014d26df49d3ec0300ca1f04bbf2b`. Oversized radius1 and radius1/1000 rejected for `WIDTH` and `NEW_MARGIN` respectively.
- The bounded exact rational-simplex exchange record for K_H is `frontier-20261028-harder-box-exchange-result-v1.json`, SHA `91bfba41b1f679402673ec28f70658c7fad1e11756b3be7d503db6447af6d0d2`. Its sampled-grid or optimizer status is NOT used as proof of all-frequency positivity; the exact frozen/replayed leaves above are the proof.

All computations were exact integers/Fraction inside the owner's Eval kernel; algorithms are separately structured but share owner, harness and sources. No native scientific subprocess, external-model CLI, nested agent, Git or publication was used in these checks. The result needs full independent source/whole-proof review; no formal/kernel, human, configured-family or novelty acceptance is claimed. The original universal septic synthesis or obstruction question remains OPEN.

**END.**
