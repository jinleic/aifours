# Parent disposition - PH7 at z = 8/9: the supported 3+1+3 chain family is obstructed for every u > 0 (f8)

Observed native clock before writing: **2026-10-28T17:28:42-0700 PDT**. Same-harness written support with exact rational checks; not formal/kernel, human, configured-family or novelty acceptance. Frontier-first direction: [contract addendum 2](../contract-addendum-2-frontier-first-owner-direction-v1.json).

## Complete reads by Main

| Input | SHA-256 | LF | Read |
|---|---|---|---|
| Candidate `frontier-20261028-ph7-three-chain-critical-obstruction.md` (MathResearch96h-2) | `d231c72575c414d0891269e536100c05388896cfd8ce8a4325b50de07a37e817` | 145 | raw 1-145 through ending |
| Review `frontier-review-f8-ph7-three-chain-v1.md` (PhysicsRQLS10-2) | `13eff7c715012a34cbccd49930babf12f8dc3871af3be0115a5ca8e39bb7dd9d` | 163 | raw 1-163 through ending |
| Assignment `review-waves/f8-ph7-three-chain/assignment-v1.json` | `526a668d88aa8991e7e20409ddb6bf14abbf47a810f8fb02579aec1a549f7eba` | 22 | frozen before dispatch |

## Adopted statement (exact scope)

For the registered H_(1,2) target normalized to d = 1, y = s + c, D_z(y) = y[(y+1)² + z]², consider the actual seven-state family with upstream Jordan chain J_u (free rate u > 0), one center with holding w, downstream chain J_1, backward entries D_1, D_2, D_3, last-to-center feedback phi, input beta = (C, B, 1, 0, 0, 0, 0) and exit K e_7, realized by a positive diagonal similarity. Coefficient matching of det(yI - G) = D_z(y) Q(y), Q = (y+u)² + B(y+u) + C = y² + py + q, forces w = p + 4 - a, q = (a-4)p + h0 - 2z, Lp = N and the displayed phi formula (a = 3u+3, b = 3u²+9u+3, c3, e4, h0, L, N as in the candidate). **Theorem.** At z = 8/9 no u > 0 admits B >= 0, C >= 0 and phi >= 0 simultaneously (necessary for alpha >= 0 and a Metzler generator under positive diagonal similarity); the singular branch L = 0 admits no coefficient match. Hence no positive-diagonal normalization of this chain is a critical-ratio PH7 realization. Moreover there is some open z-neighbourhood of 8/9 (width not evaluated) on which the same obstruction holds uniformly for all u > 0.

## Parent verification

Main checked by hand the algebraic structure Q = y² + py + q with p = 2u + B, q = u² + uB + C (so B, C >= 0 and u > 0 give q > 0), the inference chain qL = Q_*(u) > 0 => L > 0 and -243 L phi = P_*(u) > 0 => phi < 0, and the L = 0 exclusion via N = ((8u-1)/3) L + (110u-103)/27 (u = 103/110 gives L < 0). Main independently verified, with exact Fraction arithmetic in the parent kernel at ten rational points (sufficient for degree <= 6 polynomial identities), that with the candidate's explicit coefficient definitions at z = 8/9: L = 3u² - 3u - 7/9, N = 8u³ - 9u² + 3u - 32/9, (a-4)N + (h0-2z)L = Q_*(u) and the cleared -243 L phi expression equals P_*(u); the remainder identity also holds. All printed Bernstein coefficients and tail coefficients are strictly positive (read); the reviewer independently recomputed the symbolic 7x7 determinant, the beta-adjugate numerator, every Bernstein list and both tails with newly written exact polynomial code (PASS), and reconstructed the compactification/uniform-continuity neighbourhood argument. Reviewer verdict NO_SUBSTANTIVE_DEFECT, 0F/0M/0m.

## Not established

Any all-topology PH7 exclusion at 8/9; the exact minimum order at 8/9; a numerical width of the obstruction neighbourhood; the earlier PH6 boundary and earlier PH7 band results (historical context, not re-verified here); novelty (NR). The lane's later explicit PH7 constructions (bands up to 41/50 and the algebraic endpoint zeta) are separate candidates under review.
