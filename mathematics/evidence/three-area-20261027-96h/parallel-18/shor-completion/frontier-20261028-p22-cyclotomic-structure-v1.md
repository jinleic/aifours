# Shor completion: an all-order two-prime structure for a 22-head border

Owner **MathShor-2**, math-5. Native clock of the finite algebra controls: **Wed Oct 28 21:17:42 PDT 2026**.
**ALL-ORDER WRITTEN necessary condition with an explicitly named classical theorem; no branch exclusion, original noncompletion, formal/peer/cross-family acceptance or novelty claim.**

## 1. Exact theorem

Let `P+Q` be a direct tiling of `Z_n`, with `0,11 in P`, `|P|=22`, `v_11(n)=1`, and `v_2(n)=k>=1`. Then:

1. In EACH of the 11 residue classes modulo11, P has exactly one even and one odd element.
2. Q's counts in the `2^k` residue classes are a common integer `a` on all even classes and a common integer `b` on all odd classes. In particular `a+b=n/(11*2^k)`.

For the literal Shor code, this is a necessary property of the SAME actual P,Q border pair of any finite UD factor-complete extension satisfying the stated n and |P| conditions. If the old tails0 and1 are also in Q then a,b are positive. At n2640 (`k=4`), this gives `a+b=15` and the exact parity-folded Q condition used in the ongoing even-Q P22 investigation. It does not itself exclude P22.

## 2. Explicit named import

We use the **Coven–Meyerowitz (T2) theorem for a tiling set of cardinality with at most two prime factors**: if two prime-power cyclotomic polynomials of different primes divide that set's mask, their product-order cyclotomic polynomial also divides it. See [Kiss–Londner–Matolcsi–Somlai, Theorem1.2](https://arxiv.org/html/2411.03854v3), which states this classical result. This is an explicit external mathematical import, not a new proof or a novelty claim.

It applies: a cyclic tiling `P+Q=Z_n` gives a tiling of the integers by finite set P and the periodic translate set `Q+nZ`, and `|P|=22=2*11`. The mask polynomial is the 0/1 polynomial of the actual residue set P.

## 3. Prime-power allocation and the old-head constraint

Since `v_11(n)=1` and 11 divides |P| but not |Q|, primitive 11th-root vanishing forces `Phi_11` to divide P. Thus P is uniform modulo11, with exactly2 elements in each class.

For each `j=1,...,k`, the tiling identity puts `Phi_(2^j)` in P or Q. Each evaluates to2 at1. The total 2-adic valuation of `P(1)Q(1)=n` is k, while `v_2(P(1))=1`. Therefore EXACTLY one of those cyclotomic factors lies in P, the remaining k-1 lie in Q, and none is shared. Write P's unique factor as `Phi_(2^s)`.

By (T2), `Phi_(11*2^s)` also divides P. Put `u=2^(s-1)`. The elementary identity

    Phi_(2^s)(X) * Phi_(11*2^s)(X) = 1 + X^(11u)            (1)

forces the coefficients of the P-mask folded modulo `22u` to agree at positions r and r+11u. Within each mod11 class there are exactly two P-elements, so their folded positions must be such a pair. In class0 those two actual elements are the old heads0 and11. Their difference is11, whereas a paired separation is `11u mod22u`; this is possible only for `u=1`, i.e. `s=1`.

Thus `Phi_2` divides P. Equation(1) for s=1 makes the two P-elements in every mod11 class occupy opposite residues modulo22: one even and one odd. This proves conclusion1.

## 4. Tail folded balance

For s=1, Q owns every `Phi_4,Phi_8,...,Phi_(2^k)`. Their product is

    1 + X^2 + X^4 + ... + X^(2^k-2).

Reducing the Q-mask modulo `X^(2^k)-1` preserves this divisibility. A polynomial of degree below `2^k` divisible by the displayed polynomial is `(a+bX)` times it, so all even residue counts equal a and all odd residue counts equal b. Summing gives `|Q|=2^(k-1)(a+b)=n/22`, or `a+b=n/(11*2^k)`.

For k=1 the product is the empty product1 and the two residue classes are simply the two coefficients a,b, so the same conclusion remains valid.

## 5. Exact controls and limits

`frontier-20261028-p22-cyclotomic-check.py`, SHA256 `5efba57fecd33b121e10f94b815077b7f389b3cb73642be0202ea55c844e3be1` (19 LF, 751 bytes), checks identity(1) by integer coefficient cancellation and verifies the old-head separation test for s=1,...,8. These are bounded controls; the argument above covers every k>=1. It does not independently verify the imported Coven–Meyerowitz theorem.

The original unrestricted finite UD factor-completion problem remains OPEN. No human, peer, formal, independent-model-family or novelty gate is claimed.

**END OF ALL-ORDER P22 CYCLOTOMIC STRUCTURE.**
