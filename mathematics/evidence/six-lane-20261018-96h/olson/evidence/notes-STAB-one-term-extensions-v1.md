# Notes (handoff; NOT claims, unreviewed): one-term (ZP_kappa)-extensions of E2(kappa - 1), worked before the ownership
# transfer, v1

Owner ContinueOlson.  Written after /bin/date 2026-10-19T03:56:49-0700.  Written down from computations done before the parent's ownership
transfer of STAB to the Slice A successor (run review/olson-two-slice-successor-brief-v1.md); no new STAB work after that
message.  Context: evidence/proof-LSplus-partials-v2.md (eedfa0f16572f1636bfa4f387e3a1566b87864ae4ced6fddcf063cddaedcb6b2) and its addendum MAX v2 (4b0be3e304199cc61180e2b5bdad7eb63acb8b2c6e5ada6e95cfb0e099a451c7); STAB not
assumed.  Notation: p >= 7 prime, kappa0 + 1 <= kappa <= p - 2, e := p - kappa (so 2 <= e and 3e <= p - 1), h a generator,
E2(kappa - 1) = h^(a') (3h)^(p-1) with a' = 3(kappa - 1) - p + 2 = 2p - 3e - 1.  E2(kappa - 1) satisfies (ZP_(kappa-1)), hence
(ZP_kappa).  Window for (ZP_kappa): lengths in [2kappa + 2, 2p] = [2p - 2e + 2, 2p].

## Observation 1 (one-term extensions)
For y = c h (c odd in [1, 2p - 1]), E2(kappa - 1) y satisfies (ZP_kappa) iff c is in {1, 2p - 3, 2p - 1} (y in {h, -3h, -h}).
- c in [3, 2p - 5]: level 4p (c + i + 3j = 4p).  Feasible j: [j1, j2], j1 = max(0, ceil((2p + 3e + 1 - c)/3)),
  j2 = min(p - 1, floor((4p - c)/3)).  Window: j in [w1, w2], w1 = (2p + 1 - c)/2, w2 = (2p + 2e - 1 - c)/2.  w1 <= j2 (c >= 3),
  j1 <= w2 (c <= 2p - 5), j1 <= j2 (c >= 3e + 4 - p, true as 3e <= p - 1, and 2p + 3e + 1 <= 4p), w1 <= w2: a window zero-sum
  through y exists.  (c = 3 also directly: h^p (3h)^p, as a' >= p.)
- c = 1: E2(kappa - 1) h = h^(2p-3e) (3h)^(p-1): level-2p zero-sums need j >= e (lengths <= 2kappa), level-4p ones have
  j <= p - 1 (lengths >= 2p + 2): admissible.
- c = 2p - 1 (y = -h): through y, i + 3j in {1, 2p + 1, 4p + 1}; level 2p + 1 has length 2p + 2 - 2j, window iff j in [1, e],
  feasibility needs j >= e + 1; level 4p + 1 needs j >= p + 1 > p - 1: admissible.
- c = 2p - 3 (y = -3h): i + 3j in {3, 2p + 3, 4p + 3}; level 2p + 3 has length 2p + 4 - 2j, window iff j in [2, e + 1],
  feasibility needs j >= e + 2; level 4p + 3 needs j >= p + 2: admissible.
## Observation 2 (some multi-term extensions)
- (-h)^2 violates: h^(2p-3e-1) (3h)^(e+1) (-h)^2 has length 2kappa + 2.
- h^2 (-h) violates: with a' + 2 copies of h, j = e at level 2p + 1 gives length 2kappa + 2.
- h^2 (-3h) violates: j = e + 1 at level 2p + 3 gives length 2kappa + 2.
- h^3 gives E2(kappa) (admissible, Lemma TV).  Not computed: h (-h), h (-3h), (-3h)^2, (-h)(-3h), and all extensions of
  E3(kappa - 1).
## Status for the successor
Because (ZP) is hereditary, every (ZP_kappa) extension of E2(kappa - 1) uses only h, -h, -3h, so classifying three-term
extensions is a finite check (incomplete above).  The open step identified by the parent's brief remains: the existence, in a
length-(3kappa + 1) (ZP_kappa) non-(S1) sequence, of three occurrences meeting every 2kappa-zero-sum while a long zero-sum
survives; nothing here proves it.
