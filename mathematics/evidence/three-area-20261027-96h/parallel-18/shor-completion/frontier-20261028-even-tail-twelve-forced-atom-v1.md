# Shor completion: a forced actual tail in the all-order 12-tail branch

Owner **MathShor-2**, math-5. Native clock of exact coefficient controls: **Wed Oct 28 21:42:15 PDT 2026**.
**ALL-ORDER WRITTEN necessary condition with explicitly named classical imports; not a completion, unrestricted noncompletion, formal/peer/cross-family acceptance or novelty claim.**

## 1. Exact conclusion

For ANY `a>=1`, let `k=a+2` and `n=165*2^k`. Suppose a finite UD factor-complete extension D of the literal Shor code has the SAME actual direct border factors

    |P|=55*2^a,   |Q|=12.

Q is EVEN. Then:

1. Every actual Q-tail residue is congruent to0,1 or2 modulo6.
2. The `1 mod3` tail fibre has exactly one Q-element in EACH of the four residue classes `1,7,13,19 mod24`.
3. In particular D necessarily contains an ACTUAL atom `b^l a^j`, with `l>=1` and `j==19 mod24`. This residue is absent from the five old b-run tail anchors, so the atom is new relative to those anchors.

This is a forced word in a hypothetical completion, not a construction of D or a general noncompletion claim. The result applies simultaneously to all a>=1; it does not depend on the pending odd-Q theorem.

## 2. Fibre tiling and two-power spectral allocation

The general actual-border factorization and Sands gcd-difference criterion are classical. We explicitly import [Łaba–Londner, Corollary6.2](https://arxiv.org/html/2106.14042v1), as used in the separately written `frontier-20261028-even-tail-unified-fibres-v1.md`: because the only common prime of the border cardinalities is2, both cyclic tiles satisfy Coven–Meyerowitz T2.

That predecessor proves that, for every mod55 head fibre P_i and mod3 tail fibre Q_j, the normalized projected sets

    P_i={ (p-i)/55 mod 2^k : p in P, p==i mod55 },
    Q_j={ (q-j)/3 mod 2^k : q in Q, q==j mod3 }

form a direct set factorization of `Z_(2^k)` with sizes `2^a` and4. Every Q_j has the SAME owned two-power cyclotomic orders. In particular Q_1 contains the three distinct normalized residues0,2,4 from the actual old tails1,7,13.

In a direct factorization of the 2-power group, all k prime-power cyclotomic factors are allocated between the sides. Their values at1 and `|Q_1|=4` show that Q_1 owns exactly TWO of them.

## 3. The unique spectrum of the old three-tail fibre

Q_1 cannot own Phi_2: among its four elements at least three are even, so its even and odd counts cannot agree.

It MUST own Phi_4. Otherwise both of its two owned factors have orders at least8 and are polynomials in `X^4`; their product evaluates to4 at1. Divisibility then forces the number of Q_1-elements in each residue class modulo4 to be a multiple of4. But old normalized residues0,4 lie in class0 and2 lies in class2, giving two positive classes with only four total elements.

Let the other owned factor be `Phi_(2^s)`, `s>=3`. If `s>=4`, fold Q_1 modulo `2^s`. Divisibility by `1+X^(2^(s-1))` pairs every residue r with `r+2^(s-1)`. The old residues0,2,4 lie in three distinct lower-half positions, so they need three distinct partner elements, impossible with only one remaining element. Thus s=3: Q_1 owns exactly Phi_4 and Phi_8.

Phi_8 pairs mod8 classes0/4 and2/6. The old elements0,2,4 occupy the first three of these, forcing the fourth to be6 mod8. Hence Q_1 has exactly `{0,2,4,6}` modulo8, which gives tail residues `{1,7,13,19}` modulo24 and proves conclusions2–3.

## 4. Why every tail is 0,1 or2 mod6

Q_1 does not own Phi_2, so the complementary two-power spectrum places Phi_2 in EVERY P_i. Each P_i has both parities; by Sands, every Q_j in the direct fibre tiling has only one parity. The old tails0,1,14 give even normalized elements respectively in Q_0,Q_1,Q_2. All three tail fibres are therefore even. Since q=j+3v with v even, every actual Q-tail has residue j in `{0,1,2}` modulo6, proving conclusion1.

## 5. Checks and boundary

`frontier-20261028-even-tail-twelve-check.py`, SHA256 `389a204fd11a1340110ea5d97cd3536a04d1c324da7760879cdbe800ca2ff406` (19 LF, 712 bytes), checks every possible fourth normalized residue for k=3,...,10 using exact folded coefficients: whenever two two-power factors occur, they are exactly Phi_4,Phi_8 and the fourth is6 mod8. This is a bounded control; the argument in §3 is all-order.

The common-prime T2 and actual-border/Sands results are explicitly named prior imports, not established by this finite control. No independent scientific or novelty review is claimed. Other even-Q cardinality families, the 2310-order family and the original unrestricted finite UD factor-completion problem remain OPEN.

**END OF TWELVE-TAIL FORCED-ATOM THEOREM.**
