# info-6: simultaneous positive/negative support bounds in every Walsh phase

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Actual `/bin/date` observed before this write: **2026-10-27T14:57:12-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** It is a uniform necessary condition for an original object, not a witness, global exclusion, rank/type exclusion, numerical nonlinearity improvement, formal/kernel or novelty claim. No scientific program or selected state/frequency was probed.

## Claim

Suppose f is balanced on F₂⁹ with |W_f|≤28, and let k=W_f/4. For **every** x∈F₂⁹ define the two phase-modulated support sets

    P_x={a:k(a)(−1)^{a·x}>0},    N_x={a:k(a)(−1)^{a·x}<0}.

Then |P_x|,|N_x|≥159 simultaneously for all x. If T=Σ_{y:f(y)=1}y is zero, both bounds improve to 217; if T≠0, both improve to 165. Every x and both T alternatives remain in scope; no particular sign origin or special state is chosen.

## Proof

From the exact Boolean inverse, for every x,

    Σ_a k(a)(−1)^{a·x}=128·(-1)^{f(x)},   Σ_a k(a)²=2¹⁴.        (1)

Let A_x and B_x be the sums of positive and absolute negative modulated coefficients. Then |A_x−B_x|=128 and A_x+B_x=Σ_a|k(a)|. Since |k|≤7,

    A_x+B_x ≥ 2¹⁴/7,
    min(A_x,B_x) ≥ (2¹⁴/7−128)/2.

Every nonzero summand has magnitude at most 7, so |P_x|,|N_x| are each at least the ceiling of `(2¹⁴/7−128)/14`, namely 159. No assumption is made about the sign of the inverse at any x.

If T=0, the universal parity identity k(a) mod 2=a·T makes every nonzero coefficient even, with |k|≤6. The same argument gives min(A_x,B_x)≥(2¹⁴/6−128)/2 and hence at least the ceiling of `(2¹⁴/6−128)/12`, namely 217, in each set.

If T≠0, exactly 256 coefficients are odd, and each has square at most 49. Let E_even be the total square energy of the even coefficients. Then E_even≥2¹⁴−256·49. On odd and even coefficients separately,

    Σ_a|k(a)| ≥ (2¹⁴−E_even)/7+E_even/6 ≥ 2432.

Thus min(A_x,B_x)≥(2432−128)/2=1152, and division by the universal maximum 7 gives at least 165 coefficients of each sign. All identities and inequalities hold for every x simultaneously. ∎

## Status and exact gap

These bounds constrain the **same actual** phase array under every character modulation; they do not construct one or exclude all possibilities. Together with the independently unreviewed shift-cover candidate, they are necessary support/sign couplings, not sufficient conditions for the original Boolean inverse. The original question still needs an actual balanced peak-28 witness or a proof excluding every actual candidate, including all rank/weight and `(24,24,2)` alternatives.

Inputs are the S1 definition packet and the all-variable Boolean inverse/parity facts derived in `prerequisite-derivation-v1.md`, SHA-256 `075f61ffe1b5cfb000bb3bbda9ddd7fefea04e27806f19bedd9c5a2318fa3df9`, 87 LF. No old proof, candidate, held source, selection or method guide is an input. Parent-source/book equivalence, independent written review, human, formal/kernel, executable and novelty gates remain NOT PERFORMED. Prior author exposure, HOLD, all STOP/ZERO/NONINPUT, N4 UNKNOWN and aux214 STOP remain binding.
