# Closed parentage coefficients for the deficit-five boson family

Snapshot: 2026-10-14 (America/Los_Angeles).

Bao Chengguang's chapter “Solve the Recurrence Relation of the Fractional Parentage Coefficients,” in *10000 Selected Problems in Sciences: Physics* (Science Press, 2009), pp. 348–349, asks for analytic parentage coefficients that avoid particle-number recursion and thereby make few-body methods useful for larger systems. The full problem spans spins, multiplicities and particle statistics and remains much broader than this work. After the user approved precise scoped subproblems, this target fixes an infinite general-spin family with a two-dimensional missing-label space rather than an isolated numerical instance.

## Approved scoped target and verdict

**SOLVED for the specified reduced family; PARTIAL relative to the book.**

**FRONTIER_METHOD: DELIVERY-READY for the explicit formula/proof; NOVELTY-UNCLEAR.** A literature-search miss does not certify openness or priority. Known near-stretched seniority properties and spin-3 solvable energies are credited in STATUS.md.

For every integer spin `f>=3`, derive every signed **reduced one-body CFP** of seniority-v states with total spin `L=f*v-5`, into **all** seniority-`v-1` daughter blocks. The parent basis is Gram–Schmidt of

1. `z0^(v-3) * C5`,
2. `z0^(v-5) * H2*T3` when `v>=5`,

with the explicit covariants and positive normalization convention in RESULTS.md. All daughter bases are specified too. The stable domain is `v>=6`, with 14 coefficients; exact exceptional tables for `v=3,4,5` contain 3, 5 and 12 coefficients respectively. No parent exists at `v<=2`.

The answer consists of **explicit rational Gram/insertion matrices and fixed two-by-two square-root normalization**, not a recursion, matrix-size growth with v, numerical interpolation, or an unspecified basis choice. Every entry's squared rational function and signed numerator are also exported to `results/closed-form.json`.

This covers the `v -> v-1` branch only. The known quasi-spin factor supplies its all-N dependence. The `v -> v+1` branch, arbitrary deficit and general low-spin missing labels are not claimed solved. No second parentage core was created: the sibling engine is read-only and used for independent checks.

## Reproduction

From this folder:

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-venvs/phys-fractional-parentage-coefficients/bin/python code/deficit_five.py --write
```

Without `--write`, the same checks run without rewriting result files. The existing environment provides Python 3.13.9, SymPy 1.14.0 and python-flint 0.9.0. The shared generic ai4s environment lacks python-flint; no installation or new environment is required. The calculation is single-core and deterministic.

The script checks the complete stable identity over `Q(f,v)`, each low-v identity over `Q(f)`, fixed covariants and Gram/insertion formulas against the sibling deficit implementation, all signed entries over the frozen finite domain `f=3..7, v=3..10` against its occupation-polynomial engine, and a separately normalized first-quantized contraction. These finite controls are not substitutes for the universal written proof.

The independent Codex referee returned **correct-with-fixes**, with no mathematical gap identified. Its single finding concerned an overstated phase-negative-control assertion; the control was changed to explicitly reject the reversed signed coefficient. The complete report and author dispositions are preserved. The final exact replay after this correction passed 450 signed coefficients, 190 daughter blocks, three first-quantized overlaps and the stable/low-v symbolic identities.

## Files

- `source/problem.zh.txt`: unedited source chapter excerpt copied from the original parentage intake.
- `source/prior-art-evidence.json`: primary-source scope anchors, matching source-excerpt hash and shared-core input hashes.
- `STATUS.md`: approved contract, primary-source screen, standard/local baselines and novelty limits.
- `RESULTS.md`: the complete fixed-size formulas, domains, proof, verification and review dispositions.
- `code/deficit_five.py`: closed-matrix evaluation and exact derivation/checks.
- `results/closed-form.json`: full stable and low-v rational entries and signed numerators.
- `results/verification.json`: exercised domains, counts and runtime versions.
- `review/`: self-contained hostile-referee prompt, response and evidence receipt.

## Screening history and next action

The previous cone target is preserved at `../phys-fibonacci-cone-spirals/`. Its approved Fermat-tail density continuation was screened as a known Lagrange-spectrum mechanism and does **not** count as a newly solved open problem. This parentage family was assigned as a replacement; the original parentage worker retains the independent low-total-spin target and its folder.

The remaining scientific prerequisite is a specialist prior-art comparison for this explicit general-f deficit-five table, especially older many-boson CFP sources. Correctness and a completed analytic expression do not establish novelty. Extending the formulas to upward seniority would be a distinct target requiring higher-deficit families, not an unreported completion of this one.
