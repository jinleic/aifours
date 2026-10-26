# Off-axis leading rank2 classification: one-heavy complete-graph tag erratum v1

Observed author-discovery clock:2026-10-24T04:50:19-07:00. No execution. Original working snapshot remains unchanged.

Affected source: `off-axis-leading-rank2-classification-v1.md`, section2. Its complete-one-heavy conclusion correctly requires the negative one-rook class, but the subsequent phrase “its sole rook-positive pair is one endpoint of U-V, not H or J” is **false and must not be used**. The sole rook-positive vertex can be H,J,U orV. All four positions remain in the genuine residual.

The distinction comes from the actual three-parallel-rook construction before negation. If its two leftover y-levels a,b are the two nonzero levels, the unique heavy edge joins the diagonal pair to a rook pair. If one of a,b is0, two rook pairs themselves are parallel and form the unique heavy edge. Negating the source exchanges rook/nonrook tags but preserves this possible heavy-edge incidence. A heavy negative-cycle triangle alone does not locate the sole actual rook.

Explicit counterexample to the old tag restriction: before negation choose vertical rook R0 in column0 with root e1-e2, R1 in column1 missing row0 with the same root e1-e2, and R2 in column2 missing row1 with root e0-e2. The leftover diagonal D joins(1,0) to(2,1), with y-root e0-e1 and an independent x-root. Label the resulting negative core's vertices H=D,J=R2,U=R0,V=R1. Then

    A1_UV=-2, A1_JU=A1_JV=-1,
    A1_HU=A1_HV=+1, A1_HJ=-1,

so it is exactly the degree3-H leading-star cancellation, but its sole rook-positive vertex after negation is H. Relabeling the two nonparallel directions also permits J, while the other raw geometry permits the heavy endpoints.

The support classification, the negative one-rook cycle conclusion, and the separate two-heavy K4 tag conclusion are not changed by this erratum. The four-core A1=-A0 packet and the same-isolate axis-triangle closures do not depend on this complete-K4 tag statement. They are not silently altered. This repairs an overrestrictive working-family statement, not a final accepted theorem or a permission for scientific execution.
