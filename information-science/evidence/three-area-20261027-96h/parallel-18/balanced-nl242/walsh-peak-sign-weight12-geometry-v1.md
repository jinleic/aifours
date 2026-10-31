# info-6: every 12-point peak-sign relation is a symmetric difference of two 3-flats

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Actual `/bin/date` observed before this write: **2026-10-27T15:31:30-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** This is a universal characterization of a possible phase-relation support, not an assertion that such a relation or original witness exists. No scientific program, selected-state/plane probe, rank/type selection, formal/kernel or novelty claim.

## Claim

For the degree≤2 feature relation space on the odd Walsh half, a 12-point relation R is **exactly** the symmetric difference of two affine 3-flats meeting in an affine line. Either 3-flat's two common points need not be peak frequencies. This is a characterization of all such relations, not a selected example.

## Proof: a suitable pair of planes exists

By `walsh-peak-sign-circuit-gap-v1.md`, aff(R) has dimension 5. Form the 6-dimensional binary code C of all affine-linear evaluation words on the 12 points of R. Its row-space dimension is 6, and the degree≤2 relation identities imply C⊆C^⊥; thus C=C^⊥. It contains the all-one word. Its columns are distinct and nonzero, so self-duality rules out weight 1 or 2; complementing by the all-one word rules out weight 10 or 11. Let A₄,A₆,A₈ count weights 4,6,8. Complementation gives A₈=A₄ and A₆=62−2A₄.

Any two distinct columns are linearly independent, so exactly 16 codewords contain any specified pair of coordinates. Counting such incidences over all 66 coordinate pairs gives

    6A₄+15A₆+28A₈+66 = 66·16,

hence A₄=15. For a fixed coordinate, exactly 16 of the 32 weight-6 words contain it (pair each with its complement); if α weight-4 words contain it, then 15−α weight-8 words do. Counting codewords containing it and one further coordinate gives

    3α+5·16+7(15−α)+11 = 11·16,

so α=5. Every weight-4 word of the self-dual code selects four distinct R-points with XOR zero, hence an affine 2-flat.

Fix one such plane P. The other 14 weight-4 planes have total intersection size 4(5−1)=16 with P. Two distinct affine 2-flats meet in at most two points, so some other plane P′ meets P in exactly two. Their affine span F₁ is a 3-flat containing at least the six points P∪P′ of R.

## Proof: the second 3-flat is forced

Every full affine 3-flat is a degree≤2 feature relation. Therefore R△F₁ is also a relation. If |R∩F₁| were 7 or 8, its weight would be 6 or 4, contradicting the universal minimum relation weight 8. Thus |R∩F₁|=6 and |R△F₁|=8. By the previous weight-8 theorem, F₂:=R△F₁ is an affine 3-flat. Moreover F₁∩F₂=F₁\R has exactly two points, an affine line, and R=F₁△F₂.

Conversely, two affine 3-flats are each feature relations; if they meet in a line, their symmetric difference has 12 points and is also a relation. ∎

## Exact status and dependencies

For a peak-sign relation, the actual peak signs on R must multiply to +1. The two common points of the associated 3-flats are not asserted to be in the peak set, and no particular relation is constructed. The ≥49 independent checks need not include any weight-12 relation. These necessary phase constraints do not reconstruct all 512 Boolean bits or solve the original unrestricted peak-28 witness-or-exclusion problem; `(24,24,2)` remains open.

Inputs are the S1 supplied definitions and `walsh-peak-sign-circuit-gap-v1.md`, whose exact preceding author scope and dependencies remain unreviewed; the required finite-dimensional self-dual-code incidence counts are proved above rather than imported from an external classification. No old Gate-I body, candidate, held source, stopped half-split method or source-selection/method guide is an input. Main-notified 86/92 support retains its exact MINOR correction and does not adopt this theorem. Book-source equivalence, independent full-scope review, human, formal/kernel, executable and novelty gates remain unperformed; prior exposure, metadata-poll MINOR, S1 STOP/HOLD/ZERO, N4 UNKNOWN and aux214 STOP persist.
