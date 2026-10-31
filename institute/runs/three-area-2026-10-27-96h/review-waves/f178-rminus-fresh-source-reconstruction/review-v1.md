# review-v1 — f178-rminus-fresh-source-reconstruction

- Reviewer: `ReviewF178RminusSources` (same-harness task agent). This is not a human review, an independent-model-family review, a formal/kernel check, or a novelty audit.
- Wave manifest: `manifest-v1.json`, SHA-256 `01793ad7c45a2f444e7c155284bb81dadca943c24aeb39801603efe341570764`, verified 2026-10-29T15:05:31Z.
- Native clock, read immediately before this file was written: `2026-10-29T08:49:44-0700 PDT` (`2026-10-29T15:49:45Z`).
- Scope: only the standalone `716/107` certificate v12c and whether it applies to the actual R-minus graph and its asymptotic guessing number. Out of scope: the other three bounds in the bundle, exactness of the old publisher LP (`1847/276`), lower-bound closure, novelty, publication.
- I solved no LP. I did not reconstruct the DFZ inequality from its copy steps; it is used as an explicit source import.

## 0. Bottom line

Within my source slice I found **no F (fatal) and no M (major) finding**. The chain "every strategy on R-minus ⇒ `log_q|W| ≤ 716/107`" reconstructs from the actual sources, with one conditional import: **the DFZ list item `3 7 2 2 3 0 0 3 2` (DFZ Section FourCopies, TeX line 2088) is assumed valid**. Its validity is INCONCLUSIVE at my level because I imported it rather than re-deriving it. Under my independently reconstructed row semantics, the exact identity does hold, and exactly one orientation convention makes it hold. That recomputation was only a decoding-consistency control; the raw-arithmetic slice is outside my scope (§11).

| Id | Claim | F | M | m | INCONCLUSIVE | Status |
|---|---|---|---|---|---|---|
| CL1 | Bundle 26-edge graph = publisher R-minus (Fig. 2, p. 570) | – | – | m1 | – | VERIFIED: exact vector decoding plus Appendix B group plus cp_f |
| CL2 | g1, g2 are automorphisms generating an 8-element group, equal to publisher σ, τ; Aut(R-minus) = ⟨g1,g2⟩ | – | – | – | – | VERIFIED (exact) |
| CL3 | FD, cap and objective rows hold for every finite alphabet and every strategy | – | – | m2 | – | VERIFIED |
| CL4 | The strategy product over G gives a G-invariant law that keeps the objective exactly | – | – | – | – | VERIFIED (proof plus exact/toy controls) |
| CL5 | Copy-lemma semantics: marginal equalities for U ⊆ over and Q ⊆ entries, step independence, sequential steps. Atomic tuples are not used | – | – | – | – | VERIFIED against publisher Lemma 2.10 and DFZ copyLemma; exact controls |
| CL6 | Bundle's transcription of publisher branches 1(a)–(c) | – | – | – | – | VERIFIED. v12c does not use branch 1(a) |
| CL7 | Every v12c row type is valid on one shared family of actual random variables, and also on independent branch laws | – | – | m3 | – | VERIFIED under my decoding. The `dfz` type is conditional on CL8b |
| CL8a | DFZ coefficient form and item transcription; validity of conditional/union substitution | – | – | – | – | VERIFIED; substitution proved in §8 |
| CL8b | The DFZ item inequality itself | – | – | – | **INCONCLUSIVE (import)** | Rests on DFZ's published list claim, TeX lines 296, 1954–1956, 1964–1965 |
| CL9 | Exact identity Σ w·row = h(V) and Σ caps = 716/107 | – | – | – | – | Consistent in my decoding control. Certification belongs to the arithmetic slice (§11) |
| CL10 | "Standalone": no dependence on the publisher LP optimum, branch 1(a), checker or receipts | – | – | m4 | – | VERIFIED for my reconstruction (§9) |
| CL11 | gn(R-minus) ≤ 716/107 | – | – | – | conditional on CL8b (and CL9 slice) | No F/M found |

## 1. Inputs, integrity, actual read order and deviations

The manifest SHA was verified first. Then I checked SHA-256, bytes and LF for all seven declared inputs; every value matched the manifest. All seven were re-verified unchanged at 2026-10-29T15:48:39Z.

| # | Input | SHA-256 | bytes | LF |
|---|---|---|---|---|
| 1 | parent-fresh-route-admission-v1.json | 82f89e18b8ba0a89972cef8db0e4e117a02ac6c1146ef9b2c4d24cad85cc16ba | 5183 | 71 |
| 2 | frontier-20261028-full-source-lp-optimum-v1-erratum-1.md | c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9 | 2024 | 13 |
| 3 | frontier-20261029-upper-bound-review-input-v1.md | e8c46fc195dd22ebcd28e485587a9872582a99ed89b25ce8d2e2ba4cee9e505a | 12496 | 165 |
| 4 | gurpinar-kybernetika60-2024-553-575.pdf | 373e8a2567fc7de9d40d0e5fabca9655cbb7b689a162005262b4f4d432bb46d8 | 502687 | 3061 |
| 5 | gurpinar-publisher-layout-v1.txt | 98d1dba760d383db92948026002bfa7dd95ebbe558cf1917f0c471189b528c88 | 66399 | 1156 |
| 6 | parent-dfz-primary-extract-v1.txt | 2b59a111a1cb7f69de0385926305d5f7456ef67b6045a78d98bba3fcd0f072a6 | 6172 | 119 |
| 7 | parent-input-certificate-v12c.json | 6d5dc5c62833243db23870bcc34f3869149bd48e13843bee4ca977cd04eca886 | 239532 | 1 |

Actual order:
1. Manifest.
2. Input 1, read fully; status only.
3. Input 2 (erratum), read fully, before any scientific input.
4. Input 3 (bundle). I read the preface (lines 1–15: title, author line, bound table, scope sentence), then Section 0 (from line 16), then Sections 1–4.
5. Input 4 (PDF) text. The harness PDF reader stopped at page 19, partway through Theorem 5.2(b). To read the whole PDF I ran `pdftotext -layout` (poppler 26.04.0). Its output, `ReviewF178RminusSources-publisher-pdftotext-layout.txt`, is **byte-identical to input 5** (SHA `98d1dba7…`), so input 5 is exactly the poppler layout extraction of input 4.
6. Input 5, all lines 1–1156 (includes loci 873–995 and Appendices A–C).
7. Back to input 4 for the figure: I rendered page 18 (printed p. 570) as PNG and viewed it, converted it to SVG vectors with `pdftocairo -svg`, and listed the figure paths.
8. Input 6, read fully.
9. Input 7. Parsed completely with a strict loader: duplicate keys rejected (none present), non-finite constants rejected (none present). All 2,377 rows were machine-decoded. Every non-elemental special row (fd, cap, 3 independence, 3 xindependence, 7 mindependence, the dfz row) and samples of every other type were inspected by eye. The full decoded rendering is `ReviewF178RminusSources-decoded-rows.tsv`.
10. Mathematics started here: label mapping (crop text, then `pdftotext -tsv` word boxes), edge decoding, automorphisms, row decoding.
11. One named direct primary-source read beyond the packet. The DFZ TeX pin was verified (SHA `ab01cd41…`, 173,135 B, 3,677 LF). I grepped its `\section`/`enumerate`/`copy step` lines; the displayed grep context included lines such as 105 and 296–297. I also read lines 799–873 for the copy-step notation. I did not read the full TeX.

Deviations, all disclosed:
- **D1 (ordering).** Step 7 belongs to input 4, but I did it after input 5. It included listing the Fig. 2 SVG paths and a first mental reading of edges from them, which happened before inputs 6–7 were opened. The label mapping, automorphism, row and DFZ mathematics all came after every input had been read.
- **D2.** Before starting I opened one harness skill document (`independent-snapshot-review`). It is tooling text, not a scientific input, and it describes an external-model procedure that I did **not** run.
- **D3.** `pdftotext -bbox` crashed (exit 134, libc++abi `out_of_range`). Its 298-byte partial output is kept unused (`ReviewF178RminusSources-p18-bbox.html`, SHA `ad026a74…`). `-tsv` worked.
- **D4.** Exploratory computations in my eval kernel came before the receipted scripts. Only the scripts in §10 are controls.
- **D5.** Control 3 run 1 exited 1 because I had coded two mutation expectations inverted. The audit itself behaved as intended. Both files from that run are kept (§10).
- **D6.** The extra DFZ TeX reads in step 11 (allowed as a named public-source read).

Not opened: any f161 report, code, result, transcript or parent assessment; earlier candidate or bound packets (including `frontier-20261028-weighted-law-certificate-v1.md`, `frontier-20261028-gurpinar-certificate-audit-v1.md`, and source packet `08af469a…`); every author checker, producer, DFZ-verify script, receipt, result or controls JSON named in the bundle; BCDRV. I used no web search, external model/API, Git, deletion, publication, author contact or infrastructure change.

## 2. Exact source transcriptions (hypotheses used)

Layout-text line numbers refer to input 5. Math is quoted as poppler renders it: `J1, sK` = ⟦1,s⟧ and `→(v)` = in-neighbours.

- **Game** (lines 361–367): "1. At every node v ∈ V there is a player. 2. Every player is assigned a hat colour sv from J1, sK = {1, 2, . . . s} uniformly ran- domly and independent of the hats of the other players. 3. The edges of the graph show who can see whom … 4. The players win as a team if every single one of them guesses their own hat colour correctly and lose otherwise."
- **Def. 2.13** (382–390): "A guessing function for the player on x ∈ V is a mapping from J1, sK{y∈V |(x,y)∈E} to J1, sK. … A strategy is a family of guessing functions F = (fv )v∈V for every vertex of the graph."
- **Def. 2.14** (403–413), linearised by me; the extraction drops the cardinality bars, which Remark 2.15 (416–420) states as "the logarithm on base s of the cardinality": "gn(G, s) := max_{F strategy} log_s (Prob[winning with F] / s^{−|V|}) = max_{F str.} log_s |{winning config. in J1, sK^V for F}|".
- **Def. 2.17** (424–430): "The following limit exists. lim_{s→∞} gn(G, s) It is called the asymptotic guessing number of G and noted gn(G). In particular, it is equal to sup_{s≥2} gn(G, s)." The upper bound needs only gn(G,s) ≤ B for every s; it does not use the existence of the limit.
- **Reduction** (449–458, 460–472, Prop. 2.18): "1. The entropy Hs ((Xv )v∈V ) … is the logarithm of the cardinality of the set on which F wins … 2. … the hat colour of a player is determined by the colours of the hats they see, therefore, H(Xv |(Xu )u∈→(v) ) = 0." Followed by "Maximize H((Xv )v∈V ) subject to: H(Xv ) ≤ 1, H(Xv |(Xu )u∈→(v) ) = 0".
- **Lemma 2.10** (246–265): "Let X, Y, Z be three jointly distributed random vectors. 1. There exists a random vector Z′ such that • X, Z and X, Z′ are identically distributed, • Z′ and Y, Z are independent given X. 2. There exists a random vector Z′ such that • every sub-vector of X, Z has the same entropy as the sub-vector of X, Z′ that consist of the same coordinates, • I(Z′ : Y, Z|X) = 0. Z′ is called a Y -copy of Z over X or simply Y -copy of Z when X consist of all the other variables".
- **R-minus** (873–874): "The graph R− is given in Figure 2 which is obtained from R by removing the edge 9 ↔ 10 from it."
- **cp_f** (901–902): "The fractional clique cover number for R and R− are both 10/3 = 3.3, which implies the lower bound 10 − 10/3 = 20/3 = 6.6 by [10]."
- **Theorem 5.2** (933–958), item 1:
  - "(a) X2′ be a X3 -copy of X2 ;"
  - "(b) • (X4′′ , X5′′ ) be a X10 -copy of (X4 , X5 ) over X1 , X2 , X3 , X6 , X7 , X8 , X9 , • and X7′′′ be a (X4′′ , X5 , X10 )-copy of X7 over X1 , X2 , X3 , X4 , X5′′ , X6 , X8 , X9 ;"
  - "(c) • (X6′′′′ , X7′′′′ ) be a copy of (X6 , X7 ) over X1 , X2 , X3 , X4 , X5 , X8 , X9 , X10 , • and X8′′′′′ be a (X7 , X7′′′′ )-copy of X8 over X1 , X2 , X3 , X4 , X5 , X6 , X6′′′′ , X9 , X10 ;"
  - Item 2 gives the three elemental sets; item 3 is "the symmetry constraints."
  - The proof opens "as in Corollary 2.18". No Corollary 2.18 exists (there is Proposition 2.18 and Corollary 3.7). This is a harmless source typo.
- **Remark 5.4** (985–995): "… we did not take all the elemental information inequalities for all the combinations of old and new random variables. For example there is no Shannon- type inequality involving both X2′ and X4′′ in the first linear program …". This matches the erratum, which is the correct source reference in place of Remark 3.8 (673–674).
- **Appendix B** (1143–1149): "The symmetry group of R− is generated by two permutations: σ = (18)(2 10 5 9)(3746) and τ = (25)(36)(47). Aut(R− ) = ⟨σ, τ ⟩." and "The symmetry group of RL is same as that of R, namely Aut(RL ) = ⟨(25)(36)(47), (26)(35)(8 10), (24)(57)(89)⟩."
- **DFZ copy lemma** (packet S1|348–357):
  - "Let $A$, $B$, $C$, $D$ be jointly distributed random variables. Then there is another random variable $R$ … [C1.] The marginal distributions of $(A,B,C)$ and $(A,B,R)$ are the same with $R$ replacing $C$. [C2.] $I(CD;R|AB)=0$ In this case we say that $R$ is a $D$-copy of $C$ over $(A,B)$."
  - Construction (S1|363–366): "$p'(a,b,c,d,r) = \frac{p(a,b,c,d)\sum_d p(a,b,r,d)}{\sum_{c,d}p(a,b,c,d)}$."
- **DFZ form** (S1|1957–1963): "nine integers … coefficients $a,b,c,d,e,f,g,h,i$ for the non-Shannon inequality of the form aI(A;B) ≤ bI(A;B|C) + cI(A;C|B) + dI(B;C|A) + eI(A;B|D) + fI(A;D|B)+ gI(B;D|A) + hI(C;D) + iI(C;D|A)".
- **DFZ item** (S1|2088): `\item 3 7 2 2 3 0 0 3 2 rs bd ac.t c abs.u t bcr.`
- **DFZ structure** (direct TeX):
  - `\section{…Four Copy Variables with at most Three Copy Steps}` at 1952; `\begin{enumerate}` at 1968; `\end{enumerate}` at 2183; the next `\section` at 2188. Line 2088 is therefore inside the FourCopies list.
  - Line 296: "Our final list of inequalities appears in Section~\ref{FourCopies}. To save space, rather than giving the proof of each one, we provide the sequence of copy steps used in the proof."
  - Notation, lines 853 and 864–871: "$RS$ is a copy of $CD$ over $AB$". W, the discarded part, is everything not in Z and not copied. Parentheses mark an atomic tuple.
  - So the item's steps read: (R,S) := copy of (B,D) over (A,C); T := copy of C over (A,B,S); U := copy of T over (B,C,R). This is context only, because the item is imported.

## 3. Graph applicability (CL1, CL2)

All figure geometry comes from the PDF's own vector strokes, not from visual tracing.

- Page 18 has **no raster image** (`pdfimages -list` is empty). Fig. 2 consists of 10 white-filled node circles (r ≈ 1.99 pt) and 23 black stroke segments. Each digit label maps to exactly one circle by word-box nearest distance: nearest 7.0–8.7 pt, second-nearest ≥ 17.2 pt. A crop-box text test confirmed the same map.
- 20 black strokes (straight lines and cubic curves) each start and end on a circle boundary (2.19 pt from the centre) and come within r+0.5 pt of no third circle. They give 1–2, 1–3, 1–4, 1–5, 1–6, 1–7, 2–9, 2–10, 3–8, 3–9, 4–8, 4–10, 5–9, 5–10, 6–8, 6–9, 7–8, 7–10, 8–9, 8–10.
- **One closed black path 2→6→4→2** passes, within 0.20 pt, through the centres of nodes 7, 5 and 3, which sit at the side midpoints. Read with the usual convention that a node on a drawn segment subdivides it, this is the hexagon 2–7, 7–6, 6–5, 5–4, 4–3, 3–2. Together with the 20 edges that is **exactly the bundle's 26 edges**, and the bundle's neighbourhood table encodes the same symmetric set.
- A **white** (invisible) closed path 8→10→9 is also present. Its side 10–9 is the removed edge 9↔10, which is consistent with lines 873–874.
- **m1.** On geometry alone, Fig. 2 has a second reading: the chords 2–6, 6–4, 4–2 hidden behind nodes 7, 5, 3 (23 edges). The bundle says only "visually transcribed" and does not mention this. The publisher's own text settles it:
  - Subdivided reading: g1 = σ and g2 = τ are automorphisms, and the **full Aut has order 8 and equals ⟨σ,τ⟩**, matching Appendix B.
  - Chord reading: σ is not an automorphism and |Aut| = 2 (receipted, control 1). τ also fails (exploratory kernel check only).
  - Adding 9–10 to the subdivided reading gives Aut(R) equal to the publisher's order-12 group ⟨(25)(36)(47),(26)(35)(8 10),(24)(57)(89)⟩. The chord reading plus 9–10 does not.
  - For both R-minus and R, ω = 3. An exact 3-fold triangle cover (10 triangles, weight 1/3 each) together with the dual y ≡ 1/3 certifies cp_f = 10/3, giving lower bound 20/3, as stated at 901–902 (receipted, control 1). The chord reading contains a K4, e.g. {1,2,4,6} (exploratory kernel check only).
- G = ⟨g1,g2⟩ is dihedral of order 8 (g1 has order 4; g2·g1·g2 = g1⁻¹). Its elements: id, (3 7)(4 6)(9 10), (2 5)(3 4)(6 7)(9 10), (2 5)(3 6)(4 7) = τ, (1 8)(2 9)(5 10)(6 7), (1 8)(2 9 5 10)(3 6 4 7), (1 8)(2 10)(3 4)(5 9), (1 8)(2 10 5 9)(3 7 4 6) = σ. All eight are automorphisms. The listing and the dihedral relation come from my exploratory kernel; |G| = 8 and the automorphism property of every element are receipted in control 1.
- Certificate variable names a..j = X1..X10 = publisher vertex labels 1..10, as in bundle §2.4.
- Boundary: "R-minus" here means Gurpinar's Fig. 2 graph. Its identity with BCDRV's R-minus is the publisher's attribution; I did not read BCDRV.

## 4. Game → entropy rows, any finite alphabet (CL3)

Fix q ≥ 2 and any deterministic strategy (f_v) with W = {x ∈ [q]^V : x_v = f_v(x_{N(v)}) for all v}. Random strategies are averages of deterministic ones (lines 391–396), and Def. 2.14 maximises over deterministic F. If W = ∅ there is nothing to prove. Otherwise let X be uniform on W. Then:
- H(X_V) = log|W|;
- H(X_v | X_{N(v)}) = 0, because x_v is a function of x_{N(v)} on W. These are the `fd` rows h(N(v)+v) − h(N(v)) = 0, using the full neighbourhood. Control 3 shows that dropping a single neighbour breaks the identity.
- H(X_v) ≤ log q, because X_v takes values in [q]. These are the `cap` rows.

Every other row type is homogeneous, so normalising by any log-alphabet constant changes nothing except the caps, which become h(v) ≤ 1.

**m2 (presentational).** Bundle §2.2 claims the bound "for every q and every strategy" directly. It actually needs §2.3 as well, because the `sym` rows hold only for the symmetrised law. The quantifiers still close via §5: (q,F) ↦ (q⁸, F^G) with the same objective.

## 5. Symmetrisation by strategy product (CL4)

Take independent copies X^(g), g ∈ G, each uniform on W, and set Y_v = (X^(g)_{g(v)})_{g∈G} ∈ [q]^G.
- **It is a strategy on the same graph.** For component g of vertex v, guess f_{g(v)}(x^(g)_{N(g(v))}). Because g is an automorphism, N(g(v)) = g(N(v)), so every X^(g)_w with w ∈ N(g(v)) sits in Y_{g⁻¹(w)}, and g⁻¹(w) ∈ N(v). The decoder for v reads only Y_{N(v)}.
- **Winning set.** Y wins iff every component wins: for all g and v, x^(g)_{g(v)} = f_{g(v)}(…), and v ↦ g(v) is a bijection. Hence W_Y ≅ W^G and |W_Y| = |W|⁸ on alphabet q⁸. The objective is preserved exactly: log_{q⁸}|W|⁸ = log_q|W|.
- **Entropy profile.** Y is uniform on W_Y, and H(Y_S) = Σ_g H(X_{g(S)}) by independence of the copies. For k ∈ G, H(Y_{k(S)}) = Σ_g H(X_{(gk)(S)}) = H(Y_S), because g ↦ gk is a bijection of the *group* G. So every `sym` row h(S) = h(g_i(S)) holds. FD and caps (now ≤ log q⁸) hold for Y as in §4.
- This argument is direct. It does not need the publisher's Lemma 3.1 / Remark 3.2 route through convexity of the closure of the entropy region. It suits a dual certificate, which must be evaluated on an actual law.
- Exact and toy controls (control 1 and control 2):
  - Σ_g h(g S) is invariant for random rational h over all 1,023 subsets; it fails for the non-subgroup {id, g1}.
  - The full-G product decoder reads exactly Y_{N(v)}; this fails for a non-automorphism.
  - For a parity-triangle strategy with |W| = 64, full enumeration over 4¹⁰ configurations shows W_Y = W×W for ⟨g2⟩. It also gives H(Y_S) = H(X_S) + H(X_{g2 S}) and H(Y_S) = H(Y_{g2 S}) for all S, while X itself is asymmetric by up to 2 bits.
  - For the full G, 300 sampled W⁸ points all win, and flipping one component makes Y lose.

## 6. Copy semantics, branches, programs, availability (CL5, CL6)

**Semantics.**
- A step (over O, copied tuple C, new N) is realised by the DFZ kernel p′ = p(all)·p(O, C=n)/p(O), sampled given O.
- Then law(O, N) = law(O, C), so h(U ∪ N_Q) = h(U ∪ C_Q) for **every U ⊆ O and every nonempty Q ⊆ entries** (C1 / Lemma 2.10.2).
- And N ⫫ (all existing variables) | O (C2). This implies the branch-restricted independence I(N; E∖O | O) = 0 for every E ⊆ existing.
- Alphabets stay finite. Steps chain, and an over-set may contain earlier copies of the same branch.
- U must lie inside O. It must not contain the other entries of the same step (original or copy), the Y-variables, or later variables. Mixed old/new tuples are not copy marginals.

**Transcription.** The bundle's branch list matches Theorem 5.2 exactly:
- b′0 copies X2 over {1,4..10}, using the "Y-copy of Z when X consist of all the other variables" convention with Y = X3.
- (d′1,e′1) copies (X4,X5) over {1,2,3,6,7,8,9}.
- g′2 copies X7 over {1,2,3,4,6,8,9}+e′1, with Y = (d′1, X5, X10).
- (f′3,g′3) copies (X6,X7) over {1,2,3,4,5,8,9,10}.
- h′4 copies X8 over {1,2,3,4,5,6,9,10}+f′3, with Y = (X7, g′3).

**v12c usage.**
- Publisher branch 1(a) (b′0) is **not used**.
- Extra single copies: s′0 = X1 over X{2,3,5,6,8,9}; s′1 = X1 over X{2,3,5,6,8,9,10}; s′2 = X3 over X{1,2,4,5,6,9,10}.
- Programs m0–m5 copy only originals X2, X3 and X4, one entry per step. Over-sets contain originals plus `c0`/`c1` created at earlier steps. m4 re-copies X4 with its earlier copy c1 in the over-set, which is valid.
- m2 and m3 are declared but unused.
- The structure audit found no list-valued (atomic) entry, no forward `c<j>` reference, and no copied entry inside its own over-set. Each of these defects is caught when injected.

**Per-row availability.** Every one of the 118 `copy`, 58 `xcopy` and 117 `mcopy` rows has U ⊆ its step's over-set and a valid Q. Bit masks index the branch's own variable list (base a..j = bits 0–9, then the branch's copies in creation order). The union of used bits per step equals or lies inside the over-set; for example, g′2 rows use bit 11 = e′1, and h′4 rows use bit 10 = f′3.

**Shared family vs independent branch laws.** Build publisher 1(b), publisher 1(c), s′0–s′2 and m0–m5 sequentially on Y in one probability space. Every row then holds there, and every branch marginal equals the separately built branch law (exact, control 2). No row has a coordinate that mixes branches; all coordinates lie within the row's own branch list. So both readings are valid: one construction, or independent branch laws that share only the base marginal.

**Exact copy controls** (control 2: random rational pmf on five binary variables, mimicking every v12c step shape):
- Positive: 84 marginal identities and 6 independence factorisations hold exactly.
- All nine mutations fail, each for its intended reason: U contains a Y-variable; U contains the sibling original; mixed old/new tuple; wrong tuple map; U contains a later variable; U contains the copied original (program and xcopy cases); independence including a later variable; independence with a wrong over-set. Each mismatch is exact (the pmfs differ, or the factorisation fails), and the smallest |ΔH| or CMI among them is 1.366e-3 bits.

## 7. Raw certificate v12c: decoded row types (CL7)

Top-level fields: `bound` "716/107", `branches` "gurpinar-sym", 3 `extra_single_copies`, 6 `programs`, 2,377 `multipliers`, `convention`, plus informational floats and timing. All multipliers are reduced nonzero rationals; no row is duplicated.

Decoding is my own. It rests on bundle §2, the `convention` string and Theorem 5.2. The row encoding (mask index spaces, the orientation of independence rows) is not documented anywhere I was allowed to read (**m3**). It is pinned by the identity: of the 2⁸ sign conventions for the equality types, exactly one makes it hold.

| type | n | expression (`≥0`/`=0`/`≤1`) | multiplier sign | validity on the shared family |
|---|---|---|---|---|
| mono | 37 | h(L) − h(L∖L_i) ≥ 0 | all < 0 | Shannon elemental on branch list L |
| cmi | 1504 | I(L_i;L_j\|L_K) ≥ 0 (i<j, K∌i,j) | all < 0 | Shannon elemental |
| fd | 10 | h(N[v]) − h(N(v)) = 0 | all > 0 | strategy law (§4) |
| cap | 3 (v=4,5,8) | h(v) ≤ 1 | 280/107, 288/107, 148/107 | alphabet size |
| sym | 516 | h(S) − h(g_k(S)) = 0, S ⊆ base; gen 0 = g1, 1 = g2, image direction | ± | product law (§5) |
| copy | 118 | h(U∪N_Q) − h(U∪C_Q) = 0, U ⊆ O | ± | C1 |
| independence | 3 | −I(N; E_pre∖O \| O) = 0, for (d′1,e′1), g′2, (f′3,g′3) | all < 0 (genuinely uses I ≤ 0) | C2 |
| xcopy | 58 | h(U∪s′k) − h(U∪X_S) = 0, U ⊆ T | ± | C1 |
| xindependence | 3 | −I(s′k; base∖T \| T) = 0 | all < 0 | C2 |
| mcopy | 117 | h(U∪c_s) − h(U∪X_copy) = 0, U ⊆ O_s | ± | C1, sequential |
| mindependence | 7 | −I(c_s; pre∖O_s \| O_s) = 0 | all < 0 | C2, sequential |
| dfz | 1 | RHS − LHS ≥ 0 (§8) | −1/214 | **DFZ import** + §8 substitution |

Elemental-row counts by branch: base 110; d′1,e′1,g′2 221; f′3,g′3,h′4 415; s′0 202; s′1 12; s′2 51; m0 84; m1 8; m4 433; m5 5.

Argument: ge rows carry w ≤ 0, caps carry w ≥ 0, and equality rows vanish on the family. So h(V) = Σ w·row ≤ Σ caps = 716/107, where h(V) = log_q|W| (§5).

## 8. DFZ row and conditional/union substitution (CL8)

Row `["dfz",[3,7,2,2,3,0,0,3,2],512,256,32,8,199]`, with masks over a..j:
- A = {X10}, B = {X9}, C = {X6}, D = {X4}, Z = {X1,X2,X3,X7,X8}. The five blocks are disjoint and nonempty; X5 is unused.
- The tuple equals TeX line 2088 exactly.
- Instance: 3I(A;B|Z) ≤ 7I(A;B|CZ) + 2I(A;C|BZ) + 2I(B;C|AZ) + 3I(A;B|DZ) + 0 + 0 + 3I(C;D|Z) + 2I(C;D|AZ).
- Expansion of RHS−LHS ≥ 0, recomputed by hand and by code; the h(Z) and h(Z+4) terms cancel. Notation: h(Zxy) = h(Z ∪ {X_x, X_y}).
  - −4h(Z6) −5h(Z9) −7h(Z10) −3h(Z46) +3h(Z49) +5h(Z4,10) +9h(Z69) +11h(Z6,10) +7h(Z9,10) −2h(Z46,10) −3h(Z49,10) −11h(Z69,10).

**Substitution proof.**
1. *Union.* For disjoint vertex sets, X_A = (X_v)_{v∈A} is one random variable with finite alphabet ∏[q]. DFZ's letters already denote collections: direct TeX line 105 reads "For collections $A$, $B$, and $C$ of jointly related discrete random variables", and the copy-lemma proof works over arbitrary discrete alphabets (S1|360–362). So the item holds for (X_A, X_B, X_C, X_D).
2. *Conditioning.* For each z with P(Z=z) > 0, the conditional law of (X_A,…,X_D) given Z=z is a joint law of four finite random variables, so the item holds under it. Multiply by P(z) ≥ 0 and sum. Each term Σ_z P(z)·I(X;Y|W, Z=z) equals I(X;Y|W,Z), and the empty-W term gives I(X;Y|Z). The conditional instance follows, whatever the signs of the coefficients, since it is a nonnegative mixture of valid inequalities.

The multiplier −1/214 ≤ 0 matches the ≥0 orientation. The row is **load-bearing**: dropping it, or changing b from 7 to 6, breaks the identity (control 3). It applies to Y, which is a finite-alphabet law, and it involves base variables only.

**Import status (CL8b).** I did not re-derive the item from its three copy steps; that would need an LP or Shannon-certificate search, which is excluded. Validity rests on DFZ's claim that each listed item is derivable from the listed copy steps. The author's DFZ re-derivation receipts were not opened and carry no weight here.

## 9. Infinite-validity premises, imports, dependency boundary (CL10, CL11)

Premises:
- **P1.** Def. 2.14/2.17: gn(R-minus,q) = max_F log_q|W_F|, and gn(R-minus) ≤ sup_q.
- **P2.** N(v) = the bundle table = the Fig. 2 subdivided reading, singled out by Appendix B (§3).
- **P3.** The uniform law on W gives FD, caps and the objective (§4).
- **P4.** G = ⟨g1,g2⟩ is an automorphism group of order 8.
- **P5.** The product law Y satisfies FD, caps (base q⁸), sym, and h(V) = log_q|W| (§5).
- **P6.** Constructive copy steps (DFZ kernel) give C1 and C2 on finite alphabets, sequentially (§6).
- **P7.** One shared family of all used branches; no cross-branch coordinates (§6).
- **P8.** Elemental Shannon inequalities hold on every branch list.
- **P9.** *Import:* DFZ item 3 7 2 2 3 0 0 3 2, plus the §8 substitution.
- **P10.** My row decoding, pinned uniquely by the identity (§7).
- **P11.** The exact identity and signs, with Σcaps = 716/107 (§11 boundary).
- **P12.** Conclusion: log_q|W_F| ≤ 716/107 for every q ≥ 2 and every F, so gn(R-minus) ≤ 716/107.

Conditional imports: P9 only. Standard facts used without citation: Shannon inequalities, the entropy of a uniform law, and the averaging identity for conditional mutual information.

**Not depended on:**
- the publisher LP optimum 1847/276 (old context only, unverified here);
- publisher Lemma 3.1 / Remark 3.2;
- branch 1(a); programs m2 and m3;
- the BCDRV value 59767/8929;
- checker v5, the producers, and all author receipts and controls;
- the three other bounds.

**m4.** Bundle §3 lists checker v5 and the DFZ receipts among the 716/107 dependencies. In this reconstruction they are author tooling, not validity premises; the validity premises are P1–P12.

There is no lower-bound closure, optimality or novelty claim. Note that 20/3 < 716/107 < 1847/276.

## 10. Bounded exact controls (own code; real clock, exit and hash receipts; max 120 s each; no cap reached)

| Control | Script SHA-256 | Start → end (UTC) | Exit | Cases | Output SHA-256 |
|---|---|---|---|---|---|
| 1 graph `ReviewF178RminusSources-ctl-graph.py` | 83e8c807168458f30237e650b623256167f8e91af05861982e66b3e5fe9223c3 | 15:30:39 → 15:30:40 | 0 | 20 (11 positive, 9 mutations), all as expected | `-ctl-graph-out.json` b9d85af63488d741b592acf6c88471c8b2a512b97a24d0c1913852fdf05762ea |
| 2 copy+product `ReviewF178RminusSources-ctl-copy.py` | f41fed2854bd097a0bec542651c30c1ec4fc93e9fbab40299d517eb486ed3da8 | 15:36:24 → 15:36:40 | 0 | 35 (23 positive, 12 mutations), all as expected | `-ctl-copy-out.json` 69b35726070e36a317e210bcc3d7120e243b43b80229d711f9ef6e03124122dc |
| 3 decode, run 1 (`-ctl-decode-run1.py`, copy of the run-1 script) | 89edb39fb4cd139018763c7b7d3464cfee9d2e5a8aff7eac9967554b8b1f489f | 15:39:06 → 15:39:14 | **1** | 22. Two mutation cases had inverted *expected* values (my coding error); the audit correctly flagged both defects | `-ctl-decode-out-run1-exit1.json` 785105a33254e794cedd944a9c0d4c9099434005ec0cea638f7ec82c391387bb |
| 3 decode, run 2 `ReviewF178RminusSources-ctl-decode.py` | bc0b5968d47d5c34dac1c209420a3c21d38f09101f34f7165ee19d92f5040fe9 | 15:42:03 → 15:42:12 | 0 | 22 (7 positive, 15 mutations), all as expected | `-ctl-decode-out.json` 5db6fde391bf665d41a32c5f013e9ca26c2589d2a56b310a397f0f590c489870; `-decoded-rows.tsv` ad828537f06bacbd4b434db19bf5568f1d07f9e191082bb83994e37506ea8c73 (identical in both runs) |

Control 3 mutations, each failing for its intended reason:
- duplicate JSON key; atomic-tuple entry; forward over-set reference;
- copy U containing X10 (a Y-variable of 1(b)); mcopy U containing a later copy; copy (g′2) U containing d′1; independence E containing the later g′2;
- generator labels swapped; g → g⁻¹ (both pin the convention; validity is unaffected because both are in G);
- DFZ b 7→6; DFZ row dropped; FD N(1) without 7;
- a positive cmi multiplier (sign flag); cap +1/107; a cross-branch cmi variable list.

Control inputs were pinned in-script: PDF `373e8a25…`, SVG `64142da3…`, TSV `0a96ad1a…`, certificate `6d5dc5c6…`.

## 11. Raw-arithmetic checks outside my source slice (explicit)

1. Certifying the exact identity Σ w_i·row_i = h(V) over all 2,377 rows, the sign audit, and Σcaps = 716/107. I ran these **once, only as a decoding-consistency control**, in a single same-harness implementation that passed. They are not offered as the arithmetic-slice acceptance.
2. Any rerun or audit of author checker v5 and its negative and program-mutation controls; I did not open them.
3. Provenance of `source_result_sha256` (`b488a1be…`) and `elapsed_s`. The float fields were checked only for agreement to 1e-12, for information.
4. LP optimality of 716/107, the publisher optimum 1847/276, and whether a smaller certificate exists.
5. A Shannon/LP derivation of the DFZ item from its copy steps (import, §8).
6. The other three bounds in the bundle.

## 12. Minor findings (m), detail

- **m1** (CL1). Fig. 2 is geometrically ambiguous: three straight strokes pass through mid-side nodes 7, 5 and 3. The bundle's "visually transcribed" justification does not mention this. It is resolved only by the publisher's Appendix B statements for R-minus and R, with cp_f = 10/3 as corroboration. No effect on validity.
- **m2** (CL3). Bundle §2.2 states the bound without saying it relies on §2.3 for the `sym` rows. The argument closes via the product. Presentational.
- **m3** (CL7). The v12c row encoding is undocumented in the reviewable inputs: mask index spaces, generator direction, and the −I orientation of independence rows. I reconstructed it, and the identity pins it uniquely. A documentation gap, not a validity defect.
- **m4** (CL10). The bundle's dependency list includes checker and receipts that are not validity premises, and it treats a DFZ receipt as the admission criterion. Here the DFZ item is an explicit source import.
- Source note (not about the certificate): Theorem 5.2 cites a nonexistent "Corollary 2.18".

## 13. Compliance

- Writes: only `review-v1.md` and `ReviewF178RminusSources-*` files in this wave directory. That includes the page renderings, and a redundant copy of the layout extraction that is byte-identical to input 5.
- Nothing was deleted and no input was modified (re-verified).
- No author code executed; no held payload consumed.
- Maximum run 16.5 s; no heavy compute; no LP solved.

## 14. Reviewer artifact inventory (SHA-256, bytes)

| SHA-256 | bytes | file |
|---|---|---|
| 98d1dba760d383db92948026002bfa7dd95ebbe558cf1917f0c471189b528c88 | 66399 | ReviewF178RminusSources-publisher-pdftotext-layout.txt |
| 59595d9626759ea42ed533734cc3d1f14ed5eb6566d7cfbc4cc50ff86677e3df | 345630 | ReviewF178RminusSources-p18-r200-18.png |
| 64142da3b73659d5085c072df2b01810d1b455b9f1149a3b30cb19e96402f9b7 | 236344 | ReviewF178RminusSources-p18.svg |
| 0a96ad1a7c08dffedaa6190f9728aa4f35083383b6d112b3865d7680dee551cb | 22959 | ReviewF178RminusSources-p18-words.tsv |
| ad026a74d0726c38e15a3367138887ca217bf0c611220b4d8108d043740cebf6 | 298 | ReviewF178RminusSources-p18-bbox.html (crashed partial, unused) |
| 83e8c807168458f30237e650b623256167f8e91af05861982e66b3e5fe9223c3 | 12011 | ReviewF178RminusSources-ctl-graph.py |
| b9d85af63488d741b592acf6c88471c8b2a512b97a24d0c1913852fdf05762ea | 7105 | ReviewF178RminusSources-ctl-graph-out.json |
| f41fed2854bd097a0bec542651c30c1ec4fc93e9fbab40299d517eb486ed3da8 | 12024 | ReviewF178RminusSources-ctl-copy.py |
| 69b35726070e36a317e210bcc3d7120e243b43b80229d711f9ef6e03124122dc | 8008 | ReviewF178RminusSources-ctl-copy-out.json |
| 89edb39fb4cd139018763c7b7d3464cfee9d2e5a8aff7eac9967554b8b1f489f | 15681 | ReviewF178RminusSources-ctl-decode-run1.py |
| 785105a33254e794cedd944a9c0d4c9099434005ec0cea638f7ec82c391387bb | 5097 | ReviewF178RminusSources-ctl-decode-out-run1-exit1.json |
| bc0b5968d47d5c34dac1c209420a3c21d38f09101f34f7165ee19d92f5040fe9 | 15683 | ReviewF178RminusSources-ctl-decode.py |
| 5db6fde391bf665d41a32c5f013e9ca26c2589d2a56b310a397f0f590c489870 | 5096 | ReviewF178RminusSources-ctl-decode-out.json |
| ad828537f06bacbd4b434db19bf5568f1d07f9e191082bb83994e37506ea8c73 | 338308 | ReviewF178RminusSources-decoded-rows.tsv |
