# Addendum: the repeated-hidden-root trace bound is strict

Status: **WRITTEN**, awaiting independent scientific review. This is an additive strengthening of `frontier-20261029-ph7-critical-repeated-hidden-root-bound-v1.md` (SHA256 `17924ce6bfa54fd9d78456d9a3aaacf3c4cbac46f2c4cc81126a9d65442ec622`), not an edit to that pinned file.

Under the hypotheses of that manuscript, the hidden decay rate actually satisfies

`r > 4/5 + sqrt(434)/15`.

If equality held, the trace-square equality conditions recorded in the original source force all seven diagonal escape rates equal to `a=(4+2r)/7` and every directed two-cycle product to vanish. Since there are no bidirectional edge products, the exact third-trace expansion gives

`tr(G^3) >= -7*a^3`:

all diagonal terms total `-7a^3`, the repeated-index two-cycle terms vanish, and all distinct-index directed-triangle products are nonnegative. The target spectrum gives `tr(G^3)=20/3-2r^3`. Therefore

`20/3-2r^3+7*((4+2r)/7)^3 >=0`,

or, after exact simplification,

`-(2/147)*(135r^3-72r^2-144r-586) >=0`.

At the equality candidate `r_0=4/5+sqrt(434)/15`, the cubic has exact value

`135r_0^3-72r_0^2-144r_0-586 = (434*sqrt(434)-4802)/25 > 0`.

The last inequality is immediate from `sqrt(434)>20`, since `434*20>4802`. Thus the required third-trace inequality is violated. Equality is impossible, proving the strict bound. No selected numerical state or computational proof is used; the displayed rational-radical simplification was also checked symbolically in the owner's kernel.

This excludes only equality in a necessary bound conditional on coincident hidden roots; it does not establish that hidden roots coincide, rule out PH7, prove a new PH6 theorem, confer independent scientific review or formal verification, or establish novelty or parent adoption.
