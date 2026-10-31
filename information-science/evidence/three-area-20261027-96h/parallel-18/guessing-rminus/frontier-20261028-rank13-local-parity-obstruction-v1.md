# Rank-13 low-marginal construction: exact obstruction

**Status: WRITTEN with exact finite quotient checks.** This rules out one explicitly specified equal-weight construction criterion, for all syndrome subspaces, not all guessing strategies or entropy laws. It explains why the preceding bounded searches failed without relying on their solver statuses.

## The tempting strict-gain criterion

Use the fixed `q=8` binary triangle cover and coordinate order of `frontier-20261028-triangle-two-coset-obstruction-v1.md` (SHA-256 `da26dfb13dfe38bdcc5c07a3d33a90a5b7adba77eebbcb6d36c2141ce4e032b7`). Mark triangle indices `0,3,6,9`. For vertex `v`, let the one-bit local form `g_v` be the XOR of its component bits belonging to marked triangles. Let `C` be the ten-parity code and

\[
K=\{x\in C:g_v(x)=0\text{ for all }v\}.
\]

Exact binary linear algebra gives `dim K=13`, and the image of `K` in every vertex's three-bit alphabet is the two-dimensional plane `g_v=0`. Hence a uniform mixture of **16 compatible K-cosets**, each with probability `1/16`, in which `g_v=1` appears in at most two cosets for every `v`, would have

\[
H(X_V)=17,\qquad H(X_v)\le 2+h_2(1/8).
\]

It would strictly beat `20/3` as an entropy ratio: `h_2(1/8)<11/20` follows exactly from `7^5=16807>2^14=16384`. This was a concrete admissible target, not merely an architecture check.

## Obstruction for this particular K

**Theorem.** No 16 compatible K-cosets have at most two occurrences of `g_v=1` at every vertex.

Proof using the finite certificate below. First, any two distinct K-cosets with the same ten-bit `g` pattern conflict: their difference has zero `g` pattern, and the certificate finds an original-graph isolated-vertex difference in every one of the 127 nonzero quotient classes with zero pattern. Thus any compatible selection has distinct `g` patterns.

The 16 patterns have total Hamming weight at most 20. Among 16 distinct ten-bit vectors the minimum possible total weight is `0+10*1+5*2=20`. Consequently the selection must contain exactly one zero pattern, all ten singleton patterns, and five weight-two patterns forming a perfect matching. Translate every selected coset by the unique selected zero-pattern coset. This preserves all `g` patterns and all original-neighbour conflicts, and makes that coset `K` itself.

The exact certificate enumerates **all** quotient classes in `F_2^30/K`, not just a selected syndrome subspace. Among the 1,280 classes whose `g` pattern has weight one, the only classes compatible with `K` have singleton pattern at vertex **1 or 9**; there are 12 such classes. Thus the eight required singleton patterns at the other vertices cannot be selected. Contradiction. QED.

## Exact quotient certificate

The checker `frontier-20261028-rank13-local-parity-obstruction.py` SHA-256 `168fe11cd3560ff8198e3b82ce3e00ac1bff20ea12519d104d49946778867e7e` constructs the quotient using ten triangle syndromes and seven independent code-coordinate forms, so there are `2^17=131072` classes. For each original vertex it allows nonzero coordinates only at that vertex and its graph non-neighbours, explicitly enumerates the images of all such differences with the vertex symbol nonzero, and unions these images. The resulting 20,003 quotient classes are exactly the classes containing an isolated-vertex difference. It independently verifies `dim K`, every vertex image rank, the full `g`-pattern image and preimage counts; in particular only the zero quotient is nonconflicting with pattern zero, and only vertices 1 and 9 occur among nonconflicting singleton patterns. Receipt `frontier-20261028-rank13-local-parity-obstruction-result.json` has SHA-256 `f310ca326f23607a8a06a2445cf4bfc2752b5cfa98aad255cbb92ff4fd78154f`.

An earlier 4D-syndrome Z3 search had returned UNSAT in a restricted 128-class instance (receipt SHA-256 `426027712169185aeab9f2d7ac2c13d4a7bcc1f3eac6f94dca110a1869e57e60`); ten further sampled 4D spaces yielded solver UNSAT for this equal-weight criterion (receipt SHA-256 `77167b55c5944b67ce086991dfb96316feffc9cf30110f5b1247eccbab6beae2`). The theorem above is broader for the specified `K`, uses no LP/solver status and covers every syndrome class. An expanded solver run was stopped once the finite obstruction was found.

Different rank-13 subcodes, unequal coset weights, other numbers of cosets, and all original unrestricted strategies remain open. No formal proof, cross-model review or novelty clearance was performed.
