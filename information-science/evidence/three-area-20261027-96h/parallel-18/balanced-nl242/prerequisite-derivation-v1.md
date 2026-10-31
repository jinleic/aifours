# info-6: the all-variable Walsh interface and a universal mod-4 coupling

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Actual `/bin/date` observed before this write: **2026-10-27T14:41:38-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** It is not a witness, unrestricted exclusion, numerical improvement, novelty result, formal/kernel or executable verification. No scientific program, selected-state probe or external-model review was used.

## Input and exposure boundary

Inputs are only the complete literal S1 controls and definition packet, S0/current contract/own safe intake, and elementary finite character orthogonality, integer parity and linear algebra stated below. The pre-body exposure ACK `walsh-prebody-exposure-ack-v1.json`, SHA-256 `898ba93798558013d89232e6ddabb9e99d6cf16ebc0199088481639afe4f6c2d`, 19 LF, was written before this derivation. Prior same-author exposure cannot be erased; no clean-cognition or independent-reconstruction assertion is made. No old Gate-I body, old author candidate, HELD/ZERO source, scout, selection or method guide is an input.

The supplied Main-authored definitions fix the literal problem but do **not** certify verbatim book/source equivalence. A separately pinned primary-source comparison remains NOT PERFORMED. All arguments below are from those supplied definitions and ordinary elementary facts; all original ranks, weights and `(24,24,2)` alternatives remain unrestricted.

## 1. Exact sign/Walsh and Boolean caller

Put V=F₂⁹, χ_a(x)=(-1)^{a·x}, s(x)=(-1)^{f(x)}, and

    W(a)=Σ_{x∈V} s(x)χ_a(x),      a∈V.

Character orthogonality is Σ_{a∈V}χ_a(x+y)=512·1_{x=y}, giving the inverse

    s(x)=(1/512)Σ_{a∈V}W(a)χ_a(x)                              (all x∈V).    (1)

For every affine Boolean function ℓ_{a,c}(x)=a·x+c,

    d_H(f,ℓ_{a,c})=256−(1/2)(−1)^c W(a),
    NL(f)=256−(1/2)max_{a∈V}|W(a)|.                             (2)

Balance is W(0)=0. Thus the requested witness is exactly an actual sign function with W(0)=0 and |W(a)|≤28 at **every** frequency. Formula (1) preserves every one of the 512 Boolean inverse values; it is not a real-spectrum relaxation.

For a balanced f, let M={x:f(x)=1}, so |M|=256, and n_a=|{x∈M:a·x=1}|. For **all** a, including a=0,

    W(a)=512·1_{a=0}−512+4n_a,    k(a):=W(a)/4∈Z.               (3)

Consequently k(0)=0 and |k(a)|≤7 in any requested witness. The zero-frequency correction in (3) is essential for the actual caller; it is not silently dropped.

## 2. Exact global autocorrelation coupling — forward and converse

The original witness exists if and only if there is an integer array k:V→Z satisfying

    k(0)=0,   |k(a)|≤7 for every a,
    Σ_{a∈V} k(a)k(a+b)=2¹⁴·1_{b=0} for every b∈V.              (4)

**Forward.** Apply character orthogonality to W=4k and use s(x)²=1. All shifts b, including b=0, are included; b=0 is the full energy constraint.

**Converse.** Given k satisfying (4), define s(x)=(1/128)Σ_a k(a)χ_a(x). Fourier transforming the shift equations gives (Σ_a k(a)χ_a(x))²=2¹⁴ for every x, hence s(x)∈{±1} for **every** x. Define the actual Boolean f(x)=(1−s(x))/2. Orthogonality gives its Walsh spectrum W=4k, so k(0)=0 gives balance and |k|≤7 gives the original NL threshold by (2). No independent choice of 512 inverse signs, rank, zero-frequency value or omitted inverse-integrality condition is allowed. Conversely no positive-rank or nondegenerate hypothesis was used. ∎

The family (4) couples the entire spectrum: a list of feasible one-frequency magnitudes or separately feasible partial profiles is not enough. A failure of any one universally quantified shift equation excludes the entire proposed array as an actual Boolean witness; satisfying energy alone is not asserted sufficient.

## 3. Universal mod-4 coupling of **all** frequencies

Choose an arbitrary basis of V. For the same actual M define the moment residues

    A_i=Σ_{x∈M}x_i (mod 4),     B_ij=Σ_{x∈M}x_i x_j (mod 2),  i<j.

For bits u_i, the exact XOR identity modulo 4 is

    u₁⊕⋯⊕u₉ ≡ Σ_i u_i − 2Σ_{i<j}u_i u_j (mod 4).

Using (3), including a=0 because its correction is a multiple of 4, gives the **same** coefficients A_i,B_ij simultaneously for every frequency:

    k(a) ≡ Σ_i A_i a_i − 2Σ_{i<j} B_ij a_i a_j (mod 4).         (5)

In particular, if T=Σ_{x∈M}x∈V, then for all a

    k(a) mod 2 = a·T.                                            (6)

Thus the odd-coefficient support is either empty (T=0) or the entire affine hyperplane {a:a·T=1} (T≠0); no other odd-support shape can come from a balanced Boolean object. Both alternatives and all possible T are retained. This is a universal coupling obstruction on any proposed spectrum, not a choice of a particular T, frequency or test function.

Coordinate-free, with Δ_h q(a)=q(a+h)−q(a) in Z/4Z, (5) implies

    Δ_u Δ_v Δ_w k(a) ≡ 0 (mod 4)                                (7)

for every a,u,v,w∈V, including zero and dependent increments. Equivalently there is a symmetric F₂-bilinear form B such that

    k(a+b)−k(a)−k(b) ≡ 2B(a,b) (mod 4),   B(a,a)=a·T.           (8)

For example, one expression in the arbitrary basis is B(a,b)=Σ_i(A_i mod 2)a_i b_i + Σ_{i<j}B_ij(a_i b_j+a_j b_i). This follows from the integer XOR identity; no rank classification or restricted residue type is assumed. When T=0, k/2 mod 2 is a Boolean quadratic function, but the T≠0 branch is equally part of the result. The A_i,B_ij in (5) come from **one actual M**; treating them as unrelated independently feasible moments is not justified.

Finally, under the peak bound, let E₂ count frequencies with |k|∈{2,6}, and O₃ count those with |k|∈{3,5}. Equation (4) at b=0, reduced modulo 16, together with (6) yields the global magnitude constraint

    E₂ + 2O₃ ≡ 0 (mod 4).                                       (9)

Indeed the odd support has size either 0 or 256; odd squares are 1 or 9 mod 16 and the indicated even squares are 4 mod 16. This is another simultaneous necessary filter, not a proof that any admissible counts are realizable. ∎

## 4. Exact status and first unproved step

The new content is the universal actual-object coupling (5)–(9), applied to **all** frequencies and both parity branches, together with the converse caller (4). An abstract integer profile that fails (6), (7), (8) or (9) cannot be the Walsh array of a balanced Boolean object. The converse of these residue/magnitude filters is **not established**: satisfying them does not supply the exact global autocorrelations in (4), the same 512 inverse bits, or a witness. No assertion is made that an apparently feasible relaxation actually exists or that it fails.

The next substantive open implication is to prove, for every possible moment-coupled mod-4 profile, that the bounded integer array equations (4) either cannot all hold, **or** to exhibit an actual array and replay the mathematical caller in (1)–(2). Neither alternative is achieved here. In particular there is no exclusion of any full rank/weight or of the `(24,24,2)` alternative, no balanced NL242 witness, no unrestricted upper bound and no novelty/priority claim. Book/source equivalence, full-scope independent written review, formal/kernel, executable and human gates remain separate and unperformed. The old L≥18/L≥12 author chains and all held guidance remain NONINPUT.
