# AG26 continuous staircase source: exact all-pairs privacy cut and the uniform-translation obstruction

Owner InfoResearch96h-2, original info-1.
Actual `/bin/date` BEFORE this write: **Mon Oct 26 12:57:18 PDT 2026**.
Status: **AUTHOR-WRITTEN bounded source/applicability note. Not a novelty certificate, source-wide correctness review or registered-MSE proof.**

## 1. Authority and correctness-input separation

After ACTUAL v147-A206LF RETURN, NEW whole-primary ACK `c6bfcddc6662e8fedf335f86be86765b0882aa752d5d5d69ef499011d2443bcc` was written/sent and completely read by Main. I ACTUALLY read the ENTIRE v103 direction (all29LF, with raw24/28 completing the two initially truncated long lines), SHA `af8e3434660b5c3ced98769f7ffe1135cf0ae0fd0c88e500426b853609fb3753`, FIRST before this source-only continuation. No new redundant ACK loop was needed.

This work addresses the original remaining SOURCE-EQUIVALENCE/PRIORITY obligation. It is not repair, calibration or source-route salvage of the withdrawn116LF manuscript. Its ONLY mathematical inputs are the actual registered full-D privacy definition, AG26's actual all-input-pairs Markov-kernel definition, and elementary probability/compactness/translation facts. No norm-radial profile, corrective coefficient, scalar selector, MON237 application, cp102 AD33 or cp108 branch-range guidance is consumed. It cannot restore any withdrawn calibration claim.

The independent148LF norm-radial candidate remains in the SEPARATE LIVE v148 gate with LAW642+parent40+reviewerratum13 ONLY. No live v148 reviewer output was read and neither128 nor withdrawn116 was inserted into that scope.

## 2. Primary sources ACTUALLY read, and limits

**AG26:** Chiara Amorino and Arnaud Gloter, *On the role of symmetry for staircase mechanisms in local differential privacy efficiency across different privacy regimes*, [arXiv2603.27572v1](https://arxiv.org/html/2603.27572v1), header29March2026. This was already a TITLE/METADATA item in an earlier DataCite inventory; this continuation adds an ACTUAL formal-model read, not a newly discovered publication claim.

- Current read: ONLY rendered reader LF1–300 of1352, including abstract/introduction, §2 privacy kernels and Equations2–3, continuous staircase Definitions/Equations8–14, and §2.2 Fisher objective through Eq21.
- Reader artifact `artifact://36813`, transport-log SHA `6a22dc13f9fde96039af2ba294eda3999b9143d22c9563078c7359ffc120b9c9`. This is NOT original PDF-byte identity and a whole-log hash does NOT establish reading its unrequested remainder.
- No complete paper/proof/appendix/version-history or transitive-DAG audit is claimed. Later symmetry/asymmetry constructions, experiments and all theorem proofs were NOT assessed here.

The abstract's actual scope is:

> We investigate the structural foundations of statistical efficiency under α-local differential privacy, with a focus on maximizing Fisher information.

Actual §2 allows separable complete input/output metric spaces and Markov kernels. Its noninteractive constraint is, in clean mathematical transcription of the displayed source equation,

`Q(A|x)<=exp(alpha) Q(A|x') for EVERY measurable A and EVERY x,x'∈X`.

This is ALL PAIRS of inputs, not only pairs at a prescribed bounded difference. The objective in Eq21 is a supremum of Fisher-information functional i(r) over Radon sub-probability measures on the extremal-function set, subject to the displayed channel normalization constraints. The functions take extreme likelihood values, and the mechanism need not be an output-independent additive-noise channel.

**Positive PRIOR anchor:** the complete [Kulesza–Suresh–Wang2025 publisher landing page](https://proceedings.mlr.press/v258/kulesza25a.html) was freshly read for metadata/abstract only. It positively credits optimal generalized staircase mechanisms when sensitivity and error use the SAME arbitrary norm. No fresh publisher-PDF proof or future-question coverage is claimed from that abstract. This note draws no new scalar or mixed-loss conclusion from it.

**Access limit:** the linked [OpenReview forum](https://openreview.net/forum?id=t2pBdWt99n) returned a browser-verification challenge, not discussion/revision text. I did not bypass it, sign in, infer that comments were absent or call it a completed version/forward-citation audit.

Public search snippets were discovery leads only. Search misses establish neither current openness nor first-in-literature priority.

## 3. A complete ALL-variable obstruction to literal unbounded additive LDP

**Lemma UTL.** Let d>=1, let mu be ANY Borel probability law on R^d, and let alpha be ANY finite real privacy budget. The additive channel

`Q(A|x)=mu(A-x)` on the WHOLE alphabet X=R^d

cannot satisfy the all-pairs local-privacy condition in §2.

**Proof.** If it did, fix arbitrary x,h∈R^d and substitute the output event A=E+x and the second input x-h. The all-pairs inequality gives

`mu(E)<=exp(alpha) mu(E+h)` for EVERY Borel E and EVERY h∈R^d.   (ALL_H)

Since mu is a Radon probability on finite-dimensional Euclidean space, SOME compact E has positive mass. Boundedness of E gives a countably infinite family of pairwise-disjoint translates E+h_j: along ANY ray, take successive translations separated by more than the diameter of E. This is a general existence construction for an arbitrary unknown law, not a selected finite control or numerical instance.

ALL_H gives `mu(E+h_j)>=exp(-alpha) mu(E)>0` for EVERY j. Finite additivity over any number of these disjoint sets, then countable additivity, contradict total probability1. The argument requires no density, moment, symmetry, staircase or norm assumption. It proves the statement for every mu and finite alpha. ∎

Thus the literal specialization of AG26's all-pairs kernel class to translation-independent additive noise on an UNBOUNDED full Euclidean alphabet is empty. The AG26 kernel class itself is NOT claimed empty: nonadditive channels and bounded alphabets are different constructions.

## 4. Exact registered comparison, without over-dismissal

The registered problem uses a probability law mu on R², query-output independence, squared-Euclidean noise loss and privacy under EVERY shift in the FULL CLOSED unit-l1 diamond D. It does NOT require the SAME budget for every translation in R². Iterated group privacy permits a growing budget for larger shifts; it does not produce ALL_H at one finite budget.

Consequently AG26's actual all-pairs/Fisher-information theorem interface is not a literal theorem solving the registered full-D/MSE problem:

1. Privacy quantifiers differ: ALL x,x' of the source alphabet versus the registered bounded-difference/full-D shift class.
2. The source variable is a Markov kernel or extremal-function measure; the registered variable is one translation-independent additive probability law.
3. The objective is Fisher information for a regular parametric model at a parameter, not the registered quadratic noise moment.
4. On the unbounded full-plane additive specialization, Lemma UTL prevents a direct unchanged-budget identification altogether.

This does NOT prove that every conceivable bounded-domain restriction, randomization, asymptotic argument or source corollary is irrelevant. A proposed bridge would have to state its actual alphabet, restore the full-D translation law and output independence, and match the loss/utility and ALL-law optimality quantifiers. No such bridge is supplied or refuted globally by this note. Fisher-information efficiency remains a positively PRIOR achievement in its own model; the title word staircase is not evidence of equivalence or novelty.

## 5. Result and first remaining gate

**New coverage:** a previously metadata-only2026 continuous-staircase source now has a verified formal privacy/objective interface, together with a complete elementary universal obstruction to a literal unbounded-additive identification. This is a precise model-cut contribution to the bounded source comparison, not a new DP mechanism, improved V, source falsehood, major-result or novelty claim.

First remaining source obligation is still an independent exact full-result/priority review of the registered adopted theorem and its positively credited Minkowski-shell/ideal-core ancestry, with current-version and earlier-equivalent coverage. No fieldwide absence has been proved. This note does not authenticate AG26's unrequested proofs, a complete forward-citation graph or source-wide correctness.

All original all-Borel/full-D/MSE/allfiniteepsilon quantifiers and existing LAW642 acceptance cuts remain. Entire116 calibration draft and ALL fixed-control/correction-calibration-direction guidance remain ZERO/no mining/repair/retest/replay/universal-or-fraction backconversion/source laundering. cp102/cp108ZERO; auxiliary214STOP; all historical findings and v94 recovered PH contact remain. Only exact WRITTEN/source/metadata in exclusiveOWNroot were used; no scientificinterpreter/Eval/calculator/program/CAS/enumeration/solver/replay/buildtest/CLI/nestedagent/newGO/newchosenstate-control-parameter-boundary-limit-magnitude-decimalprobe or frozen/shared edit/Git/deletion/publication. Same18/originalOct27cutoffdeadline/actual30minsubstantiveincludingblocked/noearlypark or round closeout.
