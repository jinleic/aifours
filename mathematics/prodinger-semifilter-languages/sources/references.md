# Sources, baseline and novelty gate

Checked: 2026-10-14 PT. The mathematical proof and the publication-priority question are independent. Status: **NOVELTY-UNCLEAR**, not a claim of a newly solved open problem. No author contact, purchase, login or access-control bypass was performed.

## 1. Exact book source

Guo Yuqi and Wang Shoufeng, “A Model of Systematic Generalizations for an Important Kind of Congruences on Semigroups,” in *10000 Selected Problems in Sciences: Mathematics*, book pp.61–63, PDF pp.77–79. The exact independently stated targets are Questions2 and3 on p.62. The original local PDF is identified in `../source/problem.zh.txt`; the three page images are retained alongside it. The parent and worker independently checked the images rather than relying on the mangled text extraction. An official public copy is also indexed at [Chinese Ministry of Education](https://video.moe.gov.cn/kejisi/shuxue.pdf).

The source requires a finite alphabet, left quotients by all words, and closure under the **complement of symmetric difference**, not intersection/upward closure for semifilters. It imposes no properness axiom. Question1 (cofinite filter) is already positively answered in the book. Questions4/5 concern further semigroup/two-sided settings and are outside this dossier's resolution claim.

## 2. Primary full texts recovered

### Prodinger 1980

Helmut Prodinger, “Congruences Defined by Languages and Filters,” *Information and Control* **44**(1), 36–46 (1980), [DOI10.1016/S0019-9958(80)90123-0](https://doi.org/10.1016/S0019-9958(80)90123-0).

* Lawful [author-hosted PDF](https://helmut-prodinger.de/pdffiles/Congruences%20and%20Filters.pdf), retained as `prodinger1980.pdf`.
* SHA-256: `a8531deb215e77369813074007fe3f1c34541b09bf6d33575350a8ba5cf722d2`.
* Image-only source: all eleven pages were rendered and OCRed in the assigned scratch repository; the load-bearing hypothesis on original p.43 was directly image-checked.
* Definition2.2 introduces the division-property semifilter; Theorem2.4 establishes the right congruence. Section5 defines finite-index generalized regularity.
* **Important scope qualification:** immediately before Lemma5.3, original p.43 says that henceforth the families are FD′ and FD, i.e. filters. The subsequent intersection/Boolean-algebra result is not an arbitrary-semifilter closure theorem. Our proof never imports such closure.
* The final open question on original p.45 is the cofinite characterization. This is the book's already-solved Question1, not by itself a resolution of the book's later general Questions2/3.

### Guo–Wang–Shum 2010

Yuqi Guo, Shoufeng Wang and K.P. Shum, “A survey of combinatorial semigroups: characterizing and generalizing regular languages by semifilters,” *Journal of Shandong University (Natural Science)* **45**(6), 1–7 (2010).

* [Publisher article](https://lxbwk.njournal.sdu.edu.cn/CN/Y2010/V45/I6/1).
* [Publisher download](https://lxbwk.njournal.sdu.edu.cn/CN/article/downloadArticleFile.do?attachType=PDF&id=1841), recovered using the ordinary article-page PDF link in a fresh headless browser after static-reader HTTP403. The link explicitly authorized the public download; no credentials, purchase or CAPTCHA workaround was used.
* Retained as `guo-wang-shum2010.pdf`, SHA-256 `1e9741dcbbfbb788942006f301050f452a37535689fdbcdba648d934d734b895`. Page4, containing the closest special-case criteria, is also retained as `guo-wang-shum2010-page-4.png` and was directly inspected.
* Theorem2.7 records the known cofinite result of Guo–Wang–Li1983.
* For a suffix code S, the paper studies the special filter L_S={A⊆X*:X*S⊆A}. Theorem3.3 says its generalized regular class equals Reg iff S is finite and maximal among suffix codes.
* Theorem3.4 gives a necessary and sufficient condition for equality of two such suffix-code classes: compatibility of one-word suffix-code extensions, mutual suffix comparability, and finiteness of the union of the two language quotients. This is a prior Q3-type criterion for that special family, not an all-semifilter criterion.
* Theorem3.5 compares a second specially constructed semifilter to L_S; the general right congruences can differ while their finite-index language classes agree.
* Proposition5.5 gives an equality criterion for finite prefix-suffix sets, and Problem5.7 asks for arbitrary prefix-suffix sets. These use two-sided contexts, not the exact arbitrary-one-sided-semifilter classification here.
* The final paragraph says remarkable results for general semifilters seem difficult and recommends studying special kinds. Inspection of all seven pages found no stated arbitrary-semifilter version of our proof's (8) or (12). This observation is **not** novelty clearance.

The survey's Theorem2.4 states Boolean-algebra closure with semifilter terminology without repeating Prodinger's filter restriction. This dossier neither relies on nor claims to have resolved that potential discrepancy.

## 3. Relevant later sources whose full text remains unavailable

| Source | Verified evidence | Exact limit |
|---|---|---|
| Guo, Wang, Li, “The Prodinger problem and the Schreier method of regular languages,” *Acta Math.Sin.*26(3),332–340(1983) | Book Fact1; recovered 2010 Theorem2.7; [zbMATH0571.68052](https://zbmath.org/0571.68052) | Original full text not recovered. The cofinite theorem is already established, not a discovery here. |
| Wang, Guo, Xu, “PS-regular languages,” *Int.J.Comput.Math.*88(12),2464–2484(2011), [DOI10.1080/00207160.2010.548517](https://doi.org/10.1080/00207160.2010.548517) | Publisher/Crossref metadata; [zbMATH1243.68217](https://zbmath.org/1243.68217); primary 2010 survey §§5–6 cites its then-submitted version | Publisher full text returns HTTP403. Review describes prefix-suffix-set two-sided congruences and special regularity criteria; it does not establish that arbitrary semifilters were classified. |
| Guo, Wang, Shum, “Restricted Burnside problem for semigroups and its application to language theory,” *Asian-European J.Math.*10(3),1750045(2017), [DOI10.1142/S1793557117500450](https://doi.org/10.1142/S1793557117500450) | [Crossref primary abstract](https://api.crossref.org/works/10.1142/S1793557117500450); [zbMATH1377.20038](https://zbmath.org/1377.20038) | Abstract says it answers a question in Prodinger1980 but does not identify its theorem or scope. PDF HTTP403 and ordinary browser Cloudflare challenge; OpenAlex supplies no repository full text. Do not infer that Q2/Q3 are solved, or not solved, from the abstract. |
| **Wang, “On languages defined by generalized principal right congruences,” Southeast Asian Bull.Math.45(6),969–975(2021)** | [zbMATH1513.68033](https://zbmath.org/1513.68033), independently checked by parent. Summary explicitly studies suffix-closed-language semifilters and reobtains a regularity characterization. | [Public journal link](http://www.seams-bull-math.ynu.edu.cn/downloadfile.jsp?filemenu=_202106&filename=14_45(6).pdf) returns HTTP403. HTTPS fails TLS; ordinary browser HTTP blocked; exact Wayback CDX query returned no PDF capture. Parent also tried the non-www host (DNS failure). This direct-scope paper is a material additional novelty blocker, not an absent paper. |
| Guo, Liu, Wang, *Topics on Combinatorial Semigroups* (Springer2024), [book DOI10.1007/978-981-99-9171-6](https://link.springer.com/book/10.1007/978-981-99-9171-6) | Primary front matter retained as `guo-liu-wang2024-frontmatter.pdf`; [chapter3 landing](https://link.springer.com/chapter/10.1007/978-981-99-9171-6_3) and bibliography read | Chapter3 is pp.77–102; §3.4 “A Decomposition of Regular Languages” starts p.90 and §3.5 “Restricted Burnside Problem and Regular Languages” p.96. The actual chapter PDF redirects to a purchase/institutional-access page. Chapter6 concerns relatively regular languages and chapter8 PS-regular languages. Front matter and abstracts cannot exclude an overlapping theorem. |
| Zhang, “An equivalence relation on suffix codes defined by generalized regular languages,” *Int.J.Comput.Math.*35,15–24(1990), [DOI10.1080/00207169008803887](https://doi.org/10.1080/00207169008803887) | [zbMATH0699.68102](https://zbmath.org/0699.68102) | Related special suffix-code equality problem, not enough to establish an all-semifilter result. Original not recovered. |

**Required novelty action:** obtain lawful full texts of Wang2021, the 2017 paper and the relevant 2024 chapter; identify exact theorem statements and compare their assumptions and conclusions with proof.md Theorems1–5. The 2011 and older original proofs should also be compared before publication. Until that comparison succeeds, label the output a reviewed structural answer with **NOVELTY-UNCLEAR**; do not label a new discovery or count it as a newly solved open problem.

## 4. math/ reference corpus

The local `math/` corpus is read-only. A targeted topic search found one genuine nearby formal-language entry, not a covering semifilter theorem:

* `math/lean/docs/134.md`: generalized star-height bounds for ordinary regular languages. [Remote current counterpart](https://raw.githubusercontent.com/openai/math/main/lean/docs/134.md) was also read.
* `math/lean/ComparatorChallenges/GeneralizedStarHeight.lean`, lines9–35: expression constructors and interpretation using Mathlib's `Language`, complement, ordinary union/concatenation and Kleene star; line42 uses `[Finite Alphabet]` and `Language.IsRegular`.
* Transferable convention: finite alphabets may be modeled with `[Finite Alphabet]`, including the empty type; language semantics use lists of letters. **Mismatch:** its addition and multiplication are ordinary union/concatenation, not the F₂ operations used here. They must not be silently reused for parity products.
* The challenge's `sorry` is a trusted-statement template, not a usable proof. No OAI challenge or solution module was imported or modified.
* No matching arbitrary-semifilter theorem was found in the inspected local/remote entries. This is only a bounded corpus-overlap check, never proof of openness or novelty.

## 5. Evidence ownership

The independent no-tools referee checked mathematical reasoning only; it did not authenticate these sources. Primary-source comparisons above are worker checks, with parent independently checking the book and the Wang2021 bibliographic record. The exact reviewed proof snapshot and all post-review dispositions are in `../evidence/`.
