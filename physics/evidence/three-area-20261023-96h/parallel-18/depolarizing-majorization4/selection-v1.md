# Physics-2 selection v1 — four-qubit output majorization

Observed selection clock: **2026-10-23T13:59:51-0700**, from `/bin/date '+%Y-%m-%dT%H:%M:%S%z'`. Author: PhysicsDepol4. Status: **PROOF-OBLIGATION; unrestricted target not solved**. Only written research/source operations are admitted.

## Literal target and conventions

For every positive semidefinite trace-one operator `rho` on `(C^2)^tensor4` and every physical **replacement** parameter `0 <= p <= 4/3`, prove

`lambda_down(D_p^tensor4(rho)) prec lambda_down(D_p^tensor4(|0000><0000|))`,

or give a rigorously positive exact counterexample and a rigorously violated Ky-Fan sum. Here `D_p(X)=(1-p)X+(p/2)Tr(X)I_2`; `x prec y` means `sum_{j=1}^k x_j^down <= sum_{j=1}^k y_j^down` for **every** `1 <= k <= 15`, with equal total trace. This is not the Pauli total-error parameter: the latter is `3p/4`.

Pure inputs suffice by convexity of each Ky-Fan sum and linearity of the channel. Global spin flip sends the output spectrum at `p` to that at `2-p`, so it suffices to work at `q=min(p,2-p)` in `[0,1]`. For `p>1` it is essential to reorder the product spectrum rather than treat `1-p/2` as its larger entry. Write `a=1-q/2 >= b=q/2`. The product spectrum is `a^(4-h)b^h` with multiplicity `binom(4,h)`, in increasing Hamming weight `h`.

## Book/source relationship and current openness evidence

This is a **modern scoped instance**, not a literal four-qubit theorem printed in the 2009 book. It belongs to the book's quantum-channel theme (book pp. 591–592, PDF pp. 626–627); the book's capacity question must not be relabeled solved by a spectral subclaim. Source-volume identity/mapping: `books/README.md`.

The actual primary open statement read is Song–Wang–Tomamichel–Fang, [arXiv:2609.37240v1](https://arxiv.org/abs/2609.37240v1), Eq. (2), definitions (1), (7)–(9), and introductory text: exact majorization is conjectured, while Theorem 1 is approximate/asymptotic. Local PDF SHA-256: `456ba1cd2c82b37db9ac5e59986f1d54c9e90995daacc678922a4ab43ebfd6df`. Live arXiv abstract/API and exact-title search still returned this v1 lead. No later exact four-qubit resolution was located in that bounded refresh; this is **not a certified exhaustive openness/novelty result**.

Corpus gate: local `/Users/jinleic/jinleic-workspace/math/{CONTENTS.md,overview.tex,README.md}` was searched for `depolariz`, `majorization`, `log-determinant`, and `spin.alignment` without matches. The live remote [openai/math CONTENTS](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md) was fetched and searched for the same strings without matches; a bounded GitHub site search returned only the repository. This rules out a matched advertised claim in these indexes, not every unindexed argument.

Amosov [arXiv:2401.05104v1](https://arxiv.org/html/2401.05104v1) is a priority/import lead requiring care: its majorization condition (8) and Proposition 1 are not an automatically usable theorem for this problem. The primary text has been read; its applicability must be established, not inferred from an abstract. The existing three-qubit result and the weaker shifted-logdet order are baselines, not this slot's result.

## Actual strongest internal baseline

The short assignment label resolves to `physics/evidence/six-lane-20261016/depolarizing-majorization-n4/`. Read: current README, frozen `PROOF.md`, `ADDENDUM_v1_1.md`, actual `review/codex-frozen-partial-output.md`, the exact manifest and `zlemma-route/FROZEN_STATEMENTS.md`.

- All physical `p`: indices `{1,5,11,12,13,14,15}` already closed.
- `2/3 <= p <= 4/3`: indices `{2,3,4}` already closed.
- Remaining: central `{6,7,8,9,10}` away from trivial noise values; low-noise `{2,3,4}` for `0<p<2/3`.
- Plain twirled PPT is **provably loose**, not merely inconclusive: exact primal points give excess one for the central `U_2` bounds, and excess `2,2,1` for `U_3(2,3,4)`. The level-two numerical hierarchy did not close the gap. The earlier Pauli-Gram/Z-map relaxation is also loose. None is a state counterexample.

Pinned baseline proof: `6789e392dbc70dbed479ba8f307e0eb6c786d735de691d425583ec0d8b2fce8a`; addendum: `73b6abb4e0a10b4fb9fe54ae5be853130c45a466b65a258c17385bc9911267d4`; Gram outcome: `b3db2407c950fc56bdbbe041dce7aa329ed403685886deef6951cec38166b71b`.

## Consequential missing inequality and headroom

Define `X_s(rho)=sum_{|I|=s} rho_I tensor I_{I^c}` with **unnormalized** identity factors. The first frozen missing obligation is

`U_2(6): K_6(X_2(|psi><psi|)) <= 19` for **every** unit four-qubit vector `psi`.

The stronger central family is `K_k(X_2)<=k+13` for `6<=k<=10`. Its product reference has spectrum `(6,3,3,3,3,1,1,1,1,1,1,0,0,0,0,0)` and trace 24. This is a sufficient missing ingredient, not a claim that termwise majorization is necessary for the channel target.

Bridge: `D_q^tensor4(rho)=sum_s (1-q)^s q^(4-s)2^(s-4) X_s`. At `k=6`, all other subset sizes have established bounds, and their product references share the Hamming order. Therefore a proof of the displayed `U_2(6)` closes the **previously missing k=6 channel inequality for every physical p**, not merely `p=1/2`. At `p=1/2` the exact channel target is `K_6 <= (81+4*27+9)/256 = 99/128`.

## First bounded attack and acceptance

Use **pure-state compatibility and quadratic spectral information**, not another PPT solve: derive `Tr X_2^2` in terms of one-qubit Bloch lengths and the four-qubit spin-flip overlap, then derive a universal Ky-Fan envelope. Determine exactly which entangled-state region this closes and isolate the complementary near-product obstruction. Follow with a written perturbation/compression argument only if it preserves unrestricted quantifiers. A restricted criterion must remain explicitly partial.

Verification route for a complete candidate: immutable proof snapshot and source hashes; independent in-harness written reconstruction arranged by parent; exact algebra checked symbolically on paper. No numerical optimizer, scientific script, eigensolver, enumeration, solver or executable certificate replay is authorized. Any later compute requires exact source/input-pinned parent GO first.

Redirect condition: if a matched primary source already settles the unrestricted target, report it and request parent collision-check of a **distinct** replacement outside all eighteen roster entries. If the quadratic envelope cannot control the residual region, retain the honest partial inequality and identify the additional compatibility estimate rather than pretend that a relaxation proves majorization. Full-target status remains unresolved unless every missing index/parameter is covered or an exact violated partial sum is supplied.
