# Exact original-vs-marginal privacy gaps at epsilon=ln 2

**AUTHOR CANDIDATE — WRITTEN plus exact rational checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:06:41 PDT 2026`.

## Scope and named imports

At epsilon=ln 2, let V_J,V_L be the actual full-D 2D all-law minima of J=E|X|^2 and L=E||X||_1. Let V_1,J,V_1,L be the corresponding actual 1D all-shift private minima. Condition on the unreviewed original-target and source certificate `frontier-20261028-ln2-original-target-certificate-v1.md`, SHA-256 `50bfec41598fc25005f9630694f374571e92e2afc0788c5f37eed86154b1d5e4`, with its named parent v253/v241/MDA inputs, AND on the unreviewed exact 1D theorem `frontier-20261028-exact-scalar-marginal-relaxation-v1.md`, SHA-256 `cde9bcc08bd4f87e635f1a2566fb2eaae6f1b289df5ebd4d36707229c8fc60ed`.

The written and exact-Fraction-checked target values are

    V_J-2V_1,J in (7221939429934783761/50000000000000000000,
                    7221939429934783767/50000000000000000000),           (1)
    V_L-2V_1,L in (624500259708001251/12500000000000000000,
                    249800103883200501/5000000000000000000).             (2)

Their decimals are approximately 0.1444387885986956753 and 0.0499600207766401001. These are gaps from the exact separate-marginal lower bounds, not source-target cost-selector gaps and not assertions of novelty. In particular (1) proves a much stronger conditional instance bound than the general conditional tiny gap in the unreviewed 30d candidate.

## Exact ingredients and arithmetic

At m=1, cde9 gives `2V_1,J=4+2*3^(2/3)` and `2V_1,L=2sqrt(2)`. The 50bf exact target certificate supplies

    83046064347025039043/10^19 < V_J < 83046064347025039044/10^19.     (3)

Its exact L-selector root bracket, combined with the positive-coefficient outward evaluation of its L rational function, gives

    28783871455228301977/10^19 < V_L < 28783871455228301978/10^19.     (4)

Exact integer cubing and squaring give

    208008382305190411453/10^20 < 3^(2/3)
      < 208008382305190411454/10^20,
    141421356237309504880/10^20 < sqrt(2)
      < 141421356237309504881/10^20.                                     (5)

Subtract the UPPER endpoint in (5), multiplied by 2, from the LOWER endpoint of (3) or (4); subtract the LOWER algebraic endpoint from the UPPER target endpoint. Direct fraction arithmetic gives exactly (1)–(2). In particular the two gaps exceed 7/50 and 1/25, respectively.

## Actual checks and limits

The Python eval kernel used `fractions.Fraction` to check the cubed/squared inequalities in (5), the outward L rational-function evaluations, and all endpoint subtractions. Decimal strings above are renderings of those exact endpoints. The computations do not verify either imported optimizer theorem, formalize the probability model, establish novelty or constitute an independent review. No parent adoption of this candidate is claimed.
