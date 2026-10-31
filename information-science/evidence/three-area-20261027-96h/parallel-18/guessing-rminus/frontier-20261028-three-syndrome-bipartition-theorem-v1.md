# A three-syndrome binary XOR support class has nonpositive gap

**Status: WRITTEN with an exact rational multi-branch Shannon/one-hot certificate; independent scientific review pending.** In the ten-triangle q=8 binary-XOR factor encoding of the original R-minus graph, let `S=(S_1,...,S_10)` be the vector of triangle parity bits. Suppose its support is contained in

\[
\{s,\ s\oplus u,\ s\oplus v\},\quad
\operatorname{supp}(u)=\{1,2,5,6,8,9\},\quad
\operatorname{supp}(v)=\{3,4,7,10\}.\tag{52}
\]

The masks `u,v` are disjoint and cover all ten factor indices. For **every** original-neighbour FD law on such a support, with arbitrary probabilities and correlations,

\[
\boxed{\quad H(X_V)\le\frac23\sum_{i=1}^{10}H(X_i).\quad}\tag{53}
\]

Consequently every such FD support has at most `2^20` words. In particular this result covers arbitrary laws supported on exactly three syndrome values of (52), not just a uniform law. It is not a general three-syndrome theorem, an unrestricted q-ary bound or a positive-gain witness. It does not depend on the separate repaired two-syndrome theorem.

## Reduction to two indicator functions

Translate each fixed factor bit so that `s=0`, without changing any entropy or graph FD. Label the three possible states by `0,1,2`; put `A=1{state=1}` and `B=1{state=2}`. On the factors indexed by `supp(u)`, parity equals `A`; on the complementary factors it equals `B`. Let `C=1{state=0}`; then `S`, `A`, `B`, `C` are deterministic functions of each other in the usual one-hot way: `S` determines each indicator and any two indicators determine `S`. The statement includes degenerate supports with a state of zero probability.

Every original-neighbour tuple determines the central vertex by the graph FD, and hence determines all factor syndromes incident to that vertex. In (52) each vertex meets at least one factor from each of the two listed groups, so every neighbourhood determines both `A` and `B`, hence full `S`. Every triangle's three vertex blocks determine its own parity indicator. Given full `S`, every local component is the XOR of its other two triangle components and the corresponding syndrome bit; therefore `H(X_i|X_{L(i)},S)=0` even at the vertices adjacent across the extra edge `3--4`.

Conditioning on the full syndrome fixes all ten triangle parities. Triangle factor tensorization gives the unconditional-gate premise

\[
3H(X_V)+17H(S)-2\sum_i H(X_i,S)\le0.\tag{54}
\]

The proof is by conditioning factor by factor on `S` and the earlier factor tuples; within each fixed-parity triple any two components determine the third. This gate holds for any number of syndrome values and does not use the two-syndrome theorem.

## One-hot inequalities and exact coefficient identity

For any conditioning tuple `X_A`, the one-hot entropy inequalities

\[
\frac53H(S\mid X_A)\le H(A\mid X_A)+H(B\mid X_A)+H(C\mid X_A)\le2H(S\mid X_A)
\tag{55}
\]

are proved in `frontier-20261028-three-state-exclusion-entropy-v1.md` SHA-256 `9c5ee203ba255776702e93e90b958663e98a43ebfb3b522b97898381116785e7` and its addendum SHA-256 `a2f68e7268f05244ffb224b457df94083e3125c4fcf545d6b149f1bcb9c853ce`; their proofs use only elementary entropy/KL and concavity. Ordinary Shannon/data-processing inequalities also give, for distinct indicators `Y,Z`, `H(Y|X_A)<=H(S|X_A)`, `H(S|X_A)<=H(Y|X_A)+H(Z|X_A)`, and `I(S;X_i|X_A)>=I(Y;X_i|X_A)`.

`frontier-20261028-three-syndrome-color-dual-v1.json` SHA-256 `bf64aff615954a609183407aee09f3fab0b556eae1758b3344aa6292579f5acd` is an exact rational identity for `Delta` as a four-automorphism average of 376 elemental CMIs, 82 indicator-refined CMIs, 38 indicator data-processing rows, 20 indicator-pair subadditivity rows, 16 one-hot inequalities, the gate (54), and 24 original-FD, syndrome-visibility or local-decoder equalities. Every nonnegative Shannon row appears with a negative multiplier, every nonpositive inequality with a positive multiplier, and the equality multipliers are unrestricted. Hence the right side is nonpositive.

The separately written checker `frontier-20261028-three-syndrome-color-dual-check.py` SHA-256 `61a2b755fab6de658c13ea116af71ed33459e732615bbd09fb1498a9252a13dc`, receipt SHA-256 `e8bd014038e208ab4d2af9eb09dc314d564b8bb8c507e1ab6823f0f6e05ca014`, validates all four graph/factor/color automorphisms, the state-visibility incidence premises, every term's sign, and cancellation of all 5,119 nonempty original/auxiliary-branch entropy coefficients with exact `Fraction` arithmetic. It rejects a changed target and a flipped CMI sign. Written justification of the one-hot inequalities, decoder, factor gate and scope remains a separate review obligation. No proof-assistant formalization, independent adoption or novelty clearance is claimed.
