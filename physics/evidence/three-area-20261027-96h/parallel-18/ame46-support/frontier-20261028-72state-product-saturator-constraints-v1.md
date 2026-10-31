# Necessary equal-H and column-rigidity conditions for a 72-family product saturator

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 18:27:25 PDT 2026`; not an exact completion clock. **WRITTEN author candidate**, requiring independent review. This is a necessary-condition theorem, not an existence result, an unrestricted orbit minimum, or a global AME(4,6) lower bound.

## 1. Scope and statement

Consider any AME tensor in the E∪P∪P′ 72-support family and gauge described in `frontier-20261028-72state-one-restricted-party-orbit-barrier-v1.md`, SHA-256 `cd3eccbfd5e6efd67b7be594d5932a90392d14e1ea5fae0696906f24272bf536`: E is the signed Pauli sector, each of the 24 P/P′ coefficients is nonzero, and each all-K 2×2 block is invertible. In this gauge the AME condition makes those blocks unitary after the common normalization. The source decomposition and color relabeling are pinned in that dependency and its exact source certificate.

A **product saturator** is a normalized product vector φ with `|<φ,T>|=1/6`, the maximum allowed by any 2|2 AME cut. Define

`h_i=||φ_{i,H}||²`, `p_i(g)=|φ_{i,K,g}|²`, `k_i=Σ_g p_i(g)=1−h_i`.

For any hypothetical product saturator:

1. every party is mixed H/K, and all four H masses are equal: `h_i=h` with `0<h<1/2`;
2. all six K-probability inner products equal `h²`: `p_i·p_j=h²`;
3. for each color g, among the four real numbers `p_0(g),…,p_3(g)`, at least three are equal;
4. for complementary party pairs ij|kl and complementary unordered color pairs `{a,b}|{c,d}`,

   `p_i(a)p_j(b)+p_i(b)p_j(a) = p_k(c)p_l(d)+p_k(d)p_l(c)`.       (1)

These are necessary only; they do not prove that a product saturator exists or fails to exist. A rank-one two-party contraction would yield such a product saturator, so the statement constrains the outstanding unrestricted-orbit rank-one question.

## 2. Product saturation and two elementary identities

Since every 2|2 flattening of T is U/6 with U unitary, equality `|<φ,T>|=1/6` forces U to map the product of the conjugated input factors to the product of the output factors, up to phase, in **every** 2|2 cut. In particular, every two-party contraction of φ has rank one. By §§3–4 of the dependency, no pure-H or pure-K input covector can occur in a rank-one contraction of an interior 72-support state. Thus `0<h_i<1` for all i.

For distinct i,j,k,l, the HH-output Pauli blocks give

`h_i h_j = Σ_g p_k(g)p_l(g)`,                                      (2)

because the four signed Pauli matrices are Hilbert–Schmidt orthogonal and have normalized coefficient `1/√2`. At one matched K output `(g,g)`, only the HH input block contributes. The Pauli matrix is unitary, so Cauchy–Schwarz and (2) imply the pointwise constraint

`p_k(g)p_l(g) ≤ (1/2) h_i h_j = (1/2)Σ_t p_k(t)p_l(t)`.        (3)

Both formulas hold for every pair and color and do not depend on the P/P′ phases.

## 3. Local parity stabilizer and possible H masses

For each `(s,t)∈F_2×F_2²`, let a local diagonal D act by `(-1)^s` on H and by `(-1)^{t·g}` on K color g. The tensor is invariant under the tensor product of these four D maps: E has two H factors and two equal K colors, while every P/P′ term contains each of the four K colors once, whose XOR is zero. This remains true for arbitrary phases.

A product saturator and any 2|2 source unitary therefore give equality of the expectation of a two-party stabilizer on the two sides of every cut. For `(s,t)=(1,0)`, put `z_i=1−2h_i`; then

`z_i z_j = z_k z_l` for all three complementary pairs.          (4)

If no z_i is zero, (4) makes all `|z_i|` equal and their sign product positive. Hence the h_i are either all h<1/2, all 1−h>1/2, or two of each. The all-high case contradicts (2), since `h_i h_j>(1−h_k)(1−h_l)≥p_k·p_l`. In the two-low/two-high case let the low mass be `a∈(0,1/2)`. Equation (2) gives `p_high1·p_high2=a²`, while both K masses equal a. Equality in `p·q≤(Σp)(Σq)` forces these two nonzero probability vectors to be supported on the same singleton; that contradicts (3), which forbids a single color to carry the entire positive inner product. Therefore the nonzero-z case has all `h_i=h<1/2`.

If some z_i is zero, (4) implies at least three are zero. If all four vanish, all h_i=1/2; equation (2) saturates `p_k·p_l≤k_k k_l=1/4`, again forcing a common singleton and contradicting (3).

It remains to exclude exactly three zeros. Let their indices be 0,1,2 and let `h_3=b∈(0,1)`. From (2), `p_i·p_3=1/4` for i=0,1,2, and `p_i·p_j=b/2` for i,j∈{0,1,2}. By (3), for each color g, `p_i(g)p_j(g)≤b/4`; also each `p_i(g)≤1/2`. Put `q_g=p_0(g)+p_1(g)+p_2(g)`. If the largest of these three terms is at most `√b/2`, then `q_g≤3√b/2`. Otherwise, calling it x, the other two are each at most `b/(4x)`, and `x∈[√b/2,1/2]`. The convex function `x+b/(2x)` attains its maximum on this interval at an endpoint. Thus in all cases

`q_g ≤ max(3√b/2, 1/2+b)`.                                      (5)

However `Σ_g p_3(g)q_g=3/4` and `Σ_g p_3(g)=1−b`, so (5) implies

`3/4 ≤ max((1−b)3√b/2, (1−b)(1/2+b)) ≤ max(1/√3,9/16) < 3/4`.

The first displayed upper bound is attained at b=1/3, the second at b=1/4; both elementary inequalities hold for `b∈(0,1)`. This contradiction excludes exactly three zeros. Consequently all H masses are the same h∈(0,1/2), and (2) gives every K-probability pair inner product h².

## 4. Unitary color-pair conservation and the column theorem

In any cut ij|kl and for distinct input colors a,b, the all-K source block connects the two ordered inputs `(a,b),(b,a)` to the two ordered outputs `(c,d),(d,c)`, where `{c,d}` is the complementary color pair. This is a unitary 2×2 block after normalization. Product saturation therefore preserves the sum of the two squared amplitudes, proving (1), including possible interference inside each block.

All K row sums equal `k=1−h`, and all pair inner products equal `q=h²`. Fix a color a and sum (1) over all `b≠a`, for a fixed party partition ij|kl. The left side is `k(p_i(a)+p_j(a))−2p_i(a)p_j(a)`. The right side is `(k−p_k(a))(k−p_l(a))−[q−p_k(a)p_l(a)]`. Rearranging,

`k Σ_r p_r(a) − (k²−q) = 2[p_i(a)p_j(a)+p_k(a)p_l(a)]`.   (6)

The left side does not depend on the party partition. Therefore, writing `x_i=p_i(a)`,

`x_0x_1+x_2x_3 = x_0x_2+x_1x_3 = x_0x_3+x_1x_2`.

Subtracting gives `(x_0−x_3)(x_1−x_2)=0` and `(x_0−x_2)(x_1−x_3)=0`. If any two of the four x_i differ, these identities force the remaining two to equal one of them; they cannot form two unequal pairs. Thus at least three of the four column entries are equal. This is a written deduction over real nonnegative probabilities, not a finite-field inference.

## 5. Remaining gap

The diagonal-stabilizer and color-pair identities are necessary conditions, not an exclusion of all feasible matrices p or phases. In particular, the prior exhaustive F_5 rank-one diagnostic concerns only one finite field and cannot eliminate complex solutions. Determining whether any product saturator satisfies the equal-mass, column-rigidity, Pauli-overlap, and complex phase conditions remains open in this work. If no such saturator existed, every nonzero two-party contraction would have rank at least 2 and the full GL(6)^4 orbit would have support at least 72; that implication is conditional, and no such unrestricted conclusion is claimed here.
