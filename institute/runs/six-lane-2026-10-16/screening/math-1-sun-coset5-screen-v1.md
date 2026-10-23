<!-- Parent capture 2026-10-18T02:24:47-07:00 of read-only scout SunCoset5SuccessorScreen (25m16s). Hand derivations R0-R3/N1-N3 are unreviewed; a search miss is not novelty. -->

**Verdict: OPEN-IN-SCOPE.** No proof or claim of the k = 5 case for arbitrary groups turned up in the bounded screen on 2026-10-18; that is a search miss, not proof the case is open. The latest dated status statements (Fornal–Sun and PPL 057, both 2026-07-27) say only k = 3, 4 are proved for groups. Using published results, the whole k = 5 case reduces to one family. The prior screen missed two key sources: Margolis–Schnabel 2019 and Menon, Aug 2026. Menon's work was done with AI help, so priority risk is high. I wrote no files and ran no code.

## 1. Exact statement (checked against primary sources)
- **Book:** p. 106 (PDF p. 122), article 关于不同模覆盖系的厄尔多斯问题 by 孙智伟 (Nanjing University), pages 104–106 (PDF 120–122). I read the repo's 150-dpi page images (`…/math-p0104/math-p0104-pdfp-121.png`, `-122.png`); their header records the canonical PDF SHA `3c69cf2c…`. Quotes: "孙智伟的下述猜想远未解决" and "如果群G的有限个左陪集a1G1,…,akGk两两不相交且诸指标…都是有穷的, 则必有1⩽i<j⩽k使得[G:Gi]与[G:Gj]的最大公因子至少为k".
- **Primary:** Sun, Internat. J. Math. 17 (2006), Conjecture 1.2 ([arXiv math/0501451v4](https://arxiv.org/abs/math/0501451), 2006-11-09): "Let a₁G₁,…,a_kG_k (k>1) be finitely many pairwise disjoint left cosets in a group G with [G:G_i]<∞ … Then ([G:G_i],[G:G_j]) ≥ k for some 1≤i<j≤k." Remark 1.5(a): "The conjecture remains open even for the additive cyclic group Z."
- **How to read it:**
  - G is any group; each index is finite; k ≥ 2 is finite.
  - The subgroups G_i may coincide; only the cosets must be pairwise disjoint.
  - The conclusion is that some pair has gcd ≥ k. It is sharp: take k cosets of one subgroup of index k.
  - Right cosets give the same problem, since Ha = a(a⁻¹Ha).
- **Prize:** [Cover.pdf](http://maths.nju.edu.cn/~zwsun/Cover.pdf) (2005 talk), Conjecture 4.2: "I'd like to offer a prize of $200 for a proof of Conjecture 4.2." PPL 057 (checked 2026-07-27) lists it as open since 2004. The prize is for the full conjecture, not for k = 5.

## 2. What is already known
| Result | Scope | Source |
|---|---|---|
| k = 2; all p-groups | all groups | Sun 2006, Remarks 2.2 and 1.5(b); [conj.pdf](http://maths.nju.edu.cn/~zwsun/conj.pdf) Remark 5 (last updated 2009) |
| k = 3, 4 | all groups | [Zhu 0807.2207v1](https://arxiv.org/abs/0807.2207); Int. J. Mod. Math. 3 (2008) 197–206; full text read |
| k = 3, 4 reproved: (2r₁,2r₂,2r₃) and (3r₁,…,3r₄) cannot be realised. **Prop 4.5:** (2r₁,4r₂,4r₃,4r₄) with r₁ odd cannot be realised. Theorem B: for n ≤ 4, any index tuple realisable by disjoint cosets in a group is also realisable by disjoint residue classes in Z | all groups | [Margolis–Schnabel 1803.03569](https://arxiv.org/abs/1803.03569); Beitr. Algebra Geom. 60 (2019) |
| That transfer to Z fails at n = 5: (6,6,6,10,15) is realisable in A₅ but not in Z. Found with "Anthropic's Claude Opus 5" and GLM-5.2 | groups | [Menon 2608.15873v1](https://arxiv.org/abs/2608.15873), 2026-08-16 |
| k ≤ 20 | integers only | [O'Bryant math/0604347v2](https://arxiv.org/abs/math/0604347); cases k ≤ 19 used a Mathematica run |
| max gcd ≥ k^(1−o(1)) | integers only | [Fornal–Sun 2607.24655v1](https://arxiv.org/abs/2607.24655), v1 only, 0 citing works in OpenAlex |

Fornal–Sun state the status directly: "Zhu proved the group-theoretic conjecture for k = 3,4 [13]."

Because Menon shows the integer-to-group transfer fails at length 5, O'Bryant's k = 5 result for Z does not settle groups.

## 3. Prior-work search and gaps
**Checked:**
- OpenAlex works citing Zhu (1), Margolis–Schnabel (7), Sun 2006 (14) and Fornal–Sun (0), plus a full-text search for "Sun" with "disjoint cosets" (14 hits).
- DataCite, which includes Zenodo: three phrase/title queries. The only Zenodo "Sun disjoint congruence" records are 2023 deposits of O'Bryant's 2006 paper.
- arXiv API: four queries, plus Menon's author listing.
- The local openai/math clone and its remote CONTENTS.md.
- Two web searches.

No claim for k = 5 or k = 6 in groups was found. Related 2024–26 papers (Akman–Sissokho "Steiner coset partitions", transversal coset partitions) are about Herzog–Schönheim, not this conjecture.

**Not checked:** Google Scholar, CNKI and Nanjing University theses, the Springer and journal versions of Margolis–Schnabel and Zhu, Sun 1992 (Chin. Ann. Math.), Huhn–Megyesi 1982, Zenodo full text, MathOverflow beyond one search, and EulerSolve or other AI-math listings.

## 4. Reductions (my own derivations, unreviewed)
**R0. Reduce to a finite group.** Let N = core_G(∩G_i). Each coset is the full preimage of its image in G/N, so indices, the indices of intersections, and disjointness are all unchanged. G/N acts faithfully on the disjoint union of the five coset spaces (Menon §2 states the same). So a counterexample is a finite permutation group G with points s_i, t_i such that no element of G maps (s_i, s_j) to (t_i, t_j) for any i ≠ j.

**R1. Sun at k = 5 is equivalent to a single family, Core(5).** Core(5): there is no group G with subgroups of indices (4r₁,…,4r₅), the r_i pairwise coprime, having pairwise disjoint cosets. All pairwise gcds are then exactly 4. Proof sketch of the equivalence:
- No pair of indices is coprime (k = 2 case), and every gcd is at most 4, so every gcd is 2, 3 or 4.
- Every pair must share exactly one of the primes 2 and 3. So either all five indices are divisible by 3, or all five are even.
- If all are divisible by 3, every gcd is 3, which contradicts the k = 4 result (Prop 4.3).
- If all are even, the odd parts are pairwise coprime. Two indices of exact 2-power 2 contradict Prop 4.2.
- One index of exact 2-power 2 together with three of the others contradicts Prop 4.5. What remains is Core(5).

This corrects both earlier screens. The "all divisible by 3" branch is already impossible, and all five indices, not three, must be divisible by 4.

**R2. Restriction.** If a subgroup K satisfies KG_i = G for every i, the configuration restricts to K with the same indices. So a minimal counterexample has no such proper K, and if G is solvable it is a π-group.

**R3. Coprime-fibre descent.** If Q is normal in G and the numbers [Q : Q∩G_i] are pairwise coprime, the images in G/Q are still pairwise disjoint, with indices dividing the original ones. So a minimal counterexample to Core(5) has O(G) = 1 (no non-trivial normal subgroup of odd order). Consequently k = 5 holds for nilpotent groups, for groups with a normal 2-complement, and for supersolvable groups. These are routine special cases and should not be a gate.

## 5. Calculus, missing lemma, and remaining gaps
For each pair define α_ij by [G : U_i∩U_j] = 4 r_i r_j α_ij, where U_i is the subgroup with index 4r_i. Then |U_iU_j| = α_ij·|G|/4 and α_ij ∈ {1,2,3}. The products U_iU_j and their intersections are unions of double cosets, so their sizes come in fixed steps, typically |G|/4.

**Published rules (Margolis–Schnabel):**
- Cor 3.9: no subgroup can have α = 1 with all four others.
- Lemma 3.7: three subgroups with all α = 1 generate a common subgroup of index 4.
- Triangle rules from Lemma 3.10 and Cor 3.11, applied to any three of the subgroups:
  - a triangle with α-values {1,1,2} forces the opposite r to be even;
  - {1,1,3} or {1,2,3} forces 3 to divide the r opposite the 3-edge;
  - {1,3,3} is impossible.
- Since the r_i are pairwise coprime, at most one r is even and at most one is divisible by 3.

**New candidate lemmas (my derivations, unreviewed):**
- **N1.** A subgroup U_i with gcd(r_i, 6) = 1 cannot have α = 3 with all four others. Each product with U_i covers 3/4 of G, any two of them overlap in exactly half, so the four missing quarters are disjoint and fill G — but every product contains the identity.
- **N2.** The pattern with all ten α = 2 is impossible: the pairwise overlaps must all coincide in one quarter of G, and then the four sets need 5/4 of G.
- **N3.** No four subgroups can have α = 1 pairwise. They share an index-4 subgroup H whose four cosets each hold one of the four disjoint cosets. The fifth coset then meets some coset of H in a coset whose index there is coprime to the one already in it, so the two meet.

**Missing lemma:** Core(5) for mixed α-patterns. **Gaps that matter most:**
- patterns with no α = 1 that mix the values 2 and 3;
- patterns at the special subgroup with even r or with 3 | r, where the triangle rules leave α-patterns open.

**Extraction caveats in the Margolis–Schnabel text:** Lemma 4.4 should read α ≠ 2. Cor 3.11 needs a swap of the two subgroups, which is valid when α is the prime 2 or 3. The parent should read pp. 8–10 before freezing, because R1 depends on Prop 4.5.

## 6. Correctness, novelty and significance, kept separate
- **Correctness:** R1–R3 and N1–N3 are unreviewed hand derivations.
- **Novelty:** none is established. Priority risk is high, because Menon used AI on exactly this machinery two months ago.
- **Significance:** settling k = 5 would be the first progress for groups since 2008. That is a modest specialist result, not the full book question. Small k does not mean easy: Menon shows group behaviour departs from the integers exactly at length 5.
- **Room for a proof:** there is a finite exact case structure (three α values on 10 pairs, plus the at-most-one special subgroups described in §5), and its extreme cases collapse. A complete proof is plausible but not assured [INFERENCE].

## 7. Ready to paste into the contract
- **target:** Sun Conjecture 1.2 at k = 5 for every group, via R1 as Core(5). Not the whole book question.
- **first_obligation:**
  1. Freeze R0–R3 with their citations.
  2. Write every rule as a lemma with explicit hypotheses: published ones plus N1–N3 with written proofs.
  3. Enumerate the α-labellings, together with the choice of special subgroups, up to relabelling. Output a certificate per pattern or a list of survivors. This is a tiny exact computation, not a search over groups.
  4. Attack the survivors by hand.
- **controls:**
  - The same engine must reproduce Prop 4.2, Prop 4.3 and Prop 4.5.
  - Configurations known to be realisable must survive every rule: Menon's A₅ and C₂×S₄ examples, all four-subgroup subconfigurations, and k cosets of one subgroup.
  - The rules must give cyclic groups all α = 1 and abelian groups α ≤ 2.
  - Mutating a label in a certificate must break it for the intended reason.
- **stop rules:**
  - Repeat the DataCite, arXiv and OpenAlex search before freezing and after any result; a prior claim means stop.
  - Small-group or permutation-group searches are never evidence for the gate.
  - If no survivors are eliminated by the agreed checkpoint, stop and report PARTIAL with the exact surviving pattern list.
  - A claimed counterexample needs two independent exact checks plus a parent recomputation.
  - Stop by 18:20 PT.
- **acceptance:** a full written Core(5) proof covering every pattern, or an exact verified counterexample; hostile review from both CLI families; a parent re-derivation; a post-result priority audit. A finite or partial reduction is not the gate.
- **resources:** one process, under 1 GiB, kilobyte outputs.

## Files
- `/Users/jinleic/repos/aifours/mathematics/evidence/mathematics-hard-20261015/sources/math-p0104/` — page images (PDF 120–122) and `excerpt.txt`, whose header records the SHA match.
- `/Users/jinleic/repos/aifours/books/README.md:10,17` — page offset (+16) and the book's SHA.
- `/Users/jinleic/jinleic-workspace/research-institute/explorer/inventory/math.json:664-677` — inventory entry math-p0104.
- `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/screening/math-1-phase-type-complex3-screen-v1.md:97-111` — earlier light screen, now superseded on the points above.
- `/Users/jinleic/repos/aifours/mathematics/evidence/mathematics-more-20261014/discrete-screen.md:75-87` — older nomination; its claim that three indices are divisible by 4 is now strengthened to all five.
- `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/screening/math-1-phase-type-complex3-contract.json` — contract format used for §7.
