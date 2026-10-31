# Review f135: third gluing inequality L3 (12-CMI−2CI identity, universal validity, 9-variable Shannon witness)

**Verdict: 0 FATAL / 0 MAJOR / 3 MINOR.** (a) identity: HOLDS exactly; (b) universal entropy validity: HOLDS by conditional product gluing, reconstructed independently; (c) non-Shannon separation of the contracted nine-variable inequality: ESTABLISHED by an independently checked 9-variable polymatroid. The one-cut reoptimized value `+5021/3450000` is reported here as a **status claim only** (not verified, not a bound on R-minus). No novelty and no guessing-number claim is made or reviewed.

Native clock observed before composing: **2026-10-28T20:43:50-0700 PDT**. Reviewer: same-harness Claude session (`f135`, slot info-2); this is **not** human, independent-model-family, formal/kernel, or novelty clearance. Manifest `manifest-v1.json` SHA-256 `bb7a9f5221e6422f72ac3553659d3f55bf9a4186f9ae8b1022f0c8b41cd685ed` (5,192 B) verified at 2026-10-29T03:34:07Z.

## 1. Inputs read, in declared order, all SHA-256/bytes/LF rechecked and matched

| # | Role | SHA-256 (full) | bytes/LF |
|---|---|---|---|
| 1 | MANDATORY label erratum (read first) | `e6b01fe0362c99ad0a35dff4aea4a16bda7f0586a38144d1110c152913f7ed7a` | 757/8 |
| 2 | candidate `frontier-20261028-third-gluing-inequality-v1.md` | `dc51023de716613629fbcd11e57f19098e50af1a16b84c05f268153c9e6a2a61` | 5288/57 |
| 3 | author term-map checker (read only, not executed) | `c76930fcfcb09ab95e6e2be18a2a8aa5e64cb6014fb17994561575a7102f9809` | 3242/65 |
| 4 | author term-map receipt | `d3e6b6734e06403eb68efd1e8ac08fa83b6674add8f39c6bc600118eb27c54aa` | 4092/276 |
| 5 | author Shannon-witness checker (read only, not executed) | `33b781bf15aa9e8b352bb820ad12d5c7c2fb9e12eea224dcc22d0809b185e398` | 5804/113 |
| 6 | author Shannon-witness receipt (512 values used as data) | `486fe82f61fe70bef56027897f08422f8812115265bd5443c75cb524b6aea60c` | 10161/618 |
| 7 | cut receipt (independent identity) | `b2e4e3d31006c40774601f0e91bd4ba6651aba1de9b4de3c75f87d64fd1904ac` | 1847/102 |
| 8 | cross-cut scan result (read after erratum) | `c11773bfc9e3106ace76b8553fd13d308875951848e9198f5d460f332665a76c` | 865/18 |
| 9 | adopted second-gluing disposition (framework only) | `489cf7ee5899f050d70054058ec22eb04bf7cfaea814b0309edf97803b1c1a45` | 4701/33 |

Erratum applied: input 8's `limits` text "one second gluing inequality" is read as "one third gluing inequality"; its `cut_receipt_sha256` (`b2e4e3d3…`) and the numeric count/minimum fields are unchanged. No author checker was executed or imported. No web search, external model, Git, deletion, or publication action was taken.

## 2. Reviewer controls (all exact unless stated; receipts carry `/bin/date` start/end stamps and script SHA)

| Artifact | SHA-256 |
|---|---|
| `reviewer-identity-check.py` | `00db2972ee805fd93841b190dbfcfdf72cb78598b9b47d256e77b4e1d519c17a` |
| `reviewer-identity-check-receipt.json` | `ad2fd28284cdf6eaae7e7451521c7c70e710e01ab4c17afbfdf7f190c99c01a4` |
| `reviewer-gluing-finite-law-control.py` | `d7fcfb1da22f73ba307b8fc8ad493b85d9ee6282271de802152ae4f3eb4dad59` |
| `reviewer-gluing-finite-law-control-receipt.json` | `62246af6c6aea522d5932362a72a69592828bca2ee1b02a940536f408f38eb59` |
| `reviewer-nine-variable-witness-check.py` | `598fab71530afab859c9ed5028ebb09fc2a2a23c9ec6f0f490d0cd5848408e5e` |
| `reviewer-nine-variable-witness-check-receipt.json` | `e3a5f6f406c71aff124424d57c1085a735717c7ee9cc0fa4acf27662bcf21620` |

Run clocks (UTC): identity 03:39:32.441–03:39:32.448; gluing 03:40:51.876–03:41:02.958; witness 03:42:13.800–03:42:15.085 (2026-10-29). Python 3.14.3, `fractions`/`decimal` only; no scipy present, so the Shannon-cone check is an exact feasibility check rather than an LP (stronger, not weaker).

## 3. (a) The 18-term expression and the 12-CMI−2CI identity — HOLDS

Reconstruction. The 18 terms were hand-transcribed from the candidate's LaTeX block into `L3_TERMS` (coefficient, variables), and the 12 CMI rows from its table into `CMI_ROWS`; a reviewer-written parser of the frozen text then confirmed `latex_block_equals_hand_transcription: true` (18 terms) and `table_equals_hand_transcription: true` (12 rows). Structure of `L3`: 18 distinct subsets, coefficient sum 0, **0 mixed D,F terms**, 3 X-only / 5 D-only / 10 F-only terms, every term contains the background `{a,c,h}`, max |coefficient| 2.

Identity. With `I(A;B|C) = H(AC)+H(BC)−H(ABC)−H(C)` expanded on exact integer coefficient maps, `Σ_{k=1}^{12} I_k − 2·I(D;F|abcdefghij)` equals `L3` **exactly** (difference map empty). Fourteen distinct mixed D,F subsets appear before cancellation and all fourteen cancel; the two non-mixed subsets `abcdefghiF` (rows 4 and 9) and `abcehiD` (rows 6 and 12) also cancel, leaving exactly the 18 written terms. I also expanded the twelve rows by hand before coding and obtained the same tally.

Negative controls (20, all rejected): altered coefficient sign of `H(abcehi)`; coefficient 2→1 on `H(abcdefghij)`; removed term `H(abcdfhjF)`; **each of the 12 CMI rows removed individually**; independence weight −2→−1 and −2→0; conditioning of row 6 enlarged by `j`; conditioning of row 1 missing `F`; row 11 replaced by a duplicate of row 12.

Cross-check against author data: my term map equals the cut receipt's 18 `known_terms` masks (bit order a..j,D,F) and the term-map receipt.

## 4. (b) Universal entropy validity by conditional product gluing — HOLDS

**Gluing lemma (reviewer statement).** Let `P` be a law on finite alphabets for `(X,D,F)` with `X=(a,b,c,d,e,f,g,h,i,j)`. Define `Q(x,d,f) = P(x)·P(d|x)·P(f|x)` where `P(x)>0`, else 0. Then (i) `Q` is a law; (ii) `Q_{XD}=P_{XD}` and `Q_{XF}=P_{XF}`, hence `H_Q(S)=H_P(S)` for every `S ⊆ X∪{D}` and every `S ⊆ X∪{F}`; (iii) `Q(d,f|x)=Q(d|x)Q(f|x)`, so `I_Q(D;F|X)=0`. **Glued variables: `D` and `F`; gluing (conditioning) set: the full original vector `X`.**

**Proof of `L3 ≥ 0` for every finite law.** `L3` has no mixed D,F term (§3), so by (ii) `L3(P)=L3(Q)`. The identity of §3 is a formal identity of set functions, so at `Q`: `L3(Q)=Σ_k I_k(Q) − 2·0 ≥ 0`, each `I_k(Q)` being a conditional mutual information of the law `Q`. Hence `L3(P) ≥ 0`. The half-space `L3 ≥ 0` is closed, so the almost-entropic closure satisfies it. No functional dependence or prior independence is used. This matches the candidate's argument; the one wording point is MINOR-2 below.

**Exact finite-law controls (reviewer, four laws, all PASS).** For each law: `Q` sums to 1, `Q_{XD}=P_{XD}` and `Q_{XF}=P_{XF}` as exact rational dictionaries, and `Q(x,d,f)·Q(x)=Q(x,d)·Q(x,f)` for every atom (exact conditional independence). Entropies at 60-digit `Decimal`: identity residual `0` at `P` and at `Q` (to 1e-50), `L3(P)=L3(Q)` (to 1e-45), `L3(Q)=Σ glued CMIs`, all twelve glued CMIs ≥ 0, `L3 ≥ 0`. All four laws have `I_P(D;F|X)>0` so the negative term is active: random full-support 12-bit law (`I_P=0.0756`, `L3=0.1726`); sparse random law, 1,463 atoms (`I_P=0.1628`, `L3=1.3114`); full-support law with ternary `D,F`, 9,216 atoms (`I_P=0.1294`, `L3=0.1348`); `D=F=` fair coin independent of `X` (`I_P=1` bit exactly, `L3=0.1443`, one glued CMI exactly 0).

**Wrong-conditioning control.** Gluing on `X∖{j}` preserves `Q_{XD}` but **not** `Q_{XF}` and changes `L3` (0.1726→0.1544): the full-`X` conditioning set is load-bearing. **Negative identity control at a finite law:** dropping row 1 leaves residual 0.0166 ≠ 0.

## 5. (c) Nine-variable contraction and non-Shannon separation — ESTABLISHED

**Contraction.** Every term contains `{a,c,h}` and the coefficient sum is 0, so `L3 = Σ_S c_S H(S∖{a,c,h} | a,c,h)`, i.e. the 12-variable inequality is the conditional (on `(a,c,h)`) form of a 9-variable inequality on `(b,d,e,f,g,i,j,D,F)`; conversely setting `a,c,h` constant recovers the 9-variable form. My contraction (bit order b,d,e,f,g,i,j,D,F) gives exactly the author's table `[(37,−1),(60,−1),(127,2),(173,1),(188,1),(236,−1),(237,1),(255,−2),(293,1),(300,−1),(316,1),(317,−1),(331,−1),(347,1),(364,1),(365,−1),(367,1),(383,−1)]`, coefficient sum 0. Independently of the contraction argument, the **9-variable identity holds directly**: `L3^(9) = Σ_k I_k' − 2·I(D;F|bdefgij)` with `a,c,h` deleted from every conditioning set (rows listed in the receipt), so the §4 gluing proof applies verbatim on nine variables with `X'=(b,d,e,f,g,i,j)`.

**Witness.** The 512 rational coordinates `nine_variable_primal_values` of receipt #6 were loaded as data (receipt SHA re-pinned). Reviewer enumeration of Yeung's elemental inequalities for n=9 yields 9 + C(9,2)·2^7 = **4,617** rows; the witness has `h(∅)=0` and **0 violations**. Redundant full-axiom check: 0 violations over all 2,304 single-element monotonicity steps and all **130,816** submodular pairs `h(S)+h(T) ≥ h(S∪T)+h(S∩T)`. Hence the witness lies in the 9-variable Shannon cone Γ₉. Its value is **`L3^(9) = −7123/3450000`** exactly (negative). Also exact: `I(D;F|bdefgij) = 8043/23000` (matches the receipt field); the twelve 9-variable CMIs at the witness are `31/500, 1259/69000, 0, 42163/575000, 0, 1687/143750, 0, 0, 0, 4807/25000, 31721/150000, 9219/71875` (all ≥ 0, five exactly 0), and `Σ I_k − 2·CI = L3^(9)` reproduces −7123/3450000.

**Classification.** `L3^(9) ≥ 0` holds on all entropic (hence almost-entropic) 9-variable vectors by §4–§5, yet fails at a point of Γ₉; therefore it is not a nonnegative combination of elemental Shannon inequalities, i.e. it is **non-Shannon-type on nine variables**, and the witness lies outside the almost-entropic closure. This is a cone classification only; whether it is implied by known non-Shannon inequalities (e.g. Zhang–Yeung and successors) is a novelty question not assessed here.

**Positive controls (must be ≥ 0, all pass):** uniform matroids U_{k,9}, k=1..9 (values 0,0,0,1,3,3,3,0,0; all 4,617 rows satisfied); a modular function (L3=0); the entropic vector of a random 9-bit law (0 elemental violations to 1e-40, L3=0.2009). **Negative controls (all rejected):** nonzero `h(∅)`; `h(full)` lowered by 1e-6 (monotonicity breaks); coordinate 37 raised by 1/7 (elemental breaks); a missing coordinate; altered coefficient on mask 37 (value becomes 5505959/1150000), removed term mask 331 (27560017/6900000), coefficient 2→1 on mask 127 (−12744623/3450000) — each changes the value from −7123/3450000.

## 6. The one-cut reoptimized value `+5021/3450000` — STATUS ONLY, not verified

The candidate states that adding the displayed `L3` cut and reoptimizing the second star branch yields a candidate `e31643a1…` with `L3 = 5021/3450000 > 0`, verified by a separate checker/receipt (`93171f8c…`/`cbbdb5f8…`). Neither that candidate nor its receipt is among the frozen inputs, so this review **does not verify** the value. Consistency check against the pinned star constraints only: (i) the cross-cut receipt #8 pins `new_star_sha256 = e31643a1…`, equal to the candidate's cited SHA, and `cut_receipt_sha256 = b2e4e3d3…` (input #7); (ii) its `new_point_exact_scan` reports 5,443,200 (= 10!/3! · 9) active-role permutations with `negative_count 0` and minimum `1697/1725000 = 3394/3450000 ≤ 5021/3450000`, consistent with the claimed value being one scanned instance; (iii) the `old_point_negative_control` reports 18 negatives with minimum `−17569/6900000`, which is more negative than the displayed `−7123/3450000`; the candidate does not claim the displayed cut is the most violated, so no conflict. Metadata-only step disclosed: I hashed (did not read) the seven files cited in the candidate's Evidence section; all exist with exactly the cited SHA-256s. **This value is not a bound on R-minus**, carries no entropic realization, and the candidate itself says no graph improvement follows.

## 7. Findings

- **MINOR-1 (labels, not covered by the erratum).** Author checker #3's docstring says "16-term inequality" (the code and receipt say 18); author checker #5's docstring says "second cross-copy gluing cut" although it binds the third inequality. The erratum corrects only receipt #8's `limits` text. Math unaffected; an additive label erratum for these two docstrings would close the copied-label pattern.
- **MINOR-2 (wording).** "proves the inequality from the twelve nonnegative CMIs" should read "the twelve CMIs **of the glued law**"; at the original law the identity includes `−2I(D;F|X)` (controls in §4 show `I_P(D;F|X)` up to 1 bit). Same point as f122's MINOR.
- **MINOR-3 (reproducibility boundary).** The 12-variable statements — the star primal's `L3=−7123/3450000` at `D=g'2,F=f'3`, the 67,596-row 12-variable polymatroid "without conditional independence", the 45,360/272,160 first/second-family scans, and the provenance of the 512 contracted values — rest on files outside the frozen inputs (`aadf8410…`, `1037f7da…`, `437b5045…`, `c22fab73…`, `fc526f67…`) and are **not verified here**; they are consistent with the receipts read (contracted value and `I(D;F|X)=8043/23000` agree). The non-Shannon classification in §5 does not depend on them.

## 8. Explicit dependencies of each verdict

- **(a) identity HOLDS:** depends only on the frozen candidate text (SHA `dc51023d…`) and reviewer code `00db2972…`; unconditional.
- **(b) universal validity HOLDS:** depends on (a), the standard nonnegativity of conditional mutual information, and the gluing lemma of §4 (reviewer-proved; exact finite-law controls `d7fcfb1d…`); unconditional for finite laws, and for the almost-entropic closure by half-space closedness.
- **(c) non-Shannon separation ESTABLISHED:** depends on (a), (b), the contraction/9-variable identity (reviewer-verified), and the 512 coordinates in receipt #6 (SHA `486fe82f…`) checked by reviewer code `598fab71…` against reviewer-enumerated elemental rows and full polymatroid axioms. It does **not** depend on the 12-variable provenance of those coordinates.
- **One-cut value `+5021/3450000`:** status claim only; dependencies outside inputs (MINOR-3); not a bound on R-minus.
- **Not assessed:** novelty/prior-art, guessing-number or R-minus implications, entropic realizability of any LP point, and the f110 inputs (unchanged per erratum scope).
