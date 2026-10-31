# A universal support obstruction from unique simple routes

Status: **WRITTEN**, conditional on the separately frozen supported-five-edge-path theorem, awaiting independent scientific review. This is a graph/input-output restriction for any number of transitions; it is not a general PH7 exclusion.

Let a seven-state PH representation of the original target have `z>1/5` and a normalized shifted generator with nonpositive diagonal entries. Suppose its directed graph has the following property:

> For every ordered pair of distinct states `i,j` at directed distance four, there is exactly one simple directed `i`-to-`j` path.

Then its input and exit cannot both be supported on singleton states. Equivalently, at least one of the actual input and exit supports has size at least two.

Indeed the target transform has relative degree five. Because all off-diagonal rates and input/exit weights are nonnegative, singleton input at `i` and singleton exit at `j` force their shortest directed distance to equal four. The graph property gives a unique supported simple path, necessarily of length four. But `frontier-20261028-ph7-five-edge-path-and-hidden-sum-bound-v1.md` (SHA256 `f38f7874e21431cf3a1661c566570b215f656c59d9d9d0b1c73bc876ea31381b`) proves that every such PH representation with `z>1/5` has a supported **simple path of length exactly five**. A unique supported simple path cannot have both lengths, contradiction.

The statement holds with directed two-cycles and arbitrarily many graph edges; the uniqueness premise must be verified for the actual graph rather than inferred from the graph's degree or a sampled route. It is weaker than the specialized nine-edge obstruction where explicit triangle geometry proves uniqueness for all cross-component pairs. The five-edge theorem and actual PH normalization remain pending disjoint scientific review; no PH7/PH8 existence verdict, formal proof, novelty, or parent adoption is claimed.
