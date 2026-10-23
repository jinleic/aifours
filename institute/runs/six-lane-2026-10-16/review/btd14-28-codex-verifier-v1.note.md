RESULT: VALID

All four commands ran inside `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/btd14-28-codex-verifier-v1/` and exited with code 0.

Command 1:

```sh
python3 -B -c 'from pathlib import Path; print(Path("/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/btd14-28-codex-verifier-v1/task.md").read_text(encoding="utf-8"), end="")'
```

Output:

```text
python3: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
python3: error: couldn't create cache file '/tmp/xcrun_db-Vai2QjM0' (errno=Operation not permitted)
python3: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
python3: error: couldn't create cache file '/tmp/xcrun_db-wzWImorT' (errno=Operation not permitted)
# Task: independently verify a claimed balanced ternary design witness

Definition (Francel-Hurd; repeated blocks allowed). A BTD(V,B;rho1,rho2,R;K,Lambda) is a V x B matrix M with entries in {0,1,2} such that
- every row has exactly rho1 entries equal to 1 and exactly rho2 entries equal to 2 (so its sum is R = rho1 + 2 rho2);
- every column sums to K;
- any two distinct rows i != k have inner product sum_j M[i][j] M[k][j] = Lambda.
Target: V=14, B=28, rho1=8, rho2=3, R=14, K=7, Lambda=6.

File: btd14-28-witness-v1.btd, expected SHA-256 18cadb923274cbad3f35112d26edf00889971f76d8a0cec28540dcb9d2e40bb1.
Format: line 1 exactly "BTD 14 28 8 3 14 7 6"; then exactly 14 lines, each exactly 28 tokens from {0,1,2} separated by single spaces; one final LF; nothing else.
```

Command 2 — independent verifier and in-memory corruption controls:

```sh
python3 -B -c 'import hashlib
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

V, B, ONES, TWOS, R, K, LAMBDA = 14, 28, 8, 3, 14, 7, 6
HEADER = b"BTD 14 28 8 3 14 7 6"
EXPECTED = "18cadb923274cbad3f35112d26edf00889971f76d8a0cec28540dcb9d2e40bb1"

class Rejected(ValueError):
    pass

def verify(data):
    if not data.endswith(b"\n"):
        raise Rejected("format: missing final LF")
    lines = data.split(b"\n")
    if len(lines) != V + 2 or lines[-1] != b"":
        raise Rejected("format: expected exactly 15 LF-terminated lines")
    if lines[0] != HEADER:
        raise Rejected("format: header does not match exactly")
    matrix = []
    for i, line in enumerate(lines[1:-1], 1):
        tokens = line.split(b" ")
        if len(tokens) != B or any(t not in (b"0", b"1", b"2") for t in tokens):
            raise Rejected("format: row %d must contain exactly 28 single-space-separated tokens from {0,1,2}" % i)
        matrix.append([int(t) for t in tokens])
    row_checks = []
    for i, row in enumerate(matrix, 1):
        signature = (row.count(1), row.count(2), sum(row))
        row_checks.append(signature)
        if signature != (ONES, TWOS, R):
            raise Rejected("row composition: row %d has (ones,twos,sum)=%s, expected %s" % (i, signature, (ONES, TWOS, R)))
    columns = [tuple(matrix[i][j] for i in range(V)) for j in range(B)]
    column_checks = []
    for j, column in enumerate(columns, 1):
        total = sum(column)
        column_checks.append(total)
        if total != K:
            raise Rejected("column sum: column %d has sum %d, expected %d" % (j, total, K))
    pair_checks = []
    for i, k in combinations(range(V), 2):
        dot = sum(matrix[i][j] * matrix[k][j] for j in range(B))
        pair_checks.append(dot)
        if dot != LAMBDA:
            raise Rejected("row pair: (%d,%d) has inner product %d, expected %d" % (i + 1, k + 1, dot, LAMBDA))
    if (len(matrix), len(row_checks), len(column_checks), len(pair_checks)) != (14, 14, 28, 91):
        raise Rejected("internal accounting failure")
    return matrix, columns, row_checks, column_checks, pair_checks

def encode(matrix):
    return HEADER + b"\n" + b"".join(b" ".join(str(x).encode("ascii") for x in row) + b"\n" for row in matrix)

def expect_rejected(name, data, reason):
    try:
        verify(data)
    except Rejected as exc:
        message = str(exc)
        if not message.startswith(reason):
            raise RuntimeError("control %s rejected for wrong reason: %s" % (name, message))
        print("CONTROL %s: PASS; REJECTED; %s" % (name, message))
    else:
        raise RuntimeError("control %s was incorrectly accepted" % name)

raw = Path("btd14-28-witness-v1.btd").read_bytes()
actual = hashlib.sha256(raw).hexdigest()
print("raw_bytes=%d; sha256_calls=1" % len(raw))
print("expected_sha256=" + EXPECTED)
print("actual_sha256=" + actual)
if actual != EXPECTED:
    raise Rejected("integrity: SHA-256 mismatch")
matrix, columns, row_checks, column_checks, pair_checks = verify(raw)
print("integrity=PASS; strict_format=PASS")
print("line_accounting: header=1; matrix_rows=14; noncomment_lines=15; comment_lines=0; ignored_lines=0; final_LF=1; trailing_content=0")
print("row_checks=%d; (ones,twos,sum)_histogram=%s" % (len(row_checks), dict(Counter(row_checks))))
print("column_checks=%d; sum_histogram=%s" % (len(column_checks), dict(Counter(column_checks))))
print("row_pair_checks=%d; direct_inner_product_histogram=%s" % (len(pair_checks), dict(Counter(pair_checks))))
print("distinct_columns=%d; total_columns=%d" % (len(set(columns)), len(columns)))
print("column_(ones,twos)_types=%s" % dict(sorted(Counter((c.count(1), c.count(2)) for c in columns).items())))
groups = defaultdict(list)
for j, column in enumerate(columns, 1):
    groups[column].append(j)
repeated = [(column, indices) for column, indices in groups.items() if len(indices) > 1]
print("repeated_column_groups=%d; columns_in_repeated_groups=%d; extra_copies=%d" % (len(repeated), sum(len(indices) for _, indices in repeated), B - len(groups)))
print("repeated_column_positions_1_based=%s" % [indices for _, indices in repeated])
print("CONTROL POLICY: mutate only in memory; reuse no hash; exercise format/design checks directly")

i, j = next((i, j) for i in range(V) for j in range(B) if matrix[i][j] == 1)
entry = [row[:] for row in matrix]
entry[i][j] = 2
print("entry_control_position_1_based=(%d,%d); change=1->2" % (i + 1, j + 1))
expect_rejected("entry_1_to_2", encode(entry), "row composition:")

switch = None
for i, k in combinations(range(V), 2):
    for j, l in combinations(range(B), 2):
        a, b = matrix[i][j], matrix[i][l]
        if a == b or matrix[k][j] != b or matrix[k][l] != a:
            continue
        candidate = [row[:] for row in matrix]
        candidate[i][j], candidate[i][l] = b, a
        candidate[k][j], candidate[k][l] = a, b
        bad_pairs = []
        for x, y in combinations(range(V), 2):
            dot = sum(candidate[x][z] * candidate[y][z] for z in range(B))
            if dot != LAMBDA:
                bad_pairs.append((x + 1, y + 1, dot))
        if bad_pairs:
            switch = (i, k, j, l, a, b, candidate, bad_pairs)
            break
    if switch is not None:
        break
if switch is None:
    raise RuntimeError("could not construct a pair-violating 2x2 control")
i, k, j, l, a, b, candidate, bad_pairs = switch
preserves_rows = [(r.count(1), r.count(2), sum(r)) for r in candidate] == row_checks
preserves_columns = [sum(candidate[x][z] for x in range(V)) for z in range(B)] == column_checks
if not preserves_rows or not preserves_columns:
    raise RuntimeError("2x2 control did not preserve its required invariants")
print("switch_control: rows_1_based=%s; columns_1_based=%s; before=%s; after=%s" % ((i + 1, k + 1), (j + 1, l + 1), ((a, b), (b, a)), ((b, a), (a, b))))
print("switch_preserves_row_compositions_and_sums=%s; switch_preserves_column_sums=%s; bad_row_pairs=%d" % (preserves_rows, preserves_columns, len(bad_pairs)))
print("switch_bad_row_pairs_(row,row,inner_product)=%s" % bad_pairs)
expect_rejected("2x2_switch", encode(candidate), "row pair:")
expect_rejected("drop_final_LF", raw[:-1], "format: missing final LF")
expect_rejected("alter_header", b"BTD 14 28 8 3 14 7 5" + raw[len(HEADER):], "format: header does not match exactly")
print("WITNESS_RESULT=VALID; CORRUPTION_CONTROLS=4/4_PASS")'
```

Output:

```text
raw_bytes=805; sha256_calls=1
expected_sha256=18cadb923274cbad3f35112d26edf00889971f76d8a0cec28540dcb9d2e40bb1
actual_sha256=18cadb923274cbad3f35112d26edf00889971f76d8a0cec28540dcb9d2e40bb1
integrity=PASS; strict_format=PASS
line_accounting: header=1; matrix_rows=14; noncomment_lines=15; comment_lines=0; ignored_lines=0; final_LF=1; trailing_content=0
row_checks=14; (ones,twos,sum)_histogram={(8, 3, 14): 14}
column_checks=28; sum_histogram={7: 28}
row_pair_checks=91; direct_inner_product_histogram={6: 91}
distinct_columns=27; total_columns=28
column_(ones,twos)_types={(3, 2): 18, (5, 1): 6, (7, 0): 4}
repeated_column_groups=1; columns_in_repeated_groups=2; extra_copies=1
repeated_column_positions_1_based=[[25, 27]]
CONTROL POLICY: mutate only in memory; reuse no hash; exercise format/design checks directly
entry_control_position_1_based=(1,4); change=1->2
CONTROL entry_1_to_2: PASS; REJECTED; row composition: row 1 has (ones,twos,sum)=(7, 4, 15), expected (8, 3, 14)
switch_control: rows_1_based=(1, 2); columns_1_based=(1, 2); before=((2, 0), (0, 2)); after=((0, 2), (2, 0))
switch_preserves_row_compositions_and_sums=True; switch_preserves_column_sums=True; bad_row_pairs=10
switch_bad_row_pairs_(row,row,inner_product)=[(1, 7, 4), (1, 8, 8), (1, 10, 8), (1, 11, 2), (1, 12, 8), (2, 7, 8), (2, 8, 4), (2, 10, 4), (2, 11, 10), (2, 12, 4)]
CONTROL 2x2_switch: PASS; REJECTED; row pair: (1,7) has inner product 4, expected 6
CONTROL drop_final_LF: PASS; REJECTED; format: missing final LF
CONTROL alter_header: PASS; REJECTED; format: header does not match exactly
WITNESS_RESULT=VALID; CORRUPTION_CONTROLS=4/4_PASS
```

Command 3:

```sh
python3 -B -c 'import json
from pathlib import Path

def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate manifest key: " + key)
        result[key] = value
    return result

def reject_constant(value):
    raise ValueError("non-JSON numeric constant: " + value)

raw = Path("manifest.json").read_bytes()
text = raw.decode("utf-8", errors="strict")
print(text, end="" if text.endswith("\n") else "\n")
json.loads(text, object_pairs_hook=unique_object, parse_constant=reject_constant)
print("manifest_strict_json_parse=PASS")'
```

Output:

```text
{
 "witness_sha256": "18cadb923274cbad3f35112d26edf00889971f76d8a0cec28540dcb9d2e40bb1",
 "task_sha256": "891bfd8024272eb8f48c894af776c0f55230a1fb5a2b36ba8c6e920949a20968"
}
manifest_strict_json_parse=PASS
```

Command 4:

```sh
python3 -B -c 'import hashlib
import json
from pathlib import Path

manifest = json.loads(Path("manifest.json").read_bytes())
task_digest = hashlib.sha256(Path("task.md").read_bytes()).hexdigest()
verified_witness_digest = "18cadb923274cbad3f35112d26edf00889971f76d8a0cec28540dcb9d2e40bb1"
print("actual_task_sha256=" + task_digest)
print("manifest_task_sha256=" + manifest["task_sha256"])
if task_digest != manifest["task_sha256"]:
    raise ValueError("manifest task SHA-256 mismatch")
if manifest["witness_sha256"] != verified_witness_digest:
    raise ValueError("manifest witness SHA-256 differs from the verified digest")
print("manifest_task_hash=PASS; manifest_witness_hash=PASS; witness_not_rehashed=True")'
```

Output:

```text
actual_task_sha256=891bfd8024272eb8f48c894af776c0f55230a1fb5a2b36ba8c6e920949a20968
manifest_task_sha256=891bfd8024272eb8f48c894af776c0f55230a1fb5a2b36ba8c6e920949a20968
manifest_task_hash=PASS; manifest_witness_hash=PASS; witness_not_rehashed=True
```

There are **27 distinct columns**. Column `(ones,twos)` types are `(3,2): 18`, `(5,1): 6`, and `(7,0): 4`. Columns **25 and 27** are identical: one repeated group and one extra copy. Repeated columns are permitted by the definition.

All four corruption controls passed, including the switch that preserved every row composition and column sum while violating 10 row-pair conditions.

Concern: the first command emitted sandbox-denied macOS cache-write errors, but completed successfully. Subsequent commands completed without those messages. No files were created, modified, or deleted; no delegation or network was used.