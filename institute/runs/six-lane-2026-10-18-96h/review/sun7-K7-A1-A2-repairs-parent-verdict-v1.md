# Sun(7) lane: K7 A1-STRUCT, TC, TC-A22 and A2-FIVE repairs

Recorded at 2026-10-19T08:24:22-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL.** This verdict accepts written, model-reviewed proofs relative to the accepted RICH/D23P verdict (`1167bc4f…`) and LFC/INV verdict (`8621e744…`). Every closure includes the computer-assisted Sun(5)/Sun(6) imports. K6.2*, full K7 and Sun(7) all remain **OPEN**.

## Text of record

The four frozen sources are read through [overlay v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A1-A2-delta-erratum-v1.md) `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e` and then [overlay v2](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A1-A2-delta-erratum-v2.md) `9580ef7996d92d94f3f68c0df8934ab4889aeed227406e670cfd413281443181`, which amends v1:

| Source | sha256 |
|---|---|
| [A1-STRUCT](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A1-STRUCT-v1.md) | `c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf` |
| [TC](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-TC-v1.md) | `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117` |
| [TC-A22](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-TC-A22-v1.md) | `9ebec2797485ac18ff1f1080cafd0634edd86117d166338631e04c4db1a46b41` |
| [A2-FIVE](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A2-FIVE-v1.md) | `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc` |

The parent read v2 in full. It implements the reviewers' minimal fixes and strengthens no statement. In particular:
- V2.6 states the actual-family marked-first chain for every Q, including empty and singleton Q. This removes the remaining reliance on the earlier FG7-use inventory.
- V2.7 adds β_zu ≤ 3 on W′ via D23P, and adds (iv′) for the new R1/A22 consumers.
- V2.8 replaces the TC-P proof with Codex's minimal one: R1 at u3 and Lemma TC at u4 give D_u2∩D_u3=∅; then 4/6 + 2/6 = 1, which contradicts V4.

## Accepted conclusions

**(a1)**
- Corollary W3 (W3 = W3* = ∅, and all W–W entries in {1,2,4}); Lemma E3; Lemma PFG-t (i)/(ii) under connectivity, with Corollary L as a necessary condition only; Lemma B and Theorem CASEB under their stated hypotheses.
- Lemma TC and Lemma FG-V (finite G; actual families only).
- R1 for every E≥1; R3, R4, R5 and the ({1,4,4,4}|c|1) exclusion for E≥2.
- Theorem K7-TC-B: α*_v1v2 = 2 and α* = 2 on T*.
- Proposition TC-P for the TC.11 matrix data. It is generalised to every E≥1 via TC.4, so Pc5′ is not realised.
- Theorem K7-TC-A22 for every E≥1 and every group. Case A with two fours in each orientation at every W-vertex is excluded.

**(a2)**
- Lemma F: only the z–t entry can be 5, and in at most one orientation.
- FG-a2, Corollary 5/6-a2, D23-a2, and Proposition ZT5 (S1)–(S5).
- Theorem K7-A2-BRIDGE in its enumerated A2.10 form.
- Corollary K7-A2-TRANSFER for exactly its named list in (a2-no5), with W = W′∪{p}.

## Reviews

- [Codex repair review](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K7-A1-A2-repair-codex-v1.prompt.stdout.txt) `1697abdf74e577e7ec9ab673bb50b3161bfce6b836816e602536a1f45af4ecde`, observed gpt-6.1-sol max, read-only: ACCEPT_REPAIRS_WITH_FIXES, 0 FATAL / 0 MAJOR / 3 MINOR (M1–M3), all folded into v2.
- [Claude repair review](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K7-A1-A2-repair-claude-v1.prompt.note.md) `66c93000ab9a35aaa34b004e6262e82b698dd657dd283c613366d91dd4bf8157`, observed claude-opus-5-5 max, no tools: 0 FATAL / 0 MAJOR / 7 MINOR plus 4 optional, all folded into v2.

## Not accepted or open

- **Bound by their own hypotheses:** PFG-t (connectivity), CC (separation), TC-B (Case B), A22 (Case A plus the A22 hypothesis), and S1–S4 (survivors only).
- **Not transferred:** FG7 for auxiliary families; RICH §§6 and 9; A1-STRUCT §§6–7; TC §§5–6, including Q_B′; A22 §4.
- **Open:**
  - (a1) as a whole;
  - Case A four-degree patterns (3,1), (1,3), (2,1), (1,2);
  - the Case B residue;
  - (a2-zt5) beyond S1–S5;
  - the (a2-no5) residue;
  - K6.2*, full K7 and Sun(7).
- **Pending, not part of this verdict:** the candidates CASEA-K23, K7-CELL, the A2-ZT5 errata v1–v4 and the conditional closure map. They are pending their own dual review.
- **No novelty claim.**
