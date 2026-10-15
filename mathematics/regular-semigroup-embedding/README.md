# Two embedding problems for regular semigroups (Problem 1: weakly E-unitary locally r-orthodox)

**No resolution of Problem 1 located as of 2026-10-14; status uncertified.**

This target proves:

* the necessary direction of Problem 1;
* a Kad'ourek-type necessary condition for finite semigroups;
* a reduction of the orthodox part of Problem 1 to an embedding question for E-unitary orthodox
  semigroups into band ⋊ group (Theorem A);
* two positive special cases;
* a computer-assisted verification of the orthodox case for the group Z2 and bands of order
  ≤ 6 (Proposition F);
* idempotent purity of ξ for **every finite weakly E-unitary locally orthodox regular semigroup**
  (Theorem X, a complete written, parent-audited proof; **not Lean-checked**, no novelty claim).

The second positive case (Theorem C) may already follow from Billhardt–Szendrei 1995; see
Remark C.1. A computation shows that three simple obstruction patterns cannot give a
counterexample.

## HMZ + Lean continuation, 2026-10-14

[Full evidence and reproduction](hmz-lean-20261014/README.md). The actual frozen HMZ loop ran
for 3600.387 seconds with the required Codex worker/Claude reviewer pairing. The reviewer
returned **`done:false`**; the run ended **`stopped`**, exit 143, with the frozen task/checker
unchanged. **The original embedding problem remains unresolved.**

The self-contained Lean module verifies 32 reported roots: genuine semidirect, Pastijn and
restricted constructions; the necessary direction for both product readings; local-band
characterizations; and a constructive derived-functor wreath criterion with its converse.
The criterion still assumes a faithful functor, rather than deriving one from P1.
Final artifact acceptance passed: positive Lean exit 0, semantic rejection control exit 1;
observed axiom union `{propext, Quot.sound}`. No Comparator or nanoda claim is made.

Separately, the new written, parent-audited **Theorem X** closes the finite ξ-non-purity
counterexample route. It is **not** among the Lean-checked results and is not an embedding
theorem. The 357 construction checks and 48 certificates were not rerun. Older-source
inaccessibility and book-formulation caveats remain explicit.

## Source

* Book problem: 关于正则半群的两个嵌入问题 (Two Embedding Problems for Regular Semigroups).
* Author: 郭聿琦 (Guo Yuqi, 西南大学).
* Location: 《10000个科学难题·数学卷》 (Science Press, 2009), book pp. 66–67, PDF pp. 82–83.
* Excerpt: [`sources/book-excerpt.txt`](sources/book-excerpt.txt).
* The book says the two problems were posed in 2002 and cites its ref. [2]:
  M. B. Szendrei, "Some open problems in the structure theory of regular semigroups",
  *Semigroup Forum* 64 (2002) 213–223, doi:10.1007/s002330010100.
  - The paper is paywalled. Only its abstract was readable (Springer page, 2026-10-14): "…
    formulate several open problems… the written version of the author's talk given at the
    problem session of the Colloquium on Semigroups, Szeged, 2000…".
  - So the definitions below are the book's. Szendrei's own wording is **not verified**.
* The book attributes Fact 1 to refs [1,2]. Ref. [1] is printed as "Billhardt B, Hsieh S C.
  Weakly E-Unitary locally inverse semigroups. preprint".
  - The paper published under that title is **B. Billhardt, M. B. Szendrei**, *J. Algebra* 267
    (2003) 559–576, doi:10.1016/S0021-8693(03)00395-8. Abstract:
    [`sources/core_api_BillhardtSzendrei2003_metadata.json`](sources/core_api_BillhardtSzendrei2003_metadata.json).
  - The book's co-author (Hsieh) differs from the published one (Szendrei). Both are recorded;
    which is right is not established.

## Problem

The book's definitions, quoted from the excerpt:

* **Bands.** 称带 E(S) 是一半格 (交换带)、正则带、正规带、半正规带, 如果它们分别满足
  ∀e,f ∈ E(S), ef = fe; ∀e,f,g ∈ E(S), efege = efge; ∀e,f,g ∈ E(S), efge = egfe;
  ∀e ∈ E(S), eE(S)e 是正则带.
  - Semilattice: `ef = fe`.
  - Regular band: `efege = efge`, equivalently `axya = axaya`.
  - Normal band: `efge = egfe`.
  - **Seminormal band:** every `eE(S)e` is a regular band. Called *locally regular* here; the
    variety is `L(ReB)`.
* **Completely simple.** 一正则半群称为完全单的, 如果它不含真理想, 而且含一本原幂等元.
* **Locally inverse.** 称半群 S 是局部逆的, 如果关于任意幂等元 e, eSe 是逆子半群.
* **Weakly E-unitary.** 称正则半群 S 是弱 E-酉的, 如果 ∀e ∈ E(S), ∀a ∈ S, e ⩽ a → a ∈ E(S),
  where 自然偏序 `a ⩽ b ↔ ∃e,f ∈ E(S), a = eb = bf`.
* **Locally r-orthodox.** 称一正则半群 S 是局部 r-纯正的, 如果关于任意 e ∈ E(S), eSe 是以
  E(eSe) 为正则带的纯正 (幺) 半群. Every `eSe` is an orthodox monoid with regular band
  `E(eSe)`.

The book never defines "semidirect product of a band by a completely simple semigroup"
(…经由完全单半群的半直积). Two readings are fixed in advance; both match Fact 1 as Billhardt–Szendrei
proved it:

* **(P) Pastijn product `B ⊙ C`.** Definition in Szendrei's survey arXiv:1909.05280 §5.2, for a
  normal band. For an arbitrary first factor it is the Pastijn–Rees product with sandwich `Q ≡ 1`
  [Auinger–Szendrei 2005, Remark 3.1].
* **(R) Restricted semidirect product `B ⊙* C`.** Definition from Auinger–Polák, *Acta Sci.
  Math.* 63 (1997), Def. 3.1. Over completely simple `C`, the product reduces to
  `(a,x)(b,y) = (a·φ_x(b), xy)` on `{(a,x) : φ_{xx'}(a) = a}`.

That (P) and (R) have the same embeddable classes is due to Billhardt–Szendrei 2003, as reported
in Auinger–Szendrei 2005, p. 40. The exact formulas are in [`proof.md`](proof.md) §0.

Two other plausible readings are **not** adopted:

* the ordinary semidirect product `B * C`, with `C` acting by endomorphisms;
* the Jones–Trotter `Reg(B * C)`.

Positive results hold in every reading. Theorem A and Lemma 0′ are proved only for (P) and (R).

## Status as of 2026-10-14 — status: uncertified-open

**(a) Book statement, verbatim.**

> 事实 1[1,2] 每一弱 E- 酉局部逆半群可嵌入一 "正规带经由完全单半群" 的半直积.
> 问题 1[2] 是否每一弱 E- 酉局部 r- 纯正半群可嵌入一 "半正规带经由完全单半群" 的半直积？
> 事实 2[2∼5] 每一逆半群可嵌入一 "半格经由群" 的半直积的幂等元分离同态像.
> 问题 2[2] 推广事实 2 到正则半群的一个尽量大的子类中.

Faithful English:

* *Fact 1.* Every weakly E-unitary locally inverse semigroup embeds in a semidirect product of a
  normal band by a completely simple semigroup.
* *Problem 1.* Does every weakly E-unitary locally r-orthodox semigroup embed in a semidirect
  product of a seminormal band by a completely simple semigroup?
* *Fact 2.* Every inverse semigroup embeds in an idempotent-separating homomorphic image of a
  semidirect product of a semilattice by a group.
* *Problem 2.* Extend Fact 2 to as large a subclass of regular semigroups as possible.

**(b) Dated search log (2026-10-14): no resolution found; this is not proof of openness.**

No primary source after 2002 found states that Problem 1 is open or solved.

* **Szendrei's 2019 survey** (arXiv:1909.05280, *Semigroup Forum* 100 (2020) 119–140; local copy)
  is by the poser. It reports only the locally inverse theorem (Thm 5.5) and the regular-band
  orthodox theorem. It names extending the McAlister–Lawson approach "to a subclass containing
  both orthodox and locally inverse semigroups" as a challenge.
* **Works citing Szendrei 2002.** OpenAlex lists 3 and Semantic Scholar 4
  (`sources/openalex_citing_Szendrei2002_*.json`, `sources/semanticscholar_citations_Szendrei2002.json`):
  - Hollings 2015, history;
  - Hartmann 2004/05, "E-unitary covers over group varieties";
  - Auinger–Bitterlich–Otto, *Adv. Math.* 482 (2025) 110563.

  I opened ABO: it cites the 2002 paper for the finite F-inverse cover problem, a different problem
  from the same list, which ABO solve. No title concerns Problem 1.
* **Works citing Billhardt–Szendrei 2003** (12 in OpenAlex,
  `sources/openalex_citing_BillhardtSzendrei2003_*.json`): Szendrei 2004 and 2011, Billhardt 2002
  and 2006, Auinger–Szendrei 2004 and 2005, Gomes–Szendrei 2007, Guo–Shum 2011,
  Dékány–Szendrei–Szittyai 2019, Meakin et al. 2021, and the 2019 survey. All concern locally
  inverse, weakly ample or GC-lpp semigroups, judging by title, abstract and, for AS 2005 and the
  survey, full text.
* **Works citing Billhardt 1998** (4 in OpenAlex): Gomes–Szendrei 2007, Szendrei 2002, the survey,
  and Dékány's thesis.
* **Web searches** (English and Chinese) for "weakly E-unitary locally orthodox", "Pastijn
  product" plus band or orthodox, "semidirect product of a band by a completely simple
  semigroup", and 弱E-酉 局部纯正 半直积 完全单: nothing on this problem.
* **Reviewer's searches** (`evidence/codex_review.md`, with query list): no resolution of
  Problem 1 found.
* **openai/math corpus screen, as reported by the parent agent:** no family on this topic in
  local clone `adc7f1241` or in the remote listing, 2026-10-14. Not re-checked here.
* **Not readable:**
  - Szendrei 2002 (paywall).
  - Billhardt 1998, *J. Algebra* 206: 40–50, and Billhardt–Szendrei 2003: ScienceDirect
    blocked automated access with a captcha, and the Elsevier API without a key returned metadata
    only.
  - Billhardt–Szendrei, "A new class of embeddable E-unitary regular semigroups", Proc. Luino
    1992, World Sci. 1994, pp. 27–35 (year per Szendrei's own publication list).

  Any of these could contain relevant results [UNVERIFIED].

  A further lawful source-recovery pass opened both authors' university publication lists and
  accessible author copies of Szendrei 2011 and Hartmann–Szendrei 2012, plus Dékány's 2019 thesis.
  None supplies the missing 1998 construction or the original 2002/2003 full texts.
  [Exact routes and limits](hmz-lean-20261014/source-access.md) distinguish recovered statements
  from unavailable proofs; the Billhardt local-regularity question is still unverified.

**(c) Formal statement attacked, fixed in advance.**

> **P1.** For every regular semigroup `S` that is weakly E-unitary and locally r-orthodox, do
> there exist a locally regular band `B` and a completely simple semigroup `C` such that `S`
> embeds in `B ⊙ C` (reading P) or in `B ⊙* C` (reading R)?

Lemma 0 in `proof.md` shows that the converse always holds.

The orthodox part is the sub-question

> **Q_orth.** Does every E-unitary orthodox semigroup with a locally regular band embed in a
> semidirect product of a locally regular band by a group?

Theorem A makes it equivalent to the orthodox part of P1 in both readings.

## State of the art

* **Locally inverse (Fact 1).** Billhardt–Szendrei 2003, including the finite version and
  refinements: straight gives a semilattice, left/right straight a left/right normal band.
  Kad'ourek: a locally inverse `S` is weakly E-unitary iff its least completely simple congruence
  is idempotent pure.
* **Orthodox, over groups.**
  - Szendrei 1987, *Proc. Roy. Soc. Edinburgh A* 106: 89–102. Publisher abstract in
    `sources/szendrei1987_PRSE106_abstract.txt`. For a band variety `V`, embeddability in a
    `V`-band ⋊ group is equivalent to a canonical embedding into the free `V`-band over a partial
    semigroup, and E-unitary orthodox semigroups with a regular band `E` embed with the band in
    `var(E)`.
  - Billhardt–Szendrei 1995, *Proc. Edinburgh Math. Soc.* 38: 361–385 (local copy). They prove:
    - quasi-F-orthodox semigroups embed in some band ⋊ group (Thm 4.1);
    - generalized F-orthodox ones embed with the band in `var(E)` (Thm 4.2);
    - an iff criterion for embedding into a `V`-band ⋊ group (Result 1.11).
  - Billhardt 1998: a finite E-unitary orthodox semigroup with a left semiregular band that does
    not embed in any band ⋊ group.
* **Problem 2, partial results (survey Thms 5.2, 5.6).**
  - Inverse: McAlister–Lawson, via almost factorizable semigroups.
  - Orthodox: Hartmann 2007, idempotent-separating images of band ⋊ group.
  - Locally inverse: Szendrei 2011, images of Pastijn products.

  Not attacked here.

## Attack

1. **Definitions.** The definitions of (P) and (R) were recovered from opened sources. The
   reduction formula for (R) over completely simple `C` was derived from Auinger–Polák Def.
   2.1/3.1; the reviewer confirmed it.
2. **Reduction (Theorem A).** For orthodox `S`, an embedding in a Pastijn or restricted product
   forces the image in `C` into a rectangular group, and it collapses to band ⋊ group.
3. **Is local regularity genuinely weaker than regularity?** Yes:
   - the smallest locally regular non-regular band has order 5 (`E5`), by SAT search plus an
     independent exhaustive enumeration of orders ≤ 4;
   - every band with at most two D-classes is locally regular;
   - `FB(3)` is locally regular;
   - `E5` with an identity adjoined is left semiregular but not locally regular, so Billhardt's
     1998 class is not inside the problem automatically.
4. **Positive cases.**
   - Regular bands, hence all monoids (Theorem B, via Szendrei 1987).
   - Bands with at most two D-classes, any group (Theorem C). The proof uses a normal form
     `Φ = π∘σ∘p` for the action of the top rectangular group on the bottom one and an explicit
     functor into a band `B0` with at most two D-classes. The reviewer found BS95, and its
     consequences are recorded in Remark C.1.
5. **Counterexample routes that failed.**
   - *(C2), (C3), (I1).* Necessary conditions from band ⋊ group were searched for violations by
     SAT over Z2-graded semigroups. The exact grids are in `proof.md` §7: up to `|S| = 10` for
     (C2)/(C3) and `|S| = 8` for (I1). No violation was found. (C2) and (C3) were then proved to
     hold in every E-unitary orthodox semigroup, with matching σ-classes, which the reviewer
     showed are needed.
   - *Generic extensions of 2-D-class bands.* Exhaustive generic SAT enumeration of the
     Z2-graded extensions of three non-regular 2-D-class bands gave 7 semigroups
     (`evidence/enum_extensions.log`):
     - `E5` with ≤ 5 odd elements;
     - `E_A` with 4 or 6 odd elements;
     - `E_C` with 6 odd elements.

     All embed. Theorem C's construction is verified on each, and the structured SAT
     (`evidence/embed2chain_sat.log`, with models) agrees for the two `E5` cases with 5 odd
     elements. The `E_C` run with 8 odd elements timed out.
   - *Non-orthodox route via Lemma 0′.* The original tests concerned ideal extensions `K ∪ {f}`:
     all 355 checked instances (300 non-orthodox) had ξ idempotent pure. The new
     [Theorem X](hmz-lean-20261014/xi-purity.md) proves this for **every finite** weakly E-unitary
     locally orthodox regular semigroup. The complete coordinate proof is written and
     parent-audited, not Lean-checked. It rules out finite ξ-non-purity counterexamples to P1,
     without proving embeddability.
   - *Three or more D-classes, group Z2 (Proposition F).*
     - There are exactly 10 locally regular non-regular bands of order 6 with ≥ 3 D-classes, up
       to isomorphism, and none of order ≤ 5.
     - All their Z2-graded E-unitary extensions were enumerated exhaustively: 48 semigroups. At
       most 6 odd elements are possible, by `odd_bound_3d.py`.
     - Each embeds in `B ⋊ Z2` with `B` locally regular and `|B| ≤ 7`; each certificate was
       verified independently.
     - A first run reported spurious non-embeddings because of an over-strict injectivity
       constraint. It was fixed and rerun; the old outputs are archived.
   - Consequence: a counterexample to Q_orth needs a band with ≥ 3 D-classes and, if
     `S/σ ≅ Z2`, with ≥ 7 elements. (C2), (C3) and (I1) are excluded as obstructions; other
     local obstructions are not excluded.

## Claims

| Claim | Status | Evidence |
|---|---|---|
| Lemma 0: every regular subsemigroup of `B ⊙ C` or `B ⊙* C` (`B` locally regular) is weakly E-unitary and locally r-orthodox | PROVED | `proof.md` Lemma 0 |
| Lemma 0′: if a finite `S` embeds in `B ⊙ C` or `B ⊙* C` (`B` any band), then ξ(S) is idempotent pure | PROVED | `proof.md` Lemma 0′ |
| ξ idempotent pure on 355 random weakly E-unitary, locally r-orthodox ideal extensions `K ∪ {f}` (300 non-orthodox) | COMPUTED+VERIFIED | `work/check_xi_ideal_extensions.py` → `evidence/check_xi_ideal_extensions.log` |
| Theorem X: a regular locally orthodox semigroup with a completely simple ideal has a completely simple quotient; weak E-unitarity makes it idempotent pure. Hence ξ is pure for every finite member of P1's class | WRITTEN PROOF, PARENT-AUDITED; not Lean-checked; no novelty claim | `hmz-lean-20261014/xi-purity.md` |
| Orthodox: weakly E-unitary ⟺ E-unitary; E-unitary ⇒ σ ∩ H = Δ | PROVED | `proof.md` §1 |
| Theorem A: for orthodox `S` and band varieties `V ⊇ RB`, embeddability in `B ⊙ C` or `B ⊙* C` (`B ∈ V`) ⟺ in `B ⋊ G` (`B ∈ V`). No earlier explicit statement found | PROVED (reviewer: correct) | `proof.md` §3 |
| The orthodox part of P1 (readings P, R) ⟺ Q_orth | PROVED (corollary) | `proof.md` §3 |
| Bands in which every element of the structure semilattice has at most one element strictly below it (in particular, bands with ≤ 2 D-classes) are locally regular | PROVED | `proof.md` Lemma 5 |
| `E5` is a band, locally regular, not regular, left semiregular, not right semiregular; no locally regular non-regular band of order ≤ 4 | COMPUTED+VERIFIED | `work/check_band_facts.py` → `evidence/check_band_facts.log`; `evidence/sat_small_band.log` |
| `FB(3)` (159 elements) is locally regular, not regular, not left or right semiregular | COMPUTED+VERIFIED (uses the Green–Rees normal form) | `evidence/check_band_facts.log`, `evidence/locally_regular_vs_regular_FB3.log` |
| LSRB ⊄ L(ReB) (`E5` with identity adjoined) | COMPUTED+VERIFIED | `evidence/check_band_facts.log` |
| Theorem B: P1 holds for orthodox `S` with regular band, hence for all monoids | PROVED modulo Szendrei 1987 (abstract confirms the statement used) | `proof.md` §5; `sources/szendrei1987_PRSE106_abstract.txt` |
| Theorem C: E-unitary orthodox `S` whose band has ≤ 2 D-classes embeds in `B0^G ⋊ G` with `B0` locally regular, so P1 holds for these. Novelty doubtful (Remark C.1) | PROVED (reviewer: correct after minor fixes, now applied); construction COMPUTED+VERIFIED on 357 instances | `proof.md` §6; `evidence/check_two_chain_theorem_random200.log`, `evidence/check_two_chain_theorem_hard150.log`, `evidence/check_two_chain_generic.log` |
| Theorem C's semigroups are quasi-F-orthodox (BS95), so BS95 Thm 4.1 already embeds them in some band ⋊ group | PROVED | `proof.md` Remark C.1; `sources/billhardt_szendrei1995_PEMS38_quasiF.pdf` |
| Theorem C's semigroups are generalized F-orthodox, so BS95 Thm 4.2 gives a band in `var(E)` | CONJECTURED (reviewer's deduction, not checked here) | `evidence/codex_review.md` |
| Proposition F: Q_orth holds for every E-unitary orthodox `S` with `S/σ ≅ Z2` and a locally regular band of order ≤ 6 | COMPUTED+VERIFIED: Theorems B, C, plus exhaustive SAT enumeration (10 bands, 48 extensions) and 48 independently verified embedding certificates with locally regular `B`. Completeness relies on SAT UNSAT answers | `proof.md` Prop. F; `evidence/enum_locreg_bands.log`, `evidence/odd_bound_3d.log`, `evidence/pipeline_3d.log`, `evidence/pipeline_3d_certificates.log`, `evidence/ext/3d/` |
| (C2), (C3), with σ-hypotheses, hold in every E-unitary orthodox semigroup | PROVED; SAT consistent | `proof.md` §7; `evidence/sat_search_C2.log`, `evidence/sat_search_C3.log`, `evidence/sat_search_I1.log` |
| P1 in general; Q_orth for bands with ≥ 3 D-classes; ξ purity for infinite members without a completely simple ideal | UNRESOLVED HERE; current literature status uncertified | finite ξ-purity route closed by Theorem X, not an embedding theorem |
| Problem 2 | OPEN (open-ended; partial literature results only) | survey Thms 5.2, 5.6 |

## Independent review

* **Delegate:** Codex CLI, `gpt-6.1-sol`, effort `max` (from `DELEGATE_MODELS.json`), read-only,
  live web search, restricted to this directory, no further delegation. It ran on 2026-10-14 for
  about 31 minutes.
* **Files:** prompt [`evidence/codex_review_prompt.md`](evidence/codex_review_prompt.md); output
  [`evidence/codex_review.md`](evidence/codex_review.md).

**Verdicts.**

| Item | Verdict |
|---|---|
| Theorem A, Theorem B, Lemmas 0, 1, 2–6 | correct |
| Theorem C | correct with minor fixes |
| §7 | had errors |
| Formalization | correct with minor fixes |
| Status claim | correct with minor fixes |

The reviewer reran `check_band_facts.py`, both Theorem C checkers and the FB(3) script, and
reproduced the 357-instance claim. It inspected the SAT scripts but could not rerun them, because
`pysat` was missing in its sandbox.

**Objections and how they were resolved.**

1. **(C2), (C3) lacked σ-class hypotheses** (a two-element group is a counterexample as stated).
   Fixed: the hypotheses are now stated and their necessity noted. The missing `ss' D_E tt'` step
   in (C3) was added, using the reviewer's argument.
2. **Theorem C.** The one-D-class case and the `s's ∈ D` case of Step 1(b) were made explicit, and
   the statement now says "at most two D-classes".
3. **Attribution.** The P/R equivalence is now credited to BS 2003 via AS 2005 p. 40, not to the
   survey. The Pastijn product for arbitrary bands is credited to AS 2005, Remark 3.1.
4. **Search-coverage overstatement.** The exact SAT grids and the Z2-grading restriction are now
   stated. The I1 maximum is corrected to 8. The enumeration and structured-SAT logs are added.
   The enumerator now prints `exhausted=True`.
5. **Novelty of Theorem C.** The reviewer found Billhardt–Szendrei 1995. I checked property (R)
   myself (Remark C.1), which gives quasi-F-orthodoxy and so embeddability into *some*
   band ⋊ group. The reviewer's further deduction (generalized F-orthodox, hence a band in
   `var(E)`) is recorded as CONJECTURED. Theorem C is no longer claimed as new.
6. **Openness wording.** The phrase "still open" is replaced everywhere by "no resolution located;
   status uncertified".
7. **Overreach.** The claim that any obstruction must be multi-step was limited to (C2), (C3) and
   (I1).
8. **Minor.** FB(3)'s band check is now part of the checker's aggregate result.

**Second, focused review** (same delegate, about 9 minutes, no web). Files:
[`evidence/codex_review2_prompt.md`](evidence/codex_review2_prompt.md),
[`evidence/codex_review2.md`](evidence/codex_review2.md). It covered Proposition F,
Lemma 0′ and Remark C.1.

| Item | Verdict |
|---|---|
| Remark C.1 | correct |
| Exhaustiveness of the extension enumeration | correct |
| Band enumeration, odd-element bound, Lemma 0′ | minor fixes |
| Certificate verifier | had errors |

The reviewer independently re-checked all 48 embeddings, both coordinates and local regularity
of `B`; they are valid. The fixes applied:

1. The verifier now checks that parity is a homomorphism and that the idempotents form a
   prefix.
2. Local regularity of `B` is now mandatory: `--require-locreg` in the verifier and in
   `pipeline_3d.py`. All 48 certificates were re-verified under it.
3. The labelled count is corrected: 9360 is the total, of which 5760 have at least three
   D-classes.
4. The odd-element bound now states the H-class counting explicitly.
5. Lemma 0′ cites the band-only projection computation. The ideal-extension explanation now
   uses orthodoxy of `fKf`, and records the reviewer's example showing that linking alone is
   not enough.
6. A spurious `Reg(B*C)` mention was removed from a docstring.

## Reproduction

All commands run from `work/`.

```
python3 check_band_facts.py                                   # E5, E5^1, order<=4 enumeration, FB(3)
python3 check_two_chain_theorem.py 200 1                      # Theorem C, random instances
python3 check_two_chain_theorem.py 150 1000 --hard            # Theorem C, non-regular bands, twisted actions
uv run --with python-sat python enum_extensions.py E5.json 5 ../evidence/ext/E5_m5.json   # generic extensions (exhaustive)
python3 check_two_chain_generic.py ../evidence/ext/E5_m3.json ../evidence/ext/E5_m5.json ../evidence/ext/E_A_m4.json ../evidence/ext/E_A_m6.json ../evidence/ext/E_C_m6.json
python3 check_xi_ideal_extensions.py 400 1                    # Lemma 0' route, family K u {f}
uv run --with python-sat python sat_small_band.py 5           # smallest locally regular non-regular band
uv run --with python-sat python sat_search_C2.py 6 4          # (C2) violation search (UNSAT)
uv run --with python-sat python sat_search_C3.py 6 4          # (C3) violation search (UNSAT)
uv run --with python-sat python embed2chain_sat.py ../evidence/ext/E5_m5_0.json 2 4 6 2   # structured embeddability SAT
uv run --with numpy python locally_regular_vs_regular.py 3    # verbal congruences on FB(3)
uv run --with python-sat python enum_locreg_bands.py 6 ../evidence/ext/locreg6_3D.json --max 200000   # Prop. F bands
python3 odd_bound_3d.py ../evidence/ext/locreg6_3D.json        # Prop. F odd-element bound
uv run --with python-sat python pipeline_3d.py ../evidence/ext/locreg6_3D.json 12 1 2 3 4 5 6   # Prop. F extensions + embeddings
python3 verify_embedding_certificate.py ../evidence/ext/3d/E0_m5_S0.json ../evidence/ext/3d/cert_0_5_0.log  # one certificate
```

`work/embed_generic_sat.py` is a generic embeddability SAT: an unknown band `B` of order `k`, an
involution, and β, injective on each σ-class. It is used by `pipeline_3d.py` for Proposition F,
and every embedding it finds is re-checked by `work/verify_embedding_certificate.py`. An UNSAT
answer only excludes bands of that order.

## Next steps

1. **Obtain the full texts** of Szendrei 2002, Billhardt 1998, Billhardt–Szendrei 1994 and BS
   2003 through further lawful access. Both author sites, public repositories and linked grant
   archives were pursued; [the access ledger](hmz-lean-20261014/source-access.md) records the
   specific missing texts rather than assuming the first paywall was conclusive.
   - Check Szendrei's exact wording of Problem 1 and of "semidirect product".
   - Check whether Billhardt's 1998 band is locally regular. If it is, Theorem A makes his example
     a counterexample to P1. By Theorem C, his band has at least 3 D-classes.
2. **Check the reviewer's generalized-F-orthodox deduction** against BS95 §3 (left/right normal
   extended F-cross-sections in the least R-/L-unipotent quotients) for Theorem C's class.
3. **Use, rather than repeat, the finite ξ-purity reduction.** Theorem X gives a pure completely
   simple quotient for every finite target member. The missing step is an embedding theorem for
   these extensions with the required local regular-band constraints. The ξ-purity question
   itself remains for infinite semigroups without a completely simple ideal.
4. **Look for a counterexample to Q_orth with three D-classes.** Use BS95 Result 1.11 or Szendrei
   1987's free-band criterion as the decision procedure.
   - Bands with a 3-chain whose top local submonoids are regular but not of depth 2 are where
     local regularity is a real constraint.
   - V-shaped bands (two maximal classes over one bottom class) are automatically locally regular.
     There `G` may permute the tops, which the orthogroup argument of Theorem C does not cover.
