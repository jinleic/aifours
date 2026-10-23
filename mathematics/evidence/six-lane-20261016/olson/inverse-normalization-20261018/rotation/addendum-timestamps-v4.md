# Timestamp addendum v4 (rotation slice): approximate labels after 06:37:56

Written after host clock 2026-10-18T14:54:28-07:00 by OlsonRotationRigidity.  Extends addendum-timestamps-v3.md
(fb423070...81bb, kept; it covers labels up to its own writing at 06:37:56).  Every label below containing "x" is NOT a
host-clock read: its timestamp is UNAVAILABLE.  For context only, the nearest exact host-clock reads printed in the
README entries before and after it (README line order) are given.  README entries were mostly, but not always,
appended in event order (e.g. lines 491-497 cite a verdict recorded at 10:25:24 but precede the entry labelled
10:22:24, which names a file-write time), so these neighbours are context, not certified bounds.  No proof content
depends on any of these labels.

| README line | label | item | nearest exact reads (before ; after, in README order) |
|---|---|---|---|
| 306 | 06:4x | results-v3.md written | 06:47:08 ; 06:48:15 |
| 309 | 06:5x | proof-ROT-few-E-v1.md written | 06:49:52 ; 06:51:51 |
| 316 | 06:5x | inline experiment start | 06:51:51 ; 06:59:19 |
| 319 | 06:5x | IRC from OlsonReflectionRigidity | 06:51:51 ; 06:59:38 |
| 322 | 07:0x | proof-INVstar-few-v1.md written | 06:59:38 ; 07:01:11 |
| 329 | ~07:04:1x | parent-reported floor dip (quoted, parent estimate) | 07:01:11 ; 07:04:23 |
| 333 | 07:0x | parent IRC (Codex round B) | 07:08:16 ; 07:09:07 |
| 338 | 07:1x | proof-KAPPA01-v2.md written | 07:09:07 ; 07:10:09 |
| 361 | 07:3x | notes-RIGID-STRUCT-v1.md written | 07:29:58 ; 07:32:27 |
| 365 | 07:3x | proof-OLSON-few-v1.md written | 07:32:27 ; 07:34:34 |
| 369 | 07:3x | proof-OLSON-few-v2.md written | 07:34:34 ; 07:36:37 |
| 372 | 07:4x | parent IRC (round C) and results-v4.md | 07:36:37 ; 07:40:35 |
| 387 | 07:5x | notes-SC-lengthp-addendum-v1.md written | 07:47:41 ; 08:11:21 |
| 390 | 08:0x | parent IRC (option (b), engine review) | 07:47:41 ; 08:11:21 |
| 425 | 08:2x | parent IRC (Claude few-odd chain review) | 08:26:24 ; 08:26:19 (errata it prompted) |
| 431 | 08:3x | proof-ROT-o4-p5-finite-v1.md written | 08:29:40 ; 08:31:59 |
| 434 | 08:4x | notes-SC-lengthp-addendum-v2.md written | 08:31:59 ; 08:35:20 |
| 438 | 08:3x | bundle-v3.md written | 08:35:20 ; 08:40:18 |
| 440 | 08:3x | parent IRC (targeted SHgen-E review) | 08:35:20 ; 08:40:18 |
| 446 | 09:1x | parent IRC (Codex p5o4 review) | 08:40:18 ; 09:25:45 |
| 454 | 09:2x-09:3x | compare_p5o4_v2.py and fixtures written | 09:30:45 ; 09:34:23 |
| 489 | 08:2x | reference to earlier messages | 08:26:01 ; 08:29:30 (the messages' context) |
| 491 | 09:4x-10:1x | parent IRC (replay, reviews) | 09:36:55 ; 10:22:24 |
| 496 | 10:2x | parent verdict p5o4 (file records 10:25:24) | 09:36:55 ; 10:22:24 (out of order, see above) |
| 505 | 10:2x-10:3x | eval transcript of the lift checks | 10:27:55 ; 10:32:16 |
| 515 | 10:3x | parent IRC (lift accepted) | 10:32:16 ; 10:57:16 |
| 531 | 11:0x | parent IRC (v1 frozen, reviews) | 11:01:35 ; 11:06:17 |
| 534 | 11:0x | zs-check-v1 freeze end | 11:06:17 ; 11:06:47 |
| 550 | 11:2x | parent IRC (half range accepted; file records 11:18:04) | 11:21:49 ; 11:40:01 |
| 560 | 11:2x-11:3x | parent IRC (ZS v2 reviews) | 11:40:01 ; 11:44:02 |
| 567 | 11:4x | parent IRC (v2 both-family) | 11:44:02 ; 11:47:04 |
| 576 | 11:5x | parent IRC (ZX v1 under review) | 11:47:42 ; 11:53:11 |
| 590 | 12:1x | parent verdict ZX/S1c (file records 12:13:33) | 11:57:01 ; 12:26:59 |
| 605 | 12:2x-12:3x | parent IRC (index-one import identified) | 12:34:38 ; 12:38:08 |
| 659 | 12:5x | parent IRC (B-classification) | 12:55:10 ; 12:59:59 |
| 727 | 13:4x | parent IRC (K01 under review) | 13:40:20 (message sent) ; 13:52:18 (append) |
| 743 | 14:3x | parent ruling on t-search-v2 | corrected at line 748: appended at 14:19:46 |

Also: proof-ROT-K0-v2.md header "13:37:3x" (actual reads 13:37:31 before writing, 13:37:48 after; README line 729);
proof-ROT-ZX-addendum-S1g-v2.md header "after 13:03:20" is a lower bound (actual read 13:03:27; README line 673);
t-search-v2/gate_v1.sh line 2 "13:17 PDT" is an estimated label from a parent message (actual launch 13:14:14).
From 13:52 onward new entries carry actual date reads, except line 743 (corrected).
