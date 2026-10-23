# Exact sharpening of the joint-tree node bound (2026-10-19T08:08:03-0700)

Supplements ext-search-controls-resources-v1.md, with no run. Independent joint specification chooses an uncovered
(row x,value v) item at every search node. For each unassigned column c there is EXACTLY ONE value w in Zn that
can cover it: w=D[x][c]-v. Thus there are at most r remaining-column branches, then at most r-1, etc.
For a chunk leaving r=n-1-m columns unassigned, the entire tree is bounded by
T_joint <= sum_(d=0)^r r!/(r-d)!, which is sharper than the safe n-ary bound in the first resource note.
The bound counts pruned nodes too, includes root, and does not assume any random pruning or solution probability.
It is not an estimate of the actual target work.

|case|r|joint node upper bound|
|---|---|---|
|N6|5|326|
|N12|2|5|
|P21|2|5|
|P57|2|5|
|anchor|38|1421722876932548239555534242726381983188762661|

For the planted positive controls and N12 (r=2), at most5 nodes are visited in each chunk by an item-MRV joint
search after fixed assignments are applied. This checks reconstruction/correctness, not target-scale performance.
For the unrestricted anchor, the sharp bound remains enormous and does not justify a full run.
