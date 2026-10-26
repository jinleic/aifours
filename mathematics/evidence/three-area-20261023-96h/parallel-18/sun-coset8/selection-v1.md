# Math-6: unrestricted Sun(8) — selection v1

Observed selection clock: `2026-10-23T14:03:01-0700` (`/bin/date`). Agent: MathSun8. Governing contract: `institute/runs/three-area-2026-10-23-96h/contract-v2-eighteen-slots.json`, read in full, with both mandatory parent errata. Deadline remains 2026-10-27T12:35:38-07:00. New files only in this exact slot root; no scientific program has run.

## Literal target

For **every group** G, **every eight finite-index subgroups** U_1,...,U_8 (possibly equal), and **every choice of pairwise disjoint LEFT cosets** g_i U_i, prove that there exist distinct i,j with gcd([G:U_i],[G:U_j]) >= 8; alternatively produce an exact group/subgroup/coset counterexample. There is no covering, finiteness-of-original-group, normality, solvability, index, valuation or private-cofactor restriction. Eight cosets of an index-eight subgroup show the numerical threshold would be sharp.

## Book and primary-source relationship

The mathematics source is Science Press 2009, ISBN 978-7-03-024267-9; page mapping is book+16. I extracted and read PDF pp.120–124 (book pp.104–108) into `book-pages-104-108-v1.txt`. Sun's article **Erdős' Problem on Covering Systems with Distinct Moduli**, book pp.104–106, ends on p.106 with the unrestricted disjoint-left-coset conjecture (extraction lines 86–88), not a coset-partition hypothesis. The article's author is Zhi-Wei Sun (lines114–115). The present target is its exact k=8 instance, not the article's distinct-modulus covering-system question.

The primary modern formulation is Sun, *Finite covers of groups by cosets or subgroups*, International Journal of Mathematics17(2006),1047–1064, Conjecture1.2, arXiv:math/0501451v4 (9November2006): <https://arxiv.org/pdf/math/0501451>. Read the conjecture and Remark1.5 and the k=2 discussion (Remark2.2). The PDF extraction drops some inequality glyphs; Zhu's independent primary statement agrees: Wan-Jie Zhu, *On Sun's conjecture concerning disjoint cosets*, IJMM3(2008),197–206, Theorem1.1, <https://arxiv.org/html/0807.2207v1>, confirms k=3,4 for arbitrary groups. Its introduction states the full conjecture and left-coset definition. Neither source proves k=8.

## Matched current baseline and source screen

The **strongest matched internal baseline** is arbitrary-group Sun(7), at the literal theorem interface of `institute/runs/six-lane-2026-10-18-96h/review/sun7-complete-written-composition-parent-verdict-v1.md`, SHA256 as recorded in final acceptance: `94abd506aec9879e294a5eb84129794af0c7ac78917b091d2f2c113d665c34f2`. I read that verdict and final-acceptance JSON, final reportv17 §3, mandatory v17 delivery erratum, and ledger parent errata15 then16. This is **internal written-composition acceptance**, not formal/kernel/human or priority acceptance. I will import ONLY its full arbitrary-group seven-coset statement; its proof components and solver logs are not implicitly generalized. Classical elementary subgroup facts and, if needed, Zhu Sun3/4 are explicit separate imports. Sun7 does NOT imply Sun8 without a new argument.

Fresh public screen also read Menon, *Two Questions on G-harmonic Tuples*, arXiv:2608.15873v1 (16August2026), abstract/introduction/definitions and its two theorem descriptions, <https://arxiv.org/html/2608.15873v1>. It disproves Ginosar's stronger transfer-to-Z question via (6,6,6,10,15) in A5; this is NOT a counterexample to Sun8 and does not license replacing groups by congruence classes. Its later theorem concerns a particular five-tuple, not eight arbitrary cosets. Full comparison remains bounded.

Local openai/math screen: `CONTENTS.md`, `overview.tex`, `lean/formalization.yaml` searched for disjoint-coset/Sun-conjecture patterns; broader `coset` hits concern unrelated algebraic-torsion and Kervaire cosets. Remote <https://raw.githubusercontent.com/openai/math/main/CONTENTS.md> was fetched and searched for the same terms and broader `coset`/`G-harmonic` terms: no matched resolution was located in that index. This is an index screen, not an audit of every manuscript. Public searches for newer disjoint-coset work and eight-coset results found no matched resolution in the sources checked. The2026 Prize Problem Ledger links Sun's current survey, but is secondary. Sun's official Cover.pdf/82f.pdf endpoints refused connections; the2026 Graz slides endpoint timed out. Thus **UNCERTIFIED-OPEN as a current global literature status**, with an actual primary open statement and no matched later solution located. No novelty claim follows.

## Missing ingredient and consequential delta

Assuming a counterexample, every pairwise gcd is at most7, while Sun7 forces a gcd-seven pair in every seven-element subfamily. The new prime7 is the structural difference from Sun7's 2/3/5 composite-six obstruction. First determine exactly what the incidence of7 can be, using only this literal deletion interface plus the allowed gcd set; then attack the surviving prime-seven configuration in actual coset geometry. An arithmetic index pattern, feasible row or LP solution is never a realizable coset counterexample.

A complete consequence would be unrestricted Sun8, conditional only on the explicitly trusted internal Sun7 interface plus classical imports. A nontrivial necessary reduction with its exact residual is PARTIAL, not a solution or discovery. A standalone proof of the new prime-seven residual would supply the full bridge.

## First bounded written attack and verification

1. Re-prove the common finite-core quotient, preserving indices and left-coset disjointness, with no assumption on original G.
2. Let A_p={i:p divides n_i}. Use every-seven-subset Sun7 to force the size of A_7, then exploit that two members of A_7 cannot share2,3,5 or any other prime under pairwise gcd<=7. Freeze a new exhaustive eight-coset residual, not copied seven-coset marker enumeration.
3. Derive subgroup-product / actual coset-action constraints on that residual; look for a written prime-seven obstruction and compare existing primary theorems before claiming progress.
4. Pin any complete written candidate and request parent/separate-agent reconstruction. No old runtime/checker, scientific program, compilation, enumeration or CLI is authorized or planned here. A later executable check would need an exact named parent GO.

Redirect condition: a genuinely matched primary proof/counterexample ends this target and is reported for parent collision-checked replacement; a necessary-index-pattern survivor is only an exact barrier, not a reason to silently narrow G. If the new obstruction cannot be closed, deliver a written reduction and clearly specified missing group-theoretic assertion with all verification and novelty boundaries intact.
