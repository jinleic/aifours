# Shor continuation — actual primary-source check

Before-creation clock observed: 2026-10-22T23:05:11-0700. These are actual reader/browser observations during this round, not a comprehensive literature search or proof audit.

## Authenticated alternate statement

Cordero, _Factorizations of Cyclic Groups and Bayonet Codes_, arXiv2301.13566v1 (posted2023-01-31), Lemma5.2 was read in:

- [Official HTML](https://arxiv.org/html/2301.13566v1#S5.Thmtheorem2), including the exact MathML inequality signs;
- [Author-hosted manuscript](https://www.normalesup.org/~cordero/Publications/Factorizations_and_Bayonet_Codes.pdf), printed p.17;
- Existing retained `../sources/cordero2023.txt` LF815–817, SHA256 `c2cc3649b9b9ad36a3b563b2a9c88fca7bc07406e43263cb44f43afa75e57f86`.

Statement, paraphrased: for a normalized cyclic direct factorization, if one factor's cardinality has at most two distinct prime divisors, at least one factor generates a proper subgroup. The completion application has n≥20, so no trivial-group case is used. The lemma explicitly cites Szabó–Sands2009 Theorem5.5. That book's proof was not obtained/read: this is an authenticated theorem statement, not independent proof verification. The author page lists the paper in _Journal of Automata, Languages and Combinatorics_,2023; the opened manuscript itself is dated2022-11-20. These dates are not conflated.

Other actual source reads included Cordero definitions of n-cbc/compatibility/stability, the prime-power-border theorem and its proof, and the prefix-suffix consequence. They are contextual reads; the new order derivation uses only Lemma5.2 from this source, plus the dossier's written bridge/multiplier/8-divisibility interfaces. No general Hajós or factorization conjecture is assumed.

## Szabó2006 remains unverified

[Crossref DOI record](https://doi.org/10.1016/j.tcs.2006.02.002) confirms Sándor Szabó, _Completing codes and the Rédei property of groups_, _Theoretical Computer Science_359(1–3),449–454, August2006. It supplies no abstract or theorem body. Actual attempts:

| Endpoint | Observed outcome |
|---|---|
| [Recorded author-uploaded PDF](https://www.researchgate.net/profile/Sandor-Szabo-6/publication/220149955_Completing_codes_and_the_Redei_property_of_groups/links/61ca1e78da5d105e55ff8a32/Completing-codes-and-the-Redei-property-of-groups.pdf) | HTTP403 |
| [ResearchGate article](https://www.researchgate.net/publication/220149955_Completing_codes_and_the_Redei_property_of_groups) | HTTP403 |
| [ScienceDirect article](https://www.sciencedirect.com/science/article/pii/S0304397506001277) | HTTP403 in reader |
| [Publisher PDF indexed by OpenAlex](https://www.sciencedirect.com/science/article/pii/S0304397506001277/pdf) | HTTP403 |
| [Crossref-deposited text endpoint](https://api.elsevier.com/content/article/PII:S0304397506001277?httpAccept=text/plain) | HTTP400 |
| [Linkinghub primary link](https://linkinghub.elsevier.com/retrieve/pii/S0304397506001277) | Redirect shell only |
| Dedicated managed-browser navigation to the actual ScienceDirect article | “Just a moment...” page; no article text |

The browser open and close calls each reported a display-bridge TypeError after side effects. The actual tab was inspected via the browser helper, then closed; the final managed-tab list was empty. No challenge bypass, account login, credential change, purchase or contact was attempted. Browser navigation used eval only as a tool transport, not for mathematical computation.

OpenAlex's actual record reports no repository fulltext and points to that same publisher PDF. Exact-title/DOI web searches returned irrelevant results; those are not evidence that no other copy exists. The2009 monograph DOI likewise supplied metadata only. Thus the original requested2006 theorem/proof authentication remains BLOCKED, not silently completed by the alternate route.

## Status and novelty boundary

The local openai/math docs/preprint keyword screen found no target-relevant match; unrelated occurrences of “finite completion” were discarded. The opened2019/2022/2023 source texts did not contain the numeric strings19800/9900 in the bounded search, but this is not a novelty certificate. The old dossier's conditional statements already imply the same order restriction if their source premise holds. The contribution of this round is a more defensible citation/derivation path and explicit structural restatement, not a claim of a new mathematical bound.
