# K7-A2-ZT5-erratum-v1: Theorem K7-ZT5-A withdrawn (gap); two repairs in K7-ZT5-B; map and package updated

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T07:59:04-0700.
- **Owner:** Sun7K62Successor. Author's self-review; no computation.
- **Overlays (frozen, not modified):** `K7-A2-ZT5-A-v1.md` 4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919; `K7-A2-ZT5-B-v1.md`
  f482090adae221ea7bcaa23e1102aa4d3d4081933fd762f756f190d4ddf1f3a8; `K7-family-closure-map-v1.md` 922572acd826c3e18ef661c50a617c197c9623e287f560d3e3eae2108b43a81e;
  `review-package-A2-ZT5-v1.md` 75146e9faf7db2be4b337a5b8ec75e01a43f0a61c09facefe7cd274a47280157.

## The gap (item ZA.1)
Theorem K7-ZT5-A transfers K7-CASEA-K23 and K7-CELL-A to (a2-zt5) with T* = W. Both sources assume that every W-W and
W-t entry of **alpha*** lies in {1,2,4} (A1-STRUCT Corollary W3 and Lemma E3 for alpha*, which in (a1) come from the
second statement of Theorem K7-D23-RICH). In (a2-zt5) the alpha*-rows have only the z-free / t-free granularity of Lemma
FG-zf: the R3-survivor weights vanish on t, so they give "every fibre containing t and another vertex contains z" but
not L*_t subset L*_z (fibres with S_C = {t} may be light), and several R3 kills use weights positive on both z and t.
So W3* = empty and alpha*_ut != 3 are **not established** in (a2-zt5), and the audit of Theorem K7-ZT5-A is incomplete.
The theorem is withdrawn; the branch T* = W of (a2-zt5) is OPEN. Lemma FG-zf and Lemma ZS are unaffected (ZS uses only
the alpha-side W3 argument, with full granularity for alpha-rows, TZ (i) and Lemma B for alpha-rows).

Theorem K7-ZT5-B does not use W3* = empty: its alpha*-entries on W are a-a (<= 2, as alpha = 4), v1 v2 (<= 2), a-v
(3 or 4, treated explicitly) and t-a (treated in Step 2, with the repair ZB.1). It stands as a conditional candidate.

## Replacements (verbatim Old -> New)

**Item ZA.1.** `K7-A2-ZT5-A-v1.md`, Theorem K7-ZT5-A statement. Old:

```text
**In (a2-zt5) there is no configuration with T* = W.**
```

New:

```text
**[WITHDRAWN by `K7-A2-ZT5-erratum-v1.md` item ZA.1: the audit below omits the alpha*-side prerequisites; the branch
T* = W of (a2-zt5) is OPEN.]** Former statement: in (a2-zt5) there is no configuration with T* = W.
```

**Item ZA.2.** `K7-A2-ZT5-A-v1.md`, section 4 scope. Old:

```text
Proved (accepted imports + A2-FIVE as amended): Lemma FG-zf, Lemma ZS. Conditional: Theorem K7-ZT5-A. Open: the branch
```

New:

```text
Proved (accepted imports + A2-FIVE as amended): Lemma FG-zf, Lemma ZS. Theorem K7-ZT5-A is withdrawn (item ZA.1). Open: the
branch T* = W, and the branch
```

**Item ZB.1.** `K7-A2-ZT5-B-v1.md`, Step 2 (ii). Old:

```text
If it is not (2,2,4,4 | 4), it is R1*, R1-* or R5* (or the
```

New:

```text
If alpha*_ta = 3, t's label 3^(A+1) w_t meets only z and y = (fours 1/2, t 1) has value 7 (FG-zf, y_z = 0); otherwise, if it
is not (2,2,4,4 | 4), it is R1*, R1-* or R5* (or the
```

**Item ZB.2.** `K7-A2-ZT5-B-v1.md`, Step 2 (iii). Old:

```text
with value 4 + e*/3, so e* = alpha*_ta <= 2 (FG-zf, y_z = 0).
```

New:

```text
with value 4 + e*/3, so e* = alpha*_ta <= 3 (FG-zf, y_z = 0; e* = 4 gives 16/3).
```

**Item MAP.1.** `K7-family-closure-map-v1.md`, edge E-a2-7. Old:

```text
| E-a2-7 | (a2-zt5), T* = W -> empty | Thm K7-ZT5-A | `K7-A2-ZT5-A-v1.md` | pending | (3) |
```

New:

```text
| E-a2-7 | (a2-zt5), T* = W -> empty | Thm K7-ZT5-A | `K7-A2-ZT5-A-v1.md` | **WITHDRAWN (gap; erratum ZA.1): OPEN** | - |
```

**Item MAP.2.** `K7-family-closure-map-v1.md`, section 2 (iv). Old:

```text
by (iv) and inversion it may be called alpha.
```

New:

```text
by inversion it may be called alpha.
```

**Item PKG.1.** `review-package-A2-ZT5-v1.md`, section 5 scope. Old:

```text
- (a2) only: (a2-no5) through the named-claim transfer; (a2-zt5) through Theorems K7-ZT5-A and K7-ZT5-B.
```

New:

```text
- (a2) only: (a2-no5) through the named-claim transfer; (a2-zt5) with |T*| = 3 through Theorem K7-ZT5-B. Theorem K7-ZT5-A
  is WITHDRAWN (erratum ZA.1); only Lemmas FG-zf and ZS of that file remain under review; the branch T* = W is OPEN.
```

## Effect
- Conditional chain of the closure map: (a2-zt5) with T* = W is now an OPEN node (edge E-a2-7 withdrawn); all other edges
  unchanged. No closure is claimed anywhere.
- ZB.1 closes a missing case (alpha*_ta = 3) in Step 2 (ii); ZB.2 corrects a non-load-bearing bound (e* <= 3, not <= 2);
  the conclusion "a1, a2 fall under (ii)" is unchanged since (iii) gives e* <= 3 < 4.
