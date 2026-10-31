# Addendum 1: gn(R-minus) <= 977/146

**Status: WRITTEN with an exact rational dual certificate, independently checked in kernel.** Additive to `frontier-20261029-upper-bound-10834-1619-v1.md` (SHA-256 `c01ded9d20651d455adf14f50b86b54ac478351153b03ef875cdf7a4fa32f371`), whose validity argument (symmetrized product of eight relabeled copies, then the copy lemma) applies verbatim. No review, formalization or novelty audit has been performed.

## Statement

`gn(R^-) <= 977/146 = 6.6917808219...`, which is `1/236374` below `10834/1619` and `1847/276 - 977/146 = 5/20148` below the publisher bound.

## What changed in the program

1. **Central-point separation.** Vertex optima of the 10834/1619 program are easy to cut without changing the value (300 violated DFZ instances on copy variables and three violated single-copy structures were each added at a crossover vertex; the optimum stayed `6.6917850525`). The program was instead solved by IPM **without** crossover, which returns a point in the relative interior of the optimal face (`frontier-20261029-central-point-v9a.json`, SHA-256 `55860bb86ff8ce55a9826426edfd3c5c81748e00d18adbfba4eb55f646e7d158`).
2. At that central point every conditional DFZ instance on the ten original variables and every one of the 725 orbit representatives of single-copy structures is satisfied (`frontier-20261029-central-cutting-plane-v8-result.json`, SHA-256 `78ae71f7d48b4de1b2ac4e37c9a596649bc35e162722f3352bb46bc1c0129514`); so those families alone cannot lower `10834/1619`.
3. DFZ instances on the **branch-1 variable set** (the ten originals and the copy `b'0`) are violated there: 102 instances (`frontier-20261029-branch-dfz-scan-v9a-b1.json`, SHA-256 `f49f6d7087e4190dced6b30988c1b9c9a771781e33e12a2b63113f278414d331`). DFZ inequalities hold for any random variables, including copy variables, so these rows are valid.
4. The program also keeps three extra single-copy branches found earlier: `X1` copied over `X{2,3,5,6,8,9}`, `X1` over `X{2,3,5,6,8,9,10}`, `X3` over `X{1,2,4,5,6,9,10}` (each: all subset marginal equalities, conditional independence from all originals given the conditioning set, all elemental Shannon rows on the 11 variables).

Re-solving gives the central point `frontier-20261029-central-point-v9b.json` (SHA-256 `bfc4220f854739817e8b1e1dcdf8446ee11db4fec9a5057a1c8312e5a51e7c0e`) with value `6.691780818`.

## Certificate and check

* Producer `frontier-20261029-copy-certificate-producer-v6.py` (SHA-256 `1979976239fc8f4c1dab9bd168bbb6a9426061e69db3177cf7476e400a5365e2`): crossover basic dual, exact flint solve. Certificate `frontier-20261029-certificate-v9b.json`, SHA-256 `b318c80e51a787567e4c156fb57f965e1b128787767ac5d1594bf37538d29cb5`, 1,451 rows: 722 CMIs, 16 monotonicity rows, 10 FDs, 3 caps, 511 symmetry equalities, 122 publisher copy equalities, 5 publisher independence equalities, 57 extra-branch copy equalities, 3 extra-branch independence equalities, one original-variable DFZ instance (item `3 7 2 2 3 0 0 3 2`) and one branch-1 DFZ instance (item `3 5 6 2 3 0 0 3 0`, copy steps `rs ad bc.t a cr.u b acrt.`). Sum of cap multipliers `977/146`.
* The new item was re-derived exactly from its copy steps: `frontier-20261029-dfz-inequality-verify-v9b.json`, SHA-256 `614fda6760c476ff15330dc489dbb463930261808740c708cbcefb1048a574e5`.
* Independent checker `frontier-20261029-dfz-certificate-check-v4.py` (SHA-256 `06b73587d6287929f9d81bfc2218460b2a417ee69d0a0deacb26f9e296b4ce87`) rebuilds every row kind from its description (including extra branches declared in the certificate and branch-local DFZ masks), requires exact re-derivations for both DFZ items, checks signs and the identity, and recomputes `977/146`; three negative controls rejected. Receipt `frontier-20261029-certificate-v9b-check-result.json`, SHA-256 `f85dcf47251d819e929c50318e11be3650ef8511fbfe52b941cdab116343afb5`.

## Limits

Interval now `20/3 <= gn(R^-) <= 977/146`, subject to review. The decrease from `10834/1619` is small; further branch-variable DFZ rounds (branches 2 and 3 are being scanned) may lower it further.
