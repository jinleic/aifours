# Thirty independently replayed anisotropic septic boxes

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** A bounded exact search found a common strict positive-real numerator for each of 30 separately generated seven-dimensional oscillatory-centered anisotropic coefficient boxes. The 30 cases are examples, not an exhaustive class or a probability statement, and they do not resolve the original arbitrary-box decision.

Each numerator was shortened to rational coefficients with denominator 10 or 100 and then replayed from scratch. The independent exact checker for cases 1–29 verified, for every box:

1. Positive widths and positive numerator coefficients, with leading numerator coefficient exactly one.
2. All 28 leading Hurwitz determinants across its four actual Kharitonov parity corners.
3. Strict positivity of each compactified corner pairing on a full dyadic Bernstein partition of \([0,1]\), including \(t=0\) and \(t=\infty\).

That replay checked **812 strict Hurwitz minors** and **15,432 strict Bernstein coefficients** for cases 1–29. Case 0 has a separate independent replay with 28 minors and 544 coefficients, giving totals of **840** and **15,976** across all 30 boxes. The classical Kharitonov theorem and affine corner minimization extend each individual finite proof to every polynomial and every real frequency in that box. Each box's separate exact numerator, endpoints, dyadic leaves, margin and pinned source are in the frozen data; the same numerator also works for its subboxes.

The search selected two exact frequencies inside every even and odd root band using rational Sturm isolation. Its initial strict-certificate LPs were UNSAT on those finite grids, a statement that by itself has no all-frequency implication. Earlier positive exchanges with unscaled variables timed out or returned unknown. The successful replacement used positive coordinate/row scaling, one-sided exact rational integer rounding, an exact simplex, direct checking on the original rows, and adaptive exact negative-frequency exchange. Final claims rely solely on the independent all-frequency replays, not the rounded LP or finite-grid UNSAT results.

Frozen cases 1–29, their separate rational numerators and leaves: `frontier-20261028-sturm-band-batch-simple-frozen-v1.json`, SHA-256 `87827043af153b0ecd5d2ac002bb1095ccd67cb9661c3076f4578e335464b509`. Independent checker `frontier-20261028-sturm-band-batch-independent-kernel-v1.py`, SHA-256 `4c443d559cca788a06d3a232a3e9bfed09f9a1bf1a260e5841f1a75b5ef66242`; result `frontier-20261028-sturm-band-batch-independent-result-v1.json`, SHA-256 `6e5b7289eeb9c8f32800e9acb8f8530847e8ea1ce6a4c74b43ef7d0b37659987`. Case 0's endpoints, explicit numerator and its separate checker are in `frontier-20261028-sturm-band-anisotropic-box-synthesis-v1.md`, SHA-256 `a7ad2c77a2f155ef1b82e9d7e3eee73058a303547d0e9b7f600771f16b99f80f`.

All finite computations used integers and `fractions.Fraction` on one Python Eval host. No formal proof, cross-vendor review, novelty clearance, universal positive conclusion, or all-numerator negative certificate is claimed.
