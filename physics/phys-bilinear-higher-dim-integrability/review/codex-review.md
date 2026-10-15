Theorem 4.4 survives the algebraic checks. The main problems are the interpretation of test failure, an incomplete literature baseline, and several narrower qualification errors.

1. **Major — Failure of the universal test is overstated as absence of multisoliton solutions.**  
   Location: [RESULTS.md, C4 corollaries](/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/RESULTS.md:188), [README.md summary](/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/README.md:36).  
   For **every** polynomial \(p\),
   \[
   F=1+\sum_i a_i e^{k_ix+l_iy-p(k_i)t},\qquad G=1
   \]
   solves both systems with arbitrary wave numbers. Thus generic FFF families survive even when FFG fails. The test also excludes constrained polarizations, other backgrounds, and other tau-function ansätze. Its failure establishes failure of the specified **all-pattern, square-free test**, not nonintegrability in every conventional sense.  
   **Fix:** qualify “no generic three-soliton solutions” by the failing pattern and ansatz. Qualify C5’s **COUNTEREXAMPLE** verdict as a counterexample to the generic Hirota-property implication; failure alone does not exclude a Lax representation.

2. **Major — The proposed “extra condition” exceeds the proved result.**  
   Location: [README.md:42](/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/README.md:42).  
   Requiring genuine two-function integrability is not shown sufficient for the higher-dimensional conclusion. The theorem concerns three solitons; the required all-\(N\) implication remains open in the folder.  
   **Fix:** state that genuine two-function **3ST** gives the proved classification in \(\mathcal P\), rather than presenting it as a sufficient condition resolving the book’s integrability question.

3. **Major — The literature exclusion and positive baseline are incorrect.**  
   Location: [STATUS.md:60](/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/STATUS.md:60), [STATUS.md §5](/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/STATUS.md:101), [RESULTS.md novelty audit](/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/RESULTS.md:271).  
   Hietarinta explicitly rotates the odd-\(B\) formulation into **both equations acting on the same pair**. His Eq. (37), with its parameter zero and variables renamed, contains the cubic extension here. See [Hietarinta’s own account, §4.2](https://arxiv.org/pdf/solv-int/9708006). Moreover, [Peng et al. (2008), Eqs. (6), Proposition 1](https://doi.org/10.1016/j.physleta.2008.01.090) provide Wronskian solutions, a Bäcklund transformation, and a Lax representation for that cubic system.  
   **Fix:** replace the “different second equation” rationale and symmetry-only baseline. Distinguish their restricted soliton families from your independent-amplitude test. The arbitrary-degree novelty of Theorem 4.4 remains unverified; these sources do not by themselves settle it.

4. **Minor — Lemma 4.1’s displayed hypotheses omit a condition needed for its failure witness.**  
   Location: [RESULTS.md, Lemma 4.1](/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/RESULTS.md:126).  
   The residual contains \(m_3\). With \(p=k^4\), \(k=(1,2,-4)\), \(l=(1,3,0)\), and unit nonzero seed amplitudes, all listed subset conditions hold and \(\Phi=-672768\), but **every residual vanishes**. I reproduced this exactly.  
   **Fix:** explicitly require \(m_3a_1a_2b_3\ne0\) when asserting that this coefficient witnesses failure. Theorem 4.4’s chosen witnesses satisfy this restriction.

5. **Minor — The discrete classification wording outruns the supplied proof.**  
   Location: [README.md:38](/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/README.md:38), [RESULTS.md, C7](/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/RESULTS.md:246).  
   The code proves the passing identities and tests three failing polynomials; it does not establish failure for **every** degree-\(\ge4\) polynomial.  
   **Fix:** narrow the summary, or supply the continuum-limit argument: set \(z_i=e^{\epsilon l_i}\), divide the second equation by \(\epsilon\), and use convergence to the nondegenerate continuous recursion to transfer its obstruction.

6. **Minor — The cubic-\(Q\) example does not invalidate the conditional \(R=Q\) rule.**  
   Location: [RESULTS.md, C8](/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/RESULTS.md:260).  
   Both systems fail for that example. A false antecedent supplies no counterexample to the implication.  
   **Fix:** say that cubic multipliers destroy this passing example; remove the inference against extending the conditional rule.

7. **Minor — C5’s completely linear limit is undefined under the stated test.**  
   Location: [RESULTS.md, C5](/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/RESULTS.md:200).  
   At \(c_3=c_5=0\), all pair phase ratios become \(0/0\). The symbolic zero numerator cannot certify that specialization using the defined nondegenerate test.  
   **Fix:** require \((c_3,c_5)\ne(0,0)\), and discuss the linear transport limit separately.

8. **Nit — C6 overcounts its two-function checks.**  
   Location: [RESULTS.md:234](/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/RESULTS.md:234).  
   There are \(4\times2\times2=16\) cases, each at three points: **48**, not “24 cases × 3 points.”  
   **Fix:** correct the count and list the six control cases separately.

All computations were read-only. I reproduced Parts A–D, the discrete checks, N=4,5 numerical cases, and the independent differentiation witness. A separate denominator-cleared symbolic calculation confirmed C5’s full factorization. The engine’s submask enumeration, signs, Cramer solve, and actual callable symbols checked correctly against independent ordered-pair enumeration.

| Claim | Assessment |
|---|---|
| **C1** | **Correct**, where the generic recursion is defined. The diagonal specialization preserves its nonzero determinants. |
| **C2** | **Correct.** Oddness gives the stated cancellation; amplitude specialization introduces no denominator problem. |
| **C3** | **Correct.** All 86 symbolic checks reproduced; coefficient specialization is justified. |
| **C4** | **Correct with fixes.** The closed form, tail inequality, and nondegeneracy checks hold. The leading coefficient \(c_d^3\Phi_d\ne0\) handles every odd or mixed-parity \(p\). Findings 1 and 4 concern scope and hypotheses. |
| **C5** | **Correct with fixes.** Factorization and \(3600/247\) verified. The pure fifth-order obstruction is already present in [Wang et al., Eq. (16)](https://www.researchgate.net/publication/377022634_A_novel_21-dimensional_Sawada-Kotera_type_system_multisoliton_solution_and_variable_separation_solution); qualify the integrability verdict. |
| **C6** | **Correct** as finite-point evidence; symbolic N=4 certification is **unverifiable** from the supplied outputs. |
| **C7** | **Correct with fixes** to the blanket classification wording. |
| **C8** | **Correct with fixes.** The reported finite scan reproduced; its cubic-\(Q\) inference does not follow. |