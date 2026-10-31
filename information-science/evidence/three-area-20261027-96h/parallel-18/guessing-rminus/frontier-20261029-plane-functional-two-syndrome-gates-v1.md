# Functional-fiber gates for affine binary syndrome planes

## Required source order

Read BOTH errata before their source consumers:

1. `frontier-20261028-full-source-lp-optimum-v1-erratum-1.md`, SHA-256 `c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9` (Remark 5.4, not 3.8).
2. `frontier-20261028-two-syndrome-local-neighborhood-erratum-v1.md`, SHA-256 `8ff79f6d07b935025e0b2f3de27928f030d251787724b64e05ccd9f1f012a37f`. This withdraws the unsupported old general two-syndrome application; its local FDs at vertices 3 and 4 do NOT follow from the original graph FDs alone.

The ONLY two-syndrome theorem imported here is the repaired actual-component theorem `frontier-20261028-two-syndrome-repaired-theorem-v1.md`, SHA-256 `9feb6cd50a2b376b971c2091369b5c5ad7d50e18446ce4cd3293bfc718b776b1`. It supplies local component FDs from actual triangle parities, not by strengthening the original graph FDs. It has its own named certificate, gadget and proper-subgraph imports and remains WRITTEN/unreviewed; no earlier withdrawal is silently cleared. No held review is an input.

**Status: WRITTEN implication conditional on that repaired theorem.** This note adds new, explicitly import-dependent rows to a successor functional relaxation. Older certificates/checkers using only the full-state gate are unchanged.

## Setting

Use the ten binary triangle factors in the q=8 encoding. Let the full parity syndrome lie in any subset of an affine two-plane. Let J be its varying-factor set. Condition first on the complete tuples of factors outside J, as in `frontier-20261028-syndrome-cover-entropy-gate-v1.md` (SHA-256 `d6df004e025f067a14a6cc69e9aef8d9fc78a20a2fc49c4e431328120e32014b`). In a positive-probability fiber, write Y_v for the selected components at vertex v and S=(A,B) for affine coordinates of the selected syndrome. Its support can be any subset of the four plane points, with arbitrary probabilities.

The selected variables retain the original graph FDs: every conditioned component is a known constant that can be supplied to the original full-neighbor decoder. S is a deterministic function of Y_V. Each selected triangle's parity is an affine functional of S, with its constant part fixed on the plane.

## Lemma

For each nonzero linear functional l in {A,B,A+B},

3 H(Y_V) + 17 H(l) - 2 sum_v H(Y_v,l) <= 0.

## Proof

Fix a value l=e of positive probability. An affine line in a binary two-plane has at most two points, so the selected syndrome has at most two values on this fiber.

Embed Y back into the full ten-triangle binary encoding by filling every omitted component with a fixed zero bit. These inserted constants change none of H(Y_V) or H(Y_v). The original graph FDs remain valid, because constants can be supplied to each decoder. The full syndrome has the selected parity entries and fixed zero entries elsewhere, hence at most two values.

The repaired actual-component two-syndrome theorem therefore applies to this embedded law and gives

3 H(Y_V | l=e) - 2 sum_v H(Y_v | l=e) <= 0.

Average over e. Since l is determined by Y_V, expand conditional entropies:

3[H(Y_V)-H(l)] - 2 sum_v [H(Y_v,l)-H(l)] <= 0,

which is exactly the stated row (20-3=17). This uses no uniformity, independence of factors, full four-point support or numerical entropy cap on S.

## Relaxation and verification boundary

The old functional LP had only the full-state gate G_S. Its direct dual search recovered three hard exact certificates but found the remaining twenty cases floating-dual-infeasible. That does not establish a primal counterexample, much less an actual coding law.

A successor may now add G_A, G_B and G_(A+B), but only with the repaired theorem and its required erratum explicitly bound as imports. Its checker must reject these rows when those bindings are absent. Any resulting all-plane conclusion is conditional on all imported written proofs and their lifting; it is not a global guessing-number bound or scientific adoption.
