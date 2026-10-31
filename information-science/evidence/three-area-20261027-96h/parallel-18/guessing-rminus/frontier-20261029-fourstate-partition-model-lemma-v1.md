# Four-state nonlinear syndrome selectors: a partition-information relaxation

## Required scope and first inputs

Read the historical graph/LP source erratum `frontier-20261028-full-source-lp-optimum-v1-erratum-1.md` before its consumers. The literal graph and ten-triangle binary q=8 encoding are those in `frontier-20261029-all-affine-syndrome-plane-entropy-v1.md` and the earlier triangle-code definition. The completed affine-plane theorem is MOTIVATION, not an entropy-gate import in this initial relaxation.

**Status: WRITTEN model-validity argument; no new exclusion or witness claimed here.** The new inputs are four syndrome values of affine rank three, not another affine-plane census. No two-syndrome theorem, conditional Delta gate, held review or external model is used.

## Four selector states and their fifteen information partitions

Let S have labels 0,1,2,3 for four specified syndrome values. Every factor parity is a fixed offset plus a Boolean function of S. Up to complement, a nonconstant Boolean function is one of seven unordered bipartitions. Encode it by a mask 1..7: value 0 at state 0, with the three mask bits giving values at states 1,2,3. Mask 0 denotes a fixed factor.

Use every one of the fifteen partitions P of the four states, including the constant partition 0 and the discrete partition top. Let T_P be the block label of S under P. A coordinate h(U,P) means H(Y_U,T_P), with the constant auxiliary dropped. Partition block labels are immaterial bijections.

Order partitions by information: P<=Q means Q refines P, so T_P is a function of T_Q. The join P+Q is their common refinement (the information in the pair); the meet P^Q is their greatest common coarsening. Both are computed on the literal four-state set, including states of probability zero.

## Valid Shannon rows

For every P, the tuple (Y1,...,Y10,T_P) satisfies the full elemental Shannon system. In addition:

- For P<=Q, h(U,P)-h(U,Q)<=0.
- For P<=Q and v outside U,
  h(U+v,P)+h(U,Q)-h(U+v,Q)-h(U,P)>=0.
  This is I(Y_v;T_Q | Y_U,T_P)>=0.
- For all P,Q,
  h(U,P)+h(U,Q)-h(U,P+Q)-h(U,P^Q)>=0.
  This is I(T_P;T_Q | Y_U,T_(P^Q))>=0, since the meet is known from either variable and the join is equivalent to their pair.

These are ordinary entropy inequalities; no distribution-specific bound or numerical cap is assumed.

## Actual coding premises

Condition on complete tuples of fixed factors and write Y_v for its selected components, just as in the affine-plane proof. The original graph FDs remain valid. The join of all selected parity partitions must be the discrete partition: the specified four syndromes are distinct, hence S is determined by Y_V, and every T_P is determined by Y_V.

For vertex v, define P_v as the join of its incident selected parity partitions. The original-neighbor tuple recovers Y_v and then all those parities, hence T_(P_v) is determined by Y_(N(v)). Each individual incident parity is visible too. Each selected triangle determines its parity partition.

Most importantly, given T_(P_v) and the other vertices L_J(v) of the selected triangles through v, every incident parity is known and each missing component is solved by its XOR equation. Therefore

H(Y_v | Y_(L_J(v)), T_(P_v))=0.

This is the correct minimal local state. It may be a three-block partition, not a single Boolean bit and not the full S. The old local decoder given the full S remains valid as a redundant premise. These are actual component identities, not stronger abstract graph FDs.

Given the full S, every selected parity is fixed. The same conditional factor tensorization gives the full-state gate

3H(Y_V)+17H(S)-2 sum_v H(Y_v,S)<=0.

This initial model imports NO gate for Delta conditioned on a proper partition. Any such future extension needs a separately stated, pinned theorem and scope.

## Symmetry and claim boundary

The four factor-preserving graph permutations and the twenty-four permutations of the four selector labels act on the partitions. Use only pairs preserving the complete input parity-partition pattern; recompute this predicate literally. Complements only change fixed parity offsets, which are allowed and do not change the entropy premises. Every exact identity is checked on all raw h(U,P) coordinates after averaging over those verified actions.

An exact Delta<=0 identity would exclude only the named four-syndrome pattern (and its verified transports/affine offsets). A positive polymatroid profile would remain a relaxation countermodel, not a probability law or winning code. No all-four-syndrome, unrestricted guessing-number, novelty, formal-proof or scientific-adoption claim is made by constructing this model.
