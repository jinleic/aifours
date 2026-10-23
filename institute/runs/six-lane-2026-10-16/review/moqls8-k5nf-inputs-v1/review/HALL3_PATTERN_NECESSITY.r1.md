# H3: a necessary rank condition missing from the pairwise Gram-pattern model

Mathematical/encoding proposal, frozen before any new generator or solve. Parent approval is required before the
pilot below. Nothing in existing CNFs, receipts or ledgers is changed. This is not an exclusion of K4 or K5.

## 1. Necessary condition and proof

Let U be the transition matrix between two orthonormal bases of C^8: U[a,b]=<u_a,v_b>. For any three distinct rows
R and any two columns C,

    OR_{a in R, b not in C} [U[a,b] != 0]

must hold. Otherwise the three rows of U would be nonzero pairwise orthogonal vectors contained in the same
2-dimensional coordinate subspace, which is impossible. The transposed assertion holds for three columns and any
two rows. The only facts used are that U is unitary and that three nonzero orthogonal vectors are linearly independent.

In the actual QLS model the two ONBs may be any two row/column lines of the same square. This condition is valid
whether the lines are parallel or intersect, including the shared-point diagonal U[c,c]=1. It holds for classical
and non-classical squares, and does not use F3, P4, weight1, minimality, catalogue counts, or a symmetry choice.

## 2. Why this is not already the stated G3 condition

The 8x8 support matrix with three diagonal components J_(3x2), J_(2x3), and I_3 has every row/column nonempty, every
row/column degree at most3, and no pair of rows or columns intersecting in exactly one nonzero. Thus it passes the
stated pairwise G3 support conditions (with no singleton interacting outside its isolated I_3 component).
It cannot support a unitary: its first three rows are supported on the first two columns. H3 rejects it.

No claim is made that this counterpattern extends to a satisfying assignment of all the OTHER existing G2/G4/G5/P4
constraints. H3 might be logically redundant in the full formula; adding an explicit valid consequence could still
speed search. Its validity for genuine configurations is independent of whether it strengthens the Boolean relaxation.

## 3. Minimal proposed encoding delta

Use only transition matrices between the reference row0 and each of the other15 row/column lines (rows1..7 and
columns0..7), in each square s=1..5. For each matrix and each R3,C2 add the 18-literal positive clause

    g_s(a,b) for a in R, b in (line not C),

and the transpose-oriented family (three columns, two rows). Interpret self pairs as True and distinct pairs on a
common row/column as False, exactly as the pinned encoder does. All other pairs use the ALREADY allocated g-variable
ids (no new variables, no auxiliary gates). Raw clause candidates:

    5 * 15 * choose(8,3) * choose(8,2) * 2 = 235200.

This is before constant folding and dropping tautologies. An independent generator should check every literal id
against the pinned complete g map. The new formula is F_H3=F AND H3, not a new interpretation of F. A refutation of
F_H3 excludes genuine configurations by the original necessity bridge plus section1; it need not prove F UNSAT.

## 4. Frozen proposed pilot (pending approval)

- Target: the unchanged K5 hard leaf c016.L2.040.L3.104, whose OLD leaf-CNF SHA is
  6d84469eed207e6f0944c52ccbfbaa0596078966dfba432743ab78541ce6aebd.
- Matched observation: old model remained UNKNOWN under CaDiCaL900s and1800s, and under a proof-free kissat900s run.
- Append H3 to the SAME unconditional K5 base (6ecb77a7…469b), then the SAME21 path units. Hash exactly the bytes
  streamed, record generator hash, raw/emitted clause counts and all input hashes. Do not overwrite the old base.
- One proof-free CaDiCaL solve with native limit600s, one solver, memory guard under the existing lane caps, no other
  own heavy pipeline. It is EXPLORATORY even if UNSAT. No full pass before an observed timing/resource projection.
- Controls before the pilot: the section2 nonunitary pattern must fail H3 while passing stated G3; identity and
  permutation support matrices must pass; exact ONB matrices (including a full-support Fourier matrix) must pass;
  positive classical AG(2,8) support patterns must pass the family in the relevant relaxed encoder mode.
- Any follow-up certificate must bind the new F_H3 bytes, undergo independent H3-generator/bridge review, use the
  strict existing streamed DRAT pipeline, and retain all UNKNOWN leaves and old histories. No old certificate is
  silently relabelled as a certificate of a different formula.
