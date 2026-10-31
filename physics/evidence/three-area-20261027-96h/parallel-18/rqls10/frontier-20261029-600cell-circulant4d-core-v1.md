# A second 4D parity core with circulant 15-context incidence

**EXACT-ALGEBRAIC-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 02:03:45 PDT 2026. This is an explicit partial configuration, not a 6D lift or a 1RQLS10.

## Positive construction

There are 30 distinct rays in real 4-space forming 15 ONBs such that each ray appears in exactly two bases and every pair of bases shares at most one ray. The context-intersection graph is the 4-regular circulant

`G4 = Circ(15; ±1, ±4)`.

Color context i by `i mod 3`. The three colors each have five contexts and every G4 edge crosses colors, so G4 embeds in K5,5,5. Its required 6D edge complement is therefore

`G6 = Circ(15; ±2, ±5, ±7)`,

with 15 vertices and 45 edges. The indices, 15 bases and all actual ray coordinates are in `frontier-20261029-600cell-circulant4d-core-v1.json` SHA-256 `665517cf4f42ad2ddc1b9f83893449e4cb26d0c5802c0a46476cafd9e2c8073c`.

The explicitly regenerated 60-ray source is the standard 600-cell coordinate family. In unnormalized Q(sqrt(5)) coordinates, it consists of the projective classes of:

- `(4,0,0,0)` and its coordinate permutations;
- `(±2,±2,±2,±2)`; and
- all even coordinate permutations of `(0, ±2, ±(1+sqrt(5)), ±(sqrt(5)-1))`, with the three signs independent.

Opposite vectors represent the same ray; every listed representative has squared norm 16. The witness file stores each coordinate as the integer pair `(a,b)` for `a+b sqrt(5)`. The source contains 60 distinct rays and 75 orthogonal four-ray bases. A 15-context, 30-ray parity proof from the 600-cell and the 15-fold source organization are also described by [Aravind et al., Section 4 and Table 4](https://arxiv.org/html/2510.01063v4#S4.T4); the present labels and G6 caller are checked directly rather than inferred from matching their numbering.

## Independent exact checks and difference from the previous core

`frontier-20261029-600cell-circulant4d-core-replay-v1.py` SHA-256 `59fbfabb899b43e7350b13777cd2973c7658bffb15db7fc618a551f197469dbe` independently regenerates the original 60 rays, evaluates **all 435** original-vector inner products among the selected 30 rays in exact integer-pair Q(sqrt(5)) arithmetic, checks the 15 bases and their exact 0/2 multiplicities, and reconstructs both circulant graphs and the balanced partition. Its result `frontier-20261029-600cell-circulant4d-core-replay-v1.json` SHA-256 `d0943fb0e19074febaff009a2005368d7662a621a485ace1bb186bfc6139eb14` is **PASS** at 02:03:45 PDT.

This is genuinely a different incidence branch from the earlier positive Pauli core `frontier-20261029-pauli60-positive-tripartite-4d-core-v1.md` SHA-256 `734e0ff4397534dd8e486f9375984ddb6b3bcbdc51530e57505621726571af96`: the new G6 has **35 triangles**, while the independently reconstructed Pauli-core G6 has **29**, so the two 6D target graphs cannot be isomorphic. The exact new core does not inherit the earlier Pauli-specific finite-source, D6-equivariant, or fixed-spoke exclusions.

## Remaining gap

To form the balanced-quotient 75-ray parity core, one still needs **45 distinct 6D rays** assigned to G6's edges, forming a six-ray ONB at every vertex. Even a positive solution would leave the other 25 cells of a resolved order10 QLS to construct and check. No such 6D solution or general obstruction is claimed here. The original-vector replay and linkage to the 1RQLS10 caller need independent review; no formal proof or novelty claim is made.
