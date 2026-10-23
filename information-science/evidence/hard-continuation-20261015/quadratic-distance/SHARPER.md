# Sharper universal residue obstruction: distance at least 112

**Status: written proof; independent Codex `gpt-6.1-sol` review ACCEPT with no required fixes (`institute/review/continuation-20261015/quadratic-distance-sharper-codex-review.md`, pinned SHA-256 `01760780…5f39` of the reviewed text). Not formally verified or human peer reviewed; novelty unestablished.** This strengthens the separately reviewed distance96 argument in `PROOF.md`. It does not solve balanced NL242 existence. The residue/canonical-sign tools are prior art; the Fourier-correlation strategy closely follows the rank argument in Lou–Xu–Wang, arXiv:2610.17897v1 Section3.2. No new-method claim is made.

## Theorem

For odd-weight Boolean functions `g,h:F_2^8 -> F_2` with Walsh spectra satisfying `|G|+|H|<=28` pointwise, put

```
D = (G^2-4)/32 + (H^2-4)/32 mod2,
d = wt(D),             polarRank(D)=2r.
```

Then

```
40d >= 6656 - 512*2^r.                           (A)
```

In particular `d>=112`. More precisely the only rank/weight pairs not excluded by this inequality and the standard quadratic spectrum are

```
(0,256), (2,192), (4,128), (4,160),
(6,112), (6,128), (6,144), (8,120), (8,136).
```

The pair theorem needs neither a Walsh zero nor a balanced nine-variable completion.

## Proof

Use the proved odd-spectrum/canonical-sign lemmas in [the parent proof](../proof.md). Let `K_g,K_h` be the canonically signed spectra. They have the same magnitudes as `G,H`, their character transforms take values only `+256,-256`, and

```
K_g = 2+8 J_g mod16,       K_h = 2+8 J_h mod16,
J_g=(G^2-4)/32 mod2,       J_h=(H^2-4)/32 mod2.
```

Both residues are quadratic. Set `S=K_g+K_h`, `R=K_g-K_h`, and `T=(-1)^D S`. The capacity bound gives `|S|,|R|<=28`. The congruences imply

```
S = 4+8D mod16,         R = 8D mod16,
T = 4 mod16.
```

Consequently `T` belongs to `{-28,-12,4,20}`. Every one of these four values obeys

```
T^2+8T <= 560,
```

while `R^2<=256` when `D=0` and `R^2<=576` when `D=1`. Thus, writing `C=sum_a (-1)^D(a) S(a)`,

```
sum S^2 <= 143360 - 8C,
sum R^2 <= 65536 + 320d.
```

Two Parseval identities give `sum(S^2+R^2)=262144`. Therefore

```
C <= 40d-6656.                                  (B)
```

Since `S` is the sum of two canonical spectra, its character transform has magnitude at most512. Character orthogonality gives

```
C = (1/256) sum_x transform(S)(x) * Walsh_D(x).
```

A quadratic on eight variables of polar rank `2r` has exactly `2^(2r)` nonzero Walsh coefficients, each of magnitude `2^(8-r)`. Hence its Walsh L1 norm is `2^(8+r)`, including affine/radical-linear cases. It follows that

```
|C| <= 2 * ||Walsh_D||_1 = 512*2^r.             (C)
```

Combining the lower bound from (C) with (B) proves (A). Quadratic weights at each polar rank are

| Polar rank | Possible weights | Weights allowed by (A) |
|---|---|---|
|0|0,128,256|256|
|2|64,128,192|192|
|4|96,128,160|128,160|
|6|112,128,144|112,128,144|
|8|120,136|120,136|

The smallest surviving weight is112. No equality, existence or sharpness is claimed.

## Intrinsic balanced-nine-variable corollary and eight residue types

The correspondence in [PROOF.md Section6](PROOF.md#6-intrinsic-necessary-condition-on-a-balanced-nine-variable-spectrum) identifies `D` with

```
Q(a) = W_f(a)/8 mod2    on the eight-dimensional space s-perp,
```

for a balanced peak28 target with nonzero support XOR `s`. In particular `Q(0)=0`, so `(rank0,weight256)` is impossible. Every balanced target must therefore have

```
#{a : a.s=0 and |W_f(a)| in {8,24}} >= 112,
```

and its intrinsic quadratic lies in one of eight affine-equivalence types:

- rank2, weight192;
- rank4, weights128 or160;
- rank6, weights112,128 or144;
- rank8, weights120 or136.

These are all remaining *quadratic residue types*, not eight truth tables or eight small completion classes. Each type may contain an enormous unresolved family. Affine frequency normalization preserves the existence of a Walsh zero but need not keep that zero at the origin, so a solver using canonical forms must allow a zero at any eligible frequency and explicitly rebalance a recovered witness. A solver-only UNSAT or UNKNOWN does not eliminate a type.

## Limits

This is an additional necessary condition derived from known tools, not a new mechanism or a resolved book question. It does not prove any of the eight remaining types infeasible. It does not inherit the unrestricted covering-radius claims of either 2026 preprint. Written proof review, exact finite arithmetic controls, formal verification and novelty are separate gates.
