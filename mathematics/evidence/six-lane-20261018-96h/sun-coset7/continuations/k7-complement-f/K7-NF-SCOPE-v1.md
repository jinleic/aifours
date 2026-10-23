# K7-NF-SCOPE-v1: frozen scope for the exclusion of class K7 outside F [target; CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read immediately before this write: 2026-10-19T16:07:20-0700. Frozen **before** any derivation is written in this
  directory (created empty at 2026-10-19T16:06:55-0700).
- **Owner:** SunM13MixedFibres. Owned path, new files only:
  `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-complement-f/`.
  Exclusive-create (`x`) files only; corrections are new versions or errata. Written mathematics only: no scientific
  computation, enumeration, solver, test, compile, Lean, model CLI, nested agent, /tmp, deletion, commit or push.
  Hash/byte/range metadata only.
- **Authority:** parent transition `RUN/control/six-slot-written-resumption-20261019-1603-v1.json`, sha256
  ac09b46532a233c6d9ce1b227c3dffecee9655bd83413d96d3a403065a0ef0f8, slot math-1, and the parent IRC that announced it.
  RUN := `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`. Global HOLD unchanged; no runtime authority.

## 1. Target (fixed now)
**Class K7** (old README section 5, sha256 2a6d6d6e…3fd1): seven pairwise disjoint left cosets of finite-index
subgroups whose 21 pairwise index gcds all equal 6; equivalently n_i = 6 r_i with the r_i pairwise coprime. Write
m_i for the {2,3,5}-part of r_i. A **2-marker** (3-marker, 5-marker) is a vertex i with 2 | m_i (3 | m_i, 5 | m_i).
**F** := the K7 configurations having a 2-marker z and a 3-marker t with z != t (as in the parent transition).
- **Primary target, Theorem K7-NF:** no configuration of K7 \ F exists in any group with finite-index subgroups:
  every case with the 2-marker absent, the 3-marker absent, or the 2- and 3-markers on one vertex, with every
  admissible 5-marker placement (absent, on a marked vertex, or on a separate vertex) and all exponents/cofactors
  unbounded.
- **Method fixed now:** an exact, exhaustive partition of K7 \ F by marker placement, each block matched to the
  LITERAL hypothesis of an accepted theorem (statement text and mandatory overlays read, not headings). Accepted
  subfamilies are cited, not re-proved, and not counted as new mathematics.
- **Fallback:** if some block is not covered by an accepted literal statement, deliver the exact uncovered block and
  the smallest missing statement as an obstruction; never call a partial cover full.
- **Optional separately named navigation corollary:** combine with the accepted (a1) closure to identify the exact
  K7 remainder; it must not use A2X or any K62 candidate, and must not be called a K7 or Sun(7) exclusion.

## 2. Premise discipline (fixed now)
- **Accepted, literal scopes with mandatory overlays only:** README (R0, P0/P1, class K7; written verdict 73a25ba6…9f35);
  K7-M0 (K7-LFC-INV-v1 45be9162…726c with erratum 7af9acf0…75bd5; verdict 8621e744…cca18); K7-M1 (6e9b2d09…5d63 with
  erratum 4094b537…c510; verdict 7121ceed…ed84); K7-Z2 (cda7573d…be7 with erratum 3aa30555…e456f9; verdict 0f6b9aa3…19c);
  K7-35 (5624d978…fc5a with errata b13e1cf2…6e32 and 93f99707…0d44; verdict 1a1c6390…3919); K7-U1 (d4e6cdc9…1965 with
  erratum a795c5b7…99d5; verdict 44dfbe85…5c86); Z23-P5 (63255032…8e04 with erratum 737e82a3…823d; verdict
  7179e564…6f8d); for the navigation corollary only, the K7-R2 (a1) closure (verdict 9b0f7df5…926d).
- **Not premises:** A2X units (k7-a2-closure), K62-FULL, M13X (accepted only at K6.2* scope, irrelevant to K7), MK, R2MIX,
  M3R, TX/ZA/ZB, the conditional family closure map, any pending candidate. Computer-assisted Sun(5)/Sun(6) remain
  transitive imports of the accepted theorems.

## 3. Pre-freeze disclosure
Before this freeze I read the transition record, the six accepted K7 verdicts (M0 via LFC/INV, M1, Z2, K63DE-K735, U1,
Z23P5), the D23 and K7-R2 verdicts, the literal theorem statements with every mandatory overlay of M1, Z2, K7-35, U1 and
Z23-P5, and the README class definition. While reading I formed (thought only, unwritten) the expected 8-block table:
(no 2, no 3) with 5 absent / present; (no 2, 3 on t) with 5 absent / on t / elsewhere; (2 on z, no 3) with any 5;
(2 and 3 on z) with 5 absent or on z / elsewhere; and the expected matches M0, M1, M1, M1, K7-35, Z2, U1, Z23-P5. Several
verdict frontier sentences already state this conclusion informally; the deliverable is the exact checked assembly.

## 4. Deliverables
`K7-NF-v1.md` (proof with exact interface/scope table), `review-package-NF-v1.md`, `review-excerpts-NF-v1.json`
(entries {path, sha256, start, end}; package + selected source <= 100 KB), checkpoints `checkpoint-NNN-v1.md` at most
1800 s apart (target 1200 s) with `/bin/date`, IRC of full paths and SHA256s, then park. Every new claim
CANDIDATE_UNVERIFIED; no full K7, Sun(7), novelty, Lean or human-review claim.
