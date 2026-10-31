# Strict uniform group-coset gain requires at least 384 effective states

**Status: WRITTEN with independently replayed exact index screen; conditional on pinned graph-FD and rank certificates; scientific review and novelty clearance pending.** For a uniform finite-group coset law `X_i=gH_i` satisfying all original R-minus FDs, let `K=intersection_i H_i` and `m=[G:K]`. If `Delta=H(X_V)-(2/3)sum_i H(X_i)>0`, then

\[
\boxed{m\ge384.}
\]

This strengthens the `288`-state obstruction `frontier-20261028-uniform-coset-288-barrier-v1.md` SHA-256 `d260d2b6a370a3c0afd9b77ed94d027d61093948f795e085c648da057dfc04ac`. It covers **uniform group-coset laws only**, not arbitrary FD laws or nonuniform coset laws. No attainability or unrestricted guessing-number claim is made.

## Exact index screen

The `288` packet pins the conditioned inequality, linear-rank bound, the lower bound `m>=180`, the nonzero/distinct index-two character bound, the divisor and factorial-action conditions, and the exact exclusion of `m=192`. The identical arithmetic screen, extended through `m=383` and replayed separately, leaves exactly the following new possibilities:

| `m` | number of index-two vertices | nonbinary indices |
|---:|---:|---|
| 288 | 7 | `3,3,3` or `3,3,4` |
| 288 | 8 | `3,3`; `3,4`; `3,6`; or `4,4` |
| 320 | 8 | `4,5` |
| 336 | 8 | `3,7` or `3,8` |
| 360 | 7 | `3,3,5` |

All other `180<=m<384` violate at least one exact necessary arithmetic condition. The remaining cases are excluded below.

## Common quotient facts

Let `K_2` be the intersection of all index-two subgroups, `Q=G/K_2`, `|Q|=2^t`, `s=[K_2:K]`, and `phi:G -> Q` the quotient map. Thus `m=2^t s`. For a subgroup `H`, write `H_0=H∩K_2`. Since `K_2` is normal,

\[
[G:H]=[Q:phi(H)]\,[K_2:H_0].\tag{7}
\]

If `[G:H]` is odd, its image has power-of-two index dividing an odd number, so `phi(H)=Q` and `[K_2:H_0]=[G:H]`. Every group FD is equivalent to the neighbour-subgroup intersection inclusion because `g` is uniform on the whole group. Index-two variables are distinct by the conditioned mutual-information inequality, so `b` of them imply `2^t-1>=b`.

With exactly two nonbinary subgroups `A,B`, their vertices must be adjacent by the `175` barrier. Their two FDs imply `K_2∩A=K_2∩B=K`; hence `s` divides both nonbinary indices by (7). This rules out:

* All four `m=288, b=8` patterns: `9` divides `s`, while none of the displayed nonbinary indices is divisible by 9.
* The `m=320, b=8` and `m=336, b=8` patterns: the two displayed indices are coprime, forcing `s=1`, although `m` is not a power of 2.

## The 360-state pattern

For `m=360` there are seven binary vertices and three exceptions of indices `3,3,5`. Distinct binary characters require `t>=3`; `2^t` divides 360, so `t=3` and `s=45`. The two index-three subgroups have full image in `Q`, hence their intersections with `K_2` have index 3. Fixing the binary quotient and these two ternary cosets fixes the third exception by its graph FD, because all its neighbours are among those variables and constants. Equivalently, intersecting `K_2` with the two ternary subgroups already gives `K`. Thus `s<=3*3=9`, contradicting `s=45`.

## The 288-state pattern 3,3,4

Let `A,B` be the two index-three subgroups and `C` the index-four subgroup; put `A_0=A∩K_2`, etc. Equation (7) gives `[K_2:A_0]=[K_2:B_0]=3` and `[K_2:C_0]=c` with `c` a power of 2 dividing 4. Because `m=288`, `s=m/2^t` is divisible by 9.

If `A_0=B_0`, then `K=A_0∩C_0`. Intersections of subgroups of coprime indices 3 and `c` have index exactly `3c`: their intersection index is a multiple of each index and at most the product. Hence `s=3c`, not divisible by 9, impossible. Thus `A_0!=B_0`.

The FD at the vertex of `A` forces it to be adjacent to both exceptional vertices. If it were not adjacent to `B`, then `C_0` would lie in every neighbour subgroup and hence in `A_0`, impossible because `[K_2:C_0]=c` is not divisible by 3. If it were not adjacent to `C`, then `B_0<=A_0`; both have index 3, contradicting `A_0!=B_0`. Its FD now yields `B_0∩C_0<=A_0`, hence `K=B_0∩C_0` and `s=3c`, again contradicting `9|s`.

## The 288-state pattern 3,3,3

The seven binary and three ternary singleton entropies give exactly `3 Delta=1` bit. For any two ternary variables `X_a,X_b`, the conditioned inequality says

\[
1+2I(X_a;X_b)\le\log_2 3.\tag{8}
\]

Their joint coset index divides 288, is a multiple of 3 and at most 9; it is therefore `3`, `6`, or `9`. The first two cases give mutual information `log2 3` and `log2(3/2)` respectively, both violating (8). Thus every ternary pair has joint index 9 and is independent. Each one- and two-ternary subgroup intersection has odd index, so it projects onto all of the binary quotient `Q`.

Every ternary vertex must be adjacent to the other two. If it had no ternary neighbour, its FD would force `K_2` into its subgroup, impossible because its intersection with `K_2` has index 3. If it had only one ternary neighbour, the FD would force that neighbour's index-three intersection with `K_2` inside its own; they would be equal, contradicting the pair's index 9 and full projection to `Q`. Hence the three ternary vertices form a triangle. R-minus is `K4`-free, so no binary vertex neighbours all three.

Now replace each subgroup by its image under `phi` and take the uniform quotient law on `Q`. The three ternary variables become constant; the seven binary characters are unchanged and span the dual of `Q`. The quotient law still satisfies all original FDs: at a binary vertex, at most two ternary neighbours occur, and their subgroup intersection projects onto `Q`; intersection with binary-neighbour subgroups (all containing `K_2`) commutes with projection. Ternary quotient variables are constant, so their FDs are automatic. The pinned conditioned inequality applied to a constant quotient variable gives `Delta<=0`, hence `t<=2*7/3` and so `t<=4`.

On the other hand, fix the binary quotient and any two ternary cosets. The remaining ternary variable is determined by its original FD, so `s<=3*3=9`. Since `288=2^t s`, this requires `t>=5`, a contradiction. The last surviving `m=288` case is impossible.

## Evidence and scope

The producer `frontier-20261028-coset-index-screen384.py` SHA-256 `f139e5700dbf9486cea8240f653b448eecdadb64ead565153787e42b1e04f76a`, receipt SHA-256 `17025c600d307a1df8d84bdb71be893f8f57906471882a3d04c4397f13f50a25`, checks the divisor, character-count, strict product and factorial-action conditions. Separately written multiset replay `frontier-20261028-coset-index-screen384-independent.py` SHA-256 `7c7e84af25fb2e5317898b7de5f36095cb92983d5b4cba8fe7458fd72326db63`, receipt SHA-256 `1d3c02beb157934766a0f180b904215626ad3de7549fe51108cc5d63a7a7eda5`, checks all 36 product-bound patterns and the 11 factorial survivors. The `m=192` graph/character exclusion and its independent replay are pinned in the preceding `288` packet. R-minus `K4`-freeness is independently checked in receipt SHA-256 `5994e7fbec78f4fa864e713438e28d9676a107bf4a5e66df9044fe3103863eb4`.

All finite checks use exact integers. The subgroup, entropy and quotient deductions are written mathematics, not a proof-assistant formalization or independently completed scientific review. The genuine unrestricted guessing-number question remains open.
