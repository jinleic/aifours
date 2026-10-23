# Lemma U certificate — exact format v1 (interoperability addendum) (2026-10-19T06:35:24-0700, ContinueCFR21)

Refines (does not change the certified anchor claim of) the specification
/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/lemmaU-certificate-spec-v1.md (sha256 b151a61f9f84ccf8a0b261bfeb056ff6a9db58fc99e516b7562e1cea98f57df2) and its erratum
/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/lemmaU-certificate-spec-v1-erratum1.md (sha256 beca7d3330230672e19ea5561f1844e721496ec7283e07c69a76672d62fb9135).
Purpose: fix the exact data format, indexing and checks so that the producer and an independently written checker
interoperate, and make both generic in n = 3q (gcd(3, q) = 1) and k >= 2 rows, as the DM21 positive control of spec
section 5 requires. Written only; nothing is run under this file. Running requires a separate parent GO.

## 1. Input
A raw file: k non-empty lines, each with n whitespace-separated decimal integers; entry D[x][c] = int value mod n
(rows x = 0..k-1 and columns c = 0..n-1 in file order). The raw file is pinned by its sha256.

## 2. Derived objects (each program computes these itself from the raw file)
- q = n / 3; require n % 3 == 0, q >= 1 and q % 3 != 0.
- E[x][c] = (D[x][c] - D[0][c]) mod n;  B[x][c] = E[x][c] mod q;  T[x][c] = E[x][c] mod 3.
- Pairs: all (x, y) with 0 <= x < y <= k-1 in lexicographic order; pair index p = 0..P-1, P = k(k-1)/2.
- Fibre (p, t), t = 0..q-1: the increasing list of columns c with (B[x][c] - B[y][c]) mod q == t, where (x, y) is
  pair p. Every fibre must have exactly 3 columns. Fibre (= equation) index j = p*q + t; J = P*q.
- Gauged unknowns: A[x][c] for x = 1..k-1 and c = 1..n-1, with variable index v(x, c) = (x-1)*(n-1) + (c-1);
  U = (k-1)*(n-1). A[0][c] = 0 for all c and A[x][0] = 0 for all x are fixed zeros.
- Equation vector e_j in F_3^U for fibre j = (p, t), p = (x, y): start from zero; for every column c >= 1 of the fibre:
  if x >= 1 add 1 at v(x, c); add 2 (= -1) at v(y, c). Arithmetic mod 3. (e_j . A = 0 says that the fibre sum of
  A[x] - A[y] is 0.)
- A point is a vector A in F_3^U, read as the k x n array with the fixed zeros.
- Rainbow: A is rainbow iff for every fibre j = (p, t), p = (x, y), the three values (A[x][c] - A[y][c]) mod 3 over
  the fibre's columns are pairwise distinct.
- alpha_hat in F_3^U: alpha_hat[v(x, c)] = (T[x][c] - T[x][0]) mod 3; minus_alpha_hat = (3 - alpha_hat) mod 3 entrywise.
- Point index: for z in {0,1,2}^dim, idx(z) = sum over r of z[r] * 3^(dim-1-r) (z[0] most significant);
  point(z) = sum over r of z[r] * basis[r] (mod 3). For dim = 0 there is exactly one point, the zero vector (idx 0).

## 3. Certificate file
One JSON object, UTF-8, produced by json.dumps(obj, sort_keys=True, separators=(",", ":")) followed by "\n". Keys
(exactly these; any other key is a format error):
- "format": the string "lemmaU-cert-v1"
- "anchor_sha256": 64 lowercase hex digits
- "n", "q", "k", "U", "J", "dim": integers
- "basis": list of dim lists, each of U integers in {0,1,2}
- "free_columns": list of dim distinct integers in [0, U)
- "rank_witness": list of objects {"pivot": integer in [0, U), "combination": [[j, coef], ...]}, with the j strictly
  increasing in [0, J) and every coef in {1, 2}
- "rainbow": strictly increasing list of point indices in [0, 3^dim)
- "failures": list of [idx, j] pairs, idx strictly increasing in [0, 3^dim), j in [0, J)
- "producer": object {"name": string, "sha256": string} (informational only; the checker must not use it)

## 4. Checks (VALID iff all pass; report the number of the first failing check)
0. Format: all keys present, no extra keys, types and ranges as in section 3; q = n/3, U = (k-1)(n-1),
   J = q*k*(k-1)/2, len(basis) = len(free_columns) = dim, len(rank_witness) = U - dim.
1. Anchor: the raw file's sha256 equals both the command-line value and "anchor_sha256"; it parses to exactly k rows of
   n integers; D is a (Z_n, k; 1)-difference matrix (for every pair x < y the n values (D[x][c] - D[y][c]) mod n are
   pairwise distinct); every fibre has exactly 3 columns.
2. Solutions: e_j . basis[i] = 0 (mod 3) for every j and every i.
3. Free-column identity: basis[i][free_columns[r]] == (1 if i == r else 0) for all i, r.
4. Rank witness: the pivots are pairwise distinct and none is a free column; for each record i, R_i = sum of
   coef * e_j over its combination (mod 3) satisfies R_i[pivot_i] == 1 and R_i[pivot_m] == 0 for every other
   record m. (Then the R_i are linearly independent combinations of the equations, so the rank is at least U - dim;
   with checks 2 and 3 the solution space is exactly the span of the basis and has dimension dim.)
5. Rainbow list: for every listed idx, point(idx) is rainbow.
6. Failures and coverage: the rainbow indices and the failure indices are disjoint and together are exactly
   {0, ..., 3^dim - 1}; for every failure [idx, j], fibre j of point(idx) does NOT carry three distinct values.
Facts reported only when VALID (otherwise null): dim; rank = U - dim; rainbow_count; alpha_hat_listed
(alpha_hat = point(z) for some listed rainbow idx); minus_alpha_hat_listed; rainbow_is_pm_alpha_hat (rainbow_count == 2,
both listed, and alpha_hat != minus_alpha_hat).
Hint (not normative): since the basis is the identity on the free columns, the only z with point(z) = alpha_hat is
z[r] = alpha_hat[free_columns[r]]; check point(z) == alpha_hat.

## 5. Checker interface
python3.14 -I -B cert_checker.py --anchor RAW --anchor-sha256 HEX --cert CERT_JSON --out OUT_JSON [--budget-s S]
Writes one JSON object to OUT_JSON (exclusive create) and prints the same object as one line. Keys: verdict ("VALID",
"INVALID" or "ERROR"), first_failed_check (int or null), reason (string), cert_sha256 (sha256 of the certificate
file bytes), anchor_sha256 (of the raw bytes read), n, q, k, U, J, dim, rank, rainbow_count, alpha_hat_listed,
minus_alpha_hat_listed, rainbow_is_pm_alpha_hat, wall_s. Exit 0 iff VALID, 1 if INVALID, 2 for ERROR (unreadable
input, existing OUT_JSON, budget exceeded, or bad arguments).

## 6. Producer interface
python3.14 -I -B lemmaU_cert_producer_v1.py --anchor RAW --anchor-sha256 HEX --out CERT_JSON [--budget-s S]
Writes the certificate (exclusive create) and prints one JSON summary line (status, n, q, k, U, J, rank, dim,
rainbow_count, cert_sha256, wall_s). Exit 0 on success.

## 7. Claim predicate for Lemma U (exact anchor)
Checker verdict VALID, anchor_sha256 = 3c8dbe62da8705eb6e713e85dae4d2fbf303614b2254f832a7291fe2f38a882a, n = 39,
k = 6, dim = 5, rank = 185, rainbow_count = 2 and rainbow_is_pm_alpha_hat = true.
