# Exchangeable conditional-copy blocks: a compressed representation

## Required first input

Read `frontier-20261028-full-source-lp-optimum-v1-erratum-1.md` first, SHA-256 `c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9`. Its correction is Remark **5.4**, not Remark 3.8, for omitted cross-branch elemental rows. Then the graph/game/FD/cap/symmetry contract is Section 2 of `frontier-20261029-upper-bound-review-input-v1.md` (SHA-256 `e8c46fc195dd22ebcd28e485587a9872582a99ed89b25ce8d2e2ba4cee9e505a`). No held review or assessment is an input.

**Status: WRITTEN, elementary conditional-probability argument; not formally verified, independently reviewed, or novelty-cleared.** This is a new representation, not another enumeration of the previously saturated five-step copy chains. It adds valid auxiliary exchangeability and makes longer iid blocks linear-size rather than exponential-size.

## 1. A simultaneous construction

Let O=(X1,...,X10), let

- T2 = X{1,4,5,6,7,8,9,10};
- T4 = X{1,2,5,6,7,8,10}.

First take C0 to be a copy of X2 over T2, conditionally independent of O given T2. Write B=(O,C0) and Y=(T4,C0).

For any positive integer k, conditionally on B, sample C1,...,Ck independently from the conditional law of X4 given Y. Thus

P(C1=c1,...,Ck=ck | B=b) = product_j P(X4=cj | Y=y(b)).

This finite conditional-kernel construction preserves the law of B and has all of the following properties:

1. Each Cj has the joint law of X4 with Y.
2. The tuple (C1,...,Ck) is conditionally independent of B given Y.
3. The law of (B,C1,...,Ck) is invariant under every permutation of C1,...,Ck.
4. In the ordered view, Cj is precisely a copy of X4 over (Y,C1,...,C(j-1)), conditionally independent of all previous variables given that over-set. Indeed, by property 2, the conditional law of X4 given Y and the previous copies is its law given Y alone; the proposed kernel has exactly that law.

Consequently this constructs the same sequential-copy specifications used by the repeated-X4 programs, but additionally makes their valid exchangeability explicit.

## 2. An optional last X2 copy

Let Z=(T2,C0,C1,...,Ck). Sample a fresh D from the conditional law of X2 given Z, independently of all previous variables given Z. This is another ordinary copy step.

The joint law of the previous variables is invariant under permutations of the Cj. The conditional law P(X2 | Z) is invariant under the corresponding permutations of Z, on its support: both the joint numerator and the marginal denominator are invariant. Therefore the augmented law (O,C0,D,C1,...,Ck) is still exchangeable in the Cj. Values of a kernel on zero-probability fibers can be chosen arbitrarily and do not change the joint law.

This construction covers the program X2 followed by k copies of X4 and then a copy of X2. It does not assert that arbitrary sequential copy programs have auxiliary permutation symmetry.

## 3. Entropy coordinates

Take the ordinary base to be B=(O,C0) without the optional D, or B=(O,C0,D) with it. Let b=11 or 12 accordingly. An entropy coordinate is

h(U,r) = H(B_U, any r distinct copies Cj), 0 <= r <= k.

By exchangeability, the coordinate depends only on U and r, not on the chosen copies. Nonempty coordinates number 2^b*(k+1)-1. The original coordinates (r=0, U using only X1..X10) are shared with the other LP branches. Other coordinates remain branch-local.

## 4. Full elemental Shannon system, not a subset

Every full-set conditional entropy is either an ordinary-variable row

h(B,k) - h(B minus i,k) >= 0,

or a copy-variable row

h(B,k) - h(B,k-1) >= 0.

Every elemental conditional mutual information is one of:

- Two ordinary variables i,j: h(U+i,r)+h(U+j,r)-h(U+i+j,r)-h(U,r) >= 0, with U excluding i,j and 0<=r<=k.
- One ordinary i and one copy: h(U+i,r)+h(U,r+1)-h(U+i,r+1)-h(U,r) >= 0, with U excluding i and 0<=r<k.
- Two distinct copies: 2h(U,r+1)-h(U,r+2)-h(U,r) >= 0, with 0<=r<=k-2.

These cases exhaust every pair of distinct variables and every conditioning subset under the exchangeability quotient. Thus imposing the displayed rows is exactly the quotient of the full elemental Shannon system on b+k variables.

The row count before tautology removal is

(b+1) + choose(b,2)*2^(b-2)*(k+1) + b*2^(b-1)*k + 2^b*(k-1),

where the last summand is absent for k=1. It grows linearly in k for fixed b.

## 5. Copy equalities in these coordinates

Write E=(O,C0), Y=(T4,C0). The first-copy equalities and independence are unchanged.

For 0<=r<k and every U subset of Y:

h(U,r+1) = h(U+X4,r),

h(E,r+1)+h(Y,r)-h(E,r)-h(Y,r+1) = 0.

These are exactly the copy-marginal and independence constraints of a repeated-X4 step, modulo the exchangeability quotient.

If D is present, for every U subset of (T2,C0) and 0<=r<=k:

h(U+D,r) = h(U+X2,r).

Its independence is

h(E+D,k)+h(T2+C0,k)-h(E,k)-h(T2+C0+D,k) = 0.

All are valid for the construction above. The compressed LP need not imply that every feasible profile is entropic; only the existence of this extension for each original law is required for an upper bound.

## 6. Implementation scope

`frontier-20261029-exchangeable-copy-lp-v1.py` implements the rows above. Its initial test replaces the two four-step programs of the 2603/389 model by k=2 with D and k=3 without D (`frontier-20261029-exchangeable-specs-r1.json`). No new bound is asserted in this packet. A strict improvement requires a separate exact certificate and independent row reconstruction.
