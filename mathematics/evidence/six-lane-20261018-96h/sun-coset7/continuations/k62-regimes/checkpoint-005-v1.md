# k62-regimes checkpoint 005 — marked (1,1) slice: derivation status

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T11:15:04-0700.
- Previous: `checkpoint-004-v1.md`, sha256 c61a5be975299e032041dbc91f427a28b664b0ed5c2a942261e25b42a1fe71de (10:56:30);
  gap 1114 s. Owner SunK62Regimes; written research only; no computation, process or model call.
- Frozen scope: `K62-MK-SCOPE-v1.md`, sha256 12cad4f7e9f7d29c5aa7d7520bda50534b3ecd64702cf4198ff01050ef0ef1bd (11:04:40).
- Parent IRC received: GS Codex review ACCEPT (fecc0372…), Claude pending; GS stays CANDIDATE and is not imported here.

## Actual result so far (unwritten derivation, to be frozen in `K62-MK-v1.md`; nothing claimed yet)
- At any O-vertex the O-labels are ell_u x (ell_u = n_u / 6 odd, pairwise coprime, markers included): EQ's one-tight
  case survives every marker.
- gcd(n_v, T_y(V minus {v})) = 6 for every v in O other than t (re-provable at p by the (C1) chain); at t it equals 6 iff
  9 does not divide T_y(V minus {t}); y_(e i*) = 3 at some e in O minus {t} forces 9 | T_y(V minus {t}).
- At t, plain-LFC certificates exclude a row with four O-entries in {1, 2} unless its i*-entry is 2 (entry 5 needs h_d >= 1
  by the T rule).
- The four-subset bound can be proved without the chain step that adds t (new case split when t is an endpoint of a
  2-pair).
- Planned statements (inside the frozen scope): Theorem M5 (M5 empty); for M3(1,1) a residual theorem: every
  configuration has an R1-instance (tight equal-X pair at t, forcing 9 | T_x(V minus {t})) or an R2-instance (t-row with
  four O-entries in {1,2}, i*-entry 2, forcing 9 | T_x'(V minus {t})); conditional/sub-case emptiness when 9 divides
  neither T_alpha(V minus {t}) nor T_alpha*(V minus {t}).

## Blocker
None; writing the proof file next.

## Next bounded action
Freeze `K62-MK-v1.md`, then the review package and manifest; report paths/SHA256.
