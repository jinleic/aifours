VERDICT: ACCEPT-WITH-FIXES

**Fatal/major:** None found in the delta. The pinned SHA-256 matches. References below are LF line numbers in [r2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/chi8-parent-inputs-r2/PROOF_CHI8.r2.md).

**Minor findings:**

- **L367–369: the scope inference is too strong.** A lower bound supporting AM04’s global Θ statement does not necessarily require their false *pointwise* feasibility assertion. Global comparability could follow from a common feasible maximiser; at the uniform overlap, the relaxed optimiser is feasible. Replace “would need the tightness assertion” with “does not follow from the relaxed upper bound alone.” L362–366 correctly preserve the published upper bounds and avoid claiming a colouring theorem false.

- **L275–278: undefined edge normalisation.** The file never defines ℓ_e. With this file’s β_e = b_e/n, the direct correspondence is **β_e = d y_e**. The displayed ℓ_e = dk y_e is correct only after defining ℓ_e := kb_e/n. Prefer the existing β notation. Likewise, **L351** should explicitly define \(M_t=(1-t)J+tI\); the quoted \(M_{2/3}\) numbers are correct under that interpretation.

- **L311–313: qualify the row-stochastic domain.** Theorem C states the E inequality on all row-stochastic matrices, but its U inequality only on doubly stochastic matrices. A row-stochastic matrix with every row \((1,0,0,0)\) has E = 0. Either describe the E bound here or explicitly extend U to −∞ when E = 0.

The requested substantive checks pass:

1. **Load-bearing argument and renames — L101–117, 207–268, 373–465, 499–610.** No delta breaks or weakens Lemma A, Proposition B, Lemma 3.1, analytic Lemma 3.2, Theorem C, §§5.1–5.3 or §6.1. All specified renames are consistent throughout the **836-line file**. Old names in L826–829 explicitly describe historical notation; surviving S, c and K usages denote row functions, cited notation, the kernel or verifier labels. Every matching occurrence in §5.3 uses η. The multiplier shift at L261 preserves the bound exactly. The added polynomial degree at L517 is correctly \(16+8+145/2+3=199/2\).

2. **GSVY identification — L279–299.** Equation (15), with Δ = 8 and paired interaction, gives
   \[
   \Phi_1^{B\otimes B}(M^{7/8})
   =4\log(2E(M))-7\log4
   =-10\log2+4\log E(M)=U(M).
   \]
   Map (20) sends this R to \(M/4\). The precursor framing correctly distinguishes this algebraic identity from a pointwise reparameterisation of Ψ. The spectrum \(9,-3^{(6)},1^{(9)}\) is correct, so \(B\otimes B\) is not PSD and factorisation (18) is unavailable.

3. **AM04 feasibility and loss — L329–359, 679–683.** AM04 source L454–455 explicitly asserts feasibility and tightness. The marginal discrepancy is exactly
   \[
   \frac{d\alpha_{ij}}p\left(\alpha_{ij}-\sum\alpha^2\right).
   \]
   Thus feasibility holds precisely when positive overlap entries are equal. Exact arithmetic confirms:
   - At \((J+I)/2\): marginals \(35/26,17/78\), required \(5/4,1/4\).
   - At \(M_{2/3}\): marginals \(99/62,25/186\), required \(3/2,1/6\).

   Write \(L(M)=H(M/4)+4\log p=\log4+\phi_8(M)\). At the first counterexample,
   \[
   L(M)-U(J)=0.00741931598\ldots,\qquad
   U(M)-U(J)=-0.02876421895\ldots.
   \]
   Independently certified rational bounds give
   \[
   0.036183534932<L(M)-U(M)<0.036183534933.
   \]
   Since \(\Psi_8(M)\le U(M)\), the relaxation overestimates the **exact exponent** by more than 0.036. This compares L(M) with U(M), not merely with U(J).

4. **First moment — L615–637.** The polynomial factor
   \(P_3=e^4(8n+1)^{3/2}(4n+1)^{7/2}\) is correct. Setting \(q=1-\sum r_i^2\), optimisation gives \(e^{2c_1-1}=d/q\), leaving \(H(r)+(d/2)\log q\). Both component bounds attain equality at the uniform vector, giving maximum \(\log(16/27)\). The class-count bound and conditioning on simplicity are valid. Independent exact counting also reproduces the n = 60 rate −0.5484383666….

5. **KPW — L33–37, 136–137, 483.** The convention paragraph matches source L23–27 and L105–107: k = 5 gives {4,5}; the exact-value clause fails. A9′ accurately identifies source L1251: \(18>16\) at k = 4, while \(8<9\) at k = 3.

GSV-only and CLMS source attributions were not independently checked because those sources were outside the permitted inputs.