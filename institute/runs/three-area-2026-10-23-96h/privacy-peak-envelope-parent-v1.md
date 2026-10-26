# All-law peak-envelope certificate and strict relaxation gap — parent disposition

Actual clock observation preceding this record: **2026-10-23T16:07:39-07:00 PDT** (`/bin/date`). Written checking and source/metadata only; no numerical root solve, integration or formal kernel was used.

## Decision

**SUPPORTED at the in-harness written-check level**, for every `0<b<1` in the full continuous-diamond all-Borel-law model:

1. Every finite-cost feasible law has a density obeying the full-tail envelope `M g_b(x-c) <= p(x) <= M` a.e., with `M=ess sup p` finite and the center **derived** from finite cost (not assumed, not attained).
2. The unique root `s_b` of `F_b(s)=(pi/2)s^2` gives a valid **all-law lower certificate**: `J >= s_b` for every feasible law.
3. The point-envelope relaxation has exact optimum `s_b` with a unique a.e. optimizer (cap on the Euclidean `sqrt(s_b)` disk, `M_b g_b` outside).
4. That relaxed optimizer **violates the fixed permitted shift h=(1,0) on a positive-area open region for every b**. Since the original infimum is attained (Prokhorov/weak-closure), `V_b > s_b` strictly for every finite b.

**Not established:** exact V_b, a quantitative gap magnitude, an original minimizer formula, feasibility of any one-peak relaxation, novelty, formal/human verification. The relaxed primal is never an admissible full-DP law and must not be presented as one. The obstruction is precisely the omitted plateau coupling: a positive-area maximum plateau forces a b-height floor on its whole diamond expansion, not only the point-centered tail.

## Evidence and full reads

- Complete285-line `information-science/evidence/three-area-20261023-96h/parallel-18/privacy-diamond-mse/proof-full-peak-envelope-relaxation-v1.md`, SHA256 `0bf1f46015d1da201677f6fa0700dee45d7e8d66599e0edda7e2ccf7ad8b95a0`.
- Actual complete149-line `mathematics/evidence/three-area-20261023-96h/parallel-18/shor-completion/peer-review-privacy-peak-envelope-v1.md`, SHA256 `637aa78ecae9a32356e55d573fd0d1d16c299ef4e205ceeb7b01bef03fd2210b`, read in full. Verdict **0F/0M/0 substantive MINOR** at the complete stated theorem, with contextual reads of the finite-V selection, the exploratory residual, the disk source/qualification and the disk parent disposition correctly treated as comparison rather than premise.

## Parent hand checks

- Null-set integration gives absolute continuity. Integer-shift iteration gives per-t domination; the bad-pair Tonelli step is applied per integer k and only **countably** many full-measure sets are intersected — no uncountable null-set union is taken.
- `g_b=(1-b)sum b^k 1_(kD)` is pointwise correct with the closed-set convention; `Z_g`, `N_g` and `F_b` are exact full-tail geometric sums.
- Finite cost bounds the near-peak centers because `J>=a_n(N_g+Z_g||c_n||^2)` with `a_n->M>0`; a convergent subsequence and the null integer-l1 spheres give the limiting envelope without an attained peak.
- `F_b` is strictly decreasing against strictly increasing `pi s^2/2`: unique root. The translated penalty is convex/even and strictly larger off zero via the midpoint gap `2||c||^2` on a positive-mass exterior region.
- The split inequality multiplies the interior cap by the negative excess and the exterior floor by the positive excess; at the root it is nonnegative. Equality forces `c=0`, cap/floor saturation and hence the unique relaxed density.
- For the fixed shift, both `delta` cases (`R<=1` giving `x0+h` radius `1+R/2`, `R>=1` giving `R+1/2`) put `x0` strictly inside and `x0+h` strictly outside with `||x0+h||_1>1`; the failure region is open and positive-area, and `b^2<b` makes it a genuine a.e. violation.
- The Laplace product law is feasible with finite cost, so a minimizing sequence is tight. Weak closure with bounded-continuous tests passes the all-fixed-h inequalities to the limit without h-dependent subsequences; `min(||x||^2,L)` gives `J(mu_*)<=V_b`, so the infimum is attained. Attainment plus the equality characterization then forbids `V_b=s_b`.

## Boundary and next obligation

This result composes honestly with the record so far: the sharp leading asymptotic `2/sqrt(3pi)`, the strict finite-b improvement of every disk core, and now an all-law certificate with a proved strict gap to its own one-peak relaxation. The genuinely open finite-V step is a **coupled-level-set dual** that pays for plateau expansions (or an equally strong all-law condition) matched by an admissible law. Continue only on that structural question; envelope-constant variants and further core-family perturbations are not the target. Each new packet needs its own actual review; novelty remains UNCLEAR.
