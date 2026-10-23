# Physics-1 replacement screen after the capacity certificate

Read-only scout PhysNextScreen; preserved verbatim. Its hand derivations are untrusted leads.

I recommend the dual-unitary question T7, case d = 3, as the next phys-1 target. The AME(4,6) support ≤ 59 lead is a real, explicitly stated open question, but it is the weakest of the three for this slot. No new compute was run. Every claim marked **[INFERENCE]** is my own hand derivation; nothing checked it by machine and nobody has reviewed it.

## Lead audit: AME(4,6) with support ≤ 59

- **Latest text.** Only arXiv:2610.16673v1 (12 Oct 2026) exists; asking for v2 returned 404 on 2026-10-17. §VI, p. 7 says: "Whether the gap between 38 and 60 can be closed is open." The open question is the exact minimum support. "≤ 59" is only the upper-bound half of it.
- **Support convention.**
  - Support means the number of non-zero coefficients in a product basis (p. 2: "The support of |ψ⟩ thus has 12+2·24 = 60 basis states").
  - Every local-unitary image of an AME state is again an AME state, so the minimum is taken over all local bases. The 2610.17170 paper explicitly says its 96/60-term counts were not optimised over local bases.
  - A classical officer is a basis state with coefficient of modulus 1/6. It sits alone in its row and column in all three reshapings.
- **Baseline.**
  - Best known support is 60, reached by four groups independently:
    - Pandya's state, with an exact proof over Q(√2) in [real-ame46 v1.0](https://github.com/palashpandya/real-ame46);
    - Bruzda, [2610.16882](https://arxiv.org/abs/2610.16882), which Pandya says is locally equivalent to his state;
    - Rather's [repository](https://github.com/suhailahmadrather/Real-AME-4-6-state): "the most sparse candidates we obtain have only 60";
    - Hontarenko–Życzkowski's sign variant in [2610.17170](https://arxiv.org/abs/2610.17170).
  - Before October 2026 the sparsest state had 112 non-zero coefficients.
  - Lower bound 38, from Pandya: classical officers form a (4,t,3)₆ code with t ≤ 34 (Parker 1975), and support ≥ 72 − t.
- **What is proved.** None of the sources I read reaches ≤ 59 or rules it out.
- **New necessary condition [INFERENCE].**
  - Two rows of a unitary that share exactly one column cannot be orthogonal. So if every non-classical row has two entries, the non-classical part splits into 2×2 blocks, which needs 36 − t to be even.
  - A single three-entry row with all other rows two-entry is impossible, by the same closure argument.
  - Consequences: t ≤ 12 gives support ≥ 60, and t = 13 gives support ≥ 61. Support ≤ 59 therefore needs at least 14 classical officers.
  - Support 58 needs t = 14 with every reshaping a pure 2×2-block support, as in Pandya's Lemma 1.
- **Independent check path.**
  - A witness is a list of basis states with exact coefficients. Three checkers verify that U, U^R and U^Γ are exactly unitary and count the non-zeros.
  - A nonexistence claim needs the written reduction plus an exhaustive pattern search with proof logs. That search must rediscover Pandya's t = 12 support as a positive control.
- **Verdict.** The lead is eligible but not recommended now. The question is five days old, at least three of the four groups that reached 60 publicly are still producing work (Pandya posed the gap, Rather has a paper "upcoming"), and every independent sparsification stopped at exactly 60. Closing the gap almost certainly needs a multi-day nonexistence classification.

## Ranked targets

| Rank | Exact claim | Strongest matched baseline | Dated primary quote | Certificate / verification path | Next bounded experiment and decision value | Priority and access risks |
|---|---|---|---|---|---|---|
| **1 (alt)** | T7 at d = 3. Let O be the 2-unitary orbit {(v₁⊗v₂)P₉(v₃⊗v₄)}. Is there an ε > 0 such that every dual-unitary (U^R unitary) or T-dual (U^Γ unitary) U within ε of P₉ lies in O? Global corollary, using the published uniqueness of order-9 2-unitaries: entangling power e_p stays below 1 on non-2-unitary dual unitaries | Only a numerical gap. Best known non-2-unitary dual gate has e_p = 15/16. At d = 4, continuous families do reach 2-unitaries (review ref. [62]) | "(T7). Are there dual/T-dual gates in U(9) arbitrarily close to the 2-unitary permutation matrix P9 related to the state AME(4,3)?" ([2508.04777v3](https://arxiv.org/pdf/2508.04777v3), 25 Jun 2026, p. 21). Also p. 9: "the gap, the rigorous existence of which is yet to be established" | Exact rank of the linearised marginal map at ψ₉ (expected kernel 33) against the local-unitary tangent (33). Two independent exact implementations plus a hand proof (constant-rank argument, then compactness). Controls: the 3-cut kernel must also be 33; at P₁₆ and P₂₅ the dual kernel must exceed the local-unitary tangent; SWAP is dual but not T-dual | About 2 h. Matching dimensions give a complete "no" for d = 3, dual and T-dual, ready for review. Any excess dimension points to a second-order test or an explicit nearby family (a "yes" counterexample). Continuation: T7's "other dimensions" part for q = 4, 5, 7, and the soft claim that 15/16 is "likely the highest" | Short argument, so some folklore or scoop risk from the Lakshminarayan and Życzkowski groups. Rather's PhD thesis [62] and the journal body were not read. Significance is modest. Book link is related only (p0491, quantum chaos) |
| **2 (alt)** | Ball–Simoens Problem 16, smallest open case: is every set of 4 mutually orthogonal quantum Latin squares of order 7 classical? Equivalently M(7) ≤ 3, where M(7) is currently known to lie between 2 and 4 | M(7) ≥ 2 from Corollary 7 and Huang–Li. 5 such squares are always classical (Theorem 5). The case n = 5 is proved (PRL Theorem 12) | "Problem 16. Is a set of n − 3 MOQLS(n), n ≠ 4, necessarily classical?" ([2607.12933v2](https://arxiv.org/pdf/2607.12933v2), 27 Jul 2026, p. 7; Table 2, p. 2) | A counterexample would be four squares with exact entries in Q(ζ₇) or Q(ζ₂₁), checked by three checkers for orthonormality, pairwise product orthogonality and more than 7 distinct rays. A proof would be a pattern search with proof logs, then their Lemma 10 plus the Shrikhande extension. Controls: Theorem 5 must come out classical, the Corollary 7 pair must pass as non-classical, and the full set of 6 classical squares must pass as classical | About 2 h: exhaustive search for weight-3 entries. By their rules #2 and #3 the four supports are disjoint inside 6 coordinates, so weight is at most 3 **[INFERENCE]**. No weight-3 entry means an adapted Theorem 5 argument probably finishes the proof. A realisable weight-3 pattern could give a counterexample to Problem 16 | Ball–Simoens, Huang–Li and Haitao Cao's group are all active. The problem is mostly combinatorics, so the physics fit is weak (p0578, related only) |
| **3 (lead)** | Some AME(4,6) state with ≤ 59 non-zero coefficients in some product basis. Necessary condition: at least 14 classical officers **[INFERENCE]** | 60 from four groups; lower bound 38 | Pandya §VI, p. 7 (quoted above), [2610.16673v1](https://arxiv.org/pdf/2610.16673v1) | As in the audit | SAT search for pure 2×2-block supports with t = 14: 14 isolated points, 44 points in 2×2 rectangles in all three reshapings (E + 2P is an orthogonal array of index 2). Then exact phase solvability by Smith normal form; moduli s = 1 always solve Lemma 1. Control: t = 12 must recover Pandya's support. A hit gives a support-58 record, which narrows the gap but does not close it. UNSAT excludes only the block route | Extreme crowding, since the question is five days old. Weak evidence that 60 is optimal. The negative direction is multi-day |

### Key derivation behind rank 1 [INFERENCE]

ψ₉ is the uniform superposition over the tetracode C = {(a, b, a+b, a+2b)} over F₃. For one cut, the linearised condition "this two-party marginal stays I/9" pairs each off-code basis state y with τ(y) and forces δψ_y = −conj(δψ_{τ(y)}). On codewords it forces Re δψ = 0. Here τ_AB and τ_AC are linear involutions that fix C pointwise.

Their product acts trivially on F₃⁴/C and has order 3 with no fixed points off C. So the group they generate is S₃ acting freely on the 72 off-code points, giving 12 orbits. The kernel has dimension 9 + 2·12 = 33, which equals the local-unitary orbit dimension 36 − 3.

The mechanism is that the tetracode is perfect (9·(1+8) = 81). Every off-code point is a single-coordinate error, and those are exactly the directions local unitaries generate. Among [4,2,3]_q codes, only q = 3 is perfect, which matches the d = 3 versus d = 4 contrast. The T-dual case follows by swapping parties C and D, up to a local relabelling.

## Screens and dropped leads

- **openai/math:** the local `CONTENTS.md` (722 manuscripts, 372 families) has no AME, 2-unitary, dual-unitary, officers or quantum Latin square items; the nearest is family 266 (MUBs in d = 6). The remote fetch was truncated at family 289.
- **EulerSolve:** the papers listing has no matching items.
- **arXiv API on 2026-10-17:** the newest AME(4,6) papers are the three Oct 12 companions. The newest dual-unitary and quantum Latin square papers do not address T7 or Problem 16.
- **OpenAlex:** the review (DOI 10.1088/1361-6633/ae672a) has one indexed citer, Bistroń–Czartowski–Życzkowski (Quantum 2026). Its text does not touch P₉ isolation.
- **Dropped:**
  - Ball–Simoens PRL Open Problem 1 (are 2 MOQLS(7) classical?) is already resolved: non-classical pairs exist for n ≥ 7 (2607.12933 Theorem 4).
  - The LU-LC minimal counterexample question is settled by Claudet [2603.25219](https://arxiv.org/abs/2603.25219).
  - Smallest order of a maximal-cardinality orthogonal QLS pair (Lv–Zhang–Cao 2609.29070): by Rédei's theorem, Fourier-type pairs cannot work at prime orders **[INFERENCE]**, so there is no bounded route.
  - AME(8,4) and heterogeneous AME cases are not boundable in 2 h.
  - The tensor rank of the cube of the W state is already determined (Zuiddam 2015).
- **Not read / access holes:** Rather's PhD thesis [62], the PRL and Rep. Prog. Phys. journal bodies, and Rather's upcoming paper.
- `screening/physics-finite-target-screen.md` is absent; nothing was inferred from it.

## Files

- `institute/runs/six-lane-2026-10-16/screening/{physics-exact-model-screen.md, fresh-physics-screen.md, finite-info-target-screen.md, parent-primary-leads.json}`
- `institute/runs/six-lane-2026-10-16/outcomes.md`, `checkpoints.md`, `transitions.json:139-203` (AME kept as the phys-2 backup)
- `physics/PHYSICS_RESELECTION.md`, `physics/evidence/physics-hard-20261015/catalog.md`
- `/Users/jinleic/jinleic-workspace/math/CONTENTS.md`

**Target justified:** yes, T7 at d = 3. If the parent freezes it, the contract should also include the continuation (other dimensions, and the 15/16 question) so the slot does not idle once the first cycle settles d = 3.
