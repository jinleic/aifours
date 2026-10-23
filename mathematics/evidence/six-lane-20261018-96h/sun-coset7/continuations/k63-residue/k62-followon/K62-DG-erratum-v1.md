# K62-DG-erratum-v1: wording of section 5 step 3 (no statement change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T06:12:43-0700.
- **Overlays:** `K62-DG-v1.md`, sha256 a4bfc41e832ebc4e77770cab7a8092a3341827cec93a01bfb437c978c1e84f52 (frozen, unchanged).
- **Source:** my own re-read; the frozen sentence on the choice of e is garbled. The Old block below was checked to
  occur exactly once in the frozen file.

**Old:**
```text
3. *Depths.* v2(T*_R) = 3 for all ten R (DG-3). For Q = {c_i, ..., c_(i+3)} take R = {c_i, c_(i+1), c_(i+2)}, e = c_(i+3)
   (choose i so that e is unmarked: the five 4-subsets are rotations, and each 4-subset has at least two unmarked
   vertices among its two ends c_i, c_(i+3) or else use the end c_i with R = {c_(i+1), c_(i+2), c_(i+3)}, which is also
   consecutive): m_e = min(4, 4, 2) = 2, so v2(T*_Q) <= 4 (DG-4).
```

**New:**
```text
3. *Depths.* v2(T*_R) = 1 + v2(4) = 3 for all ten R (DG-3 with tau* = 4). Every 4-subset Q of O is a path
   {c_i, c_(i+1), c_(i+2), c_(i+3)} of the 5-cycle, so every vertex e of Q has a cycle-neighbour in Q, and alpha* = 2 on
   that cycle edge; hence m_e <= 2 for every e in Q. Q has at least two unmarked vertices (at most two O-vertices are
   marked); take one of them as e and R = Q minus {e}: DG-4 gives v2(T*_Q) <= 3 + 1 = 4.
```

Nothing else changes.
