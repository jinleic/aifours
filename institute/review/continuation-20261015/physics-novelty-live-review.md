**1. Verdict: PRIOR-ART-FOUND**

Earlier sources claim the small-k 1RSB upper bound, and an earlier public Lean development covers general k. **Priority for your explicit certified constants remains unestablished.**

| Audit question | Result |
|---|---|
| **(a)** Earlier rigorous-bound publication or claim below the classical comparison values | **PRIOR-ART-FOUND at the claim/variational-bound level.** This does not establish certified accuracy of the printed numerical values. |
| **(b)** Earlier explicit rational/interval evaluation for k=4 or 5 | **NONE-FOUND-IN-CHECKED-SOURCES.** |
| **(c)** Earlier Lean/Coq/Isabelle formalization covering k≥4 upper bounds | **PRIOR-ART-FOUND:** general-k Lean source exists. No earlier formal certification of your particular constants was located. |

This positions the supplied claims; it does not assess their correctness.

**2. Findings**

**Mertens–Mézard–Zecchina: an earlier upper-bound claim, with uncertified numerical estimates.**  
Version: [arXiv cs/0309020v2](https://arxiv.org/pdf/cs/0309020v2), 24 February 2005; journal publication 2006.

> “is an upper bound to the true threshold values”

The introduction applies this statement to even K. Table 1 reports 9.931 for k=4 and 21.117 for k=5; Figure 4 separately reports a k=4 regression root of 9.9324. Section 5.3 describes population dynamics, empirical averages and statistical error estimates. **Stance:** counter to claiming the first sub-classical 4-SAT upper-bound principle or prediction; no certified decimal endpoint established by the passages checked. **Read scope:** introduction, §5.3, Table 1, Figure 4, numerical uncertainty discussion and selected expansion/conclusion passages. [Primary text](https://arxiv.org/pdf/cs/0309020v2)

**Chatterjee et al.: a particularly relevant modern statement covering small k.**  
Version: [arXiv 2506.01359v2](https://arxiv.org/html/2506.01359v2), 18 November 2025.

> “turns the physics prediction into a rigorous upper bound”

Section 2.6 explicitly says interpolation verifies an upper bound matching the 1RSB prediction for small k, then discusses k=3,4,5. Table 1 prints degree parameters 39.724 and 105.585; because the model uses Poisson(dn/k) clauses, these correspond to clause densities **9.931 and 21.117**. That conversion is arithmetic, not an additional theorem. The table labels these values as physics predictions; the checked text supplies no outward-rounded certificate for those decimals. **Stance:** directly relevant prior claim for **(a)**; not evidence resolving **(b)**. **Read scope:** model, introduction, Table 1, §2.1 and §2.6. Its clause law matches yours; fixed-count comparison additionally requires transfer from the Poisson count. [Primary text](https://arxiv.org/html/2506.01359v2)

**Achlioptas–Menchaca-Méndez: the full 2012 paper is accessible.**  
Version: ICALP 2012, pp. 1–12.

> “truncating an infinite sum to a finite one”

The paper already develops computationally tractable rigorous energetic bounds. Its initial clause model matches iid uniform legal signed clauses. Section 7 gives an explicit Poisson-sum evaluation procedure for general k-SAT, but I located no evaluated 4-SAT/5-SAT endpoint in the checked sections. **Stance:** substantial methodological and computational antecedent; no competing constants located. **Read scope:** model, motivating results, §3.1 and §7. This closes the earlier author-PDF access hole. [Author PDF](https://cgi.di.uoa.gr/~optas/papers/Energetic.pdf)

**Menchaca-Méndez’s thesis: accessible, with relevant unsuccessful extension work.**  
Version: March 2013 dissertation.

> “we could not find a convex combination that would give better bounds”

Section 3.4 derives a rigorously truncatable energetic calculation. Section 5.1 discusses convex combinations of independent models and their relation to 1RSB bounds, reporting no improved combination. No explicit near-cavity k=4/5 certificate was located in the checked passages. **Stance:** important antecedent, without a located numerical priority conflict. **Read scope:** contents, model, and targeted passages in §§2.2, 3.4, 4.1 and 5.1. This closes the earlier thesis access hole. [Institutional thesis PDF](https://escholarship.org/content/qt6kk446qh/qt6kk446qh.pdf?t=mmfaj6)

**The underlying interpolation framework—including the odd-arity route—is established prior work.**

| Source/version | Short quotation | Stance and read scope |
|---|---|---|
| Franz–Leone, arXiv v1, 14 August 2002; journal 2003 | “In the case of K-SAT the replica method thus gives upper bounds of the satisfiability threshold.” | Prior framework; the text restricts its proof to even arity. Read abstract, model and general strategy. [PDF](https://arxiv.org/pdf/cond-mat/0208280) |
| Panchenko–Talagrand, arXiv v1, 18 May 2004 | “Let p ≥ 2 be an even integer” | Prior general principle; this source alone does not establish the odd-arity extension. Read introduction/model and bound statements. [PDF](https://arxiv.org/pdf/math/0405357) |
| Lelarge–Oulamara, v2, 17 January 2018 | “new bounds for the size of the largest independent set” | Condition (4) allows even arity **or nonnegative factors**, relevant to odd SAT arity. Its explicit numerical application is another model. Read model conditions, comparison argument and numerical-application scope. [HTML](https://arxiv.org/html/1708.02457v2) |

**Post-2010 tables require careful interpretation.**  
Duffy–Bordenave–Leith’s 2013 paper separates:

> “Theory bounds:”  
> “Estimated:”

Its Table I lists **10.23/21.33** in the theoretical upper-bound row and **9.93/21.12** as estimates. **Stance:** supports the historical distinction between classical explicit bounds and cavity estimates; it cannot establish the 2026 best-known bound. **Read scope:** Table I and adjacent model/comparison discussion. The institution identifies the publication as 2013. [Paper](https://mural.maynoothuniversity.ie/6218/1/KD-Decentralized.pdf), [institutional record](https://mural.maynoothuniversity.ie/id/eprint/6218/)

Achlioptas’s older handbook chapter similarly captions its table:

> “Best known rigorous bounds”

It lists 10.23 and 21.33 and attributes the general upper-bound sharpening to Dubois–Boufkhad and Kirousis et al. **Stance:** historical baseline only. **Read scope:** model, Theorem 3, Table 8.1 and attribution paragraphs. [Author manuscript](https://cgi.di.uoa.gr/~optas/papers/handbook.pdf)

**Vorobyev: close certificate/formalization antecedent, explicitly k=3.**  
Version: [arXiv 2610.10599v1](https://arxiv.org/html/2610.10599v1), 6 October 2026; the inspected arXiv history lists only v1.

> “The proof is formalized in Lean 4.”

The pinned development exposes the 1067/250 endpoint and a three-literal model. No k=4/5 extension was located in the inspected public material. **Stance:** essential attribution, without a located competing endpoint. **Read scope:** paper/model/certificate/formalization descriptions, repository README, and pinned `Model.lean`/`Threshold.lean`. The repository page showed zero forks; the open-issues page showed zero open issues, subject to the access limitations below. [Pinned source](https://github.com/yamelton/sat-upper-4268/tree/87fb64825b24159418aa0cdca830a76a9d85ff84), [issues](https://github.com/yamelton/sat-upper-4268/issues)

**OpenAI’s October 2026 collection: additional general-k Lean prior art.**  
Version: initial snapshot `adc7f1241b42e322a6451854ab7e4b4c146bf78a`; collection announced **6 October 2026**.

> “theorem supercritical_limit”

Actual implementation source—not merely a challenge statement—contains a general-k unsatisfiability limit, threshold existence for k≥3, and a coarse bound `limitingCenter k ≤ 2^k + 1`. The documented model uses iid legal clauses with distinct variables and fair signs. **Stance:** a direct obstacle to “first formalization of random k-SAT upper bounds for k≥4”; no competing near-cavity constants located. **Read scope:** pinned scope document, challenge/configuration and implementation `Main.lean`; no build or dependency audit performed. [Pinned implementation](https://raw.githubusercontent.com/openai/math/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Probability/RandomSAT/Main.lean), [scope](https://raw.githubusercontent.com/openai/math/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/235.md), [dated announcement](https://openai.com/index/sharing-ai-progress-in-mathematics/)

**Other requested lines supplied context, without a located competing certificate.**

- **Kirousis et al., 1998:** the abstract says its technique “generalizes in a straightforward manner”; the reported calculations concern 3-SAT. **Scope:** publisher abstract, not full proof. [Publisher](https://onlinelibrary.wiley.com/doi/10.1002/%28SICI%291098-2418%28199805%2912%3A3%3C253%3A%3AAID-RSA3%3E3.0.CO%3B2-U)
- **Díaz et al., arXiv v1, 23 July 2008:** “at least 4.4898” concerns 3-CNF. **Scope:** abstract and opening/model passages. [PDF](https://arxiv.org/pdf/0807.3600)
- **Coja-Oghlan–Panagiotou, 2012/2013 preprints:** asymptotic bounds contain k-dependent error terms; these do not themselves supply numerical k=4/5 certificates. **Scope:** introductions and main statements. [Going after the threshold](https://arxiv.org/pdf/1212.1682), [asymptotic threshold](https://arxiv.org/pdf/1310.2728)
- **Ding–Sly–Sun:** “with \(k_0\) an absolute constant”; the stated result is for sufficiently large k. **Scope:** abstract/main-result framing. [Paper](https://arxiv.org/pdf/1411.0650)
- **Nike Sun, ICM 2026:** “we also focus here on this regime” refers to large k. The full survey is now accessible; its principal exposition concerns random regular NAE-SAT. **Scope:** introduction and §2; no competing k=4/5 certification located. [Full survey](https://epubs.siam.org/doi/full/10.1137/25M1805801)
- **Carenini, ECCC TR26-229, 5 October 2026:** “this establishes the satisfiability conjecture” is a threshold-existence claim, without explicit k=4/5 values in the abstract. **Scope:** abstract only; the earlier TR26-145 introduction concerns window width. [TR26-229](https://eccc.weizmann.ac.il/report/2026/229/), [TR26-145](https://eccc.weizmann.ac.il/report/2026/145/download/)

**3. Access holes**

- **Citation graphs:** OpenAlex, Semantic Scholar and Crossref API requests failed to fetch; direct runtime attempts also failed. Forward traversal therefore relied on indexed citations and primary-paper references, not a complete API citation graph.
- **Antonopoulou, 2020**, *Kolmogorov complexity based upper bounds for the unsatisfiability threshold of random k-SAT*: publisher abstract accessible; full text unavailable. This remains a relevant numerical-comparison hole. [Publisher abstract](https://www.tandfonline.com/doi/abs/10.1080/09720529.2020.1711602)
- The **2021 handbook chapter**, complete **Kaporis** article, full **Kirousis 1998** proof, and **TR26-229 PDF** were not successfully inspected. The older handbook and other checked passages cannot substitute for them.
- Complete GitHub commit histories, closed-issue searches and fork-network enumeration were unavailable. No external Lean development was compiled during this audit.

**4. Strongest defensible wording**

**Claim 1:**

> We provide explicit finite rational certificates for whp unsatisfiability of standard random 4-SAT at 3973/400 and 5-SAT at 8447/400, within the established 1RSB interpolation framework. Earlier work already supplies the variational upper-bound principle and nearby numerical predictions. We located no earlier certification of these endpoints in the sources checked; priority remains unresolved.

Position its prospective significance as **reproducible numerical certification near established cavity predictions**. Avoid “first sub-classical upper bounds,” “new interpolation method,” or an established global record.

**Claim 2:**

> We generalize Vorobyev’s k=3 energetic Lean development to a general-arity criterion with finite weighted warning laws, instantiated at 9.96 for k=4 and 21.14 for k=5. The improved written-proof constants 9.9325 and 21.1175 are not yet formally certified in this development.

The plausible contribution is the **formalized interpolation criterion and explicit small-k certificates**. A broad first k≥4 formalization claim is unsupported.

A search miss does not prove novelty, and this model audit is not peer review. No files were changed and no delegation was used.