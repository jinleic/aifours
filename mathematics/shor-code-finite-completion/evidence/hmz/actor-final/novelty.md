# Source and novelty audit

Date: 2026-10-14 PT. This is a bounded audit, not a certification that every
publication or unpublished manuscript has been located. No novelty is
claimed for the partial deductions in `proof.md`.

## Primary texts actually read

1. The original *10000个科学难题·数学卷*, printed pages 64–65 / PDF pages
   80–81. Both pages were visually inspected. Local text and page renderings
   are retained in `sources/`. They confirm the exact code, factor-completeness
   definition, and distinction between Questions 1 and 2.
2. Restivo, Salemi, Sportelli, [Completing codes (1989)](https://www.numdam.org/item/ITA_1989__23_2_135_0.pdf),
   especially printed pages 144–147. The cyclic embedding theorem is a
   necessary condition for completion. Conjecture 2 excludes embeddings of
   $(\{0,p,k\},\{0,1\})$ for prime $p\nmid k$. On pages 146–147 the authors
   observe that Shor's pair contains $(\{0,3,8\},\{0,1\})$ and on that
   conjectural basis conjecture no finite completion for Shor's code.
   The page-144 formula, missing from the text extraction, was checked in
   the retained rendering `sources/rss-1989-page144.png`.
3. Cordero, [A Note with Computer Exploration on the Triangle Conjecture (2019)](https://www.normalesup.org/~cordero/Publications/A_Note_with_Computer_Exploration_on_the_Triangle_Conjecture.pdf),
   Introduction and Sections 2–3. The source explicitly leaves the exact
   Shor code unresolved. Its Section 2.2 table already gives
   $n=330k,\ k\geq4$. Its page 8 was also rendered and inspected, including
   the incorrect displayed arithmetic in the `3R` example.
4. De Felice, [Finite maximal codes and factorizations of cyclic groups, arXiv:2202.09675](https://arxiv.org/html/2202.09675),
   Selected passages from Sections 2.3, 3–4, 7.3 and the Appendix. Corollary 7.1 imposes the
   order hypothesis $\Omega(n)\leq2$. The Appendix's triangle results retain
   hypotheses on the induced factorization system. None is an all-order
   proof for the present code.
5. Cordero, [Factorizations of Cyclic Groups and Bayonet Codes, arXiv:2301.13566](https://arxiv.org/html/2301.13566),
   Definitions 1.2, 2.3 and 3.1; Propositions 1.3, 2.4 and 3.3;
   Theorems 1.4 and 7.2; and the special-order conclusions. This is the
   published framework used for the partial deduction in `proof.md` Section 3.
   The author's [publication list](https://www.normalesup.org/~cordero/)
   identifies the journal publication as 2023. The downloaded arXiv PDF's
   manuscript date is November 20, 2022; that difference is not evidence of a
   later all-order solution.
6. Cordero's [2019 poster/slides](https://www.normalesup.org/~cordero/Presentations/2019/GdR_IM.pdf).
   The same Shor code and boundary-factorization question appear there.
7. Szabó, [Completing codes and the Rédei property of groups (2006)](https://doi.org/10.1016/j.tcs.2006.02.002),
   TCS 359, 449–454. Theorem 7 is an earlier primary publication of the
   condition indexed as the 2009 book's Theorem 10.5. The parsed primary
   PDF, including its proof, was read. Verbatim parsed hypothesis and
   conclusion fragments, plus an explicitly labelled mathematical
   paraphrase, are retained in
   `sources/szabo-2006-theorem7-excerpt.txt`, with URL, retrieval time and
   page number. The chronology and scope are in
   `sources/rss-later-work.txt`.
8. Sands, [A question concerning the factorization of cyclic groups (2007)](https://doi.org/10.1142/S0218196707004293),
   IJAC 17(8), 1573–1575. The publisher-provided first-page preview reports
   a refutation of the RSS factorization conjecture. The construction on
   pages 1574–1575 was not retrieved. Thus the general RSS heuristic is gone,
   but no conclusion about which specific $(p,k)$ are realized is claimed.
   In particular, this preview is not a construction for Shor's full pair.

The five downloaded PDFs have URLs and SHA-256 digests in
`sources/manifest.json`; extracted text is retained alongside them. There
was no local corpus search for another reproduction of the known bound.

## Apparent stronger or full results: how they were treated

The author-uploaded [Zhang–Shum draft dated September 8, 2008](https://www.researchgate.net/profile/Kar-Shum/publication/360931527_Finitely_Completable_Codes_and_Triangle_Conjecture/links/6293747cc660ab61f84fbcf0/Finitely-Completable-Codes-and-Triangle-Conjecture.pdf)
claims full noncompletion. PDF text on pages 4 and 11–13 was inspected.
Direct download was denied and the screenshot did not yield a locally
inspectable image. It is not represented as a visually audited local PDF.
Focused parsed mathematical excerpts and scope fragments are now retained in
`sources/zhang-shum-2008-excerpt.txt`, with URL, retrieval time and page
labels. Section 6 checks the hypotheses, including the infinite derived
$Y$, against that retained source and refutes its tail-polynomial step.
The draft is not an established full answer; its ResearchGate metadata
does not establish journal provenance.

The actual [2017 Zhang–Shum journal article](https://doi.org/10.1016/j.disc.2016.10.008)
has a different title, *Finite maximal codes and triangle conjecture*,
and pages 541–549. De Felice's Appendix states its triangle conclusion
with a Krasner-factorization condition. It cannot be upgraded to the 2008
draft's unrestricted claim.

Search-indexed book text points to Szabó–Sands, *Factoring Groups into
Subsets* (2009), Theorem 10.5, printed page 212. The indexed statement gives
the necessary condition that $330p_1p_2p_3$ divides $n$, for three distinct
primes, and hence $n\geq9900$. As a divisibility condition this is
**incomparable** with $1320\mid n$: the numerical values 9900 and 1320
witness the two failures of implication. Its lower bound of 9900 is stronger
than the lower bound of 1320. The complete primary book pages
and proof were not retrieved: the accessible [indexed copy](https://www.scribd.com/document/417239748/Sandor-Szabo-Arthur-D-Sands-Factoring-Groups-Into-Subsets-CRC-Press-2009)
returned a reader shell when downloaded. This is retained as an **unaudited
book lead**. The earlier primary article listed as item 7 independently
establishes the stated necessary condition and the published $n\geq9900$
bound.

As corrected in `proof.md` Section 3, combining that theorem with
$8\mid n$ gives $n\geq19800$: the minimum of
$\operatorname{lcm}(8,330p_1p_2p_3)$ occurs at the distinct primes
$\{2,3,5\}$. This is a **partial corollary whose novelty is unaudited**.
The full Szabó–Sands (2009) Section 10 pages and Cordero's thesis were not
read. It does not decide Question 1. This review correction involved no
further divisor, lower-bound or finite-order search.

The chronology matters: Szabó (2006), page 450, restates RSS Conjecture 2 as
its Conjecture 1; Sands (2007) then reports counterexamples. Cordero (2019),
Section 2, still explicitly leaves the embedding of Shor's full pair
unsettled. The 2023 results have the special-order and cbc scope already
described. No published proof or construction deciding that full pair was
validated in this audit. This is a statement about the sources checked,
not an inference of current open status from a search miss.

A recent author-uploaded [A Weak Structural Form of Commutative Equivalence in Finite Codes](https://www.researchgate.net/publication/403308673_A_Weak_Structural_Form_of_Commutative_Equivalence_in_Finite_Codes)
was also checked for scope. Its Theorem 1.9 preserves a weighted occurrence
quantity in another prefix code; it does not assert containment of $C$ in
a finite complete code or nonexistence of such a code. Its proof was not
adopted for any deduction here.

## What can and cannot be claimed

- Recovering $n\geq1320$ is reproduction of the supplied 2019 table.
- The scout's $660\mid n$ follows from a standard published multiplier
  method. Its correctness does not establish novelty.
- The derived $1320\mid n$, the infinite survival argument for unit
  multipliers, and the explicit audit counterexample are arguments documented
  in this attempt. No claim that they were absent from earlier literature is
  justified by the searches performed.
- No published full answer was validated, and no new full answer was proved.
  A search miss is not evidence of novelty or a proof that the problem remains
  open as of the current date.

The exact remaining all-order gap is stated in `proof.md` Section 7.
