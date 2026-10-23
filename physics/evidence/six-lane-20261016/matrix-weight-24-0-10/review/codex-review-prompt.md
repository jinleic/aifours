You are a hostile, independent referee. Work ONLY inside the current directory (a research lane) and read-only.
Do not delegate. Do not access the network. You may run Python with
`../noncws-code/env/venv/bin/python` (has numpy, sympy, fractions) using inline scripts (`python - <<'EOF' ... EOF`);
you cannot write files.

## Claim under review
Anglès Munné–Huber, "SDP bounds on quantum codes: rational certificates", arXiv:2603.19901v1, §3.3, Open Problem 1:
for the hypothetical [[24,0,10]]_2 stabilizer code with weight distribution Eq. (38)
(A10..A24) = (18216, 156492, 1147608, 3736557, 6248088, 4399164, 1038312, 32778), provide a putative INTEGER matrix
weight enumerator λ^{t,p}_{i,j} satisfying their Eq. (31) together with (32) pure, (33) self-dual, (34) additive
(x ≥ 0, λ ∈ Z) and (35) Type II constraints, where x^{t,p}_{i,j} = λ^{t,p}_{i,j}/γ^{t,p}_{i,j}.
The lane claims an explicit table `evidence/lambda_24_0_10.json` (entries [i,j,t,p,λ]; all other λ = 0) that satisfies
ALL these constraints exactly, and additionally the genus-2 (pair-enumerator) MacWilliams self-duality identities and
2-dim-subspace divisibility. It does NOT claim the code exists.

Primary text: `sources/amh-2603.19901v1.txt` (HTML-extracted; Eq. (31) is the block "find x subject to ...", the
factors γ (41) and α, β (42) are in Appendix A; the PDF is `sources/rational-sdp-2603.19901.pdf`). The authors'
Julia definitions of beta/alpha/gamma are in `sources/amh-repo/fun.jl`.

## Your tasks
1. From the primary text (not from the lane's code), write down every constraint of Eq. (31)–(35) for n=24, K=1,
   δ=10, including the exact formulas for γ, α, β and the block index ranges. Note any ambiguity.
2. Write your OWN independent exact verifier (Fractions; exact PSD via LDL^T or principal-minor/eigen-free method;
   note α is rational whenever i+j is even) and run it on `evidence/lambda_24_0_10.json`. Report every constraint's
   pass/fail. Do not import the lane's modules.
3. Mutation controls: perturb the table (e.g. +1 on one entry, swap two entries) and confirm your verifier fails.
4. Positive control: build the hexacode (6,2^6,4) or another small even self-dual additive code yourself, compute
   its pair counts by brute force, and confirm your verifier passes it with the corresponding (n, δ, A).
5. Hostile assessment: Is the lane's interpretation of Open Problem 1 faithful? Is a positive table a complete answer
   to what was asked? Any hidden assumption, convention error (e.g. Pauli Y labeling, symmetry reduction validity,
   orbit normalization), or overclaim? Optionally spot-check the genus-2 claims with `code/verify_g2.py`'s logic
   re-derived independently (polynomial identity W(Tz) = 2^48 W(z) with T = [[1,3,3,3,6],[1,-1,3,-1,-2],[1,3,-1,-1,-2],[1,-1,-1,3,-2],[1,-1,-1,-1,2]] in variables (00,0x,x0,xx,xy)).

## Output (final message): JSON with keys
"verdict" ("ACCEPT" | "ACCEPT-WITH-FIXES" | "REJECT"), "constraints_checked" (list of {name, pass, note}),
"independent_verifier_summary", "mutation_results", "positive_control", "findings" (list of {severity, issue, fix}),
"interpretation_assessment".
