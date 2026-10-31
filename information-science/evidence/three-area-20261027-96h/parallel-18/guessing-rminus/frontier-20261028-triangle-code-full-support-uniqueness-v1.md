# The uniform triangle-code law is the unique full-support equality case

**Status: WRITTEN corollary of the pinned global product-support identity; scientific review pending.** On the standard ten-triangle XOR code, every full-support probability law other than the uniform code law has **strictly negative** balance gap. For laws that omit codewords, equality can occur in other ways, including a point mass.

The global inequality and exact CMI decomposition are in `frontier-20261028-triangle-code-global-obstruction-v1.md` SHA-256 `bdf79fd631e8e58a734a4ef4c93f899e319f45712a219a876f527b52f1d61bb4`; its symbolic identity addendum is SHA-256 `9c9b77a128fc3064cb8750f1248ae8254df3b437acc44fcaf6bd8e340b9862df`. This strengthens the local `epsilon<1/5` conclusion for full-support laws to the entire probability simplex interior. It remains a **fixed-support** statement, not a general R-minus bound.

## Proof

If a full-support law has zero balance deficit, every nonnegative CMI in equation (15) of the global packet is zero. In particular, for each triangle factor and every positive-probability past-factor configuration, its three XOR-zero bits are pairwise independent.

A pairwise-independent XOR-zero binary triple is either uniform on its four allowed configurations or a point mass. To see this, write its first two independent bits as `U,V`, with success probabilities `p,q`, and let `W=U xor V`. If `U` is nondegenerate, independence of `U,W` forces `q=1/2`; if `V` is nondegenerate, independence of `V,W` forces `p=1/2`. If either input is deterministic, the other input and `W` determine one another, so their independence forces that input to be deterministic too. The only nondegenerate case is `p=q=1/2`.

Because the joint law is positive on **every** product-code word, for every past-factor configuration all four outcomes of the current triangle factor have positive conditional probability. Thus the point-mass alternative is impossible, and every factor is conditionally uniform given the whole past. Induction over the ten factors shows that the joint law is exactly the uniform product law. Conversely the uniform product law has `Delta=0`. The global inequality gives strict negativity for every other full-support law.

No claim is made for equality classifications on proper sub-supports, different codes, an unrestricted guessing-number bound, formal proof or novelty.
