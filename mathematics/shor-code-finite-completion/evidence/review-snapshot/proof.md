# Exact finite-completion question and audited obstruction

Date: 2026-10-14 PT. Status: **PARTIAL / OPEN-BLOCKED**, not a full resolution.

## 1. Exact target and quantifiers

Let `A={a,b}`, with distinct letters, and let

\[
C=b\{1,a,a^7,a^{13},a^{14}\}
\cup\{a^3,a^8\}b\{1,a^2,a^4,a^6\}
\cup a^{11}b\{1,a,a^2\}.
\]

The question is whether

\[
\exists X\subseteq A^+\quad
X\text{ finite},\quad C\subseteq X,\quad
X\text{ uniquely decipherable},\quad
\forall w\in A^*\;\exists u,v\in A^*:uwv\in X^*.
\]

Unique decipherability quantifies over arbitrary finite lists of words from `X`, not only two-word products or words containing a bounded number of `b`s. No bound on the size of `X`, its maximum word length, or the number of `b`s in its words is imposed. The book's general decidability Question 2 is distinct and is not answered here.

## 2. The actual finite checks

`work/check_evidence.py` reconstructs the 16 words independently from the three unions. It checks unique decipherability in two representations:

1. Sardinas–Patterson, with the exact reachable residual language retained.
2. The absolute-difference graph from Cordero 2019, Proposition 2: for distinct bayonets `(i,j),(k,l)`, add the edge `|i-k| -> |j-l|`; there is no nonempty path from 0 back to 0.

The cardinality is 16 and the longest word has length 15. Their dyadic Kraft sum is `13763/16384`, not 1. More directly, a flower automaton whose codeword paths all return to a base vertex recognizes `C*`; making every vertex initial and accepting recognizes its factors. Exact subset reachability finds that `bbaab` is missing. `a^26` is independently checked missing as well. These are certificates that **C itself is incomplete**, not that it has no finite completion.

For a hand check of `bbaab`, every word of `C` has one `b`. An adjacent pair of `b`s in a product of codewords requires the second `b`'s word to have left exponent zero. That row has right exponents only `0,1,7,13,14`. None can combine with a next left exponent in `0,3,8,11` to make an intervening run of two `a`s. The same argument is valid when the displayed word is a factor rather than a whole product, because its three `b`s are consecutive `b`s in the ambient word.

Controls distinguish these properties: `{a,b,ab}` is complete but ambiguous; `{aa,b}` is uniquely decipherable but incomplete; the nonprefix complete example `{b,ab,a^4,a^2ba,a^3b,a^2b^2}` is accepted; adding `a` or `ba^3` to the Shor instance creates a real parsing ambiguity and is rejected. Changing the doubled collision to a false equality is rejected. Receipts: `evidence/verification.json`.

## 3. Necessary bridge to a cyclic factorization

The direction below is the Restivo–Salemi–Sportelli lemma and Theorem 4 (1989, pp.145–146), restated as Theorem 1 in Cordero 2019 and Theorem 1.1 in Cordero 2023. The original proof image is retained as `sources/rss1989-page145.png`.

Suppose a finite complete uniquely decipherable `X` contains `C`. Let `d` be its maximum word length. Completeness applied to a sufficiently long run of `a`s forces some codeword to be a nonempty pure `a`-power. There is exactly one such codeword, say `a^n`: two different pure powers would give two different lists with equal concatenation. This `n` is the **order of the letter a in X**. It is not the maximum word length 15 of the original `C`, nor the cardinality 16 of `C`.

Define, modulo `n`,

\[
L=\{k\bmod n:\exists t\ge1,\ a^k b^t\in X\},\qquad
R=\{k\bmod n:\exists t\ge1,\ b^t a^k\in X\}.
\]

Then every residue has a unique representation `l+r`, with `(l,r) in L x R`.

- **Existence:** for a sufficiently large representative `m` of any residue, embed `b^d a^m b^d` in a word of `X*`. The two transitions between letters cannot belong to the same codeword when `m>d`. The intervening codewords are pure `a^n`s. Thus `m=r+jn+l` for suitable boundary codewords `b^s a^r` and `a^l b^t` and integer `j>=0`.
- **Uniqueness:** two representations congruent modulo `n` can be made equal as nonnegative integers by inserting different numbers of `a^n` codewords. Pad the outer `b`-blocks with copies of the codeword `b`, which belongs to `C`. This produces two distinct lists of codewords with the same concatenation, contradicting unique decipherability. The same padding argument rules out two different raw left exponents, or two different raw right exponents, representing one residue.

Consequently the sum map is a bijection and

\[
|L||R|=n,\quad \{0,3,8,11\}\subseteq L,\quad
\{0,1,7,13,14\}\subseteq R.
\]

The displayed residues are distinct. More explicitly, if two original words `a^i b,a^j b` had `j-i=kn>0`, the second would equal `(a^n)^k(a^i b)` as a concatenation; the analogous suffix argument applies to `ba^i,ba^j`. Hence `|L|>=4`, `|R|>=5`, and already `n>=20`. This justifies the distinctness of all later collision pairs without any bounded search.

**No converse is asserted.** A cyclic factorization with the indicated subsets is only necessary. It does not impose the six middle-row words with nonzero suffixes, or the two nonzero suffixes in the final row, as additional compatibility requirements. Nor does an `n`-complete bayonet code automatically give a finite complete code in the book's sense. Cordero 2023 explicitly leaves the general realization bridge open (p.6); its sufficient completion theorem requires the Hajós hypotheses.

## 4. Multiplier lemma, with its proof

Let `G` be a finite abelian group and suppose `A+B=G` with unique representations. If a positive integer `s` is coprime to `|A|`, then the map `(a,b) -> s*a+b` is again bijective. In particular, multiplication by `s` is injective on `A`, and `(sA,B)` is a factorization. The roles of `A,B` can be interchanged.

This is the Sands multiplier result cited by Cordero 2019, Theorem 2. The following group-ring proof makes the dependency explicit instead of assuming a strengthened statement from memory.

First take a prime `p` not dividing `|A|`. In the commutative group ring `F_p[G]`, put `U=sum_{a in A}[a]`, `V=sum_{b in B}[b]`, and `W=sum_{g in G}[g]`. The original factorization says `UV=W`. Translation permutes `G`, so `UW=|A|W`. Therefore

\[
U^pV=|A|^{p-1}W=W.
\]

The last equality is Fermat's theorem in `F_p`. The characteristic-`p` identity gives `U^p=sum_{a in A}[pa]`. Thus the integer number `N_g` of pairs `(a,b)` with `pa+b=g` satisfies `N_g=1 (mod p)` for every `g`. Every `N_g` is nonnegative, hence at least 1. But `sum_g N_g=|A||B|=|G|`, so all `N_g` equal 1. This proves the prime case, including injectivity on `A`. Iterate over the prime factors of `s`, with multiplicity; the cardinality of the scaled factor remains `|A|` throughout. This proves the stated lemma.

This classical proof has not been formalized in Lean in this dossier. In particular, the numerical checker does not certify this all-group theorem.

## 5. Audit of the 330 and 660 divisors

Since `n>=20`, the following integer equalities produce genuinely different component pairs modulo `n`:

| Scaled factor | First representation | Second representation | Consequence |
|---|---|---|---|
| `8R` | `8+8*0` | `0+8*1` | `2` divides `|R|` |
| `3R` | `3+3*0` | `0+3*1` | `3` divides `|R|` |
| `5R` | `8+5*0` | `3+5*1` | `5` divides `|R|` |
| `11R` | `11+11*0` | `0+11*1` | `11` divides `|R|` |
| `2L` | `2*3+1` | `2*0+7` | `2` divides `|L|` |

For example, if `|L|` were odd, the multiplier lemma would make `(2L,R)` a factorization, contradicting the last equality. For `8R`, the negation of coprimality with 8 says precisely that `|R|` is even. The other three right multipliers are prime.

It follows that

\[
330\mid |R|,\qquad 2\mid |L|,\qquad
\boxed{660\mid n},\qquad
\boxed{n\ge1320}.
\]

The lower bound follows already from `|L|>=4` and positive `|R|>=330`; it does **not** depend on the new audit of the doubled-left collision. Cordero 2019 §2.2 already states, for Shor's code `Y1`, `n=330*k` with `k>=4`. Therefore **1320 is recovered prior art**, not an improvement. The `660` divisibility follows by the same published multiplier technique; no originality is claimed, and the absence of that exact number in the screened sources does not establish novelty.

There is a literal arithmetic typo in the author-hosted 2019 text: the `3R` collision is printed with `8+3*0=0+3*1`. The correct collision uses `3` on the left as above. This does not invalidate the argument because `3` belongs to the forced left factor. The checker evaluates the repaired equality directly.

## 6. Why this does not decide Question 1

The obstruction leaves infinitely many possible orders, for example `n=1320,1980,2640,...`. No factorization search at those orders was used to promote a universal conclusion. The one HMZ attempt has the exact completion/noncompletion target, not this weaker obstruction.

A negative answer still requires an argument for **every** finite complete uniquely decipherable `X` containing `C`. One sufficient route is to exclude every cyclic factorization with the required subsets, but failure to exclude such factorizations does not imply a positive answer. A positive answer requires the actual finite `X` and independent unique-decipherability and completeness certificates, not just a cyclic factorization or an `n`-cbc.

Cordero 2023 proves the triangle result for cbc Hajós orders: products of at most three primes, or `p^k q` with primes `p,q`. Every remaining multiple of 660 has at least four distinct prime factors, so those families do not cover it. De Felice 2022's at-most-two-prime result is narrower. Sands 2007's primary abstract says the older Restivo–Salemi–Sportelli factorization conjecture is false; that conjecture must not be silently imported to close the gap. The full Sands 2007 text was not accessible in this investigation.

The exact unresolved obligation is unchanged: produce a finite complete code containing all 16 words, or prove that no such code exists. No such witness or all-order nonexistence proof is supplied here.
