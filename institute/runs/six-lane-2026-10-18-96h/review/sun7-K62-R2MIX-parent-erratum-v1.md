# K62-R2MIX parent wording erratum v1

Recorded at 2026-10-19T12:37:46-0700. Read after immutable proof `b75e6dc7e72b8c0b1cd5388e8845a3bcd23854b0fbd83292fa6ff7c22ade0806` and frozen scope `12a64d8e4c19cd6dd8f7d04d6ee7dabef06bd23707522fae07d27a2b4651e4e5`. Disposes Codex `e89a76f1c9bbbd7a419d9d48506aa952206b6d667fca31a6b5ff1dcf20309427` (ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR / 3 MINOR; no principal-derivation gap found). No statement, case, proof step or import changes. Each Old span occurs exactly once in its source.

## m1 granularity qualifier (section 7)

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-r2-mixed/K62-R2MIX-v2.md

Old:
````text
the light-fibre bound once tau_y'({d, i*, e}) = 3 gives granularity 18,
````

New:
````text
the light-fibre bound once tau_y'({d, i*, e}) = 3 gives granularity at least 18 (Gamma_y'(t) = 2*3^min(f_t, v_3 T) >= 18),
````

## m1 granularity qualifier (section 7, Step 1 sentence)

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-r2-mixed/K62-R2MIX-v2.md

Old:
````text
it now suffices because Step 1 removes granularity 18.
````

New:
````text
it now suffices because Step 1 excludes every product equality that would give granularity at least 18 (the opposite-family gcd is exactly 6).
````

## m1 granularity qualifier (mutation check 6)

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-r2-mixed/K62-R2MIX-v2.md

Old:
````text
6. *Granularity 18 at t* (some tau_y' = 3): Step 3 gives only 11/12 <= 17/18, no contradiction (K62-MK-v2 mutation (1)); this
````

New:
````text
6. *Granularity at least 18 at t* (some tau_y' = 3): even the strongest resulting case, Gamma = 18, gives only 11/12 <= 17/18 in Step 3 (larger Gamma gives the weaker bound 1 - 1/Gamma), no contradiction (K62-MK-v2 mutation (1)); this
````

## m2 no nonvacuity or existence assertion

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-r2-mixed/K62-R2MIX-v2.md

Old:
````text
- **Necessary fact beyond R2-rows:** Proposition 5 (a) is not vacuous after R2X: for any family y and e in O' whose three
  t-entries y_tu (u != e) lie in {1, 2} (for example with y_te = 4), tau_y'({d, i*, e}) lies in {1, 2}.
````

New:
````text
- **Necessary fact beyond R2-rows:** Proposition 5 (a) also addresses the formal three-small-entry case, which R2X alone does not exclude; no existence assertion is made: for any family y and e in O' whose three
  t-entries y_tu (u != e) lie in {1, 2} (formally including y_te = 4; no such configuration is exhibited), tau_y'({d, i*, e}) lies in {1, 2}.
````

## m3 computation disclaimer (header)

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-r2-mixed/K62-R2MIX-v2.md

Old:
````text
No computation of any kind was run (no compute
  GO; global runtime HOLD respected); no model call.
````

New:
````text
No scientific computation, enumeration or tests were run (no compute
  GO; global runtime HOLD respected); metadata operations (date, hashes, wc, range extraction) are disclosed separately; no model call.
````

## m3 computation disclaimer (frozen scope)

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-r2-mixed/K62-R2MIX-SCOPE-v1.md

Old:
````text
Written research only: no computation, enumeration, process, model call, import or runtime.
````

New:
````text
Written research only: no scientific computation, enumeration, tests, model call, import or runtime; metadata operations (date, hashes, wc, range extraction) are disclosed separately.
````

## Scope reminder

Codex accepted Lemmas 1-4, Proposition 5, Theorem R2X, Lemma 6, Theorem 7 (stated weakened RR conclusion only), Corollary R1X and Corollary 6.1 (NR). Corollary M3E remains conditional on the pending K62-MK-v2 Theorem M3R. This erratum grants no acceptance; the parent verdict requires the second-family review of the corrected snapshot. Sun(5)/Sun(6) remain computer-assisted transitive imports.
