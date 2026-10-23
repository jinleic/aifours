# k62-followon checkpoint 008 (Sun63Successor) — hand-off state

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T06:17:00-0700. Previous: `checkpoint-007-v1.md`
  (sha256 8b9e9155a1df0cf3aa463f855e2bdeddb2c84622b80921dde209f1f493173afb).

## Candidates and documents of this follow-on (status as known to this worker)
| file | sha256 | status |
|---|---|---|
| `K62-E3-v1.md` + errata v1, v2 | 70a60d55… / 095c31dc… / f9f52e1bc4896d94cd014ed3f8915af0318ddcd06d1efc1ad7f14478685add4c | PARENT ACCEPTED (verdict 576969dd…) |
| `K62-SH-v1.md` | 4f17451c60c6018e7fadbca8c36eb92fb23d3e6daef076506aed14f4c5446b5a | candidate, sent, unreviewed |
| `K62-DG-v1.md` + erratum v1 | a4bfc41e832ebc4e77770cab7a8092a3341827cec93a01bfb437c978c1e84f52 / e435430c6d4ff855871dfa7a9004757561435821dae8f53e7304b10e64626801 | candidate, sent, unreviewed |
| `K62-ARCH-v1.md` | b0f5face7242ce572aa4d0b011b463e808fd4a97978b59a4449a30fe7383cf03 | planning only |
| `probe-survivor-map-v1.py` | 8569f726069766bd7ee0b284b5ded2396c0615e5fa14754bfe7211dff55d81be | frozen, NOT RUN (HOLD) |
Earlier superseded candidates (K62-FG, K62-R2) and navigation files (K62-STATUS-v1/v2 + addendum) stay frozen.

## Navigation notes for the next worker (NOT claims; unproved)
- Theorem DG forces, in each family to which it applies, deep alpha*/alpha-triples ((2,4,4) with tau = 8, or (4,4,4)
  with tau in {8, 16}) or a deep 4-subset. A (2,4,4)-triple {v, a, b} with tau = 8 forces X^v_a = X^v_b at its apex v.
  Sketch (needs the 1/6 grid at v, i.e. the chain lemma of K62-FG section 3, not accepted): if va, vb are tight in the
  other family, the two points of Y^v_a carry exactly the pieces of a and b, so they avoid Y^v_d (Y^v_d is then the
  other three points) and every tight O-neighbour c of v has x_vc = 4; the other-family row (2,2,2,2 | .) is excluded
  by the 5/6 bound. Pushing this to all patterns is a finite case analysis (or the K62-ARCH computation after HOLD).
- Two families cannot both have two 4-triangles in their 4-graphs (edge-disjoint in K5), so at least one family needs
  forcing deep triples or a deep 4-subset.

## Resources
No process was ever launched by this worker; nothing to settle. Full K6.2* (e_d >= 4) and full Sun(7) OPEN.
