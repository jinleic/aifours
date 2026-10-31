# Actual robustly Hurwitz septic box: no common numerator from the denominator box, but an unrestricted one exists

Owner **InfoSPR7-2**, slot info-2. Native `/bin/date` observation immediately before this write: **Wed Oct 28 17:13:14 PDT 2026**.

**Result level: exact rational candidate with two separately implemented local verification routes; not yet peer/parent adopted, Lean/kernel verified or novelty cleared.** It falsifies the concrete premise that every robustly Hurwitz monic septic coefficient box admits a common SPR numerator that is itself a member of that box. It is **NOT** a counterexample to unrestricted SPR synthesis: an explicit unrestricted common numerator is also certified below.

## 1. Original target and the failed shortcut

The original question asks whether EVERY independent monic septic coefficient box whose members are all Hurwitz admits ONE unrestricted real polynomial of EXACT degree7 with strictly positive real ratio against every denominator at every finite real frequency, including zero; or whether there is an actual eligible counterexample.

The shortcut tested here is stronger: after normalizing the positive leading coefficient of a valid numerator to1, require all its other coefficients to lie in the SAME denominator box. This would imply a common numerator could always be chosen as an actual denominator (even allowing a positive scalar multiple). The result below disproves that shortcut for a genuine seven-positive-width, all-member-Hurwitz box while explicitly retaining a common numerator OUTSIDE the box. It does not answer the original all-box question.

No old held candidate/provenance claim is a premise. The initial floating-point search only discovered a lead; all final bounds below are exact rational arithmetic on the displayed data. The four-corner fixed-b reduction is independently proved below. Root-continuity and the standard Routh–Hurwitz criterion for ONE polynomial are named classical facts used only for stability, not a general Kharitonov theorem or an unverified corner-only stability claim.

## 2. Actual rational box and a common numerator

For `a(s)=s^7+sum_(j=0..6) a_j s^j`, let each `a_j` vary independently in the interval below. All endpoints are divided by1000.

| j | lower numerator | upper numerator |
|---:|---:|---:|
|0|4435|4586|
|1|10747|11496|
|2|23670|24364|
|3|40980|43182|
|4|10632|11217|
|5|13071|14315|
|6|1089|1147|

Every width is positive. Let K denote this entire closed coefficient box. Define the four actual coefficient corners K_{--},K_{-+},K_{+-},K_{++} by alternating lower/upper choices separately in the even and odd coefficients, beginning with the lower choice for each `-`. Concretely, in ascending `s^j` coefficients (with the monic coefficient appended), all shown integers are divided by1000:

- K_{--}: `(4435,10747,24364,43182,10632,13071,1147;1000)`.
- K_{-+}: `(4435,11496,24364,40980,10632,14315,1147;1000)`.
- K_{+-}: `(4586,10747,23670,43182,11217,13071,1089;1000)`.
- K_{++}: `(4586,11496,23670,40980,11217,14315,1089;1000)`.

The following unrestricted monic numerator has degree EXACTLY7 and is an actual common SPR numerator for the whole K:

`b_*(s)=s^7+(3413/100)s^6+(3851/100)s^5+(23757/100)s^4+(16691/100)s^3+(7183/100)s^2+(883/25)s+1/1000`.

Its constant term is below the lower endpoint for a_0, so b_* is not in K. Section5 gives a rigorous strict positive margin for ALL a∈K and ALL finite real frequencies. No reliance on a floating-point SDP optimum is made in that proof.

## 3. Exact proof that EVERY member of K is Hurwitz

Put `t=w^2` and write `a(iw)=E_a(t)+iw O_a(t)`. For t>=0 the actual even and odd evaluation ranges have extrema

`E_-(t)=(4435-24364t+10632t^2-1147t^3)/1000`,
`E_+(t)=(4586-23670t+11217t^2-1089t^3)/1000`,
`O_-(t)=(10747-43182t+13071t^2-1000t^3)/1000`,
`O_+(t)=(11496-40980t+14315t^2-1000t^3)/1000`.

For each of these FOUR cubics, the exact rational checker isolates three disjoint positive intervals on which its endpoint signs differ. A cubic has at most three roots counting multiplicity; therefore those are its three distinct positive roots, each simple, with no further roots. The paired root intervals are contained in the following six strictly ordered rational bands:

| corresponding roots of BOTH extrema | containing band |
|---|---|
| E first | `[99/500, 27/125]` |
| O first | `[27/100, 63/200]` |
| E second | `[2621/1000, 434/125]` |
| O second | `[139/40, 1057/200]` |
| E third | `[2799/500, 933/125]` |
| O third | `[1503/200, 5263/500]` |

The **actual dyadic root brackets and exact endpoint polynomial values** are in `frontier-20261028-hurwitz-certificate-v1.json`; the independent verifier re-evaluates every bracket from the above rational box. Outside the E bands, E_- and E_+ have the same nonzero sign; outside the O bands, O_- and O_+ have the same nonzero sign. The E and O bands are disjoint. Consequently, at every positive t at least one of the two actual value intervals excludes zero. At t=0 all a_0>0. Thus **no a∈K has an imaginary-axis root**.

The actual corner K_{--} has the exact Routh first column

`1, 1147/1000, 4360437/1147000, 8747523173/2180218500,`
`14388450063677/17495046346000, 132696847231194959/14388450063677000,`
`75727012355886964457/33174211807798739750, 887/200`.

Every displayed entry is strictly positive, so K_{--} is Hurwitz by the ordinary Routh–Hurwitz criterion. The box is convex and consists of monic fixed-degree polynomials. A straight coefficient segment from that stable actual corner to ANY actual member stays in K. By continuity of polynomial roots, the stable root count cannot change without an imaginary-axis crossing; none exists anywhere in K. Hence **every actual member of K is strictly Hurwitz**. No all-box stability inference from the four corner Routh signs alone is used.

## 4. Exact two-frequency obstruction to ANY monic numerator IN K

For any real degree-at-most7 numerator b write
`P_(a,b)(t)=Re[b(i sqrt(t)) a(-i sqrt(t))]`.
If b/a is strictly positive real at finite w, then P_(a,b)(w^2)>0 because a is Hurwitz. Consider the two ACTUAL corners K_{-+} and K_{+-}, the exact finite points t=4 and t=8, and the positive weights1 and10:

`W(b)=P_(K_{-+},b)(4)/5^7 + 10 P_(K_{+-},b)(8)/9^7`.

Let b_j denote the coefficient of s^j. Exact coefficient expansion gives

`373669453125000 * W(b)`
`= -1489012673 b_0 +177836497616 b_1 +82374800692 b_2`
`  -457220990464 b_3 -940849202768 b_4 -204116038144 b_5`
`  +8654196811072 b_6 +17080464152576 b_7`.

For b∈K, b_7=1 and each b_j has its stated interval. Maximizing this linear expression over the ENTIRE box means choosing the corresponding upper endpoint for a positive coefficient and lower endpoint for a negative coefficient. The exact maximum is **strictly negative**:

`max_(b∈K) W(b) = -356413503300067/373669453125000000 < 0`.

Were b∈K common SPR, BOTH summands of W would be strictly positive, since their denominators K_{-+},K_{+-} are actual Hurwitz box members and t=4,8 are finite nonnegative squared frequencies. This contradicts the exact bound. Therefore **no monic numerator in K** can be a common SPR numerator for K.

Positive rescaling of a numerator leaves all SPR signs unchanged. Thus this also rules out ANY positive scalar multiple of any actual member of K as a common numerator. It does **not** rule out a b outside K, and it does not claim unrestricted infeasibility. The two weighted pairings give a valid separating certificate only against the coefficient-constrained numerator set; their lower-coefficient combination is not zero and is NOT an unrestricted dual annihilator.

## 5. Exact whole-half-line positivity of the unrestricted numerator

For each corner a_i, set `P_i(t)=P_(a_i,b_*)(t)` and `x=t/(1+t)`. The exact checker constructs
`Q_i(x)=(1-x)^7 P_i(x/(1-x))`, `0<=x<=1`,
in degree7 Bernstein form. If `P_i(t)=sum_(k=0..7)c_k t^k`, the initial Bernstein coefficient at index k is exactly `c_k/binomial(7,k)`. Exact de Casteljau halving recursively restricts this polynomial to closed dyadic subintervals.

For the four corners the independent rational verifier produced respectively **7, 8, 9, 7** dyadic leaves, with EVERY Bernstein coefficient strictly positive. The leaf intervals, all exact coefficients, and their rational minima are persisted in `frontier-20261028-independent-bernstein-check-v1.json`. A Bernstein basis is nonnegative and sums to1, so this proves, for all four corners and all t>=0,

`P_i(t)/(1+t)^7 >= 1229013649779/3006477107200000 > 0`.

This is an exact rational lower bound, not a sampled-frequency inference. The initial and final compactified endpoints are included; the leading coefficient b_{*,7}=1 ensures the degree/infinity boundary.

For fixed t, the independent even/odd coefficient intervals make the value `a(i sqrt(t))` lie in the rectangle spanned by the four actual corner values. Every real linear pairing with the SAME b_* is therefore a convex combination of the four corner pairings. The same lower bound holds for EVERY a∈K. This is a value-rectangle argument at each frequency, not the false assertion that the full coefficient box is the convex hull of four points.

All coefficients a_j in this specific K are positive and
`S=1+sum_(j=0..6) upper_j =111307/1000`.
For every real w and j<=7, `|w|^j <= (1+w^2)^(7/2)`; hence `|a(iw)|^2/(1+w^2)^7 <= S^2`. Dividing the exact pairing lower bound by this denominator upper bound proves the explicit common literal SPR margin

`Re[b_*(iw)/a(iw)] >= 6145068248895/186239956180180926464 > 0`

for **EVERY actual a∈K and EVERY finite real w**. In particular zero and exact degree7 are paid. The number is a conservative certified lower bound, not an optimal synthesis margin.

## 6. Actual execution and verification boundary

The following local commands were exercised (using `-B`; no build/lint/test suite was run):

1. `frontier-20261028-box-search-v1.py --seed 91031 --trials 120 --seconds 50`: visited120 boxes; exact four-corner Routh checks passed120; no exact in-box separation was found. Positive finite-grid LP margins were NOT treated as global proofs.
2. `frontier-20261028-focused-search-v1.py --seed 106029 --trials 700 --seconds 55`: visited373 boxes, solved373 focused finite-grid LPs and found the exact in-box separation at trial372. The script uses numpy/scipy floating-point roots/LP only as a search device; none of its approximate solver output is the proof above.
3. `frontier-20261028-exact-box-check-v1.py` independently reconstructed the corners, rational Routh columns and two-frequency rational separation; it simplified the original discovered box to the displayed denominator1000 box and weights1,10. Its negative-weight and collapsed-width mutations were rejected for their intended validation reasons.
4. `frontier-20261028-hurwitz-certificate-v1.py` used exact rational cubic sign changes and exact Routh arithmetic to certify the WHOLE box via the disjoint-band/homotopy proof, without importing Kharitonov's theorem.
5. CLARABEL via `frontier-20261028-small-witness-v1.py` produced a numerical unrestricted lead. Its rationalization had zero positive roots in the four exact Sturm chains. **Independently**, `frontier-20261028-independent-bernstein-check-v1.py` imported neither the search nor Sturm checker, replayed the entire actual-box stability and weighted obstruction, and verified the displayed simpler rational b_* by exact Bernstein subdivision. It rejected zero numerator constant and negative atom-weight controls for the expected reasons.

This is two locally implemented positivity mechanisms (Sturm and Bernstein) and two local stability/obstruction checks by the SAME owner, not independent-human/configured-family or formal-kernel certification. The exact elementary verifier and all receipts are present for independent reconstruction; scientific novelty/priority has not been screened. The actual original universal question remains OPEN.

## 7. Reproducibility and pinned evidence

All paths are within the same new `robust-spr7/` exclusive root. Hashes observed at17:09:19–17:12:19 PDT:

| Evidence | SHA256 |
|---|---|
| `frontier-20261028-box-search-v1.py` | `bba0e98a51e308598159b65f4f160ce3fd93f7ba511d1ff476dba262e29a1d46` |
| `frontier-20261028-focused-search-v1.py` | `28719fe4677ad982eefe5febd5c5d7e67690b9837d3880a7ec0f8820743e87cb` |
| `frontier-20261028-focused-search-v1.json` | `591e87718a12b037adae7bc88c039a1a111b16d03f866e201bab46292787b99e` |
| `frontier-20261028-exact-box-check-v1.py` | `7d2d8c671d0bd7d3e213f98eb7d8b2ce0ad96350a874c744aefaf6904a01d6db` |
| `frontier-20261028-exact-box-check-v1.json` | `3db3d2cb1565e18b5b19678e3aeb68d4838142f1bf9762ffd977bed05a5b0306` |
| `frontier-20261028-hurwitz-certificate-v1.py` | `fd61172941a5539fbfb3715c6a8b2ea1a85095f0551f07ddacf960f18bf599cd` |
| `frontier-20261028-hurwitz-certificate-v1.json` | `eb06246afc46b913f1418269471f3182c1cdabd4d9119dace6005ff5ead24609` |
| `frontier-20261028-small-witness-v1.py` | `d98bdad727958f9453d29a7fdc85a9f2873add26462649f51b019847a412506d` |
| `frontier-20261028-small-witness-v1.json` | `94a8a02fe8d042afb041f494cd5bb9dcb965f3472e5aeb1afa4b619422734c15` |
| `frontier-20261028-independent-bernstein-check-v1.py` | `f160a56ea716cc8caa036ba9804e47bb478c06b6bb1ace495521a6b3505d063d` |
| `frontier-20261028-independent-bernstein-check-v1.json` | `a1082adb14075aeab9e87b95e8962fead56699bf0e892db9cf78d5b7d0c1773d` |

The numerical discovery used the existing local Python environment's numpy2.5.4/scipy1.18.1/cvxpy1.9.3 and CLARABEL. Independent rational verifiers use the Python standard library only and no search-code imports. All output files are new; no old/frozen result was edited or deleted. Historical quarantines and prior process findings are neither treated as accepted mathematical premises nor retroactively reclassified by the new owner direction.

**Remaining task:** continue at the original unrestricted actual-box shared-numerator/dual-sign interface. This concrete positive box rules out one tempting stronger construction but is not the desired unrestricted negative witness or an all-box existence proof.
