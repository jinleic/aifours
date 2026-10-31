# Parent disposition - two-horizontal-node chain: simultaneous-lowering injectivity at (1,1,n) and graded Serre equality on the {0,1}² horizontal slice (f13)

Observed native clock before writing: **2026-10-28T17:30:37-0700 PDT**. Same-harness written support conditional on two named prior parent inputs and the PBW import; not formal/kernel, human, configured-family or novelty acceptance. Frontier-first direction: [contract addendum 2](../contract-addendum-2-frontier-first-owner-direction-v1.json).

## Complete reads by Main

| Input | SHA-256 | LF | Read |
|---|---|---|---|
| Candidate `frontier-20261028-two-horizontal-chain-theorem-v1.md` (MathKacMoody-2) | `d3cf1666c9b7eac84bc052da6af932c3199c878faaca717dcb987ac85109ec67` | 193 | raw 1-100 and 100-193 through ending |
| Review `frontier-review-f13-kacmoody-horizontal-chain-v1.md` (MathSemigroup-2) | `e09d6db77b22709092ac7ff079ff7eec49a0e61dadd424648ed4368509f2efd2` | 106 | raw 1-106 through ending |
| Assignment `review-waves/f13-kacmoody-horizontal-chain/assignment-v1.json` | `339d019d535342cba3c883999410245db69994414cba3deaa88056602865786f` | 22 | frozen before dispatch |

Imports carried at their exact prior scopes (not re-reviewed here): I1 full-Cartan grading/ideal splitting/first-defect parent (`08217c89...`), I2 free positive source and Serre-ideal transport parent (`f08daf3e...`) with the PBW normalized-transcription qualification (`21b5b074...`).

## Adopted statements (exact scope)

For every r, s >= 1, every full complex Cartan realization of A(r,s) = [[2,-1,-1],[-1,2,-1],[-r,-s,2]], with X_k = (ad e3)^k e1, Y_l = (ad e3)^l e2, V_k = [X_k, Y_{n-k}], U_j = [X_j, Y_{n-1-j}]:

1. At degree (1,1,n), n >= 1, the actual Serre quotient has basis the classes of V_k for max(0, n-s) <= k <= min(n, r) (zero space if empty), and the simultaneous simple-lowering map has zero kernel: f3 alone is injective when s < n, or when s >= n and r < n; the pair (f1, f3) is injective when r, s >= n. Formulas: [f3, X_k] = k(r-k+1) X_{k-1}, [f3, V_k] = k(r-k+1) U_{k-1} + (n-k)(s-n+k+1) U_k, [f1, V_0] = (n+1) Y_n, [f1, V_1] = -Y_n, [f1, V_k] = 0 for k >= 2.
2. Reached-target correction at (1,1,n): Δ(G_C)_α ∩ ⊕_i J_{α-ε_i} = Δ(J_α), with j = x itself as the common correction.
3. J_(a,b,n) = τ_(a,b,n) for every nonzero positive degree with a, b in {0,1} and n >= 0 (all r, s, full C), by the minimal-height argument over the lowering-closed slice with all boundary degrees ((1,0,n), (0,1,n), (1,1,0), (0,0,n)) paid.

## Parent verification

Main reconstructed by hand: the Serre seeds fitting degree (1,1,n) are exactly X_{r+1} and Y_{s+1}; the ideal spans (X-seed descendants are V_k with k >= r+1, Y-seed descendants V_k with n-k >= s+1); the leading tensor word e1 e3^k e2 e3^{n-k} of V_k with coefficient (-1)^n (independence); the induction [f3, X_k] = k(r-k+1) X_{k-1} via [f3,[e3,X_{k-1}]] = -[h3, X_{k-1}] + [e3,[f3,X_{k-1}]] and [h3, X_{k-1}] = (-r + 2k - 2) X_{k-1}; the f1 formulas ([f1,X_1] = [e3, -h1] = -e3, [h1, Y_n] = -(n+1) Y_n); and all three kernel cases including the U_0 row n(s-n+1)c_0 + r(n+1)c_0 = 0 in Case III and the positivity of every elimination factor. Reviewer verdict NO_SUBSTANTIVE_DEFECT, 0F/0M/0m, with a standalone tensor-word/rational-elimination program (no author code) confirming 3430 formula identities and claimed ranks for n, r, s <= 7 (finite range only).

## Not established

The remaining level-4 horizontal degrees outside {0,1}² (the separate level-4 rectangle certificate is under review f28), the full original band/conjecture, the five-source 3->5 invariant, I1/I2/PBW themselves, novelty (NR). Historical held episodes for this slot remain historical records, not premises.
