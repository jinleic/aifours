# Direct prior source: Song–Chen Proposition 3

Parent inspected [Zhiwei Song and Lin Chen, *A counterexample to the strong spin alignment conjecture*, arXiv:2603.25410v1](https://arxiv.org/html/2603.25410v1), Section III, Proposition 3 and Eq. (15), on 2026-10-30. The HTML read lists the arXiv header 26 March 2026 but displays a different regenerated title-page date; the [bounded source auditor's full report](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f467-three-qubit-exact-majorization-bounded-public-source-audit/review-v1.md) separately reports version history and the primary PDF. No journal publication or exhaustive priority determination is asserted.

Exact stated prior result: for \(a,b,c\ge0\), \(a+b+c=1\), and arbitrary **one shared three-qubit state** \(\rho_{ABC}\),
\[
a\rho_{AB}\otimes I_C+b\rho_{AC}\otimes I_B+cI_A\otimes\rho_{BC}
\prec a|00\rangle\!\langle00|_{AB}\otimes I_C+b|00\rangle\!\langle00|_{AC}\otimes I_B+cI_A\otimes|00\rangle\!\langle00|_{BC}.
\]
Equal weights and scaling by 3 give precisely the unweighted \(H_2\prec\operatorname{diag}(3,1,1,1,0,0,0,0)\). This exact two-body statement is prior and cannot be claimed new. The source's unweighted proof uses pure-state spin flip, \(X_3=D+P\), local marginal eigenvalue polygon inequalities, and Weyl/Ky Fan bounds; it does not display the new candidate's paired-projection compression proof. Method novelty is **not** established.

The same source's Section II strong-spin-alignment counterexample uses independently chosen two-body states not compatible as marginals of one shared state; it is **not** a counterexample to Proposition 3 or a physical depolarizing output. A source theorem plus one-body bound and the three-use channel expansion creates an explicit prior-corollary comparison obligation; it does not by itself establish novelty or settle the unreviewed negative-parameter transport. Older Amosov manuscripts print stronger tensor majorization claims; identified proof-step obstructions do not disprove their statements.
