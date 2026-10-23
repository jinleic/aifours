{
  "verdict": "ACCEPT-WITH-FIXES",
  "checks": [
    {
      "item": "Section 1: expansion coefficients",
      "pass": true,
      "note": "The coefficients a_s=(1-p)^s p^(4-s) 2^(s-4) are correct. Independent symbolic checks on all five Pauli-weight classes confirm the channel expansion."
    },
    {
      "item": "Section 1: common-order lemma and Hamming alignment",
      "pass": true,
      "note": "The lemma follows from simultaneous maximizing spectral projections and Ky Fan subadditivity. T_s(x)=C(z(x),s) gives the required common order whenever the coefficients are nonnegative."
    },
    {
      "item": "Section 1: all trivial-index claims",
      "pass": true,
      "note": "U_0 and U_4 are immediate. U_1 follows by diagonalizing the marginals and expressing their Kronecker sum as a convex mixture of bit-flip conjugates of T_1. The T_2 spectrum is (6,3 repeated 4 times,1 repeated 6 times,0 repeated 5 times), with trace 24. The T_3 spectrum is (4,1 repeated 4 times,0 repeated 11 times), with trace 8. All stated thresholds are correct."
    },
    {
      "item": "Section 1: R1",
      "pass": true,
      "note": "Nonnegative coefficients, the established U_s inequalities, and common ordering justify the entire inequality chain."
    },
    {
      "item": "Section 2: spin flip and sign conditions",
      "pass": true,
      "note": "The spin-flip identity holds, and the resulting operator is a state because this is global transpose followed by unitary conjugation. D=D+−a_3 rho_tilde is correct. In particular, b_1=p(1-p)(2-p)(3p-2)/8. The stated equivalence is correct on (0,1); on [0,1], p=0 is an additional zero."
    },
    {
      "item": "Section 2: Y+ and Ky Fan sums",
      "pass": true,
      "note": "Y+=Y+a_3|1111><1111|. On [2/3,1], a_3<=a_1, so the modified entry remains a smallest entry. Consequently every K_k with k<=15 is unchanged, including at both endpoints."
    },
    {
      "item": "Section 2: reflection",
      "pass": true,
      "note": "The single-qubit identity tensors to global transpose followed by conjugation with sigma_y tensor 4. It preserves spectra for every input and correctly maps (1,4/3] to [2/3,1)."
    },
    {
      "item": "Section 3: bilinear form and relaxation",
      "pass": true,
      "note": "The transpose in Tr[(sigma tensor Pi)J]=Tr[Pi N(sigma^T)] is necessary and correctly handled. Every stated constraint contains every admissible product sigma tensor Pi. The dependence sigma_omega=Tr_Pi(omega)/k is linear for fixed positive k."
    },
    {
      "item": "Section 3: invariance of constraints and objective",
      "pass": true,
      "note": "Both are invariant. The partial-transpose conjugation formula correctly uses conjugate(U) tensor conjugate(U). Thus Haar averaging preserves feasibility and the objective; the reduction does not merely preserve the feasible set."
    },
    {
      "item": "Section 3: commutant",
      "pass": true,
      "note": "Each local representation is trivial plus the irreducible three-dimensional adjoint representation. Their tensor products for U(2)^4 are pairwise inequivalent and multiplicity-free. The 16 projectors E_S therefore span the full commutant."
    },
    {
      "item": "Section 3: exact LP data and dual",
      "pass": true,
      "note": "Ranks, both partial traces, normalized marginal I/16, coefficient bounds, PPT eigenvalues, objective coefficients, dual signs, and weak duality are correct. The marginal inequality is redundant because its left side equals k/16."
    },
    {
      "item": "Stored rational certificates",
      "pass": true,
      "note": "All ten stored certificates independently satisfy nonnegativity and every dual inequality, with exactly the claimed bounds. Every dual column has zero slack."
    },
    {
      "item": "Section 4: partial theorem and scope",
      "pass": true,
      "note": "Both parameter ranges and both index sets follow exactly. The remaining-index reductions are correct. The package does not claim full majorization or interpret a loose relaxation as a counterexample."
    },
    {
      "item": "Frozen auxiliary computation completeness",
      "pass": false,
      "note": "exact_U3.log terminates with a SymPy InfeasibleLPError at k=12. This is an incomplete supporting run, not a failure of the theorem: these indices have elementary trace bounds, and independent exact certification recovered all LP optima."
    }
  ],
  "independent_tests": {
    "read_only": "All audit code ran in memory; no files were modified. The provided certificate checker was not executed.",
    "manifest": {
      "entries_checked": 14,
      "mismatches": []
    },
    "explicit_matrix_checks": {
      "dimension": 256,
      "arithmetic": "Integer-scaled projectors and exact Fraction arithmetic",
      "projector_identities_and_resolution_of_identity": true,
      "both_partial_traces": true,
      "objective_coefficients_checked": 80,
      "PPT_row_entries_checked": 256,
      "U2_objective_by_subset_size": [0, 0, 36, 36, 24],
      "all_antisymmetric_PPT_row_by_subset_size": [
        "81/16",
        "-27/16",
        "9/16",
        "-3/16",
        "1/16"
      ],
      "two_antisymmetric_sites_sample": {
        "S_empty": "9/16",
        "S_both_antisymmetric_sites": "1/16",
        "S_one_symmetric_and_one_antisymmetric_site": "-3/16"
      }
    },
    "certificate_bounds": {
      "1": "6",
      "2": "9",
      "3": "12",
      "4": "15",
      "5": "18",
      "11": "24",
      "12": "24",
      "13": "24",
      "14": "24",
      "15": "24"
    },
    "certificate_details": {
      "dual_column_inequalities_checked": 160,
      "all_nonnegative_multipliers_valid": true,
      "minimum_and_maximum_column_slack": ["0", "0"],
      "all_bounds_equal_independently_computed_targets": true,
      "all_targets_lowered_by_1_over_1000_rejected": true,
      "distinct_stored_dual_points": 2
    },
    "analytic_certificate_extraction": {
      "identity": "obj.c = 3k + 48 c_full − 72 sum_{tau with exactly two antisymmetric sites} e_tau(c)",
      "consequence": "LP_k <= min(3k+3,24)",
      "note": "The first certificate family therefore has a short analytic verification."
    },
    "independent_LP_optima": {
      "method": "Independent five-variable permutation reduction; numerical search followed by exact Fraction checks of primal feasibility, dual feasibility, and matching objectives.",
      "k_order": "1 through 15",
      "U2": [6, 9, 12, 15, 18, 20, 21, 22, 23, 24, 24, 24, 24, 24, 24],
      "U3": [4, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
      "mutation_controls_k_2_through_5": {
        "without_PPT": ["61/4", "77/4", "93/4", "24"],
        "without_coefficient_upper_bounds": [12, 18, 24, 30],
        "without_marginal_inequality": [9, 12, 15, 18]
      }
    },
    "additional_identity_checks": {
      "spin_flip_matrix_units_checked_exactly": 256,
      "product_input_twirl_feasibility": "Verified exactly for k=1..16; all five Phi_s objectives attain their product-reference targets.",
      "complex_unitary_convention_checks": "Bilinear identity, objective covariance, reduction-constraint covariance, and partial-transpose conjugation agreed within 1.8e-14."
    }
  },
  "findings": [
    {
      "severity": "low",
      "issue": "The frozen exact_U3.log contains an aborted computation.",
      "fix": "Label the run explicitly as incomplete and explain the independent trace argument for the omitted indices, or replace it with a complete verified run."
    },
    {
      "severity": "low",
      "issue": "The description of twirl_ppt_lp.py as an independent explicit-matrix LP build is too broad. It constructs J and E_S explicitly, but obtains PPT rows and marginal coefficients from the same closed formulas.",
      "fix": "Qualify the independence claim, or derive those rows directly from partial transposes and partial traces of the explicit matrices. The present audit independently verified them."
    },
    {
      "severity": "low",
      "issue": "u2_dual_cert.py checks newly generated points rather than loading and verifying the frozen certificate JSON, and its main entry point writes a recomputed file.",
      "fix": "Provide a separate read-only verification mode that loads the frozen JSON, checks dimensions and multiplier signs, reconstructs every dual inequality, and independently computes the targets."
    }
  ],
  "novelty_assessment": {
    "already_known": "k=1 follows from King's maximal-output norm multiplicativity by taking q to infinity, as acknowledged in PROOF.md. [King, Theorem 3](https://arxiv.org/pdf/quant-ph/0204172).",
    "elementary_baseline": "k=11..15 require no LP certificates: the stated trace bounds, U_1, R1, and reflection already establish them.",
    "substantive_increment": "Relative to that baseline and the cited spectral inequalities, the contribution is k=5 throughout [0,4/3], together with k=2,3,4 throughout [2/3,4/3], obtained from U_2 and the spin-flip reduction.",
    "SWTF_comparison": "Theorem 4 gives shifted log-determinant ordering; Proposition 11 supplies norm and entropy consequences. The approximate-majorization results do not supply these exact n=4 indices. Schur concavity of those particular functionals does not establish ordering for every Schur-concave functional. [SWTF v1](https://arxiv.org/html/2609.37240v1).",
    "independent_nonimplication_example": {
      "reference": "At p=2/3, the reference spectrum has numerators (160,80,80,80,80,40,40,40,40,40,40,20,20,20,20,10), divided by 810.",
      "construction": "Replace one triple (160,80,40) by (157,84,39), leaving the other entries unchanged.",
      "result": "The resulting spectrum satisfies every King Schatten-norm inequality and every positive-shift log-determinant inequality, but exceeds the reference K_k by 1/810 for k=2,3,4,5.",
      "exact_justification": "The changed triple increases its shifted determinant by 187t/810^2 + 2332/810^3. Along (160-3u,80+4u,40-u), 0<=u<=1, weighted AM-GM and 157^3*39>84^4 show that every power sum with exponent q>1 decreases.",
      "scope": "This is an arbitrary spectral example, not a claimed channel output. It establishes nonimplication from the cited spectral inequalities alone."
    },
    "priority": "The audit establishes a valid partial result and its distinction from the cited bounds; it does not establish literature-wide priority."
  }
}