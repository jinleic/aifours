# Checkpoint 001

Host clock 2026-10-19T13:59:24-0700

Scope frozen: scope-v1.md 792332e9b6285e42f8114c4718b9aba1757aff353c73e3872a384072e38af9df.
Rederived imports: imports-v1.md dd6f7e8e5ff1f280f2a72daf56ca7f4693c8d86d4e024d9964e3fadba581fddd.
New reductions: reductions-v1.md bac8addacbd4d7ee3f21f7b3fb220ecf5501b1b6def9dc17fdac616bbeb06fa7.

Actual result: complete FIVE-category occupancy classification (not array classification); new AT2 theorem: at most4 distinct t2 rows can be all-triple in P1 (five would force6 disjoint pairs in a graph with at most5 edges). Four all-triple rows force a path/star with its three edges agreeing once each across P1. b65 forced to Q1, with two C-pair orbits and explicit C-column nonempty projections; b63 reduced to G1/T2 or G2/C0,Q1, and in G2 third pair cannot be two privates. b66/b68 have at most2 private pair endpoints (not the old bound3).

Current derivation (unfrozen sketch): testing b65's actual seven-empty incidences. A t3 row's eps3 quad leaves four empty partners for its two P0 triples; those four need a matching in the graph of empty pairs not already agreeing in P1. This forces a high-quad row's other P1 triple to have eps0 in one orientation. One explicit nonempty projection then fails the P0 rainbow/capacity condition: private p0 has already met all four rows of Q3, leaving no mate in its P0-column4 triple. This is a restricted-branch exclusion only so far.

No case closure yet; all four whole cases remain unproved. Next: derive the matching/zero-triple lemma rigorously and finish b65's two-orbit projection branches; then retain exact remaining obligations for b63/b66/b68. No e2 expansion, no runtime work, no runner/test edits. Checkpoints target1200s/max1800s.
