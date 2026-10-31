# Two exact obstructions to a naive level-six global positivity shortcut

**MathKacMoody-2 / math-3.** Native clock before this additive write: **Wed Oct 28 18:51:23 PDT 2026**. WRITTEN-checked-in-kernel on the exact new free-Levi source data; unreviewed and not a formal/human/external-model verdict. This result is a NEGATIVE result about one proposed proof device, NOT a non-Serre witness.

## Exact statement

For the full level-six `(2,2,6)` lowest source, use the 34 rational vectors and the **entire 235-row unweighted tensor-word target coordinate set** reconstructed by `frontier-20261028-level6-free-22-pencil-v1.json`, SHA `b3779b89c8a5e67bb0478ac31dae9c96cd2c32f912f8f8c63baa4e8227c6e5bc`. Denote the actual full-target pencil by

\[
D=A+xB+yC,\qquad x=r-6,\quad y=s-6,
\]

where A,B,C have real rational entries. A natural sufficient route to all-orthant injectivity would be to show the two unweighted Euclidean symmetric slope forms

\[
H_x=A^TB+B^TA,\qquad H_y=A^TC+C^TA
\]

are both positive semidefinite: then the real part of `(Av)^*D v` would be strictly positive for nonzero v because A has full column rank. **That particular route fails**: both 34×34 symmetric forms are INDEFINITE.

For each form, the FIRST standard source-basis vector gives the same positive quadratic value `32578`. Two explicitly given different rational vectors in the pinned witness JSON give respectively

\[
v_x^T H_x v_x=-348002061658205738495568873096495816418227091760133404797613539714182002831/7422757863554950116395051224950968117487269402309263239264604492618999<0,
\]
\[
v_y^T H_y v_y=-331785005763535449582655134433463570674669615511783796409643421384022467860/29330795633882012696693297881048881657822942097901423365777768331436799<0.
\]

All 34 coordinates of both v vectors are explicitly stored. A separate exact replay recomputes both positive and both negative values from the actual 235-row pencil; all arithmetic is Fraction/integer.

## Scope and nonclaims

This excludes ONLY the asserted positivity of these two PARTICULAR full-target forms under the unweighted standard tensor-word inner product and the given source normalization. A different positive target weighting, a different left certificate, an alternative combination of minors or a different global argument is NOT excluded. A negative quadratic direction is not a zero of the full D3 map, a counterexample at any integer parameter, a negative norm in the original nonsymmetrizable algebra, or a non-Serre element. It does not weaken the independently replayed `|r-s|<=41` strip candidate or the separate row-product cone; both remain under full review at their named inputs.

## Evidence

`frontier-20261028-level6-226-naive-accretivity-obstruction.py`, 48LF SHA `cbb3585d595fb0207c6af1cf28580b9378215bc9af05134393d666e15cebc66e`, produced the two rational negative vectors in `frontier-20261028-level6-226-naive-accretivity-obstruction-v1.json`, 95LF SHA `0c472e2f56e2fd5bc7305b351f96aa5c1982c36380ed35e2128471497e956520`; actual return **18:50:52 PDT**. The initial program checked the two negative values but its status word INDEFINITE did not by itself certify positive directions. The mandatory NEW replay `frontier-20261028-level6-226-accretivity-indefinite-replay.py`, 33LF SHA `d32bb0b11ddb9e028367bc89e65f0aefa3895f7dc7ade17b1efbe880b5f568b8`, independently recomputed BOTH `+32578` first-coordinate values and both exact negative values; its 28LF output `frontier-20261028-level6-226-accretivity-indefinite-replay-v1.json` SHA `53bb5f0d51368913801520af9db718d9ee315cbb74c86df553459ae6a962571a` returned PASS by **18:51:23 PDT 2026-10-28**. Both use shared current-round source helpers, not independent-model/formal review.

The older cone-status methodological exposure recorded in the level-six candidates remains attached; no held guide is an accepted premise. The original full `(4,4,6)` leading replay remains a distinct pending job.

**END — exact obstruction to one naive positivity route only.**
