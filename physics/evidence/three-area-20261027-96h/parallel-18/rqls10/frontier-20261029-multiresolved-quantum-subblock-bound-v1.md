# A t-resolved quantum subblock requires N at least (t+2)k

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 00:21:03 PDT 2026**. This strictly generalizes the one-resolution quantum bound `frontier-20261029-resolved-quantum-subblock-n3k-v1.md` SHA **45d7fa3a31571ac210c3776557122f7d96f0caeb870aae77972d7a64fd0992f1**. It is a necessary embedding condition, not an unrestricted existence theorem.

## Statement

Let Q be a t-resolvable QLS of order N, with t pairwise orthogonal resolution Latin squares. Suppose a proper k×k subarray on k rows R and k columns C is a QLS(k) spanning a k-dimensional subspace H, and each resolution, restricted to R×C, is Latin on some k-element label set. Then

`N >= (t+2) k`.                                                       (1)

The result includes t=0, for which the local-resolution hypothesis is vacuous. All outside vectors are arbitrary; no classical, product or sector assumption is imposed.

## Proof

Each column of C contains a block ONB of H, so every outside-block cell in that column lies in H-perpendicular. For each resolution a and each of its local k labels, the corresponding global transversal also contains a block ONB of H, so all its outside-block cells lie in H-perpendicular.

Fix any row outside R. Its k cells in columns C and its k cells with a local label of resolution a are disjoint: each C-column already uses each such label in R. For two distinct resolutions a,b, their two k-label sets also cannot occur together in any outside-block cell. Indeed the k² block cells realize k² distinct ordered label pairs, since any two transversal classes from different resolutions meet once globally; all possible local label pairs are already exhausted inside the block. Therefore the outside row contains `(t+1)k` DISTINCT cells whose vectors lie in H-perpendicular. They form part of an ONB, so `(t+1)k<=N-k`, proving (1).

## Consequences

- For t=1,N=10, `k<=3`; a k=3 QLS is necessarily classical, but the 1RQLS10 itself need not be.
- For t>=2,N=10, `k<=2`, and k=2 cannot itself admit even one transversal because every QLS2 is classical and the cyclic Latin square of order2 has none. Thus no proper nontrivial block with both resolution restrictions can occur in a 2RQLS10, if one exists.
- The same argument applies to arbitrary exact quantum subblocks, including subblocks of higher-order constructions. It does not apply when the block's labels do not form k local Latin symbols, or when local block vectors fail to span a common k-space.

The restriction of different resolutions to the block is automatically orthogonal under the stated hypotheses; this is what makes the outside-row groups disjoint. The written dimension argument requires independent review.
