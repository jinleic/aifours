# Erratum 1 to `proof/float-audit-v1.md`

**Amends:** `proof/float-audit-v1.md`, sha256 e04753f858865dc4477dd3575f3833a02e943a97f83a33d6333ddac172851c8c. That file
is kept unchanged.

**Cause:** hostile delta review `review/me3-charts-v2-delta-codex-v1.note.md` (sha
df03a74a1be4f5c50d931463507f7e2859010b96ca0e60895167dcd2fe2ce474), finding 6 (MINOR). Non-strict comparisons can be
True for coincident exact singleton balls, so "comparisons of overlapping balls are False" is too broad.

**Scope:** wording of the comparison contract only. No site disposition, defect count or conclusion of the audit
changes.

## Exact change (LF169–170 of float-audit-v1.md)

```diff
-* Every acceptance is a positive certified ball comparison: `<`, `>`, `>=` or `<=`, all of which are False when the
-  balls overlap or are non-finite (smoke B5–B6).
+* Every acceptance is a positive ball comparison `<`, `>`, `>=` or `<=` (Arb arb_lt/le/gt/ge via python-flint). Such a
+  comparison returns True only when the relation is certified, i.e. holds for every pair of points of the two stored
+  balls. A False result carries no information: it may also occur when the relation holds, e.g. at a touching
+  endpoint once a union radius has been rounded upward. Consequences:
+  * a strict comparison of overlapping balls is False;
+  * a non-strict comparison of overlapping balls is True only when the relation still holds for every pair, e.g.
+    for equal exact points (`1 <= 1` is True);
+  * every comparison involving an indeterminate ball is False. Such balls have a NaN midpoint and arise from a
+    quotient by a ball containing 0, or a log of a ball containing 0; on this build that includes log of exact 0.
+
+  Observed on the installed build: smoke s04 (`code/binding_smoke_v4.py`, checks B10a–B10f all pass, B10g
+  information) and s02 B5–B6. Smoke s03 is kept as a failed attempt: its B10a wrongly expected a union-built [1, 2] to
+  satisfy `<= 2`.
+* Two sites select a value on a False outcome instead of rejecting: `me3dual_v6.py` lines 143 and 154,
+  `Cp = arb(Cv.upper()) if Cv.upper() > 0 else arb(0)` (likewise with `Cm`).
+  * The comparison is between the exact, zero-radius, upward-rounded bound `upper()` and 0, so it is decided exactly
+    (smoke s02 B8_upper: `upper()` has radius 0).
+  * Both outcomes give Cp ≥ max(sup C, 0), which is what the SWB inequality needs.
+* The `is_finite()` branches (`me3dual_v4.py` W_enclosure; `me3dual_v6.py` test_bedge; `me3dual_v9.py` test_corner)
+  set the result to the intersection of two valid enclosures u, v of the same quantity when u.is_finite(), and to v
+  otherwise. Each outcome is therefore a valid enclosure, given Arb's sound intersection, a trusted import. If the
+  result is indeterminate, every later comparison is False and the box is rejected.
```

LF171–176 are unchanged and remain correct. Negated comparisons occur only on rejection or fallback paths, so an
indeterminate evaluation can lead only to a split or a FAIL, never to an acceptance.

**Related wording:**
* The docstring of `code/binding_smoke_v2.py` (B5: "Comparisons of overlapping balls are False in both directions")
  carries the same overstatement. Its check itself is correct, because it tests balls overlapping in their interiors.
  It is superseded by the contract stated in `code/binding_smoke_v4.py`.
* Proof v4 §6 (LF168) is corrected in proof v5 §6.
