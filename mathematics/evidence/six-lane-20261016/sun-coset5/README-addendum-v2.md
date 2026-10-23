# README addendum v2

Written 2026-10-18, finished at or before 09:57 PDT by the host clock. The freeze time is recorded in `evidence/proof-v2.sha256`. This addendum does not change `README.md` (6bff400c…a75e), which stays frozen.

## 1. R1 arrow labels were reversed (Codex additional note)

In README §2 R1, the two halves of the proof carry swapped labels.

- **The paragraph marked "(⇐)"** ("Core(5) is a special case of the target") actually proves **Sun(5) ⇒ Core(5)**. A Core(5) configuration has every pairwise gcd equal to 4, so it would contradict Sun(5).
- **The paragraph marked "(⇒)"** ("suppose five disjoint cosets have all pairwise gcds ≤ 4 … Core(5) configuration") actually proves **Core(5) ⇒ Sun(5)**, by contraposition.

The mathematics in both paragraphs is unchanged; only the labels were swapped.

## 2. M-S Lemma 4.4

README §2 says the first bullet of M-S Lemma 4.4 is "misprinted". It is not. The paper reads α ≠ 2, and the "= 2" came from text extraction. See `rules-v1-erratum-v1.md` E3.

## 3. Timestamps

As already stated in `README-addendum-v1.md`, the creation times written inside `README.md` ("about 09:40") and `rules-v1.md` ("about 09:35") were estimates. The governing time is the host-clock record: freeze at 09:33:21 PDT (`evidence/freeze-v1.sha256`). Throughout the lane, the filesystem, freeze-manifest and command-clock records take precedence over any time written in the text of a file.

## 4. Current candidate

The current candidate is `proof-v2.md`. It supersedes `proof-v1.md`, which remains frozen. The independent checker `code/core5_check_v2.py` (9e4aac2a…48ae2) found 0 survivors among all 2,125,764 labelled patterns (`evidence/check-v2-run1/summary.json`).

Status is CANDIDATE: computer-assisted, not Lean-checked, and the gate is not claimed. The pending items are:
- the parent's finite audit;
- the Claude written review;
- the post-result priority audit.
