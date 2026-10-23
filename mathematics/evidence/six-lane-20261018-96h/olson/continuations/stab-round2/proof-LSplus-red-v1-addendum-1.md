# Addendum 1 to proof-LSplus-red-v1.md: case (alpha) with a = -1 is impossible for p >= 10e - 13

Owner OlsonSTABSuccessor.  Written after /bin/date 2026-10-19T06:12:31-0700.  Status: CANDIDATE [W], UNREVIEWED.  Applies to proof-LSplus-red-v1.md
(166fbac828e7e55a8f2139648930c82c5df1e8823bf9d8c4f84daf36086b4c27); same dependencies; no new import.  Consequence: for e >= 3 and p >= 10e - 13, LS+(p, kappa) is reduced to excluding
case (alpha) with a = -1/2 (U' mostly involutions).  LS+ is NOT claimed.

## Setting
Y, g, delta0 <= 3e - 4, U, Z0, U', delta' >= 1, S', E' as in Theorem LS+-RED (A), (B), with a = -1: every u in U' is = -x_u (mod p) and
delta' + E' <= 2e - 2 (so E' <= 2e - 3).  n1 := number of u in U' with x_u = 1 (copies of -g, mu = p - 1); n1 >= |U'| - E' >=
p - 3e + 2 + delta' - E' >= p - 5e + 6.  (F*): every W <= U with rho(W) <= e - 1 has |W| + 2rho(W) <= delta0 - 1 (|W| <= r <= p - 2).
Assume p >= 10e - 13 (this also gives p >= 9e - 13 and n1 >= 5e - 7).

## Step 1 (Z0 terms are small)
For z in Z0 let zeta_z in [1, p - 1] be its residue.  Suppose zeta_z <= S'.  If zeta_z > n1, W := {z} u W' with W' <= U' of x-sum zeta_z has
residue 0 and |W| >= 1 + zeta_z - E' >= 2 + n1 - 2E' + E'... precisely |W| >= 2 + n1 - E' >= p - 7e + 11 >= delta0: against (F*).  So
zeta_z <= n1, and W := {z} u (-g)^(zeta_z) has residue 0 and |W| = 1 + zeta_z; (F*) gives zeta_z <= delta0 - 2.  Call such z positive,
z~ := zeta_z in [1, delta0 - 2].  Otherwise zeta_z >= S' + 1: z negative, z~ := zeta_z - p in [-(p - 1 - S'), -1] <= [-(3e - 4), -1].
For Z'' <= Z0, zeta~(Z'') := sum of z~ (an integer = sigma(Z'') mod p).
## Step 2 (positive part)  T1 := max(e - 1, delta0 - e) <= 2e - 3.  The positive z~ sum to <= T1 - 1.
Else add them one at a time; the first partial sum zeta~ >= T1 is <= T1 + delta0 - 3 <= 5e - 10.  For that Z'',
W := Z'' u (-g)^(zeta~ - (e - 1)) (available: zeta~ - (e - 1) <= 4e - 9 <= n1) has integer sum e - 1 and
|W| + 2(e - 1) = |Z''| + zeta~ + e - 1 >= 1 + (delta0 - e) + e - 1 = delta0: against (F*).
## Step 3 (negative part)  The negative z~ sum to >= -(p - S') + 1.
Else add them one at a time; the first partial sum zeta~ <= -(p - S') is >= -(p - S') - (3e - 5).  For that Z'' and W'' <= U' of x-sum
p + zeta~ in [S' - 3e + 5, S'], W := Z'' u W'' has integer sum -p (residue 0) and |W| >= 1 + (p + zeta~) - E' >= |U'| - 3e + 6 =
p - 6e + 8 + delta' >= delta' + |Z0| = delta0 (|Z0| <= 3e - 5, p >= 9e - 13): against (F*).
So zeta~(Z'') is in [-(p - S') + 1, 2e - 4] for every Z'' <= Z0.
## Step 4 (no long zero-sum)
By CF (b), a zero-sum of length >= 2p + 2 needs W* <= U with rho(W*) >= 1 and |W*| + 2rho(W*) >= 2p + delta0.  Write W* = W' u Z''
(W' <= U' of x-sum s in [|W'|, S'], Z'' <= Z0), sigma~ := zeta~(Z'') - s in [-p + 1, 2e - 4], = sigma(W*) (mod p).
- sigma~ >= 0: |W*| + 2rho(W*) <= s + |Z''| + 2zeta~ - 2s <= (3e - 5) + 2(2e - 4) < 2p.
- sigma~ <= -1: rho(W*) = p + sigma~ and |W*| + 2rho(W*) <= 2p + |Z''| + 2zeta~ - s; if this is >= 2p + delta0 then (s >= zeta~ + 1)
  zeta~ >= delta0 + 1 - |Z''| >= 2.  Put rho0 := min(zeta~, e - 1) and W := Z'' u (-g)^(zeta~ - rho0) (zeta~ - rho0 <= 2e - 4 <= n1): integer
  sum rho0, residue rho0 in [1, e - 1], |W| + 2rho0 = |Z''| + zeta~ + rho0 >= delta0 + 1 + rho0 > delta0: against (F*).
So Y has no zero-sum of length >= 2p + 2: contradiction.  []
(Editorial: in Step 1 the displayed chain is |W| >= 1 + zeta_z - E' >= 2 + n1 - E' >= 2 + (p - 3e + 3 - E') - E' >= p - 3e + 5 - 2(2e - 3) =
p - 7e + 11, and p - 7e + 11 >= 3e - 4 >= delta0 as p >= 10e - 15.)

## Remaining (exact)
For e >= 3, p >= 10e - 13: an LS+ counterexample must be in case (alpha) with a = -1/2: g dominant (v_g >= 2p - 3e + 4), U' = (x_u (-1/2)),
delta' + E' <= e - 1, so at least |U'| - E' >= p - 4e + 3 + 2delta' terms of U' are the involution p (x_u = 1).  Expected lever (not
executed): the mirror of Steps 1-4 with the involution as unit (residue -tau/2 for integer x-sum tau), plus even deletion of involution
pairs (any long zero-sum must contain >= 2p + 1 non-involution terms) -- the two long-zero-sum patterns are tau even with a negative
Z0 sub-sum <= |Z''| - delta0, or tau odd in (p, 2p) with a positive Z0 sub-sum >= 2e.
