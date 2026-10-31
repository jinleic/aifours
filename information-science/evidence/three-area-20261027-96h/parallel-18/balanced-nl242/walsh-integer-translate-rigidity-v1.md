# info-6: exact Boolean rigidity for integer combinations of all translates

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Actual `/bin/date` observed before this write: **2026-10-27T14:54:27-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** This is an all-variable conditional coupling, not a witness, global exclusion, rank/type restriction, numerical improvement, formal/kernel or novelty claim. No scientific program, selected-state probe or external-model review was used.

## Claim: actual Booleanity is equivalent to a common spectral support condition

Let f:F₂⁹→{0,1} be any balanced function. Its original sign and Walsh transform are s_f=(-1)^f and W_f. For an arbitrary finite number of translations t_i∈F₂⁹ and arbitrary integers c_i with Σ_i c_i=1, define

    g(x)=Σ_i c_i f(x+t_i),      C(a)=Σ_i c_i(-1)^{a·t_i}.          (1)

Then the following are equivalent:

1. g is an actual Boolean function at **every** x;
2. C(a)∈{−1,+1} at **every** frequency a for which W_f(a)≠0.

When they hold, g is balanced and |W_g(a)|=|W_f(a)| for every a. In particular, if f were an original balanced NL≥242 witness, so would g be. This is conditional and constructs no initial f.

## Proof

Because the c_i are integers with odd sum 1, g(x) is integer, s_g(x):=1−2g(x) is an odd integer, and C(a) is an odd integer. The sum condition gives the exact identity, before assuming g Boolean,

    s_g(x)=Σ_i c_i s_f(x+t_i),
    W_{s_g}(a)=C(a)W_f(a).                                       (2)

Orthogonality and Parseval give

    Σ_x[s_g(x)²−1] = (1/512)Σ_a W_f(a)²[C(a)²−1].                (3)

Every term on each side is nonnegative: odd integers have square at least 1. If g is Boolean, s_g(x)=±1, so the left side is zero and every nonzero W_f(a) forces C(a)²=1. Conversely, if the support condition holds, the right side is zero and every odd integer s_g(x) has square 1, so g(x)∈{0,1} for every x. In that case Σ_x s_g=Σ_i c_iΣ_x s_f=0, and (2) gives the same Walsh magnitudes at all frequencies. ∎

The result includes zero/duplicate/dependent translations, negative coefficients and cancellations: no generic-position or nonzero-support assumption is needed. It uses the common actual function f throughout; independently feasible translated marginals are not a substitute.

## Consequences for the original peak-28 scope

For an original candidate put k=W_f/4 and A_C={a:C(a)∈{−1,+1}}. The exact energy Σ_a k(a)²=2¹⁴, k(0)=0, and |k|≤7 show that any Boolean g of form (1) must satisfy the universal conditional obstruction

    49·|A_C\{0}| ≥ 2¹⁴.                                          (4)

This is quantified over **every** integer translation combination; it does not select or test one. Moreover, with T=Σ_{x:f(x)=1}x, the definition-first parity coupling gives two exhaustive possibilities:

- T≠0: every frequency with a·T=1 belongs to A_C, because k(a) is odd and hence nonzero there;
- T=0: every k(a) is even, so |k(a)|≤6 and the stronger conditional bound is 36·|A_C\{0}|≥2¹⁴.

These are necessary conditions on a transformation **if** an original witness f exists and its integer combination is Boolean. They do not establish the existence of a nontrivial combination, prohibit f itself, narrow the original target, or show the bounds are attained.

## Inputs and exact remaining gap

Inputs are the S1 packet and the all-variable character/Boolean facts derived in `prerequisite-derivation-v1.md`, SHA-256 `075f61ffe1b5cfb000bb3bbda9ddd7fefea04e27806f19bedd9c5a2318fa3df9`, 87 LF; elementary Parseval and integer parity are shown above. No prior-round Gate-I, author candidate, held source, method or selection guide was opened or used. Prior same-author exposure is preserved, not represented as blind or clean cognition.

The original unrestricted problem still requires an actual balanced peak≤28 f or a proof that **every** actual 512-bit candidate fails. Neither is supplied. Parent-authored definition-to-book equivalence, complete independent written review, human, formal/kernel, executable and novelty gates are not performed. S1 STOP/HOLD/ZERO/NONINPUT, N4 UNKNOWN and aux214 STOP remain binding.
