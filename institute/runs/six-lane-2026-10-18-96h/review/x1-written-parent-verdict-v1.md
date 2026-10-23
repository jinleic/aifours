# X1 written exclusion: computation no longer load-bearing for K5.3

Recorded at 2026-10-19T01:31:33-0700.

**CORRECTNESS-ACCEPTED (written, computation-free).** No group admits five pairwise disjoint left cosets of finite-index subgroups with indices (3r_1,3r_2,6r_3,6r_4,6r_5), where r_1,r_2 are odd and all five r_i are pairwise coprime. Through the already accepted written K5.3→X1 deletion bridge, K5.3 is now excluded by a written proof whose only coset-counting import is the pairwise left-fibre bound proved inside the clarification. The previous StageA checker replay is no longer load-bearing for K5.3.

This is not Sun(7), not a novelty claim (Menon/Margolis–Schnabel material already claims this family), and not Lean or human review.

## Frozen evidence

- [Candidate](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/x1-written-parent-candidate-v1.md), SHA256 `09948b0cc35203683abd1ff0ccf50d10ff9b5fbb2797b5ec8a817568ce0825af`.
- [Mandatory pairwise-fibre clarification](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/x1-written-parent-candidate-v1-clarification-v1.md), SHA256 `49f956b2c6d0b8a17abaf2bd59e070b483792243f49d2fb54ac9def65297a0c9`.
- [Codex review](x1-written-codex-v1.prompt.stdout.txt), SHA256 `5c89473e0caaa318cc35b67346176eb4badf1444944507af8d0d716ed28027b7`: ACCEPT, 0 FATAL/0 MAJOR/0 MINOR; observed CLI model gpt-6.1-sol, read-only, max effort.
- [Claude review](x1-written-claude-v1.prompt.note.md), SHA256 `1ec111271da58dc630bae436e69aae2925dc5644f772037be70db902dbbdc5b4`: ACCEPT, 0 FATAL/0 MAJOR/2 editorial MINOR; observed CLI model claude-opus-5-5, prompt-only.
- ContinueSun7 independently rederived every step before the CLI reviews (not counted as a reviewer).

## Mandatory editorial overlays (parent-applied, no statement change)

1. **Import item 1 replaced** by the exact pairwise statement: if F⊆V∖{v} has pairwise-coprime local indices, then sum_(j∈F) t_j≤n_v−1, i.e. sum_(j∈F) alpha_vj/g_vj≤1−1/n_v. Every “feasible/no allowed set contains both” phrase in Steps 2 and 4 reads “no fibre holds pieces of two members of F”. No general hereditary LFC or Sun(3)–Sun(6) is used.
2. **Range of alpha derived**: lcm(n_i,n_j) divides the intersection index by Lagrange, so alpha is a positive integer; mu(U_iU_j)=alpha_ij/g_ij<1 because disjointness puts a_i^(-1)a_j outside U_iU_j. Hence 1≤alpha_ij≤g_ij−1.

## Parent cross-check of both reports

Both referees independently verified: gcds 3/3/6 from oddness of r_1,r_2 and coprimality (C cofactors may be even); the single orientation choice alpha_(d1d2)=1 and its symmetric use at d_2; actual-fibre counting with the exclusive fibre a_vU_v removed (strictness); both D-triangles' tau_min=x/gcd(x,r_i), tau_max=min(x,2), killing x=4 and requiring both 3|r_1,r_2 or both 5|r_1,r_2 for x=3,5; the two exhaustive Step-4 indicator families with total exactly n_c against n_c−1; and the finite-core lift. Claude's load-bearing remarks (Step 1 orientation needed; both other C vertices needed in Step 4) are consistent with the proof.

## Status changes and preserved records

- K5.3: exclusion now rests on written mathematics (bridge + this proof). The earlier scoped-partial verdict and its one-checker replay remain valid historical evidence; the permanent late-freezing deviation F-1 remains recorded and is not retroactively cured.
- Remaining Sun k7 frontier unchanged by this verdict: K7 with both 2- and 3-markers (pending K7-35 review for split 3/5), K6.2* partly, K6.3 residue (3-marker on d with 2-marker in C pending K63-D/E reviews).
