# Cyclic (v,5,1) difference families: parent verdict

## Results

**Cyclic (321,5,1), (501,5,1), (621,5,1) and (681,5,1) difference families exist.** Each certificate lists (v−1)/20 base blocks of five residues mod v. Their v−1 ordered differences cover every nonzero residue mod v exactly once. Equivalent forms: a perfect (v,5,1) optical orthogonal code, and a strictly cyclic Steiner system S(2,5,v).

| Order | Blocks | Witness | SHA-256 | Pinned copy |
|---|---|---|---|---|
| 501 | 25 | main | `517e02fa330269323f70de11e66ac89aac97da106775efb7dca1d674fd7aab74` | [`cdf501-parent-inputs-v1/cdf_501.txt`](cdf501-parent-inputs-v1/cdf_501.txt) |
| 501 | 25 | second (seed 2) | `fd1f9a6559e7ddf2534441a9672670b1a93c6db593d31103aa2ba939b68ded0a` | [`cdf501-parent-inputs-v1/cdf_501_alt_seed2.txt`](cdf501-parent-inputs-v1/cdf_501_alt_seed2.txt) |
| 321 | 16 | main | `0304c61ba5f0a756259c0d12970f1e0d6c4e4909d931e997c7e37312dc37034b` | [`cdf321-parent-inputs-v1/cdf_321.txt`](cdf321-parent-inputs-v1/cdf_321.txt) |
| 321 | 16 | seeds 2, 3 | `a71174db…a392`, `789bc79b…3016` | [`cdf321-parent-inputs-v1/`](cdf321-parent-inputs-v1/manifest.json) |
| 681 | 34 | main | `16af75391a6b01bd6fc7ee8ec45bd3b53396bd72403e667297af89c1dc09f7b7` | [`cdf681-parent-inputs-v1/cdf_681.txt`](cdf681-parent-inputs-v1/cdf_681.txt) |
| 621 | 31 | main | `257d85f25cd85afc06f6762f1a8f7d4f72e37cbfde806927838f1ac6b7ae05f5` | [`cdf621-parent-inputs-v1/cdf_621.txt`](cdf621-parent-inputs-v1/cdf_621.txt) |

Worker-reported discovery times (host-clock file mtimes, corrected by the worker): 501 at 22:59:50 PDT and 23:00:02 PDT; 321 at 23:15:55 PDT; 681 at 23:23:23 PDT. The worker reports a byte-exact replay of the 321 main certificate from its search program and seed; the parent has not replayed that run.

## Open-status sources (read by the parent)

- Abel, Costa, Finizio, *Discrete Appl. Math.* 143 (2004) 43–53, Theorem 14: a cyclic (v,5,1) DF exists for every v ≡ 1 (mod 20), v ≤ 1001, except possibly v ∈ {321, 501, 621, 681, 801, 901}. In §3 they note that the Handbook's Remark 4.10.18 had listed 501, 681 and 801 as known, incorrectly.
- Hetman, Baicheva, Topalova, *J. Algebra Comb. Discrete Appl.* 13(1) (2026) 111–119, §1 (accepted 20 Sep 2025): "A (20t+1,5,1) CDF exists for 1 ≤ t ≤ 50 except possibly for t = 16, 25, 31, 34, 40, 45." Here t = 16, 25, 31 and 34 are v = 321, 501, 621 and 681.
- Baicheva–Topalova, [*Axioms* 15(1):35 (1 Jan 2026)](https://doi.org/10.3390/axioms15010035), pp.2–4: the same six exceptions, and the equivalence with perfect CPCW codes and strictly cyclic designs ([parent-read excerpt and access limits](cdf-latest-primary-excerpt.txt)).

## Verification

| Gate | Result | Artifact |
|---|---|---|
| Parent stdlib checker (strict parser, exact difference multiset, developed pair coverage, periodic correlation ≤ 1) | 501: VALID for both witnesses | [`cdf501-parent-verification-v1.json`](cdf501-parent-verification-v1.json), [`cdf501-alt-parent-verification-v1.json`](cdf501-alt-parent-verification-v1.json) |
| Parent checker controls | 5 literature positives (v = 81, 121, 141, 221, and 381 with a multiplier expansion) accept; 9 mutations reject for their intended reason; fixtures retained | [`cdf-checker-controls-v2.json`](cdf-checker-controls-v2.json) |
| Cross-vendor checker: written by Claude Opus 5.5 (max effort) from the definition alone; executed by the parent | 501: VALID for both witnesses, under `python3` and `python3 -O`. A wrong SHA, a wrong v and all 9 negative fixtures reject for their intended reasons; all 5 positives accept | [`cdf-claude-verifier-v1/`](cdf-claude-verifier-v1/parent-execution.json) |
| 321: parent checker and cross-vendor checker | VALID for all three witnesses (16 blocks; 320 differences once; 51,360 developed pairs once; correlation 1) | [`cdf321-verification-receipt.json`](cdf321-verification-receipt.json) |
| 681: parent checker and cross-vendor checker | VALID (34 blocks; 680 differences once; developed pairs once; correlation 1) | [`cdf681-verification-receipt.json`](cdf681-verification-receipt.json) |
| 621: parent checker and cross-vendor checker | VALID (31 blocks; 620 differences once; 192,510 developed pairs once; correlation 1), including the cross-vendor checker under `python3 -O` | [`cdf621-verification-receipt.json`](cdf621-verification-receipt.json) |
| Worker lane verifier | ACCEPT for all four orders, with its own controls (24 literature families; 117 mutations rejected for the intended check) | `information-science/evidence/six-lane-20261016/cdf-k5/` |
| Structural claim audit (501) | Every block's difference multiset is stable under x ↦ 166x: 20 blocks are invariant and 5 map to translates of their negatives. The family as a whole is **not** closed under 166, so 166 is not a multiplier in the sense of Hetman–Baicheva–Topalova Definition 1.2. The certificate's validity does not depend on this | [`cdf501-multiplier-parent-audit.json`](cdf501-multiplier-parent-audit.json) |
| Structural claim audit (621) | Under x ↦ 298x, 27 blocks map to translates of base blocks (5 fixed, 22 swapped), but 4 map only to translates of their own negatives. Thus 298 is not a multiplier in the translation-only sense; validity is unaffected | [`cdf621-multiplier-parent-audit.json`](cdf621-multiplier-parent-audit.json) |

The three implementations are independent: the worker's, the parent's, and the Claude-written checker run by the parent. All three read the same pinned bytes.

## Priority and significance

A read-only priority audit ([report](cdf-k5-priority-audit.md)) located **no earlier construction, announcement or nonexistence proof** for any of 321, 501, 621, 681, 801, 901. The newest status statements still list all six as possible exceptions: Hetman–Baicheva–Topalova (online 22 Dec 2025) and Baicheva–Topalova, *Axioms* 15(1):35 (1 Jan 2026), both read by the parent. Later 2026 papers from the same group do not touch these orders according to the scout. The 1996 Handbook listed 501, 681 and 801 as known; Abel–Costa–Finizio 2004 declared that listing incorrect. No such object was located in the bounded Sage database, Baicheva–Topalova data-page, openai/math or EulerSolve screen. Residual risks: the unread body of the Handbook 2nd edition (2007) §VI.16, paywalled 2004–2024 OOC/whist papers, and unindexed venues. A search miss does not establish priority; avoid "first".

Significance: **modest specialist finite results.** Each settles one of six explicitly named small open cases in the existence spectrum of cyclic (v,5,1) difference families below 1001, open since 2004 and restated in 2025–2026. The methods are standard computer search with structured difference-class and Chinese-remainder reductions. If all six close, the cyclic spectrum for v ≡ 1 (mod 20), v ≤ 1001 is complete. The remaining orders 801 and 901 are still being searched.

**FRONTIER:** certified finite cases (321, 501, 621, 681) meeting the contract's finite-target gate (explicit open statement, independent verification with a cross-vendor checker, primary-source comparison, bounded priority audit); NOVELTY-UNCLEAR in the strict sense because the audit is bounded.
