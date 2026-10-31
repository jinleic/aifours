## Summary

- **Suzuki: the imported order and maximal-subgroup statements support the candidate’s argument for every \(q=2^{2m+1}\), \(m\ge1\).** I found no omitted maximal type or parameter exception that defeats the full-\(2\)-part comparison. The conclusion remains conditional on the named **Sun5 statement** and classical classification.
- **Demonstrated prior project overlap:** the earlier final report already records arbitrary-group Sun6 and Sun7 statements. Thus the candidate’s Suzuki Sun6/Sun7 conclusions are not new relative to those recorded internal statements. I did **not** locate an earlier accepted all-parameter Suzuki **Sun8** exclusion in the screened parent reports.
- **Public overlap exists, but for a different conjecture:** Garonzi–Margolis prove the **Herzog–Schönheim coset-partition conjecture** for all simple groups, explicitly including Suzuki and small Ree families. That is not the candidate’s assertion about arbitrary disjoint six/seven/eight cosets.
- **`PRIORITY_UNKNOWN`** for the Suzuki Sun8 family result and its particular short derivation. Search misses do not establish novelty.
- **Separate small-Ree scope:** its order/maximal-type/\(3\)-part argument also matches the inspected sources. I independently confirmed the disputed **2025 HTML order formula**, including its raw MathML/TeX annotation; the candidate correctly does not use that formula.

## 1. Suzuki: exact source comparison

### Sources actually inspected

Héthelyi–Horváth–Petényi, *The depth of subgroups of Suzuki groups*, arXiv:1404.1523v1:

- [§2, “The Suzuki groups”](https://arxiv.org/html/1404.1523v1#S2): parameter domain, exceptional \(Sz(2)\), group order, Sylow-2 order, point stabilizer and dihedral normalizer.
- [§3, Theorem 3.1](https://arxiv.org/html/1404.1523v1#S3.Thmtheorem1): subgroup types and orders.
- [§4, Theorem 4.1](https://arxiv.org/html/1404.1523v1#S4.Thmtheorem1): **part (a) explicitly identifies the exhaustive maximal-subgroup representatives**. I also read the rest of the theorem, not its subsequent depth proofs.
- [References](https://arxiv.org/html/1404.1523v1#bib.bib11): the direct §3 proof references are **Lüneburg, Theorem 4.12**, and **Huppert–Blackburn III, Chapter XI, Theorem 3.10**. Theorem 3.1 itself is labelled “Suzuki.”

Theorem 3.1 alone says that the groups listed exist; **Theorem 4.1(a) supplies the explicit maximal-list exhaustiveness needed by the candidate.**

### Parameters and every maximal type

The source uses \(r=2^m\); the candidate’s \(\theta=2^{m+1}\) is exactly \(2r\).

| Item | Inspected source statement | Candidate comparison |
|---|---|---|
| Ambient group | \(q=2^{2m+1}\), positive integer \(m\) | Exact match: \(q\ge8\). |
| Exceptional ambient case | \(Sz(2)\) is a nonsimple Frobenius group of order \(20\) | Correctly excluded at candidate line 16. |
| Group order | \(|Sz(q)|=q^2(q^2+1)(q-1)\) | Exact match. Since the last two factors are odd, \(|G|_2=q^2\). |
| Sylow-2 normalizer \(N_G(F)=FH\) | Order \(q^2(q-1)\) | Candidate \(B\); \(2\)-part \(q^2\), index \(q^2+1\). |
| Dihedral \(N_G(H)\) | Order \(2(q-1)\) | Exact match; \(2\)-part \(2\), not \(4\). |
| First torus normalizer \(N_G(A_1)\) | Order \(4(q+2r+1)\) | Exact match; \(2\)-part \(4\). |
| Second torus normalizer \(N_G(A_2)\) | Order \(4(q-2r+1)\) | Exact match; \(2\)-part \(4\). |
| Subfield Suzuki subgroup | \(Sz(s)\), \(s\) an odd power of \(2\), \(s\ge8\); maximal subfield choices in Theorem 4.1(a) | Candidate considers the broader set of all proper \(q=s^t,\ t>1\). This is harmless over-inclusion for the exclusion argument: \(|Sz(s)|_2=s^2<q^2\). |

**Subfield qualification:** the candidate does not reproduce the exact maximality restriction on the extension degree. Maximal proper subfields have prime relative degree; the source phrases this as maximal \(s\). The proof only needs an exhaustive containing list and a strict \(2\)-part bound, so considering all proper subfield Suzuki groups does not introduce a gap.

### Boundary checks

- At the smallest allowed field, \(q=8\):
  \[
  |G|=29120,\quad |G|_2=64;
  \]
  the four nonsubfield maximal orders are \(448,14,52,20\), with \(2\)-parts \(64,2,4,4\). There is no proper subfield \(s\ge8\). The claimed divisor is \(65\).
- The proof’s strict inequality \(q^2>4\) holds throughout its stated domain.
- An exceptional subgroup \(Sz(2)\), if conservatively included as an additional possible containing subgroup, would have \(2\)-part \(4\), so it could not undermine this full-Sylow-2 exclusion.
- For every allowed \(q\), \(q\equiv-1\pmod3\), giving \(3\nmid q^2(q^2+1)(q-1)\), exactly as used.

### Does the source support the actual coset implication?

**Yes, at the named imports.** The following is a written deduction from the inspected statements, not a theorem attributed to the 2014 paper:

1. Every proper odd-index \(H<G\) has full \(2\)-part \(q^2\).
2. A maximal subgroup containing \(H\) must therefore be a conjugate of \(B\); all other listed types have insufficient \(2\)-part.
3. Consequently \(q^2+1\mid[G:H]\).
4. In a proposed Sun6/7/8 counterconfiguration, five even indices would contradict Sun5: their pairwise gcds would have to lie in \(\{2,4\}\), since they are at most \(7\) and not divisible by \(3\).
5. Hence at most four indices are even. At least two are odd, and their gcd is at least \(q^2+1\ge65\).

This applies to **all actual proper subgroups**, not just maximal subgroups or a selected normalizer list. It does not require different subgroups to contain the same Sylow subgroup.

**Citation precision:** candidate line 14’s description of §3’s ancestry should be read with the exact references above: Lüneburg and Huppert–Blackburn are the direct cited proof sources. I did not inspect their proofs or Suzuki’s original classification proof.

## 2. Prior project records checked

Paths below are relative to `/Users/jinleic/repos/aifours`.

| Record and relevant lines | What it establishes for this screen |
|---|---|
| `mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/frontier-20261028-suzuki-simple-family-v1.md:1-74` | Entire assigned candidate read, including named imports, proof, quoted experiment and limits. |
| `institute/runs/three-area-2026-10-23-96h/final-report-v2.md:256-265` | Prior math-6 summary: accepted SL/PSL and Sp/PSp families; direct-P7 bounded existence; later Ree and other leads do not inherit those verdicts. |
| `institute/runs/three-area-2026-10-23-96h/sun-entire-all-ranks-SL-PSL-two-route-parent-v1.md:9-18,54-62` | Entire returned parent report inspected. Its family statement is SL/PSL, with other Lie types explicitly outside its conclusion. |
| `institute/runs/three-area-2026-10-23-96h/sun-Sp6-Sp8-and-all-symplectic-entire-parent-v1.md:3,35,39-49` | Entire parent report inspected. Its conclusion is Sp/PSp. “Suzuki” at line 35 is part of classical proof ancestry, **not an adopted \(Sz(q)\) coset-family theorem**. |
| `institute/runs/three-area-2026-10-23-96h/sun-rank-free-P7-bounded-simple-existence-entire-parent-v1.md:5-13,45-63` | Entire parent report inspected. It gives conditional bounded simple-factor existence, not Suzuki/Ree exclusion or a Sun8-to-P7 reduction. |
| `institute/runs/six-lane-2026-10-18-96h/report/continuation-report-2026-10-22-final-v17.md:38-57` | Explicit recorded arbitrary-group Sun7 statement; line 44 also identifies the operative written all-group Sun5/6 statements. This is demonstrated statement-level overlap with Suzuki Sun6/Sun7. |
| `institute/runs/six-lane-2026-10-18-96h/report/sun-named-historical-results-v1.md:1-21` | Keyword/scope inspection of historical result summaries; no Suzuki family gate identified. Historical/computational boundaries remain qualified. |

I additionally performed filename discovery of prior Sun parent records and targeted content searches in the above admitted report corpus using **Suzuki, Sz, 2B2 / \(2B_2\), Ree**, and subgroup/index terminology.

**Limits of the repository conclusion:** this was a bounded report-level ancestry screen, not a complete proof-DAG or repository-history audit. I did not open the older held/unreviewed Ree payloads or other quarantined candidates. Their exact individual contents/statuses were not reconstructed.

**Important non-overlap:** a theorem for \(SL_4(q)\) or \(Sp_4(q)\) does not automatically give the same Sun bound for its Suzuki subgroup. Viewing subgroup cosets in a larger ambient group multiplies every index by the ambient index; the required gcd threshold is not thereby preserved.

## 3. Public priority screen and demonstrated related work

Searches used the requested alternative names, both with the Sun terminology and with **“disjoint cosets,” “gcd,” “indices,” “harmonic subgroups,”** and six/seven/eight variants. Narrow searches were broadened or retried under alternative notation when they returned no relevant result.

| Public source inspected | Demonstrated scope | Relation to candidate |
|---|---|---|
| [Zhu, arXiv:0807.2207v1, §1 and Theorem 1.1](https://arxiv.org/html/0807.2207v1#S1) | Sun conjecture for \(k=3,4\) in arbitrary groups; same disjoint-left-coset/gcd formulation | Baseline, not a Suzuki Sun6/7/8 family result. |
| [Margolis–Schnabel, arXiv:1803.03569v1, §1, Definition 1.1 and Theorem B](https://arxiv.org/html/1803.03569v1#S1) | Every \(G\)-harmonic tuple of length at most four is \(\mathbb Z\)-harmonic; also a small-order Herzog–Schönheim theorem | Related machinery and terminology, not the assigned family result. The initially empty ar5iv route was retried successfully through arXiv. |
| [Garonzi–Margolis, arXiv:2509.25118v2, §1, Theorem 1.3](https://arxiv.org/html/2509.25118v2#S1.Thmdefi3) | Herzog–Schönheim for all simple groups | Actual prior coset theorem covering both families, **but requires a partition of the whole group and concludes repeated indices**. |
| [Same paper, Proposition 4.8 and Table 5](https://arxiv.org/html/2509.25118v2#S4.Thmdefi8), [Table 5](https://arxiv.org/html/2509.25118v2#S4.T5) | Explicit all-parameter Suzuki and small-Ree treatment; respective orders and minimum indices \(q^2+1\), \(q^3+1\) | Confirms substantial prior family treatment of a neighboring problem, not the Sun6/7/8 statement. |

The last paper also reports earlier Herzog–Schönheim treatment of \(Sz(8)\) and \(Sz(32)\) in its introduction. I inspected that attribution, **not the cited earlier proof**.

The 2014 Suzuki paper concerns subgroup depth; the 2025 small-Ree paper concerns Wiegold/Nielsen equivalence. Neither inspected statement is a Sun coset theorem.

**Disposition: `PRIORITY_UNKNOWN`.** No exact earlier public all-\(q\) Suzuki Sun8 result was located in this screen. That is a search result, not novelty evidence. The project’s already-recorded all-group Sun6/Sun7 statements must be acknowledged separately.

## 4. Separate scope: small Ree candidate

I read all **78 lines** of:

`mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/frontier-20261028-small-ree-simple-family-v1.md`

### Exact sources

- [Pierro, arXiv:1410.8702v2, §2.1](https://arxiv.org/html/1410.8702v2#S2.SS1): Sylow and Hall orders, factored group order.
- [Pierro, §2.2 and §§2.2.1–2.2.5](https://arxiv.org/html/1410.8702v2#S2.SS2): exhaustive maximal types and their structure.
- [Alavi–Daneshkhah–Mosaed, arXiv:1606.00049v1, §2](https://arxiv.org/html/1606.00049v1#S2): explicit
  \[
  |{}^2G_2(q)|=q^3(q^3+1)(q-1)
  \]
  immediately after Lemma 2.2; Lemmas 2.1, 2.2 and 2.8 provide additional structural corroboration.
- [Busch–Pengitore–Schillewaert–Van Maldeghem, arXiv:2510.06479v1, §2.2 and Lemma 2.1](https://arxiv.org/html/2510.06479v1#S2.SS2): an additional independent exposition of the types, subject to the order discrepancy below.

### Every maximal type and \(3\)-part

For \(q=3^{2m+1}\), \(m\ge1\), let \(a=\sqrt{3q}=3^{m+1}\).

| Type | Order used by candidate | \(3\)-part | Match |
|---|---:|---:|---|
| Sylow-3 normalizer/parabolic | \(q^3(q-1)\) | \(q^3\) | Pierro §§2.1, 2.2.2 |
| Involution centralizer \(2\times PSL_2(q)\) | \(q(q^2-1)\) | \(q\) | Pierro §§2.1, 2.2.3 |
| Four-group normalizer \((2^2\times D_{(q+1)/2}):3\) | \(6(q+1)\) | \(3\) | Pierro §2.2.4; its \(D_n\) denotes a dihedral group of **order \(n\)** |
| First Hall normalizer | \(6(q-a+1)\) | \(3\) | Pierro §§2.1, 2.2.5 |
| Second Hall normalizer | \(6(q+a+1)\) | \(3\) | Same |
| Proper subfield \( {}^2G_2(q_0)\) | \(q_0^3(q_0^3+1)(q_0-1)\) | \(q_0^3<q^3\) | Pierro §2.2.1; maximal relative degree is prime |

All valuation comparisons in candidate lines 35–49 follow. Thus the parabolic is the only maximal type capable of containing a full Sylow-3 subgroup, and every proper \(3\)-free index is divisible by \(q^3+1\).

**Edge cases:**

- \(q=27\) is covered by Pierro’s structural section: its global convention is \(q>3\), an odd power of \(3\). The different \(n>3\) wording in his main Möbius-function Theorem 2 is **not** a restriction on the cited §2 classification.
- \( {}^2G_2(3)\) is excluded as the ambient simple group but correctly retained as a possible subfield subgroup. Pierro identifies it as \(P\Gamma L_2(8)\); its order is \(1512\), with \(3\)-part \(27\).
- The candidate’s general \(p\)-free criterion correctly excludes \(p=7\). For \(p=3\), a gcd divisible by \(3\) and at most \(7\) can only be \(3\) or \(6\), contradicting Sun7 on seven such cosets.

**Independent-source qualification:** the 2016 HTML writes a cyclic \(C_{(q+1)/2}\) in its four-group-normalizer display where Pierro writes a dihedral \(D_{(q+1)/2}\), and has shifted Hall labels in Lemma 2.8. I have not silently equated those literal isomorphism statements. Its displayed order still gives \(6(q+1)\); the 2025 §2.2 explicitly describes the factor as dihedral of order \((q+1)/2\), corroborating Pierro’s convention.

### Independently verified 2025 HTML discrepancy

At [§2.2, first paragraph](https://arxiv.org/html/2510.06479v1#S2.SS2.p1), the raw HTML contains:

```text
alttext="q^{3}(q+1)(q-1)"
```

and the same expression in its `application/x-tex` annotation. This is therefore **present in the served HTML**, not merely a missing exponent in the text reader.

It conflicts with:

- the correct 2016 displayed order;
- Pierro’s §2.1 Hall-factor product;
- the 2025 paper’s own degree-\(q^3+1\) action and point stabilizer of order \(q^3(q-1)\).

Those give \(q^3(q^3+1)(q-1)\). **I did not inspect the PDF or author’s TeX**, and make no claim about where the discrepancy originated.

Earlier project coverage remains the report-level boundary at `final-report-v2.md:263`: later Ree leads did not inherit adoption. No held payload was opened. **`PRIORITY_UNKNOWN`** also applies to this new small-Ree Sun8 candidate.

## 5. Dependency architecture and review limits

- **Suzuki:** classical order/maximal list → common divisor of proper odd indices; together with \(3\nmid|G|\) and Sun5 → Sun6/7/8.
- **Small Ree:** classical order/maximal list → common divisor of proper \(3\)-free indices; together with Sun7 → Sun8.

This was a **same-harness, non-blind source and written-argument review**. I had the supplied task, inherited status/memory context, and candidate ancestry descriptions; I cannot certify clean cognition or absence of prior familiarity. No external reviewer/model, human review, kernel verification or priority certification was performed.

The candidates’ clocks and experimental outputs were read **as author-recorded text**, not independently authenticated. No review-time native clock was sampled. I did not execute either checker, inspect its implementation, recompute hashes, run builds/tests/formatters, change files, or use held/withdrawn research as proved premises.