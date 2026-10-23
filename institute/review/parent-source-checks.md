# Parent source checks and selection decisions — 2026-10-15 PT

These are selection checks, not proofs or research results. A literature search miss does not certify
openness, novelty, or the strongest current bound. Catalog rows marked inference/unverified remain leads.

## Mathematics: flag-transitive projective planes

- Parent opened the book image, PDF p. 55 (book p. 39), in
  `mathematics/evidence/mathematics-hard-20261015/sources/math-p0039/`.
- The article explicitly identifies nonexistence of non-Desarguesian flag-transitive projective planes
  as its motivating conjecture. Its literal diameter-two claim for a dihedral Cayley graph generated
  only by reflections is inconsistent: that graph is bipartite, with degree smaller than either part.
- **Decision:** target the geometric nonexistence conjecture that the article itself states, using the
  precise difference-set formulation in Thas–Zagier. Preserve and disclose the printed inconsistency;
  do not present a correction of the easy literal false statement as solving a difficult open problem.
- Parent opened [Thas–Zagier, JEMS 10 (2008), 173–190](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.4171/JEMS/107/fulltext.pdf),
  including Theorems 1.1/2.4 and the computational appendix. The reported baseline is no such plane for
  order `n < 2 × 10^11`. The necessary congruence is `n ≡ 8 (mod 24)`; the base-two modular filter and
  its exceptional cases are stated in the appendix.
- Parent opened [Xia, arXiv:1707.05486](https://arxiv.org/abs/1707.05486), which explicitly describes
  the conjecture as longstanding and gives further necessary conditions. The selection worker's
  citation search found no later range extension; this is not proof that no extension exists.
- **Decision:** the published Feit divisibility condition, as used by Thas–Zagier, may be a declared
  imported mathematical premise. Do not claim a self-contained or Lean-kernel proof of it.
- **Scope and verification:** a longer finite range is only partial progress. Random samples, survivor
  rechecks, block counts, and hashes are not independent exhaustive verification of the entire range.
  Report the producing computation separately from its sampled cross-checks. The unsolved all-orders
  conjecture remains the headline.

## Physics: random k-SAT bounds from the statistical-physics chapter

- Parent opened the book image PDF p. 459 (book p. 426), Challenge 5, in
  `physics/evidence/physics-hard-20261015/sources/phys-p0422/`. It explicitly calls for rigorous bounds
  on k-SAT phase transitions using interval arithmetic or other certified numerical techniques.
- Parent opened the full reader text of [Achlioptas–Peres, arXiv:cs/0305009v2](https://arxiv.org/pdf/cs/0305009v2)
  and checked the table on paper p. 2: upper bounds 10.23 (k=4), 21.33 (k=5), 87.88 (k=7).
  The paper initially allows independently drawn literals, including repetitions. The model transfer
  to distinct-variable clauses must be proved, not hidden in a numerical comparison.
- Parent opened the abstract and proof setup of [Vorobyev, arXiv:2610.10599v1](https://arxiv.org/html/2610.10599v1),
  submitted 2026-10-06. It claims 4.268 for **k=3**, with an exact-rational calculation and a Lean
  formalization. The parent did not rebuild or validate that Lean development. Treat the preprint as
  a method lead, not a verified premise or a result for k≥4.
- **Decision:** attempt k=4 and k=5 bounds first. A negative numerical functional is not yet a threshold
  theorem: the general-k interpolation inequality, its hypotheses, truncation error, sign conventions,
  and model transfer are load-bearing proof obligations. Keep conditional numerical certificates
  separate from an unconditional random-k-SAT bound.
- **Scope:** improved bounds would address part of Challenge 5, not determine the exact thresholds,
  solve the other four challenges, or resolve general constraint satisfaction.

## Information science: balanced nine-variable nonlinearity

- Parent opened the book image PDF p. 424 (book p. 403). It explicitly asks about maximum balanced
  nonlinearity for odd `n ≥ 9` and constructing balanced functions above the bent-concatenation bound.
- Parent opened [Kavut–Yücel, arXiv:0808.0684](https://arxiv.org/pdf/0808.0684), including its
  unbalanced 242 constructions and the explanation that their spectra contain no zero coefficient.
  Those particular functions cannot be balanced merely by adding a linear function.
- Parent opened [Wang–Lou–Wang, arXiv:2610.17871](https://arxiv.org/pdf/2610.17871), posted
  2026-10-13. Section 6 explicitly leaves existence of a balanced nine-variable function with
  nonlinearity 242 open. Its claimed universal upper bound 242 is unrefereed and was not validated here.
- Parent opened [Lou–Xu–Wang, arXiv:2610.17897](https://arxiv.org/abs/2610.17897), also posted
  2026-10-13. It claims to exclude balanced eight-variable nonlinearity 118; this is a different,
  already-claimed question, not the selected target.
- **Decision:** select the nine-variable question. Checking an explicit positive truth table does not
  require trusting either new preprint. An independently reconstructed exact Walsh calculation must
  establish balance and the peak bound. A local or symmetry-class exclusion remains only partial;
  heuristic failure and a solver timeout establish no nonexistence.

## Protocol deviation recorded by the information-science screening worker

The worker reported one read-only `git ls-remote` against `openai/math`, despite the no-Git screening
instruction. It reported no repository mutation. This deviation is preserved rather than claiming
that no Git command occurred. No commit, push, or external scientific contact was authorized.

## Budget decision for completed batches 01–03

Exactly three visits, one per volume, each with a 21,600-second ceiling. Stage allocations are in the
run's `config.json`. After the owner explicitly authorized fresh allocations, recovery began at
12:02:24 PT. The later attack continuation consumes only the remaining allocation and retains the
18:02:24 PT wall-clock cutoff. A one-off identity-checked process watcher requests graceful stop two
minutes before that cutoff; its receipt is `approved-deadline-watchdog.json`.
The operator adds no paid API fallback, global model/config change, recurring scheduler, commit, push,
or external scientific contact. Scientific early stops remain allowed; unused quota is not fabricated
as research time. Final accounting must distinguish epochs 1+2 from the earlier failed batch and from
parent replay of finalized artifacts.

## Additional primary-source attribution check

- Parent opened [Lelarge–Oulamara, arXiv:1708.02457v2](https://arxiv.org/pdf/1708.02457),
  published in *Journal of Statistical Physics* in 2018
  ([DOI](https://doi.org/10.1007/s10955-018-1964-6)). Section 2, condition (4), explicitly permits
  odd interaction sizes when the factor is nonnegative. Its numerical application is the hard-core
  model on regular graphs, not a table establishing current k=4/5 SAT records.
- Parent inspected the introduction and attribution/formalization passages of
  [Vorobyev, arXiv:2610.10599v1](https://arxiv.org/html/2610.10599v1). The energetic integer-cost
  comparison, exponential reweighting and nonnegative-replica approach are direct method predecessors;
  do not label the present implementation independent discovery. That paper's stated result is k=3.
  Its claimed Lean formalization was not replayed here and does not formally verify our k=4/5 argument.
- Current best published numerical bounds for k=4/5 have not been established by these parent checks.
  The historical 10.23/21.33 comparison alone cannot support a state-of-the-art or novelty claim.

## Subsequent continuation authorization

After those visits closed, the owner explicitly authorized continued scientifically reasonable
research without the former total time/token limit. The old cutoff and unused allocations describe
only the completed batches. The new [continuation contract](continuation-20261015/README.md) preserves
the same headline problems, declares new claim-changing obligations, and retains explicit requeues
and conservative per-visit checkpoints. Publication, commits, pushes, deletions, paid-API fallbacks,
external scientific contact and infrastructure changes remain outside scope.
