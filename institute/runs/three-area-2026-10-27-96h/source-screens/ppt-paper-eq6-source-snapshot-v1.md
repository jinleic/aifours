# Public primary-source excerpt

Source: https://arxiv.org/html/2508.21348v2
Rendered source lines: 318-345
Purpose: Published Eq5–8 and free-marginal PPT relaxation
This is a bounded text excerpt, not an assertion about all versions, priority or complete-paper coverage.

In other words, the separability problem was implicitly hidden in the optimization’s feasible set. While, intuitively, this may be “how” the NP-hardness of entanglement detection translates to hardness of deciding (kk-)positivity, one has to be careful with such conclusions because for k=dk=d this argument somehow has to break down (as deciding complete positivity is certainly a lot simpler than deciding separability).

At point we want to stress that, unsurprisingly, Coro. [1](#Thmcorollary1 "Corollary 1. ‣ 3.3. Third condition: Connection to the separability problem ‣ 3. Novel characterizations of 𝑘-positivity ‣ 𝑘-Positive Maps: New Characterizations and a Generation Method") is not the only way to encode kk-positivity in a bilinear optimization problem: recall that Φ\Phi is positive if and only if tr⁡(𝖢⁡(Φ)​(ρ⊗ω))≥0{\rm tr}(\mathsf{C}(\Phi)(\rho\otimes\omega))\geq 0 for all states ρ,ω\rho,\omega (block positivity). Thus kk-positivity of a Hermitian-preserving linear map Φ:ℂd×d→ℂd×d\Phi:\mathbb{C}^{d\times d}\to\mathbb{C}^{d\times d} is equivalent to

|  | minρ,ω∈𝔻⁡(ℂd⊗ℂk)⁡tr⁡(𝖢⁡(Φ⊗idk)​(ρ⊗ω))≥0.\min_{\rho,\omega\in\mathbb{D}(\mathbb{C}^{d}\otimes\mathbb{C}^{k})}{\rm tr}(\mathsf{C}(\Phi\otimes{\rm id}_{k})(\rho\otimes\omega))\geq 0\\,. |  | (5) |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- |

One reason these bilinear formulations are interesting is that there already exist tools to compute them numerically.
Aside from the well-established seesaw method or branch-and-bound algorithms [[35](#bib.bib35)], another way to tackle this is via SDP hierarchies for bilinear optimization problems [[3](#bib.bib3)].
In fact, applying the first level of the hierarchy in [[3](#bib.bib3), Thm. 3.1] (with the PPT condition PT1≥0P^{T_{1}}\geq 0 included)
to the optimization problem in ([5](#S3.E5 "In 3.3. Third condition: Connection to the separability problem ‣ 3. Novel characterizations of 𝑘-positivity ‣ 𝑘-Positive Maps: New Characterizations and a Generation Method")) yields the quantity

|  | F(Φ):=minP∈ℙ⁡(ℂd​k⊗ℂd​k)ρ∈𝔻⁡(ℂd⊗ℂk)ω∈𝔻⁡(ℂd⊗ℂk){tr(𝖢(Φ⊗idk)P):tr1(P)=ω,tr2(P)=ρ,PT1≥0},F(\Phi):=\min_{\begin{subarray}{c}P\in\mathbb{P}(\mathbb{C}^{dk}\otimes\mathbb{C}^{dk})\\\\ \rho\in\mathbb{D}(\mathbb{C}^{d}\otimes\mathbb{C}^{k})\\\\ \omega\in\mathbb{D}(\mathbb{C}^{d}\otimes\mathbb{C}^{k})\end{subarray}}\Big\\{{\rm tr}(\mathsf{C}(\Phi\otimes\text{id}_{k})P):{\rm tr}_{1}(P)=\omega,\\\\[-25.00003pt] {\rm tr}_{2}(P)=\rho,\\,P^{T_{1}}\geq 0\Big\\}, |  | (6) |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- |

where ℙ\mathbb{P} denotes the set of positive semi-definite linear operators, and (⋅)T1=(T⊗id)​(⋅)(\cdot)^{T_{1}}=(T\otimes{\rm id})(\cdot) is the partial transpose over the first subsystem. In fact, by making the key observation that

|  | F⁡(Φ)≤minρ,ω∈𝔻⁡(ℂd⊗ℂk)⁡tr⁡(𝖢⁡(Φ⊗idk)​(ρ⊗ω))F(\Phi)\leq\min_{\rho,\omega\in\mathbb{D}(\mathbb{C}^{d}\otimes\mathbb{C}^{k})}{\rm tr}(\mathsf{C}(\Phi\otimes{\rm id}_{k})(\rho\otimes\omega)) |  | (7) |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- | --- |

(because F⁡(Φ)F(\Phi) involves a minimization with respect to a set that contains the optimization domain of ([5](#S3.E5 "In 3.3. Third condition: Connection to the separability problem ‣ 3. Novel characterizations of 𝑘-positivity ‣ 𝑘-Positive Maps: New Characterizations and a Generation Method"))), this leads to the following sufficient condition for a Hermitian-preserving linear map Φ\Phi to be kk-positive:
If F⁡(Φ)≥0F(\Phi)\geq 0, then Φ\Phi is kk-positive, because then

|  | minρ,ω∈𝔻⁡(ℂd⊗ℂk)⁡tr⁡(𝖢⁡(Φ⊗idk)​(ρ⊗ω))≥F⁡(Φ)≥0,\min_{\rho,\omega\in\mathbb{D}(\mathbb{C}^{d}\otimes\mathbb{C}^{k})}{\rm tr}(\mathsf{C}(\Phi\otimes{\rm id}_{k})(\rho\otimes\omega))\geq F(\Phi)\geq 0\\,, |  | (8) |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- |

i.e., ([5](#S3.E5 "In 3.3. Third condition: Connection to the separability problem ‣ 3. Novel characterizations of 𝑘-positivity ‣ 𝑘-Positive Maps: New Characterizations and a Generation Method")) holds.
To be transparent, when doing a numerical study of this sufficient condition (i.e., generating random Hermitian matrices and checking the condition in ([8](#S3.E8 "In 3.3. Third condition: Connection to the separability problem ‣ 3. Novel characterizations of 𝑘-positivity ‣ 𝑘-Positive Maps: New Characterizations and a Generation Method"))), we only found decomposable positive maps that this sufficient criterion could detect as positive, among several thousand trials. Whether this has to do with our underlying sampling method, or whether including the PPT condition PT1≥0P^{T_{1}}\geq 0 somehow tailors this condition more towards detecting decomposable maps, is unclear to us. The code used to implement the optimization in ([6](#S3.E6 "In 3.3. Third condition: Connection to the separability problem ‣ 3. Novel characterizations of 𝑘-positivity ‣ 𝑘-Positive Maps: New Characterizations and a Generation Method")) can be found in the ancillary files of the arXiv submission of this paper.

## 4. A new way to sample non-decomposable kk-positive maps

With this, let us return to the other question raised in the introduction: How can one numerically sample kk-positive11 1 For simplicity we will drop the “kk-” and focus on positive maps, but we stress that the method presented in this section works exactly the same for kk-positivity. maps?

[510 more lines in URL output. Use :349 to continue]
