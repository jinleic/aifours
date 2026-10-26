# Candidate v1 — analytic exclusion of the binary-full / three-thin AME support profile

Observed before creation: `2026-10-23T14:12:18-0700`. PhysicsAME46, physics-6. Immutable WRITTEN CANDIDATE / PARTIAL. No scientific execution, graph enumeration, certificate replay or independent review has occurred. This continues `thin-slice-obstruction-v1.md`, SHA256 `ba269009d0f352e9b9fed1967cead86b5594b9ddee6d822cd8190fc67c2bce4f`.

## Theorem and exact delta

**Candidate theorem.** There is no AME(4,6) state, with arbitrary complex amplitudes and in any product orthonormal basis, having e=0 and deficit profile

    {6,6}{2,2,2,2,2,2}³.

Here d_(i,a)=6−|{x∈T:x_i=a}|, T={x:|6ψ_x|=1}, and e=|supp ψ|−(72−|T|). A profile specifies positive deficits only. This hypothesis forces t=24, h=12, and support48. The coordinate carrying{6,6} can be any of the four. Reordering parties simply permutes the six marginal conditions.

This is the entire formerly difficult profile of the t24/e0 layer, **not merely one support graph or symmetry representative**. The historical README reports42 phase-excluded exploratory supports and an UNKNOWN proof run after a disk guard; this proof does not use that enumeration or its scripts. It does not prove s_min≥49: all other t24/e0 profiles and all required e>0 cases still need a complete, verified composition. The documented unrestricted range remains48..60.

The proof imports only:

1. The elementary exact-two/block facts and Theorem A of the pinned structural candidate (the complete derivation is supplied there).
2. The standard impossibility of AME(4,2), with all six reductions and an elementary Pauli proof supplied in the pinned candidate §4.
3. Tarry's classical theorem that two orthogonal Latin squares of order6 do not exist (explicitly cited in Pandya arXiv:2610.16673v1 and Bruzda arXiv:2610.16882v1).

The officer-counting contradiction at the end is re-derived below. It is the existing LOWER48 Lemma17 mechanism, not a new result claimed here. **No computer-assisted lower bound42/46/48 is needed by this proof.**

## 1. The binary shadow and its doubled modules

Write A=6ψ. Choose the binary coordinate as coordinate1; its only active values are a,b, each deficit6. There are no officers on these two local values. All other values of coordinate1 have deficit0 and no non-officer entries. Thus N⊂{a,b}×[6]³ and |N|=24. For each of coordinates2,3,4, each of its six values has deficit2 and occurs in exactly4 points of N.

For each doubled triple z=(x2,x3,x4), both(a;z),(b;z) lie in N. By structural Theorem A, the doubled triples form disjoint simple cubic bipartite components. A component C has2r vertices, with r≥3. In each of the three remaining coordinates its vertices use exactly r distinct values, each appearing twice; this follows because each color is a perfect matching.

**Isolation of a component's values.** For one such coordinate value v, two doubled triples of C contain v. Their four tensor entries already exhaust the non-officer slice x_j=v, since its deficit is2. Consequently no non-officer entry outside C uses any of C's values in any of coordinates2,3,4. In particular distinct doubled components use disjoint value sets in each coordinate.

Remove all values used by doubled components, in the sense of restricting the remaining support; no physical file or state is being deleted. The three residual alphabets have the same size

    n = 6 − Σ_C |C|/2.

The residual support R⊂{a,b}×B×C×D has4n points, because each remaining value in coordinate2 occurs four times. There is no doubled triple in R: all such triples were included in the complete doubled graph. Every pair-line meeting R has exactly two entries in R. Indeed pair-lines on remaining values cannot meet a removed module by its value-isolation property; pair-lines fixing coordinate1 to a or b contain no officers. For any remaining value in any of coordinates2,3,4, its hole neighbors in each other remaining coordinate form exactly two values.

## 2. A residual without doubled triples forces four-qubit blocks

We prove n cannot be positive. Let H_BC,H_BD,H_CD be the bipartite graphs whose edges are value pairs occurring in R. Each graph is simple2-regular on its two n-element parts, by the deficit2 slice property. A triple(b,c,d) occurring in R is a triangle of this tripartite graph. There is exactly one coordinate1 value attached to it, because R has no doubled triple.

Take an edge(b,c) of H_BC. Its pair-line contains two R entries. They must have different d-values: if the d-value were the same, the entries would form a doubled triple. These d-values are common neighbors of b and c in D. Each of b and c has exactly two D-neighbors, so their D-neighbor sets coincide and consist of exactly these two values.

Now fix b with C-neighbors c0,c1 and D-neighbors d0,d1. The previous paragraph says that both c0 and c1 are connected to both d0 and d1. Since their D-degrees are2, those are their entire D-neighbor sets; likewise d0,d1 have C-neighbor set{c0,c1}.

The edge(c0,d0) has two R entries with different B-values, again because no triple is doubled. One B-value is b, so call the other b′≠b. From the edge(b′,c0), b′ has D-neighbor set{d0,d1}. From(b′,d0), its two C-neighbors must be{c0,c1}, because these are d0's only C-neighbors. Thus b,b′,c0,c1,d0,d1 form a complete K_(2,2,2) component. All their degrees to each other part are already2, so they have no graph edges to other values.

Every one of the eight triples in{b,b′}×{c0,c1}×{d0,d1} occurs in R. For each edge(b,c), its two common D-neighbors must both occur by the exact-two line and no-doubling property. Each triple has one coordinate1 label, hence this component contributes exactly8 non-officer tensor entries on

    {a,b}×{b,b′}×{c0,c1}×{d0,d1}.

There are no outside entries on any selected pair-line:

- For a pair of coordinates among2,3,4, the selected pair lies in this K_(2,2,2), and its two entries have just been identified inside the block.
- For coordinate1 paired with one other coordinate, the two rows for a,b together contain the four entries of that thin value's slice. Each individual row has exactly two entries, all in the same block.

Therefore in each cut12|34,13|24,14|23, the submatrix B_P on the four selected row values and four selected column values has no outside row/column entries and is unitary. For ω=3ψ restricted to these8 entries, ||ω||²=9·4/36=1 and the flattening of2ω is B_P. Consequently all six required reductions are, explicitly,

    ρ^ω_12=B_12 B_12†/4=I4/4,     ρ^ω_34=(B_12†B_12)^T/4=I4/4,
    ρ^ω_13=B_13 B_13†/4=I4/4,     ρ^ω_24=(B_13†B_13)^T/4=I4/4,
    ρ^ω_14=B_14 B_14†/4=I4/4,     ρ^ω_23=(B_14†B_14)^T/4=I4/4.

This contradicts no-AME(4,2), so n=0. This argument is a general triangle-saturation lemma, not a finite graph census or an inference from examples.

## 3. Every residual entry is doubled; only two component decompositions remain

Since n=0, every point of N belongs to a doubled component. There are12 doubled triples. Every component has an even number of vertices, at least6. Their sizes are therefore either12, or6+6.

For any component C, structural Theorem A provides a single2×2 local unitary on span{|a⟩,|b⟩} taking its two alternating rays to the two coordinate axes. This operation preserves **all six** AME reductions: if a two-party set contains party1 its marginal is unitarily conjugated, while if it does not, tracing over party1 is invariant under the unitary. Hence I36/36 remains I36/36 for every pair. The24 old officers are unaffected, since none uses a or b.

### A single twelve-vertex component

Rotate its rays to the coordinate axes. Each of its12 vectors has norm1, so it becomes a singleton officer. There are then36 officers and no other support entries. Each two-coordinate line contains one officer, so the36 words determine a pair of orthogonal Latin squares of order6. This contradicts Tarry.

### Two six-vertex components

Each component is a simple cubic bipartite graph on3+3 vertices, hence K_(3,3). Each uses three values in each of coordinates2,3,4; their value sets are disjoint and partition all six values.

Rotate the first component's rays to the axes. It becomes6 officers, three on a and three on b. In the other component all vectors alternate along one common orthogonal pair of rays. Either that pair is the coordinate-axis pair, in which case it also becomes6 officers and the preceding36-officer contradiction applies, or both coordinates of both rays are nonzero. In the latter case all12 entries of the second component remain non-officers.

There are now t′=30 officers, h′=6, N′ of size12 and support42. The new deficit profile is exactly

    {3,3}{2,2,2}³.

For coordinate1, three new officers on each of a,b change its two deficits from6 to3. In another coordinate, each of the three values used by the first component is incident with two doubled triples, one from each bipartition class (the edge of that color). After rotation these become two officers. Its old deficit2 becomes0. The three values of the untouched second component keep deficit2. This verifies the profile rather than inferring it from support count alone.

## 4. The30-officer profile is impossible by an existing elementary count

Here is the count in full, without invoking a computational lower bound. For any AME officer set, put V_i={v:d_(i,v)>0}, v_i=|V_i|, h=36−t, and c(x)=|{i:x_i∈V_i}| for x∈T. Then

    Σ_(x∈T) c(x)=6Σ_i v_i−4h,
    Σ_(x∈T) binom(c(x),2)=Σ_(i<j) v_i v_j−6h.

The first identity counts officers on active coordinate values: for coordinate i, the count is Σ_(v∈V_i)(6−d_(i,v))=6v_i−h. For the second, within the v_i×v_j active pair-value grid, exactly h pair-lines contain non-officers and no officer; every other line contains exactly one officer. Thus exactly v_i v_j−h officers have both active values. Sum over the six pairs.

For the displayed profile, v=(2,3,3,3), t=30,h=6. Hence the two sums are respectively42 and9. But every integer c∈{0,1,2,3,4} satisfies(c−1)(c−2)/2≥0, whereas

    Σ_(x∈T) (c(x)−1)(c(x)−2)/2
       = Σ binom(c(x),2) − Σ c(x) + t
       = 9−42+30
       = −3.

Contradiction. This is precisely the historical officer-counting Lemma17 specialized to this profile; it is an import/redisplayed calculation, not this round's discovery.

Both possible component decompositions are impossible. The candidate theorem follows. ∎

## Verification and limits

- This proof did not run the old native pipeline, replay old48 certificates, enumerate the42 old supports, or trust their exploratory completeness.
- The load-bearing new steps are: cubic bipartite qubit-module closure; isolation by deficit2 slices; no-doubling triangle saturation; the actual common local-unitary action and its two component cases.
- Every constructed qubit shadow has all six pair reductions explicitly checked in writing. The local unitary also preserves all six original AME conditions.
- The accepted old lower bound48 remains unchanged. A full lower49 proof would require every other deficit profile/case, proper evidence for any executable part, and independent composition review. No claim that one profile settles that target is made.
- Status: CANDIDATE pending parent and a separately authored reconstruction on pinned bytes. No Lean/kernel, human or independent-model CLI review. Novelty and external significance remain unestablished.
