You are an independent referee for a mathematical research note. Work read-only. You may read ONLY files inside the current directory (the target directory `regular-semigroup-embedding`, which contains README.md, proof.md, sources/, work/, evidence/). Do not read anything outside it. Do not delegate to other agents or tools that spawn agents. You may use web search for literature/status checks.

Context. The Chinese book 《10000个科学难题·数学卷》 (2009, pp. 66-67, excerpt in sources/book-excerpt.txt) poses, citing M. B. Szendrei, "Some open problems in the structure theory of regular semigroups", Semigroup Forum 64 (2002) 213-223:
 Problem 1: Is every weakly E-unitary locally r-orthodox semigroup embeddable in a "semidirect product of a seminormal band by a completely simple semigroup"?
 (seminormal band = every local submonoid eBe is a regular band; locally r-orthodox = every eSe is orthodox with regular band of idempotents.)
The note fixes two readings of "semidirect product": (P) Pastijn product B ⊙ C (definition in sources/szendrei2019_survey_arXiv1909.05280.pdf, §5.2) and (R) Auinger–Polák restricted semidirect product B ⊙* C (sources/auinger_polak1997_ActaSciMath63.pdf, Definition 3.1).

Your tasks:
1. Check every proof in proof.md line by line: Lemma 0, Lemma 1, Lemmas 2-3, Theorem A (both directions, both readings, including the derivation that for completely simple C the restricted product reduces to (a,x)(b,y) = (a·φ_x(b), xy)), Lemma 4, Lemma 5, Lemma 6, Theorem B (positive answer via Szendrei 1987 as cited from the survey), Theorem C (all Steps 1-5, in particular: Step 1(a)-(d); the normal form Φ = π∘σ∘p; the band B0 and the functor F; the use of a left transversal of H1 in G), and the (C2)/(C3) proofs in §7.
2. Check that the formal statement (README "Status (c)") faithfully formalizes the book's Problem 1, and whether the choice of readings (P)/(R) is justified; flag any other plausible reading that would change the answer.
3. Check the status claim "uncertified-open": search the literature (2002-2026) for any resolution of Problem 1 (weakly E-unitary locally orthodox / locally r-orthodox semigroups embedded in Pastijn products or semidirect products by completely simple semigroups), and for prior appearances of Theorem A or Theorem C (e.g. Billhardt–Szendrei 1993 "A new class of embeddable E-unitary regular semigroups", or Billhardt 1998 J. Algebra 206). Report concrete citations if found.
4. Inspect the checker scripts in work/ (check_band_facts.py, check_two_chain_theorem.py, check_two_chain_generic.py, and the SAT scripts) and the logs in evidence/: do they actually verify what README's Claims table says? You may run them if your sandbox allows (python3 only, no installs); otherwise inspect the code.

Output format (Markdown):
- "Verdict:" one of {correct, correct-with-minor-fixes, has-errors}, for each of: Theorem A, Theorem B, Theorem C, Lemmas 0/1/5/6, §7, formalization, status claim.
- "Concrete errors:" numbered list; for each give file, section/line, what is wrong, and a fix. Distinguish fatal errors from gaps that are fixable.
- "Literature findings:" any relevant papers with full citations (and what they prove), or "none found" with the queries you ran.
- "Checker assessment:" what the scripts do and do not verify.
Be specific and skeptical; do not praise.
