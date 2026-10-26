# Consolidated seed obstruction: a critical gap forces another length scale

Observed before creation: **2026-10-23T16:33:46-0700 PDT**. MathShor, math-5. **CANDIDATE new all-order mixed-length compatibility result for the accepted seed branch.** No seed words are added here. No execution, finite enumeration, solver, CAS or proof assistant was used.

This is ONE consolidated branch packet, not an incremental sequence of seed additions or another scalar normalization. It rules out completing the actual mixed-length seed by one common remaining word length, and gives an explicit three-way constraint on EVERY finite completion of that seed. It does not exclude arbitrary mixed-length completions of C or even arbitrary multi-length completions of this seed.

## 1. Actual seed and exact theorem

Let

    A=ba, W=ba^2b, P=a^3b,
    V=ba^2ba, Q=ba^2ba^2, Z=a^3bab,
    M_n=C∪{W,V,Q,Z,a^n},          n≥26.

The reviewed construction proves M_n UD but incomplete, uniformly for all n≥26, with unique free-end parses for all cores having at most four a's. The full16-word C remains literal; no claimed completion order bound is inferred from n≥26.

**Theorem.** Any finite UD factor-complete M⊇M_n must contain a unique raw pure-core-five word

    H=b^R a^5 b^T,             R,T≥1.                   (1)

Put g=R+T-1≥1. At least ONE of the following ACTUAL raw words must also lie in M:

    X_45=a^4 b^g a^5 b^beta,            beta≥0;           (2a)
    X_52=b^alpha a^5 b^g a^2,          alpha≥0;          (2b)
    X_55=b^alpha a^5 b^g a^5 b^beta,   alpha,beta≥0.     (2c)

Every one of these lies outside M_n and is strictly longer than H. More exactly their respective lengths are at least

    |H|+3,       |H|+1,       |H|+4.                   (3)

Two additional actual-C collisions show

    T≥2 ⇒ X_45 cannot occur,
    R≥2 ⇒ X_52 cannot occur.                            (4)

Thus when R,T≥2, X_55 is forced, and its delays satisfy

    alpha≥R OR beta≥T,
    |X_55|≥|H|+4+min(R,T).                              (5)

**All-length corollary on the actual constructive branch.** For every n≥26 and every positive N, there is NO finite UD COMPLETE extension of M_n of the form

    M=M_n∪T_N,        T_N⊆{a,b}^N.

This is a new obstruction beyond the old C∪T_N no-go: M_n is already mixed-length, but its remaining completion cannot be one flat length. Arbitrary finite multi-length extensions of M_n remain open. No assumption says every completion of C contains this seed.

## 2. Exact reviewed input and no verdict transfer

Consumed constructive sources:

- `construction-MIXED-LENGTH-UD-SEED-v1.md`, SHA256 `c45ef598f9b7cbf234d6dfc5adad448285b80ff58bf5650bc994948a8ff081df`;
- `construction-MIXED-LENGTH-UD-SEED-pure-power-addendum-v1.md`, SHA256 `9205b212da51dc295e0e6e938ec1d414e5b0297d8dff3b026639970959df0678`.

Their actual separate review is SHA256 `e8e4ce8601967a24351b794cfc3f2d2ef948eef167dfe45b047795bdd4336f92`, and the parent boundary is `shor-mixed-length-parent-v1.md`, SHA256 `f1d49e7b38f94d3b00f4b2b539664f8a8b691f3f80a991a6ccf12f20880b1097`. These support the source seed and raw padding interfaces, not the new theorem here.

Precisely needed: b∈M_n; the displayed W,V,Q,Z and original C; all ≤4-a cores already have a unique free-end parse; and any two different free-end parses can be padded with b to an actual UD contradiction. In a finite complete extension, long b-margins isolate any fixed internal core and force some parse. No Redei/Szabo statement, n-cbc realization converse, old order arithmetic or scientific program is used.

## 3. Why the short-core structure cannot change in a UD extension

No NEW raw word with one through four a's can be adjoined to any UD superset of M_n. Its internal core already has a free-end parse by M_n. If it is a different raw word, pad that parse and the proposed single-word parse to common leading/trailing b-lengths. The resulting raw word has two distinct M-lists. Thus the only ≤4-a words of an actual UD extension are the seed's existing ones.

For a PURE adjacent a-run of length≤4, the only seed words whose internal a-core fits are A,W,P. The multi-b V,Q,Z have positive internal b-gaps and cannot fit adjacent a's. The pure-a word a^n has n≥26 and cannot fit such a short core. At a zero b-gap, the only allowed boundary among A,W,P is

    A→P,

because only A has trailing delay0 and only P has leading delay0. Therefore the unique free-end pure-run parses are

    length1:A;   length2:W;   length3:P;   length4:A,P.  (6)

Their outer-delay pairs are respectively

    (1,0), (1,1), (0,1), (1,1).                        (7)

In particular a^5 has no proper parse into shorter-a codewords.

## 4. The missing five-a core forces H, with both delays positive

Completeness with b-margins longer than the finite maximum word length forces one actual word with internal core a^5, since no proper partition in(6) produces five adjacent a's. Outer b-padding injectivity gives its uniqueness, so it has the form H=b^R a^5 b^T.

If T=0, then

    (H)(a^3b)=(b)^R(a^8b),

a literal ambiguity using original C. This includes R=0; no inverse b-power appears. Hence T≥1.

If R=0, with T≥1 already established, then

    (ba^7)(H)=(ba)(a^11b)(b)^(T-1),

both equal b a^12 b^T with different first codewords. Thus R≥1 as well.

H is not a seed word: C has no pure internal a^5 core, the extra seed words have at most four a's, and a^n has n≥26. It must therefore be a genuinely new word in a completion.

## 5. The critical-gap parse is an all-order mixed-length constraint

Apply completeness to the core

    a^5 b^g a^5,                g=R+T-1.

Use b-margins exceeding the maximum word length of the hypothetical finite M. Then every a-containing factor lies inside the displayed padded core. There are two possibilities.

### No codeword spans the central gap

Each adjacent five-a run would have to use H as a single word: shorter-a words cannot partition it, and a different pure-five codeword violates raw core injectivity. The boundary between H,H requires at least T+R b's, but there are only g=R+T-1. Thus this case is impossible.

### One codeword spans the central gap

At most one codeword can span the same gap in an ordered factorization. Let it cover i≥1 a's at the end of the left run and j≥1 at the start of the right run. Its internal core is exactly a^i b^g a^j; all remaining left/right a's are adjacent prefixes/suffixes of lengths5-i and5-j, between0 and4.

If a nonempty left prefix is present, joining it to the spanning word at gap0 requires the prefix's last trailing delay to be0. By(6)–(7) only the one-a prefix A has this property. Hence either i=5, or i=4 and the spanning word has leading delay0.

If a nonempty right suffix is present, gap0 requires its first leading delay0. Only the three-a suffix P has that property. Hence either j=5, or j=2 and the spanning word has trailing delay0.

The only possible spanning types are therefore

    (i,j)=(4,2),(4,5),(5,2),(5,5),

with the forced zero outer delays just described. This is an exhaustive actual parse classification, not a selected reflection/word ordering or an ansatz about M's word lengths.

## 6. The(4,2) escape is forbidden at EVERY critical gap

The(4,2) type would be the literal word B=a^4 b^g a^2, with both outer delays0.

If g=1, the actual seed relation V=W a and literal C-word a^3ba^2 give

    (W)(B)=(V)(a^3ba^2).

Both equal b a^2 b a^4 b a^2, and the first codewords W,V differ. Thus B cannot belong to a UD extension.

If g≥2, then

    (b)(B)(b)=(A)(P)(b)^(g-2)(W),

both equal b a^4 b^g a^2 b. All powers are nonnegative, and the first codewords b,A differ. This is the proper lower parse of B made possible once its internal gap reaches2. Again B cannot be a raw codeword.

Consequently the spanning word must be one of(2a)–(2c). Their core lengths are g+9,g+7,g+10, while |H|=R+T+5=g+6. This proves(3), including strict growth in EVERY allowed escape.

This is the crucial global interaction: the smallest possible crossing escape is rejected by a seed/C identity at gap1 and by a different actual parse at all larger gaps. No bound or enumeration of g is used.

## 7. The C-dependent boundary exclusions and the self-pair alternative

For X_45=a^4 b^g a^5 b^beta with T≥2, put B0=max(beta,T). Then

    (ba^7)(X_45)(b)^(B0-beta)

and

    (b)(a^11b)(b)^(T-2)(H)(b)^(B0-T)

both equal b a^11 b^g a^5 b^B0, since1+(T-2)+R=g. This violates UD, proving the first part of(4).

For X_52=b^alpha a^5 b^g a^2 with R≥2, put L0=max(alpha,R). Then

    (b)^(L0-alpha)(X_52)(a^11b)

and

    (b)^(L0-R)(H)(b)^(R-2)(ba^13)(b)

both equal b^L0 a^5 b^g a^13 b, since T+(R-2)+1=g. This proves the second part of(4). The subscripts45 and52 name left/right a-run sizes, not physical dimensions or separate targets.

If R,T≥2, only X_55 remains. If its alpha≤R-1 and beta≤T-1, the two actual lists

    (H)(b)^(R-1-alpha)(X_55)(b)^(T-beta),
    (b)^(R-alpha)(X_55)(b)^(T-1-beta)(H)

give the same b^R a^5 b^g a^5 b^g a^5 b^T. Their first codewords differ and all exponents are nonnegative. Thus alpha≥R OR beta≥T, yielding(5). No unconditional infinite-growth iteration is inferred from this alternative.

## 8. No one-flat-length completion of the actual mixed seed

Assume M=M_n∪T_N is finite UD complete with every further word in T_N of length N. Section4 forces H outside M_n, so |H|=N.

Each of the three allowed spanning types is outside M_n as well. X_45 starts with four a's before its first b, a row absent from the seed; X_52 and X_55 have an internal core beginning with five adjacent a's and a positive gap, absent from all seed words. The existing a^n has no b and cannot be any of them. Thus the forced spanning word also lies in T_N and has length N.

But(3) makes that length at least |H|+1=N+1. Contradiction. This proves the corollary for EVERY n≥26 and EVERY positive N, including all possible large admissible pure-a orders. No count of failed finite cases or scalar lower-bound arithmetic settles it.

The result does not iterate automatically over a CHANGED base containing further words. Its proof uses the exact seed's complete≤4-a interface and missing pure-five core. Replacing the base or assuming that an arbitrary mixed completion can be flattened to one remaining length would be an unproved extra theorem.

## 9. Exact remaining scientific obligation

The unrestricted C target remains unresolved. On the sufficient M_n branch, a completion would need genuinely heterogeneous further lengths and an actual coherent choice among the critical-gap escapes, together with all other raw gap conditions. No finite final M or GP/residual certificate is supplied here.

This packet is an all-order obstruction to the natural one-step flat remainder and a concrete mixed-length branching requirement, not a new finite completion or an exhaustive negative answer. Its prior-art novelty is unassessed. It needs its own complete separate reconstruction and parent disposition, even though its seed inputs were previously supported. No program, solver, execution GO or incremental seed mutation is requested.
