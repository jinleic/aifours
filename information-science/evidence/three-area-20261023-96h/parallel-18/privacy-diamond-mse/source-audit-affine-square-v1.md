# Finite-V source screen in affine-equivalent square coordinates

Observed clock before creation: **2026-10-23T15:45:25-0700**. Same info-1 finite-epsilon V; no second problem, program or novelty clearance. This source scoping supplements the previous audits and preserves every frozen mathematical packet unchanged.

## 1. Exact equivalence, not a new discovery

Let `T(x1,x2)=(x1+x2,x1-x2)`. Then

`max(|(Tx)1|,|(Tx)2|)=|x1|+|x2|`, and `||(Tx)||_2^2=2||x||_2^2`.

Thus T maps the **full** unit sensitivity diamond bijectively onto the **full** square `C=[-1,1]^2`. For every Borel feasible law mu, the pushforward nu=T#mu satisfies

`nu(F)<=exp(epsilon)nu(F+s)` for every Borel F and every s in C,

by applying mu's inequality to `T^-1 F` and `T^-1 s`. The inverse linear map proves the converse for all Borel laws. No density is assumed in this correspondence. Costs multiply by2, so if W is the squared-Euclidean optimum with full-square sensitivity,

`W(epsilon)=2 V(epsilon)`.

Consequently source screening must include **l-infinity/full-square sensitivity with Euclidean squared loss**, not just papers using the words l1/diamond. Homothetic diamond staircases map to homothetic square staircases; this does not turn their squared-Euclidean cost into squared l-infinity loss. These linear-algebra facts are a source-interface check, not a new research contribution.

## 2. New2026 optimal-central-cost claim: actual formal interface differs

[Pathegama–Avasarala–Cadambe–Ziani, **Local Differential Privacy with Correlated Noise Achieves Central-DP Optimal Cost**, arXiv:2605.30476](https://arxiv.org/html/2605.30476), actual arXiv record May28,2026. The abstract, Introduction/Definitions1–2, SectionII-B/II-C cost model, Theorem1 interface and whole Conclusion were actually read at the relevant passages.

The displayed formal perturbation set is

`T_n^Delta = union_i {0}^{i-1} x [-Delta,Delta] x {0}^{n-i}`,

explicitly a **union of coordinate-axis segments**, not its convex hull and not a full cube. Its objective is

`E L(sum_i Z_i)`,

and its central benchmark is the **one-dimensional** optimal noise cost for L:R->R. Theorem1 compares that scalar aggregate cost, not E(sum_i Zi²) for the full transcript. Even n=2 therefore does not give our full-diamond or full-square Euclidean-MSE optimum. A per-axis fixed-epsilon privacy condition cannot silently be convexified at the same epsilon: composing two axis shifts gives at most a2epsilon guarantee without an additional theorem.

The Conclusion contains an **informal vector-extension statement**: under l-infinity sensitivity the problem “decouples coordinatewise and reduces to the scalar setting,” while other norms' extensions are suggested with a citation to Kulesza2025. That comment was opened in full rather than omitted from this audit. It supplies no formal vector objective, privacy-budget allocation or all-law planar squared-Euclidean theorem in the read formal packet. We therefore record it as an **unresolved broad-claim interface**, not an authenticated exact solution of W or V, and not a claim we have disproved by source reading alone. If a full theorem giving the exact same square/MSE interface is located, it must immediately supersede any open/novelty inference here.

The formal scalar-aggregation theorem and our optimization can both hold; no contradiction or acceptance of the informal decoupling comment is asserted. No external contact was made to clarify it.

## 3. New2025 optimization framework: scalar RDP, not this planar value

[Gilani–Gomez–Asoodeh–Calmon–Kosut–Sankar, **Optimizing Noise Distributions for Differential Privacy**, arXiv:2504.14730v2](https://arxiv.org/html/2504.14730v2), June9,2025 displayed version. Actual abstract, model and Section3 optimization interface were read, not just the title.

Section3 expressly takes the query/noise output domain Z to be **the real numbers or the integers**, with allowed shifts `[-s,s] intersect Z`, scalar symmetric cost c, and a minimax **Renyi-DP** objective at order alpha under a cost budget. Its algorithms/composition comparisons recover scalar staircase and Cactus limits and numerical improvements in approximate-DP regimes. The read model does not provide a full-square, two-dimensional squared-Euclidean pure-DP optimum or a circular-core finite-optimality theorem. No algorithm or experiment was executed.

## 4. Current matched baseline and limits

The same-norm Kulesza2025/Melbourne2026 theorems still do not settle W: Euclidean squared loss is not a function only of the l-infinity radius, since `(1,0)` and `(1,1)` have equal l-infinity norm but costs1 and2. The public GoogleResearch notebook's non-matching metrics are empirical norm-error comparisons, not the missing exact all-law squared-error result, as recorded in the prior audit.

Targeted square/cube/infinity-sensitivity searches returned the claims above and previously screened scalar, approximate-DP and stronger metric-privacy sources. No matched exact finite-V resolution or every-b,r disk-core comparison was authenticated at these read interfaces. **Search misses do not prove absence; the informal2026 vector comment remains explicitly unresolved. NOVELTY_UNCLEAR continues.**

The active scientific obligation remains matching an all-law finite-epsilon lower/dual certificate with a genuinely admissible optimizer, or recording an exact structural obstruction. Affine rephrasing, coordinate-decoupling assumptions, mechanism-family optimization and standard ingredients are not counted as solutions or new problems.
