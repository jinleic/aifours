# Universal entropy bound for 206 four-factor syndrome planes

**Status: WRITTEN with independently replayed exact finite color certificates; scientific review pending.** In the q=8 binary triangle-factor encoding of R-minus, let a joint original-neighbour FD law have its ten-bit syndrome support contained in an affine binary two-plane whose varying factor set has size exactly four and covers all ten graph vertices. There are 247 such direction planes. For **206 explicitly listed planes** in `frontier-20261028-three-syndrome-fourfactor-color-screen-result.json` SHA-256 `218c42798aa317236225f99e5b03f2cd6bd87c21cbaeb606ebdb54b53d1ac7a8`, every such law satisfies

\[
\Delta(X)\le0.\tag{59}
\]

The law may use any subset of the entire four-syndrome affine plane and arbitrary probabilities; this is stronger than a three-syndrome-only statement for the listed planes. A uniform support has at most `2^20` words. The remaining **41** planes have no supplied universal color in this screen, but no assertion that they lack a color, law, or no-gap proof is made without a separate exact nonexistence certificate. This result is not an unrestricted q-ary or general guessing-number bound.

## Exact reconstruction argument

Write `J` for the four varying factors and condition on the six fixed-syndrome factor tuples. The selected four-factor blocks remain an original-neighbour FD law on each fiber, with only eight binary and two quaternary vertex alphabets. Every difference of two selected-block words has syndrome in the four-element plane `P={0,a,b,a xor b}`. A nonzero word difference of any FD support must have, at every active vertex, at least one active original neighbour. The independently verified finite census lists **all** active vertex masks that can occur with a difference syndrome in `P`, subject only to that necessary graph condition.

For each of 206 planes the certificate assigns one of three colors to each of the ten vertices such that no allowed nonzero difference mask is contained in one color class. Therefore every pair of color-class tuples determines the full selected-block word: two words equal on those two classes could differ only inside the third, contradicting the color certificate. Three pairwise entropy subadditivity inequalities yield

\[
H(Y_V)\le\frac23\sum_{v=1}^{10}H(Y_v)
\]

on each conditional fiber, for **arbitrary** laws and without assuming uniformity, factor independence or maximality. Process the six fixed-parity triangle factors first; each separately has nonpositive balance gap under arbitrary conditional correlations. The usual conditional tensorization then lifts the mixed-block inequality to the original ten q=8 vertex triples.

## Exact evidence

Producer `frontier-20261028-three-syndrome-fourfactor-color-screen.py` SHA-256 `1d293de0cf066bd1d7ad3c25a6797625c4905fae3808edbc2bb90ebf10833322` enumerates all 19 four-factor vertex covers and all 13 full-support two-dimensional planes on each, with color proposals. Independently written `frontier-20261028-three-syndrome-fourfactor-color-check.py` SHA-256 `dbb4a6f3b73387d15ddda8b68d824a87906fc1f694cbde3f437d4a23c90cbf0d`, receipt SHA-256 `87b6d473e68795c3c6710d642d9a7de4fd03f9fed2378aecb2db216d878e1ea9`, reconstructs all factor-local triples and 147,825 allowed mask entries across the 247 planes, checks all 206 supplied colors, validates coverage and rejects a monochromatic-color control. The program does not certify nonexistence of colors for the other 41 planes. This argument does not use the repaired two-syndrome theorem. Written entropy lifting, graph semantics, novelty and scientific review remain separate obligations.
