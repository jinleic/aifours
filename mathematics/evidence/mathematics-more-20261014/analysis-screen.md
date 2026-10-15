I screened all nine assigned articles. Only one exact book question is still open and has a concrete route: hot spots question (ii), and only part of it remains. Smooth domains are claimed by openai/math family 369, which has not been re-verified. What remains is the non-smooth Lipschitz case. No second article gives an exact, unresolved question with a credible full route. I wrote no files, ran no builds, tests or model CLIs, and used no git.

## Summary

- **Solved or settled**
  - Hot spots (i), Kawohl's conjecture, is false as stated: there are counterexamples in high dimensions.
  - Topological similarity of periodic matrices is solved by Hambleton–Pedersen, which is the book's own reference [5].
  - Sierpiński carpet questions (1) and (3) are answered analytically by Grigor'yan–Yang.
- **Still open, with a primary source saying so, but out of reach:** Veech/Katznelson, McMullen's conjecture beyond the disjoint type, M3⇒M1, and Getoor's conjecture.
- **Not precisely posed:** 2D instantaneous frequency, Hunt questions 1 and 2, the SDE "Sobolev conditions" question, and the loop-group "convex functional / gradient flow" question.
- **Hot spots (ii), what remains:** Rauch's strict form (HS1) on bounded, simply connected, non-smooth Lipschitz planar domains. Two pieces are missing: strictness, and the case where the first positive eigenvalue is double. Burdzy's Remark 7.1 explicitly says his argument does not cover every eigenfunction in the double case.

## Files

- `/tmp/math10000_full.txt`: the nine articles. Key question lines are 7536–7538, 7586–7587, 8592–8593, 8614–8617, 9450–9456, 9511–9514, 10471–10472, 10488–10491, 13931–13934, 14034–14035, 14056–14058, 14353, 14379–14402 and 14421–14423.
- `ai4s/README.md:62-163`: earlier coverage. None of these nine were screened before.
- `math/CONTENTS.md:8956,8963-8965`; `math/lean/docs/369.md`: family 369 and its preprint, dated 2026-09-24.
- `math/lean/ComparatorChallenges/HotSpots.{lean,json}`: the Comparator statement (`SmoothBoundary`, `AdmissibleDomain`, `InFirstNeumannEigenspace`, `MainConclusion`).
- `math/lean/OAI/Analysis/HotSpots/Main.lean:78-80`: `main_theorem`. A grep of `OAI/Analysis/HotSpots/` found no `sorry`, `admit` or `axiom`. I did not replay it.
- OAI preprint `build/sections/`:
  - `01-introduction.tex:36,65`: the proof starts from Rohleder's principle and uses smooth-boundary regularity.
  - `02-preliminaries.tex:78-81`: the eigenspace has dimension at most 2 (citing Nadirashvili 1988 and Bañuelos–Burdzy 1999).
  - `06-conclusion.tex:42-58`: the two-case contradiction.
- `ai4s/evidence/mathematics-intake/hmz-lean-verification/harness/`: the existing Comparator harness.

## Architecture (hot spots evidence chain)

The OAI smooth theorem (no interior critical points, multiplicity allowed) is the input. Burdzy approximates the domain from inside by conformal images of smaller concentric disks. Interior estimates make the approximating eigenfunctions converge locally uniformly. For a simple eigenvalue this gives the non-strict conclusion. The steps below add strictness, the symmetric double case, and the remaining double case.

## Report

### A. Screen of the nine articles

PDF page = book page + 16.

| Article (book pp. / PDF pp.) | Exact question | Status and primary source | Disposition |
|---|---|---|---|
| 广义度量空间 211–212 / 227–228 | "是否每个 M3 空间都是 M1 空间？" (7536–7538) | Declared open in [Gruenhage's survey](http://webhome.auburn.edu/~gruengf/papers/genmetricfinalb.pdf), which predates the claim below. Unaccepted negative claim: [Chen–Wang arXiv:1809.03763](https://arxiv.org/abs/1809.03763); I found no citing work. | Famous and hard. Optional audit only. |
| 矩阵拓扑相似 213–214 / 229–230 | "如何完全刻画拓扑相似的周期矩阵" (7586–7587) | Solved: [Hambleton–Pedersen](https://arxiv.org/abs/math/0109036), "we solve a problem of De Rham" with an effective necessary-and-sufficient condition, plus a complete classification for 2-power orders. | Excluded as solved. |
| 2D 瞬时频率 245–248 / 261–264 | Criteria ①–④ for a definition (8614–8617) | Criteria ② and ③ ("physical meaning", "mode mixing not too serious") are informal. | Excluded: not precisely posed. |
| Sierpiński 狄氏型 268–269 / 284–285 | (1) analytic construction; (2) domain and walk dimension; (3) heat-kernel estimates (9450–9456) | [Grigor'yan–Yang arXiv:1706.03318](https://arxiv.org/abs/1706.03318) give a "purely analytic construction". They identify the domain as a Besov space with β\* = log(8ρ)/log 3, and give an analytic sub-Gaussian heat-kernel proof (Thm 2.8). They state that ρ's "exact value remains still unknown". | (1) and (3) solved. (2)'s exact walk dimension has no route. |
| Sierpiński 双曲分支 270–271 / 286–287 | "H(f) ⊂ M_d 是紧集吗?" (9511–9514) | Read literally the answer is trivially no: H(f) is a nonempty open proper subset of the connected M_d. The intended question is boundedness. [Dudko–Luo arXiv:2509.25658](https://arxiv.org/abs/2509.25658) prove the disjoint-type case. They write that the conjecture "remains wide open beyond degree 2" and credit Epstein (2000) and Nie–Pilgrim with earlier bounded examples, so the book's "no example known" is outdated. | Non-disjoint types in degree ≥3 are hard. |
| Veech 299–300 / 315–316 | "S 相对稠密 ⇒ S−S 是 0 的 Bohr 邻域?" (10471–10472) | Equivalent to Katznelson's question (10488–10491; the converse follows by taking A = ℤ∖(S−S)). Declared open in [Alweiss arXiv:2511.21680](https://arxiv.org/html/2511.21680) ("central and long-standing open problem"). [arXiv:2610.10416](https://arxiv.org/abs/2610.10416) (Oct 2026) does not resolve it. | Famous and hard. |
| Hunt/Getoor 397–398 / 413–414 | Q1 "除去极端不对称 (需要界定)…半极集是极集"; Q2 "更好的充分条件" (13931–13934) | Declared open in [Hu–Sun arXiv:1908.06825](https://arxiv.org/abs/1908.06825), p. 2: "remains open … major unsolved problem". | Not precise and hard. |
| ODE/随机分析 399–401 / 415–417 | (a) Sobolev conditions for strong SDE solutions (14034–14035); (b) "凸泛函" Φ whose "梯度流" is the heat measure ν_t on L(G) (14056–14058) | (a) Answered many times: [Fang–Luo–Thalmaier, JFA 2010](https://www.sciencedirect.com/science/article/pii/S0022123610000911); [Champagnat–Jabin, AOP 2018](https://projecteuclid.org/journals/annals-of-probability/volume-46/issue-3/Strong-solutions-to-stochastic-differential-equations-with-rough-coefficients/10.1214/17-AOP1208.full). (b) The quoted terms are informal. [INFERENCE] Driver–Srimurthy (AOP 29, 2001, 691–723) show ν_T is equivalent to pinned Wiener measure. Then ν_s and ν_t are mutually singular, and the Wasserstein distance under the H¹ metric is infinite, so the literal metric reading…
| 最热点 410–412 / 426–428 | Standing assumption: Lipschitz boundary (14353). Rauch's original is HS1 (14401–14402). (i) Kawohl; (ii) "对每一个单连通的有界平面区域最热点猜测是否都成立？" (14421–14423) | (i) False as stated: [de Dios Pont arXiv:2412.06344](https://arxiv.org/abs/2412.06344), "counterexamples … for all sufficiently large d". (ii) Smooth domains: OAI family 369. Non-smooth domains with a simple eigenvalue, non-strict only: [Burdzy arXiv:2610.12622](https://arxiv.org/abs/2610.12622). Burdzy says the note was ChatGPT-generated and that he has not checked every detail. | (ii) remainder is candidate #1. |

### B. Ranked candidates

**#1 — Hot spots (ii) on non-smooth Lipschitz simply connected domains.**

Burdzy's note sets the boundary of what is proved. After Corollary 2.2 he writes that the theorem "does not assert that an interior point cannot share an extremal value with the boundary." Remark 7.1 says that without simplicity the argument covers "at least one nonzero element… It does not establish them for every element." I found nothing that resolves either gap, but a search miss is not proof.

0. **Prerequisite.** Kernel-replay family 369 (`HotSpots.json`, `Main.lean:78`) and audit whether the Lean statement says what the theorem means. If the OAI smooth theorem fails, (ii) reverts to the famous open problem.
1. **Simple eigenvalue, strict HS1.** This is my own sketch, not refereed; novelty is not established and Bañuelos's parallel note is unseen.
   - Let M = max u on the closed domain, which equals the boundary maximum by Burdzy's Cor 2.2. Let Z = {x ∈ Ω : u(x) = M}.
   - **(a) Z has no isolated points.** An isolated point would be a strict interior local maximum. Burdzy's approximating first eigenfunctions converge locally uniformly, so they would have nearby interior local maxima, contradicting the OAI theorem.
   - **(b) Z separates Ω.** At any point of Z the Hessian is negative semidefinite with trace −μM < 0. Rank 2 would make the point isolated, so the rank is 1. The implicit function theorem plus analyticity then make Z an embedded analytic arc near every point. So Z is a closed 1-manifold. Each component is a loop or a properly embedded line, and either one separates the simply connected domain, so Ω∖Z is disconnected.
   - **(c) Ω∖Z is connected.** For each component W of Ω∖Z, test the weak eigen-equation with Φ_ε = χ_W·min(1,(M−u)/ε), which lies in H¹(Ω). This gives μ∫_W u Φ_ε = −ε⁻¹∫_{W∩{M−ε<u<M}}|∇u|² ≤ 0, so ∫_W u ≤ 0. These integrals sum to ∫_Ω u = 0, so every one is zero. By Courant's theorem {u<0} is a single connected nodal domain. A component W missing it would have u ≥ 0 and ∫_W u = 0, so u ≡ 0 there, which unique continuation rules out. So there is only one component.
   - (b) and (c) contradict each other, so Z is empty. Applying the same argument to −u handles the minimum.
   - The argument works for any eigenfunction that is a locally uniform limit of first eigenfunctions of smooth simply connected domains filling out Ω.
2. **Double eigenvalue forced by symmetry.** Suppose Ω has k-fold rotational symmetry with k ≥ 3, and the eigenspace E is the 2-dimensional irreducible representation. Centre the Riemann map φ at the symmetry centre; then φ commutes with the rotation, so each φ(D_r) is symmetric. By Schur's lemma E stays exactly double on each φ(D_r), so every direction in E is a limit of first eigenfunctions and step 1 applies. This covers regular polygons [INFERENCE: their first eigenspace is that representation].
3. **The real gap: accidental double eigenvalue on non-smooth domains.** OAI preliminaries:78–81 give dimension at most 2, citing Nadirashvili 1988; whether that covers all Lipschitz domains still needs checking.
   - **(3a) Degree argument.** Use exhaustions recentred by Möbius maps, φ∘M_a(D_r).
     - The traceless splitting of the two-eigenvalue cluster should satisfy T(a,r) ≈ (1−r)·Q(a). Here Q is the Poisson extension of G₀ = ½[(∂_θZ)² − μ|φ′|²Z²], with Z = V₁ + iV₂ built from the boundary traces of a basis of E.
     - For the disk, Q ∝ a², a zero of index 2.
     - A zero of Q with nonzero index would give smooth approximating domains with an exactly double first eigenvalue. Then every direction in E is a limit, and step 1 finishes.
     - The crux is proving that first-order asymptotic, and the index of Q, when the boundary has corners.
   - **(3b) Extend the OAI proof to Lipschitz boundaries.** Rohleder's vector-field principle, the starting point of the OAI proof, already works on lip domains ([arXiv:2106.05224](https://arxiv.org/abs/2106.05224)), so the question is whether the OAI multiplier argument (conclusion:42–58) can be carried over.

**#2 — none qualifies.** An optional low-confidence task: auditing Chen–Wang's roughly 40-page construction would settle 广义度量 exactly, negatively, if it is correct. I found no citing work in eight years.

### C. Source-access blockers

- Read only as citations: the full texts of Driver–Srimurthy, Nadirashvili 1988 and Bañuelos–Burdzy 1999 Prop 2.5.
- Not seen: Bañuelos's parallel note (Burdzy §1(ii)) and McMullen 1995. I found no post-2018 expert status for M3⇒M1.
- I did not open the original PDF. Formulas garbled in the text that need it:
  - PDF p. 417: H(G), the H¹ norm and the heat equation (text 14039–14055).
  - PDF p. 426: system (0.1) (about 14362–14369).
  - PDF p. 262: the WVD kernel (8557–8568).

### D. Corpus overlaps

openai/math family 369 is the only overlap among the nine articles. Neither the title list (families 003–376) nor the local preprint directory names touch the others.

[Some lines truncated to 768 chars. Use agent://MoreMathAnalysis:raw:45-45 to read line 45 whole]