# A forced mixed-length growth step closes EVERY homogeneous-tail selector

Observed before creation: **2026-10-23T15:52:44-0700 PDT**. MathShor, math-5. **CANDIDATE new consequence requiring its own reconstruction and parent disposition.** No execution, finite failed search, order enumeration, solver, compilation, symbolic program or proof assistant was used.

This addresses the actual RAW-SELECTOR route rather than cataloguing another layer. It proves that the ENTIRE concrete homogeneous-tail family offered in the Bernoulli construction cannot realize a completion, for ANY tail length. It also gives a word-length interaction required in EVERY mixed-length completion. It does **not** prove unrestricted noncompletion or a new pure-a order bound.

## 1. Exact result

For any hypothetical finite UD complete M containing the literal Shor16 code C, let its unique two-a word be

    W=b^r a^2 b^t,             r,t≥1,
    v=r+t,                    g=v-1≥1.

Then M has an actual four-a word

    Q=b^alpha a^2 b^g a^2 b^beta,        alpha,beta≥0,   (1)

whose delays necessarily satisfy

    alpha≥r  OR  beta≥t.                               (2)

Consequently

    |Q|≥|W|+1+min(r,t)≥|W|+2.                          (3)

The literal Shor words also imply

    r≥2 ⇒ beta≥1,         t≥2 ⇒ alpha≥1.               (4)

In particular if r,t≥2, (3) strengthens to |Q|≥|W|+2+min(r,t).

**All-order route closure.** There is NO finite UD complete extension of C of the form

    M=C∪T_N,       T_N⊆{a,b}^N,

for ANY positive integer N. This forbids one common ADDED length, not general mixed-length extensions. No reduction of an arbitrary completion to this ansatz is claimed.

**Bernoulli consequence.** For every n≥246002, EVERY composition-respecting selector in `proof-BERNOULLI-TAIL-REALIZATION-v1.md` is non-UD. The earlier explicit ambiguous choice was only a control; this new consequence closes the entire selector family. The raw mass construction remains correct.

## 2. Declared input boundary

The source input is the unrestricted raw two-/three-a structure in

    proof-RAW-TWO-THREE-A-LAYERS-v1.md
    SHA256 0614a8e399f789397cdfaf4c6c6adb3d514f884264f6bc5fbd9e22cd71465ba2.

It was separately reconstructed and supported at the in-harness written-check level by `shor-raw-structure-parent-v1.md` (parent record SHA256 44cd995080ce6b66e3d31c8a6c7d4c58cbebbd3039c375c22f118514b1533f9c). That record does not automatically accept the new deductions here.

Precisely consumed: M contains b, its only one-a word is A=ba; W above is its unique two-a word with r,t≥1; its only three-a words are

    P=a^3b,
    U_s=b^(alpha_s) a b^s a^2 b^(beta_s),    1≤s<r,
    V_s=b^(gamma_s) a^2 b^s a b^(delta_s),   1≤s≤t.

Also consumed is the actual b-padding forcing principle: for any core beginning/ending in a, completeness and margins longer than the finite maximum word length force one raw codeword of that core if no proper lower-a partition can parse it. Boundary gaps between words u,w require at least beta_u+alpha_w b's. This is the reviewed GP principle, not a residue-realization converse.

No Rédei/Szabó import, 1320/19800 arithmetic, homogeneous endpoint restriction or new execution is a premise.

## 3. Why Q is forced: exhaust every proper partition

Consider the actual core

    a^2 b^g a^2,              g=r+t-1.

A product realizing this core with free outer b-padding could properly partition its four a-positions only with one of the seven compositions of4 from1,2,3.

- **1+1+1+1:** adjacent a's in either pair cannot both be separate ba words.
- **2+1+1:** W could cover the first pair, but the final adjacent pair cannot split into two ba words.
- **1+1+2:** the initial adjacent pair cannot split into two ba words.
- **1+2+1:** the middle two a's have positive intervening gap g, whereas W's two a's are adjacent.
- **2+2:** W,W requires the middle boundary gap t+r=v. The actual gap is v-1.
- **3+1:** the initial three-a core would have gaps(0,g), so it could only be V_g if g≤t. Even when that happens (r=1), the last boundary to ba has actual gap0 and would require delta_g+1≥1. Hence it still fails.
- **1+3:** the final triple has gaps(g,0), so it could only be U_g if g<r. But g=r+t-1≥r for t≥1; no such U_g exists.

Thus no proper partition is possible. P=a^3b cannot cover either triple since their positive middle gap prevents three adjacent a's. By finite-completion padding, a single codeword with exactly that core is forced, namely Q in(1). The reviewed four-a table yields the same conclusion: its(0,j,0) row forces j=v-1, because j<v and j≥r makes the alpha_j=0 exception unavailable. The direct seven-case proof above makes the new use explicit rather than treating a filename as proof.

## 4. Mixed-length compatibility from an actual six-a ambiguity

Suppose, contrary to(2), that alpha≤r-1 AND beta≤t-1. Then the two lists

    (W)(b)^(r-1-alpha)(Q)(b)^(t-beta)

and

    (b)^(r-alpha)(Q)(b)^(t-1-beta)(W)

concatenate to the SAME raw word

    b^r a^2 b^g a^2 b^g a^2 b^t.                       (5)

All displayed exponents are nonnegative. The second list starts with at least one copy of b, while the first starts with W≠b, so the lists are genuinely different.

For the first list, the gap after W is t+(r-1-alpha)+alpha=g; for the second, the later gap is beta+(t-1-beta)+r=g. Both outer b-runs and both inner g-runs therefore agree exactly. This is a literal UD contradiction, not an unordered Parikh match or a finite test.

Hence(2) holds. Since the core of Q has length4+g=v+3 and alpha+beta≥min(r,t),

    |Q|=v+3+alpha+beta≥v+3+min(r,t)
        =|W|+1+min(r,t),

proving(3) for every finite mixed-length completion.

## 5. Extra endpoint restrictions from the actual C

These are not required for homogeneous route closure, but show that the compatibility really retains the Shor words.

If r≥2 and beta=0, put L=max(alpha,r). Then

    (b)^(L-alpha)(Q)(a^11b)

and

    (b)^(L-r)(W)(b)^(r-2)(ba^13)(b)

both equal b^L a^2 b^g a^13 b. The middle gap on the second side is t+(r-2)+1=g. All exponents are nonnegative, and the lists contain different actual a-containing words. Thus beta≥1.

If t≥2 and alpha=0, put R=max(beta,t). Then

    (ba)(Q)(b)^(R-beta)

and

    (b)(a^3b)(b)^(t-2)(W)(b)^(R-t)

both equal b a^3 b^g a^2 b^R, again with distinct lists. The second middle gap is1+(t-2)+r=g. Thus alpha≥1.

When r,t≥2, both delays are positive and(2) forces their sum at least min(r,t)+1, giving the stated stronger length comparison. No claim is made at a boundary where the proof would use b^(-1).

## 6. Every common-added-length extension is impossible

Suppose M=C∪T_N with every additional word length N. The literal Shor list contains **no two-a word and no four-a word**: its total a-counts are0,1,3,5,7,8,9,10,11,12,13,14, with the stated multiplicities.

Therefore both W and the forced Q must be in T_N, so

    |W|=|Q|=N.

This contradicts(3), which gives |Q|≥|W|+2. The conclusion holds for every positive N; there is no finite-order cutoff, arithmetic enumeration, assumption that N is the smallest admissible a-order, or hypothesis that C itself is prefix.

This does NOT rule out a completion containing words of several additional lengths. Indeed the conclusion identifies exactly why a genuine RAW-SELECTOR must use mixed lengths: its unique two-a word must be followed by an actual longer four-a word satisfying(2). Merely choosing a different point in a homogeneous coefficient table cannot cure the obstruction.

## 7. Update to the prior constructive route, without rewriting history

The all-Bernoulli raw construction produces literal finite supersets C∪T_n and exact binary Kraft equality. Suppose ANY of its selectors were UD. The proved raw certificate/counting implication UD+Kraft1⇒factor completeness would make it a finite completion. Section6 forbids this. Hence every such selector is non-UD, not only the explicitly chosen W_n=(ba)^2 b^(n-4).

The older source documents remain unchanged. Their statements that a hypothetical successful homogeneous selector would suffice are logically valid conditional statements, but **that selector route is now closed by this candidate consequence**. The old endpoint restrictions remain valid necessary conditions on an empty ansatz if the present proof is accepted; they must not be counted as a live successful construction family or retroactively relabelled a general impossibility.

`completion-shape-v1.md` must therefore be read with this numbered continuation before using its section9 homogeneous selector as a proposed live next attack. RAW-SELECTOR itself is unchanged and unrestricted: supply actual finite MIXED-LENGTH raw M with a UD/completeness certificate, or prove an all-order obstruction for every such finite M. Neither is supplied here.

## 8. Review and significance boundary

The relative growth(3), six-a compatibility(2) and all-common-added-length no-go are new deductions from the recorded source packet and require their own separate reconstruction/parent disposition. They do not inherit acceptance merely from the reviewed four-a table. No novelty/priority comparison of this homogeneous-completion obstruction has yet been completed; its immediate value is decisively eliminating the actual proposed RAW-SELECTOR family before exponential generation or any GO.

The unrestricted Shor completion question remains unresolved. There is no new pure-a order restriction and no finite failed-search inference. Further science must handle actual mixed-length compatibility or an actual decodable finite realization, not another homogeneous attempt or an endless fixed-layer count.
