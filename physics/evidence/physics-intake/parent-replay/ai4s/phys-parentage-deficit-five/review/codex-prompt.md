# Hostile referee: complete general-spin deficit-five reduced CFP family

Today is 2026-10-14. You may read only /Users/jinleic/jinleic-workspace/ai4s/phys-parentage-deficit-five/ and descendants. Do not read sibling or parent files, do not write or edit, do not delegate, and do not run reproduction scripts (the caller is independently running the exact computation). No network is needed. Return a precise mathematical/code review in your final message; the caller manages the output file.

Review README.md, STATUS.md, RESULTS.md and code/deficit_five.py, and result JSON files if present. The claim is a closed formula for ALL signed one-body reduced CFPs at N=v, parent total spin L=f*v-5, all integer f>=3, v>=3, into seniority v-1 daughters. Stable v>=6 has 14 entries; low v=3,4,5 have 3,5,12 entries; v<=2 has no parent. Upward seniority at N>v is explicitly not covered. No novelty claim is made: Pan's spin-2 tables, the 2014 general-spin solvable-energy statements, and the 2026 Redmond-recursion baseline are acknowledged; a search miss is not proof of openness.

Representation: z_j is the unnormalized orbital m=f-j, norm weight w_j=1/binom(2f,j). Fock monomial norm is product a_j! w_j^a_j. J+ z_j=j z_(j-1). Particle-first Condon–Shortley CG phases are used. Parent raw basis is z0^(v-3) C5 then z0^(v-5) H2*T3 (second only v>=5), where
H2=z0*z2-z1^2,
T3=z0^2*z3-3*z0*z1*z2+2*z1^3,
Q4=z0*z4-4*z1*z3+3*z2^2,
C5=z0^2*z5-5*z0*z1*z4+2*z0*z2*z3+8*z1^2*z3-6*z1*z2^2.
Daughters k=0,2,3,4,5 use the analogous covariants with Q4 then H2^2 at k4 and C5 then H2*T3 at k5. Every block is Gram–Schmidt in stated order, positive norm square roots, no rephasing.

The central closed formula uses raw Gram matrices G divided by n!, and X=<raw parent,z_(5-k)*raw daughter>/v!. If T=[[1,-G12/G11],[0,1]] (scalar case T=1) and h=diag(T^T G T), Y=T_parent^T X T_daughter, then
r_ia=(-1)^(5-k) Y_ia/sqrt(w_(5-k) * CG_squared * h_parent_i * h_daughter_a),
CG_squared=product_(s=0..4-k) [2*f*(v-1)-2*k-s]/[2*f*v-8+s], empty at k5.
All G and X entries are explicitly displayed in RESULTS.md; no varying-size sum or recurrence remains. Low-degree absent columns are removed BEFORE evaluating, avoiding spurious poles.

Attempt to falsify: (1) highest-weight covariants and completeness dimension; (2) every daughter/triangle/seniority block; (3) factorial normalization and particle-first sign; (4) insertion matrix coefficients; (5) basis positivity/no hidden poles on all f>=3 and admissible v; (6) low-v exceptions; (7) whether this is a legitimate fixed closed form rather than a tautological algorithm; (8) symbolic proof vs finite checks; (9) scope and prior-art wording. Explain any error with exact counterexample or algebra and smallest fix. The code imports the existing sibling engine read-only, with bytecode writes disabled; it does not clone it. The shared engine is not part of your allowed read scope. Do not claim to have independently authenticated external sources or run tests.

Return verdict correct / correct-with-fixes / incorrect / insufficient-information, then numbered findings by severity and precise file/section, then central claims that survive and any exact remaining proof gap. Avoid generic suggestions or demands for broader unassigned work.