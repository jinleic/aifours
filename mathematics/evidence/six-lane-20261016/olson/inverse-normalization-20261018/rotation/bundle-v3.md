# Rotation slice: bundle v3 (current files, statuses, import map) at 08:35 PDT

Written after host clock 2026-10-18T08:35:20-07:00 by OlsonRotationRigidity.  Supersedes bundle-v2.md (376c2dfd...8165)
and results-v4.md (1d481e3d...064ac) as the summary; README.md remains the append-only log.  Paths relative to
mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/; R = institute/runs/six-lane-
2026-10-16/review/.  No novelty claim anywhere; no claim of full ROT(p), INV*(p) or ordered Olson for D_(2p).

## 1. Current files (sha256) and review state

| result | current file (sha256) | review state | exact scope |
|---|---|---|---|
| GRX, PM*, K1/K2, ROT-o2 | notes-GRX-v1.md afc6c31a...0a30; proof-ROT-lowodd-v1.md 8ba3e6c7...9785 | parent-accepted (lowodd verdict v2) | as accepted |
| ROT-o3; ROT-o4 | proof-ROT-o3-v4.md 55670658...e8cf; proof-ROT-o4-v4.md 7fa49e97...425a (wording errata of v3) | parent-accepted: ROT-o3 p >= 5, ROT-o4 p >= 7 | o_F = 3, 4 |
| ROT-o4 at p = 5 | proof-ROT-o4-p5-finite-v1.md 7c8a5051...404c; packet p5o4-v1/ (PLAN-v1 7d7793cb...0588) | [F] finite exact, run1 PASS (verdict.json ca156d58...df0f); Codex audit pending | p = 5, o_F = 4 |
| SHgen | proof-SHgen-v3.md fcbd5a97...eb5e (errata of v2 8fde88c0...d239) | v2: Codex ACCEPT, Claude ACCEPT | all-odd, nonempty runs, (H), (K) |
| ROT-FEW | proof-ROT-few-v4.md abd3973c...b521 (errata of v3 5f158d69...efaa) | v3: Codex ACCEPT, Claude ACCEPT; cond. SHgen | constant runs, 5 o_F <= 2p + 4 |
| ELT0-FEW | proof-ELT0-FEW-v3.md 8557666c...0cb3b | v2 Claude A-W-F MAJOR M1 repaired by route (b); v3 unreviewed; cond. SHgen | constant runs, kappa = 0, 3 o_F <= 2p + 1, all rotations equal |
| ROT-FEW-E | proof-ROT-few-E-v3.md cc74bbb8...5e9b (errata of v2 cb4bca7b...917e) | v2 Codex ACCEPT; Claude: Sec. 0, 2 A-W-F, Sec. 1 INCONCLUSIVE (text missing), targeted check pending; cond. SHgen + REFL | any runs, 5 o_F <= 2p + 4 |
| INV*-FEW | proof-INVstar-few-v3.md 779218b4...5531 | v1 Codex A-W-F, v2 Claude A-W-F; v3 unreviewed | (a) o_F <= 3 (p >= 5), = 4 (p >= 7), cond. REFL-few-odd only; (b) 5 o_F <= 2p + 4, also SHgen, ROT-few-E Sec. 0-2, ROT-few MULT/Steps 1-5 |
| KAPPA01 | proof-KAPPA01-v4.md 416f40ee...fa91 | v2 Codex ACCEPT, Claude A-W-F; v3, v4 errata unreviewed | INV* for kappa in {0, 1}, 3 o_F <= 2p + 1, cond. SHgen + REFL-few-odd |
| OLSON-FEW | proof-OLSON-few-v3.md ae151f9b...cd66a (errata of v2 d19e5a30...a7a1) | v1 Codex ACCEPT; v2 Claude A-W-F, Codex review running; v3 unreviewed | ORDERED OLSON at length 4p-1: (a) o_F <= 3 (p >= 5), <= 4 (p >= 7), cond. REFL-few-odd; (b) 5 o_F <= 2p + 4, also the (b) chain of INV*-FEW |
| RIGID-STRUCT | notes-RIGID-STRUCT-v1.md 23ffb490...4d83 | [W] note from accepted imports | RGR-shape avoiders: type (I) kappa = 0 equal rotations, or (II) kappa = k - 1, one run c^(2p-1), other runs one -c |
| S(p) (Savchev-Chen at length p, odd) | notes-SC-lengthp-v2.md 0c991ac3...1eadf; addendum v1 fc3feae3...a9c0; addendum v2 dbf768c5...2080 | NOTES, partial | proved: upward induction, S(p) <=> SAT(p-1), small-s case, pure-form reduction, T1-T3; OPEN: large-s case |

With the p = 5 finite result (if the audit passes): INV*-FEW (a) and OLSON-FEW (a) also hold at p = 5 with o_F <= 4.

## 2. Import map (who uses what)

* OLSON-FEW -> INV*-FEW -> {ROT-o2, ROT-o3, ROT-o4 (accepted); REFL-few-odd (reflection/proof-REFL-fewodd-r2.md
  db16274f...c2c6, Sec. 4 interface); for (b): ROT-FEW-E Sec. 0-2 -> {SHgen, Lemma SHgen-E, ROT-few MULT and Steps 1-5}}
  and RGR-LONG(p) (accepted, RUNS verdict).
* KAPPA01 -> {ROT-few-E normal form and SHgen-E; ROT-few MULT; SHgen; REFL-few-odd Sec. 4; accepted GRX, PM*, K1, (D),
  (V)}.  ELT0-FEW -> {PM*, GRX, ROT-few MULT, SHgen}.  ROT-FEW -> {SHgen; accepted GRX, PM*, (D), INC (a), (b); (V)}.
* SHgen -> {GRX, K1 (accepted); B'(b), C1, KBH, uncapped KB (RUNS verdict); (V) with erratum m4; trivial cut}.
* ROT-o4 at p = 5 -> {accepted PM*; frozen code}; Stage D is GRX-free, Stage G uses accepted GRX.
* No file uses Corollary ELT0-ROT / proof-ELT0-v3.md any more; no file uses the historical D10 census.

## 3. Open, with the exact obstruction

* ROT for o_F > (2p+4)/5 (general kappa): WT (b), (c) of ROT-FEW need G >= 2kappa + w_+; padding with Y' instead of g
  fixes WT (b) up to e + kappa <= p - 1, but heavy negatives (sum_N b >= 2p) still bind at (F) (no file).
* kappa = 0 beyond 3 o_F <= 2p + 1: needs S(p); with S(p) the SHgen route reaches 5 o_F <= 4p - 1 only.
* p = 5 with o_F >= 5; REFL for o_F > p (reflection slice).
* General ordered Olson for D_(2p): would follow from INV*(p) for the remaining avoiders.
