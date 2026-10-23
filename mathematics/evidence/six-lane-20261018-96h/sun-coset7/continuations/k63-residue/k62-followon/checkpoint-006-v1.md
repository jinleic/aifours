# k62-followon checkpoint 006 (Sun63Successor)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T06:05:11-0700. Previous: `checkpoint-005-v1.md`
  (sha256 18753a2faf4f87301e214a58345b73c910042be1a7df878fcaedac7c623eafdd).

## New files since 005
| file | sha256 | status |
|---|---|---|
| `K62-SH-v1.md` | 4f17451c60c6018e7fadbca8c36eb92fb23d3e6daef076506aed14f4c5446b5a | CANDIDATE (partial necessary conditions on i*-rows); sent |
| `probe-survivor-map-v1.py` | 8569f726069766bd7ee0b284b5ded2396c0615e5fa14754bfe7211dff55d81be | exploratory source, frozen, **NOT RUN** |

## Parent HOLD
`RUN/review/runtime-guard-admission-HOLD-v1.json` sha256 6c1d8440419c50b399a8f8aa66d37bd280451619abffce618caa25c188d6dc1f:
no new computational launches. Acknowledged to the parent; this worker has never launched a process in this
continuation and has no live child. The probe above stays unrun unless a new exact item GO is issued.

## Written progress (not yet frozen)
Pattern P_ob, multi-vertex coupling through the triangle quotients tau (shared by the three apexes):
- alpha*-triples: the five (2,2,4)-triples have tau* = 4 forced (tau_min = tau_max = 4); each (2,4,4)-triple has
  tau* in {4, 8}. tau* = 8 on {c_i, c_(i+1), c_(i+3)} forces X*_(c_i) = X*_(c_(i+1)) at apex c_(i+3); with the forced
  containments from the two (2,2,4)-triples through c_(i+3), the two complement points then carry pieces of two
  label-type-2 vertices and two more vertices: not allowed (Sun(3) instance). So tau* = 4 on all ten alpha*-triples,
  and likewise tau = 4 on all ten alpha-triples (relabelling c_i -> c_(2i)).
- With tau* = 4 everywhere, the d-LP (granularity 1/8 for every triple) remains feasible (explicit B-distribution with
  beta_5 close to 1/8) and the 6-point model at c4 (VFC side) remains consistent. P_ob is constrained, not excluded.

## Resources
No process launched; no GO held.
