# k7-direct-marker-residual checkpoint 001 — erratum done; scope frozen; derivation status

- **Written:** `/bin/date` read at 2026-10-19T18:24:16-0700, immediately before this exclusive create. Slice start 2026-10-19T18:12:26-0700.
  If this clock read is later than 18:42:26, the 1800-second checkpoint cadence was exceeded during uninterrupted written
  derivation (no tool activity); that deviation is recorded here and not hidden. Owner SunM13MixedFibres; written only.
- Done: `../sun7-written-import-cutover/CUT-erratum-v1.md` 3da79c1c88442dedba09920253336b16b1e1a403f7b3ec33d1255c234948cc40 (propagates parent S56W erratum b2299b6f…0aae).
- Frozen: `KDM-SCOPE-v1.md` 997950d867567d563b89e1dafc77d7d72f1881d174ab65eeaf64f6950f2300b0 before any derivation.

## Working results (unwritten; to be frozen in KDM-v1.md)
- Lemma P5 (proved on paper): in (a2), in either family, no apex has an UNMARKED neighbour with multiplier 5 (Sun(2) +
  actual inversion), for every apex type u, z, t, p.
- Obstruction found: an explicit symmetric-type multiplier pattern G2 on all 21 edges, with its inverse pattern, satisfying
  alpha + alpha* <= 6 and Lemma P5, which passes the left-fibre count at EVERY apex in BOTH families with explicit fractional
  covers of total < 1, even when Sun(5)/Sun(6) clauses are added. So fibre counts + actual inversion alone cannot exclude
  (a2); a short proof of this type does not exist. Outcome (B) with exact local/global obstruction is being written.

## Next
Write KDM-v1.md (P5 proof, G2 with all 14 cover certificates, failed routes, what extra structure is needed), package,
manifest, final checkpoint, IRC, park.
