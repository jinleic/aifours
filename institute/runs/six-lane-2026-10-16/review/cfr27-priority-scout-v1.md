<!-- Parent transcription 2026-10-17 18:23:34 PDT of the read-only scout Cfr27Priority's final report (agent://Cfr27Priority, transcript history://Cfr27Priority), verbatim below. The scout wrote no files and had no host clock; its time base is the server stamps it quotes. -->

# CFR(5,27) post-result priority and derivability screen

## Verdict: **NONE-FOUND-IN-SCOPE**

I found no earlier construction of CFR(5,27), and no source that makes it a consequence of published constructions. That covers DataCite, OpenAlex full text, arXiv, zbMATH, CPro1, Sage, GitHub, OEIS, the Handbook update pages, and works citing Pan et al. 2022, Ge 2005 and Abel–Ge 2005. A search miss is not novelty. Several key primary texts could not be read, so they remain possible sources of prior art (listed below).

There is one correction to the baseline. The 5-row cyclic DM over Z_27, which gives CFR(4,27), dates from **2005**, not from Pan et al. 2022. arXiv 2006.06921 states it as Lemma 4.11, citing Abel–Ge 2005, Theorem 4.2. The new witnesses add one row to a 2005 baseline.

**Time base.** I made no executions, so I had no host clock. Server timestamps seen during the screen: arXiv API feeds updated 2026-10-18T00:48:18Z and 01:05:33Z; zbMATH 2026-10-18T00:58:26Z; newest DataCite record seen created 2026-10-17T23:55:52Z. That puts the screen at about 2026-10-17 17:40–18:10 PDT, before the deadline. I wrote no files.

## Equivalent objects and how they count

These are all the same object, so I searched for each of them:

- **CFR(5,27)** has 5 rows.
- **(Z_27, 6; 1) difference matrix** over the cyclic group: 6 rows × 27 columns. In the Chinese-school notation this is a "(6,27)-CDM", equivalently a semi-cyclic 6-GDD of type 27^6.
- **Orthomorphisms:** 4 mutually orthogonal normalized orthomorphisms of Z_27, i.e. ω(Orth(Z_27)) ≥ 4 in Evans's convention.
- **MOLS:** 5 MOLS(27) of the form L_i(x,y) = f_i(x) + y; one of them may be the Cayley table.
- **Diagonally cyclic squares:** 4 mutually orthogonal diagonally cyclic Latin squares (MODCLS).
- **Frequency-hopping sequences:** a (27,27,5) one-coincidence set. Long–Ke–Chang prove the CFR⇒FHS direction; the converse is my derivation.

These are **not** applicable:
- MOLS or DMs over GF(27) (the group Z_3^3) or over Z_9×Z_3.
- CPro1's non-circular FR(7,27): a circular rectangle is also a Florentine rectangle, but not the reverse.

## Evidence

| Source (date / version) | Verbatim quote, ≤40 words | Bearing |
|---|---|---|
| [CPro1 problem_def.py](https://raw.githubusercontent.com/Constructive-Codes/CPro1/main/CPro1/design_definitions/circular-florentine-rectangle/problem_def.py), main@827f02b (2026-06-03). File touched only by cfe6fda (2025-01-28). | "OPEN_INSTANCES = [[6,21],[5,25],[5,27],[4,33]]"; the dev list includes "[3,27],[4,27]" | Still listed open. `designs/` has no CFR results; the one fork has no pushes after 2025-01-30. |
| DataCite `query="circular florentine"`: 3 hits in total | "Certify v0.5.0: an explicit 5x25 circular Florentine rectangle establishing F_c(25) >= 5" (Kirtchakov, registered 2026-08-07T03:58:59Z) | Only the n=25 claim. The `florentine` query (17), orthomorphism (45), "orthogonal orthomorphisms" (5), cyclic-DM (10), Tuscan/diagonally-cyclic (13) and recent Latin-square (93) queries found no claim for Z_27. |
| [05oz/certify](https://github.com/05oz/certify), last commit 3159a74 (2026-08-19T03:11:57Z) | Kirtchakov's note: "one more than the value 4 recorded for n = 25 in the Handbook … Table 62.27 (p. 677)" | No CFR(5,27). The Handbook table is quoted only for n=25. |
| [IEICE 2026EAL2054](https://www.jstage.jst.go.jp/article/transfun/advpub/0/advpub_2026EAL2054/_pdf), Long–Ke–Chang, publicized 2026-08-19, full text read | "p− 1 ≤ F̄(N) ≤ N− 1, where p is the smallest prime factor"; "attains the known theoretical upper bound when N is an odd prime" | The newest primary CFR paper; generic bounds only. |
| [arXiv 2006.06921](https://arxiv.org/pdf/2006.06921), Lemma 4.11 | "A (5, g)-CDM exists for any integer g which satisfies … (1) gcd(g, 6)=1, (2) g ∈ {15, 27, 39, 51}." citing Abel–Ge 2005 Thm 4.2; also Ge 2005 Lemma 3.10 for (5, 3^i)-CDMs | Moves the 5-row baseline back to 2005. Known only through this citing statement; the 2005 bodies were not read. |
| [vGJ arXiv 1806.04279v3](https://arxiv.org/abs/1806.04279), 29 Nov 2018 | "Question 7.2. For which primes p and abelian p-groups G is the largest integer m for which a (G, m, 1) difference matrix exists not a power of p?" | No Z_27 6-row result. The new witness does not answer Q7.2, because the maximum for Z_27 is unknown. |
| [Pan et al., DCC 2022](https://link.springer.com/article/10.1007/s10623-021-00981-6) (abstract, reference list, visible appendix) | "a (G, 5, 1)-DM exists, except for G ∈ {Z_3, Z_2⊕Z_2, Z_4⊕Z_2, Z_9} and possibly…" | Five rows only. The 12 citing works (newest 2026-09-18) have no 6-row cyclic result. |
| [Evans 2018, Ch. 13 abstract](https://link.springer.com/chapter/10.1007/978-3-319-94430-2_13) | "Work on these larger groups has been concentrated on trying to improve lower bounds for ω(G) for groups G that are direct products of elementary abelian groups." | [INFERENCE] probably no ω(Z_27) ≥ 4; body unread. |
| [zbMATH review of Song 2000](https://zbmath.org/?q=%22circular+Florentine%22) (Mullen) | "Using sets of mutually orthogonal latin squares with an additional property, the author is able to reduce the gap between upper and lower bounds on F_c(n) for infinitely many values of n." | General bounds; Table 1 unread. |
| Sage develop `database.py` (last touched 2025-09-02) | `DM = {(12,1)…(21,1)…(28,1)…(33,1)…(993,1)}` | No 27 entry; the quasi-difference matrix table has no 27 either. |
| [Dinitz, Handbook "New results" Part VI](https://site.uvm.edu/jdinitz/?page_id=413), last edited 10/18/2019 | "Page 656, Table 62.26 … no 9 x 9 Tuscan-2 square." | No update for Table 62.27 (F_c) or for the difference-matrix chapter. The Part III page has no DM entries either. |
| [Grzeszczuk, arXiv 2603.20084 v4](https://arxiv.org/abs/2603.20084) (2026-07-24) | "Every noncyclic 3-group G≇M_{3^r} (r≥4) carries three mutually orthogonal Latin squares" | Not applicable: noncyclic groups only, and only 3 MOLS. |
| Zhang–Helleseth TIT 2022; Song–Song TIT 2021 (abstracts reconstructed from OpenAlex) | "depends on the existence of circular Florentine arrays" | They use existing arrays as inputs; no evidence of a new F_c(27). Zhang–Vinterbo 2023 (read) gives only generic lemmas. |

Other checks that found nothing:
- GitHub repository search: only TuscanSquare (2020), od-flaky, and an orthomorphism counter.
- frontier-atlas: a prompt for complete mappings and orthomorphisms (2026-07-23), with no result files.
- OEIS: no F_c(n) sequence; the only Florentine entry is A004079, the non-circular F(n), whose data stop at n=12.
- zbMATH "circular Florentine": 5 documents, none newer than 2023.

## Can CFR(5,27) be derived from published constructions? (my analysis)

| Route | Applies to Z_27? |
|---|---|
| CRT product of DMs over coprime factors | No: 27 is a prime power. |
| Field multiplication table | Gives a DM over Z_3^3, not Z_27. |
| Multiplier rows x ↦ cx; Buratti's p^⌊n/e⌋ | 3 rows only. |
| Holey DM plus a DM on the hole subgroup | Would need a 6-row DM over Z_3 or Z_9. Impossible: Z_3 allows at most 3 rows, and no 4-row DM over Z_9 exists [Pan–Chang 2016, Lemma 2.2]. |
| Deleting rows from a larger known cyclic DM over Z_27 | No DM over Z_27 with ≥6 rows was found. |

Any 6-row DM over Z_27 therefore has to be a direct construction, and none was located. Derivability from the unread bodies below is unresolved.

## Access holes (not proof that nothing was published)

- **Handbook VI.62** Table 62.27, n=27 entry: not read. The recorded value 4 is inferred from CPro1's dev/open lists [INFERENCE]. **VI.17** and **III.3** also unread.
- **Song 2000** body: ScienceDirect and CORE both returned 403, although OpenAlex lists it as bronze open access.
- **Song 1991 USC thesis** ([doi:10.25549/usctheses-c30-541679](https://doi.org/10.25549/usctheses-c30-541679)): USC digital library returned 403.
- **Abel–Ge 2005 and Ge 2005** bodies: unread.
- **Abel–Finizio–Ge–Greig, DAM 2006**, "Table 1. Constructions of (v,k,1)-DMs with v<1000": seen only as a search snippet.
- **Evans:** 2018 Chapters 8 and 13, and Evans 2007 (JCD), unread. The QRS 2015 survey PDF downloaded but no text could be extracted (a format problem, not a paywall).
- **Wanless 2004:** author PDF returned 503; the ANU copy is restricted until 2037.
- **IEEE papers** (Zhang–Helleseth 2020/2022, Song–Song 2021): bot challenge or closed access.
- **Zhang–Feng–Wang 2022** (Discrete Math. note, about pairs of orthomorphisms only): unread.
- **JCD 2026 covering-schemes paper:** Wiley returned 403.
- **Zenodo API/pages:** 403. DataCite metadata was used instead.

**Other limits:**
- The researcher-name query was dominated by Ferudun's many unrelated records. The topic queries above are the decisive check.
- One web_search summary claimed that "(n,6,1)-CDMs do not exist when 3 | n". I dropped it as a hallucination: Sage's `DM_33_6_1` over Z_33 contradicts it.

## Significance and recommended wording

If the witnesses check out and nothing turns up in the unread sources, this is a **modest extension**:
- an explicit lower bound F_c(27) ≥ 5, one above the presumed recorded 4;
- equivalently, one row beyond the 2005 5-row cyclic DM;
- one CPro1 open instance resolved, comparable to Kirtchakov's CFR(5,25).

It does not determine F_c(27), whose only upper bound is the trivial 26, and it does not answer vGJ Question 7.2.

Suggested wording:

> "We exhibit explicit 5×27 circular Florentine rectangles, equivalently 6-row difference matrices over cyclic Z_27, so F_c(27) ≥ 5. A bounded screen on 2026-10-17 PDT found no earlier construction. Song (2000), the Handbook VI.62/VI.17 bodies, Evans (2018) and Wanless (2004) were not readable, and we claim no priority over them."

Never write "first". Before any deposit, re-run the DataCite `"circular florentine"` and `florentine` queries on the same day and quote registration timestamps. If library access is available, read Handbook Table 62.27 and Song 2000 Table 1 first; they are the most likely place for any prior construction to turn up.

```json
{
  "verdict": "NONE-FOUND-IN-SCOPE",
  "target": "CFR(5,27) == (Z_27,6;1)-DM (cyclic) == 4 MOO of Z_27 == 5 MOLS(27) L_i=f_i(x)+y == 4 MODCLS == (6,27)-CDM == (27,27,5) OC-FHS",
  "not_applicable": ["GF(27)/Z_3^3 DMs or MOLS", "Z_9xZ_3 DMs", "non-circular FR(7,27)", "noncyclic 3-group colouring bijections (arXiv 2603.20084)"],
  "screen_time": {"host_clock": "unavailable (no executions)", "server_stamps_utc": ["2026-10-18T00:48:18Z arXiv", "2026-10-18T00:58:26Z zbMATH", "2026-10-18T01:05:33Z arXiv", "newest DataCite created 2026-10-17T23:55:52Z"]},
  "baseline_correction": {"claim": "5-row cyclic DM over Z_27 (CFR(4,27)) known since 2005", "quote": "A (5, g)-CDM exists for any integer g which satisfies ... (2) g ∈ {15, 27, 39, 51}.", "url": "https://arxiv.org/pdf/2006.06921", "cites": "Abel–Ge, EJC 26 (2005) Thm 4.2; Ge, DM 301 (2005) Lemma 3.10", "verified": "secondary citation only"},
  "findings": [
    {"source": "CPro1 problem_def.py main@827f02b 2026-06-03", "quote": "OPEN_INSTANCES = [[6,21],[5,25],[5,27],[4,33]]", "url": "https://raw.githubusercontent.com/Constructive-Codes/CPro1/main/CPro1/design_definitions/circular-florentine-rectangle/problem_def.py", "stance": "supports-open"},
    {"source": "DataCite query \"circular florentine\" (total 3)", "quote": "Certify v0.5.0: an explicit 5x25 circular Florentine rectangle establishing F_c(25) >= 5", "url": "https://api.datacite.org/dois?query=%22circular%20florentine%22", "date": "registered 2026-08-07T03:58:59Z", "stance": "no CFR(5,27) claim"},
    {"source": "IEICE 2026EAL2054 Long–Ke–Chang (full text)", "quote": "p− 1 ≤ F̄(N) ≤ N− 1, where p is the smallest prime factor of N", "url": "https://www.jstage.jst.go.jp/article/transfun/advpub/0/advpub_2026EAL2054/_pdf", "date": "publicized 2026-08-19", "stance": "generic bounds only"},
    {"source": "van Greevenbroek–Jedwab arXiv:1806.04279v3", "quote": "For which primes p and abelian p-groups G is the largest integer m for which a (G, m, 1) difference matrix exists not a power of p?", "url": "https://arxiv.org/abs/1806.04279", "date": "2018-11-29", "stance": "no 6-row Z_27"},
    {"source": "Pan et al. DCC 90 (2022) abstract/refs/appendix", "quote": "a (G, 5, 1)-DM exists, except for G ∈ {Z_3, Z_2⊕Z_2, Z_4⊕Z_2, Z_9}", "url": "https://link.springer.com/article/10.1007/s10623-021-00981-6", "stance": "5 rows only; 12 citers none 6-row cyclic"},
    {"source": "Evans 2018 Ch.13 abstract", "quote": "Work on these larger groups has been concentrated on trying to improve lower bounds for ω(G) for groups G that are direct products of elementary abelian groups.", "url": "https://link.springer.com/chapter/10.1007/978-3-319-94430-2_13", "stance": "[INFERENCE] likely no ω(Z_27)>=4"},
    {"source": "zbMATH review Song 2000", "quote": "reduce the gap between upper and lower bounds on F_c(n) for infinitely many values of n", "url": "https://zbmath.org/?q=%22circular+Florentine%22", "stance": "Table 1 unread"},
    {"source": "Sage develop database.py (2025-09-02)", "quote": "DM = {(12,1)...(21,1)...(28,1),(33,1)...(993,1)}", "url": "https://raw.githubusercontent.com/sagemath/sage/develop/src/sage/combinat/designs/database.py", "stance": "no 27"},
    {"source": "Dinitz HCD new results Part VI (edited 2019-10-18)", "quote": "Page 656, Table 62.26. An exhaustive search has shown that there is no 9 x 9 Tuscan-2 square.", "url": "https://site.uvm.edu/jdinitz/?page_id=413", "stance": "no F_c or DM update"},
    {"source": "05oz/certify HEAD 3159a74", "quote": "PROVENANCE §7: longevity of the record", "url": "https://api.github.com/repos/05oz/certify/commits", "date": "2026-08-19T03:11:57Z", "stance": "only CFR_5_25"}
  ],
  "derivability": {"crt_product": "inapplicable (prime power)", "field": "Z_3^3 not Z_27", "multiplier_or_Buratti": "3 rows", "holey_recursion": "needs (6,3)- or (6,9)-CDM, which do not exist", "row_deletion": "no larger Z_27 DM known", "conclusion": "not derivable from any located construction; unread bodies unresolved"},
  "access_holes": ["Handbook VI.62 Table 62.27 n=27 / VI.17 / III.3", "Song 2000 body (ScienceDirect/CORE 403)", "Song 1991 USC thesis (403)", "Abel–Ge 2005, Ge 2005 bodies", "Abel–Finizio–Ge–Greig DAM 2006 Table 1", "Evans 2018 Ch.8/13, Evans 2007 JCD, Evans QRS 2015 (no text extracted)", "Wanless EJC 2004 (503; ANU restricted to 2037)", "IEEE Zhang–Helleseth 2020/2022, Song–Song 2021", "Zhang–Feng–Wang DM 2022", "JCD 2026 covering schemes (403)", "Zenodo API 403"],
  "significance": "modest extension: F_c(27)>=5 (+1 over presumed recorded 4; +1 row over 2005 5-row cyclic DM); resolves one CPro1 open instance; does not determine F_c(27) or answer vGJ Q7.2",
  "recommended_wording": "We exhibit explicit 5x27 circular Florentine rectangles (6-row difference matrices over cyclic Z_27), so F_c(27) >= 5; a bounded 2026-10-17 screen found no earlier construction; Song (2000), Handbook VI.62/VI.17, Evans (2018), Wanless (2004) unread; no priority claimed over them.",
  "dropped": ["web_search summary asserting no (n,6,1)-CDM when 3|n, contradicted by Sage DM_33_6_1"],
  "next_checks": ["library read of Handbook Table 62.27 and Song 2000 Table 1", "AFGG 2006 Table 1", "same-day DataCite re-run before deposit"]
}
```
