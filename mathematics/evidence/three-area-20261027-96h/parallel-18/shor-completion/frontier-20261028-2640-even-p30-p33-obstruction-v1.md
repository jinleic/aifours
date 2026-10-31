# Shor completion: two even-tail head obstructions at order 2640

Owner **MathShor-2**, math-5. Native clock of the exact check: **Wed Oct 28 20:47:23 PDT 2026**.
**WRITTEN necessary-border argument plus exact finite candidate checks; no n2640/all-order no-go, peer/formal/cross-family acceptance or novelty claim.**

## 1. Setup

For any hypothetical finite UD factor-complete extension of the literal Shor code of actual pure-a order2640, the same actual border factors P,Q tile the cyclic group directly, with old heads `A={0,3,8,11}` and old tails `Y={0,1,7,13,14}`. The actual-border theorem and the necessary Sands gcd-difference criterion are classical, independently reconstructed in the earlier packets. P must avoid the old-tail gcd classes `{1,2,6,12}`.

Both branches treated here have EVEN |Q|: P30/Q88 and P33/Q80. In each, P is uniform modulo3 and the old-anchor screen has exactly24 candidates in mod3 class1. They split into disjoint sets T and Z with

    |T|=8:  x mod5 !=3 and x mod11 !=0;
    |Z|=16: x mod5 ==3 and x mod11 ==0.

Every element of Z has a forbidden-gcd blocker set inside T of size2 or4. The eight size2 blocker sets consist of four disjoint pairs of T-elements, each appearing for exactly two elements of Z. The pinned checker verifies these exact structural facts and all gcds.

## 2. Excluding P33/Q80

P is uniform modulo3, so it needs11 heads in class1. It is also uniform modulo11, with3 heads in class0. The old heads0 and11 already occupy two places in that class; hence at most ONE element of Z can be selected. Even using all8 of T gives at most9 heads in mod3 class1, below11. Thus P33 is impossible.

## 3. Excluding P30/Q88

P is uniform modulo3, so it needs10 heads in class1. It is uniform modulo5, with6 heads in class3; the old heads3 and8 already occupy two positions, so at most FOUR elements of Z can be selected.

Let t be the number selected from T. If `t<=4`, at most `t+4<=8` heads are possible. If `t=7 or8`, every Z-element has at least2 blockers in T and no Z can be selected. If `t=6`, the two omitted T-elements can equal at most one of the four disjoint size2 blocker pairs, allowing at most two Z-elements; total<=8. If `t=5`, three omissions contain at most one blocker pair and no size4 blocker set, again allowing at most two Z-elements. Thus at most8 heads are possible, below10. P30 is impossible.

`frontier-20261028-2640-even-p30-p33-check.py`, SHA256 `b1a4c25a860d4ecd14dbd58c3daa4df9de2c90e8a6c3ef45e3e711b59f0ff6c8` (29 LF, 1492 bytes), verifies the complete candidate split, every blocker set and all 256 T-subsets by exact integers. This is a finite check, not a formal proof or independent-model-family review.

## 4. Remaining branch

Together with the earlier even-Q screen and P10/P15/P55/P88 exclusions, the only remaining even-Q P-sizes at order2640 are `{12,20,22,24,40,44}`. They are not claimed feasible; order2640 and the original unrestricted finite-completion problem remain OPEN. No pending odd-tail theorem is used.

**END OF ORDER-2640 EVEN P30/P33 OBSTRUCTIONS.**
