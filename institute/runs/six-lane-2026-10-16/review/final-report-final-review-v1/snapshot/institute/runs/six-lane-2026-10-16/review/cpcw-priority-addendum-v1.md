# CPCW gate — priority addendum: an earlier public claim exists

Recorded 2026-10-17 (PT) after a new-surface priority audit ([scout report](info-prior-gap-audit-v1.md)). The original [verdict](cpcw-optimal-parent-verdict.md) is unchanged; this addendum supersedes only its priority and gate status.

**Earlier claim (read directly by the parent in DataCite):** Reynout Vos (independent researcher, RAIV.nl), *Resolving the Remaining Open CPCW Cases for k = 5 and k = 6: Nine Explicit Optimal Constructions*, Zenodo technical note, [doi:10.5281/zenodo.22076107](https://doi.org/10.5281/zenodo.22076107) (version of concept 10.5281/zenodo.22068088). Issued 2026-08-24; registered 2026-08-24T17:43:47Z, about 54 days before this run's CPCW contract froze. It lists OpenAI and Anthropic (Claude) as contributors. The abstract gives explicit base blocks for all nine Baicheva–Topalova cases, (122,123,124,126;6,1) and (143,144,146,162,167;5,1), which includes all eight cases we froze.

**Parent check of the earlier codes:** from the DataCite abstract, the parent parsed all nine codes and checked them exactly. Every block has k distinct elements, all directed differences mod v are distinct, and every block count equals the difference bound ⌊(v−1)/(k(k−1))⌋. So all nine codes are valid and meet the bound we used for optimality. The Zenodo files and Vos's verifier returned HTTP 403 and were not read. The scout notes that some of our codes have different leaves (e.g. 123), so ours are independent constructions rather than copies.

**Why the run missed it:** Vos's record deposits no references, so citation sweeps cannot see it. OpenAlex indexes the concept DOI under its first-version title (case 122 only). Only DataCite full-text and related-identifier search finds it.

**Status:** CORRECTNESS-ACCEPTED (unchanged: explicit codes, four verifier routes, parent byte-exact rebuilds, parent-replayed Lean kernel proofs of existence and optimality). **PRIOR-CLAIM; no longer counted as a contract gate.** Our work is an independent, kernel-checked confirmation of a claim that was already public.
