# k62-r2-mixed checkpoint 001 — scope frozen; mixed-family route under written derivation

- **Written:** `/bin/date` read at 2026-10-19T12:10:25-0700 (the reading immediately before this file).
- Owner SunR2MixedFibres; written research only; no computation, process or model call.
- Previous lane-local checkpoint: none (first). Scope frozen at 12:01:42:
  `K62-R2MIX-SCOPE-v1.md`, sha256 12a64d8e4c19cd6dd8f7d04d6ee7dabef06bd23707522fae07d27a2b4651e4e5.
- Parent IRC received 11:5x: K62-M3R-v2 Codex review 9f244c93 (load-bearing parts ACCEPT, 5 MINOR), parent erratum
  RUN/review/sun7-K62-M3R-parent-erratum-v1.md (sha256 cb42f3e77c63c2932a17ccbf041df81c3f81f5bd4ba402a758d5119395df34c7);
  M3R-v2 stays CANDIDATE and is treated here as pending (re-prove or conditional only).

## Claim under derivation (CANDIDATE_UNVERIFIED; nothing checked by anyone else)
Theorem R2X (full M3(1,1)): no R2-row. Route (thought-checked, being written): in the OPPOSITE configuration y' at d,
six labels with pairwise gcd 3 cap fibres at three pieces; pair granularity from y gives at least n_d/4 d-fibres shared
by t and each u in O'; their sum is at most n_d minus the t/i* overlap. The product equality
(Phi'_d cap Phi'_e)(Phi'_d cap Phi'_(i*)) = Phi'_d (equivalent to tau_y'({d, i*, e}) = 3) forbids e and i* from sharing a
d-fibre; counting e's n_d/2 fibres then fails by one (d's own fibre). Hence no e has tau_y' = 3, so
gcd(n_t, T_y'(V minus {t})) = 6, and the light-fibre count at t with weights 1/2 on O' and d gives 11/12 > 5/6.

## Actual result so far
Scope frozen; the argument above was checked step by step in thought (no file yet). No blocker at present.

## Next bounded action
Write `K62-R2MIX-v1.md` (proof with interface table, re-proved Lemma C/A/RR, mutation checks), then the review package and
excerpt manifest; next checkpoint <= 12:40.
