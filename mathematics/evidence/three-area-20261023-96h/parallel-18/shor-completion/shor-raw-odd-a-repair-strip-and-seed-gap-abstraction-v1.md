# Shor — every finite RAW completion needs an odd-a repair word in a bounded strip

Owner MathShor-2. Actual `/bin/date` before composing: **Mon Oct 26 05:41:57 PDT 2026** (earlier observation bound). WRITTEN/unreviewed. Exact symbolic fractions/integer coefficients only. No scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent or new GO.

This is a Shor-specific necessary theorem for the ORIGINAL finite RAW completion problem, **independent of I3/I4/I5**. It follows from the finite-code Bernoulli identity and literal UD, not signed-factor existence or a residue ansatz. It leaves all b-counts, delays, maximum lengths and orders unbounded. No actual completion or all-order contradiction is supplied.

## 1. A direct finite-code coefficient identity

Suppose M is a finite RAW UD factor-complete code containing the literal16-word C. It contains exactly one pure-a word a^n and no pure-b word except b. The elementary finite-code Bernoulli argument is supplied in the raw signed packet and in the self-contained sufficiency packet: for symbolic0<z<1,

    sum_(w in M) z^(|w|_a)(1−z)^(|w|_b)=1.

Let Z_k(z)=sum_(w in M, |w|_b=k) z^(|w|_a), a finite polynomial with nonnegative integer coefficients. Thus Z_0=z^n, and for the finite maximum b-count D,

    z^n+(1−z)Z_1+sum_(k=2)^D (1−z)^k Z_k=1.

This equality on an open real interval is a polynomial identity. Set G_n=1+...+z^(n−1). Dividing once and rearranging gives the EXACT FINITE identity

    H(z):=sum_(k=2)^D (1−z)^(k−2) Z_k(z),
    Z_1(z)=G_n(z)−(1−z)H(z).                            (RAW)

The sixteen Shor one-b words all have at most14 occurrences of a. Summing coefficients of RAW through degree14 gives

    [z^14]H=min(15,n)−sum_(d=0)^14[z^d]Z_1 <= −1.         (NEG)

This H is defined directly from ACTUAL raw words. No Reutenauer factor or raw-to-residue injectivity is needed.

## 2. Forced repair strip, with ALL b-counts retained

Expand each finite term of H. A raw word having d occurrences of a and k occurrences of b contributes

    (−1)^j * binom(k−2,j),  j=14−d,

to [z^14]H when0<=j<=k−2. If every nonzero contribution were nonnegative, NEG would be impossible. Hence at least ONE ACTUAL codeword w of M has

    d=|w|_a odd,  1<=d<=13,
    k=|w|_b >=16−d.                                     (STRIP)

In particular k>=3 and |w|=d+k>=16. It is not one of the sixteen original one-b words. This does NOT bound k from above; arbitrarily long b-delays and codeword lengths remain allowed.

There is no d=0 exception: the only pure-b word of M is b, and pure-b words with k>=2 are forbidden by UD. The parity assertion comes from14−d being odd, not a numerical trial or exhaustive word search.

## 3. Literal b-boundary hardness and removal of d=1

Define a word w outside C to be *C-b-boundary-completable* if b^r w b^s belongs to C* for SOME nonnegative integers r,s. Any NEW codeword w of an extension M containing C must FAIL that property. Otherwise the raw word b^r w b^s has one M-parse using the new codeword w and another using C alone. Those lists are different because w is not in C, contradicting UD. This is an actual raw ambiguity, not formal cancellation of powers.

Every word with exactly ONE a is C-b-boundary-completable: C contains ba and b. After adding enough leading b's, parse its a using ba and parse every remaining b individually. Therefore the forced word in STRIP cannot have d=1.

**Unconditional repair-word theorem.** Every hypothetical finite RAW complete UD extension contains a NEW word w that is NOT C-b-boundary-completable and satisfies

    |w|_a in {3,5,7,9,11,13},
    |w|_b >=16−|w|_a.

This is one necessary repair word, not a claim that only these arities need consideration in the full completion. Higher-a words may also be present and affect every global raw compatibility constraint.

## 4. A finite seed-ambiguity abstraction, not a general delay truncation

Write the maximal a-runs of w as

    b^alpha a^(r1) b^(g1) a^(r2) ... b^(g_(t−1)) a^(rt) b^beta,

with r_i>0,g_i>0 and sum r_i=d<=13. C-b-boundary-completability depends ONLY on:

- the finite composition(r1,...,rt) of d;
- for each internal b-gap, whether g_i=1 or g_i>=2.

It does NOT depend on alpha,beta or the precise value of a g_i>=2.

*Proof.* Leading/trailing b counts can always be increased by the allowed padding and standalone b codewords, so they give no additional obstruction to existence of a C-parse. Every C-word has exactly ONE b. At an internal run of at least two b's, the first and last b may belong to adjacent a-containing C-words, but every further interior b must be a standalone b codeword. Deleting such interior standalone b's reduces the gap to two; inserting them recovers every larger gap. A one-b gap may instead be crossed by a C-word with positive a-runs on both sides, so it must remain a separate category. This proves the exact abstraction for C-boundary tests. ∎

Consequently the forced word has a shape in a FINITE family indexed by those compositions and binary gap labels. No enumeration of that family has been executed or claimed complete here. Its raw lifts still have unbounded gaps and endpoint delays and must satisfy STRIP plus ALL M-compatibility/completeness conditions.

Crucially, this is a quotient of **ambiguity with the FIXED seed C only**. It is NOT valid to collapse gaps in an unknown completion whose added words may contain many b's. It does not supply raw STAB, finite decision of the original question, or a realization of an abstract shape.

## 5. Two exact shape consequences, not a case census

If every a-run of w had length1, enough leading b-padding would let ba consume each a, with standalone b's filling surplus gaps. So the forced w must contain aa as a factor.

If w has only ONE a-run, its odd d must be5 or9: the other possible values1,3,7,11,13 are already boundary-completable by ba,a^3b,ba^7,a^11b,ba^13 respectively. Thus the forced repair is either a one-run5/9 word or a genuinely multi-run word with some adjacent a's. No exclusion or construction of those remaining shapes is claimed.

## 6. Original residual and next mathematical move

The raw necessary strip comes from ACTUAL finite completeness, so it does not depend on the signed-factor converse or on guessing a small modulus. It creates a bounded-a interface for at least one indispensable new codeword while honestly retaining arbitrary b-gaps/delays and all other codewords.

A useful next proof would show that every RAW lift in this necessary seed-incompletable shape family conflicts with the entire sixteen-word seed or forces another incompatible repair. A useful positive result would supply actual finite compatible words and prove the all-gap GP/Kraft/UD conditions. Merely enumerating shapes, finding one C-compatible word, or meeting STRIP is not a completion and will not be promoted to one.

All earlier FACT/three-mate/rawPR/isolated/higher-gap/heterogeneous-delay/STAB gaps remain, except that the present necessary repair word is now explicit in its quantified scope. I3/I4/I5 retain their named boundaries; H* is FALSE/WITHDRAWN. Original Shor completion is **NOT_PROVED** either way.

Own permanent v109-A exactness MAJOR and all older findings remain. No source/shared/frozen edit, git/deletion/publication, scientific GO or stronger formal/kernel/human/family/executable/novelty acceptance. Original cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 unchanged; no early final park.
