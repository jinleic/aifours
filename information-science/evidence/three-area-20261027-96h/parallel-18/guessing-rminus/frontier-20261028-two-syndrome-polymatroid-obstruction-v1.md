# An exact Shannon-level obstruction for the two-syndrome route

**Status: WRITTEN-CHECKED-IN-KERNEL; independent scientific review pending.** For each of the four factor-preserving representatives of the seven distance-six residual two-syndrome cases, the following natural necessary conditions for an actual reduced FD law admit an exact rational polymatroid with **positive** entropy-balance gap. Consequently these conditions and Shannon inequalities alone cannot establish `Delta<=0` in any of those four cases. This is an obstruction to the specified proof method, **not** an entropic law, a guessing strategy, a strict-gain witness, a full-copy LP point, or a proof of any optimum.

## The tested necessary conditions

For one chosen six-triangle set `J`, let `X_1,...,X_10` be the corresponding vertex blocks and let the common binary syndrome selector be `S`. Each selected triangle has the same syndrome bit `S` after an affine translation of its two allowed syndrome classes. Set `k_i` to the number of triangles of `J` containing vertex `i`, and for `A` a vertex subset let

\[
r_J(A)=\sum_{T\in J}\min(|A\cap T|,2).
\]

The precise outer relaxation consists of:

1. All elemental Shannon inequalities on the eleven coordinates `X_1,...,X_10,S` and `h(empty)=0`.
2. The ten original graph FDs `H(X_i|X_{N(i)})=0`; `H(S|X_{N(i)})=0` for every `i`; and `H(S|X_T)=0` for every `T` in `J`.
3. `H(S)<=1`, `H(X_i)<=k_i`, and `H(X_A|S)<=r_J(A)` for all nonempty `A`.
4. The previously pinned syndrome gate `3 Delta+2 sum_i I(X_i;S)<=3 H(S)`, equivalently `3H(X_V)+17H(S)-2 sum_i H(X_i,S)<=0`.

All are necessary for an actual two-class law: every `i` lies in a selected triangle, so its original decoder makes `S` a function of its neighbours; on a fixed syndrome, each factor projection has at most `2^min(|A intersect T|,2)` possible values, giving the stated rank cap. Nothing here assumes an actual distribution exists for a polymatroid satisfying them.

## Four explicit rational countermodels

| factor representative `J` | checked positive `Delta` | checked `H(S)` |
|---|---:|---:|
| `1,2,5,6,8,9` | `9/142` | `9/142` |
| `1,3,4,6,7,10` | `48/1301` | `48/1301` |
| `2,3,4,6,7,10` | `5/102` | `5/102` |
| `2,3,5,6,9,10` | `11/228` | `11/228` |

The syndrome gate and nonnegativity of mutual information imply `I(X_i;S)=0` for every `i` in each countermodel. This is a statement about the **abstract polymatroids only**, not a constructed FD law. It explains why the natural condition `sum_i I(X_i;S)>=3H(S)/2` cannot be deduced from this relaxation.

Numerical proposals were obtained by the symmetry-reduced LP `frontier-20261028-two-syndrome-symmetric-lp.py` SHA-256 `144f4f27770b3054767ad1e979fff194ad2075a1b2695f43a09db2a5d4ee981d`, result SHA-256 `82c2f65850380925bc4ecf76384c1b2e394f23e62aeffdfea7f8d548dcaccc3f`. The independent checker `frontier-20261028-two-syndrome-polymatroid-check.py` SHA-256 `b90b5d3cbacc6c4b5f1f30342ba5dc4acd5cb7fa37b8e1367950946e5ed54538` rationally reconstructs every coordinate and checks all 28,160 CMIs, 11 elemental monotonicity rows, ten graph FDs, ten neighbourhood-syndrome FDs, six selected-triangle syndrome FDs, 1,023 conditional projection caps, ten actual vertex caps, the binary cap, the syndrome gate and the positive objective in each case. Receipt SHA-256 `975f5b8222bffc37630b0aa93e64676202e82042301a0e87c24d7abc7874affa` includes an intended negative control. The exact inequalities are checked independently of the numerical solver's optimum report.

The checked automorphism-orbit receipt `frontier-20261028-sixfactor-residual-orbits-check-result.json` SHA-256 `ba3ce740c83ba989871e3d3f5bbc57deee864df3c4a9426bc8b93c7cf713e8e4` maps these four cases to all seven six-factor residual sets. Additional actual-bit, non-Shannon, support, or weighted-min-cut information may still settle the branch; the obstruction does not show that such approaches fail. Scientific review, formalization and novelty clearance are not claimed.
