RESULT: VALID

All 26 row weights, 130 column weights, and 325 directly counted row pairs pass. There are 130 distinct columns and no repeated columns. Ten corruption controls and four positive invariances pass.

The checker command executed was:

```sh
/usr/bin/python3 -B -c 'import hashlib, json
from collections import Counter, defaultdict
from pathlib import Path

base = Path("/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/brd26-codex-verifier-v1")
task = (base / "task.md").read_bytes()
manifest = json.loads((base / "manifest.json").read_bytes())
raw = (base / "brd26-130-witness-v1.brd").read_bytes()
V, B, R, K, L = 26, 130, 25, 5, 4
header = b"BRD 26 130 25 5 4"
expected = "eb15cba18110e8c2e4ba7798838fc0a8fd508310d8a73a04132abb49977d71fe"
digest = hashlib.sha256(raw).hexdigest()
integrity = digest == expected == manifest["witness_sha256"]
task_integrity = hashlib.sha256(task).hexdigest() == manifest["task_sha256"]

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

def encode(a):
    return header + b"\n" + b"".join(
        b" ".join(str(x).encode("ascii") for x in row) + b"\n" for row in a)

def verify(data):
    parts = data.split(b"\n")
    body = parts[1:-1] if parts[-1] == b"" else parts[1:]
    tokens = [line.split(b" ") for line in body]
    fmt = []
    if parts[0] != header:
        fmt.append("header")
    if not data.endswith(b"\n") or data.endswith(b"\n\n"):
        fmt.append("finalLF")
    if len(parts) != V + 2 or parts[-1] != b"":
        fmt.append("line_count")
    if len(body) != V:
        fmt.append("row_count")
    if any(len(row) != B for row in tokens):
        fmt.append("token_count")
    if any(t not in (b"-1", b"0", b"1") for row in tokens for t in row):
        fmt.append("token_alphabet")
    if fmt:
        return {"errors": ["format:" + f for f in fmt]}
    a = [[int(t) for t in row] for row in tokens]
    require(encode(a) == data, "unaccounted bytes")
    rw = [sum(x != 0 for x in row) for row in a]
    cw = [sum(a[i][j] != 0 for i in range(V)) for j in range(B)]
    rb = [(i + 1, w) for i, w in enumerate(rw) if w != R]
    cb = [(j + 1, w) for j, w in enumerate(cw) if w != K]
    pairs = []
    for i in range(V):
        for j in range(i + 1, V):
            products = [a[i][c] * a[j][c] for c in range(B)]
            p, n, z = products.count(1), products.count(-1), products.count(0)
            require(p + n + z == B, "unaccounted product")
            pairs.append((i + 1, j + 1, p, n, z))
    require(len(pairs) == V * (V - 1) // 2 == 325, "pair coverage")
    require(len({(p[0], p[1]) for p in pairs}) == 325, "duplicate pair")
    pb = [p for p in pairs if p[2:] != (L // 2, L // 2, B - L)]
    errors = [name for name, bad in
              (("rowweights", rb), ("columnweights", cb), ("paircounts", pb)) if bad]
    return dict(errors=errors, a=a, rw=rw, cw=cw, rb=rb, cb=cb, pairs=pairs, pb=pb)

def histogram(values):
    return sorted(Counter(values).items())

original = verify(raw)
print("SHA256", digest, "exact_match", integrity, "witness_hash_calls=1")
print("MANIFEST task_sha256_match", task_integrity)
print("FORMAT errors", [e for e in original["errors"] if e.startswith("format:")])
if "a" not in original:
    print("RESULT: INVALID")
    raise SystemExit(1)
a = original["a"]
print("ACCOUNTING bytes", len(raw), "LF", raw.count(b"\n"),
      "lines", len(raw.split(b"\n")) - 1, "matrix_tokens", sum(map(len, a)),
      "token_histogram", histogram(x for row in a for x in row),
      "canonical_roundtrip", encode(a) == raw)
print("ROW_WEIGHTS checked", len(original["rw"]), "histogram", histogram(original["rw"]),
      "sum", sum(original["rw"]), "bad", original["rb"])
print("COLUMN_WEIGHTS checked", len(original["cw"]), "histogram", histogram(original["cw"]),
      "sum", sum(original["cw"]), "bad", original["cb"])
print("PAIR_COUNTS checked", len(original["pairs"]), "histogram_positive_negative_zero",
      histogram(p[2:] for p in original["pairs"]), "bad", original["pb"])
print("PAIR_PRODUCT_TOTALS positive_negative_zero",
      tuple(sum(p[k] for p in original["pairs"]) for k in (2, 3, 4)),
      "positions", 325 * B)
columns = [tuple(a[i][j] for i in range(V)) for j in range(B)]
groups = defaultdict(list)
for j, col in enumerate(columns, 1):
    groups[col].append(j)
repeated = [js for js in groups.values() if len(js) > 1]
print("COLUMNS distinct", len(groups), "repeated_excess", B - len(groups),
      "repeated_participants", sum(map(len, repeated)), "repeated_groups", repeated)
signed = [[sum(a[i][c] * a[j][c] for c in range(B))
           for j in range(V)] for i in range(V)]
unsigned = [[sum(abs(a[i][c]) * abs(a[j][c]) for c in range(B))
             for j in range(V)] for i in range(V)]
signed_ok = all(signed[i][j] == (R if i == j else 0)
                for i in range(V) for j in range(V))
unsigned_ok = all(unsigned[i][j] == (R if i == j else L)
                  for i in range(V) for j in range(V))
print("GRAM signed_diag", histogram(signed[i][i] for i in range(V)),
      "signed_upper_offdiag", histogram(signed[i][j] for i in range(V) for j in range(i + 1, V)),
      "equals_25I", signed_ok)
print("GRAM unsigned_diag", histogram(unsigned[i][i] for i in range(V)),
      "unsigned_upper_offdiag", histogram(unsigned[i][j] for i in range(V) for j in range(i + 1, V)),
      "equals_21I_plus_4J", unsigned_ok)
require(signed_ok == (not original["rb"] and all(p[2] == p[3] for p in original["pairs"])),
        "signed diagnostic disagrees")
require(unsigned_ok == (not original["rb"] and all(p[2] + p[3] == L for p in original["pairs"])),
        "unsigned diagnostic disagrees")
if not integrity or not task_integrity or original["errors"]:
    print("RESULT: INVALID")
    raise SystemExit(1)

def clone():
    return [row[:] for row in a]

controls = 0
invariances = 0

def reject(name, data, expected_errors, proof):
    global controls
    result = verify(data)
    require(set(result["errors"]) == set(expected_errors), name + ": wrong rejection")
    require(proof(result), name + ": intended reason not demonstrated")
    controls += 1
    if "a" in result:
        print("CONTROL", name, "PASS", "errors", result["errors"],
              "bad_rows", result["rb"], "bad_columns", result["cb"],
              "bad_pairs", len(result["pb"]), "first_pair", result["pb"][:1])
    else:
        print("CONTROL", name, "PASS", "errors", result["errors"], "matrix_checks=skipped_format")

m = clone()
require(m[0][0] == -1, "signflip source")
m[0][0] = 1
reject("signflip_r1c1_-1_to_1", encode(m), ["paircounts"],
       lambda t: t["rw"] == original["rw"] and t["cw"] == original["cw"]
       and all(abs(t["a"][i][j]) == abs(a[i][j]) for i in range(V) for j in range(B))
       and len(t["pb"]) == K - 1 and all(p[2] + p[3] == L for p in t["pairs"]))

m = clone()
require(m[0][1] == 1, "deletion source")
m[0][1] = 0
reject("delete_r1c2_1_to_0", encode(m), ["rowweights", "columnweights", "paircounts"],
       lambda t: t["rb"] == [(1, 24)] and t["cb"] == [(2, 4)] and len(t["pb"]) == 4)

m = clone()
require(m[0][1] == 1 and m[0][2] == 0, "move source/destination")
m[0][1], m[0][2] = 0, 1
reject("move_r1_c2_to_c3", encode(m), ["columnweights", "paircounts"],
       lambda t: t["rw"] == original["rw"] and t["cb"] == [(2, 4), (3, 6)])

reject("header_L4_to_L6", raw.replace(header, b"BRD 26 130 25 5 6", 1),
       ["format:header"], lambda t: True)
reject("missing_finalLF", raw[:-1],
       ["format:finalLF", "format:line_count"], lambda t: True)
reject("extra_finalLF", raw + b"\n",
       ["format:finalLF", "format:line_count", "format:row_count",
        "format:token_count", "format:token_alphabet"], lambda t: True)
reject("double_space", raw.replace(b"\n-1 1", b"\n-1  1", 1),
       ["format:token_count", "format:token_alphabet"], lambda t: True)
reject("tab", raw.replace(b"\n-1 1", b"\n-1\t1", 1),
       ["format:token_count", "format:token_alphabet"], lambda t: True)
reject("token_2", raw.replace(b"\n-1 1", b"\n-1 2", 1),
       ["format:token_alphabet"], lambda t: True)
reject("CRLF", raw.replace(b"\n", b"\r\n"),
       ["format:header", "format:token_alphabet"], lambda t: True)

def accept(name, m):
    global invariances
    result = verify(encode(m))
    require(not result["errors"], name + ": unexpected rejection")
    invariances += 1
    print("INVARIANCE", name, "PASS", "rows", len(result["rw"]),
          "columns", len(result["cw"]), "pairs", len(result["pairs"]))

m = clone()
m[0] = [-x for x in m[0]]
accept("row1_signflip", m)
m = clone()
for row in m:
    row[0] = -row[0]
accept("column1_signflip", m)
accept("reverse_rows", list(reversed(clone())))
accept("reverse_columns", [list(reversed(row)) for row in a])
print("CONTROL_SUMMARY rejections", controls, "invariances", invariances,
      "mutation_hash_calls=0")
print("RESULT: VALID")
'
```

Exit code: `0`. Exact checker output, including launcher diagnostics:

```text
python3: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
python3: error: couldn't create cache file '/tmp/xcrun_db-mH4dFd4z' (errno=Operation not permitted)
python3: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
python3: error: couldn't create cache file '/tmp/xcrun_db-arMJ8rSU' (errno=Operation not permitted)
SHA256 eb15cba18110e8c2e4ba7798838fc0a8fd508310d8a73a04132abb49977d71fe exact_match True witness_hash_calls=1
MANIFEST task_sha256_match True
FORMAT errors []
ACCOUNTING bytes 7103 LF 27 lines 27 matrix_tokens 3380 token_histogram [(-1, 325), (0, 2730), (1, 325)] canonical_roundtrip True
ROW_WEIGHTS checked 26 histogram [(25, 26)] sum 650 bad []
COLUMN_WEIGHTS checked 130 histogram [(5, 130)] sum 650 bad []
PAIR_COUNTS checked 325 histogram_positive_negative_zero [((2, 2, 126), 325)] bad []
PAIR_PRODUCT_TOTALS positive_negative_zero (650, 650, 40950) positions 42250
COLUMNS distinct 130 repeated_excess 0 repeated_participants 0 repeated_groups []
GRAM signed_diag [(25, 26)] signed_upper_offdiag [(0, 325)] equals_25I True
GRAM unsigned_diag [(25, 26)] unsigned_upper_offdiag [(4, 325)] equals_21I_plus_4J True
CONTROL signflip_r1c1_-1_to_1 PASS errors ['paircounts'] bad_rows [] bad_columns [] bad_pairs 4 first_pair [(1, 14, 1, 3, 126)]
CONTROL delete_r1c2_1_to_0 PASS errors ['rowweights', 'columnweights', 'paircounts'] bad_rows [(1, 24)] bad_columns [(2, 4)] bad_pairs 4 first_pair [(1, 2, 2, 1, 127)]
CONTROL move_r1_c2_to_c3 PASS errors ['columnweights', 'paircounts'] bad_rows [] bad_columns [(2, 4), (3, 6)] bad_pairs 8 first_pair [(1, 2, 3, 1, 126)]
CONTROL header_L4_to_L6 PASS errors ['format:header'] matrix_checks=skipped_format
CONTROL missing_finalLF PASS errors ['format:finalLF', 'format:line_count'] matrix_checks=skipped_format
CONTROL extra_finalLF PASS errors ['format:finalLF', 'format:line_count', 'format:row_count', 'format:token_count', 'format:token_alphabet'] matrix_checks=skipped_format
CONTROL double_space PASS errors ['format:token_count', 'format:token_alphabet'] matrix_checks=skipped_format
CONTROL tab PASS errors ['format:token_count', 'format:token_alphabet'] matrix_checks=skipped_format
CONTROL token_2 PASS errors ['format:token_alphabet'] matrix_checks=skipped_format
CONTROL CRLF PASS errors ['format:header', 'format:token_alphabet'] matrix_checks=skipped_format
INVARIANCE row1_signflip PASS rows 26 columns 130 pairs 325
INVARIANCE column1_signflip PASS rows 26 columns 130 pairs 325
INVARIANCE reverse_rows PASS rows 26 columns 130 pairs 325
INVARIANCE reverse_columns PASS rows 26 columns 130 pairs 325
CONTROL_SUMMARY rejections 10 invariances 4 mutation_hash_calls=0
RESULT: VALID
```

The preliminary input-inspection command was:

```sh
/usr/bin/python3 -B -c 'from pathlib import Path; b=Path("/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/brd26-codex-verifier-v1"); print("=== task.md ==="); print((b/"task.md").read_text()); print("=== manifest.json ==="); print((b/"manifest.json").read_text()); print("=== brd26-130-witness-v1.brd ==="); print((b/"brd26-130-witness-v1.brd").read_text())'
```

Limits: verification covers the supplied bytes and definition. Malformed-format controls stop before matrix checks. The checker writes no files; the macOS launcher’s cache-write attempts were denied. No network, delegation, existing checker, or mutation hashing was used.