# Prior-art search log (depolarizing threshold), 2026-10-16 PDT (times = file mtimes)

A search miss is not a novelty result. Claims found elsewhere are priority/correctness evidence only.

| Where | Query / method | Result |
|---|---|---|
| arXiv API (18:39:55 PDT = 2026-10-17T01:39:55Z) | `abs:depolarizing AND abs:capacity`, `"coherent information" AND threshold`, `"symmetric subspace" AND "coherent information"`, `"permutation-invariant" AND "coherent information"`, `"thermal attenuator" AND "quantum capacity"` (sorted by date) | Newest relevant: 2609.39747v2 (Ahmed et al., 0.2029161 claimed, asymptotic, float), 2608.15870v2 (KG, 0.194868 certified). 2610.02176 (Khanian–Leung–Smith: per-use rates of permutation-invariant inputs; no threshold improvement). 2607.27449 (Mele et al.: thermal attenuator non-Gaussian positivity, different channel family/parameters). Files: `arxiv-search-*.xml`, `arxiv-related-abstracts-20261016.xml`. |
| EulerSolve (https://eulersolve.org/papers/, fetched 19:30:54 PDT, 285 papers) | full-text grep of index HTML for depolariz / quantum capacity / coherent information / quantum channel / antidegrad / hashing / thermal attenuator | No hit. Quantum-titled entries concern quantum groups, skein modules, quantum max-cut. File: `eulersolve-papers-index-20261016.html`. |
| Zenodo API | records search `"depolarizing channel" capacity`; record 21962925 (KG artifact) | HTTP 403 (traffic restriction) — **inaccessible, not a negative**. Web search (search engine) found no Zenodo record claiming a threshold beyond the arXiv ones. |
| openai/math remote `CONTENTS.md` (main, 638,727 bytes) | grep depolariz / quantum capacity / coherent information / qubit channel / hashing / antidegrad / quantum channel | Only family 276 (classical capacity of generalized amplitude damping) — different question. File: `openai-math-CONTENTS-20261016.md`. |
| Agarwal et al. public repo (GitHub tree sha 1c5b6fc0…) | fetched `NewPoints_for_Depolarizing/n_is_45/n_45_ens.pt` | byte payload SHA-256 9a94606d…4ca4cc1c6 = KG's state R hash; used as external control. |
