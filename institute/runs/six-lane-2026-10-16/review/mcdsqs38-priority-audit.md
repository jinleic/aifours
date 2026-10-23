# mcDSQS(38): bounded priority audit

## Verdict

**NO-PRIOR-FOUND-IN-BOUNDED-SEARCH for the mcDSQS(38) property, with a prior-object caveat.** The read-only scout `McDsqs38Priority` found no accessible source that constructs an mcDSQS(38) or proves one impossible. The scout's search and readings are its evidence, retained at `agent://McDsqs38Priority`; this file records them with the parent's own confirmation of the prior-object finding.

**The underlying SQS(38) is already published.** The pinned certificate's block set is isomorphic to record 143 (of 1,547) in the SQS(38) dataset of Kiermaier–Krčadinac–Wassermann ([Zenodo 10.5281/zenodo.17153238](https://doi.org/10.5281/zenodo.17153238), file `3-38-4-1.des.gz`, registered 2025-09-18 per DataCite). The parent confirmed this independently from the dataset bytes:

- dataset SHA-256 `715ab56db350e4eade13b3f1b84df9a0108f4f2670dc41115adafcbcdda17b25`; 1,547 records parsed;
- record 143 is an SQS(38) (2,109 distinct blocks, all 8,436 triples once);
- the explicit map i ↦ i−1 (i odd), i ↦ (21−i) mod 38 (i even), from 1-based dataset points to certificate points, is a bijection and maps the record's block set exactly onto the certificate's;
- the record's three listed automorphism generators preserve it and generate a group of order 342 by closure.

Receipt: [parent isomorphism check](mcdsqs38-dataset-isomorphism-v1/parent-result.json), driver [mcdsqs38_dataset_isomorphism_check.py](mcdsqs38_dataset_isomorphism_check.py); the extracted record is retained there. That the listed group is the full automorphism group is the dataset authors' claim (computed with nauty/Traces), not re-proved here.

KKW's paper ([arXiv:2509.23483v1](https://arxiv.org/abs/2509.23483v1), Table 1, p.4: "38 4 2109 ≥1547 3 3") and dataset make no colouring, resolvability, chromatic-index or Hanani claims. **The contribution is therefore the explicit, verified 19-colourings of all 38 derived STS(37) of an already-published SQS(38), not a new design.**

## Open statements and consequences

- Latest explicit open statement: Tan–Zhou, arXiv:2503.11934v1 §4(1): "Find more examples of mcDSQS(v)s, for example, an mcDSQS(38) and an RDSQS(52) (the smallest unknown mcDSQS(6n + 2)s …)". Its journal version (DCC 93:4117–4140, 2025) body is paywalled; only the abstract was compared.
- Older related conjecture, missed by the earlier RDSQS(52) audit: Shi–Xia–Krotov, [arXiv:2212.00048v2](https://arxiv.org/abs/2212.00048v2), Conjecture 2 (p.21): "If 20 ≤ n ≡ 2 mod 6, then there is an SQS(n) such that all its derived STS have chromatic number n/2 … (equivalently, q0′(3, 4, n) = n/2 + 1)." Their Proposition 3 covers only n = 14 and n = 20. The certificate settles the n = 38 case of this conjecture; the conjecture itself remains open.
- Stated consequence, Tan–Zhou Corollary 1.4(1): "For n ≡ 2 (mod 6) and n ≥ 20, if there exists an mcDSQS(n), then q0′(3, 4, n) = n/2 + 1." Hypotheses hold at n = 38, so q′₀(3,4,38) = 20 for the source's diameter-perfect constant-weight code problem. Theorem 1.3 ([16, Theorem 5]) also gives the converse.
- [INFERENCE, scout derivation] No new order or infinite family follows through Tan–Zhou's recursive constructions without ingredients not known to exist (e.g. gcDCQS(36ⁿ:2), gcDCQS(38ⁿ:0)); no LKTS/OLKTS consequence. The smallest mcDSQS(6n+2) order not covered by the sources read becomes 44.

## Sources read by the scout

- Tan–Zhou local arXiv v1 text and Springer abstract; Shi–Xia–Krotov v2 full text; KKW arXiv v1, dataset and DataCite metadata.
- Full-text searches of arXiv 2512.22754, 2510.24132, 2602.16319, 2505.23881, 2503.15116, 2610.13852 and local Wang 2607.21521: no mention of mcDSQS, minimum colourable, q0′(3,4,38) or mcDSQS(38).
- OpenAlex citations (Shi–Xia–Krotov 5, Tan–Zhou 1, KKW 0) and Semantic Scholar (7, 3, 1): nothing relevant.
- arXiv API since 2023 and OpenAlex text searches for Hanani triple systems, partial parallel classes, diameter perfect, Steiner quadruple, mcDSQS, SQS(38): nothing beyond Tan–Zhou.

## Access holes

Tan–Zhou and tilings journal bodies (paywalled); Google Scholar, MathSciNet, CNKI and Chinese theses not searched; later versions of the KKW dataset (concept DOI 10.5281/zenodo.17153237) not checked; Zenodo web pages returned 403, though the file downloaded.

## Calibrated significance

A single-order result: it answers the first example in Tan–Zhou §4(1) and the n = 38 case of Shi–Xia–Krotov Conjecture 2, fixing q′₀(3,4,38) = 20, by certifying colourings of a design published in September 2025. Modest specialist significance; no family, no new design, and a search miss is not priority.
