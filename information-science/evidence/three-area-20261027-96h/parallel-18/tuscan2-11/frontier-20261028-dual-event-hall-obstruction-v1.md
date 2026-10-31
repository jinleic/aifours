# Per-symbol event-to-row Hall obstruction: a strict strengthening

Native `/bin/date` observed before writing: **Wed Oct 28 18:09:23 PDT 2026**. **WRITTEN universal necessary condition**, plus a separately checked finite example. It applies to every actual T2(n) completion and n≥3; it is not an unrestricted nonexistence result, a T2 witness, novelty claim, or formal/kernel/human/model verification. The earlier start/end-to-event conditions are in `frontier-20261028-row-support-hall-obstruction-v1.md`, SHA-256 `92387d63301a8d86589fa061c51adc4f19dd4fd703e212e8e29ec08fd3a39289`.

## The universal dual Hall condition

Let P be any k rows of the SAME hypothetical T2(n) array. Let S be the n−k unused starting symbols and let Ω(P) contain **every** permutation row compatible with the D1/D2 events and endpoints already used by P (or any independently justified superset of those rows). As shown in the earlier packet, D1 completeness forces exactly one row with each start.

Fix a symbol a and any set F of directed D1 pairs `(a,b)` not yet used by P. These pairs MUST all occur in any completion because n(n−1) distinct D1 events exhaust every ordered nonloop. Distinct members of F must occur in distinct future rows: a permutation row contains a exactly once, so has at most one outgoing adjacency from a. Each such row also has a distinct first symbol in S. Define

`N_P(F) = {s∈S : some row in Ω(P) starts at s and contains a pair of F at distance 1}`.

The required actual rows give an injection from F into N_P(F). Therefore, for **every** a and **every** F consisting of still-missing outgoing D1 pairs of a,

`|N_P(F)| ≥ |F|`.

The same proof holds for sets of still-missing incoming pairs `(b,a)`, since a row has at most one incoming adjacency to a, and also with unused ending symbols used as the row labels. These are necessary conditions only: the existence of all such matchings does not itself construct compatible rows or prove a T2 completion. The complete/superset requirement on Ω is essential; an arbitrary restricted search neighborhood is not a sound source of a global exclusion.

## Checked strict separation from the previous Hall conditions

Consider the following actual six-row partial array on `0,...,10`. The first three are rows3,5,10 of `frontier-20261028-three-row-fast-run-01.json`, SHA-256 `fe7742f066d2a0a6d996eab1f2b65bc4f3c12b2032443de7f5af6154678e14fb`; the last three were found by the bounded probe:

```text
1 7 2 10 0 9 5 8 4 3 6
4 9 7 5 0 8 6 10 1 2 3
10 6 3 5 2 0 7 9 4 1 8
9 1 10 4 0 5 3 7 6 8 2
0 3 10 8 7 1 6 5 4 2 9
8 5 7 3 9 10 2 1 4 6 0
```

Its 60 D1 and 54 D2 events are individually distinct, and its six starts and six ends are distinct. A separately written breadth-first prefix generator found **all 39** eligible next rows in 2,443 prefix nodes. The five unused starts are `{2,3,5,6,7}` and the five unused ends are `{1,4,5,7,10}`.

The earlier tests all pass for this partial array: every one of the 50 missing D1 events is individually supported; the eligible rows support **50** D2 events, at least the 45 required; the available endpoint graph even has matching `2→1, 3→7, 5→4, 6→5, 7→10`. Moreover ALL 31 nonempty subsets of unused starts and ALL 31 nonempty subsets of unused ends satisfy both previously stated D1- and D2-support lower bounds. Thus this is not merely a failure of a previously published singleton, aggregate, endpoint-matching or all-subset support test.

However the three missing D1 pairs `(1,0),(1,3),(1,5)` have eligible-row start neighborhoods respectively `{3}`, `{2}`, and `{2,3}`. All three are individually possible, but their joint neighborhood is only `{2,3}`. Each must appear in a different future row and those rows have different starts, so the dual Hall condition demands three distinct starts but only two are available. Therefore **this concrete six-row partial set has no T2(11) completion**. This is strictly stronger on this example than the earlier independently checked Hall/support conditions, but no claim is made that every six-row partial array fails the new condition.

## Evidence

The bounded exact diagnostic `frontier-20261028-dual-hall-probe-v2.py`, SHA-256 `dece106a6711f8ef842fe32c4244bd249a512059d9ff720795a4de1740bb5c9e`, found the partial array after 44 attempts, of which 13 gave compatible six-row samples; its output `frontier-20261028-dual-hall-probe-run-02.json` has SHA-256 `fa107b2b237d763d0786d559e437d23d81f089435bcd32f5851eb3453a50bf2a`. This bounded sampling is used only to locate the concrete instance, not to establish a universal claim.

The separately written BFS checker `frontier-20261028-dual-hall-check-v2.py`, SHA-256 `1a8066d7019b383d95296743eb7048a3478f225cc784db06d21ead443fdd96cb`, regenerated all 39 eligible rows and all 62 start/end support subsets, checked the endpoint matching and exact event neighborhoods; its output `frontier-20261028-dual-hall-check-run-02.json`, SHA-256 `8aab52e50358d3e30e6845c4fa89f84079a6cdd387ea0622a178758af461a199`. The implementations share the elementary eligibility definition; this is exact finite corroboration, not a formal proof certificate. The theorem itself is the written injection argument and does not depend on the sample.
