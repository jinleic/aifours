## Summary

**Qu’s arXiv:2610.26122v1 is not a resolution of Olson’s original ordered conjecture.** Its Gao constant explicitly permits rearrangement. The nilpotent-group theorem of Han and the recent Heisenberg-group theorem of Qu–Wang use the same rearrangeable convention.

I located **genuine ordered-subsequence results for finite \(p\)-groups**, particularly Dimitrov’s ordered-Davenport/Loewy-length bound and subsequent class-two results. However, their stated conclusions concern **a nonempty subsequence of unspecified length**, not literally the requested \(|G|\)-term subsequence. These are the most important unresolved **prior-art implications**, and prevent a novelty clearance for the \(p\)-group/class-two restrictions.

**No directly stated resolution of the exact nonabelian target was established by this screen—for all nilpotent groups, all \(p\)-groups, all class-two \(p\)-groups, or all finite groups. This is not evidence that those restrictions remain open.** No proof or result is accepted by Main through this report.

## 1. Exact target: primary statements

For \(n=|G|\), the target is
\[
\forall(a_1,\ldots,a_{2n-1})\in G^{2n-1},\quad
\exists\,1\le i_1<\cdots<i_n\le2n-1:
a_{i_1}\cdots a_{i_n}=1.
\]
The selected terms retain their original relative order; they need not be consecutive.

| Source, author, date | Definition and scope actually found | Proof access |
|---|---|---|
| **[Olson’s Conjecture](https://www.sfu.ca/~mohar/Problems/P0604_OlsonConjecture.html)** — Bojan Mohar; page revised **5 August 2006** | Exactly the target. Verbatim: “there exist indices \(0<i_1<i_2<\ldots<i_n<2n\) such that the product \(a_{i_1}a_{i_2}\ldots a_{i_n}=1\).” The page distinguishes the abelian theorem from Olson’s weaker nonabelian theorem “where reordering is permitted.” | Entire short problem statement opened. It contains **no proof of the conjecture**. |
| **[Olson’s Conjecture](https://www.openproblemgarden.org/op/olsons_conjecture)** — Matt DeVos posting, attributed to John E. Olson; **10 March 2007** | Defines \(z(G)\) using a subsequence of length \(|G|\) with product one **“in the given order”**, and states the conjecture as \(z(G)\le2|G|-1\). This is an historical open statement, not a current-status certificate. | Entire page opened; no general proof. |
| **[Subsequence Sums II: length \(=|G|\)](https://www.sfu.ca/~mdevos/notes/comb_numb/notes4.pdf)** — Matt DeVos, **undated lecture notes** | Conjecture 5.8, PDF p. 4, again requires “an \(n\) element subsequence … equal to one in the given order.” Its \(D^{\mathrm{ord}}\) notation earlier means **order-length** in the abelian setting, not the ordered Davenport constant discussed below. | Relevant text opened, including the conjecture and surrounding distinction. No nonabelian conjecture proof. |
| **[On a combinatorial problem of Erdös, Ginzburg, and Ziv](https://doi.org/10.1016/0022-314X(76)90021-4)** — John E. Olson; *J. Number Theory* **8**, 52–57, **February 1976** | Title/author/date/DOI confirmed through publisher-deposited metadata. Mohar and the opened contemporary papers identify its \(2|G|-1\) result as **rearrangeable**. | **Original theorem and proof not read.** Both publisher article routes returned HTTP 403. The attribution above is not presented as a direct reading of Olson’s original text. |

## 2. Relevant solutions and near-matches

Here \(D_o(G)\) denotes the ordered Davenport constant: every sufficiently long word has **some nonempty** identity subsequence with increasing indices. In contrast, \(E(G)\) below forces **exactly \(|G|\) selected terms**, but allows their rearrangement.

| Primary source and available version | Exact convention and relevant scope | Match to target / proof opened? |
|---|---|---|
| **[The Erdős–Ginzburg–Ziv theorem for finite nilpotent groups](https://link.springer.com/article/10.1007/s00013-015-0739-4)** — **Dongchun Han**; online **13 March 2015**, *Archiv der Mathematik* **104**, 325–332, April issue | Abstract explicitly says a subsequence of length \(|G|\) with product one **“(in some order)”**. For every finite **noncyclic nilpotent** \(G\), with \(p\) the least prime divisor of \(|G|\), it states \(E(G)\le |G|+|G|/p+p-2\). | **Not an ordered match.** Publisher abstract opened; full article is subscription content, so **full proof not read**. |
| **[On the Strong Davenport Constant of Nonabelian Finite \(p\)-Groups](https://www.math.bas.bg/infres/MathBalk/MB-18/MB-18-129-140.pdf)** — **Vesselin Dimitrov**; *Mathematica Balkanica* **18** (2004), 129–140 | Original title and pagination confirmed in the [journal’s own contents](https://www.math.bas.bg/infres/MathBalk/index-mb-18.htm). The following two first-party research papers explicitly attribute \(D_o(G)\le L(G)\), for **every finite \(p\)-group**, to this paper. \(L(G)\) is the Loewy length of \(\mathbb F_p[G]\). | **Important ordered prior art, but unspecified subsequence length.** Original PDF fetched; all 12 pages failed text extraction. **Original theorem/proof unread; attribution checked through the later papers, not merely search snippets.** |
| **[An algebraic approach towards a conjecture on the Davenport constant](https://arxiv.org/html/2407.01148v2)** — **Naveen K. Godara, Renu Joshi, Eshita Mazumdar**; v1 **1 July 2024**, current v2 **23 November 2025** | Definition explicitly uses \(i_1<\cdots<i_m\), but **\(m\) is not prescribed**. Theorem 1.3 restates Dimitrov’s bound for **all finite \(p\)-groups**. Theorem 1.5 gives exact ordered constants for specified nonabelian families. For example, its class-two family \(G_1(\alpha,\beta,1)\), with \([a,b]=c\), central \(c\), orders \(p^\alpha,p^\beta,p\), and \(\alpha\ge\beta\ge1\), has \(D_o=p^\alpha+p^\beta+2p-3\), for odd \(p\). | **Ordered but not a literal fixed-\(|G|\) theorem.** Definitions, theorem statements, family presentations, and preliminary material opened. **Full main proofs not read.** |
| **[Combinatorial invariants for certain classes of non-abelian groups](https://arxiv.org/html/2408.13558v2)** — **Godara, Joshi, Mazumdar**; v1 **24 August 2024**, current v2 **2 January 2026** | Explicitly separates ordered words in the **free nonabelian monoid** from rearrangeable sequences in the **free abelian monoid**. Lemma 2.2 states \(D_o(G)\le L(G)\) for every finite \(p\)-group; introduction states \(L(G)\le|G|\). Theorem 1.5 proves \(D_o=L\) for its specified class-two \(2\)-group families \(G_1\) with \(\gamma=1\), \(G_2\), \(G_3\) with \(\sigma=1\), and \(G_4\) with \(\gamma\in\{1,2\}\)—**not all class-two \(2\)-groups**. Its Gao results separately retain rearrangement. | **Genuine ordered prior art, different length quantifier.** Definitions, statements, and some preliminary propositions opened; **full main proofs not read**. |
| **[The Gao–Zhuang conjecture for the Heisenberg group over \(\mathbb F_p\)](https://arxiv.org/html/2608.23319v2)** — **Yongke Qu, Guoqing Wang**; v1 **24 August 2026**, current v2 **6 September 2026** | “Product-one” means terms **“can be ordered so that their product is the identity.”** Theorem 1.1 states \(E(\operatorname{UT}_3(\mathbb F_p))=p^3+3p-3\) for every odd prime \(p\). The paper also states Gao–Zhuang equality for every group of order \(p^3\). | **Rearrangeable class-two result, not the ordered target.** Current §§1–2 opened, including the permutation-based product-set definition; **full proof not read**. |
| **[The Erdős–Ginzburg–Ziv theorem constant of finite groups](https://arxiv.org/html/2603.21052v1)** — **Yang Zhao, Guoqing Wang**; **22 March 2026**, v1, only version listed | Abstract explicitly permits products **“in some order.”** Theorem 1.2 gives \(E(G)\le3|G|/2\) for noncyclic \(G\) with \(4\nmid|G|\), with equality iff \(G\) has a cyclic subgroup of index two. | **Not ordered.** Definitions/main statement opened; **full proof not read**. |
| **[The Erdős–Ginzburg–Ziv theorem for finite groups](https://arxiv.org/html/2610.26122v1)** — **Yongke Qu**; **19 October 2026**, v1, only version listed | A sequence is a **finite multiset**. Section 2 defines \(\pi(S)\) using **all permutations**. Theorem 1.4 states \(E(G)\le |G|+|G|/p-1\) when no cyclic subgroup has index \(p\). Corollary 1.5 states \(E(G)\le |G|+|G|/p+p-2\) for every noncyclic finite \(G\), with the stated cyclic-index equality characterization. | **General rearrangeable theorem claim—not a general ordered resolution.** §§1–2 and final §16 opened; full-text terminology searched. **Complete proof/dependency chain not read or assessed.** |

### What Qu says about “ordered”

Qu does use expressions such as **“ordered product”** in intermediate lemmas. That does **not** change its invariant: \(\pi(S)\) ranges over permutations, and intermediate constructions choose and concatenate orderings. I found **no explicit theorem preserving the original order of an arbitrary input word**, nor a stated resolution of Mohar’s ordered conjecture. Thus the finding is stronger than a title/snippet mismatch, but narrower than a correctness review of Qu’s paper.

## 3. Additional false positives and corpus screen

- **Benjamin Girard and Sofia Zotova, [The Erdős–Ginzburg–Ziv constant of rank-two-like \(p\)-groups](https://arxiv.org/html/2510.23543v1), 27 October 2025, v1:** the introduction restricts to **finite abelian groups** and defines its principal constant using subsequences of length **\(\exp(G)\)**, not \(|G|\). It is not a nonabelian ordered solution. Definitions/introduction opened; full proof not read.

- **Vesselin Dimitrov, [Zero-sum problems in finite groups](https://web.mit.edu/rsi/www/pdfs/papers/2003/2003-vessel.pdf):** the document itself displays **31 July 2007**, notwithstanding its `2003` URL. It states a soluble-group result involving \(G\oplus C_{|G|}\), but defines sequences through a **free abelian semigroup**. It cannot be counted as an ordered solution from that statement. Relevant definitions, statement, and soluble-group argument opened; complete manuscript not read.

- **OpenAI’s public `openai/math` inventory:** inspected [CONTENTS.md at commit `42907c9e999cc00d6abe7a50bfc1023250edd1b9`](https://github.com/openai/math/blob/42907c9e999cc00d6abe7a50bfc1023250edd1b9/CONTENTS.md) and the corresponding [overview](https://github.com/openai/math/blob/42907c9e999cc00d6abe7a50bfc1023250edd1b9/overview.pdf). The inventory declares **721 manuscripts / 373 families**; its latest recorded contents change is **26 October 2026**. Searches for Olson, Davenport, Ginzburg, Gao, product-one, identity-subsequence, and broader related wording located **no matching family/title/abstract**. This is an **inventory-level negative finding**, not a full-corpus proof search or evidence of openness. No manuscript proof or Lean artifact was opened or executed.

## 4. Ranked unresolved comparisons

Ranked by immediate importance to avoiding a false priority claim:

1. **All finite \(p\)-groups, hence class-two \(p\)-groups:** Dimitrov’s genuinely ordered \(D_o\le L\) theorem is the principal prior-art boundary. The exact-length implication requires a separate comparison, including cyclic length-tagging/direct-product behavior. **This screen does not certify that implication or novelty.** An absence of the phrase “Olson’s conjecture” is particularly uninformative here.

2. **All finite nilpotent groups, including mixed-prime order:** Han’s theorem is explicitly rearrangeable. No directly stated original-order \(2|G|-1\) theorem was located. Neither Han nor the \(p\)-group ordered-Davenport statements alone were certified here as settling this precise scope.

3. **All finite groups:** Mohar/DeVos give the exact historical target; Qu gives a general theorem for a different invariant. **No exact current resolution was established in the checked primary sources.** The current open/closed status therefore remains **uncertified**, not “proved open.”

Only public literature and public source metadata were used for these findings. No owner proofs, protected evidence, code execution, tests, builds, or formatters were accessed or run.
