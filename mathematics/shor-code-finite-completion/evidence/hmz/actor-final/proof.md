# Exact Shor finite completion: incomplete attempt

Date: 2026-10-14 PT. Baseline commit: `af6baa9`.

**Result: `done:false`.** No finite complete witness and no universal
noncompletion proof were obtained. In particular, there is no `witness.json`
or `Solution.lean`. The divisibility conclusions below are necessary conditions,
not an answer to Question 1. Novelty and source limitations are recorded
separately in [novelty.md](novelty.md).

## 1. Correspondence with the frozen question

The original book PDF was read locally, without modification:

`/Users/jinleic/jinleic-workspace/ai4s/10000个科学难题·数学卷(10000个科学难题数学编委会).pdf`

Printed pages 64–65, PDF pages 80–81, were extracted and rendered in `sources/`.
Page 64 defines a code by uniqueness of finite sequences of codewords and
completeness by the factor condition. Page 65 displays exactly the code in
`Statement.lean` and asks Question 1 about its finite completion. The following
Question 2 asks about decidability and is a different problem.

The correspondence is the letter bijection `a ↦ false`, `b ↦ true`, extended
to lists. It preserves concatenation, empty words, and contiguous factors.
The 16 entries of `original` are exactly the four rows

\[
\begin{array}{c|l}
i&j\ \text{with }a^iba^j\in C\\\hline
0&0,1,7,13,14\\
3&0,2,4,6\\
8&0,2,4,6\\
11&0,1,2
\end{array}
\]

Different pairs give different words, by the position of the unique `b`.
`UniquelyDecipherable` quantifies over arbitrary finite lists and compares
their flattened concatenations. It also excludes the empty codeword: otherwise
the lists `[]` and `[[]]` would violate its implication. `Complete` asserts
exactly that every word occurs between two contexts in a concatenation of
codewords. A `Finset Word` expresses finiteness without a bound on word length
or cardinality. Thus `HasFiniteCompletion` expresses the book's Question 1
under this relabeling. This is a mathematical audit of the definitions, not a
Lean proof of either answer.

For completeness, the positive certificate's Kraft bridge can be justified
directly. Let a finite UD code $X$ have nonempty words and let

\[
K(X)=\sum_{x\in X}2^{-|x|}.
\]

If $K(X)=1$, unique decoding gives
\(\sum_{z\in X^*}2^{-|z|}=\sum_{r\geq0}K(X)^r=\infty\).
If a nonempty word $w$ of length $h$ were absent as a factor of $X^*$,
the number of its words of length $m$ would be at most

\[
2^m(1-2^{-h})^{\lfloor m/h\rfloor}.
\]

Indeed, each of the disjoint length-$h$ blocks must differ from $w$.
The resulting weighted sum over all lengths converges, a contradiction.
So $X$ is complete.

Conversely, write $M=\max_{x\in X}|x|$, and let $f_m$ count the words
of length $m$ in $X^*$. Completeness allows any length-$m$ word to be
covered by consecutive whole codewords with fewer than $M$ extra letters
on each side. Consequently

\[
2^m\leq(2M+1)\sum_{k=m}^{m+2M}f_k.
\]

If $K(X)<1$, finiteness and continuity give a real $z\in(1/2,1)$ with
\(\sum_{x\in X}z^{|x|}<1\). Unique decoding then implies
\(\sum f_k z^k<\infty\), so the right side above is bounded by a constant
times $z^{-m}$. This contradicts $2z>1$. Together with McMillan's
inequality, this proves $K(X)=1$. This bridge supplies no missing witness.

## 2. Audit of the scout collision

Assume, only for deriving necessary conditions, that a finite completion $X$
exists. There is a unique positive $n$ with $a^n\in X$. One can see
existence directly from finiteness and factor-completeness: if every codeword
contains `b` and has length at most $M$, no concatenation has an `a`-run
longer than $2M-2$. Uniqueness follows because two distinct powers

\[
(a^r)^s=(a^s)^r
\]

would give different codeword lists of lengths $s$ and $r$.

Use the Restivo–Salemi–Sportelli necessary factorization $L\oplus R=\mathbb Z_n$, with $L\supseteq\{0,3,8,11\}$ and

\[
R\supseteq\{0,1,7,13,14\},\qquad n=|L||R|.
\]

The passage from the book's completeness to finite maximality is its stated
fact, also Theorem 2.2 of De Felice (2022). The cyclic factorization theorem
is the lemma and Theorem 4 of Restivo–Salemi–Sportelli (1989), restated as
Theorem 1 of Cordero (2019).

The already-published restriction $n=330k,\ k\geq4$ is taken as prior art,
not rediscovered by a bounded search. It ensures that the small residues in
the following collisions are distinct. The arithmetic behind the prime
divisors of $|R|$ can be checked without copying the 2019 typo:

\[
\begin{array}{c|c}
\text{scaled right factor}&\text{two representations}\\\hline
8R&8+8\cdot0=0+8\cdot1\\
3R&3+3\cdot0=0+3\cdot1\\
5R&8+5\cdot0=3+5\cdot1\\
11R&11+11\cdot0=0+11\cdot1
\end{array}
\]

Sands's multiplier theorem therefore forces $2,3,5,11\mid |R|$.
The printed 2019 equality with `8 + 3*0` and `0 + 3*1` is false; the
second row above is the valid collision.

For the scout, suppose $|L|$ is odd. Sands permits $2L\oplus R$, but

\[
2\cdot3+1=2\cdot0+7.
\]

These really are different pairs in the *image sets*: $6\not\equiv0\pmod n$, and $1\not\equiv7\pmod n$, since $n\geq1320$. This does not assume
that multiplication by 2 is injective on all of $L$. It only needs the two
displayed image elements to be different. Thus $2\mid |L|$, and

\[
660\mid n.
\]

This audits the scout successfully and does not prove noncompletion.

## 3. Using the inner words: a necessary divisor of 1320

Let $Y=C_X(b)$ be the $n$-cbc provided by the context theorem. Since
the original exponents are less than $n$, it contains all 16 pairs of $C$.
A border $(P,Q)$ of the stable family generated by $Y$ exists. Here

\[
|P||Q|=n.
\]

Theorem 7.2 of Cordero (2023) permits multiplying the left exponents by

\[
u\quad\text{when }\gcd(u,|Q|)=1,
\]

and the right exponents by $v$ when $\gcd(v,|P|)=1$, reducing modulo $n$.
It also preserves compatibility of the generated family. In particular,
every unit modulo $n$ is an allowed multiplier on either side. This
statement concerns the existing hypothetical cbc; it does not construct one.

We already have $660\mid n$, so $4\mid n$. If $8\nmid n$, write

\[
n=4m,\qquad m\text{ odd}.
\]

Choose an odd integer $u$ with $2u\equiv1\pmod m$. Such a choice exists
by the Chinese remainder theorem. Then $\gcd(u,n)=1$, and

\[
8u\equiv4\pmod n.
\]

Set $s=3u\bmod n$. The left-scaled cbc must contain

\[
a^sba^4,\quad b,\quad a^sb,\quad a^4b,
\]

coming respectively from $a^3ba^4,b,a^3b,a^8b\in C$. But

\[
(a^sba^4)(b)=(a^sb)(a^4b)
\]

is an ordinary word equality with different first codewords. This contradicts
unique decoding of that cbc. All exponents displayed are canonical residues;
in particular $4\neq0$ modulo $n$. No illicit collision of collapsed
image elements is involved. Therefore $8\mid n$, and hence

\[
\boxed{1320\mid n}.
\]

The published lower bound is $n\geq9900$: Szabó (2006), Theorem 7,
printed page 453, proves that $330p_1p_2p_3\mid n$ for some three distinct
primes. The hypothesis and conclusion excerpts are retained in
`sources/szabo-2006-theorem7-excerpt.txt`; see also the source audit in
`novelty.md`. The condition $1320\mid n$ alone does not improve that
published numerical bound.

Combining Theorem 7 with the $8\mid n$ established above gives the partial
corollary

\[
\operatorname{lcm}(8,330p_1p_2p_3)\mid n,\qquad n\geq19800.
\]

The minimum occurs at $\{p_1,p_2,p_3\}=\{2,3,5\}$, where
$\operatorname{lcm}(8,9900)=19800$. Indeed, if 2 is one of the three
primes, the other two have product at least $3\cdot5$; if 2 is absent,
their product is at least $3\cdot5\cdot7$, giving a larger least common
multiple.

This is a **partial corollary whose novelty is unaudited**. The full
Szabó–Sands (2009) Section 10 pages and Cordero's thesis were not read.
No originality is claimed, and no all-order obstruction or finite
completion follows.

## 4. An infinite family survives the entire unit-multiplier graph test

This is the precise failure of the attempted all-$n$ extension of Section 3.
It is a uniform argument about infinitely many orders, not an enumeration of
orders up to a cutoff.

For two different bayonet pairs $(i,j),(k,\ell)$, the modular difference
graph has the edge

\[
i-k\longrightarrow\ell-j\quad(\bmod n).
\]

A nonempty path from 0 back to 0 is the obstruction used in the modular
code/compatibility criterion. In applying it to the 16 forced pairs, one
must keep only edges from pairs belonging to the *same* transformed code.
Edges from one word of each of two different transformed codes would test a
different, unjustified condition.

Take **every** pair of units $u,v\in(\mathbb Z_n)^\times$, transform $C$
by $(i,j)\mapsto(ui,vj)$, and superpose their difference graphs. This is
the part of the hypothetical compatibility graph forced by the known words.
Two small difference sets control paths out of zero:

\[
D_L=\{|i-k|:i\neq k\}=\{3,5,8,11\},
\]

\[
D_0=\{|j-\ell|:i=k,\ j\neq\ell\}
     =\{1,2,4,6,7,12,13,14\}.
\]

Now suppose $1320\mid n$. Each element of $D_L$ divides $n$, so
the gcd with $n$ of a nonzero *source* vertex of any edge belongs to

\[
\{3,5,8,11\}.
\]

Multiplication by a unit and change of sign preserve this gcd. Any edge
starting at 0, on the other hand, must come from a same-left row, because
unit multiplication is injective. Its nonzero target has gcd in

\[
\{1,2,4,6,12\}\ \cup\ \{7,13,14\}.
\]

More precisely, the gcd for 7 or 13 is either 1 or that prime, and for 14 it
is 2 or 14. All these possibilities are disjoint from $D_L$. Thus every
edge out of 0 ends at a vertex with **no outgoing edge in the entire
superposition**. There are no edges $0\to0$, since distinct same-row pairs
have different right residues. There is no nonempty path $0\leadsto0$.

Accordingly, this test on the forced words survives for every order

\[
n=1320t,\qquad t\geq1.
\]

The same conclusion holds after arbitrary compositions of these partial
sets in the sense of Cordero's Definition 2.1. Indeed, an output pair
$(i,\ell)$ of $U\circ_r V$ comes from $(i,j)\in U,(k,\ell)\in V$ with
$j+k=r$ modulo $n$. For two such output pairs, the two matching equations
give $j'-j=k-k'$. Their difference-graph edge therefore expands as

\[
i-i'\longrightarrow j'-j=k-k'\longrightarrow\ell'-\ell.
\]

If one component pair is identical, omit its zero-length step. For distinct
output pairs, at least one genuine edge remains. Inductively, every edge
of a composition expands to a nonempty path in the original superposition.
A cycle from 0 to 0 in a family of compositions would consequently produce
one in the original graph, which has just been excluded. Two different
intermediate decompositions of the same output pair would likewise give
a forbidden path $0\to d\to0$; the identical-decomposition case is not an
ambiguity. This proves survival for the forced words under units and
compositions, without supplying the unknown words of a full cbc.

This is not a factorization or a cbc construction. The unknown other

\[
n-16
\]

elements of a prospective cbc can add edges, and their existence is not
proved. Nor are the stronger conditions for arbitrary internal words of a
finite complete code discharged.

Even replacing unit multipliers by all the multipliers coprime to the border
cardinalities does not yield a contradiction from these numerical data
alone. For the infinite **numerical assignments**

\[
n=(1320t)^2,\qquad |P|=|Q|=1320t,
\]

the allowed multipliers are exactly the units modulo $n$. These assignments
satisfy the prime divisibility constraints already derived. No assertion is
made that a border or factorization with these cardinalities exists. Their
role is to exhibit the unproved step in an attempted contradiction based
only on cardinalities and forced-word graph edges.

## 5. Why a one-b argument does not answer the question

For a hypothetical finite complete code, the Bernoulli identity with
weights $a=x,b=1-x$ gives

\[
1=x^n+(1-x)P_1(x)+(1-x)^2P_2(x)+\cdots+(1-x)^rP_r(x),
\]

where $P_j$ counts codewords with exactly $j$ occurrences of `b` by
their numbers of `a` letters. This identity follows by the same finite-code
counting argument as in Section 1 with positive letter weights.

If no codeword has two or more `b` letters, then

\[
P_1(x)=1+x+\cdots+x^{n-1}.
\]

But both $ba^7$ and $a^3ba^4$ belong to $C$, giving coefficient at
least 2 at $x^7$, a contradiction. This excludes only the one-b class.
In the actual problem $r$ is arbitrary, and the terms $P_2,\ldots,P_r$
cannot be discarded. No sign, factorization, or termination argument was
obtained that eliminates them for every finite $r$.

## 6. A full-proof claim audited and rejected as a route

An author-uploaded draft by Zhang and Shum, dated September 8, 2008,
*Finitely Completable Codes and Triangle Conjecture*, claims the full
conclusion in its Theorem 3.7. The source URL, UTC retrieval time, selected
parser output from pages 4 and 11–13, and scope fragments are retained in
[the source excerpt](sources/zhang-shum-2008-excerpt.txt). This is an audit
against retained parsed text; no locally inspected PDF image is claimed.

On page 4 the context definition is

\[
X_w=(a^*wa^*\cap X^*)\setminus
\bigl[a^n(a^*wa^*\cap X^*)\cup(a^*wa^*\cap X^*)a^n
       \cup a^n(a^*wa^*\cap X^*)a^n\bigr].
\]

Page 11 sets, for $X_w=\{a^{i_1}wa^{j_1},\ldots,a^{i_n}wa^{j_n}\}$,

\[
p_w(x)=x^{i_1+j_1}+\cdots+x^{i_n+j_n},
\]

and page 12 sets

\[
p_0(x)=1+x+\cdots+x^{n-1}.
\]

The proof's scope on page 11 is a finite complete binary code $X$ with
$a^n\in X$, and a positive Bernoulli distribution $\pi(a)=x$,
$\pi(b)=1-x$. Its second branch on page 12 assumes

\[
p_w(x)\not\equiv p_0(x)\quad\text{for every }w\in b(a^*b)^*.
\]

Here and below these are mathematical transcriptions of the retained
formulas. The parser renders the negated identity sign as `6≡`; that
artifact is documented in the source excerpt.

Here is an independent counterexample to the step. Put

\[
X_0=\{aa,ab,ba,bb\},\qquad n=2.
\]

It is a finite complete prefix code and $X_0^*$ is the set of words of
even length. With the draft's trimmed-context definition, the possible
context polynomials are

\[
p_w(x)=\begin{cases}2x,&|w|\text{ odd},\\1+x^2,&|w|\text{ even},\end{cases}
\qquad p_0(x)=1+x.
\]

For words $w$ beginning and ending in `b`, these formulas follow simply
by allowing $i,j\in\{0,1\}$ with $i+j+|w|$ even. Neither polynomial
equals $p_0$, so the draft's branch that assumes no equality actually
applies to this example for every permitted $w$. The family of context
polynomials is finite, both values at 1 are 2, and the maximal polynomial
near 1 is $1+x^2$, since $(1+x^2)-2x=(1-x)^2$. Thus the subsequent maximum
selection also applies. Every $0<x<1$ gives the required positive
distribution.

Let

\[
Y=(X_0\setminus\{aa\})(aa)^*
 =\{ab,ba,bb\}(aa)^*.
\]

This is exactly the derived $Y=(X\setminus\{a^n\})(a^n)^*$ introduced
on page 12. The source imposes finiteness on $X$, not on this $Y$.
Our $Y$ is infinite, as is allowed by that construction. It is UD by
the block argument below and is complete independently of any claim in the
draft: extend any binary word to even length, prepend the block `bb`,
and append `bb`. Partition this block string before each non-`aa`
block; each part belongs to $Y$. Hence the original word is a factor of
a word in $Y^*$. Its Bernoulli measure is also 1, as $q_1+q_2=1$ below.

Under $a=x,b=1-x$, the sublanguages with respectively one and two `b`
letters have measures

\[
q_1(x)=\frac{2x}{1+x},\qquad q_2(x)=\frac{1-x}{1+x}.
\]

The words in $Y\cup Y^2$ with more than two `b` letters have measure

\[
\pi(Y_{>2})=2q_1q_2+q_2^2
            =\frac{(1-x)(1+3x)}{(1+x)^2}.
\]

Products and the three contributing sublanguages are disjoint because

\[
Y=\{ab,ba,bb\}(aa)^*
\]

is a code: every word of $Y$ consists of exactly one length-two block
other than `aa`, followed by zero or more `aa` blocks; each concatenation
therefore has a unique division at those non-`aa` blocks.

For general $r$, page 12 defines

\[
Y_{>r}=\{u\in\textstyle\bigcup_{i=1}^rY^i:|u|_b>r\},\qquad
Y_{\leq r}=\{u\in\textstyle\bigcup_{i=1}^rY^i:|u|_b\leq r\}.
\]

Its displayed tail formula is

\[
\pi(Y_{\leq r})=
\pi\!\left(\bigcup_{i=1}^rY^i\right)-\pi(Y_{>r})
=r-\frac{(1-x)^{r+1}f(x)}{1-x^n},
\qquad f\in\mathbb R[x].
\]

The preceding equality in the parsed source also contains a factor
$\pi(a^*)$; the following equality explicitly has denominator $1-x^n$.
Both source fragments are retained, and the latter is the formula used
again on page 13. No correction of that denominator is assumed here.
For $X_0$ and $r=2$ the asserted formula would require

\[
\pi(Y_{>2})=\frac{(1-x)^3f(x)}{1-x^2}
\]

for a polynomial $f$. Instead it forces

\[
f(x)=\frac{1+3x}{1-x^2},
\]

which has a pole at 1 and is not a polynomial. Equivalently, the actual tail
has a simple zero at 1; the asserted form has a zero of order at least two.
The later Taylor choice also permits $r=2$: for its maximal context
polynomial, $P(x)=p_0(x)-(1+x^2)=x(1-x)$ has a zero of order one at 1.
Thus its condition $r>k+1$ holds with $k=0,r=2$.
The draft's Taylor argument consequently cannot supply the required proof.
This rejects a proof step, not the truth of the triangle conjecture. It
does not establish the present target's negation.

## 7. Exact remaining gap and acceptance status

RSS (1989), printed pages 144 and 146–147, gives a specific historical
factorization route toward a negative answer. Its Conjecture 2 excludes
embeddings of

\[
(T,R)=(\{0,p,k\},\{0,1\}),\qquad p\text{ prime},\ p\nmid k.
\]

The paper notes that Shor's pair contains $(\{0,3,8\},\{0,1\})$ and,
using that conjectural obstruction, conjectures that Shor's code has no
finite completion. This was a conjectural argument, not a proof.

Later work prevents using the general conjecture as a theorem. Sands's
2007 paper, DOI [10.1142/S0218196707004293](https://doi.org/10.1142/S0218196707004293),
reports a refutation of the RSS conjecture in its publisher-provided
abstract. The retained preview evidence and its access limitation are
recorded in [the later-work audit](sources/rss-later-work.txt).
The general RSS heuristic is therefore unavailable as a universal
obstruction. Only the first-page preview was obtained, so this attempt
does not assert which individual $(p,k)$ occur in the counterexamples.

For the exact target, a sufficient mathematical statement would still be

\[
\forall n\geq15,\quad
\nexists L,R\subseteq\{0,\ldots,n-1\}:\
L\oplus R=\mathbb Z_n,\quad
L\supseteq\{0,3,8,11\},\quad R\supseteq\{0,1,7,13,14\}.
\]

Here the inclusions use canonical integer representatives, and the sum is
modulo $n$. Every possible completion already has $n\geq1320$, so this
formulation covers all possible completion orders and avoids small-modulus
collapse in the stated embedding target.

In particular, a valid proof of the special RSS obstruction for $p=3,k=8$
would suffice, despite the general conjecture being false. Neither that
special obstruction nor the full displayed assertion is proved here.
Cordero (2019), Section 2, explicitly leaves the full pair's embedding
unsettled. No later full answer for that pair was validated in this audit.
Szabó (2006), Theorem 7, is an earlier primary publication of the indexed
Szabó–Sands necessary condition; it supplies a restriction, not a full
answer. See [novelty.md](novelty.md) for the exact provenance and scope.

To resolve the negative direction, an argument must still exclude a finite
UD complete extension for **every** remaining order $n=1320t$, without
assuming a one-b restriction, a bounded maximum codeword length, a Krasner
border, or the desired triangle inequality. No such argument was found.
Even the simpler boundary-factorization embedding problem is not settled
here. A proof that its embedding is impossible for all orders would suffice;
existence of a boundary factorization alone would not suffice for a positive
answer.

To resolve the positive direction, one must actually build a finite code
containing all 16 original words, prove unique decoding, and prove
factor-completeness (or exact Kraft equality). No such code was built.
The infinite family in Section 4 is a family of orders surviving a *partial
test*, not a family of completions.

The 2022 two-prime-order results and the 2023 cbc special-order results do
not cover these arbitrary remaining orders. No premise asserting the full
triangle conjecture or the desired noncompletion is adopted. None of the
cited structural results is formalized in Lean in this attempt.

All completed research artifacts are to be frozen before the single run
of `python3 -B verify.py`. Its output and exit status belong in
`verification-result.json` and `verification.log`. Absence of a certificate
is an expected acceptance failure and must not be converted into `done:true`.
