# info-6: a seven-dimensional difference obstruction forces at least 53 peak cubes

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Actual `/bin/date` observed before this write: **2026-10-27T15:59:23-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** This is a universal conditional combinatorial strengthening, not a chosen peak set, witness, unrestricted no-go, rank/type exclusion, numerical nonlinearity improvement, formal/kernel or novelty claim. No scientific program, enumeration of states, selected-state/direction/plane probe or external-model review was used.

## Claim

Any original balanced peak≤28 Boolean object would have at least **53 distinct affine 3-flats entirely of peak frequencies**; each has positive peak-sign product. This strengthens the unreviewed ≥46 statement. It neither constructs an object/flat nor proves the original target impossible.

## 1. An elementary seven-dimensional difference lemma

A subset A of F₂⁷ whose unordered pair sums of distinct points are all different has at most 15 points.

Suppose instead that |A|=16. Its 120 nonzero pair sums are distinct, leaving a set D of seven nonzero vectors. For any nonzero character ξ, the Fourier convolution identity gives

    Â(ξ)² = 14−2 D̂(ξ).                                          (1)

Here D̂ is an odd integer between −7 and 7, and Â is even. The only possible values of D̂(ξ) are 7,5,−1. Let their counts over nonzero ξ be A₇,A₅,A₋₁. Since 0∉D, Parseval and the sum of all D̂-values yield

    A₇+A₅+A₋₁=127,   2A₇+A₅=30,   4A₇+3A₅=60.

Thus A₇=15 and A₅=0. Including ξ=0, there are 16 characters taking value 7, exactly the annihilator of span(D). Therefore span(D) has dimension 3, and D is precisely its seven nonzero vectors. Since no difference of two A-points lies in that 3-space, A is a transversal of its 16 cosets.

Choose a linear complement and write this transversal as the graph of a function φ:F₂⁴→F₂³. For every nonzero u∈F₂⁴, its eight unordered u-pairs must have eight distinct differences, so the derivative φ(v)+φ(v+u) takes every value of F₂³ exactly twice as v ranges over F₂⁴. For every nonzero λ∈F₂³, the sign function (-1)^{λ·φ(v)} therefore has zero autocorrelation at every nonzero u; character orthogonality gives a Walsh transform of magnitude 4 at every input frequency. In particular Σ_v(-1)^{λ·φ(v)}=4ε_λ with ε_λ∈{±1}.

Let N_y=#{v:φ(v)=y}. Fourier inversion on the output group gives, for **every** y,

    2N_y = 4+Σ_{λ≠0} ε_λ(-1)^{λ·y}.

The right side is odd, because it is 4 plus seven signs, whereas the left side is even. Contradiction. This is a uniform integer/character argument, not a search over graphs or a selected control. ∎

## 2. Universal peak-cube count

The peak set S of a putative original object lies in an affine 8-space and has n≥92 by Main-notified same-harness written support, with the mandatory count-direction MINOR. For each nonzero direction b, let e_b be the number of disjoint b-pairs in S, and let G_b count pairs (D, peak 3-flat) where D is a two-dimensional direction containing b inside that 3-flat. The 127 possible D correspond to nonzero vectors of the 7-dimensional quotient by ⟨b⟩.

If e_b=16 and G_b=0, the 16 quotient points have distinct unordered pair differences, contrary to the lemma. If e_b≥17, the plane-direction pigeonhole gives G_b≥binom(e_b,2)−127. Together these imply for every nonzero b

    G_b ≥ max{0,8e_b−127}.

Every peak 3-flat is counted by exactly 21 pairs (b,D), and Σ_b e_b=binom(n,2). Thus, for G the total number of peak 3-flats,

    21G ≥ 8 binom(n,2) −255·127 ≥ 1103,
    G≥53.

The v1 mod-4 third-difference caller makes the product of peak signs on each 3-flat positive, as in the direct sign addendum. These are universal counts/constraints on one actual array; no individual direction or 3-flat was selected. ∎

## Exact scope and inputs

The ≥92 peak premise is Main-notified same-harness written support for `walsh-peak-multiplicity-v1.md` SHA-256 `8a64a73bc552f9e71cc04f07159c1f09feab17894d31966c16ebfe80d9fd37b8`, 28 LF, with `walsh-support-xor-coupled-count-erratum-v1.md` SHA-256 `810e3e55c52288f252b335a776a134752702df33d70d8d689fb009aac127273c`, 30 LF. The direct sign consequence is in `walsh-forced-peak-3flat-sign-addendum-v1.md` SHA-256 `b46d6cc50c83af88d327e3e097b853c9bfb642bbcae9476fc2603aa188ee5cef`, 15 LF; the new combinatorial argument and ≥53 claim are unreviewed. The 4+3 decomposition in §1 is an internal quotient of an arbitrary abstract pair-difference set, not the stopped original Walsh half-split/canonical Gate-I method or the stopped global truth-degree/ANF branch.

The unrestricted balanced peak-28 witness-or-no-go, all original ranks/weights and `(24,24,2)` remain open. No old proof, held guide, stopped method or selected input is used. Main's parent/review bodies were not reopened. Book-source equivalence, independent full-scope review of this result, human, formal/kernel, executable and novelty gates remain unperformed. Prior exposure, metadata-poll MINOR, all S1 STOP/HOLD/ZERO, N4 UNKNOWN and aux214 STOP persist.
