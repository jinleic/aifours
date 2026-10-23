# K3 cover / G6 / lex / AMENDMENT-4 static review — parent disposition (phys-2) — 2026-10-18 00:42:59 PDT (host clock)

Source: delegated desk [RESULT.md](moqls7-k3-cover-review-v1/RESULT.md) (`0f80460c1059a10fe6f3c614e55a5fdd7fd2af6606cc0b8b80781cc8d89eef84`) and [RESULT.json](moqls7-k3-cover-review-v1/RESULT.json) (`cf9156fb058d130f0a0bd7c36435dedd7eb7c62bdc2d4a48d92e2c0f0c53a1b2`). Reviews: Codex `moqls7-k3-cover-codex-v1` ACCEPT-WITH-FIXES (0 FATAL, 2 MAJOR, 2 MINOR; note `42392eaa75503f0c0d50925c8941c69a96fbcb95658377be1d67b91acd458809`); Claude `moqls7-k3-cover-claude-v1` ACCEPT-WITH-FIXES (0 FATAL, 2 MAJOR, both on the AMENDMENT-4 draft, 15 MINOR; note `7ab7de84e6d6c7e38de2ea97562860b59834e8b2051d0550d8eab0c28b0479b3`). Static review only; no K3 or M(7) verdict.

## Disposition

| Step | Parent disposition |
|---|---|
| Q1 three-cube cover | **ACCEPTED** as a covering argument (all three readings sound). Wording fix: cite G1 for the zero (0,0) coefficient. |
| Q2 G6 and variable maps | **ACCEPTED** mathematically. The B-map runtime claim in `AMENDMENT-2.r1.md:43-45` is an erratum: index equality for B rests on static reading of `gram_encB.py:113-118`. **No B-route certificate may be relied on until a runtime B-map oracle passes** (for example by driving B's `--fix-json` branch) in a new versioned file. |
| Q3 lex leaders | **ACCEPTED** mathematically, with two text fixes: invariance holds for the base-and-cube g-projection (C411's column (3,4) swap moves unit var109 to cube unit var145), and T(X)_v = X_σ(v) must be defined. |
| Q4 composition and bindings | **FIXES REQUIRED, provenance only.** No soundness defect was found, and the CNF bytes, headers and hashes were verified by the desk. Needed in new sidecars or versions: bind A_C311 lex metadata to source cube metadata `3b2ab04f…` and to the control-receipt SHA; replace the stale driver field (r2 driver `49677766…`, 3600/3600 caps) by binding `K3-CERTIFICATION-DRIVER-DELTA.r2.json`; restate the K2 prerequisite; repoint the Gram r1 citation to Gram r2. |
| Q5 AMENDMENT-4 draft (`d9794b9d…47d7ee`) | **NOT FROZEN; inactive.** Its mathematics is conditionally sound: own row/column frame transport and 238,140 distinct clauses (26,460 + 211,680). Any successor must be a new reviewed version that adds all nine prerequisites listed in the desk RESULT (lines 106–115): an explicit K1/K2/encoder-bridge/minimal-configuration hypothesis, and gating on **parent-accepted** exclusions of the exact C321 (`d598…8388`) and C411 (`2b92…ddf2`) CNFs, not on producer certificates. |

## Consequences for the K3 route

- The K2 prerequisite is now met: [K2 parent verdict](moqls7-k2-parent-verdict.md).
- C321 and C411 currently have producer A-route certificates only. Parent acceptance of each exclusion needs (i) a parent replay of the exact CNF and proof, or an independent B-route certificate after the B-map oracle, plus parent replay; and (ii) a parent verdict naming the exact CNF hashes.
- C311 is unresolved. The two lex screens ended UNKNOWN because of resources, and these records support no lex-screen statement beyond UNKNOWN.
- Desk deviations accepted as recorded: four off-by-few code line references in `desk-analysis.md`, corrected in RESULT.md, with the file left unmodified; the reviewer TMPDIRs are empty.
