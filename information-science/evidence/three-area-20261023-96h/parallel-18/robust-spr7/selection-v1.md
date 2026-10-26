# Info-2 selection v1 — universal degree-seven robust SPR synthesis

Observed clock immediately before creation: **2026-10-23T14:07:15-0700**. Owner: InfoSPR7. Write root is this directory only. The eighteen-slot contract and both parent errata govern this work; no scientific execution is authorized or performed.

## Literal target and quantifiers

For every pair of finite endpoint vectors `l,u in R^7` with `l_j <= u_j`, let

`K(l,u) = {a(s)=s^7+a_1 s^6+...+a_7 : l_j <= a_j <= u_j, j=1,...,7}`.

Assume **every** member has all complex roots strictly in the open left half-plane. Prove that there is **one fixed** real polynomial `b` of **exact degree seven**, allowed to depend on `l,u` but not on the denominator or frequency, such that

`Re(b(i omega)/a(i omega)) > 0` for **every** `a in K(l,u)` and **every finite real** `omega`, including zero; or give an exact robustly Hurwitz box and an exact obstruction proving no such numerator exists. Degenerate closed coefficient intervals remain allowed. No common-factor cancellation may substitute for the stipulated denominator stability. The problem is monic; uncertain leading coefficient is a distinct variant, not silently included. No extra positive lower bound at infinite frequency is imposed beyond what follows from the equal-degree strict formulation.

## Book and modern source relationship

- Actual book images read: `information-science/robust-spr-interval-synthesis/sources/book/pdfpage-0701.png` through `0703.png`, book pp680–682. Page680 defines `P^n` as exact-order polynomials and requires `b in P^n`, `a in H^n`, and strict positivity for all real frequencies. Page682 explicitly poses sufficiency for stable interval families of order greater than four. The book does not itself say monic.
- [Wang–Yu, arXiv:math/0202242v1](https://arxiv.org/html/math/0202242v1), actual Sections1–2 read: its interval family is monic, and its low-order interval result covers `n<=4`; fixed even or odd parts are already known synthesizable. Its introduction sometimes uses the reciprocal convention, so this selection follows the book's denominator/numerator definition rather than that wording.
- [Xu–Dou–Ji–Wang–Yu, arXiv:2609.26541v2](https://arxiv.org/html/2609.26541v2), actual Theorem2.1 and Section2 definitions read: monic sextic closed boxes, exact degree-six numerator, all members and all finite real frequencies, strict Hurwitz denominators; degenerate intervals allowed. Sections5/8 explicitly separate double contacts from global positivity and assert no arbitrary-order conclusion. Its claimed Lean development is **not authenticated by this worker**: no compilation, replay or imported axiom conclusion.
- [Latest public quintic README](https://raw.githubusercontent.com/dgjszy/quintic-spr-proof/main/README.md) read: the same equal-degree full-box statement at degree five and an explicit disclaimer of a general higher-order claim. This is source-status evidence, not a kernel replay.

## Strongest matched baseline and status

Current dossier: `information-science/robust-spr-interval-synthesis/README.md` and complete relevant mathematical statements/proofs in `work/theory.md`, especially I–M, together with `evidence/continuation/review-resolution.json`. Baseline SHA256s:

- `work/theory.md`: `0194378f4311ab4dbd00b4b9a24f84c2208678d1108f0ce8eb9c546546859478`.
- dossier `README.md`: `b9afd01e3f30274c95fa8a0a7369cc2348ab20ec60c9cdc344224f633d0f28fc`.
- review disposition: `7d4f9475ae71628c06b0c86f229bbbed441c6af95b1527e7d7c022c33a2013b3`.

The baseline already proves all-order critical-contact certificate alternatives, contact rank, unwrapped phase restrictions and a closed-to-strict transfer/radial-boundary equivalence. It already gives an exact degree-seven countercontrol to the arbitrary-Hurwitz-contact-vector shortcut. **None is this round's discovery.** The universal positive pairing mechanism remains absent, including partial/collapsed radial boundary strata and zero/infinity critical supports.

Current openness: **UNCERTIFIED-CURRENT-OPEN**. The book contains an explicit primary open statement and the bounded current refresh located no matched degree-seven solution, but search misses do not certify openness or priority. Current checks include the sextic primary article, quintic live README, author's public repository inventory and searches for seventh-order/degree-seven/arbitrary-order interval synthesis. The author's inventory listed quintic and sextic projects, not a degree-seven project. This does not exclude unpublished or differently named results.

Required corpus screen performed before attack: local `/Users/jinleic/jinleic-workspace/math` searched for strictly-positive-real/SPR synthesis/interval polynomial/Kharitonov terms; hits were unrelated token adjacency or generic positive-real wording. The live remote [openai/math CONTENTS.md](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md) was fetched and searched for strictly-positive-real/SPR synthesis/interval polynomial/Kharitonov/Hurwitz terms: no matched claim. The remote inventory is not a full remote-source audit and is not an openness certificate.

## Missing ingredient and consequential delta

Universal success needs either a globally nonnegative numerator for every radial degree-seven stability-boundary box (with strictness then transferred correctly), or exclusion of both exact critical support alternatives. Neither low-order segment results nor choosing a Hurwitz vector in the contact kernel suffices.

First bounded written attack: test whether the attractive **Routh degree-lowering plus coefficient-interval hull** route can legitimately bring the new sextic theorem to degree seven. Preserve coefficient correlations exactly, rather than treating the reduced interval hull as automatically stable. Seek an all-parameter exact obstruction, not a floating-point example; if the route fails, construct a genuine common numerator for the original obstructing degree-seven families and prove global strict pairings analytically. This should distinguish a failure of intervalized induction from an actual counterexample to the target. A positive-residue partial-fraction bound is the intended verification mechanism, not another feasibility encoding.

Pre-freeze disclosure: source reading and preliminary informal algebra suggested a fixed-odd-part one-interval family as a stress test. No file-backed candidate, numerical sample, scientific program or executable check was produced before this freeze. Fixed-odd-part synthesis is prior art and will not be relabeled an unsolved subproblem or a discovery.

## Verification and redirect conditions

A complete manuscript must display the literal parameter box, a symbolic all-member Hurwitz proof, the degree-lowering map, an exact unstable member of its interval hull, an actual degree-seven common numerator for the original family, and a whole-half-line strict-positivity proof including zero and infinity. New material is candidate written reasoning until separately reconstructed on pinned bytes; no kernel, human or cross-vendor claim. Scientific executable checks need an exact parent GO first.

If the induction route survives, pursue its actual correlated-family lifting obligation without silently importing a false box hypothesis. If it fails, record the exact route obstruction and its original-target gap, then pursue only a materially different analytic ingredient; do not sample more boxes. If a primary source settles the universal degree-seven target, notify parent and propose a distinct replacement outside all eighteen entries for collision approval.
