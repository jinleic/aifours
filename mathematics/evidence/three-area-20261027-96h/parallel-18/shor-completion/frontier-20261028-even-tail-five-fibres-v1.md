# Shor completion: two-power fibre structure for `5*2^a` heads

Owner **MathShor-2**, math-5. Native clock of exact synthetic controls: **Wed Oct 28 21:36:10 PDT 2026**.
**ALL-ORDER WRITTEN necessary structure with an explicitly named classical import; no full completion/noncompletion, formal/peer/cross-family acceptance or novelty claim.**

## 1. Exact even-tail family

Let `k>=2`, `1<=a<k`, `b=k-a`, and `n=165*2^k`. Suppose the SAME actual border factors of a finite UD factor-complete extension of the literal Shor code tile `Z_n` directly and have

    |P|=5*2^a,   |Q|=33*2^b,
    A={0,3,8,11} subset P,   Y={0,1,7,13,14} subset Q.

Q is EVEN. For `i=0,...,4` and `j=0,...,32`, define normalized exponent multisets modulo `m=2^k` from actual representatives in `[0,n)`:

    P_i={ (p-i)/5 mod m : p in P, p==i mod5 },
    Q_j={ (q-j)/33 mod m : q in Q, q==j mod33 }.

EVERY one of the165 pairs `P_i,Q_j` is a direct SET factorization of `Z_m`, with sizes `2^a,2^b`. For each old tail `j in Y`, all Q_j residues are even; therefore every actual Q-tail in the same mod33 class has form

    q = j+66t  (mod n).                                         (1)

Comparing to opposite-parity old tail anchors further forces t into the following residues modulo5:

| old tail j | allowed t mod5 |
|---:|---|
| 0 | {0,4} |
| 1 | {0,1,2} |
| 7 | {0,1,4} |
| 13 | {0,3,4} |
| 14 | {0,1} |

The coordinate t is defined modulo `n/66=5*2^(k-1)`, so its mod5 residue is unambiguous. These are necessary restrictions only.

## 2. Named classical import and fibre factorization

The general actual-word border theorem and Sands gcd-difference disjointness are classical and independently reconstructed in prior packets. We also explicitly import **Łaba–Londner, Corollary6.2**: when at most two primes divide both cyclic tile cardinalities, both tiles satisfy Coven–Meyerowitz T2. See the [original corollary](https://arxiv.org/html/2106.14042v1). Here the only common prime of `5*2^a` and `33*2^b` is2.

The tiling identity forces Phi_5 into P and Phi_3,Phi_11 into Q. T2 puts Phi_33 into Q, so P is uniform mod5 and Q uniform mod33: their normalized fibre sizes are2^a and2^b. For every two-power order `2^s` owned by P, T2 with5 makes `Phi_(2^s)(X^5)` divide P; decomposing the mask over `Z[X^5]` makes every normalized P_i divisible by `Phi_(2^s)`. For every two-power order owned by Q, T2 with3 and11 similarly gives `Phi_(2^s)(X^33)|Q`, so every normalized Q_j has that factor.

The two sides' two-power factors partition `s=1,...,k` by evaluation at1. Fourier inversion then gives convolution1 for every folded pair P_i,Q_j on Z_m; their nonnegative integer weights must all be0/1. Thus all165 are direct SET tilings of Z_m.

The normalized P_3 contains0 and1 from old heads3 and8. Sands applied to each `P_3+Q_j` forces Q_j to have a single parity. Each old j has normalized Q_j-element0, proving (1).

## 3. Old-head gcd5 gives the residue table

Old heads3 and8 differ by5, so Q cannot contain a difference with gcd5 against n. For an odd old j in `{1,7,13}`, the q in (1) is odd. Compare it with even old tails0 and14: each difference is odd and nonzero modulo3 and11, so it has gcd5 precisely when t equals `-j mod5` or `14-j mod5`, respectively. The complement gives the three odd rows of the table.

For j=0 or14, q is even. Compare it with odd old tails1,7,13; the differences are odd and nonzero modulo3 and11. Equality modulo5 to one of those old tails is therefore forbidden by gcd5. This gives `{0,4}` for j0 and `{0,1}` for j14. No unmentioned t-residues are excluded by this argument.

## 4. Controls and scope

`frontier-20261028-even-tail-five-fibre-check.py`, SHA256 `ffee542574b2085c9fb8a6e09d9110fbc9729bc8f5689a600e83a02d2c2b581a` (23 LF, 1144 bytes), checks all165 fibre tilings and parity for the synthetic n2640 tiling `P={0,...,19}`, `Q={0,20,...,2620}`, plus the displayed gcd5 residue implications. That synthetic Q lacks the old Shor tails and is NOT a completion. The classical import is not independently reproved by the finite test.

No branch is excluded by this packet. Other even-Q cardinality families, other 2310-family branches, and the original unrestricted finite UD factor-completion problem remain OPEN. No peer, human, formal, independent-family or novelty acceptance is claimed.

**END OF FIVE-PRIME EVEN-TAIL FIBRE STRUCTURE.**
