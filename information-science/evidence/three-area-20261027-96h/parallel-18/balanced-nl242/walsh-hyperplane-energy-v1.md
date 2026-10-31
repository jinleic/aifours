# info-6: all-hyperplane energy divisibility from one balanced Boolean object

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Actual `/bin/date` observed before this write: **2026-10-27T14:49:18-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** This is an all-variable necessary coupling, not a witness, unrestricted exclusion, rank exclusion, numerical improvement, formal/kernel or novelty claim. No scientific program, selected-state probe or external-model review was used.

## Setup and claim

Use only the released definitions and the elementary sign/Walsh caller derived in `prerequisite-derivation-v1.md`, SHA-256 `075f61ffe1b5cfb000bb3bbda9ddd7fefea04e27806f19bedd9c5a2318fa3df9`, 87 LF. Let V=F₂⁹, f:V→{0,1} be balanced, W its actual Walsh transform, k=W/4, and |k|≤7 at every frequency for the original target.

For every nonzero t∈V, both frequency-half energies satisfy

    Σ_{a:t·a=b} k(a)² ≡ 0 (mod 128),      b∈{0,1}.                (1)

Equivalently the Walsh transform of the single global squared-spectrum array k² is divisible by 256 at every t. These statements are simultaneous: no arbitrary choice of an independent profile in each half is permitted.

## 1. Exact local transform and Boolean caller

Fix an arbitrary nonzero t, put H=t^⊥, and take any a₀ outside H. The 256 characters of H are indexed by source pairs [x]={x,x+t}. For each pair put

    F([x]) := Σ_{h∈H} k(a₀+h)(−1)^{h·x}.

All frequencies a₀+h are nonzero. From the actual Boolean definition and orthogonality on H,

    F([x])=−128·(−1)^{a₀·x}[f(x)−f(x+t)] ∈{0,±128}.            (2)

The expression is independent of the representative x: the two sign changes cancel. Let m_t be the number of source pairs for which f(x)≠f(x+t). Parseval on H gives

    Σ_{a:t·a=1} k(a)² = 64m_t.                                  (3)

This holds for **every** nonzero t, without choosing a test direction. Since the 256 ones of balanced f occur as either two ones in a source pair or one in a disagreeing pair, m_t is even. Therefore the right side of (3) is a multiple of 128. The total energy Σ_a k(a)²=2¹⁴, so the other half is a multiple of 128 too. This proves (1). For t=0 the b=0 energy is 2¹⁴ and the b=1 set is empty, so the degenerate statement also holds. ∎

A second exact coupling is

    Σ_{t∈V}m_t=|{f=1}|·|{f=0}|=256².                            (4)

Here m₀=0. Count ordered pairs (x,y) with f(x)=1,f(y)=0 by t=x+y: for each nonzero t each disagreeing unordered t-pair contributes exactly one such ordered pair. The m_t in (3)–(4) must all come from this **same** f; (4) is not a grant to choose them independently.

## 2. Simultaneous magnitude restrictions on each frequency half

For each nonzero t and b∈{0,1}, let n_j(t,b) count frequencies in that half with |k|=j, j=1,…,7. From the definition-first coupling in the previous file, the odd support is either empty or a full affine hyperplane. Its intersection with any frequency half therefore has 0, 128 or 256 points, always divisible by 32. Reducing (1) modulo 32 and using the possible squares of j gives, for **every** t≠0 and b,

    n₂+n₆+2n₃+6n₅+4n₄+4n₇ ≡ 0 (mod 8).                           (5)

This family constrains overlapping halves of one global magnitude array; it is stronger than imposing only one aggregate congruence. The odd-support statement itself and the source f are inherited from the explicitly derived actual-object caller, not from an old rank/type theorem. No special t or magnitude pattern is tested.

## 3. Exact remaining implication

The necessary energy restrictions (1) and (5) may rule out an independently proposed magnitude array without choosing its spectral signs, but **no such array is proposed or tested here**. They are not claimed sufficient: phase signs, all shift autocorrelations and all 512 Boolean inverse values must still be realized simultaneously by one array, as in the prior exact caller. The unresolved unrestricted problem is to construct that actual balanced object or exclude every array satisfying the full coupled conditions. Neither alternative is achieved; every rank/weight and the `(24,24,2)` gap remain open.

The Main-authored source definitions have not been certified against the original book. Full-scope independent written review, human, formal/kernel, executable and novelty gates remain NOT PERFORMED. Prior author exposure and all S1 HELD/ZERO/NONINPUT, STOP/HOLD, N4 UNKNOWN and aux214 STOP controls remain binding.
