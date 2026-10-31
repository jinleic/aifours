# info-6: every affine restriction is coupled to a global Walsh coset

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Actual `/bin/date` observed before this write: **2026-10-27T15:15:50-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** This is a universally quantified original-object restriction and saturation lemma, not a selected affine flat, a witness, unrestricted no-go, rank/type exclusion, numerical nonlinearity improvement, formal/kernel or novelty claim. No scientific program or selected-state/direction probe was used.

## 1. Exact local/global interface

Suppose f:F₂⁹→{0,1} is balanced and |W_f(a)|≤28 for **every** a. Let s=(-1)^f and T=Σ_{f(x)=1}x. Take an arbitrary affine d-flat F=x₀+U, 1≤d≤9, and an arbitrary linear functional η on U. Let A_η={a∈F₂⁹:a|_U=η}, with N=|A_η|=2^{9−d}. Define the local Walsh coefficient

    L(F,η)=Σ_{u∈U} s(x₀+u)(−1)^{η(u)}.

Character orthogonality gives the exact same-object identity

    L(F,η)=(1/N)Σ_{a∈A_η} W_f(a)(−1)^{a·x₀}.                  (1)

The all-frequency parity identity from the released definition-first caller is W_f(a)/4 mod 2=a·T. Thus each summand in (1) has absolute value at most 24 on the even-parity frequencies and at most 28 on the odd-parity frequencies.

## 2. Universal local bounds, including the zero-frequency correction

For every F and η, define

    B(U,η,T) = 24  if T∈U and η(T)=0;
               28  if T∈U and η(T)=1;
               26  if T∉U.

Then

    |L(F,η)| ≤ 2 floor( min{2^d, B−1_{η=0}·24/N}/2 ).           (2)

If T∈U, every extension in A_η has a·T=η(T). If T∉U, exactly half the extensions have each parity, giving their average bound 26. When η=0 the extension set contains a=0, where W_f(0)=0 by balance, so its even-parity bound 24 must be subtracted before averaging. Finally L is even for d≥1 and cannot exceed 2^d in magnitude. These observations prove (2), including U=V, zero T and all degenerate characters. ∎

For any local affine Boolean function ℓ(x₀+u)=η(u)+c, the exact Hamming distance is (2^d−(−1)^cL)/2. In particular, **every** affine 5-flat of an original object has both labels at least five times if T∈U, and at least four times if T∉U. For arbitrary local affine ℓ on a 5-flat, the distance is at least 4 when T∈U and η(T)=0, at least 2 when T∈U and η(T)=1, and at least 3 when T∉U. No flat or local function is selected.

## 3. Exact saturation coupling

For η≠0, if |L(F,η)|=B(U,η,T), equality in the average in (1) forces **every** global extension a∈A_η to have the same oriented sign W_f(a)(−1)^{a·x₀} and to attain its parity-specific bound: magnitude 24 at even-parity a and 28 at odd-parity a. Conversely, that simultaneous alignment makes |L|=B. When 2^d<B this case is simply impossible.

Consequently, for example as a universally quantified conditional statement, any 5-flat restriction at local affine distance exactly 2 must have T∈U, η(T)=1, and all sixteen global frequencies extending η at magnitude 28 with the stated coherent signs. This describes what **would** be required for equality; it neither chooses nor asserts an existing flat. The target remains open even if no equality occurs. ∎

## Scope and imports

The proof uses the supplied S1 definitions, elementary character orthogonality and the actual-object parity identity in `prerequisite-derivation-v1.md`, SHA-256 `075f61ffe1b5cfb000bb3bbda9ddd7fefea04e27806f19bedd9c5a2318fa3df9`, 87 LF. Main has notified that the v1 caller/mod-4 filters have same-harness written support; this later local restriction theorem is NOT thereby reviewed or adopted. No old proof/candidate/held source or selection/method guide is an input.

These are necessary local-global couplings, not sufficient 512-bit reconstruction conditions. The unrestricted balanced peak-28 witness-or-exclusion question, every rank/weight and `(24,24,2)` remain open. Book-source equivalence, independent full-scope review of this candidate, human, formal/kernel, executable and novelty gates remain unperformed. Prior exposure, the administrative metadata-poll MINOR, and all S1 STOP/HOLD/ZERO, N4 UNKNOWN and aux214 STOP remain binding.
