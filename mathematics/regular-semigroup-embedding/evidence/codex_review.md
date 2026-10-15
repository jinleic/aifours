**Verdict:**

Theorems A–C’s embedding conclusions survive review. Section 7 contains false statements as displayed, with fixable omissions. The literature search does not certify openness or novelty.

| Item | Verdict | Qualification |
|---|---|---|
| Theorem A | correct | Both reductions and both converse constructions work. |
| Theorem B | correct | The cited embedding theorem is confirmed by Szendrei’s original 1987 abstract. |
| Theorem C | correct-with-minor-fixes | Two small proof omissions; its positive embedding case overlaps older results. |
| Lemma 0 | correct | The local idempotent-band descriptions work in both products. |
| Lemma 1 | correct | Uses the standard characterization \(\sigma^{-1}(1)=E(S)\). |
| Lemma 5 | correct | Handle the one-class local monoid separately as the trivial case. |
| Lemma 6 | correct | The listed conditions account for all mixed associativity cases. |
| Lemmas 2–3 and Lemma 4 | correct | No mathematical error found. |
| §7 | has-errors | C2 and C3 lack essential hypotheses; C3 also has an unstated intermediate argument. |
| Formalization | correct-with-minor-fixes | Faithful under the specified readings, which are not uniquely determined by the book. |
| Status claim | correct-with-minor-fixes | “No resolution found” is supported; “still open” is not certified. |

The following are the substantive results of checking the proofs.

- **Restricted-product formula, §0:** correct. If \(x=(i,g,\lambda)\) and \(y=(j,h,\mu)\), then
  \[
  y\wedge x=(j,p_{\lambda j}^{-1},\lambda),\qquad x(y\wedge x)=x.
  \]
  Thus the correction factor is \(\phi_{xx'}(a)=a\), giving
  \[
  (a,x)(b,y)=(a\phi_x(b),xy).
  \]
  The “some/every inverse” assertion agrees with Auinger–Polák’s Lemma 3.1. [Auinger–Polák, Definition 3.1](https://www.acta.hu/download.phtml?id=2399)

- **Lemma 0:** projection preserves the relevant order equations, and completely simple semigroups have equality as their natural order. For a local idempotent \((b,e)\), the local idempotent bands are respectively \(bBb\) and \(bBb\cap\operatorname{Fix}\phi_e\). These are regular bands. Regularity of the local subsemigroup follows from regularity of the subsemigroup \(U\).

- **Lemma 1:** the construction \(aa'ea\leq a\) works because orthodox bands are closed under conjugation. The argument establishing \(\sigma\cap\mathcal H=\Delta\) works with aligned inverses. Add a reference for the standard kernel characterization if the note is intended to be self-contained.

- **Lemmas 2–3:** the repeated middle band factor in Lemma 2 is legitimately removed by idempotency. In Lemma 3, \(^{h}f(g)=f(gh)\) has the correct composition order, including for nonabelian groups.

- **Theorem A:** the orthodox projected image supplies all idempotents on the occurring rectangular grid. Their multiplication forces \(p_{\lambda i}=u_\lambda v_i\). The Pastijn coordinate change preserves multiplication. In reading R, the projections in each row have a common image \(B_i\); \(\phi_{e_0}\) is injective on each \(B_i\), with the stated left inverse. The induced action on \(B_{i_0}\) consists of automorphisms. Subbands and products with rectangular bands remain in \(V\). The group-based constructions establish both converse directions.

- **Lemmas 4–6:** Lemma 4’s implication works in both directions by inserting elements of \(wBw\). Lemma 5 uses the singleton identity class and a rectangular ideal. Its extension to the stated structure-semilattice condition follows because local \(\mathcal D\)-classes do not split an ambient band class. Lemma 6’s remaining associativity cases with two bottom factors are automatic.

- **Theorem B:** its use of the regular-band embedding theorem is accurate. For a monoid in the problem’s class, \(1S1=S\), so the required global orthodoxy and regular band follow.

- **Theorem C, Step 1(a)–(d):** the local-band isomorphism excludes a shared \(\mathcal D_S\)-class; the ideal argument works after making its bottom-domain case explicit; the top-product calculation proves closure; and the regular primitive-idempotent argument gives rectangular groups. The identification of their group coordinates with subgroups of \(G\), and \(H_2=G\), follows.
- **Steps 2–3:** the row/column independence and the normal forms \(\Phi=\pi\sigma p\), \(\Psi=\pi'\sigma'p'\) follow from associativity and rectangular-group factorization.
- **Steps 4–5:** both families satisfy \(p^0_\mu\pi^0_\rho=\mathrm{id}\), including the dual family. A transversal of left cosets \(tH_1\) gives \(k_{ah}=k_ah\); no normality assumption on \(H_1\) is needed. The bottom–top calculation correctly uses the antihomomorphism order. The functor and injectivity arguments work. Local regularity of \(B_0^G\) uses closure of \(L(ReB)\) under direct powers, not a claim that the power has two \(\mathcal D\)-classes.

**Concrete errors:**

1. **Fatal as displayed; fixable — C2 omits matching group coordinates.**  
   [proof.md, §7, lines 471 and 476](/Users/jinleic/jinleic-workspace/ai4s/regular-semigroup-embedding/proof.md:471).

   In the group \(C_2=\{1,g\}\), choose \(s=s_1=t=1\), \(t_1=g\), with ordinary inverses. All three displayed idempotent equalities hold, but \(st=1\ne g=s_1t_1\).

   **Fix:** require \(\sigma(s)=\sigma(s_1)\) and \(\sigma(t)=\sigma(t_1)\). The proof then works; it does not actually require the two common coordinates to be inverses. For the preceding displayed \(\beta\)-formula, retain its additional inverse-coordinate hypothesis.

2. **Fatal as displayed; fixable — C3 omits \(\sigma(s)=\sigma(t)\).**  
   [proof.md, §7, line 472](/Users/jinleic/jinleic-workspace/ai4s/regular-semigroup-embedding/proof.md:472).

   Again take \(S=C_2\), now \(s=1,t=g\). Then \(p=q=1\), so \(p\mathcal D_Eq\), but
   \[
   q(t's)q=g\ne1.
   \]

   **Fix:** explicitly require \(s,t\) to belong to the same \(\sigma\)-class, specify \(\mathcal D_E\), and quantify the chosen inverses. The contextual sentences suggest these intended restrictions but do not state them adequately in the claims.

3. **Fixable proof gap — C3 does not establish the range-idempotent relation it uses.**  
   [proof.md, §7, line 490](/Users/jinleic/jinleic-workspace/ai4s/regular-semigroup-embedding/proof.md:490).

   The assertion needed is \(ss'\mathcal D_Ett'\), not merely a relation in \(S\).

   **Fix:** with matching group coordinates, put \(a=st'\), \(b=ts'\). Both are idempotents. Since \(p=s's\mathcal D_Eq=t't\),
   \[
   ab=sqs'=ss',\qquad ba=tpt'=tt'.
   \]
   In any band, \(ab\mathcal D_Eba\). This supplies the missing assertion; the subsequent Green and Clifford–Miller argument then works.

   Also define the unexplained maps \(\alpha_s\) and \(\theta_{e,f}\) at line 469, or remove that preliminary formula.

4. **Minor proof omissions in Theorem C.**  
   [proof.md, §6, lines 301 and 315–321](/Users/jinleic/jinleic-workspace/ai4s/regular-semigroup-embedding/proof.md:301).

   The one-class case does not explicitly meet the theorem’s requirement that \(B_0\) have **two** classes. Step 1(b) discusses nonidentity elements although \(d_1=s's\) when \(s's\in D\).

   **Fix:** in the one-class case take \(B_0=R^0\) and use constant functions \(G\to R\). In Step 1(b), separate \(s's\in D\): its local band is a singleton and its image is \(ss'\in D\). The existing argument handles \(s's\in T\).

5. **Incorrect source attribution.**  
   [proof.md, §0, lines 62–63](/Users/jinleic/jinleic-workspace/ai4s/regular-semigroup-embedding/proof.md:62).

   Survey §5.2 states the Pastijn embedding theorem; it does not state the claimed P/R equivalence there.

   **Fix:** cite Billhardt–Szendrei 2003, §3, as reported explicitly in Auinger–Szendrei 2005, p. 40. For the definition with an arbitrary band, cite a source defining Pastijn products for arbitrary semigroups rather than saying that the survey’s normal-band definition was copied unchanged.

6. **Overstated search coverage and incomplete evidence.**  
   [README.md, lines 175–182](/Users/jinleic/jinleic-workspace/ai4s/regular-semigroup-embedding/README.md:175) and [proof.md, line 494](/Users/jinleic/jinleic-workspace/ai4s/regular-semigroup-embedding/proof.md:494).

   C2/C3 logs reach total size \(n+m=10\). I1 logs reach only 8. All three search selected \(\mathbb Z_2\)-graded configurations, not all semigroups through those orders. No structured-embedding SAT log or certificate accompanies the claimed two SAT results.

   **Fix:** give the exact parameter grid and grading restriction, correct I1’s maximum, and qualify the unlogged SAT results. Saved enumeration tables alone do not establish that enumeration ran to exhaustion.

7. **Literature gap concerning the “new” positive case.**  
   [README.md, lines 172 and 199](/Users/jinleic/jinleic-workspace/ai4s/regular-semigroup-embedding/README.md:172).

   The older generalized-\(F\)-orthodox embedding theorem gives the locally regular target conclusion for this case; see the deduction below.

   **Fix:** distinguish the known positive embedding case from the particular explicit two-class \(B_0\) wreath construction, whose prior appearance I have not located.

8. **Unsupported categorical openness assertions.**  
   [README.md, lines 3 and 201](/Users/jinleic/jinleic-workspace/ai4s/regular-semigroup-embedding/README.md:3), [proof.md, lines 3 and 501](/Users/jinleic/jinleic-workspace/ai4s/regular-semigroup-embedding/proof.md:501).

   A negative search does not establish that the problem remains open. The README itself correctly admits this.

   **Fix:** consistently write “No resolution located as of 2026-10-14; current status uncertified.”

9. **Unsupported inference that every obstruction must be multistep.**  
   [proof.md, lines 494–497](/Users/jinleic/jinleic-workspace/ai4s/regular-semigroup-embedding/proof.md:494).

   Proving C2/C3 excludes those particular obstructions; it does not exclude every other local obstruction.

   **Fix:** retain the proven conclusion that a counterexample to \(Q_{\mathrm{orth}}\) needs at least three idempotent-band \(\mathcal D\)-classes, and limit the obstruction conclusion to C2/C3.

**Literature findings:**

- **M. B. Szendrei**, “E-unitary regular semigroups,” *Proceedings of the Royal Society of Edinburgh, Section A* **106** (1987), 89–102, DOI: **10.1017/S0308210500018229**. Its original abstract explicitly states the theorem used in B, including choosing the target band from the variety generated by \(E(S)\). [Publisher abstract](https://www.cambridge.org/core/journals/proceedings-of-the-royal-society-of-edinburgh-section-a-mathematics/article/abs/eunitary-regular-semigroups/7C075D71F9EE16B6C363C49117812CFE)

- **B. Billhardt and M. B. Szendrei**, “On quasi-\(F\)-orthodox semigroups,” *Proceedings of the Edinburgh Mathematical Society* **38** (1995), 361–385, DOI: **10.1017/S0013091500019192**. Theorem 4.1 gives embeddability for quasi-\(F\)-orthodox semigroups; Theorem 4.2 gives variety-preserving embeddability for generalized-\(F\)-orthodox semigroups. [Full paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D944A40474ACC6806F540E9660735EFA/S0013091500019192a.pdf/on-quasi-f-orthodox-semigroups.pdf)

  **My deduction for C:** choose core vectors \(y_g,z_g\) equivariant under left/right \(H_1\) multiplication using right/left coset transversals. Choose \(r_g\) in the top group for \(g\in H_1\setminus\{1\}\), and \((y_g,g,z_g)\) otherwise, with \(r_1=1\). These form an \(F\)-cross-section. The normal-form equations make its images in the least \(\mathcal R/\mathcal L\)-unipotent quotients left/right normal. Hence C’s semigroups are generalized-\(F\)-orthodox, and Theorem 4.2 gives a band in \(\operatorname{var}E\subseteq L(ReB)\). I did not locate C’s exact \(B_0^G\) construction there.

- **B. Billhardt and M. B. Szendrei**, “Weakly E-unitary locally inverse semigroups,” *Journal of Algebra* **267** (2003), 559–576, DOI: **10.1016/S0021-8693(03)00395-8**. This proves the locally inverse case and establishes the general P/R embeddability equivalence. The latter is explicitly reported in the next primary source. [Article](https://doi.org/10.1016/S0021-8693(03)00395-8)

- **K. Auinger and M. B. Szendrei**, “Rees matrix semigroups and the regular semidirect product,” *Journal of the Australian Mathematical Society* **79** (2005), 39–60, DOI: **10.1017/S1446788700009320**. Page 40 reports P/R equivalence for arbitrary regular first factors, using a subsemigroup in one direction and a direct power in the other. It also distinguishes broader regular semidirect and Pastijn–Rees constructions. [Full paper](https://archive.austms.org.au/Publ/JAustMS/V79P1/pdf/e46.pdf)

- **B. Billhardt**, “On embeddability into a semidirect product of a band by a group,” *Journal of Algebra* **206** (1998), 40–50. Szendrei’s survey confirms a finite nonembeddable E-unitary orthodox example with a left semiregular band. I did not obtain its full multiplication table, so its local regularity remains unchecked. [Primary survey, §5.1](https://arxiv.org/pdf/1909.05280)

- **B. Billhardt and M. B. Szendrei**, “A new class of embeddable E-unitary regular semigroups,” in C. Bonzini, A. Cherubini and C. Tibiletti, eds., *Semigroups: Algebraic Theory and Applications to Formal Languages and Codes*, World Scientific, Singapore, pp. 27–35. Bibliographies disagree between 1993 and 1994; Szendrei’s list gives 1994. I did not obtain the full text and cannot assign it a precise overlap with A or C. [Author bibliography](https://www.math.u-szeged.hu/tagok/bszendre/papers.html)

- **M. B. Szendrei**, “Structure theory of regular semigroups,” *Semigroup Forum* **100** (2020), 119–140, DOI: **10.1007/s00233-019-10055-8**, arXiv:1909.05280. It reports the locally inverse result and regular-band result, without resolving the stated locally r-orthodox problem. [Survey](https://arxiv.org/abs/1909.05280)

- **K. Auinger, M. Bitterlich and M. Otto**, “Finite approximation of free groups I: The \(F\)-inverse cover problem,” *Advances in Mathematics* **482** (2025), 110563, DOI: **10.1016/j.aim.2025.110563**. This resolves a different problem from Szendrei’s list. [Paper](https://arxiv.org/abs/2208.03273)

**No resolution of the full Problem 1 was found in the 2002–2026 search.** Nor did I locate an explicit prior statement of A’s full orthodox-to-group reduction. Important full texts remain unavailable, so neither conclusion certifies absence.

Queries included:

- `"weakly E-unitary" "locally orthodox" embedding`
- `"weakly E-unitary" "locally" "r-orthodox"`
- `"locally r-orthodox" embedding semigroups`
- `"locally orthodox" "semidirect" embedding`
- `"locally regular" "E-unitary"`
- `"quasi-regular" "E-unitary"`
- `"seminormal band" "semidirect"`
- `"Szendrei" "2002" "locally orthodox"`
- `"weakly E-unitary" "Pastijn"` with 2020–2026 terms
- `"弱" "局部" "半正规带" 半直积`
- Exact-title searches for the 1993/1994, 1998 and 2002 papers.

The [book excerpt](/Users/jinleic/jinleic-workspace/ai4s/regular-semigroup-embedding/sources/book-excerpt.txt:45) supports README Status (c)’s hypotheses and target band class. P/R are justified interpretations and, for band varieties, their embeddability questions coincide by the known subband/direct-power constructions. Matching Fact 1 does **not** uniquely select them: the ordinary semidirect product, equivalently its regular part for embeddings of regular \(S\), is another plausible reading. The Jones–Trotter and Pastijn–Rees alternatives weaken the target restriction. I have not established whether the full problem’s answers differ under these broader readings.

**Checker assessment:**

I reran the following, with bytecode writing disabled:

| Checker | Result | What it establishes |
|---|---|---|
| `check_band_facts.py` | Passed | E5/E5¹ facts, exhaustive minimum-order check through 4, and the implemented FB(3) facts. |
| `check_two_chain_theorem.py 200 1` | Passed | The 200 generated explicit embeddings. |
| `check_two_chain_theorem.py 150 1000 --hard` | Passed | The 150 generated hard instances. |
| `check_two_chain_generic.py` on the five listed files | Passed: 7 tables | Extracted normal forms and explicit embeddings for the saved generic tables. |
| `locally_regular_vs_regular.py 3` | Matched log | Quotient sizes 51 and 159 and the reported identity failure. |

The **357-instance construction claim is reproduced**.

Specific limitations:

- The random generator **builds the normal form into its inputs**. It checks constructed semigroups and embeddings, not the necessity of that normal form for arbitrary inputs. The generic checker supplies additional evidence, but shares the final construction checker.
- The band enumeration is genuinely exhaustive for labelled bands of orders 1–4, reproducing counts \(1,4,35,604\). FB(3)’s identification additionally relies on the implemented Green–Rees normal-form theorem. Its band check is printed but omitted from the final aggregate Boolean.
- The SAT encodings inspected are consistent with their stated finite searches: associativity, grading and odd-element inverse witnesses yield E-unitary orthodox semigroups. C2/C3 use the intended group-coordinate restrictions absent from the displayed note.
- **C2/C3:** logged totals are 6, 8, 9 and 10. **I1:** logged totals are 6, 7 and 8, with only the displayed patterns. These are not exhaustive searches over all orders, gradings or groups.
- `enum_extensions.py` can exhaust the specified fixed-band search, but also supports truncation. The saved tables and embedding log do not independently demonstrate exhaustion.
- `embed2chain_sat.py` searches a specified two-class target with coordinate bounds. A valid SAT model establishes an embedding for a validated input; injectivity follows from its injective idempotent map and \(\sigma\cap\mathcal H=\Delta\). **UNSAT establishes only failure within those bounds**, absent a completeness theorem.
- `pysat` was unavailable, so I inspected the SAT scripts rather than rerunning them. No installations or file changes were made.