# Information-science selection review: disposition

Date: 2026-10-14. Review: `selection-review.result.json`; original CLI events and prompt are preserved alongside it. The no-tools delegate reported `claude-opus-5-5`, effort max, successful exit. This is a portfolio/scope review, not verification of external papers or a proof referee.

## Accepted corrections

- **Openness:** a 2011 book plus unsuccessful searches does not certify that a problem is still open. Report dated, evidence-limited unresolved status, not exhaustive absence of a solution.
- **Difficulty:** no guarantee of an easy full solution. Difficulty and practical ranking are explicitly [INFERENCE]. A small per-instance experiment does not bound the difficulty of a uniform theorem.
- **Disturbance decoupling:** the parent independently read Chen et al. (2000), p.1722 and Appendix A (A.7). Exact rational-input algebraic decision of both variants is prior art. A structural residual must not be recast as a polynomial-time conjecture; the book does not impose that requirement. This target is not counted as a cleanly confirmed open/easy problem.
- **SPR:** degree five/six public proof claims are not a general-order solution and were not locally kernel-replayed. The parent read arXiv:2609.26541v2, Theorem 2.1 and Lemma 2.2; independent closed coefficient intervals and an actual degree-six numerator are explicit. The worker separately audits public Lean sources. The whole degree-greater-than-four question remains the target; a new degree or fixed family is partial.
- **Stochastic preview:** preserve the literal expected-norm formulation and filtration assumptions. A standard mean-square reformulation is not silently interchangeable with the book's expression. A successful mean-square simulation cannot prove necessity or equivalence of the two gains.
- **Visual cryptography:** distinguish general access structures from thresholds; fix security/contrast conventions. An LP/ILP encoding or a finite participant table is not a full uniform solution.
- **P-type ILC:** separate full-interval robustness from exact tail tracking, pure constant-gain P from adaptive/D-type/filter designs, output divergence from an isolated divergent initial input, and finite adversarial witnesses from one infinite bounded sequence. The worker's final report preserves these distinctions.
- **Closure:** every target must retain the original statement, scope changes, result type, source access limits, proof-review limits, and exact remaining gap. No full solution is inferred from launching agents or passing numerical checks.
- **Provenance:** extracted table of contents is PDF pages **11–21**, not the initial index's 13–19. Source hash and selected page ranges are in `intake.json`. Book pages beyond the front matter were inspected to read the actual questions; the selected statements are not claimed to lie within the first few physical PDF pages.

## Declined or qualified advice

- The suggested requirement to assign only one of four absolute status labels is too coarse for a problem with solved subclasses and source-limited residuals. Use explicit mixed status and caveats instead; do not treat search completeness as proof.
- Calling every fixed-instance computation or finite table a mere restatement is too broad. A checked computation can establish a previously unknown finite optimum or falsify a uniform conjecture. Correctness, novelty, and scope must be assessed separately; no novelty is claimed without prior-art comparison.
- Growth of `u_i(0)` alone does **not** prove later-time output divergence or failure of every output-error robustness specification. The ILC worker supplies a separate output-divergence proof; its partial scope remains explicit.
- Referee attack suggestions are advice only. No generic monotonicity, interlacing, or stochastic norm implication is imported without a proof and its hypotheses.

## Parent-exercised checks

- **Disturbance decoupling:** reran the exact verifier with an isolated output destination. Exit 0: 6,561 scalar plants, of which 2,583 admit DDP and 997 admit internally stable DDP. The worker's evidence was preserved.
- **P-type ILC:** reran both verification/simulation commands with an isolated output destination. Exit 0: 200 trials per scenario, 16 scenario summaries, exact finite witnesses and nonlinear diagnostics. These are finite checks, not kernel verification of the infinite theorems.
- **Visual cryptography:**
  - Replayed the n<=5 certificate verifier into `visual-replay.json`. Exit 0: 248 exact LP certificates, 744 integer witnesses, all four tamper controls rejected, `certified: true`.
  - Replayed the collection-bound relaxation. Four instances are UNSAT, and five relaxation witnesses remain explicitly not VCS witnesses.
- **Robust SPR:**
  - 31/31 exact self-tests passed.
  - The sextic example passed its construction and certificate checks.
  - A separate code path confirmed 5/5 sampled degree-6 certificates.
  - Lean builds were not replayed.
- **Stochastic preview:**
  - Reran the kernel identities: maximum relative K2 error `3.33e-6`, maximum M0 discrepancy `2.00e-10`. The saddle Monte Carlo estimates move toward `x0ᵀP(0)x0`.
  - Reran the literal-criterion probe: its largest observed literal ratio was `0.84867`, below the controller's exact discrete mean-square gain `1.02660`. This is empirical evidence only; the literal criterion is not solved.
- **Literature:**
  - Re-read the primary abstracts for the two excluded entries that were resolved after publication: [sorting by transpositions](https://arxiv.org/abs/1011.1157) and [convex polyhedra intersection](https://arxiv.org/abs/1312.1001).
  - Re-read the [2023 ILC initial-shift survey](https://pmc.ncbi.nlm.nih.gov/articles/PMC10686873/) §§2.5 and 5, and the full [2009 D-type rectification paper](https://www.ee.cityu.edu.hk/~twschow/pubs/papers/50.pdf). The latter is not imported as a P-type theorem.
  - Read Chen et al. (2000), p.1722, the arXiv:2609.26541v2 theorem statement, and Blundo–De Santis–Stinson (1999), Theorem 4.7.

Full parent command receipts and outputs: `parent-smoke/`. No target is certified as a full solution of its book problem. The replays exercised packaged finite or numerical evidence only; they are not independent proof replays.