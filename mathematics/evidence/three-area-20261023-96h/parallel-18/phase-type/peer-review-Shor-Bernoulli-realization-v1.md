# Independent written reconstruction: finite Shor raw-tail Bernoulli realization

Before-creation clock observed: **2026-10-23T14:37:58-07:00**. Reviewer: `MathResearch96h`, at the parent's bounded peer-review request. PH remains the only owned scientific problem. Complete proof, protocol and selection read; no scientific program, arithmetic replay, word generation, enumeration, CLI or nested agent was used. Only this PHslot receives the review file.

## Pinned three-file packet and verdict

1. `mathematics/evidence/three-area-20261023-96h/parallel-18/shor-completion/proof-BERNOULLI-TAIL-REALIZATION-v1.md`, all161lines, SHA256 **`3918ca67108d0dc98620760209474cc306750110d910dbdb2fd167d7eea48de3`**.
2. Adjacent `raw-realization-protocol-v1.md`, all144lines, SHA256 **`544f547ba826076f452d3f478bf4585ecfe9e2da0f2d643f03e79732e568e578`**.
3. Adjacent `selection-v1.md`, all60lines, SHA256 **`d7ac86b0c69dc96b82361d16c17145593e47b6c3d8dce7c99a539bf34be00ba3`**.

**Verdict: 0 FATAL /0 MAJOR /0 MINOR. No substantive defect found in the all-n raw-set construction or the explicitly non-UD control at the stated protocol boundary.** This is construction/control evidence, not a finite completion, noncompletion, new necessary order bound or priority result.

## 1. Literal Shor polynomial and positive remainder

From the exact four rows in the selection, the one-b exponents i+j are

    0,1,7,13,14;
    3,5,7,9;
    8,10,12,14;
    11,12,13.

Thus the displayed A polynomial, including multiplicities2 at7,12,13,14, has coefficient sum16. Multiplication by1-x gives1-(1-x)A=x2H with

    H=1-x+x2-x3+x4-2x5+x6-x10+2x13.

The regrouping(1-x)(1+x2+x4-x5)+x10(2x3-1) expands exactly to it.

On[0,4/5], the bracket is at least1 because x2>=0 and x4-x5=x4(1-x)>=0. Hence H>=1-x-x10>=1/5-(4/5)10>9/100. On[4/5,1], the first summand is nonnegative and the final factor2x3-1 is at least3/125, yielding H>(1/10)(3/125)=3/1250>1/500. Both exact inequalities for(4/5)10 follow from the stated integers1048576 and9765625; no point sampling is used.

Direct coefficient sums give H(1)1 and H'(1)14. All signs and the high-order coefficient2x13 are necessary and correctly retained.

## 2. Uniform degree-elevation positivity

The binomial identity

    binomial(d-j,k-j)/binomial(d,k)=(k)_j/(d)_j

holds for j<=k, and the numerator is zero for j>k. At d>=13 all denominators for j<=13 are nonzero. The falling-factorial ratio is the all-in-subset probability for sampling without replacement;(k/d)j is its with-replacement counterpart.

Conditioning the with-replacement sample on distinct draws produces the without-replacement law. For any event E, the difference between its conditional and unconditional probabilities is at most the probability of the conditioning event's complement. The collision union bound is binomial(j,2)/d. This proves the claimed error even for k<j; j0/1 contribute no error.

For the nonzero H coefficients, the exact absolute weighted sum is

    1+3+6+20+15+45+156=246.

Therefore b_(d,k)>=H(k/d)-246/d>=1/500-1/1000=1/1000 whenever d>=246000. All g_(d,k) are integers, so every such coefficient is strictly positive, uniformly over ALL k0,...,d and all d in the range. No positivity theorem or enumerated finite range is imported.

## 3. Actual finite raw words and all Bernoulli identities

For n=d+2, substituting x=X/(X+Y) into1-(1-x)A=x2H and multiplying by(X+Y)n gives exactly

    X2 H_d(X,Y)+sum_s A_s Xs Y(X+Y)^(n-s-1)=(X+Y)n.

Every exponent is nonnegative because n is far larger than15, and every coefficient in the second term is nonnegative. Thus the integer tail coefficient G_(n,k) is between0 and binomial(n,k), the literal count of available length-n binary words of that composition. Selecting that many distinct words independently by composition gives a finite SET, not a multiset or a formal signed polynomial. Since n>15, none duplicates a literal Shor word.

For any x in[0,1], substitution Xx,Y1-x makes the second term exactly(1-x)A(x), while each selected tail word has the prescribed monomial mass. Hence the all-Bernoulli equality holds including both endpoints; it is not just the uniform x1/2 Kraft sum.

The pure-a coefficient is g_(d,d)=sum h_j=1, so a^n is selected exactly once and no other pure-a word occurs. The one-b tail coefficient is

    g_(d,d-1)=sum_j h_j(d-j)=dH(1)-H'(1)=n-16.

The16distinct literal one-b Shor words then give exactly n one-b words. These properties do not make the raw set a code or a cyclic factorization.

## 4. Exact ambiguity and why it does not settle UD

The a-count2 coefficient is g_(d,0)=h0=1. Choosing that tail word as

    W_n=(ba)(ba)b^(n-4)

gives length n, exactly2a's and n-2b's, as required. The single-codeword list[W_n] and the list[ba,ba,b,...,b] with n-4 copies of b concatenate to the same word. Both b and ba are literal words of the frozen C, so this is an actual ambiguity for every n>=246002, not a residue or Parikh-vector collision.

The lexicographic choices in the other compositions are finite exact definitions; no exponentially large list is claimed generated. This chosen family is non-UD, but it does NOT show every possible composition-respecting selector is ambiguous. The proof explicitly preserves that distinction.

## 5. Raw residual protocol: sufficiency and completeness boundary

The protocol's A–D conditions are actual raw-word conditions: literal Shor binding; all initial proper-prefix residuals; full prefix-comparison closure in a finite residual set S excluding epsilon; and exact integer uniform Kraft equality. Prefix cancellation starting from the first unequal codewords of any hypothetical two-list collision would keep a residual in S until it becomes empty, impossible. Thus B–C prove UD without relying on a producer traversal claim.

UD makes the weighted sum over all products equal sum_t f^t, where f=sum_x in M 2^-|x|. At f1 this diverges. If a word of length h were absent as a factor, the disjoint h-block avoidance bound gives total normalized mass at most h2h, a contradiction. Hence the protocol gives the book's factor-completeness quantifier, not merely maximality of a residue code.

I also reconstructed the protocol's necessity, so its positive-witness language does not silently exclude a legitimate finite completion: reachable Sardinas–Patterson residuals are proper suffixes of finite M words and form a finite epsilon-free closure when M is UD. Counting t-word products proves f<=1. If a complete finite UD code had f<1, trimming a factor occurrence to its endpoint codewords gives an injection into pairs of end lengths< D and a product z, bounding the infinite total normalized mass of all binary words by D2·2^(2D-2)/(1-f), impossible. Thus f1 is necessary.

The auxiliary M0 raw-control construction is valid too: its four-symbol substituted suffix code is UD because its underlying K is a prefix code; the binary Kraft sum is1. It has pure-a word a2 and one-b residues00,11, yet aba is not in M0* since no M0word prefixes aba. This correctly demonstrates why canonical residue presence is not literal M* membership.

## 6. Exact remaining sufficient selector obligation

A sufficient positive route is still to find SOME integer n>=246002 and choose, for EACH composition k, exactly G_(n,k) distinct literal length-n tail words so that M=C union T_n admits a finite residual set S satisfying the protocol's full coverage/closure and epsilon exclusion. The raw tails already give exact Kraft equality, literal inclusion, pure-a order and one-b cardinality. Such an S would add the missing UD condition; A–D would then prove a genuine finite complete extension.

No such selector or residual certificate is supplied by the reviewed packet. Failure of this homogeneous-tail ansatz would not exclude arbitrary finite completions with several additional lengths; the selection explicitly keeps that unrestricted target. The number246002 is a coarse construction-positivity threshold and NOT a necessary lower bound on a true completion, an improvement of19800 or a new divisibility restriction. Neither all-Bernoulli normalization nor the intentional ambiguity is misreported as a solution.

## Scope, trust and status

The reviewed construction and protocol are self-contained polynomial/counting/probability/prefix-cancellation arguments. They do not use an unauthenticated Szabo proof, an n-cbc realization converse or imported positivity theorem. Classical priority and the full Shor existence question remain unresolved. This is ordinary in-harness written checking with shared supplied proofs, not formal/kernel, human, blind or cross-vendor acceptance. The two parent errata remain mandatory. No P24 work or scientific execution is authorized by completing this review; I return to the owned PH problem.
