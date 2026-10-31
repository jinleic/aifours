# info-6: exact full-spectrum projective-code formulation and dual subset constraints

Owner **InfoBalancedNL242-2-2**, same original info-6 slot. Native `/bin/date` observed before write **2026-10-27T16:45:36-0700 PDT**. **AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** This direct, all-variable reformulation begins from the admitted Boolean/Walsh definitions; it is not an imported coding-theory result, a selected numerical probe, a new target, an actual witness or a no-go.

## Exact equivalence

The original existence question for a balanced nine-variable Boolean function with peak Walsh magnitude ≤28 is equivalent to existence of a binary linear code C of length 256 and dimension 9 with **256 distinct nonzero generator columns**, and with **every nonzero codeword** of weight in the closed interval [121,135]. Neither the generator-column condition nor the upper endpoint 135 may be dropped.

For a hypothetical Boolean witness, let D={x:f(x)=1}, so |D|=256. Since the complement of D is nonempty, every t outside D gives a translated witness f_t(x)=f(x+t) whose one-support D+t does not contain 0; this is an existential symmetry argument over all such t, not a selected state/probe. Translation multiplies Walsh coefficients by signs and preserves the bound. Take the 256 distinct nonzero points of D+t as the columns of a 9×256 binary matrix G and let c(a)=aᵀG. For every a≠0, direct character cancellation gives

    W_{f_t}(a)=4(w(c(a))−128).                                 (1)

The peak bound gives 121≤w(c(a))≤135, so c(a) is never zero for a≠0. Thus G has rank 9 and C={c(a):a∈F₂⁹} satisfies the claimed conditions.

Conversely, take the distinct nonzero generator columns of any such C as D, and define f=1_D on F₂⁹. Then f is balanced. The dimension guarantees c(a)≠0 for a≠0; (1) and the all-codeword weight window give |W_f(a)|≤28, while W_f(0)=0. This constructs a genuine original Boolean witness from any code satisfying **all** stated conditions. ∎

This is an exact existence equivalence, not an assertion that any such code exists. It does not discard any original function or rule out any rank/weight type: a no-go for the full code class would exclude the entire original target, including `(24,24,2)` if that type occurs. Translation is not claimed to preserve a particular earlier decomposition label.

## Necessary full weight-distribution and dual constraints

For such a code write A_t for the number of its nonzero codewords of weight 128+t, where −7≤t≤7. Because the columns are nonzero and pairwise distinct, linear orthogonality gives

    Σ_t A_t=511,    Σ_t t A_t=128,    Σ_t t² A_t=16384.          (2)

The parent-notified written-supported T≠0 and ≥92 peak results, with the mandatory count-direction correction, add

    Σ_{t odd} A_t=256,   Σ_{t even} A_t=255,
    A_{−7}+A_7≥92.                                               (3)

For each j=0,…,256 let D_j count weight-j vectors in C⊥, and let

    K_j(w)=Σ_{i=0}^j (−1)^i binom(w,i) binom(256−w,j−i).

Character orthogonality, summed over all j-subsets of column positions, proves the exact identities

    512 D_j = binom(256,j)+Σ_{t=−7}^7 A_t K_j(128+t).          (4)

Consequently every right side is a nonnegative multiple of 512. Distinct nonzero columns give D₁=D₂=0, and the parent-notified T≠0 gives D₂₅₆=0. These are necessary simultaneous conditions for one common code, not independent choices of dual data. They are not claimed sufficient for a code or for the Boolean witness.

As one explicit symbolic consequence, D₃ is exactly the number of unordered triples of distinct generator columns with XOR zero, and (2), (4), and |t|≤7 give

    Σ_t t³ A_t = 2²¹ − 384 D₃,        5163 ≤ D₃ ≤ 5760.       (5)

Indeed |Σ t³A_t|≤7Σ t²A_t=114688; the displayed integer bounds follow. This does not itself contradict existence. No spectrum, code, state, column, rank, direction or numerical test case was selected; (4) holds for **every** j at once.

## Provenance and remaining gap

This candidate uses only the original all-frequency character sum, whole 512-bit Boolean input, elementary linear orthogonality and the stated parent-notified bounds. It does not use the newly HELD cross-sector route or its consumers, any stopped half-split representation/transform, the stopped truth-degree/ANF method, L1 or any held/old source. The author cannot assert clean cognition. No external source, code execution, independent review, human, formal/kernel or novelty claim is made.

Live pre-write pins: `prerequisite-derivation-v1.md` SHA-256 `075f61ffe1b5cfb000bb3bbda9ddd7fefea04e27806f19bedd9c5a2318fa3df9`, 87 LF; `walsh-hyperplane-energy-v1.md` SHA-256 `6a1000f1c95ef4264e82fba6d229e59393241efaed367ee4d3e5687cec0f88a0`, 49 LF; `walsh-peak-multiplicity-v1.md` SHA-256 `8a64a73bc552f9e71cc04f07159c1f09feab17894d31966c16ebfe80d9fd37b8`, 28 LF; `walsh-support-xor-coupled-count-erratum-v1.md` SHA-256 `810e3e55c52288f252b335a776a134752702df33d70d8d689fb009aac127273c`, 30 LF. The original witness or unrestricted exclusion, book-source/novelty gates and all existing STOP/HOLD/ZERO/NONINPUT, L1 quarantine, w44 and count-direction overlays, N4 UNKNOWN and aux214 STOP remain binding.
