# Sun(7) lane: priority and applicability note v2 (scout SunStructuralPriority2)

Recorded at 2026-10-19T04:51:33-0700. Supplements [note v1](sun7-priority-parent-note-v1.md); v1 is unchanged. Correctness is NOT re-assessed here; it rests on the parent verdicts.

**Outcome: no located published theorem implies or contradicts the accepted K6.3 closure, K7-U1 or Z23-P5; D23 is a row-pattern restriction only. Calibrated significance: modest extension, not major. A search miss is not novelty.**

## Source pins (read by the scout, bounded search)
- Menon, *Two Questions on G-harmonic Tuples*, [arXiv:2608.15873v1](https://arxiv.org/pdf/2608.15873v1): the only version (the v2 URL returns 404; the arXiv API and DataCite list v1 only). Its only tuple-family exclusion is X1, which needs two indices of the form 3·odd. K6.3 has one such index and K7 none, so X1 does not apply.
- Margolis–Schnabel, [arXiv:1803.03569v1](https://arxiv.org/pdf/1803.03569v1) (journal text paywalled): tuple results up to length 5; Prop 3.8 and Cor 3.9 exclude only patterns heavy in alpha=1 entries; Theorem B transfers only length ≤4 to Z.
- Zhu, [arXiv:0807.2207v1](https://arxiv.org/pdf/0807.2207v1): proves Sun(3) and Sun(4) for arbitrary groups and nothing for k≥5. This is the classical source of the Sun(4) instance used by the K62-E3 candidate.
- Sun's own status notes ([MathOverflow 316709](https://mathoverflow.net/questions/316709/a-challenging-problem-on-disjoint-cosets); [2024 slides](http://maths.nju.edu.cn/~zwsun/Cover-Z+G.pdf)): k=5 attributed to Gong's unpublished thesis; nothing for k≥6.

## Applicability and credit
- The FG granularity lemma and the 5/6 fibre bound are elementary extensions of Zhu (3.1), Margolis–Schnabel Lemmas 3.2/3.5/3.10 and Menon Prop 4.1. They are supporting tools, not a new method, and the report must cite these ancestors.
- Restated by the scout [INFERENCE]: the K6.3 closure says (3r_0, 6r_1, …, 6r_6) with pairwise coprime r_i and r_0 odd is not G-harmonic for any group; K7 is (6r_1, …, 6r_7).
- Dependence: the K6.3 closure inherits the internal computer-assisted Sun(6) and, through K63-U0's 1/4-weight step, Sun(5) (consistent with the [LFC/INV verdict](sun7-lfc-inv-parent-verdict-v1.md), which lists Sun(5) and Sun(6) as computer-assisted imports). Only Sun(5) has an external (unpublished) claim.

## Counterpoints recorded
Unpublished overlapping work on k=6,7 cannot be excluded; CNKI, MathSciNet, zbMATH and Google Scholar were not searched; anyone analysing a Sun(7) counterexample meets these index families; correctness rests on written proofs, CLI model reviews and parent re-derivation with no Lean or human review. Full Sun(7) remains OPEN.

Scout output: agent://SunStructuralPriority2 (39 findings, access holes listed there).
