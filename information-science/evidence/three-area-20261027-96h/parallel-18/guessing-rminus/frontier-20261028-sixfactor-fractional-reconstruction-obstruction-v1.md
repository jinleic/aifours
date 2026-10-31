# Fractional universal-reconstruction covers also fail in all seven residual cases

**Status: exact rational LP primal/dual identities with separately checked allowed-difference masks; scientific review pending.** In each of the seven six-factor two-syndrome cases left by `frontier-20261028-two-syndrome-distance5-v1.md` SHA-256 `606e74ea5d7ede9580c217091e240663641d23d43141ac9db49c5b753b0a38df`, not only a single universal three-coloring but also the natural **fractional universal-reconstruction cover** method fails to prove the `2/3` entropy bound.

Let `D_J` be the exact family of vertex supports of all nonconfusable mixed-space differences having syndrome zero or all-one on the six selected factors. A vertex set `I` is `D_J`-free when no member of `D_J` is contained in `I`. Exactly for such an `I`, the complement `V\I` reconstructs every possible FD-consistent two-coset support: if a difference support is contained in `I`, the two-word FD support `{0,d}` is a counterexample to reconstruction; otherwise projection to the complement is injective.

For weights `w_I>=0`, the fractional cover LP is

\[
\min\sum_I w_I\quad\text{subject to}\quad
\sum_{I\ni v}w_I\ge1\quad(v=1,...,10).
\]

An objective at most 3 would let one average the valid inequalities `H(X_V)<=sum_{v notin I} H(X_v)` to obtain the desired two-thirds singleton-entropy bound. In the seven residual cases the exact optimum is **strictly larger**:

| Varying factor set | Exact fractional-cover optimum |
|---|---:|
| `{1,2,5,6,8,9}` | `10/3` |
| `{1,3,4,6,7,10}` | `7/2` |
| `{2,3,4,6,7,10}` | `10/3` |
| `{1,3,4,7,8,10}` | `10/3` |
| `{2,3,4,7,8,10}` | `7/2` |
| `{2,3,5,6,9,10}` | `7/2` |
| `{1,3,5,8,9,10}` | `7/2` |

The certificate includes positive rational primal covers and nonnegative rational vertex weights `y_v` with `sum_v y_v` equal to the displayed objective and `sum_{v in I}y_v<=1` for every `D_J`-free set `I`. Weak duality proves optimality exactly; no floating solver status is used.

The obstruction is deliberately narrow: reconstruction sets might be chosen **after** fixing a particular support, or another entropy inequality/tensorization may succeed. These LPs do not imply a strict-gap law or any impossibility result for the seven cases.

Evidence: `frontier-20261028-sixfactor-fractional-cover-certificates-v1.json` SHA-256 `6caf5532b3c8c2eb74401afc39e669372ec618e8806c97242bafa056c0d4f77e`; exact checker `frontier-20261028-sixfactor-fractional-cover-check.py` SHA-256 `d69bfcaa9785e0ddb55ac77aa67e7b87f676b8eb565ef28d4b38ed34ba3ae581`, receipt SHA-256 `81bf6ad105765a31795f30a38affac4ca67188ce12ce090066cb88437136abae`. It pins the Möbius and independent direct-difference replays, checks all 1,024 vertex subsets per case, primal coverage and dual bounds, equality of objectives and a changed-dual mutation. No proof-assistant formalization or independent scientific review has been performed.
