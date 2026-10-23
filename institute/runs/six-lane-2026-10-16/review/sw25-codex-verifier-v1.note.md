RESULT: VALID

SHA256 matches: `bfadf44596bc5138106432690bf507a8ff9c36cd3c40eb8eeb08195a9b2d4ab0`.

- Exact format: 1,459 bytes = 9 header bytes + 825 token characters + 600 spaces + 25 row LFs. Exactly 26 ASCII lines, final LF, no extra lines.
- Entries: 625/625 ternary; counts `{−1: 200, 0: 225, +1: 200}`.
- Symmetry: 625/625 equalities pass.
- Row weights: all 25 equal 16.
- \(WW^T=16I\): all 625 entries pass using exact integer arithmetic.
- Observed extra invariants: trace **20**; diagonal distribution `{−1: 0, 0: 5, +1: 20}`.

Controls invoked the mathematical predicate separately, without hashing mutations:

| Control | Result |
|---|---|
| Swap rows 0 and 1 only | Rejected: 60 symmetry equalities fail; all weights and Gram entries pass |
| Flip diagonal sign at `(0,0)` | Rejected: 30 Gram entries fail; symmetry and weights pass |
| Set `(0,0)` to 2 | Rejected: nonternary entry detected; symmetry passes |
| Drop last row | Rejected: dimensions fail |
| Simultaneous row/column permutation | Valid |
| Signed conjugation | Valid |
| Global negation | Valid |

Actual executed command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 python3 -B -c 'import hashlib, resource, sys

P = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sw25-parent-inputs-v1/sw25-16-witness-v1.sw"
H = "bfadf44596bc5138106432690bf507a8ff9c36cd3c40eb8eeb08195a9b2d4ab0"
N, W = 25, 16

def need(ok, message):
    if not ok:
        raise AssertionError(message)

def inspect(a):
    if len(a) != N or any(len(row) != N for row in a):
        return dict(shape=False, valid=False)
    entries = sum(type(x) is int and x in (-1, 0, 1) for row in a for x in row)
    symmetry = sum(a[i][j] == a[j][i] for i in range(N) for j in range(N))
    row_weights = [sum(x*x for x in row) for row in a]
    weights = sum(v == W for v in row_weights)
    gram = sum(sum(a[i][k]*a[j][k] for k in range(N)) == (W if i == j else 0)
               for i in range(N) for j in range(N))
    return dict(shape=True, entries=entries, symmetry=symmetry,
                row_weights=row_weights, weights=weights, gram=gram,
                valid=(entries == 625 and symmetry == 625 and weights == 25 and gram == 625))

def control(name, a, expected):
    r = inspect(a)
    need(r["valid"] == expected, name + ": unexpected validity")
    print(name, {k:v for k,v in r.items() if k != "row_weights"})
    return r

with open(P, "rb") as f:
    raw = f.read(1460)
digest = hashlib.sha256(raw).hexdigest()
print("INPUT", "bytes", len(raw), "sha256", digest)
need(len(raw) == 1459 and digest == H, "raw length or pinned hash mismatch")
raw.decode("ascii")
lines = raw.split(b"\n")
need(len(lines) == 27 and lines[-1] == b"" and b"\r" not in raw, "line layout")
need(lines[0] == b"SW 25 16", "header")
tokens = [line.split(b" ") for line in lines[1:-1]]
need(len(tokens) == 25 and all(len(row) == 25 for row in tokens), "token layout")
need(all(t in (b"-1", b"0", b"1") for row in tokens for t in row), "token syntax")
a = [[int(t) for t in row] for row in tokens]
rebuilt = b"SW 25 16\n" + b"".join(b" ".join(str(x).encode("ascii") for x in row) + b"\n" for row in a)
need(rebuilt == raw, "unaccounted bytes")
counts = {v:sum(x == v for row in a for x in row) for v in (-1, 0, 1)}
diagonal = [a[i][i] for i in range(N)]
print("BYTES", dict(header_including_LF=9, token_characters=625+counts[-1], spaces=600, row_LFs=25))
print("FORMAT ASCII, exact reconstruction, 26 lines, final LF, no extra lines")
original = inspect(a)
print("ORIGINAL", original)
need(original["valid"], "original mathematical predicate")
print("INVARIANTS", "entry_counts", counts, "trace", sum(diagonal),
      "diagonal_distribution", {v:diagonal.count(v) for v in (-1, 0, 1)})

b = [row[:] for row in a]
b[0], b[1] = b[1], b[0]
r = control("rows_only_swap_0_1", b, False)
need(r["shape"] and r["entries"] == 625 and r["symmetry"] < 625 and r["weights"] == 25 and r["gram"] == 625, "swap intended reason")

k = next(i for i in range(N) if a[i][i] != 0)
b = [row[:] for row in a]
b[k][k] = -b[k][k]
r = control("diagonal_sign_flip_" + str(k), b, False)
need(r["shape"] and r["entries"] == 625 and r["symmetry"] == 625 and r["weights"] == 25 and r["gram"] < 625, "sign intended reason")

b = [row[:] for row in a]
b[0][0] = 2
r = control("diagonal_entry_2", b, False)
need(r["shape"] and r["entries"] == 624 and r["symmetry"] == 625, "nonternary intended reason")
r = control("drop_last_row", [row[:] for row in a[:-1]], False)
need(not r["shape"], "drop intended reason")

p = [(7*i+3) % N for i in range(N)]
need(sorted(p) == list(range(N)), "permutation")
control("simultaneous_row_column_permutation", [[a[p[i]][p[j]] for j in range(N)] for i in range(N)], True)
d = [-1 if i % 3 == 0 else 1 for i in range(N)]
control("signed_conjugation", [[d[i]*a[i][j]*d[j] for j in range(N)] for i in range(N)], True)
control("global_negation", [[-x for x in row] for row in a], True)

peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
peak_bytes = peak if sys.platform == "darwin" else peak*1024
need(peak_bytes <= 1024**3, "peak resident memory exceeded 1 GiB")
print("RESOURCES single_thread=True peak_resident_bytes=" + str(peak_bytes))
print("RESULT: VALID")
'
```

The successful run exited 0, used one Python thread, and reported peak resident memory **19,644,416 bytes**, below 1 GiB. macOS rejected attempted hard memory caps; the memory bound was checked through measured peak usage.

Only the named witness was opened as input. No files were written, edited, or deleted; no network, delegation, supplied checker, producer, circulant assumption, or solver was used. This verification assumes correct Python arithmetic, hashing, filesystem I/O, and OS resource reporting. Model verification is not peer review.