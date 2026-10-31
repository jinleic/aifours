# No Fourier-product transversal for a continuous order-eight Diţă family

**COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 21:35:56 PDT 2026**. This attacks the even-order question with ARBITRARY interblock complex phases rather than a root-order filter. It does NOT classify all order8 complex Hadamards and is not a universal even-order theorem or order10 no-go.

## 1. Exact scope

Let `i=zeta8²`. For a∈{0,1}, t,b∈{0,1,2,3}, any permutation mu of Z4, and arbitrary unit complex phases delta_t, define

`K_((a,t),(0,b))=i^(t b)`,
`K_((a,t),(1,b))=(-1)^a delta_t i^(mu(t) b)`.

This K is Hadamard: each within-group inner product is the 4-point Fourier sum and cross-group terms cancel between a=0 and1. Take ANY ordering of its eight source rows as physical coordinates and form the ordinary order8 Fourier-product QLS. **Claim:** it has no orthogonal transversal, even with repeated rays. Arbitrary K row/column phases and column permutations are harmless common-coordinate unitaries and cell phases/relabelings; arbitrary source-row order is explicitly enumerated.

This contains the Fourier4/Fourier4 2×4 Diţă deformation with ALL four unit phases, all independent Fourier row permutations mu and physical row orders. It does NOT include arbitrary one-parameter 4×4 Hadamard blocks A,B or every BH(8,8); those are outside the claim.

## 2. Exact finite reduction

A transversal assigns each of the eight K columns a different physical row. Cyclic physical-coordinate rotation places source `(a,t)=(0,0)` at coordinate0 without changing Gram orthogonality; a common physical row shift puts column `(0,0)` in physical row0. Subtract mu(0) and divide delta_t by delta_0 using column phases. Thus without loss the exact census has

- `O[0]=0`, with all **5040** permutations of the other source rows;
- `R0[0]=0`, with all `7*6*5=210` injections for the other h=0 columns;
- all permutations of the four remaining physical rows for h=1;
- `mu(0)=0`, with all six permutations of its other values.

For either h separately, the six within-group transversal inner products depend only on O, its assigned rows and the appropriate t-map, not on delta. Their zeta8 sums are checked exactly in the integer basis `1,zeta8,zeta8²,zeta8³`. Among 5040*210 initial assignments, **6016** pass the h=0 equations; extending over all h=1 row assignments and all six mu gives exactly **113664** branches passing BOTH within-group constraints.

For each surviving branch, every cross-group inner product is a linear homogeneous equation in the SAME four delta variables. With `tau(a,t)` the physical coordinate occupied by source `(a,t)`, its 16×4 coefficient matrix is

`C_(b,c;t)=i^(mu(t)c-t b) * [zeta8^((R1(c)-R0(b))*tau(0,t)) - zeta8^((R1(c)-R0(b))*tau(1,t))]`.

A genuine transversal requires `C delta=0` and `|delta_t|=1` for ALL four t.

## 3. Exhaustion by exact modular certificates

Use the prime `p=65521` and root `w=57852`; integer-only `frontier-20261028-n8-dita-prime-check-v1.py` SHA **11533f22400d08f18c3d130875cef54aa548526dc803b0aefd4f2cafce751d19**, result SHA **ed07ae081920c32c91e36e0f34cba3f0cf48651342d4654d0950815401977ab2**, checks divisibility through isqrt(p)=255, `w⁴=-1`, and conjugate root `w^(-1)=8031`. Evaluation `zeta8 -> w` is therefore a ring homomorphism from Z[zeta8] to F_p.

C++ exact census `frontier-20261028-n8-dita-allphase-rank-v1.cpp` SHA **f251ccdd4cbf63ca11ed0ddff9e3a26755d8abc04f60c0299cb51f61dcec1f7c**, result SHA **3d695347636f7c0ad00d59bf4eed7d120948416c229961805178de244d6f4e0b**, finds modular rank4 for **105472** branches. Their 4×4 minors are nonzero algebraically, so no nonzero delta solves them. The remaining **8192** rank3-mod-p branches are in JSONL SHA **2a24d7bda8184ecca5ea31f9a60b63ef1eda2a487a77b01ddd24f1ea940478c6**.

For each remaining branch, select three rows independent modulo p, form the four signed 3×3 cofactors v_t over Z[zeta8], and evaluate `v_t*conjugate(v_t)` by evaluating the same cofactors at w and w^(-1). If the exact complex C had rank4 there is no nonzero delta. If it had rank3, these cofactors form a nonzero kernel vector and every unit-phase kernel vector would be proportional to it, so ALL four exact squared magnitudes would agree. On **all8192** branches at least two cofactor norm residues differ; equality in Z[zeta8] would imply equality after reduction, so none admits a unit-phase kernel. The no-survivor checker SHA **7588e3fde65d13318a98f10471e0b56bc69441c6a35ab0209837be29e82b1f6d**, result SHA **3e4267692a40b4a944839eea69f89b2880f9dc8eb3a0c1a7de9d5e31dd856d0f**, implements that step.

A separately written full-regeneration replay `frontier-20261028-n8-dita-allphase-replay-v1.py` SHA **0aa8b669c172dd2fce523f2d2acbb2f2e2a8adf49762fd7cda7df37169bb97fb**, result SHA **ad4623e554d8818b339bd8428bae429e56f64d496e6ee32a561b25db03ae32b9**, reconstructs the SAME entire normalized search without reading the producer's branch list and obtains 5040,6016,113664,105472,8192,0 unresolved. Its primality-bound expression uses a floating square-root only for the small trial-loop endpoint; the separately pinned integer-isqrt check above independently establishes the prime without floats. Both replays use the same prime and mathematical caller; neither is a formal proof or external-model review.

## 4. Limits

This is an exact finite certificate of a restricted CONTINUOUS family, not a failed numerical search or an extrapolation from discrete phases. It is not an exhaustive no-go over arbitrary 4×4 sub-Hadamards, arbitrary 8×8 K, other even n, or the original QLS10. Normalization, enumeration completeness, finite-field reduction, cross equations and both implementations require independent full review before adoption.
