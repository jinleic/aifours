# Olson's ordered EGZ conjecture: exact resolution attempt

Date: 2026-10-14 PT. This is one bounded research round, not an implementation scaffold.

## Exact goal

For every finite group G of order n, and every list (a_1,...,a_(2n-1)) in G, there exist 1 <= i_1 < ... < i_n <= 2n-1 with a_(i_1) ... a_(i_n) = 1 in THAT increasing-index order. Either prove this all-groups statement or give one explicit finite group and one list that refutes it. Do not replace it with unordered EGZ, a smaller length, a special class, a conditional theorem, or an equivalent unproved hypothesis.

The book is 10000 Selected Problems in Sciences, mathematics volume, printed p142 / PDF158, text /tmp/math10000_full.txt:5332-5334. Exact page image: /Users/jinleic/jinleic-workspace/scratch/ai4s-math-more-20261014/source-images/olson/page-158.png. It explicitly adds i_1<...<i_n to Olson's already-proved reorderable theorem.

## Baseline and prior work

- Original citation: John E. Olson, On a combinatorial problem of Erdos, Ginzburg, and Ziv, J. Number Theory 8(1) (1976),52–57, DOI 10.1016/0022-314X(76)90021-4. Publisher article and PDF returned 403; Elsevier text endpoint 400. Full original text not recovered. Crossref metadata and exact conjecture corroborated by https://www.sfu.ca/~mohar/Problems/P0604_OlsonConjecture.html (revised 2006-08-05), https://openproblemgarden.org/op/olsons_conjecture (2007-03-10).
- Important primary baseline recovered: Vesselin Dimitrov, On the Strong Davenport Constant of Nonabelian Finite p-Groups, Mathematica Balkanica 18 (2004),129–140. PDF at https://www.math.bas.bg/infres/MathBalk/MB-18/MB-18-129-140.pdf, local /Users/jinleic/jinleic-workspace/ai4s/olson-ordered-egz/sources/dimitrov-2004.pdf. First three pages OCR there as dimitrov-2004-ocr.txt. Theorem 2 proves ORDERED Olson for ALL finite p-groups; the subsequent solvable-group corollary is UNORDERED. No novelty for p-group cases.
- 2026 arXiv2603.21052 is explicitly product 'in some order', NOT this problem.
- Agarwal–Lou, IMSA 2016, https://digitalcommons.imsa.edu/sir_presentations/2016/oralsession1/55/, already reports sharp lower bound 4m-1 for odd dihedral groups of order 2m. The word r^(2m-1)s^(2m-1) avoids a 2m-term ordered identity product but is ONE TERM TOO SHORT, and therefore not a counterexample or new discovery. Adding one letter at a three-block boundary does not work.
- Parent exploratory BFS found no counterexample for C6,S3,D4,Q8, and is separately attempting D5. Do not duplicate those searches. Read-only model: ../feasibility/olson_probe.py. Search miss is not a proof of general truth.
- Local math/lean/docs and math/preprints keyword screen and remote openai/math main CONTENTS found no covering entry. This is not proof of no prior solution. Applicable methodological pattern: math/lean/docs/187.md and math/lean/ComparatorChallenges/SnakyCertificate.{lean,json}, finite certificate bound to exact quantifiers. No Snaky theorem solves this group problem.

## Research route

Prioritize a structurally motivated counterexample in a non-p-group not already covered, or an actual all-groups argument. Keep searches exact, memory bounded, and distinguish exhaustive coverage from heuristic failure. A multiplication-table certificate must include complete group axioms, cardinality, list length 2n-1, and absence of every increasing-index n-term product. Independently enumerate raw subsets for any claimed witness; dynamic programming alone is insufficient for final acceptance. If a theorem can be proved, preserve the order of interleaved subsequences: quotient-block induction generally loses it.

Do not fill time with tiny group theorems or padded Lean counts. A useful precise reduction or obstruction may be recorded but does not earn done:true. Do not spend this round re-proving the known p-group case.

## Output and verification

Write proof.md, claims.json, and (if present) Formal.lean and certificate.json. claims.json must contain full_goal_solved boolean and each claim's exact quantified statement, assumptions, full/partial scope, prior-art relation and theorem root if any. Never mark full_goal_solved true without a written complete proof or fully checked counterexample.

Frozen verifier: python3 verify.py. It independently validates a supplied certificate by raw increasing-index subset enumeration and cross-checks dynamic programming. It validates any Formal.lean against the exact universal ordered formula using the required theorem name Olson.ordered_egz for a proof, or Olson.ordered_egz_false for a refutation. A passing verifier supports, but does not replace, independent mathematical scope review.

Lean reference cwd is /Users/jinleic/jinleic-workspace/scratch/ai4s-math-hmz-20261014/verification/lean-verify. Use PATH=$HOME/.elan/bin:$PATH lake env lean /ABSOLUTE/PATH/TO/YOUR/FILE.lean from that cwd. Never write into that cwd. No sorry, admit, new axiom, native_decide, ofReduceBool, unsafe, opaque, custom executable elaborators, external execution or proof-bypass mechanisms. Include #print and #print axioms for theorem roots. Negative controls must fail because the proposition is false, not missing synthesis.

## Scope and safety

Your only writable repository is /Users/jinleic/jinleic-workspace/scratch/ai4s-math-more-20261014/olson. Other paths are read-only, including the dossier, math/, shared Lean caches, global configs, and other HMZ tasks. Do not change TASK.md, ACCEPTANCE.md, verify.py, existing journals or source snapshots. No delete/reset/push, runtime/model/credential edits, dependency installs, paid API opt-ins or extra HMZ runs. Preserve failed proofs and search logs. At most 4 CPU threads, 12GB RAM and 200MB added files. Avoid a single brute-force assay above 300 seconds without a new mathematical reason. The parent owns independent dossier work outside this repository.

One sanctioned HMZ run is bounded to 3600 seconds by the wrapper. The reviewer MUST return done:false unless the EXACT all-groups ordered conjecture is fully proved or refuted and mandatory evidence succeeds. Partial proof, finite verification, timeout, or an actor claim is not full resolution. Stop all search processes you launch before finishing.
