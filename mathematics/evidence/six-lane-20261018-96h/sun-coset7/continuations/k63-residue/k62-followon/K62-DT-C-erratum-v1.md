# K62-DT-C-erratum-v1: correction of one count in section C3 (statements C1-C3 otherwise unchanged)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T06:34:22-0700.
- **Overlays:** `K62-DT-C-v1.md`, sha256 7e8bde21d6f5a162d5ecd5bd5950c90cbcd18763880bd1ee781d240b91f2186b (frozen, unchanged).
- **Source:** my own re-read. The frozen text says "at least 6" tight 4-pairs; for A + C = 1, F = G = 0, H = 4 the
  count is B + D = 10 - 1 - 4 = 5. The Old block was checked to occur exactly once.

**Old:**
```text
In every case at least 6 of the 10 O-pairs are tight 4-pairs ((4,2) or (2,4)), entries 1 occur on at most three
```

**New:**
```text
In every case at least 5 of the 10 O-pairs are tight 4-pairs ((4,2) or (2,4)): B + D >= 5 when A + C = 1
(equality only for F = G = 0, H = 4), B + D >= 6 when A + C = 2, B + D = 7 when A + C = 3; entries 1 occur on at most three
```

Nothing else changes.
