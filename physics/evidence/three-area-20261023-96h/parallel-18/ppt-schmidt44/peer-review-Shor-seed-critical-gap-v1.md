# Shor seed critical-gap compatibility — actual cross-domain reconstruction

Reviewer: **PhysicsPPT44**, physics-3; own P44 ownership retained. Assignment: `institute/runs/three-area-2026-10-23-96h/peer-review-wave-eighteen-v10.json`, exact PhysicsPPT44 entry. Actual `/bin/date` observations: first assignment read `2026-10-24T02:53:25-07:00`; post-contract ACK `2026-10-24T02:54:30-07:00`; during reconstruction `2026-10-24T03:00:39-07:00`; before this output `2026-10-24T03:04:51-07:00`. These are observed clocks, not asserted exact file-creation times or a claim of uninterrupted activity.

**Verdict: 0 FATAL / 0 MAJOR / 0 MINOR defects found at the literal supplied-proof scope.** The critical-gap theorem, its endpoint restrictions and its no-UD-AND-FACTOR-COMPLETE-one-remaining-length corollary reconstruct as written. No mathematical repair requested. This is a different-domain, same-harness written reconstruction, not blind/cross-vendor/human/formal verification, novelty clearance or parent acceptance.

## 1. Exact snapshots and actual coverage

All paths below are relative to `/Users/jinleic/repos/aifours`. Abbreviations:

- `S/` = `mathematics/evidence/three-area-20261023-96h/parallel-18/shor-completion/`.
- `A/` = `physics/evidence/three-area-20261023-96h/parallel-18/ame46-support/`.
- `R/` = `institute/runs/three-area-2026-10-23-96h/`.
- `B/` = `mathematics/shor-code-finite-completion/`.

These hashes were independently obtained from actual on-disk bytes, and the specified bodies were read, not inferred from the hashes:

| Actual input | SHA-256 | Actual coverage |
|---|---|---|
| `S/proof-SEED-CRITICAL-GAP-MIXED-COMPATIBILITY-v1.md` | `5c9ecf12e98b92bb97406dbf7f70fdac024172795ed47c92a1db46fba350b364` | Complete 183-line new proof |
| `S/construction-MIXED-LENGTH-UD-SEED-v1.md` | `c45ef598f9b7cbf234d6dfc5adad448285b80ff58bf5650bc994948a8ff081df` | Complete 123-line actual seed |
| `S/construction-MIXED-LENGTH-UD-SEED-pure-power-addendum-v1.md` | `9205b212da51dc295e0e6e938ec1d414e5b0297d8dff3b026639970959df0678` | Complete 60-line actual addendum |
| `S/proof-RAW-GAP-PARSER-AND-FOUR-A-COMPATIBILITY-v1.md` | `adf92f65c11c0fe03e3941102bf4492979dcb68e493443553b3802c71a26c2bb` | Complete 163 lines, including actual GP definition/proof |
| `S/proof-RAW-TWO-THREE-A-LAYERS-v1.md` | `0614a8e399f789397cdfaf4c6c6adb3d514f884264f6bc5fbd9e22cd71465ba2` | Complete 188 lines, including raw padding principles |
| `S/selection-v1.md` | `d7ac86b0c69dc96b82361d16c17145593e47b6c3d8dce7c99a539bf34be00ba3` | Complete 60 lines; literal target/source boundary |
| `A/peer-review-Shor-mixed-length-nogo-and-seeds-v1.md` | `e8e4ce8601967a24351b794cfc3f2d2ef948eef167dfe45b047795bdd4336f92` | Complete 153 lines, with truncated LF19 recovered raw |
| `R/shor-mixed-length-parent-v1.md` | `f1d49e7b38f94d3b00f4b2b539664f8a8b691f3f80a991a6ccf12f20880b1097` | Complete 31 lines; actual seed-coverage qualification |
| `R/shor-raw-structure-parent-v1.md` | `44cd995080ce6b66e3d31c8a6c7d4c58cbebbd3039c375c22f118514b1533f9c` | Complete 40 lines; exact raw import boundaries |
| `B/evidence/raw-instance.json` | `6eb38f63bfee602369a09b22be26a0c598111f33b8202d44349786903f63ecf4` | Complete JSON; actual sixteen pairs |
| `B/source/problem.zh.txt` | `642b818093ac231cbc44006dc324d73492c6ad9a9b71c469a327cbb4307a75c8` | Complete 30 lines; literal factor-completeness quantifier |
| `R/peer-review-wave-eighteen-v10.json` | `b725e1f7d4a8eca73a283cc1133b0ab91e7b0685432be56bfbc7d9285e82c7ca` | Complete common contract and exact reviewer entry; manifest read through its end |

Prior exposure: parent Shor status summaries and MathShor's supplied N4 mathematical review/coordination. Before this assignment I had not read the Shor seed or this critical-gap proof. During the assigned reconstruction I read the earlier actual review and parent qualifications as explicitly required; their verdicts are exposure, not a verdict transferred to the new 183 lines. The older homogeneous no-go manuscript is not a premise of the new argument and is not independently re-reviewed here.

The seed addendum's actual basename above is the one with the frozen `9205b212…` hash. I read the earlier review's dispatch-only suffix-order correction and D1: dropping COMPLETE from a no-go claim would be false. The present new theorem/corollary and this review retain UD **and factor completeness** throughout. Parent's earlier seed coverage was the full peer reconstruction rather than line-by-line seed-body reading; my current full body reads do not retroactively alter that historical coverage. The book transcription's historical image-check statement is not a new page-image inspection by me.

## 2. Literal statement and the raw interface actually used

The actual sixteen words are

    C = b{1,a,a^7,a^13,a^14}
        ∪ {a^3,a^8}b{1,a^2,a^4,a^6}
        ∪ a^11b{1,a,a^2}.

In particular `b`, `ba`, `ba^7`, `ba^13`, `a^3b`, `a^3ba^2`, `a^8b` and `a^11b` used below really are present. A code is a set of nonempty raw words; UD concerns all finite codeword lists, not just bounded parses. Factor completeness is exactly

    for every binary raw word u, some xuy belongs to M*.

Fix any integer n≥26 and the actual 21-word seed

    M_n=C∪{W,V,Q,Z,a^n},
    A=ba, W=ba^2b, P=a^3b,
    V=ba^2ba, Q=ba^2ba^2, Z=a^3bab.

The new result is conditional on an arbitrary **finite UD factor-complete** M containing this M_n. There is no uniform bound on its words, delays or number of b's. The pure-a seed parameter n and a hypothetical common new-word length N are different variables. No claim says that every completion of C contains this seed.

I reconstructed the two necessary raw principles directly from their actual definitions:

1. Since b∈M, two different raw words with one fixed internal core can be padded to common leading/trailing b lengths. They then give distinct M-lists for the same word. Hence each fixed internal core has at most one raw M-word. The same padding turns two different labelled free-end parses into a UD violation.
2. For finite M, let D be its maximum word length. Embed `b^(2D) U b^(2D)` as a factor of an M-product. Every codeword meeting an a of U lies inside this padded factor. If U's a-positions cannot be partitioned by smaller-a codewords, one ACTUAL codeword must contain the entire core U. This is not an inference from a factor to a codeword without checking partitions.

At each free-end boundary u,v the exact condition is `gap≥beta_u+alpha_v`; surplus b's are the uniquely determined intervening b codewords. The empty gap list represents **one a**; pure-b words are handled separately. These elementary interfaces suffice here. No historical pure-a-order bound, Szabó/Rédei theorem, realization converse, mass-counting layer theorem or finite automaton execution is needed.

## 3. Supplied seed imports reconstructed, not merely accepted from the old verdict

### All-list UD and pure-power family

For the 20-word seed, first-b delays are `I={0,3,8,11}`. Positive same-row right-exponent differences are exactly

    S0={1,2,4,6,7,12,13,14}.

The positive i−s with i∈I, s∈S0, s<i have row lists `2,1`; `7,6,4,2,1`; `10,9,7,5,4`. Their union is `B0={1,2,4,5,6,7,9,10}`; both S0 and B0 avoid I.

All initial proper-prefix residuals are either a power `a^s`, s∈S0, or `a^k b q`, k∈B0, total length≤14. Different first-b rows are incomparable. Within row0, W,V,Q give residuals a/a^2 and, against b/ba, first-b-delay2/1 residuals. Longer old row0 tails disagree at the new second b. Within row3, only P prefixes Z, leaving ab; the other old tails disagree before either ends. Rows8/11 are unchanged. These cover all pairs.

A b-containing residual with first-b delay in B0 is incomparable with every seed word, because its first b disagrees with the first-b row I. A pure residual can only prefix a word whose first-b delay exceeds s; the new delay i−s lies in B0. It cannot equal a codeword. Thus the stated finite residual invariant is closed and excludes epsilon. Prefix cancellation proves UD of **all finite lists**, not a finite-depth empirical test.

For every n≥26, replace pure residuals by powers with lengths in `S0∪(n−S0)`. All are strictly between0 and n, and n−s≥12 exceeds every old first-b delay. The new a^n is initially incomparable with all old words; its only pure-residual transitions exchange s and n−s. B-containing residuals remain incomparable. Even an overlap between those two length sets cannot reach epsilon. This independently reconstructs the uniform 21-word UD import.

### Every low-a gap pattern, not selected examples

The actual free-end existence table reconstructs as follows; displayed unspecified gaps are positive:

| Number of a's / gaps | Existing labelled parse |
|---|---|
| 1 / empty list | A |
| 2 / 0; positive | W; A,A |
| 3 / (0,0); positive-positive; (i,0) | P; A,A,A; A,W |
| 3 / (0,1); (0,k≥2) | V; W,A |
| 4 / all positive | A,A,A,A |
| 4 / (0,j≥2,k); (0,1,k) | W,A,A; V,A |
| 4 / (i,0,1); (i,0,k≥2) | A,V; A,W,A |
| 4 / (i,j,0) | A,A,W |
| 4 / (0,0,1); (0,0,k≥2) | Z; P,A |
| 4 / (0,1,0); (0,j≥2,0) | Q; W,W |
| 4 / (i,0,0), including i=0 | A,P |

All thresholds follow from the actual outer delays, for example W,A and W,W require gap≥2, while V,A requires≥1 and A,P permits gap0. The table exhausts the zero/nonzero patterns and every positive gap value. UD plus b-padding gives uniqueness. The added a^n cannot enter any ≤4-a core. Therefore any UD superset of M_n forbids **every new raw word with one through four a's**: the old parse and the proposed single-word parse would pad to two actual lists. A further pure-b word is already forbidden by b∈M and UD.

For completeness of the import check, the row Kraft numerators at denominator32768 are 24707,2720,85,14, totaling27526; the four new words add4096. Thus the seed mass is15811/16384, and adding2^(−n) remains below1. More directly, the 20-word seed has no a-run longer than25, while the pure-power family replaces that obsolete missing factor by `b^30a^5b^30`: only A,W,P could cover its central a's, and their only zero-gap boundary is A→P. No partition of five adjacent a's is possible. This reconstructs incompleteness without substituting mass for factor completeness. These are written arguments, not arithmetic-code or residual-enumeration results.

## 4. New H forcing and positive-delay endpoints

For pure adjacent runs of sizes1,2,3,4 the only possible parses in a UD extension are respectively

    A; W; P; A,P,

with outer-delay pairs `(1,0),(1,1),(0,1),(1,1)`. The only zero-gap boundary is A→P, so no proper partition makes five adjacent a's. Long b-padding therefore forces one actual word `H=b^R a^5 b^T`, initially R,T≥0. Padding injectivity makes this core's word unique. This does **not** assert that H is the only word with five a's in total: C already contains `a^3ba^2`, a different internal core.

I expanded both endpoint ambiguities with literal listed words:

- If T=0, `(H)(a^3b)=(b)^R(a^8b)`, both `b^R a^8b`. The lists differ; R=0 is allowed in this contradiction.
- If R=0 and T≥1, `(ba^7)(H)=(ba)(a^11b)(b)^(T−1)`, both `b a^12 b^T`, with different first codewords.

Every exponent is nonnegative, including T=1. Thus R,T≥1. No seed word has the pure internal core a^5; in particular a^n has n≥26. Hence H is genuinely new.

## 5. Exhaustive critical-gap reconstruction and rejection of the sole nongrowing escape

Set `g=R+T−1≥1` and force a parse of `a^5 b^g a^5` using sufficiently long b-margins.

If no word contains a's on both sides of the central gap, each five-a run must be H. Their boundary requires at least T+R b's, exceeding g. Thus a crossing word exists. Two such words cannot both cross the same gap in a disjoint ordered factorization.

Let the crossing word cover i left a's and j right a's. Its core is exactly `a^i b^g a^j`, with 1≤i,j≤5. A nonempty remaining left prefix has size≤4 and meets the crossing word at gap0; its last trailing delay must be0. In the reconstructed pure-run table only the size1 prefix A has that property. Hence i=4 with leading delay0, or i=5. Similarly a nonempty right suffix must have first leading delay0; only the size3 suffix P qualifies. Hence j=2 with trailing delay0, or j=5.

This leaves exactly:

| (i,j) | ACTUAL crossing word |
|---|---|
| (4,2) | `a^4 b^g a^2` |
| (4,5) | `X45=a^4 b^g a^5 b^beta` |
| (5,2) | `X52=b^alpha a^5 b^g a^2` |
| (5,5) | `X55=b^alpha a^5 b^g a^5 b^beta` |

No real-only, reflected-word, selected-order or bounded-g restriction entered this classification.

For the first type, write `B42=a^4 b^g a^2`. I checked both exhaustive gap cases:

- g=1: `(W)(B42)=(V)(a^3ba^2)`, both `b a^2 b a^4 b a^2`. The fixed five-a word is in literal C; W and V are different first codewords.
- Every g≥2: `(b)(B42)(b)=(A)(P)(b)^(g−2)(W)`, both `b a^4 b^g a^2 b`. Here the middle b-count is `1+(g−2)+1=g`; first codewords b and A differ. At g=2 the intervening power is simply an empty list of b's, not an epsilon codeword.

Thus the only possible nongrowing crossing type is impossible at **every** g≥1. One of X45/X52/X55 must actually lie in M.

The length arithmetic is literal, with no asymptotic qualification:

    |H|=g+6,
    |X45|=g+9+beta=|H|+3+beta,
    |X52|=g+7+alpha=|H|+1+alpha,
    |X55|=g+10+alpha+beta=|H|+4+alpha+beta.

This proves all three claimed strict-growth bounds.

## 6. Additional endpoint exclusions and the X55 disjunction

For X45 with T≥2 let U=max(beta,T). The actual lists

    (ba^7)(X45)(b)^(U−beta),
    (b)(a^11b)(b)^(T−2)(H)(b)^(U−T)

both give `b a^11 b^g a^5 b^U`. The inner b-count is `1+(T−2)+R=g`; all padding is nonnegative, including T=2, and the first codewords differ. Hence this X45 is forbidden.

For X52 with R≥2 let L=max(alpha,R). The actual lists

    (b)^(L−alpha)(X52)(a^11b),
    (b)^(L−R)(H)(b)^(R−2)(ba^13)(b)

both give `b^L a^5 b^g a^13 b`, since `T+(R−2)+1=g`. All powers remain nonnegative at R=2. The lists are distinct: the second uses only b,H,ba^13, none equal to the crossing word X52 present in the first.

Therefore R,T≥2 excludes both alternatives and forces X55. If also alpha≤R−1 and beta≤T−1, compare

    (H)(b)^(R−1−alpha)(X55)(b)^(T−beta),
    (b)^(R−alpha)(X55)(b)^(T−1−beta)(H).

Both spell `b^R a^5 b^g a^5 b^g a^5 b^T`. All exponents are nonnegative; the second list begins with b while the first begins with H, since R−alpha≥1. Consequently **alpha≥R OR beta≥T**, not an unjustified AND. It follows that `alpha+beta≥min(R,T)` and `|X55|≥|H|+4+min(R,T)`. The source correctly makes no automatic infinite-growth iteration from this disjunction.

## 7. All-n/all-N flat-remainder consequence and missing-premise check

Assume `M=M_n∪T_N` is finite UD factor-complete, with all additional words in `{a,b}^N`. H is outside M_n, so |H|=N. Each forced crossing alternative is also outside M_n:

- X45 begins with four a's before its first b, a first-b row absent from the literal seed.
- X52/X55 have a positive internal gap following a run of five a's, absent from every listed seed word. If alpha=0 their first-b delay5 is absent; if alpha>0 their actual multi-b pattern is not a seed pattern.
- The pure-a a^n contains no b and cannot be any alternative.

Thus the forced crossing word also belongs to T_N and has length N, contradicting its strictly larger length. This works for **every integer n≥26 and every positive integer N**, with no requirement N>n, no sampled orders and no assumption that all such n admit any completion.

**Missing premises for this literal conditional theorem: none identified** after reading and reconstructing the actual seed, padding/free-end definitions and listed C words. Finiteness, UD, factor completeness and containment of this fixed seed are indispensable explicit hypotheses. The result neither excludes arbitrary heterogeneous further lengths on this branch nor shows that an arbitrary completion of C contains this branch. It does not produce a finite complete code or prove unrestricted noncompletion. It adds no pure-a-order bound; 26 remains the sufficient seed-separation parameter. UD INCOMPLETE supersets exist, so omitting COMPLETE would destroy the corollary.

## 8. Mandatory overlays, execution boundary and disposition

The complete common contract and exact reviewer entry were read before substantive work. All five mandatory overlays were read completely; the nested quarantine record was also read to distinguish its superseded live-process status from the corrected execution receipt. Actual observed control pins:

| `R/` control file | SHA-256 |
|---|---|
| `parent-timestamp-erratum-v1.md` | `1ad365961ba16360450eaa8b694ad82fe25bf663dc024b5e12801398e0dc8b01` |
| `parent-verification-erratum-v1.md` | `163e8fbea4328674c181aba6a6a13fa99d07e1562cd401e8fbbb3c782ecd1f27` |
| `parent-evidence-erratum-v2.md` | `5985021a2f0429681c6e7f9c53e69fec310dbdf90d138465ba6717f6efe102e9` |
| `parent-evidence-erratum-v3.md` | `1f346c1f8d4e10b960e0b157a2fb19603dbce2f073320cd44b8d56b369ed0e26` |
| `physics-ppt44-normalized-n4-001-execution-receipt-v2.json` | `646566eca5a750a92676b0ed615553626660f09ea008dc3464afa21de5284f11` |
| `n4-overrun-quarantine-v1.json` | `6213f891a2d6aca508c114355678dc647d2aca26aeba01e0b84724350064c067` |

N4's corrected UNKNOWN/process-absent/resource-failure and unestablished-child-exit qualifications are retained; no native retry or admission follows from this review. No scientific execution, arithmetic script, code import, syntax-check, compile, test, enumeration, solver, native launch, external-model CLI or nested agent was used. All concatenations, gap cases and length comparisons above were reconstructed in writing. Metadata hashes/clocks and local source reads are the only command/tool observations. Only this named NEW owned-root output is written; author/shared files remain untouched.

**Disposition:** the pinned critical-gap packet is supported at its literal supplied-proof written scope, subject to separate parent disposition. No source repairs or expanded review are requested. Correctness at this level, source/import trust, scope, novelty, significance and formal acceptance remain separate. Literature priority is unassessed; the unrestricted Shor target and heterogeneous seed completions remain unresolved. Return this exact full path/pin directly to author MathShor and Main; no additional dependent reviewer is named in this entry. Then retain the owned P44 primary without any scientific execution permission.
