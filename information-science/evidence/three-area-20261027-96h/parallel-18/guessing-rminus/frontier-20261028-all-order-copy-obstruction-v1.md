# R-minus: exact all-order copy-family obstruction for the source-certificate core

## Result and exact boundary

There is an explicit rational point at objective **`1847/276`** satisfying:

1. the **1920 individual rows appearing in the published Gürpınar certificate**, with their stated row directions;
2. all original ten-variable elemental Shannon inequalities, all ten R-minus functional-dependence equalities, all ten singleton caps and original-variable symmetry under the two verified graph generators;
3. **every** conditioned inequality in the copy family `F_n` below, for **every positive integer n** and every choice of pairwise disjoint original-vertex blocks `A,B,C,D,Z`, including empty blocks.

Consequently, even adding this entire specified family to that **1920-row certificate-core relaxation** cannot lower its optimum below `1847/276`: the published rational dual proves the upper bound on the core, and the explicit feasible rational point attains it. This is an exact statement about that relaxation, not an entropic law or an original guessing-number lower bound.

**Important limitation:** the 1920 certificate rows are only a subset of the full published copy LP. The particular saved point actually violates other required full-copy equalities and auxiliary Shannon inequalities. It is therefore **not** a feasible point of the full source LP; no conclusion about adding `F_n` to that stronger LP follows. It also says nothing about overlapping block substitutions, arbitrary functions, different valid information inequalities, other copy extensions, or the true guessing number.

## 1. Universal family, including conditioning

For finite random variables `A,B,C,D,Z`, put

```
a     = I(A;B | C,Z),
Delta = I(A;B | Z) - I(A;B | D,Z) - I(C;D | Z),
d     = I(A;C | B,Z) + I(B;C | A,Z).
```

For every integer `n>=1`, define

```
F_n = (n+1)a - n Delta + n(n+1)d/2.
```

Then **`F_n >= 0` for every finite joint law**. The form permits A–D to be arbitrary tuples; the finite obstruction below is narrower because it scans disjoint original-vertex blocks only.

A self-contained proof uses ordinary entropy chain rules and conditional nonnegativity. It suffices to prove the formula for fixed `Z=z` and average; suppress Z below. Attach `R_1,...,R_(n+1)` independently from the conditional distribution of C given `(A,B)`, independently of `(C,D)` given `(A,B)`. Let `S_j=(R_1,...,R_j)`, `h=H(C|A,B)`, and for `0<=j<=n` set

```
a_j = I(A;B | S_j),
B_j = H(R_(j+1) | S_j) - h,
d_j = H(R_(j+1) | A,S_j) + H(R_(j+1) | B,S_j) - 2h.
```

Each `B_j,d_j` is a sum of nonnegative conditional mutual informations, `a_1=a` and `d_0=d`. Entropy chain rules and the conditional-copy construction give

```
a_(j+1) = a_j - B_j + d_j,
d-d_j = I(R_(j+1);S_j|A) + I(R_(j+1);S_j|B) >= 0,
I(S_k;A,B|C) = sum_(j=1)^k B_j.
```

The last identity uses exchangeability of `C,R_1,...,R_(k+1)` conditional on `(A,B)`. Define

```
E_k = a_k + I(S_k;A,B|C) - Delta.
```

Expanding chain rules and using both conditional independences `I(S_k;D|A,B)=0` and `I(S_k;D|A,B,C)=0` yields

```
E_k = I(A;B|S_k,D) + I(S_k;D|A) + I(S_k;D|B)
      + I(C;D|S_k) + I(S_k;A,B|C,D) >= 0.
```

Telescoping the displayed recurrence gives `E_k=a_1+sum_(j=1)^(k-1)d_j+B_k-Delta`. Summing over k and substituting `a_(n+1)` gives the exact nonnegative decomposition

```
F_n = sum_(k=1)^n E_k + a_(n+1)
      + sum_(j=1)^n (n-j+1)(d-d_j) >= 0.
```

This is a mathematical derivation, not an assumption from the numerical LP. No claim of novelty for this classical copy-family form is made.

## 2. Why checking only the first four orders misses a real cut

The first frozen exact sparse-core point has 2558 rational coordinates, satisfies **15374** source/original/prior-cut rows and has objective `1847/276`. At the disjoint original-variable substitution

```
A={2}, B={10}, C={6}, D={3,4}, Z={1,5,8,9},
```

its exact scaled values are `a=11/276`, `Delta=1/23`, `d=0`. Thus

```
F_n = (11-n)/276,
F_12 = -1/276.
```

So this exact relaxation point passes `F_1,...,F_11` for that substitution but violates `F_n` for every `n>=12`. This is not an FD-law counterexample to `F_n`: the point is not asserted entropic. `frontier-20261028-f12-separating-point-check.py` (SHA256 `a037625709913080a6dda6f4e6fe1baa442b30e55ea9b5f59bc7015578dff55c`) independently rechecked every saved row and this `F_12` arithmetic; receipt SHA256 `d1cada8bcb620dda024cb047aba7f5a167862c6908b4ad65e82c04359b1268b3`.

## 3. A different point survives ALL disjoint-block orders

After adding six valid higher-order rows on the above substitution, a second exact sparse-core point was frozen as `frontier-20261028-all-order-primal-frozen.json`, SHA256 `af431478fdad330f5f79fa416bdcaf1c56a56fb30ed4855fc65b50d1cac50545`. Its **2558** rational coordinates are all listed in that file; its original-variable entropy coordinates share integer denominator **25944**. The exact original full-set entropy is `1847/276`.

The independent checker `frontier-20261028-all-order-primal-independent.py`, SHA256 `d4268fd6db3b4573462f04b19253b345d94e81295405a7acf7d1e3f68976210a`, imports neither the producing primal scanner nor the producing LP solver. It rechecks exactly the 1920 certificate-core rows, 10 original conditional entropies, **11520** original elemental CMIs, 10 FDs, 2046 generator symmetry equalities, nonnegativity of every stored coordinate and singleton caps. Receipt `frontier-20261028-all-order-primal-independent-result.json` has SHA256 `44d4de7f20a5045928d11f1a476909cf86f3353ecc1e1b3ccbf8ffc7d999e4e5`.

For each disjoint original-variable substitution write `c=a-Delta`. Then

```
F_n = a + n c + n(n+1)d/2.
```

The checker tests all **13,729,980** nonempty `A,B,C,D` substitutions modulo the symmetry `A<->B`, with `Z` any disjoint subset. This count is independently confirmed by inclusion–exclusion:

```
[6^10 - 4*5^10 + 6*4^10 - 4*3^10 + 2^10] / 2 = 13,729,980.
```

All comparisons use integer entropy numerators at scale 25944. For `d=0`, if `c<0` the inequality eventually fails; otherwise its minimum is at `n=1`. For `d>0`, the quadratic on real n has vertex `-(2c+d)/(2d)`; checking the two adjacent integers, clipped to `n>=1`, suffices for **all** positive integer n. The second checker uses this quadratic-vertex method and a different base-6 enumeration split from the producer’s first-difference scan. It found no negative value; the smallest twice-scaled slack is 0. The largest adjacent candidate n encountered was 23, but the quadratic argument covers every n, not just `n<=23`. Two in-memory cap/objective mutations produced their intended rejections.

Empty original blocks cannot add a missing restriction: if A or B is empty, `F_n` is a sum of nonnegative CMIs; if C is empty, it is `I(A;B|Z)+n I(A;B|D,Z)`; if D is empty, `Delta=0`. These follow directly from the original Shannon rows. Thus the stated disjoint-block result includes empty A–D as well.

The two independent implementations share the published PDF text extraction and common mathematical definitions, were written in the same harness, and are **not** cross-model/human/formal independent review. The source core’s exact 1920-row upper identity was separately checked in `frontier-20261028-gurpinar-certificate-audit-v1.md`, SHA256 `d0b494122660394b46d8ce647ed17e2f890c1f3ccf393cd4e44ccc48e87dcaf6`.

## 4. Explicit failure of full-source feasibility

The saved point's original-coordinate family test does **not** make it feasible for the full source copy model. A separate exact scan `frontier-20261028-all-order-full-source-gap.py`, SHA256 `efc41564e6db8d9cad7b95767e4ed19aba7f11f317015d14f2a98c98e64b4eb1`, receipt SHA256 `f73582a5a6fa8e99a8b6de7a75c70431aafe05e6661c0f473068e6c51d37e394`, checks only rows whose entropy coordinates are actually stored; unknown coordinates are never filled with zero.

A particularly direct failed full-source equality is

```
H(d) - H(d'1) = 1,
```

where `d'1` is the publisher’s copy of original `d`; the copy condition requires this difference to be zero. The same scan found respectively 28, 301 and 384 negative elemental Shannon rows among 11802, 12997 and 14522 evaluable rows of the three source branches; it found 15 nonzero among 493 evaluable full-copy equality forms. The remaining source-branch rows/forms were not evaluable from the stored sparse coordinate set. These are exact **violations by this chosen point**, not violations of Shannon/copy theorems.

Therefore this point cannot simply be promoted into a full-source-LP feasible witness. It remains possible that its original-variable projection has another valid auxiliary extension, or that full-copy constraints plus `F_n` produce a strictly better bound. Both are unestablished; additional source-copy Shannon/copy constraints and different inequality families remain live directions.

## 5. Reproducibility and scope

The source-core primal freeze program has SHA256 `169ef09c93e87305710001216a1ef4d3d122daaad162eaf15adbfcd77f608fd6`; the prior exact refinement program has SHA256 `13393bd03fccd66cd3167ce9ecf031bbef2ec43599421175dd0cf7f8fdc038f7`, with result SHA256 `92f5b31ac81956960d9d34e3c72acfa9acdcba8a54487eab603ec83fab910ba1`. LP solving merely proposed the rational points; all stated feasibility/objective/slack conclusions above come from subsequent exact integer/rational checks. The last independent family-check receipt was observed at **Wed Oct 28 17:30:09 PDT 2026**; the full-source gap receipt at **17:30:52 PDT**.

No new original upper or lower bound, entropic realization, general impossibility, source-priority or formal proof is claimed. Review the explicit source graph/copy transcription and full exact finite witness before adopting this relaxation obstruction.

**END.**
