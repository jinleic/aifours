# Float-contamination audit of the certified evaluator code — v1

Worker `MathPhaseType3`, 2026-10-18 PDT. This follows hostile review `review/me3-charts-codex-v1.note.md` (sha
55caa19e…acfb), finding 1 (FATAL), and the parent's request for a static audit of all chart and primal evaluator code.
An independent second audit by a separate subagent is in `independent-float-audit/` (cross-check in proof v4).

## Method

* **Static, exhaustive** (run f01, `code/audit_float_v1.py` sha d7a519f8…11bd; `runs/f01-float-audit/static_sites.txt`
  sha df2378d4…03e1, `static_sites.json` sha 57063bc1…2d8f). The 17 files below were parsed with `ast`. Every site of
  each of these classes was listed (269 sites):
  * true division `/`: 198;
  * `**`: 34;
  * `float()` / `round()`: 16;
  * `math.*` calls: 12;
  * float literals: 6;
  * `import math`: 3.
* **Dynamic type trace** (supporting evidence only; same run, `trace.json` sha 556491fd…7144).
  * The evaluator modules and the drivers' definition prefixes were loaded from source with every `+ - * / **`
    rewritten to record (left, right, result) types.
  * Evaluated on 120 recorded leaves per chart plus up to 256 coarse initial cells per chart (to exercise rejection
    branches). Every recomputed leaf outcome equals the recorded one (0 mismatches).
  * 906 binary-operation sites were traced and 472 exercised.
  * Flagged (a float operand or result, or int/int `/`): only 10 sites, all in the G-chart TRIANGLE-angle heuristic of
    `cert_dual_v5.py` (lines 49–52, 68, 70). Disposition below: OK-heuristic.
* **Trusted versus audited.**
  * Trusted import: the outward-correct FLINT 3.6.0 / Arb ball arithmetic.
  * Python-binding behaviours relied on (exact entry of Python ints, fmpq → enclosing ball, float → exact binary
    value, False comparisons on overlap or non-finite balls, union, intersection, upper()): smoke-tested on the
    installed build in run s02 (`code/binding_smoke_v2.py`; all 16 checks true). v1, run s01, is kept: its big-int
    check wrongly expected `==` for a 133-bit integer at 128-bit precision.
  * Runtime identity: run r01 (`runs/r01-runtime/runtime.json`).

Dispositions:
* **OK-exact**: the operands are flint types (arb, acb, fmpq) or jets, or one of them is a Python int; the operation
  is exact (fmpq) or an outward-rounded ball operation.
* **OK-heuristic**: floats only choose a candidate that is then checked exactly.
* **OK-reporting**: printed or recorded, never used in a decision.
* **DEAD**: not on any certified path.
* **DEFECT**: as stated.

Certified paths:
* P: `cert_primal_v3` + `me3lib_v1` + `me3jet_v1`.
* G, SWB, LW, LD1, LD2: `cert_dual_v5` + `me3dual_v7` → `me3dual_v6` → `me3dual_v4` / `me3dual_v3` + jets.
* SWC (rerun d03): `cert_dual_v7` + `me3dual_v9` + jets.
* The invalid SWC run d02 used `cert_dual_v6` + `me3dual_v8`.

## Result

**DEFECT class (one): corner-series coefficients `3 * (-1) ** j / j` (int/int → float).** Four sites:
* `me3dual_v8.py:28` — on the certified path of d02-SWC, so **d02 is INVALID**, as the review found. It is kept as
  failed evidence.
* `me3dual_v7.py:35`, `me3dual_v3.py:220` and `me3dual_v3.py:217` — DEAD: used only by the exploratory SWC
  calibrations k02–k04. Line 217's value `3 * (-1) / 1` is exactly −3.0, but it is float-typed.
* Repair: `me3dual_v9.py:37` `(-2 * RE(pk) + 3 * (-1) ** j) / j`. Traced types are acb/int → acb and J/int → J.
* Controls in run n04:
  * at s = 0 and ξ = 1/2 the exact truncated value Ig₂₀ = 1048575/524288 is contained in the v9 ball and excluded by
    the v8 ball;
  * the v9 corner test still FAILs at T′ = 3/10 (70 FAIL boxes);
  * the v9 corner test certifies a positive-control cell at T.
* The SWC rerun d03-SWC under the newly frozen `spec_dual_v3.json` is certified. Its leaf record is byte-identical
  to d02's (same leaves and outcomes; sha256 0b0f7640…db75), so no decision of d02 was flipped by the rounding.
  Validity rests on d03.

**No other site can inject float rounding into a certified decision or into box geometry.**

## Per-file dispositions (every static site; line numbers of the listed file)

### `cert_primal_v3.py` (chart P driver) — 18 sites
* 54 `1 / (1 + R*Wv - I*Wv)` (int/acb, int/J) and 55 `(R - I)/(1 + R*R)` (acb/acb, J/J): OK-exact.
* 90 (three midpoints) and 91 (six half-widths): `(lo ± hi)/2` with fmpq/int → fmpq. OK-exact.
* 116 `(lo + hi)/2` in `children`, statically fmpq/int, since boxes are tuples of fmpq built at 128–129: OK-exact.
* 128–129 initial cells `reg + (hi − lo)·idx/nsplit`, fmpq·int/int → fmpq: OK-exact.
* 161–162 `float(iv[0])`, `float(iv[1])`: OK-reporting (DPOS bounding box in `primal.json`).
* 166, 177 `round(time…)`: OK-reporting.
* Spec ingestion: `Q()` accepts only int or "a/b" strings; a decimal raises ValueError. So JSON floats cannot enter.

### `me3lib_v1.py` — 3 sites
* 22 `one / acb(…)` (acb/acb) and 23 `acb(r, −1)/(1 + r*r)` (acb/arb): OK-exact.
* 50 `S_point` division: DEAD (never called).

### `me3jet_v1.py` — 13 sites (jets: P MVF, G, SWB MVF, SWC)
* 46–48, 51–52, 66: acb/acb, arb/arb, acb/int, int/acb, int/arb — all OK-exact, and all traced.

### `me3jet_v2.py` — 1 site
* 9 `1 / (2*r)` in `SQRT` (int/acb): OK-exact, but DEAD for certified runs (only the v7 corner uses `SQRT`).

### `me3dual_v3.py` — 70 sites
* On certified paths (traced):
  * 54 `sym` (fmpq/int);
  * 115, 117 `test_largew` (LW: acb/acb, acb/arb);
  * 129 `Pb / Pv` and 133 `arb.pi() / 2` in `_ld_ratio_small_beta` (LD1/LD2 via `me3dual_v6._ld_common`).
  * All OK-exact.
* DEAD (superseded before any certified run; calibration only):
  * `W_generic` 46;
  * `test_general` 77, 92 (×3), 102, 105 (superseded by `me3dual_v4.test_general`);
  * `test_ld1` 143 (×3), 152, 159 and `test_ld2` 186, 192, 199, 201 (superseded by v6);
  * `corner_series_generic` 214, 215, 217 (×2), 220 (×2), and the `**` at 220;
  * `test_corner` 239, 245 (×2), 246 (×2), 254 (×3), 264 (×3), and the `**` at 245 (×2) and 246 (×2);
  * `gk_real_generic` 279, 280 (×2), 281 (×2), 282 (×2);
  * `test_bedge` 292, 293, 294, 300 (×2), 304 (×2), 308 (×2), 316 (×2), 317 (×2), and the `**` at 295 (×3), 296 (×3)
    and 299 (superseded by `me3dual_v6.test_bedge`).
  * Apart from the DEFECT lines 217 and 220, their operand types are those of the live analogues (OK-exact if
    executed).

### `me3dual_v4.py` — 19 sites
* Certified (G; traced):
  * `W_generic` 28 (int/acb, int/J), 29–31 (acb/acb, J/J);
  * `W_enclosure` 38 (×3, fmpq/int);
  * `test_general` 67, 86, 89 (arb/arb).
  * All OK-exact.
* DEAD: `test_ld1` 107 (×3), 116, 123 and `test_ld2` 145, 151, 158, 160 (superseded by v6).

### `me3dual_v6.py` — 42 sites (LD1, LD2, SWB; all traced)
* `_ld_common` 50, 55, 57 (arb/arb); `test_ld1` 65 (×3, arb/arb); `test_ld2` 85, 87 (acb/arb): OK-exact.
* `gk_real` 98–101: the `Nt/N1`-type divisions (arb/arb, J/J) and `3/z`, `3/(z*z)`, `6/(z*z*z)` (int/arb, int/J).
  OK-exact.
* `test_bedge`:
  * 115, 116 (arb/acb) and 117 `1/abs(zR)` (int/arb);
  * the `**` at 118 (×3), 119 (×3) and 122 (arb ** int);
  * 123 (×2), 129 (×2), 137 (×2), 141 (×2), 150 (×4), 151 (×3): arb/int, where the ints are 2, 6, 24, 120.
  * 125 (×2) midpoints (fmpq/int).
  * All OK-exact.

### `me3dual_v7.py` — 18 sites
* `corner_series_stable` 29, 30, 31, 35 (×2), the `**` at 35, and `test_corner` 54, 60 (×2), 61 (×2), 64 (×3), with
  the `**` at 60 (×2) and 61 (×2): DEAD. The corner was never certified with v7 (k04 calibration only).
* 35 `3 * (-1) ** j / j` is a DEFECT (dead). The rest of the file is re-exports.

### `me3dual_v8.py` — 16 sites
* 28 `3 * (-1) ** j / j`: **DEFECT on certified path d02-SWC → d02 INVALID**.
* Others are OK-exact by type: 24 (acb/acb, J/J), 47 (arb/arb), 53–54 (arb/arb; `**` arb ** int), and 57 (×3,
  fmpq/int).

### `me3dual_v9.py` — 15 sites (SWC rerun d03; all traced)
* 33 (acb/acb, J/J); **37 `(-2*RE(pk) + 3*(-1)**j) / j`** (acb/int, J/int); the `**` at 37 (`(-1) ** j`, int/int → int,
  j ≥ 1).
* 56, 62 (×2), 63 (×2) (arb/arb; `**` arb ** int) and 66 (×3, fmpq/int).
* All OK-exact.

### `cert_dual_v5.py` (G, SWB, LW, LD1, LD2), `cert_dual_v6.py` (d02, invalid), `cert_dual_v7.py` (SWC d03) — 16 sites each
* 38 `kap = arb(1 / (1 + T))`: int/fmpq → fmpq (50/61) → enclosing ball. OK-exact.
* 14 `import math`; 51 `0.5`; 52 `math.cos/sin/exp`; 68 `float(…)/float(…)`; 70 `math.floor(th*10000)` and `1e-6`:
  **OK-heuristic**.
  * They are used only for kind G, to pick the TRIANGLE angle θ′ = fmpq(⌊10⁴·th⌋, 10⁴).
  * Since `theta1_float` starts its bisection at lo = π and only raises lo, th ≥ π, so θ′ ≥ 31415/10⁴ > 0.
  * TRIANGLE validity needs only θ′ ≥ 0; the review concurs. θ′ then enters as an exact rational ball.
  * For SWC (kind C) this code is not executed.
* 123 split midpoint `(lo + hi)/2` (fmpq/int): OK-exact.
* 134, 145 `round(time…)`: OK-reporting.
* Spec ingestion as in the primal driver (`Q()`). All spec numbers are strings "a/b" or ints; there are no JSON
  floats.

### Coverage checkers
* `check_cover_v1.py` 40, 41, 58 and `check_cover_v2.py` 47: Fraction arithmetic. OK-exact.
* `check_cover_v3.py` 92 `arb.pi() / 2` (arb/int) and 123 (Fraction): OK-exact.
* The skip-d rule uses arb balls: 53-bit default precision in v2 and 128 bits in v3. A True comparison is certified
  in either case.

### `lane_guard.py` and `run_v1.sh`
* `lane_guard.py` contains no arithmetic. On import it replaces `os.remove`, `os.unlink`, `os.rmdir`,
  `os.removedirs`, `os.replace`, `os.rename`, `shutil.rmtree`, `shutil.move` and the `tempfile` creators with a
  raising stub. `xopen` is `open(path, 'x'|'xb')` and `new_dir` is `os.makedirs(exist_ok=False)`. It has no effect
  on numerics.
* `run_v1.sh` does integer disk-gate arithmetic and float wall time (OK-reporting) only.

## Acceptance logic (non-float, for completeness)

* Every acceptance is a positive certified ball comparison: `<`, `>`, `>=` or `<=`, all of which are False when the
  balls overlap or are non-finite (smoke B5–B6).
* Negated comparisons occur only on rejection or fallback paths:
  * `if not (…): return False`;
  * `_ld_ratio_small_beta` returning None;
  * the corner `corner-img` rejection.
* Intersections are guarded by `is_finite()`. The SWB naive and MVF paths require finite B, C, M₄ and M₅.
* So an indeterminate evaluation can only lead to a split or a FAIL, never to a CERT, SGE, DPOS, INFEAS or SKIP.
