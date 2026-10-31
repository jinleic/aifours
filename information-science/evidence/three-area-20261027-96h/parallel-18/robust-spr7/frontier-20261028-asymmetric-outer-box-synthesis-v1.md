# Exact synthesis for an asymmetric, band-guided septic box

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** A band-guided negative-certificate search was followed by a different exact Bernstein inner-cone construction. The latter proves a common numerator for the whole chosen outer box and all its subboxes. No general septic conclusion follows.

Let
\[
a_0(s)=(s+1)((s+1)^2+4)((s+1)^2+25)((s+1)^2+121)
\]
have ascending coefficients \((15860,23684,12348,5144,785,171,7,1)\). With \(r=16401431/134217728\), define the independent box by
\[
\ell_j=a_{0,j}(1-rw_j^-),\quad u_j=a_{0,j}(1+rw_j^+),
\]
where
\[
w^-=(19/20,1,3/20,1,2/5,3/20,17/20),\qquad
w^+=(19/20,3/10,1/2,1/10,4/5,9/20,2/5).
\]
All seven widths are positive. Every denominator is strictly Hurwitz, and one common monic numerator is
\[
(b_0,\ldots,b_7)=(5148139/25,286927/2,2379257/25,3492237/100,
929853/100,12887/25,1942/25,1).
\]
The compactified pairing satisfies
\[
\frac{P_{a,b}(t)}{(1+t)^7}\ge
\frac{920802767554622493}{201761263306198220800}>0
\]
for all \(t\ge0\) and all members. Thus
\[
\operatorname{Re}\frac{b(i\omega)}{a(i\omega)}\ge
\frac{34103806205726759}{28367585321201771651303355156}>0.
\]
Every subbox inherits the same numerator and stability. In particular, no finite nonzero nonnegative atom combination can give a coordinatewise nonpositive coefficient vector for the outer box or any subbox.

The 12 rational endpoint-root brackets form six strictly separated even/odd bands. Together with the positive reference Routh column, the sign-band/no-imaginary-crossing homotopy proves all-member stability. For pairings, the minimum at each frequency over the independent box is the minimum of its four actual parity corners; the four exact Bernstein proofs cover the compactified half-line with 8, 6, 8, 9 leaves, respectively.

The search deliberately included two exact inversion-bearing frequencies in each of the six parity bands, then performed eight rational finite-grid exchange rounds. Their positive grid duals alone did **not** prove the box feasible. An exact inner Bernstein cone built from a smaller-box template then found a full-halfline numerator in two rounds; a rational simplification was independently replayed. Frozen search history is `frontier-20261028-band-guided-asymmetric-search-results-v1.json`, SHA-256 `7fddca9ab6d7bbf90952f98cee0df46070564794fa293492687803029ae6fd1c`.

Frozen endpoints, root brackets, numerator, pairing polynomials, leaves and bounds: `frontier-20261028-asymmetric-outer-common-numerator-frozen-v1.json`, SHA-256 `a639c58f792bf88bad9f99d13b7a4e5bc404a6e9c9b39e44ecd1aa39123aac9d`. Standalone checker `frontier-20261028-asymmetric-outer-independent-replay-kernel-v1.py`, SHA-256 `b979687fa44d9efccfc03b2296063080146e47af9dc2edf68652a24ad482ffdd`, independently rebuilds the nominal factorization, all 28 rational corner Hurwitz minors, 12 root brackets and six bands, the reference Routh column, all pairing coefficients and leaves, and the margins; corrupted leaf and reversed-root controls were rejected. Receipt `frontier-20261028-asymmetric-outer-independent-replay-result-v1.json`, SHA-256 `557dc790cfcb989fae5eff900329050ee9758d8f34997393e602de73381ecc92`.

Exact computations use integers and `fractions.Fraction` on one Python Eval host. Root continuity and Bernstein positivity are written arguments. No formal verification, cross-vendor review, novelty clearance or unrestricted septic verdict is claimed.
