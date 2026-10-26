# Primary-source comparison and Kuroki access gate v1

Before-creation clock observed: **2026-10-23T13:04:17-07:00**. This is a bounded source audit, not a novelty clearance. Scientific correctness and publication priority remain separate. No external contact, payment, account/config change, challenge bypass or model CLI occurred.

## 1. Candidate's exact interface

The candidate identifies delta=E[Y_(S_1)-Y_(S_0)] over arbitrary joint laws of binary S_0,S_1 and bounded real Y_0,Y_1 in [0,1]. It assumes treatment randomization and strong surrogacy Y_(t,s)=Y_s. Inputs are the **complete control-arm joint distribution** of S_0,Y_(S_0), q=P(S_1=1), and the **external causal mean gamma=E[Y_1-Y_0]**. It imposes no latent independence, individual monotonicity, rank invariance or outcome parametric family. It supplies sharp attainable endpoints, complete interval attainment and a sharp strict-positive-effect threshold.

## 2. Matched, actually read primary sources

### Yin–Liu–Geng–Luo

- Actual full source retained: [arXiv:1607.05454v1](https://arxiv.org/html/1607.05454v1), `sources/yin-1607.05454v1.html` and `.txt`.
- Read scope: binary-domain statement, randomized-treatment and strong-surrogate assumptions, data interface, Theorem 1 and its seven lower/upper terms, sharpness statement, Discussion's future continuous-Y sentence. The entire historical 16-type elimination was not independently authenticated.
- Exact match: same control joint law, treated surrogate marginal and external ACE(S->Y) input.
- Exact difference: its endpoint/potential outcomes are binary; the candidate allows all [0,1] potential outcomes and complete arbitrary factual distributions.
- Binary boundary: `proof-binary-reduction-v1.md` recovers all fourteen expressions directly. The operative `proof-bounded-outcome-sharp-bounds-ADDENDUM-1.md` proves conditional Bernoulliization preserves the entire attainable gamma/delta projection on binary factual data, without falsely identifying the underlying feasible-law sets.
- Publication metadata: [doi:10.1111/sjos.12398](https://doi.org/10.1111/sjos.12398), online 2019 / journal 2020. The publisher's full journal proof was not separately fetched.

### Hsiao–Tian–Parast, resilience 2025

- Actual primary source: [arXiv:2506.12194v1](https://arxiv.org/html/2506.12194v1), retained as `sources/surrogate-resilience-2506.12194v1.html` and `.txt`.
- Read scope: abstract, Introduction and §1.3.1 comparison to prior work, model description and objective.
- Its data interface has Study A with both surrogate and outcome observed in both arms and Study B with only the surrogate. It explores controlled deviations of conditional mean functions across studies and defines resilience probability/bound/set. The introduction explicitly distinguishes the more specific binary bounds of Yin et al. from sufficient-condition work.
- This accessed text does not give the candidate's unrestricted fixed-gamma, full-control-law identified set. This is a precise scope comparison, not a theorem that no section of any version contains an equivalent corollary.

### Hsiao–Tian–Parast, empirical assumptions 2025

- Actual author manuscript: [PMC12382359](https://pmc.ncbi.nlm.nih.gov/articles/PMC12382359/), doi:10.1080/10485252.2025.2498609, retained as `sources/surrogate-assumption-tests-PMC12382359.html` and `.txt`.
- Read scope: abstract, Introduction, model and the three sufficient assumptions.
- Its setting observes (Y,S) in both randomized arms, permits continuous S and discrete/continuous Y, and tests first-order stochastic dominance, conditional-mean monotonicity and nonnegative residual effects. These are sufficient assumptions; they are not imposed in the candidate's identified-set calculation. The paper describes Yin's bounds as binary-only.
- The continuous-S domain is broader in a different direction; no claim that the candidate dominates its inferential framework is made.

## 3. Kuroki 2013: authenticated facts versus unknown hypotheses

**Bibliographic identity:** Manabu Kuroki, *Sharp bounds on causal effects using a surrogate endpoint*, Statistics in Medicine 32(25), 4338–4347, online 11 June 2013; [doi:10.1002/sim.5873](https://doi.org/10.1002/sim.5873); [PMID 23754776](https://pubmed.ncbi.nlm.nih.gov/23754776/).

The [publisher-deposited Crossref abstract](https://api.crossref.org/works/10.1002/sim.5873) and the NCBI abstract were actually read. Crossref JSON is retained as `sources/kuroki-crossref.json`. They authenticate the following abstract-level interface:

> “derives closed-form formulas for the sharp bounds”

on treatment X's causal effect on true endpoint Y, using treatment's causal effect on surrogate S and the joint probability of S and Y, with unmeasured S–Y confounding, “under various assumptions.” The abstract separately mentions a monotonicity assumption between X and S for a null-effect testing statement.

That abstract is a serious overlap lead. It does **not** supply the following full-theorem facts, and this audit does not invent them:

| Model/interface item | Candidate | What Kuroki's accessed primary abstract establishes |
|---|---|---|
| Domain of X,S,Y and potential outcomes | Binary treatment/surrogate, arbitrary [0,1] outcomes | **UNKNOWN**; no full domain statement was accessed |
| Strong-surrogate exclusion | Y_(t,s)=Y_s | **UNKNOWN**; no exact graphical/potential-outcome assumption was accessed |
| Treatment randomization | Explicit | **UNKNOWN** at theorem level |
| Complete joint P(S,Y) is control-arm conditional | Explicit mu_s=P(S_0=s,Y_s in dy) | Abstract says joint probability of S,Y; **which regime/arm is UNKNOWN** |
| External gamma=ACE(S->Y) supplied | Explicit scalar equality | Not specified in the abstract; **presence/absence in full theorem UNKNOWN** |
| Individual monotonicity | Not assumed | Abstract mentions it for one null-testing result; **which bound theorems require it UNKNOWN** |
| Sharp attainable bounds | Both endpoints and full interval | Abstract explicitly claims closed-form sharp bounds; exact formulas and proof remain unread |
| Quantile/full-distribution formula or equivalent corollary | Explicit | **UNKNOWN** |

**Consequent status:** the exact Kuroki/theorem comparison is **ACCESS_BLOCKED / UNRESOLVED**, not “different model,” not “binary only,” not a cleared novelty gate and not evidence that the candidate is new. The candidate could be a corollary or overlap with this work. Mathematical derivation can be assessed independently, but a novelty/publishability promotion must not outrun this missing source.

### Legitimate access attempts actually made

1. Static publisher full article `/doi/full/10.1002/sim.5873`: HTTP403.
2. Publisher `/doi/epdf/10.1002/sim.5873`: HTTP403.
3. Publisher-deposited `/doi/pdf/10.1002/sim.5873`: HTTP403.
4. The exact Crossref-deposited TDM endpoint `https://api.wiley.com/onlinelibrary/tdm/v1/articles/10.1002%2Fsim.5873`: HTTP400 without a key; no credential acquisition or workaround attempted.
5. Normal managed Chromium navigation to the publisher full article: actual page displayed **“Performing security verification”** / Cloudflare, not article content. No challenge was solved or bypassed. The lane-owned tab `InfoKurokiPrimary` was released afterward.
6. OpenAlex DOI record: closed access, no OA URL and `any_repository_has_fulltext=false`; retained `sources/kuroki-openalex.json`. Metadata is not proof of global unavailability.
7. Semantic Scholar DOI API: `openAccessPdf` empty / CLOSED; retained `sources/kuroki-semantic-scholar.json`.
8. Europe PMC DOI lookup: `inPMC=N`, `inEPMC=N`, `hasPDF=N`; retained `sources/kuroki-europepmc.json`.
9. ORCID public author record 0000-0003-4219-351X: no researcher URLs.
10. Actual institutional profile [Yokohama National University](https://er-web.ynu.ac.jp/html/KUROKI_Manabu/en.html) was opened and retained. Its displayed selected publications do not provide this manuscript. Author/grant and institutional-repository searches produced no authenticated full-text copy in the results checked.
11. Exact-title/DOI and Japanese/English author-title searches repeatedly routed to the same abstract/metadata. Search misses are not a source-domain fact or priority evidence.

The precise missing prerequisite is **legitimately accessible full theorem text, including assumptions/data definitions and formulas, for Kuroki 2013**. No external contact or payment is authorized. The parent may supply a lawful local copy or a new reachable public route; no source is fabricated in its absence.

## 4. Other screens and calibrated claim

The current complete openai/math title/abstract catalog was retained and screened for surrogate, causal inference, partial identification and instrumental variable: no matching family. Receipt `sources/openai-math-causal-screen-v1.json` pins the catalog. This does not inspect every paper body and is not novelty certification.

**Defensible wording now:** “A complete candidate quantile-allocation derivation extends the already-known all-binary sharp-bound formula to arbitrary bounded real factual laws under the stated fixed-gamma model. A separate model has independently reconstructed the core proof with one minor baseline-domain clarification. Priority and the full Kuroki comparison remain unresolved.” It must not be called the first sharp continuous-outcome surrogate theorem, an accepted theorem, a general solution of causal inference, or a clinical recommendation.
