# cert_checker: independent checker for Lemma U certificates (format lemmaU-cert-v1)

Written 2026-10-19 by ContinueCFR21.CertChecker from the normative
`../../evidence/lemmaU-certificate-format-v1.md` (sha256 1b6537a42dd936a16337c58fd65039ece9e150099e2b8a297ab21d206dfd6ba0)
alone. Background only: `lemmaU-certificate-spec-v1.md` and `lemmaU-certificate-spec-v1-erratum1.md`. The raw files
`controls-v1/dm39_six_anchor.raw` and cfr21 `checker-controls-pass-v1/controls/pos_sage_dm21_k6.raw` were looked at
for their format only (both: 6 lines, each terminated by "\n"). Nothing from the producer, `mols39/code/`, other
`mols39/review/` content, `runs-*`, `probes*` or `institute/` was read.

**Not executed.** No run, test, linter, py_compile or formatter was used; the program was desk-checked only.

- `cert_checker.py`: sha256 e7e849627865db5c592507563b482a62873bd21413e0f46d4fec8bb5429e99a0 (610 lines, 23900 bytes).
- Python 3.14 standard library only (hashlib, json, math, sys, time); one process; no threads, subprocesses,
  network or lane imports; exact integer arithmetic mod 3 and mod n.

## What is checked
Checks 0-6 of format section 4, in that order; the first failing check stops the run and is reported in
`first_failed_check` (verdict INVALID). All section-2 objects (q, E, B, T, pairs, fibres, e_j, v(x,c), alpha_hat,
idx/point) are recomputed from the raw file; certificate sizes are used only after check 0 ties them together and
check 1 ties them to the raw file.
- 0 format: UTF-8 JSON object, exactly the 14 keys, types and ranges of section 3, q = n/3, U = (k-1)(n-1),
  J = q*k*(k-1)/2, len(basis) = len(free_columns) = dim, len(rank_witness) = U - dim.
- 1 anchor: raw sha256 equals `--anchor-sha256` and `anchor_sha256`; exactly k rows of n integers; D is a
  (Z_n, k; 1)-difference matrix; every fibre has exactly 3 columns.
- 2 solutions: e_j . basis[i] = 0 (mod 3) for all j, i.
- 3 identity: basis[i][free_columns[r]] = (1 if i == r else 0).
- 4 rank witness: pivots pairwise distinct and not free; R_i = sum coef*e_j (mod 3) has R_i[pivot_i] = 1 and
  R_i[pivot_m] = 0 for every other record m (all pivots, not only neighbours).
- 5 rainbow list: point(idx) is rainbow on all J fibres for every listed idx.
- 6 failures and coverage: no duplicates, rainbow and failure indices disjoint, together exactly
  {0, ..., 3^dim - 1}; for each failure [idx, j] the three values of fibre j of point(idx) are not pairwise distinct.
- Facts, only when VALID (else null): dim, rank = U - dim, rainbow_count, alpha_hat_listed,
  minus_alpha_hat_listed, rainbow_is_pm_alpha_hat.

## CLI, output, exit codes
    python3.14 -I -B cert_checker.py --anchor RAW --anchor-sha256 HEX --cert CERT_JSON --out OUT_JSON [--budget-s S]
`--flag=value` is also accepted; each flag at most once; `--budget-s` is positive finite seconds (default 240).
One JSON object with exactly the section-5 keys (verdict, first_failed_check, reason, cert_sha256, anchor_sha256,
n, q, k, U, J, dim, rank, rainbow_count, alpha_hat_listed, minus_alpha_hat_listed, rainbow_is_pm_alpha_hat,
wall_s) is written to OUT_JSON (reserved with `open(path, "x")` before any input is read) and printed as one line.
cert_sha256 and anchor_sha256 are the sha256 of the bytes actually read and parsed.

| exit | verdict | when |
|---|---|---|
| 0 | VALID | checks 0-6 passed within the budget; reason "checks 0-6 passed" |
| 1 | INVALID | first failing check N in first_failed_check; reason "check N: ..." |
| 2 | ERROR | reason "budget"; "bad arguments: ..."; "output file already exists"; "cannot create/read/write ...: ..."; "internal error: ..." |

first_failed_check is null for VALID and ERROR. For a claim (format section 7) the caller must still check
anchor_sha256 = 3c8dbe62..., n = 39, k = 6, dim = 5, rank = 185, rainbow_count = 2, rainbow_is_pm_alpha_hat = true.

## Complexity
Check 0 is linear in the certificate size. Check 1 is O(k^2 n). Each e_j has at most 6 nonzeros. Check 2 needs at
most 6*J*dim steps, check 3 dim^2, check 4 (U - dim)*(6*sum|combination| + U), check 5 |rainbow|*(dim*U + 3J),
check 6 3^dim + |failures|*(dim*U + 3), facts k*n + |rainbow|*dim*U. That is roughly 1e6 elementary steps for the
anchor (U = 190, J = 195, dim 5, 243 points) and 2.5e6 for DM21 (U = 100, J = 105, dim 7, 2187 points). Memory is
O(k*n + J + dim*U + 3^dim) small integers. Expected to run far below 60 s in CPython; this is an estimate, nothing
was measured. Before check 6 enumerates the 3^dim indices, it checks that the count matches, so a short
certificate never triggers that enumeration.

## Desk-check table (cert_checker.py line numbers)
| check | normative requirement | lines |
|---|---|---|
| 0 | UTF-8 JSON; duplicate keys, NaN/Infinity rejected | 102-112 (hooks 89-90, 93-99) |
| 0 | exactly the 14 keys | 117-124 (key set 24-26) |
| 0 | format tag; anchor_sha256 64 lowercase hex; n q k U J dim integers (bool rejected) | 125-132 (is_int 76-78) |
| 0 | q = n/3; q >= 1, q mod 3 != 0; k >= 2; U = (k-1)(n-1); J = q*k(k-1)/2 | 133-144 |
| 0 | basis: dim lists of U entries in {0,1,2} | 145-154 |
| 0 | free_columns: dim distinct integers in [0, U) | 155-162 |
| 0 | rank_witness: U - dim records {pivot, combination}; pivot in [0,U); j strictly increasing in [0,J); coef in {1,2} | 163-185 |
| 0 | rainbow strictly increasing in [0,3^dim); failures [idx, j], idx strictly increasing in [0,3^dim), j in [0,J) | 186-209 |
| 0 | producer {name: str, sha256: str}, otherwise unused | 210-214 |
| 1 | raw sha256 == --anchor-sha256 and == anchor_sha256 | 248-251 (digest 520) |
| 1 | exactly k rows of n decimal integers | 222-243, 252-259 |
| 1 | own q, U, lexicographic pairs, J from the raw shape (equal to header) | 261-268 |
| 1 | D mod n; every pair's n differences pairwise distinct (DM) | 269-273 |
| 1 | E, B, T; fibre (p,t) = increasing columns with (B[x][c]-B[y][c]) mod q = t; exactly 3; j = p*q + t | 274-287 |
| sec. 2 | v(x,c) 293-295; fixed zeros 298-302; e_j 305-319; idx(z)/point(z) 322-336; fibre values 339-347 | 293-347 |
| 2 | e_j . basis[i] = 0 (mod 3) for all j, i | 352-358 |
| 3 | basis[i][free_columns[r]] = [i == r] | 363-370 |
| 4 | pivots distinct 378-380; none free 381-384; R_i 385-390; R_i[pivot_i] = 1 391-392; R_i[pivot_m] = 0 for all m != i 393-395 | 375-395 |
| 5 | every listed point(idx) rainbow on all J fibres | 400-407 |
| 6 | no duplicates 416-420; disjoint 421-422; count 3^dim 423-425; union exact 426-428; each failure fibre fails 429-434 | 412-434 |
| facts | alpha_hat 442-445; minus 446; listed by definition 447-453; pm 462-463; only on VALID 552-556 | 439-464 |
| order | 0 -> 6, first failure stops (CheckFailed carries the number) | 529-556 |
| budget | Budget 62-73; ticks 149 167 192 201 229 271 279 355 366 386 403 426 430 450; ERROR "budget" 549-551; deadline passed at the end -> ERROR 557-558 | 62-73, 549-558 |
| interface | CLI 469-497; reserve OUT_JSON 590-597; read and hash 514-527; n..J after check 1 534-535; write, print, exit 561-579; unexpected exception -> ERROR 598-602, exit 2 605-610 | 469-610 |

## Ambiguities in the format file and how they were resolved
1. Check 0 does not list section 2's "require q >= 1 and q % 3 != 0" or the stated scope k >= 2. All three are
   enforced in check 0, because they constrain header integers that check 0 validates. Only degenerate
   certificates are affected.
2. Section 3 says the file is written by `json.dumps(sort_keys=True, separators=(",", ":"))` plus "\n", but check 0
   lists only keys, types and ranges. The checker does not require byte-canonical form; cert_sha256 binds the exact
   bytes. It does reject non-UTF-8 input, invalid JSON, duplicate keys (at any level), NaN/Infinity, and floats or
   booleans where integers are required.
3. Nested objects: rank_witness records must have exactly {pivot, combination}, and producer exactly {name, sha256}
   with string values. Producer is not used for anything else.
4. Raw syntax: the file is split at "\n" (one final terminator allowed; CR counts as whitespace) and each line is
   split on ASCII whitespace. Every token must match [+-]?[0-9]+. A non-ASCII or non-decimal token, or an empty or
   whitespace-only line, fails check 1. Values are reduced mod n after the shape check.
5. `--anchor-sha256` is compared exactly with the lowercase hex digest. A malformed or uppercase value is a check-1
   mismatch, not a CLI error, so the "wrong anchor hash" control fails at check 1. A certificate anchor_sha256 that
   is not 64 lowercase hex digits fails at check 0.
6. n, q, k, U, J are outputs but not "facts". They hold the checker's own raw-derived values once checks 0 and 1
   have passed, and are null before that.
7. Budget: the clock starts at program start and is tested inside every loop. If the deadline has passed when the
   checks finish, the verdict becomes ERROR "budget", so neither VALID nor INVALID is reported after the budget.
   A non-positive or non-finite --budget-s counts as bad arguments.
8. OUT_JSON is reserved before any input is read, so an existing file is detected before any work. For unreadable
   inputs the ERROR object is written there too. For bad arguments or an existing or uncreatable OUT_JSON it is
   only printed.
9. alpha_hat_listed and minus_alpha_hat_listed use the definition: point(idx) is compared with +-alpha_hat for every
   listed rainbow idx. They do not use the non-normative hint, which is equivalent given check 3.
10. Check 0 already enforces "strictly increasing" and the index ranges. Check 6 still re-tests duplicates,
    disjointness, the count 3^dim and exact set equality.
