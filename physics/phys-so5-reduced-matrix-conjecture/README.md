# SO(5) reduced matrix elements: the CRW conjecture

Date: 2026-10-14 (America/Los_Angeles).

**Selection verdict: ALREADY-SOLVED in equivalent pre-2009 literature.** Evidence class: **Certification / Reproduction**. Frontier state: **HEADROOM-ABSENT** for a new open-problem claim. The full convention-matched theorem is proved here, but the independent review identified its equivalent class-one SO(n) closed form in prior literature. **Do not count this folder as a newly solved scientific open problem.**

Bao Chengguang's entry “母配分系数递推关系的破解” in *10000个科学难题·物理学卷* (2009), pp. 348–349, asks for analytic fractional-parentage coefficients beyond spin-1 bosons. This folder addresses a related SO(5) representation-theory subproblem used in spin-2/d-boson calculations: the common SO(5)-reduced matrix element of multiplication by a normalized spherical harmonic on S4. It does **not** solve the complete book problem, all missing-label coupling coefficients, or arbitrary general-spin CFP recurrences.

## Exact target and result

For **every** nonnegative integer triple `(v1, v2, v3)`, prove Caprio–Rowe–Welsh, *Computer Physics Communications* 180 (2009), 1150–1163, [arXiv:0902.0020](https://arxiv.org/abs/0902.0020), **§2.5 Eq. (29)**, with their measure mass `16*pi^2/3` and positive reduced-element phase. The value is zero for odd sum or violated triangle inequalities. The formula and complete all-integer proof are `RESULTS.md`, Theorem 1 and §§1–5.

CRW explicitly state on PDF p. 8:

> “However, we stress that is has not been proved in full generality.”

Welsh–Rowe (2016), [arXiv:1408.3824v3](https://arxiv.org/abs/1408.3824v3), §IV Eq. (45), and Rowe–Wood (2010), §4.5.4 p.199 Eq. (4.175), still label it empirical. Nevertheless, **Ališauskas [math-ph/0509035v1](https://arxiv.org/abs/math-ph/0509035v1), PDF Eq. (26a), already contains the same invariant in class-one SO(n) notation**, attributed there to Junker (1993). `RESULTS.md` §4A proves the exact dictionary \(R^2=d_{v_1}d_{v_2}G_5^2/V\). This stronger backward prior art defeats new-open-problem eligibility, despite the genuine historical conjecture wording. The convention-matched addition-theorem/Rogers proof remains a useful certification.

## Reproduction

From the repository root:

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python -B physics/phys-so5-reduced-matrix-conjecture/code/verify.py
```

Observed base checks: symbolic ratios `1,1`; **2,197** exact univariate triples (616 admissible, 1,581 forbidden); Cartesian harmonic dimensions **1,5,14,30**, **20** degree multisets reused for **64** ordered triples, and **58,840** triple overlaps; `pi^2*R(2;2,2)^2 = 7/8`. The raw integrals/traces are independently calculated, but both receive the analytic measure/trace prefactors; they do not independently verify the universal convention bridge. Five rescaling/forbidden-value inequalities are only **arithmetic illustrations**, not a mutation certificate. The same command also runs `prior_art_identity.py`, checking the exact equivalent-literature dictionary and a direct stretched-state normalization calibration. No floating-point tolerance is used; finite checks are not the universal proof.

Finalized prior-art replay also passed: symbolic ratio `1`, **125** SO(3) Wigner controls, **2,197** SO(5)-CRW dictionary comparisons, `G_5(2,2,2)^2 = 1/42`, and the direct stretched-state value `pi^2*R(2;1,1)^2 = 15/56`. Both independent reviews and their dispositions are in `RESULTS.md` §9.

## File map

- `source/problem.zh.txt`: unchanged supplied book excerpt.
- `STATUS.md`: primary eligibility quotes, SOTA, classical baseline, forward-screen depth, and priority limitations.
- `RESULTS.md`: full proof, conventions, boundary cases, observed commands, and review dispositions.
- `code/crw_formula.py`: exact rational `pi^2*R^2` implementation of the published formula.
- `code/verify.py`: symbolic cancellation, direct Legendre-derivative integral, boundaries, arithmetic illustrations, receipts, and the full one-command replay.
- `code/cartesian_oracle.py`: independent rational five-variable harmonic construction and triple trace, degrees 0–3.
- `code/prior_art_identity.py`: literal Ališauskas Eq. (26a) specialization, SO(3) Wigner control, SO(5)-CRW dictionary, and a direct fixed-L normalization calibration.
- `results/prior-art-identity.json`: exact equivalent-prior-art replay receipt.
- `results/exact-checks.json`: observed exact-arithmetic receipt and 64 Cartesian values.
- `results/source-sha256.json`: preserved-source hashes.
- `source/`: primary PDFs/text, original CRW/open-statement and equivalent-prior-art images, public Rowe–Wood pp.197–199 preview images, exact Rogers formula, and the dated OpenAlex inventory.
- `review/`: completed Claude Opus 5.5 mathematical review (MINOR-REVISION; no mathematical defect) and Codex gpt-6.1-sol convention/evidence review (ACCEPT), raw outputs, 19 pinned and preserved input files, and dispositions. See `RESULTS.md` §9 for the launcher postprocessing failure, recovered evidence, and every correction.

## Remaining boundary

The written proof uses classical invariant theory, spherical-harmonic/measure facts, and Rogers linearization; no Lean/kernel or human-peer-review certification is claimed. The exact mathematical content is already known in equivalent form, so remaining bibliographic gaps cannot justify a new-discovery claim. The parent accepted this candidate's rejection and owns selection of a different genuinely open target. The broad CFP problem and its missing-label obstructions remain unsolved by this folder.
