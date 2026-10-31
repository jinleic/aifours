# Source-bound original definitions — info-2

Literal canonical-dossier problem statement, /Users/jinleic/repos/aifours/information-science/robust-spr-interval-synthesis/README.md SHA256 b9afd01e3f30274c95fa8a0a7369cc2348ab20ec60c9cdc344224f633d0f28fc, LF1-27 (prefix = source line number):

1| # Robust SPR synthesis for interval polynomial families of degree > 4
2| 
3| 区间系统的鲁棒严格正实综合 — 郁文生 (Yu Wensheng), 王龙 (Wang Long).
4| 《10000个科学难题·信息科学卷》, Science Press 2011, book pp. 680–682 (PDF pp. 701–703);
5| page images in [`sources/book/`](sources/book/). Dates are Pacific time; work done 2026-10-14.
6| 
7| ## 1. Problem as posed (book p. 682)
8| 
9| Let P^n be the real polynomials of order n and H^n ⊂ P^n the Hurwitz ones. For b ∈ P^n and
10| a ∈ H^n, b/a is strictly positive real (SPR) iff Re[b(jω)/a(jω)] > 0 for all real ω
11| (Definition 1). A polynomial set F is robustly stable iff every member is Hurwitz (Definition 2).
12| 
13| **Question.** For a robustly stable interval polynomial family of order n > 4, does there always
14| exist one fixed polynomial b(s) such that b(s)/a(s) is SPR for every a(s) in the family? Equivalently:
15| is robust stability of an order-n (n > 4) interval family necessary and sufficient for robust SPR
16| synthesizability? The authors conjecture yes (no counterexample in their numerical examples).
17| Necessity is immediate; the open part is sufficiency.
18| 
19| **Formalization used here.** Following the authors' own papers (Wang & Yu, ACC 2001,
20| arXiv:math/0202242: K = {s^n + Σ a_i s^{n−i}, a_i ∈ [a_i^−, a_i^+]}) and the 2026 announcements for
21| n = 5, 6, an interval family is a **monic** box of closed coefficient intervals (degenerate
22| intervals allowed); the numerator has **exact degree n** (b ∈ P^n); SPR means **strict** positivity
23| of Re(b/a) at **every real ω** for **every** member. The book text itself does not say "monic";
24| boxes with an uncertain leading coefficient are treated as a separately labelled variant
25| (Prop. E in [`work/theory.md`](work/theory.md), outcome O6).
26| 
27| **Fully solved means:** for every n ≥ 5, either a proof that every robustly Hurwitz monic box of

Slot specialization (registered in the closed round and supplied in your envelope): n=7, actual monic closed coefficient box, every member strictly Hurwitz, one common real numerator of EXACT degree seven, strict Re(b(jw)/a(jw))>0 at EVERY finite real w including zero, for EVERY member; or one genuine robustly Hurwitz monic septic box with no such numerator.

## Provenance and limits

The quoted lines are the 2026-10-14 canonical dossier transcription of book pp.680–682 (page images exist but were NOT re-read by Main). Main's scout recorded that an earlier scouting display of lines 1–103 incidentally showed attack-log content; NONE of that is supplied here. This packet certifies no book-image equivalence, theorem, or current openness.
