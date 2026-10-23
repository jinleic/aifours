<!-- Parent transcription 2026-10-17T22:42:09-07:00 of the read-only scout M7K1Priority's final report (agent://M7K1Priority; transcript history://M7K1Priority), verbatim below. The scout wrote no files and had no host clock; its time base is the server stamps it quotes. -->

NONE-FOUND-IN-SCOPE

The screen was bounded, and not finding a prior result does not make K1 new. I did not assess correctness. Correctness here rests on the parent's RESULT.json (all five routes PASS); the whole-claim CLI reviews are still pending. I ran no code and wrote no files.

## Summary
- **No prior result found.** No primary source I read proves K1 as known, or implies it in a routine way. That covers the main statement, the maximal-net clause and the Desarguesian rigidity clause.
- **The reformulation is not new.** K1 §1 (C1) and its "net form" are already in two sources, and K1 should cite both:
  - Zhang–Cao, Lemma 2.2: a QLS with t resolutions into transversals is the same thing as that QLS plus t classical squares forming a (t+1)-MOQLS.
  - Ball–Simoens, Lemma 21: the n = 6 case of the same idea, stated as an orthonormal representation of the complement of a Latin-square graph.
- **New finding: K1 settles two order-7 cases that two 2026 papers list as open.** Neither K1-THEOREM.r1.md nor the earlier run screens state this.
  - In Zhang–Cao's language, K1 says exactly: every 2-RQLS(7) is classical. (A 2-RQLS(n) is a QLS of order n with two orthogonal partitions of its cells into transversals.)
  - A pandiagonal QLS(7) (PQLS(7)) is a 2-RQLS(7) on the harmonic Desarguesian net. So every PQLS(7) has cardinality 7.
  - Hence no maximal-cardinality PQLS(7) (MCPQLS(7)) exists; Huang–Li left this open. And no maximal-cardinality 2-RQLS(7) exists; Zhang–Cao left this open.
  - The run's screens had listed these two objects only as possible routes to a positive answer (`screening/phys-2-moqls7-maximum-contract.json:11`, `phys-next-screen-v3.md:13,25-26`).
- **Rédei's theorem explains why the known constructions stop at order 7, but does not prove K1.** Ball–Simoens cite Rédei to show that their function-based family Ψ(f) cannot produce a K1 triple at q = 7. The same argument applies to Huang–Li's complete-mapping construction [INFERENCE]. K1 extends the obstruction from these families to every QLS.
- **M(7) is unchanged:** it is still 2 or 3. K2 and K3 remain open.

## Theorem-applicability table
| Source (version, date) | Exact scope | Relation to K1 | Effect |
|---|---|---|---|
| Ball–Simoens [2607.12933v2](https://arxiv.org/abs/2607.12933v2), 27 Jul 2026; v2 is still the latest per the arXiv API | M(n), Table 2 (M(7) is 2–4), Thm 5 (n−2 squares), Problem 16 | K1 is one branch of the question "is M(7) ≥ 3?" | Excludes only triples with two classical squares and one quantum square. With the run's 4-set result, M(7) is 2 or 3 |
| Same paper, Thm 6 / Cor 7 / §4.1 | Ψ(f) family. For q = 7: at most 2 squares, exactly one non-classical | Hypothesis is narrower than K1's (the Ψ(f) family only) | Consistent with K1, but does not imply it |
| Ball–Simoens [2603.02334v1](https://arxiv.org/abs/2603.02334v1) / PRL 137, 050202 | n = 6: Lemma 21 plus a search over the 12 main classes of Latin squares of order 6 | Same template (classify, then show no representation), applied to 3-nets of order 6 | Prior art for the reformulation and the method, not for the result |
| Han et al. [2507.20154v1](https://arxiv.org/abs/2507.20154v1), 27 Jul 2025, Thm 3.8 | Non-classical 3-MOQLS exist for v ≥ 16; v = 4..15 left open | K1 removes the two-classical branch at v = 7 | v = 7 stays open |
| Huang–Li [2606.27758v1](https://arxiv.org/abs/2606.27758v1), 26 Jun 2026; v1 is the latest | Definition of PQLS; §5 lists MCPQLS(7) as open | Applies exactly; see the isomorphism below | K1 ⇒ every PQLS(7) is classical, so MCPQLS(7) does not exist |
| Huang–Li, Thm 5.1 | MCDQLS(n) (main diagonal and anti-diagonal only); 7 is in the exception list P₂ | Not a 4-net | Does not apply; MCDQLS(7) stays open |
| Huang–Li, Lemma 2.9; Zhang–Cao, Thm 1.2(2) | A maximal-cardinality 1-RQLS(7) exists | 3-net level | Combined with K1, order 7 shows a sharp threshold: a 3-net admits a 49-ray assignment, while no 4-net admits even 8 rays [INFERENCE] |
| Zhang–Cao [2608.29201v2](https://arxiv.org/abs/2608.29201v2), 7 Sep 2026: Def 1.1, Lemma 2.2, Cor 2.3, §5 | 2-RQLS(v); maximal-cardinality 2-RQLS left open at 7 among other orders | K1 is literally "every 2-RQLS(7) is classical" | Settles v = 7 in the negative. Lemma 2.2 is prior art for K1 §1 |
| Lv–Zhang–Cao [2609.29070v1](https://arxiv.org/abs/2609.29070v1), 24 Sep 2026 | Orthogonal pairs where both squares have maximal cardinality | Different object | None |
| Zhang–Cao [2609.24653](https://arxiv.org/abs/2609.24653); Lv–Cao [2609.09695](https://arxiv.org/abs/2609.09695); Zhang–Lv–Cao [2607.19969v2](https://arxiv.org/abs/2607.19969v2); Guo [zenodo.22852779](https://doi.org/10.5281/zenodo.22852779) | Cardinalities of single squares, with no orthogonality condition | None of these contain "pandiagonal", "RQLS" or "MOQLS" (I grepped the first two) | None. Guo's spectrum {7, 9, …, 49} is consistent with K1 |
| Egan–Wanless 1406.3681v2 | Classical classification of 2-MOLS(7): 7 classes, 5 of them maximal | Input only | Not a quantum statement |
| Wocjan–Elphick [1806.02734v3](https://arxiv.org/abs/1806.02734v3) | Spectral bounds on the chromatic number also bound the orthogonal rank ξ | The net graph is srg(49, 24, 11, 12) with eigenvalues 24, 3, −4, so the Hoffman bound is 1 + 24/4 = 7 [INFERENCE] | Cannot reach ξ ≥ 8 |
| Ball–Simoens Thm 2, Thm 5, Lemma 10; Thm 9 (Shrikhande); Huang–Li Lemma 1.5 | Need ≥ 5 squares (Thm 2/5); weights ≤ 2 (Lemma 10); 4 MOLS(7) (Thm 9); n ≤ 5 (Lemma 1.5) | K1 has 3 squares, weights up to 4, 2 MOLS, n = 7 | None apply. The run's own 4-set theorem has a strictly stronger hypothesis |
| Kochen–Specker; realizability of orthogonality hypergraphs (Megill–Pavičić style) | 0/1 valuations of a fixed vector set; low dimensions | K1 is about whether a vector realization exists at all | No implication; no treatment of order-7 nets found |

**Why the harmonic net is the pandiagonal net** [INFERENCE; K1 should add this as a written corollary]. The pandiagonal net has slopes {∞, −1, 0, 1}. The shear (x, y) ↦ (x, y + x) maps slope m to m + 1, giving {∞, 0, 1, 2}, which is K1's class 5. K1 §1 states the condition is symmetric in the four parallel classes and invariant under net isomorphism. Separately, "cardinality 7" (the Huang–Li/Zhang–Cao convention) is the same as "classical" (the Ball–Simoens convention) for a single square: every row is an ONB that uses all 7 rays, so the 7 rays themselves form an ONB.

**Graph formulation.** Let G_N be the collinearity graph of the net: 49 vertices, with 28 maximum cliques of size 7 (the lines).
- An ONB-assignment is the same as an orthogonal representation in C⁷ with adjacent vertices orthogonal (Wocjan–Elphick convention). Equivalently, it is an orthonormal representation of the complement of G_N (Lovász / Ball–Simoens convention).
- **Maximal-net clause:** for the five maximal nets, the orthogonal rank satisfies ξ(G_N) ≥ 8. It follows that the rank-one quantum chromatic number satisfies χ_q^(1) ≥ 8, since ξ ≤ χ_q^(1) [INFERENCE].
  - K1 says nothing about the arbitrary-rank quantum chromatic number χ_q, about the projective rank ξ_f, or about the exact value of ξ.
- **Desarguesian clause:** this is a rigidity statement, not an existence statement. Here ξ = χ = 7, and every 7-dimensional representation comes from a 7-colouring.
  - A 7-colouring is the same as a new parallel class, which is why χ(G_N) = 7 exactly when the net extends [INFERENCE].
- **Existence versus uniqueness:**
  - maximal nets: no representation exists;
  - Desarguesian nets: representations exist, and all of them are classical.

## Citations with quotes
- **Ball–Simoens v2** (pinned copy `sources/2607.12933v2.raw.txt`):
  - L32: "we define M (n) as the largest value of t such that a non-classical set of t MOQLS(n) exist"
  - L121: "If q is a prime power and q − 1 has a proper divisor d ̸= 1, then there exist d − 1 MOQLS(q), exactly one of which is non-classical."
  - L626–627: "Rédei [11] proved that when q is an odd prime, any non-affine function determines at least (q + 3)/2 directions, so this is the best we can do."
- **Ball–Simoens [2603.02334v1](https://arxiv.org/abs/2603.02334v1):**
  - Lemma 21: "There exist 2 MOQLS(6) if and only if there is a Latin square graph on 6 × 6 vertices whose complement has an orthonormal representation in C⁶."
  - Their open problem: "Open problem 1. Are 2 MOQLS(7) classical?" Huang–Li Theorem 5.2 later answered it.
- **Ball–Simoens [DMD2026 poster](https://users.ugent.be/~rnsimoen/poster%20Mutually%20entangled%20quantum%20Latin%20squares.pdf)** (29 Jun 2026): "If a LS(n) can be extended to 2 MOQLS(n), its Latin square graph has an orthonormal representation in Cⁿ"
- **Han et al., Thm 3.8:** "For v ≥ 4, there exists a non-classical 3-MOQLS(v), except possibly for v ∈ {4, 5, ..., 15}."
- **Huang–Li:**
  - Definition: "A QLS(n) is called a pandiagonal quantum Latin square, denoted as PQLS(n), if its main diagonal, anti-diagonal, and all broken diagonals in both directions are each a transversal."
  - §5: "an MCPQLS(n) exists when gcd(n,6) = 1 and n ∉ {5,7,11}. Here, an MCPQLS(5) does not exist, and the existence of MCPQLS(7), MCPQLS(11), and MCPQLS(n) with gcd(n,6) ≠ 1 remains to be determined."
- **Zhang–Cao v2:**
  - Lemma 2.2: "A is a t-RQLS(v) if and only if there exist t classical QLS(v)s, B₀,...,B_{t−1}, such that A,B₀,...,B_{t−1} form a (t + 1)-MOQLS(v)."
  - §1: "pandiagonal quantum Latin square of odd order v which is a 2-RQLS(v)."
  - §5: "the known result at present are gcd(v, 6) = 1 and v ∉ {5, 7, 11} or v = n² for all n ≥ 6. It remains to determine the existence of maximal-cardinality 2-RQLS(v)s for the remaining orders."
  - §5: "every maximal-cardinality 2-RQLS(v) yields a non-classical 3-MOQLS(v) consisting of one maximal-cardinality quantum Latin square and two classical quantum Latin squares."
- **Guo** (DataCite record created 2026-09-20T05:01:04Z): "We show that the possible cardinalities for order seven are exactly {7, 9, 10, ..., 49}, with 8 excluded."
- **Wocjan–Elphick:**
  - "We prove that many spectral lower bounds for the chromatic number, χ, are also lower bounds for ξ."
  - "the quantum chromatic number and the orthogonal rank are incomparable."

**Freshness screen.** All queries returned no claim about a 3-MOQLS(7), a 2-RQLS(7) or a PQLS(7).

| Source | Query | Result |
|---|---|---|
| DataCite | "quantum latin" | 36 records; newest is 2610.17170 (created 2026-10-14T07:26:10Z) |
| DataCite | orthogonal quantum Latin / MOQLS | 10 records; same newest |
| DataCite | pandiagonal AND quantum | 1 record (Huang–Li) |
| DataCite | resolvable / RQLS / transversals | Only Zhang–Cao is relevant |
| DataCite | orthogonal rank + Latin / net / affine plane | Noise only |
| DataCite | Zenodo "Latin square" | Newest 2026-10-16; no quantum Latin square records |
| DataCite | Zenodo creator families, newest record each | Kirtchakov 2026-08-14; Griffin Long 2026-10-15 (SW matrices); Vos 2026-10-10; Raval 2026-09-11; Ferudun 2026-10-18T01:25:46Z; Gippini Requeijo 2026-10-17T22:26:15Z; Sadhu 2026-10-16; Guo, Ball/Simoens, Cao: nothing new on quantum Latin squares |
| arXiv API | "quantum Latin" | Newest is 2610.17170v1 |
| OpenAlex | Title/abstract and full-text searches | 20 and 15 hits; none relevant |
| OpenAlex | Citation counts for Ball–Simoens and Huang–Li | 0 for both |
| INSPIRE | Citers of Ball–Simoens | 1 (2608.29201) |
| Simoens homepage | Preprint list | Still only 2607.12933 on quantum Latin squares |

Clock: the newest Zenodo DOI was created at 2026-10-18T02:00:51Z, so the screen finished after that. Please timestamp the report on your side.

## Strongest counter-evidence
- The reformulation and the "classify the nets, then exclude representations" template are prior art (Ball–Simoens Lemma 21 / n = 6; Zhang–Cao Lemma 2.2). The method is not new; only this case is.
- Rédei's bound, quoted by Ball–Simoens, already explains why no construction of a K1-type triple was known at order 7. So a negative answer was expected.
- The field is crowded and moving fast: the Cao group posted 4 preprints in Aug–Sep 2026, and the definitions of 2-RQLS and PQLS(7) date from Jun–Sep 2026. A parallel resolution could appear in material I could not see; see the access limits below.

## Exact remaining open scope
- **M(7)** is 2 or 3. Still open: one classical plus two non-classical squares (K2), and three non-classical squares (K3).
- **Han et al. v = 7** remains open, as do 8, 10, 12, 14 and 15.
- **Huang–Li:** MCPQLS(11) and MCDQLS(7) remain open.
- **Zhang–Cao, maximal-cardinality 2-RQLS:**
  - Open for 8–12 and the other orders not covered.
  - The smallest order at which one exists lies in {8, …, 13} [INFERENCE].
  - The smallest order with any non-classical 2-RQLS is 8 or 9; at 9, Cor 7 with q = 9 and d = 4 gives one non-classical plus two classical squares [INFERENCE].
- **Graph side:** the exact orthogonal rank ξ, the quantum chromatic number χ_q and the projective rank ξ_f of the maximal-net graphs are open.
- **Other orthogonality notions:** weak orthogonality and entangled (AME-type) squares are not addressed.

## Significance
I count as "major" any of: a new method, a long-standing or prominent problem, a broad quantitative gain over the state of the art, or a physical consequence. K1 meets none of these.

**Rating: potentially substantive specialist result, narrow.** On its own, as a step toward M(7), it would be a modest extension. It moves up because it settles, in a strengthened form, the order-7 cases that Huang–Li and Zhang–Cao explicitly listed as open in 2026. In character it is comparable to the run's Problem-16 (n = 7) result. Limits: a single order, open questions that are months old and posed in unrefereed preprints, a computer-assisted proof, and no human review.

**Suggested wording:** "No QLS(7) orthogonal to two MOLS(7) is non-classical (equivalently, every 2-RQLS(7) is classical). Hence every PQLS(7) is classical; neither MCPQLS(7) nor a maximal-cardinality 2-RQLS(7) exists. M(7) ∈ {2,3}." Avoid "first", "determines M(7)" and "solves".

## Access limits
- **Blocked or unavailable:** the tool rejected Semantic Scholar; I did not check Google Scholar, zbMATH, MathSciNet or CNKI; Zenodo API and record pages returned HTTP 403, so I used DataCite metadata instead; GitHub code search needs authentication (repository search gave only spam).
- **Index limits:**
  - DataCite indexes metadata, not full text.
  - OpenAlex citation counts lag.
  - INSPIRE does not index Huang–Li.
  - The newest arXiv DOI visible in DataCite was submitted 2026-10-15T17:59:59Z. Anything submitted after that is not public until the next announcement (2026-10-17 is a Saturday) [INFERENCE].
- **Partial reads:**
  - Musto's 2019 thesis (Oxford archive, all rights reserved) was not read.
  - Han et al. tables and page 5 of Zhang–Cao extracted only partially.
  - I did not search Kochen–Specker / MMP hypergraph databases.
- **Re-screen before any release:** after the next arXiv announcement, and check for a v3 of Ball–Simoens and a v2 of Huang–Li.
