# Four-party cross-pair mixing of the 60-support tensor: a unique-source support floor

Owner **PhysicsAME46-2**. Native clock observed before writing: `Thu Oct 29 13:58:48 PDT 2026`; not an asserted completion time. **WRITTEN reduction with bounded exact finite source-support checks**, an unreviewed author candidate, not a formal proof, novelty clearance, or global AME support bound.

## 1. Exact scope and result

Let `S` be the 60 positions in `frontier-20261028-pandya-table-v1.txt`, SHA-256 `cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38`, the transcribed published 60-term example. Let X be **any complex tensor with support exactly S**, with arbitrary nonzero coefficients at those positions; X is not assumed to be AME or to have the published signs or magnitudes.

At each of the four parties set `H={1,2}`, `K={0,3,4,5}`. Select zero, one, or two disjoint cross-pairs `{h,k}` with h∈H, k∈K. In the chosen coordinate basis let the local invertible matrix be the direct sum of an arbitrary **entrywise-nonzero** complex 2×2 matrix on each selected pair and arbitrary nonzero 1×1 scalars on the unmatched values. The pairs and their matrices may differ independently across parties. Arbitrary output monomial maps and input diagonal scalings are also allowed.

For **every** X and all such maps:

1. The output support is at least 60; identity attains 60. Thus the exact support minimum of this restricted family is 60.
2. If at least one party has a selected pair, the output support is at least **81**.
3. If all four parties have at least one selected pair, the output support is at least **108**.

The values 81 and 108 are lower bounds; their attainability is not claimed. They hold for arbitrary complex phases and even nonunitary invertible blocks. For the published tensor, if the local maps are unitary, each output is an AME state, but the bounds do **not** cover arbitrary U(6)^4 or AME states outside this tensor's orbit.

A general U(2) block with a zero entry is monomial: unitarity forces it to be diagonal or antidiagonal. A support-preserving output permutation turns it into diagonal scalar blocks. Thus the physical version above covers arbitrary independent disjoint cross-pair U(2) gates, with an **active** party meaning at least one entrywise-nonzero, genuinely mixing pair after that reduction. In particular, none of these four-active-party moves can yield a sub-60 witness from the published tensor.

## 2. Unique-source cell lemma

Consider any four coordinate partitions into blocks. A local block matrix is entrywise nonzero within each selected block, with zero entries between different blocks. The partitions induce disjoint product cells `C=B_A×B_B×B_C×B_D` in the tensor-coordinate universe.

If a cell C contains exactly one source position `w∈S`, then **every** output position z∈C has exactly one contributing input position: w. Its value is `X_w·∏_i M_i[z_i,w_i]`, which is nonzero. Different cells are disjoint. Therefore

`|supp((⊗_i M_i)X)| ≥ L(S;B_A,B_B,B_C,B_D) := Σ_{C:|C∩S|=1} |C|`.    (1)

This is an all-variable statement; it does not assert that an output in a cell with two or more source positions is nonzero. Such contributions can cancel. Input diagonal scalings preserve nonzeroness of every X_w; output monomial maps merely rescale or permute the final positions, so (1) remains valid with those maps.

The selected cross-pair layouts have one two-element block per pair and singleton blocks for all other values. A party has 1 zero-pair layout, 8 one-pair layouts, and 12 two-pair layouts, or 21 total. Thus there are `21^4=194,481` layout quadruples. For each, (1) is an integer depending only on S and the chosen blocks.

## 3. Complete exact support count

For a layout quadruple let a be the number of parties with at least one selected cross-pair and d the number with two. The case count is `C(4,a) C(a,d) 8^(a−d) 12^d`. The minimum in each row is the minimum of L, **not** an asserted attainable output support minimum for that row.

| a | d | layout quadruples | min L | max L |
|---:|---:|---:|---:|---:|
|0|0|1|60|60|
|1|0|32|81|81|
|1|1|48|102|102|
|2|0|384|94|110|
|2|1|1,152|122|138|
|2|2|864|142|174|
|3|0|2,048|102|148|
|3|1|9,216|132|186|
|3|2|13,824|157|233|
|3|3|6,912|196|293|
|4|0|4,096|108|199|
|4|1|24,576|140|249|
|4|2|55,296|127|311|
|4|3|55,296|150|388|
|4|4|20,736|176|482|

Thus the minimum L over every layout is 60, over nonempty layouts is 81, and over all-four-active layouts is 108. The identity gives the matching upper value 60 for the full restricted family. The all-four conclusion is not inferred from the known three-party orbit result; it explicitly includes simultaneous nontrivial H–K mixing at every party.

## 4. Exact source check and limitations

`frontier-20261029-four-party-pair-cell-floor-v1.py`, SHA-256 `e345726d38dd1fdf74d027ab19ae1b76f3a7b97313ed28a87777e4412be0299f`, reads the pinned table, checks the complete 36-cell AB grid, 60 distinct source positions and coefficient-token counts. On all 194,481 quadruples it compares two integer methods:

- group the 60 source positions by their product cell and sum cell sizes with source count 1;
- independently expand each source position to all accessible output positions and count outputs with source count 1.

They agree on every layout. Receipt `frontier-20261029-four-party-pair-cell-floor-v1.json`, SHA-256 `20afb6f884e35cc003725f341cef8ed2abb7b68f54371bb75dc86f0b8f90c6bf`, records row counts, extrema, representative minimizing layouts, and score-stream SHA-256 `4f0f018d377881cc06afaf6a9ff83d1bd38a41a63bc1a8bd3c4040cdf5e38140`. One foreground run took 22.9 seconds. Both methods share the same source parser and layout generator; this is not a cross-model or human review.

Controls include the identity's 60 singleton-source outputs, intended-reason rejection of a dropped source position, duplicated source position, overlapping pairs and a non-cross pair, and an explicit **mutated-amplitude** two-source cancellation with invertible entrywise-nonzero `[[1,1],[1,−1]]` blocks. The last control illustrates why multi-source cells are not counted in (1); it does not modify the published tensor or assert a published-tensor cancellation.

This packet uses only the pinned source table and the finite computations described here. It does not use the f226 or f222 reviews or their dispositions, the pending f231 audit, any withdrawn certificate, SAT result, v203/v124 held material, or the earlier withdrawn mixed-sector argument. Prior exposure to the published tensor and its reviewed orbit results is not a blind reconstruction. Review should independently audit the table transcription, the 21-layout completeness, the one-source lemma, all 194,481 counts and the unitary-to-monomial reduction. No exact minimum over all AME(4,6) states, sub-60 witness, or priority claim follows.
