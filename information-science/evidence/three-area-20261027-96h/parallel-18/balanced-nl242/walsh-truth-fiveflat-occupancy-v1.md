# info-6: every truth-space affine five-flat contains at least five of each truth value

Owner **InfoBalancedNL242-2-2**, same original info-6 slot. Native `/bin/date` observed before this write **2026-10-27T16:48:37-0700 PDT**. **AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** The claim and equality analysis quantify over **every** affine five-flat and all 512 Boolean inputs; no flat, direction, truth table, extremal instance or numerical boundary probe is selected.

## Claim

Let f be any balanced nine-variable Boolean function with Walsh peak ≤28, and let D={x:f(x)=1}. Then, for every affine five-dimensional subspace F of F₂⁹,

    5 ≤ |D∩F| ≤ 27.                                             (1)

In particular both truth values occur at least five times in every such 32-point flat. This is a universal necessary occupancy condition; it neither constructs f nor excludes all possible D.

## Whole-array restriction identity and the elementary bound

Write k=W_f/4 and T=⊕_{x∈D}x. The parent-notified caller and T≠0 result give

    k(a) mod 2=a·T,      k(a+b)−k(a)−k(b) ≡ 2𝔅(a,b) (mod 4),

with one symmetric F₂-bilinear 𝔅, and |k(a)|≤7. Let F=x₀+U be an arbitrary five-flat; A=U⊥ has dimension four. The indicator expansion of an affine subspace, applied to the original whole truth table, yields

    |D∩F| = 16 − (1/8) Σ_{a∈A\{0}} (−1)^{a·x₀} k(a).          (2)

If T∈U, all 15 nonzero a∈A have even k(a), hence |k(a)|≤6. Equation (2) and integrality give 5≤|D∩F|≤27.

If T∉U, the kernel E={a∈A:a·T=0} has dimension three. There are seven nonzero even coefficients of magnitude at most six and eight odd coefficients of magnitude at most seven, so the absolute sum in (2) is at most 7·6+8·7=98. Integrality first gives 4≤|D∩F|≤28. It remains to rule out both equality values **for every F**, without evaluating any particular F.

## Universal exclusion of equality 4 or 28

Suppose |D∩F|=4 or 28. The signed sum in (2) is respectively 96 or −96. Choose a symbolic sign σ∈{±1} making its signed value +96. For a∈A\{0}, write u_a=σ(−1)^{a·x₀}k(a), and set M_a=6 for a∈E\{0} and M_a=7 for a∈A\E. Each M_a−u_a is a nonnegative even integer; their sum is 98−96=2. Hence exactly one coefficient has a deficit 2 and all other 14 attain their respective maxima.

On E put q(h)=k(h)/2 mod 2; q(0)=0. Dividing the global mod-4 identity by two shows that q is a quadratic function on the three-dimensional E, with polar 𝔅|E. Its sum over all eight h∈E is 0 mod 2: in any basis, each linear term occurs four times and each bilinear term twice.

If the unique deficit is at an odd coefficient, every one of the seven nonzero even coefficients has magnitude six. Thus q=1 at all seven nonzero points, contradicting the even parity just proved.

Otherwise the unique deficit is at an even coefficient. Its absolute value is four; the other six nonzero even coefficients have magnitude six. Thus q has exactly six ones on E. On the other hand, **all eight** odd coefficients have magnitude seven and have signs σ(−1)^{a·x₀}, an affine character on their E-coset. For odd a define Q(a)=(k(a)−1)/2 mod 2. At a peak, Q is the indicator of positive sign, so Q is affine on this entire coset. The second derivative of Q in any directions u,v∈E is 𝔅(u,v); hence 𝔅|E=0. Then q is linear on E and has either zero or four ones, not six. This is a contradiction.

Both equality cases are impossible, proving (1). ∎

## Scope, controls and inputs

The proof is a direct character expansion on an arbitrary four-dimensional normal subspace, plus the already-supported pointwise global mod-4 identity. It does not form, transform or decompose complementary frequency sectors, choose a sample/boundary instance, use truth-degree/ANF, the stopped half-split/canonical branch, the newly HELD post-052 cross-sector route or any of their consumers. It uses no executable mathematics or external source; no clean-cognition assurance is inferred.

Pre-write live pins: `prerequisite-derivation-v1.md` SHA-256 `075f61ffe1b5cfb000bb3bbda9ddd7fefea04e27806f19bedd9c5a2318fa3df9`, 87 LF; `walsh-support-xor-obstruction-v1.md` SHA-256 `380655caaa06ea27e4236070ff66e070be63963960efebfabef2e730d2091fc4`, 49 LF; mandatory `walsh-support-xor-coupled-count-erratum-v1.md` SHA-256 `810e3e55c52288f252b335a776a134752702df33d70d8d689fb009aac127273c`, 30 LF; `walsh-projective-code-equivalence-v1.md` SHA-256 `b68e9f6bc546872e96066625ebfb7872f92f7a78d0187e9fa1925045148dbfeb`, 50 LF, author-only and not needed for the proof. The original witness-or-unrestricted-exclusion, all ranks/weights including `(24,24,2)`, book-source/novelty gate, independent review, human and formal/kernel status remain open. Parent PROCESS MAJOR overlay, L1 quarantine, earlier STOP/HOLD/ZERO/NONINPUT, w44/count-direction corrections, N4 UNKNOWN and aux214 STOP remain binding.
