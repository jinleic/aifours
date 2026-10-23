# README addendum v3: priority status and current candidate

The host-clock freeze record is in `evidence/proof-v3.sha256`. Earlier README files stay frozen.

## 1. Priority: a prior unpublished claim exists

The parent's post-candidate priority record is S/math-1-sun-coset5-post-candidate-priority-v1.md (1d7043ae…7b84). It found that Z.-W. Sun himself reports an **unpublished** confirmation of k = 5 for general groups:

- **MathOverflow Q316709 (2018-12-02):** "In 2010, Zhu Gong (another student of Nanjing University whose bachelor thesis was supervised by me) confirmed the conjecture for k=5 (again with G a general group). Since 2010, there is no further progress on the conjecture."
- **Slides Cover-Z+G.pdf (2024), slide 38:** "In 2009, Z. Gong confirmed the conjecture in the case k = 5."

No public text of that work was located. Neither the Core(5) reduction nor the double-coset mechanism was found in public sources.

**Consequences.**
- The k = 5 case is **not** an open target that this lane solved.
- The correct description of this lane's result, if it is verified, is: *a public written proof of a case for which a prior unpublished claim exists*.
- This lane never claims "first" or "novel".
- The frozen contract's stop rule ("stop on a prior claim of k=5 for groups") applies to any claim that an open target was solved. Correctness verification continues at the parent's instruction.

## 2. The lane's own post-candidate refresh

The lane ran `code/priority_search_v2.py` (156c6210…9c74c), producing `evidence/priority-search-v2/summary.json` (363b8252…055d). It covered arXiv (10 queries), OpenAlex (works citing Menon, M-S, Zhu and Sun 2006, plus 3 searches), DataCite (3 queries) and Crossref (2 queries). None of these returned a public k = 5 group proof.

Three 2026 records were checked at abstract level:

| record | assessment |
|---|---|
| arXiv 2609.09052, "On the complement of a union of cosets" | concerns coset covers and complements; not Sun's conjecture |
| arXiv 2603.26043 | concerns disjoint covering systems of the integers |
| arXiv 2609.00032, "EULER" | a multi-agent discovery system evaluated on 120 conjectures; the abstract names no k = 5 group result; its full text was not checked |

The lane's search missed the MathOverflow and slides statements that the parent found. A search miss is not evidence of novelty.

## 3. Current candidate

`proof-v3.md` supersedes proof-v1 and proof-v2, which stay frozen. It contains the fixes from the Claude review (F-1 to F-10) and the Codex engine-audit wording; see its fix map. `rules-v1-erratum-v2.md` adds errata E5–E8.

**Status:** candidate, computer-assisted, not Lean-checked. The gate is not claimed. The parent's independent replay of the 21,150 certificates is pending.
