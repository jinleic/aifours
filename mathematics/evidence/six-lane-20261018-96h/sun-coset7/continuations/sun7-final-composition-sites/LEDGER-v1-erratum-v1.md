# LEDGER-v1-erratum-v1 — self-check corrections to LEDGER-v1 (bookkeeping only; no mathematical change)

- **Written:** `/bin/date` read at 2026-10-20T00:46:42-0700, immediately before this exclusive create. Owner SunM13MixedFibres, math-1.
- **Applies to:** `LEDGER-v1.md` (this directory) fb8699b77370efcc838be0c4474cf3ba7024ced1a5b909ae4f13511c4daac5de, which stays byte-identical. Found by
  re-reading the rows against section 3 before delivery; read after LEDGER-v1. Every item only adds conservative forward
  edges or narrows a wording; the order N01..N59, acyclicity and the residual list are unchanged.

| # | location | correction |
|---|---|---|
| X1 | section 3 (new convention, read before the table) | A Sun(t) application inside an LFC fibre or a VFC right coset is represented by the edge from N12 or N11, whose inputs contain N01 (Zhu Sun(3)/(4)), N02 (Sun(2)) and N07/N08 (S5W/S6W at sites S4/S5). A direct N01 edge is listed where Sun(3)/(4) is applied outside such fibres (original cosets, K cap L cells) or where the module declares direct Sun instances (conservative). |
| X2 | section 3, rows N40 NO4, N41 RICH, N43 A1S, N44 TC, N45 A22, N46 K23, N49 A2F, N55 DG, N56 M13A | add N01 (cons.: declared direct Sun(2)/(3)/(4) instances at NO4 LF50-51, RICH LF39-40, OV1 A1.4 New LF87-88, OV1 TC header LF242-243, OV1 LF426, K23 LF12-13, F5 LF35, SD LF164-165, M13 LF15); add N02 to N40 (Sun(2), NO4 LF50-51). All are forward edges (N01, N02 < N40). |
| X3 | section 3, row N52 A2X | add N01: Sun(3) inside K cap L in the size-three branch (U3A LF134-139; CA LF38). Forward edge. |
| X4 | row F02 (consumers) | read: "direct edges from N01: N04, N05, N07, N08, N11, N12, N16, N18, N19, N21, N22, N26, N27, N40, N41, N43-N47, N49-N53, N55, N56, N58; every other Sun(3)/(4) use enters through N11/N12 (X1)". |
| X5 | row R14 (consumers) | add N13 (INV uses VFC (V1) for q = alpha*: LE E7 LF56-59) and N16 (RW). |
| X6 | row F22, last sentence | read: "Every node of section 1 except N01 (external) and N59 (the composition text, checked by FR LF55, LF57-61 against C LF57) lies in one of these groups, so the union covers the operative graph (section 3 C2)." |
| X7 | section 4, site S6 (consumers) | read "N14; inherited by N28-N35, N37, N38, N40-N42" (N36 NF consumes theorems, not ROW-U; N39 does not use ROW-U). |
| X8 | section 3, closure C4 | read "Every path from N59 ends at N01 (Zhu) or N02 (ELEM: S56 section 2, LE E1-E2); R0 (N03) depends only on N02." |

No new premise, statement or discharge; no acceptance claim. Full Sun(7) UNACCEPTED.
