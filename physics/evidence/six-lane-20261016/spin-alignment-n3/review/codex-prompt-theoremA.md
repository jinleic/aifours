You are a hostile, independent referee. Work only in the current directory (read-only). Do not delegate, no network.
You may run python via `../../noncws-code/env/venv/bin/python - <<'EOF2' ... EOF2` (numpy, scipy, sympy available); do not write files.

Review `PROOF.md` (Theorem A and Corollary B for Song–Chen arXiv:2603.25410v1 Conjecture 2 at n=3, d=2, Q=I/2, and the
depolarizing corollary). Primary text of Song–Chen is `song-chen-2603.25410v1.txt` (Prop. 3 on lines ~131–243).
Tasks:
1. Check every step: the decomposition of X and Y, the use of Prop. 3 (hypotheses, scaling), Lemma K (Kronecker-sum
   majorization) and its proof, the alignment inequalities for T_1, T_2 in the order 000,001,010,100,011,101,110,111,
   the Ky Fan additivity for aligned diagonal targets, and Ky Fan subadditivity.
2. Corollary B: verify the expansion of D_p^{⊗3} into weights (1−p)^{|I|} p^{3−|I|} with the stated convention, that
   these weights satisfy (i)–(ii), and the identity σ_y X^T σ_y = Tr(X)I − X ⇒ σ_y D_p(X)^T σ_y = D_{2−p}(X) and the
   resulting spectral identity for the 3-fold tensor power (including the reference |000⟩).
3. Independently test numerically: random 3-qubit states and random weights inside the region (i)–(ii), and the
   depolarizing case for p in {0.2, 0.5, 0.9, 1.1, 4/3}; report the largest Ky Fan violation found (should be ≤ 1e-9).
   Also confirm a weight vector OUTSIDE (i)–(ii) where the separate-block bound Σ K_k(target) exceeds K_k(Y)
   (to make sure the hypotheses are load-bearing).
4. Hostile assessment: gaps, hidden assumptions, overclaims, whether Corollary B really is the d=2, n=3 instance of
   Eq. (2) of Song–Wang–Tomamichel–Fang (file swtf-2609.37240v1.pdf), and whether the result looks already known.
Final message: JSON with keys "verdict" (ACCEPT | ACCEPT-WITH-FIXES | REJECT), "checks" (list of {item, pass, note}),
"numerical_tests", "findings" (list of {severity, issue, fix}), "novelty_assessment".
