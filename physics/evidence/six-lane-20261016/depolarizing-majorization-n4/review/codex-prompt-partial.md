You are a hostile referee. Read-only. Working directory: a research lane on the four-qubit case (d = 2, n = 4) of the
depolarizing-output majorization conjecture, Eq. (2) of arXiv:2609.37240v1 (`sources/swtf-2609.37240v1.pdf`/.txt):
for all 4-qubit states ρ and 0 <= p <= 4/3, spec D_p^{⊗4}(ρ) is majorized by spec D_p^{⊗4}(|0000><0000|), where
D_p(X) = (1-p) X + p Tr(X) I/2.

Review the CANDIDATE PARTIAL THEOREM in `README.md` items 2-5 and the files `code/twirl_lp_exact.py`,
`code/u2_dual_cert.py`, `code/twirl_ppt_lp.py`, `evidence/u2_dual_certificates.json`. Check, independently and
adversarially:
1. Reduction R1: expansion D_p^{⊗4}(ρ) = Σ_s a_s X_s with a_s = (1-p)^s p^{4-s} 2^{s-4}; Hamming alignment of T_s;
   Ky Fan subadditivity; the claimed trivial ranges (U_3 trivial at k=1 and k>=5; U_2 trivial at k=1 and k>=11);
   the Kronecker lemma for U_1 at n=4; reflection p -> 2-p for p > 1.
2. Reduction R2: spin-flip identity ρ~ = Σ_s (-1)^s X_s at n = 4 (X_0 = 1, X_4 = ρ); D = D+ - a_3 ρ~; the claim
   K_k(Y+) = K_k(Y) for k <= 15 iff/when a_1 >= a_3, i.e. p >= 2/3.
3. The twirled PPT relaxation: is every constraint valid for ω = σ ⊗ Π (σ a state, 0 <= Π <= 1, Tr Π = k)? Is the
   symmetry group / commutant (conj(U) ⊗ U per site, span{Φ+, 1-Φ+}) correct, including the ordering conventions and
   the Choi-type operator J with Tr[(σ⊗Π) J] = Tr[Π N(σ^T)]? Are the closed forms (Choi coefficients, partial
   transposes Φ+ -> F/2, traces) right? Does twirling preserve feasibility and the objective?
4. The dual certificates: re-derive the dual LP and check exactly (use your own exact arithmetic) that each stored
   certificate in `evidence/u2_dual_certificates.json` is dual-feasible with bound equal to the target at k = 2..5.
5. Whether the stated conclusions (k in {1,5,11..15} for all p; plus {2,3,4} for p in [2/3, 4/3]) follow, and whether
   anything is overstated. Is any of this already known (King's results, SWTF's own partial results)?
Run any independent numerical or exact checks you need (sandbox is read-only: write nothing). Output a JSON object:
{"verdict": "ACCEPT" | "ACCEPT-WITH-FIXES" | "REJECT", "checks": [{"item","pass","note"}], "independent_tests": {...},
 "findings": [{"severity","issue","fix"}], "novelty_assessment": {...}}.
