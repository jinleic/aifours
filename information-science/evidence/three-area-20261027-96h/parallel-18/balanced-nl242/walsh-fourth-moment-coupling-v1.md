# info-6: an integral fourth-moment coupling for every balanced Boolean object

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Actual `/bin/date` observed before this write: **2026-10-27T14:59:23-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** This is an all-variable necessary constraint, not an original witness, unrestricted exclusion, rank/weight exclusion, numerical nonlinearity improvement, formal/kernel or novelty claim. No scientific program, selected-state probe or external-model review was used.

## Claim

For every balanced f:F₂⁹→{0,1}, let k=W_f/4. Then

    Σ_a k(a)⁴ ≡ 0 (mod 256),       Σ_a k(a)⁴ ≥ 532480.             (1)

Under |k|≤7, if n_j counts frequencies with |k|=j, the **one common global histogram** must also obey

    n₂+n₆+5n₃+7n₅+6n₇ ≡ 0 (mod 16).                               (2)

All frequencies and both parity branches are included. No particular histogram, f or test direction is chosen or generated.

## Proof

Write s(x)=(-1)^{f(x)} and C(t)=Σ_x s(x)s(x+t). For each t≠0 the unequal source pairs number m_t, and balance implies m_t is even. Hence C(t)=512−4m_t is divisible by 8; C(0)=512 is divisible by 8 too. Put J(t)=C(t)/8∈Z. Then J(0)=64 and, because Σ_x s(x)=0,

    Σ_t J(t)=(1/8)(Σ_x s(x))²=0.                                (3)

Character orthogonality on k=W/4 gives

    Σ_a k(a)²χ_a(t)=32C(t)=256J(t).

Applying Parseval to the real function a↦k(a)² yields the exact identity

    Σ_a k(a)⁴ = 128Σ_t J(t)².                                   (4)

Integer squares are congruent to their bases mod 2. By (3), Σ_t J(t)² is even, proving the divisibility in (1). Also

    Σ_{t≠0}J(t)² ≥ Σ_{t≠0}|J(t)| ≥ |Σ_{t≠0}J(t)|=64.

Including J(0)²=4096 in (4) gives the lower bound. Equality could hold only if every nonzero-t J is 0 or −1, with exactly 64 values −1; this is a necessary equality condition, not a claim that it is realizable.

For (2), the exact parity coupling from the definition-first caller says the number n₁+n₃+n₅+n₇ of odd k-values is either 0 or 256, hence 0 mod 256. Reduce the exact fourth moment modulo 256, subtract this odd count, and divide the resulting congruence by 16. The terms of magnitudes 2,6 have fourth power 16 modulo 256; the differences from the odd baseline for magnitudes 3,5,7 are respectively 80,112,96; magnitude 4 contributes 0. This gives (2). ∎

## Exact status and inputs

The moment/divisibility constraints are necessary for all actual Boolean witnesses and couple an entire shared spectrum, but no satisfying histogram or contradicting candidate is selected. They do not replace the common phase/autocorrelation equations or the exact 512-bit caller. Neither an actual balanced peak-28 witness nor an unrestricted exclusion is obtained; all ranks/weights and `(24,24,2)` remain open.

Inputs are only the S1 definition packet, elementary character orthogonality and the actual Boolean/parity facts in `prerequisite-derivation-v1.md` SHA-256 `075f61ffe1b5cfb000bb3bbda9ddd7fefea04e27806f19bedd9c5a2318fa3df9`, 87 LF, and `walsh-hyperplane-energy-v1.md` SHA-256 `6a1000f1c95ef4264e82fba6d229e59393241efaed367ee4d3e5687cec0f88a0`, 49 LF. Both are unreviewed own derivations from the same supplied definitions, not independent evidence. No old candidate, held source or selection/method guidance is an input. Source/book equivalence, independent full-scope review, human, formal/kernel, executable and novelty gates remain unperformed; all S1 HOLD/STOP/ZERO, N4 UNKNOWN and aux214 STOP persist.
