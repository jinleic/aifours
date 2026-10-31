# Additive diagnostic v2: the whole displayed defective witness family is f274-certified, conditional on the written 2+2 proof

**WRITTEN, owner candidate, UNREVIEWED.** This successor strengthens the separate one-parameter diagnostic `frontier-20261029-2plus2-witness-f274-overlap-diagnostic-v1.md` (SHA-256 b3a91511e7e233327d4dab1229c51a5498691ff32211713eff4c85c86a350a1b); neither the earlier diagnostic nor the immutable 2+2 packet is changed. The conclusion uses the UNREVIEWED all-variable 2+2 T2 proof `frontier-20261029-d4-t2-arbitrary-2plus2-blocks-v1.md` (SHA-256 bb09c6bf442b9d497241297c57f9da678b559b5d13ee56cc871de4a6fc7f1473) for cross-component bounds and uses the adopted f274 definition of `η`. No selected physical q, numerical instance, execution, false f198 estimate, or held source is used.

## 1. Correct qualification of the comparison

For **every** `α,β,c,d∈C`, let

`A=(α I2+c E12)⊕(−α I2)`, `B=(β I2+d E12)⊕(−β I2)`, `X=A⊗I4+I4⊗B`, `H=X†X`, `L=||A||_F²+||B||_F²`.

**Conditional on the new 2+2 written T2 theorem, the displayed product basis, after harmless diagonal phase gauges, satisfies `ρ(|H^[2]|)≤2L`.** Thus the entire symbolic family offered in the 2+2 manuscript to distinguish the old *structural* classes is in f274's certificate-success region, not merely the equal-parameter subfamily. For `αcβd≠0` both squares are nonnormal and both factors are defective, but these facts do not establish a single member outside f274. Whether any other separately 2+2 reducing pair has `η>2L` remains UNPAID. There is no physical counterexample, general T2 or novelty claim.

## 2. Nontrivial four-vertex compound block

By one common scalar phase and diagonal unitary gauges within the two first blocks, take `t=|α+β|`, `c=|c|`, `d=|d|` nonnegative without changing singular values, `L`, the 2+2 pattern, or the entrywise-modulus compound Perron value in the correspondingly gauged product basis. The `11`-sector factor is

`X11=t I4+c E12⊗I2+d I2⊗E12`,

and `H11=X11†X11` has entries

```
[[ t²,       tc,       td,              0],
 [ tc,    t²+c²,       cd,             td],
 [ td,       cd,    t²+d²,             tc],
 [  0,       td,       tc,      t²+c²+d²]].
```

It is entrywise nonnegative. We prove

`ρ(|H11^[2]|)≤Tr H11=4t²+2(c²+d²)`,  (2.1)

with strict inequality if `t>0`. This is a property of this structured block; it is **not** asserted for an arbitrary PSD 4×4 matrix.

Let `T=2t²`, `u=c²`, `v=d²`, `C=u+v`, and `Q=(Tr H11)I6−|H11^[2]|`. Order the pair basis as `12,13,34,24,14,23`. The last two diagonal entries of `Q` are `T+C`, have zero mutual coupling, and have identical couplings to the first four: after replacing them by symmetric and antisymmetric combinations, the antisymmetric coordinate is the positive scalar `T+C`, while the remaining block is

```
[ Q1    0   −√T (d,c)ᵀ ]
[  0   Q2   −√T (d,c)ᵀ ]
[−√T(d,c) −√T(d,c)  T+C ]

Q1 = [[T+u+2v, −cd], [−cd, T+2u+v]],
Q2 = [[T+u,    −cd], [−cd, T+v   ]].
```

For `t>0`, both `Q1,Q2` are positive definite. Let `z=(d,c)ᵀ`. Since `Q2 z=T z` and `zᵀz=C`, the Schur-complement contribution from `Q2` is `T zᵀQ2⁻¹z=C`. The remaining scalar is

`T+C−C−T zᵀQ1⁻¹z = T(1−zᵀQ1⁻¹z)`.

Now

`Q1−zzᵀ = T I2 + [[C,−2cd],[−2cd,C]]`,

and the second matrix has nonnegative eigenvalues `(c−d)²,(c+d)²`. Therefore `Q1−zzᵀ` is positive definite for `T>0`, hence `zᵀQ1⁻¹z<1`. The Schur complement is positive; so `Q` is positive definite and (2.1) is strict. At `t=0`, (2.1) follows by continuity. This proof includes `c=0` or `d=0`; in disconnected limiting cases the block remains the full six-dimensional compound.

## 3. Every other compound component

The remaining `X` sectors are

`X12=(α−β)I4+c E12⊗I2`,

`X21=(β−α)I4+d I2⊗E12`,

`X22=−(α+β)I4`.

After a permutation of product basis, each of `H12,H21` is the direct sum of two identical 2×2 Hermitian PSD blocks. Each such block's support graph is a single edge or two isolated vertices; hence the Perron radius of its entrywise modulus equals its actual top eigenvalue. `H22` is diagonal. The `H11` block also has `ρ(|H11|)=λmax(H11)` because its entries are nonnegative. Taking connected components as necessary, **every** one-particle component `Hi` of `H` therefore has `ρ(|Hi|)=λmax(Hi)`.

For two distinct one-particle components `Hi,Hj`, the corresponding two-token block of the compound, up to a signed permutation of pair basis, is `Hi⊗I+I⊗Hj`; its entrywise modulus has Perron radius `ρ(|Hi|)+ρ(|Hj|)=λmax(Hi)+λmax(Hj)`. These are two actual eigenvalues of `H` from orthogonal components, so their sum is at most `S2(X)≤2L` by the written 2+2 theorem. Inside a component of size two, the compound consists of the single diagonal value `Tr Hi≤2λmax(Hi)`. In `H12,H21` the identical second copy supplies a distinct eigenvalue `λmax(Hi)`, so again `2λmax(Hi)≤S2(X)≤2L`. Singleton components have no within-component two-token block. A disconnected `H11` in a limiting case is already covered by (2.1), which treats its whole compound.

For the only remaining within-component block, (2.1) and the trace-zero block identities imply

`ρ(|H11^[2]|)≤4|α+β|²+2(|c|²+|d|²)≤8(|α|²+|β|²)+2(|c|²+|d|²)=2L`.

The maximum over the compound's orthogonal component blocks is therefore `≤2L` in this explicit basis, so `η≤2L`. The proof does not establish **strict** certificate success in every parameter case and does not establish a criterion for general non-Jordan 2+2 blocks.

## 4. Non-claims and provenance

The proof's only new comparison is the full four-complex-parameter witness family above. It does **not** establish that all arbitrary 2+2 pairs are f274-certified, or that any is not. It does not imply physical q3, T3/Z2, novelty, or correctness of external source claims. This is a later disclosure made after the 2+2 packet pin; it is not retroactively part of any already frozen review and must be supplied as a separate additive input if reviewed. The `S2≤2L` use is explicitly conditional on the current UNREVIEWED candidate, not parent adoption.
