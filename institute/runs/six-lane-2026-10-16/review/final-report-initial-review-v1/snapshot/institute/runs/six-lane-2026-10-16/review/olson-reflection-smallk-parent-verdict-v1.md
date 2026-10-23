# Olson reflection residual class at k≤p — parent correctness verdict

Parent disposition at 2026-10-18T05:24:44-07:00: **B0S and MXG CORRECTNESS-ACCEPTED at the scopes below, with the listed local errata.** Consequently RES_<(p) has no avoider with k≤p, for every prime p≥5. This is a partial theorem, not a new campaign gate or a claim of full REFL, INV* or ordered Olson. Priority and significance have not been separately established for this increment.

## Exact statements and source pins

A G-word has length4p−2 over D_2p, F,R≥1, rotation letters in one nonzero pair {rho_x,rho_−x}, normalized to {rho_1,rho_−1}, and its maximal constant reflection blocks separated by possibly empty rotation runs. A genuine empty run has distinct adjacent reflection-block values. H is the sum of floor(block_length/2) over these constant blocks, κ=p−1−H, and k counts those blocks, including the boundaries across empty rotation runs. An avoider has no increasing-index identity subword of length2p.

| Result | Accepted scope | Source |
|---|---|---|
| B0S | All rotations rho_1, all constant reflection blocks odd, k≤p, κ≥1; any number of genuine empty runs. Every such word is solvable. | `proof-B0S-r3.md`, `95851b9c3231ec665341145d779ec9eb11da71c5a5ed772f88cb2222595de1ee` |
| MXG | All constant reflection blocks odd, every rotation run pure rho_1, pure rho_−1 or empty; A≥B≥1, B<κ, k≤p. Every such word is solvable. | `proof-MXG-r2.md`, `f2235ed9964e92ca7554678bfae612b7eebb2760eb1b086e487b2e04688aae2f` |
| Combined residual statement | No avoider in RES_<(p) with k≤p. Split B=0 versus B≥1; the residual definition supplies all remaining hypotheses. | Definition in `proof-RED-r2.md` L132–133; no RED implication is needed for this direct corollary. |

Proof sources are in `mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/`. B0S's statement here uses the nonzero-common-rotation G-word scope; its broader literal zero-rotation wording is not needed for the residual corollary. The zero-rotation case separately follows by selecting H equal-letter pairs and2κ+2 identity rotations (R=2p−k+2κ≥p+2κ).

## Independent reviews

| Target | Codex gpt-6.1-sol | Claude claude-opus-5-5 |
|---|---|---|
| B0S-r2 | ACCEPT-WITH-FIXES;0FATAL/0MAJOR/1MINOR | ACCEPT-WITH-FIXES;0FATAL/0MAJOR/9MINOR |
| MXG-r2 | ACCEPT-WITH-FIXES;0FATAL/0MAJOR/1MINOR | ACCEPT-WITH-FIXES;0FATAL/0MAJOR/6MINOR |

Notes and exact hashes:
- [olson-b0s-r2-codex-v1.note.md](olson-b0s-r2-codex-v1.note.md): `de3b1fa17bf30755dc8864ecbdfdb9b1ef16ad548b93d9a8a405182226490030`.
- [olson-b0s-r2-claude-v1.note.md](olson-b0s-r2-claude-v1.note.md): `9a7d5390b4de00a12dd2c0122fc6487718a50a769fcc060c4517e1cd416ce032`.
- [olson-mxg-r2-codex-v1.note.md](olson-mxg-r2-codex-v1.note.md): `3cc3dda200c011c36250a9c8d99b5d3d50a21aa48b0db63fc7cfd6f9d8bae3d1`.
- [olson-mxg-r2-claude-v1.note.md](olson-mxg-r2-claude-v1.note.md): `b79bd72d1222e973253d13e5296d718582b9fd79632cd9129e05205b75690953`.

B0S reviews audit r2, with r3's Step0 symmetry repair inspected by the parent. MXG's reviewers independently checked the adapted proofs, not just the previously accepted Theorem M statement. Claude re-derived the H0 specialization used by B0S directly from GRX. No finite search is a premise.

## Parent verification

[Independent receipt](olson-residual-small-parent-v1/RESULT.json), SHA `0704877b2cb9f850e51f91651a0479cb278a0fdda6fe8c52ed5cc8781f8ace54`; script `f933f5a9e554d16df8129e11fbf87006795b5f76fcc7938150e02a93f69e8e3b`, frozen before execution. No worker code imported.

- Exact ordered-product bitset DP cross-checked with direct subset enumeration on360 small instances; six sharp-boundary controls distinguish length4p−2 avoiders outside the target hypotheses from their solvable extensions.
- 282,940 direct-count/half-window equalities for B0S at the primes5,7,11,13,17,19,23,29,31, including zero rotation mass and all feasible pattern interval counts. Direct counts enumerate permitted selected-rotation counts rather than evaluate the claimed interval formula twice.
- 7,600 generated words:3,800 B0S and3,800 MXG at p=5,7,11, each with genuine empty gaps. All have identity2p-subwords by raw DP and an independently reconstructed H0 witness. These are generated checks, not a claimed census or7,600 distinct words.
- Explicit B0S CaseII fixture p=7, κ=3, r=(0,0,1,1,1,1,9), x=(−1,−1,1,1,1,1,5), Z={0,1}, W={3}: all six kill inequalities hold and raw DP confirms solvability.
- Parent read the full B0S proof and MXG's new GIANT, tightened MIX-R and SPLIT/assembly obligations. In SPLIT, C≠[k] prevents both a cycle and a double adjacency edge; greedy orientations differ by at most1, hence integrality gives min c≥floor((|C|+|E|)/2). Repeated empty defects contribute BH(E)≤−2|E| to the two halves. These are the correct replacements for the old nonempty-run counting arguments, not an assumption that the old RGR theorem already covers empty runs.

These checks support implementation/arithmetic consistency only. The universal results rest on the written proof plus named classical/accepted imports, not on the finite aids. No Lean or independent numerical kernel is claimed.

## Required local errata

B0S: explicitly handle or exclude rho_0; state Step0 symmetry (already in r3); show P=Z∪W is proper; distinguish GRX from its GR0 specialization and H0's review status; fix the GRX hash suffix; qualify the unaudited comparison to S1′/A1′; clarify B=0-only scope; correct the fix-map count and parity wording. The accepted H0 is also covered by the [K0*/RED verdict](olson-reflection-K0star-RED-parent-verdict-v1.md), read with its [wording correction](parent-claim-provenance-addendum-v1.md).

MXG: qualify the I(empty) equivalence by A,B≤2p−1; separate the reused g/β symbols from empty-run count/boundary parity; list all Lemma S hypotheses; replace literal R*_G subset R* by implication between their residual inequalities; explicitly exclude double adjacency edges in SPLIT; say the corollary leaves k≥p+1 unresolved. The parent agrees these repairs do not alter the accepted mathematical argument. New worker versions must preserve the reviewed predecessors and provide a fix map; no second CLI pass is claimed merely from applying wording fixes.

## Remaining obstruction

The accepted [RED reduction](olson-reflection-K0star-RED-parent-verdict-v1.md) now leaves **RES_<(p), k≥p+1**, both B=0 and1≤B<κ. Closing only k≤p does not prove reflection rigidity. Rotation rigidity beyond separately reviewed low-odd cases also remains a distinct obligation. No unrestricted ordered Olson conclusion follows.
