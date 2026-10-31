# Shor completion: divisor-class packing at order 1320

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 19:04:06 PDT 2026**.
**Conditional necessary conditions at exactly n=1320, with an independently checked finite certificate. Not an exclusion of 1320, an all-order no-go, a completion construction, a formal proof or a novelty claim.**

## 1. Statement

If any finite UD factor-complete extension of the literal Shor code has actual pure-a order `n=1320`, its actual direct border factorization `P+Q=Z_1320` must satisfy

    |P| <= 80,     |Q| <= 130,
    |P| in {12,15,20,22,24,30,33,40,44,55,60,66},
    |P| >= 12,     |Q| >= 20.

This reduces the preceding 17 border-cardinality possibilities to12. It **does not** show that any one of the12 is feasible or that order1320 is impossible.

The 80/130 bounds are exact finite consequences of divisor-class incompatibility and the actual old border anchors

    A={0,3,8,11} subset P,      Y={0,1,7,13,14} subset Q.

The relevant general criterion is the classical Sands divisor-class theorem; see [Kiss–Londner–Matolcsi–Somlai, Theorem2.1](https://arxiv.org/html/2411.03854v3). A direct proof of the only direction used here follows.

## 2. Why gcd-difference classes cannot meet

For any direct tiling P+Q of Z_n, no two nonzero differences `p-p'` and `q-q'` can have the same `gcd(.,n)`. Indeed, if `gcd(d,n)=gcd(e,n)`, there is a unit u modulo n with `u d=e`: solve modulo `n/gcd(d,n)` and lift by CRT to avoid every remaining prime divisor of n.

Moreover `uP+Q` is also a direct tiling. At any nontrivial n-th root of unity ζ, `P(ζ)Q(ζ)=0`; because u is a unit and P has integer coefficients, `P(ζ^u)=0` iff `P(ζ)=0` by cyclotomic irreducibility. Thus the same Fourier vanishing condition, together with `|P||Q|=n`, gives `uP+Q=Z_n` directly. But `u(p-p')=q-q'` then creates the collision `up+q'=up'+q`. This contradiction proves the necessary condition.

At n=1320, the positive gcd classes occurring among old-anchor differences are exactly

    G_A={3,5,8,11},      G_Y={1,2,6,12}.

Hence each new P-residue x must have `gcd(x-a,1320) not in G_Y` against each a in A unless x=a; any two P-residues must likewise avoid G_Y. Similarly each new Q-residue must avoid G_A against Y and pairwise against all of Q.

## 3. Certificate-checked bounds

Direct integer enumeration gives112 individually permitted P-residues and286 individually permitted Q-residues. The immutable certificate `frontier-20261028-1320-divisor-packing-v1.json` contains:

* 16 disjoint triples among the112 P-candidates, every pair inside each triple having gcd-difference in G_Y. P takes at most one from each, so `|P|<=112-2*16=80`.
* A partition of all286 Q-candidates into130 nonempty cliques, every within-clique pair having gcd-difference in G_A. Q takes at most one from each, so `|Q|<=130`.
* An 80-element set containing A that passes the P-side divisor screen pairwise. It proves that 80 is sharp **for this one-sided screen only**; it is not a tiling or a code completion, and80 does not divide1320.

`frontier-20261028-1320-divisor-packing-check.py` independently reconstructs both candidate sets and gcd classes, verifies disjointness/coverage and every pair in the certificate, and checks the 80-element control. Its actual output was `P_candidates=112, Q_candidates=286, P_bound=80, Q_bound=130`.

Since `|P||Q|=1320`, the 80/130 bounds alone leave `|P| in {11,12,15,20,22,24,30,33,40,44,55,60,66}`. Size11 is also impossible by the elementary prime-balance argument already written in the six-head border packet: `11` divides |P| but not |Q|, so P is uniform modulo11, yet it contains both0 and11 in one class and has total size11. This leaves the 12 sizes in §1. Their reciprocals are all at least20.

## 4. Sharpened actual multi-b consequences, only at n=1320

The previously written graded head-border tradeoff with `|P|>=12` implies that `N_out<264` forces at least **eight actual atoms** `a^i b^k`, `k>=2`, with distinct head residues outside `{0,3,8,11}`. The dual tail-border tradeoff with `|Q|>=20` implies that `N_Y<220` forces at least **fifteen actual atoms** `b^l a^j`, `l>=2`, with distinct tail residues outside Y. `N_out` and `N_Y` count actual one-b atoms outside the stated head and tail sets, respectively.

If both strict inequalities held for the same D, at least23 distinct multi-b border atoms would be necessary. The two classes cannot share a word except a pure b-run, and UD with the actual b atom excludes a pure `b^k` atom for `k>=2`. These are still conditional necessities, not actual examples.

## 5. Pins and scope

| Artifact | SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-1320-divisor-packing-v1.json` | eb73d65b4e9d2f79b917e4da2d390cd157388341bb75e5c5049a914cf6ef39cb | 1 / 2081 |
| `frontier-20261028-1320-divisor-packing-check.py` | 937a789eba003c735dd6e0b72dc7c6967058d9b4417a48d9d9b8a9689567dfc6 | 36 / 2027 |
| `frontier-20261028-1320-divisor-packing-generator.py` | 505613bbf4192b8d289b70917f9a9d8ae0ce4115f966d0bb0431a0b3a1615085 | 45 / 2198 |

The exhaustive candidate computation and finite witness verification are same-harness exact integer computations, not formal proof, peer acceptance, cross-model review or novelty screening. The general Sands criterion and classical border factorization are named imports; the necessary gcd direction was also reconstructed above. The original all-order completion/noncompletion problem remains OPEN.

**END OF 1320 DIVISOR-CLASS OBSTRUCTION.**
