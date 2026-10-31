# dual-review-v1 — f110-rminus-full-copy-lp-optimum

**Reviewer artifact prefix:** `dual-` · **Native clock (report written):** 2026-10-28T19:44 -0700 PDT (manifest observed 19:23:37; checker run 19:42:00–19:42:03 PDT) · **Host:** macOS 27.0.1 arm64, Python 3.14.3, numpy 2.4.3, poppler pdftotext/pdftoppm 26.04.0.

**Headline verdicts**

| Item | Verdict | One-line basis |
|---|---|---|
| Source correspondence (Theorem 5.2 / cross-branch remark) | **MINOR** — mis-citation; content exact | Copy protocol, three elemental sets, caps/FDs/symmetry all match the pinned paper; but the cross-branch-exclusion statement is **Remark 5.4**, not Remark 3.8 (Remark 3.8 is about [1] using non-Shannon inequalities instead of copy constraints). |
| 1,920-row publisher dual identity | **PASS (no finding)** | Own parser: all 1,920 PDF rows and TXT rows bound by position; every TXT name independently decoded and equal to its PDF expression; every row classified and valid; every row inside one branch set; Σ c_r·row_r ≡ H(V) exactly and Σ c_r·rhs_r = 1847/276. |
| Exact primal feasibility and LP optimum 1847/276 | **PASS (no finding)** | Own integer check of 28,171 + 159,757 + 159,757 elemental rows, 257 + 642 + 1,282 copy equalities, FDs, caps, generator symmetries, objective, and tightness of all 1,920 rows; weak duality then gives optimum exactly 1847/276. |
| F_n all-n proof and all-disjoint-substitution arithmetic | **PASS (no finding)** | E_k identity machine-verified modulo the two stated CIs; recurrences numerically confirmed on random copy constructions; family coincides with a published DFZ/Matúš-type infinite family (public PDF fetched); own enumeration of 13,729,980 substitutions, all n ≥ 1, minimum 2F_n = 0. |
| Candidate's overall claim as scoped | **VERIFIED, same-harness** | Exact no-improvement statement for the specified three-branch LP plus all disjoint original-variable F_n; no entropic realization and no guessing-number improvement is implied, and none is claimed. |

Nothing FATAL or MAJOR was found. The one MINOR item is a citation error that should be corrected by an additive erratum (it also propagates into the manifest `scope` text). All verification here is same-harness Python written by this reviewer; it is not independent-family, human, formal/kernel, or novelty verification.

---

## 0. Scope, imports, and pins

* Manifest `manifest-v1.json` read first. All ten inputs re-hashed: every SHA-256, byte count, and LF count equals the manifest (observed 19:24:14 PDT). Inputs were read in manifest order; the four large JSON profiles were parsed in full by my own code (not printed).
* Publisher sources used at the actual bytes: paper PDF `public-sources/gurpinar-kybernetika60-2024-553-575.pdf` SHA-256 `373e8a25…46d8` (502,687 B); Annex C certificate TXT `b0bd3f61…8b22`, PDF `8befddb0…ec6b`, ZIP `09b3bcbd…f6d0`, and the pinned `pdftotext -layout` derivative `6ff906bb…c2ca5`. My own `pdftotext -layout` of the paper reproduces the existing `gurpinar-publisher-layout-v1.txt` byte-for-byte (SHA-256 `98d1dba7…28c88`, saved as `dual-paper-layout.txt`).
* Public primary source additionally fetched directly (no web_search): Dougherty–Freiling–Zeger, *Non-Shannon Information Inequalities in Four Random Variables*, arXiv:1104.3602 PDF, SHA-256 `0e46a170…52b3` (`dual-dfz-1104.3602.pdf`, layout text `dual-dfz-layout.txt`).
* No author checker was imported or executed. The only code run is `dual-check-v1.py` (SHA-256 `6149cf44…06f4d`), standard library + numpy, producing `dual-check-v1-result.json` (SHA-256 `c47938e6…bbe47`), wall time 2.67 s. Two heredoc patches during development (sym-name grammar; JSON key serialization) are visible in the shell transcript; the hashed script is the final one.
* Not done, by instruction: no author contact, no Git, no deletion, no external model/paid API, no held payloads. Files written by a sibling reviewer (prefix `primal-`) appeared in this directory during the review and were **not read**; sibling candidate files named `frontier-20261028-crossbranch12-*` exist in the evidence root, are outside this manifest, and were **not read**.

## 1. Source correspondence — Theorem 5.2 reconstructed at the pinned text

**1.1 Copy lemma semantics (Lemma 2.10, p557–558).** "Z′ is a Y-copy of Z over X" means (entropic form, item 2): every sub-vector of (X,Z) has the same entropy as the corresponding sub-vector of (X,Z′), and I(Z′ : Y,Z | X) = 0; when "over X" is omitted, X is all other variables.

**1.2 Theorem 5.2 proof text (p571), my transcription with the audit's letter names a…j = X₁…X₁₀:**

| Paper step | Z (copied) | Z′ (name) | X = conditioning base | Y (rest) | CI row implied |
|---|---|---|---|---|---|
| 1(a) X₂′ is a X₃-copy of X₂ | b | b′0 | a d e f g h i j | c | I(b′0; b,c \| a,d,e,f,g,h,i,j)=0 |
| 1(b) (X₄″,X₅″) is a X₁₀-copy of (X₄,X₅) over X₁X₂X₃X₆X₇X₈X₉ | d,e | d′1,e′1 | a b c f g h i | j | I(d′1,e′1; d,e,j \| a,b,c,f,g,h,i)=0 |
| 1(b) X₇‴ is a (X₄″,X₅,X₁₀)-copy of X₇ over X₁X₂X₃X₄X₅″X₆X₈X₉ | g | g′2 | a b c d e′1 f h i | d′1, e, j | I(g′2; d′1,e,g,j \| a,b,c,d,e′1,f,h,i)=0 |
| 1(c) (X₆⁗,X₇⁗) is a copy of (X₆,X₇) over X₁X₂X₃X₄X₅X₈X₉X₁₀ | f,g | f′3,g′3 | a b c d e h i j | ∅ | I(f′3,g′3; f,g \| a,b,c,d,e,h,i,j)=0 |
| 1(c) X₈⁗′ is a (X₇,X₇⁗)-copy of X₈ over X₁X₂X₃X₄X₅X₆X₆⁗X₉X₁₀ | h | h′4 | a b c d e f f′3 i j | g, g′3 | I(h′4; g,g′3,h \| a,b,c,d,e,f,f′3,i,j)=0 |

For every step X ∪ Y ∪ Z equals exactly the variables already existing in that branch (checked programmatically), which is the paper's "over X" convention. The five CI rows above are **literally** the certificate rows `copy02, copy12, copy22, copy32, copy42` (§2). The audit's table (steps 0–4) is therefore an exact translation of Theorem 5.2's primes into the Annex C names.

**1.3 Every LP condition (Corollary 3.7 instantiated by the proof of Theorem 5.2):** (i) h(X_i) ≤ 1 for the ten originals only; (i′) ten FD equalities h(N(i) ∪ i) = h(N(i)); (ii) copy equalities for the five steps — all sub-vector marginal equalities (256 / 384+256 / 768+512) plus the five CI equalities (257 / 642 / 1,282 per branch, matching the candidate's table); (iii) elemental inequalities **only** on the three sets {11 vars: a…j,b′0}, {13: a…j,d′1,e′1,g′2}, {13: a…j,f′3,g′3,h′4} (n + C(n,2)·2^(n−2) = 28,171 / 159,757 / 159,757); (iv) symmetry equalities on original-variable subsets under Aut(R⁻); objective max h(a…j). The candidate's "16,383 distinct coordinates" equals 1,023 + 1,024 + 7,168 + 7,168 (verified).

**1.4 Cross-branch scope — the citation error.** The paper's statement that inter-branch Shannon rows were omitted is **Remark 5.4** (p572): "we did not take all the elemental information inequalities for all the combinations of old and new random variables. For example there is no Shannon-type inequality involving both X₂′ and X₄″ in the first linear program … Our choice of the sets … follows from the applications of the copy lemma: a copy variable used in order to define another copy variable is put in the same set as the latter." **Remark 3.8** (p566) instead reads: "In [1] non-Shannon-type inequalities were added to such a linear program instead of item (ii) (the copy lemma constraints)." The candidate text ("Remark 3.8 says that cross-branch Shannon inequalities such as one involving both b′0 and d′1 were not included") and the manifest scope ("by the cited Remark 3.8") therefore cite the wrong remark; the substantive content (and the b′0/d′1 ≙ X₂′/X₄″ example) is correct. **MINOR**; fix by additive erratum. Omitted scope quantified: a full 17-variable elemental system has 17 + 136·2¹⁵ = 4,456,465 rows; the three-branch LP has 324,625 distinct elemental rows (347,685 with the original 11,530 counted thrice), so 4,131,840 cross-branch elemental rows are absent, and no cross-branch copy/independence equality is imposed. (Paper typo noted, immaterial: the proof says "as in Corollary 2.18"; the paper has Proposition 2.18 and Corollary 3.7.)

**1.5 Graph and symmetry group.** Figure 2 (p570) was rendered by me at 200–2000 dpi (`dual-paper-p570-18.png`, `dual-fig2-*.png`). The three publisher FD rows pin N(1)={2,3,4,5,6,7}, N(2)={1,3,7,9,10}, N(6)={1,5,7,8,9}; propagating through the Appendix B generators σ=(1 8)(2 10 5 9)(3 7 4 6), τ=(2 5)(3 6)(4 7) closes consistently to a 26-edge graph (degrees 6,5,5,5,5,5,5,6,5,5; 3–4 present; 9–10 absent), which agrees with the figure. Brute force over the 2·8! permutations preserving the degree-6 pair {1,8} finds exactly 8 automorphisms, equal to ⟨σ,τ⟩ — confirming the paper's Aut(R⁻)=⟨σ,τ⟩ and that generator rows imply the full group's symmetry constraints.

## 2. The 1,920-row dual — independent replay

Own parser of the pinned PDF layout: 1,920 rows, 5,751 `H{` tokens consumed = total, 63 non-row lines = 4 header lines + 59 page numbers. TXT: header `Objective Value = 1847/276` + 1,920 `name = value` lines; **0 coefficient mismatches by position**. Independently decoded name grammar (closing the audit's stated open boundary "TXT names not decoded"): `csti{b}set{p}/{q}/{m}` = I(X_p;X_q|X_m) in branch b+1 with bits over the sorted branch variables; `csti{b}set{p}/{p}` = H(X_p | rest of branch); `sym{g}/{moved-mask}/{fixed-mask}` = H(S) − H(g·S) for g ∈ {σ,τ}; `copy{s}1at{T}n{S}` = H(S∪T) − H(S∪T′) for step s; `copy{s}2` = the step-s CI; `la,lb,lf` = H(N(v)) − H(N(v)∪v) ≥ 0; `la2,lb2,lf2` = H(v) ≤ 1. **All 1,920 decoded expressions equal the PDF expressions exactly.**

Name-independent semantic classification of the PDF rows:

| Kind | Rows | Validity check applied | Coefficient sign |
|---|---:|---|---|
| Elemental CMI I(i;j\|K) ≥ 0 | 958 | exact set algebra; \|A\|=\|B\|=1 for all | all ≤ 0 ✓ |
| Elemental conditional entropy H(i\|rest) ≥ 0 | 22 | T ⊂ S, \|S∖T\|=1, S = branch set | all ≤ 0 ✓ |
| FD written as ≥ 0 | 3 | S = N(v) exactly, v ∈ {a,b,f} | all ≤ 0 ✓ |
| Symmetry equality | 456 | T = g·S with g ∈ Aut(R⁻); all 456 use a generator | unrestricted |
| Copy marginal equality | 473 (56/75/30/204/108 by step) | S ⊆ X_step, ∅≠T ⊆ Z_step | unrestricted |
| Copy CI equality | 5 (one per step) | equals I(Z′;Y,Z\|X) of the step verbatim | unrestricted |
| Cap H(v) ≤ 1 | 3 | original singleton | all ≥ 0 ✓ |

Unrecognized rows: 0. Rows outside every branch set: 0. Branch signature: 119 rows need branch 1 only, 429 branch 2 only, 868 branch 3 only, 504 are original-only (inside all three): 623 / 933 / 1,372 rows lie inside branches 1/2/3 — identical to the candidate's "publisher rows checked tight" column. **Dual identity:** Σ_r c_r·(row_r LHS) = H(a,b,c,d,e,f,g,h,i,j) exactly (all 15,360 auxiliary-coordinate terms cancel); Σ_r c_r·rhs_r = 191/138 + 743/276 + 361/138 = 1847/276. Coefficient denominators have LCM 79,488. Random-law control: on laws built by the five copy kernels, all 478 copy rows vanish (max |value| 1.8e−15) and all 980 Shannon rows are ≥ −2.7e−15, while the three FD rows are strictly negative (≈ −0.68), confirming they are FD-dependent rows rather than generic inequalities.

Every dual row is thus a constraint of the LP in §1.3 (or its FD equality in one direction), so the dual certifies **optimum ≤ 1847/276** for exactly that LP.

## 3. Exact primal feasibility — independent integer replay

Base profile: 4,397 coordinates, of which the 1,023 original-variable coordinates were imported; all ten singletons = 1; h(V) = 1847/276; balance expression h(V) − (2/3)Σh(v) = 7/276. Each branch file supplies exactly 1,024 / 7,168 / 7,168 auxiliary coordinates within its variable set; merged with the originals each branch is a complete 2ⁿ−1 vector. Integer scales (LCM of denominators): 32,430,000 / 324,300,000 / 32,430,000.

| Branch | Elemental rows checked (all ≥ 0) | tight CMI / tight H(i\|rest) | Copy equalities (all exact) | FD / caps / generator-symmetry | Objective |
|---:|---:|---:|---:|---|---|
| 1 (11 vars) | 28,171 | 7,313 / 10 | 256 + 1 = 257 | 10 / 10 / 2,046 ✓ | 1847/276 ✓ |
| 2 (13 vars) | 159,757 | 13,100 / 10 | 640 + 2 = 642 | 10 / 10 / 2,046 ✓ | 1847/276 ✓ |
| 3 (13 vars) | 159,757 | 19,962 / 12 | 1,280 + 2 = 1,282 | 10 / 10 / 2,046 ✓ | 1847/276 ✓ |

All 1,920 publisher rows are **exactly tight** on the merged profiles (per-branch 623 / 933 / 1,372, including original-only rows). Candidate's "crucial coordinate boundary" reproduced: the base file's older partial auxiliary coordinates differ from the new branch values in 4/302, 243/1070, 460/2002 shared coordinates, so the primal is the 1,023-coordinate original projection plus the three new extensions, not an extension of the old 4,397-coordinate assignment. Primal feasible with objective 1847/276 ⇒ optimum ≥ 1847/276; with §2, **the specified three-branch LP has optimum exactly 1847/276**.

## 4. F_n family — proof, literature identity, and exhaustive arithmetic

**4.1 Written proof (all-order text §1).** Verified step by step: B_j = I(R_{j+1};A,B|S_j) ≥ 0 and d_j = I(R_{j+1};B|A,S_j) + I(R_{j+1};A|B,S_j) ≥ 0 by the conditional i.i.d. construction; a_{j+1} = a_j − B_j + d_j is the chain-rule identity I(A;B|S,R) = I(A;B|S) − I(A;R|S) − I(B;R|S) + I(A,B;R|S); d − d_j = I(R_{j+1};S_j|A) + I(R_{j+1};S_j|B) ≥ 0; I(S_k;A,B|C) = Σ_{j≤k} B_j by conditional exchangeability of C,R₁,…,R_{k+1}; the E_k identity was **machine-verified as exact linear algebra** on the 31-dimensional (A,B,C,D,S) entropy space: LHS − RHS = −I(S;D|A,B) − I(S;D|A,B,C), both zero under the stated independences (S ⊥ (C,D) | (A,B) gives both). Telescoping and the final decomposition F_n = Σ_k E_k + a_{n+1} + Σ_j (n−j+1)(d−d_j) check by hand and numerically (random laws, alphabets 2–3, n = 1…4, worst recurrence/decomposition error 1.3e−14). Conditioning on Z by averaging is legitimate because every term is a conditional information quantity. The proof is **correct for all n ≥ 1 and all finite joint laws**.
**4.2 Literature identity (public source fetched).** DFZ arXiv:1104.3602, proof of Theorem 12 (p36 of the layout), derives "iterating Rule 2 … the infinite list: sI(A;B) ≤ (s+1)I(A;B|C) + (s(s+1)/2)I(A;C|B) + (s(s+1)/2)I(B;C|A) + sI(A;B|D) + sI(C;D), where s is any non-negative integer" — this is F_s ≥ 0 verbatim (F₁ is Zhang–Yeung). The family is therefore a known, published valid information inequality family (Matúš-type; DFZ Rule 2), consistent with the author's explicit "no novelty" statement.
**4.3 Exhaustive substitution scan (own enumeration).** Base scale 25,944 (as claimed). Enumeration by disjoint nonempty (A,B) with A<B numerically (28,501 pairs) and vectorized base-4 assignment of the remaining variables to {none,C,D,Z}, different from the author's base-6 split: **13,729,980 substitutions**, equal to the inclusion–exclusion count (6¹⁰ − 4·5¹⁰ + 6·4¹⁰ − 4·3¹⁰ + 2¹⁰)/2. For each: a,d ≥ 0; if d = 0 then c = a − Δ ≥ 0 (else F_n would fail for large n) and F₁ ≥ 0; if d > 0 the integer minimum of the convex quadratic 2F_n = 2a + 2nc + n(n+1)d over n ≥ 1 is at max(1,⌊n*⌋) or that +1 with n* = −(2c+d)/(2d), both evaluated exactly plus n = 1. Result: no violation; **minimum 2F_n = 0**, attained at A={a}, B={b}, C={e}, D={d}, Z=∅, n=1 (Zhang–Yeung tight on this point); largest vertex-neighbour n examined 23; elapsed 2.35 s. Empty-block cases reduce to original Shannon rows as the author states. The all-order text's earlier example (A={2},B={10},C={6},D={3,4},Z={1,5,8,9}) evaluates on **this** profile to a = 11/276, Δ = 563/12972, d = 1/6486, F₁₂ = 121/12972 > 0 (the −1/276 value belonged to the earlier, superseded point, which is not an input here). Since F_n rows use original coordinates only, they hold on all three merged branch profiles; the dual is unchanged, so **adding every disjoint original-variable F_n for every n leaves the optimum at 1847/276**.

## 5. Remaining boundaries (unchanged by this candidate, none inferred)

* **Not entropic.** The primal is a Shannon/copy-LP point. Nothing here shows it is (almost) entropic; the 7/276 balance gap is a property of an LP point only, and no FD-law or strategy is implied.
* **Exact 17-variable boundary.** The LP with all 4,456,465 elemental rows on the 17 variables (and any cross-branch equalities a joint construction would add, e.g. independence of branches given the originals, which the audit notes is realizable) is **not** solved by this packet; its optimum lies in [gn(R⁻), 1847/276] and could be strictly smaller. The sibling `crossbranch12` material is outside this manifest and was not reviewed.
* **Guessing number.** gn(R⁻) ∈ [20/3, 1847/276] ≈ [6.6667, 6.6920] exactly as in the paper; no new upper or lower bound.
* **Family coverage.** Only disjoint original-variable substitutions of this one family are covered. Not covered: overlapping blocks, substitutions using auxiliary variables inside a branch, other non-Shannon families (e.g. DFZ's Rule-1 list, Matúš lists (80)/(81)), additional copy steps, or symmetric copies.
* **Independence.** Author checkers and this review were produced in the same harness family; the publisher extraction (`pdftotext`) is shared; no human, formal/kernel, cross-vendor, or novelty verification is claimed. The paper's priority stands.

## 6. Reproducibility receipt

```
cd <this review directory>
python3 dual-check-v1.py        # 2.67 s; writes dual-check-v1-result.json (open 'x': delete/rename to rerun)
```
Own artifacts (SHA-256): `dual-check-v1.py` 6149cf4453072e22528638f66689a7deac851b1612133c0f5289fb8b07106f4d · `dual-check-v1-result.json` c47938e6e357238e9edf6eb2bfa100e9edd2a6d58273a7964dd15d7d4f1bbe47 · `dual-paper-layout.txt` 98d1dba760d383db92948026002bfa7dd95ebbe558cf1917f0c471189b528c88 · `dual-dfz-1104.3602.pdf` 0e46a1700e59d99a6dafc6340d87ac85f9709ff91d1d539409f060ba39cd52b3 · `dual-dfz-layout.txt` 61d9fd812c788f559ec218d51080c011f6d83d4b38a56d7dfd9ba45a25974f46 · `dual-paper-p570-18.png` 59595d96…e3df · `dual-fig2-zoom-18.png` f6df2cf7…c417 · `dual-fig2-bottom-18.png` 72805795…7834 · `dual-fig2-v10-18.png` 51c53e38…9b49 · `dual-fig2-v9-18.png` 0509eabb…993a. The automorphism brute force and the sym/copy name surveys were one-off shell commands recorded in the session transcript; their results are restated in §1.5 and §2.

**Disposition requested of the parent:** accept the candidate's scoped exact-optimum claim as same-harness verified; attach an additive erratum changing "Remark 3.8" to "Remark 5.4" in the candidate text and in the manifest scope wording; keep the entropic-realization, 17-variable, and guessing-number items open.

**END.**
