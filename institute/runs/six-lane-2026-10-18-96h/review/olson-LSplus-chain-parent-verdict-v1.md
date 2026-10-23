# Olson sequence lane: LS+ linear band

Recorded at 2026-10-19T07:35:52-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL.** This is a sequence-level written result, relative to the accepted imports below. It does not prove unrestricted LS+, STAB, INV* or ordered Olson. No computation or Lean verification was used.

## Accepted statement

For a prime p and an integer kappa with floor(2p/3)+1 <= kappa <= p-2, put e=p-kappa. Let Y be an odd sequence over C_(2p) with no zero-sum subsequence of even length in [2kappa+2,2p], and containing a long zero-sum (length >=2p+2). Then |Y| <=3kappa+1 if either
- e=2 and p>=7, or
- e>=3 and p>=10e-13.

E2(kappa)=h^(3kappa-p+2)(3h)^(p-1) and E3(kappa)=h^(3kappa-2p+2)(3h)^(2p-1), for an odd generator h, attain the bound. In every covered cell this is verified by a direct CF(a) calculation and an exhibited length-(2p+2) zero-sum subsequence. Earlier LS+2 acceptance is not stretched to these new kappa values.

The chain also accepts these intermediate results:
- **LS+-RED:** under p>=9e-13 there is exactly one heavy generator, and the reduced zero-sum-free core has multiplier a in (-1, -0.5).
- **Addendum 1:** the a=-1 case is excluded for p>=10e-13.
- **Addendum 2:** the a=-1/2 case is excluded for prime p>=10e-13. Its Remark4 holds at its stated range but is not used.

## Coverage boundary

- The band e>=3, p>=10e-13 adds **no new LS cell**: those cells are already in the accepted LS-lin range. The e=2 cells are the earlier LS-small/LS+2 cells.
- BASE1+ cells remain accepted through the separate delta verdict, not through this chain.
- Undecided cells are exactly those with 3<=e<=floor((p-1)/3) and p<10e-13, excluding the separately accepted BASE1+ cells. Examples: (11,8), (13,10), (17,12-13), (19,14-15), (23,16-19), (29,20-24), (31,22-26). "Undecided" means not decided by these arguments, not a counterexample.
- STAB is accepted only at the BASE1 cells. The listed alternatives for a and the classification remarks for length 3kappa+1 are [INFERENCE], not conclusions.

## Texts and reviews

- Governing [consolidated erratum v3](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/erratum-1-lsplus-chain-consolidated-v3.md) `f1573d6c8b1ac00afe3ce438ff5ebca64cce1e4c2682aaf3ef01e18831a608c0`. Read the four frozen chain files through it; v1/v2 were never sent and do not govern.
- [Codex](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-LSplus-chain-codex-v1.prompt.stdout.txt) `0c82174fe2d9dc4d4cd15f75927ae8c636b3d1c0054f4dc89b203a972f33fd63`: observed gpt-6.1-sol, max, read-only. All four statements ACCEPT/ACCEPT-WITH-FIXES, 0FATAL/0MAJOR/2MINOR.
- [Claude](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-LSplus-chain-claude-v1.prompt.note.md) `50452b786e18599c4f7b89b283f637e524c45cb069b1471cf6bd71be147b7bf9`: observed claude-opus-5-5, max, no tools. All four statements ACCEPT/ACCEPT-WITH-FIXES, 0FATAL/0MAJOR/16MINOR; two of the MINORs are optional.
- The parent read the erratum's C0–C16 dispositions. The repairs supply exact no-wrap defects, explicit core minimality and greedy hypotheses, signed-representative sums, the governing Addendum 1 chain, the CF(b)/R4 long-zero-sum translations, direct sharpness and the BASE1/LS exclusions. No theorem is strengthened.

## Import closure and calibration

- **Accepted delta inputs** ([verdict](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-STAB-delta-parent-verdict-v1.md)): CT, CTgen, LS+2 and BASE1+. **Prerequisites:** CF through E1, CF(b) through R4, SLZ3 used only to cut a shortest long zero-sum T to length 3kappa+2, and the external index-one theorem at n=p as pinned. The external proof was not replayed.
- [Olson priority note v3](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-priority-parent-note-v3.md) `9ae460f244dabda925112c589a7ba4081051058c710c2866c793e4a98a645502` calibrates this as a modest, sharp partial band. It is not a matched SOTA improvement and not a major result. The classical tools named there may make parts routine; a search miss is not novelty.
