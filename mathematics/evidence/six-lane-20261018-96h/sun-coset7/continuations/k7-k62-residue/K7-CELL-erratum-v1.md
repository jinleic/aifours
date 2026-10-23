# K7-CELL-erratum-v1: four corrections to K7-CELL-v1 (no statement change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T07:40:17-0700.
- **Overlays:** `K7-CELL-v1.md` sha256 d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae, frozen byte-identical.
- **Source:** author's own re-read immediately after freezing (no review yet). No computation.
- C.1 states the coprimality of odd parts used in Lemma EQ; C.2 removes a citation of Lemma CELL (iii) whose hypothesis
  (distinct K-cosets) is what the step proves, and records that only CELL (i) and Sun(3) are used; C.3 is a typo;
  **C.4 corrects the configuration in which LFC (d) at t is applied in Theorem K7-CELL-B (C^alpha*, not C^alpha).**

**Item C.1.** Old:

```text
(local indices 4 times an odd number)
```

New:

```text
(local indices 4 times an odd number; the odd parts of all local indices involved are pairwise coprime, as they are products of distinct w's and of 3^A 5^Bt for t)
```

**Item C.2.** Old:

```text
Lemma CELL (iii) applied to the vertex t (with
  N_t = 2 3^A 5^Bt w_t) excludes it.
```

New:

```text
these three pieces are pairwise disjoint left cosets of subgroups of K cap L after translation; this uses only part (i)
  of Lemma CELL (which needs U_xK = G for an L-vertex x, not the distinctness of the K-cosets) and Sun(3), and excludes it.
```

**Item C.3.** Old:

```text
So v1, v2, t occupy the three K-coset and Lemma CELL applies.
```

New:

```text
So v1, v2, t occupy the three K-cosets and Lemma CELL applies.
```

**Item C.4.** Old:

```text
LFC (d) at t in C^alpha (labels a: 4w; v with alpha*_tv = 1: w)
```

New:

```text
LFC (d) at t in C^alpha* (the inverted configuration, whose alpha-matrix is alpha*; labels a: 4w; v with alpha*_tv = 1: w)
```

No other change. Every statement of K7-CELL-v1 is unchanged; it remains a conditional candidate.
