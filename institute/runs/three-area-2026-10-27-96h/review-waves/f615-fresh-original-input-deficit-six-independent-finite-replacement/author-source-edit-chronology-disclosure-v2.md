# F615 author source provenance: exact editing disclosure

**Process disposition, as directly communicated by Main:** ONE PROCESS MAJOR. The frozen new-files-only/no-overwrite requirement also applied to the author's own newly created draft, so the three in-place source edits were a source-provenance deviation. No compliant initial freeze or initial SHA-256 is claimed. On the reported facts—no scientific execution, no pre-existing or frozen input changed, and no held payload used—Main did not automatically infer mathematical falsity or impose an entire-episode mathematical hold. This deviation is separate from the earlier worker-interruption major. Main will inspect native history and current bytes before any prospective GO.

## Recorded order and actual metadata

1. The author created the new `independent-finite-author-checker-v1.py`. The write tool reported 35,441 bytes and a tool snapshot tag `70B3`. This tag is **not** a SHA-256. The initial draft bytes were not separately saved, and their initial SHA-256 was not observed.
2. The author performed the first edit-tool operation, using snapshot `70B3`; the edit response showed snapshot `88D7`. Its exact operations are recorded below.
3. The author performed the second edit-tool operation, using snapshot `88D7`; the response showed snapshot `5D69`.
4. The author performed the third edit-tool operation, using snapshot `5D69`; the response showed snapshot `0AA9`.
5. The author created the separate `author-candidate-v1.md`, and then the earlier administrative `author-source-edit-chronology-disclosure-v1.json`. The original source and report remain unchanged after Main's disposition. The exact creation and edit times were not independently observed and are not inferred.
6. After receiving Main's disposition, the author ran **metadata-only** `/bin/date`, `/usr/bin/shasum -a 256`, and `/usr/bin/wc -c -l` on the current source and report. The child-native clock printed `2026-10-30T15:13:27-0700 PDT` before the hash and count commands. It is an actual clock observation before this v2 disclosure was created, not an edit/creation timestamp, and is not the parent-supplied earlier metadata clock.

Current bytes observed by that child metadata command:

| File | SHA-256 | bytes | LF |
|---|---|---:|---:|
| `independent-finite-author-checker-v1.py` | `7164e87a473abc5a506e58bd6fce715df816e1d4b942b31e4c0b0d64734d3468` | 37781 | 887 |
| `author-candidate-v1.md` | `7b356af648b83763986720941c183f850ba82d3ef78031f7bc7f2094d13ca0a0` | 9615 | 65 |

The above are current source/report pins, not initial draft pins. Scientific execution of the source remains **NOT RUN**; the metadata commands did not execute it.

## First edit: original snapshot `70B3`

All line locators below are the original locators submitted in this single edit operation; inserted text and replacements are reproduced exactly, with `+` identifying the replacement/inserted lines. The before text is included where the original source is observable in the author transcript.

* **Line 212, replacement.** Before: `    need(adjacent <= boundaries, "BOUNDARY_ROTATION")`. After: `    check_boundary(adjacent, boundaries)`.
* **Lines 220–221, replacement.** Before:

```python
def check_boundary(part, boundaries):
    need(part["adjacent"] <= boundaries, "BOUNDARY_ROTATION")
```

  After:

```python
def check_boundary(adjacent, boundaries):
    need(adjacent <= boundaries, "BOUNDARY_ROTATION")
```

* **After line 595, insertion:**

```python
    require_phase_chain(ps, c1)
    require_phase_chain(ps, c2)
```

* **Line 678, replacement.** Before: `def control_cases(sample, counts):`. After: `def control_cases(sample, counts, coverage):`.
* **Lines 701–702, replacement.** Before:

```python
    check_boundary(part, part["boundaries"])
    expected_rejection("BOUNDARY_ROTATION", lambda: check_boundary(part, set()), controls)
```

  After:

```python
    check_boundary(part["adjacent"], part["boundaries"])
    dropped = next(iter(part["adjacent"]))
    expected_rejection("BOUNDARY_ROTATION",
                       lambda: check_boundary(part["adjacent"],
                                              part["boundaries"] - {dropped}), controls)
```

* **Lines 739–741, replacement.** Before:

```python
    expected_rejection("INCOMPLETE_TYPE_COVERAGE",
                       lambda: need(set(TYPES[:-1]) == set(TYPES), "INCOMPLETE_TYPE_COVERAGE"),
                       controls)
```

  After:

```python
    missing_coverage = {key: value for key, value in coverage.items()
                        if key != (p, TYPES[-1])}
    expected_rejection("INCOMPLETE_TYPE_COVERAGE",
                       lambda: require_type_coverage(missing_coverage), controls)
```

* **Before line 745, insertion:**

```python
def require_type_coverage(coverage):
    for p in PRIMES:
        for typ in TYPES:
            records = coverage.get((p, typ), [])
            generic = {x["variant"] for x in records if x["family"] == "generic"}
            need(generic == {0, 1}, "INCOMPLETE_TYPE_COVERAGE", (p, typ))


```

* **Lines 812–816, replacement.** Before:

```python
    for p in PRIMES:
        for typ in TYPES:
            records = coverage.get((p, typ), [])
            generic = {x["variant"] for x in records if x["family"] == "generic"}
            need(generic == {0, 1}, "INCOMPLETE_TYPE_COVERAGE", (p, typ))
```

  After: `    require_type_coverage(coverage)`.
* **Line 820, replacement.** Before: `    controls = control_cases(sample, counts)`. After: `    controls = control_cases(sample, counts, coverage)`.

## Second edit: snapshot `88D7`

* **After line 623, insertion**, immediately inside `for p in PRIMES:` and before the pre-existing `for d in range(1, p):` loop:

```python
        for a in range(p):
            for u in range(p):
                first = [(a, 1), (u, 0), (a, 1), (a, 1)]
                second = [(a, 1), (a, 1), (u, 0), (a, 1)]
                for word, triple, rot, slot in (
                    (first, (0, 2, 3), 1, 0),
                    (second, (0, 1, 3), 2, 1),
                ):
                    need(bool(set(check_local(word, triple, rot, slot, p))),
                         "EMPTY_CONSTANT_BLOCK")
                    counts["constant_rotated_blocks_checked"] += 1
```

* **Line 762, replacement.** Before:

```python
              "field_Dd_De": 0, "field_rich_direction_pairs": 0,
```

  After:

```python
              "field_Dd_De": 0, "field_rich_direction_pairs": 0,
              "constant_rotated_blocks_checked": 0,
```

## Third edit: snapshot `5D69`

* **After line 688, insertion:**

```python


def compare_dp(actual, exhaustive):
    need(actual == exhaustive, "GENERAL_DP_MISMATCH")
```

* **After line 693, insertion**, immediately after `    p = 7` inside `control_cases`:

```python
    tiny = [(i % p, i % 2) for i in range(2 * p + 2)]
    dp = general_group_dp(tiny, p)
    exhaustive = [[0, 0] for _ in range(2 * p + 1)]
    for indices in itertools.combinations(range(len(tiny)), 2 * p):
        group = product(tiny, indices, p)
        rotations = sum(tiny[i][1] == 0 for i in indices)
        exhaustive[rotations][group[1]] |= 1 << group[0]
        counts["brute_dp_subwords"] += 1
    compare_dp(dp, exhaustive)
    mutated_dp = [pair[:] for pair in dp]
    mutated_dp[0][0] ^= 1
    expected_rejection("GENERAL_DP_MISMATCH",
                       lambda: compare_dp(mutated_dp, exhaustive), controls)
```

* **After line 735, insertion**, following the duplicate-position negative control:

```python
    expected_rejection("SELECTOR_LENGTH",
                       lambda: validate_selector(part, selected[:-1],
                                                 sample["protected"]), controls)
    missing_rotation = sample["rotations"][0]
    extra_reflection = next(i for tri in part["triples"] for i in tri
                            if i not in set(selected))
    wrong_count = [i for i in selected if i != missing_rotation] + [extra_reflection]
    expected_rejection("ROTATION_COUNT",
                       lambda: validate_selector(part, wrong_count,
                                                 sample["protected"]), controls)
```

* **Line 774, replacement.** Before: `              "constant_rotated_blocks_checked": 0,`. After: `              "constant_rotated_blocks_checked": 0, "brute_dp_subwords": 0,`.

## Limits

The tool snapshots above are ordinary edit anchors, not cryptographic hashes or independent freeze receipts. The inline edit history records the exact changed lines and operations available to this author; it does not reconstruct or certify the full lost initial file bytes. No checker run, test, linter, formatter, solver, proof replay, PASS/FAIL, or observed runtime is claimed. The current final source and report must remain preserved, and any correction requires a new successor file.
