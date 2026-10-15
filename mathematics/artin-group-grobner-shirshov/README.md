# Gröbner–Shirshov bases of finite-type Artin groups on the Artin–Garside alphabet

## Source

- Book: 《10000个科学难题·数学卷》 (10000 Selected Problems in Sciences: Mathematics), Science Press, 2009.
- Problem: 阿廷 (Artin) 群的 Gröbner-Shirshov 基 / *Gröbner–Shirshov Bases for the Artin Groups*.
- Authors: L. Bokut, 陈裕群 (Chen Yuqun), 华南师范大学.
- Pages: book pp. 30–34 = PDF pp. 46–50. Extract: [`sources/book-excerpt.txt`](sources/book-excerpt.txt)
  (`pdftotext -layout -f 46 -l 50`).

## Problem

The entry asks seven questions (book p. 33, verbatim in Status (a)). This target attacks
**question (3)**. Formal statement, every modelling choice fixed in advance:

- **Types.** Finite Coxeter systems $(W,S)$ ($A_n,B_n,D_n,E_{6,7,8},F_4,H_3,H_4,I_2(m)$ and products).
- **Alphabet (the book's Artin–Garside alphabet).** $X=\{\sigma_s:s\in S\}\cup\{\Delta,\Delta^{-1}\}$, $\Delta$ the
  positive lift of the longest element $w_0$. The book defines it for type $A$
  ($\Delta=\sigma_1\sigma_2\sigma_1\cdots\sigma_{n-1}\cdots\sigma_1$); for every finite type the same definition via
  $w_0$ (Garside, Brieskorn–Saito) is used. $A(W)$ is presented as a semigroup on $X$ by the braid
  relations, $\Delta=$ (a positive word for $\Delta$), $\Delta\Delta^{-1}=\Delta^{-1}\Delta=1$.
- **Monomial order (our choice; the book fixes none).** Deg-lex induced by
  $\Delta^{-1}<\Delta<s_1<\dots<s_n$ for a fixed linear order of $S$, stated with each result (Bokut's
  order for type $A$, arXiv:0806.1125). Other monomial orders are not treated.
- **What counts as an answer.** The set of all valid equalities is not an informative GS basis.
  The initial round sought reduced bases: finite lists, parametrized families, or an automaton
  for leading words with Garside-normalized tails. The continuation gives a stronger explicitness
  result at the book's stated (not necessarily reduced) level: **both sides** are specified by
  a finite pair-labelled transducer using finite Coxeter joins, with no Artin normal-form oracle
  in the rule definition (Theorem G). These new bases are generally **non-reduced**; they do not
  settle the stronger request for compact reduced templates in every type.
- **Other alphabets in the book.** Artin–Burau generators (question 2) are defined in the book only
  for type $A$; outside type $A$ no canonical analogue is given, so (2) is undefined there until a
  generator dictionary is chosen. Birman–Ko–Lee generators (question 4) are defined only for type
  $A$; a generalization needs a dual Garside structure (Bessis). Not attacked.
- **Not this problem.** Convergent rewriting on the alphabet of *all* simple elements is known for
  all finite types (State of the art); that is a different alphabet.

## Status as of 2026-10-14

**(a) Book statement, verbatim** (`sources/book-excerpt.txt`, lines 63–65, 131–141):

> Garside 用 Artin-Garside 生成元 ∆, ∆−1, σi (1 ⩽ i ⩽ n − 1, ∆ = σ1σ2σ1 · · · σn−2 · · · σ1σn−1 · · · σ1) 找到了 Bn 的正规形式 …
> (1) 给出一般 Coxeter 群的 Gröbner-Shirshov 基 (参见 Bokut-Shiao 在 [3] 中提出的猜想);
> (2) 给出有限型 Artin 群 Bn, Dn, G2, F4, E6, E7, E8 在 Artin-Burau 生成元下的 Gröbner-Shirshov 基;
> (3) 给出有限型 Artin 群在 Artin-Garside 生成元下的 Gröbner-Shirshov 基;
> (4) 给出有限型 Artin 群在 Birman-Ko-Lee 生成元下的 Gröbner-Shirshov 基;
> (5) 将上述 (1)-(3) 三个问题推广到任意 Artin 群;
> (6) 给出奇异辫子幺半群 SBn 分别在 Artin-Garside 生成元和 Birman-Ko-Lee 生成元下的 Gröbner-Shirshov 基;
> (7) 给出虚辫子群 VBn, welded 辫子群 WBn, 逆辫子幺半群 IBn 和辫子群 B(W) 在标准生成元下的 Gröbner-Shirshov 基.

English: "Garside found the normal form of $B_n$ with the Artin–Garside generators
$\Delta,\Delta^{-1},\sigma_i$ ($\Delta=\dots$). … (3) Give Gröbner–Shirshov bases of the Artin groups of finite type
in the Artin–Garside generators." The other questions ask for GS bases of: (1) general Coxeter
groups (cf. the Bokut–Shiao conjecture); (2) $A(B_n),A(D_n),A(G_2),A(F_4),A(E_{6,7,8})$ in Artin–Burau
generators; (4) finite-type Artin groups in Birman–Ko–Lee generators; (5) arbitrary Artin groups
for (1)–(3); (6) the singular braid monoid in Artin–Garside and BKL generators; (7) $VB_n$, $WB_n$,
$IB_n$ and complex braid groups $B(W)$ in standard generators.

**(b) Dated evidence on openness.**
- Latest primary source asserting the open status: L. A. Bokut, Y. Chen, *Gröbner–Shirshov bases
  and their calculation*, Bull. Math. Sci. 4(3) (2014) 325–395, doi:10.1007/s13373-014-0054-6,
  arXiv:1303.5366 (opened; `sources/arXiv-1303.5366.txt` lines 550–553): "Artin–Tits groups … GS
  bases are not known except for braid groups (the Artin–Tits groups of type $A_n$)."
- Dated search log 2014–2026 (`sources/literature-notes.md`, 2026-10-14): web queries, forward
  citations of Bokut JSC 43 (2008) (Semantic Scholar 22 records, OpenAlex 29) and of
  Bokut–Fong–Ke–Shiao (15/18 records), the 2020 World Scientific monograph preview, SCNU pages.
  **No resolution found on the Artin–Garside alphabet beyond type $A$; this is not proof of
  openness.** Closest later work: the positive Artin *monoid* of type $B_3$ in standard generators
  (Iqbal–Munir–Ayub–Nizami 2024; no $\Delta$, not the group; Claim C9), type $B$ on the
  all-simple-element alphabet (Chen–Zhong 2013). The parent's screen of the openai/math corpus found
  no family for this topic (local clone `adc7f1241` and remote listing, 2026-10-14).
- **Question (3) beyond type $A$, before this work: status: uncertified-open.** The initial round
  constructed reduced bases in ranks $\le3$ and type $D_4$. The continuation supplies a
  **uniform explicit rational GS basis for every finite type and every chosen atom order**
  (Theorem G), on the exact alphabet $\{\sigma_i,\Delta^{\pm1}\}$, generally non-reduced.
  This is a complete constructive answer to the fixed-order interpretation of (3), not a
  priority claim or a solution of the other six questions. No all-$n$ assertion rests on
  testing finitely many ranks: its validity, termination, completeness, and both composition
  types have an unbounded written proof.

**(c) Formal statements attacked.** For each finite $(W,S)$ and each order of $S$, explicitly
specify a GS basis of $A(W)$ on $X$ for deg-lex with $\Delta^{-1}<\Delta<S$. Additionally determine
the reduced basis and classify finite/bounded reduced-family descriptions. Theorem G settles
the first formulation. The earlier reduced-family results and their remaining limitations
continue to be stated separately.

**Status per (type, alphabet, order).**

| type | alphabet | order | status |
|---|---|---|---|
| $A_n$ | Artin–Garside | $\Delta^{-1}<\Delta<\sigma_1<\dots<\sigma_n$ | solved, Bokut 2008 (arXiv:0806.1125, Thm 1.1; opened) |
| $A_n$ | Artin–Burau | inverse tower order | solved, Bokut–Chainikov–Shum 2007 (arXiv:0806.1124; opened) |
| $A_n$ | BKL $+\delta^{\pm1}$ | Bokut's deg-lex | solved, Bokut 2009 (arXiv:0806.1123; opened) |
| $I_2(m)$, all $m\ge2$ ($A_2,B_2,H_2,G_2,A_1^2$); $A_1$ | Artin–Garside | both orders | **solved here: finite 8-rule (3-rule) basis (C3, PROVED)** |
| $B_3$ | Artin–Garside | $s_1<s_3<s_2$ ($s_1-s_2\overset4-s_3$) | **solved here: 12 families (C5)** |
| $D_4$ | Artin–Garside | $s_1<s_3<s_4<s_2$ (centre $s_2$ largest) | **solved here: 179 families (C11)** |
| $H_3$ | Artin–Garside | $s_3<s_1<s_2$; $s_1<s_3<s_2$ ($s_1\overset5-s_2-s_3$) | **solved here: 38 / 58 families (C11)** |
| $A_3$ | Artin–Garside | $s_1<s_3<s_2$ | **solved here: 14 families (C11)** (natural order: Bokut) |
| every finite type | Artin–Garside | every chosen atom order, $\Delta^{-1}<\Delta<S$ | **explicit rational GS basis with both sides prescribed, generally non-reduced (C14, Theorem G); reduced leading-language automaton C2** |
| $B_n$, all $n\ge2$ | Artin–Garside | every atom order | **all-$n$ formula via signed permutations (C14); proof independent of finite-rank experiments** |
| $B_4,F_4$ | Artin–Garside | $s_1<s_3<s_4<s_2$ | **materialized paired regular expressions with explicit outputs (C15); not reduced bases** |
| $A_4,B_5$ | Artin–Garside | orders $[s_1,s_3,s_4,s_2]$, $[s_1,s_3,s_5,s_2,s_4]$ | **additional materialized/verified rational bases (C15)** |
| $A_n,B_n$ ($n\ge4$), $D_n$ ($n\ge5$), $E_{6,7,8}$, $F_4$, $H_4$ | Artin–Garside | every order | no bounded-family basis (C6,C12); compact reduced templates not supplied here except known type-$A$ order |
| $A_3,B_3,H_3,D_4$ | Artin–Garside | other orders | reduced growth classified in proof.md §8; Theorem G still supplies a non-reduced rational basis |
| $B_3$ (positive monoid only) | standard atoms, no $\Delta$ | $z_1<z_2<z_3$ | Iqbal et al. 2024; 3 of 14 relations misprinted, corrected list verified (C9) |
| non-A types | Artin–Burau | — | alphabet undefined in the book outside type $A$ |
| non-A types | BKL / dual | — | open as far as found (not attacked) |
| all finite types | all simple elements | various | solved (Hermiller–Meier 1999; Chen–Zhong 2013 type $B$; Gaussent–Guiraud–Malbos 2015; Dehornoy–Guiraud 2016) — different alphabet |

Questions (1), (2), (4)–(7): `sources/literature-notes.md` §A (search-scoped: (1) partially solved —
the original Bokut–Shiao conjecture is refuted by Chen–Liu, arXiv:0910.0096, finite types done;
(2) open as far as found and under-specified; (4)–(5) partially solved; (6)–(7) open as far as
found). Not attacked here.

## State of the art

- **Type $A$, book alphabets:** Artin–Garside (Bokut, JSC 43 (2008) 397–405), Artin–Burau
  (Bokut–Chainikov–Shum, Comm. Algebra 35 (2007)), BKL with $\delta^{\pm1}$ (Bokut, J. Algebra 321 (2009)),
  Adyan–Thurston (Chen–Zhong, Algebra Colloq. 20 (2013)); positive braid monoid (Bokut–Fong–Ke–Shiao 2003).
- **Rank 2:** positive dihedral Artin monoids, infinite deg-lex completion (Autord, arXiv:0712.0525,
  Prop. 3.4); all two-generator Artin groups in HNN/free-by-cyclic generators with a tower order
  (Bokut–Vesnin, JSC 41 (2006)); standard signed generators shortlex automatic (Holt–Rees,
  arXiv:1003.6007).
- **Type $B_3$ positive monoid, standard generators:** Iqbal–Munir–Ayub–Nizami, Rev. Un. Mat.
  Argentina 67(2) (2024) 503–516.
- **All finite types, larger alphabets:** finite complete rewriting on all simple elements
  (Hermiller–Meier, JPAA 136 (1999)); coherent convergent presentation on $W\setminus\{1\}$
  (Gaussent–Guiraud–Malbos, arXiv:1203.5358, Prop. 3.2.1); finite quadratic convergent presentations
  on finite Garside families for every finitely generated Artin–Tits monoid (Dehornoy–Guiraud,
  arXiv:1504.02717).
- **Regular normal forms:** lex-minimal positive braid words are regular in type $A$
  (Flores–González-Meneses, arXiv:1808.02755); finite-state geodesic cross-sections on standard atoms
  for all finite-type Artin monoids (Fuchiwaki–Fujii–Saito–Tsuchioka, RIMS 1646, 2008), not
  lex-minimal. No source found giving a regular lex-minimal language on $\{\sigma_i,\Delta^{\pm1}\}$ for all
  finite types.
- **Coxeter groups (question 1):** finite types $A,B,D$ (Bokut–Shiao 2001), $E_6,E_7$ (D. Lee 2008),
  $H_{2,3,4}$ (Lee–Lee, arXiv:1809.08419), $G_2,F_4,E_{6,7,8}$ (Pang–Wang, arXiv:2002.07369 v2, 2026);
  Bokut–Shiao conjecture refuted (Chen–Liu, arXiv:0910.0096).

## Attack

1. **Reduction to Garside theory** (proof.md §§2–4). Lemma 1 turns the GS problem into finding the
   minimal non-normal words and gives a counting criterion. Lemma 2: deg-lex normal forms are
   $\Delta^{(k)}\mathrm{lexmin}(p)$. Theorem A: reduced basis = 2 cancellations + $2|S|$ twists
   $s\Delta^{\pm1}\to\Delta^{\pm1}\varphi(s)$ + positive minimal non-normal words.
2. **Right-complement automaton** (§5). Lemma 4 characterizes lexmin, $\Delta$-free words by right
   complements; Theorem B builds a finite automaton for the leading words from $W$, for every finite
   type ($N\ge2$) and order (`work/automaton.py`). Floating-point root tables are validated by exact
   integer checks (`work/validate_tables.py`).
3. **Rank 2 / finiteness** (§6): finite 8-rule basis with a full critical-pair proof; no finite
   basis in rank $\ge3$ (explicit infinite families).
4. **Closed forms.** Leading words were enumerated independently from the Garside normal form
   (`work/gs_oracle.py`) and grouped (`work/families.py`); varying the generator order showed that
   the bipartite order with the middle node largest gives bounded families in rank 3. $B_3$: 12
   families by hand, proved by braid-move identities and a growth-series certificate (Theorem E).
   Then families were read off the automaton automatically (`work/extract_families.py`) for $D_4$,
   $H_3$ (two orders), $A_3$, $B_3$, and certified by the same pipeline (`work/certify.py`, Theorem F).
5. **Growth classification** (§8, `work/classify.py`): exact SCC analysis for all orders of
   $A_3,B_3,H_3,A_4,B_4,D_4,F_4,H_4$, plus parabolic inheritance; with Theorems E–F this gives the
   classification of bounded bases (Corollary in §7).
6. **Independent checks.** Knuth–Bendix completion (`work/kb.py`, sees only the defining relations)
   reproduces the bases up to the truncation length ($B_3$ two orders, $A_3$, $G_2$, $H_2$, $D_4$, $B_3$
   monoid); automaton NF counts equal the growth series.
7. **Published $B_3$ monoid basis** (§10): checked Iqbal et al. 2024; three relations misprinted.
8. **Uniform explicit right sides (continuation).** Track a simple residual $e$. Reading $y$
   replaces it by $y\backslash e$ and outputs a fixed reduced Coxeter word for $e\backslash y$.
   The identity $e(e\backslash y)=y(y\backslash e)$ telescopes to the actual rule equality.
   Starting from $x\backslash q$, $q<x$ or $q=\Delta$, gives a smaller output and covers every
   minimal non-normal word. This yields Theorem G for all finite types, including all $B_n$.
9. **Explicit $B_4/F_4$ expressions.** State elimination gives pair-expression DAGs, with exact
   words at the leaves, rather than a placeholder normal-form call. The two six-state $B_4$
   components have displayed hub regular expressions and copy the same arbitrary subword to
   the right side. An independent checker validates edge identities, every elimination step,
   leading-language equality, the all-length growth identity, 400 random equalities per
   instance, and corrupt-output/corrupt-expression controls. Bounded composition replay checks
   10,946 $B_4$ and 7,328 $F_4$ ambiguities; the all-length proof is Theorem G, not these counts.

Limits retained: no order gives bounded families for $A_4,B_4,F_4,H_4$; the continuation now
handles their unbounded parts by paired regular expressions. It does **not** supply compact
reduced RHS templates in these types. $E_7,E_8$ expressions were not materialized; the uniform
proof specifies them without requiring an experiment. A first $D_4$ family extraction timed out;
fixed by a faster normal form and a bounded search. The first certificate version over-approximated
right sides with consecutive powers (shared NFA loop state); found via a false "reducible right side"
alarm for $D_4$, fixed with epsilon moves; the affected check could only err on the safe side, and
all certificates were re-run.

## Claims

| # | claim | status | evidence |
|---|---|---|---|
| C1 | Lemmas 1–3, Theorem A: deg-lex normal forms are $\Delta^{(k)}\mathrm{lexmin}(p)$; reduced basis = cancellations + twists + positive minimal non-normal words ($N\ge2$, all orders; smaller cases are separate) | PROVED | proof.md §§2–4 |
| C2 | Lemma 4, Theorem B: for every finite type with $N\ge2$ and every order, the leading words form a regular language with an explicit automaton built from $W$ | PROVED | proof.md §5; `work/automaton.py`; automaton = oracle word-for-word up to length 15 (`evidence/oracle/`) |
| C3 | Theorem C: rank 2, all $m\ge2$, both orders: 8-rule finite reduced basis (incl. $G_2$, $B_2$); rank 1: 3 rules; literal empty system: 2 erasing rules | PROVED (rank-zero rewriting additionally Lean-checked) | proof.md §6; `evidence/certify/I2_*.json` (m=3..12); `hmz-lean-20261014/Formal.lean` |
| C4 | Theorem D: for these orders a finite GS basis exists iff rank $\le2$ | PROVED | proof.md §6 |
| C5 | Theorem E: reduced basis of $A(B_3)$, order $s_1<s_3<s_2$: 12 families + twists + cancellations | COMPUTED+VERIFIED (validity also by hand: braid-move chains; completeness by growth-series certificate) | proof.md §7; `evidence/certify/B3.json`, `B3_derivations.txt`; `evidence/kb/kb_compare.jsonl` |
| C6 | Growth: bounded families only for rank $\le3$ and $D_4$ in specific orders; exponential for every order of $A_4,B_4,F_4,H_4$, hence (Lemma 3) of $A_n,B_n$ ($n\ge5$), $D_n$ ($n\ge5$), $E_{6,7,8}$ | COMPUTED+VERIFIED (exact automata; depends on Lemma 4 and validated tables) | proof.md §8; `evidence/classify/*.jsonl` |
| C7 | Normal forms on this alphabet = Garside normal form $\Delta^k\cdot$(lex-least positive word) | PROVED | Lemma 2 |
| C8 | Bounded-length agreement of oracle, automaton, KB and family lists | COMPUTED+VERIFIED (bounded lengths only) | `evidence/oracle/`, `evidence/kb/`, `evidence/certify/*.json` |
| C9 | Iqbal et al. 2024, Thm 2.3 ($B_3$ monoid): $R_3,R_6,R_9$ as printed are invalid; with $z_2^n\mapsto z_2^{n+1}$ on the left the list is a GS basis for all lengths | REFUTED (as printed) / COMPUTED+VERIFIED (corrected) | proof.md §10; `evidence/iqbal2024_check_L13_*.json`, `evidence/certify/iqbal2024_corrected_certificate.json` |
| C10 | No GS basis on the Artin–Garside alphabet beyond type $A$ found in the literature (2014–2026) | search log, not proof of openness | `sources/literature-notes.md` |
| C11 | Theorem F: explicit reduced bases for $D_4$ (179 families), $H_3$ (38; 58), $A_3$ (14), $B_3$ (20, re-derived) in the stated orders | COMPUTED+VERIFIED | proof.md §7; `evidence/certify/{D4,H3,H3b,A3,B3auto}.json` and `*_families.md` |
| C12 | Corollary: an irreducible finite type has a bounded-family reduced basis for some order iff rank $\le3$ or $D_4$; finite iff rank $\le2$ | COMPUTED+VERIFIED | proof.md §7 Corollary |
| C13 | The numerically generated Coxeter tables are exact (relations, order, lengths, descents; weak order exhaustively except $H_4$, sampled per labelling and exhaustive for the default labelling by review 2) | COMPUTED+VERIFIED (integer checks + negative control) | `evidence/validate_tables.json` |
| C14 | Theorem G: explicit generally non-reduced rational GS basis on the exact Artin–Garside alphabet for every finite Coxeter system with $N\ge2$ and atom order; all-$n$ signed-permutation formula for $B_n$; rank-zero/one handled by C3 | PROVED (written uniform argument; full all-type Lean instantiation still absent) | proof.md §11; `work/complement_rules.py`; `hmz-lean-20261014/progress.md` |
| C15 | Materialized rational bases for $B_4,F_4,A_4,B_5$: explicit pair-expression DAGs, local identities, all-length leading/growth checks, random-word checks and rejected corruptions | COMPUTED+VERIFIED | `evidence/certify/{B4,F4,A4,B5}_paired_{rules,certificate}.json`; `*_paired_expression.txt` |
| C16 | Finite composition replay: $B_4$ 10,938 intersection + 8 inclusion, $F_4$ 7,328 intersection, all joinable using full infinite-rule reducers | COMPUTED+VERIFIED (leading lengths $\le10$ only) | `evidence/certify/{B4,F4}_composition_checks.json` |
| C17 | Signed-permutation convention and length formula agree exhaustively with Cayley distance for $B_2,\ldots,B_6$ | COMPUTED+VERIFIED (not an all-$n$ proof) | `evidence/certify/signed_b_formula.json` |
| C18 | Exact-rule transducer telescoping, validity, degree-lex termination, minimal/full-word coverage, and conditional equality iff joinability / normal forms / confluence | LEAN-CHECKED under explicit local/Garside hypotheses; not a complete Artin GS proof | `hmz-lean-20261014/{Formal.lean,claims.json,acceptance.json}`; 82 claims with permitted axioms |
| C19 | Pruning nonnormal outputs or using only commutations does not reduce the existing $B_4/F_4$ bases | EXACT FINITE COUNTEREXAMPLES; no impossibility claim about other reductions | `hmz-lean-20261014/reduced-filter-controls.json`; proof.md §13 |

No novelty is claimed. C3, C4, C7 and the complement identities in C14 use standard Garside theory.
C5/C11 are single-type partial results; C14 is uniform at the book's non-reduced GS level.
Neither the original seven-part entry nor the stronger compact reduced-template problem is
claimed solved. The historical literature search remains a search, not a priority certificate.

## Independent review

Codex `gpt-6.1-sol`, effort max, read-only, 2026-10-14 02:33–02:48 PDT; prompt
`evidence/codex-review-prompt.md`, output `evidence/codex-review.md`, log `evidence/codex-review.log`.
**Verdict: correct-with-fixes.** It verified Lemmas 1–4, Theorems A, C (all overlap types; it
exhaustively checked overlaps for $m=2,3,7,12$), D, the rational-function degree bound, the $B_3$ and
$I_2(7)$ certificates, hand-checked F8, F9, F12 and all 30 derivation chains (95 braid moves), and the
corrected Iqbal certificate. Objections and resolutions:

1. *Theorem B fails for $A_1$* (the created obligation $a^{-1}\Delta=1$ is not checked): Theorem B now
   assumes $N\ge2$; $A_1$ is Theorem C's separate case; `automaton.py` refuses $N<2$.
2. *Dihedral row in the growth table wrong for monoid bases*: corrected (monoid basis infinite of
   degree 0 for $m\ge3$, group basis finite).
3. *Floating-point root identification*: added exact integer validation of all tables
   (`work/validate_tables.py`, all pass, with a negative control).
4. *SCC growth statement needs periodicity qualifications*: restated with limsup / arithmetic
   progressions (proof.md §8, `work/classify.py` docstring).
5. *"Free sub-words are unavoidable" overclaims*: removed; only the exclusion of bounded families
   is claimed.
6. *Theorem E's label; README missing at review time*: relabelled COMPUTED+VERIFIED; README written.

Second targeted review (same model and settings, 03:20–03:33 PDT; prompt
`evidence/codex-review2-prompt.md`, output `evidence/codex-review2.md`): **correct-with-fixes.** It
verified the general validity criterion, the Corollary (Lemma 3 with monoid bases; bounded unions
have $O((L+1)^r)$ counts), the epsilon-NFA change, live certificates for A3, H3, H3b, B3auto, D4,
all five family tables against their JSON specs, three random $D_4$ families on 31 parameter
vectors, all $207{,}360{,}000$ prefix-order pairs of $H_4$ (default labelling), and exponential monoid
growth for all orders of $A_4,B_4$. Fixes applied: table validation now covers every labelling used
(148 tables; $H_4$ weak order sampled per labelling); the "remaining orders" row now separates
polynomial and exponential orders; "closed form open" no longer covers Bokut's type-$A$ order;
docstrings of `work/specs.py` and `work/certify.py` updated to the general criterion.

Focused all-rank review: Codex `gpt-6.1-sol`, max, read-only (`evidence/codex-uniform-review.md`,
prompt `codex-uniform-review-prompt.txt`, runtime receipt `codex-uniform-review-run.json`).
**Verdict: correct-with-fixes; Theorem G's mathematical proof is sound for $N\ge2$.**
The reviewer confirmed that the construction genuinely specifies an explicit rational GS
basis on the book's alphabet, with no hidden normal-form oracle or added generators; it
separately rejected any implication of reducedness. It checked all 36 B4 endpoint regexes by
720 language-product states, all 147,456 B4 weak-order pairs and 1,536 simple/atom joins with
independent integer signed permutations, both copy-output SCCs, and both B4/F4 certificates.
Its three corrections are applied:
1. `I 0 --m 4` now derives the default atom order from the actual matrix rank, not the CLI's `n=0`.
2. The core transducer constructor immediately rejects $N<2$; rank one remains Theorem C.
3. Pair-expression leaves are described as $S^*\times X^*$, since initial outputs can contain $\Delta$.
Both executable fixes pass `work/check_complement_boundaries.py`, including an all-length
dihedral certificate (`evidence/certify/complement_boundary_regressions.json`).

Executable scope: the bundled finite-table constructor has a 200,000-element cap and uses
numerical roots to generate candidate tables. The new certificate checker verifies group
order/relations, all lengths, and every used join with exact integer Cayley-graph methods.
This implementation cap does not occur in the abstract all-rank theorem; large exceptional
expressions were not materialized.

## HMZ + Lean continuation (2026-10-14 PT)

The actual frozen RLAR run used the shared runner with `--timeout 3600`, baseline
`e757f04c146039059a28726cbb977326f48387d9`, worker `gpt-6.1-sol:max` and reviewer
`claude-opus-5-5:max`. **Not accepted:** reviewer `done:false`, journal `ended how:stopped`,
process rc143 after 3600.408 seconds. It independently replayed the first 57 claims.
The owner preserved the interrupted second-turn source, repaired its two recorded Lean errors,
and completed conditional full-word joining/normal-form/confluence and order-sensitive controls
after the run, bringing the claim ledger to 82; these additions were not reviewed by that HMZ run.

The substantive Lean theorem `ArtinG.Completeness.conditional_equal_iff_join` concerns the
**actual infinite rule family (11.1), twists and cancellations**, not an arbitrary relation
assuming confluence. Its coverage and termination are proved, but positive-monoid local laws,
generation/homogeneity, the Delta twist and G5 uniqueness remain explicit hypotheses.
They have not been instantiated for every actual finite-type Artin group; the polynomial
Composition–Diamond bridge also remains unformalized. **Theorem G is still a written proof,
not a fully kernel-certified all-type GS theorem.** The arbitrary atom order and exact
alphabet are retained. Rank zero's omitted boundary is corrected by two erasing rules.

The package includes successful Lean statements/axioms, two rejected corrupt-output controls
(commutative lost-output and noncommutative reversed-block models), exact local `math/`
reference applicability, the actual HMZ journals, preserved failed attempts, and finite
counterexamples to two reduced-basis shortcuts. Reduced $B_4/F_4$ templates and the other six
book questions remain separate. See [`hmz-lean-20261014/progress.md`](hmz-lean-20261014/progress.md).
Reproduce this continuation only with `python3 hmz-lean-20261014/reproduce.py`; it does not
rerun the previous long certificate portfolio.

## Next steps

1. Reduce the explicit $B_4/F_4$ rational bases and determine whether the right-normalization map
   itself admits a comparably compact description. This is a stronger task than supplying a GS
   basis; Theorem G already supplies one on the prescribed alphabet.
2. Compare the uniform rational construction against the Garside/reversing literature for
   novelty and publication positioning; make no priority claim from a search null result.
3. Other monomial orders (weighted or tower orders): no assertion about finite/bounded bases
   for those orders is made here. Questions (1),(2),(4)–(7) are not solved by this continuation.

## Reproduction

```sh
cd mathematics/artin-group-grobner-shirshov
sh work/reproduce.sh          # regenerates evidence/ (python3 stdlib only, ~8 min, 1 core)
python3 work/certify.py B3 --Lmax 14      # Theorem E certificate
python3 work/certify.py D4 --Lmax 10      # Theorem F certificate for D4
python3 work/certify.py I2_6 --Lmax 12    # Theorem C for G2
python3 work/classify.py F 4 --all-orders # growth classification for F4
python3 work/check_complement_rules.py evidence/certify/B4_paired_rules.json
python3 work/check_complement_rules.py evidence/certify/F4_paired_rules.json
```

Files: `proof.md` (statements and proofs), `work/` (code), `evidence/` (outputs, reviews),
`sources/` (book excerpt, papers, `literature-notes.md`).
