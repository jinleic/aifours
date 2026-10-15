# Exact Shor finite-completion question

Date: 2026-10-14 PT. This is one bounded HMZ attempt, not a license to replace the target by a bounded search.

## Goal

Let the alphabet be {a,b}, with a != b. Set

C = b{1,a,a^7,a^13,a^14} union {a^3,a^8}b{1,a^2,a^4,a^6} union a^11 b{1,a,a^2}.

There are 16 words, all of length at most 15. Question 1 on book pages 64–65 (PDF 80–81) of 10000个科学难题·数学卷 asks whether there exists a FINITE uniquely decipherable COMPLETE code X over {a,b} with C subset X. Complete means every finite binary word is a contiguous factor of some word in X*. For finite codes this is equivalent to maximality. Either an explicit positive witness, or a proof that no such X exists, resolves the exact question. The general decidability question (book Question 2) is NOT this task.

The exact frozen Lean proposition is in Statement.lean. Do not change that file, TASK.md, ACCEPTANCE.md or verify.py.

## Baseline and known limitations

Primary source read by the caller: Cordero 2019, A Note with Computer Exploration on the Triangle Conjecture, https://www.normalesup.org/~cordero/Publications/A_Note_with_Computer_Exploration_on_the_Triangle_Conjecture.pdf (HAL hal-03682699 metadata). Sections 2–3 distinguish necessary factorization conditions from completion. The paper explicitly leaves this exact code unresolved. Its Table in section 2.2 already proves n=330*k with k>=4 for any completion, where a^n is the unique pure a-word in X. Thus n>=1320 is ALREADY PRIOR ART, not a new improvement. Section 2.2 text contains an apparent arithmetic typo in one displayed 3R collision: verify collisions yourself.

Restivo–Salemi–Sportelli theorem: if a finite maximal X contains b,a^n then (L,R) factors cyclic Z_n, where L is the set of residues k with some a^k b^t in X (t>=1), and R analogously has b^t a^k in X. Thus L includes {0,3,8,11}, R includes {0,1,7,13,14}. Sands multiplier theorem: if (L,R) factors and gcd(p,|L|)=1, then (pL,R) factors. The analogous statement holds for R. Failure of necessary conditions is an obstruction, but existence of one factorization is NOT a finite code construction. A complete bayonet code (cbc, |Y|=n and Y union {a^n} a code) is NOT by terminology a finite complete code in the book's sense.

Unreviewed scout refinement: scaling L by 2 causes 2*3+1=2*0+7, so perhaps 2 divides |L| as well as 330 divides |R|, hence 660 divides n. Audit carefully: scaling mod n can collapse the two elements, especially at small n. This is at most a partial obstruction; do not inflate it into noncompletion.

Further sources: De Felice arXiv:2202.09675, https://arxiv.org/html/2202.09675 (2022); Cordero arXiv:2301.13566, https://arxiv.org/html/2301.13566 (2023; later publication). Their special-order and cbc results do not establish the full all-n conclusion. Original Completing codes (1989): https://www.numdam.org/item/ITA_1989__23_2_135_0.pdf. Cordero's 2019 slides: http://www.normalesup.org/~cordero/Presentations/2019/GdR_IM.pdf.

## Work and scope

Read primary sources, attack the exact all-n problem, and write actual arguments with their precise gap in proof.md. Establish novelty status separately. You may use the workspace math/ corpus read-only; caller found no covering title in local CONTENTS.md, lean/docs or remote openai/math preprint tree. Do not infer novelty from a search miss. If no exact resolution is achieved, preserve useful failed attempts and return done:false with the exact all-n gap. Do not repeat a search for the already known n>=1320 obstruction.

Write only inside this scratch repo. Do not edit the permanent ai4s dossier, other workers' files, shared caches, math/, global configurations, existing journals or wrappers. No deletion, pushes, external contact, paid API opt-ins, new environment, or dependency downloads >200MB. At most 4 CPU threads and 12GB RAM. No further HMZ run or subagent process is authorized. Do not leave processes running.

## Verification

Freeze completed artifacts before one verification pass; do not run builds/lint/tests/formatters mid-edit. Mathematical research checks are allowed. The frozen verification command is `python3 -B verify.py`. For a positive solution put the actual finite code as a JSON list of binary strings (letters a,b) in witness.json: the verifier checks exact containment, unique decipherability, and exact dyadic Kraft equality, with false-proposition mutations. For a negative solution put proof.md and Solution.lean with theorem `ShorCompletion.noncompletion : ¬ ShorCompletion.HasFiniteCompletion` using the frozen Statement.lean definitions. Solution.lean is appended after Statement.lean for checking; do not import Statement.lean. No sorry/admit/new axiom/native_decide/ofReduceBool/unsafe/opaque or external execution. Include #print and #print axioms. No theorem whose hypothesis assumes the desired conclusion or equivalent substantive statement. The verifier checks this exact root via an additional check declaration. A mathematical reviewer must still audit the frozen statement's correspondence to the book and the whole proof.

Lean cwd is /Users/jinleic/jinleic-workspace/scratch/ai4s-math-hmz-20261014/verification/lean-verify, invoked as PATH=$HOME/.elan/bin:$PATH lake env lean ABSOLUTE_FILE. Write all generated files in THIS repo, never in that cache cwd. Partial Lean lemmas are allowed only if load-bearing and honestly scoped; they do not satisfy acceptance.

## Reviewer instruction

Return done:true only if exact Question 1 is answered, the full bridge from the proof/certificate to the book statement is established, the frozen verifier passes, all assumptions are discharged, and mutation controls reject false propositions. A timeout, report, verified bound, cyclic factorization, one-b-only completion, finite n UNSAT, or correct partial lemma is done:false. Existing published full answers must be identified as reproduction rather than discovery. Read ACCEPTANCE.md.
