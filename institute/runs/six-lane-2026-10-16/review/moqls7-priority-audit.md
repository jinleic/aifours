# MOQLS(7), Ball–Simoens Problem 16 at n = 7: bounded priority audit

## Verdict

**NO-PRIOR-FOUND-IN-BOUNDED-SEARCH.** The read-only scout `MoqlsPriority` (report retained at `agent://MoqlsPriority`) found no accessible source deciding whether every set of four MOQLS(7) is classical, and no source that implies M(7) ≤ 3 or constructs a non-classical 4-MOQLS(7). This audit concerns priority only; the candidate's correctness is under separate review, and a search miss does not establish novelty.

## Latest open statement and implication

- Ball–Simoens, [arXiv:2607.12933v2](https://arxiv.org/abs/2607.12933v2) (27 Jul 2026, "Correction of Theorem 6"), p.7: "Problem 16. Is a set of n − 3 MOQLS(n), n ≠ 4, necessarily classical?" Table 2 gives M(7) as 2–4. v1 (14 Jul 2026) has the same Problem 16. Preprint only: no journal-ref, OpenAlex lists it as an unpublished preprint, and Simoens' publication page lists it under preprints.
- Known: their Theorem 5 at n = 7 gives M(7) ≤ 4; Huang–Li, [arXiv:2606.27758](https://arxiv.org/abs/2606.27758), Theorem 5.2, and Ball–Simoens Corollary 7 give M(7) ≥ 2.
- The candidate (every four MOQLS(7) classical) is exactly Problem 16 at n = 7 and would give **2 ≤ M(7) ≤ 3**. It would not determine M(7): no non-classical 3-MOQLS(7) is known (Han et al. [arXiv:2507.20154](https://arxiv.org/abs/2507.20154), Theorem 3.8, leaves orders 4–15 open; Huang–Li call MCPQLS(7) open).
- Problem 16 stays open for every n ≥ 8 (e.g. Table 2 gives M(8) as 2–5). n = 7 is the smallest open instance [INFERENCE: n = 5 settled by 2603.02334 Theorem 12, n = 6 vacuous by its Theorem 6, n = 4 excluded].
- Forward citations (Zhang–Cao [2608.29201](https://arxiv.org/abs/2608.29201), Lv–Zhang–Cao [2609.29070](https://arxiv.org/abs/2609.29070)) neither restate Problem 16 nor treat M(7).

## Notion scope

The result concerns product-ONB orthogonality (Ball–Simoens §2.3). It does not carry over to weak/left orthogonality (Musto, [arXiv:1605.08919](https://arxiv.org/abs/1605.08919)), entangled quantum orthogonal Latin squares / AME(4,n) states (Hontarenko–Życzkowski, [arXiv:2610.17170](https://arxiv.org/abs/2610.17170)), or counts of mutually unbiased bases.

## Imported theorems (accessibility)

- Hall, PAMS 4 (1953) 912–916, doi:10.1090/S0002-9939-1953-0058986-4, with a Correction, PAMS 5 (1954) 994–997, doi:10.1090/S0002-9939-1954-0065179-4: bodies inaccessible (HTTP 403). Accessible cross-check [INFERENCE]: Egan–Wanless count 120 reduced complete 6-MOLS(7), matching the Desarguesian count.
- Shrikhande, Sankhyā A 23 (1961) 115–116: inaccessible; verified only as quoted in Ball–Simoens Theorem 9. The n = 7 consequence used also follows from Egan–Wanless Table 5.
- Egan–Wanless, Math. Comp. 85 (2016) 799–824: Table 5 lists n = 7 rows only for k = 1, 2, 6, so no maximal 3-, 4- or 5-MOLS(7) exist.
- Lemma 10 originates in the PRL paper doi:10.1103/hxzf-nmpx, which has a publisher Correction (2026-08-28, unread). Ball–Simoens v2 re-proves the lemma (raw text lines 342–356), so the impact is likely nil [INFERENCE].

## Required claim wording

If correctness is accepted: "resolves the n = 7 instance of Problem 16; 2 ≤ M(7) ≤ 4 becomes 2 ≤ M(7) ≤ 3". Never "solves Problem 16", "determines M(7)" or "first". Recheck arXiv for a v3 before any release.

## Access holes

Semantic Scholar (tool rejected all URL forms), Google Scholar, ADS not checked; arXiv search covers titles/abstracts only; AMS, JSTOR/Sankhyā, Cambridge, scispace, phys.org blocked; the PRL body, Reutter–Vicary and Musto's thesis not read.

## Calibrated significance

[INFERENCE] If verified: a genuine but narrow, computer-assisted advance closing the smallest open instance of a problem posed three months earlier in an unrefereed preprint. It tightens one table entry; it neither determines M(7) nor says anything about n ≥ 8. No human peer review has taken place.
