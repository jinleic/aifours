# Lawful source recovery and applicability

Date: 2026-10-14 (PT). This is the integration owner's source work performed while the frozen HMZ actor worked in its separate scratch repository. Saved raw sources and SHA-256 values are in `sources/manifest.json`.

## What was actually recovered

| Source | Access and exact relevant content | What it does not establish |
|---|---|---|
| [Mária B. Szendrei's institutional publication list](https://www.math.u-szeged.hu/tagok/bszendre/papers.html) | HTTP 200, raw HTML saved. Entries 40 and 41 confirm the 2002 and BS2003 bibliography. Raw HTML inspection confirms **no full-text links on those two entries**. The list does provide author-hosted PDFs for later papers. | A web-search summary said BS2003 appeared available as a PDF. This was not supported by the actual page and is not adopted. No confusion with Ágnes Szendrei's different publication page. |
| [Bernd Billhardt's institutional publication list](https://www.mathematik.uni-kassel.de/~billhard/) | HTTP 200, raw HTML saved. Items 9 and 15 confirm Billhardt1998 and BS2003. Neither item links a full text. | No verification of the actual 1998 example, its local monoids, or its band identities. |
| [Szendrei, Almost factorizable locally inverse semigroups (2011), author PDF](https://www.math.u-szeged.hu/~bszendre/a-fact-LI.pdf) | HTTP 200, PDF saved. Preliminaries pp. 2–5 state the exact natural order, weak E-unitarity, Kad'ourek's idempotent-pure least-completely-simple congruence theorem **for locally inverse semigroups**, and define the Pastijn product for an **arbitrary semigroup K**. Result 6 restates the BS2003 locally inverse embedding theorem. | The later author paper is not the original BS2003 proof. It does not replace normality by local regularity or settle P1. It does supply a direct lawful primary source for the arbitrary-first-factor Pastijn formula, in addition to the earlier AS2005 citation. |
| [Hartmann–Szendrei, E-unitary almost factorizable orthodox semigroups (2012), author PDF](https://www.math.u-szeged.hu/~bszendre/e-un_fact.pdf) | HTTP 200, PDF saved. The abstract and §1 distinguish being **isomorphic to** a band-by-group semidirect product from being E-unitary almost factorizable. Proposition 3.1 characterizes certain idempotent-separating E-unitary congruences on `B⋊G`; Construction 3.4 and Theorem 3.5 use Q-products. | Its negative is an isomorphism obstruction, not non-embeddability in a larger band-by-group product. It is not a counterexample to P1 or Q_orth. |
| [Dékány, E-solid locally inverse semigroups as extensions (2019 thesis)](https://doktori.bibl.u-szeged.hu/id/eprint/9998/1/disszertacio_DT.pdf) | Public University of Szeged repository, HTTP 200; PDF saved. Introduction pp. 1–5 cites the regular-band embedding theorem and Billhardt's nonembedding, without reproducing the counterexample. §2.2 gives semidirect/wreath coordinate conventions. | The main result concerns E-solid **locally inverse** semigroups and λ-semidirect products of completely simple semigroups by inverse semigroups. Those factors/order differ from the book's locally r-orthodox target. No theorem is imported as a substitute. |

These full-text recoveries were reached through the authors' actual institution-hosted links. No access control, CAPTCHA, paywall, credential, or subscriber login was bypassed.

## Three requested older sources: limits after additional routes

### Billhardt 1998

Exact title: *On Embeddability into a Semidirect Product of a Band by a Group*, J. Algebra 206 (1998), 40–50; DOI [10.1006/jabr.1997.7390](https://doi.org/10.1006/jabr.1997.7390).

- OpenAlex [W1967329499](https://api.openalex.org/works/W1967329499) was fetched and saved. It calls the publisher PDF bronze open access but lists no repository full text. Metadata is not evidence that a working download was available.
- The supplied [ScienceDirect PDF URL](https://www.sciencedirect.com/science/article/pii/S0021869397973907/pdf) returned HTTP 403 in the static reader.
- Billhardt's own institution-hosted publication list was opened; its citation is not a download link.
- Targeted university-site queries and a title/DOI search produced no accessible copy of this article. Other irrelevant search hits were not treated as evidence.
- Dékány's lawful thesis and Szendrei's 2019 survey confirm the nonembedding result but do not supply the construction or its local-regularity check.

**Unchanged precise limit:** it remains unverified whether Billhardt's actual left-semiregular band is locally regular. The existing `E5^1` example only disproves the class implication; it does not decide Billhardt's particular band. No inference from the title, year, left-semiregularity, or unsuccessful searches is promoted to an answer.

### Szendrei 2002

- The [Springer article page](https://link.springer.com/article/10.1007/s002330010100) opened, with the explicit subscription-preview boundary. It gives the abstract, pages 213–223, issue date February 2002, and online date 16 November 2001.
- The author's publication-list entry 40 has no full-text link. [OpenAlex W2087029700](https://api.openalex.org/works/W2087029700), saved here, reports closed access and no repository full text.
- The [2000 Szeged colloquium program](https://www.math.u-szeged.hu/confer/algebra/2000/program.htm) confirms the problem-session talk, but contains no statement of the problem or manuscript.
- University-site and Hungarian repository searches did not expose an accessible copy of the paper.

**Unchanged precise limit:** the source author's exact Problem 1 wording and original product convention remain unverified. The book excerpt, with the two adopted P/R readings, is still the statement authority for this project. The 2011 author-hosted paper confirms the adopted Pastijn formula but not the wording of the 2002 problem.

### Billhardt–Szendrei 2003

- Both authors' institution-hosted publication lists confirm the citation but have no link at the article's entry.
- The old metadata's [CORE download](https://core.ac.uk/download/81943467.pdf) returned HTTP 403; its [reader](https://core.ac.uk/reader/81943467) returned HTTP 410; the two known API output URLs `/v3/outputs/81943467` and `/v3/outputs/203266127` returned HTTP 404; [work page](https://core.ac.uk/works/41252261) returned HTTP 403.
- An indexed [ResearchGate record](https://www.researchgate.net/publication/215520995_Weakly_E-unitary_locally_inverse_semigroups) returned HTTP 403; no login or request-for-full-text action was taken.
- Searches of REAL and the Szeged institutional repositories found grant reports and later papers, not this full text. The lawful [OTKA-37877 report](https://real.mtak.hu/387/1/37877_ZJ1.pdf) points to `http://www.math.u-szeged.hu/kozos/37877/`; that page now returns HTTP 404. A public Wayback index query for PDFs under that exact path returned no rows. A broader archive query found a [2006 grant-index page](https://web.archive.org/web/20060408041107/http://www.math.u-szeged.hu:80/~dorman/MAIN/OTKA-T37877/); opening it showed only `cim.pdf` and `cmcpc.pdf`, not the requested title, and its current counterpart returned HTTP 404. The report cites BS2003 in its external bibliography, not necessarily among the linked grant outputs, so its general statement that grant papers were available does not prove BS2003 was hosted there.
- The fully readable 2011 author paper explicitly restates the embedding as Result 6, but its proof is not the missing 2003 article.

**Unchanged precise limit:** BS2003 full text was not recovered. Its title/abstract and later author statements remain usable at their exact scope; the original proof is not claimed inspected.

## Implication for the attack

There is no justified source-based negative resolution of P1 here. Equally, there is no justified claim that P1 remains open in the literature as of today: no resolution was found in this dated bounded search, which is not proof of openness.

The new written finite `ξ`-purity argument is in `xi-purity.md`; it is independent of all three missing older texts. The parent has audited the coordinate argument, finite corollary and hypothesis-omission control and found no gap (`written-claim-audit.json`). It is not Lean-checked and does not prove an embedding. None of the recovered later-source theorems is silently substituted for the original goal.
