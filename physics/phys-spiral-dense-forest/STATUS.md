# Spiral dense forests: source status and prior-art boundary

Checked: **2026-10-14, America/Los_Angeles**. A bounded public-source screen is not worldwide priority clearance.

## 1. Explicit published question and exact meaning

**Yohay Ailon Tevet, “Chabauty Limits of Fermat Spirals,” [arXiv:2506.22863v2](https://arxiv.org/abs/2506.22863v2), revised 2025-09-16.** The preserved arXiv API record resolves to v2. The publication is *Combinatorics and Number Theory* **14(3-4)** (2025), 239–249, DOI [10.2140/cnt.2025.14.239](https://doi.org/10.2140/cnt.2025.14.239), published 2025-10-24. Raw Crossref and OpenAlex target records are preserved as `source/crossref-target-20261014.json` and `source/openalex-target-20261014.json`; the [publisher landing page](https://msp.org/cnt/2025/14-3/p02.xhtml) independently confirms the metadata. Its full PDF was subscription-blocked. The exact text audited here remains the pinned arXiv v2, not an assumed publisher-layout match.

**Further Questions, PDF p.12** explicitly states:

> “The author conjectures that there is a spiral set that is a dense forest”

This was checked both in the original rendered page (`source/tevet-page-12.png`) and the full-text passage. The introduction defines a spiral set as \(\{\sqrt{k}u_k:k\ge1\}\), with arbitrary unit vectors \(u_k\). A dense forest must have finite density and one visibility length for **all positions and orientations** at every positive width. Its definition does not require Delone separation. The paper proves that **no constant-angle Fermat spiral** is a dense forest; it does not exclude arbitrary-direction spirals.

An earlier primary source gives the opposite conjecture: **F. Adiceam and I. Tsokanos, “Visibility properties of spiral sets,” Moscow Journal of Combinatorics and Number Theory 11(2) (2022), 149–159**, DOI [10.2140/moscow.2022.11.149](https://doi.org/10.2140/moscow.2022.11.149), [arXiv:2111.01843v1](https://arxiv.org/abs/2111.01843v1). In the introduction following Figure 1:

> “By contrast, the existence of a spiral set which is a dense forest remains an open question.”

Their following sentence conjectures nonexistence. Their main theorem characterizes spiral visibility; that characterization is not a construction or a nonexistence theorem. Tevet's later conjecture is existence. The target here is that exact existence question, so a successful construction would also refute the earlier nonexistence conjecture—not Tevet's Fermat-spiral obstruction.

## 2. Connection to the supplied physics book

The original source is Cao Zexian's “Are the Fibonacci Parastichous Spirals a Least-Energy Configuration on Conical Surface?”, *10000个科学难题·物理学卷* (2009), book pp.541–543 / PDF pp.574–576. The unchanged supplied excerpt is `source/problem.zh.txt`.

This is an explicitly labeled **broader mathematical refinement of phyllotactic spiral-distribution questions**, approved by the parent. The construction is planar, arbitrary-angle, and designed for visibility. It does **not** establish minimum energy on cones, a specific interaction law, Fibonacci packing optimality, a preferred chirality, or a sunflower construction. No such book-scale claim is made.

## 3. Strongest comparable established ingredients

| Primary source | Established result used or compared | What is not claimed here |
|---|---|---|
| **V. Shirandami**, “Dense forests constructed from grids,” *Mathematische Zeitschrift* (2023), DOI [10.1007/s00209-023-03331-5](https://doi.org/10.1007/s00209-023-03331-5), [arXiv:2303.14719v2](https://arxiv.org/abs/2303.14719v2), Introduction and Theorem 1.1 | Irrationality characterization of finite unions of translated lattices; two appropriately rotated planar grids suffice. | The base two-grid forest is **prior art**, not an invention of this project. RESULTS §3 supplies a sufficient special-case proof with uniform time and arbitrary phases. |
| **F. Adiceam, Y. Solomon, B. Weiss**, “Cut-and-project quasicrystals, lattices, and dense forests,” *Journal of the London Mathematical Society* (2022), DOI [10.1112/jlms.12534](https://doi.org/10.1112/jlms.12534), [arXiv:1907.03501v2](https://arxiv.org/abs/1907.03501v2) | Finite-grid forest constructions and generic visibility results, including extensions of the Peres construction. | No new lattice-forest theorem or improved generic visibility exponent is claimed. |
| **J. Guo**, “Lattice points in rotated convex domains,” *Revista Matemática Iberoamericana* 31(2) (2015), 411–438, DOI [10.4171/rmi/839](https://doi.org/10.4171/rmi/839), [primary PDF](https://ems.press/content/serial-article-files/38537), §1 p.411 | The stated standard smooth positive-curvature bound is \(O(R^{n-2+2/(n+1)})\), hence \(O(R^{2/3})\) for the planar disk. | We use this classical introductory bound, **not** an almost-every-rotation improvement. RESULTS §4 writes a self-contained smoothing/Poisson proof of the needed planar case. |
| **F. Adiceam**, “Around the Danzer Problem and the Construction of Dense Forests,” [arXiv:2010.06756](https://arxiv.org/abs/2010.06756) (2021 survey) | Context linking dense forests, finite density and Danzer sets. | Survey references are not evidence that the new exact-radius bridge is unpublished. |
| **K. Kashkan**, “A New Construction of Forests with Low Visibility,” [arXiv:2407.01633v2](https://arxiv.org/abs/2407.01633v2) (2024); *Mathematika* 71(2) (2025), e70013, DOI [10.1112/mtk.70013](https://doi.org/10.1112/mtk.70013) | Introduction and Theorem 1.1 construct finite-density forests by augmenting a Poisson process, with visibility \(O(\varepsilon^{-(d-1)}\log\varepsilon^{-1})\). | Relevant introductory/full-theorem passages were inspected, not the entire proof. This is a visibility benchmark, not a competing exact-radius spiral construction identified here. We do not improve its rate. |

The actual bridge requiring proof is **norm-ranking an established forest while preserving the uniform all-segment visibility property**. A mere radial volume asymptotic would not suffice. The sharper disk count gives an \(o(1)\), uniformly tie-controlled displacement from \(\sqrt{2\pi}(\mathbb Z^2\cup Q\mathbb Z^2)\). A finite-core stability lemma then transfers visibility, including rectangles whose centerlines pass through the core. This is why the obligation is bounded; the argument does not try to solve the general Danzer problem or optimize visibility.

The related workspace result `../phys-spiral-delone-uniform-density/RESULTS.md` §§3–4 was read for the general rank/discrepancy argument. Its owner supplied references and warnings. The present proof and code are written independently for the two-grid planar forest; its uniform-discreteness conclusion is **not** imported.

## 4. Current forward/backward screen, with actual depth

### Forward screen

- **OpenAlex, 2026-10-14:** `source/openalex-target-20261014.json` binds [W4415529271](https://openalex.org/W4415529271) to Tevet's journal DOI. The separately preserved [citing query](https://api.openalex.org/works?filter=cites:W4415529271&per-page=100&select=id,title,doi,publication_date) returns **`meta.count=0` and `results=[]`** in `source/openalex-citing-20261014.json`. This excludes neither unindexed work nor an indexing lag.
- **Current arXiv record:** the API links to **2506.22863v2**. The specific existence conjecture is still present in that version. A date printed by regenerated HTML is not substituted for the arXiv version date.
- **Exact-term web queries:** `"spiral" "dense forest" "Tevet"`, `"spiral set" "dense forest" proof construction`, `"spiral" "dense forest" "lattice"`, and `"dense forest" "radial"`. No additional settling source was identified. Many generic “forest” search results concerned trees and were irrelevant; those are not mathematical evidence.
- The journal's metadata was checked through raw Crossref, OpenAlex and its publisher landing page. The publisher PDF returned an explicit subscription/purchase denial, which was not bypassed. Source definitions/quotes use arXiv v2. Late access attempts and additional scope checks are recorded in `review/late-source-checks.txt`.

### Source-depth ledger

| Source | Depth actually checked | Relevant conclusion / limit |
|---|---|---|
| Tevet 2506.22863v2 | Full-text introduction/definitions, Fermat obstruction statement, Further Questions, original p.12 image; full PDF preserved | Exact existence question and absence of a uniform-separation requirement confirmed. |
| Adiceam–Tsokanos 2111.01843v1 / 2022 paper | Full-text definitions, main theorem statement and post-Figure-1 open/nonexistence passage; PDF preserved | Earlier opposing conjecture, not an impossibility proof. |
| Shirandami 2303.14719v2 | Full-text introduction and Theorem 1.1; PDF preserved | Finite-grid forests are an established ingredient. We supply our own sufficient proof and never count zero as a direction. |
| Adiceam–Solomon–Weiss 1907.03501v2 | Abstract/introductory construction context; full PDF preserved | Established finite-union baseline; not a complete independent audit of every appendix. |
| Guo (2015) | Original §1 p.411 introductory classical bound; full PDF reader available | Correct all-fixed-dimension standard bound, not the main generic improvement. |
| Kashkan 2407.01633v2 | Introduction, definitions and Theorem 1.1 in full-text HTML; no full proof audit | Newer probabilistic visibility result; no exact-radius claim identified in those sections. |
| Adiceam survey 2010.06756 | Bibliographic/abstract context via primary references and search | Not represented as a full-text priority audit. |
| **V. N. Berestovskii**, “Spiral dispositions of nonnegative integers at lattice points,” *Mat. Tr.* 8(2) (2005), 49–68; English translation *Siberian Advances in Mathematics* 16(2) (2006), 43–61; [zbMATH](https://zbmath.org/1249.11060), [primary abstract](https://www.mathnet.ru/php/archive.phtml?jrnid=mt&option_lang=eng&paperid=62&wshow=paper) | Secondary summary and subsequently the **primary abstract**; original proof text not inspected | Integer labeling of square/hexagonal/cubic lattices and visibility of primes. The linked full-text reader timed out; a separate curl attempt failed to connect (exit 28). No conclusion about an unseen ranking lemma is drawn. |
| **F. Adiceam, I. Tsokanos**, *Higher Dimensional Spiral Delone Sets*, [arXiv:2010.06428v3](https://arxiv.org/abs/2010.06428v3), 2020 / revision 2021-03-30 | Original introduction/main theorem, construction overview and §6 open questions; full-text term search; PDF/text preserved | Toral lifting constructs Delone spirals in every dimension; §6 separately asks for asymptotic density in dimensions ≥3. No forest construction or norm-ranking transfer was identified in the inspected passages. Not a full line-by-line proof audit. |
| **S. Akiyama**, “Spiral Delone sets and three distance theorem,” *Nonlinearity* 33 (2020), 2533–2540, DOI [10.1088/1361-6544/ab74ad](https://doi.org/10.1088/1361-6544/ab74ad), [arXiv:1904.10815v2](https://arxiv.org/abs/1904.10815v2) | Original definition and main Theorems 2–3; full-text term search; PDF/text preserved | Fixed-angle Fermat Delone characterization. Delone is not dense forest; Tevet excludes this fixed-angle family from forests. |
| **J. Marklof**, “Delone sets generated by square roots,” [arXiv:2003.08319v1](https://arxiv.org/abs/2003.08319v1) (2020), DOI [10.1080/00029890.2020.1811003](https://doi.org/10.1080/00029890.2020.1811003) | All substantive text of the five-page note, Propositions 1–3 and conclusion; PDF/text preserved | Angular equidistribution versus density, annular gap characterization, and \(\sqrt{k}e^{2\pi i\alpha\sqrt{k}}\) Delone examples. No dense-forest or ranked-grid construction identified. |
| **Y. Yamagishi, T. Sushida, J.-F. Sadoc**, “Area convergence of Voronoi cells on spiral lattices,” *Nonlinearity* (2021), DOI [10.1088/1361-6544/abe733](https://doi.org/10.1088/1361-6544/abe733), [arXiv:2006.14723v1](https://arxiv.org/abs/2006.14723v1) | Original introduction, exact family definition, Theorem 1 and Corollary 2; PDF/text preserved | Voronoi-area asymptotics for \(j^\alpha e^{ij\theta}\) with fixed angle; no arbitrary-angle forest existence result identified in those sections. |

**Screen conclusion:** an exact historical open statement is confirmed, and no later or older source settling this exact spiral-forest existence question was identified in the bounded material checked. This is **not worldwide unsolved-status or first-proof certification**. All classical components are credited. The broad source screen should be extended by a human specialist before publication-priority claims.

## 5. Verdict boundary

**SOLVED for the precise existence theorem; correctness state DELIVERY-READY; evidence Certification; novelty/priority NOVELTY-UNCLEAR.** Both independent reviewers accepted the mathematical argument with minor revisions, now dispositioned in `RESULTS.md` §10. The additional spiral-Delone screen above was performed after their frozen snapshot; it strengthens provenance without clearing worldwide priority. No optimal visibility rate, Danzer spiral, Delone forest, physical energy optimum, Lean/kernel verification or worldwide-first claim is made.
