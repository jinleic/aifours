RESULT: VALID

Certificate SHA-256 matches both `task.md` and `manifest.json`:
`7ae0a828b5af08b4bd9b423564981d85e3703886553638024fdc812f564989a6`

Computed counts:

- **259,911 bytes; 28,980 lines:** 1 comment, 0 blank lines, all **28,979 noncomment lines accounted for**: 2 format headers + 5,525 blocks + 52 point headers + 1,300 class headers + 22,100 resolution triples.
- **5,525 unique blocks**, each containing 4 distinct points in `0..51`; 0 duplicate blocks.
- Coverage equals the complete set of **22,100** 3-subsets. Every triple occurs exactly once; 0 missing, 0 extra, 0 with nonunit multiplicity.
- For **every point `0..51`**: 425 derived triples, 25 classes, 17 triples per class. Every class partitions the 51 other points; every triple belongs to the derived system and occurs exactly once in its resolution.
- Overall: **1,300 classes and 22,100 resolution triple occurrences**.
- `task.md` also matches its manifest checksum.

All five in-memory controls were rejected:

| Corruption | Observed rejection |
|---|---|
| Block 0: `(0,1,2,27)` → `(0,1,2,3)` | `3-subset coverage: missing=3, extra=0, nonunit=3` |
| Swap first triples between point 0 classes 0 and 1 | `point 0 class 0: not a partition; missing=[26, 51]; repeated=[(19, 2), (44, 2)]` |
| Drop point 0 class 24 | `point 0: expected 25 classes; got 24` |
| Replace point 0 class 1 with class 0 | `point 0: derived-triple use: missing=17, extra=0, nonunit=17` |
| Append a noncomment triple line | `unaccounted noncomment lines: 1` |

<details>
<summary>Exact commands run</summary>

All commands ran inside `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/rdsqs52-codex-verify-v1`. No files were modified.

```sh
pwd
rg --files -g '*' -g '!**/.git/**' .
cat task.md
cat manifest.json
python3 -c 'from pathlib import Path; p=Path("README.md"); print(p.read_text() if p.is_file() else "No README.md exists in the allowed directory.")'
python3 -c 'from pathlib import Path; import hashlib,json; p=Path("rdsqs52_z52_m23.txt"); data=p.read_bytes(); lines=data.decode("utf-8").splitlines(); expected=json.loads(Path("manifest.json").read_text())["files"][p.name]; actual=hashlib.sha256(data).hexdigest(); print("certificate_bytes:",len(data)); print("certificate_sha256:",actual); print("manifest_expected_sha256:",expected); print("hash_matches:",actual==expected); print("physical_lines:",len(lines)); print("comment_lines:",sum(s.startswith("#") for s in lines)); print("blank_lines:",sum(not s.strip() for s in lines)); print("first_16_lines:"); print("\n".join(str(i+1)+": "+s for i,s in enumerate(lines[:16])))'
python3 -c 'from pathlib import Path
from itertools import combinations
from collections import Counter
from copy import deepcopy
import hashlib, json, re

class Rejected(Exception):
    pass

def require(ok, reason):
    if not ok:
        raise Rejected(reason)

V = set(range(52))
full = set(combinations(range(52), 3))
require(len(full) == 22100, "incorrect reference triple universe")
name = "rdsqs52_z52_m23.txt"
raw = Path(name).read_bytes()
task = Path("task.md").read_bytes()
manifest = json.loads(Path("manifest.json").read_text())
expected = re.search(r"expected SHA-256 ([0-9a-f]{64})", task.decode()).group(1)
actual = hashlib.sha256(raw).hexdigest()
require(manifest["files"][name] == expected, "task/manifest hash disagreement")
require(actual == expected, "certificate SHA-256 mismatch")
require(hashlib.sha256(task).hexdigest() == manifest["files"]["task.md"], "task SHA-256 mismatch")

def parse(text):
    lines = text.splitlines()
    rows = [(n, s.split()) for n, s in enumerate(lines, 1) if not s.startswith("#")]
    cursor = 0
    def take(marker=None, width=None):
        nonlocal cursor
        require(cursor < len(rows), "unexpected end of certificate")
        n, tokens = rows[cursor]
        cursor += 1
        if marker is not None:
            require(tokens == marker, f"line {n}: expected {marker}, got {tokens}")
            return
        require(len(tokens) == width, f"line {n}: expected {width} integers, got {tokens}")
        try:
            return tuple(map(int, tokens))
        except ValueError:
            raise Rejected(f"line {n}: invalid integer")
    take(["RDSQS", "52"])
    take(["BLOCKS"])
    blocks = [take(width=4) for _ in range(5525)]
    resolution = []
    for x in range(52):
        take(["POINT", str(x)])
        classes = []
        for j in range(25):
            take(["CLASS", str(j)])
            classes.append([take(width=3) for _ in range(17)])
        resolution.append(classes)
    require(cursor == len(rows), f"unaccounted noncomment lines: {len(rows) - cursor}")
    return blocks, resolution, {
        "physical_lines": len(lines), "comment_lines": len(lines) - len(rows),
        "blank_lines": sum(not s.strip() for s in lines),
        "noncomment_lines": len(rows), "accounted_noncomment_lines": cursor,
        "format_headers": 2, "point_headers": 52, "class_headers": 1300,
        "block_lines": len(blocks), "resolution_triple_lines": 22100
    }

def verify(blocks, resolution):
    require(len(blocks) == 5525, f"expected 5525 blocks; got {len(blocks)}")
    normalized = []
    for k, b in enumerate(blocks):
        require(len(b) == 4 and len(set(b)) == 4 and set(b) <= V,
                f"block {k}: expected 4 distinct points in 0..51; got {b}")
        normalized.append(tuple(sorted(b)))
    require(len(set(normalized)) == len(normalized), "duplicate blocks")
    coverage = Counter(t for b in normalized for t in combinations(b, 3))
    missing, extra = full - set(coverage), set(coverage) - full
    nonunit = sum(n != 1 for n in coverage.values())
    require(not missing and not extra and nonunit == 0,
            f"3-subset coverage: missing={len(missing)}, extra={len(extra)}, nonunit={nonunit}")
    derived = [set() for _ in range(52)]
    for b in normalized:
        for x in b:
            derived[x].add(tuple(y for y in b if y != x))
    require(len(resolution) == 52, f"expected 52 point resolutions; got {len(resolution)}")
    class_sizes, partition_sizes, multiplicities = Counter(), Counter(), Counter()
    for x, classes in enumerate(resolution):
        require(len(derived[x]) == 425, f"point {x}: expected 425 derived triples")
        require(len(classes) == 25, f"point {x}: expected 25 classes; got {len(classes)}")
        seen = Counter()
        others = V - {x}
        for j, triples in enumerate(classes):
            require(len(triples) == 17, f"point {x} class {j}: expected 17 triples")
            canonical = []
            for t in triples:
                require(len(t) == 3 and len(set(t)) == 3 and set(t) <= others,
                        f"point {x} class {j}: invalid triple {t}")
                t = tuple(sorted(t))
                require(t in derived[x], f"point {x} class {j}: nonderived triple {t}")
                canonical.append(t)
            hits = Counter(y for t in canonical for y in t)
            require(hits == Counter(others),
                    f"point {x} class {j}: not a partition; missing={sorted(others - set(hits))}; repeated={sorted((y, n) for y, n in hits.items() if n != 1)}")
            seen.update(canonical)
            class_sizes[len(triples)] += 1
            partition_sizes[len(hits)] += 1
        missing, extra = derived[x] - set(seen), set(seen) - derived[x]
        nonunit = sum(n != 1 for n in seen.values())
        require(not missing and not extra and nonunit == 0,
                f"point {x}: derived-triple use: missing={len(missing)}, extra={len(extra)}, nonunit={nonunit}")
        multiplicities.update(seen.values())
    return {
        "blocks": len(normalized), "unique_blocks": len(set(normalized)),
        "reference_3_subsets": len(full), "covered_unique_3_subsets": len(coverage),
        "block_triple_occurrences": sum(coverage.values()),
        "coverage_multiplicity_histogram": dict(Counter(coverage.values())),
        "points_checked": len(resolution),
        "points_by_derived_triple_count": dict(Counter(map(len, derived))),
        "points_by_class_count": dict(Counter(map(len, resolution))),
        "classes_by_triple_count": dict(class_sizes),
        "classes_by_partition_size": dict(partition_sizes),
        "total_classes": sum(class_sizes.values()),
        "resolution_triple_occurrences": sum(k * n for k, n in multiplicities.items()),
        "derived_resolution_multiplicity_histogram": dict(multiplicities)
    }

blocks, resolution, accounting = parse(raw.decode("utf-8"))
counts = verify(blocks, resolution)
controls = []
def reject(name, action, reason):
    try:
        action()
    except Rejected as e:
        require(reason in str(e), f"control {name}: wrong rejection: {e}")
        controls.append({"control": name, "result": "REJECTED", "reason": str(e)})
    else:
        raise Rejected(f"control {name}: corruption accepted")

bad_blocks = list(blocks)
replacement = min(V - set(blocks[0]))
bad_blocks[0] = blocks[0][:-1] + (replacement,)
reject(f"block 0: {blocks[0]} -> {bad_blocks[0]}",
       lambda: verify(bad_blocks, resolution), "3-subset coverage: missing=3, extra=0, nonunit=3")
swapped = deepcopy(resolution)
swapped[0][0][0], swapped[0][1][0] = swapped[0][1][0], swapped[0][0][0]
reject("swap first triples of point 0 classes 0 and 1",
       lambda: verify(blocks, swapped), "point 0 class 0: not a partition")
dropped = deepcopy(resolution)
dropped[0].pop()
reject("drop point 0 class 24",
       lambda: verify(blocks, dropped), "point 0: expected 25 classes; got 24")
duplicated = deepcopy(resolution)
duplicated[0][1] = list(duplicated[0][0])
reject("replace point 0 class 1 with class 0",
       lambda: verify(blocks, duplicated), "point 0: derived-triple use: missing=17, extra=0, nonunit=17")
reject("append noncomment triple line",
       lambda: parse(raw.decode("utf-8").rstrip("\n") + "\n0 1 2\n"),
       "unaccounted noncomment lines: 1")

print("RESULT: VALID")
print(json.dumps({"certificate_bytes": len(raw), "sha256": actual, "expected_sha256": expected,
                  "task_manifest_hash_verified": True, "accounting": accounting,
                  "counts": counts, "corruption_controls": controls}, indent=2, sort_keys=True))
'
```

</details>