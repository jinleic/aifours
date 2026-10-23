# DELTA2 baseline audit v1 - current numerical union and complete retained word conditions

Written by hand after `/bin/date`2026-10-21T19:31:01-0700; after the published exposure acknowledgement,
before any new delta2 proof attempt. This is Step0, not a new exclusion theorem or an existence claim.
All interval statements below are integer intervals, empty if lower>upper. p>=7 is prime throughout.

## 1. Literal accepted providers at R=p+2

Universe: 2<=kappa<=p-1. The target has F=3p-4, H=p-1-kappa and k=p-2+2kappa.
RP-2NE gives L2=[3,(p-5)/2], nonempty at p>=11. It does NOT supply kappa2.
I.14/E1 supplies
 A2=[ceil((p+8)/4),(p-7)/2] union[(p+3)/2,p-5].
The lower part is inside L2 whenever nonempty. E1's extra even-delta endpoint is
 E2={(p+7)/4} only when p=1 mod4 and p>=21; otherwise E2 is empty.
When present E2 is also inside L2: (p+7)/4<=(p-5)/2 since p>=21>=17, and its lower endpoint is>=3.
Thus the SEG-k endpoint contributes NO additional delta2 parameter beyond accepted RP-2NE.

Bprime at delta2 requires both defining bounds at least2. For eps0 this means p>=18 and p>=19;
for eps1 it means p>=14 and p>=18. Since p is prime, BOTH eps0 and eps1 are covered exactly when p>=19.
Their kappa values are (p-1)/2 and (p-3)/2. Theorem B adds nothing beyond Bprime.
Consequently the CURRENT uniform numerical provider union is EXACTLY
 U2(p)=[3,(p-5)/2] union[(p+3)/2,p-5]
       union({(p-3)/2,(p-1)/2} if p>=19, otherwise empty).
This is the union of these stated universal providers, not every word-specific structural certificate.
DELTA1, D1-END and RP-LIFT do NOT give an additional R=p+2 theorem by analogy.

The complementary parameter set V2=[2,p-1] minus U2 is:
* p>=19: {2,(p+1)/2,p-4,p-3,p-2,p-1}.
* p in{7,11,13,17}: {2,(p-3)/2,(p-1)/2,(p+1)/2,p-4,p-3,p-2,p-1}, merging repeats.
At p7 these repeats give ALL of {2,3,4,5,6}; U2 is empty. At p11 U2={3}; at p13 U2={3,4,8};
at p17 U2=[3,6] union[10,12]. These are HAND substitutions to handle exceptions, not code enumeration.

## 2. Exact mandatory diagnostics relative to that baseline

D2-LOW kappa2: not uniformly covered at ANY p>=7.
D2-MIDDLES: kappa=(p-1)/2 is ALREADY Bprime-covered for every p>=19; it remains in V2 for
p in{7,11,13,17}. Kappa=(p+1)/2 remains in V2 for EVERY p>=7.
D2-UPPER {p-3,p-2,p-1}: remains in V2 for EVERY p>=7, with repeats counted once.
The WHOLE target ALSO retains kappa=p-4 for every p, and kappa=(p-3)/2 at the four small primes.
The diagnostics do not replace these additional obligations. The target is NOT already covered.

## 3. Word-specific accepted conditions - retained, not converted to universal bands

Normalise the nonzero rotation pair and A>=B by the accepted order-preserving automorphisms.
K0star-r2 Z0/P0 give necessary avoidance constraints B<=kappa and e_R<=2kappa, with empty runs counted as
even. TheoremP's own accepted statement gives sum floor(r_i/2)<=2, since F=3p-4. These are necessary
conditions, not new assumptions on the original target. No purity or B<kappa hypothesis is imposed.

RAW SEG: let N_1,...,N_q be the nonempty rotation runs, M_i the reflection run between consecutive N_i,
b_i=number of constant blocks of M_i, g_E=k-q, d=max|a(N_i)-b(N_i)|,
 n_CA=#{i:b_i<=2}, m_lo=max(1,kappa+1-ceil((p+2-d)/4)), m_hi=p-floor((p+2+d)/4).
Here Pi_need=p-ceil((p+2)/2)=(p-3)/2>=2. Under its literal all-odd setting, accepted Theorem SEG kills a word
if ALL three hold:
 m_hi-m_lo>=(p-1)/2, n_CA>=2m_lo+2, g_E>=(p-1)/2.
Thus every remaining avoider must fail at least one of THESE ACTUAL word-dependent tests. This is not the
stronger sufficient width H-floor(d/2), not an equivalence with one numerical band, and not a no-go theorem.
Erratum4's old narrowing is superseded by the own v5 verdict; PartII is accepted but irrelevant to this R.

B.4: at delta2 its literal domain requires p>=19, eps in{0,1}. Both corresponding kappa values are ALREADY
uniformly excluded by Bprime there. It adds no condition to V2 at p7/11/13/17; it never applies to arbitrary
other kappa. Its generic |AB|<=N_O / strict x inequality remains at its own scope, not a universal band.

B=0 CJ: the own accepted equal-rotation theorem applies to this all-odd genuine-gap setting, without a
nonempty-gap or purity addition. Its original sufficient condition is R>=4kappa+1 with Delta<=0 or two
disjoint heavy admissible intervals; its corrected strengthened condition is R>=4kappa-4 AND 2kappa<=p-1,
with the same alternatives and corrected Corollary2 (Delta<=1 OR p>=kappa+5Delta-5).
Here Delta=p+kappa-1-R=kappa-3. Hence it already excludes B=0 at kappa2 for EVERY p>=7
(original R>=9 and Delta=-1), and additionally (p,kappa)=(7,3),(11,4) in V2 by the strengthened condition,
Delta0 or1. These are WORD-subclass exclusions, not AnyB parameter closures. All other V2 values fail even
the strengthened R>=4kappa-4 prerequisite, so its heavy-interval alternative yields no additional V2 word
certificate. EDGE's two exceptional R=2p-2/2p-1 values cannot equal p+2 for p>=7; no extra delta2 band.

TRANSFER/initial-word conditions remain CONDITIONAL at the own RPdelta/RED import trust boundary, not
silently upgraded or inverted. For completeness retain their actual certificate as a word filter: if the word
has a genuine empty rotation gap (hence a nonconstant maximal reflection run), put D=A-B, g0=kappa-B.
Every actual avoider must FAIL the own TRANSFER sufficient test that EACH integer box cell
 1<=g<=g0, 0<=b<=B, g+b>=2
satisfies one of the six literal clauses at kappa'=g+b,R'=D+2b,k'=2p-D+2g,Delta'=p+kappa'-1-R':
 (a) k'<=p; (b) k'>=2p+1 and k'>=3kappa'+3;
 (c) k'>=4kappa'+5 and k'>=p+floor(R'/2)+1;
 (d) p>=11,R'=p,kappa'>=(p+1)/4; (e) R'<p;
 (f) b=0,R'>=4kappa'-4 and(Delta'<=1 OR p>=kappa'+5Delta'-5), with its actual CJ/EDGE setting.
An empty box gives the reflection-run conclusion by contradiction, not a feasibility assertion. In particular
B=kappa with a genuine empty gap is already excluded at this accepted conditional boundary. T1/T2/T3 are
not independent universal delta2 solvability bands; their conclusions concern reflection-run constancy.
No new proof below may use this filter unless its entire own trust/scope/overlays are supplied explicitly.

This gives the ENTIRE-target NECESSARY residual: C2(p,kappa) with kappa in V2, retaining every target word
variable; the necessary Z0/P0/P conditions, failed raw-SEG conjunction, the B=0 exclusions just listed, and
the literal conditional TRANSFER failure wherever its own setting is invoked. No residual word, data tuple
or feasibility is asserted. It is not an inverse characterization of avoidance. In particular kappa2 still
requires mixed-rotation cases; it is not silently narrowed to pure rotations or one NF representative.

## 4. Sources used at their OWN scopes

Every entry means absolute path + WHOLE-file SHA256 + inclusive original LF range. All mandatory overlays
are read and remain governing; source-package coverage will distinguish statement-level imports from proof replay.

| Input | Path | SHA256 | LF / use |
|---|---|---|---|
| RP2NE | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-RP2NE-parent-verdict-v1.md | 320d817a4b24d2c39f04806ce84ab1977fd68f5869b8c7be0da5184d166d2eab | 1-33; exact delta2 lower band and all bindings |
| I14/FND | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-REFLHI-v5-parent-verdict-v1.md | 13ee1ba86245fc549bd79c130a9fe15248ecc3fe9fc8428e875ca939c940a547 | 1-61; current own coverage/setting/all bindings |
| RPdelta | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-RPdelta-parent-verdict-v1.md | 2ed0e96c4ceb01caec54bc3b672e17e2473df1ead24535301325777c9802d1f8 | 1-50; E1/Bprime/B4, conditional TRANSFER at its literal boundary |
| E1-E5 | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/erratum-1-RPdelta-consolidated-v1.md | 2450446d526305e561ee2c8c05b1946dd704363f31d95eef58df5797d73a2136 | 1-96; governing numerical complements and non-necessity repairs |
| parent overlay | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-RPdelta-parent-erratum-v1.md | 110338d856445866c91c42208bd900987f9761110ef47ef540104f91d70b65b4 | 1-29; governing endpoint/width/zero-gain scope |
| raw SEG | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-arcs-v5.md | 4e46374677e30bd7b306c6fcca9845a09b15daf93fa42a9f908d0beb8c8cff1c | 134-145; own raw word hypotheses, through all five errata |
| PartI | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-arcs-v5-erratum-5.md | 40832206bf581a685266c4f885ecf2d3008e6e362b6a791acc11fa2527d325f4 | 30-164; I6/I7/I12/I13/I14, read through own verdict |
| K0 facts | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/proof-K0star-r2.md | 6681676e4f80018e792c7117ce9fc524a31aeb397c35880f57468ada9c0396e1 | 66-75; Z0/P0, own authority carried into FND |
| P own | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-TheoremP-import-closure-parent-verdict-v1.md | c25230adf6356d90f0b79462aaab4dcc88bc193f0a09a8e41bb3fb70bb17dbf5 | 1-15; exact theorem through both own errata |
| CJ own | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-cj-cjx-parent-verdict-v1.md | 5cfd6a4fe15cab133e210cd6f6966e34fa633d1a8c432b79eb537c0016145f6d | 1-41; actual B0 setting, both R prerequisites, corrected corollaries |
| EDGE own | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-edge-parent-verdict-v1.md | d2b67d96ee697da6536c443354a2ea9f6a7bb32851ecd07fff9050c2fd40b58b | 1-61; scope audit only, no extra R=p+2 cell |

Original RPdelta overlays K-e/B-e1/B-e2/BP-e and original FND errata1-4 were also read in full at their
physical LF counts; their exact path/hash/ranges are retained in the source identity ledger and will travel
with used own baseline authorities. No indirect approval is substituted for an own verdict.

## 5. Process boundary

All algebra here is by hand and ONLY the required baseline audit. No new delta2 proof/lemma or route
adaptation has started. This exact gap will be sent to Main before such work. The accepted DELTA1 theorem
and its full own corrections were read as exposure; none supplies delta2 coverage. No old R-specific lemma
is imported at a new R. All permanent process departures remain. No computation/enumeration/assertions,
solver, tests, model/native/network or old-file edit was used. Metadata identities/counts are not proof.
