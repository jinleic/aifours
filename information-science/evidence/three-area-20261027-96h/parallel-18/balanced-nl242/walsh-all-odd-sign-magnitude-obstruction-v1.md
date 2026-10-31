# info-6: all odd signs are fixed by magnitudes up to one affine character

Owner **InfoBalancedNL242-2-2**, same original info-6 slot. Native `/bin/date` observed before this write: **2026-10-27T16:41:59-0700 PDT**. **NEW AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Every statement is universal over the original full-array problem; no coefficient assignment, direction, rank/type, truth table or numerical probe is selected. This is not an actual witness or an unrestricted contradiction.

## All-sign theorem

For any actual balanced peak≤28 Boolean function, let k=W_f/4 and T be the XOR of its one-support. Use the parent-notified T≠0 result, put K=T^⊥ and H={a:a·T=1}, and take an **arbitrary** a₀∈H. The actual k values on K are even, and the actual k values on H are odd and nonzero. For h∈K set

    q(h)=1_{|k(h)|∈{2,6}},   m(h)=|k(a₀+h)|∈{1,3,5,7},
    ρ(m)=(−1)^{(m−1)/2},       ε(h)=sgn k(a₀+h).

There is one affine character h↦(−1)^{c+L(h)} such that, for **every** h∈K,

    ε(h)=ρ(m(h)) (−1)^{q(h)+c+L(h)}.                           (1)

Consequently, conditional on the full magnitude profile, all 256 odd signs lie in at most 2⁹=512 patterns, and at least 256−9=247 independent binary sign-consistency equations hold. The full-cube evaluation map has rank exactly nine, so 247 is exact for this *conditional phase skeleton*. The equations are not claimed independent of earlier peak-only checks or of the other actual-Boolean constraints.

## Proof and exact phase-skeleton converse

The parent-notified definition-first caller supplies one global bilinear identity

    k(a+b)−k(a)−k(b) ≡ 2𝔅(a,b) (mod 4),  k(a) mod 2=a·T.

Since |k|≤7 and k(h) is even, q(h)=k(h)/2 mod 2. For every h∈K, this identity gives

    [k(a₀+h)−1]/2 = q(h)+[k(a₀)−1]/2+𝔅(a₀,h)  (mod 2).

For each odd nonzero integer k with |k|≤7, direct inspection of the four possible **symbolic magnitude classes** gives sgn k=ρ(|k|)(−1)^{(k−1)/2}; no actual coefficient or state was selected. Substitution proves (1), with c=[k(a₀)−1]/2 mod 2 and L(h)=𝔅(a₀,h).

For fixed magnitudes define ν(h)=ρ(m(h))ε(h)(−1)^{q(h)}. Equation (1) says ν is an affine character. Conversely, for an abstract sign array, the equations Π_{z∈h+⟨u,v⟩}ν(z)=1 on **all** affine 2-flats are equivalent to ν being affine: their additive binary form says every second derivative is zero. They impose exactly 247 independent binary constraints because the space of affine binary functions on K has dimension nine. This converse is only a phase-skeleton equivalence. It does not make the magnitudes, q, remaining even signs, global autocorrelation or inverse 512 Boolean bits realizable. ∎

## Magnitude-only autocorrelation obstruction, all directions and both polarities

For each nonzero b∈K, partition the 128 unordered b-pairs of odd positions into the two classes τ=±1 according to the **magnitude-computable** label

    λ_b({h,h+b}) = ρ(m(h))ρ(m(h+b))(−1)^{q(h)+q(h+b)}.

Let A_b^τ be the complete class with label τ. The label is independent of which endpoint represents the unordered pair. It uses only the full spectrum's absolute values and the arbitrary a₀. Then necessarily, simultaneously for **every** b≠0 and **both** τ,

    Σ_{{h,h+b}∈A_b^τ} (m(h)+m(h+b))² ≤ 2¹⁴.                  (2)

Indeed, (1) makes the products k(a₀+h)k(a₀+h+b) of all pairs in A_b^τ share one sign, namely τ(−1)^{L(b)}. The global zero autocorrelation at b partitions **all 512 frequencies** into 256 unordered pairs. The energy outside A_b^τ must therefore compensate the absolute sum of its products. Using |xy|≤(x²+y²)/2 on every remaining pair and the full Parseval energy Σ_a k(a)²=2¹⁴ gives (2). A different arbitrary choice of a₀ may interchange the two labels for a given b, but cannot change the conjunction of the two inequalities.

Thus any abstract full magnitude profile with a valid T and q that violates (2) for any direction/polarity cannot come from an original witness, regardless of all unassigned coefficient signs. This is a conditional profile obstruction, not a claim that all profiles violate it. No Fourier transform/decomposition of frequency sectors, complementary ternary representation, truth-degree/ANF method, chosen numerical probe or scientific executable is involved.

## Pinned inputs and outstanding gap

Before writing, `/usr/bin/shasum` and `/usr/bin/wc` pinned `prerequisite-derivation-v1.md` SHA-256 `075f61ffe1b5cfb000bb3bbda9ddd7fefea04e27806f19bedd9c5a2318fa3df9`, 87 LF; `walsh-peak-phase-even-magnitude-coupling-v1.md` SHA-256 `5d41ef4bac2cbc810e477af77ed5a99895450bed06a89011b688467bac331eaf`, 43 LF; and `walsh-radical-peak-occupancy-v1.md` SHA-256 `f2a8685d1178f0bd668254bed47352eff4c57a0bc5d280fa4f787afcfba96103`, 45 LF. The last two are unreviewed author-only; the argument above follows directly from the parent-notified supported caller. The T≠0 premise is at same-harness written support with the mandatory coupled-count MINOR.

Neither (1) nor (2) furnishes an actual Boolean truth table or an unrestricted no-go, and the exact original `(24,24,2)` and all ranks/weights stay in scope. No independent-review, human, formal/kernel, novelty or scientific-execution claim is made. All prior S1 STOP/HOLD/ZERO/NONINPUT, parent L1 quarantine, w44 erratum, count-direction and process MINORs, N4 UNKNOWN and aux214 STOP remain binding; no clean-cognition assurance is inferred.
