# Finite raw-word Bernoulli saturation exists; UD is the remaining realization condition

Observed before creation: **2026-10-23T14:26:25-0700 PDT**. Status: **CANDIDATE written construction / explicitly non-UD positive control**, not a Shor completion, noncompletion theorem, new necessary order bound, or novelty claim. No program, arithmetic replay, enumeration, compilation or solver was run.

This resumes the raw-word realization obligation after the bounded Olson peer review. It is not another necessary-condition list: it constructs actual finite raw supersets satisfying **all positive Bernoulli Kraft equalities at once**, with the exact Shor words, a unique prescribed pure-a word and the required number of one-b words. An explicit uniformly ambiguous choice shows why that still does not answer the code question. A different choice preserving UD would be a genuine sufficient route to a positive answer; no such choice is supplied here.

## 1. Exact statement

For every integer n≥246002 there is a finite set M_n of nonempty binary words such that:

1. M_n contains the literal sixteen-word Shor code C.
2. Every additional word has length exactly n.
3. Its only pure-a word is a^n, and it has exactly n words containing exactly one b.
4. For **every** real x∈[0,1],

       Σ_(w∈M_n) x^(|w|_a) (1-x)^(|w|_b) = 1.

5. M_n can be chosen by an explicit finite lexicographic rule so that it is **not UD**, with a displayed ambiguity using only b and ba from C.

Thus finiteness, literal inclusion, prescribed large a-order, the one-b cardinality and every Bernoulli mass identity are simultaneously realizable as raw sets. They do not supply the absent UD condition. The threshold is only a coarse bound ensuring coefficient positivity in this raw-set construction; it is **not a lower bound on any true completion**. The theorem applies in particular to all sufficiently large orders satisfying the inherited 1320-divisibility/Rédei predicate, without asserting any of those orders actually supports a code.

## 2. Exact Parikh polynomial and a uniform positive remainder

Write A(x)=Σ_(a^i b a^j∈C) x^(i+j). From the literal four rows,

    A(x)=1+x+x^3+x^5+2x^7+x^8+x^9+x^10+x^11
            +2x^12+2x^13+2x^14.

This polynomial has coefficient sum sixteen. Direct symbolic multiplication gives

    1-(1-x)A(x)=x^2 H(x),                              (1)

where

    H(x)=1-x+x^2-x^3+x^4-2x^5+x^6-x^10+2x^13.          (2)

A useful exact regrouping is

    H(x)=(1-x)(1+x^2+x^4-x^5)+x^10(2x^3-1).             (3)

**Uniform bound.** H(x)≥1/500 for 0≤x≤1.

For x≤4/5, the first bracket in (3) is at least 1, and the final term is at least -x^10. Hence

    H(x)≥1-x-x^10≥1/5-(4/5)^10>1/5-11/100=9/100.

The strict bound (4/5)^10<11/100 follows from the exact integers 4^10=1048576 and 5^10=9765625. For x≥4/5, the first summand in (3) is nonnegative, while

    H(x)≥(4/5)^10·(2(4/5)^3-1)
         =(4/5)^10·3/125 > (1/10)·3/125
         =3/1250>1/500.

Here (4/5)^10>1/10 follows from the same displayed integers. These two intervals cover [0,1]. This is a written inequality proof, not inference from tested points. Also

    H(1)=1,       H'(1)=14.                             (4)

The derivative equality follows directly from (2): -1+2-3+4-10+6-10+26=14.

## 3. An elementary degree-elevation bound with integer coefficients

Let H(x)=Σ_(j=0)^13 h_j x^j with the integer coefficients in (2). For an integer d≥13, homogenize to degree d:

    H_d(X,Y)=Σ_(j=0)^13 h_j X^j (X+Y)^(d-j)
             =Σ_(k=0)^d g_(d,k) X^k Y^(d-k),

where, with out-of-range binomial coefficients interpreted as zero,

    g_(d,k)=Σ_(j=0)^13 h_j · binom(d-j,k-j).              (5)

All g_(d,k) are integers. We prove that they are positive for every d≥246000, without importing a positivity theorem.

Normalize by the positive binomial coefficient:

    b_(d,k)=g_(d,k)/binom(d,k)
            =Σ_j h_j · (k)_j/(d)_j,                    (6)

where (k)_j is a falling factorial, and the term is zero when j>k. The j=0 term is 1.

For each j≤13, the ratio (k)_j/(d)_j is the probability that j draws **without replacement** from d positions all land in a fixed k-position subset. The quantity (k/d)^j is the same probability with replacement. Couple the two by first drawing with replacement and conditioning on all drawn positions being distinct. Conditional on that event, the ordered tuple is uniformly distributed without replacement. The probability of any collision is at most binom(j,2)/d by the union bound over pairs of draws. Therefore

    |(k)_j/(d)_j - (k/d)^j| ≤ j(j-1)/(2d).               (7)

This includes k<j, where the first probability is zero. Substituting into (6) gives

    |b_(d,k)-H(k/d)| ≤ (1/d) Σ_j |h_j|·binom(j,2)
                      =246/d.                          (8)

The exact finite sum is

    1+3+6+20+15+45+156=246,

from j=2,3,4,5,6,10,13 respectively. At d≥246000, (8) is at most 1/1000. Section 2 gives H(k/d)≥1/500, hence

    b_(d,k)≥1/1000>0.

Thus every integer g_(d,k) is strictly positive. This proves the degree-elevation statement uniformly for every k and d in the range; no enumeration over either variable occurs.

## 4. Literal finite word capacity, not a formal signed completion

Take n=d+2 with d≥246000 and set

    G_n(X,Y)=X^2 H_d(X,Y).

Its coefficients are positive at every X^kY^(n-k) for 2≤k≤n and zero at k=0,1. They are integers by (5). Homogenizing identity (1) to degree n gives the actual polynomial identity

    G_n(X,Y)
      + Σ_(s=0)^14 [x^s]A(x) · X^s Y (X+Y)^(n-s-1)
      =(X+Y)^n.                                        (9)

To see (9), substitute x=X/(X+Y) in (1) and multiply by (X+Y)^n; both sides are homogeneous polynomials and agree identically. Every exponent n-s-1 is nonnegative.

The second summand of (9) has nonnegative coefficients. Consequently if G_(n,k) is the coefficient of X^kY^(n-k) in G_n, then

    0≤G_(n,k)≤binom(n,k).                               (10)

This is the exact **raw-word availability bound**: there are binom(n,k) distinct binary words of length n with exactly k a's. Choose any G_(n,k) of them, independently for each k. Let T_n be the union of these chosen words and put

    M_n=C ∪ T_n.

Because n>15, no chosen tail word duplicates a Shor word. Within each composition choose distinct words, and different compositions are disjoint, so M_n is an actual finite set, not a multiset or signed polynomial. Substituting X=x,Y=1-x into (9) makes the homogenized C term exactly (1-x)A(x). Hence the raw set satisfies every mass equality in section 1.

The pure-a tail coefficient is

    G_(n,n)=g_(d,d)=Σ_j h_j=H(1)=1.

Thus the word a^n is chosen, and it is the only pure-a word. The one-b tail coefficient is

    G_(n,n-1)=g_(d,d-1)=Σ_j h_j(d-j)
              =dH(1)-H'(1)=d-14=n-16.                   (11)

Adding the original sixteen one-b Shor words yields exactly n such words. These cardinalities are consequences of a raw-set construction, not code-theoretic order restrictions or claims that their residue points form an n-cbc.

## 5. Explicit ambiguity and the exact remaining choice problem

The coefficient at k=2 is exactly

    G_(n,2)=g_(d,0)=h_0=1.

Choose its one raw word to be

    W_n=(ba)(ba)b^(n-4),

which has length n and exactly two a's. For each other composition k, choose the first G_(n,k) distinct words in lexicographic order, with a<b. This is a finite mathematically explicit rule; no list was generated or represented as an exercised witness.

Then M_n is NOT UD: one factorization is the single codeword W_n, while another is the two codewords ba,ba followed by n-4 copies of the codeword b. Both ba and b are literal members of the exact Shor C. These are distinct finite lists with identical concatenation. This controls precisely the UD boundary while preserving all the exact mass identities, the pure-a word and the one-b cardinality.

This intentional ambiguous choice does **not** show that every possible choice of the G_(n,k) words is ambiguous. The consequential sufficient construction problem now exposed is:

> For some n in this range, choose G_(n,k) raw words of every composition so that C∪T_n has a finite nonempty-residual closure S as in `raw-realization-protocol-v1.md`.

If that one choice were constructed and independently verified, (9) supplies exact Kraft equality and the residual certificate supplies UD; the protocol's proof would then give a genuine finite complete extension of Shor's exact C. No cyclic-factorization or general n-cbc realization converse would be needed.

Conversely, failing this **homogeneous-tail sufficient ansatz** would not rule out finite completion with arbitrary additional word lengths. The main target remains unrestricted. There is no claim that every possible completion can be transformed into this ansatz, and no such transformation is used.

## 6. Decision value and trust

This construction shows that the missing raw realization condition cannot be supplied merely by strengthening the scalar Kraft check to all Bernoulli probabilities, binding the exact words, requiring one pure-a word, or matching the one-b cardinality. All of those already hold in an explicit, uniformly ambiguous finite family. The missing ingredient is an actual decodability-compatible tail selector (or a different unrestricted realization/obstruction), not another probability normalization.

All proofs here are written and self-contained: polynomial multiplication, a two-interval positive lower bound, a collision-probability coupling/union bound, homogeneous coefficient comparison, finite selection within known binomial capacities, and an explicit ambiguity. No inaccessible theorem, source-status assertion, original Szabó proof, imported positivity theorem or scientific computation is a premise. The constant 246002 is deliberately non-optimal and is not scientific headroom on the true order problem.

This is a construction/protocol control, not a discovery claim. Separate in-harness reconstruction and parent checks on the pinned bytes remain required before written acceptance. No execution admission is requested: generating these exponentially large raw tails is not currently justified, and a solver framework would not replace the missing selector proof.
