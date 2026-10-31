# The 1847/276 base point is cut by published DFZ inequalities

**Status: WRITTEN-checked-in-kernel; exact integer evaluation and exact re-derivation of every inequality used.** This packet is about one LP point. It does not by itself give a new upper bound on the guessing number of R-minus; that requires re-optimizing the publisher's LP with the new cuts and an exact dual certificate (in progress, separate packet).

## Objects

* `h*`: the pinned original-variable profile `frontier-20261028-separator-bound-primal.json`, SHA-256 `aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651`. It is an exact optimal base point of the publisher's symmetric three-branch copy LP, with `h(V)=1847/276` and all singletons equal to 1 (`frontier-20261028-full-source-lp-optimum-v1.md`, SHA-256 `08af469a...6fcdd`, read with its pre-source erratum `c64e2a1a...ded9`).
* Dougherty, Freiling and Zeger, *Non-Shannon information inequalities in four random variables*, arXiv:1104.3602. Downloaded source in `frontier-20261029-dfz-source/` (PDF SHA-256 `0e46a1700e59d99a6dafc6340d87ac85f9709ff91d1d539409f060ba39cd52b3`; TeX `src/nonShannon.tex` SHA-256 `ab01cd4113f334715d6e80b538bfcca657d659380504be916de2bd43857e732c`). Their four-copy list (Section "Inequalities Using Four Copy Variables with at most Three Copy Steps") gives inequalities of the form

  `a I(A;B) <= b I(A;B|C)+c I(A;C|B)+d I(B;C|A)+e I(A;B|D)+f I(A;D|B)+g I(B;D|A)+h I(C;D)+i I(C;D|A)`

  together with the copy steps used to prove each one.

## Result

Every listed inequality remains valid after substituting disjoint unions of the ten original variables for `A,B,C,D` and conditioning every term on a further disjoint union `Z` (apply the inequality to each conditional law given `Z=z` and average). The scan `frontier-20261029-dfz-substitution-scan.py` (SHA-256 `b34a33307e927c40ea5fa4423348deca21e062c1a5479c17580cc62b8a03fe00`) evaluates all 240 parsed coefficient tuples on all 27,459,960 role assignments with nonempty `A,B,C,D`, using exact integers after scaling `h*` by 25,944. Receipt `frontier-20261029-dfz-substitution-scan-result.json`, SHA-256 `8ddd9f86c23885dc788f806c0f4ae0e54fea5c04c0e32bbb3327b75e6320e86a`.

Five inequalities are violated. The strongest is the four-copy item `8 17 9 5 8 0 0 8 0` (TeX line 2050, copy steps `rs ad bc.t c abr.u c abrt.`):

`8 I(A;B|Z) <= 17 I(A;B|CZ) + 9 I(A;C|BZ) + 5 I(B;C|AZ) + 8 I(A;B|DZ) + 8 I(C;D|Z)`

with `A=X10, B=X9, C=X7, D=X3, Z=(X1,X4,X5,X6,X8)`. At `h*` the right side minus the left side equals **`-1/23`**. The other four violated items are `3 9 2 2 3 0 0 3 0` (`-5/138`), `3 7 2 2 3 0 0 3 2` (`-2/69`), `2 5 2 1 2 0 0 2 0` (`-7/276`) and `5 10 3 6 5 0 0 5 2` (`-1/276`), all at the same or a closely related role assignment.

## Independent validity check of the cuts

The inequalities are not merely cited. `frontier-20261029-dfz-inequality-verify.py` (SHA-256 `c2db2bad5be6e747b30abce3e9abb46f83b2b49703dc5e976cfa7ca70b44e650`) rebuilds, for each of the five violated items and for Zhang–Yeung, every elemental Shannon inequality on the enlarged variable set, every copy marginal equality and the conditional-independence equality of each listed copy step, and solves exactly over the rationals for multipliers with the required signs. The coefficient identity holds exactly on every joint-entropy coordinate in all six cases; strengthening the first left-hand coefficient by one is rejected. Receipt `frontier-20261029-dfz-inequality-verify-result.json`, SHA-256 `12f6aa96a6ec70ee6622e4d6981d98d3e3d89ff717f061c137d8c1e52699a727`. The only imported fact is the copy lemma (DFZ Lemma, a two-line distribution construction).

## Consequences and limits

* `h*` is not almost-entropic. The publisher LP optimum `1847/276` is attained at a non-entropic point, so the LP bound is not certified tight by `h*`.
* This does not by itself lower the bound: other optimal base points of the publisher LP could satisfy the cuts. The re-optimized LP with all conditional DFZ instances is run separately.
* As a pipeline control, the same cutting-plane code on the Shannon LP alone converges to exactly `59767/8929` with an exact 760-row dual certificate re-checked by an independent checker (`frontier-20261029-dfz-certificate-base-check-result.json`, SHA-256 `408b877a02e5a13a4432e3b14eedc5f7d06cd413981e285a237ceeb30cad2151`), reproducing the published DFZ bound for R-minus.

No proof-assistant formalization, cross-model review or novelty audit was performed.
