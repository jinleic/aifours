# Shor finite completion: exact target, bridge, and audited obstructions

Date: 2026-10-14 PT. Status: **PARTIAL / OPEN-BLOCKED**. Book Question 1 is not resolved: there is no finite complete witness and no all-order nonexistence proof.

Proof status labels used below:

- **Written proof**: a complete argument in this file, read by an independent model reviewer, but not kernel-checked.
- **Lean**: kernel-checked in `work/ShorArithmetic.lean`. Only arithmetic is formalized.
- **Unverified source**: a statement this worker could not authenticate from a primary text.

## 1. Exact target and quantifiers

Let `A={a,b}` with distinct letters, and

\[
C=b\{1,a,a^7,a^{13},a^{14}\}
\cup\{a^3,a^8\}b\{1,a^2,a^4,a^6\}
\cup a^{11}b\{1,a,a^2\}.
\]

Write `(i,j)` for the word `a^i b a^j`. The 16 pairs are

| row `i` | right exponents `j` |
|---|---|
| 0 | 0, 1, 7, 13, 14 |
| 3 | 0, 2, 4, 6 |
| 8 | 0, 2, 4, 6 |
| 11 | 0, 1, 2 |

Question 1 asks whether

\[
\exists M\subseteq A^+\ \text{finite}:\quad C\subseteq M,\quad
M\ \text{uniquely decipherable},\quad
\forall w\in A^*\ \exists u,v\in A^*:\ uwv\in M^*.
\]

Unique decipherability quantifies over all finite lists of codewords. There is no bound on `|M|`, on word lengths, or on the number of `b`s in a word of `M`. The book's Fact 1 makes complete and maximal equivalent for finite codes. Question 2, decidability, is a different question and is not addressed. The exact proposition is frozen in `work/Question.lean` (`ShorCompletion.HasFiniteCompletion`) and type-checks; no Lean theorem proves or refutes it.

## 2. Finite checks on `C` itself

`work/check_evidence.py` rebuilds the 16 words from the three unions. It confirms unique decipherability by Sardinas–Patterson and, independently, by the absolute-difference graph of Cordero 2019, Proposition 2. The maximum length is 15. The Kraft sum is `13763/16384<1`. A factor automaton certifies that `bbaab` and `a^26` are factors of no word of `C^*`.

A hand check for `bbaab`: every word of `C` has one `b`, so the second `b` of an adjacent pair starts a row-0 word. Its right exponent lies in `{0,1,7,13,14}`, and the next left exponent lies in `{0,3,8,11}`. No such sum equals 2.

So `C` is not itself complete. This is not a noncompletion certificate. Controls include the complete but ambiguous `{a,b,ab}`; the uniquely decipherable but incomplete `{aa,b}`; the complete prefix code `{b,ab,a^4,a^2ba,a^3b,a^2b^2}`; and the ambiguous mutations `C ∪ {a}` and `C ∪ {ba^3}`.

## 3. Bridge from a completion to bayonet data and a factorization (written proof)

From here on, `M` is a **hypothetical** finite, uniquely decipherable, complete code over `{a,b}` with `C⊆M`. Let `d` be its maximum word length. Note `b∈C⊆M`.

**(B1) A unique pure `a`-power.** By completeness, `a^{2d}` is a factor of a product of codewords. At most one codeword crosses each end of that run, and each covers at most `d-1` letters of it. Some codeword therefore lies inside the run: a nonempty pure power `a^n∈M`. If `a^n,a^m∈M` with `n≠m`, then `(a^n)^m=(a^m)^n` has two factorizations. Hence `n` is unique. It is the order of `a`, not the length 15 or cardinality 16 of `C`.

**(B2) Data.** Define residue sets modulo `n`:

\[
Y=\{(i,j)\bmod n:\ a^iba^j\in M\},\quad
R=\{r\bmod n:\ \exists s\ge1,\ b^sa^r\in M\},\quad
L=\{l\bmod n:\ \exists t\ge1,\ a^lb^t\in M\}.
\]

`Y` is Cordero's `C_M(b)`: a word of `M^*` with one `b` is `(a^n)^k a^iba^j (a^n)^{k'}` with a single non-power codeword.

**(B3) Tiling theorem.** For every `t≥0`, the map

\[
R\times Y^t\times L\to\mathbb Z_n^{t+1},\qquad
(r,(i_1,j_1),\ldots,(i_t,j_t),l)\mapsto
(r+i_1,\ j_1+i_2,\ \ldots,\ j_{t-1}+i_t,\ j_t+l)
\]

is a bijection. For `t=0` it is `(r,l)↦r+l`. Moreover, distinct raw codewords of the forms `b^sa^r`, `a^iba^j`, `a^lb^t` have distinct residue data.

*Existence.* Fix residues `(e_0,…,e_t)`. Choose integers `E_k≥d` with `E_k≡e_k`, and put

\[
w=b^d a^{E_0}ba^{E_1}b\cdots ba^{E_t}b^d .
\]

By completeness, `uwv=x_1\cdots x_N` with all `x_k∈M`. Every codeword has length at most `d`.

- Consider position `p`, the boundary between the leading `b^d` and `a^{E_0}`. If a codeword crosses `p`, it lies inside `b^da^{E_0}` and has the form `b^sa^r`, `s,r≥1`. Otherwise the codeword ending at `p` lies inside `b^d`; it is `b^s∈M`, and `s=1` because `b∈M` and `M` is a code. Either way, a codeword `b^sa^r` with `r≥0` ends at `p+r`.
- The codeword containing the `k`-th middle `b` cannot reach the neighbouring `b`s, because `E_{k-1},E_k≥d`. It is a one-`b` word `a^{i_k}ba^{j_k}∈M`.
- Symmetrically, the codeword starting at, or crossing, the boundary before the trailing `b^d` is `a^lb^t` with `t≥1,l≥0`.
- Every codeword strictly between consecutive ones above lies inside an `a`-run. It is therefore `a^n`.

Hence `E_0=r+k_0n+i_1`, `E_k=j_k+k_kn+i_{k+1}`, and `E_t=j_t+k_tn+l`. Reducing modulo `n` proves surjectivity.

*Uniqueness and raw injectivity.* Suppose two raw codeword tuples `(β,α_1,…,α_t,λ)` and `(β',α'_1,…,α'_t,λ')` give the same residues. Pad each to the same word `b^S a^{E_0}b\cdots ba^{E_t}b^T`. Use `S,T` at least both outer `b`-lengths, and large `E_k` in the common residue classes. Supply outer copies of the codeword `b` and inner copies of `a^n`. Each list of codewords determines the tuple: `β` is the codeword containing the last leading `b`, `α_k` is the codeword containing the `k`-th middle `b`, and `λ` is the codeword containing the first trailing `b`. Distinct tuples therefore give distinct lists with equal concatenation, contradicting unique decipherability. This proves injectivity of the map and of raw codewords into residues.

**(B4) Consequences.** For `t=0`, `(R,L)` is a factorization of `Z_n`; this is the Restivo–Salemi–Sportelli lemma and Theorem 4 (1989, pp.145–146; image `sources/rss1989-page145.png`). Then `|R||L|=n`, and `t=1` gives `|Y|=n`. From `C⊆M`,

\[
R\supseteq\{0,1,7,13,14\},\qquad L\supseteq\{0,3,8,11\},\qquad Y\supseteq C .
\]

Raw injectivity makes these residues distinct, so `|R|≥5`, `|L|≥4`, and `n≥20`. No converse is asserted. An incomplete code can have tiling data: deleting `abab` from Restivo–Salemi–Sportelli Example 6 keeps the data tiling. Cordero 2023 (p.6) leaves realization of a general `n`-cbc by a finite maximal code open.

## 4. Multiplier lemma (written proof)

**Lemma M.** Let `G` be a finite abelian group and `F,B:G→Z_{≥0}`. Suppose

\[
(F*B)(g)=\sum_h F(h)B(g-h)=1\quad\text{for all }g.
\]

Let `m≥1` be coprime to `|B|=Σ_gB(g)`, and define `B^{(m)}(g)=Σ_{mh=g}B(h)`. Then `F*B^{(m)}≡1`.

*Proof.* First let `p` be a prime not dividing `|B|`. In the commutative ring `F_p[G]`, let `W` be the sum of all group elements. Then `F B=W` and `W B=|B|W`. Frobenius and Fermat give `B^p=B^{(p)}`, so

\[
F B^{(p)}=F B^p=W B^{p-1}=|B|^{p-1}W=W .
\]

Thus every integer coefficient of `F*B^{(p)}` is nonnegative and congruent to 1 modulo `p`, hence at least 1. The coefficients sum to `|F||B|=|G|`, so all equal 1. Note `|B^{(p)}|=|B|` and `(B^{(p)})^{(m')}=B^{(pm')}`. Induct over the prime factors of `m`, with multiplicity. ∎

With `F=1_L` and `B=1_R`, this is the cyclic-group Sands multiplier statement cited as Cordero 2019, Theorem 2. If `s` is coprime to `|R|`, then `(r,l)↦sr+l` is a bijection `R×L→Z_n`. The same holds with the roles exchanged. A collision of two distinct pairs would give coefficient at least 2.

## 5. Unit multipliers for tiled families (written proof)

**Lemma U.** Let `P,Q⊆Z_n` with `|P||Q|=n`, and let `𝓔` be a family of `n`-element subsets of `Z_n^2`. Suppose every product `P X_1\cdots X_t Q` with `X_k∈𝓔` and `t≥0` tiles `Z_n^{t+1}`, as in (B3). Let `X∈𝓔` and let `u` be a unit modulo `n`. Put `φ_u(X)={(ui,j):(i,j)∈X}`. Then every product from `𝓔∪{φ_u(X)}` also tiles. The same holds for right multiplication `(i,j)↦(i,uj)`.

*Proof.* Work in `Z_{≥0}[Z_n^{t+1}]`, with coordinates `x_0,…,x_t`. The product `P(x_0)X_1(x_0,x_1)\cdots X_t(x_{t-1},x_t)Q(x_t)` counts the preimages in (B3), so tiling means it equals the all-ones element `W`.

Induct on the number of occurrences of `φ_u(X)`; zero occurrences is the hypothesis. Given a product with at least one occurrence, choose one, at position `ℓ`, and replace it by `X`. The result has one fewer occurrence, so by the induction hypothesis it equals `W`. Other occurrences, if any, stay inside the two parts below. Write it as `A·B`, where:

- `A=P(x_0)Z_1\cdots Z_{ℓ-1}` involves only `x_0,…,x_{ℓ-1}`;
- `B=X(x_{ℓ-1},x_ℓ)Z_{ℓ+1}\cdots Q(x_t)` involves only `x_{ℓ-1},…,x_t`.

Slice `A` at each fixed value `v` of `x_0,…,x_{ℓ-2}`. This gives a polynomial `A_v(x_{ℓ-1})`. Translates for distinct `v` have disjoint supports, so `A_vB=W` on the last `t-ℓ+2` coordinates. Coefficient sums give `|A_v|=n/|Q|=|P|`.

Apply the automorphism `x_{ℓ-1}↦x_{ℓ-1}^u`. Since `x_{ℓ-1}` occurs in `B` only through `X`, this gives `A_v^{(u)}·B'=W`, where `B'` has `X` replaced by `φ_u(X)`.

Let `m` be a positive representative of `u^{-1} \bmod n`. It is coprime to `n`, hence to `|P|`. Lemma M gives `(A_v^{(u)})^{(m)}B'=W`, and `(A_v^{(u)})^{(m)}=A_v`. Reassembling all slices gives `A·B'=W`. The right-multiplication case is symmetric: slice the right part, whose size is `|Q|`. ∎

**Corollary.** If `P Z^t Q=W` for all `t`, then `{a^n}∪\{a^iba^j:(i,j)∈Z,\ 0≤i,j<n\}` is a code. All coefficients of `Z^t` are 0 or 1, and two factorizations with different `Z`-word sequences would have equal residue words. Conversely, padding with `a^n` shows that the code property gives 0/1 coefficients.

Cordero 2023, Theorem 7.2, proves a stronger statement for the stable sets `C_M`. Its multipliers need only be coprime to a border factor. The proofs here use only units. Lemma U is proved directly, so the 8-divisor below does not depend on unchecked details of that theorem. On the explicit maximal codes in `evidence/bridge-multiplier-sanity.json`, every unit preserves tiling up to `t=3`. Some non-units fail, consistent with Theorem 7.2's coprimality conditions: left multipliers coprime to `|L|` and right multipliers coprime to `|R|`.

## 6. Necessary divisors of the order `n`

Take `(P,Q)=(R,L)` and `𝓔={Y}`; (B3) supplies the hypothesis of Lemma U.

**660 divides `n` (written proof).** By Lemma M, each of the following collisions forces a divisor. Each collision consists of two distinct pairs with equal image, valid as integer equalities.

| multiplier | pairs from `R×L` | equal images | consequence |
|---|---|---|---|
| `8` on `R` | `(0,8)`, `(1,0)` | `8·0+8=8·1+0` | `2 ∣ |R|` |
| `3` on `R` | `(0,3)`, `(1,0)` | `3·0+3=3·1+0` | `3 ∣ |R|` |
| `5` on `R` | `(0,8)`, `(1,3)` | `5·0+8=5·1+3` | `5 ∣ |R|` |
| `11` on `R` | `(0,11)`, `(1,0)` | `11·0+11=11·1+0` | `11 ∣ |R|` |
| `2` on `L` | `(1,3)`, `(7,0)` | `1+2·3=7+2·0` | `2 ∣ |L|` |

The first coordinates differ modulo `n` because `n≥20`. Hence `330∣|R|`, `2∣|L|`, and `660∣n`. Cordero 2019, §2.2, prints the `3R` collision as `8+3·0=0+3·1`, which is false; the table uses the correct one. The 330-divisibility and `n=330k,\ k≥4` are Cordero 2019 prior art. The doubled-left collision was the scout's suggestion; it is audited here, and its novelty is not claimed.

**8 divides `n` (written proof; arithmetic in Lean).** Suppose `4∣n` and `8∤n`.

1. `ShorArithmetic.exists_unit_eight_mul_eq_four` gives a unit `u` modulo `n` with `8u≡4 (mod n)`. Explicitly, write `n=4m` with `m` odd. Take `u=(m+1)/2`, or `u=(m+1)/2+m` if the former is even.
2. By Lemma U, `Z=φ_u(Y)` satisfies `R Z^2 L=W`. Since `(0,0),(3,0),(3,4),(8,0)∈Y`, the set `Z` contains `(0,0)`, `(s,0)`, `(s,4)` and `(4,0)`, where `s=3u \bmod n`.
3. Take `r=l=0`. The distinct tuples `((s,4),(0,0))` and `((s,0),(4,0))` both map to `(s,4,0)`. They are distinct because `4≢0 (mod n)`.
4. This contradicts tiling. Equivalently, `(a^sba^4)(b)=(a^sb)(a^4b)` contradicts the corollary.

With `4∣n` from above, this gives `8∣n`. Hence

\[
\boxed{1320\mid n}.
\]

This does not raise the published minimum: Cordero 2019 already has `n≥1320`. The HMZ actor first obtained `8∣n` through Cordero 2023, Theorem 7.2. The self-contained proof through Lemma U is this dossier's audit, and its novelty is not established.

## 7. A published stronger bound that could not be authenticated

The HMZ actor retained parsed fragments of Szabó (2006), *Completing codes and the Rédei property of groups*, TCS 359, 449–454, Theorem 7. As transcribed: if `C'` is a finite completion of Shor's code and `a^n∈C'`, then

\[
330\,p_1p_2p_3\mid n\quad\text{for some pairwise distinct primes }p_1,p_2,p_3 .
\]

That would give `n≥9900`. **Status: unverified source.** This worker's fetches of the author-uploaded PDF, ScienceDirect, and ResearchGate pages returned HTTP 403 or connection resets. Only the DOI metadata, which has no abstract, was read. The excerpt is in `evidence/hmz/actor-final/sources__szabo-2006-theorem7-excerpt.txt`; it is parser output, not an authenticated image. The proof was not read.

**Conditional corollary (Lean-checked arithmetic).** If that statement holds, then `n≥19800`. Write `n=330q`. Since `8∣n` and `330` is twice an odd number, `4∣q`. Also `p_1p_2p_3∣q`. The primes may coincide with `2,3,5,11`; only pairwise distinctness is used. Every positive multiple of 4 below 60 has at most two distinct prime factors, checked by kernel computation. So `q≥60`, and `q=60` attains the bound arithmetically. Lean roots: `ShorArithmetic.quotient_ge_sixty` and `ShorArithmetic.combined_order_lower_bound`. Szabó's statement and `8∣n` enter only as hypotheses. Novelty of `n≥19800` is unaudited.

## 8. Limits of the present methods

**The forced words cannot be exhausted by units (written proof).** Take any `n` divisible by 1320. Superpose the modular difference graphs, with edge `i-k→l-j`, of all `φ_{u,v}(C)` for units `u,v`.

- Nonzero edge sources have `gcd(·,n)∈\{3,5,8,11\}`.
- Edges out of 0 come from equal rows. Their targets have `gcd(·,n)` in `{1,2,4,6,12}`, together with values coming from `7`, `13` and `14`: `{1,7}`, `{1,13}` and `{2,14}`.
- These classes are disjoint. A target of an edge from 0 is therefore a nonzero vertex without outgoing edges, and there is no cycle through 0.

The HMZ actor extended this to compositions. Known-word unit-multiplier tests thus cannot exclude any order `1320t`. For `t=1`, the tiling `R φ_{u,v}(Y) L` with only the known parts of `R`, `L` and `Y` has no collision either. If the rows differ, `u(i'-i)≡r-r'` would need `gcd(r-r',n)∈\{3,5,8,11\}`, but the known differences `0,±1,±6,±7,±12,±13,±14` have gcd classes outside that set. If the rows agree, then `r=r'`, and `v(j-j')≡l'-l` would need a same-row difference in a class `3,5,8,11`, which does not occur. Larger `t` with the known parts of `R` and `L` was not analysed beyond the actor's composition argument.

**No conjectural closure.** Restivo–Salemi–Sportelli Conjecture 2 would exclude embeddings containing `({0,3,8},{0,1})`, and hence Shor's pair. The Crossref abstract of Sands (2007), retained as `sources/sands2007-crossref.json`, says such factorizations do exist. The full construction was not obtained. The conjecture cannot be used for any specific pair without a proof.

**A claimed full proof is not usable.** The HMZ actor found an author-uploaded 2008 Zhang–Shum draft claiming the triangle conclusion for finitely completable codes. It refuted the draft's tail-polynomial step with `X_0=\{aa,ab,ba,bb\}` and `Y=\{ab,ba,bb\}(aa)^*`. There, `π(Y_{>2})=(1-x)(1+3x)/(1+x)^2` has only a simple zero at `x=1`, while the draft's formula forces a double zero. This worker re-derived the counterexample's measure algebra. The worker could not re-fetch the draft (HTTP 403), so the correspondence with the draft's hypotheses rests on the actor's parsed excerpt and the HMZ reviewer's check. The published 2017 Zhang–Shum paper, as summarized by De Felice 2022, has a Krasner-factorization hypothesis.

## 9. Exact remaining gap

The following are proved for every hypothetical finite completion: `1320∣n`; the tilings (B3) for all `t`; unit multipliers (Lemma U); and every Lemma M consequence.

- **Negative answer.** It requires a contradiction for every order `n` satisfying the known constraints. Excluding every cyclic factorization `L⊕R=Z_n` with `L⊇\{0,3,8,11\}` and `R⊇\{0,1,7,13,14\}` would suffice, but it is not proved, and the general RSS heuristic is refuted.
- **Positive answer.** It requires an explicit finite `M⊇C`, with independently checked unique decipherability and Kraft sum 1. Kraft sum 1 is equivalent to completeness for finite UD codes; see §1 of the HMZ actor's `proof.md`. By the bounds above, `M` contains `a^n` with `1320∣n`, and with `n≥19800` if Szabó's Theorem 7 is correct. A factorization or `n`-cbc alone is insufficient.

No finite-order search was used to infer a universal statement.
