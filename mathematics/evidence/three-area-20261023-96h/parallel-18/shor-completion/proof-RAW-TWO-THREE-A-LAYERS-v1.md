# The first missing raw layers of a hypothetical Shor completion are forced

Observed before creation: **2026-10-23T14:40:09-0700 PDT**. Owner MathShor, math-5. Status: **CANDIDATE all-order structural restriction on actual raw completions**, with a scoped consequence for the homogeneous-tail sufficient ansatz. This is not a new order bound, finite witness, noncompletion theorem, or priority claim. No mathematical program, enumeration, solver or executable replay was used.

Unlike a residue-only restriction or another scalar normalization, the result specifies **every actual word with two or three occurrences of a** that a finite UD complete extension can contain. It closes the first nontrivial raw-tail selection layers left open by the Bernoulli construction; all higher layers and existence remain unresolved.

## 1. Main statement: arbitrary finite complete extensions, not an ansatz

Let M be any hypothetical finite UD complete code containing the literal Shor C, with no restriction on its other words, lengths or number of b's. Then there are integers r,t≥1 such that:

**(L1)** Its only word with no a is b. Its only word with one a is ba.

**(L2)** It has exactly one word with two a's, namely

    W=b^r a^2 b^t.                                      (1)

In particular W is an actual new raw codeword, not merely a factor, a residue point or an element of M*.

**(L3)** It has exactly r+t words with three a's, and the COMPLETE list is

    a^3 b,
    U_s=b^(alpha_s) a b^s a^2 b^(beta_s),     1≤s≤r-1,
    V_s=b^(gamma_s) a^2 b^s a b^(delta_s),    1≤s≤t,       (2)

with one actual word for each indicated internal core. All alpha_s,beta_s,gamma_s,delta_s are nonnegative integers, and there are no other three-a words, in particular none with three separated a's.

The literal Shor words further force

    beta_s≥1                         for every 1≤s≤r-1;
    alpha_1≥1                        if r≥2;
    gamma_s≥1                        for every 2≤s≤t.    (3)

A range can be empty. This is a statement for all finite raw completions, not only completions whose extra words have one common length.

## 2. Exact mass identity and the layer counts

We first give the probability identity used in the count argument, rather than treating an unproved criterion as a code-theoretic import.

For 0<x<1, let mu_x(w)=x^(|w|_a)(1-x)^(|w|_b), and put f=Σ_(w∈M)mu_x(w). If D is the maximum word length, UD implies that distinct lists of exactly q codewords have distinct concatenations, of lengths between q and qD. The total mu_x-mass of all binary words of any fixed length is 1. Therefore

    f^q≤qD-q+1,

and exponential growth would contradict this if f>1. Thus f≤1.

If M is complete and f<1, then UD gives

    Σ_(z∈M*)mu_x(z)=Σ_(q≥0)f^q=1/(1-f)<∞.

Every binary word w is a factor of some product. Trim complete codewords before and after the occurrence to obtain z=u w v∈M* with |u|,|v|≤D-1. Let c=min(x,1-x)>0. For each z and pair of end lengths there is at most one w, and

    mu_x(w)≤c^(-2D+2)mu_x(z).

Summing over at most D^2 end-length pairs would make the total mass of all binary words finite. But each length contributes 1, a contradiction. Hence f=1 for every x∈(0,1). Since M is finite, this is a polynomial identity, also valid by coefficient comparison at x=0.

A pure-b codeword b^m with m≠1 would already conflict with the codeword b∈C; thus the zero-a layer is just b. For j≥1 let

    A_j(y)=Σ_(w∈M, |w|_a=j) y^(|w|_b),
    N_j=A_j(1).

The mass identity reads

    1=(1-x)+Σ_(j≥1)x^j A_j(1-x).                       (4)

Its coefficient of x gives N_1=1. Since ba∈C, A_1(y)=y. The coefficient of x^2 then gives N_2=1. Once that unique two-a word has v b's, A_2(y)=y^v; the coefficient of x^3 gives

    N_3=v.                                             (5)

Indeed the b and ba terms sum to 1-x^2, while x^2(1-x)^v=x^2-vx^3+terms of degree at least4. These are exact polynomial coefficients, not numerical derivative samples.

## 3. Two elementary raw-word principles

### Outer-b padding injectivity

If two different codewords have the same internal core U starting and ending with a,

    b^i U b^j,       b^(i') U b^(j'),

pad their leading and trailing b's to common maxima I=max(i,i'), J=max(j,j'). Since b itself is a codeword,

    b^(I-i) (b^i U b^j) b^(J-j)
      =b^(I-i') (b^(i') U b^(j')) b^(J-j')

gives two distinct lists of M-words with the same concatenation. The lists differ in their unique non-pure-b codeword. Thus **at most one codeword can have any fixed internal a-core**. This uses actual raw words and not cancellation inside M*.

### Long b-padding exposes a necessary small-a codeword

For any fixed word U starting and ending with a, completeness makes

    b^(2D) U b^(2D)

a factor of some product of M-words. Every codeword containing an a of U lies wholly within this displayed factor, because its length is at most D and both outside margins have length2D. Therefore its number and arrangement of a's come only from U. If no decomposition of U's a-positions into smaller-a codewords is possible, one codeword must contain all those a's, with exactly the internal core U and some outer b-powers. Zero-a words between constituents can only be b.

No bounded failed search or normal-form assumption is used in this forcing argument.

## 4. The unique two-a word and why both outer delays are positive

Apply the padding principle to U=a^2. If the adjacent two a's lay in distinct codewords, the codeword containing the second a would have one a and hence be ba. It would require a b immediately before that a, while that position is the first a. Impossible. Thus a single two-a codeword contains both a's, and it has form b^r a^2 b^t. Since N_2=1, it is the unique such codeword.

If r=t=0, then a^2∈M and the existing word a^8b∈C has the distinct factorization (a^2)^4(b), violating UD.

If r=0 and t≥1, compare the two actual lists

    (ba)(a^2 b^t)
       =(b)(a^3 b)(b)^(t-1).

Both concatenate to b a^3 b^t; their first codewords ba and b differ. Hence r cannot be zero.

If t=0 and r≥1, compare

    (b^r a^2)(a^11 b)
       =(b)^(r-1)(ba^13)(b).

Both concatenate to b^r a^13 b and have different non-b codewords. Thus t cannot be zero. This proves r,t≥1. In (5), v=r+t, establishing the required total N_3.

## 5. All three-a cores, counted exactly

The codeword a^3b is already in C. It is the only possible raw codeword with internal core a^3 by outer-b padding injectivity.

For each 1≤s≤r-1, consider the internal core

    a b^s a^2.

In a padded realization, three one-a words ba cannot cover the last adjacent a-pair. A two-a word must cover exactly that adjacent last pair; the only candidate is W=b^r a^2 b^t, but it would require at least r b's in the preceding internal gap, whereas the actual gap has s<r. There is no other 1+2 or 2+1 partition of these a-positions consistent with W's adjacent a-pair. Thus a single three-a codeword with this core is forced. Denote it U_s. Outer padding injectivity makes it unique.

Similarly for each 1≤s≤t, consider

    a^2 b^s a.

A decomposition into W followed by ba requires at least t+1 intervening b's: t trailing b's from W and one leading b from ba. The actual gap has s≤t. Three one-a words cannot cover the initial adjacent pair, and the reversed 1+2 partition cannot match W's adjacent a-pair. Hence a single three-a word V_s with this internal core is forced and unique.

All these cores are distinct. Together with a^3b they require exactly

    1+(r-1)+t=r+t

three-a words. Equation (5) permits exactly that many. They therefore exhaust the entire three-a layer, proving (2). In particular a different core with three separated a's cannot be present, even if it would by itself be compatible with the smaller layers.

## 6. Exact outer-delay restrictions from the actual Shor words

These restrictions are again actual UD collisions, not Parikh identities.

**Every beta_s≥1.** Suppose U_s=b^alpha a b^s a^2 (beta_s=0), s≥1. Then

    (b)(U_s)(a^11b)
      =(b)^alpha (ba)(b)^(s-1)(ba^13)(b),               (6)

both equal b^(alpha+1) a b^s a^13 b. The two lists have different non-b codewords, contradicting UD.

**alpha_1≥1 when r≥2.** If U_1=a b a^2 b^beta, then

    (ba^7)(U_1)=(b)(a^8ba^2)(b)^beta,                  (7)

both equal b a^8 b a^2 b^beta. Every displayed fixed word is in the literal C, so this is an actual ambiguity. Thus alpha_1 is positive.

**gamma_s≥1 for s≥2.** If V_s=a^2 b^s a b^delta, then

    (ba)(V_s)
       =(b)(a^3b)(b)^(s-2)(ba)(b)^delta,               (8)

both equal b a^3 b^s a b^delta. Thus gamma_s cannot be zero for these s. No assertion gamma_1≥1 is made; (8) genuinely requires s≥2.

All exponents in (6)–(8) are nonnegative at the stated boundaries. The proof does not silently use an inverse power, a fictitious reflection/word, or a failed selector as evidence of impossibility.

## 7. Consequence for the explicit Bernoulli-tail construction

In the **sufficient ansatz only** of `proof-BERNOULLI-TAIL-REALIZATION-v1.md`, M=C∪T_n and every extra word has length n. Since C has no two-a word, (1) must be in the tail and therefore

    r+t=n-2.                                           (9)

C's only three-a word is a^3b, so every U_s,V_s must also be a tail word. Their remaining choices are only outer delays:

    alpha_s+beta_s=n-3-s     (1≤s≤r-1),
    gamma_s+delta_s=n-3-s    (1≤s≤t),                    (10)

subject to (3). Thus the formerly arbitrary choice among binom(n,3) raw three-a words reduces to **exactly one word for each displayed core**, with the finite outer-delay choices in (10). This is an entire raw composition layer classified, not just one deliberately bad selector rejected.

For n≥5 this also excludes r=1 in that ansatz: then t=n-3≥2, and at s=t the second equation of (10) forces gamma_t+delta_t=r-1=0, contrary to gamma_t≥1. Hence a successful homogeneous-tail selector in the present large-n range must have

    r≥2,       t≥1,       r+t=n-2.

This last inequality is **not** asserted for arbitrary completions with mixed additional word lengths. The unrestricted structural conclusions are exactly sections1–6.

## 8. Remaining exact obligation, trust and significance

The raw tail selector has not been found. Even satisfying the complete two-/three-a layer forms and the extra endpoint inequalities does not prove that later layers can be filled with a closed nonempty Sardinas–Patterson residual set. Conversely, inability to fill this homogeneous-tail ansatz would not rule out general finite completion with mixed word lengths.

A consequential next step must handle an actual higher-layer compatibility or produce a finite decodable selector; it must not count (9), a mass identity or an acceptable order as a completion. No new numerical n restriction is claimed here. The original all-order existence question remains unresolved.

The argument's inputs are only finiteness, UD, the book's factor-completeness quantifier, and the listed actual Shor words. It does not import the unauthenticated Szabó2006 proof, the unread Rédei monograph proof, a cyclic-factorization converse, or a prefix/suffix ansatz. Its exact raw-layer application has not been compared with all older code-theoretic literature, so novelty and significance remain UNCLEAR even if the written proof survives reconstruction. Parent and separate in-harness review on these pinned bytes remain required. No scientific execution is requested.
