# Strict uniform group-coset gain requires at least 432 effective states

**Status: WRITTEN with independently replayed exact arithmetic; conditional on pinned graph-FD and rank certificates and earlier coset gates; scientific review and novelty clearance pending.** For a uniform finite-group coset law `X_i=gH_i` satisfying the original R-minus FDs, write `K=intersection_i H_i` and `m=[G:K]`. If the entropy-balance gap `Delta>0`, then

\[
\boxed{m\ge432.}
\]

This strengthens the `384`-state obstruction `frontier-20261028-uniform-coset-384-barrier-v1.md` SHA-256 `6e07abb00a8b9f271fe6d9b9a05f7a68354e17ab9d94a9335dd14461fb038bc8`. It excludes uniform coset witnesses on groups of order at most 431, but makes no claim about nonuniform coset laws, arbitrary FD laws, attainability, or the unrestricted guessing number.

## Necessary arithmetic and remaining indices

The earlier `384` packet pins the original conditioned Shannon/FD inequality, the linear-rank bound, the no-duplicate-index-two condition, factorial-action divisibility, and the two-exception subgroup intersection condition. Write `d_i=[G:H_i]` and `P=product_i d_i`. In addition to `m^3>P^2` for strict balance, the conditioned inequality gives

\[
m^3\le (\min_i d_i)P^2,\tag{9}
\]

because `3 Delta<=min_i H(X_i)=log(min_i d_i)` under the uniform coset law. Applying (9) together with all the preceding exact necessary conditions to every `384<=m<432` leaves exactly

| `m` | index-two vertices | nonbinary indices |
|---:|---:|---|
| 384 | 6 | `3,3,3,4` |
| 384 | 7 | `3,3,6` or `3,4,4` |

Two separately written exact enumerators agree on these three patterns. All are ruled out below.

## Patterns 3,3,3,4 and 3,3,6

In both patterns direct entropy arithmetic gives `3 Delta=log2(32/27)` bits. Choose an index-three subgroup `A` and another index-three subgroup `B`. Their joint coset index divides 384, is a multiple of 3 and at most 9; since 9 does not divide 384 and equal subgroups are forbidden by the conditioned inequality, the joint index is 6. Thus `I(X_A;X_B)=log2(3/2)`.

For pattern `3,3,3,4`, choose a third index-three subgroup `C`; the same reasoning gives `I(X_A;X_C)=log2(3/2)`. For pattern `3,3,6`, choose the index-six subgroup `C`. Its joint index with `A` divides 384, is a multiple of 6 and at most 18. The value 6 would make `H_C<=H_A` and the index-six coset determine the index-three coset, forbidden by the strict-gap inequality; 18 does not divide 384. Thus the joint index is 12 and again `I(X_A;X_C)=log2(3/2)`.

In either case,

\[
3\Delta+2I(X_A;X_B)+2I(X_A;X_C)
=\log_2(32/27)+4\log_2(3/2)=\log_2 6>\log_2 3=H(X_A),
\]

contradicting the conditioned inequality at `A`.

## Pattern 3,4,4

Let `A` have index 3 and `B,C` index 4. Let `K_2` be the intersection of the seven index-two subgroups, `Q=G/K_2`, `|Q|=2^t`, `K=intersection_i H_i`, and `s=[K_2:K]`. For `H`, put `H_0=H∩K_2` and let `phi(H)` be its image in `Q`. Since `m=384=2^7*3`, `s` is divisible by 3. The index formula

\[
[G:H]=[Q:phi(H)]\,[K_2:H_0]
\]

shows `[K_2:A_0]=3`, while `c_B=[K_2:B_0]` and `c_C=[K_2:C_0]` are powers of 2 dividing 4.

The original FD at `A` gives `K_2∩B∩C<=A`: this intersection is contained in every binary neighbour subgroup, and includes both other exceptional subgroups whether or not they are neighbours. Consequently `K=B_0∩C_0`, and `s=[K_2:B_0∩C_0]` is divisible by both `c_B,c_C` and at most their product. As `3|s`, the only possible choice among powers `1,2,4` is

\[
c_B=c_C=4,\qquad s=12,\qquad t=5.\tag{10}
\]

Hence all three exceptional subgroup images are all of `Q`. Their pairwise intersections also project onto all of `Q`: for `A,B` and `A,C`, global and internal intersection indices are both 12 by coprimality of 3 and 4. For `B,C`, the internal intersection is `K` of index 12, while its global index is at most `4*4=16` and is the internal index times a power of 2, so it too is 12.

The three exceptional vertices form a triangle. The FD at `A` forces it to neighbour both `B` and `C`: if it missed, say, `B`, then `C_0<=A_0`, impossible because `[K_2:C_0]=4` is not divisible by `[K_2:A_0]=3`. If `B,C` were nonadjacent, the FD at `B` would force `A_0<=B_0`, impossible because index 3 is not divisible by index 4.

R-minus is `K4`-free, so no binary vertex neighbours all three exceptional vertices. For any binary vertex, the intersection of its at most two exceptional neighbour subgroups projects onto all of `Q`; intersecting with binary-neighbour subgroups commutes with projection because those contain `K_2`. Therefore the uniform quotient variables satisfy the same graph FDs. The three exceptional quotient variables are constant, while the seven binary characters are nonconstant and span `Q`. Their quotient law has joint entropy `t=5` bits and singleton sum 7 bits, so its balance gap is `5-14/3=1/3>0`. This contradicts the pinned proper-subgraph inequality, which forces `Delta<=0` whenever any original vertex is constant. Thus pattern `3,4,4` is impossible.

## Exact evidence

Arithmetic producer `frontier-20261028-coset-index-screen432.py` SHA-256 `0d1b3cdd82194dad5ecca05d4454fde7eddc2a3f61885da54956df1913bd437c`, receipt SHA-256 `fd8bce56db370e6006510ef1edf40aa89aff9fbcf028c8b3e4ac42f7f249af84`; independent recursive replay `frontier-20261028-coset-index-screen432-independent.py` SHA-256 `6e6141b6b81f7dc354c4296237c3867808a2213b5ad2e30fb0aa20c19a4cff1b`, receipt SHA-256 `e8fe214fedbbc2d9f5355ebf9567a5b5a52ab16dc73f8dcbdfd7cc69ac2a8eb0`. The independent check verifies all 14 strict-and-conditioned product patterns, the three survivors, and a changed-survivor control. Earlier graph and character checks are pinned in the preceding packet.

The group/entropy deductions are written mathematics; no independent scientific review, proof-assistant formalization, or novelty clearance has yet been completed.
