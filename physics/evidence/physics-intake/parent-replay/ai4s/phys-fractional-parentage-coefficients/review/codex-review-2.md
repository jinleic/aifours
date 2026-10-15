The ten B′ reduced formulas survive review. The finite-\(T\) obstruction also survives an exact rerun, but its implementation contains a new arithmetic bug, and several conclusions exceed that obstruction’s scope.

1. **Major — [code/brauer_residues.py:62](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/code/brauer_residues.py:62), Theorem D residue certification.**  
   `(-1) ** (a*b)` becomes a Python float when `a*b < 0`, contaminating the rational arithmetic before `sqclass` receives it. This occurs at an actual spin-2 place: for \(k=6\), generator \(v+1/2\), and \(r=-1/2\), the exact tame symbol is \(32768/800415\), of square class **30**; the implementation returns **11799795063484930**.

   **Fix:** use `sp.Integer(-1) ** (a*b)` or an integer parity sign. Add this actual pole case as a regression check and check reciprocity for every generator, not merely the base quaternion. Refresh the exact-arithmetic claims and §D’s stale description of quadratic-extension factorization.

   My read-only rerun with the exact sign factor still found **zero solutions for all five spin-2 families**. The bounded conclusion survives. The spin-\(f\ge3\) controls are useful quadratic-square regressions, but their polynomial discriminants do not exercise this finite-pole failure.

2. **Major — [RESULTS §D, optimality and scope](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/RESULTS.md:218), and [README verdict table](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/README.md:43).**  
   Excluding Bao–Li forms over the specified finite set \(T\) does **not** establish that every rational basis must introduce a nonlinear factor. A norm could instead have rational linear factors outside \(T\). Consequently, the unrestricted “optimality” deduction at §D’s end, README’s unrestricted negative answer and quadratic-minimum claim, and §G’s blanket statement about multiplicity are unsupported.

   The assertion that every §B formula uses roots in \(T\) is also false: at \(f=7\), \(g=91v+393\), whose root \(-393/91\) lies outside \(T\).

   **Fix:** retain the theorem explicitly over \(L_T\), qualify every summary accordingly, and restrict optimality to the corresponding support class and square-class metric. Withdraw unrestricted optimality pending an additional proof.

3. **Major — [RESULTS §B′, “all N” conclusion](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/RESULTS.md:154).**  
   The ten reduced transitions do not provide **every** CFP of these parents when \(N>v\). Theorem A’s ascending-seniority branch requires reduced coefficients from seniority \(v+1\) into the current parent. For a deficit-4 parent, those higher-seniority states can have deficits \(4,\ldots,2f+4\), exceeding B′’s coverage.

   This is an actual missing branch: the engine gives nonzero CFPs for \(f=3,N=7,v=5,L=11\) into \(v'=6,L'=12\), whose deficit is 6.

   **Fix:** state that B′ supplies the ten reduced CFPs and their associated all-\(N\) couplings through A. Qualify the README’s “SOLVED” entry if it presently means every daughter branch.

4. **Minor — [code/top_family_symbolic.py:254](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/code/top_family_symbolic.py:254), B′ phase convention.**  
   The docstring suggests that both resulting states receive `leading_sign_fix`; the second does not. Its largest-single-deficit coefficient is negative. Applying the earlier positive-leading-coefficient convention to that residual would change signs.

   **Fix:** explicitly define
   \[
   Q4=z_fz_{f-4}-4z_{f-1}z_{f-3}+3z_{f-2}^2,\qquad
   H2=z_fz_{f-2}-z_{f-1}^2,
   \]
   and normalize \(A\) and \(B-tA\) with positive normalization factors, where
   \[
   t=\frac{(f-1)(2f-3)}{g(v)}.
   \]
   Preserve the residual’s inherited sign. Under this convention, **all listed signs are correct**.

5. **Minor — [code/top_family_symbolic.py:269](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/code/top_family_symbolic.py:269), B′ symbolic certification.**  
   `run_general_k4` computes the entries but does not assert the advertised symbolic completeness identities. The numeric checker asserts completeness only on its finite grid; `large_sign` also supplies an asymptotic sign rather than a domain certificate.

   **Fix:** include symbolic row-sum assertions and explicit positivity certification on \(f\ge3,v\ge5\). I independently verified all ten displayed expressions, both symbolic sums equal to 1, and sign constancy throughout that domain. The harmonicity argument is valid, and Gram–Schmidt uses the correct degrees \(v\) and \(v-1\). The domain ensures that both daughter deficit-4 states exist.

6. **Minor — [RESULTS §E2, evidence accounting](/Users/jinleic/jinleic-workspace/ai4s/phys-fractional-parentage-coefficients/RESULTS.md:306).**  
   The reproduced total of 800 agreements comprises **742 individual CFP comparisons plus 58 block-weight comparisons**, not 800 individual table entries. Individual formulas have **27–30** available checks, contradicting “19–28.” The 26 individual entries also include the proved E1 case and the trivial scalar-parent transition.

   **Fix:** report these counts separately and distinguish 24 conjectured individual formulas, two proved/trivial entries, and two conjectured block weights. E2’s explicit conjecture label is appropriate; E1’s proof supports its stated generality.

The revised quadratic square criterion is correct, including imaginary quadratic fields. The cubic/quintic prime-degree argument is also valid: nonrational \(\alpha\) generates the prime-degree field, and a degree-\(d\) square-root factor therefore places its square root in that field. After fixing the sign arithmetic, the rational-place enumeration covers roots of every multiplicity, infinity, searched extra places, and the different contributions of \(c_0\) at odd- and even-valuation places.

Per-item verdicts:

| Item | Verdict |
|---|---|
| 1. Theorem B′ | **Accept with fixes** — reduced formulas accepted; clarify phases and all-\(N\) scope. |
| 2. Theorem D and revised checks | **Accept with fixes** — finite-\(T\) theorem accepted; withdraw unrestricted optimality. |
| 3. E1 and E2 | **Accept with fixes** — E1 accepted; E2 remains conjectural, with corrected accounting. |
| 4. README verdict table | **Reject as written** — its unrestricted no-go and family-completeness wording overstate the evidence. |

All checks were read-only; no files were modified and no work was delegated.