# Explicit full-dimensional independent septic boxes: one strict common-SPR numerator

**Disposition: scoped same-harness written support with independent exact all-frequency polynomial verification.** Native observation before composition: 2026-10-30T11:47:07-0700 PDT. f443 and fresh f451 each report **0 FATAL / 0 MAJOR / 0 MINOR** within their scopes. Stopped f444’s ENTIRE mathematical review episode and all consumers remain HELD/ZERO/NONINPUT; no fragment is salvaged. This is actual constructive synthesis for the stated seven-coefficient family, NOT every all-Hurwitz septic box.

## Actual independent box and fixed numerator

Use the SAME monic numerator

q(s)=s⁷+s⁶+9s⁵+(13/2)s⁴+23s³+11s²+15s+4.

Put F(t)=(1/2−t)(2−t)(4−t), G(t)=(1−t)(3−t)(5−t), so q(s)=F(−s²)+sG(−s²). Let gamma=65/481890304 and0<=epsilon<=epsilon*=65/18311831552=gamma/38. In a(s)=s⁷+sum_(j=0)^6 a_j s^j, EVERY coefficient is independently chosen from:

| Coefficient | Allowed interval |
|---|---|
| a0 | [3−epsilon,5+epsilon] |
| a1 | [1197/80−epsilon,15+epsilon] |
| a2 | [11−epsilon,11+epsilon] |
| a3 | [23−epsilon,467/20+epsilon] |
| a4 | [13/2−epsilon,13/2+epsilon] |
| a5 | [179/20−epsilon,9+epsilon] |
| a6 | [1−epsilon,1+epsilon] |

For every allowed epsilon, EVERY actual member is strictly Hurwitz, q is strictly Hurwitz, and for all t>=0,

F(t)E_a(t)+tG(t)O_a(t)>=(gamma−19epsilon)(1+t)⁶>=(65/963780608)(1+t)⁶>0,

where a(iomega)=E_a(omega²)+iomega O_a(omega²). Thus Re[q(iomega)/a(iomega)]>0 at every real frequency and the ratio tends to1 at infinity. The numerator is already strict; no weak-to-strict existence step remains for this class. For positiveepsilon all seven nonleading intervals have positive width. Every nonempty independent subbox inherits the result; no optimal enlargement radius is claimed.

## Complete all-member and all-frequency proof

At epsilon0, E_a=F+c, c∈[−1,1]. The actual independent odd envelopes are L=(19/20−t)(7/2−t)(9/2−t) and U=G, with U−L=3/80+(7/20)t+(1/20)t²>0. Every odd cubic has one simple root in each of[19/20,1],[3,7/2],[9/2,5]. Uniformeven signs andE_a(0)>=3 give strictalternating evenroots in(0,19/20),(1,3),(7/2,9/2). Named Hermite–Biehler supplies the Hurwitz orientation; fresh f451 also reconstructs it directly by the positive-residue partial-fraction representation for each general member, not a new selectedexample.

Three even-root neighborhoods, three opposite-sign odd bands, and their complement cover the entire t>=0axis. The respective uniform pairing lower bounds are3/4,43/128,7/32,89/400,39/320,77/16,65/4096. The sharper middle-odd-band factor product is<=861/320 while the even contribution is>=45/16. For t>=6, the exact tail bound P_a>=(25/5184)t⁷, combined with the compactfrequency margin, gives P_a>=gamma(1+t)⁶.

Coordinatewiseprojection of any enlarged member onto thecore gives abs(delta a_j)<=epsilon withoutcouplingcoefficients. Its parity errors obey abs(deltaE)<=epsilon(1+t)³ and abs(deltaO)<=epsilon(1+t)²; abs(F)<=4(1+t)³, abs(G)<=15(1+t)³ then give the EXACT19epsilon loss above. Along the monic coefficientsegment from a stablecore member to the enlarged member, positivepairing excludes EVERY imaginary-axiszero, including0. Boundedcoefficients/fixeddegree boundallroots; continuity prevents a half-plane crossing or escape throughinfinity. This is the all-member stability argument; cornerRouth checks alone would notprove it.

## Actual ray consumers, no orientation omitted

The fixed roots(1/2,2,4) are strictly interior relative to EACHenlargedbox’s OWN actualoddendpointbands, not merely the oldcore markers. At aroot ofF, positivePforces the alternatingGsigns for EVERYoddcomponent; strictendpointenvelope ordering supplies the required root slots.

For any nonzero finite positive combination ofactual atoms with allfour signedoddmoment coordinates R1,R3,R5,R7<=0,

sum_i w_i t_i G(t_i) O_i=15R1+23R3+9R5+R7<=0.

Consequently sum_i w_i F(t_i)E_i>=sum_i w_i P_i>0. Fresh f451 explicitly checks every R4 omitted-moment choice, BOTH R5orientations, zero-odd singletons, same-frequency opposite-odd cancellation andt0. Actualparityindependence makes the pointwiseminimizingeven envelope valid at eachnode; it need notbe onefixedpolynomial acrossnodes. The rawcoefficientvector(4,15,11,23,13/2,9,1,1) isstrictlypositive, so noall-eight-strictnegativeaggregate exists FOR THESE BOXES.

## Actual verification and remaining target

[Author](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f434-spr7-actual-box-interior-common-test-or-strict-obstruction/review-v1.md) · [Uniform/core written review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f443-spr-explicit-independent-box-uniform-pairing-proof-review/review-v1.md) · [Fresh enlargement/consumer review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f451-spr-enlargement-all-ray-fresh-written-replacement/review-v1.md) · [Independent finite report](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f445-spr-full-dimensional-box-independent-exact-finite-check/review-v1.md) · [Exact verifier](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f445-spr-full-dimensional-box-independent-exact-finite-check/independent-actual-septic-box-sturm-routh-v1.py) · [Parent execution](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f445-spr-full-dimensional-box-independent-exact-finite-check/parent-independent-finite-run-v1-receipt.json). Parent displayed all844logicalauthorlines,629f443/539f451reviewlines and813finite-report/source lines, reconstructedintervals, allclosedfrequencyregions, exactmargin, coefficientprojection, no-crossinghomotopy andcompleteactualconsumer, andcheckedfrozenpins. The authoroptionalcode wasread aspartofitscompletebody but NOT run or suppliedto theindependentverifier.

Separatelyauthored stdlibFraction checker parent-ran ONCE, exit0: actual128independent enlarged corners,4actualeven/oddenvelopes,128cornerRouth checks,68EXACTSturm positivity certificates overcompleteintervals/halfaxes includingweightedmargin, and9intended-invariantmutations. It independentlyreconstructs thephysicalrealconjugateproduct directlyfroms-coefficients. Negativecontrols includeatan­gentialpositive-axiszero, wrongconjugation andwrongstabilityorientation. Exactepsilon andweightedmargin match the theorem. Childexecution was NOTRUN. The all-boxconsumer/homotopy remainswrittenproof, not aninferencefromcornerchecks alone.

The universal synthesisproblem forarbitraryall-Hurwitzindependentsepticboxes remainsopen here; no boxoutside thisregion is claimed reducibletoit, andnoeligibleboxwith anall-eight-strictnegative obstruction is supplied. Source-wide correspondence, novelty/priority, human/independent-family andformal/kernel acceptance remainunpaid. Historicalheldepisodes andeveryconsumer remainNONINPUT.
