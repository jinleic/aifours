# Shor completion: two-power fibre structure for `11*2^a` heads

Owner **MathShor-2**, math-5. Native clock of exact synthetic controls: **Wed Oct 28 21:37:40 PDT 2026**.
**ALL-ORDER WRITTEN necessary structure with named classical imports; no full completion/noncompletion, formal/peer/cross-family acceptance or novelty claim.**

## 1. Exact even-tail family

Let `k>=2`, `1<=a<k`, `b=k-a`, and `n=165*2^k`. Suppose the SAME actual direct b-run border factors of a finite UD factor-complete extension of the literal Shor code satisfy

    |P|=11*2^a,   |Q|=15*2^b,
    A={0,3,8,11} subset P,   Y={0,1,7,13,14} subset Q.

Q is EVEN. For `i=0,...,10` and `j=0,...,14`, form normalized actual-residue multisets modulo `m=2^k`:

    P_i={ (p-i)/11 mod m : p in P, p==i mod11 },
    Q_j={ (q-j)/15 mod m : q in Q, q==j mod15 }.

Every one of the165 pairs `P_i,Q_j` is a direct SET factorization of `Z_m`, with sizes `2^a,2^b`. The normalized P_0 contains0 and1 from old heads0,11, so every Q_j is contained in a single parity class. Since every old j is less than15 and occurs as a Q-tail, its normalized fibre contains0 and therefore

    q=j+30t (mod n)    for every actual Q-tail q==j mod15.      (1)

The old head difference11 further forbids the following t-residues modulo11 in these anchored fibres:

| old tail j | forbidden t mod11 |
|---:|---|
| 0 | {3,5,7} |
| 1 | {3,4} |
| 7 | {5,6} |
| 13 | {7,8} |
| 14 | {4,6,8} |

Here t is defined modulo `n/30=11*2^(k-1)`, so the mod11 restriction is unambiguous. No claim is made about other fibres or the existence of an original completion.

## 2. Explicit imports and proof

The actual-word border theorem and Sands gcd-difference criterion are classical and independently reconstructed in earlier packets. We explicitly import [Łaba–Londner, Corollary6.2](https://arxiv.org/html/2106.14042v1): in a cyclic tiling where at most two primes divide both tile cardinalities, both tiles satisfy Coven–Meyerowitz T2. The only common prime here is2.

The tiling identity puts Phi_11 in P and Phi_3,Phi_5 in Q; T2 also puts Phi_15 in Q. Thus P is uniform mod11 and Q mod15. For each two-power order `2^s` owned by P, T2 with11 gives `Phi_(2^s)(X^11)|P`; mask decomposition modulo11 gives that factor in EVERY P_i. For each order owned by Q, T2 with3 and5 gives `Phi_(2^s)(X^15)|Q`; mask decomposition modulo15 gives the factor in EVERY Q_j. Their two-power allocations partition all s by evaluation at1, so Fourier inversion yields convolution1 for every fibre pair, and the nonnegative folded weights must be0/1. This proves the direct tilings and, by Sands applied to P_0's difference1, their single-parity Q fibres.

For (1), Q's old anchors give parity0 in their normalized fibres. Old P has gcd-difference11, so Q cannot have a difference of gcd11. When j is odd, compare `j+30t` to old even tails0 and14; when j is even, compare to old odd tails1,7,13. In each comparison the difference is odd and nonzero modulo3 and5; it has gcd11 exactly when `t==7*(other-j) mod11`, because 30 has inverse7 modulo11. The resulting forbidden classes are precisely those in the table.

## 3. Controls and limits

`frontier-20261028-even-tail-eleven-fibre-check.py`, SHA256 `be153d1d4d75c5d6755fd0da4441eb04084bbab24d1b5795f3a3ee74ef79865b` (21 LF, 1003 bytes), directly checks all165 fibre tilings and parity for a synthetic n2640 tiling `P={0,...,43}`, `Q={0,44,...,2596}`, and checks every listed gcd11 residue implication. The synthetic Q lacks the old Shor tails and is NOT a completion. The classical common-prime T2 corollary is an explicit import, not proved by this control.

No cardinality branch is excluded here. Other even-Q families, the 2310-order family and the original unrestricted finite UD factor-completion problem remain OPEN; no human/peer/formal/independent-family or novelty acceptance is claimed.

**END OF ELEVEN-PRIME EVEN-TAIL FIBRE STRUCTURE.**
