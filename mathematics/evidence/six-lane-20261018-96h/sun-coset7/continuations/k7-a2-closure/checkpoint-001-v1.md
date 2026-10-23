# k7-a2-closure checkpoint 001 — scope frozen; inputs read; route chosen (no claim yet)

- **Written:** `/bin/date` read at 2026-10-19T13:34:11-0700, immediately before this file. Slice authority: transition
  4b617b815ae3ae96adc769e86b84e7840fd79612967da605be5e113800092697. Previous lane checkpoint:
  `../k62-full-closure/checkpoint-002-v1.md` (23363fe8…4eac).
- **Process note (parent provenance erratum on K62-FULL):** unknown message times are no longer written; only
  `/bin/date` readings appear in my files.
- **Frozen scope:** `K7-A2-SCOPE-v1.md`, sha256 4a9502ac1116a4a0f06a92ffa8fc95e00a60595fe051085ffb5fa17f0a2ee320 (written before any derivation).

## Actual result
Read (no derivation written): the four accepted verdicts (K7-R2 9b0f7df5, A1/A2 2a7c5b6c, RICH/D23P 1167bc4f, LFC/INV
8621e744); A2-FIVE (Lemma F, FG-a2, D23-a2, ZT5 S1-S5, BRIDGE, TRANSFER); A1-STRUCT; K23 and CELL with the R2 repair erratum
E1-E29; the conditional closure map v2; pending TX, ZA, ZB, ZE1-ZE4; Codex first-family outputs of R3a/R3b (ACCEPT-WITH-FIXES,
EQ five-index repair; R3a/R3b second family NO_VERDICT, so nothing there is a premise).
Assessment: (a2-no5) has FULL granularity at W-apexes in both orientations (accepted FG-a2), so it needs only a re-derived
K23/CASEB-T/CELL chain with p in W (labels of p carry 5^B, never shared because no entry is 5). (a2-zt5) has full
granularity only for alpha-rows; alpha*-side bounds at W-apexes are available only for z-free or t-free subsets (checked: the
chain step adding the second of z, t has gcd >= 18 and multipliers up to 10-12, so primes > 5 dividing w_u are not excluded).

## Blocker
None yet; the route is long. No claim.

## Next bounded action
Write unit U1: the exact (a2) partition and a consolidated re-derivation of the K23/CELL chain in an explicit
restricted-granularity setting, applied to (a2-no5). Then units for (a2-zt5). Next checkpoint by 14:15.
