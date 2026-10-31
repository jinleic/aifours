# Public primary-source excerpt

Source: https://arxiv.org/html/2509.07086v1
Rendered source lines: 108-145
Purpose: Theorem2 one-local-dimension Schmidt-number loss and Schur proof
This is a bounded text excerpt, not an assertion about all versions, priority or complete-paper coverage.


For a given unnormalized state ρc\rho_{c} in m×nm\times n, which we call a core state, we say that ρ\rho is its (δA,δB)(\delta_{\mathrm{A}},\delta_{\mathrm{B}})-extension, if ρc⊂Lρ\rho_{c}\subset_{\mathrm{L}}\rho in (m+δA)×(n+δB)(m+\delta_{\mathrm{A}})\times(n+\delta_{\mathrm{B}}), with δA,δB∈ℕ\delta_{\mathrm{A}},\delta_{\mathrm{B}}\in\mathbbm{N}.
In what follows, we study the (1,0)(1,0)-extensions, if not further specified, i.e. subsystem A\mathrm{A} is extended by adding a state |⊥⟩\ket{\bot} to ℂm\mathbbm{C}^{m}.
This adds a new diagonal block supported on |⊥⟩⊗ℂn\ket{\bot}\otimes\mathbbm{C}^{n}, referred to as ρe\rho_{e}, and new off-diagonal elements χ∈ℬ⁡(ℂn,ℂm⊗ℂn)\chi\in\mathcal{B}(\mathbbm{C}^{n},\mathbbm{C}^{m}\otimes\mathbbm{C}^{n}). Hence, the full local extension may be written as unnormalized state,

|  | ρ=ρc+χ​⟨⊥\|+\|⊥⟩​χ†+\|⊥⟩​⟨⊥\|⊗ρe=(ρcχχ†ρe).~\hskip-4.26773pt\rho=\rho_{c}+\chi\bra{\bot}+\ket{\bot}\chi^{\dagger}+\ket{\bot}\bra{\bot}\otimes\rho_{e}=\begin{pmatrix}\rho_{c}&\chi\\\\ \chi^{\dagger}&\rho_{e}\end{pmatrix}. |  | (3) |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- |

Since we require that local extensions ρ≥0\rho\geq 0, we learn the relations between ranges, R⁡(χ)⊆R⁡(ρc)R(\chi)\subseteq R(\rho_{c}), and R⁡(χ†)⊆R⁡(ρe)R(\chi^{\dagger})\subseteq R(\rho_{e}). Furthermore, by the (generalized) Schur complement ρe\c≡ρe−χ†​ρc−1​χ≥0\rho_{e\backslash c}\equiv\rho_{e}-\chi^{\dagger}\rho_{c}^{-1}\chi\geq 0 and ρc\e≡ρc−χ​ρe−1​χ†≥0\rho_{c\backslash e}\equiv\rho_{c}-\chi\rho_{e}^{-1}\chi^{\dagger}\geq 0. See SM [B](#A2 "Supplementary Material B Convex geometry of PSD local extensions ‣ Scaling Bound Entanglement through Local Extensions") and [C](#A3 "Supplementary Material C Convex geometry of PPT local extensions ‣ Scaling Bound Entanglement through Local Extensions") for a more detailed discussion of the convex geometry of local extensions.
We are ready to formulate a strengthened version of Observation [1](#Thmobservation1 "Observation 1. ‣ Scaling Bound Entanglement through Local Extensions"):

###### Theorem 2.

Let ρ∈ℬ⁡(ℋA⊗ℋB)\rho\in\mathcal{B}(\mathcal{H}_{\mathrm{A}}\otimes\mathcal{H}_{\mathrm{B}}) and |ϕ⟩∈ℋA\ket{\phi}\in\mathcal{H}_{\mathrm{A}}. Then, the Schmidt number SN⁡((A⊗𝟙)​ρ​(A†⊗𝟙))\mathrm{SN}{((A\otimes\mathbb{1})\rho(A^{\dagger}\otimes\mathbb{1}))} drops at most by 11, compared to SN⁡(ρ)\mathrm{SN}(\rho), if A=𝟙−|ϕ⟩⟨ϕ|A=\mathbb{1}-\outerproduct{\phi}{\phi}.

The above statement can be reversed to refer to local extensions, yielding: A (1,0)(1,0)-extension cannot increase the Schmidt number by more than one. This leads to an immediate observation that

###### Observation 3.

Any 3×43\times 4 PPT state ρ~\tilde{\rho} with a product vector |α​β⟩\ket{\alpha\beta} in its kernel has Schmidt number at most 22.

To see this, project ρ~\tilde{\rho} on a 2×42\times 4 block which contains the product state |α​β⟩\ket{\alpha\beta}. Then the resulting state is PPT with the product vector in its kernel. Such states are known to be separable by Ref. [[45](#bib.bib45)]. Theorem [2](#Thmobservation2 "Theorem 2. ‣ Scaling Bound Entanglement through Local Extensions") then implies that ρ~\tilde{\rho} has Schmidt number at most 22.
We now prove Theorem [2](#Thmobservation2 "Theorem 2. ‣ Scaling Bound Entanglement through Local Extensions") (See Supplemental material (SM) [A](#A1 "Supplementary Material A Proof for the Schur-complement peel-off theorem ‣ Scaling Bound Entanglement through Local Extensions") for the equivalent statement in terms of kk-positive maps).

###### Proof.

We use the notation in Eq. ([3](#S0.E3 "In Scaling Bound Entanglement through Local Extensions")). We show that for any conic decomposition of ρc\rho_{c} into vectors {|ψic⟩}i<N\\{\ket{\psi^{c}_{i}}\\}_{i<N} we can induce a conic decomposition ρ=∑i|ψ~i⟩​⟨ψ~i|+ρsep\rho=\sum_{i}\ket{\tilde{\psi}_{i}}\bra{\tilde{\psi}_{i}}+\rho^{\mathrm{sep}}, with SR⁡(|ψ~i⟩)≤SR⁡(|ψic⟩)+1\mathrm{SR}(\ket{\tilde{\psi}_{i}})\leq\mathrm{SR}(\ket{{\psi}^{c}_{i}})+1 and a separable ρsep\rho^{\mathrm{sep}},
with the following ansatz:

|  | \|ψ~i⟩=ρ​(ρc−1​\|ψic⟩0)=(\|ψic⟩χ†​ρc−1​\|ψic⟩)∈R⁡(ρ),\ket{\tilde{\psi}_{i}}=\rho\begin{pmatrix}\rho_{c}^{-1}\ket{\psi^{c}_{i}}\\\\ 0\end{pmatrix}=\begin{pmatrix}\\,\ket{\psi^{c}_{i}}\\\\ \chi^{\dagger}\rho_{c}^{-1}\ket{\psi^{c}_{i}}\end{pmatrix}\in R(\rho), |  | (4) |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- |

|  | ρ~≡∑i\|ψ~i⟩​⟨ψ~i\|=(ρcχχ†χ†​ρc−1​χ),\displaystyle\tilde{\rho}\equiv\sum_{i}\ket{\tilde{\psi}_{i}}\bra{\tilde{\psi}_{i}}=\begin{pmatrix}\rho_{c}&\chi\\\\ \chi^{\dagger}&\chi^{\dagger}\rho_{c}^{-1}\chi\end{pmatrix}, |  | (5) |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- |

where ρc−1\rho_{c}^{-1} is the pseudoinverse and we used identity ρc​ρc−1​|ψic⟩=|ψic⟩\rho_{c}\rho_{c}^{-1}\ket{\psi^{c}_{i}}=\ket{\psi^{c}_{i}} and the identity ρc​ρc−1​χ=χ\rho_{c}\rho_{c}^{-1}\chi=\chi.
Using the Schur complement, we see that ρ−ρ~=ρe\c⊗|⊥⟩⟨⊥|≥0\rho-\tilde{\rho}=\rho_{e\backslash c}\otimes\outerproduct{\bot}{\bot}\geq 0, is
trivially separable and, thus, can be added to ρ~\tilde{\rho} without increasing its Schmidt number. Also, SR⁡(|ψ~i⟩)≤1+SR⁡(|ψic⟩)\mathrm{SR}(\ket{\tilde{\psi}_{i}})\leq 1+\mathrm{SR}(\ket{\psi^{c}_{i}}) , as SR⁡(|ψ~i⟩−|ψic⟩)≤1\mathrm{SR}(\ket{\tilde{\psi}_{i}}-\ket{{\psi}^{c}_{i}})\leq 1. Now suppose that SR⁡(|ψic⟩)≤k\mathrm{SR}(\ket{\psi^{c}_{i}})\leq k, and that this is the minimum kk for which a decomposition exists. Then, Theorem [2](#Thmobservation2 "Theorem 2. ‣ Scaling Bound Entanglement through Local Extensions") follows automatically. ∎

Results on PPT local extensions –
Every PPT state permits PPT local extensions, but we are interested in those that may increase the Schmidt number. Local extensions obtained by SLOCC operations, given by SA∈ℬ⁡(ℋA,ℋA⊕|⊥⟩)S_{\mathrm{A}}\in\mathcal{B}(\mathcal{H}_{\mathrm{A}},\mathcal{H}_{\mathrm{A}}\oplus\ket{\bot}), where |ϕ⟩∈ℋA\ket{\phi}\in\mathcal{H}_{\mathrm{A}},


[451 more lines in URL output. Use :149 to continue]
