# PH7 nonuniform construction on the closed band [7/9, 41/50]

Native clock actually observed before writing: **2026-10-28T17:41:49-0700 PDT**. This disposition concerns the v2 six-rate construction only, not the separate v1 or v3/v4 candidates. It is same-harness written support backed by exact rational computations; not a human, cross-vendor, kernel, publication, or novelty verdict.

## Exact result

For every `a>c>0`, `b>0`, put `d=a-c` and `z=b²/d²`. For every `z` in the **closed interval `[7/9,41/50]`**, the seven-state `T`, initial row `alpha`, and exit `-T1` constructed in the [v2 candidate](/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/frontier-20261028-ph7-explicit-band-41over50-v2.md) give an actual continuous-time phase-type representation of

`H(s) = c(a²+b²)² / ((s+c)((s+a)²+b²)²)`.

The construction has `T` Metzler and Hurwitz, `-T1>=0`, `alpha>=0`, and `alpha 1=1`. It is one actual, linked matrix/input/exit, not independently optimized coefficients. The conclusion here is **PH order at most 7**.

**Conditional exact order.** The [prior B6 disposition](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/PH6-unrestricted-parent-disposition-v1.md) states that the same registered family has no representation of order at most six for `z>1/2`. Assuming that previously written-supported theorem at its exact scope, the minimum is **exactly 7 on `[7/9,41/50]`**. The prior B6 proof was not re-reviewed in this parent check. Assuming additionally the [earlier PH7 band disposition](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/PH7-entire-rational-seven-ninths-band-parent-v1.md), which records exact order 7 on `[13/20,z_star]` with `z_star>7/9` under its own stated dependencies, the overlapping union yields exact order 7 on `[13/20,41/50]`. This is a conditional composition, not a fresh verification of the earlier source DAG.

## Inputs and complete reads

- V2 candidate: 152 LF, SHA-256 `8e9d10653ef1c930a07bf8a6ee06ae6e99f61194eccb2edaeeac4f51c4ffde91`, read completely, including its ending.
- [f18 v2 reviewer addendum](/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody/frontier-review-f18-ph7-seven-band-addendum-1-v1.md): 80 LF, SHA-256 `d90e4eae2de36c075d459321e9066191b22095baa05a3671e67bb066e3fd4b1b`, read completely. Same-harness verdict: no new fatal, major, or minor at the v2 scope. Its separate symbolic checker used SymPy and its own prior helper. The earlier f18 review's v1 wording minor concerns fixed-zero off-diagonal entries and is not a v2 finding.
- The [registered target](../written-releases/math-1-ph-order-definitions-v1.md), the complete earlier B6 disposition, and the earlier PH7 band disposition were read for the stated target/import boundaries. Their underlying proof DAGs were not re-reviewed here.

## Parent reconstruction and independent execution

The raw rates are `(1331/1000, 341/250, 1339/1000; 33/25, 257/250, 132/125)`. The source defines the ten linked quantities `L`, `Lp`, `Lq`, `Lw`, `LB`, `LC`, `Lphi`, `LD1`, `LD2`, and `LD3`. All their Bernstein coefficients are strictly positive on the whole closed band. Thus `L,p,q,w,B,C,phi,D1,D2,D3` are positive for the same parameter `z`.

The parent independently wrote and actually ran [parent-ph7-v2-exact-check-v1.py](../review-waves/f18-ph7-seven-band-construction/parent-ph7-v2-exact-check-v1.py), SHA-256 `5eaf4b4462d3f8c32e0872007713fa0d4af148c815544047637cc885d2a5ec9b`, with Python standard-library `Fraction` and independently implemented sparse bivariate-polynomial operations. It imports neither the author's nor the reviewer's checker. The run exited 0 and verified, as complete polynomial identities in `(y,z)`, the actual seven-by-seven determinant `det(yI-G)=D_z(y)Q(y)` and the rank-one determinant-update/adjugate numerator `beta adj(yI-G)e7=Q(y)`. It recomputed all ten full Bernstein lists as exact rational coefficients and found each positive. Two in-memory mutations, changing a feedback entry or an initial-vector coefficient, were rejected by their respective identities. The [receipt](../review-waves/f18-ph7-seven-band-construction/parent-ph7-v2-exact-receipt-v1.json) records the command and result.

The same script independently solved nine actual rational normalizations: both band endpoints and the midpoint `719/900`, each with `c/d` equal to `1/2`, `1`, and `2`. Every case had positive normalizer, nonnegative normalized initial law, Metzler generator and exact exit-row ties; the actual resolvent agreed with the target at `s=0,1,3` in each case. These 27 transfer evaluations are diagnostics, not the all-parameter proof.

For arbitrary `c/d>0`, the written recurrence gives positive `h`. Six of the equations `(cI-G)h=D_z(c)e7` are immediate; the remaining center equation follows by eliminating the two chains and using the full determinant identity at `y=c`. The numerator identity and `Q(c)>0` give `beta h=1`. The characteristic factorization has the roots of `D_z` and `Q`; `p,q>0` put both roots of `Q` in the open left half-plane, and shifting by `-c` makes `T` Hurwitz. Finally, constructing at `c/d` and scaling the generator and exit by `d` gives the original dimensional transform. This is the all-`c,d` argument; it is not inferred from the nine rational samples.

## Remaining boundary

`8/9` is outside this band. No all-topology PH7 exclusion, maximal endpoint, full minimum-order function, or solution of the general printed minimal-representation problem is established. The later algebraic-endpoint and richer-topology candidates have not been reviewed here. No novelty/priority is asserted, and historical held outputs are not used as premises or retroactively cleared.
