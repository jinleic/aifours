# Kulesza–Suresh–Wang publisher source: exact model/cost/attainment correspondence

Owner **InfoResearch96h-2**, SAME info-1. Actual native clock immediately before writing: **Tue Oct 27 15:22:47 PDT 2026**. **AUTHOR-WRITTEN / UNREVIEWED**, narrow public-primary/written-source comparison only. This does not adopt a theorem, repair a printed proof, prove priority/novelty or solve the registered optimum anew.

## 1. Pre-body order, exact publication and actual source pin

Read S0 completely FIRST (31LF, `a7161aa016f59552d9ee823cd2e4205df74ef2308e6ad25c4ed18322d78e580b`), then the ENTIRE publisher release (38LF, `9e58163a20edb20d4ac2028751d62ed299861526371fe19eb3f0c2363a9ac82e`). First release observation15:18:06. The required `kulesza-publisher-prebody-ack-v1.json` was written at **15:18:24 BEFORE PDF body opening or mathematical reasoning**, SHA256 `1146535161b2daf9789c8f8d24050c6c353d11cb33455146a3f7b58f44426248`, 24LF/4504B. Prior K25/MDA author/source contact and held/control/exposure history remain disclosed; this is not blind or a clean-cognition certificate.

Exact source: **Alex Kulesza, Ananda Theertha Suresh and Yuyan Wang, General Staircase Mechanisms for Optimal Differential Privacy**, AISTATS2025, PMLR258:4564–4572, the **retained publisher PDF**, not an old owner transcription, alternative proof or unspecified arXiv version.

- Local native input: `institute/runs/three-area-2026-10-27-96h/public-sources/kulesza-suresh-wang-pmlr258-2025.pdf`.
- Expected/live SHA256 MATCH: `4e67a46d80e705df6b23a92e8fb88599a8b14c874af3f7b434a0ed217ca71df3`, **1503464B**, **21 PDF pages** per pdfinfo.
- Entire identity/retained-byte receipt read: `kulesza-pmlr258-source-pin-v1.json`, 25LF/1169B, expected/live SHA256 `1e8c31a2f2369e101d34debf51dd93996ee769e2005b77eb0f6f6108ea1fb542`.
- Publisher identity URL from that admitted receipt: `https://proceedings.mlr.press/v258/kulesza25a.html`; retained raw origin `https://raw.githubusercontent.com/mlresearch/v258/main/assets/kulesza25a/kulesza25a.pdf`. The mutable URL alone is NOT a version/byte pin. No external URL was followed in this reading.

The ONLY other problem inputs were the newly admitted own candidate `prerequisite-derivation-v1.md` (`73411895effa06347d605c1957f8cda548130d0f350fc35eae50459eb46810b6`) and own noncircular ledger (`1076a2d926bcd9e064f7619651576534add671aa664f2ad63d35eb9e1144c92c`), both author-only. No prior LAW642/v253 proof is used to establish what the external paper independently proves.

## 2. Rendering, complete reading and formula evidence

The native text extractor demonstrably drops inequalities, minus signs, floors and Greek/operator glyphs. Its returned index also stopped inside the appendix text; it is NOT a full exact-formula record. I did not infer missing symbols from memory or use that index as proof evidence.

Permitted DOCUMENT rendering command, after ACK and native-byte match:

`pdftoppm -png -r 140 -f 1 -l 21 [exact retained PDF] [OWN]/kulesza-publisher-page`

It returned successfully. ALL **21 rendered pages** were then opened/read visually in order, in page groups1–3,4–6,7–9,10–12,13–15,16–18,19–21. Actual page images are `kulesza-publisher-page-01.png` through `-21.png` in the exclusive new root. This is document extraction only, not a scientific program, numerical check or simulation.

| PDF pages visually read | Actual contents and formula checks |
|---|---|
| 1 | Title/authors/publication, abstract and introduction: matching sensitivity/error norm scope. |
| 2–3 | ALL Definitions1–6, theoretical loss, Theorems1–2, Lemma1/Corollary1; visually confirmed inequality directions, all-event/all-shift conditions, `gamma in (0,1]`, staircase floor/exponent and expected FIRST-power norm. |
| 4–5 | Sampling/theory-comparison statements and experimental scope; inspected, not executed, no empirical value used as theorem evidence. |
| 6–8 | ALL Section6.1 and Section6.2 definitions/lemmas/proofs: absolute continuity, finite pointwise density, polar representation, angular averaging, privacy and loss preservation; upper radial density and Lemmas8–10. |
| 9 | Lemma11, the actual Theorem2 proof chain, Section7's explicit limitations/future mismatched-error question; references not followed. |
| 10 | Checklist; no mathematical premise. |
| 11–14 | ALL AppendixA.1–A.3, Lemmas12–16 and sampling proofs through their endings; first-moment selector/value formulas read visually. Lemma17 begins at page14 bottom. Ancillary asymptotics/sampling are not source-match evidence. |
| 15–17 | ALL AppendixA.4 through its TRUE ending: complete Lemma17 proof, radial discretization/Lemma18, discrete Lemma19, Lemma9 proof, cited Lemma10 proof, Lemma11 proof and continuous limit argument. Visual equation evidence, not lossy extracted operators. |
| 18–21 | ALL AppendixB through the final Figure14/document ending. Experimental prose/captions inspected; small chart/bar values not individually transcribed or verified and are NONINPUT to the mathematical conclusions. |

All load-bearing definitions/theorem/proof formulas for this comparison were legible in the rendered pages. No such formula is left NR solely for a missing glyph. Reading the whole source is NOT accepting every printed proof inference, numerical result, algorithm or citation. The separate mathematical NR cuts below remain.

## 3. Exact model and law-class edges

### 3.1 Query, neighbours and sensitivity set (page2, Definitions1–3)

Definition1 states dataset-neighbour epsilon-DP. The paper describes add-remove and swap neighbour conventions but is deliberately neutral between them; Definition2 defines the ACTUAL sensitivity space

`K={q(D)-q(D'): D,D' neighbouring}`.

It observes origin symmetry and ASSUMES K convex. The Minkowski functional is used as the K-norm. For the registered caller, K is literally the full closed l1-unit diamond D, which is a bounded full-dimensional centrally symmetric convex norm ball. No issue about a degenerate/unbounded or nonclosed sensitivity set is concealed by this specialization. The paper's general phrase “any sensitivity set” remains subject to its Section2 convex/K-norm framework; no extension to arbitrary nonconvex sets is inferred.

The additive mechanism samples noise from ONE distribution P and adds it to q(D), independent of the dataset. Definition3 defines `(K,epsilon)` privacy by the measure inequality for ALL measurable output events S and ALL x in K:

`P(S)<=exp(epsilon)P(S+x)`.

Borel events of the registered model are included. If K is the actual difference set this matches the additive query condition; a norm bound or convex hull of a smaller actual set is not silently asserted to make that set equal to D. With K=D, ALL boundary shifts are included by the literal `x in K` quantifier. The source does not replace the target by open shifts, generator-only privacy or metric privacy proportional to every infinitesimal displacement.

### 3.2 All noise distributions to suitable densities (pages6–7, Lemmas3–4)

The initial class is noise probability DISTRIBUTIONS, not an assumed radial/density family. Lemma3 asserts and proves absolute continuity. Its null-set argument integrates intersection mass over shifts in K by Tonelli, finds a shift with zero overlap, and iterates the null-set union until positive probability would exceed total mass. For the registered D caller the required positive finite volume and uniform-shift integration are available. The notation omits the harmless uniform-volume normalizer in a displayed zero integral; that does not affect the zero-overlap conclusion.

Lemma4 supplies a finite pointwise-DP density representative via limsup shrinking-ball averages, not an arbitrary version of a Radon–Nikodym derivative. Visual page7 confirms the ALL-pairs condition `x-y in K` and the bound `p(x)<=exp(epsilon)p(y)`. Finiteness at each x uses K's positive measure and almost-everywhere finiteness of a density. This pays a genuine all-law/pointwise-density correspondence for the nondegenerate registered full-ball setting at its ordinary Tonelli/RN/differentiation inputs. It is NOT a hidden restriction to initially smooth/radial laws.

These direct current-source arguments are distinct from, and do not repair, MDA's earlier NR-A observation. No old K25 alternative proof is input.

## 4. Exact objective: first norm, squared norm, and mismatched squared Euclidean

### 4.1 What is PRINTED (pages2–3, Section2.1/Definition5/Theorems1–2)

The theoretical loss is explicitly

`ell(A(D),q(D))=||A(D)-q(D)||_K`, hence expected loss `E_P||Z||_K`.

Definition5 makes `(K,epsilon)` optimality mean minimum expected FIRST-power K-norm among all `(K,epsilon)` private noise distributions. Theorems1–2 assert existence of an optimal equicontour density and an optimal generalized staircase distribution at that objective. This is NOT a printed arbitrary nondecreasing `phi(||Z||_K)` or general moment theorem.

The generalized staircase density (Definition6, visually page3) has `p(x)=f_gamma(||x||_K)` with `gamma in (0,1]` and `f_gamma(r)` proportional to `exp(-epsilon floor(r-gamma))`. Its levels are homothetic K-balls. Lemma1/Corollary1 concern the mean-norm optimal offset/error's independence of K; AppendixA.1 and Lemmas13–14 explicitly use that FIRST moment. No squared-cost selector is obtained merely by renaming it.

### 4.2 A real but LIMITED squared-norm edge (pages7–8, Lemmas5–7)

The displayed angular averaging is

`pbar(x)=C^(-1) integral_Theta p(||x||_K u(theta))g(theta)dtheta`, `C=integral_Theta g(theta)dtheta`.

At the source's polar-change-of-variables premise (Lemma5), it preserves the ENTIRE K-radius marginal, not only the one printed mean formula: multiplying the polar integral by ANY nonnegative Borel `phi(r)` and using Tonelli gives

`integral phi(||x||_K)pbar(x)dx = integral phi(||x||_K)p(x)dx`

in the extended sense. This is an elementary consequence of the printed averaging formula, not a new global-optimality/attainment theorem or proof repair. Lemma6's actual all-pairs norm argument preserves privacy. Thus **same-norm squared-l1 expectation can be preserved in the equicontour reduction when K=D**.

But that pays only the radialization edge. It does NOT prove that the MEAN-norm-optimal gamma also minimizes squared-l1 cost, or that the remaining staircase/attainment proof has been established for that objective. AppendixA.4's discretization and utility convergence are written for expected K-norm; no full squared-moment attainment extension is stated or independently reconstructed here. In particular one cannot infer minimum of a second moment from minimum of the first.

### 4.3 The registered squared-Euclidean cost (pages2,5,9,19)

With K=D the source norm is l1, while the registered error is `||Z||_2^2`. The earlier allowed candidate already proves the whole-variable mismatch: arbitrary positive u,v give equal l1 radii but squared-Euclidean cost difference `2uv` between `(u,v)` and `(u+v,0)`. This rules out treating that objective as a function of the same radius, including after a norm/scale-preserving invertible linear change. No selected point/value is evaluated here.

Section5.3 and AppendixB.3 discuss OTHER error metrics empirically; they do not assert all-law optimality for them. Visual page19 explicitly notes that the gamma selected to minimize sensitivity-norm error need not minimize a mismatched norm error. Section7 (page9) identifies deriving optimal mechanisms for error metrics not matching sensitivity as a future question. That positive scope statement supports a bounded comparison, not a worldwide absence inference.

Therefore neither theoretical mean-norm optimality nor empirical superiority over K-norm/Laplace mechanisms pays the registered squared-Euclidean all-law lower bound, exhaustive equality or rounded-core selector.

## 5. Attainment, equality and selector: actual printed dependency chain

| Edge / printed result | Exact pages and prerequisites | What this source comparison pays |
|---|---|---|
| All-law class | Def3 page2, Lemmas3–4 pages6–7 | Measure class and finite pointwise-density version on genuine K-norm balls; registered D caller fits. |
| Equicontour reduction / Theorem1 | Lemma5 polar representation and Lemmas6–7 pages7–8 | Angular averaging preserves privacy and mean K-norm. The formula also preserves squared SAME-norm expectation as in §4.2, but not arbitrary angular Euclidean cost. Existence of an OPTIMAL equicontour law also invokes the later existence premise. |
| Optimal generalized staircase / Theorem2 | Page3 statement; page9 combines Lemmas10–11 with existence Lemma17; full AppendixA.4 pages14–17 | PRINTED existence of a mean-K-norm optimizer in the staircase family. Complete printed-proof verification remains limited by NR-K17 and NR-K10 below. No theorem falsity is asserted. |
| Radial structural constraints | Definition8/Lemma8 page8, Lemmas9–11 pages8–9; AppendixA.4 pages15–17 | Upper radial density, monotone profile, cyclic decay and two levels on a unit radial interval at mean-objective optimality. They are not an exhaustive original squared-Euclidean equality-law theorem. |
| Attaining first-moment gamma | Theorem2, Lemma1 and the compact-parameter calculations in AppendixA.1–A.2 | Some optimal gamma is asserted; numerical grid search is suggested. No unique-law/every-optimizer classification for the registered mismatched cost. Numerical search is not executed or verification evidence. |
| Squared-l1 all-law attaining optimizer | Requested case(A), not Definition5's cost | Equicontour preservation is paid; complete staircase/attainment conclusion for SECOND moment is **NOT STATED / NOT RECONSTRUCTED** in this source read. It would require an expressly separated hypothesis-matched argument, not first-moment substitution. |
| Squared-Euclidean full-diamond optimizer | Requested case(B) | Cost mismatch blocks direct theoretical application. No actual registered selector, unique equality or rounded-core result is stated in the fully read operative chain. |
| Independent source implication versus prior mathematical union | Existing candidate/ledger only as target comparison | The LAW642-dependent v253 union is not used to attribute an independent publisher proof. Neither this read nor any printed mean-norm theorem closes SOURCE-MATCH-U1 by circular composition. |

The source's epsilon parameter is positive; no epsilon-zero/infinite endpoint, zero-sensitivity case or general data-dependent/nonadditive channel optimum is silently included. Attainment statements have the source objective and geometric premises; alternative-metric experiments have neither universal quantifiers nor an all-law equality proof.

## 6. Named unpaid proof/import cuts — observed, NOT repaired

### NR-K17 — the as-printed existence inference (AppendixA.4, pages14–15)

Lemma17 states that an optimal `(K,epsilon)` noise distribution exists. Its proof argues that the DP set is closed, the norm objective continuous/linear and bounded below, and concludes the infimum is attained. The visually read publisher page15 contains that inference.

Closed feasible set plus continuous bounded-below objective does NOT by itself ensure a minimum; a compactness/coercivity/appropriate limiting argument is missing from this displayed inference. The topology on the probability-distribution space is not specified there; in particular an unbounded norm expectation is not automatically weakly continuous. I have NOT inserted tightness, a repaired topology, a new existence proof or an old alternative proof. **The printed proof step is not reconstructed**, not the theorem declared mathematically false. Page9 explicitly invokes Lemma17 before concluding Theorem2, so this is a real existence dependency, not an unrelated appendix comment.

### NR-K10 — externally referenced cyclic-decay proof (AppendixA.4, page17)

The proof of Lemma10, `fhat(r)=exp(epsilon) fhat(r+1)`, is referred to Geng–Viswanath2014, AppendixB Step5. That external proof is not reproduced in this retained paper and was NOT followed or recovered from old bodies. Its exact weighted multidimensional application therefore remains an explicitly unpaid source-proof dependency in this read. No hidden scalar-to-vector proof transfer is newly certified.

### NR-POLAR / other noninputs

Lemma5 cites Blumenson1960 for the polar representation; no external original proof was opened. The displayed norm-polar formula is a named change-of-variables input for the averaging edge, not new source-authenticated evidence about that external reference. Ancillary asymptotic Theorem4 uses a cited scalar result, but that asymptotic comparison is NOT an input to cases(A)/(B). All algorithm and experimental claims were read but not executed or accepted as proofs of those cases.

The exact glyphs/signs of these load-bearing printed formulas were visually available; the above NR labels concern MATHEMATICAL proof/import steps, not unresolved OCR operators. The source also has local textual inconsistencies in its discretization/monotonicity discussion; I do not repair them or use them to enlarge a theorem. The already mandatory NR-K17/NR-K10 and objective mismatch suffice to prevent full source-proof/target acceptance here.

These observations do not retrospectively withdraw any separately adopted alternative-source theorem, prove the publication false, or authenticate the old K25 owner proof. They state precisely the present printed-primary evidence ceiling.

## 7. Separate requested answers and exact remaining implication

### (A) Same-norm squared-l1 all-law attainment

- **Model/event/full-D shift/law class:** compatible at K=D, with the source's explicit all-law-to-density lemmas.
- **Squared-l1 radialization:** preserved by the actual angular-average formula at Lemma5's polar premise; this is a positive partial edge.
- **Complete SECOND-moment optimum/attainment:** not the source's printed Definition5/Theorem2 objective and not reconstructed by its mean-utility convergence/selector proof. No first-moment-optimal gamma is relabelled a squared-moment optimizer. NR-K17/NR-K10 also remain on the printed existence/structure chain.

Thus this paper read does **not presently pay the complete requested(A) implication**. That is not proof that no further argument using the paper could establish it.

### (B) Full diamond plus squared-Euclidean error, optimizer/equality/rounded selector

- **Model geometry:** compatible full CLOSED D; no loss of Borel law/event quantifiers.
- **Cost:** incompatible with the matching FIRST-norm theory, and not a function of the l1 radius even under a general same-radius-cost interpretation.
- **Attainment/equality/selector:** no registered all-law MSE lower bound, matching law/unique equality or genuine rounded-core selector is stated in the complete operative theory/proofs. Alternative-metric empirical comparisons are not substitutes.

Thus the **first failed direct application is the objective** at Section2.1/Definition5, before any gamma selector. The independent missing SOURCE-MATCH-U1 edge remains an actually supplied external implication for that SAME mismatched-cost model and its equality/selector. No LAW642-dependent union is allowed to prove this source independently established LAW642.

**Nonclaims:** no worldwide source absence, firstness, novelty, priority, major-contribution clearance or global mathematical non-equivalence. This is the exact source/version/scope just read. No new source beyond the released retained PDF was opened; no bibliography expansion, selected numeric/state/boundary probe, NR-A/NR-D repair, old K25 body or guide was used. All old STOP/HOLD/ZERO/findings, N4 UNKNOWN/historical exit UNESTABLISHED and auxiliary214 STOP persist.

## 8. Render evidence pins (all in the exclusive new root)

Document renderer used the exact native PDF above. These actual opened images bind page-numbered visual formula evidence; regeneration/byte identity is transport, not mathematical verification.

| PDF page / `kulesza-publisher-page-NN.png` | SHA256 |
|---|---|
| 01 | `e9b2c0a857be7a7d38e650e2ca75698938f0b5d5527df75a9f0a0c12161c8aaf` |
| 02 | `8dd847a46e7dd08128b5c4ffd98ac78be73bde410488f0f4df86fa0ea9c7977f` |
| 03 | `7186bad518e7bf9e2cb717bd9fec9275690e9088d0cfb0719c46335d8b37a315` |
| 04 | `f84d4aca6f5e531628ab67b6cce9aaa3ba519f042a45627959b0bf6a76ea542d` |
| 05 | `d62732ac60888b2779d940408345a26c25d89fc8a276d4781671d3afafa73551` |
| 06 | `fed7be1031f1231e5a4d05131794955b9addcf2341f6e31d7bff6267f858c829` |
| 07 | `ffe25143ade8a7b7cefe5bccc67c9d3daab4b448412e8cbea564494844edf45e` |
| 08 | `a3015edd05745b036537269a8da9a0823f1c1422ce080c269222522dacde608f` |
| 09 | `9007ad500accaefc892c4e8b09c414dff7d6e4a9420dba04ebc2d553bb9373fa` |
| 10 | `52bf9dbc06752f68b61f10e8d92a82dbcace2969ffbd20ce814890dd5c4b6c10` |
| 11 | `be5c291a0abd7f780a60e1e645a7e92647240d8609de3c94f7d6fd11f29e66e6` |
| 12 | `83cdb7c4992b6dfc9a90575d85892f4bdc0f011adb06e42585c2c5d1cd916457` |
| 13 | `e8f9918456dc427fc22176dbcec6c5f5775ea9cf5e6359655fdab654f63c9e75` |
| 14 | `276b1d1312fe4296cda4f1b1fa0a4172f376f8115791269a42ff259d7f7f0b4f` |
| 15 | `cd5feed2b6d90ebdea1ec3941d0a0f05a28c912b1427adc414c659852113efd9` |
| 16 | `71024667d7ecb94796bafde36596f6bc47923bbd62a4df4817db3acda706ae26` |
| 17 | `5e672b8c523f2e4cdf2ebb2520fbd537340c49dc0501865895378db70650866e` |
| 18 | `be00a9104bc1829bf82d1de7219f62a4e10a1e3c66ae2e70541f2fbbe9cc43fe` |
| 19 | `66237a9dde00b5ea9d25d68566efc5be5b97debac61db1bc1989736b95e60af7` |
| 20 | `fa1c2adb6ea95359b5bc7eeb90b53792d8e1794c0aa012e2285b7813c88383db` |
| 21 | `72c4a36f9d369bcf6fa080ff9c74adce686fe62630d3408b09f2faebdb6ba5b1` |

**END COMPLETE PUBLISHER CORRESPONDENCE —21/21 pages visually inspected, all operative proof/appendix endings read; author-only, no source-match/priority adoption.**
