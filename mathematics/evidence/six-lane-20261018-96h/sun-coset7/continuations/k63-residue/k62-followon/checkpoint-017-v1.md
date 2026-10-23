# k62-followon checkpoint 017 (Sun63Successor) — ONE M13 written slice frozen, Parts A-D

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T08:04:48-0700.
- Previous checkpoint: `checkpoint-016-v1.md`, sha256 3cfbed2a4dda19f60ec38e0ca07f5db6ff28973aa81d9e84e33a77141bac3125.

## New since 016
| file | sha256 |
|---|---|
| `K62-M13-C-v1.md` | 13f2c8dc42a95be24b819ec3cf68dbb178140bb2cd876b2c491d941d1e552e12 |
| `K62-M13-D-v1.md` | d5fabd614afd1ef626d206df01f165db25883e54668c5ceab1e8ca69b7462194 |

## Complete slice inventory
| file | sha256 | status / scope |
|---|---|---|
| `K62-M13-SCOPE-v1.md` | e5795694e99c0d0ae535bd0b8edf6d8d58d2fd17683f1abbaf3498ac5ce5d625 | scope only (timing correction below) |
| `K62-M13-A-v1.md` | 77ce4077584582c699ce1bec870f2b19c55242bfc05aac99febcfbd69c466a8d | candidate, accepted imports only: second-family d-count/DG/C2/budget in (1,3) |
| `K62-M13-B-v1.md` | 455c58f9d35cc165f666eeaec9462e6b6ab6286196450532e619d6c0b9810058 | candidate: B1/B2 accepted imports only, B3 conditional on CAP/DT verdict |
| `K62-M13-C-v1.md` | 13f2c8dc42a95be24b819ec3cf68dbb178140bb2cd876b2c491d941d1e552e12 | candidate, conditional: missing granularity, both-row bounds, both-family CI at unmarked O-vertices |
| `K62-M13-D-v1.md` | d5fabd614afd1ef626d206df01f165db25883e54668c5ceab1e8ca69b7462194 | candidate, conditional: R4/R3 with marked neighbours; local degree/parity at unmarked O-vertices |

## Dependency edges
- A -> accepted LFC/INV, K62-E3 (Z10/Z11), DG-1/DG-3. No CAP/DT premise.
- B1/B2 -> accepted LFC/INV and SH (ii); B3 -> CAP/DT Lemma RC (RC-i*, f* = 1).
- C1w is an arithmetic implication given a small-entry witness; witness existence C2 -> B1+B3. Row consequences -> Lemma
  RC; original low-family granularity -> CAP (C1) at its exact distinguished-entry-1 scope. CI13 is re-proved with the
  new granularity, not applied outside CI's old scope. Section 4 also cites A.
- D -> C's global 5/6 bounds; positive-support certificates are re-proved, not imports from the G-only DT-B statements.
All conditional edges stay conditional until the CAP/DT verdict, and all new claims remain unreviewed candidates.

## Material written gain
A supplies DG/C2 in both families of (1,3), using the four-piece fibres' forced special pair (t,i*) rather than falsely
assuming at most three pieces. B supplies an i*-row small-entry gap. C uses that gap to add i* last with k <= 6, recovering
the missing granularity and CI for the high family at unmarked O-vertices. D re-proves both row obstructions there,
repairing the 3/5-marker positive-support exceptions. Thus both families have the usual local degree/parity rules at
unmarked vertices, but marked centres still escape the global degree / cherry arguments. No K4/bowtie/global-pattern
closure is claimed.

## Process corrections / deviations
- **Scope timing correction:** preliminary hand reasoning about the inverted d-fibre count and i*-row certificates took
  place before `K62-M13-SCOPE-v1.md` was frozen. The scope note was frozen before any of Parts A-D were written, but not
  before all exploratory derivation. The note's phrase "before any derivation" is withdrawn as inaccurate. The parent's
  requested ordering was not fully met; no preregistration claim is made.
- **Scope wording correction:** C clarifies that "CAP (C1) fails in general for alpha*" in the scope note meant that its
  hypothesis is unmet, not that a counterexample to its conclusion was proved.

## Closeout boundary
This ONE written slice is complete at the stated partial-result boundary and sent to the parent. No new computation GO,
no process, no enumeration. The remaining marked-centre patterns, the (1,3)/(3,1) regimes, full K6.2* and full Sun(7) remain
OPEN. Computer-assisted Sun(5)/(6) provenance remains in the import closure. Parked pending parent review/steering.
