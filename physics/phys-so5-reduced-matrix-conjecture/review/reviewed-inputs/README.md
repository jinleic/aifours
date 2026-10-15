# SO(5) reduced matrix elements: the CRW conjecture

Date: 2026-10-14 (America/Los_Angeles).

**Verdict: SOLVED for the precise statement below.** Evidence class: **Certification**. Frontier state: **NOVELTY-UNCLEAR**. This is a proof of a historically explicit conjecture using classical ingredients; worldwide proof priority and publication novelty are not established.

Bao Chengguang's entry “母配分系数递推关系的破解” in *10000个科学难题·物理学卷* (2009), pp. 348–349, asks for analytic fractional-parentage coefficients beyond spin-1 bosons. This folder addresses a related SO(5) representation-theory subproblem used in spin-2/d-boson calculations: the common SO(5)-reduced matrix element of multiplication by a normalized spherical harmonic on S4. It does **not** solve the complete book problem, all missing-label coupling coefficients, or arbitrary general-spin CFP recurrences.

## Exact target and result

For **every** nonnegative integer triple `(v1, v2, v3)`, prove Caprio–Rowe–Welsh, *Computer Physics Communications* 180 (2009), 1150–1163, [arXiv:0902.0020](https://arxiv.org/abs/0902.0020), **§2.5 Eq. (29)**, with their measure mass `16*pi^2/3` and positive reduced-element phase. The value is zero for odd sum or violated triangle inequalities. The formula and complete all-integer proof are `RESULTS.md`, Theorem 1 and §§1–5.

CRW explicitly state on PDF p. 8:

> “However, we stress that is has not been proved in full generality.”

Welsh–Rowe (2016), [arXiv:1408.3824v3](https://arxiv.org/abs/1408.3824v3), §IV Eq. (45), still present it as empirical. The bounded forward-citation screen and inaccessible sources are detailed in `STATUS.md`; they do not establish current worldwide unsolved status. The proof identifies the CRW normalization sum with a triple-harmonic trace, applies the normalized addition theorem, and evaluates the remaining integral by classical Rogers linearization. The integral itself is prior art.

## Reproduction

From the workspace root:

```sh
scratch/ai4s-venv/bin/python ai4s/phys-so5-reduced-matrix-conjecture/code/verify.py
```

Observed result: symbolic ratios `1,1`; **2,197** exact univariate triples (616 admissible, 1,581 forbidden); independent Cartesian harmonic dimensions **1,5,14,30**, **64** ordered degree triples and **58,840** triple overlaps; **5/5** negative controls detected; `pi^2*R(2;2,2)^2 = 7/8`. No floating-point tolerance is used. Finite calculations control the derivation and implementation; they are not the universal proof.

## File map

- `source/problem.zh.txt`: unchanged supplied book excerpt.
- `STATUS.md`: primary eligibility quotes, SOTA, classical baseline, forward-screen depth, and priority limitations.
- `RESULTS.md`: full proof, conventions, boundary cases, observed commands, and review dispositions.
- `code/crw_formula.py`: exact rational `pi^2*R^2` implementation of the published formula.
- `code/verify.py`: symbolic cancellation, independent Legendre-derivative integral, boundary and negative controls, and receipt generation.
- `code/cartesian_oracle.py`: independent rational five-variable harmonic construction and triple trace, degrees 0–3.
- `results/exact-checks.json`: observed exact-arithmetic receipt and 64 Cartesian values.
- `results/source-sha256.json`: preserved-source hashes.
- `source/`: primary PDFs/text, original Eq. (29)/open-statement images, exact Rogers formula, and the dated OpenAlex citing-record inventory.
- `review/`: read-only independent referee prompts, pinned snapshot, raw responses, and run receipts.

## Remaining boundary

There is no remaining mathematical gap in the stated proof conditional on the cited classical linearization theorem. The remaining **novelty/eligibility** uncertainty is whether inaccessible or convention-equivalent prior literature already supplies the same proof. The most valuable next action is to inspect the Rowe–Wood book and Rowe–Welsh–Caprio PRC paper, then obtain a human domain referee's priority assessment. This folder is not evidence of a new general CFP solution.
