# BRD(26,130,25,5,4) bounded priority screen (scout report, verbatim)

Recorded 2026-10-17 13:01:42 PDT from read-only scout `Brd26Priority`. The parent independently read the zbMATH review Zbl 1229.05045 and the Springer landing-page abstract of Abel–Chan–Combe–Palmer, Des. Codes Cryptogr. 61 (2011) 285–300, which state the sufficiency theorem quoted below.

**BRD(26,130,25,5,4) (BRD(v=26, k=5, λ=4)) is not an open existence case in the published literature.** Abel, Chan, Combe and Palmer, *Des. Codes Cryptogr.* 61 (2011) 285–300, online 2011-01-14, state in their abstract that the necessary conditions for BRD(v,5,λ) with λ∈{4,10,20} are sufficient except at v=5, λ∈{4,10}. (v,λ)=(26,4) meets every condition, so its existence was asserted in 2011. Our 26×130 matrix is therefore an explicit witness for a design already claimed to exist; it settles nothing open and completes no spectrum.

Evidence is abstract-level only: the paper body is paywalled, so how they built v=26 was not inspected. The CPro1/Rosin "open" label comes from the 2006 Handbook, and neither Rosin paper cites the 2011 paper or the 2002 paper it builds on.

**Theorem applicability**

| Source | Statement (scope) | Definition match | Applies to (26,4)? | Read level |
|---|---|---|---|---|
| Abel–Chan–Combe–Palmer (ACCP) 2011, [Springer](https://link.springer.com/article/10.1007/s10623-010-9477-6), [zbMATH](https://zbmath.org/1229.05045) | BRD(v,5,λ), λ∈{4,10,20}: conditions (i)–(iv) are sufficient except v=5, λ∈{4,10} | Standard BRD. The v=5, λ=20 case exists, and with v=k=5 every block is the same 5-set, so repeated blocks are allowed [INFERENCE] | **Yes** [computed]: 26≥5; 4·25=100≡0 (mod 4); 4·26·25=2600=40·65; λ even; v≠5. Gives b=130, r=25 | Abstract on two indexes. Crossref `relation:{}` (no erratum deposited) |
| Chaudhry–Greig–Seberry (CGS) 2002, *JSPI* 106:303–327, [zbMATH](https://zbmath.org/0997.05020), [author copy](https://documents.uow.edu.au/~jennie/WEBPDF/2002_09.pdf) | Sufficient for λ=4,10,20 "with a few (possible or definite) exceptions" | Same definition. The author copy has a theorem on identical blocks and the BRD(k,k,t) construction, so repeated blocks are contemplated | Probably listed 26 as a possible exception [INFERENCE] | Author PDF loads, but our text extraction drops every digit and math symbol |
| Handbook 2nd ed. V.4 (2006) | Source of the open lists, per Rosin §3.1 | — | Lists (26,4) [INFERENCE via CPro1] | Not accessed |
| CPro1 [problem_def](https://raw.githubusercontent.com/Constructive-Codes/CPro1/main/CPro1/design_definitions/bhaskar-rao-design/problem_def.py), HEAD [827f02b](https://github.com/Constructive-Codes/CPro1/commit/827f02b4048fc96a6b79f0970c87ca5a54f31f40) (2026-06-03) | 26 is in `OPEN_INSTANCES`; the [results directory](https://github.com/Constructive-Codes/CPro1/tree/main/designs/bhaskar-rao-design) has files for 15-42, 16-48 and 15-126 only | Equivalent to the standard definition. The verifier has no distinctness check, and dev instance [5,16,16,5,16] forces repeated supports | Lists 26 as open | Read |
| Rosin [2505.23881v1](https://arxiv.org/abs/2505.23881v1) Table 1(a) | Marks (15,4), (15,12), (16,4) as solved; 26 absent | Same as CPro1 | No claim about 26 | Pinned layout, lines 126–129 and 142 |
| GBRD over a group of order 2 ([EJC 2011](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v18i1p32)) | A BRD is a GBRD over Z2 | Distinct, more general object | No separate GBRD(26,5,4;G) result found | Read |
| c-BRD (Hurd–Sarvate; Greig–Hurd–Sarvate 2004) | The c=0 case is a BRD | Distinct object | Not used | ScienceDirect 403 |
| c-BRBTD, [Francel–Hurd 2008](https://ajc.maths.uq.edu.au/download/42/ajc_v42_p003.pdf) | Entries in {0,±1,±2} | Different object (ternary) | No | Pinned copy |

```json
{
 "attestations": [
  {"src":"CPro1 problem_def (main, 827f02b)","quote":"OPEN_INSTANCES = [[15,42,14,5,4],[16,48,15,5,4],[26,130,25,5,4],[15,126,42,5,12]]"},
  {"src":"Rosin 2505.23881v1 §3.1, layout lines 239-242","quote":"Each of these has clearly defined open instances in the Handbook ... Instances which have already been solved in the literature are omitted [43, 35, 17, 13, 8, 16, 18, 9]","note":"None of those refs is a BRD paper; grep of both Rosin layouts finds no Abel, Palmer, Chaudhry, Seberry or de Launey"},
  {"src":"Rosin 2505.23881v1, layout line 142","quote":"(a) Open instances from 2006 Handbook, that were solved and found to exist by CPro1."}
 ],
 "prior_claims": [
  {"claim":"BRD(v,5,λ) spectrum for λ∈{4,10,20} complete except v=5, λ∈{4,10}","quote":"necessary existence conditions are (i) v ≥ 5, (ii) λ(v − 1) ≡ 0 (mod4), (iii) λ v(v − 1) ≡ 0 (mod 40), (iv) λ ≡ 0 (mod 2). We show these are sufficient, except for v=5, λ∈{4,10}.","url":"https://doi.org/10.1007/s10623-010-9477-6","date":"received 2010-04-23; online 2011-01-14","kind":"peer-reviewed theorem (abstract)","verified":"abstract only","stance":"counter to 'open'"},
  {"claim":"Scope of that theorem","quote":"Chaudhry et al. (J Stat Plann Inference 106:303–327, 2002) have examined the existence of BRD(v, 5, λ)s for λ ∈ {4, 10, 20}.","note":"Read literally for all λ the claim fails at (5,2): the conditions hold but 5 orthogonal ±1 vectors of length 2 cannot exist. So the scope must be λ∈{4,10,20}. (26,4) is covered under either reading [computed]"},
  {"claim":"Same abstract hedges where cases remain open","quote":"and possibly for λ = |G|, (v,|G|) ∈ {(10,2h), (5,6h), (7,4h)}","note":"The BRD part has no 'possibly'"},
  {"claim":"CGS 2002 left exceptions","quote":"prove that the necessary divisibility conditions turn out to be sufficient for λ=4, 10 and 20 with a few (possible or definite) exceptions","src":"zbMATH review (Boyvalenkov)","note":"Author PDF text shows a λ=4t theorem 'withthepossibleexceptionofBRD BRD BRD BRD' with digits lost. A match to CPro1's four instances is plausible but unverified"},
  {"claim":"Corollary: all four CPro1 BRD open instances are covered","note":"(15,4) and (16,4) directly; (15,12) as three copies of BRD(15,5,4) [INFERENCE]. So CPro1's three 2025 BRD 'solutions' were also already covered, per the abstract"}
 ],
 "priority": "Existence is not new: published claim since 2011. No explicit public BRD(26,5,4) matrix or base blocks located in the bounded screen, but the ACCP body is unread, so whether they printed one is unknown. No correction located (Crossref relation empty). Citing works checked by title only: 6 for ACCP (2012-2022), 10 for CGS on OpenAlex. Since-2019 OpenAlex full-text search found no paper on BRD(v,5,λ) existence. Both Rosin papers are still v1 (arXiv API 2026-10-17). The NeurIPS 2025 workshop abstract does not mention BRD(26).",
 "significance": "already-known/corollary for existence. At most a modest result: an explicit, parent-checked certificate that independently confirms one case of a 2011 theorem, plus a correction to the open list's provenance. No spectrum consequence: per ACCP the λ∈{4,10,20} spectrum was already complete in 2011.",
 "caveats": ["ACCP evidence is abstract-level; the v=26 construction was not inspected", "The CGS exception table was not read", "Handbook V.4 not read", "Parent's distinct_columns=130 counts signed columns; whether the underlying 2-(26,5,4) design is simple (distinct supports) is unchecked"],
 "next_read_only_checks": ["Pin the author CGS PDF and run pdftotext -layout to recover the λ=4 exception table and the four-exception λ=4t theorem", "Get the ACCP body through legitimate institutional access to see the v=26 construction", "Parent to relabel the contract, README row and transitions entry ('the last CPro1-listed open BRD' / 'settles one explicitly listed finite existence case') as 'explicit witness for a case covered by ACCP 2011'"],
 "blocked": {"springer_pdf":"paywall, redirects to abstract", "ro.uow.edu.au/infopapers/313":"AWS WAF challenge", "sciencedirect S0012365X03000815":"403", "unsworks API":"403", "openreview":"browser check", "IA Scholar":"anti-scrape page", "citeseerx":"404", "google books API":"429", "r.jina.ai (tried once to get digits from the author PDF)":"401", "designtheory HCD_V_4.pdf":"404", "not retried per instruction":"ScienceDirect S0378375802002203, ResearchGate CGS preprint"},
 "read_scope": "Springer ACCP page; zbMATH 1229.05045 and 0997.05020 with their citing lists; OpenAlex cites lists for both papers; Crossref ACCP record; CPro1 problem_def, commits, BRD results directory and README, issues; arXiv API; pinned Rosin layouts; Dinitz 'New results in Part V' (last edited 2/15/18, no BRD entries); Nelson 2018 preprint; EJC 2011; Seberry 1994-04 publication list; CGS author PDF (digits lost). No files written, no contact made."
}
```

Two facts the parent can verify directly:
- The [Seberry publication list](https://documents.uow.edu.au/~jennie/94-04publications.html) links an author-hosted CGS 2002 PDF, a route not tried before.
- The [Nelson 2018 preprint](https://www.maths.usyd.edu.au/u/pubs/publist/preprints/2018/nelson-10.pdf) cites ACCP 2011 and CGS 2002 as "limited results … principally for designs with block sizes 4 or 5".
