RESULT: VALID

Exact command, with all verification and corruption controls performed in memory:

```sh
python3 -B -c '
import hashlib
import itertools as it
import re
from collections import Counter

class Invalid(Exception):
    pass

def require(ok, reason):
    if not ok:
        raise Invalid(reason)

V, K, C, T = 87, 85, 43, 29
points = set(range(V))
point_once = Counter(range(V))
pair_once = Counter(it.combinations(range(V), 2))
universe = set(it.combinations(range(V), 3))

def verify(source):
    raw = source.splitlines()
    lines = [(n, s.strip()) for n, s in enumerate(raw, 1)
             if not s.lstrip().startswith("#")]
    pos = 0
    blocks = []
    systems = classes = 0

    def take():
        nonlocal pos
        require(pos < len(lines), "STRUCTURE: unexpected end of file")
        item = lines[pos]
        pos += 1
        return item

    def expect(wanted):
        n, s = take()
        require(s == wanted,
                f"STRUCTURE: line {n}: expected {wanted}, got {s!r}")

    expect("LKTS 87")
    for i in range(K):
        expect(f"KTS {i}")
        pairs = Counter()
        for j in range(C):
            expect(f"CLASS {j}")
            flat = []
            for _ in range(T):
                n, s = take()
                require(re.fullmatch(r"[0-9]+[ \t]+[0-9]+[ \t]+[0-9]+", s),
                        f"SYNTAX: line {n}: unrecognized triple")
                block = tuple(sorted(map(int, s.split())))
                require(len(set(block)) == 3 and set(block) <= points,
                        f"POINTS: line {n}: invalid 3-subset")
                flat.extend(block)
                blocks.append(block)
                pairs.update(it.combinations(block, 2))
            require(Counter(flat) == point_once,
                    f"CLASS_PARTITION: KTS {i}, CLASS {j}")
            classes += 1
        require(pairs == pair_once,
                f"PAIR_COVERAGE: KTS {i}: "
                f"missing={sum(p not in pairs for p in pair_once)}, "
                f"repeated={sum(v > 1 for v in pairs.values())}")
        systems += 1
    if pos != len(lines):
        n, s = lines[pos]
        raise Invalid(f"STRUCTURE: trailing line {n}: {s!r}")
    counts = Counter(blocks)
    require(len(counts) == len(blocks),
            f"REPEATED_BLOCK: repeated_blocks="
            f"{sum(v > 1 for v in counts.values())}, "
            f"extra_occurrences={len(blocks) - len(counts)}")
    require(set(counts) == universe,
            f"UNION: missing={len(universe - counts.keys())}, "
            f"extra={len(counts.keys() - universe)}")
    require((systems, classes, len(blocks)) == (85, 3655, 105995),
            "COUNTS: incorrect totals")
    return len(raw), len(raw) - len(lines), pos, systems, classes, len(blocks)

data = open("lkts87_g903.txt", "rb").read()
digest = hashlib.sha256(data).hexdigest()
require(digest == "65ab29ae6d24545c4ed41c3a4ea027becdf497b6810384b728379cfd0cae273e",
        f"SHA256: unexpected digest {digest}")
source = data.decode("ascii")
physical, comments, accounted, systems, classes, blocks = verify(source)
print("RESULT: VALID")
print(f"SHA-256: {digest}")
print(f"bytes={len(data)} physical_lines={physical} comments={comments} "
      f"noncomment_lines_accounted={accounted} unrecognized=0")
print(f"systems={systems} classes_per_system={C} total_classes={classes}")
print(f"triples_per_class={T} blocks_per_system={C*T} total_blocks={blocks}")
print(f"class_partitions=PASS ({classes} classes, {V} points each)")
print(f"pair_coverage=PASS ({systems} systems, {len(pair_once)} pairs once each)")
print(f"distinct_blocks={blocks} repeated_blocks=0 "
      f"union_size={len(universe)} missing_triples=0 extra_triples=0")

def control(name, mutated, intended):
    try:
        verify("\n".join(mutated))
    except Invalid as error:
        require(str(error).startswith(intended + ":"),
                f"CONTROL_WRONG_REASON: {name}: {error}")
        print(f"{name}: REJECTED: {error}")
    else:
        raise Invalid(f"CONTROL_ACCEPTED: {name}")

print("CONTROLS (parser and mathematical checks; no hash gate)")
lines = source.splitlines()
first = lines.index("CLASS 0") + 1
bad = lines.copy()
u, v = bad[first].split(), bad[first + 1].split()
u[0], v[0] = v[0], u[0]
bad[first], bad[first + 1] = " ".join(u), " ".join(v)
control("swap_points_in_one_class", bad, "PAIR_COVERAGE")
a, b, c = (lines.index(f"KTS {i}") for i in range(3))
bad = lines[:b + 1] + lines[a + 1:b] + lines[c:]
control("duplicate_KTS_0_as_KTS_1", bad, "REPEATED_BLOCK")
start = lines.index("CLASS 42")
bad = lines[:start] + lines[start + 1 + T:]
control("drop_KTS_0_CLASS_42", bad, "STRUCTURE")
bad = lines.copy()
u, v = bad[first].split(), bad[first + 1].split()
u[0] = v[0]
bad[first] = " ".join(u)
control("repeat_point_in_one_class", bad, "CLASS_PARTITION")
control("append_unrecognized_line", lines + ["UNRECOGNIZED"], "STRUCTURE")
print("controls_passed=5/5")
'
```

Output, exit status `0`. The sandbox blocked the Python launcher’s cache creation attempts:

```text
python3: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
python3: error: couldn't create cache file '/tmp/xcrun_db-CHkcB0Ad' (errno=Operation not permitted)
python3: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
python3: error: couldn't create cache file '/tmp/xcrun_db-Q7WNpJxR' (errno=Operation not permitted)
RESULT: VALID
SHA-256: 65ab29ae6d24545c4ed41c3a4ea027becdf497b6810384b728379cfd0cae273e
bytes=950110 physical_lines=109737 comments=1 noncomment_lines_accounted=109736 unrecognized=0
systems=85 classes_per_system=43 total_classes=3655
triples_per_class=29 blocks_per_system=1247 total_blocks=105995
class_partitions=PASS (3655 classes, 87 points each)
pair_coverage=PASS (85 systems, 3741 pairs once each)
distinct_blocks=105995 repeated_blocks=0 union_size=105995 missing_triples=0 extra_triples=0
```

Controls from the same execution, bypassing the hash check so each rejection tests the intended condition:

```text
CONTROLS (parser and mathematical checks; no hash gate)
swap_points_in_one_class: REJECTED: PAIR_COVERAGE: KTS 0: missing=4, repeated=4
duplicate_KTS_0_as_KTS_1: REJECTED: REPEATED_BLOCK: repeated_blocks=1247, extra_occurrences=1247
drop_KTS_0_CLASS_42: REJECTED: STRUCTURE: line 1264: expected CLASS 42, got 'KTS 1'
repeat_point_in_one_class: REJECTED: CLASS_PARTITION: KTS 0, CLASS 0
append_unrecognized_line: REJECTED: STRUCTURE: trailing line 109738: 'UNRECOGNIZED'
controls_passed=5/5
```