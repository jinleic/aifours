# Additive clarification: strictness only on admissible compactification faces

Owner MathResearch96h-2 / math-1. Native clock observed before writing: **Thu Oct 29 14:14:33 PDT 2026**. This new clarification supplements, but never edits, `frontier-20261029-ph7-global-caller-face-obligations-addendum-v1.md`, SHA256 `e9fdf9f05350032281c7e885adc537b52328520bf9a59384e8cf79eeede82d90`, and the unchanged global candidate SHA256 `b2b7770d8b024782c5d0c1cfbd8f6e01368892801d1f3882e7b3279b59059ca5`. It responds to the parent's **reported** f223 observation: an apparent conflict between the blanket sentence about strict bounds on closed cells and the QO/HO permission for zeros on compactification boundaries. The author has not read the f223 review body; no statement here is attributed to a full review read. f223's completed frozen scope did NOT include this later file, and its result is not retroactively changed. Parent disposition is pending; NO full-global GO.

## Clarified QO/HO predicate

For positive finite rates, `r_i=s_i/(1-s_i)` has **actual domain** `(0,1)^6`. The compactified polynomial P is continuous on the closed leaf cube and the whole closed parameter interval J after multiplication by the positive clearing factor on the actual domain. For a `pos` leaf, the intended sufficient rule is exactly the specific rule in §4 of `e9fdf9f0`, NOT a requirement that P have a strictly positive minimum on the ENTIRE closed leaf:

1. All Bernstein coefficients of P on the closed spatial leaf x J are **nonnegative**.
2. The path has depth at least6. At each spatial leaf vertex whose six coordinates are all in `(0,1)`, **every** z-parameter Bernstein coefficient at that vertex is strictly positive; there is at least one such vertex.

An entire face fixing some `s_i=0` (rate zero) or `s_i=1` (infinite rate) contains NO actual positive finite-rate point. Its polynomial values and coefficients may be zero, provided (1) holds. By contrast, a dyadic leaf face at an interior coordinate `0<s_i<1` IS admissible: condition (2), together with depth>=6, gives a strictly positive coefficient supported in the relative interior of every such face and each of its admissible subfaces, for each parameter index. Thus P is strictly positive at every actual finite-positive point of the closed leaf, including shared internal faces and both endpoints of J. The infimum over the actual open domain may nevertheless be zero; a positive rational lower bound over the whole closed leaf is NOT required. Example: P=s_1 is positive on the actual open cube but vanishes on the irrelevant face s_1=0.

Consequently, interpret the earlier general sentence "Every strict inequality needs a strictly positive rational lower bound ... on the whole closed cell" as applying to the **uniform closed-domain rules where such a bound is explicitly required**, not overriding the QO/HO rule above. A single positive coefficient somewhere is still insufficient: P=t with an admissible INTERNAL lower face can vanish there and must fail the vertex rule.

## Other selectors and boundaries

NB, MC, SB and MP use the finite closed rate boxes and their stated exact whole-cell strict/non-strict tensor predicates; all z and, where applicable, both independent dual-interval endpoints remain included. R3's Abar<=0 and Dbar<=0 rules are non-strict on the closed compactified superset; its current all-coefficient-strict f1-4<0 rule is a deliberately strong SUFFICIENT predicate, not a claim that an artificial infinity face must be strictly negative for the underlying theorem. If the strong rule cannot cover a boundary, the checker must route it with another sound leaf rule or return INCOMPLETE; it must not convert failure to an exclusion. The current semantic clarification makes no claim that the seven required exact covers exist.

The earlier compactification test suite has synthetic controls for an irrelevant zero outer face and a zero admissible internal face. Those controls are not global leaf certificates, and no GLOBAL obligation has been run. M1 and the prospective M3 review/parent disposition remain open.

END — QO/HO require strictness at actual finite-positive points and admissible internal faces, not at excluded zero/infinity compactification faces.
