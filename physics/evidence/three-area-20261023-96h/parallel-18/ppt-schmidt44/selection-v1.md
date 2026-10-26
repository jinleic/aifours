# P44 selection v1 — ququart PPT Schmidt number three

Observed immediately before creation: **2026-10-23T14:05:39-07:00**. Owner PhysicsPPT44, slot physics-3. Governing contract: `institute/runs/three-area-2026-10-23-96h/contract-v2-eighteen-slots.json`, with both parent errata read. Deadline remains 2026-10-27T12:35:38-07:00. This is a source/statement freeze, not scientific execution admission.

## Literal target and acceptance

Does there exist a Hermitian `rho in M_16(C)` such that `rho >= 0`, `Tr(rho)=1`, `rho^{Gamma_B} >= 0`, and `SN(rho) >= 3` across `C^4 : C^4`? Here `SN(rho)` is the minimum, over all pure-state convex decompositions, of the largest Schmidt rank in the decomposition. There is no reality, rank, symmetry, sparsity, grid, or support restriction on the target.

A positive answer requires an exact density matrix and a Hermitian `W` satisfying `vec(C)^* W vec(C) >= 0` for **every complex 4 by 4 matrix C of rank at most two**, together with `Tr(W rho)<0`. A negative answer requires `SN(rho)<=2` for **every** PPT 4 by 4 state. A construction in 4 by 5, an NPT state, an ordinary indecomposable one-positive map, or exclusion of a chosen ansatz does not answer P44.

## Book connection, exactly scoped

The book is *10000 Selected Problems in Sciences: Physics*, Science Press 2009, ISBN 978-7-03-024269-3, SHA-256 `a4524a2fb26903b13dc76b0fc8edabefe0a3d822b8a400d6149658317631193f`. The source entry `books/README.md` and retained extraction `physics/evidence/physics-hard-20261015/sources/phys-p0591/excerpt.txt` were read. Article **Quantum Channel**, Zhou Xiangfa and Guo Guangcan, book pp.591–592 / PDF pp.626–627, discusses entanglement as a communication resource and the distinction between assisted capacities and regularized quantum capacity. P44 is a modern finite-dimensional question about the strength of an undistillable resource; the book does **not** literally ask P44. A solution would not solve the full channel-capacity article.

## Primary-source/status baseline

1. Krebs–Gachechiladze, [2402.12966v1](https://arxiv.org/html/2402.12966v1), submitted 20 February 2024, constructs PPT SN3 in 5 by 5, and SN3 in 4 by 12; its introduction explicitly leaves the smallest 4 by d open. Captured raw HTML SHA-256 `015de34f2a82f286caba8f8049c0f6df415199fa14ee5154834d45c3cd4685db`.
2. Krebs–Gachechiladze, [2509.07086v1](https://arxiv.org/html/2509.07086v1), submitted 8 September 2025, Theorem 5 and Eqs.(10)–(12) give PPT SN3 in **4 by 5** using local extensions. Supplement E proves its particular intermediate 4 by 4 state has SN2. Theorem 4 closes one-sided extensions of rank-four two-qutrit PPT cores, not every 4 by 4 state. Captured raw SHA-256 `115f3102fc7f3c9be9992cbb130633da40d729b6f3c353338de0153770ea5070`.
3. Johnston–Lovitz, [2609.11849v1](https://arxiv.org/html/2609.11849v1), submitted 10 September 2026, Introduction and Theorem 1 expressly do not improve the small-dimensional lower bounds; in 4 by 4 its bound is `4-floor(sqrt(7))=2`, not three. Its perturbation argument requires `rank(sigma)<(4-2)^2=4` with positive-definite partial transpose, whereas its cited universal minimum rank is seven. This is a limitation of that mechanism, not a universal SN bound. Captured raw SHA-256 `8c017ce9f44a2dcc459bf55acace63109f0f2d7eaebb7752bd592ec2ae4f25aa`.
4. Yang–Leung–Tang, [1603.03534v1](https://arxiv.org/html/1603.03534v1), submitted 11 March 2016, proves all two-positive M3-to-M3 maps decomposable. It does not supply the M4-to-M4 classification. The generated HTML's displayed August 2026 title-page date is not its submission date. Captured raw SHA-256 `d4dd1f3e7ef14cb4befac63381440064acbe3f1387c36269e8b09f7388b5f698`.
5. Newly located Park, [2602.09860v1](https://arxiv.org/html/2602.09860v1), submitted 10 February 2026, Theorem 1.1 explicitly classifies the symplectic-covariant two-parameter family: for d=4 every two-positive member is decomposable and every PPT state in the associated invariant family has SN at most two. Hence depolarizing a Breuer–Hall map within that symmetric family is **already excluded**, not a new discovery route. The paper's introduction says “upper bound” in a passage describing the prior constructive d/2 scaling; that wording is not an unrestricted SN upper-bound theorem. The actual theorem quantifiers are family-restricted.

The strongest matched lower-dimensional construction read is 4 by 5. Accessible containing open statements exist, but no checked primary source certifies global present-day openness of the exact 4 by 4 instance. Status is **UNCERTIFIED-OPEN**, not already solved in the exercised screen. Search misses are not openness or novelty proof.

## Corpus/later-claim screen actually exercised

Read root README, physics index, current physics round selection and its source captures. Searched local `math/CONTENTS.md` and `math/overview.tex` for `Schmidt.number`, `bound.entangl`, `2-positive`, `decomposable.map`, then the broader `Schmidt|PPT|distill|entangl|positive map`. Re-fetched public [openai/math CONTENTS](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md), 638727 bytes, SHA-256 `cc7c0b8a1cdedd845a777e77cf682657308503daf8346c1349e06e9259d063c2`, and searched the same broad terms. Family272 concerns secret-key/PPT-composition claims in dimensions ten and twenty-one, not an exact P44 claim. This is a contents/overview screen, **not** full-text review or acceptance of the corpus. No direct target entry was found. Current arXiv abstracts for all three initial leads plus 2509.07086 were read; a v2 HTML request for 2509.07086 returned404, which is not proof no later version exists. Web searches of exact dimension/map variants identified Park's classification; ordinary 4 by 4 PPT entangled-state papers are not SN3 results.

## Frozen construction mechanism and bounded attack

Use the **known 4 by 5 local-extension state as input, not as this round's result**, and compress Bob's two auxiliary levels coherently to one level. In the convention `|ij>` with i=0,...,3 and j=0,...,4, the unnormalized input read from Fig.1, Eqs.(10)–(11) and the extension weights is

`R45 = |00+11+22><00+11+22| + |01+12><01+12| + |10-21><10-21|`
`      +3|02+34><02+34| +3|20+33><20+33|`
`      +3|30><30| +3|32><32| +3|23><23| +3|04><04|`.

Here `|x+y><x+y|` denotes the projector on the indicated unnormalized sum. Its trace is31. The original paper uses a harmless sign reparametrization between some core-coordinate displays; use the explicit vectors above, not a mixture of parameter conventions.

For arbitrary complex `(u,v) != (0,0)`, set `B_uv|j>=|j>` for j=0,1,2, `B_uv|3>=u|3>`, and `B_uv|4>=v|3>`. The candidate is

`rho_uv = (I_4 tensor B_uv) R45 (I_4 tensor B_uv)^* / Tr(...)`.

It is exactly 4 by 4 and PPT by local congruence. There is no claim yet that it has SN3. The **first bounded attack** is to determine whether this coherent merging preserves the source's Schmidt-rank-two range obstruction, and then seek an exact Schmidt-rank-two decomposition or a genuinely two-block-positive separator for the merged state. This starts with all complex u,v, not a numerical grid. The source's u=0 or v=0 intermediate endpoints and symmetric map families are baselines only. A structural no-go proved here is labeled restricted and does not change the unrestricted P44 target.

Source screening produced informal diagnostic manipulations before this written freeze; no resulting theorem, solver output or discovery is being grandfathered as accepted. Subsequent formal candidate snapshots must expose the full algebra and state the achieved quantifiers.

### Missing ingredient, consequence, verification, redirect

The missing ingredient is an exact SN3 witness that survives dimension reduction, or a rigorous decomposition showing why the compression route cannot supply one. A successful compression plus witness would answer P44 positively. A restricted no-go would stop this specific route, not establish universal nonexistence.

Written verification must independently reconstruct positivity/PPT, the coefficient-matrix rank conditions, and all decomposition or separator identities. Parent plus a separate in-harness reconstruction on pinned bytes are required before acceptance. No numerical SDP, scientific program, enumeration, compilation, proof kernel, CLI review, build/test/lint/formatter, or scientific replay has been run. Only source retrieval, text extraction and metadata hashing were executed. Formal verification and external expert review are **not performed**; novelty is separate.

Redirect if (a) a current source solves the exact P44 target, immediately report and request a collision-checked distinct replacement; (b) a full algebraic obstruction/decomposition closes this compression family, return to the unrestricted residual rather than claiming P44; (c) range tests alone are inconclusive, do not call UNKNOWN a no-go or run an unadmitted solver. Any scientific executable requires an exact separately frozen parent GO.
