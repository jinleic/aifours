# Spiral Delone sets with uniform asymptotic density

The physics-book chapter by Cao Zexian, *Are the Fibonacci Parastichous Spirals a Least-Energy Configuration on Conical Surface?* (Science Press, 2009, pp. 541–543), concerns the geometry of packing identical units and phyllotactic arrangements. The user-approved reselection here addresses a **different, precise mathematical subproblem suggested by that packing/phyllotaxis theme**, not the full elastic-energy or cone-packing conjecture.

## Exact target and eligibility

Adiceam and Tsokanos, *Higher Dimensional Spiral Delone Sets*, arXiv:2010.06428v3 (30 March 2021), §6, pp. 22–23, explicitly ask whether a spiral Delone set in ambient dimension `n>=3` can have asymptotic density. The required points are `s_k=k^(1/n)u_k`, `u_k` on the unit sphere, and the density limit is required for **every bounded Jordan-measurable set**, not only origin-centered balls. The normalization `1/V_n` was verified against both rendered source pages and the exact radial count. Later-source clearance is recorded separately in `STATUS.md`.

**Verdict: SOLVED for this precise existence theorem, in every fixed `n>=2` (hence all `n>=3`). Correctness state: DELIVERY-READY. Evidence label: Certification; novelty/priority remains uncertified.** Sort all nonzero integer lattice vectors `z_k` by Euclidean norm with lexicographic ties and set `s_k=k^(1/n) z_k/|z_k|`. The complete proof gives a vanishing displacement from `V_n^(1/n) Z^n \\ {0}`, uniformly through ties; global separation including finite/cross-prefix pairs; global covering; density `lambda_n(X)/V_n` for every bounded Jordan set; and angular uniform distribution. The classical lattice discrepancy and all bridges are written in `RESULTS.md`. The independent other-vendor referee found the argument correct, with four minor clarifications integrated. No full cone-energy solution, optimal packing claim, or first-in-literature claim is made.

## Contract and file map

- `source/problem.zh.txt`: unmodified book excerpt copied from the earlier cone intake.
- `source/adiceam-tsokanos-v3.pdf`, selected page images and `source/primary-evidence.json`: pinned public primary source and normalization/open-question evidence.
- `STATUS.md`: explicit primary open statement, later citing works, mathematical baseline, and limits of novelty screening.
- `RESULTS.md`: complete argument, precise hypotheses, evidence labels and independent-review dispositions.
- `code/verify.py`, `results/verification.json`: deterministic lattice construction and scientific boundary/negative controls; finite checks are not a Delone proof.
- `review/`: read-only independent referee prompt, untouched result and receipt.
- `review/source-audits.json`: separate forward-citation and classical/prior-construction audits, with access limitations.

## One-command scientific replay

From this directory:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/verify.py
```

Observed: exit 0, **five PASS groups**, and `results/verification.json`. The deterministic 3D sample has 57,776 points; independent exact enumerators and tie/normalization/negative controls are included. These finite checks do not prove the universal statement or supply global separation/covering constants—the written proof does.


Old optics and cone certificates are preserved unchanged. No campaign, registry, git, external-contact or paid-run actions belong to this target.
