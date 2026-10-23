<!-- Parent transcription 2026-10-17T22:42:09-07:00 of the read-only scout OlsonParPriority's final report (agent://OlsonParPriority; transcript history://OlsonParPriority), verbatim below. The scout wrote no files and had no host clock; its time base is the server stamps it quotes. -->

NONE-FOUND-IN-SCOPE

I found no earlier source that proves MIX_low(p) or PAR(p), and none that proves the full ordered Olson statement for dihedral groups of order 2p with p an odd prime, or for any class that contains them. The screen was limited, so this does not show novelty. I did not check correctness. There is no host clock in this scout, so the times below are server timestamps; the parent should timestamp this report. The candidate file `c2/proof-R4-closure.md` was frozen at 2026-10-18T00:53:26Z (c2 README progress log).

## 1. Which sources could cover the theorems

| Source | Keeps the original order? | Groups covered | What it proves | Covers MIX_low(p)? | Implies PAR(p)? |
|---|---|---|---|---|---|
| Erdős–Ginzburg–Ziv 1961 | Order does not matter in abelian groups | Abelian only | 2n−1 terms give n with sum 0 | No | No |
| Olson 1976 (zbMATH review only) | No ("n distinct indices") | All finite groups | Some n of the 2n−1 terms have product 1 after reordering | No | No |
| Yuster–Peterson 1984 (CJM) | No: the order is chosen, not given | Solvable groups | Unordered constant E(G) ≤ 2\|G\|−2, as Zhao–Wang report it | No | No |
| Sury 1999 (PAMS) | No ("in some order") | Solvable groups | Unordered Olson for solvable groups | No | No |
| Dimitrov 2004, Theorem 2 | **Yes** | Finite p-groups only | Ordered Olson, with a stronger threshold for non-cyclic p-groups | No (2p is not a prime power) | No |
| Zhuang–Gao 2005; Bass 2007; Gao–Lu 2008; Oh–Zhong 2020 | No | Dihedral and related groups | Unordered E(D₂ₙ) = 3n; Oh–Zhong's inverse theorem is at length 3n−1 | No | No |
| Agarwal–Lou 2016 (student talk abstract, Python experiments) | Yes | D₂ₙ | Lower bound only: 4n−1 for odd n | No | No |
| Godara–Joshi–Mazumdar, arXiv 2407.01148 (v1 2024-07-01, v2 2025-11-23) | Yes: their E(G) is exactly z(G) | All finite groups, but only as a conjecture | Conjecture 5.1: E(G) = D(G) + \|G\| − 1. No theorem about dihedral groups | No; the conjecture is false for odd dihedral groups (§4) | No |
| Godara–Joshi–Mazumdar, JNT 283 (2026), arXiv 2408.13558 | Ordered Davenport constant D_o, for subsequences of any length; their Gao constant is unordered | Even-order groups, 2-groups | Davenport-type constants | No | No |
| Zhao–Wang 2603.21052; Qu–Wang–Li 2608.15568 | No | Non-abelian groups | Unordered E(G) and s(G) | No | No |
| Frick et al., Forum Math. Sigma 2025 | No | All finite groups | Topological proof of unordered Olson | No | No |
| Hamidoune–Quiroz 2005 | No: indices distinct, not increasing | All finite groups | Weighted products | No | No |
| Open Problem Garden 2007, Mohar 2006, CanaDAM 2015 | Statement only | All finite groups | Listed as open | — | — |

None of these sources has an ordered result at length 2|G|−2. None has structure built from runs of letters, and none has conditions like B < κ ≤ k−1 or the inheritance conditions. The unordered dihedral inverse theorem (Oh–Zhong) is about length 3p−1. Every word of length 4p−2 already has an unordered solution, so it cannot imply anything about MIX_low or PAR.

## 2. Citations with exact scope

- **Open Problem Garden**, M. DeVos, posted 2007-03-10, https://openproblemgarden.org/op/olsons_conjecture. Re-read; it has no comments. "Apart from Olson's result, there appears to be very little known about this problem." The only bound given is z(G) ≤ |G|(|G|−1)+1.
- **Mohar's problem page**, revised 2006-08-05, https://www.sfu.ca/~mohar/Problems/P0604_OlsonConjecture.html. Unchanged: "for nonabelian groups, Olson proved a weaker version where reordering is permitted, but little else is known."
- **CanaDAM 2015 open problem by K. Halasz**, https://canadam.org/archives/2015f/program/abs/op/. "Save some special cases, this problem remains open."
- **Dimitrov**, Math. Balkanica 18 (2004) 129–140 (Zbl 1079.20037; local OCR `sources/dimitrov-ocr/page-03.txt:17-20`). "He further conjectured that the chosen elements can strictly follow any initial arrangement, but this is not known even for soluble groups. In this paper, we prove Olson's conjecture in the case of all finite p-groups."
- **Sury**, PAMS 127 (1999) 951–953, author copy https://www.isibang.ac.in/~sury/cwprocams.pdf. This had not been screened before. Its abstract says it will "solve a conjecture of J. E. Olson", which could be misread as the ordered problem. The question it actually answers is unordered: "Given a sequence of 2n − 1 elements of a group G of order n, can one always choose exactly n of them, whose product (in some order) is the identity?" It then states "Corollary. Solvable groups are C-W groups." So it does not cover dihedral groups in the ordered sense.
- **Yuster–Peterson**, CJM 36 (1984), https://doi.org/10.4153/CJM-1984-032-x. The Crossref abstract says: "The 'sets' in this paper are actually multi-sets" and "the result of that r-sum is the product of its elements in the designated order." The order is chosen, so this is the unordered problem.
- **Olson 1976**, zbMATH review Zbl 0333.05009: "there are n distinct indices i₁,…,iₙ such that g_{i₁}+…+g_{iₙ}=0". This is unordered.
- **Agarwal–Lou**, IMSA, talk 2016-04-28, page posted 2016-05-12. "for odd n ≥ 3, the lower bound on the length of a sequence made from elements in the dihedral group of order 2n that contains a zero – sum sequence is 4n -1." This is a lower bound from experiments only.
- **Godara–Joshi–Mazumdar, arXiv 2407.01148**. DataCite gives v1 submitted 2024-07-01T10:16:21Z and v2 2025-11-23T07:05:20Z. Section 5 of both versions defines E(G) with "|G| indices 1≤i₁<⋯<i_{|G|}≤k … ∏x_{i_σ(j)}=1 holds for σ=id". It then states "Conjecture 5.1. For any finite group G, E(G)=D(G)+|G|−1." No journal version located.
- **Godara–Joshi–Mazumdar, arXiv 2408.13558v2 / JNT 2026**, introduction: "In 1977, Olson and White proved that D_o(G) ≤ ⌈(|G|+1)/2⌉" for every finite non-cyclic group G.
- **Qu–Wang–Li, arXiv 2608.15568** (2026-08-16). The earlier screen had not checked its ordering convention. It is unordered: a product-one subsequence is one whose "terms can be ordered so that their product is the identity". Its π(S) ranges over permutations τ.
- **Oh–Zhong**, arXiv 1904.13171v2 / Israel J. Math. 2020. Uses "finite unordered sequence" throughout. Theorem A: E(D₂ₙ) = 3n.
- **Hamidoune–Quiroz**, CPC 2005 (Zbl 1095.20013): "pairwise distinct elements i₁,…,i_k∈I such that ∏σ_j(v⁻¹x_{i_j})=1". The indices are distinct, not increasing.
- **Who cites Dimitrov and Olson (zbMATH).** Dimitrov 2004 is cited by 6 documents: Godara–Joshi–Mazumdar (JNT 2026), Gao–Li–Peng (2014), Alkan (2008), Wang–Gao (2008), Gao–Lu (2008) and Gao–Geroldinger (2006). Olson 1976 is cited by 25. I scanned all titles and checked the likely ones; every one is unordered, abelian, a Davenport-type constant or a Ramsey problem.

## 3. Strongest counter-evidence and residual risk

- **Gao–Lu, JPAA 2008** cites Dimitrov's ordered p-group result, according to its Crossref reference list. I could not read the full text (ScienceDirect returned 403), and the zbMATH review is one line. Its title and keywords point to the unordered E(D₂ₙ) problem. A remark about the ordered problem in its introduction cannot be excluded; I judge that unlikely, but it is an inference.
- **Yuster 1988** (Arch. Math.) is paywalled and I did not read it. Dimitrov wrote after it, in 2004, that the ordered version was "not known even for soluble groups".
- **The field is active, including AI-assisted work.** There is a public GitHub repo for this exact problem (Open Problem Garden #155): vibemathing/problem-um-opg-155-olson-s-conjecture-75c1c101, created 2026-09-06T21:00:26Z. It is a template only: its single attempt is marked "planned" and it has no pull requests. Godara–Joshi–Mazumdar's 2024–2025 conjecture also shows specialists are thinking about the ordered constant. No result had appeared as of the newest DataCite record I saw, created 2026-10-18T01:32:28Z.

## 4. What remains open

**In the literature, as far as I located:**
- Ordered Olson is open for every finite group that is neither abelian nor a p-group, including D₂ₚ.
- For D₂ₚ the only known bounds are z(D₂ₚ) ≥ 4p−1 (the Agarwal–Lou claim, also proved in the local Lean file `odd_dihedral_sharp_lower_bound`, receipt exit 0) and the trivial z ≤ n(n−1)+1.
- I located no inverse or structure theorem for ordered products at length 2|G|−2 in any non-abelian group.

**In the lane:**
- Theorems M and P are written proofs only and have not been reviewed. Lemmas ZP and C and Lemma R4 are new and unreviewed. Lemma M0 has not been reviewed independently.
- RUNS(p) and INV*(p) are still open, so ordered Olson for D₂ₚ is not proved.

**Scope detail for the wording of PAR(p).** In `proof-INV-reduction.md:14-16`, "inherited" is defined by five conditions, (E), (P), (V), (Pairs) and (D0). It is not defined as "obtained by deleting one letter". The wording should state those conditions.

**Side finding, independent of MIX_low.** Conjecture 5.1 of arXiv 2407.01148 is false for every odd dihedral group D₂ₘ with m ≥ 3:
- The Olson–White bound gives D(D₂ₘ) ≤ m+1, so the conjecture predicts E(D₂ₘ) ≤ 3m.
- The word r^{2m−1}s^{2m−1} has length 4m−2 and no identity product of 2m letters in order, so E(D₂ₘ) ≥ 4m−1.
- The smallest case is S₃: the conjecture predicts at most 9, but the 10-letter word r⁵s⁵ has no such product.

This follows from sources already located (Olson–White 1977 as quoted, plus the Agarwal–Lou claim). I found no published note of the conflict.

## 5. Significance

- **MIX_low(p) and PAR(p) are mainly technical components of an unfinished proof.** They change no published bound on z(D₂ₚ), so the matched delta on that scale is zero. What they add is a structural statement about possible extremal words of length 4p−2 in one rigid family, and no published result of that kind exists to compare against. Rating: modest extension. They are not a contract gate: they settle neither the book problem nor any published question.
- **A full proof of ordered Olson for D₂ₚ would be potentially substantive specialist work.** It would give z(D₂ₚ) = 4p−1 = 2|G|−1, so Olson's bound would be sharp for an infinite family of groups that are neither abelian nor p-groups. That needs RUNS(p) and INV*(p) and is not established. A "major" rating is not established.

**Recommended wording:** "If the pending review accepts it, Theorem M shows the following for every prime p ≥ 5. Take any word of length 4p−2 over D₂ₚ in the rigid run family: rotations are only r and r⁻¹, and k nonempty rotation runs alternate with k nonempty constant reflection runs, all of odd length. If k ≤ p, A ≥ B ≥ 1 and B < κ ≤ k−1, the word contains 2p letters, taken in increasing index order, whose product is the identity. Theorem P (PAR(p)) follows for words satisfying conditions (E), (P), (V), (Pairs) and (D0). These are partial inverse results for one specified family; they do not prove ordered Olson for D₂ₚ. No earlier equivalent was located in a bounded screen."

## 6. DataCite, Zenodo and recency checks (titles and abstracts only, not article full text)

**Topic queries:**
- "Olson's conjecture" returned one hit, in astrophysics.
- Erdős–Ginzburg–Ziv combined with ordered, order-preserving, "given order" or "increasing indices" returned only Oh–Zhong.
- All Erdős–Ginzburg–Ziv records, newest first: arXiv 2610.21577 (2026-10-16, abelian), 2610.19965 (2026-10-15, integer vectors), Yiming Liu on Zenodo (2026-10-09, AI-assisted, cyclic groups) and EDOU NZE (2026-08-27, abelian). None is relevant.
- Queries combining dihedral, non-abelian, product-one, "ordered zero-sum", "strong Davenport" and Davenport found nothing relevant. Hits included the unordered Heisenberg-group Davenport series (2607.14379, 2608.13747, 2609.19810) and the abelian sense of "strong Davenport".
- Records created since 2026-10-15: the only zero-sum item is Baillargeon's signed Davenport constant of C₅⊕C₁₅ (2026-10-17T19:24:54Z, abelian).

**Creator families** (through DataCite, because the Zenodo API returned 403). No item touches Olson, ordered EGZ or dihedral groups:

| Creator | Records seen / latest | Notes |
|---|---|---|
| Kirtchakov | 20; latest 2026-08-14T10:50:44Z | |
| Griffin Long | 2 (SW(25,16) etc.); 2026-10-15T20:42:34Z | |
| Reynout Vos | latest 2026-10-10T16:27:32Z | |
| Ruturaj Raval | latest 2026-09-11T17:33:06Z | |
| Alper Ferudun | latest 2026-10-18T01:25:46Z | |
| Gippini Requeijo | latest 2026-10-17T22:26:15Z | |
| Sadhu | — | No hit in the topic intersection query; full list not enumerated |
| EulerSolve publisher | latest 2026-10-17T16:01:32Z | Topic query: 8 unrelated hits |

**arXiv.** Several queries (Olson with ordered; Ginzburg with order in math.CO; "strong Davenport"; recent dihedral, product-one and Davenport papers) found nothing relevant. The latest published item seen was 2026-10-15T17:33:21Z; the feed's server time was 2026-10-18T01:58:04Z.

## 7. Access limits

- Full texts not read:
  - Gao–Lu 2008 and Caro's 1996 survey: not read (Gao–Lu page returned 403; Caro not fetched).
  - Olson 1976 body: only the zbMATH review read.
  - Yuster 1988: paywalled.
  - Yuster–Peterson 1984: abstract only.
  - Bass 2007: not re-read.
  - Grynkiewicz's book *Structural Additive Theory*: not consulted.
- Blocked or rate-limited: the AMS PAMS page (403, but the author copy was read), the Zenodo API (403), unsolvedmath.com (429), and one arXiv API call (429).
- Citation coverage:
  - The Semantic Scholar API could not be used through the tool, and Google Scholar was not used.
  - Dimitrov 2004 has no DOI and is not in OpenAlex or Crossref, so citations of it come from zbMATH only.
  - OpenAlex full-text search covers only part of the literature.
- arXiv submissions after about 2026-10-15 had not been announced yet.
- No CNKI search; Chinese-language coverage is a single web search.
- The agent-afk GitHub account was not checked, and no Kevin Halasz thesis was located.
