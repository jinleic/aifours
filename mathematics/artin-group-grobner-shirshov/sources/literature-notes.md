# Artin-group Gröbner–Shirshov bases: literature/status notes

Survey date: 2026-10-14 (Pacific time). Target: L. Bokut and Yuqun Chen, “阿廷 (Artin) 群的 Gröbner-Shirshov 基”, *10000 Selected Problems in Sciences: Mathematics*, Science Press, 2009, pp. 30–34; questions transcribed in `book-excerpt.txt`, lines 130–141.

**Book-level unresolved-status designation: `uncertified-open`.** The dated searches below found no resolution of the residual generator-specific questions; **no resolution found is not proof of openness**. The mandatory table labels are descriptive survey labels, not an open-problem certification. Parent-reported additional screen: no matching topic family was found in the local `openai/math` clone at `adc7f1241` or in the remote listing checked 2026-10-14; that screen was not independently repeated here and does not establish mathematical status.

## Scope and evidence convention

- **This is a literature survey, not a verification of the papers' composition calculations.** “Opened PDF” means the abstract and relevant theorem/presentation passages were read, usually through the accompanying `pdftotext -layout` file. “Opened abstract” is weaker. Metadata alone is explicitly **[UNVERIFIED]** for mathematical content.
- **“Open as far as found” is a search conclusion, not a theorem that no solution exists.** It refers to the specified group, alphabet, and order, not merely to a word-problem algorithm. The 2014 survey is a historical source, not the sole basis for the present conclusion. Forward-citation searches, newer papers, the 2020 book preview, and rewriting/automaticity literature were also checked; see sections C–E.
- Write `A(B_n)` for the Artin–Tits group of Coxeter type B, to avoid confusing it with the ordinary n-strand braid group `B_n=A(A_{n-1})`. Coxeter groups additionally impose `s_i^2=1`; a basis for that quotient is not a basis for the Artin group.
- The book's **Artin–Garside alphabet is the small alphabet `{sigma_i, Delta, Delta^{-1}}`**. A presentation on **all nonidentity simple elements** (positive lifts of `W\{1}`) is a different alphabet, even when its authors call it “Garside's presentation”. Similarly, a dual-monoid presentation or a Koszul/PBW theorem is not automatically a completed GS basis in BKL/reflection generators.
- A finite convergent rewriting presentation implies unique irreducible words on its own alphabet. It does not automatically supply a GS basis for a prescribed *different* alphabet or prescribed monomial order. A coherent presentation adds relations between relations; coherence alone is not confluence of the oriented standard relations.
- GS bases can be infinite. In particular, “no finite basis for this degree-lex order” is not “no GS basis”. Mere abstract existence by including all equalities is not the explicit/effective problem posed in the book; compare Autord [AU07], §1.2.

### Alphabet/order precision before claiming a new result

Status must ultimately be attached to a **(type, alphabet, monomial order)** triple. This literature assignment fixes no new proof target and makes no claim to have formalized all seven book questions.

- **Type A Artin–Burau:** the extra generators are the Burau conjugates specified in [BCS07], with the inverse-tower order of that paper. **Outside type A, no canonical Artin–Burau alphabet is defined by the seven-question list or by the opened sources used here.** Thus (2) is additionally under-specified until an explicit per-type generator dictionary and total monomial order are chosen; “no result found” is not a certified theorem about every possible such choice.
- **Finite-type Artin–Garside:** for a fixed labeled Coxeter system `(W,S)`, take the standard positive lift of each `s in S`, and the positive lift `Delta` of the longest element `w0`, plus a formal inverse letter for Delta. A proposed small-alphabet project must additionally fix an order on S and the position of the Delta letters. The established type-A triple uses exactly [BG08]'s degree-lex order; this survey does not silently transport that result to another type/labeling/order.
- **BKL beyond type A:** one must fix the dual presentation, Coxeter element, reflection lifts, whether `delta^{±1}` is adjoined, and a total letter/word order. [BE03]/[PI02] provide dual-monoid structures/presentations, not a definition-free all-orders solution of the book's shorthand. The verified source-level type-A triple is [BKL09]'s enlarged alphabet and specified degree-lex order.
- **All-simple-element systems** [HM99], [CZ13], [GGM15], [DG16] remain separately recorded triples. Their alphabet must not be collapsed to the small Artin–Garside alphabet in a status claim.
- **(6)–(7):** singular generators, deleted-strand idempotents, inverse letters, and the chosen complex-reflection braid presentation all belong to the alphabet specification. A standard presentation without a chosen monomial order is not yet a fully fixed GS problem. The opened papers' orders are reported individually; unreported inverse-letter positions are not invented.

## A. Seven-question status table

Reference keys below resolve to full citations and opened-source details in section B. The labels cover the whole numbered question; the non-A residual questions are stated explicitly.

| Book question | Status | Precisely what is established, and what is not |
|---|---|---|
| **(1) General Coxeter groups; Bokut–Shiao conjecture** | **partially solved** | The original conjectural formula is **false**, not still an unrefuted conjecture: Chen–Liu [CL09], Example 3.2, gives a four-generator counterexample in standard involutive generators with degree-lex `s1<s2<s3<s4`; their replacement pre-GS conjecture is proved only under stated restrictions. Explicit finite-type results include Lee–Lee [LL19] for H2/H3/H4 (standard reflection generators, degree-lex increasing indices), and Pang–Wang [PW26] for G2/F4/E6/E7/E8 (degree-lex, their relabeled Coxeter diagrams). The latter authors state that this completes their finite irreducible list; this does **not** settle an explicit uniform basis for arbitrary Coxeter matrices. Ustaoğlu [US24] treats affine B/D in standard involutive generators and degree-lex. All these PDFs were opened. |
| **(2) A(B_n), A(D_n), A(G2), A(F4), A(E6), A(E7), A(E8), specifically in Artin–Burau generators** | **open as far as found** | No opened source supplies the requested uniform bases in this alphabet. The established ordinary type-A Artin–Burau result is Bokut–Chaynikov–Shum [BCS07], inverse-tower order; it is the background, not a solution for Coxeter type B. Chen–Zhong [CZ13] genuinely treats type B, but in **Adyan–Thurston/all-simple-element generators**. Bokut–Vesnin [BV06] treats every two-generator Artin group, hence G2, but in **HNN/free-by-cyclic generators and tower order**, not the required Burau alphabet. These are opened PDFs; none justifies an “all non-A types solved” claim. |
| **(3) Finite-type Artin groups in `{sigma_i, Delta, Delta^{-1}}`** | **partially solved** | **Type A is solved** by Bokut [BG08], Theorem 1.1, degree-lex `Delta^{-1}<Delta<a1<...<an`; this was already the book's baseline. The residual non-A family is **open as far as found in this small alphabet**. Hermiller–Meier [HM99] gives finite complete systems for every spherical Artin group but uses **all simple elements**, not just atoms plus Delta. [CZ13] also uses all simples. The newer explicit type-B3 result [IMAN24] is an **infinite completed presentation of the positive monoid on three standard atoms**, not the group with Delta/inverses. Autord [AU07] gives standard-atom dihedral positive-monoid completion information. Neither monoid result supplies the missing group cutover. |
| **(4) Finite-type Artin groups in BKL generators** | **partially solved** | **Type A**: Bokut [BKL09] gives a GS basis in BKL generators **enlarged by `delta^{±1}`**, with degree-lex `delta^{-1}<delta<a_ts` and lexicographic order on `(t,s)`. For other finite types, Bessis [BE03] constructs the dual Garside monoid and Picantin [PI02] supplies explicit type-B/D dual presentations; neither opened source asserts the needed completed GS basis in the small BKL/reflection alphabet. Josuat-Vergès–Nadeau [JN23] proves Koszulity of the dual monoid algebra and a PBW statement for its **quadratic dual**, not a group GS basis. The non-A generator-specific question remains unclosed in this search. |
| **(5) Extend (1)–(3) to arbitrary Artin groups** | **partially solved** | Type A and several restricted group classes have strong results: [BV06], [CZ13], [HM99], Holt–Rees [HR12]. A major broader **monoid** result is Dehornoy–Guiraud [DG16], Corollary 6.3.4: every finitely generated Artin–Tits monoid has a **finite quadratic convergent presentation on a finite Garside-family alphabet**; finiteness comes from [DDH15]. Gaussent–Guiraud–Malbos [GGM15] gives a convergent presentation on positive lifts of `W\{1}` and a coherent standard Artin presentation. These are not bases for arbitrary **groups** in the prescribed Burau or atom-plus-Delta alphabets. No such general group result was found. |
| **(6) Singular braid monoid SB_n in Artin–Garside and BKL generators** | **open as far as found** | Vershinin [VS10], opened PDF, proves Garside and greedy normal forms in the singular setting and gives a BKL-style presentation. Theorem 1 uses the usual positive braid/singular letters with the lex order `sigma1<...<sigma(n-1)<x1<...<x(n-1)` for its positive base; Theorem 6 uses `a_ts^{±1}, b_qp`. These are **normal-form/presentation results, not a displayed GS completion in both requested alphabets**. Chaynikov [CH06] is an important BKL normal-form lead already known to the book, but mathematical content was not opened here: **[UNVERIFIED]**. “Singular part of the Brauer semigroup” is a different object and was excluded. |
| **(7) VB_n, WB_n, IB_n, and complex-reflection braid groups B(W), standard generators** | **open as far as found** | No reliable opened source closes this combined question. Karpuz–Özalan [KO20] claims GS bases for **pure** virtual `PV_n` on `mu_ij^{±1}`, not full `VB_n`; the displayed basis also has the inverse-overlap caveat in C. Karpuz–Özalan–Çevik [KOC19] claims a `B(G24)` GS basis on `s,t,u` and inverses, but has a similar displayed-list caveat. Çevik–Albargi [CA20] is a false positive: despite its title, its Theorem 3.1 imposes `s²=t²=u²=1` and works with **G12**, not a verified basis for `B(G12)`. Vershinin [VI09] gives inverse-braid normal forms/word-problem methods, not the specified GS basis. Çevik et al. [CI20] treats the **symmetric inverse monoid I_n**, not `IB_n`. For complex braid groups, [CLL15] and [FM26] provide presentations/Garside-type structures, not completed standard-generator GS bases. No direct welded GS theorem was located. |

For (3) and (4), “partially solved” includes the pre-2009 type-A baseline because the printed question says “finite-type Artin groups”. If “the same types as (2)” is imposed, the **residual non-A status is “open as far as found”** in the specified alphabets. The table does not count changed-generator rewriting results as solutions of that residual problem.

## B. Opened primary sources and exact rewriting scope

### B1. Explicit GS results and counterexamples

**[CL09] Yuqun Chen and Cihua Liu**, *Gröbner–Shirshov bases for Coxeter groups I*, arXiv preprint (2009), [arXiv:0910.0096](https://arxiv.org/abs/0910.0096). **Opened abstract and PDF.** Example 3.2 has `m12=m23=m24=infinity`, `m13=3`, `m14=2`, `m34=5`, with `s1<s2<s3<s4` and degree-lex. It disproves obtaining the conjectured basis using only commutations: the noncommuting length-three braid relation is also needed. The new conjecture concerns a pre-GS basis, not the original formula. Local text lines 184–219 are the critical passage. The general-case theorem excludes four types of nontrivial inclusion composition; do not turn it into a uniform solution.

**[BS01] L. A. Bokut and L.-S. Shiao**, *Gröbner–Shirshov bases for Coxeter groups*, *Communications in Algebra* 29 (2001), 4305–4319, [DOI:10.1081/AGB-100106002](https://doi.org/10.1081/AGB-100106002). **[UNVERIFIED] original mathematical text.** DOI metadata opened but supplied no abstract; publisher text was not obtained. Its classical A/B/D results and conjecture are described by the opened [CL09], [PW26] and 2014 survey. The counterexample claim above relies on [CL09], not merely on this metadata.

**[LL19] Jeong-Yup Lee and Dong-il Lee**, *Gröbner–Shirshov bases for non-crystallographic Coxeter groups*, *Acta Crystallographica A* 75 (2019), 584–592, [arXiv:1809.08419](https://arxiv.org/abs/1809.08419), [DOI:10.1107/S2053273319002092](https://doi.org/10.1107/S2053273319002092). **Opened abstract and PDF.** Gives group-algebra GS bases and standard monomials for H2, H3, H4; degree-lex with `s1<s2<s3<s4` as appropriate. These are finite **Coxeter** groups, not the corresponding Artin groups.

**[PW26] Xiaowei Pang and Jun Wang**, *Gröbner–Shirshov bases for the Coxeter groups of the types G2, F4, E6, E7 and E8*, [arXiv:2002.07369](https://arxiv.org/abs/2002.07369), first posted 2020; **local PDF is v2, 15 March 2026**. **Opened abstract and PDF.** Theorems 3.2/3.3/3.4 give E6/E7/E8; Appendix A gives G2/F4. Uses degree-lex and the rearranged/reflection-generator labeling of Definition 3.1; for E_n the letters are `x_{7-n},...,x6`, with the branch at `x3`. The paper's generator relabeling is material to its smaller basis; do not substitute another fixed diagram ordering without checking. The defining relations explicitly include squares equal to 1. The abstract/metadata fetched by the arXiv reader differs slightly from v2's printed abstract; v2's title page has **both Pang and Wang**, not Wang alone. No journal publication was established in this search. The authors say the finite irreducible list is complete; this survey has not independently checked their computations or historical priority. In particular [US24] cites a 2007 E8 master's thesis, so “E8 first solved in 2026” would be unwarranted.

**[US24] Uğur Ustaoğlu**, *Gröbner–Shirshov bases and normal forms for the infinite Coxeter groups of types B-tilde_n and D-tilde_n*, *Journal of Universal Mathematics* 7, special memorial issue (2024), 86–101, [DOI:10.33773/jum.1562793](https://doi.org/10.33773/jum.1562793). **Opened publisher abstract and PDF.** Standard Coxeter alphabets `s0,...,sn`, degree-lex; Lemma 2.2 and the corresponding D section give basis families and normal forms. These are affine Coxeter, not affine Artin, results.

**[BCS07] L. A. Bokut, V. V. Chaynikov and K. P. Shum**, *Markov and Artin normal form theorem for braid groups*, *Communications in Algebra* 35 (2007), 2105–2115, [arXiv:0806.1124](https://arxiv.org/abs/0806.1124), [DOI:10.1080/00927870701302115](https://doi.org/10.1080/00927870701302115). **Opened PDF.** Artin–Markov relations form the GS basis in Artin–Burau generators for ordinary braids, using inverse-tower order, with deg-inverse-lex inside the stated blocks. The 2014 survey, §3.1.1, also notes a subsequent full composition treatment by Chen–Mo (2009); the original paper's conclusion is not a type-B result.

**[BG08] L. A. Bokut**, *Gröbner–Shirshov basis for the braid group in the Artin–Garside generators*, *Journal of Symbolic Computation* 43 (2008), 397–405, [arXiv:0806.1125](https://arxiv.org/abs/0806.1125), [DOI:10.1016/j.jsc.2007.02.003](https://doi.org/10.1016/j.jsc.2007.02.003). **Opened PDF.** Theorem 1.1 is an explicit family of GS relations for ordinary `B_{n+1}` on `a1,...,an,Delta,Delta^{-1}`. Word order is degree-lex with `Delta^{-1}<Delta<a1<...<an`. Separate inverse letters `a_i^{-1}` are unnecessary because of complements in Delta. Irreducibles give Garside normal forms. The positive-word parameters make the displayed family generally infinite.

**[BKL09] L. A. Bokut**, *Gröbner–Shirshov basis for the braid group in the Birman–Ko–Lee generators*, *Journal of Algebra* 321 (2009), 361–376, [arXiv:0806.1123](https://arxiv.org/abs/0806.1123), [DOI:10.1016/j.jalgebra.2008.10.007](https://doi.org/10.1016/j.jalgebra.2008.10.007). **Opened PDF.** The preprint title says “Birman–Ko–Lee–Garside generators”, accurately indicating the extra `delta^{±1}`. Gives a GS basis for ordinary braids; degree-lex with `delta^{-1}<delta<a_ts<a_rq` iff `(t,s)<(r,q)` lexicographically. Not an all-finite-type theorem.

**[BFKS03] L. A. Bokut, Y. Fong, W.-F. Ke and L.-S. Shiao**, *Gröbner–Shirshov bases for the braid semigroup*, in *Advances in Algebra* (2003), 60–72, [arXiv:0806.1118](https://arxiv.org/abs/0806.1118), [DOI:10.1142/9789812705808_0005](https://doi.org/10.1142/9789812705808_0005). **Opened PDF.** Gives the positive type-A braid-monoid basis in standard Artin generators and degree-lex; general Artin-monoid formulas are conjectural in its introduction. Do not date the original theorem to 2008 merely because of the later arXiv deposit.

**[BV06] Leonid Bokut and Andrei Vesnin**, *Gröbner–Shirshov bases for some braid groups*, *Journal of Symbolic Computation* 41 (2006), 357–371, [DOI:10.1016/j.jsc.2005.09.009](https://doi.org/10.1016/j.jsc.2005.09.009), [author PDF](https://math.nsc.ru/~vesnin/papers/bokut-vesnin2006.pdf). **Opened PDF**, after ScienceDirect returned 403. Propositions 3.1 and 3.2 cover **all two-generator Artin groups** `A(m)`, not only `A(3)=B3`. For `m=2n`, use `t=x`, `y_i=t^i y t^{-i}` (`0<=i<n`) and their inverses, a free-by-cyclic presentation, and tower order. For `m=2n+1`, use `t=x`, conjugates `z_i=t^i(yx^{-1})t^{-i}` (`0<=i<2n`) and inverses. For B3/B4, Gorin–Lin generators/tower order give bases and normal forms (Theorem 5.1 for B4). This settles the rank-two **changed-alphabet** problem, not the book's named Burau/Garside-alphabet version.

**[CZ13] Yuqun Chen and Chanyan Zhong**, *Gröbner–Shirshov bases for braid groups in Adyan–Thurston generators*, *Algebra Colloquium* 20(2) (2013), 309–318, [arXiv:0909.3639](https://arxiv.org/abs/0909.3639), [DOI:10.1142/S1005386713000278](https://doi.org/10.1142/S1005386713000278). **Opened abstract, publisher DOI abstract and PDF.** Type A is treated in §2; **type B** is treated in §3. Alphabet: `r(alpha)` for every nonidentity element of the appropriate finite Coxeter group, plus `Delta^{-1}` for the group. Letters satisfy `r(alpha)<r(beta)` if Coxeter length of alpha is *larger*, with lex tie-break; use degree-lex on words. Theorems 3.3 and 3.6 give the positive-monoid and group bases; Corollary 3.7 gives `Delta^k r(alpha1)...r(alphas)`. This is an important correction to reading the 2014 survey's “except braid groups/type A” sentence literally as exhaustive.

**[AU07] Marc Autord**, *Comparing Gröbner bases and word reversing*, arXiv preprint (2007), [arXiv:0712.0525](https://arxiv.org/abs/0712.0525). **Opened abstract and PDF**, especially §3.1. Shows the two completion procedures can differ radically. Example 3.3 supplies the reduced positive B3 basis `{bab=aba} ∪ {ba^n ba=aba^2 b^{n-1}: n>=2}`, degree-lex `b>a`. Proposition 3.4 treats noncommuting two-generator Artin presentations and shows infinite degree-lex completion despite finite reversing-completeness; its even-parameter proof explicitly gives `{(ba)^n=(ab)^n} ∪ {ba^p(ab)^n=(ab)^n ba^p: p>=1}` (use `n>=2` for the noncommuting case). Thus positive G2/dihedral completion is not wholly unstudied. Proposition 3.5 proves infinitude of degree-lex completion for ordinary positive braid monoids with at least three strands. These are **positive monoid**, not Delta/inverse group, results; no claim about every possible monomial order is made here.

**[IMAN24] Zaffar Iqbal, Muhammad Mobeen Munir, Maleeha Ayub and Abdul Rauf Nizami**, *Complete presentation and Hilbert series of the mixed braid monoid MB_{1,3}*, *Revista de la Unión Matemática Argentina* 67(2) (2024), 503–516, [DOI:10.33044/revuma.3479](https://doi.org/10.33044/revuma.3479), [publisher PDF](https://inmabb.criba.edu.ar/revuma/pdf/v67n2/v67n2a06.pdf). **Opened PDF.** Page 505 explicitly identifies this monoid with the **Artin monoid of type B3**. Theorem 2.3 gives standard-positive-generator completion families for `z3z2z3=z2z3z2`, `z2z1z2z1=z1z2z1z2`, `z3z1=z1z3`, with length-lex `z1<z2<z3`. There are eleven parameterized additional families, not eleven individual finite rules. No inverse/Delta group completion is supplied. This 2024 paper is a genuine non-A positive-monoid result missed by a search limited to titles containing “Artin” or “Gröbner–Shirshov”. It was found through Hilbert-series/citation trails. The basis calculation has not been independently audited here.

### B2. The most relevant finite-type and general-monoid rewriting results

| Reference | Actual theorem and alphabet | Order/convergence and limitation |
|---|---|---|
| **[HM99] Susan M. Hermiller and John Meier**, *Artin groups, rewriting systems and three-manifolds*, *Journal of Pure and Applied Algebra* 136 (1999), 141–156; [DOI:10.1016/S0022-4049(97)00171-0](https://doi.org/10.1016/S0022-4049(97)00171-0), [author PDF](https://www.math.unl.edu/~shermiller2/webppr/artin.pdf). **Opened PDF.** Included although before the main search window because essential to interpreting the question. | Theorem 1: every finite-type Artin **group** has a geodesic finite complete rewriting system. §3 uses `S={ [w]: w in W\{1} }`, i.e. every nonidentity positive simple. First alphabet `S ∪ {Delta^{-1}}`; second alphabet `S ∪ S^{-1}`. Theorem 2 additionally treats groups whose defining graph is a tree. | §3.1 orients a **right-greedy** system by shortlex: positive letters are ordered by their underlying Coxeter length, and the inverse Delta letter is largest. §3.2 gives the signed-simple system with the corresponding positive/negative length ordering. These are explicit finite complete systems, not merely existence of a normal form. Neither alphabet is `{sigma_i,Delta^{±1}}`. The printed overbars denote inverse letters and are lost in plain-text extraction. |
| **[GGM15] Stéphane Gaussent, Yves Guiraud and Philippe Malbos**, *Coherent presentations of Artin monoids*, *Compositio Mathematica* 151 (2015), 957–998; [arXiv:1203.5358](https://arxiv.org/abs/1203.5358). **Opened abstract and PDF.** | Proposition 3.2.1 gives a coherent **convergent** presentation of the Artin **monoid** on `W\{1}`: length-additive multiplication rules `u|v -> uv` and completion/sliding rules `u|vw -> uv|w` with the exact length conditions in §3.1. The alphabet/rule set is finite for finite W and generally infinite otherwise. Theorem 4.1.1 gives a coherent presentation on **standard atoms**, with one Tits–Zamolodchikov 3-cell for each finite rank-three parabolic. | §3.2's termination comparison first uses number of simple letters and then their Coxeter lengths from the right. The standard-atom result is **coherence**, not a claim that the oriented Artin relations are confluent. Group inverses are not part of these monoid theorems. |
| **[DDH15] Patrick Dehornoy, Matthew Dyer and Christophe Hohlweg**, *Garside families in Artin–Tits monoids and low elements in Coxeter groups*, *Comptes Rendus Mathématique* 353 (2015), 403–408; [arXiv:1411.7498](https://arxiv.org/abs/1411.7498). **Opened abstract and PDF.** | Theorem 1.1: every finitely generated Artin–Tits **monoid** has a finite Garside family. Theorem 1.2 concerns low Coxeter elements, including finiteness and closure under suffix/join. | The arXiv abstract says “group”, but the actual theorem says **monoid**; use the theorem. This provides the finite alphabet used by [DG16], not a group presentation on standard atoms. |
| **[DG16] Patrick Dehornoy and Yves Guiraud**, *Quadratic normalization in monoids*, *International Journal of Algebra and Computation* 26(5) (2016), 935–972; [arXiv:1504.02717](https://arxiv.org/abs/1504.02717), [DOI:10.1142/S0218196716500399](https://doi.org/10.1142/S0218196716500399). **Opened abstract and PDF.** | Proposition 6.3.3: for a left-cancellative monoid with no nontrivial units and Garside family S, rules normalize each **pair of S-letters** to its minimal-length S-normal decomposition; the resulting system on `S\{1}` is convergent. Corollary 6.3.4: every finitely generated Artin–Tits monoid admits a **finite quadratic convergent presentation**. In spherical type S can be all simples/positive W-lifts. | Theorems B/C and Proposition 5.2.1 establish termination via class-(4,3) normalization/domino arguments; this is not a theorem about standard-atom degree-lex. The bound in Theorem B is `2^p-p-1`, not `2p-p-1` (the PDF-to-text superscript is lost). “Quadratic” allows a length-two left side and a shorter normal output after deleting the unit letter. |
| **[BS07] Patrick Bahls and Tyler Smith**, *Rewriting systems and orderings on Artin monoids*, *International Journal of Algebra and Computation* 17(1) (2007), 61–75; [DOI:10.1142/S0218196707003482](https://doi.org/10.1142/S0218196707003482). **Opened publisher-supplied abstract via DOI/Crossref; full text not opened.** | Constructs a complete rewriting system for every **large-type Artin monoid**, derived from Burckel's well-ordering, and studies associated well-orderability. | Do not infer finiteness, exact alphabet, or the requested Delta-order completion from the abstract. “Large type” does not include all spherical types: commuting pairs matter. |

Additional useful structural sources, not substitutes for the requested GS completion:

- **[BE03] David Bessis**, *The dual braid monoid*, *Annales scientifiques de l'École normale supérieure* 36 (2003), 647–683; [arXiv:math/0101158](https://arxiv.org/abs/math/0101158), [DOI:10.1016/j.ansens.2003.01.001](https://doi.org/10.1016/j.ansens.2003.01.001). **Opened abstract; PDF saved.** Constructs a dual Garside monoid for every finite Coxeter type, with reflection rather than simple-reflection generators; type A recovers BKL. No specific GS monomial order is asserted in the abstract.
- **[PI02] Matthieu Picantin**, *Explicit presentations for the dual braid monoids*, arXiv preprint posted 2001, [arXiv:math/0111280](https://arxiv.org/abs/math/0111280) (the citation key is only mnemonic; publication venue/year not established here). **Opened abstract; PDF saved.** Explicit dual presentations for B and D and their Garside combinatorics; not a verified GS completion.
- **[JN23] Matthieu Josuat-Vergès and Philippe Nadeau**, *Koszulity of dual braid monoid algebras via cluster complexes*, *Annales mathématiques Blaise Pascal* 30(2) (2023), 141–188; [arXiv:2107.13442](https://arxiv.org/abs/2107.13442), [DOI:10.5802/ambp.420](https://doi.org/10.5802/ambp.420). **Opened abstract, publisher page and PDF passages.** Journal issue is 2023; publisher says online 2024-04-30. Theorem 1.1 proves Koszulity of `k[D(W)]`; §5 constructs a PBW basis of the **quadratic dual `P(W)`**. Do not turn this into a GS theorem for `B(W)` or even a statement that the original dual-monoid relations already form a GS basis.

### B3. Singular, virtual, inverse and complex braid sources

- **[VS10] V. V. Vershinin**, *On the singular braid monoid*, *St. Petersburg Mathematical Journal* 21 (2010), 693–704; [arXiv:math/0309339](https://arxiv.org/abs/math/0309339), originally posted 2003. **Opened abstract and PDF.** Theorems 1–2: Garside/greedy normal forms; Theorem 6: BKL-style generators `a_ts^{±1},b_qp` and presentation. The normal-form theorem is not a GS-composition theorem. The book already knew this work.
- **[CH06] V. V. Chaynikov**, *Garside structure for singular braid monoid in Birman, Ko, Lee generators*, *Communications in Algebra* 34 (2006), 1981–1995; [DOI:10.1080/00927870500542952](https://doi.org/10.1080/00927870500542952). **[UNVERIFIED] theorem content**: metadata opened, no abstract returned; publisher 403 and a MathNet full-text route timed out. The book's prose dates the relevant work 2007, whereas the journal metadata is 2006. Do not manufacture a GS result from the title.
- **[KO20] Eylem Güzel Karpuz and Nurten Urlu Özalan**, *Word problem for special braid groups*, *Quaestiones Mathematicae* 43(7) (2020), 931–957; [DOI:10.2989/16073606.2019.1588178](https://doi.org/10.2989/16073606.2019.1588178), [institutional PDF](https://acikerisim.karatay.edu.tr/yayinaea/word-problem-for-special-braid-groups_6721fbee6920f.pdf). **Opened PDF.** Online first 2019-03-25. Theorems 2.1/2.2 claim GS bases for PV3/PVn (`n>=4`) on `mu_ij^{±1}`, degree-lex, larger index pair larger, each positive letter above its inverse. This is not full VBn, and the displayed-list caveat below prevents treating the claimed result as independently established here.
- **[KOC19] Eylem Güzel Karpuz, Nurten Urlu Özalan and A. Sinan Çevik**, *Gröbner–Shirshov basis for complex reflection group*, *Konuralp Journal of Mathematics* 7(1) (2019), 79–90; [publisher PDF](https://dergipark.org.tr/tr/download/article-file/697952). **Opened PDF; DOI/arXiv not found.** Despite its short title, it explicitly starts with a braid-group presentation associated with G24, then uses `s,t,u` and inverse letters. Theorem 3.2 claims a GS basis, degree-lex with positive-letter order `u>s>t`; placement of inverse letters is not fully specified. See caveat below. Do not confuse with the G12 finite-quotient issue.
- **[CA20] Ahmet Sinan Çevik and Amer Hassan Albargi**, *A solution of the word problem for braid groups via the complex reflection group G12*, *Filomat* 34(2) (2020), 461–467; [DOI:10.2298/FIL2002461C](https://doi.org/10.2298/FIL2002461C). **Opened abstract and PDF.** Theorem 3.1, p.463, explicitly presents `s²=u²=t²=1`, `suts=utsu`, `tsut=suts`. Theorem 3.2 completes these on `s,u,t` with degree-lex `t>u>s`. Thus the displayed object is the finite reflection quotient G12, not a demonstrated GS basis for its braid group. The title/abstract alone is unsafe evidence for question (7).
- **[VI09] Vladimir V. Vershinin**, *On the inverse braid monoid*, *Topology and its Applications* 156 (2009), 1153–1166; [arXiv:0704.3002](https://arxiv.org/abs/0704.3002). **Opened abstract; PDF saved.** Word problem via an embedding into partial monomorphisms of a free group and a Garside-style approach; also two-generator Artin-style and graph presentations. This is not a stated standard-generator GS basis for IBn.
- **[CI20] Ahmet S. Çevik, Eylem G. Karpuz, Hamed H. Alsulami and Esra K. Çetinalp**, *A Gröbner–Shirshov basis over a special type of braid monoids*, *AIMS Mathematics* 5(5) (2020), 4357–4370; [DOI:10.3934/math.2020278](https://doi.org/10.3934/math.2020278). **Opened publisher abstract and saved PDF.** Object is the **symmetric inverse monoid I_n**. This is not IBn; the involutive permutation generators are a decisive distinction.
- **[CLL15] Ruth Corran, Eon-Kyung Lee and Sang-Jin Lee**, *Braid groups of imprimitive complex reflection groups*, [arXiv:1404.5430](https://arxiv.org/abs/1404.5430), preprint 2014. **Opened abstract; PDF saved.** New positive homogeneous presentations for `B(de,e,r)` (`d,r>=2`), quasi-Garside structures, and a semidirect product with affine type A. No completed standard-generator GS basis is stated in the opened abstract. Journal metadata was not independently established here.
- **[FM26] Francesca Fedele and Bethany Rose Marsh**, *Presentations of the braid group of the complex reflection group G(d,d,n)*, *Journal of the London Mathematical Society* (2026), [DOI:10.1112/jlms.70478](https://doi.org/10.1112/jlms.70478), [arXiv:2412.12802](https://arxiv.org/abs/2412.12802). **Opened arXiv abstract; PDF saved.** Gives the index-d orbifold-braid subgroup description and presentations from tagged triangulations, recovering BMR presentations for a special triangulation. It is a 2026 presentation result, not an abstract claim of a GS completion.

## C. Important source-reading qualifications

### The 2014 survey is not a current blanket nonexistence theorem

**L. A. Bokut and Yuqun Chen**, *Gröbner–Shirshov bases and their calculation*, *Bulletin of Mathematical Sciences* 4 (2014), 325–395, [arXiv:1303.5366](https://arxiv.org/abs/1303.5366), [DOI:10.1007/s13373-014-0054-6](https://doi.org/10.1007/s13373-014-0054-6). **Opened PDF**, particularly introduction and §3.1.

- Local text lines 550–553 say: “Artin–Tits groups ... GS bases are not known except for braid groups (the Artin–Tits groups of type A_n).” This is a historical generalization, not adequate as a 2026 verdict: [BV06] covers all rank two in changed generators, and the survey itself cites [CZ13], whose §3 treats type B.
- §3.1 distinguishes Artin–Burau, Artin–Garside, BKL, and Adjan/Adyan–Thurston alphabets. Theorem 3.2 explicitly uses inverse-tower order; §3.1.2 explicitly uses `Delta^{-1}<Delta<sigma1<...<sigman` degree-lex.
- The introduction's broad finite-Coxeter sentence should not be used to assign priority for E8/H4; newer primary papers and earlier thesis citations are more precise.

### Two published claimed bases with visible inverse-overlap concerns

These are **[INFERENCE] from the displayed relations and the specified degree-lex order**, not a published erratum, not a full proof audit, and not a machine verification. They are recorded to avoid promoting a paper's theorem heading to a certified solution.

1. **[KO20], Theorem 2.1, pp.934–935.** It lists the positive rule `mu23 mu13 mu12 -> mu12 mu13 mu23` and cancellation `mu12 mu12^{-1}->1`. The overlap word
   `mu23 mu13 mu12 mu12^{-1}`
   has the two reducts `mu23 mu13` and `mu12 mu13 mu23 mu12^{-1}`. For the displayed list (1)–(26), the former has length two with no inverse pair; the latter has no listed positive leading triple, no longer positive leading word, and no cancellation. Thus they appear distinct irreducibles. The paper lists this overlap among ambiguities but does not display its reduction to zero. This needs repair/independent checking before the displayed system is relied upon.
2. **[KOC19], Theorem 3.2, p.81.** The displayed noncancellation rules are positive, including `sts->tst` (`u>s>t`), and the remaining rules cancel inverse pairs. The overlap `sts s^{-1}` reduces either to `st` or to `tst s^{-1}`; neither contains a displayed leading positive rule or inverse cancellation. This is the same structural issue. The paper's presentation is of the complex braid group, unlike [CA20], but its claimed group basis still cannot be accepted here without resolving this issue.

These cautions do not claim the word problems themselves are unsolvable, nor that no corrected basis exists.

## D. Later surveys, 2020 book, citation chains, and standard-generator automaticity

### D1. Later Bokut/Chen material and the 2020 monograph

1. **Bokut–Chen, *Gröbner–Shirshov bases and PBW theorems***, [arXiv:1502.06472](https://arxiv.org/abs/1502.06472). **Opened abstract and PDF.** §5 lists braid normal forms in Artin–Burau, Artin–Garside, BKL and Adyan–Thurston generators, citing the familiar papers. It does not supply a new non-A atom-plus-Delta theorem. The document has a 2014 datestamp; Chen's 2018 CV records the related journal paper in *Journal of Siberian Federal University, Mathematics and Physics* 6(4) (2013), 417–427. The later arXiv identifier is not evidence of a new 2015 solution.
2. **L. A. Bokut, Yuqun Chen and Abdukadir Obul**, *Some new results on Gröbner–Shirshov bases for Lie algebras and around*, *International Journal of Algebra and Computation* 28(8) (2018), 1403–1423, [DOI:10.1142/S0218196718400027](https://doi.org/10.1142/S0218196718400027). **Opened publisher-supplied abstract via DOI/Crossref; full text not opened.** Its stated scope is Lie, operated Lie, Gelfand–Dorfman–Novikov, Leibniz, and extension results. No Artin-group update is stated in that abstract; **the full paper's Artin status discussion is [UNVERIFIED]**.
3. The similarly titled *Gröbner–Shirshov Bases: Some New Results* (Bokut–Chen, [arXiv:0804.1344](https://arxiv.org/abs/0804.1344)) and *Some new results on Gröbner–Shirshov bases* (Bokut–Chen–Shum, [arXiv:1102.0449](https://arxiv.org/abs/1102.0449)) are **older leads**, not 2014–2026 updates. Their full mathematical texts were not opened here: **[UNVERIFIED]**. Chen's opened 2018 CV dates the latter proceedings version to 2012, pp.53–102.
4. **Leonid Bokut, Yuqun Chen, Kyriakos Kalorkoti, Pavel Kolesnikov and Viktor Lopatkin**, *Gröbner–Shirshov Bases: Normal Forms, Combinatorial and Decision Problems in Algebra*, World Scientific (2020), 308 pp., [DOI:10.1142/9287](https://doi.org/10.1142/9287), ISBN 9789814619486 / 9789814619509. **Opened author-institution description, Google Play book page, and an actual Google Books preview/TOC** ([book ID GmjvDwAAQBAJ](https://books.google.com/books?id=GmjvDwAAQBAJ&printsec=frontcover)).
   - The author-institution and Google Play descriptions mention the **Artin–Markov braid normal form in Burau generators**, not a theorem for non-A Artin–Tits groups.
   - The preview TOC gives chapters: Introduction; Free algebras; Composition–Diamond Lemma; Applications; Lie algebras over a commutative algebra; Decision problems for groups; (Co)homology. It does not display a dedicated all-type Artin chapter.
   - Actual preview pages **53–55** were visually opened. §4.1 starts with the general semigroup/group GS-to-normal-form dictionary; p.54's example and Theorem 4.2 concern the **alternating group**, not an Artin group of type A; p.55 proceeds to the **Chinese monoid** (Theorem 4.4).
   - The in-book search `Artin` returned “No results found”; this is **not** reliable proof of absence because it is a limited preview/search index. No non-A Artin theorem or updated open-problem declaration was verified in the opened portion. **The unviewed book is [UNVERIFIED] for such a claim.** Therefore this book is not used to certify either solution or continued openness.
   - Access attempts: World Scientific book page and write-up endpoint returned 403; Google Books API ISBN query returned 429; accessible HTML preview returned 403; the ordinary interactive Google Books preview worked. No purchase/sign-in was performed, and no complete copyrighted book was downloaded.
5. **SCNU group check:** opened the [faculty listing](https://maths.scnu.edu.cn/shizhi/yjsds/) and [Chen's 2018 CV/publication list](https://statics.scnu.edu.cn/pics/userfiles/2018/0620/20180620103813693.pdf). The live individual profile was blocked by the site. The CV confirms [CZ13], the 2014 survey, and later algebra-focused work, but is dated and not a complete 2026 bibliography. It was saved as `chen-2018-scnu-cv.pdf`.

### D2. Forward-citation searches, rather than relying only on the old survey

The following **programmatic searches were actually executed** with public APIs (no key/account needed). The specialized reader could not parse the Semantic Scholar API URL, so the same endpoint was fetched with `urllib` and a browser user-agent. All returned pages fit the requested limits; no `next` offset was returned for the two Semantic Scholar citation sets.

- [Semantic Scholar: Bokut Artin–Garside citations](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.jsc.2007.02.003/citations?fields=title,year,externalIds&limit=100): **22 records**.
- [OpenAlex: same DOI metadata](https://api.openalex.org/works/https://doi.org/10.1016/j.jsc.2007.02.003) resolves to `W2048168233`; [citing works](https://api.openalex.org/works?filter=cites:W2048168233&per-page=100&select=id,title,publication_year,doi): **29 records**, including duplicate/preprint records and book chapters.
- [Semantic Scholar: BFKS arXiv citations](https://api.semanticscholar.org/graph/v1/paper/ARXIV:0806.1118/citations?fields=title,year,externalIds&limit=100): **15 records**. The [published-chapter DOI query](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1142/9789812705808_0005/citations?fields=title,year,externalIds&limit=100) returned the same count/list.
- [OpenAlex: BFKS chapter DOI](https://api.openalex.org/works/https://doi.org/10.1142/9789812705808_0005) resolves to `W2962733537`; [citing works](https://api.openalex.org/works?filter=cites:W2962733537&per-page=100&select=id,title,publication_year,doi): **18 records**.

Important candidates were opened rather than dismissed from titles:

- **Xing Chen and Xuezhi Zhao**, *Normal forms in braid groups with respect to some Gröbner–Shirshov basis*, *Journal of Knot Theory and Its Ramifications* 29(13) (2020), 2043005, [DOI:10.1142/S0218216520430051](https://doi.org/10.1142/S0218216520430051). **Opened DOI abstract.** Derives concrete irreducible/normal-form expressions from **Bokut's 2008 ordinary-braid Artin–Garside basis**. No non-A extension is claimed in the opened abstract. No OA PDF located.
- **Usman Ali and Barbu Berceanu**, *Canonical forms of positive braids*, *Journal of Algebra and Its Applications* 14 (2015), 1450076, [DOI:10.1142/S0219498814500765](https://doi.org/10.1142/S0219498814500765). **Opened DOI abstract.** Consequences of the positive ordinary-braid GS basis (canonical/square-free forms, exponents and divisibility), not a non-A group theorem.
- [CZ13], [KO20], [KOC19], and [AU07] were opened; their exact scope/caveats are above. The G24 paper was found through Semantic Scholar/OpenAlex even though broad title searches were poor.
- **Zaffar Iqbal, Xiujun Zhang, Mobeen Munir and Ghina Mubashar**, *Hilbert series of mixed braid monoid MB_{2,2}*, *AIMS Mathematics* 7(9) (2022), 17080–17090, [DOI:10.3934/math.2022939](https://doi.org/10.3934/math.2022939). **Opened publisher abstract; PDF saved.** An ambiguity-free presentation for a particular mixed **monoid**; it is not a claimed all-B-type Delta group basis. Following its references/nearby Hilbert-series literature found the genuine type-B3 monoid result [IMAN24].
- **E. G. Karpuz, F. Ateş, N. Urlu, A. S. Çevik and I. N. Cangul**, *A note on the Gröbner–Shirshov bases over ad-hoc extensions of groups*, *Filomat* (2016), [DOI:10.2298/FIL1604037K](https://doi.org/10.2298/FIL1604037K). **Opened DOI abstract only.** Knit products of cyclic groups and iterated semidirect products of free groups; no specified non-A Artin alphabet in the abstract.
- **E. G. Karpuz, F. Ateş and A. S. Çevik**, *Gröbner–Shirshov bases of some Weyl groups*, *Rocky Mountain Journal of Mathematics* 45 (2015), 1165–1175, [DOI:10.1216/RMJ-2015-45-4-1165](https://doi.org/10.1216/RMJ-2015-45-4-1165). **Opened DOI abstract only.** Extended/elliptic Weyl groups with toroidal-type generators, not spherical Artin groups.
- *Gröbner–Shirshov bases of some monoids*, DOI `10.1016/j.disc.2011.03.008`, and *Gröbner–Shirshov bases of some semigroup constructions*, DOI `10.1142/S100538671500005X`, remained **[UNVERIFIED] for content** (metadata/no abstract or 403). They are not used as proof of a null result.

**Citation-chain conclusion:** no opened citing paper gives the requested non-A **group** GS basis in the small alphabet `{sigma_i,Delta^{±1}}`, and none supplies the missing uniform Artin–Burau result. This is a bounded bibliographic observation. API coverage is incomplete, counts are not total worldwide citation counts, and failure to index a paper is not evidence of nonexistence.

### D3. Standard-generator lex/shortlex languages: what is actually known here

| Source and opened flag | Exact language/alphabet | What it does not establish |
|---|---|---|
| **[HR12] Derek F. Holt and Sarah Rees**, *Artin groups of large type are shortlex automatic with regular geodesics*, *Proceedings of the London Mathematical Society* 104 (2012), 486–512; [arXiv:1003.6007](https://arxiv.org/abs/1003.6007), [DOI:10.1112/plms/pdr035](https://doi.org/10.1112/plms/pdr035). **Opened abstract and PDF**, §§1–2. | Standard signed alphabet `X ∪ X^{-1}`, **any ordering**. Large type: every finite off-diagonal Artin parameter is at least 3; no commuting pair. Shortlex automaticity and FFTP/regularity of all geodesics. The paper separately proves the two-generator versions for every `m>=2` (Theorems 2.4/2.6), hence covers G2/dihedral directly. | It does not cover all spherical types: A3, B3 and higher familiar types contain a commuting pair. Shortlex automaticity is not itself a finite GS-rule list. |
| **Fuchiwaki–Fujii–Saito–Tsuchioka**, *Geodesic automata and growth functions for Artin monoids of finite type*, RIMS preprint 1646 (2008), [primary PDF](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1646.pdf). **Opened PDF**, abstract and §§4–5. | Constructs a finite-state **unique geodesic cross-section on the standard positive atoms for every finite-type Artin monoid**. It replaces each simple letter in a Charney language by a chosen atom-word lift `iota`; §5.2 makes the dependence on this lift explicit. Then determinizes/minimizes the acceptor. | The theorem is not that these words are globally **lexicographically least** among all atom-words. “Geodesic” alone is weak for a homogeneous positive monoid: all positive representatives of an element have the same atom length. This does not prove a standard-atom shortlex group language or an atom-plus-Delta GS basis. |
| **Ramón Flores and Juan González-Meneses**, *On lexicographic representatives in braid monoids*, *Journal of Algebraic Combinatorics* 52 (2020), 561–597; [arXiv:1808.02755](https://arxiv.org/abs/1808.02755). **Opened abstract and PDF**, introduction and §2. | The minimal/maximal lexicographic representatives of the **positive type-A braid monoid** on standard atoms are regular. Describes the minimal DFA, following Gebhardt–González-Meneses, with detailed state counts. Positive relations preserve length, so minimal lex is also shortlex in this monoid setting. | Not a theorem for all finite types, not a theorem for signed group words, and not a theorem after adding Delta. |
| **Derek F. Holt and Sarah Rees**, *Artin groups of type (2,3,n)*, arXiv preprint (2023), [arXiv:2310.14632](https://arxiv.org/abs/2310.14632). **Opened abstract and PDF**, Theorem 1.1. | For the rank-three presentation `aba=bab`, `ac=ca`, `[bc]_n=[cb]_n`, `n>=5`, length-preserving rules plus free cancellation reduce signed standard-generator words to **a geodesic representative** in quadratic time. This includes the spherical H3 case `n=5`. | Does not assert a unique shortlex normal form, a regular shortlex language, or a confluent GS presentation. Do not infer those stronger results from a geodesic word-problem algorithm. |
| **Sarah Rees**, *The development of the theory of automatic groups*, 2022 survey, [arXiv:2205.14911](https://arxiv.org/abs/2205.14911). **Opened PDF**, §5.1. | Explicitly says Charney's spherical-type biautomatic structures are geodesic over **Garside/simple-element generators, not the standard generators**. Also summarizes standard-generator shortlex for large/sufficiently large type. | Ordinary automaticity/biautomaticity is invariant under change of finite generators, but **being the shortlex language for a particular alphabet/order is not supplied by that invariance**. |

Thus there are strong positive standard-alphabet results, especially rank two, type-A positive monoids, and standard-atom *cross-sections* for all spherical positive monoids. **No opened source in this search establishes a uniform regular lex/shortlex language for every spherical Artin group over the standard signed generators, or for every non-A group over `{sigma_i,Delta^{±1}}`.** Likewise the all-finite-type monoid cross-section source must not be advertised as an all-finite-type lex-minimal theorem. These are search-scoped statements, not claims that these language questions are proven open.

## E. Exact search log and notable null results

### E1. Web queries (verbatim strings sent to the search tool)

The search tool provides both links and an automatic prose summary. **The prose was treated only as discovery material**: several summaries conflated groups/monoids, type-A braid notation/type B, or supplied the wrong arXiv ID. Conclusions above use opened primary text instead.

#### Initial GS, Coxeter, generator and subgroup searches

```text
"Gröbner-Shirshov" "Artin" group basis
"Gröbner-Shirshov" Coxeter "conjecture"
"Artin" "finite complete rewriting" Hermiller Meier
"Gröbner-Shirshov" "Artin" "type B"
"Gröbner-Shirshov" "dihedral" Artin
Gaussent Guiraud Malbos coherent presentations Artin monoids
Dehornoy Guiraud quadratic normalization Artin Garside
Bokut Chen "Gröbner-Shirshov" "new results" survey
"Gröbner-Shirshov" "singular" braid
"Gröbner-Shirshov" "virtual braid"
"Gröbner-Shirshov" "welded"
"Gröbner-Shirshov" "inverse braid"
"Gröbner-Shirshov" "complex reflection" braid
"Quadratic normalisation" "Guiraud"
"Artin-Tits" "finite" "convergent"
site:scnu.edu.cn "陈裕群" "Gröbner" Artin
Bokut Chen survey "Gröbner-Shirshov bases method" 2018 2020 2024
Kalorkoti "Gröbner–Shirshov" Artin
"Gröbner-Shirshov" "Artin" "D_n"
"Gröbner-Shirshov" "Birman" "type B"
"Artin-Burau" "type B"
"Gröbner-Shirshov" "Artin" "F4" "E8"
"Quadratic normalisation in monoids" journal 2017
"Garside families in Artin-Tits monoids and low elements" arxiv
"Gröbner-Shirshov" "H4" "H3" Lee 2018
"Gröbner-Shirshov" "Artin-Tits monoid"
Vershinin "On the singular braid monoid" Birman Ko Lee normal form
"Gröbner-Shirshov" "Artin" after:2014-01-01 before:2026-10-15
"Bokut" "Chen" "Obul" "Some new results" arxiv
"complex reflection" "braid" "convergent" rewriting
"dual braid monoid" "Gröbner"
Picantin "Explicit Presentations for the Dual Braid Monoids" arxiv
Bessis "The dual braid monoid" arxiv
Fedele Marsh "Presentations of the braid group" "arxiv"
Bokut Vesnin "Gröbner–Shirshov bases for some braid groups" pdf
Bokut Chen "Gröbner-Shirshov bases method" survey after:2014-01-01
"Coxeter" "pre-Gröbner-Shirshov" after:2009-01-01
"Gröbner-Shirshov" "Artin-Garside" "type" -site:researchgate.net
阿廷 群 Gröbner Shirshov 基 陈裕群 B型
"singular braid" "Groebner" basis
"welded braid" "rewriting system"
"inverse braid monoid" "complete rewriting"
site:zbmath.org "Artin" "Shirshov"
site:mathscinet.ams.org "Artin" "Shirshov"
"Garside Structure for Singular Braid Monoid in Birman, Ko, Lee Generators"
site:arxiv.org "Artin" "Groebner-Shirshov"
"virtual braid" "Shirshov" after:2020-01-01
"Koszulity of dual braid monoid algebras via cluster complexes" arxiv
"Rewriting Braids" 2019 Endrullis
"Artin monoid" "finite complete rewriting system"
Bahls Smith "Rewriting Systems and Orderings on Artin Monoids" pdf
"Chen" "Liu" "Gröbner-Shirshov bases for Coxeter groups I" journal
"Bokut" "Shiao" "Coxeter groups" 2001 pdf
"Gröbner-Shirshov" "affine" "Coxeter" arxiv
```

#### Book, forward-citation and standard-language follow-ups

```text
"9789814619486" "Artin"
"shortlex automatic" "Artin" "finite type" "standard"
"lexicographic normal form" "Artin monoid" regular
Holt Rees "Artin" "shortlex" spherical
"Gröbner–Shirshov Bases" "2020" "books.google"
"9287" "Shirshov" "Contents"
"Gröbner-Shirshov Basis for Complex Reflection Group" 2019
"Gröbner–Shirshov Bases" "2020" "Artin–Tits"
"Normal forms in braid groups with respect to some" pdf
"Artin monoids" "lexicographic" "regular"
"spherical" "Artin" "shortlex" "standard generators"
"Artin" "lexicographic" "automaton" "spherical"
"Artin monoids" "lexicographically" "finite" "regular"
"Artin" "standard generators" "shortlex" "open"
"Geodesic automata and growth functions for Artin monoids of finite type"
"braid groups" "shortlex automatic" "standard" open
"A Solution of the Word Problem for Braid Groups via the Complex Reflection Group G12" pdf
"9789814619509" "toc" OR "contents" OR "sample"
"The development of the theory of automatic groups" Rees arxiv
"Artin" "shortlex" "B_n" "finite"
"Artin" "shortlex" "Delta" "generators"
"spherical Artin" "lexicographic" normal form regular language
site:worldscientific.com "9287" "sample"
site:books.google.com "GmjvDwAAQBAJ" "Artin"
"Hilbert series of Artin Monoid" "I2"
"10.1142/9789812705808_0005" "cited"
"Iqbal" "Ali" "Hilbert series" "2013" "475"
"complete presentation" "Artin monoid"
"Gröbner" "braid monoid" "type B"
"Artin monoid" "D" "Gröbner"
"dihedral" "Garside" "Gröbner" basis
```

Programmatic citation endpoints are given in D2. Additional discovery endpoints actually requested: `https://www.googleapis.com/books/v1/volumes?q=isbn:9789814619486` (429); Semantic Scholar paper `c515ae4f634d3d896ae6109f9381b825f209e958` details (429/API failure); `https://api.openalex.org/works/W2951867106` (succeeded and located the G24 PDF). Google Books' in-book query was exactly `Artin`.

### E2. Notable null results and false positives

- No opened uniform Artin–Burau or small Artin–Garside basis was found for the non-A types named in (2). In particular, the real type-B theorem [CZ13] is **not** in either small alphabet. No direct standard-generator GS theorem for welded braid groups was located.
- The combination “complex reflection” plus “GS” frequently found reflection-group algebras, Hecke/Temperley–Lieb quotients, or misleadingly titled braid claims. [CA20] is a concrete finite-quotient false positive; [KOC19] is a genuine braid-presentation claim with the displayed inverse-overlap issue.
- “Inverse braid” found [CI20], which is actually I_n, not IB_n. “Singular” found the singular part of the **Brauer** semigroup, not the singular braid monoid.
- The 2014–2026 exact GS/Artin searches mostly recycled the older type-A papers and surveys. The **2024 type-B3 positive monoid paper** was found only through the mixed-braid/Hilbert-series trail. This limits how strongly any title-search null result can be interpreted.
- The indexed `site:zbmath.org` and `site:mathscinet.ams.org` queries returned mostly classification/irrelevant material rather than useful article records. This was **not a complete authenticated MathSciNet or zbMATH database search**.
- Picantin's paper is **math/0111280**, not `1508.06817`: opening the latter revealed Digne–Gobet, *Dual braid monoids, Mikado braids and positivity in Hecke algebras*, an unrelated-to-completion lead. It was not used as Picantin's paper.
- Search summaries sometimes asserted standard-generator shortlex automaticity for every braid group by citing large-type results; the opened [HR12] and Rees 2022 text do not support that inference. Likewise regularity of a lifted-simple cross-section is not regularity of the lex-minimal language.
- Chaynikov [CH06] and some generic semigroup-construction citations remain content-unverified. The 2020 book was accessed as an actual preview, but unviewed chapters are not evidence for either “solved” or “open”.

## F. Saved source files

All downloads listed here completed and were converted with `pdftotext -layout`. No computational GS checks, builds, tests, or heavy calculations were run. The new files are evidence only; no README or other project document was changed.

### New arXiv PDF/text pairs

For each listed ID, the download command was `curl -sSL -A 'Mozilla/5.0' https://arxiv.org/pdf/<id> -o sources/arXiv-<filename-id>.pdf`, followed by `pdftotext -layout` to the same basename with `.txt`. Old-style slash IDs use a hyphen in the local filename.

```text
arXiv-0704.3002.pdf
arXiv-0712.0525.pdf
arXiv-0909.3639.pdf
arXiv-0910.0096.pdf
arXiv-1003.6007.pdf
arXiv-1203.5358.pdf
arXiv-1404.5430.pdf
arXiv-1411.7498.pdf
arXiv-1502.06472.pdf
arXiv-1504.02717.pdf
arXiv-1808.02755.pdf
arXiv-1809.08419.pdf
arXiv-2107.13442.pdf
arXiv-2205.14911.pdf
arXiv-2310.14632.pdf
arXiv-2412.12802.pdf
arXiv-math-0101158.pdf
arXiv-math-0111280.pdf
arXiv-math-0309339.pdf
```

### New non-arXiv OA/author/institutional PDF/text pairs

No arXiv identifier was established for these downloads, so no fictitious `arXiv-...` identifier was assigned.

| Local PDF (matching `.txt` alongside) | Download source |
|---|---|
| `bokut-vesnin-2006-some-braid-groups.pdf` | https://math.nsc.ru/~vesnin/papers/bokut-vesnin2006.pdf |
| `hermiller-meier-1999-artin-rewriting.pdf` | https://www.math.unl.edu/~shermiller2/webppr/artin.pdf |
| `karpuz-ozalan-2020-special-braid-groups.pdf` | https://acikerisim.karatay.edu.tr/yayinaea/word-problem-for-special-braid-groups_6721fbee6920f.pdf |
| `cevik-et-al-2020-symmetric-inverse-monoid.pdf` | https://www.aimspress.com/aimspress-data/math/2020/5/PDF/math-05-05-278.pdf |
| `chen-2018-scnu-cv.pdf` | https://statics.scnu.edu.cn/pics/userfiles/2018/0620/20180620103813693.pdf |
| `ustaoglu-2024-affine-bd.pdf` | https://dergipark.org.tr/en/download/article-file/4269477 |
| `fuchiwaki-et-al-2008-geodesic-automata.pdf` | https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1646.pdf |
| `cevik-albargi-2020-g12.pdf` | https://www.pmf.ni.ac.rs/filomat-content/2020/34-2/34-2-18-10134.pdf |
| `iqbal-et-al-2022-mixed-braid.pdf` | https://www.aimspress.com/aimspress-data/math/2022/9/PDF/math-07-09-939.pdf |
| `karpuz-et-al-2019-g24.pdf` | https://dergipark.org.tr/tr/download/article-file/697952 |
| `iqbal-et-al-2024-type-b3-monoid.pdf` | https://inmabb.criba.edu.ar/revuma/pdf/v67n2/v67n2a06.pdf |

### Pre-existing PDF/text pairs reused without overwriting

`arXiv-0806.1118`, `arXiv-0806.1123`, `arXiv-0806.1124`, `arXiv-0806.1125`, `arXiv-1303.5366`, `arXiv-2002.07369`.
