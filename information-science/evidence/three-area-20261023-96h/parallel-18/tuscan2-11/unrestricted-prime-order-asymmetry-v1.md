# Unrestricted prime-order rigidity: no symbol or reversal automorphism

Observed `/bin/date` before creation: **Sun Oct 25 04:42:11 PDT 2026**. Owner `InfoRecursiveMDS18`, slot info-4. Developed after completing assigned review v31-D. **WRITTEN / CANDIDATE / NOVELTY_UNCLEAR.** No scientific interpreter, arithmetic program, enumeration, symbolic computation, certificate replay or solver was launched. This is a structural result about ALL hypothetical target arrays, not a construction or an all-array nonexistence proof.

Mandatory admission qualification: [kernel-admission-correction-addendum-v1.md](kernel-admission-correction-addendum-v1.md). No earlier unadmitted finite output is a premise below.

## 1. Precise symmetries and theorem

Let A be a Tuscan-1 square of odd order n>=3: n row permutations on an n-symbol set X, with every ordered distinct adjacent pair covered once. Treat its rows as a set R; they are distinct.

A **symbol automorphism** is a permutation g of X whose simultaneous application to every row preserves R as a set. A **reversal-symbol automorphism** simultaneously reverses EVERY row and applies one common symbol permutation g, again preserving R. Arbitrary row reordering is absorbed by using a row set. Independent row reversals and arbitrary column permutations are not included.

**Theorem.**

1. At every odd order n, no reversal-symbol automorphism exists.
2. If n is an odd prime p, there is no nonidentity symbol automorphism either.
3. Consequently every unrestricted Tuscan-2 square of order11, if one exists, has trivial automorphism group under the safe symbol/row/global-reversal equivalences just described.

The first conclusion uses adjacency coverage only. The second extends the classical odd cyclic-starter sum obstruction to EVERY possible symbol automorphism, rather than imposing a cyclic development. No Latin-column or distance-2 condition is needed. The classical cyclic-starter calculation itself is not claimed as new.

## 2. Endpoint count and free action on rows

For each symbol a, let e(a) be the number of rows ending in a. Each of its n row occurrences has an outgoing adjacent arc except the terminal ones. Exact adjacent coverage has n-1 outgoing arcs from a, hence

`n-e(a)=n-1`, so `e(a)=1`.

The incoming count similarly proves that every symbol starts exactly one row. This is a genuine unrestricted consequence, not a Latin-column assumption.

Let G be the finite symbol-automorphism group. If g fixes one row as an ordered tuple, it fixes every entry of that row. Since the row contains every symbol, g is the identity. Thus G acts freely on the n-element row set, and

`|G| divides n`.  (1)

In particular |G| is odd. Equivalently, a nonidentity g cannot fix a symbol: that would preserve the unique row starting there and hence fix the whole row. No extra regularity is assumed at this step.

## 3. Reversal is impossible at every odd order

Let K be the group of all symbol/global-reversal automorphisms of R. Projection onto the reversal bit has kernel G. If any reversal-symbol automorphism exists, that projection is onto and

`|K|=2|G|`.

By the elementary Cauchy theorem, K then contains an element of order two. Since G has odd order by(1), this involution is outside G and has the form (h,reversal), with `h^2=id`.

Consider the bijection from adjacency events `(row,c)`, c=0,...,n-2, to ordered distinct pairs. Under this involution:

- an event position c becomes `n-2-c`;
- its ordered symbols (a,b) become `(h(b),h(a))`.

Because n is odd, n-2 is odd. No integer event position satisfies `c=n-2-c`. Thus **no adjacency event is fixed**, regardless of whether its row is preserved or exchanged.

If h has a transposition(a b), the ordered pair(a,b) is fixed by the symbol/reversal operation:

`(h(b),h(a))=(a,b)`.

Its unique covering event would therefore have to be fixed, by equivariance of the coverage bijection. That is impossible. An involution with no transpositions is the identity, so h must be the identity.

The putative order-two automorphism is now pure global reversal. On an odd number of rows an involution must fix a row. But a row permutation equal to its reversal has equal first and last symbols, impossible for n>=2. This final contradiction proves conclusion1.

This argument is not a count of selected arrays. It excludes every reversal-symbol symmetry of any unrestricted odd-order Tuscan-1 square.

## 4. Prime-order symbol rigidity

Now let n=p be an odd prime. By(1), a nontrivial G would have order p and be cyclic. It acts freely on the p symbols and p rows, hence regularly on both.

Choose its generator and label symbols by F_p so that the generator adds1. All rows are then the p translates of one row

`a_0,a_1,...,a_(p-1)`.

For a fixed nonzero difference delta, its directed arcs `(x,x+delta)` form one orbit of size p under translation. Therefore exact adjacent coverage requires the p-1 starter differences

`a_(j+1)-a_j`, j=0,...,p-2,

to enumerate every nonzero element of F_p once. Their sum is zero, because p is odd:

`sum_(delta!=0)delta=p(p-1)/2=0 in F_p`.

But telescoping gives that same sum as `a_(p-1)-a_0`, which is nonzero in a row permutation. Contradiction. Thus G is trivial, proving conclusions2 and3.

For order11, a proposed row set invariant under any nonidentity symbol permutation is therefore impossible already at Tuscan-1. This includes exact multiplicative/QR/power orbit symmetry when imposed on the complete eleven-row set, and not just an explicitly translation-developed starter. It does **not** exclude arbitrary asymmetric mixtures of rows selected from structured families.

## 5. Exactly22 distinct safe standard forms at order11

There is a useful canonicalization consequence for future unrestricted written or separately admitted search.

For each of the eleven rows r and each of the two global orientations epsilon:

1. Reverse all rows if epsilon=1.
2. Apply the unique global symbol relabeling taking the chosen oriented row r to `(0,1,...,10)`.
3. Order rows by their first symbol, which is legitimate by the endpoint count.

This gives a standard-form array with row0 natural and first column natural. **The22 arrays are pairwise distinct.** If two choices produced the same array, composing their inverse relabelings/orientations would give an automorphism of the original row set. The theorem makes that composition the identity; the global orientations must coincide, and the selected row must be the same because the relabeling is fixed entry-by-entry.

Conversely, every standard form of the same row/symbol/global-reversal equivalence class arises this way: its natural row0 identifies a row and global orientation of the original set, and fixes the relabeling uniquely. Thus22 is exact, not merely an upper bound.

Taking the lexicographically least of these22 forms is consequently a sound unrestricted canonical representative. It does not justify an arbitrary column permutation, an independent row reversal, a Latin middle column, a cyclic row family, or any particular second row. This is a proved symmetry interface, not a new executed search or a claim about the number of solutions.

## 6. Remaining target

This supplies an unrestricted structural obstruction to ALL nontrivial safe automorphisms and a precise canonicalization rule. It does not imply that an asymmetric Tuscan-2(11) array cannot exist.

The full criterion remains unmet: an actual eleven-by-eleven integer table with110 distinct linear adjacency pairs and99 distinct linear distance-2 pairs, or a proof covering every asymmetric arbitrary-row array as well. All previous search cutoffs remain UNKNOWN; no finite computation or earlier inadmissible certificate replay is used to upgrade that status. Separate written reconstruction, parent disposition and priority review of this theorem remain pending.
