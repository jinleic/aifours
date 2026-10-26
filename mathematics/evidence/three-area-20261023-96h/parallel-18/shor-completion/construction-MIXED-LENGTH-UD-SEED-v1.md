# An actual mixed-length UD seed, with a written all-word residual certificate

Observed before creation: **2026-10-23T15:58:33-0700 PDT**. MathShor, math-5. **CANDIDATE explicit finite UD extension, deliberately NOT complete.** This is a sufficient construction branch within the ONE Shor question, not a replacement of its unrestricted quantifiers, a finite maximal-code witness, or a novelty claim. No program, enumeration, word-generation script, solver, compilation or executable verification was used.

The common-added-length family has a new all-order obstruction in `proof-MIXED-LENGTH-GROWTH-AND-HOMOGENEOUS-NO-GO-v1.md`. This packet returns to actual mixed-length RAW-SELECTOR construction: it supplies raw words and an explicit finite residual invariant rather than another scalar-positive table. It also shows that the already-supported two-/three-/four-a shape is not internally contradictory on this branch.

## 1. Literal construction and exact achieved scope

Keep the exact16-word C. Add

    u=ba^2b       =baab,
    v=ba^2ba      =baaba,
    w=ba^2ba^2    =baabaa,
    z=a^3bab      =aaabab.

Put

    M_seed=C∪{u,v,w,z}.

These are four distinct new words, each with TWO b's, whereas every C-word has one b. Thus M_seed has20literal words. Their added lengths are4,5,6,6.

**Claim.** M_seed is UD over all finite lists, and every internal b-gap list with at most FOUR a-positions has exactly one free-end parse using M_seed. Nevertheless it is incomplete: a^26 is still a missing factor and its binary Kraft sum is15811/16384<1.

Consequently this is not a completion. The positive result is an actual mixed-length realization of all the previously derived low-a compatibility conditions, with an all-word UD certificate. A finite completion of M_seed would suffice to complete C, but no such completion is asserted and a failure of this branch would not refute C's unrestricted completion question.

## 2. A finite residual invariant proving full UD

Every M_seed-word contains b. Its first b occurs after a-count in

    I={0,3,8,11}.

Define

    S={1,2,4,6,7,12,13,14},
    B={1,2,4,5,6,7,9,10}.

The first is exactly the union of positive right-exponent differences within the four C rows. The second is exactly the set of positive differences i-s for i∈{3,8,11}, s∈S with s<i:

    i=3: 2,1;
    i=8: 7,6,4,2,1;
    i=11:10,9,7,5,4.

In particular B∩I is empty, and S∩I is empty.

Let R_res be the following finite set of nonempty raw residuals:

    {a^s:s∈S}
       ∪ {a^k b q : k∈B, q∈{a,b}*, |a^k b q|≤14}.     (R)

This is a finite set defined mathematically; no exponential list has been generated. It excludes epsilon. I prove the full initial-residual coverage and prefix-comparison closure, which is sufficient for UD by cancellation.

### Initial proper-prefix residuals: all cases

Two codewords with different first-b positions in I are not prefix-comparable: at the earlier first-b position one has b and the other a. Thus only equal-row comparisons matter.

- Between two C-words in the same row, a proper-prefix residual is a^s for s∈S.
- In the first-b0 row, the new u,v,w have common form b a^2 b a^j, j=0,1,2. Between these three the residual is a or a^2, already in(R).
- Comparing them with C's b and ba gives respectively a^2 b a^j and a b a^j. Their first-b delays2 or1 belong to B and their lengths are≤14.
- C's other first-b0 words ba^7,ba^13,ba^14 are incomparable with u,v,w: the new second b occurs after two a's while the old tails remain pure a's. Neither direction supplies a hidden residual.
- In the first-b3 row, z=a^3b a b is comparable with C's a^3b, giving residual ab, whose first-b delay1 belongs to B. The other old right tails a^2,a^4,a^6 disagree with z's tail ab before either word ends, so are incomparable.
- The first-b8 and11 rows have no new words and were already covered.

These exhaust all distinct codeword pairs. Every non-pure initial residual lies in the second part of(R); all have length at most14 since the maximum codeword length is15.

### Full residual closure

For a residual a^k b q with k∈B, its first-b delay differs from EVERY codeword's first-b delay in I. It is therefore incomparable with every codeword. Such a residual has no outgoing prefix-comparison transition at all.

For a pure residual a^s, s∈S, no codeword can be a prefix of it because every codeword contains b. It can be a prefix of a codeword only when the codeword's first-b delay i exceeds s; equality i=s never occurs since S∩I is empty. Removing that prefix leaves a residual whose first-b delay is i-s∈B and whose length is≤14. This also covers z's extra second b: the remainder may contain more than one b, which(R) explicitly allows.

Thus every possible nonempty residual transition stays inside(R), and no equality residual=codeword can produce epsilon. If two distinct finite M_seed-lists had equal concatenation, cancelling their first differing prefix-comparable codewords would enter(R), and subsequent cancellation would keep a residual there until it became empty. That is impossible. This proves UD for ALL finite lists, without a finite-depth parse test or executable Sardinas–Patterson run.

## 3. Exact realization of the low-a gap constraints

The seed's one-a word is A=ba, its two-a word is W=u=b a^2 b, so r=t=1. Its three-a words are

    P=a^3b,
    V_1=v=b a^2 b a,

with gamma_1=1,delta_1=0. There are no U_s because r=1. Its four-a words are exactly

    Q=w=b a^2 b a^2,
    Z=z=a^3 b a b.

The crossing rectangle1≤i<r is empty, not an omitted condition. The new mixed-length growth requires a Q-core a^2 b^(r+t-1)a^2=a^2ba^2. The actual Q=w has alpha1,beta0, satisfying alpha≥r, and |Q|=6=|W|+2. This realizes the relative growth locally; it does not prove sharpness among actual complete extensions.

For completeness of the claimed small-core realization, here is an all-gap argument, not a finite sampling. A free-end parse treats a boundary between codewords p,q as legal when the actual b-gap is≥beta_p+alpha_q.

- With one a, A parses the empty gap list.
- With two a's, gap0 is W; every positive gap is A,A.
- With three a's, gaps(0,0) give P; positive-positive gaps give A,A,A; gaps(i,0), i≥1 give A,W; gaps(0,1) give V_1; and gaps(0,k), k≥2 give W,A.
- With four a's and all gaps positive, use A,A,A,A.
- On(0,j,k) with j,k≥1, use W,A,A if j≥2 and V_1,A if j=1.
- On(i,0,k) with i,k≥1, use A,V_1 if k=1 and A,W,A if k≥2.
- On(i,j,0) with i,j≥1, use A,A,W.
- On(0,0,1), use Z; on(0,0,k), k≥2, use P,A.
- On(0,1,0), use Q; on(0,j,0), j≥2, use W,W.
- On(i,0,0), including i=0, use A,P.

Every actual nonnegative gap list with at most four a-positions falls into exactly one of these existence cases. The full UD proof in section2 implies at most one free-end parse: two parses could be padded to the same raw word using b. Hence these are unique parses. Higher-a C-words cannot intrude into a core with≤4a because they contain too many a's. No unrestricted completeness claim follows from this small-core coverage.

## 4. Exact incompleteness and why this is not a disguised witness

C's binary Kraft sum is13763/16384, as follows directly from its literal row lengths. The four extra words contribute

    2^(-4)+2^(-5)+2·2^(-6)=1/8=2048/16384.

Therefore

    Kraft(M_seed)=15811/16384,
    deficit=573/16384>0.

No scalar-positive completion has been manufactured. More decisively, every seed word contains a b, the maximum initial a-run is11 and maximum terminal a-run14. Any a-run in a concatenation crosses at most one codeword boundary, since every codeword has b. Thus its length is at most11+14=25. Consequently a^26 is a factor of no M_seed-product, proving literal factor-incompleteness.

The old missing C-factor bbaab IS now present: it equals the product(b)(u). This is genuine added raw coverage, not a full coverage theorem. There is still no pure-a codeword in M_seed, and an actual finite completion would need the inherited admissible pure-a order and many further raw words. Nothing in this packet asserts their existence.

## 5. Exact remaining mixed-length RAW-SELECTOR obligation

A constructive sufficient branch is now: extend this ACTUAL UD seed by finitely many further raw words, allowing mixed lengths, while retaining a finite epsilon-free residual closure and reaching exact Kraft1; equivalently provide an actual universal gap-parser certificate for the resulting M. This would genuinely settle the original C question positively. Neither a full selector nor an all-order obstruction to every such extension is supplied.

The seed branch fixes r=t=1 and particular later delays. It is not a theorem that every possible completion of C contains these extra words. A no-go for this branch would therefore not prove unrestricted noncompletion. Conversely, the present explicit UD certificate shows that the previously reviewed low-a restrictions alone do not already kill the r=t=1 mixed-length branch.

All calculations and prefix/gap arguments above are written and finite in description but universal in their stated list/gap quantifiers. No program has checked or generated the residual set. This candidate needs separate reconstruction and parent consideration on its pinned bytes before promotion. Its code-theoretic priority and significance relative to older completion techniques remain UNCLEAR; it is not counted as a solved book problem or an independent set of discoveries.
