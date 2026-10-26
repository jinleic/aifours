# Three-edge switch criterion — bounded next obligation after the defect orbit barrier

Clock observed before creation: **2026-10-23T15:23:32-0700**. Status **WRITTEN CANDIDATE / PARTIAL / NOVELTY_UNCLEAR**. This is a standard permutation-trade mechanism reconstructed exactly, not a claimed new general construction theorem. No scientific executable was run.

Read with `unrestricted-defect-orbit-candidate-v1.md`, SHA-256 `18dc11903db8b217cfb4b8517cbda600a5e4cbd5d8892bc36ddc1c40859779ae`. That packet shows why every add-zero root of the pinned published Tuscan-1(11), and its only other Tuscan-1-preserving row-rotation state, fails: two disjoint high-fault endpoint pairs survive. Merely selecting more roots of those same cycles cannot help. A new construction must actually change which directed edges belong to which Hamilton cycle.

## 1. Exact two-row switch, with no group assumption

Let P,Q be two directed Hamilton successor permutations on the same N symbols. Let

`R=Q^(−1)∘P`

act on their tail vertices. Choose ONE cycle S of R, of length k≥2. Exchange the outgoing successors of P and Q only at tails in S:

`P'(u)=Q(u), Q'(u)=P(u)` for u∈S,

and leave both unchanged elsewhere.

Because R preserves S, the two rows use the same successor-image set on S. Hence P' and Q' are permutations. For a Hamilton-cycle decomposition of the complete directed graph, the switch preserves every global directed-edge multiplicity exactly: it changes only the row/color of those edges. However it need not preserve Hamiltonicity.

Define α_P on S by sending a cut-tail u to the next member of S encountered along the original P Hamilton cycle; define α_Q similarly. Each α is a k-cycle. The unchanged segments between these tails cover every original vertex.

**Lemma.** P' is Hamilton if and only if `α_P∘R^(−1)|S` is a single k-cycle. Q' is Hamilton if and only if `α_Q∘R|S` is a single k-cycle.

*Proof.* On S, `Q(u)=P(R^(−1)(u))`. Starting from tail u under P', its new edge enters the old P segment just after `R^(−1)(u)` and reaches the next cut-tail `α_P(R^(−1)(u))`. Thus the return permutation of new segments is exactly the first displayed composition. Each new successor cycle contains a cut-tail and corresponds to a cycle of that return permutation, since the old unchanged segments cover all vertices. The Q argument uses `P(u)=Q(R(u))`. ∎

A k-cycle swap changes a row-permutation's sign by `(-1)^(k−1)`. Two Hamilton successor permutations have the same sign, so even k cannot yield Hamilton P' or Q'. This parity filter is necessary, not sufficient.

For **k=3**, R|S has only two cyclic orientations. The lemma specializes to

`α_P=R^(−1)|S` AND `α_Q=R|S`.

Saying merely “the cut triples have opposite cyclic order” is insufficient without the orientation relative to R: the other opposite-order choice splits both rows into three cycles.

## 2. Written calibration of the exact orientation

Positive pair: `P=(0 1 2 3 4)` and `Q=(0 2 1 3 4)`. Then `R|{0,1,2}=(0 2 1)`, α_P is its inverse and α_Q equals it. Exchanging the three tails simply interchanges the two successor rows (outside the three tails they agree); both remain Hamilton. This is a predicate calibration, not a new complete directed-graph decomposition claim.

Negative pair on six symbols:

`P=(0 3 1 4 2 5)`, `Q=(0 5 2 4 1 3)`.

Both are Hamilton, and `Q^(−1)P=(0 1 2)(3 4 5)`. For S={0,1,2}, α_P=(0 1 2)=R|S and α_Q=(0 2 1)=R^(−1)|S, the wrong opposite-order choice. The switched P' has cycles `(0 5)(1 3)(2 4)` and Q' has `(0 3)(1 4)(2 5)`. Thus a test which accepts any opposite order instead of the exact criterion is wrong. These explicit permutations calibrate the checker mathematically before any execution.

## 3. Exact finite bound for a possible next assay

The actual source is the11 Hamilton cycles on12 symbols obtained by appending symbol11 to every row of the primary Example2 table:

`sources/etzion-example2-tuscan1-11.table`, SHA-256 `a50fc2994053f669973f91b61ed64824d30afe390527e74d62e9e6beee6f1a20`.

There are `binom(11,2)=55` unordered row pairs. A permutation on12 tails has at most four disjoint3-cycles. Hence there are **at most220 single-relative-3-cycle switch proposals** from this exact source. This is a finite neighborhood cap, not an estimate of a large SAT solver's convergence. Each proposal needs only two Hamiltonicity checks, a full raw directed-edge-cover check, and the exact root-intersection predicate from the defect packet. At most12 roots of a surviving decomposition could then require a direct literal11×11 definition check.

A finite assay at this scale would use no47k-variable CNF, no native solver, no compilation, no random restart and no scheduler. Its positive output, if any, would be an actual unrestricted Tuscan-2(11) candidate, not merely a permitted defect graph. A complete no-hit output would exclude ONLY this one-switch neighborhood; two switches, other odd relative-cycle lengths, other source decompositions and the full target would remain open.

The concrete written stall is now precise: the source's whole add-zero orbit and its one alternative same-alphabet row-rotation state share a six-triple obstruction. The missing ingredient is an edge-color reassignment that breaks that obstruction while retaining all Hamilton rows and creating a good root. This finite neighborhood is one checkable next attempt, not a promise that it will find such a reassignment.

## 4. Permission boundary

The unrestricted encoding request remains PREPARE/NOT_ADMITTED and none of its code was executed. The earlier deletion searches remain permanently supersededHOLD. This document grants no compute permission. If a small switch assay is proposed, it must freeze actual source/input bytes, controls (including both orientation examples above), resource/deadline/settlement and exact output before an independent named parent decision. A raw implementation's no-hit is not a certificate of unrestricted nonexistence or priority.
