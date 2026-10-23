# Sharp minimal phase-type order, one complex pair — parent verdict (math-1) — 2026-10-18T01:54:29-07:00

**Disposition: GATE MET at the frozen scope of Commault–Mocanu2003Conjecture1: the sharp PH order is attained for every nondegenerate three-pole constant-numerator transform below. Correctness is accepted as a written proof; novelty is UNCLEAR after bounded primary-source screens. The book's general minimal-PH question is NOT solved.**

Version2 corrects only the worker-proof relative link in `phase-type-complex3-parent-verdict.md`; that initial file is retained. No claim or evidence changed.

## Accepted theorem

For every real a>c>0 and b>0, let

    F(s) = c(a²+b²) / [(s+c)((s+a)²+b²)].

Its minimum PH order is

    n* = min{n∈Z : n≥3, b≤(a−c)cot(π/n)}
       = ceil[π / arctan((a−c)/b)].

A PH representation is a real pair(α,T) with α≥0,α1=1,T Metzler and Hurwitz,T1≤0, and F(s)=α(sI−T)^−1(−T1). The lower bound covers **every** finite PH representation, including unreachable/unobservable states and reducible matrices, not just cycles. The construction attains it with an n*-state cycle and α=e1. Every upper endpoint is included; a lower band endpoint belongs to the smaller order.

- **Correctness:** ACCEPTED, written universal proof using ordinary background, not a finite table or numerical root-finder premise.
- **Priority:** NONE-FOUND-IN-SCOPE for an earlier all-parameter sharp-order result. Substantial spectral and boundary ingredients are prior; see below.
- **Novelty:** UNCLEAR. No "first" claim.
- **Significance:** a specialist answer to an explicitly stated2003conjecture, advancing the matched general upper bound from n*+1 to n* in every strict band interior. The minimum n* is unbounded although the denominator degree is3. This is not a general algorithm for minimal PH realization or for arbitrary numerators.
- **Gate basis:** the complete-solution half of the run contract, **not** a claim of a wholly new angle or positivity method.

## Source and exact scope

Frozen [contract](../screening/math-1-phase-type-complex3-contract.json), SHA `1bb5bc6e72605a89cab72e106f881184ed99dfb8c10477b1e39eca207c7bcd13`.

Commault–Mocanu, *Phase-type distributions and representations: some results and open problems for system theory*, International Journal of Control76(6),566–580(2003), DOI https://doi.org/10.1080/0020717031000114986. Pinned PDF SHA `8db1e4aa330a9d9989cb91498524d9cb0c41a95aa636906ed6e42391d5d70cfb`. The parent read the rendered Eq42 and Conjecture1 on printedp577/PDF13:

> Conjecture 1: There exists a representation of order n_min for such a distribution.

The transform in Eq42 is1/[(1+s/c)(1+s/(a+ib))(1+s/(a−ib))], exactly F. The printed domain says a,b,c≥0; the accepted theorem explicitly keeps the contract's **a>c>0,b>0** domain. The b=0 case is already a three-exponential convolution and is not a new contribution here. No statement about undefined zero-rate limits is made.

The mathematics book's chapter *Minimal Representation of Phase-Type Distribution*, Qi-MingHe/HanqinZhang, bookp544/PDF560, motivates the general question; only this separately stated published family is resolved. Bookp545 contains references, not the opening problem statement.

## Accepted proof and pins

| Artifact | sha256 |
|---|---|
| [Worker proof v3](../../../../mathematics/evidence/six-lane-20261016/phase-type-complex3/proof/ph3-theorem-v3.md) | `260711591c812c30f01f7662d30b583da2d7baa7c28608ce1d882090b47a2ef5` |
| Candidate pin v2 | `15144191dd2fbb8070d57873ad0db579e5fc21c0b875e14d5c3351d13b3179cb` |
| [Hostile desk RESULT.v2](phase-type-complex3-hostile-v1/RESULT.v2.json) | `084a21a5e8e3fd9d927a2610f7af89adc93f1f03fbf4dcb167478ecfbd77e958` |
| [Parent derivation with dated corrections](phase-type-complex3-parent-derivation-v1.md) | `29ed4ece2ed7a6d60a852ed955c58a23889c179194e78d0f6038b48759ca9dca` |
| [Parent exact-Fraction checks](phase-type-complex3-parent-smoke-v1/exact-rational-v1.json) | `a005c05c0033b72ffcc37cd61a499f613b644a4633516636c768e9f06eebcdb5` |
| [Parent high-precision smoke v2](phase-type-complex3-parent-smoke-v1/RESULT.v2.json) | `cff3a8dc8683ceafbd5011da2211513ab96cbedfcd0723aa2afcbf19de575c53` |

Proof route, independently read/re-derived by the parent:
1. Trim unreachable states. Hurwitz and the row-sum condition forbid any state that never reaches absorption. A Perron left-vector/Laplace-divergence argument fixes the trimmed generator's dominant eigenvalue at−c, even for reducible matrices. The sector inequality then forces n≥n*. AppendixA gives a self-contained polygon/tangent-cone/Jensen proof of the classical sector inequality.
2. Normalize δ=a−c,β=b/δ. A scalar IVT chooses three angles; n−3angles are ψ=π−2arctanβ. Their sum is2π and the sine product gives eigenvalues1,±iβ of the Metzler cycle. Its positive Perron vector fixes spectral abscissa1.
3. The remaining factor of the characteristic polynomial is cancelled by exit coefficients taken from the Taylor jet of h(x)=1/[(1−x)(x²+β²)] at m*=(1−β²)/2. The trigonometric coefficient identity gives positivity throughout every required band.
4. Positive diagonal scaling produces a Hurwitz PH generator with α=e1 and exactly F. The n=3 IVT starts at t0=2φ>0; its quotient isP=1 and its exit vector is(0,0,K), so no separate published PH-existence assumption is required.

**Imports:** ordinary background(Perron–Frobenius, IVT, Jensen, convex-plane geometry, law of sines, matrix Laplace transforms and the Chebyshev generating identity). The source's Theorems6 and14 are classical alternative comparisons, not load-bearing unproved imports in this accepted route. "No imports" in the model notes means no extra specialized theorem beyond that ordinary background, not an axiom-free proof.

## Independent verification

- The parent wrote its derivation before the worker text was delivered and independently checked the all-n angle signs, quotient/resolvent, coefficient positivity and PH scaling. It then read the worker's direct lower-bound and polygon arguments and the complete v2→v3 delta. The parent derivation and smoke were **withheld** from both hostile reviewers.
- Parent exact-Fraction route, no worker imports: three rational realizations at orders3/4/6, twelve exact transform evaluations, positivity/normalization/polynomial identities, and three wrong-initial-state controls all pass.
- Parent60-digit mpmath route, separately authored, hash-pinned before in-process execution:138/138cases,n*=4..30, fivecontrols pass. Its failed v1 remains visible: five exact upper endpoints were rejected by an over-strict floating sign check; v2 adds an explicit numerical endpoint tolerance. These are finite aids, not universal proof or interval certification.
- Worker checks, honestly scoped:32/33symbolic items with one subsequently resolved simplifier miss; b01=88/98with ten enclosure-width flags, superseded by b02=112/112and336PHchecks; dense sweep1,605instances/3,210checks; independent-labelled150-digit route187/187;47,070random-Metzler complex eigenvalues with no sector violation. The parent did not independently audit the ball eigen-enclosure internals or establish the worker's claimed code-path independence; neither is a theorem premise.

## Hostile reviews and all finding dispositions

| Reviewer | Disposition | Proof judgment | FATAL | MAJOR | MINOR |
|---|---|---|---|---|---|
| Codex gpt-6.1-sol,max,read-only ([note](phase-type-complex3-codex-v1.note.md)) | ACCEPT-WITH-FIXES | COMPLETE-NO-IMPORTS |0|0|3|
| Claude claude-opus-5-5,max,no tools ([note](phase-type-complex3-claude-v1.note.md)) | ACCEPT-WITH-FIXES | COMPLETE-NO-IMPORTS |0|0|7|

The desk wrote its own static audit before reading either note. Its consolidated11findings are all non-load-bearing. Frozen proof/pin bytes are not rewritten; these corrections govern:

1. **F1:** the standalone Theorem14 comparison presupposes F is PH. Do not use it to establish PH-ness circularly. The accepted route is PartB for **all n≥3**, which establishes PH-ness itself; Theorem14 is then a comparison.
2. **F2:** every conclusion mentioning "Eq42family" means **a>c>0,b>0**, exactly the accepted theorem above.
3. **F3:** pin-v1's01:03:30label is forward-dated relative to observedmtime01:02:22; pin-v2's01:06:00label differs from observed01:05:55. The d01run really follows pin-v1; labels, not hashes, are corrected. Filesystem mtimes are observations, not cryptographic attestations.
4. **F4:** AppendixB lists mathematical smoke runs, not every API probe(p00omitted).
5. **F5:** b01is88/98,ten flagged by its absolute enclosure-width test, not allPASS. f01aborted as numerically singular at n*=35; a pivot-scale threshold is the worker's diagnosis, not independently proved. f02is187/187but reaches maxn=29; the separate dense sweep coversn=35andlarger. No failed outcome is hidden.
6. **F6:**1,605=38·42+9instances;390arrangement cases=195distinctarrangements at two β values. These are not390distinct permutations at one parameter.
7. **F7:** AppendixA's local overloaded symbols are read with their stated local meanings; use τ for semigroup time and a distinct angle name when restating it.
8. **F8:** v3 strengthens the dependency claim by invoking the already-written n=3branch and AppendixA; the proof steps did not change, but the dependence description did.
9. **F9:** exits t1=t2=0; t3..tn>0. Read "every exit nonnegative", not all strictly positive.
10. **F10:** "non-singular PH generator" is a paraphrase of the source definition, not a literal quotation.
11. **F11:** cite the PH irreducibility definition atp568 and its positive-realization counterpart atp570; neither requires the generator matrix itself to be irreducible.

## Primary comparison and priority limits

[Full parent comparison](phase-type-complex3-priority-parent-comparison-v2.md), SHA `98bb3c5a29da4656f6b1c71dc9f03ed8d25524909d11d6364b04b08566a9fd60`:
- **Mocanu1999Theorem50:** n*+1 for this complete family; parent read the actual thesis, not just CM2003's citation.
- **Mocanu1999Lemma51/Eq4.13:** exact n on **every** boundary β=cot(π/n), including the same boundary trigonometric coefficient-positivity kernel. These are not new results.
- **Verbeken–Ginis2026:** published cycle/spectral-angle mechanism. Their single-eigenvalue placement does not by itself supply input/exit vectors for this transfer function.
- **Kim2016:** numerical HFCB methods; extra Erlang-tail states may be needed. Full technical text now read by the parent.
- **Benvenuti–Farina:** β=1,n=4 is an older shifted four-cycle example, not a new example.

Both the [pre-result](../screening/math-1-phase-type-complex3-priority-v1.md) and [post-result](../screening/math-1-phase-type-complex3-priority-post-v1.md) bounded screens located no earlier all-parameter sharp-order proof. The parent's subsequent primary readings close their specific thesis/Kim2016access holes and narrow the possible contribution to the **off-boundary n* realization plus the assembled all-n theorem**. Remaining access/search gaps include the fullPOSTAchapter,O'Cinneide1999body,somepaywalledKimwork,CNKI/GoogleScholar and possible equivalents. Search misses are not novelty; no claim of a new spectral/angle method or new boundary positivity is accepted.

## Verification boundary

This is a reviewed written proof, **not Lean/kernel formalization or human peer review**. Finite checks are aids. Claude received desk-transcribed primary excerpts without tools; Codex's claim to have checked page images is not supported by an image-tool event in its log, so that visual comparison is not counted. The parent separately read the relevant rendered sources. No publication, contact, commit or push is authorized by this verdict. The run continues exploring other targets until its frozen deadline.
