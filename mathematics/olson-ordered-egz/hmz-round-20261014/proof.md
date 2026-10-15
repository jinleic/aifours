# Olson's ordered EGZ conjecture: unresolved research round

**Status: no proof and no counterexample. `full_goal_solved` is false.**

The unchanged target is: for every finite group $G$, with $n=|G|$, and every
list $a_1,\ldots,a_{2n-1}$, some indices

\[
1\le i_1<\cdots<i_n\le 2n-1
\quad\text{satisfy}\quad a_{i_1}\cdots a_{i_n}=1.
\]

All products below respect the original index order. None of the partial
results below is submitted as a resolution. There is no `Formal.lean` or
`certificate.json`, because neither required full theorem has been obtained.

## Prior-art boundary

[Dimitrov (2004), pp. 129--131](https://www.math.bas.bg/infres/MathBalk/MB-18/MB-18-129-140.pdf)
explicitly proves the ordered conjecture for finite p-groups. His subsequent
solvable-group corollary permits rearrangement. The local recovered OCR was
read; the ordered and unordered conclusions were kept separate. No p-group
case was re-proved or claimed as new here.

[Agarwal--Lou (2016)](https://digitalcommons.imsa.edu/sir_presentations/2016/oralsession1/55/)
already reports the odd-dihedral lower bound $4m-1$. The word

\[
r^{[2m-1]}s^{[2m-1]}
\]

has $4m-2$ terms, one too few to refute the conjecture for a group of order
$2m$. Bracketed exponents here and below denote repetitions in a word, rather
than a single powered group element.

The exact ordered formulation was also checked on
[Mohar's problem page](https://www.sfu.ca/~mohar/Problems/P0604_OlsonConjecture.html).
The limited literature search in this round did not recover an all-groups
solution. This is not an exhaustive prior-art or current-open-status claim.

## Why two attempted proof routes did not close the problem

**Interleaved quotient blocks.** Use

\[
\mathrm{Dic}_3=\langle r,s\mid r^6=1,\ s^2=r^3,
\ srs^{-1}=r^{-1}\rangle,
\qquad N=\langle r\rangle.
\]

In the word $(s,r,s^{-1},r^{-1})$, the sublists with indices $(1,3)$ and
$(2,4)$ each have product $1\in N$. Multiplying their two block products
therefore gives $1$. Their increasing-index union has product

\[
srs^{-1}r^{-1}=r^{-2}=r^4\ne1.
\]

`audit_interleaving.py` evaluates this word and both pairs directly from
the saved table. Its complete output is in `interleaving-audit.log`.

Thus an induction which concatenates the products of interleaved selected
blocks has an invalid lifting step, even when both block products are already
the identity. This four-term example is an obstruction to that step, not a
counterexample to the target statement of length 23.

**Direct extension of augmentation-ideal nilpotence.** In
$\mathbb F_2[\mathrm{Dic}_3]$, for every integer $j\ge0$,

\[
(r-1)^{2^j}=r^{2^j}-1\ne0.
\]

The equality follows by repeated squaring in the cyclic subalgebra generated
by $r$. The inequality holds because $r$ has order 6 and $6\nmid 2^j$, so
the two group-basis elements differ. Consequently the augmentation ideal is
not nilpotent. The nilpotence property used in the known p-group approach
cannot simply be assumed in this non-p-group. No replacement algebraic
argument establishing the all-groups target was found.

Over $\mathbb F_3[\mathrm{Dic}_3]$, $s$ has order 4, so likewise
$(s-1)^{3^j}=s^{3^j}-1\ne0$ for every $j\ge0$.

## A cancellation obstruction used to focus the search

Let $u,v$ be elements of any group, with $u^2=v^2=z$, where $z$ commutes
with both $u$ and $v$. For every integer $h\ge0$, every word of length
$2h+1$ on the alphabet $\{u,v\}$ has a sublist of length $2h$ whose
product is $z^h$.

To prove this, first work with the two formal letters. Every odd-length
binary word allows one letter to be deleted so that the remaining word can
be reduced to the empty word by successively removing adjacent equal pairs.
Induct on its odd length. If an adjacent equal pair is present, remove it,
apply induction, and reinsert that pair. If no equal pair is present, the
word alternates; deleting its middle letter allows cancellation from the
middle outwards. This also covers the one-letter base case. On evaluation
in the group, each removed pair contributes $z$; centrality allows the
$h$ contributions to be collected, giving $z^h$.

In $D_7$, two reflections have common square 1. Thus any 15 occurrences
of just two reflection types already give a 14-term ordered identity
sublist. In $\mathrm{Dic}_3$, two elements of $\langle r\rangle s$
have common square $r^3$, central of order 2. Any 13 such occurrences
of just two types give a 12-term identity sublist, since $(r^3)^6=1$.
These observations explain an unproductive basin in the heuristic search.
They are elementary partial obstructions; no originality claim is made.

## Counterexample assays and independent checks

The presentation tables use elements $r^a s^b$, encoded as $a+qb$,
with $0\le a<q$ and $b\in\{0,1\}$. For $\mathrm{Dic}_3$, $q=6$
and $s^2=r^3$; for $D_7$, $q=7$ and $s^2=1$. The $A_4$ table uses
lexicographically ordered even permutations of four points.

`structured_search.cpp` used exact integer counts of increasing-index
identity subsets as its objective. After an initial 90-second assay for
each group, a second 120-second assay excluded every word containing $n$
copies of a letter. Such words cannot be counterexamples by Lagrange's
theorem. The initial source, logs and best words are preserved in
`initial-assay/`; the second source and logs are at the repository root.
Every single-letter insertion into every word $a^{[n-1]}b^{[n-1]}$,
for $a\ne b$, was covered before heuristic mutations. Subsequent
mutation searches were not exhaustive over all words.

`audit_best.py` separately checked the complete group axioms, the exact word
lengths, and independent faithful representations: $A_4\le S_4$, the
natural action of $D_7$ on seven points, and

\[
r=\begin{pmatrix}3&0\\0&5\end{pmatrix},\quad
s=\begin{pmatrix}0&1\\6&0\end{pmatrix}
\quad\text{in }\mathrm{GL}_2(\mathbb F_7)
\]

for $\mathrm{Dic}_3$. It enumerated **every raw increasing-index subset**
of the required size in each saved best word and compared the full product
histograms with a separately implemented count DP and the C++ objective.

| Group | Required word length | Raw subsets checked | Identity subsets |
|---|---:|---:|---:|
| $\mathrm{Dic}_3$ | 23 | 1,352,078 | 33 |
| $A_4$ | 23 | 1,352,078 | 3,066 |
| $D_7$ | 27 | 20,058,300 | 3 |

The exact words, tables, histograms and identity indices are in
`*-search-best.json` and `raw-audit.json`. Each saved word is explicitly
**not** a counterexample. The frozen certificate checker independently
rejects each on an actual ordered identity subset. The one-short $D_7$
control is rejected for having length 26 instead of 27.

A second assay exhaustively covered the following restricted family in
both presentation groups. Fix the rotation generator $r$, let $n=|G|$,
let $1\le k\le4$, and consider

\[
r^{[a_0]}(r^{v_0}s)^{[b_0]}r^{[a_1]}\cdots
(r^{v_{k-1}}s)^{[b_{k-1}]}r^{[a_k]},
\]

where all $a_i\ge0$, all $b_i\ge1$, all $v_i\in\mathbb Z/q\mathbb Z$,
and $\sum a_i+\sum b_i=2n-1$. The automorphism $r\mapsto r$,
$s\mapsto r^{-v_0}s$ normalizes $v_0=0$.

Here are the exact analytic pruning rules. Write $R=\sum a_i$ and
$F=\sum b_i$. If $R\ge n$, select $n$ copies of $r$. If $R\le n-4$,
then $F\ge n+3$; at most four constant reflection blocks have capacity
$\sum 2\lfloor b_i/2\rfloor\ge n$. Choosing even counts totalling $n$
gives product $1$: the common squares contribute $1$ in $D_7$ and
$(r^3)^6=1$ in $\mathrm{Dic}_3$. The capacity inequality at $F=n+3$
uses its odd parity, so at most three block counts are odd. Larger $F$
gives the inequality directly. Thus only $n-3\le R\le n-1$ needs enumeration.

For two reflection blocks with offsets $v_p,v_h$ and $T$ rotations
between them, selecting $n-2$ rotations and one reflection from each
block gives exponent

\[
(n-2)-2j+v_p-v_h+c\pmod q,
\quad
\max(0,n-2-(R-T))\le j\le\min(n-2,T),
\]

where $c=0$ for $D_7$ and $c=3$ for $\mathrm{Dic}_3$. A zero
exponent therefore excludes that candidate. Remaining words were checked
by ordered-product set DP. Reflection-only identity sublists were also
checked before enumerating rotation placements.

`D7-run-general.log` covers 679,801,252 normalized parameter tuples in
the remaining $R$ range; `Dic3-run-assay.log` covers 142,418,199. These
counts include duplicate words. Both assays completed without timeout or
a counterexample, within 28 and 6 seconds respectively. Earlier $R=13$
$D_7$ assay evidence is preserved separately. These are restricted-family
computer exclusions, not exhaustive checks of either group, formal proofs,
or evidence for the universal quantifier over all finite groups.

## Five reflection blocks

After the scope review, one further exact assay extended the same family to
exactly five reflection blocks. No additional mutation search was run.
`five_block_assay.cpp` keeps the old even-capacity and reflection-only
filters ahead of rotation-placement enumeration. Both runs had a 270-second
limit and finished within that limit.

Reproduce with:

```sh
clang++ -std=c++17 -O3 -Wall -Wextra five_block_assay.cpp -o five-block-assay
./five-block-assay Dic3 270
./five-block-assay D7 270
```

The new symmetry reduction is justified by cyclic cuts. If a selected
sublist has products $U$ before a cut and $V$ after it, its cyclic image has
product $VU=U^{-1}(UV)U$. Thus cyclic cuts preserve both existence and count
of ordered identity sublists of each fixed length. Moving the leading
rotation segment to the end merges it with the trailing segment. The five
remaining rotation gaps therefore form a weak composition of $R$ into five
parts. As before, normalize the first reflection offset to zero.

For a fixed reflection pattern, consider all five cyclic shifts of its
block lengths and offsets, subtracting each new first offset. Keep a
lexicographically minimal sequence of pairs $(b_j,v_j)$. Any discarded
pattern is related to a retained one by a cyclic cut and a group
automorphism, with its rotation gaps permuted. All gap compositions are
enumerated, so this reduction preserves coverage.

For five blocks, $R\ge n$ is still immediate. If $R\le n-5$, then
$F\ge n+4$. At $F=n+4$, its even parity allows at most four odd block
counts; for $F\ge n+5$, at most five are odd. In both cases the even
capacity is at least $n$. Hence only $n-4\le R\le n-1$ remains.

| Group | Remaining $R$ | Parameter tuples | Full-word DP checks | Seconds |
|---|---:|---:|---:|---:|
| $\mathrm{Dic}_3$ | 8--11 | 2,530,653,840 | 18,775,045 | 14.2292 |
| $D_7$ | 10--13 | 17,307,764,565 | 155,813,833 | 110.991 |

These counts use the merged leading/trailing gap and first-offset
normalization; they include duplicate words and tuples excluded by the
other filters or pattern symmetry. Both logs, `Dic3-five-block.log` and
`D7-five-block.log`, report `exhaustive=1`, `candidate=0`, `timed_out=0`.
No avoiding word or finite refutation certificate was produced.

`audit_five_block_symmetry.py` separately checked all offset maps as table
automorphisms and used count DP on 600 sampled full parameter words and
their 3,000 cyclic-cut/automorphism images. Every identity-subset count
was preserved; the output is in `five-block-symmetry-audit.log`. The final
audit, in `five-block-symmetry-audit-final.log`, additionally confirms an
identity sublist in each sampled full word. These tests check the new
optimization and are not raw-subset acceptance evidence.

Together with the earlier assay, this excludes the stated family through
five reflection blocks. More reflection blocks, other rotation letters,
general words in either group, and the all-groups conjecture remain outside
this restricted-family assertion. No new formal theorem is claimed.

## Acceptance and remaining gap

The goal is still unresolved in this round. Neither a complete all-groups
proof nor a group and word avoiding every required ordered product exists
among the produced artifacts. No full theorem root is claimed. The required
reviewer verdict is **`done:false`**.

`python3 verify.py` returned exit code 1 with
`NOT ACCEPTED: Exact full goal not claimed solved`; the output is retained in
`verification.log`. This rejection is not a successful acceptance. No Lean
scope check was run, because no full theorem was supplied. All launched
search and raw-audit processes exited; a final process check found none
remaining. The three frozen input hashes agree with the starting hashes.
