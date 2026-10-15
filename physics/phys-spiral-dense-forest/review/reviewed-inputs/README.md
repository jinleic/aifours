# An exact-radius spiral dense forest

Date: 2026-10-14 (America/Los_Angeles).

**Precise mathematical verdict: SOLVED by the written theorem in `RESULTS.md`.** Evidence class: **Certification**, using classical ingredients. **Novelty/priority: NOVELTY-UNCLEAR**, not a worldwide-first claim. Independent referee results and dispositions are recorded in `RESULTS.md`.

The physics-book entry by Cao Zexian, “Are the Fibonacci Parastichous Spirals a Least-Energy Configuration on Conical Surface?” (*10000个科学难题·物理学卷*, 2009, pp.541–543), motivates phyllotactic distribution questions. This folder addresses an explicitly selected **broader planar visibility refinement**, not cone-energy minimization, Fibonacci packing optimality, or a fixed-angle sunflower.

## Exact published target

Tevet, [*Chabauty Limits of Fermat Spirals*, arXiv:2506.22863v2](https://arxiv.org/abs/2506.22863v2), Further Questions, PDF p.12:

> “The author conjectures that there is a spiral set that is a dense forest”

His spiral sets have exact radii `sqrt(k)` and arbitrary unit directions; no uniform-separation/Delone condition is imposed. His theorem rules out **constant-angle Fermat spirals**, not these general spiral sets. `STATUS.md` records the original definition, later-source screen, older contrary conjecture, and limits of novelty clearance.

## Construction and universal result

Let

\[
Q=\frac1{\sqrt3}\begin{pmatrix}1&-\sqrt2\\\sqrt2&1\end{pmatrix},\quad
F=(\mathbb Z^2\setminus\{0\})\cup Q(\mathbb Z^2\setminus\{0\}).
\]

Enumerate **all** points by `(integer squared norm, lattice label, integer coordinates)`, obtaining `f_k`. Set `s_k = sqrt(k) * f_k / |f_k|`.

The complete proof establishes:

- no nonzero overlap and no common rational line direction between the two lattices;
- uniform finite hitting times for their union, by compactness in direction and both torus phases;
- `|s_k - sqrt(2*pi)*f_k| = O(|f_k|^(-1/3))`, uniformly across every tied shell, from the classical circle-discrepancy estimate;
- stability of all-segment visibility under this vanishing displacement, with the finite core and removed origin handled explicitly;
- exact radial counts `#(S intersect closed B_R) = floor(R^2)` and a single decreasing visibility function for **every position/orientation and every positive rectangle width**, including open boundaries.

The base finite-grid forests are established prior art (Adiceam–Solomon–Weiss; Shirandami). The target-specific bridge is the rank correction plus uniform visibility transfer. No optimal visibility exponent, Danzer set, or uniform discreteness is claimed.

## One-command replay

From the workspace root:

```sh
scratch/ai4s-venv/bin/python -B ai4s/phys-spiral-dense-forest/code/verify.py
```

The deterministic script independently enumerates lattice points by a bounding square and by exact squared-norm shells; checks algebraic radii and rational-direction identities; uses exact rational pi enclosures to bound finite rank displacements; tests wrong-grid/rotation/scale controls; and records separately labeled floating-point segment observations. **The finite sample is not the universal proof or a visibility certificate.**

Observed checks passed: **25,704** exact norm identities; independent enumeration at radii **8,16,32,64**; **6,400** exact direction-pair controls; **257** radial thresholds; largest sampled tie **64**; and omitted-grid, zero-rotation, wrong-scale controls. The certified finite displacement upper bound over base radii 32–64 is approximately **0.318797** (exact fraction in the receipt). The two 216-segment geometric samples are explicitly empirical, not a global visibility certificate.

## File map

- `RESULTS.md`: precise theorem and full proof, evidence ledger, observed verification and review dispositions.
- `STATUS.md`: primary explicit-open quote, exact-definition audit, SOTA, bounded forward/backward screen.
- `source/problem.zh.txt`: unchanged supplied book excerpt.
- `source/`: pinned primary PDFs/text, Tevet conjecture page, dated OpenAlex/arXiv records, provenance.
- `code/verify.py`: deterministic exact and empirical scientific replay, no solver/search.
- `results/verification.json`: finite exact controls, rational bounds, first 64 labels, empirical observations and code hash.
- `results/source-sha256.json`: source hashes.
- `review/`: folder-confined read-only referee prompts, pinned inputs, raw responses and receipts.

The most valuable external next action is a human discrete-geometry referee's assessment of the exact-definition proof and a broader backward/forward priority search. No Lean/kernel, human-peer-review, or publication-priority certification is claimed.
