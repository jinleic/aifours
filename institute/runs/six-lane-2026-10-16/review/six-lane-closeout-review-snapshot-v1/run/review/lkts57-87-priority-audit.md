# Priority audit: LKTS(57), LKTS(87), and a complete spectrum below 200

I found no earlier construction or announcement of LKTS(57) or LKTS(87) dated before 2026-10-16. This was a bounded search, so it is not a proof of novelty. No published family or theorem I checked produces either order.

The latest public statement on their status is still Chen Wang's arXiv:2607.21521. Only v1 exists, dated 2026-07-23, and it lists 57 and 87 as the only open orders below 200. Nothing I found cites it or reports progress since then. I also found no earlier announcement of a complete spectrum below 200.

Related objects are already known: overlarge sets at orders 57 and 87, and large sets at 171 = 3·57 and 261 = 3·87. None of these is an LKTS(57) or an LKTS(87).

```jsonc
{
 "LKTS57": {
  "earliest_claim_found": "none",
  "latest_public_status": "open: Wang, arXiv:2607.21521v1, 2026-07-23, §4, p.11",
  "verdict": "no earlier construction located (bounded search, not novelty proof)"
 },
 "LKTS87": {
  "earliest_claim_found": "none",
  "latest_public_status": "open: same Wang statement",
  "verdict": "no earlier construction located (bounded search, not novelty proof)"
 },

 "status_statements_after_2026_07": [
  {"source": "https://arxiv.org/abs/2607.21521v1",
   "versions": "only v1 (23 Jul 2026 17:04 UTC); abstract page re-fetched today",
   "quote_p11": "an LKTS(v) is known to exist for every v < 200 satisfying v ≡ 3 (mod 6), with the two possible exceptions being 57 and 87.",
   "quote_p11_b": "These two orders are now the smallest remaining cases of the existence problem.",
   "quote_p11_c": "Direct computer search, preferably with a prescribed automorphism group, also seems realistic for these two isolated orders.",
   "quote_p1": "the corresponding problem for LKTSs remains far from settled."},
  {"other_public_statements": "none found",
   "evidence": "OpenAlex records 0 works citing Wang (W7170252291). No LKTS item appears on arXiv, Crossref or DataCite after 2026-07-23."}
 ],

 "already_known_but_different_objects (do not conflate)": [
  {"object": "OLKTS(57): 58 KTS(57)s on a 58-point set",
   "route": "RDSQS(58) ⇒ OLKTS(57), a standard derived-design argument",
   "source": "Chang–Zheng–Zhou 2019, via Liu–Lei arXiv:2210.06214v2 p.9, Lemma 4.3",
   "quote": "There exists an RDSQS(2v) for v ∈ {23, 29, 41, 47, 53, 59, 71, 83}."},
  {"object": "OLKTS(87)",
   "route": "87 = 2·43+1 with 43 ≡ 7 (mod 12) gives RDSQS(88)",
   "source": "Zhou–Chang 2014, via Liu–Lei Lemma 4.2",
   "quote": "{2q^n + 1 : n ≥ 0, q ≡ 7 (mod 12) and q is a prime power}"},
  {"object": "LKTS(171) = LKTS(3·57)",
   "source": "Wang–Shi (13²+2); also Liu–Lei Thm 4.4, whose list L contains 57"},
  {"object": "LKTS(261) = LKTS(3·87)",
   "source": "Yuan–Kang 2008 DCC; Zhou–Chang 2014; Wang 2026 Cor 3.8"},
  {"method_proximity [INFERENCE]": "Zhou–Chang 2010 built LKTS(21) and LKTS(39), orders 3·7 and 3·13, 'by using multiplier automorphism groups'. That is analogous to the G513 action on Z19×Z3. Their generators were not opened. The G903 setup at 87 = 2·43+1 uses the same q ≡ 7 (mod 12) 2q+1 arithmetic as the Yuan–Kang and Zhou–Chang OLKTS/RDSQS families. Neither is prior art for the large sets themselves."}
 ],

 "theorem_applicability": [
  // ✗ = cannot produce the order. Abstract-level sources: arguments use the theorem statements only.
  {"result": "Denniston 1979 tripling; Zhang–Zhu 2002 TRISQ tripling (LKTS(v) ⇒ LKTS(3v))", "57": "✗ needs LKTS(19)", "87": "✗ needs LKTS(29)", "why": "19 and 29 are not ≡ 3 (mod 6)"},
  {"result": "Lei 2002 LR product (uv)", "57": "✗", "87": "✗", "why": "u, v ≡ 3 (mod 6) forces 9 | uv; neither 57 nor 87 is divisible by 9"},
  {"result": "Lei 2002 (DM 257): 3^n·m·(2·13^k+1)^t, m∈{1,5,11,17,25,35,43}", "57": "✗", "87": "✗", "why": "cofactors 19 and 29 are not representable"},
  {"result": "Zhang–Zhu 2003: 3^n·m·∏(2·13^{n_i}+1), m ∈ {1,5,11,17,25,35,43,67,91,123} ∪ {2^{2r+1}·25^s+1}", "57": "✗", "87": "✗", "why": "18 and 28 are not of the form 2^{2r+1}·25^s"},
  {"result": "Lei 2002 holes: 6·4^n·25^m+3", "57": "✗ (needs 9)", "87": "✗ (needs 14)"},
  {"result": "Lei 2004", "57/87": "✗", "why": "conditional only, on OLKF(6^k) and LGKS for k∈{6..40}"},
  {"result": "Ji 2007: LKTS(3v−3) from 2-resolvable SQS(v)", "57": "✗ v=20", "87": "✗ v=30", "why": "needs S(2,4,v), so v ≡ 1,4 (mod 12)"},
  {"result": "Yuan–Kang 2008 DCC: 3·∏(2q^r+1)∏(4^s−1), q ≡ 7 (mod 12)", "57": "✗ 19 = 2·9+1", "87": "✗ 29 = 2·14+1", "why": "87 itself enters this family only as an ingredient, giving 261"},
  {"result": "Yuan–Kang 2008 JCD: 6q^n+3, q ≡ 7 (mod 12)", "57": "✗ q^n=9", "87": "✗ q^n=14"},
  {"result": "Ji–Lei 2008 RPICS; known families up to 2013 (Wang–Shi 1307.3019 Thm 1.1)", "57/87": "✗", "why": "cofactor 19/29 is not in {r}·5^b·∏(2·13^n+1)·∏(2·7^m+1) or 3∏(2q^n+1)∏(4^m−1)"},
  {"result": "Zhou–Chang 2014: LKTS(12·7^n−3)", "57": "✗", "87": "✗", "why": "its RDSQS route outputs multiples of 9"},
  {"result": "Chang–Ge 1999, Ge 2004, ZCZ 2016/2017 finite-field q+2 (and 3^n·67)", "57": "✗ 55", "87": "✗ 85", "why": "55 and 85 are not prime powers"},
  {"result": "Wang–Shi 2013/2017: q^n+2", "57/87": "✗", "why": "55 and 85 are not prime powers"},
  {"result": "Chang–Zheng–Zhou 2019 FDH", "57/87": "✗", "why": "outputs LKTS(3(2v−1)), divisible by 9. A 2v+1 route to 57 would need FDH(28,2,4,3); a Kirkman frame of type 2^{v−1} forces v ≡ 2 (mod 3), so v=28 fails. My derivation; paper body not opened."},
  {"result": "Xu–Ji 2021: 2^{2n+1}+1; second family 6·5^m(4·5^n+1)±3", "57": "✗ (56; 9/10)", "87": "✗ (86; 14/15)"},
  {"result": "Xu–Ji 2022 LR/OLKTS; Liu–Lei 2023; Xu–Ji 2024; Tan–Zhou 2025", "57/87": "✗", "why": "LKTS(3u) with u ≡ 3 (mod 6), or u = 19/29 inadmissible. Xu–Ji 2022 body not opened, [INFERENCE]."},
  {"result": "Wang 2026: 7q+2", "57/87": "✗", "why": "55 and 85 are not divisible by 7"},
  {"result": "Wu 1990/1998: TKTS(33, 51, 105); LKTS(3^n·41)", "57/87": "✗"}
 ],

 "complete_spectrum_v_lt_200": {
  "prior_announcement": "none. No source claims all v<200; Wang states 57 and 87 as exceptions.",
  "if_both_certificates_valid": "all 32 admissible v in 9..195 would be covered. This is a new aggregate statement that inherits Wang's premises, at uneven evidence levels.",
  "premise_levels": {
   "local verified certificates": "9, 15 (dossier); 57, 87 (parent)",
   "tripling (Zhang–Zhu 2002, zbMATH: TRISQ(v) for all v ≡ 3 mod 6; Ge 2004 Lemma 2.2 opened)": "27, 45, 63, 81, 99, 117, 135, 153, 189",
   "published primary abstract or appendix opened": "21, 39 (Zhou–Chang 2010); 69, 141, 165 (ZCZ 2016); 111, 123, 159, 183, 195 (ZCZ 2017)",
   "full text opened": "171 (Wang–Shi)",
   "unrefereed preprint, full text": "93, 177 (Wang Cor 3.8; no other family reaches them)",
   "cited via Wang Table 1 only": "51, 75, 105 (Denniston 1979); 33 (Schreiber; backup Xu–Ji 2^5+1); 129 (backup Xu–Ji 2^7+1)",
   "WEAKEST: 147": "only Xu–Ji 2021's second family (m=1, n=0 gives 147). Supported only by the dossier's earlier indexed-abstract snippet; the body, abstract and zbMATH review PDF (403) were unreachable this run. I checked every other family listed here: none gives 147."
  }
 },

 "ai_or_unrefereed_claims": {
  "EulerSolve": "/papers/ lists 286 items (header); I scanned the full page and its JSON-LD: zero Kirkman/LKTS/triple-system items",
  "openai/math": "remote HEAD 1581d4c (2026-10-12; last content merge fd4aeeb, 2026-10-08) and local clone adc7f1241: CONTENTS.md has no Kirkman/LKTS/Steiner/large-set entry",
  "GitHub": "repo search 'kirkman large set' gives 0. The recent 'lkts' repos are SEO spam (axiom5730/lkts, pfwmh8bcpm/lkts sampled).",
  "other": "arXiv 2603.08322 is an AI design-theory paper about Latin squares, not LKTS. No other AI claim found."
 },

 "search_coverage": [
  "arXiv web search: Kirkman (123 hits), LKTS (12), \"large sets\"+\"triple systems\" (10), overlarge (4), schoolgirl (3); math.CO recent listing Oct 9–16 (386 entries); author pages for Chang, Zhou, Ji, Lei. Nothing on LKTS after Wang.",
  "Crossref: DCC since 2026-07 (68 items), JCD since 2026-06 (17), DM/JCTA keyword queries, 'Kirkman' titles 2025-09 to 2026-12 (7; two KTS papers, neither LKTS)",
  "OpenAlex: Kirkman title/abstract since 2025-06 (89); citing the survey since 2026 (1: Tan–Zhou tiling); citing 10 key LKTS papers since 2025-06 (2, both Tan–Zhou)",
  "DataCite/Zenodo: title, description and LKTS queries. Only unrelated records plus known arXiv DOIs."
 ],

 "access_holes": [
  "Chang–Zhou 2013 JCTA survey full text (403; its 'new existence class' is unread; Wang builds on it and still lists 57/87)",
  "Xu–Ji 2021 and Xu–Ji 2022 bodies; FDH 2019 body; Ji–Lei 2008 order list (zbMATH summaries or Liu–Lei restatements only)",
  "Semantic Scholar (tool failure), NASA ADS, Google Scholar (not used), MathSciNet, IA Scholar (bot check)",
  "arXiv API (rate limit 429 / timeout); arXiv web search used instead",
  "UnsolvedMath: site search 429. The HF grep is unreliable: a control term ('Steiner triple') also returned no match, so the dataset is unchecked. Its 15 source sets exclude the 10000-problems book.",
  "CNKI, Chinese theses, talks, private correspondence: not searchable here"
 ],

 "calibrated_verdict": "LKTS(57): no earlier construction located. LKTS(87): no earlier construction located. Complete v<200 spectrum: no earlier announcement; any such claim holds only at the evidence levels above, with 147 as the main hole. Residual risk: the 12-week window since Wang and unindexed or paywalled venues."
}
```

## Files used
- `/Users/jinleic/repos/aifours/mathematics/kirkman-large-sets-57-87/sources/wang-2607.21521.txt` — Wang §1 and §4 text; matches v1 HTML.
- `…/sources/liu-lei-2210.06214.txt:424-470,483,554` — Lemma 4.2 (from Zhou–Chang 2014), Lemma 4.3 (from FDH 2019), Theorem 4.4 (lists 57 and 87).
- `…/sources/wang-shi-1307.3019.txt:57-100` — summary of all LKTS families known as of 2013 (Thm 1.1).
- `…/sources/recursion-notes.md:49-59` — where the dossier records the Xu–Ji 147 access caveat.
- `/Users/jinleic/jinleic-workspace/math/CONTENTS.md` — local openai/math clone (no hit).
