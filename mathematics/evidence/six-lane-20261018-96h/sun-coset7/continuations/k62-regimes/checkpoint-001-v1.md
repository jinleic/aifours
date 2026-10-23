# k62-regimes checkpoint 001

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T10:20:00-0700.
- **Owner:** SunK62Regimes. Written research only; no computation, no process, no model call (HOLD respected).
- **Cadence deviation (actual):** first `/bin/date` of this slice was 2026-10-19T09:47:11-0700 (reading of inputs began
  then); this is the first checkpoint, 1969 s later, i.e. **more than 1800 s**. No checkpoint was sent earlier. Recorded
  here as a deviation; not repaired retroactively.

## Actual result
- Regime chosen and frozen before derivation: (iii) the higher-depth alternative for e_d >= 5, restricted to the generic
  sub-case G of the CAP-DT verdict (no O-marker; 3-marker on i* with any f* or absent; 5-marker on d/i* or absent).
  `K62-HD-SCOPE-v1.md` sha256 c0cbb507adc8d23fb5894e02744d1176ba27f613b904c0ddb40739feb0702f82 (frozen 10:10:11).
- Complete written candidate: **Theorem HD** — in G, for both families and every 4-subset Q of O, v2 T_x(Q) <= 4; hence
  (Corollary HD) no 4-subset has capped depth >= 5 for e_d >= 5, and Theorem DG (a)/(b) applies in G to both families with
  no remaining hypothesis. Proof: DG-4 chain with equality case, the triangle table, CI', a new Lemma EQ (one-tight case via
  VFC + INV + Sun(2)), K62-E3 Lemma 2 and C2, DT-B (R4)/B3; full case split A, B1-B4. CANDIDATE_UNVERIFIED.
  - `K62-HD-v2.md` sha256 6c1858c04d7da52bde8533ba71d4dcea814fb69b30a357462e36024226b9f476 (frozen; the candidate).
  - `K62-HD-v1.md` sha256 52611b80e2846326cd45632c653e93f8e69c9ab33851d589a68d3056819dd965 (frozen undelivered draft,
    superseded by v2: one wrong verdict-hash suffix, L0.1 location, wording of the |N| >= 4 count; no mathematical change).

## Blocker
None for the written proof. Independent review (parent-owned) has not started.

## Next bounded action
Freeze the review package and the excerpt manifest (planned 27 ranges, about 91 KB embedded, under the 100 KB cap) in
this directory, then report paths and SHA256 to the parent and park.
