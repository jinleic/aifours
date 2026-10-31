# Candidate support48/t24 exclusion of residual alphabet (5,4,4,4) by an ordered-pair parity contradiction

Owner **PhysicsAME46-2**. Native clock before writing: `Thu Oct 29 11:08:23 PDT 2026`; not an exact completion time. **WRITTEN author candidate**, not independently reviewed, adopted, formally verified or novelty-cleared. The proof is elementary counting on the support of one actual tensor, conditional on the exact-scope N48/t24 no-distance-one candidate. No solver status or finite enumeration is a premise.

## 1. Input and scope

Assume a normalized complex AME(4,6) state has `N=48`, exactly `t=24` modulus-1/6 entries P, and other support E of size24. Assume E alphabet sizes `(5,4,4,4)` at parties A,B,C,D. Each residual12×12 unitary has24 nonzeros, so every one of the six E pair projections has12 values, each with exactly two E extensions.

The sole prerequisite is the separately unreviewed N48/t24 no-Hamming-one proof in `frontier-20261029-n48-t24-noh1-and-six-alphabets-v1.md`, SHA-256 `6bbe85a8b1bec38ef5984d32408c52479ec58edeb3502398d87ab1f7e04a7c96`. It carries the named no-OLS(6) import and is not the differently scoped recorded f127 N46 lemma. The present packet does not exclude other residual profiles, other maximal counts or all support48 states.

## 2. P activity forces degrees22233 at A and3333 elsewhere

For a local E symbol a at i, the partner degree d_i(a) is j-independent and `|E_a|=2d_i(a)`. It is at least2 and the degrees at each party sum to12. Because the other alphabets have size4, A has one of

`X=(2,2,2,2,4)`, `Y=(2,2,2,3,3)`.

Let n_k count P words with k coordinates inside the E alphabets. P/E pair partition gives total active incidences `Σ k n_k=54`, total pair-active incidences `Σ C(k,2)n_k=36`, and `Σn_k=24`; hence

`n_0+n_3+3n_4=6`.                                                 (1)

For any active A symbol a, let s(a),q(a),h(a) count P words using it with respectively1,3,4 active coordinates. Subtracting its other-active incidences from its P occurrences gives

`s(a)−q(a)−2h(a)=(6−d(a))−3(4−d(a))=2d(a)−6`.                (2)

Each degree2 A symbol therefore requires `q(a)+2h(a)−s(a)=2`.

Four degree2 symbols (X) would require8, but their total is at most `n_3+2n_4≤6` by (1), impossible. Thus A is Y, with three degree2 symbols and two degree3 symbols. The three low symbols require6; equality in the same bound forces `n_0=n_4=0`, `n_3=6`. The total word and active counts then give `n_1=0`, `n_2=18`.

At a symbol b of a size4 party, the analogous difference is

`s(b)−q(b)−2h(b)=2d(b)−7`.

Since `n_1=n_4=0`, its left side is nonpositive, so `d(b)≤3`. Four degrees sum to12, so each is3. All B,C,D degrees are therefore `(3,3,3,3)`.

## 3. Normalize only the B,C missing matching

The global B,C E projection is a4×4 graph of degree3. Relabel C so that its missing matching is the identity; no E word can then have B=C. Only this one matching normalization is needed.

Each of the three low A fibers has four words, balanced twice on binary sets at B,C,D. The no-Hamming-one prerequisite makes it a parity class, so its B,C projection is a full2×2 rectangle. If its B set is U, its C set must be `U^c`: a full rectangle avoiding the diagonal has disjoint two-sets in a four-symbol alphabet.

Each of the two high A fibers has six words, takes three values twice at B and C, and is pair-injective on B,C; a repeated B,C pair inside that fiber would be a distance-one pair in the fourth coordinate. Thus its local3×3 B,C projection is the complement of a perfect matching.

Write `l_z` for how many of the three low B sets contain symbol z. Let e_B(z),e_C(z) count the two high fibers omitting z at B,C respectively. Since every B and C symbol has total partner degree3,

`l_z+2−e_B(z)=3`,  `(3−l_z)+2−e_C(z)=3`.

So `e_B(z)=l_z−1`, `e_C(z)=2−l_z`. Nonnegativity makes every l_z equal1 or2, and Σl_z=6 leaves two symbols of each type. Define

`X={z:l_z=2}`, `Y={z:l_z=1}`.

The two high B omissions are the two distinct X symbols, and the two high C omissions the two distinct Y symbols. In each high fiber, its omitted B value x∈X is paired with an omitted C value y∈Y; this gives a bijection `τ:X→Y`.

## 4. A single high fiber's local missing matching

Consider the high fiber omitting B=x and C=y, with x≠y. The global missing identity matching restricts to the two pairs `(z,z)` for z∉{x,y}. Its local missing matching is uniquely completed by `(y,x)`.

Thus its six B,C support pairs are exactly all pairs on the local3×3 grid, except those two diagonal pairs and the bridge `(y,x)`. This is forced by the pair-injective six-word fiber, not an equal-modulus or phase ansatz.

## 5. Opposite ordered pair counts differ by an odd number

Fix x∈X,y∈Y and let `t_xy=1` when τ(x)=y, otherwise0. Let L_bc and H_bc be contributions to global B,C pair multiplicity from the three low fibers and two high fibers.

For the low rectangles,

`L_xy−L_yx=l_x−l_y=1`.                                            (3)

For the high fibers:

- Pair `(x,y)` is present only if its B omission and C omission occur in the same high fiber: the other high fiber then contains both. It is never a bridge, since its first symbol is in X and second in Y. Hence `H_xy=t_xy`.
- Pair `(y,x)` belongs to both local grids: y is never omitted at B and x never at C. It is removed exactly once as the bridge when τ(x)=y. Hence `H_yx=2−t_xy`.

Combining with (3), global multiplicities M satisfy

`M_xy−M_yx=1+t_xy−(2−t_xy)=2t_xy−1∈{−1,1}`.

But x≠y, so neither pair lies on the global missing diagonal. Both global E pair values must have exactly two extensions, giving `M_xy=M_yx=2` and difference0. Contradiction.

This excludes the stated profile, conditional on the no-Hamming-one prerequisite. It is an actual common-marginal support contradiction; no separate supports or phase choices are substituted between cuts.

## 6. Tiny exact controls and error history

`frontier-20261029-n48-t24-4445-controls-v2.py`, SHA-256 `a8b776a244190357c963bb2288e8f20412092522e11a27d9b7fae4508a53237d`; receipt SHA-256 `e614c3fb8e7c70ad1b997345d605b369ae25ea74ed4ebbf49ff6a53257b77c45`, enumerates18 low-set multisets with local frequencies1,1,2,2 and both high-exclusion orders. It checks all144 cross-X/Y ordered-pair differences are exactly `2t−1`, and none of the36 states has all off-diagonal multiplicities2. These are controls, not the proof.

An earlier control v1 tried to use a non-existent BC+BD-relaxed positive and failed before writing a receipt. Investigation revealed the stronger single-BC antisymmetry contradiction above. v1 is retained, no failed control is called passed, and v2 does not invent that positive. The local six-edge high pair graph itself is valid; its incompatibility appears only when the common low/high contributions must sum to the global multiplicities.

The unresolved N48/t24 residual profiles, after the separate no-six-symbol and r4444 phase candidates, would be3555,4455,4555,5555. Those results and this prerequisite all remain separately unreviewed; no global support bound or exact tensor witness follows here.
