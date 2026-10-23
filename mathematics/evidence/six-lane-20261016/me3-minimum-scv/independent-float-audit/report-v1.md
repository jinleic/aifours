# Independent float-contamination audit v1 — ME3 minimum-SCV certified code

Auditor: `MathPhaseType3.ME3FloatAudit` (independent, read-only). Host clock at writing: 2026-10-18 ~06:30 PDT.
Independence: I did not open `proof/float-audit-v1.md`, `runs/f01-*` or `code/audit_float_v1.py`. One
receipts-wide grep for `"argv"` showed the argv line and two hash lines of `receipts/f01-float-audit-pre.json`.
Nothing else from the lane owner's float audit was read.

## 0. Verdict

* **No DEFECT on any certified call path.** No Python float, float rounding or int/int true division reaches a
  certified acceptance decision or the box geometry of the certified runs c03-primalP (P), d01-G, d01-SWB,
  d01-LW, d01-LD1, d01-LD2, d03-SWC, or the geometry audits a01-coverP and b01-cover-* (b02-cover-SWC used
  check_cover_v2 too).
* The only floats on a live certified path are (a) the G-chart TRIANGLE angle heuristic in `cert_dual_v5.py`
  (chooses an exact rational theta' that only needs theta' >= 0 and is then verified in ball arithmetic) and (b) logs
  and summary fields (elapsed time, DPOS float bounding box).
* **Latent same-class defects in DEAD code** (same bug as the hostile finding at `me3dual_v8.py:28`; no listed
  certified run executes them):
  * `me3dual_v7.py:35` (col 35): `3 * (-1) ** j / j` is int/int, so a float. It is inexact for
    j in {5,7,9,10,11,13,14,15,17,18,19,20} with N = 20. It sits in `corner_series_stable` / `test_corner`, which
    run only for kind "C". The d01 runs (kinds G, B, LW, LD1, LD2) never call it. d03-SWC uses `me3dual_v9`.
    It did run in calibration k04-cal-SWC (cert_dual_v5 + spec_dual_cal_v3). Any SWC certificate built on it would
    be invalid.
  * `me3dual_v3.py:220` (col 27): the same expression in `corner_series_generic`. It ran in calibration k02-cal-SWC
    (cert_dual_v2 + v3) and k03-cal-SWC (cert_dual_v4 + v6, then V3.test_corner). It is not certified.
  * `me3dual_v3.py:217` (col 26): `3 * (-1) / 1` gives the float -3.0, which is exact in value. It is DEAD.
* Counts by disposition, over 556 enumerated sites (section 4): **OK-exact 271, OK-heuristic 20,
  OK-reporting-only 42, DEAD 223, DEFECT 0.**

  | file | sites | OK-exact | OK-heuristic | OK-reporting-only | DEAD | DEFECT |
  |---|---|---|---|---|---|---|
  | cert_primal_v3.py | 45 | 31 | 0 | 14 | 0 | 0 |
  | me3lib_v1.py | 12 | 8 | 0 | 0 | 4 | 0 |
  | me3jet_v1.py | 27 | 27 | 0 | 0 | 0 | 0 |
  | me3jet_v2.py | 1 | 0 | 0 | 0 | 1 | 0 |
  | cert_dual_v5.py | 41 | 10 | 20 | 10 | 1 | 0 |
  | me3dual_v7.py | 31 | 1 | 0 | 0 | 30 | 0 |
  | me3dual_v6.py | 87 | 87 | 0 | 0 | 0 | 0 |
  | me3dual_v4.py | 52 | 24 | 0 | 0 | 28 | 0 |
  | me3dual_v3.py | 157 | 18 | 0 | 0 | 139 | 0 |
  | cert_dual_v7.py | 41 | 11 | 0 | 10 | 20 | 0 |
  | me3dual_v9.py | 28 | 28 | 0 | 0 | 0 | 0 |
  | check_cover_v1.py | 13 | 9 | 0 | 4 | 0 | 0 |
  | check_cover_v2.py | 20 | 16 | 0 | 4 | 0 | 0 |
  | lane_guard.py | 1 | 1 | 0 | 0 | 0 | 0 |
  | **total** | **556** | **271** | **20** | **42** | **223** | **0** |

  run_v1.sh and the three spec JSONs are audited in sections 1 and 3; they are not part of the 556 count.
* Non-float issues are in section 6. None affects a live certified path. The NaN-permissive B-edge acceptance in
  DEAD `me3dual_v3.test_bedge` (lines 309-311, 319-320) is guarded in the live `me3dual_v6.test_bedge`.

## 1. Scope, provenance, method

The file hashes below match the `code_sha256` entries in the pre-run receipts c03-primalP, d01-{G,SWB,LW,LD1,LD2},
d03-SWC, a01-coverP and b01-cover-*, so the audited text is the code that ran. The interpreter was 3.14.3 with
flint 0.9.0 (receipts).

| file | sha256 | lines | coverage |
|---|---|---|---|
| code/cert_primal_v3.py | b541a8c5…f213 | 180 | all lines read; all 45 sites listed |
| code/me3lib_v1.py | 4827676a…eaa6 | 50 | all lines read; 12 sites |
| code/me3jet_v1.py | 0db15d1b…77e6 | 102 | all lines read; 27 sites |
| code/me3jet_v2.py | a4f757c3…fc87 | 11 | all lines read; 1 site |
| code/cert_dual_v5.py | b2fcab98…855d | 148 | all lines read; 41 sites |
| code/me3dual_v7.py | b2f80d14…1895 | 81 | all lines read; 31 sites |
| code/me3dual_v6.py | de48c84f…2aaa | 157 | all lines read; 87 sites |
| code/me3dual_v4.py | ffff3d61…da4c | 174 | all lines read; 52 sites |
| code/me3dual_v3.py | 94ca521e…74c9 | 322 | all lines read; 157 sites |
| code/cert_dual_v7.py | 72fb546a…4f3f | 148 | all lines read; 41 sites |
| code/me3dual_v9.py | 77a826c0…d341 | 83 | all lines read; 28 sites |
| code/check_cover_v1.py | dd2d7bb3…9b0e | 113 | all lines read; 13 sites |
| code/check_cover_v2.py | 8781c33b…1f3c | 121 | all lines read; 20 sites |
| code/lane_guard.py | 5589b0a7…a484 | 34 | all lines read; 1 site; import-time effects only on os/shutil/tempfile; no numerics, no flint |
| code/run_v1.sh | 0cfcb20c…af40 | 85 | all lines read (section 6) |
| code/spec_primal_P_v1.json | 6339c775…759c | — | every leaf typed (section 3) |
| code/spec_dual_v1.json | 23dd1dad…f6c1 | — | every leaf typed |
| code/spec_dual_v3.json | 43d2e22e…d936 | — | every leaf typed |

**Method.**
1. I read every line by hand and traced the call graph from each driver (section 2).
2. An AST scanner I wrote (`independent-float-audit/code/scan_sites_v1.py`) lists sites by syntax. It ran once
   through the lane launcher as run `s01-scan`; receipts are in `independent-float-audit/receipts/s01-scan-*.json`.
   It found 1040 sites. I classified every site of these kinds: `/`, `//`, `%`, `**`, float literals, `math.*`,
   float(), round(), int(), str(), Fraction(), fmpq(), arb()/acb() constructors, abs(), bool(), `.upper()`,
   time.time(), min/max, divmod, json load/dump, default arguments, and comparisons with float operands.
   That gives 556 sites. Per-file totals equal the scanner's per-kind counts.
3. Remaining scanner rows were checked but are not tabulated: other comparisons (section 5 covers the acceptance
   ones), imports, len/range/open, and transcendental ball methods.
4. The scanner found no `//`, no negative or float exponents, no augmented `/=`, and no float constants in
   comparisons. It found no numpy, mpmath or decimal imports; `math` is imported only by cert_dual_v5/v7.

**Semantics assumed** (given trusted facts, plus standard Arb/Python facts; not executed by me):
* Python ints convert exactly; Python floats convert as their binary value.
* fmpq arithmetic is exact, including fmpq/int and int/fmpq.
* arb/acb arithmetic is outward-rounded. `arb(fmpq)` and arb-op-fmpq give enclosures (arb_fmpz_div_fmpz).
* Ball comparisons are True only when certain. `arb.upper()` returns an arb, not a float.
* `fractions.Fraction` arithmetic is exact, and Fraction/int stays a Fraction.
* In Python 3.14, int/int returns a float.
* json parses numbers containing `.`, `e`/`E`, NaN or Infinity as float, and every other number as int.

Type keys used in the tables: Q = fmpq, I = Python int, F = Python float, R = arb, C = acb, J = me3jet_v1.J jet
(acb components; real-arb components for me3dual_v6._rjets2), Fr = Fraction, S = str.

## 2. Certified call graph (traced from the drivers) and DEAD map

* **c03-primalP**: `cert_primal_v3` calls Q, ball, classify, split_dim, children and the initial-cell loop.
  classify calls me3lib_v1.g_feas and primal_G_D (which calls primal_terms), and calls me3jet_v1.mvf on
  primal_GD_generic, which uses EXP, RE and the J operators. `me3lib_v1.S_point` is DEAD.
* **d01-G**: `cert_dual_v5`.evaluate, kind G, does three things:
  * applies SKIP:in-primal-P (exact Q);
  * runs theta1_float plus line 70 (float heuristic);
  * calls D.test_general, which is me3dual_v7, then v6, then v4.test_general. That calls W_enclosure, which uses
    v4.W_generic, v3.N1f, v3.ball, v3.sym, jet_inputs and the J operators. It also uses v4._branch, v4.twopi,
    LOG/RE/IM and mvf.
* **d01-SWB** (kind B): v6.test_bedge calls v6.gk_real, v6._rjets2, LOG, the J operators, v3.ball and v3.sym.
* **d01-LW**: v6.test_largew is v3.test_largew, which uses v3.ball and v3.N1f.
* **d01-LD1 / d01-LD2**: v6.test_ld1 and v6.test_ld2 use v3.ball, v3.N1f and v6._ld_common, which calls
  v6._arg_candidates, v6.twopi and v3._ld_ratio_small_beta. LD2 also applies the skip-s and skip-d rules.
* **d03-SWC**: `cert_dual_v7`.evaluate, kind C only, calls v9.test_corner, which uses v9.corner_series_v9, RE,
  the J operators, v3.ball, v3.sym, v3.N1f and mvf. The kind-G branch of cert_dual_v7, including theta1_float,
  is DEAD for d03.
* **Audits**: a01-coverP ran check_cover_v1. b01-cover-{G,SWB,LW,LD1,LD2} and b02-cover-SWC ran check_cover_v2.
  b03-cover-* used check_cover_v3.py, which is out of scope and was not read.
* **DEAD in the audited files**, with the runs that did execute them:
  * v7.corner_series_stable and v7.test_corner: calibration k04-cal-SWC.
  * me3jet_v2.SQRT: only via v7.corner_series_stable.
  * v4.test_ld1, test_ld2, test_largew, _ratio_small_beta, test_corner and test_bedge: no run. v6 uses only
    v4.test_general.
  * v3.twopi, Ntf, W_generic, _branch_const, test_general, test_ld1, test_ld2, corner_series_generic, test_corner,
    gk_real_generic and test_bedge: calibration k02-cal-* (cert_dual_v2 + v3). v3.test_corner also ran in
    k03-cal-SWC.
  * The kind-C branch of cert_dual_v5 (line 62): calibration k04-cal-SWC only. The receipts show no d01-SWC run.

## 3. Spec numbers (JSON) and how they are parsed

The scanner walked every JSON leaf.

| spec | leaves | float leaves | ints (path = value) | duplicate keys |
|---|---|---|---|---|
| spec_primal_P_v1.json | 25 | **0** | prec=128, initial_split r/w/phi = 12/80/64, max_depth=40, eval_cap=40000000 | none |
| spec_dual_v1.json | 241 | **0** | prec=128, SWC.series_terms=20, max_depth 28/28/32/24/26/26, eval_cap per chart | none |
| spec_dual_v3.json | 34 | **0** | prec=128, SWC.series_terms=20, max_depth=28, eval_cap=40000000 | none |

* All rationals are strings of the form "int" or "int/int". Examples: T = "11/50", the region ends, breakpoints,
  split weights, and params "1/5", "40", "3", "15708/10000", "1/16", "1/65".
* The only other strings are names, kinds and prose.
* Drivers parse rationals with Q(), which is str, then int, then fmpq. A JSON float would make `int()` raise
  ValueError, so the drivers fail closed.
* The checkers parse with `Fraction(str(x))`, which gives the same value for every string present.
* The ints are used only for these purposes, never as rational data: precision, the split counts (exact Q/I and
  Fr/I divisors), depth and evaluation caps, and N.

## 4. Site tables (every site; L:C = line:col)

Reach keys:
* acc:X = certified acceptance decision in chart X.
* geom = box geometry in a driver; geom-audit = geometry replay in a checker.
* heur:G = TRIANGLE candidate selection in d01-G.
* report = logs or summary JSON only.
* none = not executed in any listed certified run.

### code/cert_primal_v3.py (LIVE: c03)

| sites | kind | expression | operand types | reach | disposition |
|---|---|---|---|---|---|
| 31:7 | CALL:json.load | `json.load(open(sys.argv[2]))` | spec P: 0 float leaves | geom, acc:P | OK-exact |
| 36:8 | CALL:str | `str(s)` in Q | S/I to S | geom, acc:P | OK-exact |
| 39:20, 39:28, 40:16 | CALL:int | `int(a)`, `int(b)`, `int(s)` | S to I (float text rejected) | geom, acc:P | OK-exact |
| 39:15, 40:11 | CALL:fmpq | `fmpq(int(a), int(b))`, `fmpq(int(s))` | I to Q | geom, acc:P | OK-exact |
| 44:5 | CALL:arb | `arb(T)` | Q 11/50 to R | acc:P | OK-exact |
| 48:4 | CALL:acb | `acb(0, 1)` | I | acc:P | OK-exact |
| 54:11 | DIV | `1 / (1 + R * Wv - I * Wv)` | I/C (midpoints), I/J (jets, `__rtruediv__`) | acc:P (MVF) | OK-exact |
| 55:17 | DIV | `(R - I) / (1 + R * R)` | C/C, J/J | acc:P (MVF) | OK-exact |
| 70:11, 70:25 | CALL:arb | `arb(lo)`, `arb(hi)` in ball | Q (box ends, Q half-widths) | acc:P | OK-exact |
| 78:7, 79:29, 79:20 | CALL:arb | `arb(pl)`, `arb(pl)`, `arb(rl)` | Q | acc:P (INFEAS) | OK-exact |
| 90:12, 90:32, 90:52 | CALL:arb | `arb((xl + xh) / 2)` | Q | acc:P (MVF midpoints) | OK-exact |
| 90:16, 90:36, 90:56 | DIV | `(rl + rh) / 2` etc. | Q/I to Q | acc:P | OK-exact |
| 91:15, 91:31, 91:52, 91:68, 91:89, 91:105 | DIV | `-(xh - xl) / 2`, `(xh - xl) / 2` | Q/I to Q | acc:P (MVF half-widths) | OK-exact |
| 116:10 | DIV | `(lo + hi) / 2` children | Q/I to Q | geom | OK-exact |
| 128:44, 129:44 | DIV | `(reg[d][1] - reg[d][0]) * idx[d] / nsplit[d]` | (Q*I)/I, nsplit JSON int | geom (initial cells) | OK-exact |
| 122:5, 166:58, 177:90 | CALL:time.time | `time.time()` | F | report | OK-reporting-only |
| 149:69, 175:55 | CALL:str | `str(x)` FAIL boxes, `str(k)` depths | Q/I to S | report | OK-reporting-only |
| 161:18, 162:18 | CALL:float | `float(iv[0])`, `float(iv[1])` | Q to F | report (dpos_bounding_box_float; descriptive only in me3-theorem-v3.md:100, not used by Lemma M) | OK-reporting-only |
| 163:57 | CALL:min | `min(a, b)` | F | report | OK-reporting-only |
| 164:58 | CALL:max | `max(a, b)` | F | report | OK-reporting-only |
| 165:11 | MOD | `evals % 200000` | I | report | OK-reporting-only |
| 166:52, 177:84 | CALL:round | `round(time.time() - t0, k)` | F | report | OK-reporting-only |
| 179:4 | CALL:json.dump | summary | F only in bbox/elapsed | report | OK-reporting-only |
| 180:17 | CALL:json.dumps | summary | same | report | OK-reporting-only |

### code/me3lib_v1.py (LIVE except S_point)

| sites | kind | expression | operand types | reach | disposition |
|---|---|---|---|---|---|
| 20:10, 21:8, 21:21, 22:17, 23:12, 23:23 | CALL:acb | `acb(1)`, `acb(1, -r)`, `acb(r * phi, -phi)`, `acb(1 + r * w, -w)`, `acb(phi)`, `acb(r, -1)` | I/R | acc:P (naive) | OK-exact |
| 22:11 | DIV | `one / acb(1 + r * w, -w)` | C/C | acc:P | OK-exact |
| 23:23 | DIV | `acb(r, -1) / (1 + r * r)` | C/R | acc:P | OK-exact |
| 49:39, 49:47, 49:55 | CALL:arb | `arb(r)`, `arb(w)`, `arb(phi)` in S_point | caller-dependent | none | DEAD |
| 50:11 | DIV | `2 * a0 * a2 / (a1 * a1)` in S_point | R/R | none | DEAD |

### code/me3jet_v1.py (LIVE: P, G, SWB, SWC mean-value forms)

| sites | kind | expression | operand types | reach | disposition |
|---|---|---|---|---|---|
| 46:16 | DIV | `a.v / b.v` | C/C or R/R | acc:P,G,SWB,SWC | OK-exact |
| 47:25, 47:54, 47:83 | DIV | `(a.d[k] - q * b.d[k]) / b.v` | C/C or R/R | same | OK-exact |
| 48:17, 48:27, 48:39, 48:51 | DIV | `a.v / b`, `a.d[k] / b` (J / non-J) | live divisor only I j (me3dual_v9:37); no float divisor anywhere | acc:SWC | OK-exact |
| 51:12 | DIV | `b / a.v` (`__rtruediv__`) | I/C or I/R; b in {1, 3, 6} | acc:P,G,SWB | OK-exact |
| 52:12 | DIV | `-q / a.v` | C/C or R/R | same | OK-exact |
| 66:29, 66:43, 66:57 | DIV | `x.d[k] / x.v` (LOG) | C/C or R/R | acc:G,SWB | OK-exact |
| 72:17, 72:33, 72:51, 72:69, 73:11, 78:17, 78:33, 78:51, 78:69, 79:11 | CALL:acb | `acb(x.v.real)` etc. (RE/IM) | R | acc | OK-exact |
| 83:8, 84:8, 86:14, 94:16 | CALL:acb | `acb(0)`, `acb(1)`, `acb(b)`, `acb(m)` | I, R | acc (MVF) | OK-exact |

### code/me3jet_v2.py

| sites | kind | expression | operand types | reach | disposition |
|---|---|---|---|---|---|
| 9:12 | DIV | `1 / (2 * r)` in SQRT | I/C | none (SQRT only used by v7.corner_series_stable) | DEAD |

### code/cert_dual_v5.py (LIVE: d01-G/SWB/LW/LD1/LD2)

| sites | kind | expression | operand types | reach | disposition |
|---|---|---|---|---|---|
| 23:7 | CALL:json.load | spec_dual_v1 | 0 float leaves | geom, acc | OK-exact |
| 30:8 | CALL:str | `str(x)` in Q | S/I | geom, acc | OK-exact |
| 33:20, 33:28, 34:16 | CALL:int | Q parse | S to I | geom, acc | OK-exact |
| 33:15, 34:11 | CALL:fmpq | Q parse | I to Q | geom, acc | OK-exact |
| 38:10 | DIV | `1 / (1 + T)` | I/Q to Q 50/61 | acc (kappa, all charts) | OK-exact |
| 38:6 | CALL:arb | `arb(1 / (1 + T))` | Q to R | acc | OK-exact |
| 123:22 | DIV | `(lo + hi) / 2` | Q/I | geom | OK-exact |
| 47:7 | COMPARE | `r <= 0` in theta1_float | F vs I | heur:G | OK-heuristic |
| 48:19, 49:13, 49:26, 70:73 | MODATTR | `math.pi` | F | heur:G | OK-heuristic |
| 51:14, 70:83 | FLOATLIT | `0.5`, `1e-6` | F | heur:G | OK-heuristic |
| 52:11 | CALL:math.cos | `math.cos(mid)` | F | heur:G | OK-heuristic |
| 52:31 | CALL:math.sin | `math.sin(mid)` | F | heur:G | OK-heuristic |
| 52:47 | CALL:math.exp | `math.exp(-r * mid)` | F | heur:G | OK-heuristic |
| 52:11 | COMPARE | `math.cos(mid) - r * math.sin(mid) - math.exp(-r * mid) < 0` | F | heur:G | OK-heuristic |
| 68:13 | DIV | `float((bl + bh) / 2) / float((cl + ch) / 2)` | F/F | heur:G | OK-heuristic |
| 68:19, 68:42 | DIV | `(bl + bh) / 2`, `(cl + ch) / 2` | Q/I (then float()) | heur:G | OK-heuristic |
| 68:13, 68:36 | CALL:float | `float(...)` of Q midpoints | Q to F | heur:G | OK-heuristic |
| 70:29 | CALL:math.floor | `math.floor(th * 10000)` | F to I | heur:G | OK-heuristic |
| 70:25 | CALL:int | `int(math.floor(...))` | I | heur:G | OK-heuristic |
| 70:20 | CALL:fmpq | `fmpq(int(...), 10000)` | I to Q, theta' >= 31415/10000 | heur:G | OK-heuristic |
| 70:64 | COMPARE | `th < 2 * math.pi - 1e-6` | F | heur:G | OK-heuristic |
| 62:58 | CALL:int | `int(cs["series_terms"])` | JSON int | none (kind C; no d01-SWC) | DEAD |
| 93:5, 134:51, 145:32 | CALL:time.time | `time.time()` | F | report | OK-reporting-only |
| 119:69, 119:77 | CALL:str | FAIL boxes | Q to S | report | OK-reporting-only |
| 133:11 | MOD | `evals % 200000` | I | report | OK-reporting-only |
| 134:45, 145:26 | CALL:round | elapsed | F | report | OK-reporting-only |
| 147:4 | CALL:json.dump | dual.json | F only elapsed | report | OK-reporting-only |
| 148:17 | CALL:json.dumps | summary | same | report | OK-reporting-only |

Why OK-heuristic is valid here:
* theta_tri is either None or the exact rational floor(10^4 th)/10^4, with th >= pi. So theta_tri >= 31415/10000,
  which is > 0.
* It enters only `me3dual_v4.test_general:84-92` as `arb(theta_tri)`.
* The TRIANGLE certificate W = a' + b' e^{-xi t'} with a', b' >= 0, a' + b' <= 1 and t' = theta'/w needs only
  t' >= 0 (me3-theorem-v3.md:79). Both 0 = 0·e^0 and 1 = e^{-xi·0} lie in the hull.
* The ball tests at v4:88-91 then decide acceptance rigorously.
* A bad float choice can only make TRIANGLE fail.

### code/me3dual_v7.py (imported by d01 and by d03 via v9; its own corner code is DEAD)

| sites | kind | expression | operand types | reach | disposition |
|---|---|---|---|---|---|
| 20:4 | CALL:acb | `I = acb(0, 1)` (runs at import) | I | value used only by DEAD code | OK-exact |
| 29:8, 30:8 | DIV | `(2*kap*S*S - 2*S*(1 - S)) / N1`, `kap*S*S / N1` | C/C, J/J | none | DEAD |
| 31:8 | DIV | `(-A + I * SQRT(4*B - A*A)) / 2` | C/I, J/I | none | DEAD |
| 35:17 | DIV | `-2 * RE(pk) / j` | C/I | none | DEAD |
| 35:35 | DIV | `3 * (-1) ** j / j` | **I/I to F** (inexact for j = 5, 7, 9, …) | none | DEAD — latent DEFECT (would void any SWC enclosure; ran only in k04-cal-SWC) |
| 35:39 | POW | `(-1) ** j` | I**I, j >= 1 | none | DEAD |
| 54:10, 56:10, 56:20, 56:30, 56:40, 64:12, 64:32, 64:52 | CALL:arb | Bup, `arb(dh)`, `arb(wh)`, midpoints | R/Q | none | DEAD |
| 54:14 | METHOD:upper | `.upper()` | R | none | DEAD |
| 54:15, 60:15, 60:56, 61:14, 61:44, 64:16, 64:36, 64:56 | DIV | B, tails, midpoints | R/R, Q/I | none | DEAD |
| 60:29, 60:60, 61:23, 61:48 | POW | `q1 ** (N - 1)` etc. | R**I | none | DEAD |
| 62:35, 62:44, 62:53 | CALL:acb | `acb(sb)` etc. | R | none | DEAD |

### code/me3dual_v6.py (LIVE: LD1, LD2, SWB; re-exports v4.test_general and v3.test_largew)

| sites | kind | expression | operand types | reach | disposition |
|---|---|---|---|---|---|
| 22:4, 67:21, 70:9, 83:9, 114:9, 115:48, 116:48 | CALL:acb | `acb(0, 1)`, `acb(cb, sn)`, `acb(cos 2b, sin 2b)`, `acb(cos b, sin b)`, `acb(1 + db, -(arb(0).union(whb)))`, `acb(1, ±c0)` | I/R | acc:LD1,LD2,SWB | OK-exact |
| 48:15, 50:15 | CALL:bool | `bool(aW < ...)`, `bool(bl > 0)` | R cmp, Q cmp | acc:LD1,LD2 | OK-exact |
| 50:35, 50:58, 57:18, 57:41, 88:26, 106:11, 106:19, 112:10, 114:23, 123:23, 125:13, 125:33, 143:52, 154:48 | CALL:arb | `arb(0)`, `arb(1)`, `arb(bl)`, `arb(wh)`, `arb(dh)`, midpoints | I/Q | acc | OK-exact |
| 77:7, 77:17, 77:27, 79:12, 79:23, 79:33, 79:46 | CALL:arb | skip-s / skip-d operands `arb(xl)`, `arb(ql)`, `arb(s_max)`, `arb(xh)`, `arb(d_max)`, `arb(bl)` | Q | geom (LD2 SKIP rules; ball comparisons, True only if certain) | OK-exact |
| 143:13, 154:9 | CALL:arb | `arb(Cv.upper())`, `arb(Cm.upper())` | R (finite, guarded at 142/152) | acc:SWB | OK-exact |
| 143:17, 143:32, 154:13, 154:28 | METHOD:upper | `Cv.upper()`, `Cm.upper()` | R to R | acc:SWB | OK-exact |
| 50:48, 57:31, 55:33 | DIV | `twopi() / arb(bl).tan()`, `alpha / tb` | R/R | acc:LD1,LD2 | OK-exact |
| 65:17, 65:37, 65:62 | DIV | w1, w2, w3 `/ N1` | R/R | acc:LD1 | OK-exact |
| 85:9, 87:9 | DIV | `Ph = (...) / N1`, `Pb = (...) / N1` | C/R | acc:LD2 | OK-exact |
| 98:13, 99:9, 100:9, 101:9 | DIV | `Nt / N1`, `Nz / Nt`, g2, g3 quotients | R/R or J/J (real jets) | acc:SWB | OK-exact |
| 99:19, 100:44, 101:67 | DIV | `3 / z`, `3 / (z * z)`, `6 / (z * z * z)` | I/R or I/J | acc:SWB | OK-exact |
| 115:9, 116:9 | DIV | `kap * sb / (...)` | R/C | acc:SWB | OK-exact |
| 117:35 | DIV | `1 / abs(zR)` | I/R | acc:SWB | OK-exact |
| 123:8, 123:23, 129:18, 129:44, 137:22, 137:48, 141:9, 141:19 | DIV | `w4 * M4 / 24`, `... / 120`, `... / 6`, `-g2 / 2` | R/I | acc:SWB | OK-exact |
| 125:17, 125:37 | DIV | `(sl + sh) / 2`, `(dl + dh) / 2` | Q/I | acc:SWB (MVF) | OK-exact |
| 150:10, 150:23, 150:42, 150:60, 151:11, 151:29, 151:43 | DIV | Cm terms `/ 2`, `/ 6` | R/I | acc:SWB | OK-exact |
| 69:9, 69:24, 86:9, 86:38, 117:17, 117:26, 117:39, 129:30, 137:34 | CALL:abs | `abs(...)` of R/C | to R | acc | OK-exact |
| 118:14, 118:24, 118:38, 119:15, 119:25, 119:39, 122:9 | POW | `a1 ** 4` … `whb ** 4` | R**I (4, 5) | acc:SWB | OK-exact |

### code/me3dual_v4.py (LIVE: G via test_general; the rest DEAD)

| sites | kind | expression | operand types | reach | disposition |
|---|---|---|---|---|---|
| 18:4, 37:19, 37:28, 37:37, 41:21, 51:11, 75:25, 87:32 | CALL:acb | `acb(0, 1)`, `acb(sb/db/wb)`, `acb(m)`, `acb(rr, ii)`, `acb(m)`, `acb(th.cos(), th.sin())` | I/R | acc:G | OK-exact |
| 38:12, 38:32, 38:52, 56:15, 85:13 | CALL:arb | midpoints, `arb(0)`, `arb(theta_tri)` | Q/I (theta_tri exact Q) | acc:G | OK-exact |
| 66:9 | CALL:abs | `abs(W)` | C to R | acc:G | OK-exact |
| 28:9 | DIV | `1 / (1 + Dl - I * Om)` | I/C, I/J | acc:G | OK-exact |
| 29:9, 30:9, 31:9 | DIV | w1, w2, w3 `/ N1` | C/C, J/J | acc:G | OK-exact |
| 38:16, 38:36, 38:56 | DIV | midpoints | Q/I | acc:G | OK-exact |
| 67:13 | DIV | `-2 * arb.pi() * db / wb` | R/R | acc:G (SMALL) | OK-exact |
| 86:13, 89:16 | DIV | `db / wb`, `W.imag / Zp.imag` | R/R | acc:G (TRIANGLE) | OK-exact |
| 109:21, 125:13, 143:9 | CALL:acb | v4.test_ld1/test_ld2 | R | none | DEAD |
| 116:16, 116:39, 137:7, 137:17, 137:27, 139:12, 139:23, 139:33, 139:46, 147:14, 151:16, 151:39 | CALL:arb | v4.test_ld1/test_ld2 | I/Q | none | DEAD |
| 111:9, 111:24, 146:9, 146:38 | CALL:abs | v4.test_ld1/test_ld2 | R/C | none | DEAD |
| 107:17, 107:37, 107:62, 116:29, 123:16, 145:9, 151:29, 158:16, 160:13 | DIV | v4.test_ld1/test_ld2 | R/R, C/R | none | DEAD |

### code/me3dual_v3.py (LIVE: N1f, ball, sym, test_largew, _ld_ratio_small_beta; the rest DEAD)

| sites | kind | expression | operand types | reach | disposition |
|---|---|---|---|---|---|
| 29:4 | CALL:acb | `I = acb(0, 1)` (import) | I | used only by DEAD code | OK-exact |
| 50:11, 50:25 | CALL:arb | `arb(lo)`, `arb(hi)` in ball | Q (all live callers pass box ends) | acc (all dual charts) | OK-exact |
| 54:8 | DIV | `h = (hi - lo) / 2` in sym | Q/I (live callers v4:39, v6:126, v9:67 pass Q). It would become int/int only if passed ints; never is | acc:G,SWB,SWC (MVF) | OK-exact |
| 55:11, 55:25 | CALL:arb | `arb(-h)`, `arb(h)` | Q | acc | OK-exact |
| 115:9, 115:19 | CALL:acb | `acb(nb)`, `acb(nb * (1 + db), -1)` | R/I | acc:LW | OK-exact |
| 115:9 | DIV | `acb(nb) / acb(nb * (1 + db), -1)` | C/C | acc:LW | OK-exact |
| 117:8 | DIV | `W = (...) / N1` | C/R | acc:LW | OK-exact |
| 118:7 | CALL:abs | `abs(W)` | C to R | acc:LW (SMALL) | OK-exact |
| 129:9 | DIV | `Pb / Pv` | C/C | acc:LD1,LD2 | OK-exact |
| 133:12, 135:11, 135:24 | CALL:arb | `arb(bh)`, `arb(0)`, `arb(lo.upper())` | Q/I/R | acc:LD1,LD2 | OK-exact |
| 133:22, 135:28 | METHOD:upper | `lo.upper()` (lo >= 0 certain at 131) | R | acc:LD1,LD2 | OK-exact |
| 133:35 | DIV | `arb.pi() / 2` | R/I | acc:LD1,LD2 | OK-exact |
| 217:26 | DIV | `3 * (-1) / 1` | **I/I to F** (-3.0, exact value) | none | DEAD (latent float, harmless value) |
| 220:27 | DIV | `3 * (-1) ** j / j` | **I/I to F** (inexact j = 5, 7, …) | none | DEAD — latent DEFECT (ran only in calibration k02/k03-cal-SWC) |
| 46:11, 77:13, 92:20, 92:40, 92:60, 102:13, 105:16, 143:17, 143:37, 143:62, 152:30, 159:16, 186:9, 192:30, 199:16, 201:13, 214:8, 215:8, 217:15, 220:17, 239:15, 245:15, 245:56, 246:14, 246:44, 254:20, 254:40, 254:60, 264:16, 264:36, 264:56, 279:13, 280:9, 280:19, 281:9, 281:44, 282:9, 282:67, 292:9, 293:9, 294:35, 300:8, 300:23, 304:18, 304:44, 308:9, 308:19, 316:28, 316:37, 317:16, 317:36 | DIV | W_generic, test_general, test_ld1/2, corner, gk_real_generic, test_bedge, Fb | C/C, R/R, R/I, I/C, Q/I | none | DEAD |
| 220:31, 245:29, 245:60, 246:23, 246:48, 295:14, 295:24, 295:38, 296:15, 296:25, 296:39, 299:9 | POW | `(-1) ** j`, `q1 ** (N - 1)`, `a1 ** 4` … | I**I, R**I | none | DEAD |
| 239:14, 310:13, 310:28, 319:14, 319:29 | METHOD:upper | corner Bup, B-edge Cp/Cm | R | none | DEAD (see section 6, item 1) |
| 64:15, 92:16, 92:36, 92:56, 101:13, 152:16, 152:41, 178:7, 178:17, 178:27, 180:12, 180:23, 180:33, 180:46, 188:14, 192:16, 192:41, 239:10, 241:10, 241:20, 241:30, 241:40, 254:16, 254:36, 254:56, 264:12, 264:32, 264:52, 288:10, 291:23, 300:23, 309:9, 309:47, 310:9, 310:48, 317:12, 317:32, 317:52, 318:36, 318:72, 319:10, 319:49 | CALL:arb | DEAD functions | I/Q/R | none | DEAD |
| 74:18, 74:27, 74:36, 93:23, 93:37, 93:51, 103:32, 145:21, 161:13, 184:9, 247:36, 247:45, 247:54, 291:9, 292:48, 293:48, 301:37, 301:46 | CALL:acb | DEAD functions | R/I | none | DEAD |
| 75:9, 147:9, 147:24, 187:9, 187:38, 294:17, 294:26, 294:39, 304:30 | CALL:abs | DEAD functions | C/R | none | DEAD |

### code/cert_dual_v7.py (LIVE: d03-SWC, kind C only)

| sites | kind | expression | operand types | reach | disposition |
|---|---|---|---|---|---|
| 23:7 | CALL:json.load | spec_dual_v3 | 0 float leaves | geom, acc:SWC | OK-exact |
| 30:8 | CALL:str | Q | S/I | geom, acc | OK-exact |
| 33:20, 33:28, 34:16 | CALL:int | Q | S to I | geom, acc | OK-exact |
| 33:15, 34:11 | CALL:fmpq | Q | I to Q | geom, acc | OK-exact |
| 38:10 | DIV | `1 / (1 + T)` | I/Q to Q | acc:SWC | OK-exact |
| 38:6 | CALL:arb | `arb(1 / (1 + T))` | Q | acc:SWC | OK-exact |
| 62:58 | CALL:int | `int(cs["series_terms"])` | JSON int 20; the same N drives series and tail bound | acc:SWC | OK-exact |
| 123:22 | DIV | `(lo + hi) / 2` | Q/I | geom | OK-exact |
| 47:7, 52:11, 70:64 | COMPARE | theta1_float, `th < 2*math.pi - 1e-6` | F | none (kind-G branch) | DEAD |
| 48:19, 49:13, 49:26, 70:73 | MODATTR | `math.pi` | F | none | DEAD |
| 51:14, 70:83 | FLOATLIT | `0.5`, `1e-6` | F | none | DEAD |
| 52:11 | CALL:math.cos | | F | none | DEAD |
| 52:31 | CALL:math.sin | | F | none | DEAD |
| 52:47 | CALL:math.exp | | F | none | DEAD |
| 70:29 | CALL:math.floor | | F | none | DEAD |
| 68:13, 68:19, 68:42 | DIV | rm and midpoints | F/F, Q/I | none | DEAD |
| 68:13, 68:36 | CALL:float | | Q to F | none | DEAD |
| 70:20 | CALL:fmpq | theta_tri | I to Q | none | DEAD |
| 70:25 | CALL:int | floor | I | none | DEAD |
| 93:5, 134:51, 145:32 | CALL:time.time | | F | report | OK-reporting-only |
| 119:69, 119:77 | CALL:str | FAIL boxes | Q to S | report | OK-reporting-only |
| 133:11 | MOD | progress | I | report | OK-reporting-only |
| 134:45, 145:26 | CALL:round | elapsed | F | report | OK-reporting-only |
| 147:4 | CALL:json.dump | dual.json | | report | OK-reporting-only |
| 148:17 | CALL:json.dumps | | | report | OK-reporting-only |

### code/me3dual_v9.py (LIVE: d03-SWC)

| sites | kind | expression | operand types | reach | disposition |
|---|---|---|---|---|---|
| 33:23, 64:31, 64:40, 64:49 | CALL:acb | `acb(1, c0)`, `acb(sb)`, `acb(db)`, `acb(wb)` | I/R | acc:SWC | OK-exact |
| 33:8 | DIV | `p = (S * (1 - S) * acb(1, c0) - kap * S * S) / N1` | C/C, J/J | acc:SWC | OK-exact |
| 37:17 | DIV | `(-2 * RE(pk) + 3 * (-1) ** j) / j` | (C+I)/I or (J+I)/I; the int is added exactly, then one ball division | acc:SWC | OK-exact (repaired site) |
| 37:36 | POW | `(-1) ** j` | I**I, 1 <= j <= 20 gives ±1 | acc:SWC | OK-exact |
| 56:10, 58:10, 58:20, 58:30, 58:40, 66:12, 66:32, 66:52 | CALL:arb | `arb(B.upper())`, `arb(dh)`, `arb(wh)`, midpoints | R/Q | acc:SWC | OK-exact |
| 56:14 | METHOD:upper | `(kap*sb*sb/N1).upper()` | R | acc:SWC | OK-exact |
| 56:15, 62:15, 62:56, 63:14, 63:44 | DIV | B; tail bounds | R/R | acc:SWC | OK-exact |
| 66:16, 66:36, 66:56 | DIV | midpoints | Q/I | acc:SWC | OK-exact |
| 62:29, 62:60, 63:23, 63:48 | POW | `q1 ** (N - 1)`, `xm ** (N - 1)`, `q1 ** N`, `xm ** N` | R**I (19, 20) | acc:SWC | OK-exact |

### code/check_cover_v1.py (LIVE: a01-coverP)

| sites | kind | expression | operand types | reach | disposition |
|---|---|---|---|---|---|
| 23:7 | CALL:json.load | spec P | 0 float leaves | geom-audit | OK-exact |
| 27:11 | CALL:Fraction | `Fraction(str(x))` | S to Fr | geom-audit | OK-exact |
| 27:20 | CALL:str | `str(x)` | S | geom-audit | OK-exact |
| 37:13, 38:11 | CALL:divmod | cell index | I | geom-audit | OK-exact |
| 40:30, 41:30 | DIV | `(...) * idx[d] / nsplit[d]` | (Fr*I)/I to Fr (nsplit JSON ints) | geom-audit | OK-exact |
| 58:14 | DIV | `(lo + hi) / 2` | Fr/I | geom-audit | OK-exact |
| 74:13 | CALL:int | `int(ci_s)` | S to I | geom-audit | OK-exact |
| 22:9 | CALL:int | `int(sys.argv[6])` stride | S to I | report (sampling) | OK-reporting-only |
| 98:11 | MOD | `n % stride` | I | report (sampling) | OK-reporting-only |
| 110:4 | CALL:json.dump | cover.json | | report | OK-reporting-only |
| 113:6 | CALL:json.dumps | | | report | OK-reporting-only |

### code/check_cover_v2.py (LIVE: b01-cover-*, b02-cover-SWC)

| sites | kind | expression | operand types | reach | disposition |
|---|---|---|---|---|---|
| 19:7 | CALL:json.load | spec dual | 0 float leaves | geom-audit | OK-exact |
| 21:8, 22:7, 23:10 | CALL:Fraction | breakpoints, weights, params | S to Fr | geom-audit | OK-exact |
| 21:17, 22:16, 23:19 | CALL:str | | S | geom-audit | OK-exact |
| 28:13, 29:11 | CALL:divmod | cell index | I | geom-audit | OK-exact |
| 47:14 | DIV | `(lo + hi) / 2` | Fr/I | geom-audit | OK-exact |
| 53:11 | CALL:fmpq | `fmpq(x.numerator, x.denominator)` | I to Q | geom-audit (skip-d) | OK-exact |
| 65:15 | CALL:bool | skip-d comparison | R cmp | geom-audit | OK-exact |
| 65:20, 65:45, 65:69 | CALL:arb | `arb(fq(...))` at default 53-bit precision (still rigorous) | Q | geom-audit | OK-exact |
| 80:13 | CALL:int | `int(ci_s)` | S to I | geom-audit | OK-exact |
| 18:87 | CALL:int | stride | S to I | report | OK-reporting-only |
| 106:11 | MOD | `n % stride` | I | report | OK-reporting-only |
| 118:4 | CALL:json.dump | | | report | OK-reporting-only |
| 121:6 | CALL:json.dumps | | | report | OK-reporting-only |

### code/lane_guard.py

| sites | kind | expression | operand types | reach | disposition |
|---|---|---|---|---|---|
| 25:21 | DEFAULT | `mode="x"` in xopen | S (no numeric content) | none numeric | OK-exact |

## 5. Live acceptance decisions vs indeterminate balls

Every live acceptance is decided in one of two ways:
* A ball comparison that is True only when certain. Then a NaN or infinite ball can only lead to reject or split.
* An exact Q or Fraction comparison.

The decisions checked:
* cert_primal_v3: 78-79 (INFEAS), 83-84 and 87 (naive SGE/DPOS), 93 and 96 (MVF).
* cert_dual_v5/v7:66 (SKIP:in-primal-P, exact Q).
* v4: 55-59 (branch selection; all three need certainty), 67 (SMALL), 70 and 73 (RADIAL), 77 and 82 (RADIAL-MVF),
  88 and 91 (TRIANGLE).
* v3: 118 (LW SMALL); 127, 131 and 133 (small-beta ratio, all inside `if not (...)` guards).
* v6: 35-41 (argument candidates need certain signs), 48-59, 77 and 79 (skips).
* v6.test_bedge: 120, 130, 138, 142-144 and 152-155.
* v9: 60, 68, 73, 75 and 81.
* check_cover_v2: 59, 62 and 65.

The one pattern where a False comparison is permissive is `Cp = arb(C.upper()) if C.upper() > 0 else arb(0)`, at
v6:143 and v6:154. In the live v6 it runs only after `Cv.is_finite()` (142) and `Cm.is_finite()` (152) are True.
Then `C.upper()` is a finite exact point, the comparison is decided exactly, and Cp = 0 means sup C <= 0.

Intersections at v4:49-50, v6:135-136 and v9:72 combine two valid enclosures. An empty intersection would raise,
which fails closed.

## 6. Non-float observations (separate from the counts)

1. **DEAD `me3dual_v3.test_bedge` lines 309-311 and 319-320.** There is no finiteness guard. If Cv or Cm is NaN,
   then `arb(0).union(Cv)` and `.upper()` give NaN, `NaN > 0` is False, and Cp silently becomes 0. The acceptance
   `Bv + wh^2 Cp + E < 0` could then pass with C unknown. A NaN g3 is caught first by imlow at 304-306. A NaN g2
   alone, or a NaN in the MVF Cm, is not caught. [INFERENCE: this relies on Arb's NaN propagation in union and
   upper bound; I did not execute it.] It is fixed in the live v6 (142, 152). It ran only in calibration k02.
2. **Spec hashes are not in the launcher receipts.** run_v1.sh hashes `code/*.py` and `code/*.sh`, not the spec
   JSONs, so spec provenance relies on the separate freeze receipts cited in me3-theorem-v3.md:95-119. I did not
   check those receipts. The spec_primal and spec_dual_v1 hashes above match the prefixes quoted there.
   spec_dual_v3 (43d2e22e…d936) is not cited by theorem v3.
3. **me3-theorem-v3.md still lists d02-SWC as the SWC certificate.** Its table (line 135) and text (line 126)
   predate d03-SWC and cite the v8 path. The final statement must cite d03-SWC and its coverage audit (b03 used
   check_cover_v3.py, which is out of my scope).
4. **The checkers and drivers parse spec values differently.** The checkers use `Fraction(str(x))`; the drivers
   use Q(), which accepts only "int" or "int/int". They agree on every value present. If a float were introduced,
   the drivers would fail closed, but check_cover_v1:40-41 would silently compute float cell bounds if
   `initial_split` were a JSON float. Today all three are ints.
5. **check_cover_v1 does not hard-code "no FAIL".** It enforces only the allowed-outcome list from argv; a01
   passed `INFEAS,SGE,DPOS`, so FAIL was excluded (receipt a01-coverP-pre.json).
6. **Checked and found fine:**
   * Library modules create `acb(0, 1)` at import, before `flint.ctx.prec` is set. That value is exact, and pi is
     computed at call time.
   * LD β boxes reaching past pi/2 (15708/10000) and primal φ up to 31416/5000 contain only infeasible points
     there. A tan pole gives a non-finite ratio and the box is rejected or falls back to the safe ratio.
   * SKIP rules use exact rationals (in-primal-P, and skip-s in the checker) or certain-only ball comparisons
     (skip-d, and skip-s in the driver).
   * The B-edge test ignores w_lo, which is safe because it certifies all of (0, wh].
7. **run_v1.sh has no numeric influence on the certified process.**
   * Float or integer arithmetic appears only in the disk gate (lines 16-18, integer), timing (51, 57, 68:
     `round(T1-T0, 3)`, report) and the receipt version probe (35, separate process).
   * `ulimit -t` and `/usr/bin/time -l` wrap the run.
   * The interpreter is run with `-B` only; no environment variable touches flint precision.
   * TMPDIR is the lane tmp directory.

## 7. Reproduction

`cd L && ./code/run_v1.sh independent-float-audit s01-scan 120 1000000 independent-float-audit/code/scan_sites_v1.py`
wrote `runs/s01-scan/{sites.tsv,json_types.tsv,summary.json,stdout.txt}`, exit 0. The scanner reads lane files as
text and imports nothing from `code/`. The 556-site tables above were transcribed from `sites.tsv` and classified
by hand. Per-file site totals equal the scanner's per-kind counts.
