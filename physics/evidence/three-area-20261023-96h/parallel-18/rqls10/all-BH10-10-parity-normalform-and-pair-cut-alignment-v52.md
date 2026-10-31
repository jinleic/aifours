# RQLS10 v52 — ALL tenth-root Hadamards have a two-case parity normal form; two nontrivial cuts must ALIGN to allow a resolution

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE writing this NEW manuscript: **Mon Oct 26 11:48:06 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact root/parity/monomial/block-count proof only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO/private approximate scout/backconversion. No machine/kernel/formal/configured-family/human/priority/novelty/accepted finite-witness claim.

This is a theorem about the ENTIRE BH(10,10) phase alphabet, not a Fourier/Gaussian normal form asserted WLOG. It reduces the next genuinely different Hadamard-pair cases and explicitly preserves the aligned-cut residual instead of declaring another unjustified universal no-go.

## 1. Complete basis normal form, with exact monomial operations

Let omega=exp(2pi*i/10),zeta=omega^2. Consider ANY10x10 unit-entry Hadamard with entries tenth roots. ENTIREv51's exact signed-root-count lemma says a zero ten-term tenth-root sum has binary exponent weight0,5or10. Consequently its row rays have at mostTWO projective binary parity classes; if two, they occur five rows each.

Normalize one row's parity word to0 by common coordinate phases omega^h. Normalize each row's first binary representative by a constant ray phase. These are legitimate tenth-root row/column phase operations, not arbitrary nonlinear finite-code changes.

ExactlyONE of the following holds:

**TypeI — one binary class.** All rows have binary word0; all entries are FIFTH roots. The matrix is monomial-equivalent, using only tenth-root row/column phases, to a BH(10,5).

**TypeII — two binary classes.** Five rows have parity0 and five rows have the same binary word w of weight5. Reorder those rows and the five coordinates on which w=1. Since omega^e=(-1)^e*zeta^(3e), the matrix has the exact form

    H=[[A,B],[C,-D]],

where A,B,C,D are5x5 matrices of FIFTH roots (unit entries), and the full matrix is Hadamard. The nontrivial physical binary cut is the projective class[w], defined modulo its complement.

This is an EXHAUSTIVE dichotomy for BH(10,10). The four5x5 blocks are NOT asserted individually Hadamard. Their required equations remain the actual block-unitary equations, e.g.

    AA^dagger+BB^dagger=10I5,
    CC^dagger+DD^dagger=10I5,
    AC^dagger-BD^dagger=0,

and the corresponding column equations. Deleting the minus sign need not leave a Hadamard; TypeII is not silently reclassified as a fifth-root basis.

## 2. All pairings and independent monomial normalizations remain literal

For ANY two such Hadamards H,K form the actual row-product QLS

    q_(a,b)(s)=K_(a,s)*conj(H_(b,s))/sqrt10.

Rows/columns are always ONBs. Arbitrary independent row/column phases/permutations of H,K act as cell phases/relabelings plus one common physical coordinate unitary, except the relative coordinate permutation, which is KEPT in the relative positions of the two binary cuts below. It is not discarded as a normalizer or covariance WLOG.

Normalizing the baseline binary class of each matrix independently multiplies the array by one common coordinate tenth-root diagonal, so it preserves every actual resolution and ray distinctness. Thus each TypeII matrix has row classes0,w, with five rows of each. A TypeI matrix has onlyclass0. We analyze all three possible pair-type combinations, not just two matrices with the same cut.

## 3. TypeII/TypeII MISALIGNED cuts: NO quantum transversal whatsoever

Let the normalized physical cuts be w_H,w_K, both of weight5, after the ACTUAL relative coordinate permutation is included. Suppose their projective binary classes are DIFFERENT. They are nonzero independent classes inF2^10/<1>.

Cell parity depends on its K-row type r and H-row type c in{0,1}:

    class(q)=r*[w_K]+c*[w_H].

The four classes are distinct. Their binary weight parities are even,odd,odd,even; hence the opposite pairs(00,11) and(01,10) cannot contain orthogonal rays, exactly byv51's necessary Hamming5 condition.

A full row-and-column transversal chooses five rows of each type and five columns of each type, so its four counts are(s,5-s,5-s,s). If1<=s<=4 it contains FOUR classes, impossible for an actual tenth-root ONB. If s0or5 it contains one incompatible opposite pair. Thus NO quantum transversal exists.

This holds for ALL two TypeII Hadamards, not only Fourier matrices, and for EVERY pairing with misaligned cuts. No maximality hypothesis is needed for the obstruction. Any resolvable TypeII/TypeII pair must have aligned cuts.

## 4. TypeII/TypeII ALIGNED cuts: every transversal is PURE and a full resolution splits5+5

Now suppose[w_H]=[w_K]. Choose complementary representatives/row phases so both are the same weight5 wordw. The four cell parity classes collapse to TWO:

    00 and11 have class0;
    01 and10 have class[w].

Each class occupiesFIFTY cells. A transversal with contingency(s,5-s,5-s,s) has2s cells of class0 and10-2s of classw. If BOTH classes occur, the complete basis parity theorem forces5ofeach. But2s isEVEN and cannot equal5. Therefore EVERY quantum transversal is PURE: s5(all same-type cells) or s0(all opposite-type cells).

A full resolution would require exactlyFIVE pure-class0 transversals covering its fifty cells, and exactlyFIVE pure-classw transversals covering the other fifty. Arbitrary mixing is impossible, but these pure transversals have NOT been proved absent in general.

Within either class, one fixed coordinate sign pattern turns all its ray representatives into FIFTH-root phases. Thus each hypothetical pure transversal must satisfy the exact phase5 GH balance/two-field/rank4 constraints ofv40–v42. This does NOT say the underlying unsigned5-block matrices form a pair of fifth-root Hadamards; the TypeII minus sign was essential to the original row/column bases. The all-Gaussian phase5-pair no-go cannot be copied onto this residual without proving its hypotheses.

No common5-dimensional COMPLEX sector is inferred merely from the binary classes. Their vectors are flat and have half-coordinate projection1/2, not binary0/1; such a false sector promotion would repeat an invalid marginal argument.

## 5. TypeI/TypeI and TypeI/TypeII cases remain explicitly separate

For TypeI/TypeI, after the common coordinate normalization ALL array rays are fifth-root phases. This is the full phase5 Hadamard-pair branch, with its exact finite geometries and the model-specific closures already written. No new general exclusion is claimed.

For a TypeI/TypeII pair, cell parity depends ONLY on the TypeII row/column type. Every row-and-column transversal automatically has5ofeach class, which is COMPATIBLE with the two-class basis theorem. The misalignment/four-class contradiction does NOT apply. No unrestricted no-go is asserted for this genuinely remaining mixed-type case.

Thus the exact remaining pair families are:

    fifth-root/fifth-root;
    fifth-root/nontrivial-TypeII;
    TypeII/TypeII with an ALIGNED physical5-cut,

with all original row/column/full-resolution/maximality conditions still required. The normal form does not solve those conditions by itself.

## 6. Exact interpretation for signed-Gaussian models and original geometry

Signed Gaussian BH(10,10) block constructions are examples of TypeII, but the theorem did not use their coefficients or a published classification. Two such matrices with a relative permutation NOT aligning their physical cuts are excluded at once by section3. Aligned-cut cases must be analyzed as the pure two-class problem ofsection4, not as the already closed nonsquare-ratio fifth-root Gaussian pair family.

The proof applies to arbitrary BH(10,10) entries in any common coordinate basis. It does NOT show an arbitrary original maximal1-RQLS10 has flat tenth-root coordinates, nor that every flat tenth-root QLS is a two-Hadamard construction. No phase-model WLOG, full original no-go or100-ray witness is supplied. The unrestricted intrinsic10/4+6/5+5 branches remain OPEN.

## 7. Entire gate/import/assurance contract

Read/reconstruct ALLseven sections/endings plus ENTIREv51's exact root-count/projective-binary/two-class-five-five proof, andv40–v42 only as used for the pure-class context consequence. Required new claims are complete monomial normal-form existence; both parity normalizations preserving the actual array; ALL pair-type cases; ALL relative-cut positions; misaligned four-block contingency; aligned EVENcountsversusFIVE forcing pure transversals; exact five-plus-five resolution census; and the mandatory non-Hadamard unsigned-block/non-complex-sector caveats.

No Butson/quantum-Latin/classifier output is an operative premise. All arithmetic is exact WRITTEN, NOT machine-checked. No scientific execution/private approximate scout/finite enumeration/independent finite-witness checker/control/vendor/priority gate used or called passed. No100-ray1-RQLS witness/unrestrictedno-go/formal/kernel/family/human/current-openness/novelty promotion. All old process/math findings, v9/v14 withdrawals, frozen histories and ZERO-credit quarantines persist. Original18/exclusive-root/HOLD/cadence/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38; primary continues the aligned-cut/mixed-type or genuinely unrestricted geometry, no early pending-review park.
