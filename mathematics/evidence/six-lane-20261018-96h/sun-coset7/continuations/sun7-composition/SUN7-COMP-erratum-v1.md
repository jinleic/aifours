# SUN7-COMP-erratum-v1 — mandatory precision overlay to SUN7-COMP-v1.md (no statement, case or premise change)

- **Written:** `/bin/date` read at 2026-10-19T16:38:54-0700, immediately before this exclusive write. Owner SunM13MixedFibres (self-check after
  freezing; no review input). Applies to `SUN7-COMP-v1.md`, sha256 98796f95bf2faa7f0530ad9d4d999817fb5234d89ea09ea35eb232f2954913d7, which stays byte-identical.
- Every new claim remains CANDIDATE_UNVERIFIED and CONDITIONAL. Read the old text with these replacements.

| # | location in SUN7-COMP-v1.md | old | new |
|---|---|---|---|
| P1 | line 54 (section 2, K5.3 row) | X1 clarification (49f956b2…c0a9) | X1 clarification (49f956b2…a0c9); full sha256 49f956b2c6d0b8a17abaf2bd59e070b483792243f49d2fb54ac9def65297a0c9, as already given in line 113 |
| P2 | line 118 (section 5, K2 row) | A1/A2 repairs (… 2a7c5b6c…6966) | A1/A2 repairs (… 2a7c5b6c…f966); full sha256 2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966 |
| P3 | lines 121-122 (acyclicity sentence) | N0 -> N1..N7 -> {C1..C4, K1..K3} -> T | the foundation layer N0-N7 (N1 is an external import and imports nothing; N0 imports nothing) -> {C1..C4, K1..K3} -> T |
| P4 | lines 133-134 (section 6) | Written-only class chains: C2 (computation-free), C3, C4, K1-K3 (each transitively imports N2/N3 through N6/N7). | Written-only class chains: C2's own proof is computation-free and imports neither N2 nor N3; C3, C4, K1-K3 each import N2/N3 transitively through N7. Every class (including K5.3) is reached only through N6, which uses N2 and N3. |
| P5 | lines 160-161 (section 9) | Context-only lines in U0 never replace the proofs of K0-K3: K0 is proved here, K1-K3 are proved in full in U1-U4. | Context-only lines in U0 never replace the proofs of the new nodes: K0 and T are proved in U0 (this file), K1 (K7-NF) in full in U1, K3 (A2X: units 1-3) in full in U2-U4. K2 is an ACCEPTED node (R2 verdict) cited at its literal scope, not a new node. |

Unchanged: Lemma CE-LIFT, Corollary COVER, Lemma K7-SPLIT, the hypotheses (H-NF)/(H-A2X), Theorem SUN7-COMP and its proof,
all DAG statuses/imports, the computation boundary and every gate. No scientific computation; metadata only.
