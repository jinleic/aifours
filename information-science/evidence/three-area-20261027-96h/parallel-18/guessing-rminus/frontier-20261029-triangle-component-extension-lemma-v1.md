# Actual triangle-component extensions of a coarse functional profile

## Required first inputs and independent scope

Read the historical LP-source erratum `frontier-20261028-full-source-lp-optimum-v1-erratum-1.md`, SHA-256 `c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9`, before its consumers. For old primal-check evidence, read `frontier-20261029-primal-checker-subset-coverage-erratum-v1.json`; only corrected full-subset checkers carry primal claims.

This is a new ACTUAL-COMPONENT representation, not a further enumeration of the unchanged DFZ family. Inputs are the admitted v1 functional-profile contract, its exact countermodels/proposal points, and the literal binary triangle encoding in `frontier-20261028-triangle-code-global-obstruction-v1.md` (SHA-256 `bdf79fd631e8e58a734a4ef4c93f899e319f45712a219a876f527b52f1d61bb4`). No f161 consumer, paused functional-gate import, or two-syndrome entropy theorem is used.

**Status: WRITTEN elementary extension lemma, not a Delta bound or actual code witness.**

## The actual variables

Work in a selected-factor fiber of the binary affine-plane encoding, with selected vertex tuples Y1,...,Y10 and syndrome-plane coordinate S=(A,B). Let t be one selected triangle {i,j,k}, whose parity is L+c with L one of A,B,A+B and c fixed. Write U,V,W for the three ACTUAL component bits of that factor at its three vertices.

By definition of the representation:

- U is a coordinate projection of Y_i, V of Y_j, W of Y_k;
- L is a function of S;
- L is determined by (U,V,W), since U xor V xor W = L+c;
- each component is determined by the other two components and L.

These are componentwise statements, NOT consequences of the original graph FDs alone. In particular, one must not identify Y_i with U or assume that an entire vertex tuple is determined by the other two triangle vertices. No factor independence, uniformity, numerical bit-entropy cap or two-syndrome support restriction is assumed.

Every actual law therefore has a joint entropy extension on fifteen named variables

(Y1,...,Y10,S,L,U,V,W)

satisfying all full elemental Shannon rows and the seven projection/parity/inverse equalities above (three projection FDs, one parity FD, three inverse FDs).

## Safe coordinate identification

Because L is a function of S, for every tuple K, including the component bits,

H(K,S,L) = H(K,S).

Thus a mask containing S can drop L. Coordinates involving no component bit are already known from the coarse profile: original-only, original+S, or original+L. All other entropy coordinates remain genuinely unknown; they must not be filled with zero or guessed.

A minimum-uniform-violation LP may hold the coarse profile fixed and ask whether these unknown coordinates extend it. A positive numerical minimum is only a LEAD. To claim a new coarse entropy inequality, a separate exact Farkas combination must cancel every unknown component coordinate with correct Shannon signs, and an independent checker must reconstruct every used projection/parity/CMI row.

## Initial bounded experiment

Test selected factor 2, triangle {1,4,5}, for cases 65 and 493 at the current independent v1/joint-DFZ proposal points. The corresponding functional is read from each case's own coloring. The same structural contract applies to every selected factor; no claim is made for omitted factors or abstract auxiliaries lacking actual component projections.
