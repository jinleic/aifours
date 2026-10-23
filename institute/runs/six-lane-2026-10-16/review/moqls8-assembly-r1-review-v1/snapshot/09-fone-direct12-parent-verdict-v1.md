# MOQLS(8) F_one direct leaves: all twelve accepted (addendum to the first-ten verdict)

Parent at 2026-10-18T05:49:44-07:00: the two remaining direct leaves **P2-C3 and P2-C4 are accepted UNSAT** as exact-formula facts under measured-feed parent native replay. Together with the [first-ten verdict](moqls8-fone-first10-parent-verdict-v1.md), **all 12 direct F_one leaves** (P0-B1..B6, P1-B4, P1-B6, P2-C1..C4) are parent-accepted. This is per-leaf formula evidence only. P1-B1, P1-B2, P1-B3 and P1-B5 remain open, so no K4/K5 exclusion and no Ball–Simoens Problem 16 conclusion at n=8 follows.

| Leaf | Exact formula SHA256 | Measured feed bytes | Parent receipt SHA256 |
|---|---|---|---|
| P2-C3 | `5fc6827fa9cb2856ae1ad14d1aa319f51305296ede72acb7b188060288ae5597` | 137,663,264 | `acd0763c44f93eff3c804351ce9c421c3e354559c739988a66d70feff43a961d` |
| P2-C4 | `32c4d3db7af5da46151238836dfb14f36e782ca87d139c8ae38211a1ab663b94` | 137,663,263 | `2bbd69e3f7fafe31e35c4dbf9a8023e159d248f09cc18e0135c105a6edc12070` |

Evidence: desk addendum `RESULT-ADDENDUM-v1.json` (`a051418a…8bab`); the original RESULT is unchanged (`f63dbeeb…ee0c`). The run (05:44:29–05:48:08) followed the immutable [release](moqls8-lane-admissions-v1/pilot-P1-B1-release-v1.json) (`721c0eda…9050`), with a fresh pre-exec pin. A new parent [receipt audit](moqls8-fone-direct12-parent-receipt-audit-v1.json) (`891e52bdbccc381cfceac47047b963ae1ab48ffc2a4fd6e631b1e6ff959ed262`) re-hashed receipts, pre-exec, script and raw logs. It checked:
- exact `s UNSATISFIABLE` and `s VERIFIED` lines, removing only CR;
- solver rc20 and checker rc0;
- no NOT VERIFIED or TIMEOUT;
- both feeds complete, with length and hash equal to the parent binding and the manifest.
Same trust boundary as before: untrusted CaDiCaL, parent drat-trim `a46c0c71…8e37`, the hash-bound encoder bridge and the conditionally accepted unified reduction.

Remaining obligation: closed and parent-replayed covers for the four UNKNOWN P1 templates. Two routes:
- the original refinement covers (lifecycle on HOLD);
- the proposed Boolean model-existence normal form (`P1_COLUMN0_BOOLEAN_NORMAL_FORM.r1`, `5c748dd8…faa4`). Codex review: ACCEPT-WITH-FIXES, 0 FATAL/MAJOR. A parent finite local/format check passed. Claude review is pending.
If the normal form is accepted, six strengthened formulas must be refuted and parent-replayed. Only after that and the theorem assembly can n=8 be stated.
