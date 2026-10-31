# Two triangle-syndrome classes cannot beat the q=8 triangle code

**Status: WRITTEN, conditional on the pinned triangle-code conflict bound; scientific review pending.** Fix the same q=8 component-bit labeling and ten-triangle code `W0` as in `frontier-20261028-triangle-code-trade-barrier-v1.md` SHA-256 `34b647fe99c3b03bb15553074e44c7154716ec40d0368f5078aab2dda4856e8b`. Let the ten-bit triangle syndrome of a word be its ten factor XOR parities. Any original-FD-consistent support contained in the union of **two** syndrome classes has at most `2^20` words. Therefore a q=8 fixed-point set strictly larger than the standard code must meet **at least three distinct syndrome classes**.

This is a cardinality statement in the fixed component encoding. It does not show that all such two-class supports have nonpositive entropy-balance gap under arbitrary reweighting, nor does it rule out a larger support meeting three or more classes.

## Proof

The q=8 ambient word space is `F_2^30` with the fixed factor-bit labels. The ten syndrome bits are independent linear parity maps, so every syndrome class is a coset of the 20-dimensional code `W0` and contains exactly `2^20` words. The original-neighbour confusability graph is invariant under bitwise translation: equality or inequality at any coordinate is unchanged by adding the same ambient word.

Take two distinct classes `W_s,W_t`. Translations by codewords in `W0` act transitively on each class and preserve confusability, so the bipartite graph of conflicts between them has the same degree `d` on every vertex of either side. The prior 68-conflict result makes `d>=68>0`, after translating one class to `W0`.

Let `A` be the part of an FD-consistent support in `W_s`, and let `N(A)` be its conflict neighborhood in `W_t`. Counting edges from `A` to `N(A)` gives `d|A|<=d|N(A)|`, hence `|N(A)|>=|A|`. The support's part in `W_t` avoids `N(A)`, so

\[
|A|+|W'\cap W_t|\le |A|+2^{20}-|N(A)|\le2^{20}.
\]

The same conclusion covers a support in a single class. Since the q=8 strict fixed-point threshold is `8^(20/3)=2^20`, beating it requires at least three syndrome classes. No formal proof, independent scientific review or unrestricted guessing-number claim is made.
