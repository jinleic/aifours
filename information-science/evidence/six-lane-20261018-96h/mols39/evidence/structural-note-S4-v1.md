# Structural note S4 — mod-3 lifting of known difference matrices with 3 || n (2026-10-19T04:03:12-0700, ContinueCFR21)

Status: exact stdlib measurements on KNOWN objects (no search, no candidate possible); interpretation is the worker's,
UNREVIEWED. Probe code/probe_mod3_lift_v1.py sha256 535831250d79f9a802ec8caca597de4c61bae82f21392e0635b05dd226e87c9b; runs evidence/runs-s4/* under owned_supervisor_v2 + shim
+ fresh gate (initial scope: contract-v1.json 55baff0c… resources.initial_go); stdout sha256
S4a fd06bafb8dafa5ff2bd070e1d589cfecd20079227e0f7103eaedb27df47ddce5, S4b cc2c7ef5034ddb4c271605525c39efeaaac591ab471993b11db0054a647b0112.

## Statement used (elementary; proof in the probe docstring)
n = 3q, gcd(3,q) = 1, D normalised at row r. Skeleton beta = D mod q, lift alpha = D mod 3. D is a DM iff for every
pair x<y and t in Z_q the fibre T_xy(t) = {c : beta_x(c) - beta_y(c) = t} has exactly 3 columns and alpha_x - alpha_y
is a bijection on it. Three elements of Z_3 are distinct iff their sum is 0 and two given ones differ. So the lifts of a
fixed skeleton are the points of the GF(3)-space V(beta) (fibre sums zero, A_r = 0) at which one linear functional per
fibre is nonzero. Row constants always lie in V and preserve the rainbow property (dimension k-1).

## Measurements (all: DM check passed, true alpha in V and rainbow, no fibre functional vanishes on V)
| object | n | k | rank / unknowns | dim V | m = dim V-(k-1) | functional rank | rainbow points mod constants |
|---|---|---|---|---|---|---|---|
| anchor_sage_dm39_k6 | 39 | 6 | 185 / 195 | 10 | 5 | 5 | 2 |
| sage_dm21_k6 | 21 | 6 | 93 / 105 | 12 | 7 | 7 | 2 |
| p21_sol1_k6 | 21 | 6 | 93 / 105 | 12 | 7 | 7 | 2 |
| sage_dm33_k6 | 33 | 6 | 154 / 165 | 11 | 6 | 6 | 2 |
| sage_dm51_k6 | 51 | 6 | 243 / 255 | 12 | 7 | 7 | 2 |
| singer57_k8 | 57 | 8 | 383 / 399 | 16 | 9 | 9 | 4 |
| singer57_k7_rows0to6 | 57 | 7 | 328 / 342 | 14 | 8 | 8 | 4 |

Objects: Sage DM_39_6_1 (the anchor), Sage DM_21_6_1, DM_33_6_1, DM_51_6_1, the earlier-round P21 six-row DM, and a
Singer-type (57,8;1)-DM built in the probe from the planar difference set (1,6,7,9,19,38,42,49) and an OA(8,8) over GF(8)
(Sage's DM_57_8_1 recipe with an OA built here; its DM property was checked) plus its first seven rows.

## Reading (scoped)
1. For every measured object the linear relaxation is tiny: m in {5,...,9} against 105-399 unknowns, and the rainbow
   lifts of the skeleton are exactly +-alpha (six-row objects) or 4 points (= two sign pairs) for the Singer object.
   So for these DMs the mod-3 part is determined by the mod-q skeleton up to sign and row constants.
2. Consequently the naive independence heuristic "expected lifts ~ 3^dim V (2/3)^#fibres" is not informative (it would
   predict ~1e-30 for the anchor); the rainbow events are strongly correlated with the skeleton.
3. Use for this lane: a fast exact lift test (Gaussian elimination + 3^m enumeration, < 0.1 s per skeleton in stdlib) and
   a candidate algorithm split for any future extension search (enumerate mod-13 balanced rows, then solve GF(3)).
   It gives no construction and no statement about the existence of a seven-row DM over Z_39.
