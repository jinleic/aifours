# Point-cyclic table (v ≡ 4 mod 12, 100 < v ≤ 200): bounded priority audit

Recorded 2026-10-17 06:09:23 PDT. Read-only scout `PcTablePriority` (completed after 21 min), preserved verbatim below. Its hand arithmetic is labelled [INFERENCE] where it says so. A search miss is not novelty; access holes are listed at the end.

Parent reading: the four certificates (112, 136, 160, 196) are finite existence results whose validity rests on the raw certificates alone; this audit concerns priority only.

---

# Prior-literature status of point-cyclic resolvable 2-(v,4,1) designs, v ≡ 4 (mod 12), 100 < v ≤ 200

## Summary

- **Settled by published results:**
  - **124 and 172 do not exist.** Genma–Mishima–Jimbo 1997, Theorem 2.1, excludes both, because 31 and 43 are primes ≡ 7 (mod 12).
  - **148 exists.** The Lam–Miao 1999 family covers it (37 = 12·3+1). I could not read that paper's body. Four independent secondary statements report the result.
- **No published theorem, table or example found:** 112, 136, 160, 184 and 196.
  - For these five, the published necessary conditions narrow the possible type. They allow T1 only at 112 and 184, T1 or T3 at 136 and 160, and T2 only at 196.
  - No published construction or exclusion settles any of them.
- **184 is settled only by this round's work.** The 8p corollary (unpublished written proof; Claude and Codex both returned ACCEPT; Lean-checked only for v = 88) says it does not exist. Do not label 184 as decided by the literature.
- **Topalova–Zhelezova 2026 names no order above 88.** In its text layer, none of 100, 112, …, 196 appears as an order. The only hits are "160" in a 64-point orbit table (line 264) and the page range "37–100" in reference 1.
- **The highest leftover risk is at 196,** which is forced to type T2, the type the Lam–Miao and Fuji-Hara–Miao–Shinohara machinery targets. The unread bodies of Lam–Miao 1999, Fuji-Hara–Miao–Shinohara 2002 and Lam–Miao 2001 could cover it, as could Mishima's 1999 thesis.

## Per-order table

All factorizations and congruences below are hand arithmetic and were not machine-checked; each is a one-line check.

Abbreviations: GMJ = Genma–Mishima–Jimbo 1997; MJ = Mishima–Jimbo; LM = Lam–Miao 1999; LMM = Lam–Miao–Mishima 2001; FMS = Fuji-Hara–Miao–Shinohara 2002; TZ = Topalova–Zhelezova 2026. GMJ, MJ 2000 and LMM were read as Gifu author preprints.

| v | n = v/4 | Published theorem that applies | Explicit prior example? | Confidence | Access holes that could change it |
|---|---|---|---|---|---|
| 112 | 28 = 2²·7 | **None found.** Published conditions force T1: MJ 2000 L4.2 (p.13) needs 28 ≡ 1 (mod 12), which fails; L4.1 (p.13) needs a divisor 1<v'<28 with v' ≡ 1 (mod 4), and 2, 4, 7, 14 all fail. No published T1 result applies: GMJ 2.1 needs n prime, LMM 2.1 needs a prime power, and LM needs primes 12s+1. | None found. The lane's own certificate is unpublished. | Medium, bounded search | LM 1999 body; Mishima thesis; Handbook |
| 124 | 31, prime | **Does not exist.** GMJ Thm 2.1 (preprint p.3): "When v is a prime, if a cyclically resolvable cyclic (kv, k, 1)-BIB design exists, then v ≡ 1 (mod k(k − 1)) holds." Here 31 ≡ 7 (mod 12). TZ p.2 restates it. | n/a | High | Published GMJ version not compared with the preprint |
| 136 | 34 = 2·17 | **None found.** T2 is excluded because 34 ≡ 10 (mod 12). T3 is allowed only with v'=17, u=2. T1 is not excluded by any published result. Lam–Miao does not apply (17 ≡ 5 (mod 12)). MJ 4.3 needs a type-T2 ingredient CRCB(4w) with w ∣ 34 and w ≡ 1 (mod 12), so only w=1, which is trivial. | None found; lane certificate unpublished | Medium | Same as 112 |
| 148 | 37, prime; 37 = 12·3+1, s=3 odd | **Exists, by Lam–Miao 1999** (body not read). Sources: zbMATH 0918.05013 review ("…on 4p points is shown for p=12t+1 a prime and t odd"); TZ p.2 ("v = 4q, where q is a product of primes of the form 12s + 1, and s is odd"); Gruner–Huber 2012 Thm 4(2); Huber 2013 Thm 5(2). Both Huber proofs misprint the Lam–Miao condition as "p = 20t+1" / "p = 20a+1". The type is necessarily T2. | None in accessible text; the Lam–Miao body may contain base blocks | Medium-high | Lam–Miao 1999 body |
| 160 | 40 = 2³·5 | **None found.** T2 is excluded (40 ≡ 4 (mod 12)). T3 is allowed only with v'=5, u=8. T1 is not excluded. 5 is not 12s+1, and no divisor w>1 of 40 is ≡ 1 (mod 12), so MJ 4.3 does not apply. | None found; lane certificate unpublished | Medium | Same as 112 |
| 172 | 43, prime | **Does not exist,** by GMJ Thm 2.1 (43 ≡ 7 (mod 12)). | n/a | High | As for 124 |
| 184 | 46 = 2·23 | **None published.** T2 is excluded (46 ≡ 10 (mod 12)) and T3 is excluded (2 and 23 are not ≡ 1 (mod 4)), so T1 is forced. No published T1 exclusion applies; this is the same situation TZ describe for 88. This round's unpublished 8p corollary (184 = 8·23, 23 ≡ 11 (mod 12)) gives nonexistence. | n/a | Medium for "undetermined in the literature" | As for 112 |
| 196 | 49 = 7² | **None found.** T1 is excluded by LMM L2.1 (p.4: "Let v = p^α … p relatively prime to k. Then there does not exist any CRCS(2, k, kv) of type (T1)"). T3 is excluded because 7 ≡ 3 (mod 4). T2 is allowed (49 ≡ 1 (mod 12)), so T2 is forced. Why each construction fails: Lam–Miao needs primes 12s+1 and 7 is not one; GMJ Cor 3.5 needs u prime ≡ 1 (mod 12); GMJ Cor 3.4, GMJ Thm 3.2 and MJ Cor 4.4 need factors ≡ 1 (mod 12) and ≥ 13, so the smallest output is n = 169; GMJ Thm 2.2 needs k odd; the GMJ Remark (p.7) says the GF(49) route is not cyclic; Buratti 1997 needs p prime. | None found | Medium-low | Lam–Miao 1999 ad-hoc computer constructions; FMS 2002 (CDDF⇒CRCS); Lam–Miao 2001 DCC (C₄⊕Z₄₉ ≅ Z₁₉₆); Mishima thesis; Handbook |

[INFERENCE] My hand derivation for 196: the 12 X blocks and 4 Y blocks reduce mod 49 to a (49,4,4) difference family over Z₄₉, and the 12 X blocks must partition Z₄₉∖{0}. That is why a (49,4,1) complete set of disjoint difference families in Z₄₉, which FMS might tabulate, is the relevant unread risk.

## Theorem hypotheses checked

- **GMJ Thm 3.2 and Corollaries 3.4/3.5 (preprint pp.8, 10–11)** need ingredients with properties (P1)/(P2). Lemma 3.1 (p.8) then forces n ≡ 1 (mod 12). In this range only n = 37 and 49 satisfy that, and neither has a nontrivial admissible factorization.
- **MJ 2000 Thm 4.3 (p.14)** needs (iii) "a CRCB(kw,k,1) of type (T2)", so w ≡ 1 (mod 12) by L4.2. No divisor w>1 of 28, 34, 40 or 46 qualifies. For 49, w=49 forces uv=1, which is trivial, and the output type would be T3, which is impossible at 196.
- **MJ 2000 Cor 4.4 (pp.15–16)** produces T2 at n = vw with both factors ≡ 1 (mod 12). The minimum is 13² = 169, so it gives nothing here.
- **Buratti 1997 (DCC 11:11–23), abstract read on Ovid:** "any (p,k,1)-DF (p prime) whose base blocks exactly cover (p−1)/k(k−1) distinct cosets of the k-th roots of unity … leads to a C_kp-invariantly resolvable cyclic (kp,k,1)-BBD". It is for primes only, so it is relevant at most to 148, and I did not check its condition at p = 37.
- **FMS 2002 (zbMATH 1007.05037):** a "(p,4,1)-CDDF exists" for primes p ≡ 13 (mod 24), p > 13. Since 37 ≡ 13 (mod 24), it reaches 148 only. Whether it has a k=4 application to cyclically resolvable designs is unread; the review describes only a k=3 example.
- **"Chang–Miao 2002" could not be identified as a source on these designs.** zbMATH lists three Chang–Miao joint papers:
  - DCC 26 (2002) 155–168, on double GDDs and double frames;
  - DM 261 (2003), on optical orthogonal codes;
  - IEEE Trans. Inf. Theory 49 (2003), with Fuji-Hara, on optical orthogonal codes.

  None of their reviews mentions cyclic resolutions, and none appears among zbMATH's 22 "cyclically resolvable" hits. [INFERENCE] The label in earlier audits is probably a mis-attribution.

## What TZ 2026 says (exact quotes)

- p.2: "An important necessary condition says that if a 2-(v,k,1) design possesses point-cyclic resolutions and v/k is a prime number, then v/k ≡ 1 (mod k(k − 1)) [5]."
- p.2: "The main existence result for cyclically resolvable Steiner 2-designs with block size 4 is derived in [6]. It states that there exist cyclically resolvable 2-(v,4,1) designs for v = 4q, where q is a product of primes of the form 12s + 1, and s is odd."
- p.4, Definition 5: "A resolution is point-cyclic if it has an automorphism permuting the points in one cycle."
- p.11: "That is why v = 88 is the smallest v for which the existence of cyclically resolvable 2-(v, 4, 1) designs has not yet been determined."
- Nothing in TZ concerns any specific v > 88. TZ p.5 labels MJ 2000 Lemmas 4.1/4.2 as T2/T3 "respectively"; in the preprint they are the other way round (4.1 is T3, 4.2 is T2).

## Terminology trap: a different notion also called "cyclically resolvable"

- Jimbo–Vanstone 1984 (zbMATH 0558.05009) defines a cyclically resolvable design as one with "an automorphism which permutes the resolution classes in a single r-cycle", in the 1-rotational setting.
- Reid–Rosa, EJC DS18 (2010), pp.4–5: "there exists a Z-cyclically resolvable 1-rotational S(2, 4,v)".
- Anderson–Finizio 1993 (zbMATH 0817.05005) construct designs of this kind for v = 3∏pᵢ^aᵢ+1, with primes pᵢ ≡ 1 (mod 4) and the same power of 2 dividing each pᵢ−1.
  - [INFERENCE] This family includes 112, 124, 160, 184 and 196 (196 = 3·5·13+1).
  - At 124, GMJ Thm 2.1 forbids a point-cyclic resolution, so these results must not be imported into the table.
- [INFERENCE, Anderson–Finizio body not read] Their designs are 1-rotational.

## Dated misses (all 2026-10-17)

- **zbMATH:** a phrase search for "cyclically resolvable" returned 22 documents, none deciding a table order. I checked forward citations of LM 1999 (11), GMJ 1997 (12), MJ 1997 (7), MJ 2000 (2), LMM 2001 (3), FMS 2002 (9) and Buratti 1997 (7), by title and review.
- **OpenAlex:** citing works of LM 1999 (24), GMJ 1997 (29) and MJ 2000 plus FMS 2002 (17). A full-text search surfaced only the closed Mishima thesis as new.
- **arXiv API:** abs:"cyclically resolvable" returned 0; all:cyclically AND resolvable AND Steiner returned 2, both irrelevant.
- **Web searches:** exact-order queries for all eight orders returned nothing.
- **Author pages:**
  - Topalova's ORCID was last modified 2026-10-13; her latest work is Axioms 15:762.
  - Zhelezova's data page has only the 64-point k=4 data; its "S(2,4,v) resolutions" entry has no link.
  - Topalova's homepage and Krčadinac's Steiner-design page have nothing relevant.
- **Later papers:** Lu (arXiv 2509.06663) only says "the general case remains far from settled". Ng–Paterson (arXiv 1509.05255) only says FMS used complete sets of disjoint difference families "in constructing cyclically resolvable cyclic Steiner systems". Costa–Feng–Wang (arXiv 1709.08947) has no point-cyclic content.

## Sources I could not access

- **LM 1999 body.** ScienceDirect returned 403 for both PIIs tried, S0097316598929247 (the correct one, per Crossref) and S0097316598929244. Crossref lists an Elsevier open-access licence from 2013-07-17. The Elsevier API returned 400 for both the DOI and the PII.
- **FMS 2002.** The author preprint at infoshako.sk.tsukuba.ac.jp/~fujihara/ftp/cs-ddf.pdf returned 403. There is no Wayback snapshot, CiteSeerX returned 404 and the Wayback CDX service returned 503.
- **Lam–Miao 2001 DCC 24:291–304:** abstract only.
- **Mishima–Jimbo 1997 (Congr. Numer. 123):** review only.
- **Mishima's 1999 doctoral thesis:** NDL pid 3159910, DOI 10.11501/3159910; the IIIF manifest returned 404.
- **Handbook of Combinatorial Designs, 2nd ed.:** archive.org item handbookofcombin0000unse returned 403 on search-inside, and the Google Books API returned 429.
- **Other bodies not read:**
  - Kageyama–Miao 1996 and 1998; Buratti 1997 (abstract only).
  - Fuji-Hara–Miao–Mishima 2004; Ge–Miao–Yao 2009.
  - Johnson–Weller 2003 (the submitted-version URL is dead); Johnson's 2004 thesis; Nyirenda's 2017 thesis (PDF 403).
  - Anderson–Finizio 1993 and Jimbo–Vanstone 1984 (reviews only).
- **Services:** MathSciNet, Google Scholar and ResearchGate (403).
- **Version caveat:** GMJ, MJ 2000 and LMM were read only as author preprints; the published versions may differ.

## Local files used

- `information-science/evidence/six-lane-20261016/point-cyclic-table200/sources/tz2026-axioms-15-00762.layout.txt`: lines 93–109 (p.2), 213–217 (Definition 5), 294–306 (p.5), 600–612 (p.11).
- `…/sources/gmj1997-preprint.layout.txt`: 122–123 (Thm 2.1, p.3), 162–163 (Thm 2.2, p.4), 291–294 (Remark, p.7), 348–366 (Lemma 3.1 and Thm 3.2, p.8), 478–488 (Corollaries 3.4/3.5).
- `…/sources/mj2000-preprint.layout.txt`: 654–661 (p.13), 682–694 (p.14), 750–760 (Cor 4.4; its conclusion line is on p.16, not p.15 as the README says).
- `…/sources/lmm2001-preprint.layout.txt`: 152–177.
- `point-cyclic-table200/README.md` §1.4: the lane's status table, which my results agree with except that 184 there is labelled "decided" by an unpublished corollary.
- `institute/runs/six-lane-2026-10-16/review/point-cyclic88-parent-verdict.md`: the 8p corollary is a written proof only; the Lean check covers v = 88.
