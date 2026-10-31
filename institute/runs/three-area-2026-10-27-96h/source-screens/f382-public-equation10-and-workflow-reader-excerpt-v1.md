# Primary reader excerpt: Eq10 and source workflow

URL: https://arxiv.org/html/2508.21348v2
Requested rendered-reader lines414–468, including reader-added context. Parent native observation before preservation: 2026-10-30T10:31:58-0700 PDT. Exact named workflow/map discussion only; no complete-paper, positivity or novelty certification. Reader response, not original HTML bytes.


### 4.2. The workflow

To summarize, we have a simple method to generate maps which are, by design, positive but not completely positive22 2 From here on out, when we use the term (kk-)positive we implicitly also mean that the map should not be completely positive.. All we need for it is a starting point, that is, one positive map which is not conditionally completely positive. But for now it is not even clear that such a map exists (recall the examples before Prop. [4](#Thmproposition4 "Proposition 4. ‣ 4.1. The theory ‣ 4. A new way to sample non-decomposable 𝑘-positive maps ‣ 𝑘-Positive Maps: New Characterizations and a Generation Method")).
The next most obvious pick would be the transposition map: For K=𝟏2K=\frac{\bf 1}{2}, this results in et⁡(T−id)=1+e−2​t2​id+1−e−2​t2​Te^{t(T-{\rm id})}=\frac{1+e^{-2t}}{2}{\rm id}+\frac{1-e^{-2t}}{2}T [[14](#bib.bib14), Ex. 6]. One might think that the trivial form of this semigroup is due to the poor choice of KK, and to some extent that is correct, but this example hints at a larger problem we have not considered so far: We wanted our method to generate non-decomposable positive maps; however, the set of decomposable maps satisfies all assumptions of Prop. [3](#Thmproposition3 "Proposition 3. ‣ 4.1. The theory ‣ 4. A new way to sample non-decomposable 𝑘-positive maps ‣ 𝑘-Positive Maps: New Characterizations and a Generation Method") (i.e., is a closed convex cone which is also a semigroup with identity, and contains all completely positive maps), as is readily verified. Hence, if the starting point Φ\Phi is decomposable, then the corresponding semigroup will always be decomposable, regardless of the chosen matrix KK. This insight rules out not only the transposition map as a starting point, but also the reduction map X↦tr⁡(X)​𝟏−XX\mapsto{\rm tr}(X){\bf 1}-X (its transpose is completely positive) [[30](#bib.bib30)].
Putting everything together, this lets us arrive at the definitive workflow of our new method.

###### Workflow 1.

1. (a)

   Start with a map Φ\Phi which is kk-positive, non-decomposable33 3 Strictly speaking, we need Φ\Phi to not be “conditionally decomposable”, i.e., there should not exist any K∈ℂd×dK\in\mathbb{C}^{d\times d} such that Φ−K⁡(⋅)−(⋅)​K†\Phi-K(\cdot)-(\cdot)K^{\dagger} is decomposable [[65](#bib.bib65), Thm. 3].
   However, unlike with conditional complete positivity we are not aware of a simple test for this, which is why we instead settle for the necessary condition of Φ\Phi being non-decomposable. , and not conditionally completely positive

2. (b)

   Generate a random matrix KK

3. (c)

   Compute et⁡(K⁡(⋅)+(⋅)​K†+Φ)e^{t(K(\cdot)+(\cdot)K^{\dagger}+\Phi)}. By (a), there exists t0>0t_{0}>0 such that this semigroup is kk-, but not completely positive for all t∈[0,t0)t\in[0,t_{0}) (and finding t0t_{0} is simple via the Choi matrix)

4. (d)

   Check that the semigroup is non-decomposable for small enough tt (this is an SDP, hence feasible to check, cf. Sec. [5.](#S5 "5. The PPT-square conjecture ‣ 𝑘-Positive Maps: New Characterizations and a Generation Method")).

5. (e)

   If the previous two points were successful, then we have found t0>0t_{0}>0 for which et0​(K⁡(⋅)+(⋅)​K†+Φ)e^{t_{0}(K(\cdot)+(\cdot)K^{\dagger}+\Phi)} is a non-decomposable kk-positive map. If we also check conditional complete positivity (and perhaps lower t0t_{0} accordingly), this map can be used as a new starting point for step (a).

The last point shows that this new method even has the potential to indefinitely produce new classes of non-decomposable positive maps.
This is in contrast to the only other method we are aware of to generate non-decomposable positive maps44 4 Here and henceforth, when we say non-decomposable we implicitly mean that the map should be positive, as well., which is to start from a kk-positive map Φ\Phi and tensor it with the kk-dimensional identity (i.e., idk⊗Φ{\rm id}_{k}\otimes\Phi is positive and non-decomposable) [[34](#bib.bib34)]; notably, this method only works once and it also changes the dimension, perhaps drastically, depending on kk.

All that is left now is to prove that this method works, i.e., we have to find a map which is neither decomposable nor conditionally completely positive, and then show that the corresponding semigroup is non-decomposable for small enough times. One of the very few papers we found which contains a map (or rather, a one-parameter family of maps) with these properties is [[5](#bib.bib5)]. Although going through Workflow [1](#Thmworkflow1 "Workflow 1. ‣ 4.2. The workflow ‣ 4. A new way to sample non-decomposable 𝑘-positive maps ‣ 𝑘-Positive Maps: New Characterizations and a Generation Method") with [[5](#bib.bib5), Eq. (1)] seems to always give something decomposable (recall footnote [3](#footnote3 "footnote 3 ‣ item a ‣ Workflow 1. ‣ 4.2. The workflow ‣ 4. A new way to sample non-decomposable 𝑘-positive maps ‣ 𝑘-Positive Maps: New Characterizations and a Generation Method")), we were able to slightly tweak the map in question such that our method works as intended. The map

|  | Λα′​(X)=1α+1α​(α⁡(x11+x22)x12α​x13x21x22+x33αx32α​x31x23α​x33+x11α)\Lambda_{\alpha}^{\prime}(X)=\frac{1}{\alpha+\frac{1}{\alpha}}\begin{pmatrix}\alpha(x_{11}+x_{22})&x_{12}&\alpha x_{13}\\\\ x_{21}&\frac{x_{22}+x_{33}}{\alpha}&x_{32}\\\\ \alpha x_{31}&x_{23}&\alpha x_{33}+\frac{x_{11}}{\alpha}\end{pmatrix} |  | (9) |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- |

is non-decomposable and not conditionally completely positive for all α∈(0,1]\alpha\in(0,1]. While the proof is analogous to the proof in [[5](#bib.bib5)], we nonetheless present the key arguments in Appendix D for the sake of completeness.

Here is the summary of the numerics we conducted with this map for the special case α=1\alpha=1:
First, when setting K=0K=0, the semigroup (et​Λ1′)t≥0(e^{t\Lambda_{1}^{\prime}})_{t\geq 0} crosses into the completely positive cone at t≈1.95t\approx 1.95 and, more importantly, is non-decomposable for all 0<t⪅0.440<t\lessapprox 0.44. When repeating this for randomly chosen KK the latter threshold fluctuated around ≈0.25−0.35\approx 0.25-0.35.
In a second step, we took Λ~:=e0.2​Λ1′\tilde{\Lambda}:=e^{0.2\Lambda_{1}^{\prime}} as the starting point for another iteration of Workflow [1](#Thmworkflow1 "Workflow 1. ‣ 4.2. The workflow ‣ 4. A new way to sample non-decomposable 𝑘-positive maps ‣ 𝑘-Positive Maps: New Characterizations and a Generation Method") and we found that, again for K=0K=0 for simplicity, the semigroup (et​Λ~)t≥0(e^{t\tilde{\Lambda}})_{t\geq 0} crosses into the completely positive cone at t≈7.7t\approx 7.7 and is non-decomposable for all 0<t⪅1.10<t\lessapprox 1.1 (resp. ⪅0.25−0.4\lessapprox 0.25-0.4 for random KK’s).
We tried this for a few more layers and found that this behavior continues, thus showing that this method can, with success, be used recursively.

Another advantage of ([9](#S4.E9 "In 4.2. The workflow ‣ 4. A new way to sample non-decomposable 𝑘-positive maps ‣ 𝑘-Positive Maps: New Characterizations and a Generation Method")) is
a rather simple idea behind it. Namely, transpose just a sub-block of the matrix and mix the diagonal, such that the resulting map is positive.
This allows for a generalization to higher dimensions (for simplicity for α=1\alpha=1 and d=4d=4): Φ:ℂ4×4→ℂ4×4\Phi:\mathbb{C}^{4\times 4}\to\mathbb{C}^{4\times 4}, with Φ⁡(X)\Phi(X) defined via

|  | 13​(x11+x22+x33x12x13x14x21x22+x33+x44x23x24x31x32x33+x44+x11x43x41x42x34x44+x11+x22)\frac{1}{3}{\small\begin{pmatrix}x_{11}+x_{22}+x_{33}&x_{12}&x_{13}&x_{14}\\\\ x_{21}&x_{22}+x_{33}+x_{44}&x_{23}&x_{24}\\\\ x_{31}&x_{32}&x_{33}+x_{44}+x_{11}&x_{43}\\\\ x_{41}&x_{42}&x_{34}&x_{44}+x_{11}+x_{22}\end{pmatrix}} |  | (10) |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | ---- |

is almost certainly55 5 Unlike with ([9](#S4.E9 "In 4.2. The workflow ‣ 4. A new way to sample non-decomposable 𝑘-positive maps ‣ 𝑘-Positive Maps: New Characterizations and a Generation Method")) we did not prove that ([10](#S4.E10 "In 4.2. The workflow ‣ 4. A new way to sample non-decomposable 𝑘-positive maps ‣ 𝑘-Positive Maps: New Characterizations and a Generation Method")) is positive. However, we numerically sampled five million vectors ϕ∈ℂ4\phi\in\mathbb{C}^{4} and verified that Φ⁡(|ϕ⟩​⟨ϕ|)≥0\Phi(|\phi\rangle\langle\phi|)\geq 0 every time. From this we conclude that with sufficiently high probability Φ\Phi is in fact positive. positive.
As in the previous case, we find that et​Φe^{t\Phi} is non-decomposable until t≈0.24t\approx 0.24.66 6 The code used to generate the maps is available in the ancillary files of the arXiv submission of the paper.

Finally, the only other paper we are aware of which features a positive map that is neither decomposable nor conditionally completely positive is [[47](#bib.bib47)], resp. [[58](#bib.bib58)] where it is generalized to arbitrary finite dimensions. From our testing, it also constitutes a viable input to Workflow [1](#Thmworkflow1 "Workflow 1. ‣ 4.2. The workflow ‣ 4. A new way to sample non-decomposable 𝑘-positive maps ‣ 𝑘-Positive Maps: New Characterizations and a Generation Method") (a) in that the corresponding semigroup is positive and non-decomposable for small enough times.

## 5. The PPT-square conjecture


[387 more lines in URL output. Use :472 to continue]
