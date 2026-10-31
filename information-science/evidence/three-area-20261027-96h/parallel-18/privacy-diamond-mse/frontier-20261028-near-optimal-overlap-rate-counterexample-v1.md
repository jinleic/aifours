# Near-optimal mean/Euclidean laws can overlap much more than exact optimizers

**AUTHOR CANDIDATE — WRITTEN with exact rational power checks; NOT independently reviewed or parent-adopted.** Native pre-write clock: `Wed Oct 28 18:55:57 PDT 2026`.

## 1. The precise false extrapolation

For b=e^(-epsilon)->0, my earlier still-UNREVIEWED `frontier-20261028-mean-versus-squared-tv-asymptotics-v1.md`, SHA `7307a4883179087691cb5265ece87a7ae0ddee906be88839b2ef4a6e439920da`, gives order `b^(1/6)` overlap for SPECIFIC exact centered first-norm and squared-cost optimal laws, conditional on its named optimizer/core inputs. My source-independent first-order peak-floor candidates show that ANY first-order-near-optimal mean and Euclidean laws have TV->1.

It would be FALSE to combine those statements into a uniform `1-TV=O(b^(1/6))` rate over arbitrary first-order-near-optimal laws. This note constructs actual full-Borel/full-CLOSED-D, EXACT-epsilon feasible laws P_b,Q_b such that P_b is first-order-near-optimal for E||X||_1, Q_b is first-order-near-optimal for E||X||_2^2, but

    1-TV(P_b,Q_b) >= b^(1/8),
    b^(-1/6)[1-TV(P_b,Q_b)] -> infinity.                                 (1)

Yet both weakly approach delta_0 and, by the two source-independent scaling results if reviewed, their TV distance still tends to 1. There is no contradiction: that convergence need not have the exact-optimizer overlap rate.

The laws are explicit mixtures of actual geometric-shell densities, not finite grids, approximate DP or arbitrary cost vectors. This is a counterexample to an overstrong RATE, not to either earlier theorem or to the PMLR first-norm theorem.

## 2. Exact parent-independent inputs and two actual laws

The ONLY research inputs needed to call the laws first-order-near-optimal are my own still-UNREVIEWED, source-independent peak-floor candidates:

- first-norm `frontier-20261028-peak-floor-first-norm-universal-v1.md`, SHA `fa39d7bdc125da7c8f7424d5976309227d8101a58b15efea919e8eb8376f04ea`, proving `L_*=2^(1/3)b^(1/3)+O(b^(2/3))` and the matching explicit law;
- squared-Euclidean `frontier-20261028-peak-floor-low-privacy-universal-v1.md`, SHA `d44029e458b8af871d2d849e2a5159e1885e99402d615a88eabe39d89ab4ad43`, proving `V=[2/sqrt(3pi)]sqrt(b)+O(b^(3/4))` and its matching explicit law.

These are AUTHOR candidates and not automatically reviewed/adopted. The mixture privacy, cost inequalities and TV counterexample below are derived directly; no LAW642, v241, MDA, source match or optimizer-uniqueness premise is used.

Let `L_b` be the actual shell law with centered diamond core radius `q_b=2^(1/3)b^(1/3)`. Let `E_b` be the actual shell law with centered Euclidean disk core radius `R_b=(4/(3pi))^(1/4)b^(1/4)`. In both cases the density is proportional to `b^(min{k:x in S+kD})`, so the index changes by at most 1 for EVERY closed-D shift. Thus both are actual original fully private laws.

Their directly calculated costs are

    E_Lb ||X||_1 = 2^(1/3)b^(1/3)+O(b^(2/3)),
    E_Eb ||X||_2^2 = [2/sqrt(3pi)]b^(1/2)+O(b^(3/4)).                 (2)

Cauchy–Schwarz and `||x||_1^2<=2||x||_2^2` give `E_Eb||X||_1=O(b^(1/4))`.

## 3. Explicit near-optimal mixture and the lower overlap

Set `w_b=b^(1/8)` and define

    P_b=(1-w_b)L_b+w_b E_b,       Q_b=E_b.                                (3)

Convexity of the event inequality gives P_b in the SAME full-D privacy class; Q_b is already feasible. For both compact centered cores, sufficiently far in the positive quadrant the shell index is `ceil(x1+x2-c)` with its own constant c. The SAME shift e1 raises both indices by one, so their mixture drops by factor b on a common far-quadrant open rectangle. Thus BOTH laws have actual exact epsilon privacy, not merely an upper bound.

By linearity, (2), and `w_b E_Eb||X||_1=O(b^(3/8))=o(b^(1/3))`,

    E_Pb||X||_1 <= 2^(1/3)b^(1/3)+o(b^(1/3)).

The named independent first-moment lower theorem makes P_b first-order near-optimal. Q_b is first-order near-optimal for the ORIGINAL squared-Euclidean cost by (2) and its independent lower theorem.

For ANY probability laws L,E and w in [0,1],

    TV((1-w)L+wE,E)=(1-w)TV(L,E)<=1-w.

The identity is the homogeneity of the signed measure difference. Substituting (3) gives `1-TV(P_b,Q_b)>=w_b=b^(1/8)`. Since `b^(1/8)/b^(1/6)=b^(-1/24)->infinity`, (1) follows. No estimate of the exact optimizer law or of TV(L_b,E_b) is needed.

## 4. Even slower overlap compatible with first-order near-optimality

For b<e^(-1), alternatively choose

    w_b=b^(1/12)/log(1/b).

It is positive and tends to zero; `w_b E_Eb||X||_1=O(b^(1/3)/log(1/b))=o(b^(1/3))`, so the same P_b remains first-order-near-optimal and fully private. Yet

    1-TV(P_b,Q_b)>=b^(1/12)/log(1/b),

which dominates b^(1/12+delta) for every fixed delta>0. This construction does NOT claim that 1/12 is a sharp universal exponent or that an arbitrary near-optimal pair has this lower overlap. It only disproves carrying the exact-optimizer 1/6 rate over to the full near-optimal class.

Because w_b->0, both explicit laws still tend weakly to delta_0: Q_b does by its previously derived scaled TV limit, L_b by its first-norm scaled limit, and mixtures preserve weak convergence. If BOTH named peak-floor candidates survive review, their all-near-optimal cross-scale argument separately gives `TV(P_b,Q_b)->1`; the present lower bounds specify how slowly its overlap can vanish.

## 5. Exact bounded power checks

A Fraction-only cell evaluated the power relationships for selected b=2^(-k), with k divisible by 24:

```text
b=2^- 24 weight= 1/8 relative_mean_contamination= 1/2 overlap_vs_b^(1/6)= 2
b=2^- 48 weight= 1/64 relative_mean_contamination= 1/4 overlap_vs_b^(1/6)= 4
b=2^- 96 weight= 1/4096 relative_mean_contamination= 1/16 overlap_vs_b^(1/6)= 16
```

The sampled `relative_mean_contamination` is the EXACT ratio `w_b b^(1/4)/b^(1/3)` of scaling factors; it is not a numerical evaluation of E_Eb||X||_1. The strict asymptotic proof is §3.

## 6. Review boundary

The full-event/exact-budget caller, mixture identity and rate obstruction are written without source attribution. The **near-optimal** labels depend on the two explicitly UNREVIEWED source-independent peak-floor bounds and their actual upper-law formulas; no parent/independent-model/human/formal/kernel or novelty acceptance is claimed. Request disjoint review of those bounds, the same-event exact-epsilon argument and the cross-objective quantifiers. Historical held outcomes are nonpremises.
