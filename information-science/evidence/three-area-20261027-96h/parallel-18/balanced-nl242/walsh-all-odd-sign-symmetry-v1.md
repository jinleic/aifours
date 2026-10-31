# info-6: every admissible odd-sign phase is an actual symmetry of a realized magnitude profile

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Native `/bin/date` observed before write **2026-10-27T16:43:25-0700 PDT**. **AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** This is an all-functions symmetry consequence, not a canonical case, chosen test state, construction from an abstract profile or original witness/no-go.

## Statement

Fix the complete absolute Walsh profile of any **actual** balanced peak≤28 Boolean function f. This profile uniquely determines T, since |k(a)| mod 2=a·T at all 512 frequencies; it therefore also determines K=T^⊥ and H={a:a·T=1}. Fix any a₀∈H only to describe the following invariant statement.

Among all actual balanced functions with exactly this same full magnitude profile, precisely the 512 odd-frequency sign patterns permitted by the all-sign phase-skeleton relation occur. Starting from f, all 512 occur already under the 1024 global symmetries

    f_{t,d}(x)=f(x+t)+d,   t∈F₂⁹, d∈F₂.                     (1)

Each of the 512 patterns is reached by exactly two parameter pairs (t,d). In particular, if two actual functions have the same complete Walsh magnitudes, some translation/output-complement of the first agrees with the second at **every odd-frequency Walsh coefficient**. No agreement of their even-frequency coefficients or Boolean functions is asserted.

## Proof

From the pointwise global mod-4 identity, the preceding author candidate proves that for the fixed magnitude profile and every h∈K,

    sgn k(a₀+h)=ρ(|k(a₀+h)|)(−1)^{q(h)+c+L(h)},
    q(h)=1_{|k(h)|∈{2,6}},  ρ(m)=(−1)^{(m−1)/2},

for some c∈F₂ and some linear L:K→F₂. Thus no actual function with the given profile can produce an odd sign pattern outside the 512 affine choices. Different affine choices are different patterns because all 256 h∈K are present.

The definition of the Walsh transform gives directly, for every frequency a,

    k_{f_{t,d}}(a)=(−1)^{d+a·t} k_f(a).                       (2)

Therefore the full magnitudes, balance and the peak bound are unchanged. As h varies in K, the action on odd signs is the affine character (−1)^{d+a₀·t+h·t}. Every linear functional on K extends to V, and the standard dot product on V is nondegenerate; hence h↦h·t ranges over all linear functionals on K. After choosing such a t, d ranges freely and sets the affine constant. The map (t,d) to affine characters on K is a surjective linear map from a 10-dimensional to a 9-dimensional F₂-space, so each character has exactly two preimages. This proves all claims. ∎

## Exact scope

The statement begins with an actual function f. It does **not** show that an abstract magnitude profile satisfying phase or energy checks is realizable, that two functions of one magnitude profile are globally symmetry-equivalent, or that their even signs can be chosen independently. It performs no selected numerical/state probe, sector Fourier decomposition, stopped half-split/canonical method or truth-degree/ANF inference. All 512 frequencies and all original ranks/weights, including `(24,24,2)`, stay in scope; the original witness-or-unrestricted-exclusion remains open. No independent-review, external-human, formal/kernel, novelty, executable or clean-cognition claim is made.

Live pre-write pins: `prerequisite-derivation-v1.md` SHA-256 `075f61ffe1b5cfb000bb3bbda9ddd7fefea04e27806f19bedd9c5a2318fa3df9`, 87 LF; `walsh-all-odd-sign-magnitude-obstruction-v1.md` SHA-256 `8c5bdb238f66999b9f791c545324bfeca25c654a811551387dfff0c9adaac961`, 50 LF, itself UNREVIEWED and requested for disjoint review. The caller is parent-notified same-harness written support, subject to the count-direction MINOR. Parent L1 quarantine and every earlier S1 STOP/HOLD/ZERO/NONINPUT, mandatory w44 erratum, process MINOR, N4 UNKNOWN and aux214 STOP remain in force.
