# Explicit question, prior art, and forward-citation screen

Snapshot: **2026-10-14 PT**. The target is an explicit 2025 primary-source conjecture/question. That is stronger eligibility evidence than a project-local missing proof, but it does **not** establish worldwide first priority. The local approximation and covolume ingredients already appear in Bacher (2014); this overlap is central, not a footnote.

## 1. Exact primary open statements

**Yohay Ailon Tevet**, *Chabauty Limits of Fermat Spirals*, [arXiv:2506.22863v2](https://arxiv.org/pdf/2506.22863v2), version submitted **16 September 2025** (PDF dated 18 September), **Remark on PDF p. 4**:

> The author conjectures that for α that is not badly-approximable the only non-empty Chabauty limits are isomorphic to R, Z², and Z × R, and in particular the limit cannot be R².

**Further Questions, PDF p. 12**, after explicitly introducing irrational non-BA angle differences:

The immediate antecedent on the same page is:

> As noted above, the author conjectures that the limits are isomorphic to ∅, R, Z², and Z × R.

It is followed by:

> Computational evidence suggests they are all achieved, but a full classification could be interesting, and in particular do the lattices also have co-volume π.

Each extract is under 40 words. The pinned full primary PDF is `source/tevet-2506.22863v2.pdf`, with SHA-256 in `source/manifest.json`.

The p. 4 statement gives the conjectured **containment**, while the p. 12 passages suggest all listed types are **attainable**. Our classification proves the containment in sharpened form and excludes `Z x R`. It must not be described as a counterexample to the weaker containment interpretation merely because one proposed possibility is unnecessary.

### Published version versus inspected version

The [publisher article page](https://msp.org/cnt/2025/14-3/p02.xhtml) verifies publication as **Combinatorics and Number Theory 14 (2025), no. 3–4, 239–249**, DOI [10.2140/cnt.2025.14.239](https://doi.org/10.2140/cnt.2025.14.239), published **24 October 2025**, accepted 10 September 2025. Thus this work is not merely an unrefereed preprint.

The [publisher PDF link](https://msp.org/cnt/2025/14-3/cnt-v14-n3-p02-s.pdf) returned a subscription/access-denied page, not a PDF. No access restriction was bypassed. **The exact quotations and definition audit above are from the openly accessible arXiv v2**, not an uninspected final journal text. The current arXiv landing page still identifies v2 as its latest version and supplies the journal DOI. Whether every word in the journal's Further Questions section is identical was not verified.

## 2. Definition and book bridge

The inspected paper, PDF p. 2, defines a Chabauty limit by translating a closed set with vectors tending to infinity. Theorem 1 explicitly says nonempty limits are **translations of closed subgroups**. We therefore use translation-only limits and retain affine offsets. Rotating a frame for local calculations is not permission to rotate or rescale the source in the limit definition.

The book chapter is Cao Zexian's *Are the Fibonacci Parastichous Spirals a Least-Energy Configuration on Conical Surface?*, *10000 Selected Problems in Sciences: Physics* (Science Press, 2009), pp. **541–543**, PDF pp. 574–576. Its unedited excerpt is copied to `source/problem.zh.txt`. The connection is phyllotaxis/local packing geometry of Fermat spiral point sets, the standard planar sunflower model. This precise paper question is **not** the full cone-energy-minimization question and does not assert any optimality of a physical interaction potential.

## 3. Strongest classical baseline and its bearing

**Roland Bacher**, *On geodesics of phyllotaxis*, **Confluentes Mathematici 6(1)** (2014), DOI [10.5802/cml.10](https://doi.org/10.5802/cml.10); [refereed primary PDF](https://www.numdam.org/item/10.5802/cml.10.pdf), pinned as `source/bacher-2014.pdf`.

The relevant statements in the **refereed PDF**, whose numbering differs from arXiv:1301.7568, are:

- **Theorem 1.1:** uniform-in-angle local approximation near distant spiral points by affine lattices, with an explicitly identified similarity class. Its definition of epsilon-closeness covers both local directions.
- **Proposition 3.1 and Corollary 3.2:** the actual continued-fraction-basis linearization, with local error of order `1/sqrt(n)`.
- **Remark 3.3:** the linearized lattice has fundamental area **pi** exactly. Our lattice `L_n={(q/(2sqrt(n)),2*pi*sqrt(n)*(q*alpha-p))}` is the same object after a unimodular integer basis change.
- **Remark 1.2(1)–(2):** rational angles give a rank-one local degeneration, and Bacher asserts that Voronoi-cell areas tend to pi for **every irrational** angle. The latter assertion is unproved in the paper. Read with his one-to-one local description, it already asserts the affirmative lattice-limit covolume answer in Voronoi-area form: with nonmerging local convergence, the Voronoi cells converge to the lattice cell. This implication is our reading of his statements, not a named Chabauty theorem in his paper. We do not infer Voronoi-area continuity from arbitrary Fell convergence or use the unproved area assertion in the classification proof.
- **Proposition 6.1:** states equivalence of bounded continued-fraction coefficients with uniform discreteness/relative density and compactness of the shape orbit, then says the proof is left to the reader. For the optional BA no-empty boundary, our actual proof source is the inspected Akiyama Theorem 2 below.

**Material overlap:** combining Bacher's uniform local description and area normalization with the elementary fixed-covolume planar-lattice compactification already gives the classification route. Our contribution is a self-contained quantitative certification and explicit application to the question posed in 2025, with both local inclusions, affine recentering, type realizability and negative controls written out. It is **not** a new local-lattice mechanism. A first-priority claim would require a broader review of earlier consequences and literature; none is made here.

Bacher does not frame these statements as the exact translation-only Chabauty type/covolume question in Tevet's Further Questions. Nevertheless, the implication from his results is transparent and should be acknowledged as a **classical corollary**, not hidden to manufacture originality. Tevet's inspected references do not cite Bacher. An explicit later conjecture does not erase earlier mathematical ingredients or their consequences.

### Additional direct baselines requested by the referee

**Y. Yamagishi, T. Sushida and J.-F. Sadoc**, *Area convergence of Voronoi cells on spiral lattices*, **Nonlinearity 34** (2021), 3163–3183, DOI [10.1088/1361-6544/abe733](https://doi.org/10.1088/1361-6544/abe733); primary [arXiv:2006.14723v1](https://arxiv.org/pdf/2006.14723v1), Theorem 1 and Corollary 2, p. 2, now read and pinned. **Both explicitly assume the angle divided by 2*pi is badly approximable.** With radial exponent 1/2 their conclusion is area pi. The published abstract has the same BA qualification; the journal body was not accessible. Tevet's p. 10 pointer to this result supports his BA Proposition 12. It does not remove the non-BA question by dropping that hypothesis. The unversioned arXiv landing page identifies v1 as its only version; a secondary search listing suggesting another revision was not adopted.

**Shigeki Akiyama**, *Spiral Delone sets and three distance theorem*, **Nonlinearity 33** (2020), 2533–2540, DOI [10.1088/1361-6544/ab74ad](https://doi.org/10.1088/1361-6544/ab74ad); primary [arXiv:1904.10815v2](https://arxiv.org/pdf/1904.10815v2), Theorem 2 (p. 3) and proofs in §§2–3, now read and pinned. It proves that relative density, uniform discreteness, being Delone, and BA are equivalent for these irrational-angle Fermat sets. This is a proved source for the boundary fact Bacher had announced without proof. It does not classify nonempty non-BA Chabauty limits.

These comparisons strengthen the classical-overlap record without changing the mathematical proof. In particular, “all irrational Voronoi areas converge” (Bacher's unproved remark), “BA Voronoi areas converge” (YSS21's proved theorem), and “every lattice translation limit has covolume pi” (the present fixed-covolume argument) are kept distinct.


## 4. Current follow-up screen and limits

| Source/query on 2026-10-14 | Depth actually checked | Observed result | Limitation |
|---|---|---|---|
| [OpenAlex DOI work record](https://api.openalex.org/works/https://doi.org/10.2140/cnt.2025.14.239) | Complete metadata record | Work `W4415529271`; cited-by count **0**. | Indexing is incomplete and can lag. |
| [OpenAlex direct citing-works query](https://api.openalex.org/works?filter=cites:W4415529271&per-page=100&select=id,title,doi,publication_year) | Complete returned list | Count **0**, empty results; raw response pinned. | No later full texts were available from this query to inspect. |
| OpenAlex arXiv DOI lookup `10.48550/arXiv.2506.22863` | Metadata | Resolves to the same journal-linked work, not an independent second zero-count record. | Avoids double-counting the two identifiers as separate searches. |
| Semantic Scholar public API, `ARXIV:2506.22863` | Retrieval attempted | Direct API request returned HTTP **429**; tool URL routing also rejected the colon-form URL. | **Unavailable, not zero citations.** |
| Web exact-title search; `"Fermat spirals" "covolume" "limits"`; `"Tevet" "Chabauty" "2026"` | Search results/titles, followed primary arXiv and publisher pages | Returned the source paper and secondary listings; no explicit later primary settlement identified among these results. | A bounded query screen, not exhaustive absence or novelty evidence. |
| Bacher 2014 | Relevant theorem, linearization and area sections read in full primary text | Strong earlier local-lattice machinery, explicitly retained as the baseline. | Its relationship to our conclusion is classical, even without a theorem titled “Chabauty classification.” |
| Yamagishi–Sushida–Sadoc 2021 | Primary arXiv Theorem 1/Corollary 2 and published abstract read | Area convergence theorem assumes BA, including the Fermat exponent 1/2. | Does not settle the non-BA question by itself; journal body uninspected. |
| Akiyama 2020 | Primary arXiv statement and proofs read | Establishes the relative-density/Delone/BA equivalences used only as optional boundary context. | No full non-BA limit-type classification in the inspected text. |

The raw OpenAlex work/citation records and paper hashes are under `source/`. We make no claim that the question remained worldwide unsolved until this session. The eligibility statement is precisely that **an inspected 2025 primary version explicitly poses it**, and this folder supplies a proof with classical ingredients and an explicitly bounded follow-up screen.

## 5. Exact obligation and tractability

The bounded missing bridge is geometric, not a large search:

1. approximate both directions between a fixed-radius centered spiral window and a covolume-pi lattice, uniformly without BA;
2. classify limits of fixed-covolume planar lattices by a shortest vector and a reduced complementary vector;
3. recenter arbitrary nonempty escaping translates at actual spiral points;
4. show thick subsequences for every irrational angle and thin subsequences for every non-BA irrational angle, with translation-only angular freedom.

Each part has an elementary, auditable argument in RESULTS.md. No finite convergence plot proves the universal statement. Realizability here means occurrence of the **types** for each non-BA angle, not universality of all shapes for that fixed angle. The companion project on lattice universality is separate and is not used by this classification proof.
