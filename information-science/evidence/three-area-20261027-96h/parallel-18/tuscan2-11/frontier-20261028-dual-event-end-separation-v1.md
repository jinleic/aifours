# End-labelled dual Hall is not redundant with start-labelled tests

Native `/bin/date` observed before writing: **Wed Oct 28 18:12:51 PDT 2026**. This is an **EXACT FINITE CHECKED** separation of special cases of the universal dual Hall theorem in `frontier-20261028-dual-event-hall-obstruction-v1.md`, SHA-256 `dbaa61ad8b19ae023e93c4e701882d73434e96b3240e023de1135ae69563f763`. It is not an unrestricted T2 no-go, witness, novelty claim, or formal/kernel/human/model verification.

Reverse every row of the earlier six-row partial instance. The resulting actual rows are:

```text
6 3 4 8 5 9 0 10 2 7 1
3 2 1 10 6 8 0 5 7 9 4
8 1 4 9 7 0 2 5 3 6 10
2 8 6 7 3 5 0 4 10 1 9
9 2 4 5 6 1 7 8 10 3 0
0 6 4 1 2 10 9 3 7 5 8
```

A separate breadth-first direct enumeration produces all **39** eligible next rows. All missing D1 events have individual support. The D2 event support has size50, exceeding the 45 needed. All 31 nonempty unused-start subsets and all 31 nonempty unused-end subsets satisfy the prior D1/D2 union-support bounds, and the endpoint compatibility graph has a perfect matching `1→2, 4→5, 5→6, 7→3, 10→7`. In addition, **all** per-symbol outgoing-to-start and incoming-to-start dual Hall inequalities pass.

Yet the two still-missing outgoing D1 events `3→1` and `3→9` can only occur in eligible rows ending in symbol **2**. A permutation row has just one outgoing event from3, so these two distinct events need two distinct rows; a T1 completion has unique row ends, but their union of possible ends has cardinality one. The universal event-to-end Hall condition therefore rejects this exact partial array. This explicitly shows that checking only the start-labelled dual Hall special cases does not subsume the end-labelled variant, even after the earlier support and endpoint matching tests. No claim is made for other partial arrays.

The direct checker `frontier-20261028-dual-hall-reversal-check-v1.py` SHA-256 `a36f264b197912dddc2912b07a80335eb76fb757fa70db2da597ec552a0004c4`, and result `frontier-20261028-dual-hall-reversal-check-v1.json` SHA-256 `30a529da275b8f425a7a555fd4dd6175973c9447df504b3538273646102a6fa8`, reconstruct the reversal from `frontier-20261028-dual-hall-probe-run-02.json` SHA-256 `fa107b2b237d763d0786d559e437d23d81f089435bcd32f5851eb3453a50bf2a`, regenerate every eligible permutation, and check all four directed event/endpoint Hall families. The result says outgoing/start and incoming/start have zero failing subsets, outgoing/end has three and incoming/end one. It is finite exact evidence for the displayed instance; the all-variable necessity remains the simple injection proof in the cited theorem.
