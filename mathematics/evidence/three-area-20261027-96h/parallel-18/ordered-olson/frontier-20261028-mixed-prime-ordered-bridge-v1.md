# Ordered Olson frontier — exact exchange failure and a mixed-prime elementary-kernel bridge

Owner **MathOlson-2-2**, original math-2 slot.
Native `/bin/date` before writing: **Wed Oct 28 17:04:37 PDT 2026**.
Status: **new written derivation plus bounded independently checked experiments; not peer-adopted, formal, or novelty-cleared.**

## 1. Original target and what this actually changes

The source-bound original problem asks whether, for **every finite group G of order n** and **every actual word** `g_1,…,g_(2n−1)`, there are indices `i_1<⋯<i_n` with

`g_(i_1)⋯g_(i_n)=1`

in THAT increasing-index order. The canonical book transcription is `mathematics/olson-ordered-egz/source/problem.zh.txt`; the latest owner direction authorizes new source/compute work without treating historically held outcomes as accepted premises.

This packet delivers three distinct items:

1. An exact small-group experiment and a uniformly proved counterfamily to a tempting **local exchange-diversity premise**. It is NOT an avoiding word or a disproof of the original assertion.
2. A fully proved all-prime mixed-order extension criterion, including the explicit previously unlisted rank-two boundary `p≥5`: every group with normal `C_p×C_p` and quotient `C_2` satisfies the original ordered assertion, without assuming a split extension or a particular involution action.
3. A word-dependent binary-quotient improvement when the number of chronological quotient pairs is sufficiently large; this remains a conditional WORD-class statement, not a proof for every remaining dihedral word.

The general short-kernel/chunk implication was already written-supported by the previous w42 parent gate; see `dispositions/math-2-short-kernel-mixed-prime-transport-parent-v1.md` SHA256 `c7ee97b515bb0898f8f386cef300ff4ce23bf64e47e0ea0c663dd37a8948e3a5`.
The proof below independently reconstructs its required elementary-abelian and prime-quotient inputs and specializes the exact inequality to an explicit rank-two mixed-prime class that the earlier stated `m≥3`, index-two corollary did not list.
**This is a transparent consequence/specialization of that accepted general transport lemma, not a claim to have invented it or established priority.**
The ordered finite-p-group existence theorem is already public prior; this packet does not count reproducing it as frontier progress.

## 2. Exact local premise falsified in actual nonabelian groups

For any odd prime p and d≥1, take the actual group

`G=F_p^d ⋊ C_2`,
`(v,e)(w,f)=(v+(-1)^e w,e+f mod 2)`.

Its normal elementary-abelian kernel is V=F_p^d; every `(x,1)` is a reflection. For three pairwise distinct reflection values `(v,1),(w,1),(u,1)` IN THAT ORDER, their three increasing-index pair products are

`(v−w,0), (v−u,0), (w−u,0)`.

The first and middle products can coincide only when w=u; the middle and last only when v=w. Thus, for pairwise distinct v,w,u, the **only** possible collision is

`v−w=w−u  iff  v+u=2w`.

If it occurs, there are exactly TWO, not three, distinct kernel products. The common middle-value condition is both NECESSARY and SUFFICIENT. All equations are in the ACTUAL vector kernel; each selected pair is in original increasing order.

The tempting premise **“three distinct reflections in a quotient-identity triple always give three distinct ordered pair products” is false**, uniformly: choose ANY x and ANY nonzero a and take

`v=x, w=x+a, u=x+2a`.

For every odd p these are three distinct actual reflection values, while the first and last pair products both equal `−a`; the other equals `−2a` and is different. This supplies a whole counterfamily, not just a selected finite test.

To embed it in an ORIGINAL full-length word, put those three actual reflections first and fill all remaining positions with group identities. The word has `2|G|−1` occurrences. The two colliding pairs remain actual increasing-index pairs. The padded word also has enough identity letters for an original `|G|`-occurrence selector, so it is NOT an ordered-Olson counterexample.
This falsifies only the diversity/exchange premise; it does not show that another chosen pair or another transport method cannot work.

### Exact bounded checks of this premise

The standalone producer exhaustively enumerated ALL ordered pairwise-distinct reflection triples for two bounded domains. An independent checker, importing none of the producer's code, recomputed their group products and counts:

| Actual domain | Distinct ordered triples | Triples with collision |
|---|---:|---:|
| `p=3,d=2` | 504 | 72 |
| `p=5,d=2` | 13,800 | 600 |

The checker verified for EVERY enumerated triple that collision is equivalent to `v+u=2w` and that the number of distinct pair products is respectively two or three. The counts agree with the independently derived count `p^d(p^d−1)` for colliding triples: choose v and a nonzero difference a.

A saved concrete `p=3,d=2` actual witness is `v=(0,0),w=(0,1),u=(0,2)`; the three ordered-pair products are `(0,2),(0,1),(0,2)` in the translation kernel. The saved JSON retains the actual values, group-bit labels and original zero-based pair indices. The uniform proof above, not these two finite runs, establishes the all-p statement.

## 3. An independently proved sharp short-selector theorem for an elementary kernel

Let V=F_p^d for ANY prime p and integer d≥1. Put

`m=|V|=p^d`, `D=d(p−1)`.

**Lemma A.** Every actual V-word of length `m+D` contains exactly m entries whose sum is zero. Moreover the number of such m-index subsets is congruent to1 modulo p. The threshold is sharp: there is a length `m+D−1` word with no such subset.

Because V is abelian, the sum of those selected entries agrees with their increasing-original-index product under the additive group law. Occurrence labels/repetitions remain distinct.

### 3.1 Finite-field zero-count lemma

If f_1,…,f_r are F_p-polynomials in L variables with `sum deg f_i<L`, the number of common field zeros is divisible by p. Omit an identically zero equation from the degree sum.

For any t∈F_p, t^(p−1) is0 at0 and1 otherwise. Thus `H=∏(1−f_i^(p−1))` is the common-zero indicator in F_p. Its degree is less than L(p−1), so every monomial has a variable exponent e<p−1. The full sum of that variable's e-th powers is0 in F_p: for e=0 it is p, while for0<e<p−1 choose a nonzero scalar a with a^e≠1 by the degree-e polynomial root bound and use the scaling bijection t↦at. Hence each monomial sums to0 and the count is0 modulo p. This is a written proof; the finite sums are not the experiment's numerical verification of the theorem.

### 3.2 Integer-cardinality equations and BOTH actual directions

Let `x_1,…,x_L` be an actual V-word with L=m+D, and let t_i∈F_p, `z_i=t_i^(p−1)∈{0,1}`.
For j=0,…,d−1 impose

`σ_(p^j)(z_1,…,z_L)=0`,

and for each of the d vector coordinates impose

`∑_i (x_i)_r z_i=0`.

Here σ_s is the elementary symmetric polynomial of degree s.
At a field assignment with support size w, σ_(p^j)(z)=binomial(w,p^j) modulo p. If w=∑_j w_j p^j, the identity

`(1+T)^w=∏_j(1+T^(p^j))^(w_j)` in F_p[T]

shows that coefficient of `T^(p^j)` is exactly the j-th base-p digit w_j: lower digits together have degree at most p^j−1 and higher digits contribute only greater degrees.
Thus all d cardinality equations say `m|w`.
The binomial expansion of `(1+(p−1))^d` gives `D≤m−1`, hence `L=m+D≤2m−1`. Therefore w is either0 or EXACTLY m.
The vector equations are exactly the actual sum-zero condition for that support.

After substituting z_i=t_i^(p−1), the sum of degrees of the cardinality equations is

`(p−1)∑_(j=0..d−1)p^j=m−1`,

and the vector equations cost d(p−1)=D. Their total is at most `m−1+D=L−1<L`, so the zero count C is divisible by p.
The empty support contributes exactly one assignment. Every actual m-index zero-sum subset contributes exactly `(p−1)^m` assignments, and every nonempty common zero arises from exactly such a subset. Thus

`C=1+A(p−1)^m`.

For odd p, m is odd; for p=2, −1=1 in F_2. In both cases `(p−1)^m≡−1 (mod p)`, so `A≡1 (mod p)` and A≥1. The field-to-word and word-to-field directions are both explicitly paid.

### 3.3 Sharpness — no universal one-position shortening

Take m−1 copies of 0, followed by p−1 copies of each standard basis vector e_j, j=1,…,d. This is an ACTUAL word of length

`m−1+d(p−1)=m+D−1`.

In any zero-sum subset, each basis-vector multiplicity must be divisible by p but is between0 and p−1, so every such multiplicity is0. Only m−1 zero occurrences remain; no zero-sum subset can have m occurrences.
Hence Short(V,D−1) is FALSE for EVERY p,d, while Lemma A proves Short(V,D).
The finite `p=3,d=2` check independently examined all 220 nine-index subsets of the resulting 12-occurrence word and found zero zero-sum selectors; adding one extra zero supplies a checked positive control. This finite check is NOT the proof of sharpness.

The exact elementary-abelian threshold is a known classical abelian result: the public source [Qu, *The Erdős–Ginzburg–Ziv theorem for finite groups*, Lemma 2.2(i)](https://arxiv.org/html/2610.26122v1) states the corresponding abelian constant. Its general nonabelian sequence convention permits reordering, as the paper's abstract explicitly says, so it is NOT an ordered nonabelian theorem. No novelty for Lemma A is claimed.

## 4. Prime cyclic quotient selector, proved without reordering

Let q be ANY prime. For every actual word of `2q−1` elements in C_q there are exactly q increasing-index entries with sum0.
This is the classical cyclic EGZ case, proved here for a self-contained bridge rather than accepted from a numerical run.

Write its actual entries as a_i∈F_q. With t_i∈F_q and z_i=t_i^(q−1), impose

`∑ z_i=0`, `∑ a_i z_i=0`.

The degree sum is at most2(q−1)<2q−1, so the zero-count lemma applies.
The first equation forces the integer support size to be a multiple of q between0 and2q−1; it is0 or q.
The second is its actual sum. As before, zero-count congruence forces at least one q-support solution. For the abelian quotient, increasing original order is maintained without any permutation.
The same proof includes q=2; it uses no selected q or external theorem as a correctness input.

## 5. Uniform mixed-prime bridge for all normal elementary kernels

**Theorem B.** Let p and q be DISTINCT primes, d≥1. Let G be ANY finite group with a normal subgroup K isomorphic to `C_p^d` and quotient `G/K≅C_q`. Put m=p^d, n=qm.
If

`(2q−1)d(p−1) ≤ p^d−1`,                                      (★)

then **EVERY original word in G of length2n−1 has an increasing-index identity selector of EXACTLY n actual occurrences**.

No action, semidirect-product presentation, splitting, conjugacy class, group exponent or global nilpotency assumption is added.

**Proof.** Put D=d(p−1). The inequality is precisely

`(m+D)(2q−1) ≤ 2qm−1=2n−1`.

Take ANY actual input word. Partition its first `(m+D)(2q−1)` occurrences into m+D consecutive chunks of length2q−1; discard nothing needed later except unused positions beyond those chunks.
In each chunk apply §4 to the ACTUAL quotient word, retaining q ORIGINAL increasing indices whose quotient product is1.
Their products in G are actual elements of K. Chunks are chronologically separated, so ANY increasing selection of these packets concatenates in precisely the same original order as their union.
Use an ACTUAL isomorphism K≅F_p^d, and apply Lemma A to the resulting m+D kernel products. It yields exactly m packet indices whose product in K is1.
Their union consists of exactly mq=n DISTINCT original occurrences. Its chronological G-product equals that packet product and is identity. ∎

This is an actual mixed-prime original-object bridge. It does NOT assert the conclusion if (★) fails, and it does not turn disjoint interleaved packets into separated ones by an unproved flattening step.
The universal implication itself is independently proved above and was already implicit in the earlier w42 transport+elementary-kernel gate; no novelty beyond the explicit scope is asserted.

### 5.1 Explicit rank-two mixed-prime class, including the boundary

For d=2, (★) is equivalent by cancellation of the positive factor p−1 to

`p+1 ≥ 2(2q−1)`, i.e. `p ≥ 4q−3`.

Thus, for ANY distinct primes p,q with `p≥4q−3`, EVERY extension having normal `C_p×C_p` and quotient `C_q` satisfies the full original ordered assertion.
In particular q=2 and EVERY prime p≥5 are covered; equality occurs at the p=5 boundary.
This includes all involution actions and also nonsplit presentations as given; the proof did not use a splitting theorem.

A concrete nonabelian family within the proved class is `G=F_p^2⋊_{−I}C_2`, p≥5. It is not a p-group. It is nonnilpotent: the conjugation action gives `[V,C_2]=V`, since multiplication by2 is invertible on V, so the lower central series remains at V rather than reaching1. This qualification uses the actual group action, not an asserted category based merely on its order.

### 5.2 A simple unbounded-rank sufficient condition

The exact criterion remains (★). A coarser transparent sufficient condition is

`(d−1)(p−1) ≥ 4(q−1)`.

Indeed `(1+(p−1))^d−1 ≥ d(p−1)+binom(d,2)(p−1)^2`, and the displayed condition makes the latter at least `(2q−1)d(p−1)`.
Thus for every fixed distinct p,q the theorem applies to all sufficiently large elementary-kernel ranks. This is an explicit ordinary sufficient subrange, not claimed optimal.

## 6. A word-dependent index-two extension when the uniform budget fails

Let G be ANY group with a normal K of index2, k=|K|, and suppose the actual kernel property Short(K,D) is proved for some0≤D≤k−1.
For an ACTUAL binary quotient word of length `4k−1`, make consecutive blocks greedily from left to right:

- if the next two quotient letters agree, use those two occurrences as the block's pair and consume2 positions;
- otherwise, if a third position exists, at least two of the three quotient letters agree; use the lexicographically first equal pair and consume all3 positions;
- stop when the remaining tail has at most2 unequal letters or fewer than2 positions.

This is a mathematical construction on the actual sequence, not a claim that a program was used to check all such words. Every selected pair has quotient product1 and every block is chronologically separated.
Let a be the number of consumed2-position blocks, b the number of consumed3-position blocks, t=a+b and r∈{0,1,2} the actual tail length. Then

`4k−1=2a+3b+r=3t−a+r`.

**Theorem C.** If `t≥k+D`, equivalently for THIS actual greedy decomposition

`a ≥ 3D−k+1+r`,

then the original G-word has an increasing-index identity selector of exactly2k occurrences.

**Proof.** Take the first k+D separated quotient-identity pairs. Their actual G-products lie in K. Short(K,D) selects k of those packet products with product1. The original union has exactly2k indices in their actual increasing order, with identity product. ∎

This is genuinely word-dependent: it can apply even when the all-word condition `3D≤k−1` fails, provided that actual quotient word has enough two-position blocks.
It is not an existence theorem for ALL binary quotient words. For an alternating quotient word, every equal-letter pair spans at least3 positions, and the maximum number of separated pairs is `floor((4k−1)/3)`; selecting the first and third positions of successive3-position chunks attains it. Thus the unfavorable alternating family shows why greedy/separated extraction alone does not remove the original general bridge.
For cyclic prime kernel k=p and D=p−1 this remains a restricted word class and does NOT establish all `D_(2p)` words.

## 7. Actual scientific experiment and independent checker

Both programs are NEW standalone standard-library Python scripts in this root. They use integer modular group arithmetic, no external package and no floating point.

| Artifact | SHA256 | Exact role |
|---|---|---|
| `frontier-20261028-ordered-bridge-experiment.py` | `cd2ad31893396d7e044f1a9dbefd64ebb97816f810939b6394823fe2f327bae3` | bounded producer: reflection triples, sharp-kernel finite word, actual ordered-selector corpus |
| `frontier-20261028-ordered-bridge-checker.py` | `97d607d853d2adff1b9ea022a6dc7d1058a7149001446c06639a0af6e892b1ef` | separate implementation; imports NO producer code; checks saved original words/indices/products and recounts finite assays |
| `frontier-20261028-ordered-bridge-experiment-results.json` | `864a930c187c73791ce68e5fe9c8aa535fbf781c70938f36d87185a97d37e480` | complete saved words, choices, local counterexamples, results and seed |

The producer created a new result file without overwriting an existing artifact. On the single bounded run it reported:

- reflection triples: p=3,d=2, **504 total/72 collision**; p=5,d=2, **13,800 total/600 collision**;
- sharp elementary-kernel finite obstruction: **220** actual nine-subsets checked, **0** zero-sum, plus the explicit one-extra-zero positive control;
- **30/30** complete actual words of length99 over groups of order50 produced actual strictly increasing 50-index identity selectors. The corpus includes seeded random inputs and alternating, all-reflection, all-kernel and constant patterns, across the involutions `−I`, `diag(−1,1)` and identity on F_5². The seed is20261028.

The independent checker then returned `PASS_BOUNDED_CHECKS` on the SAME result SHA above. It recomputed every actual original-order group product, word hash, selector length/index order, selected quotient-block identities and finite triple counts. Four deliberate corruptions were rejected for the intended reasons: duplicate indices, out-of-range index, falsified stored product, and quotient pair outside its actual block.

For example, the saved first `−I` alternating word has SHA256 `77454271a14199afa6dda8ebd456605484312a6c8c2da95771d4958d2277bd6e`; the result JSON preserves its whole99-letter actual word and all50 zero-based selected indices. The checker directly multiplied them in their saved increasing order and obtained identity. This is one checked selector in a small experiment, NOT a proof of Theorem B or an independently certified counterexample to Olson.

## 8. Prior, remaining gap and assurance

The exact classical kernel threshold and prime cyclic theorem are NOT claimed new. The current parent w42 already supported the general Short(K,D) transport, so Theorem B is explicitly presented as an independently reconstructed specialization with new explicit scope/word-dependent accounting, not as an independently novel discovery.
The bounded public screen located [Qu's nonabelian Gao-constant paper](https://arxiv.org/html/2610.26122v1), which DEFINES product-one sequences using some permutation. Its conclusion must not be transferred to original-index order. That screen does not establish whether the displayed mixed-prime class is new or whether the all-finite-group ordered problem is currently open worldwide.

No actual original avoiding word, all-mixed-prime theorem, all-finite-group theorem, optimal universal nonabelian threshold, or novelty is claimed.
If (★) fails or the given quotient word fails Theorem C's sufficient count, the theorem says NOTHING about existence or nonexistence of an original selector.
The old class-two p-group existence claims remain PRIOR/REPRODUCTION; separately held historical assessments are NOT accepted as premises or retroactively rehabilitated. The current proof and exact checks stand or fail on their displayed reasoning/data.

The latest owner addendum permits bounded local scientific computation prospectively; no old process violation is rewritten. This packet did not use an external model/paid API, alter infrastructure, delete files, publish or push Git. No independent model-family or human review was performed.
The only external mathematical source used here for PRIOR context is the cited public arXiv paper; all correctness arguments above are inline.
For any claimed FINITE COUNTEREXAMPLE to the ORIGINAL conjecture or gate-level witness, the stronger independent-witness protocol would still be needed. The finite objects here refute only the local exchange/shortening premises and the checked selectors attest only their supplied actual words.

**END — exact exchange-premise refutation, original-order mixed-prime bridge, and bounded checker evidence.**
