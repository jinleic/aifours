# A quantitative bound if the two hidden poles coincide

Status: **WRITTEN**, awaiting independent review. This is a topology-independent necessary bound in the repeated-hidden-real-root slice, not a proof that the hidden roots coincide or that any PH7 representation exists.

At `z=8/9`, suppose an actual critical seven-state generator has characteristic polynomial

`det(yI-G)=y*((y+1)^2+8/9)^2*(y+r)^2`

with `r>0`. Then

`r >= 4/5 + sqrt(434)/15`.

Indeed `tr(G)=-(4+2r)` and `tr(G^2)=4/9+2r^2`. Since `G` is real Metzler, `tr(G^2)>=tr(G)^2/7`: off-diagonal two-cycle terms in the square are nonnegative and diagonal squares obey Cauchy. Rearrangement yields

`45r^2-72r-58>=0`.

The displayed bound is its positive root. Equality would additionally force all seven diagonal escape rates equal and every bidirectional edge product zero, the equality cases of Cauchy and nonnegative two-cycle terms. This observation does not by itself rule out the spectrum, imply real hidden roots in general, or improve the graph's transition count. The supported PH caller uses the already separately supported irreducibility/Perron normalization and retains its historical review cut; no new PH6 theorem, independent scientific review, formal proof, novelty, parent adoption, or 8/9 existence/exclusion is asserted.
