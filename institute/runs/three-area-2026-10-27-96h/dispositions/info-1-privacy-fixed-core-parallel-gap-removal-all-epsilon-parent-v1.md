# Privacy phases: fixed-core parallel gap removal for every epsilon, with exact nonradial square example

**Disposition: same-harness written support at the frozen f238 scope; the general nonradial all-law optimization remains OPEN.** For every epsilon>0 (b=e^{-epsilon}), every compact canonical core C of the source's §1 (parameter t>=0, nonconvex cores allowed), every initial radius g>=0 and every radius sequence with R_{i+1}>=R_i+1 and finite weighted mass/second moment, the geometric-phase law P_K with levels K_i=C+R_iD (D the CLOSED l1 unit ball) is feasible for the full closed-D privacy class, satisfies J(P_K)>=J(P_{K^0}) with equality iff R_i=g+i for every i, and when any gap exists the weighted signed excess at the TRUE all-law infimum V_b is strictly positive, with no V_b<1/2 requirement. For C=[-1/2,1/2]^2, R_0=0, R_i=i+1/10: V_b>=17/4 for b>=1/2, the first signed excess is at most -956/625<0, and at b=1/2 the entire weighted excess is at least 486731/165000>0. Individual summands may be negative; the per-level sign argument is refuted, the fixed-core comparator is not.

Native clock observed before composing: **2026-10-29T14:45:06-0700 PDT**; not a file-creation time.

## Adopted statements and scope

1. Theorem A (fixed-core parallel phases, all epsilon): the three claims above, exactly as reconstructed by the reviewer (feasibility by the pointwise translated-density inequality u(x+h)>=b u(x) for every ||h||_1<=1; last-gap removal via strict monotonicity of the uniform cost j(r)=M(r)/A(r) for t+r>0 and of the tail cost J_tail(r) for r>=1; infinitely many gaps by truncation with a fixed first-gap margin under dominated convergence; the signed-series identity (Z_R-Z_0)[J(P_{K^0})-V]+Z_R[J(P_K)-J(P_{K^0})]>0).
2. The square example values, parent-rechecked: A(r)=1+4r+2r^2, M(r)=1/6+(4/3)r+3r^2+(8/3)r^3+(2/3)r^4 (independent octagon integration), area increment 41/50, moment increment 9777/5000, first excess at most -956/625 given V_b>=17/4; the all-law tail bound 17/4 at b=1/2 recomputed; no-gap square cost 571/66 at b=1/2 reproduced to the series precision used; negative control (bound 2 instead of 17/4) flips the sign as intended.
3. The explicit nonparallel feasible phase K_0={0}, K_1=D, K_2=[-2,2]^2, K_i=K_2+(i-2)D is a residual witness that the inclusion conditions do not force a common core; it is NOT an optimality counterexample.

## Not adopted

- The optimizer-structure aside (source LF 32, 47, 207-209): the reduction of optimal laws to D4/four-direction-convex Steiner phases and the "minimal shells" cost-ball criterion. The reviewer's m1 reconstructs only an almost-everywhere version under explicit hypotheses; literal set equality and the hypotheses are unspecified. INCONCLUSIVE and not a premise here.
- Any status of prior reviews, author-run cells or sweeps (INCONCLUSIVE in the review); LAW642/f208 theorems; the separately frozen nonparallel counterexample (f245) and its claims.
- Attainment, global optimum, book/source equivalence, novelty, or literature status.

## Evidence and limits

- Source: /Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261029-nonradial-parallel-core-gap-removal-v1.md, SHA-256 91478ea61fed8a9a5e0f6551d11ced9f3ee890d9e1314c3a387c81a701b52286, 331 LF. Parent displayed the statement section (LF 1-34) and relies on the reviewer's receipt (raw 15-line windows 1-331, completion clock 14:22:26 PDT) for the remainder.
- Frozen manifest: /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f238-privacy-all-epsilon-nonradial-parallel-core-gap-removal/manifest-v1.json, SHA-256 7d227f70753615619cd99b1ddb5497e2f2c0a81078289c1e8bdaedee29671f13. Review: /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f238-privacy-all-epsilon-nonradial-parallel-core-gap-removal/review-v1.md, SHA-256 28aaef8771f22be7dee7108b5e348d58851d824bc86145e1f44e1dd5ecfc573a, 116 LF, **0F/0M/1m**; parent displayed every review line (raw windows 1-15, 16-60, 61-120; a further request past 120 was empty).
- Reviewer-owned controls (exit 0, <=120 s, intended-reason negatives): exact endpoint polynomial reconstruction with positive-coefficient tables, square arithmetic, nonconvex-midpoint check, closed-boundary privacy saturation at b=1/2 with an invalid-spacing negative.
- Parent control: independent exact octagon integration and series check in the retained Python kernel at 2026-10-29T14:42:30-0700 PDT (values listed in item 2); not formal verification.
- Assurance boundary: same-harness; not human, independent-model-family, formal/kernel or novelty verification. No held, f161/f162 or withdrawn material used.
