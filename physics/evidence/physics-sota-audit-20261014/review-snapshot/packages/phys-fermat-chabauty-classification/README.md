# Chabauty limit types of Fermat spirals

Book bridge: Cao Zexian's chapter on Fibonacci parastichies and least-energy/dense packing on cones, *10000 Selected Problems in Sciences: Physics* (2009), pp. **541–543**. This project addresses a precise later question about the local geometry of the planar phyllotactic model `X_alpha={sqrt(n) exp(2*pi*i*n*alpha): n>=1}`. It does not assert that this model minimizes energy on a cone or solves the whole book chapter.

## Explicit target and frozen contract — 2026-10-14 PT

Yohay Ailon Tevet, *Chabauty Limits of Fermat Spirals*, [arXiv:2506.22863v2](https://arxiv.org/pdf/2506.22863v2) (September 2025), p. 4, explicitly conjectures the non-badly-approximable limit types; p. 12 asks whether its lattice limits retain covolume pi. The topology uses **translations only**, with translation vectors escaping to infinity. Nonempty limits are affine translates, not necessarily groups through zero.

- **Claim sought:** for any real alpha every nonempty translated Chabauty limit is an affine line or an affine lattice of covolume pi. In particular neither the plane nor a translate of `R x Z` occurs. For each irrational non-BA alpha, establish that line and lattice types actually occur, with empty limits handled separately.
- **Comparable baseline:** Tevet proves a closed-subgroup-translate theorem and classifies the BA case. Bacher's 2014 Theorem 1.1 already gives uniform local lattice approximation; its Remark 3.3 gives the exact area pi. The present route is an explicit quantitative certification using that classical framework, not a claimed new approximation mechanism or first-priority theorem.
- **Missing bounded bridge:** prove two-sided local inclusions with uniform error, carry them through arbitrary translating centers and rotating frames, then prove the fixed-covolume planar-lattice compactification. Use continued fractions only for realizability, not to assume a nearest-neighbor classification.
- **Decision value:** a complete argument answers the exact type/covolume questions, potentially excluding the paper's computational suggestion that `Z x R` is achieved. A no-plane result alone would not complete this target.
- **Protocol:** deterministic rational/interval controls of both inclusions and the constants, singular and rational boundaries, and negative controls; no extrapolation from convergence plots. Write the universal argument in full and obtain an independent hostile referee review. At most one compute process; no environment modification or edits outside this folder.

## Current verdict

**SOLVED for the exact type/covolume statements. FRONTIER: DELIVERY-READY as a classical Certification; worldwide priority remains NOVELTY-UNCLEAR.** For every real alpha, a nonempty translation limit is an affine line or an affine lattice of covolume **pi**. Neither `R x Z` nor the plane, a point or a discrete rank-one group occurs. For every fixed irrational non-BA alpha, all three types occur: empty set, every affine line, and at least one covolume-pi lattice.

The proof does **not** establish all lattice shapes for a fixed alpha, optimal packing/energy on cones, or worldwide first priority. Bacher's 2014 uniform lattice approximation and area pi are the classical baseline, with his broader Voronoi-area remark also acknowledged. Tevet's explicit 2025 question supplies the target, not a guarantee of historical novelty. The independent other-vendor referee found no mathematical gap; all eight attribution/exposition findings are disposed in RESULTS.md and a focused follow-up returned **ACCEPT**.

## Reproduction and evidence boundary

From this folder:

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-venvs/phys-fractional-parentage-coefficients/bin/python code/verify.py
```

This uses the already-existing Python 3.13 / python-flint 0.9.0 environment without installation. It checks finite rational/Arb local inclusions, independent absolute-Cartesian evaluations, exact determinants, two rigorously enclosed Liouville witnesses, six negative/boundary controls and pinned source hashes; it writes `results/verification.json`. The **universal** certificate is the complete written argument in RESULTS.md, not finite numerics or a claimed Lean/kernel check.

## Files

`STATUS.md`: exact primary quotes, definitions, classical overlap and forward-citation screen. `RESULTS.md`: complete proof, quantifiers, evidence labels and review dispositions. `source/`: unedited book excerpt and primary pins. `code/`, `results/`, `review/`: deterministic finite evidence and referee records.
